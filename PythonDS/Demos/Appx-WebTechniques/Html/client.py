# To run this application, first you must run:   
#    pip install requests
#    pip install bs4

import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('http://localhost:8000/')

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.table

dataframes = pd.read_html(str(table), index_col=0, header=0)
weather_dataframe = dataframes[0]
print('Weather DataFrame\n', weather_dataframe)