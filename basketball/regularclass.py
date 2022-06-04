from dataclasses import dataclass

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


class StatsHTTPHeader:
    base_url = "https://stats.nba.com/stats/"
    http_headers = HTTP_HEADERS


class CommonallPlayers(StatsHTTPHeader):

    __endpoint__ = "CommonallPlayers"

    def __init__(
        self,
        IsOnlyCurrentSeason=0,
        LeagueID="00",
        Season="2021-22",
        headers = None
    ) -> None:
        self.headers = headers if headers else HTTP_HEADERS
        # self.api_params["IsOnlyCurrentSeason"] = IsOnlyCurrentSeason
        # self.api_params["LeagueID"] = LeagueID
        # self.api_params["Season"] = Season
        self.IsOnlyCurrentSeason = IsOnlyCurrentSeason
        self.LeagueID = LeagueID
        self.Season = Season
        
    def api_params(self):
        return {"IsOnlyCurrentSeason": self.IsOnlyCurrentSeason,
                "LeagueID": self.LeagueID,
                "Season": self.Season}

    # ideally this is NOT instantiated (as doesn't have data, shouldn't be accessible to user until AFTER request)
    def request_data(self):
        url_api = f"{self.base_url}/{self.__endpoint__}"
        return url_api # requests.get(url_api, params=self.params, headers=self.headers)


c = CommonallPlayers(Season="1950-51")  # create with default values
# c.headers["my_new_header"] = "whatever"  # members are public
# c.api_params["my_new_param"] = "new_param"  # members are public
print(c)
# res = c.request_data()
print(c.api_params())

# print(c.headers['Accept'] = "NEW VALUE!!!")
