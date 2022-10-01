import configparser
import logging
from datetime import datetime

import requests


CONFIG_FILE = 'config.ini'
DATE_STORE_FILE = 'from_datetime'
BASE_URL = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/sales?'


def api_request():
    """Requesting the wildberries API"""

    # Loading date from config file
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    api_key_base64 = (config["keys"]["api_key_base64"])

    # Getting date from file:
    with open(DATE_STORE_FILE) as f:
        date_from = f.read()

    # Making API request
    data = []
    try:
        logging.basicConfig(level=logging.DEBUG)
        response = requests.get(
            f'{BASE_URL}dateFrom={date_from}&key={api_key_base64}', timeout=10)
        if response.status_code == 200:
            data = response.json()
            time_now = datetime.now()
            time_now_iso = time_now.isoformat(sep='T')
            with open('from_datetime', 'w') as f:
                f.write(time_now_iso)
        else:
            print(
                f'Cant request, try again later: HTTP {response.status_code}, {response.url}')

    except ConnectionError:
        print('Connection error')

    if data:
        print(f'Number of elements reached: {len(data)}')
        return data
