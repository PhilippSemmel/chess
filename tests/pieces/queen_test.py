import unittest
from board import Queen, Piece, Board


queen1 = Queen(35, True)
queen2 = Queen(21, False)


class GeneralQueenConstructionTestCase(unittest.TestCase):

    def test_piece_pos_is_given_value(self):
        self.assertEqual(queen1._pos, 35)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(queen2._pos, 21)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, Queen, 64, True)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, Queen, -1, True)

    def test_piece_color_is_given_value(self):
        self.assertEqual(queen1._white_piece, True)

    def test_piece_color_is_any_given_value(self):
        self.assertEqual(queen2._white_piece, False)

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, Queen, True, True, 0)

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, Queen, 1, 1, 1)

    def test_raises_type_error_if_type_is_not_int(self):
        self.assertRaises(TypeError, Queen, 1, True, True)


class SpecificQueenConstructionTestCase(unittest.TestCase):
    def test_queen_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Queen, Piece))

    def test_piece_type_is_queen_code(self):
        self.assertEqual(queen1._type, 4)


class GeneralQueenGetterTestCase(unittest.TestCase):
    def test_can_get_queen_pos(self):
        self.assertEqual(queen1.pos, 35)

    def test_can_get_any_queen_pos(self):
        self.assertEqual(queen2.pos, 21)

    def test_can_get_queen_color(self):
        self.assertTrue(queen1.color)

    def test_can_get_any_queen_color(self):
        self.assertFalse(queen2.color)


# class VerticalAndHorizontalQueenMovesGenerationTestCase(unittest.TestCase):
#     def test_queen_cannot_move_when_trapped_by_own_pieces(self):
#         board = Board()
#         board.parse_fen('8/8/2PPP3/2PQP3/2PPP3/8/8/8 w - - 0 1')


if __name__ == '__main__':
    unittest.main()
