"""
Author: Deepak Talan
Github: @d02d33pak
Helper module to generate request urls
"""

import time


class URLs:
    """URL class providing url generation methods."""

    def __init__(self):
        """Initialize all class variables."""
        # UNIVERSAL
        self.base_url = "https://devrant.com/api/"
        self.app_id = 3
        self.plat = 3
        # RANT RELATED
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

    def create_params(self, **kwargs):
        """Generate parameters to be passed alongside urls."""
        params = {"app": self.app_id, "plat": self.plat, "sid": time.time()}
        for key, value in kwargs.items():
            params[str(key)] = value
        return params

    def get_rants_url(self, sort, limit, skip):
        """Generate a request URL to get rants."""
        sort = self.validate_sort(sort)
        limit = self.validate_int(limit)
        skip = self.validate_int(skip)
        params = self.create_params(sort=sort, limit=limit, skip=skip)
        url = f"{self.base_url}{self.rants_url}"
        return url, params

    def get_rant_by_id_url(self, rant_id):
        """Generate a request URL to get a rant by its id."""
        params = self.create_params()
        url = f"{self.base_url}{self.rants_url}/{rant_id}"
        return url, params

    def get_user_id_url(self, username):
        """Generate a request URL to get user's id from username."""
        params = self.create_params(username=username)
        url = f"{self.base_url}{self.user_id}"
        return url, params

    def get_user_profile_url(self, user_id):
        """Generate a request URL to get complete user profile."""
        params = self.create_params()
        url = f"{self.base_url}{self.user_profile}{user_id}"
        return url, params

    def get_user_avatar_url(self, avatar_link):
        """Generate a request URL to get user's avatar png."""
        return f"{self.user_avatar}{avatar_link}"

    def get_weekly_url(self, sort, skip):
        """Generate a request URL to get the weekly rants."""
        sort = self.validate_sort(sort)
        skip = self.validate_int(skip)
        params = self.create_params(sort=sort, skip=skip)
        url = f"{self.base_url}{self.weekly_rants}"
        return url, params

    def get_collabs_url(self, skip, limit):
        """Generate a request URL to get collabs."""
        skip = self.validate_int(skip)
        limit = self.validate_int(limit)
        params = self.create_params(skip=skip, limit=limit)
        url = f"{self.base_url}{self.collabs}"
        return url, params

    def get_search_url(self, search_term):
        """Generate a request URL to search rants by keywords."""
        params = self.create_params(term=search_term)
        url = f"{self.base_url}"
        return url, params

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
        params = self.create_params(username=username, password=password)
        url = f"{self.base_url}{self.login}"
        return url, params

    def get_post_rant_url(self, body, category, tags, uid, token, key):
        """Generate a request URL to post a rant."""
        params = self.create_params(
            rant=body,
            type=category,
            tags=tags,
            user_id=uid,
            token_id=token,
            token_key=key,
        )
        url = f"{self.base_url}{self.rants_url}"
        return url, params

    def get_post_comment_url(self, rant_id, body, uid, token, key):
        """Generate a request URL to post comment on a rant."""
        params = self.create_params(
            comment=body, user_id=uid, token_id=token, token_key=key
        )
        url = f"{self.base_url}{self.rants_url}/{rant_id}{self.comment_url}"
        return url, params

    def get_vote_url(self, ele_id, mode, value, reason, uid, token, key):
        """Generate a request URL to vote on a rant/comment."""
        params = self.create_params(
            vote=value, user_id=uid, token_id=token, token_key=key
        )
        if value == -1: # Provide reason for down voting
            params["reason"] = reason
        if mode == "rant":
            url = f"{self.base_url}{self.rants_url}/{ele_id}{self.vote_url}"
        elif mode == "comment":
            url = f"{self.base_url}{self.comment_url}/{ele_id}{self.vote_url}"

        return url, params

    def get_delete_rant_url(self, rant_id, mode, uid, token, key):
        """Generate a request URL to delete a rant/comment."""
        if mode == "rant":
            url = f"{self.base_url}{self.rants_url}/{rant_id}"
        elif mode == "comment":
            url = f"{self.base_url}{self.comment_url}/{rant_id}"
        params = self.create_params(user_id=uid, token_id=token, token_key=key)
        return url, params

    def get_notif_url(self, uid, token, key):
        """Generate a request URL to get notification feed."""
        url = f"{self.base_url}{self.notif}"
        params = self.create_params(user_id=uid, token_id=token, token_key=key)
        return url, params
