#!usr/bin/env Python4
"""Login and Get Rants"""
import requests


def get_rants():
    """ Get Rants Function"""
    base_url = "https://devrant.com/api/devrant/rants"
    app = 3
    sort = "algo"
    limit = 3
    token_id = "2384447"
    token_key = "8wYpFFxWDuEWiTKd54Wve1CqyrmSvE4BsmHHum_L"
    user_id = "115067"

    params = {
        "app": app,
        "sort": sort,
        "limit": limit,
        "token_id": token_id,
        "token_key": token_key,
        "user_id": user_id,
    }

    res = requests.get(base_url, params)
    res_j = res.json()
    for rant in res_j["rants"]:
        print(rant["text"])
        print(20 * "*")


def login():
    """Login to devRant"""
    request_url = "https://devrant.com/api/users/auth-token"
    username = str(input("enter username : "))
    username = "d02d33pak"
    password = str(input("enter password  : "))
    password = "qwerty529"
    header = {"content-type": "application/json"}
    payload = {"app": 3, "username": username, "password": password}

    response = requests.post(request_url, payload, header)
    res_json = response.json()

    if res_json["success"]:
        feed_url = "https://devrant.com/api/devrant/rants"
        sort = "algo"
        limit = 10
        token_id = res_json["auth_token"]["id"]
        token_key = res_json["auth_token"]["key"]
        user_id = res_json["auth_token"]["user_id"]
        print(token_id, token_key, user_id)

        payload = {
            "app": 3,
            "sort": sort,
            "limit": limit,
            "token_id": token_id,
            "token_key": token_key,
            "user_id": user_id,
        }

        rants = requests.get(feed_url, payload)
        rants_json = rants.json()
        for rant in rants_json["rants"]:
            if rant["attached_image"] == "":
                print(rant["text"])
                print(20 * "-")

    else:
        print("FAILED")


if __name__ == "__main__":
    login()
    get_rants()
