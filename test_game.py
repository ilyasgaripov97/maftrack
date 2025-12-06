from game import Game, Player


def test_create_new_game():
    game = Game(
        [
            Player("A"),
            Player("B"),
            Player("C"),
            Player("D"),
            Player("E"),
            Player("F"),
            Player("G"),
            Player("H"),
            Player("I"),
            Player("J"),
        ]
    )
    assert isinstance(game, Game)

    for player in game.players:
        assert isinstance(player, Player)

    assert len(game.players) == 10


def test_new_player():
    nickname = "Bit"
    player = Player(nickname)
    assert isinstance(player, Player)
    assert player.nickname == nickname
