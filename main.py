import os
import requests
from dotenv import load_dotenv
from utils.inputs import input_options
from utils.dictionaries import place_dict, icon_dict
from utils.haversine import haversine
load_dotenv()
MAPBOX_ACCESS_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")


def ip_locate():
    response = requests.get("https://ipinfo.io")
    data = response.json()

    if response.status_code == 200:
        locate = data.get("loc")
        return locate.split(",")
    else:
        return None


def search_place(lat, lon, place_type):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{
        place_type}.json?proximity={lon},{lat}&access_token={MAPBOX_ACCESS_TOKEN}&limit=10"
    response = requests.get(url)
    places = response.json().get("features")

    place_list = []

    if response.status_code == 200:
        for place in places:
            lon2, lat2 = place["center"]
            distance = float(f"{haversine(lat, lon, lat2, lon2):.2f}")

            place_list.append({"icon": icon_dict.get(place_type), "text": place['text'], "address":
                               place["properties"].get("address", "Sin direccion"), "distance": distance})

        place_list = sorted(
            filter(lambda x: x["distance"] < 10, place_list),
            key=lambda x: x["distance"]
        )
        return {"error": False, "data": place_list}

    else:
        return {"error": True}


def main():
    print("🌎 Obteniendo tu ubicacion...")
    ip = ip_locate()

    if not ip:
        print("Hubo un error obteniendo tu ubicacion")
        return

    lat, lon = ip
    search = input_options(
        (
            "🔎  Que quieres buscar?\n"
            "- 1 Parques\n"
            "- 2 Restaurantes\n"
            "- 3 Cafe\n"
            "- 4 Hoteles\n"
            "- 5 Hospital\n"
            "- 6 Shopping\n"
            "- 7 Estaciones de servicio\n"
            "- 8 Museos\n"
            "- 9 Supermercados\n"
            "- 10 Cines\n"
            "$: "
        ),
        limit=10
    )

    res = search_place(float(lat), float(
        lon), place_type=place_dict.get(search))

    if res.get("error") is not True:
        print("")
        for item in res.get("data"):
            print(f"{item['icon']} {item['text']}, {
                item["address"]} a {item["distance"]} km")

        more = input("\nQuieres algo mas? (s/n)\n$: ")
        if more == "s":
            main()

    else:
        print("Error")
        return


main()
