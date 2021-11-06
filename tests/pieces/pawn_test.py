import unittest
from board import Pawn, Piece, Board


board = Board()
pawn1 = Pawn(35, True, board)
pawn2 = Pawn(21, False, board)


class GeneralPawnConstructionTestCase(unittest.TestCase):
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
    def test_cannot_move_when_blocked_by_own_pieces(self):
        pawn = Board('8/8/8/8/8/1PPP4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    # white
    # advance
    def test_can_move_one_step_up_as_white(self):
        pawn = Board('8/8/8/8/2P5/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18)}, pawn.pseudo_legal_moves)

    def test_can_move_two_steps_up_if_on_second_row_as_white(self):
        pawn = Board('8/8/8/2P5/8/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18), (10, 26)}, pawn.pseudo_legal_moves)

    def test_cannot_move_more_than_two_steps_up_on_second_row_as_white(self):
        pawn = Board('8/8/8/8/8/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18), (10, 26)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_one_step_up_as_white(self):
        pawn = Board('8/8/8/8/8/1PpP4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_up_as_white(self):
        pawn = Board('8/8/8/8/2p5/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18)}, pawn.pseudo_legal_moves)

    def test_can_move_one_step_up_anywhere_as_white(self):
        pawn = Board('8/8/8/1P6/8/8/8/8 w - - 0 1').get_piece(33)
        self.assertEqual({(33, 41)}, pawn.pseudo_legal_moves)

    def test_cannot_move_two_steps_up_anywhere_if_not_on_second_row_as_white(self):
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


if __name__ == '__main__':
    unittest.main()
