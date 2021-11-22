from player import Player
from player_reader import PlayerReader
from player_stats import Statistics

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    stats.printPlayersByNationality("FIN")
    reader.printPlayers()

if __name__ == "__main__":
    main()
