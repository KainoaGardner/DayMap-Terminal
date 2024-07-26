import json

from app.other import TerminalColor
from app import AUTH_CACHE


def check_login():
    try:
        with open(AUTH_CACHE, "r") as file:
            json_object = json.load(file)
            token = json_object["access_token"]

            if token:
                return True
            else:
                print(TerminalColor.BOLD + "Not Logged In" + TerminalColor.END)
                return False
    except:
        print(TerminalColor.BOLD + "Cache Error" + TerminalColor.END)
        return False


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
        print(TerminalColor.BOLD + "Cache Error" + TerminalColor.END)
        return False
