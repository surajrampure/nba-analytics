class Team:
    def __init__(self, year, conf, dict):
        self.year = year
        self.conf = conf
        self.name = dict['name']
        self.seed = dict['seed']
        self.wins = dict['wins']
        self.losses = dict['losses']
        self.win_percentage = self.win_pct = dict['win_percentage']
        self.games_behind = dict['games_behind']
        self.points_per_game = self.ppg = dict['points_per_game']
        self.opp_points_per_game = self.oppg = dict['opp_points_per_game']
        self.srs = dict['srs']

    def __str__(self):
        return str(self.year) + " " + self.name + ": " + str(self.wins) + "-" + str(self.losses)

    def __repr__(self): return str(self)