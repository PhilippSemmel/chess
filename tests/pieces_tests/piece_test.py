import unittest

from board import Piece, Board

"""
tests can only be run when all abstract methods are commented out
"""


class TestPiece(Piece):
    def __init__(self, *args):
        super().__init__(*args)

    def pseudo_legal_moves(self, *args):
        pass

    def _BASE_VAL(self, *args):
        pass

    def _POS_VAL_MOD(self, *args):
        pass

    def pos_val(self, *args):
        pass


board = Board()
piece1 = TestPiece(35, True, board, '♟', 'P')
piece2 = TestPiece(21, False, board, '♘', 'n')


class ConstructionTestCase(unittest.TestCase):
    def test_pos_is_given_value(self):
        self.assertEqual(35, piece1._pos)

    def test_pos_is_any_given_value(self):
        self.assertEqual(21, piece2._pos)

    def test_color_is_given_value(self):
        self.assertTrue(piece1._white_piece)

    def test_color_is_any_given_value(self):
        self.assertFalse(piece2._white_piece)

    def test_capture_data_is_none(self):
        self.assertIsNone(piece1._capture_info)

    def test_capture_data_is_always_none(self):
        self.assertIsNone(piece2._capture_info)

    def test_symbol_is_given_value(self):
        self.assertEqual('♟', piece1._symbol)

    def test_symbol_is_any_given_value(self):
        self.assertEqual('♘', piece2._symbol)

    def test_fen_symbol_is_given_value(self):
        self.assertEqual('P', piece1._fen_symbol)

    def test_fen_symbol_is_any_given_value(self):
        self.assertEqual('n', piece2._fen_symbol)


class AttributeGetterTestCase(unittest.TestCase):
    def test_can_get_queen_pos(self):
        self.assertEqual(35, piece1.pos)

    def test_can_get_any_queen_pos(self):
        self.assertEqual(21, piece2.pos)

    def test_can_get_queen_color(self):
        self.assertTrue(piece1.white_piece)

    def test_can_get_any_queen_color(self):
        self.assertFalse(piece2.white_piece)

    def test_can_get_symbol(self):
        self.assertEqual('♟', piece1.symbol)

    def test_can_get_any_symbol(self):
        self.assertEqual('♘', piece2.symbol)

    def test_can_get_fen_symbol(self):
        self.assertEqual('P', piece1.fen_symbol)

    def test_can_get_any_fen_symbol(self):
        self.assertEqual('n', piece2.fen_symbol)

    def test_can_get_capture_data(self):
        self.assertIsNone(piece1.capture_info)

    def test_can_get_any_capture_data(self):
        piece = TestPiece(35, True, board, '♟', 'P')
        piece.capture(1, True)
        self.assertEqual((1, True), piece.capture_info)


class GetterTestCase(unittest.TestCase):
    def test_can_get_rank(self):
        self.assertEqual(4, piece1.rank)

    def test_can_get_any_rank(self):
        self.assertEqual(2, piece2.rank)

    def test_can_get_file(self):
        self.assertEqual(3, piece1.file)

    def test_can_get_any_file(self):
        self.assertEqual(5, piece2.file)

    def test_not_captured_if_capture_data_is_none(self):
        self.assertTrue(piece2.on_board)

    def test_captured_if_capture_data_is_not_not(self):
        piece1.capture(1, False)
        self.assertFalse(piece1.on_board)


class SetterTestCase(unittest.TestCase):
    def test_can_set_pos(self):
        piece1.move_to(0)
        self.assertEqual(0, piece1.pos)

    def test_can_set_any_pos(self):
        piece1.move_to(63)
        self.assertEqual(63, piece1.pos)

    def test_can_be_captured(self):
        piece1.capture(1, False)
        self.assertEqual((1, False), piece1._capture_info)

    def test_any_piece_can_be_captured(self):
        piece2.capture(2, True)
        self.assertEqual((2, True), piece2._capture_info)

    def test_can_reset_capture_data(self):
        piece = TestPiece(35, True, board, '♟', 'P')
        piece.capture(1, True)
        piece.uncapture()
        self.assertIsNone(piece.capture_info)


def main() -> None:
    unittest.main()


if __name__ == '__main__':
    main()
