import unittest
from board import Knight, Piece, Board


board = Board()
knight1 = Knight(35, True, board)
knight2 = Knight(21, False, board)


class GeneralKnightConstructionTestCase(unittest.TestCase):
    def test_piece_pos_is_given_value(self):
        self.assertEqual(35, knight1._pos)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(21, knight2._pos)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, Knight, 64, True, board)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, Knight, -1, True, board)

    def test_piece_color_is_given_value(self):
        self.assertTrue(knight1._white_piece)

    def test_piece_color_is_any_given_value(self):
        self.assertFalse(knight2._white_piece)

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, Knight, True, True, board)

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, Knight, 1, 1, board)

    # def test_raises_type_error_if_board_is_not_board(self):
    #     self.assertRaises(TypeError, Knight, 1, True, 1)


class SpecificKnightConstructionTestCase(unittest.TestCase):
    def test_queen_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Knight, Piece))

    def test_piece_type_is_queen_code(self):
        self.assertEqual(1, knight1._type)


if __name__ == '__main__':
    unittest.main()
