import unittest
from board import Queen, POS, Piece, Board


class GeneralQueenConstructionTestCase(unittest.TestCase):
    queen1 = Queen(POS(35), True)
    queen2 = Queen(POS(21), False)

    def test_piece_pos_is_given_value(self):
        self.assertEqual(self.queen1._pos, 35)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(self.queen2._pos, 21)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, Queen, 64, True)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, Queen, -1, True)

    def test_piece_color_is_given_value(self):
        self.assertEqual(self.queen1._white_piece, True)

    def test_piece_color_is_any_given_value(self):
        self.assertEqual(self.queen2._white_piece, False)

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
        self.assertEqual(Queen(POS(1), True)._type, 4)


class VerticalAndHorizontalQueenMoveGeneration(unittest.TestCase):
    def test_queen_cannot_move_when_trapped_by_own_pieces(self):
        board = Board()
        board.parse_fen('8/8/2PPP3/2PQP3/2PPP3/8/8/8 w KQkq - 0 1')



if __name__ == '__main__':
    unittest.main()
