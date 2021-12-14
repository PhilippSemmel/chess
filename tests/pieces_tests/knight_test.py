import unittest
from board import Knight, Piece, Board


board = Board()
knight1 = Knight(35, True, board)
knight2 = Knight(21, False, board)


class ConstructionTestCase(unittest.TestCase):
    def test_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Knight, Piece))

    def test_base_val_is_correct(self):
        self.assertEqual(320, knight1._base_val)

    def test_base_val_is_always_correct(self):
        self.assertEqual(320, knight2._base_val)

    def test_pos_val_mod_is_correct_as_white(self):
        self.assertEqual((-50, -40, -30, -30, -30, -30, -40, -50, -40, -20, 0, 5, 5, 0, -20, -40, -30, 5, 10, 15, 15,
                          10, 5, -30, -30, 0, 15, 20, 20, 15, 0, -30, -30, 5, 15, 20, 20, 15, 5, -30, -30, 0, 10, 15,
                          15, 10, 0, -30, -40, -20, 0, 0, 0, 0, -20, -40, -50, -40,- 30, -30, -30, -30, -40, -50),
                         knight1._pos_val_mod[True])

    def test_pos_val_mod_is_correct_as_black(self):
        self.assertEqual((-50, -40, -30, -30, -30, -30, -40, -50, -40, -20, 0, 0, 0, 0, -20, -40, -30, 0, 10, 15, 15,
                          10, 0, -30, -30, 5, 15, 20, 20, 15, 5, -30, -30, 0, 15, 20, 20, 15, 0, -30, -30, 5, 10, 15,
                          15, 10, 5, -30, -40, -20, 0, 5, 5, 0, -20, -40, -50, -40, -30, -30, -30, -30, -40, -50),
                         knight2._pos_val_mod[False])

    def test_pos_is_given_value(self):
        self.assertEqual(35, knight1._pos)

    def test_pos_is_any_given_value(self):
        self.assertEqual(21, knight2._pos)

    def test_color_is_given_value(self):
        self.assertTrue(knight1._white_piece)

    def test_color_is_any_given_value(self):
        self.assertFalse(knight2._white_piece)

    def test_capture_data_is_none(self):
        self.assertIsNone(knight1._capture_data)

    def test_capture_data_is_always_none(self):
        self.assertIsNone(knight2._capture_data)


