import unittest
from board import Board


board0 = Board()
board1 = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1')
board2 = Board('rnbqkbnr/ppppp1pp/8/4p3/5P2/8/PPPPP1PP/RNBQKBNR b KQkq f5 2 2')


class BoardConstructionTestCase(unittest.TestCase):
    def test_initializes_standard_piece_positions(self):
        self.assertTrue(board0.get_piece(0).type == 3)
        self.assertTrue(board0.get_piece(1).type == 1)
        self.assertTrue(board0.get_piece(2).type == 2)
        self.assertTrue(board0.get_piece(3).type == 4)
        self.assertTrue(board0.get_piece(4).type == 5)
        self.assertTrue(board0.get_piece(5).type == 2)
        self.assertTrue(board0.get_piece(6).type == 1)
        self.assertTrue(board0.get_piece(7).type == 3)
        self.assertTrue(board0.get_piece(8).type == 0)
        self.assertTrue(board0.get_piece(9).type == 0)
        self.assertTrue(board0.get_piece(10).type == 0)
        self.assertTrue(board0.get_piece(11).type == 0)
        self.assertTrue(board0.get_piece(12).type == 0)
        self.assertTrue(board0.get_piece(13).type == 0)
        self.assertTrue(board0.get_piece(14).type == 0)
        self.assertTrue(board0.get_piece(15).type == 0)
        self.assertTrue(board0.get_piece(48).type == 0)
        self.assertTrue(board0.get_piece(49).type == 0)
        self.assertTrue(board0.get_piece(50).type == 0)
        self.assertTrue(board0.get_piece(51).type == 0)
        self.assertTrue(board0.get_piece(52).type == 0)
        self.assertTrue(board0.get_piece(53).type == 0)
        self.assertTrue(board0.get_piece(54).type == 0)
        self.assertTrue(board0.get_piece(55).type == 0)
        self.assertTrue(board0.get_piece(56).type == 3)
        self.assertTrue(board0.get_piece(57).type == 1)
        self.assertTrue(board0.get_piece(58).type == 2)
        self.assertTrue(board0.get_piece(59).type == 4)
        self.assertTrue(board0.get_piece(60).type == 5)
        self.assertTrue(board0.get_piece(61).type == 2)
        self.assertTrue(board0.get_piece(62).type == 1)
        self.assertTrue(board0.get_piece(63).type == 3)

    def test_color_to_move_is_white(self):
        self.assertTrue(board0._white_to_move)

    def test_all_castling_rights_available(self):
        self.assertEqual([True, True, True, True], board0._castling_rights)

    def test_ep_target_square_is_none(self):
        self.assertIsNone(board0._ep_target_square)

    def test_half_move_clock_is_zero(self):
        self.assertEqual(0, board0._half_move_clock)

    def test_turn_number_is_one(self):
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

    def test_raises_value_error_if_no_piece_found_on_position(self):
        self.assertRaises(ValueError, board1.get_piece, 16)


class BoardPositionsStateTestCase(unittest.TestCase):
    def test_square_is_empty_if_square_is_empty(self):
        self.assertTrue(board1.is_square_empty(36))

    def test_square_is_not_empty_if_black_piece_on_square(self):
        self.assertFalse(board2.is_square_empty(36))

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

    def test_square_is_not_attacked_if_not_attacked_by_opponent_piece(self):
        board = Board('8/8/8/8/8/8/8/8 w - - 0 1')
        self.assertFalse(board.is_square_attacked(0, True))

    def test_square_is_attacked_if_attacked_by_opponent_piece(self):
        board = Board('8/8/8/8/8/8/1q6/8 w - - 0 1')
        self.assertTrue(board.is_square_attacked(0, True))

    def test_square_is_attacked_if_attacked_by_opponent_piece_on_any_square(self):
        board = Board('7q/8/8/8/8/8/8/8 w - - 0 1')
        self.assertTrue(board.is_square_attacked(0, True))

    def test_square_is_attacked_if_attacked_by_only_opponent_piece_of_many_pieces(self):
        board = Board('pppppppq/pppppp1p/ppppp1pp/pppp1ppp/ppp1pppp/pp1ppppp/p1pppppp/1ppppppp w - - 0 1')
        self.assertTrue(board.is_square_attacked(0, True))

    def test_any_square_is_attacked_if_attacked_by_opponent_piece(self):
        board = Board('8/1q6/8/8/8/8/8/8 w - - 0 1')
        self.assertTrue(board.is_square_attacked(7, True))

    def test_square_is_not_attacked_if_attacked_by_own_piece(self):
        board = Board('7Q/8/8/8/8/8/8/8 w - - 0 1')
        self.assertFalse(board.is_square_attacked(7, True))


