import time
import pytz
from datetime import datetime
from utils.list_filtered import list_filtered
from utils.doProcess import doProcess

spain_tz = pytz.timezone('Europe/Madrid')

while True:
    games = doProcess(True)
    live_games = list_filtered(l=games, text="status", condition="live")
    next_games = list_filtered(l=games, text="status", condition="next")

    if live_games:
        doProcess()
        time.sleep(150)
    elif next_games:
        next_game_time_str = next_games[-1]["result"]
        current_time_str = datetime.now(spain_tz).strftime("%H:%M")

        next_game_time = datetime.strptime(next_game_time_str, "%H:%M")
        current_time = datetime.strptime(current_time_str, "%H:%M")

        if current_time >= next_game_time:
            doProcess()
        else:
            time_diff = (next_game_time - current_time).total_seconds()
            sleep = max(time_diff, 0)
            print(f"Falta {round(sleep/60)} minutos para el proximo partido")
            time.sleep(sleep)

    else:
        print("No hay partidos, vuelvo en 6h")
        time.sleep(6*60*60)
