from decorators import requires_login


@requires_login
def show_profile():
    print("Your Profile")


show_profile()
