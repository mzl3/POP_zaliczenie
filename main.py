from models.data import companies, customers, workers
from utils.crud import show_workers, show_companies, add_new_company, delete_company, update_company, \
    show_customers, add_new_customer, delete_customer, update_customer, add_worker, delete_worker, update_worker, \
    map_company

#Logowanie#
print("Zaloguj się:")
def login():
    print("logowanie")
    name = input("Nazwa użytkownika: ")
    password = input("Hasło: ")
    if name == "admin" and password == "admin":
        print("zalogowano")
        return True
    else:
        print("nie zalogowano")
        return False

if __name__ == "__main__":
    if login():
        while True:
            print("Menu:")
            print("0. Zakończ program")
            print("1. Zarządzaj firmami")
            print("2. Zarządzaj klientami")
            print("3. Zarządzaj pracownikami")

            menu_option: str = input("Menu:")
            if menu_option == "0":
                print("Program kończy pracę")
                break

            if menu_option == "1":
                print("Firmy - Co chcesz zrobić?")
                print("1. Wyświetl firmy")
                print("2. Dodaj firmę")
                print("3. Usuń firmę")
                print("4. Aktualizuj dane firmy")
                print("5. Pokaż lokalizację firm")
                menu_option: str = input("Menu:")
                if menu_option == "1":
                    show_companies(companies)

                if menu_option == "2":
                    add_new_company(companies)

                if menu_option == "3":
                    delete_company(companies)

                if menu_option == "4":
                    update_company(companies)

                if menu_option == "5":
                    map_company(companies)

            if menu_option == "2":
                print("Klienci - Co chcesz zrobić?")
                print("0. Zakończ program")
                print("1. Wyświetl klientów")
                print("2. Dodaj klienta")
                print("3. Usuń klienta")
                print("4. Aktualizuj dane klienta")
                menu_option: str = input("Menu:")
                if menu_option == "0":
                        print("Program kończy pracę")
                        break
                if menu_option == "1":
                    show_customers(customers)
                if menu_option == "2":
                    add_new_customer(customers)

                if menu_option == "3":
                    delete_customer(customers)

                if menu_option == "4":
                    update_customer(customers)

            if menu_option == "3":
                print("Pracownicy - Co chcesz zrobić?")
                print("0. Zakończ program")
                print("1. Wyświetl pracowników")
                print("2. Dodaj pracownika")
                print("3. Usuń pracownika")
                print("4. Aktualizuj dane pracownika")
                menu_option: str = input("Menu:")
                if menu_option == "0":
                    print("Program kończy pracę")
                    break
                if menu_option == "1":
                    show_workers(workers)

                if menu_option == "2":
                    add_worker(workers)

                if menu_option == "3":
                    delete_worker(workers)

                if menu_option == "4":
                    update_worker(workers)
