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
        print("invalid")


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
                    + f"ID:{heatmap["id"]} {heatmap["title"]}: "
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
