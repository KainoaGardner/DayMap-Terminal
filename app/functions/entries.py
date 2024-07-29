import requests
from datetime import date

from app.other import bold_print
from app import API_URL
from app.functions import auth
from app.api_calls import entries_calls, heatmap_calls


def today(search, search_by_id):
    auth.check_login()
    today_date = date.today()
    headersAuth = auth.get_auth()
    heatmap = heatmap_calls.get_heatmaps_single(search, search_by_id, headersAuth)
    response = entries_calls.get_entry_check_today(
        search, search_by_id, today_date, headersAuth
    )
    bold_print(str(today_date))
    if response.status_code == 200:
        bold_print(f"{heatmap["title"]} DONE")
    else:
        bold_print(f"{heatmap["title"]} NOT DONE")


def today_status():
    auth.check_login()
    today_date = date.today()
    result = get_status_result(today_date)
    bold_print(f"{str(today_date)}\n")

    for heatmap in result:
        finished = "----"
        if heatmap["date"]:
            finished = "DONE"
        bold_print(f"{heatmap["title"]} {finished} {heatmap["streak"]}")


def get_status_result(today_date):
    headersAuth = auth.get_auth()
    result = heatmap_calls.get_heatmaps_all(headersAuth)
    get_streak_status(result, headersAuth)
    get_date_status(result, today_date, headersAuth)
    return result


def get_streak_status(result, headersAuth):
    for heatmap in result:
        response = heatmap_calls.get_heatmaps_streak(heatmap["id"], "true", headersAuth)
        streak = len(response)
        heatmap.update({"streak": streak})


def get_date_status(result, today_date, headersAuth):
    for heatmap in result:
        response = entries_calls.get_entry_check_today(
            heatmap["id"], "true", today_date, headersAuth
        )
        if response.status_code == 200:
            heatmap.update({"date": response.json()["date"]})
        else:

            heatmap.update({"date": None})


def finish(searches, search_by_id):
    auth.check_login()
    headersAuth = auth.get_auth()
    today_date = date.today()
    for search in searches:
        heatmap = heatmap_calls.get_heatmaps_single(search, search_by_id, headersAuth)
        response = entries_calls.post_entry_finish_today(
            search, search_by_id, today_date, headersAuth
        )
        if response.status_code == 200:
            bold_print(f"{heatmap["title"]} DONE")
        else:
            bold_print(f"{heatmap["title"]} {response.json()["detail"]}")


def unfinish(searches, search_by_id):
    auth.check_login()
    headersAuth = auth.get_auth()
    today_date = date.today()

    for search in searches:
        heatmap = heatmap_calls.get_heatmaps_single(search, search_by_id, headersAuth)
        response = entries_calls.delete_entry_unfinish_today(
            search, search_by_id, today_date, headersAuth
        )
        if response.status_code == 200:
            bold_print(f"{heatmap["title"]} Unfinished")
        else:
            bold_print(f"{heatmap["title"]} {response.json()["detail"]}")
