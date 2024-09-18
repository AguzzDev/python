from bs4 import BeautifulSoup
import requests
from utils.dictionarys import matchesFilterDictionary

BASE_URL = "https://www.transfermarkt.es/ticker/index/live"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def main():
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code != 200:
        return "Error"

    html = BeautifulSoup(response.text, 'html.parser')

    league_and_position = []
    end_games = "\n---Partidos terminados---\n"
    next_games = "\n---Proximos partidos---\n"
    live_games = "\n---Partidos en vivo---\n"

    all_leagues_or_competition = html.select(
        "#spieltagsbox div[class='kategorie']")
    for i in range(len(all_leagues_or_competition)):
        find = all_leagues_or_competition[i]

        title = find.select_one("h2 a").text

        if title in matchesFilterDictionary:
            league_and_position.append({"pos": i, "title": title})

    tables = html.select("table.livescore")

    for item in league_and_position:
        league = item.get("title")
        pos = item.get("pos")
        table = tables[pos]
        rows = table.find("tbody").find_all("tr")
        i = 0

        for row in rows:
            local_team = row.select_one("td:nth-child(3) a").text.strip()
            visitant_team = row.select_one("td:nth-child(5) a").text.strip()
            result = row.select_one(
                "td:nth-child(4) a span")

            league_text = f"\n{league}\n"
            match_text = f"{local_team} - {result.text} - {visitant_team}\n"

            if "liveresult" in result.get("class", []):
                if i == 0:
                    live_games += league_text

                live_games += match_text
            elif "finished" in result.get("class", []):
                if i == 0:
                    end_games += league_text

                end_games += match_text
            else:
                if i == 0:
                    next_games += league_text

                next_games += match_text

            i += 1

    return f"{live_games}{end_games}{next_games}"


print(main())
