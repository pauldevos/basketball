from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from email import header

HTTP_HEADERS = {
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


@dataclass
class StatsHTTPHeader(ABC):
    # base_url = "https://stats.nba.com/stats"
    http_headers: dict = field(default_factory=dict)

    def make_url_string(self):
        return "endpoint"

    def __post_init__(self):
        # construct the header with any updated key-values needed
        if self.http_headers:
            d = HTTP_HEADERS.copy()
            for k, v in self.http_headers.items():
                d[k] = v
            self.http_headers = d
        else:
            self.http_headers = HTTP_HEADERS.copy()


@dataclass
class CommonallPlayers:
    __endpoint__ = "CommonallPlayers"
    base_url = "https://stats.nba.com/stats"

    IsOnlyCurrentSeason: int = 0
    LeagueID: str = "00"
    Season: str = "2021-22"
    proxies: list = field(default_factory=list)

    # def __post_init__(self):

    #     # construct the header with any updated key-values needed
    #     if self.headers:
    #         d = HTTP_HEADERS.copy()
    #         for k, v in self.headers.items():
    #             d[k] = v
    #         self.headers = d
    #     else:
    #         self.headers = HTTP_HEADERS.copy()

    def get_header():
        return super().make_url_string()

    def request_data(self):
        API_URL = f"{self.base_url}/{self.__endpoint__}"
        return API_URL


c = CommonallPlayers()

print(c)

print(c.get_header())

# print(d.request_data())
