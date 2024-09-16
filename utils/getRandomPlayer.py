import random

from data.players_data import PLAYERS
from utils.dictionarys import leagueDictionary


def parse_market_value(value):
    if value is None or "null" in value.lower() or value.split()[1] != "mill.":
        return 0

    return int(value.split()[0].split(",")[0])


def getRandomPlayer(league, difficult):

    if difficult == "1":
        min_value = 50
        max_value = 100000
    elif difficult == "2":
        min_value = 25
        max_value = 50
    else:
        min_value = 10
        max_value = 25

    players_filtered = list(
        filter(lambda player: player.get("league") == leagueDictionary[league]
               and min_value < parse_market_value(player.get("marketValue")) < max_value, PLAYERS)
    )

    return random.choice(players_filtered)
