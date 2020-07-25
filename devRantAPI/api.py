"""
Author: Deepak Talan
Github: @d02d33pak
devRant API
"""

import json

import requests

from devRantAPI.urls import URLs


class DevRant:
    """API Class providing Interface methods."""

    def __init__(self):
        """Initializing class vars."""
        self.url_builder = URLs()

    def get_rants(self, sort: str = "algo", limit: int = 10, skip: int = 0):
        """
        Returns a list of rants.

        Optional parameters:
            sort (str) : Sort rants by [algo, top, recent], default = algo
            limit (int) : No. of rants to fetch, max = 50, default = 10
            skip (int) : No. of first N rants to skip, default = 0
        """
        url, params = self.url_builder.get_rants_url(sort, limit, skip)
        response = json.loads(requests.get(url, params=params).text)
        if response["success"]:
            return response["rants"]
        return None

    def get_rant_by_id(self, rant_id: int):
        """
        Returns a single rant by its rant id.

        Parameters:
            rant_id (int) : ID of the rant to be fetched
        """
        url, params = self.url_builder.get_rant_by_id_url(rant_id)
        response = json.loads(requests.get(url, params=params).text)
        if response["success"]:
            return response
        return None

    def get_user_id(self, username: str):
        """
        Returns user id from username.

        Parameters:
            username (str) : Username
        """
        url, params = self.url_builder.get_user_id_url(username)
        response = json.loads(requests.get(url, params=params).text)
        if response["success"]:
            return response["user_id"]
        return None

    def get_user_profile(self, user_id: int):
        """
        Returns complete Profile of the User by their user id.

        Parameters:
            user_id (int) : User ID
        """
        url, params = self.url_builder.get_user_profile_url(user_id)
        response = json.loads(requests.get(url, params=params).text)
        if response["success"]:
            return response["profile"]
        return None

    # BREAKING DOWN USER PROFILE FUNCTION INTO 2 SECTIONS
    # ONE THAT GETS ONLY USER INFO AND
    # THE SECOND ONE THAT GETS ONLY CONTENT

    def get_user_info(self, user_id: int):
        """
        Returns users info like username, about, github, website, etc and counts.

        Parameters:
            user_id (int) : User ID
        """
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
        """
        Returns users content i.e., rants and comments and counts.

        Parameters:
            user_id (int) : User ID
        """
        response = self.get_user_profile(user_id)
        return response["content"]

    def get_user_avatar(self, user_id: int, image_size: str = "small"):
        """
        Returns user avatar's png image url.

        Parameters:
            user_id (int) : User ID

        Optional Parameters:
            image_size (str) : Size of the avatar to be fetched [small/large]
        """
        response = self.get_user_profile(user_id)
        if image_size == "small":
            return self.url_builder.get_user_avatar_url(response["avatar_sm"]["i"])
        elif image_size == "large":
            return self.url_builder.get_user_avatar_url(response["avatar"]["i"])
        return None

    def get_weekly_rant(self, sort: str = "top", skip: int = 0):
        """
        Returns a list of all weekly rants.

        Optional parameters:
            sort (str) : Sort rants by [algo, top, recent], default = algo
            skip (int) : No. of first N rants to skip, default = 0
        """
        url, params = self.url_builder.get_weekly_url(sort, skip)
        response = json.loads(requests.get(url, params=params).text)
        if response["success"]:
            return response["rants"]
        return None

    def get_collabs(self, limit: int = 10, skip: int = 0):
        """
        Returns a list of available collabs.

        Optional parameters:
            limit (int) : No. of rants to fetch, max = 50, default = 10
            skip (int) : No. of first N rants to skip, default = 0
        """
        url, params = self.url_builder.get_collabs_url(skip, limit)
        response = json.loads(requests.get(url, params=params).text)
        if response["success"]:
            return response["rants"]
        return None

    def get_collab_by_id(self, collab_id):
        """
        Returns collaboration rant by its rant id.

        Parameters:
            collab_id (int) : Rant ID of the collab
        """
        return self.get_rant_by_id(collab_id)

    def get_search_results(self, search_term: str):
        """
        Returns list of rants matching the search term.

        Parameters:
            search_term (str) : Search term to be looked up
        """
        url, params = self.url_builder.get_search_url(search_term)
        response = json.loads(requests.get(url, params=params).text)
        if response["success"]:
            return response["results"]
        return None

    def get_surprise_rant(self):
        """
        Returns a random rant from devRant.
        """
        url, params = self.url_builder.get_surprise_url()
        response = json.loads(requests.get(url, params=params).text)
        if response["success"]:
            return response["rant"]
        return None


