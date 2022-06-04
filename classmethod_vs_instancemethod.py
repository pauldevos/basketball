from abc import ABC


class CommonallPlayers:

    __class_dict__ = {}

    def __init__(
        self,
        IsOnlyCurrentSeason=0,
        LeagueID="00",
        Season="2021-22",
        headers = None) -> None:
        
        self.IsOnlyCurrentSeason = IsOnlyCurrentSeason
        self.LeagueID = LeagueID
        self.Season = Season

    @classmethod
    def return_class_attributes(cls):
        return cls
    
    

c = CommonallPlayers()

print(c.return_class_attributes().__dict__)

d = CommonallPlayers(Season='1999-00')

print(d.return_class_attributes())