class BoardMoveGeneration(unittest.TestCase):
    # general
    def test_generates_no_moves_if_board_is_emtpy(self):
        board = Board('8/8/8/8/8/8/8/8 w - - 0 1')
        self.assertEqual(set(), board.legal_moves)

    def test_cannot_generate_black_moves_when_white_to_move(self):
        board = Board('8/p7/8/8/8/8/8/8 w - - 0 1')
        self.assertEqual(set(), board.legal_moves)

    # white pieces
    def test_can_generate_multiple_white_moves(self):
        board = Board('8/8/8/8/1P1PP3/8/KQB5/N1RN4 w - - 0 1')
        self.assertEqual({(0, 17), (2, 1), (3, 18), (3, 20), (3, 13), (8, 1), (8, 16), (8, 17), (9, 16), (9, 17),
                          (9, 18), (9, 1), (10, 1), (10, 17), (10, 19), (10, 24), (25, 33), (27, 35), (28, 36)},
                         board.legal_moves)

    def test_can_generate_white_pawn_moves(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 0 1')
        self.assertEqual({(8, 16), (8, 24)}, board.legal_moves)

    def test_can_generate_any_white_pawn_moves(self):
        board = Board('8/8/8/8/4P3/8/8/8 w - - 0 1')
        self.assertEqual({(28, 36)}, board.legal_moves)

    def test_can_generate_white_knight_moves(self):
        board = Board('8/8/8/8/8/8/8/N7 w - - 0 1')
        self.assertEqual({(0, 10), (0, 17)}, board.legal_moves)

    def test_can_generate_any_white_knight_moves(self):
        board = Board('8/8/8/8/8/8/8/7N w - - 0 1')
        self.assertEqual({(7, 13), (7, 22)}, board.legal_moves)

    def test_can_generate_white_bishop_moves(self):
        board = Board('8/8/8/8/8/8/1B6/8 w - - 0 1')
        self.assertEqual({(9, 0), (9, 18), (9, 27), (9, 36), (9, 45), (9, 54), (9, 63), (9, 2), (9, 16)},
                         board.legal_moves)

    def test_can_generate_any_white_bishop_moves(self):
        board = Board('8/8/8/8/8/8/6B1/8 w - - 0 1')
        self.assertEqual({(14, 7), (14, 21), (14, 28), (14, 35), (14, 42), (14, 49), (14, 56), (14, 23), (14, 5)},
                         board.legal_moves)

    def test_can_generate_white_rook_moves(self):
        board = Board('8/8/8/8/8/8/1R6/8 w - - 0 1')
        self.assertEqual({(9, 1), (9, 8), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 17), (9, 25),
                          (9, 33), (9, 41), (9, 49), (9, 57)}, board.legal_moves)

    def test_can_generate_any_white_rook_moves(self):
        board = Board('8/8/8/8/8/8/6R1/8 w - - 0 1')
        self.assertEqual({(14, 15), (14, 6), (14, 13), (14, 12), (14, 11), (14, 10), (14, 9), (14, 8), (14, 22),
                          (14, 30), (14, 38), (14, 46), (14, 54), (14, 62)}, board.legal_moves)

    def test_can_generate_white_queen_moves(self):
        board = Board('8/8/8/8/8/8/1Q6/8 w - - 0 1')
        self.assertEqual({(9, 1), (9, 8), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 17), (9, 25),
                          (9, 33), (9, 41), (9, 49), (9, 57), (9, 0), (9, 18), (9, 27), (9, 36), (9, 45), (9, 54),
                          (9, 63), (9, 2), (9, 16)}, board.legal_moves)

    def test_can_generate_any_white_queen_moves(self):
        board = Board('8/8/8/8/8/8/6Q1/8 w - - 0 1')
        self.assertEqual({(14, 15), (14, 6), (14, 13), (14, 12), (14, 11), (14, 10), (14, 9), (14, 8), (14, 22),
                          (14, 30), (14, 38), (14, 46), (14, 54), (14, 62), (14, 7), (14, 21), (14, 28), (14, 35),
                          (14, 42), (14, 49), (14, 56), (14, 23), (14, 5)}, board.legal_moves)

    def test_can_generate_white_king_moves(self):
        board = Board('8/8/8/8/8/8/1K6/8 w - - 0 1')
        self.assertEqual({(9, 0), (9, 1), (9, 2), (9, 8), (9, 10), (9, 16), (9, 17), (9, 18)}, board.legal_moves)

    def test_can_generate_any_white_king_moves(self):
        board = Board('8/8/8/8/8/8/6K1/8 w - - 0 1')
        self.assertEqual({(14, 5), (14, 6), (14, 7), (14, 13), (14, 15), (14, 21), (14, 22), (14, 23)},
                         board.legal_moves)

    # black pieces
    def test_can_generate_multiple_black_moves(self):
        board = Board('8/8/8/8/1p1pp3/8/kqb5/n1rn4 b - - 0 1')
        self.assertEqual({(0, 17), (2, 1), (3, 18), (3, 20), (3, 13), (8, 1), (8, 16), (8, 17), (9, 16), (9, 17),
                          (9, 18), (9, 1), (10, 1), (10, 17), (10, 19), (10, 24), (25, 17), (27, 19), (28, 20)},
                         board.legal_moves)

    def test_can_generate_black_pawn_moves(self):
        board = Board('8/p7/8/8/8/8/8/8 b - - 0 1')
        self.assertEqual({(48, 40), (48, 32)}, board.legal_moves)

    def test_can_generate_any_black_pawn_moves(self):
        board = Board('8/8/2p5/8/8/8/8/8 b - - 0 1')
        self.assertEqual({(42, 34)}, board.legal_moves)

    def test_can_generate_black_knight_moves(self):
        board = Board('8/8/8/8/8/8/8/n7 b - - 0 1')
        self.assertEqual({(0, 10), (0, 17)}, board.legal_moves)

    def test_can_generate_any_black_knight_moves(self):
        board = Board('8/8/8/8/8/8/8/7n b - - 0 1')
        self.assertEqual({(7, 13), (7, 22)}, board.legal_moves)

    def test_can_generate_black_bishop_moves(self):
        board = Board('8/8/8/8/8/8/1b6/8 b - - 0 1')
        self.assertEqual({(9, 0), (9, 18), (9, 27), (9, 36), (9, 45), (9, 54), (9, 63), (9, 2), (9, 16)},
                         board.legal_moves)

    def test_can_generate_any_black_bishop_moves(self):
        board = Board('8/8/8/8/8/8/6b1/8 b - - 0 1')
        self.assertEqual({(14, 7), (14, 21), (14, 28), (14, 35), (14, 42), (14, 49), (14, 56), (14, 23), (14, 5)},
                         board.legal_moves)

    def test_can_generate_black_rook_moves(self):
        board = Board('8/8/8/8/8/8/1r6/8 b - - 0 1')
        self.assertEqual({(9, 1), (9, 8), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 17), (9, 25),
                          (9, 33), (9, 41), (9, 49), (9, 57)}, board.legal_moves)

    def test_can_generate_any_black_rook_moves(self):
        board = Board('8/8/8/8/8/8/6r1/8 b - - 0 1')
        self.assertEqual({(14, 15), (14, 6), (14, 13), (14, 12), (14, 11), (14, 10), (14, 9), (14, 8), (14, 22),
                          (14, 30), (14, 38), (14, 46), (14, 54), (14, 62)}, board.legal_moves)

    def test_can_generate_black_queen_moves(self):
        board = Board('8/8/8/8/8/8/1q6/8 b - - 0 1')
        self.assertEqual({(9, 1), (9, 8), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 17), (9, 25),
                          (9, 33), (9, 41), (9, 49), (9, 57), (9, 0), (9, 18), (9, 27), (9, 36), (9, 45), (9, 54),
                          (9, 63), (9, 2), (9, 16)}, board.legal_moves)

    def test_can_generate_any_black_queen_moves(self):
        board = Board('8/8/8/8/8/8/6q1/8 b - - 0 1')
        self.assertEqual({(14, 15), (14, 6), (14, 13), (14, 12), (14, 11), (14, 10), (14, 9), (14, 8), (14, 22),
                          (14, 30), (14, 38), (14, 46), (14, 54), (14, 62), (14, 7), (14, 21), (14, 28), (14, 35),
                          (14, 42), (14, 49), (14, 56), (14, 23), (14, 5)}, board.legal_moves)

    def test_can_generate_black_king_moves(self):
        board = Board('8/8/8/8/8/8/1k6/8 b - - 0 1')
        self.assertEqual({(9, 0), (9, 1), (9, 2), (9, 8), (9, 10), (9, 16), (9, 17), (9, 18)}, board.legal_moves)

    def test_can_generate_any_black_king_moves(self):
        board = Board('8/8/8/8/8/8/6k1/8 b - - 0 1')
        self.assertEqual({(14, 5), (14, 6), (14, 7), (14, 13), (14, 15), (14, 21), (14, 22), (14, 23)},
                         board.legal_moves)


if __name__ == '__main__':
    unittest.main()
