import unittest
from statistics import Statistics
from player_reader import PlayerReader
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics(PlayerReaderStub())

    def test_search_works(self):
        self.player = self.stats.search("Semenko")
        self.assertEqual(self.player.__str__(), "Semenko EDM 4 + 12 = 16")
        self.playerTwo = self.stats.search("Kuukkeli")

    def test_team_works(self):
        self.team = self.stats.team("EDM")
        self.leng = len(self.team)-1
        self.assertEqual(self.team[0].team, self.team[self.leng].team, "EDM")

    def test_top_scorers_works(self):
        self.topTwo = self.stats.top_scorers(2)
        self.assertEqual(self.topTwo[0], self.stats.search("Gretzky"))
        self.assertEqual(self.topTwo[1], self.stats.search("Lemieux"))