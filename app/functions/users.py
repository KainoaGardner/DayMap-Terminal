import json

from app.other import bold_print, bold_input

from app.functions import auth
from app.api_calls import user_calls


# Takes username and password inputs calls to get access token saves to json cache for future requests
def login(username, password):
    data = {"grant_type": "password", "username": username, "password": password}
    response = auth.get_auth_token(data)
    response.update({"username": username})
    token = json.dumps(response)
    auth.update_auth(token)
    bold_print(f"{username} Logged In")


# Checks if logged in by checking json cache reset cache
def logout():
    auth.check_login()
    username = auth.remove_auth()
    bold_print(f"{username} Logged Out")


# call api to get user based on access token
def user():
    auth.check_login()
    headersAuth = auth.get_auth()
    response = user_calls.get_users(headersAuth)
    bold_print(f"User: {response["username"]}")


# call api to make new user with given username and password
def register(username, password):
    user = {"username": username, "password": password}
    response = user_calls.post_users_create(user)
    bold_print(f"User {username} Registered")


# call api to remove current logged in user
def remove_user():
    auth.check_login()
    answer = bold_input(f"Are you sure you want to remove your account? [y/n]: ")
    if answer.lower() == "y":
        headersAuth = auth.get_auth()
        response = user_calls.delete_users_remove(headersAuth)
        logout()
    else:
        bold_print("Not Removed")
