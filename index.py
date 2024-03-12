class Game:
    """
    Represents an instance of a game.
    """
    def __init__(self, team, match_up, game_date, outcome, minutes, points, fgm, fga, fg_percentage,
                 three_pm, three_pa, three_p_percentage, ftm, fta, ft_percentage, oreb, dreb, reb,
                 assists, steals, blocks, turnovers, personal_fouls, plus_minus):
        self.team = team
        self.match_up = match_up
        self.game_date = game_date
        self.outcome = outcome
        self.minutes = minutes
        self.points = points
        self.fgm = fgm
        self.fga = fga
        self.fg_percentage = fg_percentage
        self.three_pm = three_pm
        self.three_pa = three_pa
        self.three_p_percentage = three_p_percentage
        self.ftm = ftm
        self.fta = fta
        self.ft_percentage = ft_percentage
        self.oreb = oreb
        self.dreb = dreb
        self.reb = reb
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.personal_fouls = personal_fouls
        self.plus_minus = plus_minus


games_dict = {}

with open("data.csv", "r") as file:
    file.readline()

    for line in file:
        fields = line.strip().split(',')

        game_id = len(games_dict) + 1

        game = Game(team=fields[0], match_up=fields[1], game_date=fields[2], outcome=fields[3],
                    minutes=int(fields[4]), points=int(fields[5]), fgm=int(fields[6]), fga=int(fields[7]),
                    fg_percentage=float(fields[8]), three_pm=int(fields[9]), three_pa=int(fields[10]),
                    three_p_percentage=float(fields[11]), ftm=int(fields[12]), fta=float(fields[13]),
                    ft_percentage=float(fields[14]), oreb=int(fields[15]), dreb=int(fields[16]),
                    reb=int(fields[17]), assists=int(fields[18]), steals=int(fields[19]),
                    blocks=int(fields[20]), turnovers=int(fields[21]), personal_fouls=int(fields[22]),
                    plus_minus=int(fields[23]))

        games_dict[game_id] = game
