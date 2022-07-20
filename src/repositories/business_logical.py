import ast
import json

import requests
from datetime import datetime
from requests_oauthlib import OAuth1
from repositories import bd_Agtech
from config.settings import Setting
from enums.token_fixed import Polygon


def available_companies():
    url = Polygon('available_companies')
    url_auth = f'{url}?apiKey={Setting.polygon_auth}'
    info_companies = requests.get(url_auth)
    symbols = []

    companies = json.loads(info_companies.content)['results']

    if info_companies.status_code == 200:
        for company in companies:
            company_tracker = company.get('ticker', False)
            if company_tracker:
                symbols.append(company_tracker)
        return symbols
    else:
        return "Intente nuevamente"


def price_open_close(stocksTicker, date, adjusted):
    parameter = {
        'stocksTicker': stocksTicker,
        'date': date
    }
    url = Polygon('price', **parameter)
    url_auth = f'{url}?adjusted={adjusted}&apiKey={Setting.polygon_auth}'
    response = requests.get(url_auth)
    if response.status_code == 200:
        price_symbol = json.loads(response.content)
        dic_return = {
            'symbol': price_symbol.get('symbol', ''),
            'price_max': price_symbol.get('high', ''),
            'price_min': price_symbol.get('low', ''),
            'price_open': price_symbol.get('open', ''),
            'price_closed': price_symbol.get('close', ''),
            'price_mean': (price_symbol.get('high', 0) + price_symbol.get('high', 0)) / 2,
        }

        return dic_return


def created_user(user_id, favorite_companies=[], discarded_companies=[]):
    status_table = bd_empowerment.get_status_table(_table_name=Setting.user_table)
    if status_table == 'ACTIVE':
        response = bd_empowerment.create_user(_table_name=Setting.user_table,
                                              _user_id=user_id,
                                              _favorite_companies=favorite_companies,
                                              _discarded_companies=discarded_companies)
    return {'status': ' status 201 | user created', 'user_id': user_id} if response['ResponseMetadata'][
                                                                               'HTTPStatusCode'] == 200 else None


# TODO Validar si el usuario existe previamente, aunque esto debería estar cubierto con el pipeline del auth

def companies_tracker(user_id, favorite_companies):
    status_table = bd_empowerment.get_status_table(_table_name=Setting.user_table)

    if status_table == 'ACTIVE':
        response = bd_empowerment.update_favorite_companies(_table_name=Setting.user_table,
                                                            _user_id=user_id,
                                                            _favorite_companies=favorite_companies)
    return {'status': ' status 201 | compañias agregadas en el usuario', 'user_id': user_id} if \
        response['ResponseMetadata'][
            'HTTPStatusCode'] == 200 else None


# TODO decorizar estas funciones.
def get_price_favorite(user_id, date):
    status_table = bd_empowerment.get_status_table(_table_name=Setting.user_table)

    if status_table == 'ACTIVE':
        response = bd_empowerment.get_atribute(_table_name=Setting.user_table,
                                               _user_id=user_id,
                                               _atribute='favorite_companies')

        favorite_comanies = response['Items'][0]['favorite_companies']
        companies_price = []
        for symbol in favorite_comanies:
            parameter = {
                'stocksTicker': symbol,
                'date': date
            }
            url = Polygon('price', **parameter)
            url_auth = f'{url}?adjusted=false&apiKey={Setting.polygon_auth}'
            response = requests.get(url_auth)
            if response.status_code == 200:
                price_symbol = json.loads(response.content)
                dic_return = {
                    'symbol': price_symbol.get('symbol', ''),
                    'price_max': price_symbol.get('high', ''),
                    'price_min': price_symbol.get('low', ''),
                    'price_open': price_symbol.get('open', ''),
                    'price_closed': price_symbol.get('close', ''),
                    'price_mean': (price_symbol.get('high', 0) + price_symbol.get('high', 0)) / 2,
                }
                companies_price.append(dic_return)

        return {'status':'status 201', 'prices':companies_price}



def get_price_all(user_id, date):
    status_table = bd_empowerment.get_status_table(_table_name=Setting.user_table)

    if status_table == 'ACTIVE':
        response_symbols = available_companies()

        companies_price = []
        for symbol in response_symbols:
            parameter = {
                'stocksTicker': symbol,
                'date': date
            }
            url = Polygon('price', **parameter)
            url_auth = f'{url}?adjusted=false&apiKey={Setting.polygon_auth}'
            response = requests.get(url_auth)
            if response.status_code == 200:
                price_symbol = json.loads(response.content)
                dic_return = {
                    'symbol': price_symbol.get('symbol', ''),
                    'price_max': price_symbol.get('high', ''),
                    'price_min': price_symbol.get('low', ''),
                    'price_open': price_symbol.get('open', ''),
                    'price_closed': price_symbol.get('close', ''),
                    'price_mean': (price_symbol.get('high', 0) + price_symbol.get('high', 0)) / 2,
                }
                companies_price.append(dic_return)

        return {'status':'status 201', 'prices':companies_price}