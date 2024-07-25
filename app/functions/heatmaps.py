import requests
import os
import json

from app.other import TerminalColor
from app import API_URL, AUTH_CACHE
from .auth import check_login, get_auth


def heatmaps(args):
    if "a" in args or "all" in args:
        heatmaps_all()
    elif args.isnumeric():
        heatmaps_id(int(args))
    else:
        print(TerminalColor.BOLD + "Invalid Id" + TerminalColor.END)


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
        print(TerminalColor.BOLD + "Not Logged In" + TerminalColor.END)


def heatmaps_id(id):
    if check_login():
        headersAuth = get_auth()

        response = requests.get(API_URL + f"heatmaps/{id}", headers=headersAuth)
        if response.status_code == 200:
            heatmap = response.json()
            print(TerminalColor.BOLD + "---Heatmaps---" + TerminalColor.END)
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

    else:
        print(TerminalColor.BOLD + "Not Logged In" + TerminalColor.END)


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
                + f"Heatmap {heatmap["title"]} Id:{heatmap["id"]} created"
                + TerminalColor.END
            )
        else:
            print(TerminalColor.BOLD, end="")
            print(response.json(), end="")
            print(TerminalColor.END)

    else:
        print(TerminalColor.BOLD + "Not Logged In" + TerminalColor.END)


def remove_heatmap(id):
    if check_login():
        headersAuth = get_auth()

        response = requests.delete(
            API_URL + f"heatmaps/remove/{id}/", headers=headersAuth
        )
        if response.status_code == 200:
            heatmap = response.json()
            print(
                TerminalColor.BOLD
                + f"Heatmap {heatmap["title"]} Id: {heatmap["id"]} removed"
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
                + f"Heatmap {heatmap["title"]} Id: {heatmap["id"]} updated"
                + TerminalColor.END
            )
        else:
            print(TerminalColor.BOLD, end="")
            print(response.json(), end="")
            print(TerminalColor.END)

    else:
        print(TerminalColor.BOLD + "Not Logged In" + TerminalColor.END)
