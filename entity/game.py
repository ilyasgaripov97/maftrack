class Slot:

    def __init__(self, player, n):
        self.player = player
        self.n = n


class Game:

    def __init__(self, players):
        self.slots = []
        self.winner = None
    
    def assign_roles(self):
        ...
    
    def shuffle_player_positions(self):
        ...
    
    def nominate(self, num):
        ...

    def kill(self, num):
        ...

    def disqualify(self, num):
        ...