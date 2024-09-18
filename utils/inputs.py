from utils.transformCharacter import transform_characters


def input_options(text, limit):
    options = [str(i+1) for i in range(limit)]

    while True:
        output = input(text)

        if output in options:
            return output


def input_question(i, player):
    global answer

    dictionary = {
        "1": f"El jugador es de: {player["country"]}\n$ ",
        "2": f"El jugador juega en la posicion: {player["position"]}\n$ ",
        "3": f"El jugador juega en el club: {player["team"]}\n$ ",
        "4": f"El jugador tiene un valor de mercado: {player["marketValue"]}\n$ ",
        "5": f"El jugador lleva el numero: {player["number"]}\n$ "
    }

    text = dictionary[str(i)]
    output = input(text).lower()
    player = transform_characters(player["name"].lower())
    player_parts = player.split()
    answer = output == player or output == player_parts[-1] or output == player_parts[-2:]
