from urllib import request
from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self._url = url
        self.response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

        self.players = []

        for player_dict in self.response:
            player = Player(
                player_dict['name'], player_dict['nationality'], player_dict['assists'], player_dict['goals'], player_dict['penalties'], player_dict['team'], player_dict['games'], (player_dict['goals'] + player_dict['assists'])
            )

            self.players.append(player)

    def getPlayers(self):
        return self.players

    def printPlayers(self):
        print("Oliot:")

        for player in self.players:
            print(player)

    