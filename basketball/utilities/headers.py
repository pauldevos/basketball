from dataclasses import dataclass

from header_config import BASE_URL, REQUEST_HEADER
@dataclass
class HTTPHeader:
    endpoint: str
    endpoint_params: str
    base_url: str = BASE_URL
    header: dict = REQUEST_HEADER
