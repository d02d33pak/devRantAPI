"""main func"""
from devRantAPI.api import DevRant, DevAuth


def run():
    """Calling api."""
    dev = DevRant()
    auth = DevAuth()
    # GET MULTIPLE RANTS
    # rants = dev.get_rants("recent", 2, 0)
    # for rant in rants:
    #     print(rant["text"])
    #     print(100 * "-")
    # print(len(rants))

    # GET SINGLE RANT BY ID
    # rant = dev.get_rant_by_id(2764787)
    # print(rant["text"])

    # GET USER ID FROM USERNAME
    # user_id = dev.get_user_id("d02d33pak")
    # print(user_id)

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
    print(auth.login("", ""))

    # POST COMMENT
    # print(auth.post_comment(2780108, "api comment"))

    # VOTE ON RANT
    print(auth.vote(2780108))


if __name__ == "__main__":
    run()
