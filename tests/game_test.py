import unittest
from chess import Game, Board, HumanPlayer, ComPlayer

game = Game()
w_player = HumanPlayer(True, 'w')
b_player = HumanPlayer(False, 'b')


class ConstructionTestCase(unittest.TestCase):
    game = Game()

    def test_board_attr_is_board_instance(self):
        self.assertTrue(isinstance(self.game._board, Board))

    def test_w_player_is_none(self):
        self.assertIsNone(self.game._w_player)

    def test_b_player_is_none(self):
        self.assertIsNone(self.game._b_player)


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


# class CreatePlayerTestCase(unittest.TestCase):
#     def test_w_player_is_white_and_b_player_is_black_after_initialization(self):
#         # input irrelevant
#         game._init_players()
#         self.assertTrue(game._w_player.white)
#         self.assertFalse(game._b_player.white)
#
#     def test_can_create_white_player(self):
#         # input1: y
#         player = Game._create_player('white')
#         self.assertTrue(player._white)
#
#     def test_can_create_black_player(self):
#         # input1: y
#         player = Game._create_player('black')
#         self.assertFalse(player._white)
#
#     def test_can_create_human_player(self):
#         # input1: y
#         player = Game._create_player('white')
#         self.assertTrue(isinstance(player, HumanPlayer))
#
#     def test_can_create_com_player(self):
#         # input1: n
#         player = Game._create_player('white')
#         self.assertTrue(isinstance(player, ComPlayer))


class SetBoardTestCase(unittest.TestCase):
    def test_can_set_starting_position(self):
        _game = Game()
        _game._set_board('k7/8/8/8/P7/8/8/K7 b Kq b3 1 2')
        for piece_data in [{'pos': 56, 'symbol': 'k'}, {'pos': 0, 'symbol': 'K'}, {'pos': 24, 'symbol': 'P'}]:
            piece = _game._board._get_piece(piece_data['pos'])
            self.assertEqual(piece_data['symbol'], piece._fen_symbol)
        self.assertFalse(_game._board._white_to_move)
        self.assertEqual([True, False, False, True], _game._board._castling_rights)
        self.assertEqual(17, _game._board._ep_target_square)
        self.assertEqual(1, _game._board._half_move_clock)
        self.assertEqual(2, _game._board._turn_number)

    def test_can_set_any_starting_position(self):
        _game = Game()
        _game._set_board('kr6/8/8/8/8/8/8/7K w - - 0 1')
        for piece_data in [{'pos': 56, 'symbol': 'k'}, {'pos': 57, 'symbol': 'r'}, {'pos': 7, 'symbol': 'K'}]:
            piece = _game._board._get_piece(piece_data['pos'])
            self.assertEqual(piece_data['symbol'], piece._fen_symbol)
        self.assertTrue(_game._board._white_to_move)
        self.assertEqual([False, False, False, False], _game._board._castling_rights)
        self.assertIsNone(_game._board._ep_target_square)
        self.assertEqual(0, _game._board._half_move_clock)
        self.assertEqual(1, _game._board._turn_number)


class GameOverTestCase(unittest.TestCase):
    def test_game_is_not_over_when_it_is_not_over(self):
        self.assertFalse(game.game_over())

    def test_game_is_over_when_active_player_is_in_checkmate(self):
        _game = Game()
        _game._set_board('k7/8/8/8/8/2b5/1q6/K7 w - - 0 1')
        self.assertTrue(_game.game_over())

    def test_game_is_over_when_active_player_is_in_stalemate(self):
        _game = Game()
        _game._set_board('k7/8/8/8/8/2b5/1r6/K7 w - - 0 1')
        self.assertTrue(_game.game_over())


if __name__ == '__main__':
    unittest.main()
