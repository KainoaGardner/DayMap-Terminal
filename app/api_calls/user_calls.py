import requests

from app import API_URL
from app.functions import auth


# api users/
def get_users(headersAuth):
    response = requests.get(API_URL + "users/", headers=headersAuth)
    return auth.check_response(response)


# api users/create
def post_users_create(user):
    response = requests.post(API_URL + "users/create/", json=user)
    return auth.check_response(response)


# api users/remove
def delete_users_remove(headersAuth):
    response = requests.delete(API_URL + "users/remove/", headers=headersAuth)
    return auth.check_response(response)
