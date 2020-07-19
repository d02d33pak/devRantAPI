"""
Author: Deepak Talan
Github: @d02d33pak
all URLs
"""

import time


class URLs:
    """url class"""

    def __init__(self):
        """initializing all urls"""
        self.base_url = "https://devrant.com/api/"
        self.app_id = "?app=3"
        self.rants_url = "devrant/rants"
        self.comment_url = "/comments"
        self.vote_url = "/vote"
        self.user_id = "get-user-id"
        self.user_profile = "users/"
        self.user_avatar = "https://avatars.devrant.com/"
        self.weekly_rants = "devrant/weekly-rant"
        self.collabs = "devrant/collabs"
        self.search = "devrant/search"
        ###AUTH URLs###
        self.login = "users/auth-token"

    def get_rants_url(self, sort, limit, skip):
        """multi rants"""
        sort = self.validate_sort(sort)
        limit = self.validate_int(limit)
        skip = self.validate_int(skip)
        return f"{self.base_url}{self.rants_url}{self.app_id}&sort={sort}&limit={limit}&skip={skip}"

    def get_rant_by_id_url(self, rant_id):
        """single rant"""
        return f"{self.base_url}{self.rants_url}/{rant_id}{self.app_id}"

    def get_user_id_url(self, username):
        """return user_id url"""
        return f"{self.base_url}{self.user_id}{self.app_id}&username={username}"

    def get_user_profile_url(self, user_id):
        """return user_id url"""
        return f"{self.base_url}{self.user_profile}{user_id}{self.app_id}"

    def get_user_avatar_url(self, avatar_link):
        """return png url"""
        return f"{self.user_avatar}{avatar_link}"

    def get_weekly_url(self, sort, skip):
        """return weekly url"""
        sort = self.validate_sort(sort)
        limit = self.validate_int(skip)
        return (
            f"{self.base_url}{self.weekly_rants}{self.app_id}&sort={sort}&limit={limit}"
        )

    def get_collabs_url(self, skip, limit):
        """return collabs url"""
        return f"{self.base_url}{self.collabs}{self.app_id}&skip={skip}&limit={limit}"

    def get_search_url(self, search_term):
        """return search url"""
        return f"{self.base_url}{self.app_id}&term={search_term}"

    def validate_sort(self, sort):
        """validate sort method"""
        if sort in ["algo", "recent", "top"]:
            return sort
        raise ValueError("Invalid Sort Type")

    @staticmethod
    def validate_int(num):
        """validate any int input"""
        if num >= 0:
            return num
        raise ValueError("Limit/Skip should be positive Integers")

    def get_login_url(self, username, password):
        """return login url"""
        url = f"{self.base_url}{self.login}"
        params = {
            "app": 3,
            "username": username,
            "password": password,
            "plat": 3,
            "sid": time.time(),
        }
        return url, params

    def get_post_rant_url(self, body, tags, category, uid, token_id, token_key):
        """reuturn post rant url"""
        url = f"{self.base_url}{self.rants_url}"
        params = {
            "app": 3,
            "rant": body,
            "tags": tags,
            "type": category,
            "user_id": uid,
            "token_id": token_id,
            "token_key": token_key,
        }
        return url, params

    def get_post_comment_url(self, rant_id, body, uid, token_id, token_key):
        """reuturn post comment url"""
        url = f"{self.base_url}{self.rants_url}/{rant_id}{self.comment_url}"
        params = {
            "app": 3,
            "comment": body,
            "user_id": uid,
            "token_id": token_id,
            "token_key": token_key,
            "plat": 3,
        }
        return url, params

    def get_vote_url(self, ele_id, mode, value, uid, token_id, token_key):
        """return vote url"""

        if mode == "rant":
            url = f"{self.base_url}{self.rants_url}/{ele_id}{self.vote_url}"
        elif mode == "comment":
            url = f"{self.base_url}{self.comment_url}/{ele_id}{self.vote_url}"
        params = {
            "app": 3,
            "vote": value,
            "user_id": uid,
            "token_id": token_id,
            "token_key": token_key,
            "plat": 3,
            "sid": time.time(),
        }

        if value == -1:
            params["reason"] = 0 # if user is downvoting, reason needs to be provided

        return url, params
