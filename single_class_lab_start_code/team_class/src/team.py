class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0 
    
    def add_player(self, new_player):
        self.players.append(new_player)
    
    def has_player(self, player_search):
        if player_search in self.players:
            return True 
        else:
            return False
    
    def play_game(self, play_game):
        if play_game == True:
            self.points += 3
        else:
            self.points = 0