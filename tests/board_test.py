import unittest
from board import Board


board1 = Board()
board2 = Board('rnbqkbnr/ppppp1pp/8/4p3/5P2/8/PPPPP1PP/RNBQKBNR b - f5 2 2')


class ConstructionTestCase(unittest.TestCase):
    def test_initializes_standard_piece_positions(self):
        self.assertTrue(board1._get_piece(0).type == 3)
        self.assertTrue(board1._get_piece(1).type == 1)
        self.assertTrue(board1._get_piece(2).type == 2)
        self.assertTrue(board1._get_piece(3).type == 4)
        self.assertTrue(board1._get_piece(4).type == 5)
        self.assertTrue(board1._get_piece(5).type == 2)
        self.assertTrue(board1._get_piece(6).type == 1)
        self.assertTrue(board1._get_piece(7).type == 3)
        self.assertTrue(board1._get_piece(8).type == 0)
        self.assertTrue(board1._get_piece(9).type == 0)
        self.assertTrue(board1._get_piece(10).type == 0)
        self.assertTrue(board1._get_piece(11).type == 0)
        self.assertTrue(board1._get_piece(12).type == 0)
        self.assertTrue(board1._get_piece(13).type == 0)
        self.assertTrue(board1._get_piece(14).type == 0)
        self.assertTrue(board1._get_piece(15).type == 0)
        self.assertTrue(board1._get_piece(48).type == 0)
        self.assertTrue(board1._get_piece(49).type == 0)
        self.assertTrue(board1._get_piece(50).type == 0)
        self.assertTrue(board1._get_piece(51).type == 0)
        self.assertTrue(board1._get_piece(52).type == 0)
        self.assertTrue(board1._get_piece(53).type == 0)
        self.assertTrue(board1._get_piece(54).type == 0)
        self.assertTrue(board1._get_piece(55).type == 0)
        self.assertTrue(board1._get_piece(56).type == 3)
        self.assertTrue(board1._get_piece(57).type == 1)
        self.assertTrue(board1._get_piece(58).type == 2)
        self.assertTrue(board1._get_piece(59).type == 4)
        self.assertTrue(board1._get_piece(60).type == 5)
        self.assertTrue(board1._get_piece(61).type == 2)
        self.assertTrue(board1._get_piece(62).type == 1)
        self.assertTrue(board1._get_piece(63).type == 3)

    def test_color_to_move_is_white(self):
        self.assertTrue(board1._white_to_move)

    def test_all_castling_rights_available(self):
        self.assertEqual([True, True, True, True], board1._castling_rights)

    def test_ep_target_square_is_none(self):
        self.assertIsNone(board1._ep_target_square)

    def test_half_move_clock_is_zero(self):
        self.assertEqual(0, board1._half_move_clock)

    def test_turn_number_is_one(self):
        self.assertEqual(1, board1._turn_number)

    def test_positions_is_empty_list(self):
        self.assertEqual([], board1._positions)

    def test_moves_is_empty_list(self):
        self.assertEqual([], board1._moves)


class AttributeGetterTestCase(unittest.TestCase):
    def test_can_get_pieces(self):
        self.assertEqual(board1._pieces, board1.pieces)

    def test_can_get_any_pieces(self):
        self.assertEqual(board2._pieces, board2.pieces)

    def test_can_get_color_to_move(self):
        self.assertTrue(board1.white_to_move)

    def test_can_get_any_color_to_move(self):
        self.assertFalse(board2.white_to_move)

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