class MoveGenerationTestCase(unittest.TestCase):
    # general
    def test_cannot_move_when_blocked_by_own_pieces(self):
        knight = Board('8/8/2P1P3/1P3P2/3N4/1P3P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual(set(), knight.pseudo_legal_moves)

    def test_can_make_multiple_jumps(self):
        knight = Board('8/8/5p1P/8/6N1/4p3/5P2/8 w - - 0 1')._get_piece(30)
        self.assertEqual({(30, 45), (30, 36), (30, 20), (30, 15)}, knight.pseudo_legal_moves)

    def test_attacking_squares_equal_pseudo_legal_move_target_squares(self):
        knight = Board('8/8/5p1P/8/6N1/4p3/5P2/8 w - - 0 1')._get_piece(30)
        self.assertEqual({45, 36, 20, 15}, knight.attacking_squares)

    # first direction goes two squares; second one one square
    # jumps in every direction
    def test_can_jump_up_right_if_square_is_empty(self):
        knight = Board('8/8/2P5/1P3P2/3N4/1P3P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 44)}, knight.pseudo_legal_moves)

    def test_can_jump_up_right_if_opponent_on_square(self):
        knight = Board('8/8/2P1p3/1P3P2/3N4/1P3P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 44)}, knight.pseudo_legal_moves)

    def test_can_jump_right_up_if_square_is_empty(self):
        knight = Board('8/8/2P1P3/1P6/3N4/1P3P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 37)}, knight.pseudo_legal_moves)

    def test_can_jump_right_up_if_opponent_on_square(self):
        knight = Board('8/8/2P1P3/1P3p2/3N4/1P3P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 37)}, knight.pseudo_legal_moves)

    def test_can_jump_right_down_if_square_is_empty(self):
        knight = Board('8/8/2P1P3/1P3P2/3N4/1P6/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 21)}, knight.pseudo_legal_moves)

    def test_can_jump_right_down_if_opponent_on_square(self):
        knight = Board('8/8/2P1P3/1P3P2/3N4/1P3p2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 21)}, knight.pseudo_legal_moves)

    def test_can_jump_down_right_if_square_is_empty(self):
        knight = Board('8/8/2P1P3/1P3P2/3N4/1P3P2/2P5/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 12)}, knight.pseudo_legal_moves)

    def test_can_jump_down_right_if_opponent_on_square(self):
        knight = Board('8/8/2P1P3/1P3P2/3N4/1P3P2/2P1p3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 12)}, knight.pseudo_legal_moves)

    def test_can_jump_down_left_if_square_is_empty(self):
        knight = Board('8/8/2P1P3/1P3P2/3N4/1P3P2/4P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 10)}, knight.pseudo_legal_moves)

    def test_can_jump_down_left_if_opponent_on_square(self):
        knight = Board('8/8/2P1P3/1P3P2/3N4/1P3P2/2p1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 10)}, knight.pseudo_legal_moves)

    def test_can_jump_left_down_if_square_is_empty(self):
        knight = Board('8/8/2P1P3/1P3P2/3N4/5P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 17)}, knight.pseudo_legal_moves)

    def test_can_jump_left_down_if_opponent_on_square(self):
        knight = Board('8/8/2P1P3/1P3P2/3N4/1p3P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 17)}, knight.pseudo_legal_moves)

    def test_can_jump_left_up_if_square_is_empty(self):
        knight = Board('8/8/2P1P3/5P2/3N4/1P3P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 33)}, knight.pseudo_legal_moves)

    def test_can_jump_left_up_if_opponent_on_square(self):
        knight = Board('8/8/2P1P3/1p3P2/3N4/1P3P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 33)}, knight.pseudo_legal_moves)

    def test_can_jump_up_left_if_square_is_empty(self):
        knight = Board('8/8/4P3/1P3P2/3N4/1P3P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 42)}, knight.pseudo_legal_moves)

    def test_can_jump_up_left_if_opponent_on_square(self):
        knight = Board('8/8/2p1P3/1P3P2/3N4/1P3P2/2P1P3/8 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 42)}, knight.pseudo_legal_moves)

    # cannot jump beyond the board
    def test_cannot_jump_beyond_the_board_up_right(self):
        knight = Board('P3P3/2N5/P3P3/1P1P4/8/8/8/8 w - - 0 1')._get_piece(50)
        self.assertEqual(set(), knight.pseudo_legal_moves)

    def test_cannot_jump_beyond_the_board_up_left(self):
        knight = Board('P3P3/2N5/P3P3/1P1P4/8/8/8/8 w - - 0 1')._get_piece(50)
        self.assertEqual(set(), knight.pseudo_legal_moves)

    def test_cannot_jump_beyond_the_board_left_up(self):
        knight = Board('8/8/P1P5/3P4/1N6/3P4/P1P5/8 w - - 0 1')._get_piece(25)
        self.assertEqual(set(), knight.pseudo_legal_moves)

    def test_cannot_jump_beyond_the_board_left_down(self):
        knight = Board('8/8/P1P5/3P4/1N6/3P4/P1P5/8 w - - 0 1')._get_piece(25)
        self.assertEqual(set(), knight.pseudo_legal_moves)

    def test_cannot_jump_beyond_the_board_down_right(self):
        knight = Board('8/8/8/8/1P1P4/P3P3/2N5/P3P3 w - - 0 1')._get_piece(10)
        self.assertEqual(set(), knight.pseudo_legal_moves)

    def test_cannot_jump_beyond_the_board_down_left(self):
        knight = Board('8/8/8/8/1P1P4/P3P3/2N5/P3P3 w - - 0 1')._get_piece(10)
        self.assertEqual(set(), knight.pseudo_legal_moves)

    def test_cannot_jump_beyond_the_board_right_up(self):
        knight = Board('8/8/5P1P/4P3/6N1/4P3/5P1P/8 w - - 0 1')._get_piece(30)
        self.assertEqual(set(), knight.pseudo_legal_moves)

    def test_cannot_jump_beyond_the_board_right_down(self):
        knight = Board('8/8/5P1P/4P3/6N1/4P3/5P1P/8 w - - 0 1')._get_piece(30)
        self.assertEqual(set(), knight.pseudo_legal_moves)


class PositionValueTestCase(unittest.TestCase):
    def test_can_generate_pos_value_as_white(self):
        for n, mod in enumerate((-50, -40, -30, -30, -30, -30, -40, -50, -40, -20, 0, 5, 5, 0, -20, -40, -30, 5, 10, 15,
                                 15, 10, 5, -30, -30, 0, 15, 20, 20, 15, 0, -30, -30, 5, 15, 20, 20, 15, 5, -30, -30, 0,
                                 10, 15, 15, 10, 0, -30, -40, -20, 0, 0, 0, 0, -20, -40, -50, -40,- 30, -30, -30, -30,
                                 -40, -50)):
            knight1.move_to(n)
            self.assertEqual(Knight._base_val + mod, knight1.pos_val)

    def test_can_generate_pos_value_as_black(self):
        for n, mod in enumerate((-50, -40, -30, -30, -30, -30, -40, -50, -40, -20, 0, 0, 0, 0, -20, -40, -30, 0, 10, 15,
                                 15, 10, 0, -30, -30, 5, 15, 20, 20, 15, 5, -30, -30, 0, 15, 20, 20, 15, 0, -30, -30, 5,
                                 10, 15, 15, 10, 5, -30, -40, -20, 0, 5, 5, 0, -20, -40, -50, -40, -30, -30, -30, -30,
                                 -40, -50)):
            knight2.move_to(n)
            self.assertEqual(Knight._base_val + mod, knight2.pos_val)


def main() -> None:
    unittest.main()


if __name__ == '__main__':
    main()
