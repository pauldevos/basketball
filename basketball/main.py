from dataclasses import asdict, dataclass, field

import requests

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

BASE_URL = "https://stats.nba.com/stats/"
@dataclass
class CommonallPlayers:

    __endpoint__ = "CommonallPlayers"
    
    IsOnlyCurrentSeason: int = 0
    LeagueID: str = "00"
    Season: str = "2021-22"
    headers: dict = field(default_factory=None)
    
    def __post_init__(self):
        if not self.headers:
            self.headers = HTTP_HEADERS
            
    def get_params(self):
        return {"IsOnlyCurrentSeason": self.IsOnlyCurrentSeason, "LeagueID": self.LeagueID, "Season": self.Season}
    
    def request_data(self):
        request_url = f"{BASE_URL}{self.__endpoint__}"
        return requests.get(request_url, params=self.get_params(), headers=self.headers)
    
    def to_csv(self):
        pass
    
    def to_json(self):
        pass
    
    def to_sql(self):
        pass
    
    def google_drive(self):
        pass
    
    def to_s3(self):
        pass

    # def __init__(
    #     self,
    #     IsOnlyCurrentSeason=0,
    #     LeagueID="00",
    #     Season="2021-22",  # , header=HTTPHeader
    # ) -> None:
    #     # these first 3 attributes constitute the (#2) API Params
    #     self.IsOnlyCurrentSeason = IsOnlyCurrentSeason
    #     self.LeagueID = LeagueID
    #     self.Season = Season

    # def encode_api_params(self):
    #     return self.__dict__  #  # if only 3 attributes, this works

    # def get_http_header(self):
    #     # ideally can return the http_header as a dict
    #     pass

    # # ideally this is NOT instantiated (as doesn't have data, shouldn't be accessible to user until AFTER request)
    # def request_data(self):
    #     url_api = f"{BASE_URL}/{self.__endpoint__}"
    #     return requests.get(
    #         url_api, params=self.encode_api_params(), headers=self.get_http_header()
    #     )
    

# works, has current defaults (current season)
c = CommonallPlayers()


# # a common use case, using a different Season than the default (current season)
# c = Players(Season="1999-00")

# # A possible needed change, with 2 possible desired interface
# c = Players(Season="1999-00", header={"Referer": "https://www.another-website.com/"})
# c = Players(Season="1999-00").header(Referer="https://www.another-website.com/")

# # Final outputs
# c.request_data().to_csv("downloads/my_data.csv")
# c.request_data().to_sql("table-name")


# # print(dir(c))
# print(c.get_http_header())
# c = Players(header={"Accept": "NewValue"})

# print(c.encode_api_params())
# print(dir(c))
# print(c.get_http_header())
