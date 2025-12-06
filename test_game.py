from game import Game

def test_create_new_game():

    game = Game()
    assert isinstance(game, Game)
