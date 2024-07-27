import requests
import os
import json
from datetime import date

from app.other import TerminalColor
from app import API_URL, AUTH_CACHE
from .auth import check_login, get_auth


def get_heatmap(title, headersAuth):
    response = requests.get(
        API_URL + f"heatmaps/title/{title}",
        headers=headersAuth,
    )

    if response.status_code == 200:
        heatmap = response.json()
        return heatmap

    else:
        raise Exception(TerminalColor.BOLD + "Heatmap not found" + TerminalColor.END)


def today(title):
    if check_login():
        today_date = date.today()
        headersAuth = get_auth()

        heatmap = get_heatmap(title, headersAuth)

        response = requests.get(
            API_URL + f"entry/check_today/{title}/{today_date}",
            headers=headersAuth,
        )
        print(
            TerminalColor.BOLD
            + TerminalColor.UNDERLINE
            + str(today_date)
            + TerminalColor.END
        )

        if response.status_code == 200:
            print(TerminalColor.BOLD + f"{heatmap["title"]} DONE" + TerminalColor.END)

        else:
            print(TerminalColor.BOLD + f"{heatmap["title"]} ----" + TerminalColor.END)


def today_status():
    if check_login():
        today_date = date.today()
        result = get_status_result(today_date)

        print(
            TerminalColor.BOLD
            + TerminalColor.UNDERLINE
            + "Finished "
            + str(today_date)
            + TerminalColor.END
        )
        for heatmap in result:
            finished = "----"
            if heatmap["date"]:
                finished = "DONE"

            print(
                TerminalColor.BOLD
                + f"{heatmap["title"]} {finished} {heatmap["streak"]} Days"
                + TerminalColor.END
            )


def get_status_result(today_date):
    headersAuth = get_auth()
    result = []

    get_heatmap_status(result, headersAuth)
    get_streak_status(result, headersAuth)
    get_date_status(result, today_date, headersAuth)
    return result


def get_heatmap_status(result, headersAuth):
    response = requests.get(API_URL + f"heatmaps/all/heatmaps/", headers=headersAuth)
    if response.status_code == 200:
        heatmaps = response.json()
        for heatmap in heatmaps:

            result.append(
                {
                    "title": heatmap["title"],
                    "id": heatmap["id"],
                }
            )
    else:
        raise (
            TerminalColor.BOLD + response.json()["detail"]["msg"] + TerminalColor.END
        )


def get_streak_status(result, headersAuth):
    for heatmap in result:
        response = requests.get(
            API_URL + f"heatmaps/streak/{heatmap["title"]}/", headers=headersAuth
        )
        if response.status_code == 200:
            streak = len(response.json())
            heatmap.update({"streak": streak})

        else:
            raise (
                TerminalColor.BOLD
                + response.json()["detail"]["msg"]
                + TerminalColor.END
            )


def get_date_status(result, today_date, headersAuth):
    for heatmap in result:
        response = requests.get(
            API_URL + f"entry/check_today/{heatmap["id"]}/{today_date}",
            headers=headersAuth,
        )
        if response.status_code == 200:
            entry = response.json()
            heatmap.update({"date": entry["date"]})

        else:

            heatmap.update({"date": None})


def finish(titles):
    if check_login():
        headersAuth = get_auth()
        today_date = {"date": str(date.today())}
        for title in titles:
            response = requests.post(
                API_URL + f"entry/finish_today/title/{title}/",
                headers=headersAuth,
                json=today_date,
            )
            if response.status_code == 200:
                print(TerminalColor.BOLD + f"{title} DONE" + TerminalColor.END)

            else:
                response = response.json()
                print(
                    TerminalColor.BOLD
                    + f"{title} {response["detail"]}"
                    + TerminalColor.END
                )


def unfinish(titles):
    if check_login():
        headersAuth = get_auth()
        today_date = {"date": str(date.today())}
        for title in titles:
            response = requests.delete(
                API_URL + f"entry/unfinish_today/title/{title}/",
                headers=headersAuth,
                json=today_date,
            )
            if response.status_code == 200:
                print(TerminalColor.BOLD + f"{title} ----" + TerminalColor.END)

            else:
                response = response.json()
                print(
                    TerminalColor.BOLD
                    + f"{title} {response["detail"]}"
                    + TerminalColor.END
                )
