# To run this application, first you must run:   
#    pip install flask
#    pip install flask_restful
#    pip install waitress

from flask import Flask
from flask_restful import Api
from waitress import serve

import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

df = pd.read_csv('BergenWeather2019.csv', 
                  parse_dates=['MonthYear'], 
                  index_col='MonthYear',
                  date_format='%m/%Y')
print('DataFrame loaded', df)


@app.route('/api/weather', methods=['GET'])
def get_all_data():
    return df.to_json(orient='index'), 200


@app.route('/api/weather/<month_year>', methods=['GET'])
def get_data_for_month_year(month_year):
    if month_year in df.index:
        return df.loc[month_year].to_json(orient='index'), 200
    else:
        return f'Invalid month_year index "{month_year}"', 404


@app.route('/api/weather/annual-min-temp', methods=['GET'])
def get_annual_min_temp():
    annual_min_temp = pd.Series.min(df.MinTemp)
    return json.dumps(annual_min_temp), 200


@app.route('/api/weather/annual-max-temp', methods=['GET'])
def get_annual_max_temp():
    annual_max_temp = pd.Series.max(df.MaxTemp)
    return json.dumps(annual_max_temp), 200


@app.route('/api/weather/annual-total-precipitation', methods=['GET'])
def annual_total_precipitation():
    annual_total_precipitation = pd.Series.sum(df.Precipitation)
    return json.dumps(annual_total_precipitation), 200


print('REST service listening on http://localhost:8080/')
serve(app, host="0.0.0.0", port=8080)