from pprint import pprint


class Player:

    def __init__(self, nickname):
        self.nickname = nickname


class Slot:

    def __init__(self, player = None, role = None):
        self.player = player
        self.role = role

    def __repr__(self):
        return f"{self.player} ({self.role})"


class Game:

    def __init__(self):
        self.slots = [Slot() for s in range(10)]

        

g = Game()
pprint(g.slots)