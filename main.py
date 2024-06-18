from models.data import users
from utils.crud import add_new_user

#Logowanie#
if __name__ == "__main__":
    print('Co chcesz zrobić?')
    while True:
        print("Menu:")
        print("0. Zakończ program")
        print("1. Zaloguj się")
        print("2. Nie masz konta? Zarejestruj się")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == "0":
            print("Program kończy pracę")
            break
        if menu_option == "1":
            print("Zaloguj się:")
            user_login = input("<LOGIN>")
            user_password = input("<PASSWORD>:")
            if user_login =="" and user_password=="":
                print("logowanie się powiodło")
                return True

            else:
                print("logowanie się NIE powiodło, spróbuj ponownie")
                return False

        if menu_option == "2":
            print("Zarejestruj się:")
            add_new_user(users)



