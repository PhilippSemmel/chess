import unittest
from board import Board


board0 = Board()
board1 = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1')
board2 = Board('rnbqkbnr/ppppp1pp/8/5p2/5P2/8/PPPPP1PP/RNBQKBNR b KQkq f6 2 2')


class BoardConstructionTestCase(unittest.TestCase):
    def test_color_to_move_is_white_after_construction(self):
        self.assertTrue(board0._white_to_move)

    def test_turn_number_is_one_after_construction(self):
        self.assertEqual(board0._turn_number, 1)

    def test_all_castling_rights_available_after_construction(self):
        self.assertEqual(board0._castling_rights, 15)

    def test_ep_target_square_is_none_after_construction(self):
        self.assertIsNone(board0._ep_target_square)

    def test_half_move_clock_is_zero(self):
        self.assertEqual(board0._half_move_clock, 0)


class BoardAttributeGetterTestCase(unittest.TestCase):
    def test_can_get_pieces(self):
        self.assertEqual(board1.pieces, board1._pieces)

    def test_can_get_any_pieces(self):
        self.assertEqual(board2.pieces, board2._pieces)

    def test_can_get_color_to_move(self):
        self.assertTrue(board1.color_to_move)

    def test_can_get_any_color_to_move(self):
        self.assertFalse(board2.color_to_move)

    def test_can_get_castling_rights(self):
        self.assertEqual(board1.castling_rights, board1._castling_rights)

    def test_can_get_any_castling_rights(self):
        self.assertEqual(board2.castling_rights, board2._castling_rights)

    def test_can_get_ep_target_square(self):
        self.assertIsNone(board1.ep_target_square, board1._ep_target_square)

    def test_can_get_any_ep_target_square(self):
        self.assertEqual(board2.ep_target_square, board2._ep_target_square)

    def test_can_get_half_move_clock(self):
        self.assertEqual(board1.half_move_clock, board1._half_move_clock)

    def test_can_get_any_half_move_clock(self):
        self.assertEqual(board2.half_move_clock, board2._half_move_clock)

    def test_can_get_turn_number(self):
        self.assertEqual(board1.turn_number, board1._turn_number)

    def test_can_get_any_turn_number(self):
        self.assertEqual(board2.turn_number, board2._turn_number)


class BoardGetPieceTestCase(unittest.TestCase):
    def test_can_get_piece_on_pos(self):
        rook = None
        for piece in board1.pieces:
            if piece.pos == 0:
                rook = piece
                break
        self.assertIs(board1.get_piece(0), rook)

    def test_can_get_any_piece_on_pos(self):
        rook = None
        for piece in board1.pieces:
            if piece.pos == 7:
                rook = piece
                break
        self.assertIs(board1.get_piece(7), rook)

    # def test_raises_value_error_if_no_piece_found_on_position(self):
    #     self.assertEqual(ValueError, board1.get_piece, 16)


if __name__ == '__main__':
    unittest.main()