class OtherGetterTestCase(unittest.TestCase):
    def test_all_pieces_on_board_in_active_pieces_set(self):
        board = Board('8/8/8/8/8/8/8/P7 w - - 0 1')
        piece = board._get_piece(0)
        self.assertEqual({piece}, board._active_pieces)

    def test_captured_piece_are_not_in_active_pieces_set(self):
        board = Board('8/8/8/8/8/8/8/P7 w - - 0 1')
        piece = board._get_piece(0)
        piece.capture(1, True)
        self.assertEqual(set(), board._active_pieces)

    def test_promoted_piece_are_not_in_active_pieces_set(self):
        board = Board('8/8/8/8/8/8/8/P7 w - - 0 1')
        piece = board._get_piece(0)
        piece.promote(1, True)
        self.assertEqual(set(), board._active_pieces)

    def test_no_checkmate_if_more_than_one_move_available(self):
        board = Board('8/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertFalse(board.checkmate)

    def test_checkmate_if_no_move_available_and_king_in_check(self):
        board = Board('8/8/8/8/8/2b5/1q6/K7 w - - 0 1')
        self.assertTrue(board.checkmate)

    def test_no_checkmate_if_no_move_available_and_king_not_in_check(self):
        board = Board('8/8/8/8/8/2b5/1r6/K7 w - - 0 1')
        self.assertFalse(board.checkmate)

    def test_black_can_be_in_checkmate_as_well(self):
        board = Board('8/8/8/8/8/2B5/1Q6/k7 b - - 0 1')
        self.assertTrue(board.checkmate)

    def test_no_stalemate_if_more_than_one_move_available(self):
        board = Board('8/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertFalse(board.stalemate)

    def test_no_stalemate_if_no_move_available_and_king_in_check(self):
        board = Board('8/8/8/8/8/2b5/1q6/K7 w - - 0 1')
        self.assertFalse(board.stalemate)

    def test_stalemate_if_no_move_available_and_king_not_in_check(self):
        board = Board('8/8/8/8/8/2b5/1r6/K7 w - - 0 1')
        self.assertTrue(board.stalemate)

    def test_black_can_be_in_stalemate_as_well(self):
        board = Board('8/8/8/8/8/2B5/1R6/k7 b - - 0 1')
        self.assertTrue(board.stalemate)


class GetPieceTestCase(unittest.TestCase):
    def test_can_get_piece_on_pos(self):
        rook = None
        for piece in board1.pieces:
            if piece.pos == 0:
                rook = piece
                break
        self.assertIs(rook, board1._get_piece(0))

    def test_can_get_any_piece_on_pos(self):
        rook = None
        for piece in board1.pieces:
            if piece.pos == 7:
                rook = piece
                break
        self.assertIs(rook, board1._get_piece(7))

    def test_raises_value_error_if_no_piece_found_on_position(self):
        self.assertRaises(ValueError, board1._get_piece, 16)

    def test_uses_given_piece_set(self):
        self.assertRaises(ValueError, board1._get_piece, 0, set())

    def test_uses_active_pieces_set(self):
        board = Board()
        board._get_piece(8).capture(1, True)
        self.assertRaises(ValueError, board._get_piece, 8)

    def test_can_get_white_king(self):
        board = Board('8/8/8/8/8/8/8/K7 w - - 0 1')
        king = board._get_piece(0)
        self.assertIs(king, board._get_king(True))

    def test_can_get_any_white_king(self):
        board = Board('8/8/8/8/8/8/8/7K w - - 0 1')
        king = board._get_piece(7)
        self.assertIs(king, board._get_king(True))

    def test_can_get_black_king(self):
        board = Board('8/8/8/8/8/8/8/k7 w - - 0 1')
        king = board._get_piece(0)
        self.assertIs(king, board._get_king(False))

    def test_can_get_any_black_king(self):
        board = Board('8/8/8/8/8/8/8/7k w - - 0 1')
        king = board._get_piece(7)
        self.assertIs(king, board._get_king(False))

    def test_can_get_white_king_with_two_king_on_board(self):
        board = Board('8/8/8/8/8/8/8/Kk w - - 0 1')
        king = board._get_piece(0)
        self.assertIs(king, board._get_king(True))

    def test_can_get_black_king_with_two_king_on_board(self):
        board = Board('8/8/8/8/8/8/8/Kk w - - 0 1')
        king = board._get_piece(1)
        self.assertIs(king, board._get_king(False))

    def test_can_get_white_king_on_busy_board(self):
        king = board1._get_piece(4)
        self.assertIs(king, board1._get_king(True))

    def test_can_get_black_king_on_busy_board(self):
        king = board1._get_piece(60)
        self.assertIs(king, board1._get_king(False))

    def test_only_considers_active_pieces(self):
        board = Board('8/8/8/8/8/8/8/Kr6 b - - 0 1')
        board.make_move((1, 0))
        self.assertRaises(ValueError, board._get_king, True)


class CreatePieceTestCase(unittest.TestCase):
    def test_can_create_white_pawn_on_pos(self):
        piece = board1._create_piece(0, True, 0)
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.type)

    def test_can_create_white_pawn_on_any_pos(self):
        piece = board1._create_piece(45, True, 0)
        self.assertEqual(45, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.type)

    def test_can_create_black_pawn(self):
        piece = board1._create_piece(0, False, 0)
        self.assertEqual(0, piece.pos)
        self.assertFalse(piece.white_piece)
        self.assertEqual(0, piece.type)

    def test_can_create_knight(self):
        piece = board1._create_piece(0, True, 1)
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(1, piece.type)

    def test_can_create_bishop(self):
        piece = board1._create_piece(0, True, 2)
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(2, piece.type)

    def test_can_create_rook(self):
        piece = board1._create_piece(0, True, 3)
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(3, piece.type)

    def test_can_create_queen(self):
        piece = board1._create_piece(0, True, 4)
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(4, piece.type)

    def test_can_create_king(self):
        piece = board1._create_piece(0, True, 5)
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(5, piece.type)


class PositionsStateTestCase(unittest.TestCase):
    def test_square_is_empty_if_square_is_empty(self):
        self.assertTrue(board1.is_square_empty(36))

    def test_square_is_not_empty_if_black_piece_on_square(self):
        self.assertFalse(board2.is_square_empty(36))

    def test_square_is_not_empty_if_white_piece_on_square(self):
        self.assertFalse(board2.is_square_empty(29))

    def test_is_square_empty_can_use_given_piece_set(self):
        self.assertTrue(board1.is_square_empty(16, set()))

    def test_is_square_empty_uses_active_pieces_set(self):
        board = Board()
        board._get_piece(8).capture(1, True)
        self.assertTrue(board.is_square_empty(8))

    def test_own_piece_on_square_if_own_piece_on_square(self):
        self.assertTrue(board1.own_piece_on_square(0, True))

    def test_not_own_piece_on_square_if_square_is_empty(self):
        self.assertFalse(board1.own_piece_on_square(16, True))

    def test_not_own_piece_on_square_if_opponents_piece_on_square(self):
        self.assertFalse(board1.own_piece_on_square(63, True))

    def test_own_piece_on_square_uses_active_pieces_set(self):
        board = Board()
        board._get_piece(8).capture(1, True)
        self.assertFalse(board.own_piece_on_square(8, True))

    def test_opponent_piece_on_square_if_opponent_piece_on_square(self):
        self.assertTrue(board1.opponent_piece_on_square(63, True))

    def test_not_opponent_piece_on_square_if_square_is_empty(self):
        self.assertFalse(board1.opponent_piece_on_square(16, True))

    def test_not_opponent_piece_on_square_if_own_piece_on_square(self):
        self.assertFalse(board1.opponent_piece_on_square(0, True))

    def test_opponent_piece_on_square_uses_active_pieces_set(self):
        board = Board()
        board._get_piece(8).capture(1, True)
        self.assertFalse(board.opponent_piece_on_square(8, False))

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

    def test_is_square_attacked_uses_active_pieces_set(self):
        board = Board()
        board._get_piece(8).capture(1, True)
        self.assertTrue(board.is_square_attacked(48, False))


class MoveGenerationTestCase(unittest.TestCase):
    # general
    # def test_raises_value_error_if_there_is_no_king_of_the_active_player_is_on_the_board(self):
    #     board = Board('8/8/8/8/8/8/8/8 w - - 0 1')
    #     self.assertRaises(ValueError, board.legal_moves())

    def test_cannot_generate_black_moves_when_white_to_move(self):
        board = Board('k7/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertEqual({(0, 1), (0, 8), (0, 9)}, board.legal_moves())

    # white pieces
    def test_can_generate_white_king_moves(self):
        board = Board('8/8/8/8/8/8/1K6/8 w - - 0 1')
        self.assertEqual({(9, 0), (9, 1), (9, 2), (9, 8), (9, 10), (9, 16), (9, 17), (9, 18)}, board.legal_moves())

    def test_can_generate_any_white_king_moves(self):
        board = Board('8/8/8/8/8/8/6K1/8 w - - 0 1')
        self.assertEqual({(14, 5), (14, 6), (14, 7), (14, 13), (14, 15), (14, 21), (14, 22), (14, 23)},
                         board.legal_moves())

    def test_can_generate_white_pawn_moves(self):
        board = Board('8/8/8/8/8/8/P7/K7 w - - 0 1')
        self.assertEqual({(8, 16), (8, 24)} | {(0, 1), (0, 9)}, board.legal_moves())

    def test_can_generate_any_white_pawn_moves(self):
        board = Board('8/8/8/8/4P3/8/8/K7 w - - 0 1')
        self.assertEqual({(28, 36)} | {(0, 1), (0, 8), (0, 9)}, board.legal_moves())

    def test_can_generate_white_knight_moves(self):
        board = Board('8/8/8/8/8/8/8/KN6 w - - 0 1')
        self.assertEqual({(1, 11), (1, 16), (1, 18)} | {(0, 8), (0, 9)}, board.legal_moves())

    def test_can_generate_any_white_knight_moves(self):
        board = Board('8/8/8/8/8/8/8/6NK w - - 0 1')
        self.assertEqual({(6, 12), (6, 21), (6, 23)} | {(7, 14), (7, 15)}, board.legal_moves())

    def test_can_generate_white_bishop_moves(self):
        board = Board('8/8/8/8/8/8/1B6/1K6 w - - 0 1')
        self.assertEqual({(9, 0), (9, 18), (9, 27), (9, 36), (9, 45), (9, 54), (9, 63), (9, 2), (9, 16)} |
                         {(1, 0), (1, 8), (1, 2), (1, 10)}, board.legal_moves())

    def test_can_generate_any_white_bishop_moves(self):
        board = Board('8/8/8/8/8/8/6B1/6K1 w - - 0 1')
        self.assertEqual({(14, 7), (14, 21), (14, 28), (14, 35), (14, 42), (14, 49), (14, 56), (14, 23), (14, 5)} |
                         {(6, 5), (6, 7), (6, 13), (6, 15)}, board.legal_moves())

    def test_can_generate_white_rook_moves(self):
        board = Board('8/8/8/8/8/8/1R6/K7 w - - 0 1')
        self.assertEqual({(9, 1), (9, 8), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 17), (9, 25),
                          (9, 33), (9, 41), (9, 49), (9, 57)} | {(0, 1), (0, 8)}, board.legal_moves())

    def test_can_generate_any_white_rook_moves(self):
        board = Board('8/8/8/8/8/8/6R1/7K w - - 0 1')
        self.assertEqual({(14, 15), (14, 6), (14, 13), (14, 12), (14, 11), (14, 10), (14, 9), (14, 8), (14, 22),
                          (14, 30), (14, 38), (14, 46), (14, 54), (14, 62)} | {(7, 6), (7, 15)}, board.legal_moves())

    def test_can_generate_white_queen_moves(self):
        board = Board('K7/8/8/8/8/8/1Q6/8 w - - 0 1')
        self.assertEqual({(9, 1), (9, 8), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 17), (9, 25),
                          (9, 33), (9, 41), (9, 49), (9, 57), (9, 0), (9, 18), (9, 27), (9, 36), (9, 45), (9, 54),
                          (9, 63), (9, 2), (9, 16)} | {(56, 48), (56, 49), (56, 57)}, board.legal_moves())

    def test_can_generate_any_white_queen_moves(self):
        board = Board('7K/8/8/8/8/8/6Q1/8 w - - 0 1')
        self.assertEqual({(14, 15), (14, 6), (14, 13), (14, 12), (14, 11), (14, 10), (14, 9), (14, 8), (14, 22),
                          (14, 30), (14, 38), (14, 46), (14, 54), (14, 62), (14, 7), (14, 21), (14, 28), (14, 35),
                          (14, 42), (14, 49), (14, 56), (14, 23), (14, 5)} | {(63, 54), (63, 55), (63, 62)},
                         board.legal_moves())

    def test_can_generate_multiple_white_moves(self):
        board = Board('8/8/8/8/1P1PP3/8/KQB5/N1RN4 w - - 0 1')
        self.assertEqual({(0, 17), (2, 1), (3, 18), (3, 20), (3, 13), (8, 1), (8, 16), (8, 17), (9, 16), (9, 17),
                          (9, 18), (9, 1), (10, 1), (10, 17), (10, 19), (10, 24), (25, 33), (27, 35), (28, 36)},
                         board.legal_moves())

    # black pieces
    def test_can_generate_black_king_moves(self):
        board = Board('8/8/8/8/8/8/1k6/8 b - - 0 1')
        self.assertEqual({(9, 0), (9, 1), (9, 2), (9, 8), (9, 10), (9, 16), (9, 17), (9, 18)}, board.legal_moves())

    def test_can_generate_any_black_king_moves(self):
        board = Board('8/8/8/8/8/8/6k1/8 b - - 0 1')
        self.assertEqual({(14, 5), (14, 6), (14, 7), (14, 13), (14, 15), (14, 21), (14, 22), (14, 23)},
                         board.legal_moves())

    def test_can_generate_black_pawn_moves(self):
        board = Board('k7/p7/8/8/8/8/8/8 b - - 0 1')
        self.assertEqual({(48, 40), (48, 32)} | {(56, 49), (56, 57)}, board.legal_moves())

    def test_can_generate_any_black_pawn_moves(self):
        board = Board('k7/8/2p5/8/8/8/8/8 b - - 0 1')
        self.assertEqual({(42, 34)} | {(56, 48), (56, 49), (56, 57)}, board.legal_moves())

    def test_can_generate_black_knight_moves(self):
        board = Board('8/8/8/8/8/8/8/kn6 b - - 0 1')
        self.assertEqual({(1, 11), (1, 16), (1, 18)} | {(0, 8), (0, 9)}, board.legal_moves())

    def test_can_generate_any_black_knight_moves(self):
        board = Board('8/8/8/8/8/8/8/6nk b - - 0 1')
        self.assertEqual({(6, 12), (6, 21), (6, 23)} | {(7, 14), (7, 15)}, board.legal_moves())

    def test_can_generate_black_bishop_moves(self):
        board = Board('8/8/8/8/8/8/1b6/1k6 b - - 0 1')
        self.assertEqual({(9, 0), (9, 18), (9, 27), (9, 36), (9, 45), (9, 54), (9, 63), (9, 2), (9, 16)} |
                         {(1, 0), (1, 8), (1, 2), (1, 10)}, board.legal_moves())

    def test_can_generate_any_black_bishop_moves(self):
        board = Board('8/8/8/8/8/8/6b1/6k1 b - - 0 1')
        self.assertEqual({(14, 7), (14, 21), (14, 28), (14, 35), (14, 42), (14, 49), (14, 56), (14, 23), (14, 5)} |
                         {(6, 5), (6, 7), (6, 13), (6, 15)}, board.legal_moves())

    def test_can_generate_black_rook_moves(self):
        board = Board('8/8/8/8/8/8/1r6/k7 b - - 0 1')
        self.assertEqual({(9, 1), (9, 8), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 17), (9, 25),
                          (9, 33), (9, 41), (9, 49), (9, 57)} | {(0, 1), (0, 8)}, board.legal_moves())

    def test_can_generate_any_black_rook_moves(self):
        board = Board('8/8/8/8/8/8/6r1/7k b - - 0 1')
        self.assertEqual({(14, 15), (14, 6), (14, 13), (14, 12), (14, 11), (14, 10), (14, 9), (14, 8), (14, 22),
                          (14, 30), (14, 38), (14, 46), (14, 54), (14, 62)} | {(7, 6), (7, 15)}, board.legal_moves())

    def test_can_generate_black_queen_moves(self):
        board = Board('k7/8/8/8/8/8/1q6/8 b - - 0 1')
        self.assertEqual({(9, 1), (9, 8), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 17), (9, 25),
                          (9, 33), (9, 41), (9, 49), (9, 57), (9, 0), (9, 18), (9, 27), (9, 36), (9, 45), (9, 54),
                          (9, 63), (9, 2), (9, 16)} | {(56, 48), (56, 49), (56, 57)}, board.legal_moves())

    def test_can_generate_any_black_queen_moves(self):
        board = Board('7k/8/8/8/8/8/6q1/8 b - - 0 1')
        self.assertEqual({(14, 15), (14, 6), (14, 13), (14, 12), (14, 11), (14, 10), (14, 9), (14, 8), (14, 22),
                          (14, 30), (14, 38), (14, 46), (14, 54), (14, 62), (14, 7), (14, 21), (14, 28), (14, 35),
                          (14, 42), (14, 49), (14, 56), (14, 23), (14, 5)} | {(63, 54), (63, 55), (63, 62)},
                         board.legal_moves())

    def test_can_generate_multiple_black_moves(self):
        board = Board('8/8/8/8/1p1pp3/8/kqb5/n1rn4 b - - 0 1')
        self.assertEqual({(0, 17), (2, 1), (3, 18), (3, 20), (3, 13), (8, 1), (8, 16), (8, 17), (9, 16), (9, 17),
                          (9, 18), (9, 1), (10, 1), (10, 17), (10, 19), (10, 24), (25, 17), (27, 19), (28, 20)},
                         board.legal_moves())


