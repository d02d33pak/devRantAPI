"""
Author: Deepak Talan
Github: @d02d33pak
all URLs
"""

import time


class URLs:
    """url class"""

    def __init__(self):
        """Initialize all class variables."""
        # BASE
        self.base_url = "https://devrant.com/api/"
        # RANT RELATED
        self.app_id = "?app=3"
        self.rants_url = "devrant/rants"
        self.comment_url = "/comments"
        self.vote_url = "/vote"
        # USER RELATED
        self.user_id = "get-user-id"
        self.user_profile = "users/"
        self.user_avatar = "https://avatars.devrant.com/"
        # MISC
        self.weekly_rants = "devrant/weekly-rant"
        self.collabs = "devrant/collabs"
        self.search = "devrant/search"
        # LOGIN RELATED
        self.login = "users/auth-token"
        self.notif = "users/me/notif-feed"

    def get_rants_url(self, sort, limit, skip):
        """Generate a request URL to get rants."""
        sort = self.validate_sort(sort)
        limit = self.validate_int(limit)
        skip = self.validate_int(skip)
        return f"{self.base_url}{self.rants_url}{self.app_id}&sort={sort}&limit={limit}&skip={skip}"

    def get_rant_by_id_url(self, rant_id):
        """Generate a request URL to get a rant by its id."""
        return f"{self.base_url}{self.rants_url}/{rant_id}{self.app_id}"

    def get_user_id_url(self, username):
        """Generate a request URL to get user's id from username."""
        return f"{self.base_url}{self.user_id}{self.app_id}&username={username}"

    def get_user_profile_url(self, user_id):
        """Generate a request URL to get complete user profile."""
        return f"{self.base_url}{self.user_profile}{user_id}{self.app_id}"

    def get_user_avatar_url(self, avatar_link):
        """Generate a request URL to get user's avatar png."""
        return f"{self.user_avatar}{avatar_link}"

    def get_weekly_url(self, sort, skip):
        """Generate a request URL to get the weekly rants."""
        sort = self.validate_sort(sort)
        limit = self.validate_int(skip)
        return (
            f"{self.base_url}{self.weekly_rants}{self.app_id}&sort={sort}&limit={limit}"
        )

    def get_collabs_url(self, skip, limit):
        """Generate a request URL to get collabs."""
        return f"{self.base_url}{self.collabs}{self.app_id}&skip={skip}&limit={limit}"

    def get_search_url(self, search_term):
        """Generate a request URL to search rants by keywords."""
        return f"{self.base_url}{self.app_id}&term={search_term}"

    def validate_sort(self, sort):
        """Validate the provided sort method."""
        if sort in ["algo", "recent", "top"]:
            return sort
        raise ValueError("Invalid Sort Type")

    @staticmethod
    def validate_int(num):
        """Validate that the given input is non negative."""
        if num >= 0:
            return num
        raise ValueError("Limit/Skip should be positive Integers")

    def get_login_url(self, username, password):
        """Generate a request URL to login to devRant."""
        url = f"{self.base_url}{self.login}"
        params = {
            "app": 3,
            "username": username,
            "password": password,
            "plat": 3,
            "sid": time.time(),
        }
        return url, params

    def get_post_rant_url(self, body, tags, category, uid, token, key):
        """Generate a request URL to post a rant."""
        url = f"{self.base_url}{self.rants_url}"
        params = {
            "app": 3,
            "type": category,
            "rant": body,
            "tags": tags,
            "user_id": uid,
            "token_id": token,
            "token_key": key,
        }
        return url, params

    def get_post_comment_url(self, rant_id, body, uid, token, key):
        """Generate a request URL to post comment on a rant."""
        url = f"{self.base_url}{self.rants_url}/{rant_id}{self.comment_url}"
        params = {
            "app": 3,
            "comment": body,
            "user_id": uid,
            "token_id": token,
            "token_key": key,
            "plat": 3,
        }
        return url, params

    def get_vote_url(self, ele_id, mode, value, uid, token, key):
        """Generate a request URL to vote on a rant/comment."""
        if mode == "rant":
            url = f"{self.base_url}{self.rants_url}/{ele_id}{self.vote_url}"
        elif mode == "comment":
            url = f"{self.base_url}{self.comment_url}/{ele_id}{self.vote_url}"
        params = {
            "app": 3,
            "vote": value,
            "user_id": uid,
            "token_id": token,
            "token_key": key,
            "plat": 3,
            "sid": time.time(),
        }
        if value == -1:
            params["reason"] = 0  # if user is downvoting, reason needs to be provided

        return url, params

    def get_delete_rant_url(self, rant_id, mode, uid, token, key):
        """Generate a request URL to delete a rant/comment."""
        if mode == "rant":
            url = f"{self.base_url}{self.rants_url}/{rant_id}"
        elif mode == "comment":
            url = f"{self.base_url}{self.comment_url}/{rant_id}"
        params = {
            "app": 3,
            "user_id": uid,
            "token_id": token,
            "token_key": key,
            "plat": 3,
            "sid": time.time(),
        }
        return url, params

    def get_notif_url(self, uid, token, key):
        """Generate a request URL to get notification feed."""
        url = f"{self.base_url}{self.notif}"
        params = {
            "app": 3,
            "user_id": uid,
            "token_id": token,
            "token_key": key,
        }
        return url, params
