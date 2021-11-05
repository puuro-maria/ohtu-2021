import unittest
from statistics import Statistics
from player_reader import PlayerReader
from player import Player

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics(PlayerReader("https://nhlstatisticsforohtu.herokuapp.com/players.txt"))

    def test_search_works(self):
        self.player = self.stats.search("Mikko Rantanen")
        self.assertEqual(self.player.__str__(), "Mikko Rantanen COL 30 + 36 = 66")

    def test_team_works(self):
        self.team = self.stats.team("BOS")
        self.leng = len(self.team)-1
        self.assertEqual(self.team[0].team, self.team[self.leng].team, "BOS")