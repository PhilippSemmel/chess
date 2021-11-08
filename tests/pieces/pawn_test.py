import unittest
from board import Pawn, Piece, Board


board = Board()
pawn1 = Pawn(35, True, board)
pawn2 = Pawn(21, False, board)


class PawnConstructionTestCase(unittest.TestCase):
    def test_pawn_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Pawn, Piece))

    def test_piece_type_is_pawn_code(self):
        self.assertEqual(0, pawn1._type)

    def test_piece_pos_is_given_value(self):
        self.assertEqual(35, pawn1._pos)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(21, pawn2._pos)

    def test_piece_color_is_given_value(self):
        self.assertTrue(pawn1._white_piece)

    def test_piece_color_is_any_given_value(self):
        self.assertFalse(pawn2._white_piece)


class PawnMoveGenerationTestCase(unittest.TestCase):
    # white
    def test_cannot_move_when_blocked_by_own_pieces_as_white(self):
        pawn = Board('8/8/8/8/8/1PPP4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_move_in_multiple_directions_as_white(self):
        pawn = Board('8/8/8/8/2p5/3P4/8/8 w - - 0 1').get_piece(19)
        self.assertEqual({(19, 27), (19, 26)}, pawn.pseudo_legal_moves)

    # advance
    def test_can_move_one_step_up_as_white(self):
        pawn = Board('8/8/8/8/2P5/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18)}, pawn.pseudo_legal_moves)

    def test_can_move_two_steps_up_on_second_row_as_white(self):
        pawn = Board('8/8/8/2P5/8/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18), (10, 26)}, pawn.pseudo_legal_moves)

    def test_cannot_move_more_than_two_steps_up_on_second_row_as_white(self):
        pawn = Board('8/8/8/8/8/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18), (10, 26)}, pawn.pseudo_legal_moves)

    def test_can_move_one_step_up_anywhere_as_white(self):
        pawn = Board('8/8/8/1P6/8/8/8/8 w - - 0 1').get_piece(33)
        self.assertEqual({(33, 41)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_one_step_up_as_white(self):
        pawn = Board('8/8/8/8/8/1PpP4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_up_as_white(self):
        pawn = Board('8/8/8/8/2p5/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18)}, pawn.pseudo_legal_moves)

    def test_cannot_move_two_steps_up_anywhere_not_on_second_row_as_white(self):
        pawn = Board('8/8/8/1P6/8/8/8/8 w - - 0 1').get_piece(33)
        self.assertEqual({(33, 41)}, pawn.pseudo_legal_moves)

    def test_cannot_move_up_beyond_the_board_as_white(self):
        pawn = Board('1P6/8/8/8/8/8/8/8 w - - 0 1').get_piece(57)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_move_right_up_as_white(self):
        pawn = Board('8/8/8/1P6/8/8/8/8 w - - 0 1').get_piece(33)
        self.assertEqual({(33, 41)}, pawn.pseudo_legal_moves)

    def test_cannot_move_left_up_as_white(self):
        pawn = Board('8/8/8/1P6/8/8/8/8 w - - 0 1').get_piece(33)
        self.assertEqual({(33, 41)}, pawn.pseudo_legal_moves)

    # capturing sideways
    # right up
    def test_can_capture_one_step_right_up_as_white(self):
        pawn = Board('8/8/8/3Pp3/3P4/8/8/8 w - - 0 1').get_piece(27)
        self.assertEqual({(27, 36)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_right_up_as_white(self):
        pawn = Board('8/8/5p2/3P4/3P4/8/8/8 w - - 0 1').get_piece(27)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_anywhere_one_step_right_up_as_white(self):
        pawn = Board('8/8/8/4Pp2/4P3/8/8/8 w - - 0 1').get_piece(28)
        self.assertEqual({(28, 37)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_right_up_beyond_the_edge_of_the_board_as_white(self):
        pawn = Board('8/8/p7/7P/7P/8/8/8 w - - 0 1').get_piece(31)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    # left up
    def test_can_capture_one_step_left_up_as_white(self):
        pawn = Board('8/8/8/2pP4/3P4/8/8/8 w - - 0 1').get_piece(27)
        self.assertEqual({(27, 34)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_left_up_as_white(self):
        pawn = Board('8/8/1p6/3P4/3P4/8/8/8 w - - 0 1').get_piece(27)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_anywhere_one_step_left_up_as_white(self):
        pawn = Board('8/8/8/3pP3/4P3/8/8/8 w - - 0 1').get_piece(28)
        self.assertEqual({(28, 35)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_left_up_beyond_the_edge_of_the_board_as_white(self):
        pawn = Board('8/8/8/P7/P6p/8/8/8 w - - 0 1').get_piece(24)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    # black
    def test_cannot_move_when_blocked_by_own_pieces_as_black(self):
        pawn = Board('8/4p3/3ppp2/8/8/8/8/8 b - - 0 1').get_piece(52)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    # advance
    def test_can_move_one_step_down_as_black(self):
        pawn = Board('8/4p3/3p1p2/4p3/8/8/8/8 b - - 0 1').get_piece(52)
        self.assertEqual({(52, 44)}, pawn.pseudo_legal_moves)

    def test_can_move_two_steps_down_on_seventh_row_as_black(self):
        pawn = Board('8/4p3/3p1p2/8/4p3/8/8/8 b - - 0 1').get_piece(52)
        self.assertEqual({(52, 44), (52, 36)}, pawn.pseudo_legal_moves)

    def test_cannot_move_more_than_two_steps_down_on_seventh_row_as_black(self):
        pawn = Board('8/4p3/3p1p2/8/8/4p3/8/8 b - - 0 1').get_piece(52)
        self.assertEqual({(52, 44), (52, 36)}, pawn.pseudo_legal_moves)

    def test_can_move_one_step_down_anywhere_as_black(self):
        pawn = Board('8/8/3p4/2p1p3/8/8/8/8 b - - 0 1').get_piece(43)
        self.assertEqual({(43, 35)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_one_step_down_as_black(self):
        pawn = Board('8/4p3/3pPp2/8/8/8/8/8 b - - 0 1').get_piece(52)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_down_as_black(self):
        pawn = Board('8/4p3/3p1p2/4P3/8/8/8/8 b - - 0 1').get_piece(52)
        self.assertEqual({(52, 44)}, pawn.pseudo_legal_moves)

    def test_cannot_move_two_steps_down_anywhere_not_on_seventh_row_as_black(self):
        pawn = Board('8/8/8/1p6/8/8/8/8 b - - 0 1').get_piece(33)
        self.assertEqual({(33, 25)}, pawn.pseudo_legal_moves)

    def test_cannot_move_down_beyond_the_board_as_black(self):
        pawn = Board('8/8/8/8/8/8/8/1p6 b - - 0 1').get_piece(1)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_move_right_down_as_black(self):
        pawn = Board('8/4p3/3p1p2/4p3/8/8/8/8 b - - 0 1').get_piece(52)
        self.assertEqual({(52, 44)}, pawn.pseudo_legal_moves)

    def test_cannot_move_left_down_as_black(self):
        pawn = Board('8/4p3/3p1p2/4p3/8/8/8/8 b - - 0 1').get_piece(52)
        self.assertEqual({(52, 44)}, pawn.pseudo_legal_moves)

    # capturing sideways
    # right down
    def test_can_capture_one_step_right_down_as_black(self):
        pawn = Board('8/8/8/3p4/3pP3/8/8/8 b - - 0 1').get_piece(35)
        self.assertEqual({(35, 28)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_right_down_as_black(self):
        pawn = Board('8/8/8/3p4/3p4/5P2/8/8 b - - 0 1').get_piece(35)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_anywhere_one_step_right_down_as_black(self):
        pawn = Board('8/8/8/4p3/4pP2/8/8/8 b - - 0 1').get_piece(36)
        self.assertEqual({(36, 29)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_right_down_beyond_the_edge_of_the_board_as_black(self):
        pawn = Board('8/8/8/P6p/7p/8/8/8 b - - 0 1').get_piece(39)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    # left down
    def test_can_capture_one_step_left_down_as_black(self):
        pawn = Board('8/8/8/4p3/3Pp3/8/8/8 b - - 0 1').get_piece(36)
        self.assertEqual({(36, 27)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_left_down_as_black(self):
        pawn = Board('8/8/8/4p3/4p3/2P5/8/8 b - - 0 1').get_piece(36)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_anywhere_one_step_left_down_as_black(self):
        pawn = Board('8/8/8/3p4/2Pp4/8/8/8 b - - 0 1').get_piece(35)
        self.assertEqual({(35, 26)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_left_down_beyond_the_edge_of_the_board_as_black(self):
        pawn = Board('8/8/8/p7/p7/7P/8/8 b - - 0 1').get_piece(32)
        self.assertEqual(set(), pawn.pseudo_legal_moves)


if __name__ == '__main__':
    unittest.main()