class LegalMoveGenerationTextCase(unittest.TestCase):
    def test_king_can_not_move_into_check(self):
        board = Board('8/8/8/8/8/8/7r/K7 w - - 0 1')
        self.assertEqual({(0, 1)}, board.legal_moves())

    def test_king_can_capture_checking_piece(self):
        board = Board('8/8/8/8/8/8/7r/7K w - - 0 1')
        self.assertEqual({(7, 15), (7, 6)}, board.legal_moves())

    def test_king_can_not_capture_checking_piece_if_it_is_saved(self):
        board = Board('7r/8/8/8/8/8/7r/7K w - - 0 1')
        self.assertEqual({(7, 6)}, board.legal_moves())

    def test_king_can_move_out_of_check(self):
        board = Board('7r/8/8/8/8/8/7r/7K w - - 0 1')
        self.assertEqual({(7, 6)}, board.legal_moves())

    def test_other_piece_can_capture_checking_piece(self):
        board = Board('R6r/6r1/8/8/8/8/8/7K w - - 0 1')
        self.assertEqual({(56, 63)}, board.legal_moves())

    def test_other_piece_can_interpose_checking_piece(self):
        board = Board('7r/6r1/R7/8/8/8/8/7K w - - 0 1')
        self.assertEqual({(40, 47)}, board.legal_moves())

    def test_other_piece_can_not_expose_king_to_check(self):
        board = Board('7r/6r1/8/8/8/8/7R/7K w - - 0 1')
        self.assertEqual({(15, 23), (15, 31), (15, 39), (15, 47), (15, 55), (15, 63)}, board.legal_moves())

    def test_other_piece_cannot_capture_checking_piece_when_in_double_check(self):
        board = Board('r6R/8/8/8/8/8/1P6/K6r w - - 0 1')
        self.assertEqual(set(), board.legal_moves())

    def test_other_piece_cannot_interpose_checking_piece_when_in_double_check(self):
        board = Board('r7/6R1/8/8/8/8/1P6/K6r w - - 0 1')
        self.assertEqual(set(), board.legal_moves())

    def test_king_cannot_move_if_in_checkmate(self):
        board = Board('8/8/8/8/8/2b5/1q6/K7 w - - 0 1')
        self.assertEqual(set(), board.legal_moves())

    def test_other_pieces_cannot_move_if_king_is_in_checkmate(self):
        board = Board('8/8/8/8/8/2b5/1q6/K6P w - - 0 1')
        self.assertEqual(set(), board.legal_moves())

    def test_king_cannot_move_if_in_stalemate(self):
        board = Board('8/8/8/8/8/2b5/1r6/K7 w - - 0 1')
        self.assertEqual(set(), board.legal_moves())

    def test_other_pieces_can_move_if_king_is_in_stalemate(self):
        board = Board('8/8/8/8/8/2b5/1r6/K6P w - - 0 1')
        self.assertEqual({(7, 15)}, board.legal_moves())
    # def test_other_pieces_can_move_if_king_is_in_stalemate(self):
    #     board = Board('r1bqkb1r/p1pppQpp/1pn2n2/8/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4')
    #     self.assertTrue(board.checkmate)


