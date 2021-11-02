import unittest
from board import Piece, POS


class GeneralPieceConstructionTestCase(unittest.TestCase):
    piece1 = Piece(POS(35), True, 0)
    piece2 = Piece(POS(21), False, 1)

    def test_piece_pos_is_given_value(self):
        self.assertEqual(self.piece1._pos, 35)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(self.piece2._pos, 21)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, Piece, 64, True, 1)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, Piece, -1, True, 1)

    def test_piece_color_is_given_value(self):
        self.assertEqual(self.piece1._white_piece, True)

    def test_piece_color_is_any_given_value(self):
        self.assertEqual(self.piece2._white_piece, False)

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, Piece, True, True, 0)

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, Piece, 1, 1, 1)

    def test_raises_type_error_if_type_is_not_int(self):
        self.assertRaises(TypeError, Piece, 1, True, True)


class SpecificPieceConstructionTestCase(unittest.TestCase):
    def test_piece_type_is_given_value(self):
        piece = Piece(POS(35), True, 0)
        self.assertEqual(piece._type, 0)

    def test_piece_type_is_any_given_value(self):
        piece = Piece(POS(21), False, 1)
        self.assertEqual(piece._type, 1)

    def test_raises_value_error_if_type_value_is_too_high(self):
        self.assertRaises(ValueError, Piece, 63, True, -1)

    def test_raises_value_error_is_type_value_is_too_low(self):
        self.assertRaises(ValueError, Piece, 0, True, 6)


if __name__ == '__main__':
    unittest.main()
