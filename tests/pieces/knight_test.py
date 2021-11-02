import unittest
from board import Knight, Piece


knight1 = Knight(35, True)
knight2 = Knight(21, False)


class GeneralKnightConstructionTestCase(unittest.TestCase):
    def test_piece_pos_is_given_value(self):
        self.assertEqual(knight1._pos, 35)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(knight2._pos, 21)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, Knight, 64, True)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, Knight, -1, True)

    def test_piece_color_is_given_value(self):
        self.assertEqual(knight1._white_piece, True)

    def test_piece_color_is_any_given_value(self):
        self.assertEqual(knight2._white_piece, False)

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, Knight, True, True, 0)

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, Knight, 1, 1, 1)

    def test_raises_type_error_if_type_is_not_int(self):
        self.assertRaises(TypeError, Knight, 1, True, True)


class SpecificKnightConstructionTestCase(unittest.TestCase):
    def test_queen_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Knight, Piece))

    def test_piece_type_is_queen_code(self):
        self.assertEqual(knight1._type, 1)


class GeneralKnightGetterTestCase(unittest.TestCase):
    def test_can_get_queen_pos(self):
        self.assertEqual(knight1.pos, 35)

    def test_can_get_any_queen_pos(self):
        self.assertEqual(knight2.pos, 21)

    def test_can_get_queen_color(self):
        self.assertTrue(knight1.color)

    def test_can_get_any_queen_color(self):
        self.assertFalse(knight2.color)


if __name__ == '__main__':
    unittest.main()
