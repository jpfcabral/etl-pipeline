from typing import Dict
import requests
from .interfaces.http_requester import HttpRequesterInterface


class HttpRequester(HttpRequesterInterface):
    def __init__(self, url):
        self.__url = url

    def request_from_url(self) -> Dict[int, str]:
        response = requests.get(self.__url)
        return {
            'status_code': response.status_code,
            'html': response.text
        }
