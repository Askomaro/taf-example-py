import json

import requests


class BaseResource:
    def __init__(self):
        pass

    _SCHEMA = 'https://'
    _HOST = 'www.swapi.tech/api/'

    def _get_response(self, url, params=None):
        r = requests.get(url, params=params)

        return json.loads(r.text)