class DevAuth:
    """Everything that requires a uid, token and key."""

    def __init__(self):
        """Initializing class vars."""
        self.url_builder = URLs()
        self.uid = None
        self.token = None
        self.key = None

    def login(self, username: str, password: str):
        """
        Returns True if Login to devRant is Successful.

        Parameters:
            username (str) : Username of the user
            password (str) : Password of ther user
        """
        url, params = self.url_builder.get_login_url(username, password)
        response = json.loads(requests.post(url, data=params).text)
        if response["success"]:
            self.uid = response["auth_token"]["user_id"]
            self.token = response["auth_token"]["id"]
            self.key = response["auth_token"]["key"]
            return True
        return False

    def post_rant(self, body: str, tags: str = "", category: int = 1):
        """
        Returns Rant ID if rant is posted successfully.

        Parameters:
            body (str) : Text/rant to be posted

        Optional parameters:
            tags (str) : Tags related to the rant, category is automatically appended to tags
            category (int) : Type of rant [1-6] being posted
                        1 = Rant/Story [default]
                        2 = Joke/Meme
                        3 = Question
                        4 = Collab
                        5 = devRant
                        6 = Random
        """
        url, params = self.url_builder.get_post_rant_url(
            body, category, tags, self.uid, self.token, self.key
        )
        response = json.loads(requests.post(url, data=params).text)
        if response["success"]:
            return response["rant_id"]
        return None

    def post_comment(self, rant_id: int, body: str):
        """
        Returns True if comment is posted on the rant successfully .

        Parameters:
            rand_id (int) : ID of the rant where comment  needs to be added
            body (str) : Body of comment
        """
        url, params = self.url_builder.get_post_comment_url(
            rant_id, body, self.uid, self.token, self.key
        )
        response = json.loads(requests.post(url, data=params).text)
        if response["success"]:
            return True
        return False

    def upvote(
        self, ele_id: int, mode: str = "rant", value: int = 1, reason: str = None
    ):
        """
        Returns True if Voting on rant/comment using its id, is done successfully.

        Parameters:
            ele_id (int) : ID of rant or comment to be voted

        Optional Parameters:
            mode (str) : Whether its a rant or a comment, default = rant

        Not be passed if Upvoting:
            value (int) : 1=Upvote [default], 0=Cancel Upvote, -1=Downvote
            reason (int) : Reason for downvote [0=Not for me, 1=Repost, 2= Offensive/Spam]
        """
        url, params = self.url_builder.get_vote_url(
            ele_id, mode, value, reason, self.uid, self.token, self.key
        )
        response = json.loads(requests.post(url, data=params).text)
        if response["success"]:
            return True
        return False

    def unvote(self, ele_id, mode: str = "rant"):
        """
        Returns True if Voting on rant/comment using its id, is done successfully.

        Parameters:
            ele_id (int) : ID of rant or comment to be voted

        Optional Parameters:
            mode (str) : Whether its a rant or a comment, default = rant
        """
        return self.upvote(ele_id, mode, 0)

    def downvote(self, ele_id, reason: int = 0, mode: str = "rant"):
        """
        Returns True if DownVoted on rant/comment, using its id, successfully.

        Parameters:
            ele_id (int) : ID of rant or comment to be voted
            reason (int) : Reason for downvote [0=Not for me, 1=Repost, 2= Offensive/Spam]

        Optional Parameters:
            mode (str) : Whether its a rant or a comment, default = rant
        """
        return self.upvote(ele_id, mode, -1, reason)

    def delete_rant(self, rant_id: int, mode: str = "rant"):
        """
        Returns True if rant is Deleted successfully.

        Parameters:
            rant_id (int) : ID of the rant to be deleted

        Optional Parameter:
            mode (str) : Whether its a rant/comment that being deleted, default = rant
        """
        url, params = self.url_builder.get_delete_rant_url(
            rant_id, mode, self.uid, self.token, self.key
        )
        response = json.loads(requests.delete(url, params=params).text)
        if response["success"]:
            return True
        return False

    def delete_comment(self, comment_id: int, mode: str = "comment"):
        """
        Returns True if comment is Deleted successfully.

        Parameters:
            rant_id (int) : ID of the comment to be deleted

        Optional Parameter:
            mode (str) : Whether its a rant/comment that being deleted, default = comment
        """
        return self.delete_rant(comment_id, mode)

    def get_notifs(self):
        """
        Returns list of unread user notifications.
        """
        url, params = self.url_builder.get_notif_url(self.uid, self.token, self.key)
        response = json.loads(requests.get(url, params=params).text)
        if response["success"]:
            return response["data"]

    def clear_notifs(self):
        """
        Returns True if user notifications are cleared successfully.
        """
        url, params = self.url_builder.get_notif_url(self.uid, self.token, self.key)
        response = json.loads(requests.delete(url, params=params).text)
        if response["success"]:
            return True
        return False
