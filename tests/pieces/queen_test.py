import unittest
from board import Queen, Piece, Board


board = Board()
queen1 = Queen(35, True, board)
queen2 = Queen(21, False, board)


class GeneralQueenConstructionTestCase(unittest.TestCase):
    def test_piece_pos_is_given_value(self):
        self.assertEqual(35, queen1._pos)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(21, queen2._pos)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, Queen, 64, True, board)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, Queen, -1, True, board)

    def test_piece_color_is_given_value(self):
        self.assertTrue(queen1._white_piece)

    def test_piece_color_is_any_given_value(self):
        self.assertFalse(queen2._white_piece)

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, Queen, True, True, board)

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, Queen, 1, 1, board)

    # def test_raises_type_error_if_board_is_not_board(self):
    #     self.assertRaises(TypeError, Queen, 1, True, 1)


class SpecificQueenConstructionTestCase(unittest.TestCase):
    def test_queen_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Queen, Piece))

    def test_piece_type_is_queen_code(self):
        self.assertEqual(4, queen1._type)


class QueenMoveGenerationTestCase(unittest.TestCase):
    # general
    def test_cannot_move_when_trapped_by_own_pieces(self):
        queen = Board('8/8/2PPP3/2PQP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual(set(), queen.pseudo_legal_moves)

    def test_can_move_in_multiple_directions(self):
        queen = Board('8/1p6/8/5P2/1p2Q2P/4P3/8/1P6 w - - 0 1').get_piece(28)
        self.assertEqual({(28, 29), (28, 30), (28, 36), (28, 44), (28, 52), (28, 60), (28, 35), (28, 42), (28, 49),
                         (28, 27), (28, 26), (28, 25), (28, 19), (28, 10), (28, 21), (28, 14), (28, 7)},
                         queen.pseudo_legal_moves)

    # horizontal moves
    # right
    def test_can_move_one_step_right(self):
        queen = Board('8/8/2PPP3/2PQ1P2/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_right(self):
        queen = Board('8/8/2PPP3/2PQ2P1/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36), (35, 37)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_right(self):
        queen = Board('8/8/2PPP3/2PQ3P/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36), (35, 37), (35, 38)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right(self):
        queen = Board('8/8/2PPP3/2PQ4/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36), (35, 37), (35, 38), (35, 39)}, queen.pseudo_legal_moves)

    def test_can_move_from_any_position_right(self):
        queen = Board('8/8/8/8/8/1PPP4/1PQ5/1PPP4 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 11), (10, 12), (10, 13), (10, 14), (10, 15)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_right(self):
        queen = Board('8/8/2PPP3/2PQp3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_right(self):
        queen = Board('8/8/2PPP3/2PQ2p1/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36), (35, 37), (35, 38)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right(self):
        queen = Board('8/8/p1PPP3/2PQ4/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36), (35, 37), (35, 38), (35, 39)}, queen.pseudo_legal_moves)

    # left
    def test_can_move_one_step_left(self):
        queen = Board('8/8/4PPP1/3P1QP1/4PPP1/8/8/8 w - - 0 1').get_piece(37)
        self.assertEqual({(37, 36)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_left(self):
        queen = Board('8/8/4PPP1/2P2QP1/4PPP1/8/8/8 w - - 0 1').get_piece(37)
        self.assertEqual({(37, 36), (37, 35)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_left(self):
        queen = Board('8/8/4PPP1/1P3QP1/4PPP1/8/8/8 w - - 0 1').get_piece(37)
        self.assertEqual({(37, 36), (37, 35), (37, 34)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left(self):
        queen = Board('8/8/4PPP1/5QP1/4PPP1/8/8/8 w - - 0 1').get_piece(37)
        self.assertEqual({(37, 36), (37, 35), (37, 34), (37, 33), (37, 32)}, queen.pseudo_legal_moves)

    def test_can_move_from_any_position_left(self):
        queen = Board('8/8/8/8/8/4PPP1/5QP1/4PPP1 w - - 0 1').get_piece(13)
        self.assertEqual({(13, 12), (13, 11), (13, 10), (13, 9), (13, 8)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_left(self):
        queen = Board('8/8/4PPP1/4pQP1/4PPP1/8/8/8 w - - 0 1').get_piece(37)
        self.assertEqual({(37, 36)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_left(self):
        queen = Board('8/8/4PPP1/2p2QP1/4PPP1/8/8/8 w - - 0 1').get_piece(37)
        self.assertEqual({(37, 36), (37, 35), (37, 34)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left(self):
        queen = Board('8/8/4PPPp/5QP1/4PPP1/8/8/8 w - - 0 1').get_piece(37)
        self.assertEqual({(37, 36), (37, 35), (37, 34), (37, 33), (37, 32)}, queen.pseudo_legal_moves)

    # vertical moves
    # up
    def test_can_move_one_step_up(self):
        queen = Board('8/8/8/3P4/2P1P3/2PQP3/2PPP3/8 w - - 0 1').get_piece(19)
        self.assertEqual({(19, 27)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_up(self):
        queen = Board('8/8/3P4/8/2P1P3/2PQP3/2PPP3/8 w - - 0 1').get_piece(19)
        self.assertEqual({(19, 27), (19, 35)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_up(self):
        queen = Board('8/3P4/8/8/2P1P3/2PQP3/2PPP3/8 w - - 0 1').get_piece(19)
        self.assertEqual({(19, 27), (19, 35), (19, 43)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_up(self):
        queen = Board('8/8/8/8/2P1P3/2PQP3/2PPP3/8 w - - 0 1').get_piece(19)
        self.assertEqual({(19, 27), (19, 35), (19, 43), (19, 51), (19, 59)}, queen.pseudo_legal_moves)

    def test_can_move_from_any_position_up(self):
        queen = Board('8/8/8/8/5P1P/5PQP/5PPP/8 w - - 0 1').get_piece(22)
        self.assertEqual({(22, 30), (22, 38), (22, 46), (22, 54), (22, 62)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_up(self):
        queen = Board('8/8/8/8/2PpP3/2PQP3/2PPP3/8 w - - 0 1').get_piece(19)
        self.assertEqual({(19, 27)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_up(self):
        queen = Board('8/8/3p4/8/2P1P3/2PQP3/2PPP3/8 w - - 0 1').get_piece(19)
        self.assertEqual({(19, 27), (19, 35), (19, 43)}, queen.pseudo_legal_moves)

    # down
    def test_can_move_one_step_down(self):
        queen = Board('8/2PPP3/2PQP3/2P1P3/3P4/8/8/8 w - - 0 1').get_piece(43)
        self.assertEqual({(43, 35)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_down(self):
        queen = Board('8/2PPP3/2PQP3/2P1P3/8/3P4/8/8 w - - 0 1').get_piece(43)
        self.assertEqual({(43, 35), (43, 27)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_down(self):
        queen = Board('8/2PPP3/2PQP3/2P1P3/8/8/3P4/8 w - - 0 1').get_piece(43)
        self.assertEqual({(43, 35), (43, 27), (43, 19)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_down(self):
        queen = Board('8/2PPP3/2PQP3/2P1P3/8/8/8/8 w - - 0 1').get_piece(43)
        self.assertEqual({(43, 35), (43, 27), (43, 19), (43, 11), (43, 3)}, queen.pseudo_legal_moves)

    def test_can_move_from_any_position_down(self):
        queen = Board('8/5PPP/5PQP/5P1P/8/8/8/8 w - - 0 1').get_piece(46)
        self.assertEqual({(46, 38), (46, 30), (46, 22), (46, 14), (46, 6)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_down(self):
        queen = Board('8/5PPP/5PQP/5PpP/8/8/8/8 w - - 0 1').get_piece(46)
        self.assertEqual({(46, 38)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_down(self):
        queen = Board('8/5PPP/5PQP/5P1P/8/6p1/8/8 w - - 0 1').get_piece(46)
        self.assertEqual({(46, 38), (46, 30), (46, 22)}, queen.pseudo_legal_moves)

    # diagonal moves
    # right up
    def test_can_move_one_step_right_up(self):
        queen = Board('8/8/8/8/3P4/PP6/PQP5/PPP5 w - - 0 1').get_piece(9)
        self.assertEqual({(9, 18)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_right_up(self):
        queen = Board('8/8/8/4P3/8/PP6/PQP5/PPP5 w - - 0 1').get_piece(9)
        self.assertEqual({(9, 18), (9, 27)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_right_up(self):
        queen = Board('8/8/5P2/8/8/PP6/PQP5/PPP5 w - - 0 1').get_piece(9)
        self.assertEqual({(9, 18), (9, 27), (9, 36)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right_up(self):
        queen = Board('8/8/8/8/8/PP6/PQP5/PPP5 w - - 0 1').get_piece(9)
        self.assertEqual({(9, 18), (9, 27), (9, 36), (9, 45), (9, 54), (9, 63)}, queen.pseudo_legal_moves)

    def test_can_move_from_any_position_right_up(self):
        queen = Board('8/2PP4/2PQP3/2PPP3/8/8/8/8 w - - 0 1').get_piece(43)
        self.assertEqual({(43, 52), (43, 61)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_right_up(self):
        queen = Board('8/8/8/8/8/PPp5/PQP5/PPP5 w - - 0 1').get_piece(9)
        self.assertEqual({(9, 18)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_right_up(self):
        queen = Board('8/8/8/4p3/8/PP6/PQP5/PPP5 w - - 0 1').get_piece(9)
        self.assertEqual({(9, 18), (9, 27), (9, 36)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right_up(self):
        queen = Board('8/8/8/8/p7/5PP1/5PQP/5PPP w - - 0 1').get_piece(14)
        self.assertEqual({(14, 23)}, queen.pseudo_legal_moves)

    # right down
    def test_can_move_one_step_right_down(self):
        queen = Board('PPP5/PQP5/PP6/3P4/8/8/8/8 w - - 0 1').get_piece(49)
        self.assertEqual({(49, 42)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_right_down(self):
        queen = Board('PPP5/PQP5/PP6/8/4P3/8/8/8 w - - 0 1').get_piece(49)
        self.assertEqual({(49, 42), (49, 35)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_right_down(self):
        queen = Board('PPP5/PQP5/PP6/8/8/5P2/8/8 w - - 0 1').get_piece(49)
        self.assertEqual({(49, 42), (49, 35), (49, 28)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right_down(self):
        queen = Board('PPP5/PQP5/PP6/8/8/8/8/8 w - - 0 1').get_piece(49)
        self.assertEqual({(49, 42), (49, 35), (49, 28), (49, 21), (49, 14), (49, 7)}, queen.pseudo_legal_moves)

    def test_can_move_from_any_position_right_down(self):
        queen = Board('8/8/8/8/2PPP3/2PQP3/2PP4/8 w - - 0 1').get_piece(19)
        self.assertEqual({(19, 12), (19, 5)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_right_down(self):
        queen = Board('PPP5/PQP5/PPp5/8/8/8/8/8 w - - 0 1').get_piece(49)
        self.assertEqual({(49, 42)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_right_down(self):
        queen = Board('PPP5/PQP5/PP6/8/4p3/8/8/8 w - - 0 1').get_piece(49)
        self.assertEqual({(49, 42), (49, 35), (49, 28)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right_down(self):
        queen = Board('5PPP/5PQP/5PP1/p7/8/8/8/8 w - - 0 1').get_piece(54)
        self.assertEqual({(54, 47)}, queen.pseudo_legal_moves)

    # left down
    def test_can_move_one_step_left_down(self):
        queen = Board('5PPP/5PQP/6PP/4P3/8/8/8/8 w - - 0 1').get_piece(54)
        self.assertEqual({(54, 45)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_left_down(self):
        queen = Board('5PPP/5PQP/6PP/8/3P4/8/8/8 w - - 0 1').get_piece(54)
        self.assertEqual({(54, 45), (54, 36)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_left_down(self):
        queen = Board('5PPP/5PQP/6PP/8/8/2P5/8/8 w - - 0 1').get_piece(54)
        self.assertEqual({(54, 45), (54, 36), (54, 27)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left_down(self):
        queen = Board('5PPP/5PQP/6PP/8/8/8/8/8 w - - 0 1').get_piece(54)
        self.assertEqual({(54, 45), (54, 36), (54, 27), (54, 18), (54, 9), (54, 0)}, queen.pseudo_legal_moves)

    def test_can_move_from_any_position_left_down(self):
        queen = Board('8/8/8/8/4PPP1/4PQP1/5PP1/8 w - - 0 1').get_piece(21)
        self.assertEqual({(21, 12), (21, 3)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_left_down(self):
        queen = Board('5PPP/5PQP/5pPP/8/8/8/8/8 w - - 0 1').get_piece(54)
        self.assertEqual({(54, 45)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_left_down(self):
        queen = Board('5PPP/5PQP/6PP/8/3p4/8/8/8 w - - 0 1').get_piece(54)
        self.assertEqual({(54, 45), (54, 36), (54, 27)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left_down(self):
        queen = Board('PPP5/PQP5/1PP5/8/7p/8/8/8 w - - 0 1').get_piece(49)
        self.assertEqual({(49, 40)}, queen.pseudo_legal_moves)

    # left up
    def test_can_move_one_step_left_up(self):
        queen = Board('8/8/8/8/4P3/6PP/5PQP/5PPP w - - 0 1').get_piece(14)
        self.assertEqual({(14, 21)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_left_up(self):
        queen = Board('8/8/8/3P4/8/6PP/5PQP/5PPP w - - 0 1').get_piece(14)
        self.assertEqual({(14, 21), (14, 28)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_left_up(self):
        queen = Board('8/8/2P5/8/8/6PP/5PQP/5PPP w - - 0 1').get_piece(14)
        self.assertEqual({(14, 21), (14, 28), (14, 35)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left_up(self):
        queen = Board('8/8/8/8/8/6PP/5PQP/5PPP w - - 0 1').get_piece(14)
        self.assertEqual({(14, 21), (14, 28), (14, 35), (14, 42), (14, 49), (14, 56)}, queen.pseudo_legal_moves)

    def test_can_move_from_any_position_left_up(self):
        queen = Board('8/5PP1/4PQP1/4PPP1/8/8/8/8 w - - 0 1').get_piece(45)
        self.assertEqual({(45, 52), (45, 59)}, queen.pseudo_legal_moves)

    def test_can_capture_one_step_left_up(self):
        queen = Board('8/8/8/8/8/5pPP/5PQP/5PPP w - - 0 1').get_piece(14)
        self.assertEqual({(14, 21)}, queen.pseudo_legal_moves)

    def test_can_move_and_capture_three_steps_left_up(self):
        queen = Board('8/8/8/3p4/8/6PP/5PQP/5PPP w - - 0 1').get_piece(14)
        self.assertEqual({(14, 21), (14, 28), (14, 35)}, queen.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left_up(self):
        queen = Board('8/8/8/8/8/1PP4p/PQP5/PPP5 w - - 0 1').get_piece(9)
        self.assertEqual({(9, 16)}, queen.pseudo_legal_moves)


if __name__ == '__main__':
    unittest.main()
