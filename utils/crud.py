import folium
import requests
from bs4 import BeautifulSoup

##Company##
def show_companies(companies: list[dict]) -> None:
    for company in companies:
        print(f"Imie: {company['name']} Klienci: {company['customers']}, Lokalizacja: {company['location']}")

def add_new_company(companies: list) -> None:
    company_name = input("Enter company name: ")
    company_customers = input("Enter company customers: ")
    company_location = input("Enter company location: ")
    new_company: dict = {"name": company_name,"customers": company_customers, "location": company_location}
    companies.append(new_company)


def delete_company(companies: list) -> None:
    jaka_firma = input("Podaj nazwę firmy, którą chcesz usunąć z bazy danych:")
    for company in companies:
        if company['name'] == jaka_firma:
            companies.remove(company)

def update_company(companies: list) -> None:
    kogo_szukasz = input("kogo szukasz?: ")
    for company in companies:
        if company['name'] == kogo_szukasz:
            company['name'] = input('podaj nowe nazwę firmy: ')
            company['location'] = input('podaj nową lokalizację: ')



def map_company(companies):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for company in companies:
        url = (f"https://pl.wikipedia.org/wiki/{company['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{company['name']},\n{company['location']}",
                      icon=folium.Icon(color='green')).add_to(map)

    map.save('models/map/map_companies.html')


##Customer##
def show_customers(customers: list) -> None:
    for customer in customers:
        print(f"Firma {customer['name']}")

def add_new_customer(customers: list) -> None:
    new_customers_name = input("Enter company name: ")
    new_customers_surname = input("Enter customer surname: ")
    new_customers_for = input("Enter company")
    new_customer = {"name": new_customers_name, "surname": new_customers_surname, "for": new_customers_for}
    customers.append(new_customer)

def delete_customer(customers: list) -> None:
    jaki_klient = input("Enter customers name: ")
    for customer in customers:
        if customer['name'] == jaki_klient:
            customer.remove(customer)

def update_customer(customers: list) -> None:
    kogo_szukasz = input("kogo szukasz?: ")
    for customer in customers:
        if customer['name'] == kogo_szukasz:
            customer['name'] = input('podaj nowe nazwę firmy: ')
            customer['location'] = input('podaj nową lokalizację: ')


##workers##
def show_workers(workers: list) -> None:
    for worker in workers:
        print(f"Firma {worker['name']}")

def add_worker(workers: list) -> None:
    new_worker_name = input("enter worker's name")
    new_worker_surname = input("enter worker's surname")
    new_worker_for = input("enter company")
    new_worker = {"name": new_worker_name, "surname": new_worker_surname, "for": new_worker_for}
    workers.append(new_worker)

def delete_worker(workers: list) -> None:
    jaki_pracownik = input("Enter worker's name: ")
    for worker in workers:
        if worker["name"] == jaki_pracownik:
            worker.remove(workers)

def update_worker(workers: list) -> None:
    kogo_szukasz = input("kogo szukasz?: ")
    for worker in workers:
        if worker['name'] == kogo_szukasz:
            worker['name'] = input('podaj nowe imie: ')
            worker['surname'] = input('podaj nowe nazwisko: ')
