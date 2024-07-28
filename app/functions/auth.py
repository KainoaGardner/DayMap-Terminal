import json

import requests
from app.other import TerminalColor
from app import AUTH_CACHE, API_URL


def check_login():
    try:
        with open(AUTH_CACHE, "r") as file:
            json_object = json.load(file)
            token = json_object["access_token"]

    except:
        raise Exception("Cant access auth file")

    if not token:
        raise Exception("Not Logged in")


def get_auth():
    try:
        with open(AUTH_CACHE, "r") as file:
            json_object = json.load(file)
            headersAuth = {
                "Authorization": f"{json_object["token_type"]} "
                + json_object["access_token"]
            }
            return headersAuth
    except:
        raise Exception("Cant access auth file")


def update_auth(token):
    try:
        with open(AUTH_CACHE, "w") as file:
            file.write(token)
    except:
        raise Exception("Cant access auth file")


def remove_auth():
    token = json.dumps(
        {
            "access_token": "",
            "token_type": "bearer",
        }
    )
    try:
        with open(AUTH_CACHE, "r") as file:
            json_object = json.load(file)
            username = json_object["username"]

        with open(AUTH_CACHE, "w") as file:
            file.write(token)

        return username
    except:
        raise Exception("Cant access auth file")


def get_auth_token(data):
    response = requests.post(API_URL + "auth/token/", data)
    return check_response(response)


def check_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            TerminalColor.BOLD + response.json()["detail"]["msg"] + TerminalColor.END
        )
