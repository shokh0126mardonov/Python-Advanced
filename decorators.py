correct_username = "ali"
correct_password = "1234"


def requires_login(func):

    def wrapper():
        username = input("username: ")
        password = input("password: ")

        if username != correct_username or correct_password != password:
            print("login qilishiz kerak")
        else:
            func()

    return wrapper
