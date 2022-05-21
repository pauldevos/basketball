from dataclasses import dataclass
from urllib.parse import urlencode

import requests

import utilities.headers as util


@dataclass
class CommonallPlayers(util.HTTPHeader):
    IsOnlyCurrentSeason: int = 0
    LeagueID: str = "00"
    Season: str = 2021 - 22

    @classmethod
    def encode_params(cls):
        cls.__dict__
        return urlencode(cls.__dict_)

    # def get_request(endpoint):
    #     url_string = f"{BASE_URL}/{endpoint}/"
    #     requests.get(BASE_URL)
    #     return True


c = CommonallPlayers()

print(c.encode_params())
