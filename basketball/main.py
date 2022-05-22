from dataclasses import asdict, dataclass, field

import requests

HTTP_HEADER = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "stats.nba.com",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true",
}

BASE_URL = "https://stats.nba.com/stats/"


@dataclass
class HTTPHeader:
    proxies: list[str] = None
    base_url: str = BASE_URL
    # header: field(default_factory=dict) = HTTP_HEADER # ValueError: mutable default <class 'dict'> for field header is not allowed: use default_factory
    # header: dict = HTTP_HEADER # ValueError: mutable default <class 'dict'> for field header is not allowed: use default_factory
    # header: field(default_factory=dict) = HTTP_HEADER # ValueError: mutable default <class 'dict'> for field header is not allowed: use default_factory

    # @header.setter
    # def header(self, v: dict) -> None:
    #     self.header = REQUEST_HEADER


from urllib.parse import urlencode


@dataclass
class CommonallPlayers:
    IsOnlyCurrentSeason: int = 0
    LeagueID: str = "00"
    Season: str = "2021-22"

    @classmethod
    def encode_api_params(cls):
        return cls.__dict__.items()

    # returns everything under the sun, not only the 3 attributes: IsOnlyCurrentSeason, LeagueID, Season

    def encode_api_params_1(self):
        return dict(self.IsOnlyCurrentSeason, self.LeagueID, self.Season)

    # return urlencode(cls.__dict_)

    # def get_request(endpoint):
    #     url_string = f"{BASE_URL}/{endpoint}/"
    #     requests.get(BASE_URL)
    #     return True


c = CommonallPlayers()

# print(dir(c))
print(c.encode_api_params_1())
