import requests
import os
import json
import pandas as pd
from datetime import date

from app import API_URL, AUTH_CACHE
from app.functions import auth


def get_entry_check_today(search, search_by_id, today_date, headersAuth):
    response = requests.get(
        API_URL
        + f"entry/check_date/{search}/?search_by_id={search_by_id}&date={today_date}",
        headers=headersAuth,
    )
    return response


def post_entry_finish_today(search, search_by_id, today_date, headersAuth):
    response = requests.post(
        API_URL
        + f"entry/finish_today/{search}/?search_by_id={search_by_id}&date={today_date}",
        headers=headersAuth,
    )
    return response


def delete_entry_unfinish_today(search, search_by_id, today_date, headersAuth):
    response = requests.delete(
        API_URL
        + f"entry/unfinish_today/{search}/?search_by_id={search_by_id}&date={today_date}",
        headers=headersAuth,
    )
    return response


def get_all_entries(search, search_by_id, headersAuth):
    response = requests.get(
        API_URL + f"entry/all_entries/{search}/?search_by_id={search_by_id}",
        headers=headersAuth,
    )
    return auth.check_response(response)
