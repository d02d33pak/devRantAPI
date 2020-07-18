"""
Author: Deepak Talan
Github: @d02d33pak
all URLs
"""


class URLs:
    """url class"""

    def __init__(self):
        """initializing all urls"""
        self.base_url = "https://devrant.com/api/"
        self.app_id = "?app=3"
        self.rants_url = "devrant/rants"
        self.single_rant_url = "devrant/rants/"
        self.user_id = "get-user-id"
        self.user_profile = "users/"
        self.user_avatar = "https://avatars.devrant.com/"
        self.weekly_rants = "devrant/weekly-rant"
        self.collabs = "devrant/collabs"
        self.search = "devrant/search"

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

    def validate_int(self, num):
        """validate any int input"""
        if num >= 0:
            return num
        raise ValueError("Limit/Skip should be positive Integers")
