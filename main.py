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
            if user_login == "" and user_password == "":
                print("logowanie się powiodło")
                return True

            else:
                print("logowanie się NIE powiodło, spróbuj ponownie")
                return False

        if menu_option == "2":
            print("Zarejestruj się:")
            add_new_user(users)

if __name__ == "__main__":
        while True:
            print("Menu:")
            print("0. Zakończ program")
            print("1. Zarządzaj firmami")
            print("2. Zarządzaj klientami")
            print("3. Zarządzaj pracownikami")
            if menu_option == "0":
                print("Program kończy pracę")
                break

            if menu_option == "1":
                print("Firmy - Co chcesz zrobić?")
                print("0. Anuluj")
                return
                print("1. Wyświetl firmy")
                show_companies
                print("2. Dodaj firmę")
                add_new_company
                print("3. Usuń firmę")
                delete_company
                print("4. Aktualizuj dane firmy")
                edit_company

            if menu_option == "2":
                print("Klienci - Co chcesz zrobić?")
                print("0. Anuluj")
                return
                print("1. Wyświetl klientów")
                show_customers
                print("2. Dodaj klienta")
                add_new_customer
                print("3. Usuń klienta")
                delete_customer
                print("4. Aktualizuj dane klienta")
                edit_customer

            if menu_option == "3":
                print("Pracownicy - Co chcesz zrobić?")
                print("0. Anuluj")
                return
                print("1. Wyświetl pracowników")
                show_workers
                print("2. Dodaj pracownika")
                add_new_worker
                print("3. Usuń pracownika")
                delete_worker
                print("4. Aktualizuj dane pracownika")
                edit_worker
