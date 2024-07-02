from models.data import users, companies, customers, workers
from utils.crud import add_new_user, show_workers, show_companies, add_new_company, delete_company, update_company, \
    show_customers, add_new_customer, delete_customer, edit_customer, add_worker, delete_worker, edit_worker

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
                print("1. Wyświetl firmy")
                show_companies(companies)
                print("2. Dodaj firmę")
                add_new_company(companies)
                print("3. Usuń firmę")
                delete_company(companies)
                print("4. Aktualizuj dane firmy")
                update_company(companies)

            if menu_option == "2":
                print("Klienci - Co chcesz zrobić?")
                print("1. Wyświetl klientów")
                show_customers(customers)
                print("2. Dodaj klienta")
                add_new_customer(customers)
                print("3. Usuń klienta")
                delete_customer(customers)
                print("4. Aktualizuj dane klienta")
                edit_customer(customers)

            if menu_option == "3":
                print("Pracownicy - Co chcesz zrobić?")
                print("1. Wyświetl pracowników")
                show_workers(workers)
                print("2. Dodaj pracownika")
                add_worker(workers)
                print("3. Usuń pracownika")
                delete_worker(workers)
                print("4. Aktualizuj dane pracownika")
                edit_worker(workers)
