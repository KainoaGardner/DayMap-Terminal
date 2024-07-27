import requests
import os
import json
import pandas as pd
from datetime import date

from app.other import TerminalColor, WEEKDAYS, MONTHS
from app import API_URL, AUTH_CACHE
from .auth import check_login, get_auth


def heatmaps_title(title):
    if check_login():
        headersAuth = get_auth()

        response = requests.get(
            API_URL + f"heatmaps/title/{title}/", headers=headersAuth
        )
        if response.status_code == 200:
            heatmap = response.json()
            print(
                TerminalColor.BOLD
                + f"{heatmap["title"]}: "
                + TerminalColor.END
                + f"{heatmap["description"]}"
            )
            show_heatmap_main(heatmap["id"], headersAuth)
        else:
            print(TerminalColor.BOLD, end="")
            print(response.json(), end="")
            print(TerminalColor.END)


def show_heatmap_main(heatmap_id, headersAuth):
    finished_dates = get_finished_dates(heatmap_id, headersAuth)
    all_days = get_all_days(finished_dates)
    print_heatmap(all_days)


def get_finished_dates(heatmap_id, headersAuth):
    response = requests.get(
        API_URL + f"entry/all_entries/{heatmap_id}/", headers=headersAuth
    )
    finished_dates = {}
    if response.status_code == 200:
        entries = response.json()
        for entry in entries:
            finished_dates.update({entry["date"]: True})
        return finished_dates
    else:
        raise Exception(
            TerminalColor.BOLD + response.json()["detail"]["msg"] + TerminalColor.END
        )


def get_all_days(finished_dates):
    year = date.today().year
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    date_range = pd.date_range(start_date, end_date)
    all_days = [[], [], [], [], [], [], []]

    first_day = start_date.weekday()
    for d in range(first_day):
        all_days[d].append([None, True])

    for single_date in date_range:
        day = single_date.weekday()
        if single_date.strftime("%Y-%m-%d") in finished_dates:
            all_days[day].append([single_date.strftime("%Y-%m-%d"), True])
        else:
            all_days[day].append([single_date.strftime("%Y-%m-%d"), False])

    return all_days


def print_heatmap(all_days):
    print(end="     ")
    for month in MONTHS:
        print(f"{month}", end="      ")
    print()
    for i, week in enumerate(all_days):
        print(WEEKDAYS[i], end=" ")

        for day in week:
            if not day[0]:
                print("  ", end="")
            else:
                if day[1]:
                    print("⬛", end="")
                else:
                    print("⬜", end="")
        print("")


def heatmaps_all():
    if check_login():
        headersAuth = get_auth()

        response = requests.get(API_URL + "heatmaps/all/heatmaps/", headers=headersAuth)
        if response.status_code == 200:
            heatmaps = response.json()
            print(TerminalColor.BOLD + "---Heatmaps---" + TerminalColor.END)
            for heatmap in heatmaps:
                print(
                    TerminalColor.BOLD
                    + f"{heatmap["title"]}: "
                    + TerminalColor.END
                    + f"{heatmap["description"]}"
                )

        else:
            print(TerminalColor.BOLD, end="")
            print(response.json(), end="")
            print(TerminalColor.END)


def heatmap_streak(title):
    if check_login():
        headersAuth = get_auth()

        response = requests.get(
            API_URL + f"heatmaps/streak/{title}/", headers=headersAuth
        )
        if response.status_code == 200:
            entries = response.json()
            streak = len(entries)
            print(
                TerminalColor.BOLD
                + f"{title}: "
                + f"Streak: {streak} days"
                + TerminalColor.END
            )
        else:
            print(TerminalColor.BOLD, end="")
            print(response.json(), end="")
            print(TerminalColor.END)


def create_heatmap(title, description):
    if check_login():
        data = {"title": title, "description": description}
        headersAuth = get_auth()

        response = requests.post(
            API_URL + "heatmaps/create/", json=data, headers=headersAuth
        )
        if response.status_code == 200:
            heatmap = response.json()
            print(
                TerminalColor.BOLD
                + f"Heatmap {heatmap["title"]} created"
                + TerminalColor.END
            )
        else:
            print(TerminalColor.BOLD, end="")
            print(response.json(), end="")
            print(TerminalColor.END)


def remove_heatmap(title):
    if check_login():
        headersAuth = get_auth()

        response = requests.delete(
            API_URL + f"heatmaps/remove/title/{title}/", headers=headersAuth
        )
        if response.status_code == 200:
            heatmap = response.json()
            print(
                TerminalColor.BOLD
                + f"Heatmap {heatmap["title"]} removed"
                + TerminalColor.END
            )
        else:
            print(TerminalColor.BOLD, end="")
            print(response.json(), end="")
            print(TerminalColor.END)

    else:
        print(TerminalColor.BOLD + "Not Logged In" + TerminalColor.END)


def change_heatmap(id, title, description):
    if check_login():
        data = {"title": title, "description": description}
        headersAuth = get_auth()

        response = requests.put(
            API_URL + f"heatmaps/change/{id}/", json=data, headers=headersAuth
        )
        if response.status_code == 200:
            heatmap = response.json()
            print(
                TerminalColor.BOLD
                + f"Heatmap {heatmap["title"]} updated"
                + TerminalColor.END
            )
        else:
            print(TerminalColor.BOLD, end="")
            print(response.json(), end="")
            print(TerminalColor.END)
