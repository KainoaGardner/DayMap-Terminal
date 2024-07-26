import requests
import json

from app.other import TerminalColor
from app import API_URL, AUTH_CACHE
from .auth import check_login, get_auth


def login(username, password):
    data = {"grant_type": "password", "username": username, "password": password}
    response = requests.post(API_URL + "auth/token/", data)
    if response.status_code == 200:
        response = response.json()
        response.update({"username": username})

        token = json.dumps(response)

        try:
            with open(AUTH_CACHE, "w") as file:
                file.write(token)
        except:
            print(TerminalColor.BOLD + "Cache Error" + TerminalColor.END)

        print(TerminalColor.BOLD + f"{username} Logged In" + TerminalColor.END)
    else:
        print(TerminalColor.BOLD, end="")
        print(response.json(), end="")
        print(TerminalColor.END)


def logout():
    if check_login():
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

        except:
            print(TerminalColor.BOLD + "Cache Error" + TerminalColor.END)
        print(TerminalColor.BOLD + f"{username} Logged Out" + TerminalColor.END)


def user():
    if check_login():
        headersAuth = get_auth()

        response = requests.get(API_URL + "users/", headers=headersAuth)
        if response.status_code == 200:
            user = response.json()
            print(TerminalColor.BOLD + f"User: {user["username"]}" + TerminalColor.END)


def register(username, password):
    user = {"username": username, "password": password}
    response = requests.post(API_URL + "users/create/", json=user)
    if response.status_code == 200:
        print(TerminalColor.BOLD + f"User {username} Registered" + TerminalColor.END)
    else:
        print(TerminalColor.BOLD, end="")
        print(response.json(), end="")
        print(TerminalColor.END)


def remove_user():
    if check_login():
        answer = input(
            TerminalColor.BOLD
            + f"Are you sure you want to remove your account? [y/n]: "
            + TerminalColor.END
        )
        if answer.lower() == "y":
            headersAuth = get_auth()
            response = requests.delete(API_URL + "users/remove/", headers=headersAuth)
            if response.status_code == 200:
                user = response.json()
                print(
                    TerminalColor.BOLD
                    + f"Deleted User: {user["username"]}"
                    + TerminalColor.END
                )
                logout()
            else:
                print(response.json())

        else:
            print(TerminalColor.BOLD + "Not Removed" + TerminalColor.END)
