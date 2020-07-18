"""
Author: Deepak Talan
Github: @d02d33pak
devRant API
"""

import json
import requests
from devRantAPI.urls import URLs


class DevRant:
    """API Class providing Interface methods"""

    def __init__(self):
        """Initializing class vars"""
        self.url_builder = URLs()

    def get_rants(self, sort: str = "algo", limit: int = 10, skip: int = 0):
        """Get rants with limit, skip"""
        url = self.url_builder.get_rants_url(sort, limit, skip)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response["rants"]
        return None

    def get_rant_by_id(self, rant_id: int):
        """Get rant by rant_id"""
        url = self.url_builder.get_rant_by_id_url(rant_id)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response["rant"]
        return None

    def get_user_id(self, username: str):
        """Get user id from username"""
        url = self.url_builder.get_user_id_url(username)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response["user_id"]
        return None

    def get_user_profile(self, user_id: int):
        """Get complete profile of the User by their user-if"""
        url = self.url_builder.get_user_profile_url(user_id)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response["profile"]
        return None

    # BREAKING DOWN USER PROFILE FUNCTION INTO 2 SECTIONS
    # ONE THAT GETS ONLY USER INFO AND THE SECOND ONE THAT GETS ONLY CONTENT

    def get_user_info(self, user_id: int):
        """Only get user info like bio, and count [everytihing except rants]"""
        response = self.get_user_profile(user_id)
        info = {
            "username": response["username"],
            "score": response["score"],
            "about": response["about"],
            "location": response["location"],
            "created_time": response["created_time"],
            "skills": response["skills"],
            "github": response["github"],
            "website": response["website"],
            "counts": response["content"]["counts"],
            "dpp": response["dpp"],
        }
        return info

    def get_user_data(self, user_id: int):
        """Only get user content[] rants, upvoted, comments, favs, counts[]"""
        response = self.get_user_profile(user_id)
        return response["content"]

    def get_user_avatar(self, user_id: int, image_size: str = "small"):
        """Get user avatar image url, provided the imagesize"""
        response = self.get_user_profile(user_id)
        if image_size == "small":
            return self.url_builder.get_user_avatar_url(response["avatar_sm"]["i"])
        elif image_size == "large":
            return self.url_builder.get_user_avatar_url(response["avatar"]["i"])
        else:
            return "size = small/large"

    def get_weekly_rant(self, sort: str = "algo", skip: int = 0):
        """get weekly rants based on algo"""
        url = self.url_builder.get_weekly_url(sort, skip)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response
        return None

    def get_collabs(self, skip: int = 0, limit: int = 10):
        """get collabs"""
        url = self.url_builder.get_collabs_url(skip, limit)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response
        return None

    def get_search_results(self, search_term: str):
        """get rants based on search term"""
        url = self.url_builder.get_search_url(search_term)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response
        return None
