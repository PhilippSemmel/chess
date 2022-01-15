import unittest

from board import Bishop, Piece, Board

board = Board()
bishop1 = Bishop(35, True, board)
bishop2 = Bishop(21, False, board)


class ConstructionTestCase(unittest.TestCase):
    def test_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Bishop, Piece))

    def test_base_val_is_correct(self):
        self.assertEqual(330, bishop1._BASE_VAL)

    def test_base_val_is_always_correct(self):
        self.assertEqual(330, bishop2._BASE_VAL)

    def test_pos_val_mod_is_correct_as_white(self):
        self.assertEqual((-20, -10, -10, -10, -10, -10, -10, -20, -10, 5, 0, 0, 0, 0, 5, -10, -10, 10, 10, 10, 10, 10,
                          10, -10, -10, 0, 10, 10, 10, 10, 0, -10, -10, 5, 5, 10, 10, 5, 5, -10, -10, 0, 5, 10, 10, 5,
                          0, -10, -10, 0, 0, 0, 0, 0, 0, -10, -20, -10, -10, -10, -10, -10, -10, -20),
                         bishop1._POS_VAL_MOD[True])

    def test_pos_val_mod_is_correct_as_black(self):
        self.assertEqual((-20, -10, -10, -10, -10, -10, -10, -20, -10, 0, 0, 0, 0, 0, 0, -10, -10, 0, 5, 10, 10, 5, 0,
                          -10, -10, 5, 5, 10, 10, 5, 5, -10, -10, 0, 10, 10, 10, 10, 0, -10, -10, 10, 10, 10, 10, 10,
                          10, -10, -10, 5, 0, 0, 0, 0, 5, -10, -20, -10, -10, -10, -10, -10, -10, -20),
                         bishop2._POS_VAL_MOD[False])

    def test_pos_is_given_value(self):
        self.assertEqual(35, bishop1._pos)

    def test_pos_is_any_given_value(self):
        self.assertEqual(21, bishop2._pos)

    def test_color_is_given_value(self):
        self.assertTrue(bishop1._white_piece)

    def test_color_is_any_given_value(self):
        self.assertFalse(bishop2._white_piece)

    def test_capture_data_is_none(self):
        self.assertIsNone(bishop1._capture_info)

    def test_capture_data_is_always_none(self):
        self.assertIsNone(bishop2._capture_info)


