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
        """
        Get a list of rants
        Optional params:
            sort :  [algo, top, recent] sort rants by sort method
            limit:  [0 < x < 51] no. of rants to fetch, default = 10
            skip :  [x >= 0] no. of first N rants to skip, default = 0
        """
        url = self.url_builder.get_rants_url(sort, limit, skip)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response["rants"]
        return None

    def get_rant_by_id(self, rant_id: int):
        """Get rant by its rant id."""
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
        """Get complete profile of the User by their user id."""
        url = self.url_builder.get_user_profile_url(user_id)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response["profile"]
        return None

    # BREAKING DOWN USER PROFILE FUNCTION INTO 2 SECTIONS
    # ONE THAT GETS ONLY USER INFO AND THE SECOND ONE THAT GETS ONLY CONTENT

    def get_user_info(self, user_id: int):
        """Only get user info like bio, and counts [everytihing except rants]."""
        response = self.get_user_profile(user_id)
        info = {
            "username"    : response["username"],
            "score"       : response["score"],
            "about"       : response["about"],
            "location"    : response["location"],
            "created_time": response["created_time"],
            "skills"      : response["skills"],
            "github"      : response["github"],
            "website"     : response["website"],
            "counts"      : response["content"]["counts"],
            "dpp"         : response["dpp"],
        }
        return info

    def get_user_data(self, user_id: int):
        """Only get user content[] rants, upvoted, comments, favs, counts[]."""
        response = self.get_user_profile(user_id)
        return response["content"]

    def get_user_avatar(self, user_id: int, image_size: str = "small"):
        """Get user avatar image url, provided the imagesize."""
        response = self.get_user_profile(user_id)
        if image_size == "small":
            return self.url_builder.get_user_avatar_url(response["avatar_sm"]["i"])
        elif image_size == "large":
            return self.url_builder.get_user_avatar_url(response["avatar"]["i"])
        return None

    def get_weekly_rant(self, sort: str = "algo", skip: int = 0):
        """
        Get list of weekly rants.
        Optional params:
            sort: [algo, top, recent] sort rants by sort method
            skip: [x >= 0] no. of first N rants to skip, default = 0
        """
        url = self.url_builder.get_weekly_url(sort, skip)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response
        return None

    def get_collabs(self, skip: int = 0, limit: int = 10):
        """
        Get a list of available collabs.
        Optional params:
            limit: [0 < x < 51] no. of rants to fetch, default = 10
            skip : [x >= 0] no. of first N rants to skip, default = 0
        """
        url = self.url_builder.get_collabs_url(skip, limit)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response
        return None

    def get_collab_by_id(self, collab_id):
        """Get collab by its rant id."""
        self.get_rant_by_id(collab_id)

    def get_search_results(self, search_term: str):
        """Get list of rants matching the given search term."""
        url = self.url_builder.get_search_url(search_term)
        response = json.loads(requests.get(url).text)
        if response["success"]:
            return response
        return None


class DevAuth:
    """Everything that requires a uid, token and key."""

    def __init__(self):
        """Initializing class vars."""
        self.url_builder = URLs()
        self.uid         = None
        self.token       = None
        self.key         = None

    def login(self, username: str, password: str):
        """Login to devRant with username and password."""
        url, data = self.url_builder.get_login_url(username, password)
        response = json.loads(requests.post(url, data=data).text)
        if response["success"]:
            self.uid = response["auth_token"]["user_id"]
            self.token = response["auth_token"]["id"]
            self.key = response["auth_token"]["key"]
            return True
        return False

    def post_rant(self, body: str, tags: str = "", category: int = 1):
        """
        Post rant.
        Optional params:
            body    : text/rant to be posted
            tags    : tags related to the rant, category is automatically appended to tags
            category: type of rant [1-6]
                        1 = rant/story [default]
                        2 = joke/meme
                        3 = question
                        4 = collab
                        5 = devRant
                        6 = random
        """
        url, data = self.url_builder.get_post_rant_url(
            body, tags, category, self.uid, self.token, self.key
        )
        response = json.loads(requests.post(url, data=data).text)
        if response["success"]:
            return response["rant_id"]
        return None

    def post_comment(self, rant_id: int, body: str):
        """Post comment on a rant, provided the rant id."""
        url, data = self.url_builder.get_post_comment_url(
            rant_id, body, self.uid, self.token, self.key
        )
        response = json.loads(requests.post(url, data=data).text)
        if response["success"]:
            return True
        return response["error"]

    def vote(self, ele_id: int, mode: str = "rant", value: int = 1):
        """
        Vote on rant/comment using its id.
        params:
            ele_id: id of rant or comment
            mode  : whether its a rant or a comment
            value : 1  = Upvote [default]
                    0  = Cancel Upvote
                    -1 = Downvote
        """
        url, data = self.url_builder.get_vote_url(
            ele_id, mode, value, self.uid, self.token, self.key
        )
        response = json.loads(requests.post(url, data=data).text)
        if response["success"]:
            return True
        return False

    def delete_rant(self, rant_id: int, mode: str = "rant"):
        """Delete rant made by user, given the rant id."""
        url, params = self.url_builder.get_delete_rant_url(
            rant_id, mode, self.uid, self.token, self.key
        )
        response = json.loads(requests.delete(url, params=params).text)
        return response

    def delete_comment(self, comment_id: int, mode: str = "comment"):
        """Delete comment made by user, given the comment id."""
        self.delete_rant(comment_id, mode)

    def get_notifs(self):
        """Get notifications."""
        url = self.url_builder.get_notif_url(self.uid, self.token, self.key)
        response = json.loads(requests.get(url).text)
        return response

    def clear_notifs(self):
        """Clear notifications."""
        url = self.url_builder.get_notif_url(self.uid, self.token, self.key)
        response = json.loads(requests.delete(url).text)
        return response
