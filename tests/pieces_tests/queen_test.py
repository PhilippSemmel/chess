import unittest

from board import Queen, Piece, Board

board = Board()
queen1 = Queen(35, True, board)
queen2 = Queen(21, False, board)


class ConstructionTestCase(unittest.TestCase):
    def test_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Queen, Piece))

    def test_base_val_is_correct(self):
        self.assertEqual(900, queen1._BASE_VAL)

    def test_base_val_is_always_correct(self):
        self.assertEqual(900, queen2._BASE_VAL)

    def test_pos_val_mod_is_correct_as_white(self):
        self.assertEqual((-20, -10, -10, -5, -5, -10, -10, -20, -10, 0, 5, 0, 0, 0, 0, -10, -10, 5, 5, 5, 5, 5, 0, -10,
                          0, 0, 5, 5, 5, 5, 0, -5, -5, 0, 5, 5, 5, 5, 0, -5, -10, 0, 5, 5, 5, 5, 0, -10, -10, 0, 0, 0,
                          0, 0, 0, -10, -20, -10, -10, -5, -5, -10, -10, -20), queen1._POS_VAL_MOD[True])

    def test_pos_val_mod_is_correct_as_black(self):
        self.assertEqual((-20, -10, -10, -5, -5, -10, -10, -20, -10, 0, 0, 0, 0, 0, 0, -10, -10, 0, 5, 5, 5, 5, 0, -10,
                          -5, 0, 5, 5, 5, 5, 0, -5, 0, 0, 5, 5, 5, 5, 0, -5, -10, 5, 5, 5, 5, 5, 0, -10, -10, 0, 5, 0,
                          0, 0, 0, -10, -20, -10, -10, -5, -5, -10, -10, -20), queen2._POS_VAL_MOD[False])

    def test_pos_is_given_value(self):
        self.assertEqual(35, queen1._pos)

    def test_pos_is_any_given_value(self):
        self.assertEqual(21, queen2._pos)

    def test_color_is_given_value(self):
        self.assertTrue(queen1._white_piece)

    def test_color_is_any_given_value(self):
        self.assertFalse(queen2._white_piece)

    def test_capture_data_is_none(self):
        self.assertIsNone(queen1._capture_info)

    def test_capture_data_is_always_none(self):
        self.assertIsNone(queen2._capture_info)


