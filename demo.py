"""
Author: Deepak Talan
Github: @d02d33pak
Demo.py
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

    print("# GET MULTIPLE RANTS #")
    rants = dev.get_rants("recent", 2, 1)
    for rant in rants:
        print(rant["id"])
    print()

    print("# GET SINGLE RANT BY ID #")
    rant = dev.get_rant_by_id(2780108)
    print(rant["rant"]["text"])
    print()

    print("# GET USER ID FROM USERNAME #")
    user_id = dev.get_user_id("d02d33pak")
    print(user_id)
    print()

    print("# GET USER PROFILE #")
    profile = dev.get_user_profile(user_id)
    print(profile["about"])
    print()

    print("# GET USER INFO #")
    info = dev.get_user_info(user_id)
    print(info["location"])
    print()

    print("# GET USER DATA #")
    data = dev.get_user_data(user_id)
    print(data["counts"]["rants"])
    print()

    print("# GET USER AVATAR #")
    print(dev.get_user_avatar(user_id, "small"))
    print()

    print("# GET WEEKLY RANTS #")
    weekly = dev.get_weekly_rant()
    for rant in weekly:
        print(rant["text"])
        print(50 * "*")
    print()

    print("# GET COLLABS #")
    collabs = dev.get_collabs(3)
    for collab in collabs:
        print(collab["text"])
    print()

    print("# GET COLLAB BY ID")
    collab = dev.get_collab_by_id(2793063)
    print(collab["rant"]["text"])
    print()

    print("# GET SEARCH RESULTS #")
    results = dev.get_search_results("d02d3pak")
    print(results[0]["text"])
    print()

    print("# GET SURPRISE RANT #")
    rant = dev.get_surprise_rant()
    print(rant["text"])
    print()

    print("# LOGIN #")
    if auth.login(utils.USERNAME, utils.PASSWORD):
        print("Logged In.\n")

    print("# DOWNVOTE RANT #")
    if auth.downvote(285611):
        print("Rant DOWN voted.\n")

    print("# UPVOTE RANT #")
    if auth.upvote(285611):
        print("Rant UP voted.\n")

    print("# UNVOTE RANT #")
    if auth.unvote(285611):
        print("Rant UN voted.\n")

    print("# DOWNVOTE Comment #")
    if auth.downvote(285859, 0, "comment"):
        print("Comment DOWN voted.\n")

    print("# UPVOTE Comment #")
    if auth.upvote(285859, "comment"):
        print("Comment UP voted.\n")

    print("# UNVOTE Comment #")
    if auth.unvote(285859, "comment"):
        print("Comment UN voted.\n")

    print("# POST RANT #")
    my_rant = auth.post_rant("this is an api rant")
    print("Posted rant.\n")

    print("# POST COMMENT #")
    if auth.post_comment(my_rant, "this is an api comment"):
        print("Posted comment.\n")

    print("# DELETE COMMENT #")
    if auth.delete_comment(dev.get_rant_by_id(my_rant)["comments"][0]["id"]):
        print("Deleted comment.\n")

    print("# DELETE RANT #")
    if auth.delete_rant(my_rant):
        print("Deleted rant.\n")

    print("# GET NOTIFICATIONS #")
    print(auth.get_notifs())
    print()

    print("# CLEAR NOTIFICATIONS #")
    if auth.clear_notifs():
        print("Ntofications cleared.\n")


if __name__ == "__main__":
    run()
