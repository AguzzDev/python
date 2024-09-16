from utils.getRandomPlayer import getRandomPlayer
from utils.dictionarys import leagueDictionary, difficultDictionary
from utils.inputs import input_question, input_options

"""
Guess the Player
You have five attempts to guess the player. Good Luck!
"""

POINTS = 0


def Game():
    """Game Logic"""
    global answer
    global POINTS
    answer = False

    league = input_options(
        text=f"Bienvenido al juego, elegi la liga:\n1: Premier League\n2: LaLiga\n3: Serie A\n4: Liga Profesional de Fútbol\n5: Eredivisie\n6: Ligue 1\n7: Bundesliga\n$: ", limit=7)
    print(f"Seleccionaste {leagueDictionary[league]}")
    difficult = input_options(
        text=f"Selecciona la dificultad:\n1: Facil\n2: Intermedio\n3: Dificil\n$: ", limit=3)
    print(f"Seleccionaste {difficultDictionary[difficult]}")

    player = getRandomPlayer(league, difficult)

    for attempt in range(1, 6):

        input_question(attempt, player)

        if answer:
            POINTS += 5-attempt
            print(f"Ganaste, el jugador era {
                  player['name']}, tienes {POINTS} puntos")
            break

    else:
        print(f"Perdiste, el jugador era: {
              player["name"]}, tienes {POINTS} puntos")

    play_again = input("Quieres jugar de nuevo? (s/n)\n$ ").strip().lower()
    if play_again == "s":
        Game()
    else:
        print("Gracias por jugar.")


Game()
