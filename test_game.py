from game import Game, Player


def test_create_new_game():
    game = Game()
    assert isinstance(game, Game)


def test_new_player():
    player = Player() 
    assert isinstance(player, Player)
