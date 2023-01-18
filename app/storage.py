import os

import json

from flask import current_app

from app import scraper

DATA_FILE_NAME = 'data.json'


def save_data(data: list) -> None:

    os.makedirs(current_app.instance_path, exist_ok=True)
    path = os.path.join(current_app.instance_path, DATA_FILE_NAME)

    with open(path, encoding='utf-8', mode='w') as file:
        json.dump(data, file)


def load_data() -> list:
    path = os.path.join(current_app.instance_path, DATA_FILE_NAME)

    data = []
    if os.path.exists(path):
        with open(path, encoding='utf-8', mode='r') as file:
            data = json.load(file)
    else:
        data = scraper.run()
        save_data(data)
    return data
