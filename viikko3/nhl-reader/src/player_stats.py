from player_reader import PlayerReader

class Statistics:
    def __init__(self, reader):
        self.reader = reader

        self.players = reader.getPlayers()

    def printPlayersByNationality(self, nationality):

        print("Players in " + nationality)

        natPlayers = []

        for player in self.players:
            if player.getNationality() == nationality:
                natPlayers.append(player)
        
        natPlayers.sort(key = lambda p : p.getPoints(), reverse=True)
        
        for player in natPlayers:
            print(player)