class MakeMoveTestCase(unittest.TestCase):
    # piece tests
    def test_starting_pos_is_empty(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 0 1')
        board.make_move((8, 16))
        self.assertRaises(ValueError, board._get_piece, 8)

    def test_piece_on_final_square(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 0 1')
        pawn = board._get_piece(8)
        board.make_move((8, 16))
        self.assertIs(pawn, board._get_piece(16))

    def test_can_make_pawn_moves_as_white(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 0 1')
        pawn = board._get_piece(8)
        board.make_move((8, 16))
        self.assertIs(pawn, board._get_piece(16))

    def test_can_make_any_pawn_moves_as_white(self):
        board = Board('8/8/8/8/8/8/1P6/8 w - - 0 1')
        pawn = board._get_piece(9)
        board.make_move((9, 17))
        self.assertIs(pawn, board._get_piece(17))

    def test_can_make_pawn_moves_as_black(self):
        board = Board('8/p7/8/8/8/8/8/8 b - - 0 1')
        pawn = board._get_piece(48)
        board.make_move((48, 40))
        self.assertIs(pawn, board._get_piece(40))

    def test_can_make_any_pawn_moves_as_black(self):
        board = Board('8/1p6/8/8/8/8/8/8 b - - 0 1')
        pawn = board._get_piece(49)
        board.make_move((49, 41))
        self.assertIs(pawn, board._get_piece(41))

    def test_can_make_knight_moves(self):
        board = Board('8/8/8/8/8/8/8/N7 w - - 0 1')
        knight = board._get_piece(0)
        board.make_move((0, 17))
        self.assertIs(knight, board._get_piece(17))

    def test_can_make_any_knight_moves(self):
        board = Board('8/8/8/8/8/8/8/N7 w - - 0 1')
        knight = board._get_piece(0)
        board.make_move((0, 10))
        self.assertIs(knight, board._get_piece(10))

    def test_can_make_bishop_moves(self):
        board = Board('8/8/8/8/8/8/1B6/8 w - - 0 1')
        bishop = board._get_piece(9)
        board.make_move((9, 0))
        self.assertIs(bishop, board._get_piece(0))

    def test_can_make_any_bishop_moves(self):
        board = Board('8/8/8/8/8/8/1B6/8 w - - 0 1')
        bishop = board._get_piece(9)
        board.make_move((9, 18))
        self.assertIs(bishop, board._get_piece(18))

    def test_can_make_rook_moves(self):
        board = Board('8/8/8/8/8/8/1R6/8 w - - 0 1')
        rook = board._get_piece(9)
        board.make_move((9, 8))
        self.assertIs(rook, board._get_piece(8))

    def test_can_make_any_rook_moves(self):
        board = Board('8/8/8/8/8/8/1R6/8 w - - 0 1')
        rook = board._get_piece(9)
        board.make_move((9, 10))
        self.assertIs(rook, board._get_piece(10))

    def test_can_make_queen_moves(self):
        board = Board('8/8/8/8/8/8/1Q6/8 w - - 0 1')
        queen = board._get_piece(9)
        board.make_move((9, 10))
        self.assertIs(queen, board._get_piece(10))

    def test_can_make_any_queen_moves(self):
        board = Board('8/8/8/8/8/8/1Q6/8 w - - 0 1')
        queen = board._get_piece(9)
        board.make_move((9, 8))
        self.assertIs(queen, board._get_piece(8))

    def test_can_make_king_moves(self):
        board = Board('8/8/8/8/8/8/1K6/8 w - - 0 1')
        king = board._get_piece(9)
        board.make_move((9, 10))
        self.assertIs(king, board._get_piece(10))

    def test_can_make_any_king_moves(self):
        board = Board('8/8/8/8/8/8/1K6/8 w - - 0 1')
        king = board._get_piece(9)
        board.make_move((9, 8))
        self.assertIs(king, board._get_piece(8))

    # capturing
    def test_captured_piece_is_not_in_active_pieces_set(self):
        board = Board('r7/8/8/8/8/8/8/R7 w - - 0 1')
        b_rook = board._get_piece(56)
        board.make_move((0, 56))
        self.assertNotIn(b_rook, board._active_pieces)

    def test_captured_piece_is_in_pieces_set(self):
        board = Board('r7/8/8/8/8/8/8/R7 w - - 0 1')
        b_rook = board._get_piece(56)
        board.make_move((0, 56))
        self.assertIn(b_rook, board._pieces)

    def test_capture_turn_correct_after_white_captures(self):
        board = Board('r7/8/8/8/8/8/8/R7 w - - 0 1')
        turn = board.turn_number
        b_rook = board._get_piece(56)
        board.make_move((0, 56))
        self.assertEqual(turn, b_rook._capture_data[0])

    def test_capture_turn_correct_after_black_captures(self):
        board = Board('r7/8/8/8/8/8/8/R7 b - - 0 1')
        turn = board.turn_number
        w_rook = board._get_piece(0)
        board.make_move((56, 0))
        self.assertEqual(turn, w_rook._capture_data[0])

    def test_capture_color_correct_after_white_captures(self):
        board = Board('r7/8/8/8/8/8/8/R7 w - - 0 1')
        color = board._white_to_move
        b_rook = board._get_piece(56)
        board.make_move((0, 56))
        self.assertEqual(color, b_rook._capture_data[1])

    def test_capture_color_correct_after_black_captures(self):
        board = Board('r7/8/8/8/8/8/8/R7 b - - 0 1')
        color = board._white_to_move
        w_rook = board._get_piece(0)
        board.make_move((56, 0))
        self.assertEqual(color, w_rook._capture_data[1])

    # castling moves
    def test_rook_moved_after_castling_kingside_as_white(self):
        board = Board('8/8/8/8/8/8/8/4K2R w K - 0 1')
        king = board._get_piece(4)
        rook = board._get_piece(7)
        board.make_move((4, 6))
        self.assertIs(king, board._get_piece(6))
        self.assertIs(rook, board._get_piece(5))

    def test_rook_moved_after_castling_queenside_as_white(self):
        board = Board('8/8/8/8/8/8/8/R3K3 w Q - 0 1')
        king = board._get_piece(4)
        rook = board._get_piece(0)
        board.make_move((4, 2))
        self.assertIs(king, board._get_piece(2))
        self.assertIs(rook, board._get_piece(3))

    def test_rook_moved_after_castling_kingside_as_black(self):
        board = Board('4k2r/8/8/8/8/8/8/8 b k - 0 1')
        king = board._get_piece(60)
        rook = board._get_piece(63)
        board.make_move((60, 62))
        self.assertIs(king, board._get_piece(62))
        self.assertIs(rook, board._get_piece(61))

    def test_rook_moved_after_castling_queenside_as_black(self):
        board = Board('r3k3/8/8/8/8/8/8/8 b q - 0 1')
        king = board._get_piece(60)
        rook = board._get_piece(56)
        board.make_move((60, 58))
        self.assertIs(king, board._get_piece(58))
        self.assertIs(rook, board._get_piece(59))

    # en passant moves
    def test_removes_pawn_after_capturing_en_passant_right_as_white(self):
        board = Board('8/8/8/Pp6/8/8/8/8 w - b6 0 1')
        b_pawn = board._get_piece(33)
        board.make_move((32, 41))
        self.assertNotIn(b_pawn, board._active_pieces)

    def test_removes_pawn_after_capturing_en_passant_left_as_white(self):
        board = Board('8/8/8/pP6/8/8/8/8 w - a6 0 1')
        b_pawn = board._get_piece(32)
        board.make_move((33, 40))
        self.assertNotIn(b_pawn, board._active_pieces)

    def test_removes_pawn_after_capturing_en_passant_right_as_black(self):
        board = Board('8/8/8/8/8/pP6/8/8 b - b2 0 1')
        w_pawn = board._get_piece(17)
        board.make_move((16, 9))
        self.assertNotIn(w_pawn, board._active_pieces)

    def test_removes_pawn_after_capturing_en_passant_left_as_black(self):
        board = Board('8/8/8/8/8/Pp6/8/8 b - a2 0 1')
        w_pawn = board._get_piece(16)
        board.make_move((17, 8))
        self.assertNotIn(w_pawn, board._active_pieces)

    # promotion
    def test_pawn_will_be_promoted_to_a_queen_when_moving_to_the_last_row_as_white(self):
        board = Board('8/P7/8/8/8/8/8/8 w - - 0 1')
        board.make_move((48, 56))
        self.assertEqual(4, board._get_piece(56)._type)
        self.assertTrue(board._get_piece(56)._white_piece)

    def test_pawn_will_be_promoted_to_a_queen_when_moving_to_the_last_row_as_black(self):
        board = Board('8/8/8/8/8/8/p7/8 b - - 0 1')
        board.make_move((8, 0))
        self.assertEqual(4, board._get_piece(0)._type)
        self.assertFalse(board._get_piece(0)._white_piece)

    def test_pawn_remains_in_pieces_set(self):
        board = Board('8/P7/8/8/8/8/8/8 w - - 0 1')
        pawn = board._get_piece(48)
        board.make_move((48, 56))
        self.assertIn(pawn, board._pieces)

    def test_pawn_will_be_removed_from_active_piece_set(self):
        board = Board('8/P7/8/8/8/8/8/8 w - - 0 1')
        pawn = board._get_piece(48)
        board.make_move((48, 56))
        self.assertNotIn(pawn, board._active_pieces)

    # board info except pieces
    # color to move
    def test_black_to_move_after_white_move(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 0 1')
        board.make_move((8, 16))
        self.assertFalse(board.white_to_move)

    def test_white_to_move_after_black_move(self):
        board = Board('8/p7/8/8/8/8/8/8 b - - 0 1')
        board.make_move((48, 40))
        self.assertTrue(board.white_to_move)

    # castling rights
    def test_castling_rights_do_not_change_after_unrelated_move(self):
        board = Board('r3k2r/8/8/8/8/4P3/8/R3K2R w KQkq - 0 1')
        board.make_move((20, 28))
        self.assertEqual([True, True, True, True], board.castling_rights)

    # white
    def test_white_looses_all_castling_rights_if_white_king_moves_away(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((4, 12))
        self.assertEqual([False, False, True, True], board.castling_rights)

    def test_white_cannot_regain_all_castling_rights_if_white_king_moves_back(self):
        board = Board('r3k2r/8/8/8/8/8/4K3/R6R w kq - 0 1')
        board.make_move((12, 4))
        self.assertEqual([False, False, True, True], board.castling_rights)

    def test_white_cannot_regain_all_castling_rights_if_black_king_moves_to_white_kings_starting_position(self):
        board = Board('r6r/8/8/8/4K3/R3P2R/4k3/8 w - - 0 1')
        board.make_move((12, 4))
        self.assertEqual([False, False, False, False], board.castling_rights)

    def test_white_looses_kingside_castling_right_if_kingside_rook_is_captured(self):
        board = Board('r3k2r/7r/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((55, 7))
        self.assertEqual([False, True, True, True], board.castling_rights)

    def test_white_looses_kingside_castling_right_if_kingside_rook_moves_away(self):
        board = Board('r3k2r/7r/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((7, 15))
        self.assertEqual([False, True, True, True], board.castling_rights)

    def test_white_cannot_regain_kingside_castling_right_if_kingside_rook_moves_back(self):
        board = Board('r3k2r/7r/8/8/8/8/7R/R3K3 w Qkq - 0 1')
        board.make_move((15, 7))
        self.assertEqual([False, True, True, True], board.castling_rights)

    def test_white_looses_queenside_castling_right_if_queenside_rook_is_captured(self):
        board = Board('r3k2r/r7/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((48, 0))
        self.assertEqual([True, False, True, True], board.castling_rights)

    def test_white_looses_queenside_castling_right_if_queenside_rook_moves_away(self):
        board = Board('r3k2r/r7/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((0, 8))
        self.assertEqual([True, False, True, True], board.castling_rights)

    def test_white_cannot_regain_queenside_castling_right_if_queenside_rook_moves_back(self):
        board = Board('r3k2r/r7/8/8/8/8/R7/4K2R w Kkq - 0 1')
        board.make_move((8, 0))
        self.assertEqual([True, False, True, True], board.castling_rights)

    # black
    def test_black_looses_all_castling_rights_if_black_king_moves_away(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((60, 52))
        self.assertEqual([True, True, False, False], board.castling_rights)

    def test_black_cannot_regain_all_castling_rights_if_black_king_moves_back(self):
        board = Board('r6r/4k3/8/8/8/8/8/R3K2R b KQ - 0 1')
        board.make_move((52, 60))
        self.assertEqual([True, True, False, False], board.castling_rights)

    def test_black_cannot_regain_all_castling_rights_if_white_king_moves_to_black_kings_starting_position(self):
        board = Board('8/4K3/r6r/4k3/8/8/8/R6R w - - 0 1')
        board.make_move((52, 60))
        self.assertEqual([False, False, False, False], board.castling_rights)

    def test_black_looses_kingside_castling_right_if_kingside_rook_is_captured(self):
        board = Board('r3k2r/8/8/8/8/8/7R/R3K2R w KQkq - 0 1')
        board.make_move((15, 63))
        self.assertEqual([True, True, False, True], board.castling_rights)

    def test_black_looses_kingside_castling_right_if_kingside_rook_moves_away(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((63, 55))
        self.assertEqual([True, True, False, True], board.castling_rights)

    def test_black_cannot_regain_kingside_castling_right_if_kingside_rook_moves_back(self):
        board = Board('r3k3/7r/8/8/8/8/8/R3K2R b KQq - 0 1')
        board.make_move((55, 63))
        self.assertEqual([True, True, False, True], board.castling_rights)

    def test_black_looses_queenside_castling_right_if_queenside_rook_is_captured(self):
        board = Board('r3k2r/8/8/8/8/8/R7/R3K2R w KQkq - 0 1')
        board.make_move((8, 56))
        self.assertEqual([True, True, True, False], board.castling_rights)

    def test_black_looses_queenside_castling_right_if_queenside_rook_moves_away(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((56, 48))
        self.assertEqual([True, True, True, False], board.castling_rights)

    def test_black_cannot_regain_queenside_castling_right_if_queenside_rook_moves_back(self):
        board = Board('4k2r/r7/8/8/8/8/8/R3K2R b KQk - 0 1')
        board.make_move((48, 56))
        self.assertEqual([True, True, True, False], board.castling_rights)

    # en passant target square
    def test_ep_target_square_is_none_after_unrelated_move(self):
        board = Board('8/8/8/8/8/P7/8/8 w - - 0 1')
        board.make_move((16, 24))
        self.assertIsNone(board.ep_target_square)

    def test_ep_target_square_is_none_after_unrelated_move_if_there_is_a_ep_target_square(self):
        board = Board('8/8/8/p7/8/P7/8/8 w - a6 0 1')
        board.make_move((16, 24))
        self.assertIsNone(board.ep_target_square)

    # white
    def test_sets_ep_target_square_after_double_pawn_push_as_white(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 0 1')
        board.make_move((8, 24))
        self.assertEqual(16, board.ep_target_square)

    def test_sets_ep_target_square_after_any_double_pawn_push_as_white(self):
        board = Board('8/8/8/8/8/8/1P6/8 w - - 0 1')
        board.make_move((9, 25))
        self.assertEqual(17, board.ep_target_square)

    # black
    def test_sets_ep_target_square_after_double_pawn_push_as_black(self):
        board = Board('8/p7/8/8/8/8/8/8 b - - 0 1')
        board.make_move((48, 32))
        self.assertEqual(40, board.ep_target_square)

    def test_sets_ep_target_square_after_any_double_pawn_push_as_black(self):
        board = Board('8/1p6/8/8/8/8/8/8 b - - 0 1')
        board.make_move((49, 33))
        self.assertEqual(41, board.ep_target_square)

    # half move clock
    def test_half_move_clock_increases_after_a_move(self):
        board = Board()
        board.make_move((1, 16))
        self.assertEqual(1, board.half_move_clock)

    def test_half_move_clock_resets_after_a_pawn_move(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 10 1')
        board.make_move((8, 16))
        self.assertEqual(0, board.half_move_clock)

    def test_half_move_clock_resets_after_capturing_a_piece(self):
        board = Board('8/8/8/8/8/1p6/Q7/8 w - - 10 1')
        board.make_move((8, 17))
        self.assertEqual(0, board.half_move_clock)

    # turn number
    def test_turn_number_does_not_increase_after_white_move(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 0 1')
        board.make_move((8, 16))
        self.assertEqual(1, board.turn_number)

    def test_turn_number_increases_after_black_move(self):
        board = Board('8/p7/8/8/8/8/8/8 b - - 0 1')
        board.make_move((48, 40))
        self.assertEqual(2, board.turn_number)

    def test_adds_old_position_to_position_list(self):
        board = Board()
        board.make_move((8, 16))
        self.assertEqual(['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'], board._positions)

    def test_adds_any_old_position_to_position_list(self):
        board = Board('PPPPPPPP/rKqqQRRP/BBKpQnRq/nBbpQQRQ/bbbpbQRN/nppbKKRP/npQrbPKk/NNNkkkkk w - - 0 1')
        board.make_move((0, 17))
        self.assertEqual(['PPPPPPPP/rKqqQRRP/BBKpQnRq/nBbpQQRQ/bbbpbQRN/nppbKKRP/npQrbPKk/NNNkkkkk w - - 0 1'],
                         board._positions)

    def test_two_positions_in_list_after_two_moves(self):
        board = Board()
        board.make_move((8, 16))
        board.make_move((48, 40))
        self.assertEqual(['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
                          'rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR b KQkq - 0 1'], board._positions)

    def test_adds_move_to_move_list(self):
        board = Board()
        board.make_move((8, 16))
        self.assertEqual([(8, 16)], board._moves)

    def test_adds_any_move_to_move_list(self):
        board = Board()
        board.make_move((8, 24))
        self.assertEqual([(8, 24)], board._moves)

    def test_adds_two_move_to_move_list(self):
        board = Board()
        board.make_move((8, 16))
        board.make_move((48, 40))
        self.assertEqual([(8, 16), (48, 40)], board._moves)


class UndoMoveTestCase(unittest.TestCase):
    def test_removes_last_move_from_positions_list(self):
        board = Board()
        board.make_move((1, 16))
        board._undo_move()
        self.assertEqual([], board._positions)

    # piece tests
    def test_starting_pos_is_not_empty(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 0 1')
        piece = board._get_piece(8)
        board.make_move((8, 16))
        board._undo_move()
        self.assertEqual(0, piece._type)
        self.assertEqual(8, piece._pos)
        self.assertTrue(piece._white_piece)

    def test_not_piece_on_final_square(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 0 1')
        board.make_move((8, 16))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 16)

    def test_can_undo_white_pawn_move(self):
        board = Board('8/8/8/8/8/8/P7/8 w - - 0 1')
        board.make_move((8, 16))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 16)

    def test_can_undo_any_white_pawn_move(self):
        board = Board('8/8/8/8/8/8/1P6/8 w - - 0 1')
        board.make_move((9, 17))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 17)

    def test_can_undo_black_pawn_move(self):
        board = Board('8/p7/8/8/8/8/8/8 b - - 0 1')
        board.make_move((48, 40))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 40)

    def test_can_undo_any_black_pawn_move(self):
        board = Board('8/1p6/8/8/8/8/8/8 b - - 0 1')
        board.make_move((49, 41))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 41)

    def test_can_undo_knight_move(self):
        board = Board('8/8/8/8/8/8/8/N7 w - - 0 1')
        board.make_move((0, 17))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 17)

    def test_can_undo_any_knight_move(self):
        board = Board('8/8/8/8/8/8/8/N7 w - - 0 1')
        board.make_move((0, 10))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 10)

    def test_can_undo_bishop_move(self):
        board = Board('8/8/8/8/8/8/1B6/8 w - - 0 1')
        board.make_move((9, 0))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 0)

    def test_can_undo_any_bishop_move(self):
        board = Board('8/8/8/8/8/8/1B6/8 w - - 0 1')
        board.make_move((9, 18))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 18)

    def test_can_undo_rook_move(self):
        board = Board('8/8/8/8/8/8/1R6/8 w - - 0 1')
        board.make_move((9, 8))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 8)

    def test_can_undo_any_rook_move(self):
        board = Board('8/8/8/8/8/8/1R6/8 w - - 0 1')
        board.make_move((9, 10))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 10)

    def test_can_undo_queen_move(self):
        board = Board('8/8/8/8/8/8/1Q6/8 w - - 0 1')
        board.make_move((9, 10))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 10)

    def test_can_undo_any_queen_move(self):
        board = Board('8/8/8/8/8/8/1Q6/8 w - - 0 1')
        board.make_move((9, 8))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 8)

    def test_can_undo_king_move(self):
        board = Board('8/8/8/8/8/8/1K6/8 w - - 0 1')
        board.make_move((9, 10))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 10)

    def test_can_undo_any_king_move(self):
        board = Board('8/8/8/8/8/8/1K6/8 w - - 0 1')
        board.make_move((9, 8))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 8)

    # capturing
    def test_captured_piece_is_not_captured(self):
        board = Board('r7/8/8/8/8/8/8/R7 w - - 0 1')
        b_rook = board._get_piece(56)
        w_rook = board._get_piece(0)
        board.make_move((0, 56))
        board._undo_move()
        self.assertIs(b_rook, board._get_piece(56))
        self.assertIs(w_rook, board._get_piece(0))

    # castling moves
    def test_rook_moved_after_undoing_castling_kingside_as_white(self):
        board = Board('8/8/8/8/8/8/8/4K2R w K - 0 1')
        king = board._get_piece(4)
        rook = board._get_piece(7)
        board.make_move((4, 6))
        board._undo_move()
        self.assertIs(king, board._get_piece(4))
        self.assertIs(rook, board._get_piece(7))

    def test_rook_moved_after_undoing_castling_queenside_as_white(self):
        board = Board('8/8/8/8/8/8/8/R3K3 w Q - 0 1')
        king = board._get_piece(4)
        rook = board._get_piece(0)
        board.make_move((4, 2))
        board._undo_move()
        self.assertIs(king, board._get_piece(4))
        self.assertIs(rook, board._get_piece(0))

    def test_rook_moved_after_undoing_castling_kingside_as_black(self):
        board = Board('4k2r/8/8/8/8/8/8/8 b k - 0 1')
        king = board._get_piece(60)
        rook = board._get_piece(63)
        board.make_move((60, 62))
        board._undo_move()
        self.assertIs(king, board._get_piece(60))
        self.assertIs(rook, board._get_piece(63))

    def test_rook_moved_after_castling_queenside_as_black(self):
        board = Board('r3k3/8/8/8/8/8/8/8 b q - 0 1')
        king = board._get_piece(60)
        rook = board._get_piece(56)
        board.make_move((60, 58))
        board._undo_move()
        self.assertIs(king, board._get_piece(60))
        self.assertIs(rook, board._get_piece(56))

    # en passant moves
    def test_restores_the_pawn_after_undoing_capturing_en_passant_right_as_white(self):
        board = Board('8/8/8/Pp6/8/8/8/8 w - b6 0 1')
        b_pawn = board._get_piece(33)
        board.make_move((32, 41))
        board._undo_move()
        self.assertIs(b_pawn, board._get_piece(33))

    def test_restores_the_pawn_after_undoing_capturing_en_passant_left_as_white(self):
        board = Board('8/8/8/pP6/8/8/8/8 w - a6 0 1')
        b_pawn = board._get_piece(32)
        board.make_move((33, 40))
        board._undo_move()
        self.assertIs(b_pawn, board._get_piece(32))

    def test_removes_pawn_after_capturing_en_passant_right_as_black(self):
        board = Board('8/8/8/8/8/pP6/8/8 b - b2 0 1')
        w_pawn = board._get_piece(17)
        board.make_move((16, 9))
        board._undo_move()
        self.assertIs(w_pawn, board._get_piece(17))

    def test_removes_pawn_after_capturing_en_passant_left_as_black(self):
        board = Board('8/8/8/8/8/Pp6/8/8 b - a2 0 1')
        w_pawn = board._get_piece(16)
        board.make_move((17, 8))
        board._undo_move()
        self.assertIs(w_pawn, board._get_piece(16))

    # promotion
    def test_can_undo_white_promotion(self):
        board = Board('8/P7/8/8/8/8/8/8 w - - 0 1')
        w_pawn = board._get_piece(48)
        board.make_move((48, 56))
        self.assertEqual(4, board._get_piece(56)._type)
        board._undo_move()
        self.assertIs(w_pawn, board._get_piece(48))

    def test_can_undo_black_promotion(self):
        board = Board('8/8/8/8/8/8/p7/8 b - - 0 1')
        b_pawn = board._get_piece(8)
        board.make_move((8, 0))
        self.assertEqual(4, board._get_piece(0)._type)
        board._undo_move()
        self.assertIs(b_pawn, board._get_piece(8))

    # board info except pieces
    # color to move
    def test_can_recover_white_to_move(self):
        board = Board()  # board1
        board.make_move((1, 16))
        board._undo_move()
        self.assertTrue(board._white_to_move)

    def test_can_recover_black_to_move(self):
        board = Board()  # board1
        board.make_move((1, 16))
        board.make_move((57, 48))
        board._undo_move()
        self.assertFalse(board._white_to_move)

    # castling rights
    def test_changes_nothing_if_no_rights_were_lost(self):
        board1.make_move((1, 16))
        board1._undo_move()
        self.assertEqual([True, True, True, True], board1._castling_rights)

    def test_can_recover_white_queenside_castling_right(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((0, 8))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_white_kingside_castling_right(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((7, 15))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_both_white_castling_rights(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((4, 12))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_black_queenside_castling_right(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((56, 48))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_black_kingside_castling_right(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((63, 55))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_both_black_castling_rights(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((60, 52))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_incomplete_castling_rights(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w Kq - 0 1')
        board.make_move((7, 15))
        board._undo_move()
        self.assertEqual([True, False, False, True], board._castling_rights)

    def test_can_recover_no_castling_rights(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w - - 0 1')
        board.make_move((7, 15))
        board._undo_move()
        self.assertEqual([False, False, False, False], board._castling_rights)

    # ep target square
    def test_can_recover_no_ep_target_square(self):
        board0 = Board()
        board0.make_move((1, 16))
        board0._undo_move()
        self.assertIsNone(board0._ep_target_square)

    def test_can_recover_ep_target_square(self):
        board = Board('rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR b KQkq a3 0 1')
        board.make_move((57, 48))
        board._undo_move()
        self.assertEqual(16, board._ep_target_square)

    def test_can_recover_any_ep_target_square(self):
        board = Board('rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR b KQkq b3 0 1')
        board.make_move((57, 48))
        board._undo_move()
        self.assertEqual(17, board._ep_target_square)

    # half move clock
    def test_can_recover_half_move_clock(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 10 1')
        board.make_move((60, 52))
        board._undo_move()
        self.assertEqual(10, board._half_move_clock)

    def test_can_recover_any_half_move_clock(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 25 1')
        board.make_move((60, 52))
        board._undo_move()
        self.assertEqual(25, board._half_move_clock)

    def test_can_recover_half_move_clock_after_reset(self):
        board = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 10 1')
        board.make_move((8, 16))
        board._undo_move()
        self.assertEqual(10, board._half_move_clock)

    def test_can_recover_any_half_move_clock_after_reset(self):
        board = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 25 1')
        board.make_move((8, 16))
        board._undo_move()
        self.assertEqual(25, board._half_move_clock)

    # turn number
    def test_can_recover_turn_number_after_white_move(self):
        board = Board()  # board1
        board.make_move((1, 16))
        board._undo_move()
        self.assertEqual(1, board._turn_number)

    def test_can_recover_turn_number_after_black_move(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((60, 52))
        board._undo_move()
        self.assertEqual(1, board._turn_number)

    def test_can_recover_any_turn_number_after_black_move(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 5')
        board.make_move((60, 52))
        board._undo_move()
        self.assertEqual(5, board._turn_number)


class BoardConversionTestCase(unittest.TestCase):
    # positions
    def test_can_convert_empty_board(self):
        self.assertEqual(set(), board1._pieces_to_board('8/8/8/8/8/8/8/8'))

    def test_can_convert_white_king_on_first_rank(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/K7'))[0]
        self.assertEqual(5, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_white_king_on_second_rank(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/K7/8'))[0]
        self.assertEqual(5, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(8, piece.pos)

    def test_can_convert_white_king_on_any_rank(self):
        piece = list(board1._pieces_to_board('8/8/8/K7/8/8/8/8'))[0]
        self.assertEqual(5, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(32, piece.pos)

    def test_can_convert_white_king_on_second_file(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/1K6'))[0]
        self.assertEqual(5, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(1, piece.pos)

    def test_can_convert_white_king_on_any_file(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/3K4'))[0]
        self.assertEqual(5, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(3, piece.pos)

    def test_can_convert_white_king_on_any_rank_and_any_file(self):
        piece = list(board1._pieces_to_board('8/8/8/8/6K1/8/8/8'))[0]
        self.assertEqual(5, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(30, piece.pos)

    def test_can_convert_white_queen(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/Q7'))[0]
        self.assertEqual(4, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_white_rook(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/R7'))[0]
        self.assertEqual(3, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_white_bishop(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/B7'))[0]
        self.assertEqual(2, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_white_knight(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/N7'))[0]
        self.assertEqual(1, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_white_pawn(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/P7'))[0]
        self.assertEqual(0, piece.type)
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_black_pieces(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/k7'))[0]
        self.assertEqual(5, piece.type)
        self.assertFalse(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_multiple_pieces(self):
        pieces = board1._pieces_to_board('2k5/6r1/8/3B4/8/1Q4n1/8/7P')
        piece_data = [[7, True, 0], [17, True, 4], [22, False, 1], [35, True, 2], [54, False, 3], [58, False, 5]]
        self.assertEqual(len(piece_data), len(pieces))
        for piece in pieces:
            if [piece.pos, piece.white_piece, piece.type] in piece_data:
                piece_data.remove([piece.pos, piece.white_piece, piece.type])
        self.assertEqual([], piece_data)

    def test_can_convert_complex_positions(self):
        pieces = board1._pieces_to_board('3r2k1/pp3rpp/2pR4/3bP3/1Bp1pPq1/4P3/PP5P/2K3R1')
        piece_data = [[2, True, 5], [6, True, 3], [8, True, 0], [9, True, 0], [15, True, 0], [20, True, 0],
                      [25, True, 2], [26, False, 0], [28, False, 0], [29, True, 0], [30, False, 4], [35, False, 2],
                      [36, True, 0], [42, False, 0], [43, True, 3], [48, False, 0], [49, False, 0], [53, False, 3],
                      [54, False, 0], [55, False, 0], [59, False, 3], [62, False, 5]]
        self.assertEqual(len(piece_data), len(pieces))
        for piece in pieces:
            if [piece.pos, piece.white_piece, piece.type] in piece_data:
                piece_data.remove([piece.pos, piece.white_piece, piece.type])
        self.assertEqual([], piece_data)

    def test_uses_active_pieces_set(self):
        board = Board('8/8/8/8/8/8/8/PP6 w - - 0 1')
        board._get_piece(1).capture(1, True)
        self.assertEqual('8/8/8/8/8/8/8/P7 w - - 0 1', board._board_to_fen())

    # color to move
    def test_can_convert_white_to_move(self):
        self.assertTrue(board1._color_to_move_to_board('w'))

    def test_can_convert_black_to_move(self):
        self.assertFalse(board1._color_to_move_to_board('b'))

    # castling rights
    def test_can_convert_no_castling_rights(self):
        self.assertEqual([False, False, False, False], board1._castling_rights_to_board('-'))

    def test_can_convert_white_kingside_castling_right(self):
        self.assertEqual([True, False, False, False], board1._castling_rights_to_board('K'))

    def test_can_convert_white_queenside_castling_right(self):
        self.assertEqual([False, True, False, False], board1._castling_rights_to_board('Q'))

    def test_can_convert_black_kingside_castling_right(self):
        self.assertEqual([False, False, True, False], board1._castling_rights_to_board('k'))

    def test_can_convert_black_queenside_castling_right(self):
        self.assertEqual([False, False, False, True], board1._castling_rights_to_board('q'))

    def test_can_convert_all_castling_rights(self):
        self.assertEqual([True, True, True, True], board1._castling_rights_to_board('KQkq'))

    def test_can_convert_mixed_castling_rights(self):
        self.assertEqual([False, True, True, False], board1._castling_rights_to_board('Qk'))

    # ep target square
    def test_can_convert_no_ep_target_square(self):
        self.assertIsNone(board1._ep_target_square_to_board('-'))
    
    def test_can_convert_ep_target_square(self):
        self.assertEqual(16, board1._ep_target_square_to_board('a3'))

    def test_can_convert_any_ep_target_square(self):
        self.assertEqual(46, board1._ep_target_square_to_board('g6'))

    # half move clock
    def test_can_convert_half_move_clock_value(self):
        self.assertEqual(0, board1._half_move_clock_to_board('0'))

    def test_can_convert_any_half_move_clock_value(self):
        self.assertEqual(1, board1._half_move_clock_to_board('1'))

    # turn number
    def test_can_convert_turn_number_value(self):
        self.assertEqual(1, board1._turn_number_to_board('1'))

    def test_can_convert_any_turn_number_value(self):
        self.assertEqual(2, board1._turn_number_to_board('2'))


class FenConversionTestCase(unittest.TestCase):
    # positions
    def test_can_convert_empty_board(self):
        self.assertEqual('8/8/8/8/8/8/8/8', board1._pieces_to_fen(set()))

    def test_can_convert_white_king_on_first_rank(self):
        pieces = {board1._create_piece(0, True, 5)}
        self.assertEqual('8/8/8/8/8/8/8/K7', board1._pieces_to_fen(pieces))

    def test_can_convert_white_king_on_second_rank(self):
        pieces = {board1._create_piece(8, True, 5)}
        self.assertEqual('8/8/8/8/8/8/K7/8', board1._pieces_to_fen(pieces))

    def test_can_convert_white_king_on_any_rank(self):
        pieces = {board1._create_piece(32, True, 5)}
        self.assertEqual('8/8/8/K7/8/8/8/8', board1._pieces_to_fen(pieces))

    def test_can_convert_white_king_on_second_file(self):
        pieces = {board1._create_piece(1, True, 5)}
        self.assertEqual('8/8/8/8/8/8/8/1K6', board1._pieces_to_fen(pieces))

    def test_can_convert_white_king_on_any_file(self):
        pieces = {board1._create_piece(3, True, 5)}
        self.assertEqual('8/8/8/8/8/8/8/3K4', board1._pieces_to_fen(pieces))

    def test_can_convert_white_king_on_any_rank_and_any_file(self):
        pieces = {board1._create_piece(30, True, 5)}
        self.assertEqual('8/8/8/8/6K1/8/8/8', board1._pieces_to_fen(pieces))

    def test_can_convert_white_queen(self):
        pieces = {board1._create_piece(0, True, 4)}
        self.assertEqual('8/8/8/8/8/8/8/Q7', board1._pieces_to_fen(pieces))

    def test_can_convert_white_rook(self):
        pieces = {board1._create_piece(0, True, 3)}
        self.assertEqual('8/8/8/8/8/8/8/R7', board1._pieces_to_fen(pieces))

    def test_can_convert_white_bishop(self):
        pieces = {board1._create_piece(0, True, 2)}
        self.assertEqual('8/8/8/8/8/8/8/B7', board1._pieces_to_fen(pieces))

    def test_can_convert_white_knight(self):
        pieces = {board1._create_piece(0, True, 1)}
        self.assertEqual('8/8/8/8/8/8/8/N7', board1._pieces_to_fen(pieces))

    def test_can_convert_white_pawn(self):
        pieces = {board1._create_piece(0, True, 0)}
        self.assertEqual('8/8/8/8/8/8/8/P7', board1._pieces_to_fen(pieces))

    def test_can_convert_black_pieces(self):
        pieces = {board1._create_piece(0, False, 5)}
        self.assertEqual('8/8/8/8/8/8/8/k7', board1._pieces_to_fen(pieces))

    def test_can_convert_multiple_pieces(self):
        piece_data = [[7, True, 0], [17, True, 4], [22, False, 1], [35, True, 2], [54, False, 3], [58, False, 5]]
        pieces = {board1._create_piece(p, c, t) for p, c, t in piece_data}
        self.assertEqual('2k5/6r1/8/3B4/8/1Q4n1/8/7P', board1._pieces_to_fen(pieces))

    def test_can_convert_complex_positions(self):
        piece_data = [[2, True, 5], [6, True, 3], [8, True, 0], [9, True, 0], [15, True, 0], [20, True, 0],
                      [25, True, 2], [26, False, 0], [28, False, 0], [29, True, 0], [30, False, 4], [35, False, 2],
                      [36, True, 0], [42, False, 0], [43, True, 3], [48, False, 0], [49, False, 0], [53, False, 3],
                      [54, False, 0], [55, False, 0], [59, False, 3], [62, False, 5]]
        pieces = {board1._create_piece(p, c, t) for p, c, t in piece_data}
        self.assertEqual('3r2k1/pp3rpp/2pR4/3bP3/1Bp1pPq1/4P3/PP5P/2K3R1', board1._pieces_to_fen(pieces))

    def test_converts_pieces_of_board_object_if_no_param_given(self):
        self.assertEqual('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', board1._pieces_to_fen())

    # color to move
    def test_can_convert_white_to_move(self):
        self.assertEqual('w', board1._color_to_move_to_fen(True))

    def test_can_convert_black_to_move(self):
        self.assertEqual('b', board1._color_to_move_to_fen(False))

    def test_converts_color_to_move_of_board_object_if_no_param_given(self):
        self.assertEqual('w', board1._color_to_move_to_fen())

    # castling rights
    def test_can_convert_no_castling_rights(self):
        self.assertEqual('-', board1._castling_rights_to_fen([False, False, False, False]))

    def test_can_convert_white_kingside_castling_right(self):
        self.assertEqual('K', board1._castling_rights_to_fen([True, False, False, False]))

    def test_can_convert_white_queenside_castling_right(self):
        self.assertEqual('Q', board1._castling_rights_to_fen([False, True, False, False]))

    def test_can_convert_black_kingside_castling_right(self):
        self.assertEqual('k', board1._castling_rights_to_fen([False, False, True, False]))

    def test_can_convert_black_queenside_castling_right(self):
        self.assertEqual('q', board1._castling_rights_to_fen([False, False, False, True]))

    def test_can_convert_all_castling_rights(self):
        self.assertEqual('KQkq', board1._castling_rights_to_fen([True, True, True, True]))

    def test_can_convert_mixed_castling_rights(self):
        self.assertEqual('Qk', board1._castling_rights_to_fen([False, True, True, False]))

    def test_converts_castling_rights_of_board_object_if_no_param_given(self):
        self.assertEqual('KQkq', board1._castling_rights_to_fen())

    # ep target square
    def test_can_convert_no_ep_target_square(self):
        self.assertEqual('-', board1._ep_target_square_to_fen(None))

    def test_can_convert_ep_target_square(self):
        self.assertEqual('a3', board1._ep_target_square_to_fen(16))

    def test_can_convert_any_ep_target_square(self):
        self.assertEqual('g6', board1._ep_target_square_to_fen(46))

    def test_converts_ep_target_square_of_board_object_if_no_param_given(self):
        self.assertEqual('-', board1._ep_target_square_to_fen())

    # half move clock
    def test_can_convert_half_move_clock_value(self):
        self.assertEqual('0', board1._half_move_clock_to_fen(0))

    def test_can_convert_any_half_move_clock_value(self):
        self.assertEqual('1', board1._half_move_clock_to_fen(1))

    def test_converts_half_move_clock_of_board_object_if_no_param_given(self):
        self.assertEqual('0', board1._half_move_clock_to_fen())

    # turn number
    def test_can_convert_turn_number_value(self):
        self.assertEqual('1', board1._turn_number_to_fen(1))

    def test_can_convert_any_turn_number_value(self):
        self.assertEqual('2', board1._turn_number_to_fen(2))

    def test_converts_turn_number_of_board_object_if_no_param_given(self):
        self.assertEqual('1', board1._turn_number_to_fen())


if __name__ == '__main__':
    unittest.main()
