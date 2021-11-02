import unittest
from board import Board


board0 = Board()
board1 = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1')
board2 = Board('rnbqkbnr/ppppp1pp/8/5p2/5P2/8/PPPPP1PP/RNBQKBNR b KQkq f6 2 2')


class BoardConstructionTestCase(unittest.TestCase):
    def test_color_to_move_is_white_after_construction(self):
        self.assertTrue(board0._white_to_move)

    def test_all_castling_rights_available_after_construction(self):
        self.assertEqual(15, board0._castling_rights)

    def test_ep_target_square_is_none_after_construction(self):
        self.assertIsNone(board0._ep_target_square)

    def test_half_move_clock_is_zero(self):
        self.assertEqual(0, board0._half_move_clock)

    def test_turn_number_is_one_after_construction(self):
        self.assertEqual(1, board0._turn_number)


class BoardAttributeGetterTestCase(unittest.TestCase):
    def test_can_get_pieces(self):
        self.assertEqual(board1._pieces, board1.pieces)

    def test_can_get_any_pieces(self):
        self.assertEqual(board2._pieces, board2.pieces)

    def test_can_get_color_to_move(self):
        self.assertTrue(board1.color_to_move)

    def test_can_get_any_color_to_move(self):
        self.assertFalse(board2.color_to_move)

    def test_can_get_castling_rights(self):
        self.assertEqual(board1._castling_rights, board1.castling_rights)

    def test_can_get_any_castling_rights(self):
        self.assertEqual(board2._castling_rights, board2.castling_rights)

    def test_can_get_ep_target_square(self):
        self.assertIsNone(board1._ep_target_square, board1.ep_target_square)

    def test_can_get_any_ep_target_square(self):
        self.assertEqual(board2._ep_target_square, board2.ep_target_square)

    def test_can_get_half_move_clock(self):
        self.assertEqual(board1._half_move_clock, board1.half_move_clock)

    def test_can_get_any_half_move_clock(self):
        self.assertEqual(board2._half_move_clock, board2.half_move_clock)

    def test_can_get_turn_number(self):
        self.assertEqual(board1._turn_number, board1.turn_number)

    def test_can_get_any_turn_number(self):
        self.assertEqual(board2._turn_number, board2.turn_number)


class BoardGetPieceTestCase(unittest.TestCase):
    def test_can_get_piece_on_pos(self):
        rook = None
        for piece in board1.pieces:
            if piece.pos == 0:
                rook = piece
                break
        self.assertIs(rook, board1.get_piece(0))

    def test_can_get_any_piece_on_pos(self):
        rook = None
        for piece in board1.pieces:
            if piece.pos == 7:
                rook = piece
                break
        self.assertIs(rook, board1.get_piece(7))

    # def test_raises_value_error_if_no_piece_found_on_position(self):
    #     self.assertEqual(ValueError, board1.get_piece, 16)


class BoardPositionsStateTestCase(unittest.TestCase):
    def test_square_is_empty_if_square_is_empty(self):
        self.assertTrue(board1.is_square_empty(37))

    def test_square_is_not_empty_if_black_piece_on_square(self):
        self.assertFalse(board2.is_square_empty(37))

    def test_square_is_not_empty_if_white_piece_on_square(self):
        self.assertFalse(board2.is_square_empty(29))

    def test_own_piece_on_square_if_own_piece_on_square(self):
        self.assertTrue(board1.own_piece_on_square(0, True))

    def test_not_own_piece_on_square_if_square_is_empty(self):
        self.assertFalse(board1.own_piece_on_square(16, True))

    def test_not_own_piece_on_square_if_opponents_piece_on_square(self):
        self.assertFalse(board1.own_piece_on_square(63, True))

    def test_opponent_piece_on_square_if_opponent_piece_on_square(self):
        self.assertTrue(board1.opponent_piece_on_square(63, True))

    def test_not_opponent_piece_on_square_if_square_is_empty(self):
        self.assertFalse(board1.opponent_piece_on_square(16, True))

    def test_not_opponent_piece_on_square_if_own_piece_on_square(self):
        self.assertFalse(board1.opponent_piece_on_square(0, True))


if __name__ == '__main__':
    unittest.main()
