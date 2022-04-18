from typing import Dict
import requests


class HttpRequester:
    def __init__(self, url):
        self.__url = url

    def request_from_url(self) -> Dict[int, str]:
        response = requests.get(self.__url)
        return {
            'status_code': response.status_code,
            'html': response.text
        }
