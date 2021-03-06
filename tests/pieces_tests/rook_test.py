import unittest

from board import Rook, Piece, Board

board = Board()
rook1 = Rook(35, True, board)
rook2 = Rook(21, False, board)


class ConstructionTestCase(unittest.TestCase):
    def test_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Rook, Piece))

    def test_base_val_is_correct(self):
        self.assertEqual(500, rook1._BASE_VAL)

    def test_base_val_is_always_correct(self):
        self.assertEqual(500, rook2._BASE_VAL)

    def test_pos_val_mod_is_correct_as_white(self):
        self.assertEqual((0, 0, 0, 5, 5, 0, 0, 0, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0,
                          0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, 5, 10, 10, 10, 10, 10, 10, 5, 0, 0,
                          0, 0, 0, 0, 0, 0), rook1._POS_VAL_MOD[True])

    def test_pos_val_mod_is_correct_as_black(self):
        self.assertEqual((0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 10, 10, 10, 10, 10, 5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0,
                          0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, 0,
                          0, 0, 5, 5, 0, 0, 0), rook2._POS_VAL_MOD[False])

    def test_pos_is_given_value(self):
        self.assertEqual(35, rook1._pos)

    def test_pos_is_any_given_value(self):
        self.assertEqual(21, rook2._pos)

    def test_color_is_given_value(self):
        self.assertTrue(rook1._white_piece)

    def test_color_is_any_given_value(self):
        self.assertFalse(rook2._white_piece)

    def test_capture_data_is_none(self):
        self.assertIsNone(rook1._capture_info)

    def test_capture_data_is_always_none(self):
        self.assertIsNone(rook2._capture_info)


