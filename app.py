"""
Author: Deepak Talan
Github: @d02d33pak
App.py
"""

from devRantAPI.api import DevRant, DevAuth
import utils


def run():
    """
    Interacting with the API.
    For demonstation purposes only.
    """

    dev = DevRant()
    auth = DevAuth()

    # GET MULTIPLE RANTS
    rants = dev.get_rants("recent", 1, 0)
    for rant in rants:
        print(rant["id"])
        print(7 * "-")

    # GET SINGLE RANT BY ID
    # rant = dev.get_rant_by_id(rant)
    # print("posted this rant", rant["text"])

    # GET USER ID FROM USERNAME
    user_id = dev.get_user_id("d02d33pak")
    print("d02d33pak user id =", user_id)

    # GET USER PROFILE FROM USER ID
    # data = dev.get_user_profile(user_id)
    # print(data["about"])

    # GET USER INFO FROM USER ID
    # info = dev.get_user_info(user_id)
    # print(info)

    # GET USER CONTENT FROM USER ID
    # content = dev.get_user_data(user_id)
    # print(content)

    # GET USER AVATAR PNG LINK
    # avatar = dev.get_user_avatar(user_id, "small")
    # print(avatar)

    # LOGIN
    if auth.login(utils.USERNAME, utils.PASSWORD):
        print("logged in")

    # POST RANT
    rant = auth.post_rant("ranting from apis")
    print("created rant ->", rant)

    # POST COMMENT
    if auth.post_comment(rant, "commenting from api"):
        print("comment posted on", rant)

    # VOTE ON RANT
    # if auth.downvote(2791146, 0):
    #     print("DOWN VOTED")
    # if auth.downvote(2791146, 1):
    #     print("DOWN VOTED")
    # if auth.downvote(2791146, 2):
    #     print("DOWN VOTED")
    # if auth.upvote(2791146):
    #     print("UP voted")
    # if auth.unvote(2791146):
    #     print("UN voted")

    # PRINT POSTED RANT
    # print(dev.get_rant_by_id(rant)["id"])

    # GET A RANDOM RANT
    print(dev.get_surprise_rant())

    # DELETE COMMENT
    if auth.delete_rant(rant):
        print("deleted", rant)

    # GET NOTIFICATIONS
    # print(auth.get_notifs())


if __name__ == "__main__":
    run()
