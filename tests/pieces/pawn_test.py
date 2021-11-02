import unittest
from board import Pawn, Piece, Board


board = Board()
pawn1 = Pawn(35, True, board)
pawn2 = Pawn(21, False, board)


class GeneralPawnConstructionTestCase(unittest.TestCase):
    def test_piece_pos_is_given_value(self):
        self.assertEqual(35, pawn1._pos)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(21, pawn2._pos)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, Pawn, 64, True, board)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, Pawn, -1, True, board)

    def test_piece_color_is_given_value(self):
        self.assertTrue(pawn1._white_piece)

    def test_piece_color_is_any_given_value(self):
        self.assertFalse(pawn2._white_piece)

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, Pawn, True, True, board)

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, Pawn, 1, 1, board)

    # def test_raises_type_error_if_board_is_not_board(self):
    #     self.assertRaises(TypeError, Pawn, 1, True, 1)


class SpecificPawnConstructionTestCase(unittest.TestCase):
    def test_queen_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Pawn, Piece))

    def test_piece_type_is_queen_code(self):
        self.assertEqual(0, pawn1._type)


class GeneralPawnAttributeGetterTestCase(unittest.TestCase):
    def test_can_get_queen_pos(self):
        self.assertEqual(35, pawn1.pos)

    def test_can_get_any_queen_pos(self):
        self.assertEqual(21, pawn2.pos)

    def test_can_get_queen_color(self):
        self.assertTrue(pawn1.color)

    def test_can_get_any_queen_color(self):
        self.assertFalse(pawn2.color)


if __name__ == '__main__':
    unittest.main()
