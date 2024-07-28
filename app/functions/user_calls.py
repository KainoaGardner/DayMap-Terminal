import requests

from app.other import TerminalColor
from app import API_URL
from .auth import check_response


def get_users(headersAuth):
    response = requests.get(API_URL + "users/", headers=headersAuth)
    return check_response(response)


def post_users_create():
    response = requests.post(API_URL + "users/create/", json=user)
    return check_response(response)
