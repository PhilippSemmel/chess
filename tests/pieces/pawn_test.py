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


if __name__ == '__main__':
    unittest.main()
