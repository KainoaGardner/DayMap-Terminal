import pandas as pd
from datetime import date

from app.other import bold_print, WEEKDAYS, MONTHS
from app.functions import auth
from app.api_calls import heatmap_calls, entries_calls


# search for users given heatmap and print date heatmap
def heatmaps_title(search, search_by_id):
    auth.check_login()
    headersAuth = auth.get_auth()
    response = heatmap_calls.get_heatmaps_single(search, search_by_id, headersAuth)
    show_heatmap_main(response["id"], headersAuth)


# get all finished dates print heatmap
def show_heatmap_main(heatmap_id, headersAuth):
    finished_dates = get_finished_dates(heatmap_id, headersAuth)
    all_days = get_all_days(finished_dates)
    print_heatmap(all_days)


# get all finished dates in heatmap


def get_finished_dates(heatmap_id, headersAuth):
    response = entries_calls.get_all_entries(heatmap_id, "true", headersAuth)
    finished_dates = {}
    for entry in response:
        finished_dates.update({entry["date"]: True})
    return finished_dates


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


# get all of users heatmaps and print them
def heatmaps_all():
    auth.check_login()
    headersAuth = auth.get_auth()
    response = heatmap_calls.get_heatmaps_all(headersAuth)
    bold_print("---Heatmaps---")
    for heatmap in response:
        bold_print(f"{heatmap["title"]}: {heatmap["description"]}")


# get seached heatmap finished days in a row streak
def heatmap_streak(search, search_by_id):
    auth.check_login()
    headersAuth = auth.get_auth()
    response = heatmap_calls.get_heatmaps_streak(search, search_by_id, headersAuth)

    streak = len(response)
    bold_print(f"{search}: Streak: {streak} days")


# create new heatmap with given title and description at authorized user
def create_heatmap(title, description):
    auth.check_login()
    headersAuth = auth.get_auth()
    data = {"title": title, "description": description}
    response = heatmap_calls.post_heatmaps_create(data, headersAuth)
    bold_print(f"Heatmap {response["title"]} created")


# remove searched heatamp at authorized user
def remove_heatmap(search, search_by_id):
    auth.check_login()
    headersAuth = auth.get_auth()
    response = heatmap_calls.delete_heatmaps_remove(search, search_by_id, headersAuth)
    bold_print(f"Heatmap {response["title"]} removed")


# change searched heatmap with new title and description
def change_heatmap(search, search_by_id, new_title, new_description):
    auth.check_login()
    headersAuth = auth.get_auth()
    data = {"title": new_title, "description": new_description}
    response = heatmap_calls.put_heatmaps_change(
        search, search_by_id, data, headersAuth
    )
    bold_print(f"Heatmap {response["title"]} updated")
