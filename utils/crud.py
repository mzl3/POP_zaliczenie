#rejestracja nowego użytkownika#

def add_new_user(users: list):
    new_user_login = input("<LOGIN>")
    new_user_password = input("<PASSWORD>:")
    new_user: dict = {"login": new_user_login, "password": new_user_password}
    users.append(new_user)

##Company##
def show_companies(companies: list)-> None:
    for company in companies:
        print(f"Firma {company['name']}")
def add_new_company(companies: list)-> None:
    new_name: str = input("Enter company name: ")
    new_user: dict = {"name": new_name,}
    print(new_user)

def delete_company(companies: list)-> None:
    jaka_firma = input("Enter company name: ")
def update_company(companies: list)-> None:
    kogo_szukasz = input("kogo szukasz?: ")
    for company in companies:
        if company['name'] == kogo_szukasz:
            company['name'] = input('podaj nowe imię: ')
            company['surname'] = input('podaj nowe nazwisko: ')
            company['posts'] = input('podaj liczbę postów: ')

##Customer##
def show_customers(customers: list)-> None:

def add_customer(customers: list)-> None:

def remove_customer(customers: list)-> None:

def edit_customer(customers: list)-> None:


##workers##
def show_workers(workers: list)-> None:

def add_worker(workers: list)-> None:

def remove_worker(workers: list)-> None:

def edit_worker(workers: list)-> None: