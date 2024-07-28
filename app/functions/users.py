import requests
import json

from app.other import TerminalColor
from app import API_URL
from .auth import check_login, remove_auth, update_auth, get_auth, get_auth_token
from .user_calls import get_users


def login(username, password):
    data = {"grant_type": "password", "username": username, "password": password}
    response = get_auth_token(data)
    response.update({"username": username})
    token = json.dumps(response)
    update_auth(token)
    print(TerminalColor.BOLD + f"{username} Logged In" + TerminalColor.END)


def logout():
    check_login()
    username = remove_auth()
    print(TerminalColor.BOLD + f"{username} Logged Out" + TerminalColor.END)


def user():
    check_login()
    headersAuth = get_auth()
    response = get_users(headersAuth)
    print(TerminalColor.BOLD + f"User: {response["username"]}" + TerminalColor.END)


def register(username, password):
    user = {"username": username, "password": password}
    response = requests.post(API_URL + "users/create/", json=user)

    print(TerminalColor.BOLD + f"User {username} Registered" + TerminalColor.END)


def remove_user():
    check_login()
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
