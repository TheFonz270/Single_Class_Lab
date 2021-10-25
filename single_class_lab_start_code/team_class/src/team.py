class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
    
    def add_player(self, new_player):
        self.players.append(new_player)
    
    def has_player(self, player_search):
        if player_search in self.players:
            return True 
        else:
            return False