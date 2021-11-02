import unittest
from board import King, Piece


king1 = King(35, True)
king2 = King(21, False)


class GeneralKingConstructionTestCase(unittest.TestCase):
    def test_piece_pos_is_given_value(self):
        self.assertEqual(king1._pos, 35)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(king2._pos, 21)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, King, 64, True)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, King, -1, True)

    def test_piece_color_is_given_value(self):
        self.assertEqual(king1._white_piece, True)

    def test_piece_color_is_any_given_value(self):
        self.assertEqual(king2._white_piece, False)

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, King, True, True, 0)

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, King, 1, 1, 1)

    def test_raises_type_error_if_type_is_not_int(self):
        self.assertRaises(TypeError, King, 1, True, True)


class SpecificKingConstructionTestCase(unittest.TestCase):
    def test_queen_is_subclass_of_piece(self):
        self.assertTrue(issubclass(King, Piece))

    def test_piece_type_is_queen_code(self):
        self.assertEqual(king1._type, 5)


class GeneralKingGetterTestCase(unittest.TestCase):
    def test_can_get_queen_pos(self):
        self.assertEqual(king1.pos, 35)

    def test_can_get_any_queen_pos(self):
        self.assertEqual(king2.pos, 21)

    def test_can_get_queen_color(self):
        self.assertTrue(king1.color)

    def test_can_get_any_queen_color(self):
        self.assertFalse(king2.color)


if __name__ == '__main__':
    unittest.main()
