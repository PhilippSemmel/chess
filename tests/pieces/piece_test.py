import unittest
from board import Piece, Board

"""
tests can only be run when all abstract methods are commented out
"""


board = Board()
piece1 = Piece(35, True, 0, board, '♟', 'P')
piece2 = Piece(21, False, 1, board, '♘', 'n')


class PieceConstructionTestCase(unittest.TestCase):
    def test_piece_pos_is_given_value(self):
        self.assertEqual(35, piece1._pos)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(21, piece2._pos)

    def test_piece_color_is_given_value(self):
        self.assertTrue(piece1._white_piece)

    def test_piece_color_is_any_given_value(self):
        self.assertFalse(piece2._white_piece)

    def test_piece_type_is_given_value(self):
        self.assertEqual(0, piece1._type)

    def test_piece_type_is_any_given_value(self):
        self.assertEqual(1, piece2._type)

    def test_piece_symbol_is_given_value(self):
        self.assertEqual('♟', piece1._symbol)

    def test_piece_symbol_is_any_given_value(self):
        self.assertEqual('♘', piece2._symbol)

    def test_piece_fen_symbol_is_given_value(self):
        self.assertEqual('P', piece1._fen_symbol)

    def test_piece_fen_symbol_is_any_given_value(self):
        self.assertEqual('n', piece2._fen_symbol)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, Piece, 64, True, 1, board, '♞', 'N')

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, Piece, -1, True, 1, board, '♞', 'N')

    def test_raises_value_error_if_type_value_is_too_high(self):
        self.assertRaises(ValueError, Piece, 63, True, -1, board, '♞', 'N')

    def test_raises_value_error_is_type_value_is_too_low(self):
        self.assertRaises(ValueError, Piece, 0, True, 6, board, '♞', 'N')

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, Piece, True, True, 1, board, '♞', 'N')

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, Piece, 1, 1, 1, board, '♞', 'N')

    def test_raises_type_error_if_type_is_not_int(self):
        self.assertRaises(TypeError, Piece, 1, True, True, board, '♞', 'N')

    # def test_raises_type_error_if_board_is_not_board(self):
    #     self.assertRaises(TypeError, Piece, 1, True, 1, 1)


class PieceAttributeGetterTestCase(unittest.TestCase):
    def test_can_get_queen_pos(self):
        self.assertEqual(35, piece1.pos)

    def test_can_get_any_queen_pos(self):
        self.assertEqual(21, piece2.pos)

    def test_can_get_queen_color(self):
        self.assertTrue(piece1.white_piece)

    def test_can_get_any_queen_color(self):
        self.assertFalse(piece2.white_piece)

    def test_can_get_piece_type(self):
        self.assertEqual(0, piece1.type)

    def test_can_get_any_piece_type(self):
        self.assertEqual(1, piece2.type)

    def test_can_get_symbol(self):
        self.assertEqual('♟', piece1.symbol)

    def test_can_get_any_symbol(self):
        self.assertEqual('♘', piece2.symbol)

    def test_can_get_fen_symbol(self):
        self.assertEqual('P', piece1.fen_symbol)

    def test_can_get_any_fen_symbol(self):
        self.assertEqual('n', piece2.fen_symbol)


class PieceGetterTestCase(unittest.TestCase):
    def test_can_get_rank(self):
        self.assertEqual(4, piece1._rank)

    def test_can_get_any_rank(self):
        self.assertEqual(2, piece2._rank)

    def test_can_get_file(self):
        self.assertEqual(3, piece1._file)

    def test_can_get_any_file(self):
        self.assertEqual(5, piece2._file)


class PieceSetterTestCase(unittest.TestCase):
    def test_can_set_pos(self):
        piece1.move_to(0)
        self.assertEqual(0, piece1.pos)

    def test_can_set_any_pos(self):
        piece1.move_to(63)
        self.assertEqual(63, piece1.pos)

    def test_raises_value_error_if_pos_value_too_high(self):
        self.assertRaises(ValueError, piece1.move_to, 64)

    def test_raises_value_error_if_pos_value_too_low(self):
        self.assertRaises(ValueError, piece1.move_to, -1)

    def test_raises_type_error_if_pos_value_not_int(self):
        self.assertRaises(TypeError, piece1.move_to, True)


if __name__ == '__main__':
    unittest.main()
