import requests
import logging
import configparser

from datetime import datetime


def api_request():
    # Чтение конфига
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("config.ini")  # читаем конфиг
    api_key_base64 = (config["keys"]["api_key_base64"])

    base_url = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/sales?'

    # Получение даты из файла:
    with open('from_datetime', 'r') as f:
        date_from = f.read()

    # Выполнение запроса
    data = []

    try:
        logging.basicConfig(level=logging.DEBUG)
        response = requests.get(
            f'{base_url}dateFrom={date_from}&key={api_key_base64}', timeout=10)
        if response.status_code == 200:
            data = response.json()
            time_now = datetime.now()
            time_now_iso = time_now.isoformat(sep='T')
            with open('from_datetime', 'w') as f:
                f.write(time_now_iso)
        else:
            print(
                f'Запрос не прошел, слишком частые попытки, попробуйте позже: HTTP {response.status_code}, {response.url}')

    except ConnectionError:
        print('Ошибка подключения')

    if data:
        print(f'Получено новых элементов: {len(data)}')
        return data
