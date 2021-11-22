class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games, points):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.penalties = penalties
        self.goals = goals
        self.team = team
        self.games = games
        self.points = points
    
    def getNationality(self):
        return self.nationality

    def getPoints(self):
        return self.points

    def __str__(self):
        return f"{self.name:20}" + self.team + " " + f"{str(self.goals):2}" + " + " + f"{str(self.assists):2}" + " + " + f"{str(self.goals + self.assists):2}"