class MoveGenerationTestCase(unittest.TestCase):
    # general
    def test_cannot_move_when_blocked_by_own_pieces(self):
        queen = Board('K7/8/2PPP3/2PQP3/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual(set(), queen.pseudo_legal_moves)

    def test_can_move_in_multiple_directions(self):
        queen = Board('K7/1p6/8/5P2/1p2Q2P/4P3/8/1P6 w - - 0 1')._get_piece(28)
        self.assertEqual(
            {(28, 29, None), (28, 30, None), (28, 36, None), (28, 44, None), (28, 52, None), (28, 60, None),
             (28, 35, None), (28, 42, None), (28, 49, None),
             (28, 27, None), (28, 26, None), (28, 25, None), (28, 19, None), (28, 10, None), (28, 21, None),
             (28, 14, None), (28, 7, None)},
            queen.pseudo_legal_moves)

    def test_attacking_squares_equal_pseudo_legal_move_target_squares(self):
        queen = Board('K7/1p6/8/5P2/1p2Q2P/4P3/8/1P6 w - - 0 1')._get_piece(28)
        self.assertEqual({29, 30, 36, 44, 52, 60, 35, 42, 49, 27, 26, 25, 19, 10, 21, 14, 7},
                         queen.attacking_squares)

    # horizontal moves
    # right
    def test_can_move_one_step_right(self):
        queen = Board('8/8/2PPP3/2PQ1P2/2PPP3/8/8/K7 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_right(self):
        queen = Board('8/8/2PPP3/2PQ2P1/2PPP3/8/8/K7 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None), (35, 37, None)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_right(self):
        queen = Board('8/8/2PPP3/2PQ3P/2PPP3/8/8/K7 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None), (35, 37, None), (35, 38, None)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right(self):
        queen = Board('8/8/2PPP3/2PQ4/2PPP3/8/8/K7 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None), (35, 37, None), (35, 38, None), (35, 39, None)}, queen.pseudo_legal_moves)

    def test_can_move_from_any_position_right(self):
        queen = Board('K7/8/8/8/8/1PPP4/1PQ5/1PPP4 w - - 0 1')._get_piece(10)
        self.assertEqual({(10, 11, None), (10, 12, None), (10, 13, None), (10, 14, None), (10, 15, None)},
                         queen.pseudo_legal_moves)

    def test_can_capture_one_step_right(self):
        queen = Board('K7/8/2PPP3/2PQp3/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_right(self):
        queen = Board('K7/8/2PPP3/2PQ2p1/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None), (35, 37, None), (35, 38, None)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right(self):
        queen = Board('K7/8/p1PPP3/2PQ4/2PPP3/8/8/8 w - - 0 1')._get_piece(35)
        self.assertEqual({(35, 36, None), (35, 37, None), (35, 38, None), (35, 39, None)}, queen.pseudo_legal_moves)

    # left
    def test_can_move_one_step_left(self):
        queen = Board('K7/8/4PPP1/3P1QP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_left(self):
        queen = Board('K7/8/4PPP1/2P2QP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None), (37, 35, None)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_left(self):
        queen = Board('K7/8/4PPP1/1P3QP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None), (37, 35, None), (37, 34, None)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left(self):
        queen = Board('K7/8/4PPP1/5QP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None), (37, 35, None), (37, 34, None), (37, 33, None), (37, 32, None)},
                         queen.pseudo_legal_moves)

    def test_can_move_from_any_position_left(self):
        queen = Board('K7/8/8/8/8/4PPP1/5QP1/4PPP1 w - - 0 1')._get_piece(13)
        self.assertEqual({(13, 12, None), (13, 11, None), (13, 10, None), (13, 9, None), (13, 8, None)},
                         queen.pseudo_legal_moves)

    def test_can_capture_one_step_left(self):
        queen = Board('K7/8/4PPP1/4pQP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_left(self):
        queen = Board('K7/8/4PPP1/2p2QP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None), (37, 35, None), (37, 34, None)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left(self):
        queen = Board('K7/8/4PPPp/5QP1/4PPP1/8/8/8 w - - 0 1')._get_piece(37)
        self.assertEqual({(37, 36, None), (37, 35, None), (37, 34, None), (37, 33, None), (37, 32, None)},
                         queen.pseudo_legal_moves)

    # vertical moves
    # up
    def test_can_move_one_step_up(self):
        queen = Board('K7/8/8/3P4/2P1P3/2PQP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_up(self):
        queen = Board('K7/8/3P4/8/2P1P3/2PQP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None), (19, 35, None)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_up(self):
        queen = Board('K7/3P4/8/8/2P1P3/2PQP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None), (19, 35, None), (19, 43, None)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_up(self):
        queen = Board('K7/8/8/8/2P1P3/2PQP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None), (19, 35, None), (19, 43, None), (19, 51, None), (19, 59, None)},
                         queen.pseudo_legal_moves)

    def test_can_move_from_any_position_up(self):
        queen = Board('K7/8/8/8/5P1P/5PQP/5PPP/8 w - - 0 1')._get_piece(22)
        self.assertEqual({(22, 30, None), (22, 38, None), (22, 46, None), (22, 54, None), (22, 62, None)},
                         queen.pseudo_legal_moves)

    def test_can_capture_one_step_up(self):
        queen = Board('K7/8/8/8/2PpP3/2PQP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_up(self):
        queen = Board('K7/8/3p4/8/2P1P3/2PQP3/2PPP3/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27, None), (19, 35, None), (19, 43, None)}, queen.pseudo_legal_moves)

    # down
    def test_can_move_one_step_down(self):
        queen = Board('8/2PPP3/2PQP3/2P1P3/3P4/8/8/K7 w - - 0 1')._get_piece(43)
        self.assertEqual({(43, 35, None)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_down(self):
        queen = Board('8/2PPP3/2PQP3/2P1P3/8/3P4/8/K7 w - - 0 1')._get_piece(43)
        self.assertEqual({(43, 35, None), (43, 27, None)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_down(self):
        queen = Board('8/2PPP3/2PQP3/2P1P3/8/8/3P4/K7 w - - 0 1')._get_piece(43)
        self.assertEqual({(43, 35, None), (43, 27, None), (43, 19, None)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_down(self):
        queen = Board('8/2PPP3/2PQP3/2P1P3/8/8/8/K7 w - - 0 1')._get_piece(43)
        self.assertEqual({(43, 35, None), (43, 27, None), (43, 19, None), (43, 11, None), (43, 3, None)},
                         queen.pseudo_legal_moves)

    def test_can_move_from_any_position_down(self):
        queen = Board('8/5PPP/5PQP/5P1P/8/8/8/K7 w - - 0 1')._get_piece(46)
        self.assertEqual({(46, 38, None), (46, 30, None), (46, 22, None), (46, 14, None), (46, 6, None)},
                         queen.pseudo_legal_moves)

    def test_can_capture_one_step_down(self):
        queen = Board('8/5PPP/5PQP/5PpP/8/8/8/K7 w - - 0 1')._get_piece(46)
        self.assertEqual({(46, 38, None)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_down(self):
        queen = Board('8/5PPP/5PQP/5P1P/8/6p1/8/K7 w - - 0 1')._get_piece(46)
        self.assertEqual({(46, 38, None), (46, 30, None), (46, 22, None)}, queen.pseudo_legal_moves)

    # diagonal moves
    # right up
    def test_can_move_one_step_right_up(self):
        queen = Board('K7/8/8/8/3P4/PP6/PQP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_right_up(self):
        queen = Board('K7/8/8/4P3/8/PP6/PQP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None), (9, 27, None)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_right_up(self):
        queen = Board('K7/8/5P2/8/8/PP6/PQP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None), (9, 27, None), (9, 36, None)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right_up(self):
        queen = Board('K7/8/8/8/8/PP6/PQP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None), (9, 27, None), (9, 36, None), (9, 45, None), (9, 54, None), (9, 63, None)},
                         queen.pseudo_legal_moves)

    def test_can_move_from_any_position_right_up(self):
        queen = Board('K7/2PP4/2PQP3/2PPP3/8/8/8/8 w - - 0 1')._get_piece(43)
        self.assertEqual({(43, 52, None), (43, 61, None)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_right_up(self):
        queen = Board('K7/8/8/8/8/PPp5/PQP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_right_up(self):
        queen = Board('K7/8/8/4p3/8/PP6/PQP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 18, None), (9, 27, None), (9, 36, None)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right_up(self):
        queen = Board('K7/8/8/8/p7/5PP1/5PQP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 23, None)}, queen.pseudo_legal_moves)

    # right down
    def test_can_move_one_step_right_down(self):
        queen = Board('PPP5/PQP5/PP6/3P4/8/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_right_down(self):
        queen = Board('PPP5/PQP5/PP6/8/4P3/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None), (49, 35, None)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_right_down(self):
        queen = Board('PPP5/PQP5/PP6/8/8/5P2/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None), (49, 35, None), (49, 28, None)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right_down(self):
        queen = Board('PPP5/PQP5/PP6/8/8/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual(
            {(49, 42, None), (49, 35, None), (49, 28, None), (49, 21, None), (49, 14, None), (49, 7, None)},
            queen.pseudo_legal_moves)

    def test_can_move_from_any_position_right_down(self):
        queen = Board('8/8/8/8/2PPP3/2PQP3/2PP4/K7 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 12, None), (19, 5, None)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_right_down(self):
        queen = Board('PPP5/PQP5/PPp5/8/8/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_right_down(self):
        queen = Board('PPP5/PQP5/PP6/8/4p3/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 42, None), (49, 35, None), (49, 28, None)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right_down(self):
        queen = Board('5PPP/5PQP/5PP1/p7/8/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 47, None)}, queen.pseudo_legal_moves)

    # left down
    def test_can_move_one_step_left_down(self):
        queen = Board('5PPP/5PQP/6PP/4P3/8/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_left_down(self):
        queen = Board('5PPP/5PQP/6PP/8/3P4/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None), (54, 36, None)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_left_down(self):
        queen = Board('5PPP/5PQP/6PP/8/8/2P5/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None), (54, 36, None), (54, 27, None)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left_down(self):
        queen = Board('5PPP/5PQP/6PP/8/8/8/8/7K w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None), (54, 36, None), (54, 27, None), (54, 18, None), (54, 9, None), (54, 0, None)},
                         queen.pseudo_legal_moves)

    def test_can_move_from_any_position_left_down(self):
        queen = Board('K7/8/8/8/4PPP1/4PQP1/5PP1/8 w - - 0 1')._get_piece(21)
        self.assertEqual({(21, 12, None), (21, 3, None)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_left_down(self):
        queen = Board('5PPP/5PQP/5pPP/8/8/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_left_down(self):
        queen = Board('5PPP/5PQP/6PP/8/3p4/8/8/K7 w - - 0 1')._get_piece(54)
        self.assertEqual({(54, 45, None), (54, 36, None), (54, 27, None)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left_down(self):
        queen = Board('PPP5/PQP5/1PP5/8/7p/8/8/K7 w - - 0 1')._get_piece(49)
        self.assertEqual({(49, 40, None)}, queen.pseudo_legal_moves)

    # left up
    def test_can_move_one_step_left_up(self):
        queen = Board('K7/8/8/8/4P3/6PP/5PQP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_left_up(self):
        queen = Board('K7/8/8/3P4/8/6PP/5PQP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None), (14, 28, None)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_left_up(self):
        queen = Board('K7/8/2P5/8/8/6PP/5PQP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None), (14, 28, None), (14, 35, None)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left_up(self):
        queen = Board('7K/8/8/8/8/6PP/5PQP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual(
            {(14, 21, None), (14, 28, None), (14, 35, None), (14, 42, None), (14, 49, None), (14, 56, None)},
            queen.pseudo_legal_moves)

    def test_can_move_from_any_position_left_up(self):
        queen = Board('8/5PP1/4PQP1/4PPP1/8/8/8/K7 w - - 0 1')._get_piece(45)
        self.assertEqual({(45, 52, None), (45, 59, None)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_left_up(self):
        queen = Board('K7/8/8/8/8/5pPP/5PQP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_left_up(self):
        queen = Board('K7/8/8/3p4/8/6PP/5PQP/5PPP w - - 0 1')._get_piece(14)
        self.assertEqual({(14, 21, None), (14, 28, None), (14, 35, None)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left_up(self):
        queen = Board('K7/8/8/8/8/1PP4p/PQP5/PPP5 w - - 0 1')._get_piece(9)
        self.assertEqual({(9, 16, None)}, queen.pseudo_legal_moves)


class PositionValueTestCase(unittest.TestCase):
    def test_can_generate_pos_value_as_white(self):
        for n, mod in enumerate((-20, -10, -10, -5, -5, -10, -10, -20, -10, 0, 5, 0, 0, 0, 0, -10, -10, 5, 5, 5, 5, 5,
                                 0, -10, 0, 0, 5, 5, 5, 5, 0, -5, -5, 0, 5, 5, 5, 5, 0, -5, -10, 0, 5, 5, 5, 5, 0, -10,
                                 -10, 0, 0, 0, 0, 0, 0, -10, -20, -10, -10, -5, -5, -10, -10, -20)):
            queen1.move_to(n)
            self.assertEqual(Queen._BASE_VAL + mod, queen1.pos_val)

    def test_can_generate_pos_value_as_black(self):
        for n, mod in enumerate((-20, -10, -10, -5, -5, -10, -10, -20, -10, 0, 0, 0, 0, 0, 0, -10, -10, 0, 5, 5, 5, 5,
                                 0, -10, -5, 0, 5, 5, 5, 5, 0, -5, 0, 0, 5, 5, 5, 5, 0, -5, -10, 5, 5, 5, 5, 5, 0, -10,
                                 -10, 0, 5, 0, 0, 0, 0, -10, -20, -10, -10, -5, -5, -10, -10, -20)):
            queen2.move_to(n)
            self.assertEqual(Queen._BASE_VAL + mod, queen2.pos_val)


def main() -> None:
    unittest.main()


if __name__ == '__main__':
    main()
