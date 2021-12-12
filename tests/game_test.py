import unittest
from chess import Game, Board, HumanPlayer, ComPlayer

game = Game()
w_player = HumanPlayer(True, 'w')
b_player = HumanPlayer(False, 'b')


class ConstructionTestCase(unittest.TestCase):
    def test_board_attr_is_board_instance(self):
        self.assertTrue(isinstance(game._board, Board))

    def test_w_player_is_none(self):
        self.assertIsNone(game._w_player)

    def test_b_player_is_none(self):
        self.assertIsNone(game._b_player)


class GetterTestCase(unittest.TestCase):
    game._w_player, game._b_player = w_player, b_player

    def test_can_get_active_player(self):
        game._board._white_to_move = True
        self.assertIs(game._active_player, w_player)

    def test_can_get_inactive_player(self):
        game._board._white_to_move = True
        self.assertIs(game._inactive_player, b_player)

    def test_active_player_is_b_player_when_black_to_move(self):
        game._board._white_to_move = False
        self.assertIs(game._active_player, b_player)

    def test_inactive_player_is_w_player_when_black_to_move(self):
        game._board._white_to_move = False
        self.assertIs(game._inactive_player, w_player)


class CreatePlayerTestCase(unittest.TestCase):
    def test_w_player_is_white_and_b_player_is_black_after_initialization(self):
        # input irrelevant
        game._init_players()
        self.assertTrue(game._w_player.white)
        self.assertFalse(game._b_player.white)

    def test_can_create_white_player(self):
        # input1: y
        player = Game._create_player('white')
        self.assertTrue(player._white)

    def test_can_create_black_player(self):
        # input1: y
        player = Game._create_player('black')
        self.assertFalse(player._white)

    def test_can_create_human_player(self):
        # input1: y
        player = Game._create_player('white')
        self.assertTrue(isinstance(player, HumanPlayer))

    def test_can_create_com_player(self):
        # input1: n
        player = Game._create_player('white')
        self.assertTrue(isinstance(player, ComPlayer))


if __name__ == '__main__':
    unittest.main()
