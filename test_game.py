from game import Game, Player


def test_create_new_game():
    game = Game()
    assert isinstance(game, Game)


def test_new_player():
    nickname = 'Bit'
    player = Player(nickname) 
    assert isinstance(player, Player)
    assert player.nickname == nickname