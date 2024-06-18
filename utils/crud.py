#rejestracja nowego użytkownika#

def add_new_user(users: list):
    new_user_login = input("<LOGIN>")
    new_user_password = input("<PASSWORD>:")
    new_user: dict = {"login": new_user_login, "password": new_user_password}
    users.append(new_user)

#
def show_companies(companies: list):

