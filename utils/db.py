import os
from mongoengine import connect, Document, StringField
from dotenv import load_dotenv
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")


class Games(Document):
    localTeam = StringField()
    visitantTeam = StringField()
    localTeamImg = StringField()
    visitantTeamImg = StringField()
    result = StringField()
    league = StringField()
    status = StringField()
    info = StringField()


def save_db(games):
    connect("test", host=MONGO_URL)
    Games.objects().delete()

    for game in games:
        new_game = Games(**game)
        new_game.save()