class MoveGenerationTestCase(unittest.TestCase):
    # general
    def test_cannot_move_when_blocked_by_own_pieces(self):
        rook = Board('8/8/2PPP3/2PRP3/2PPP3/8/8/K7 w - - 0 1')._get_piece(35)
        self.assertEqual(set(), rook.pseudo_legal_moves)

    def test_can_move_in_multiple_directions(self):
        rook = Board('K7/1p6/8/5P2/1p2R2P/4P3/8/1P6 w - - 0 1')._get_piece(28)
        self.assertEqual(
            {(28, 29, None), (28, 30, None), (28, 36, None), (28, 44, None), (28, 52, None), (28, 60, None),
             (28, 27, None), (28, 26, None), (28, 25, None)},
            rook.pseudo_legal_moves)

    def test_attacking_squares_equal_pseudo_legal_move_target_squares(self):
        rook = Board('K7/1p6/8/5P2/1p2R2P/4P3/8/1P6 w - - 0 1')._get_piece(28)
        self.assertEqual({29, 30, 36, 44, 52, 60, 27, 26, 25}, rook.attacking_squares)

    # horizontal moves
    # right
    def test_can_move_one_step_right(self):
        rook = Board('K7/8/2PPP3/2PR1P2/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None)}, rook.pseudo_legal_moves)

    def test_can_move_two_steps_right(self):
        rook = Board('K7/8/2PPP3/2PR2P1/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None), (35, 37, None)}, rook.pseudo_legal_moves)

    def test_can_move_three_steps_right(self):
        rook = Board('K7/8/2PPP3/2PR3P/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None), (35, 37, None), (35, 38, None)}, rook.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right(self):
        rook = Board('K7/8/2PPP3/2PR4/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None), (35, 37, None), (35, 38, None), (35, 39, None)}, rook.pseudo_legal_moves)

    def test_can_move_from_any_position_right(self):
        rook = Board('K7/8/8/8/8/1PPP4/1PR5/1PPP4 w - - 0 1')._get_piece(10)
        self.assertEqual({(10, 11, None), (10, 12, None), (10, 13, None), (10, 14, None), (10, 15, None)},
                         rook.pseudo_legal_moves)

    def test_can_capture_one_step_right(self):
        rook = Board('K7/8/2PPP3/2PRp3/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None)}, rook.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_right(self):
        rook = Board('K7/8/2PPP3/2PR2p1/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None), (35, 37, None), (35, 38, None)}, rook.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right(self):
        rook = Board('K7/8/p1PPP3/2PR4/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None), (35, 37, None), (35, 38, None), (35, 39, None)}, rook.pseudo_legal_moves)

    # left
    def test_can_move_one_step_left(self):
        rook = Board('K7/8/4PPP1/3P1RP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None)}, rook.pseudo_legal_moves)

    def test_can_move_two_steps_left(self):
        rook = Board('K7/8/4PPP1/2P2RP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None), (37, 35, None)}, rook.pseudo_legal_moves)

    def test_can_move_three_steps_left(self):
        rook = Board('K7/8/4PPP1/1P3RP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None), (37, 35, None), (37, 34, None)}, rook.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left(self):
        rook = Board('K7/8/4PPP1/5RP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None), (37, 35, None), (37, 34, None), (37, 33, None), (37, 32, None)},
                         rook.pseudo_legal_moves)

    def test_can_move_from_any_position_left(self):
        rook = Board('K7/8/8/8/8/4PPP1/5RP1/4PPP1 w - - 0 1')._get_piece(13)
        self.assertEqual({(13, 12, None), (13, 11, None), (13, 10, None), (13, 9, None), (13, 8, None)},
                         rook.pseudo_legal_moves)

    def test_can_capture_one_step_left(self):
        rook = Board('K7/8/4PPP1/4pRP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None)}, rook.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_left(self):
        rook = Board('K7/8/4PPP1/2p2RP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None), (37, 35, None), (37, 34, None)}, rook.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left(self):
        rook = Board('K7/8/4PPPp/5RP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None), (37, 35, None), (37, 34, None), (37, 33, None), (37, 32, None)},
                         rook.pseudo_legal_moves)

    # vertical moves
    # up
    def test_can_move_one_step_up(self):
        rook = Board('K7/8/8/3P4/2P1P3/2PRP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None)}, rook.pseudo_legal_moves)

    def test_can_move_two_steps_up(self):
        rook = Board('K7/8/3P4/8/2P1P3/2PRP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None), (19, 35, None)}, rook.pseudo_legal_moves)

    def test_can_move_three_steps_up(self):
        rook = Board('K7/3P4/8/8/2P1P3/2PRP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None), (19, 35, None), (19, 43, None)}, rook.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_up(self):
        rook = Board('K7/8/8/8/2P1P3/2PRP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None), (19, 35, None), (19, 43, None), (19, 51, None), (19, 59, None)},
                         rook.pseudo_legal_moves)

    def test_can_move_from_any_position_up(self):
        rook = Board('K7/8/8/8/5P1P/5PRP/5PPP/8 w - - 0 1')._get_piece(22)
        self.assertEqual({(22, 30, None), (22, 38, None), (22, 46, None), (22, 54, None), (22, 62, None)},
                         rook.pseudo_legal_moves)

    def test_can_capture_one_step_up(self):
        rook = Board('K7/8/8/8/2PpP3/2PRP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None)}, rook.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_up(self):
        rook = Board('K7/8/3p4/8/2P1P3/2PRP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None), (19, 35, None), (19, 43, None)}, rook.pseudo_legal_moves)

    # down
    def test_can_move_one_step_down(self):
        rook = Board('K7/2PPP3/2PRP3/2P1P3/3P4/8/8/8 w - - 0 1')._get_piece(43)
        self.assertEqual({(43, 35, None)}, rook.pseudo_legal_moves)

    def test_can_move_two_steps_down(self):
        rook = Board('K7/2PPP3/2PRP3/2P1P3/8/3P4/8/8 w - - 0 1')._get_piece(43)
        self.assertEqual({(43, 35, None), (43, 27, None)}, rook.pseudo_legal_moves)

    def test_can_move_three_steps_down(self):
        rook = Board('K7/2PPP3/2PRP3/2P1P3/8/8/3P4/8 w - - 0 1')._get_piece(43)
        self.assertEqual({(43, 35, None), (43, 27, None), (43, 19, None)}, rook.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_down(self):
        rook = Board('K7/2PPP3/2PRP3/2P1P3/8/8/8/8 w - - 0 1')._get_piece(43)
        self.assertEqual({(43, 35, None), (43, 27, None), (43, 19, None), (43, 11, None), (43, 3, None)},
                         rook.pseudo_legal_moves)

    def test_can_move_from_any_position_down(self):
        rook = Board('K7/5PPP/5PRP/5P1P/8/8/8/8 w - - 0 1')._get_piece(46)
        self.assertEqual({(46, 38, None), (46, 30, None), (46, 22, None), (46, 14, None), (46, 6, None)},
                         rook.pseudo_legal_moves)

    def test_can_capture_one_step_down(self):
        rook = Board('K7/5PPP/5PRP/5PpP/8/8/8/8 w - - 0 1')._get_piece(46)
        self.assertEqual({(46, 38, None)}, rook.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_down(self):
        rook = Board('K7/5PPP/5PRP/5P1P/8/6p1/8/8 w - - 0 1')._get_piece(46)
        self.assertEqual({(46, 38, None), (46, 30, None), (46, 22, None)}, rook.pseudo_legal_moves)

    # diagonal moves
    # right up
    def test_can_move_one_step_right_up(self):
        rook = Board('K7/8/8/8/3P4/PP6/PRP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual(set(), rook.pseudo_legal_moves)

    def test_can_capture_one_step_right_up(self):
        rook = Board('K7/8/8/8/8/PPp5/PRP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual(set(), rook.pseudo_legal_moves)

    # right down
    def test_can_move_one_step_right_down(self):
        rook = Board('PPP5/PRP5/PP6/3P4/8/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual(set(), rook.pseudo_legal_moves)

    def test_can_capture_one_step_right_down(self):
        rook = Board('PPP5/PRP5/PPp5/8/8/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual(set(), rook.pseudo_legal_moves)

    # left down
    def test_can_move_one_step_left_down(self):
        rook = Board('5PPP/5PRP/6PP/4P3/8/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual(set(), rook.pseudo_legal_moves)

    def test_can_capture_one_step_left_down(self):
        rook = Board('5PPP/5PRP/5pPP/8/8/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual(set(), rook.pseudo_legal_moves)

    # left up
    def test_can_move_one_step_left_up(self):
        rook = Board('K7/8/8/8/4P3/6PP/5PRP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual(set(), rook.pseudo_legal_moves)

    def test_can_capture_one_step_left_up(self):
        rook = Board('K7/8/8/8/8/5pPP/5PRP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual(set(), rook.pseudo_legal_moves)


class PositionValueTestCase(unittest.TestCase):
    def test_can_generate_pos_value_as_white(self):
        for n, mod in enumerate((0, 0, 0, 5, 5, 0, 0, 0, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0,
                                 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, 5, 10, 10, 10, 10,
                                 10, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0)):
            rook1.move_to(n)
            self.assertEqual(Rook._BASE_VAL + mod, rook1.pos_val)

    def test_can_generate_pos_value_as_black(self):
        for n, mod in enumerate((0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 10, 10, 10, 10, 10, 5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0,
                                 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0,
                                 0, 0, -5, 0, 0, 0, 5, 5, 0, 0, 0)):
            rook2.move_to(n)
            self.assertEqual(Rook._BASE_VAL + mod, rook2.pos_val)


def main() -> None:
    unittest.main()


if __name__ == '__main__':
    main()
