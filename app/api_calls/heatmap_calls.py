import requests

from app import API_URL
from app.functions import auth


# api heatmaps/single/{search}
def get_heatmaps_single(search, search_by_id, headersAuth):
    response = requests.get(
        API_URL + f"heatmaps/single/{search}/?search_by_id={search_by_id}",
        headers=headersAuth,
    )
    return auth.check_response(response)


# api get/heatmaps/all
def get_heatmaps_all(headersAuth):
    response = requests.get(API_URL + "heatmaps/all/", headers=headersAuth)
    return auth.check_response(response)


# api get/heatmaps/streak
def get_heatmaps_streak(search, search_by_id, headersAuth):
    response = requests.get(
        API_URL + f"heatmaps/streak/{search}/?search_by_id={search_by_id}",
        headers=headersAuth,
    )
    return auth.check_response(response)


# api post/heatmaps/create
def post_heatmaps_create(data, headersAuth):
    response = requests.post(
        API_URL + "heatmaps/create/", json=data, headers=headersAuth
    )
    return auth.check_response(response)


def delete_heatmaps_remove(search, search_by_id, headersAuth):
    response = requests.delete(
        API_URL + f"heatmaps/remove/{search}/?search_by_id={search_by_id}",
        headers=headersAuth,
    )
    return auth.check_response(response)


def put_heatmaps_change(search, search_by_id, data, headersAuth):
    response = requests.put(
        API_URL + f"heatmaps/change/{search}/?search_by_id={search_by_id}",
        json=data,
        headers=headersAuth,
    )
    return auth.check_response(response)
