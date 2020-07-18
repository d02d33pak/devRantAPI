"""all URLs"""


class URLs:
    """url class"""

    def __init__(self):
        self.base_url = "https://devrant.com/api/"
        self.app_id = "?app=3"
        self.rants_url = "devrant/rants"
        self.single_rant_url = "devrant/rants/"
        self.user_id = "get-user-id"
        self.user_info = "users/"
        self.user_avatar = "https://avatars.devrant.com/"

    def get_rants_url(self, sort, limit, skip):
        """multi rants"""
        sort = self.validate_sort(sort)
        limit = self.validate_int(limit)
        skip = self.validate_int(skip)
        return f"{self.base_url}{self.rants_url}{self.app_id}&sort={sort}&limit={limit}&skip={skip}"

    def get_rant_by_id_url(self, rant_id):
        """single rant"""
        return f"{self.base_url}{self.single_rant_url}{rant_id}{self.app_id}"

    def get_user_id_url(self, username):
        """return user_id url"""
        return f"{self.base_url}{self.user_id}{self.app_id}&username={username}"

    def get_user_info_url(self, user_id):
        """return user_id url"""
        return f"{self.base_url}{self.user_info}{user_id}{self.app_id}"

    def get_user_avatar_url(self, avatar_link):
        """return png url"""
        return f"{self.user_avatar}{avatar_link}"

    def validate_sort(self, sort):
        """validate sort method"""
        if sort in ["algo", "recent", "top"]:
            return sort
        raise ValueError("Invalid Sort Type")

    def validate_int(self, num):
        """validate any int input"""
        if num >= 0:
            return num
        raise ValueError("Limit/Skip should be positive Integers")
