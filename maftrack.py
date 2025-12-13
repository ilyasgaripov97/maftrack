"""
Docstring for maftrack

Judge:
  - creates a new game, 10 slots for each player
  - assign player positions and game roles
  - save game turns and results
  - kick players
  
Player:
  - nominate another players
  - vote player
  - kill (mafia/don only)
  - check player role (sheriff only)
  - check sheriff (don only)
  - outcry
  - use 2 outcries for extended speech time


Game phases:  
  * DAY/NIGHT - has index (starting from zero, excluding discussion night)

  NIGHT (MAFIA DISCUSS) nothing

  DAY

  each player start a speach (1 min, can use two outcries for extended 30 seconds)

  nominated[]   nominated players list for this day
  votes[]       who votes whom 

  if number of votes the same, these players speak again, then voted again

  NIGHT

  kill if all mafia players are shoot same number or miss if different numbers or don't shoot
  
"""

from enum import Enum
from random import randrange


class Role(Enum):
    CIVILIAN = 1
    SHERIFF = 2
    MAFIA = 3
    DON = 4


class Player:

    def __init__(self, nickname):
        self.nickname = nickname

    def __repr__(self):
        return self.nickname


class Slot:

    def __init__(self, n, player, role):
        self.n = n
        self.player = player
        self.role = role

    def __repr__(self):
        return f"<'player: {self.player.nickname}', role: {self.role}>"


class Game:

    def __init__(self):
        self.slots = {}
        self.available_roles = [
            Role.CIVILIAN, Role.CIVILIAN, Role.CIVILIAN, Role.CIVILIAN, Role.CIVILIAN, Role.CIVILIAN,
            Role.SHERIFF,
            Role.MAFIA, Role.MAFIA,
            Role.DON
        ]

    def assign_role(self, n, nickname, role):
        if self.slots.get(n):
            return
        
        self.slots[n] = Player(nickname), role

    def assign_roles(self, nicknames):
        for n, nickname in enumerate(nicknames, start=1):
            if not self.available_roles:
                return
            
            self.assign_role(n, nickname, self.available_roles.pop(randrange(len(self.available_roles))))


g = Game()
g.assign_roles(['Bit', 'Dron', 'Arwen', 'Narogami', 'Infinity', 'Bambl', 'Star', 'Ludovig', 'Gena', 'Schaslivchik'])

print(g.slots)