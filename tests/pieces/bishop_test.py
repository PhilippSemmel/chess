import unittest
from board import Bishop, Piece, Board


board = Board()
bishop1 = Bishop(35, True, board)
bishop2 = Bishop(21, False, board)


class GeneralBishopConstructionTestCase(unittest.TestCase):
    def test_piece_pos_is_given_value(self):
        self.assertEqual(35, bishop1._pos)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(21, bishop2._pos)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, Bishop, 64, True, board)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, Bishop, -1, True, board)

    def test_piece_color_is_given_value(self):
        self.assertTrue(bishop1._white_piece)

    def test_piece_color_is_any_given_value(self):
        self.assertFalse(bishop2._white_piece)

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, Bishop, True, True, board)

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, Bishop, 1, 1, board)

    # def test_raises_type_error_if_board_is_not_board(self):
    #     self.assertRaises(TypeError, Bishop, 1, True, 1)


class SpecificBishopConstructionTestCase(unittest.TestCase):
    def test_queen_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Bishop, Piece))

    def test_piece_type_is_queen_code(self):
        self.assertEqual(2, bishop1._type)


class GeneralBishopAttributeGetterTestCase(unittest.TestCase):
    def test_can_get_queen_pos(self):
        self.assertEqual(35, bishop1.pos)

    def test_can_get_any_queen_pos(self):
        self.assertEqual(21, bishop2.pos)

    def test_can_get_queen_color(self):
        self.assertTrue(bishop1.color)

    def test_can_get_any_queen_color(self):
        self.assertFalse(bishop2.color)


if __name__ == '__main__':
    unittest.main()
