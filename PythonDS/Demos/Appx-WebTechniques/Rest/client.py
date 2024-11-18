# To run this application, first you must run:   
#    pip install requests

import requests
import pandas as pd

base_address = 'http://localhost:8080/api/weather'


def demo_get_all_data():
    response = requests.get(base_address)
    if response.status_code != 200:
        print("Oops, couldn't get data")
    else:
        df = pd.read_json(response.text, orient='index')
        print('All data\n', df)


def demo_get_data_for_month_year(month_year):
    response = requests.get(f'{base_address}/{month_year}')
    if response.status_code != 200:
        print("\nOops, couldn't get data")
    else:
        df = pd.read_json(response.text, orient='index')
        print(f'\nData for month_year {month_year}\n', df)


def demo_get_annual_min_temp():
    response = requests.get(f'{base_address}/annual-min-temp')
    if response.status_code != 200:
        print("\nOops, couldn't get data")
    else:
        min = response.json()
        print(f'\nAnnual minimum temperature: {min}C')

        
def demo_get_annual_max_temp():
    response = requests.get(f'{base_address}/annual-max-temp')
    if response.status_code != 200:
        print("\nOops, couldn't get data")
    else:
        max = response.json()
        print(f'\nAnnual maximum temperature: {max}C')

        
def demo_get_annual_total_precipitation():
    response = requests.get(f'{base_address}/annual-total-precipitation')
    if response.status_code != 200:
        print("\nOops, couldn't get data")
    else:
        precip = response.json()
        print(f'\nAnnual total precipitation: {precip}mm')

        
demo_get_all_data()
demo_get_data_for_month_year('01-2019')
demo_get_data_for_month_year('wibble')
demo_get_annual_min_temp()
demo_get_annual_max_temp()
demo_get_annual_total_precipitation()