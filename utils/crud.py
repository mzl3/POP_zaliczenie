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
    company_name = input("Enter company name: ")
    company_location = input("Enter company location: ")
    companies.append(companies)

def delete_company(companies: list)-> None:
    jaka_firma = input("Enter company name: ")
    for company in companies:
        if company["name"] == jaka_firma:
            companies.remove(company)
def update_company(companies: list)-> None:
    kogo_szukasz = input("kogo szukasz?: ")
    for company in companies:
        if company['name'] == kogo_szukasz:
            company['name'] = input('podaj nowe nazwę firmy: ')
            company['location'] = input('podaj nową lokalizację: ')

##Customer##
def show_customers(customers: list)-> None:
    for customer in customers:
        print(customers)
def add_new_customer(customers: list)-> None:
    company_name = input("Enter company name: ")
    customers_surname = input("Enter customer surname: ")
    customers.append(customer)
def delete_customer(customers: list)-> None:
        jaki_klient = input("Enter customers name: ")
        for customer in customers:
            if customer["name"] == jaki_klient:
                customer.remove(customer)
def edit_customer(customers: list)-> None:


##workers##
def show_workers(workers: list)-> None:
    for worker in workers:
        print(workers)
def add_worker(workers: list)-> None:
    new_worker_name = input("enter worker's name")
    new_worker_surname = input("enter worker's surname")
    new_for = input("enter company")
    workers.append(worker)
def delete_worker(workers: list)-> None:
    jaki_pracownik = input("Enter worker's name: ")
    for worker in workers:
        if worker["name"] == jaki_pracownik:
            worker.remove(workers)
def edit_worker(workers: list)-> None:
    new_worker_name = input("enter worker's name")
    new_worker_surname = input("enter worker's surname")
    new_for = input("enter company")
