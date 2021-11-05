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

    # advance
    # white
    def test_can_move_one_step_up_if_square_is_empty_as_white(self):
        pawn = Board('8/8/8/8/2P5/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18)}, pawn.pseudo_legal_moves)

    def test_can_move_two_steps_up_if_square_are_empty_and_on_second_row_as_white(self):
        pawn = Board('8/8/8/2P5/8/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18), (10, 26)}, pawn.pseudo_legal_moves)

    def test_cannot_move_more_than_two_steps_up_on_second_row_as_white(self):
        pawn = Board('8/8/8/8/8/1P1P4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 18), (10, 26)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_one_step_up_as_white(self):
        pawn = Board('8/8/8/8/8/1PpP4/2P5/8 w - - 0 1').get_piece(10)
        self.assertEqual(set(), pawn.pseudo_legal_moves)


if __name__ == '__main__':
    unittest.main()
