from dataclasses import dataclass

import requests

from ..utils.headers import BASE_URL, REQUEST_HEADER


# r = requests.get(url, headers=headers).json()
@dataclass
class HTTPHeader:
    endpoint: str
    endpoint_params: str
    base_url: str = BASE_URL
    header: dict = REQUEST_HEADER