class MoveGenerationTestCase(unittest.TestCase):
    # general
    def test_cannot_move_when_blocked_by_own_pieces(self):
        bishop = Board('8/8/2PPP3/2PBP3/2PPP3/8/8/K7 w - - 0 1')._get_piece(35)
        self.assertEqual(set(), bishop.pseudo_legal_moves)

    def test_can_move_in_multiple_directions(self):
        bishop = Board('K7/1p6/8/5P2/1p2B2P/4P3/8/1P6 w - - 0 1')._get_piece(28)
        self.assertEqual({(28, 35, None), (28, 42, None), (28, 49, None), (28, 19, None), (28, 10, None),
                          (28, 21, None), (28, 14, None), (28, 7, None)}, bishop.pseudo_legal_moves)

    def test_attacking_squares_equal_pseudo_legal_move_target_squares(self):
        bishop = Board('8/1p6/8/5P2/1p2B2P/4P3/8/KP6 w - - 0 1')._get_piece(28)
        self.assertEqual({35, 42, 49, 19, 10, 21, 14, 7}, bishop.attacking_squares)

    # horizontal moves
    # right
    def test_can_move_one_step_right(self):
        bishop = Board('8/8/2PPP3/2PB1P2/2PPP3/8/8/K7 w - - 0 1')._get_piece(35)
        self.assertEqual(set(), bishop.pseudo_legal_moves)

    def test_can_capture_one_step_right(self):
        bishop = Board('8/8/2PPP3/2PBp3/2PPP3/8/8/K7 w - - 0 1')._get_piece(35)
        self.assertEqual(set(), bishop.pseudo_legal_moves)

    # left
    def test_can_move_one_step_left(self):
        bishop = Board('8/8/4PPP1/3P1BP1/4PPP1/8/8/K7 w - - 0 1')._get_piece(37)
        self.assertEqual(set(), bishop.pseudo_legal_moves)

    def test_can_capture_one_step_left(self):
        bishop = Board('8/8/4PPP1/4pBP1/4PPP1/8/8/K7 w - - 0 1')._get_piece(37)
        self.assertEqual(set(), bishop.pseudo_legal_moves)

    # vertical moves
    # up
    def test_can_move_one_step_up(self):
        bishop = Board('8/8/8/3P4/2P1P3/2PBP3/2PPP3/K7 w - - 0 1')._get_piece(19)
        self.assertEqual(set(), bishop.pseudo_legal_moves)

    def test_can_capture_one_step_up(self):
        bishop = Board('8/8/8/8/2PpP3/2PBP3/2PPP3/K7 w - - 0 1')._get_piece(19)
        self.assertEqual(set(), bishop.pseudo_legal_moves)

    # down
    def test_can_move_one_step_down(self):
        bishop = Board('8/2PPP3/2PBP3/2P1P3/3P4/8/8/K7 w - - 0 1')._get_piece(43)
        self.assertEqual(set(), bishop.pseudo_legal_moves)

    def test_can_capture_one_step_down(self):
        bishop = Board('8/5PPP/5PBP/5PpP/8/8/8/K7 w - - 0 1')._get_piece(46)
        self.assertEqual(set(), bishop.pseudo_legal_moves)

    # diagonal moves
    # right up
    def test_can_move_one_step_right_up(self):
        bishop = Board('K7/8/8/8/3P4/PP6/PBP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None)}, bishop.pseudo_legal_moves)

    def test_can_move_two_steps_right_up(self):
        bishop = Board('K7/8/8/4P3/8/PP6/PBP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None), (9, 27, None)}, bishop.pseudo_legal_moves)

    def test_can_move_three_steps_right_up(self):
        bishop = Board('K7/8/5P2/8/8/PP6/PBP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None), (9, 27, None), (9, 36, None)}, bishop.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right_up(self):
        bishop = Board('K7/8/8/8/8/PP6/PBP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None), (9, 27, None), (9, 36, None), (9, 45, None), (9, 54, None), (9, 63, None)},
                         bishop.pseudo_legal_moves)

    def test_can_move_from_any_position_right_up(self):
        bishop = Board('8/2PP4/2PBP3/2PPP3/8/8/8/K7 w - - 0 1')._get_piece(43)
        self.assertEqual({(43, 52, None), (43, 61, None)}, bishop.pseudo_legal_moves)

    def test_can_capture_one_step_right_up(self):
        bishop = Board('K7/8/8/8/8/PPp5/PBP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None)}, bishop.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_right_up(self):
        bishop = Board('K7/8/8/4p3/8/PP6/PBP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None), (9, 27, None), (9, 36, None)}, bishop.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right_up(self):
        bishop = Board('K7/8/8/8/p7/5PP1/5PBP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 23, None)}, bishop.pseudo_legal_moves)

    # right down
    def test_can_move_one_step_right_down(self):
        bishop = Board('PPP5/PBP5/PP6/3P4/8/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None)}, bishop.pseudo_legal_moves)

    def test_can_move_two_steps_right_down(self):
        bishop = Board('PPP5/PBP5/PP6/8/4P3/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None), (49, 35, None)}, bishop.pseudo_legal_moves)

    def test_can_move_three_steps_right_down(self):
        bishop = Board('PPP5/PBP5/PP6/8/8/5P2/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None), (49, 35, None), (49, 28, None)}, bishop.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right_down(self):
        bishop = Board('PPP5/PBP5/PP6/8/8/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None), (49, 35, None), (49, 28, None), (49, 21, None), (49, 14, None),
                          (49, 7, None)}, bishop.pseudo_legal_moves)

    def test_can_move_from_any_position_right_down(self):
        bishop = Board('8/8/8/8/2PPP3/2PBP3/2PP4/K7 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 12, None), (19, 5, None)}, bishop.pseudo_legal_moves)

    def test_can_capture_one_step_right_down(self):
        bishop = Board('PPP5/PBP5/PPp5/8/8/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None)}, bishop.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_right_down(self):
        bishop = Board('PPP5/PBP5/PP6/8/4p3/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None), (49, 35, None), (49, 28, None)}, bishop.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right_down(self):
        bishop = Board('5PPP/5PBP/5PP1/p7/8/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 47, None)}, bishop.pseudo_legal_moves)

    # left down
    def test_can_move_one_step_left_down(self):
        bishop = Board('5PPP/5PBP/6PP/4P3/8/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None)}, bishop.pseudo_legal_moves)

    def test_can_move_two_steps_left_down(self):
        bishop = Board('5PPP/5PBP/6PP/8/3P4/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None), (54, 36, None)}, bishop.pseudo_legal_moves)

    def test_can_move_three_steps_left_down(self):
        bishop = Board('5PPP/5PBP/6PP/8/8/2P5/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None), (54, 36, None), (54, 27, None)}, bishop.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left_down(self):
        bishop = Board('5PPP/5PBP/6PP/8/8/8/8/7K w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None), (54, 36, None), (54, 27, None), (54, 18, None), (54, 9, None), (54, 0, None)},
                         bishop.pseudo_legal_moves)

    def test_can_move_from_any_position_left_down(self):
        bishop = Board('8/8/8/8/4PPP1/4PBP1/5PP1/K7 w - - 0 1')._get_piece(21)
        self.assertEqual({(21, 12, None), (21, 3, None)}, bishop.pseudo_legal_moves)

    def test_can_capture_one_step_left_down(self):
        bishop = Board('5PPP/5PBP/5pPP/8/8/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None)}, bishop.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_left_down(self):
        bishop = Board('5PPP/5PBP/6PP/8/3p4/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None), (54, 36, None), (54, 27, None)}, bishop.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left_down(self):
        bishop = Board('PPP5/PBP5/1PP5/8/7p/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 40, None)}, bishop.pseudo_legal_moves)

    # left up
    def test_can_move_one_step_left_up(self):
        bishop = Board('K7/8/8/8/4P3/6PP/5PBP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None)}, bishop.pseudo_legal_moves)

    def test_can_move_two_steps_left_up(self):
        bishop = Board('K7/8/8/3P4/8/6PP/5PBP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None), (14, 28, None)}, bishop.pseudo_legal_moves)

    def test_can_move_three_steps_left_up(self):
        bishop = Board('K7/8/2P5/8/8/6PP/5PBP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None), (14, 28, None), (14, 35, None)}, bishop.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left_up(self):
        bishop = Board('7K/8/8/8/8/6PP/5PBP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None), (14, 28, None), (14, 35, None), (14, 42, None), (14, 49, None),
                          (14, 56, None)}, bishop.pseudo_legal_moves)

    def test_can_move_from_any_position_left_up(self):
        bishop = Board('K7/5PP1/4PBP1/4PPP1/8/8/8/8 w - - 0 1')._get_piece(45)
        self.assertEqual({(45, 52, None), (45, 59, None)}, bishop.pseudo_legal_moves)

    def test_can_capture_one_step_left_up(self):
        bishop = Board('K7/8/8/8/8/5pPP/5PBP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None)}, bishop.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_left_up(self):
        bishop = Board('K7/8/8/3p4/8/6PP/5PBP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None), (14, 28, None), (14, 35, None)}, bishop.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left_up(self):
        bishop = Board('K7/8/8/8/8/1PP4p/PBP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 16, None)}, bishop.pseudo_legal_moves)


class PositionValueTestCase(unittest.TestCase):
    def test_can_generate_pos_value_as_white(self):
        for n, mod in enumerate((-20, -10, -10, -10, -10, -10, -10, -20, -10, 5, 0, 0, 0, 0, 5, -10, -10, 10, 10, 10,
                                 10, 10, 10, -10, -10, 0, 10, 10, 10, 10, 0, -10, -10, 5, 5, 10, 10, 5, 5, -10, -10,
                                 0, 5, 10, 10, 5, 0, -10, -10, 0, 0, 0, 0, 0, 0, -10, -20, -10, -10, -10, -10, -10, -10,
                                 -20)):
            bishop1.move_to(n)
            self.assertEqual(Bishop._BASE_VAL + mod, bishop1.pos_val)

    def test_can_generate_pos_value_as_black(self):
        for n, mod in enumerate((-20, -10, -10, -10, -10, -10, -10, -20, -10, 0, 0, 0, 0, 0, 0, -10, -10, 0, 5, 10, 10,
                                 5, 0, -10, -10, 5, 5, 10, 10, 5, 5, -10, -10, 0, 10, 10, 10, 10, 0, -10, -10, 10, 10,
                                 10, 10, 10, 10, -10, -10, 5, 0, 0, 0, 0, 5, -10, -20, -10, -10, -10, -10, -10,
                                 -10, -20)):
            bishop2.move_to(n)
            self.assertEqual(Bishop._BASE_VAL + mod, bishop2.pos_val)


def main() -> None:
    unittest.main()


if __name__ == '__main__':
    main()
