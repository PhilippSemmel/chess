import unittest
from board import Board, Pawn, Knight, Bishop, Rook, Queen, King

board1 = Board()
board2 = Board('rnbqkbnr/ppppp1pp/8/5p2/5P2/8/PPPPP1PP/RNBQKBNR b - f5 2 2')


class ConstructionTestCase(unittest.TestCase):
    def test_pieces_initialize_correctly(self):
        for pos in [8, 9, 10, 11, 12, 13, 14, 15, 48, 49, 50, 51, 52, 53, 54, 55]:  # tests pawns
            self.assertEqual(Pawn, type(board1._get_piece(pos)))
        for pos in [1, 6, 57, 62]:  # tests knight
            self.assertEqual(Knight, type(board1._get_piece(pos)))
        for pos in [2, 5, 58, 61]:  # tests bishops
            self.assertEqual(Bishop, type(board1._get_piece(pos)))
        for pos in [0, 7, 56, 63]:  # tests rooks
            self.assertEqual(Rook, type(board1._get_piece(pos)))
        for pos in [3, 59]:  # tests queens
            self.assertEqual(Queen, type(board1._get_piece(pos)))
        for pos in [4, 60]:  # tests kings
            self.assertEqual(King, type(board1._get_piece(pos)))

    def test_pieces_always_initialize_correctly(self):
        for pos in [8, 9, 10, 11, 12, 14, 15, 29, 37, 48, 49, 50, 51, 52, 54, 55]:  # tests pawns
            self.assertEqual(Pawn, type(board2._get_piece(pos)))
        for pos in [1, 6, 57, 62]:  # tests knight
            self.assertEqual(Knight, type(board2._get_piece(pos)))
        for pos in [2, 5, 58, 61]:  # tests bishops
            self.assertEqual(Bishop, type(board2._get_piece(pos)))
        for pos in [0, 7, 56, 63]:  # tests rooks
            self.assertEqual(Rook, type(board2._get_piece(pos)))
        for pos in [3, 59]:  # tests queens
            self.assertEqual(Queen, type(board2._get_piece(pos)))
        for pos in [4, 60]:  # tests kings
            self.assertEqual(King, type(board2._get_piece(pos)))

    def test_white_to_move_is_correct(self):
        self.assertTrue(board1._white_to_move)

    def test_white_to_move_is_always_correct(self):
        self.assertFalse(board2._white_to_move)

    def test_castling_rights_are_correct(self):
        self.assertEqual([True, True, True, True], board1._castling_rights)

    def test_castling_rights_are_always_correct(self):
        self.assertEqual([False, False, False, False], board2._castling_rights)

    def test_ep_target_square_is_correct(self):
        self.assertIsNone(board1._ep_target_square)

    def test_ep_target_square_is_always_correct(self):
        self.assertEqual(37, board2._ep_target_square)

    def test_half_move_clock_is_correct(self):
        self.assertEqual(0, board1._half_move_clock)

    def test_half_move_clock_is_always_correct(self):
        self.assertEqual(2, board2._half_move_clock)

    def test_turn_number_is_correct(self):
        self.assertEqual(1, board1._turn_number)

    def test_turn_number_is_always_correct(self):
        self.assertEqual(2, board2._turn_number)

    def test_data_log_is_empty_list(self):
        self.assertEqual([], board1._data_log)

    def test_data_log_is_always_empty_list(self):
        self.assertEqual([], board2._data_log)

    def test_moves_log_is_empty_list(self):
        self.assertEqual([], board1._moves_log)

    def test_moves_log_is_always_empty_list(self):
        self.assertEqual([], board2._moves_log)

    def test_positions_log_is_list_with_all_piece_positions(self):
        self.assertEqual([{('P', 8), ('P', 9), ('P', 10), ('P', 11), ('P', 12), ('P', 13), ('P', 14), ('P', 15),
                           ('p', 48), ('p', 49), ('p', 50), ('p', 51), ('p', 52), ('p', 53), ('p', 54), ('p', 55),
                           ('R', 0), ('N', 1), ('B', 2), ('Q', 3), ('K', 4), ('B', 5), ('N', 6), ('R', 7), ('r', 56),
                           ('n', 57), ('b', 58), ('q', 59), ('k', 60), ('b', 61), ('n', 62), ('r', 63)}],
                         board1._positions_log)

    def test_positions_log_always_is_list_with_all_piece_positions(self):
        self.assertEqual([{('P', 8), ('P', 9), ('P', 10), ('P', 11), ('P', 12), ('P', 29), ('P', 14), ('P', 15),
                           ('p', 48), ('p', 49), ('p', 50), ('p', 51), ('p', 52), ('p', 37), ('p', 54), ('p', 55),
                           ('R', 0), ('N', 1), ('B', 2), ('Q', 3), ('K', 4), ('B', 5), ('N', 6), ('R', 7), ('r', 56),
                           ('n', 57), ('b', 58), ('q', 59), ('k', 60), ('b', 61), ('n', 62), ('r', 63)}],
                         board2._positions_log)


class ChessGameDataGetterTestCase(unittest.TestCase):
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


class BoardStateGetterTestCase(unittest.TestCase):
    @staticmethod
    def make_reoccurring_moves(board: Board) -> None:
        board.make_move((1, 18, None))
        board.make_move((57, 42, None))
        board.make_move((18, 1, None))
        board.make_move((42, 57, None))

    def test_no_checkmate_if_more_than_one_move_available(self):
        board = Board('k7/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertFalse(board.checkmate)

    def test_checkmate_if_no_move_available_and_king_in_check(self):
        board = Board('k7/8/8/8/8/2b5/1q6/K7 w - - 0 1')
        self.assertTrue(board.checkmate)

    def test_no_checkmate_if_no_move_available_and_king_not_in_check(self):
        board = Board('k7/8/8/8/8/2b5/1r6/K7 w - - 0 1')
        self.assertFalse(board.checkmate)

    def test_black_can_be_in_checkmate_as_well(self):
        board = Board('K7/8/8/8/8/2B5/1Q6/k7 b - - 0 1')
        self.assertTrue(board.checkmate)

    def test_no_stalemate_if_more_than_one_move_available(self):
        board = Board('k7/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertFalse(board.stalemate)

    def test_no_stalemate_if_no_move_available_and_king_in_check(self):
        board = Board('k7/8/8/8/8/2b5/1q6/K7 w - - 0 1')
        self.assertFalse(board.stalemate)

    def test_stalemate_if_no_move_available_and_king_not_in_check(self):
        board = Board('k7/8/8/8/8/2b5/1r6/K7 w - - 0 1')
        self.assertTrue(board.stalemate)

    def test_black_can_be_in_stalemate_as_well(self):
        board = Board('K7/8/8/8/8/2B5/1R6/k7 b - - 0 1')
        self.assertTrue(board.stalemate)

    def test_seventy_five_moves_rule_does_not_apply_when_half_clock_value_is_less_than_seventy_five(self):
        self.assertFalse(board1.seventy_five_moves_rule_applies)

    def test_seventy_five_moves_rule_does_not_apply_when_half_clock_value_is_seventy_four(self):
        board = Board('8/8/8/8/8/8/8/kp5K w - - 74 1')
        self.assertFalse(board.seventy_five_moves_rule_applies)

    def test_seventy_five_moves_rule_does_apply_when_half_clock_value_is_seventy_five(self):
        board = Board('8/8/8/8/8/8/8/kp5K w - - 75 1')
        self.assertTrue(board.seventy_five_moves_rule_applies)

    def test_seventy_five_moves_rule_does_apply_when_half_clock_value_is_more_than_seventy_five(self):
        board = Board('8/8/8/8/8/8/8/kp5K w - - 76 1')
        self.assertTrue(board.seventy_five_moves_rule_applies)

    def test_seventy_five_moves_rule_does_not_apply_when_active_player_is_in_checkmate(self):
        board = Board('k7/8/8/8/8/2b5/1q6/K7 w - - 75 1')
        self.assertFalse(board.seventy_five_moves_rule_applies)

    def test_fivefold_repetition_rule_does_not_apply_if_not_in_turn_nine_or_earlier(self):
        self.assertFalse(board1.fivefold_repetition_rule_applies)

    def test_fivefold_repetition_applies_if_needed_position_were_created(self):
        board_ = Board()  # first
        self.make_reoccurring_moves(board_)  # second
        self.make_reoccurring_moves(board_)  # third
        self.make_reoccurring_moves(board_)  # fourth
        self.make_reoccurring_moves(board_)  # fifth
        self.assertTrue(board_.fivefold_repetition_rule_applies)

    def test_fivefold_repetition_applies_if_needed_position_were_created_in_any_turn(self):
        board_ = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 10 1')  # first
        self.make_reoccurring_moves(board_)  # second
        self.make_reoccurring_moves(board_)  # third
        self.make_reoccurring_moves(board_)  # fourth
        self.make_reoccurring_moves(board_)  # fifth
        self.assertTrue(board_.fivefold_repetition_rule_applies)

    def test_fivefold_repetition_applies_if_needed_position_were_created_no_matter_the_moves_leading_to_them(self):
        board_ = Board()  # first
        self.make_reoccurring_moves(board_)  # second
        self.make_reoccurring_moves(board_)  # third
        self.make_reoccurring_moves(board_)  # fourth
        board_.make_move((1, 16, None))
        board_.make_move((57, 40, None))
        board_.make_move((16, 1, None))
        board_.make_move((40, 57, None))  # fifth
        self.assertTrue(board_.fivefold_repetition_rule_applies)

    def test_fivefold_repetition_does_not_apply_if_castling_rights_change(self):
        def make_reoccurring_move(board: Board):
            board.make_move((0, 8, None))
            board.make_move((57, 40, None))
            board.make_move((8, 0, None))
            board.make_move((40, 57, None))

        board_ = Board('rnbqkbnr/pppppppp/8/8/8/8/1PPPPPPP/RNBQKBPR w KQkq - 0 1')  # first
        make_reoccurring_move(board_)  # does not count due to the change of castling rights/second
        make_reoccurring_move(board_)  # first/third
        make_reoccurring_move(board_)  # second/forth
        make_reoccurring_move(board_)  # third/fifth
        self.assertFalse(board_.fivefold_repetition_rule_applies)

    def test_fivefold_repetition_does_not_apply_if_castling_rights_change_in_any_turn(self):
        def make_reoccurring_move(board: Board):
            board.make_move((0, 8, None))
            board.make_move((57, 40, None))
            board.make_move((8, 0, None))
            board.make_move((40, 57, None))

        board_ = Board('rnbqkbnr/pppppppp/8/8/8/8/1PPPPPPP/RNBQKBPR w KQkq - 0 10')  # first
        make_reoccurring_move(board_)  # does not count due to the change of castling rights/second
        make_reoccurring_move(board_)  # first/third
        make_reoccurring_move(board_)  # second/forth
        make_reoccurring_move(board_)  # third/fifth
        self.assertFalse(board_.fivefold_repetition_rule_applies)

    def test_fivefold_repetition_does_not_apply_if_ep_target_square_changes(self):
        def make_reoccurring_move(board: Board):
            board.make_move((0, 8, None))
            board.make_move((57, 40, None))
            board.make_move((8, 0, None))
            board.make_move((40, 57, None))

        board_ = Board('rnbqkbnr/pppppppp/8/8/8/8/1PPPPPPP/RNBQKBPR w KQkq a3 0 1')  # first
        make_reoccurring_move(board_)  # does not count due to the change of ep target square/second
        make_reoccurring_move(board_)  # first/third
        make_reoccurring_move(board_)  # second/forth
        make_reoccurring_move(board_)  # third/fifth
        self.assertFalse(board_.fivefold_repetition_rule_applies)

    def test_fivefold_repetition_applies_if_needed_position_were_created_for_black_as_well(self):
        board_ = Board()
        self.make_reoccurring_moves(board_)  # first
        self.make_reoccurring_moves(board_)  # second
        self.make_reoccurring_moves(board_)  # third
        self.make_reoccurring_moves(board_)  # fourth
        board_.make_move((1, 18, None))  # fifth
        self.assertTrue(board_.fivefold_repetition_rule_applies)


class PieceTestCase(unittest.TestCase):
    def test_can_get_active_pieces_publicly(self):
        self.assertEqual(board1._get_active_pieces(), board1._active_pieces)

    def test_can_get_any_active_pieces_publicly(self):
        self.assertEqual(board2._get_active_pieces(), board2._active_pieces)

    def test_does_not_recalculate_active_pieces(self):
        self.assertIs(board1._active_pieces, board1._active_pieces)

    def test_does_never_recalculate_active_pieces(self):
        self.assertIs(board2._active_pieces, board2._active_pieces)

    def test_all_pieces_on_board_in_active_pieces_set(self):
        board = Board('8/8/8/8/8/8/8/K7 w - - 0 1')
        piece = board._get_piece(0)
        self.assertEqual({piece}, board._get_active_pieces())

    def test_captured_piece_are_not_in_active_pieces_set(self):
        board = Board('8/8/8/8/8/8/8/PK6 w - - 0 1')
        piece = board._get_piece(0)
        piece.capture(1, True)
        self.assertEqual({board._get_king(True)}, board._get_active_pieces())

    def test_promoted_piece_are_not_in_active_pieces_set(self):
        board = Board('8/8/8/8/8/8/8/PK6 w - - 0 1')
        piece = board._get_piece(0)
        piece.promote(1, True)
        self.assertEqual({board._get_king(True)}, board._get_active_pieces())

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
        board._clear_active_pieces_cache()
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
        board = Board('8/8/8/8/8/8/8/k6K w - - 0 1')
        king = board._get_piece(0)
        self.assertIs(king, board._get_king(False))

    def test_can_get_any_black_king(self):
        board = Board('8/8/8/8/8/8/8/K6k w - - 0 1')
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

    def test_can_create_white_pawn_on_pos(self):
        piece = board1._create_piece(0, 'P')
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(Pawn, type(piece))

    def test_can_create_white_pawn_on_any_pos(self):
        piece = board1._create_piece(45, 'P')
        self.assertEqual(45, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(Pawn, type(piece))

    def test_can_create_black_pawn(self):
        piece = board1._create_piece(0, 'p')
        self.assertEqual(0, piece.pos)
        self.assertFalse(piece.white_piece)
        self.assertEqual(Pawn, type(piece))

    def test_can_create_knight(self):
        piece = board1._create_piece(0, 'N')
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(Knight, type(piece))

    def test_can_create_bishop(self):
        piece = board1._create_piece(0, 'B')
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(Bishop, type(piece))

    def test_can_create_rook(self):
        piece = board1._create_piece(0, 'R')
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(Rook, type(piece))

    def test_can_create_queen(self):
        piece = board1._create_piece(0, 'Q')
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(Queen, type(piece))

    def test_can_create_king(self):
        piece = board1._create_piece(0, 'K')
        self.assertEqual(0, piece.pos)
        self.assertTrue(piece.white_piece)
        self.assertEqual(King, type(piece))


class PositionsStateTestCase(unittest.TestCase):
    def test_square_is_empty_if_square_is_empty(self):
        self.assertTrue(board1.is_square_empty(36))

    def test_square_is_not_empty_if_black_piece_on_square(self):
        self.assertFalse(board2.is_square_empty(37))

    def test_square_is_not_empty_if_white_piece_on_square(self):
        self.assertFalse(board2.is_square_empty(29))

    def test_is_square_empty_can_use_given_piece_set(self):
        self.assertTrue(board1.is_square_empty(16, set()))

    def test_is_square_empty_uses_active_pieces_set(self):
        board = Board()
        board._get_piece(8).capture(1, True)
        board._clear_active_pieces_cache()
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
        board._clear_active_pieces_cache()
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
        board._clear_active_pieces_cache()
        self.assertFalse(board.opponent_piece_on_square(8, False))

    def test_square_is_not_attacked_if_not_attacked_by_opponent_piece(self):
        board = Board('8/8/8/8/8/8/8/7K w - - 0 1')
        self.assertFalse(board.is_square_attacked(0, True))

    def test_square_is_attacked_if_attacked_by_opponent_piece(self):
        board = Board('K7/8/8/8/8/8/1q6/8 w - - 0 1')
        self.assertTrue(board.is_square_attacked(0, True))

    def test_square_is_attacked_if_attacked_by_opponent_piece_on_any_square(self):
        board = Board('7q/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertTrue(board.is_square_attacked(0, True))

    def test_square_is_attacked_if_attacked_by_only_opponent_piece_of_many_pieces(self):
        board = Board('Kppppppq/pppppp1p/ppppp1pp/pppp1ppp/ppp1pppp/pp1ppppp/p1pppppp/1ppppppp w - - 0 1')
        self.assertTrue(board.is_square_attacked(0, True))

    def test_any_square_is_attacked_if_attacked_by_opponent_piece(self):
        board = Board('8/1q6/8/8/8/8/8/K7 w - - 0 1')
        self.assertTrue(board.is_square_attacked(7, True))

    def test_square_is_not_attacked_if_attacked_by_own_piece(self):
        board = Board('7Q/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertFalse(board.is_square_attacked(7, True))

    def test_is_square_attacked_uses_active_pieces_set(self):
        board = Board()
        board._get_piece(8).capture(1, True)
        board._clear_active_pieces_cache()
        self.assertTrue(board.is_square_attacked(48, False))

    def test_white_king_is_not_attacked_if_not_attacked(self):
        self.assertFalse(board1.is_king_attacked(True))

    def test_white_king_is_attacked_if_attacked(self):
        board = Board('k7/r7/8/8/8/8/8/K7 w - - 0 1')
        self.assertTrue(board.is_king_attacked(True))

    def test_white_king_can_be_attacked_anywhere(self):
        board = Board('K7/8/8/8/8/8/r7/k7 w - - 0 1')
        self.assertTrue(board.is_king_attacked(True))

    def test_white_king_is_not_attacked_by_own_pieces(self):
        board = Board('Q7/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertFalse(board.is_king_attacked(True))

    def test_black_king_can_be_attacked_as_well(self):
        board = Board('k7/8/8/8/8/8/R7/K7 w - - 0 1')
        self.assertTrue(board.is_king_attacked(False))

    def test_is_king_attacked_uses_active_pieces_set(self):
        board = Board('k7/r7/8/8/8/8/8/K7 w - - 0 1')
        board._get_piece(48).capture(1, True)
        board._clear_active_pieces_cache()
        self.assertFalse(board.is_king_attacked(True))


class MoveGenerationTestCase(unittest.TestCase):
    # general
    def test_cannot_generate_black_moves_when_white_to_move(self):
        board = Board('k7/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertEqual({(0, 1, None), (0, 8, None), (0, 9, None)}, board._legal_moves)

    # white pieces
    def test_can_generate_white_king_moves(self):
        board = Board('k7/8/8/8/8/8/1K6/8 w - - 0 1')
        self.assertEqual({(9, 0, None), (9, 1, None), (9, 2, None), (9, 8, None), (9, 10, None), (9, 16, None),
                          (9, 17, None), (9, 18, None)}, board._legal_moves)

    def test_can_generate_any_white_king_moves(self):
        board = Board('k7/8/8/8/8/8/6K1/8 w - - 0 1')
        self.assertEqual({(14, 5, None), (14, 6, None), (14, 7, None), (14, 13, None), (14, 15, None), (14, 21, None),
                          (14, 22, None), (14, 23, None)}, board._legal_moves)

    def test_can_generate_white_pawn_moves(self):
        board = Board('k7/8/8/8/8/8/P7/K7 w - - 0 1')
        self.assertEqual({(8, 16, None), (8, 24, None)} | {(0, 1, None), (0, 9, None)}, board._legal_moves)

    def test_can_generate_any_white_pawn_moves(self):
        board = Board('k7/8/8/8/4P3/8/8/K7 w - - 0 1')
        self.assertEqual({(28, 36, None)} | {(0, 1, None), (0, 8, None), (0, 9, None)}, board._legal_moves)

    def test_can_generate_white_knight_moves(self):
        board = Board('k7/8/8/8/8/8/8/KN6 w - - 0 1')
        self.assertEqual({(1, 11, None), (1, 16, None), (1, 18, None)} | {(0, 8, None), (0, 9, None)},
                         board._legal_moves)

    def test_can_generate_any_white_knight_moves(self):
        board = Board('k7/8/8/8/8/8/8/6NK w - - 0 1')
        self.assertEqual({(6, 12, None), (6, 21, None), (6, 23, None)} | {(7, 14, None), (7, 15, None)},
                         board._legal_moves)

    def test_can_generate_white_bishop_moves(self):
        board = Board('k7/8/8/8/8/8/1B6/1K6 w - - 0 1')
        self.assertEqual({(9, 0, None), (9, 18, None), (9, 27, None), (9, 36, None), (9, 45, None), (9, 54, None),
                          (9, 63, None), (9, 2, None), (9, 16, None)} | {(1, 0, None), (1, 8, None), (1, 2, None),
                                                                         (1, 10, None)}, board._legal_moves)

    def test_can_generate_any_white_bishop_moves(self):
        board = Board('7k/8/8/8/8/8/6B1/6K1 w - - 0 1')
        self.assertEqual({(14, 7, None), (14, 21, None), (14, 28, None), (14, 35, None), (14, 42, None), (14, 49, None),
                          (14, 56, None), (14, 23, None), (14, 5, None)} | {(6, 5, None), (6, 7, None), (6, 13, None),
                                                                            (6, 15, None)}, board._legal_moves)

    def test_can_generate_white_rook_moves(self):
        board = Board('7k/8/8/8/8/8/1R6/K7 w - - 0 1')
        self.assertEqual({(9, 1, None), (9, 8, None), (9, 10, None), (9, 11, None), (9, 12, None), (9, 13, None),
                          (9, 14, None), (9, 15, None), (9, 17, None), (9, 25, None), (9, 33, None), (9, 41, None),
                          (9, 49, None), (9, 57, None)} | {(0, 1, None), (0, 8, None)}, board._legal_moves)

    def test_can_generate_any_white_rook_moves(self):
        board = Board('k7/8/8/8/8/8/6R1/7K w - - 0 1')
        self.assertEqual({(14, 15, None), (14, 6, None), (14, 13, None), (14, 12, None), (14, 11, None), (14, 10, None),
                          (14, 9, None), (14, 8, None), (14, 22, None), (14, 30, None), (14, 38, None), (14, 46, None),
                          (14, 54, None), (14, 62, None)} | {(7, 6, None), (7, 15, None)},
                         board._legal_moves)

    def test_can_generate_white_queen_moves(self):
        board = Board('K7/8/8/8/8/8/1Q6/7k w - - 0 1')
        self.assertEqual(
            {(9, 1, None), (9, 8, None), (9, 10, None), (9, 11, None), (9, 12, None), (9, 13, None), (9, 14, None),
             (9, 15, None), (9, 17, None), (9, 25, None),
             (9, 33, None), (9, 41, None), (9, 49, None), (9, 57, None), (9, 0, None), (9, 18, None), (9, 27, None),
             (9, 36, None), (9, 45, None), (9, 54, None),
             (9, 63, None), (9, 2, None), (9, 16, None)} | {(56, 48, None), (56, 49, None), (56, 57, None)},
            board._legal_moves)

    def test_can_generate_any_white_queen_moves(self):
        board = Board('7K/8/8/8/8/8/6Q1/k7 w - - 0 1')
        self.assertEqual({(14, 15, None), (14, 6, None), (14, 13, None), (14, 12, None), (14, 11, None), (14, 10, None),
                          (14, 9, None), (14, 8, None), (14, 22, None),
                          (14, 30, None), (14, 38, None), (14, 46, None), (14, 54, None), (14, 62, None), (14, 7, None),
                          (14, 21, None), (14, 28, None), (14, 35, None),
                          (14, 42, None), (14, 49, None), (14, 56, None), (14, 23, None), (14, 5, None)} | {
                             (63, 54, None), (63, 55, None), (63, 62, None)},
                         board._legal_moves)

    def test_can_generate_multiple_white_moves(self):
        board = Board('k7/8/8/8/1P1PP3/8/KQB5/N1RN4 w - - 0 1')
        self.assertEqual(
            {(0, 17, None), (2, 1, None), (3, 18, None), (3, 20, None), (3, 13, None), (8, 1, None), (8, 16, None),
             (8, 17, None), (9, 16, None), (9, 17, None),
             (9, 18, None), (9, 1, None), (10, 1, None), (10, 17, None), (10, 19, None), (10, 24, None), (25, 33, None),
             (27, 35, None), (28, 36, None)},
            board._legal_moves)

    # black pieces
    def test_can_generate_black_king_moves(self):
        board = Board('K7/8/8/8/8/8/1k6/8 b - - 0 1')
        self.assertEqual(
            {(9, 0, None), (9, 1, None), (9, 2, None), (9, 8, None), (9, 10, None), (9, 16, None), (9, 17, None),
             (9, 18, None)}, board._legal_moves)

    def test_can_generate_any_black_king_moves(self):
        board = Board('K7/8/8/8/8/8/6k1/8 b - - 0 1')
        self.assertEqual({(14, 5, None), (14, 6, None), (14, 7, None), (14, 13, None), (14, 15, None), (14, 21, None),
                          (14, 22, None), (14, 23, None)},
                         board._legal_moves)

    def test_can_generate_black_pawn_moves(self):
        board = Board('k7/p7/8/8/8/8/8/K7 b - - 0 1')
        self.assertEqual({(48, 40, None), (48, 32, None)} | {(56, 49, None), (56, 57, None)}, board._legal_moves)

    def test_can_generate_any_black_pawn_moves(self):
        board = Board('k7/8/2p5/8/8/8/8/K7 b - - 0 1')
        self.assertEqual({(42, 34, None)} | {(56, 48, None), (56, 49, None), (56, 57, None)}, board._legal_moves)

    def test_can_generate_black_knight_moves(self):
        board = Board('K7/8/8/8/8/8/8/kn6 b - - 0 1')
        self.assertEqual({(1, 11, None), (1, 16, None), (1, 18, None)} | {(0, 8, None), (0, 9, None)},
                         board._legal_moves)

    def test_can_generate_any_black_knight_moves(self):
        board = Board('K7/8/8/8/8/8/8/6nk b - - 0 1')
        self.assertEqual({(6, 12, None), (6, 21, None), (6, 23, None)} | {(7, 14, None), (7, 15, None)},
                         board._legal_moves)

    def test_can_generate_black_bishop_moves(self):
        board = Board('K7/8/8/8/8/8/1b6/1k6 b - - 0 1')
        self.assertEqual(
            {(9, 0, None), (9, 18, None), (9, 27, None), (9, 36, None), (9, 45, None), (9, 54, None), (9, 63, None),
             (9, 2, None), (9, 16, None)} |
            {(1, 0, None), (1, 8, None), (1, 2, None), (1, 10, None)}, board._legal_moves)

    def test_can_generate_any_black_bishop_moves(self):
        board = Board('7K/8/8/8/8/8/6b1/6k1 b - - 0 1')
        self.assertEqual({(14, 7, None), (14, 21, None), (14, 28, None), (14, 35, None), (14, 42, None), (14, 49, None),
                          (14, 56, None), (14, 23, None), (14, 5, None)} |
                         {(6, 5, None), (6, 7, None), (6, 13, None), (6, 15, None)}, board._legal_moves)

    def test_can_generate_black_rook_moves(self):
        board = Board('K7/8/8/8/8/8/1r6/k7 b - - 0 1')
        self.assertEqual(
            {(9, 1, None), (9, 8, None), (9, 10, None), (9, 11, None), (9, 12, None), (9, 13, None), (9, 14, None),
             (9, 15, None), (9, 17, None), (9, 25, None),
             (9, 33, None), (9, 41, None), (9, 49, None), (9, 57, None)} | {(0, 1, None), (0, 8, None)},
            board._legal_moves)

    def test_can_generate_any_black_rook_moves(self):
        board = Board('K7/8/8/8/8/8/6r1/7k b - - 0 1')
        self.assertEqual({(14, 15, None), (14, 6, None), (14, 13, None), (14, 12, None), (14, 11, None), (14, 10, None),
                          (14, 9, None), (14, 8, None), (14, 22, None),
                          (14, 30, None), (14, 38, None), (14, 46, None), (14, 54, None), (14, 62, None)} | {
                             (7, 6, None), (7, 15, None)},
                         board._legal_moves)

    def test_can_generate_black_queen_moves(self):
        board = Board('k7/8/8/8/8/8/1q6/7K b - - 0 1')
        self.assertEqual(
            {(9, 1, None), (9, 8, None), (9, 10, None), (9, 11, None), (9, 12, None), (9, 13, None), (9, 14, None),
             (9, 15, None), (9, 17, None), (9, 25, None),
             (9, 33, None), (9, 41, None), (9, 49, None), (9, 57, None), (9, 0, None), (9, 18, None), (9, 27, None),
             (9, 36, None), (9, 45, None), (9, 54, None),
             (9, 63, None), (9, 2, None), (9, 16, None)} | {(56, 48, None), (56, 49, None), (56, 57, None)},
            board._legal_moves)

    def test_can_generate_any_black_queen_moves(self):
        board = Board('7k/8/8/8/8/8/6q1/K7 b - - 0 1')
        self.assertEqual({(14, 15, None), (14, 6, None), (14, 13, None), (14, 12, None), (14, 11, None), (14, 10, None),
                          (14, 9, None), (14, 8, None), (14, 22, None),
                          (14, 30, None), (14, 38, None), (14, 46, None), (14, 54, None), (14, 62, None), (14, 7, None),
                          (14, 21, None), (14, 28, None), (14, 35, None),
                          (14, 42, None), (14, 49, None), (14, 56, None), (14, 23, None), (14, 5, None)} | {
                             (63, 54, None), (63, 55, None), (63, 62, None)},
                         board._legal_moves)

    def test_can_generate_multiple_black_moves(self):
        board = Board('K7/8/8/8/1p1pp3/8/kqb5/n1rn4 b - - 0 1')
        self.assertEqual(
            {(0, 17, None), (2, 1, None), (3, 18, None), (3, 20, None), (3, 13, None), (8, 1, None), (8, 16, None),
             (8, 17, None), (9, 16, None), (9, 17, None),
             (9, 18, None), (9, 1, None), (10, 1, None), (10, 17, None), (10, 19, None), (10, 24, None), (25, 17, None),
             (27, 19, None), (28, 20, None)},
            board._legal_moves)


class LegalMoveGenerationTextCase(unittest.TestCase):
    def test_can_get_legal_moves_publicly(self):
        self.assertEqual(board1._legal_moves, board1.legal_moves)

    def test_can_get_any_legal_moves_publicly(self):
        self.assertEqual(board2._legal_moves, board2.legal_moves)

    def test_can_get_legal_moves_privately(self):
        self.assertEqual(board1._get_legal_moves(), board1._legal_moves)

    def test_can_get_any_legal_moves_privately(self):
        self.assertEqual(board2._get_legal_moves(), board2._legal_moves)

    def test_does_not_recalculate_legal_moves(self):
        self.assertIs(board1._legal_moves, board1._legal_moves)

    def test_does_never_recalculate_legal_moves(self):
        self.assertIs(board2._legal_moves, board2._legal_moves)

    def test_king_can_not_move_into_check(self):
        board = Board('k7/8/8/8/8/8/7r/K7 w - - 0 1')
        self.assertEqual({(0, 1, None)}, board._legal_moves)

    def test_king_can_capture_checking_piece(self):
        board = Board('k7/8/8/8/8/8/7r/7K w - - 0 1')
        self.assertEqual({(7, 15, None), (7, 6, None)}, board._legal_moves)

    def test_king_can_not_capture_checking_piece_if_it_is_saved(self):
        board = Board('k6r/8/8/8/8/8/7r/7K w - - 0 1')
        self.assertEqual({(7, 6, None)}, board._legal_moves)

    def test_king_can_move_out_of_check(self):
        board = Board('k6r/8/8/8/8/8/7r/7K w - - 0 1')
        self.assertEqual({(7, 6, None)}, board._legal_moves)

    def test_other_piece_can_capture_checking_piece(self):
        board = Board('R6r/6r1/8/8/8/8/8/1k5K w - - 0 1')
        self.assertEqual({(56, 63, None)}, board._legal_moves)

    def test_other_piece_can_interpose_checking_piece(self):
        board = Board('7r/6r1/R7/8/8/8/8/1k5K w - - 0 1')
        self.assertEqual({(40, 47, None)}, board._legal_moves)

    def test_other_piece_can_not_expose_king_to_check(self):
        board = Board('7r/6r1/8/8/8/8/7R/k6K w - - 0 1')
        self.assertEqual(
            {(15, 23, None), (15, 31, None), (15, 39, None), (15, 47, None), (15, 55, None), (15, 63, None)},
            board._legal_moves)

    def test_other_piece_cannot_capture_checking_piece_when_in_double_check(self):
        board = Board('r6R/1k6/8/8/8/8/1P6/K6r w - - 0 1')
        self.assertEqual(set(), board._legal_moves)

    def test_other_piece_cannot_interpose_checking_piece_when_in_double_check(self):
        board = Board('r6k/6R1/8/8/8/8/1P6/K6r w - - 0 1')
        self.assertEqual(set(), board._legal_moves)

    def test_king_cannot_move_if_in_checkmate(self):
        board = Board('k7/8/8/8/8/2b5/1q6/K7 w - - 0 1')
        self.assertEqual(set(), board._legal_moves)

    def test_other_pieces_cannot_move_if_king_is_in_checkmate(self):
        board = Board('k7/8/8/8/8/2b5/1q6/K6P w - - 0 1')
        self.assertEqual(set(), board._legal_moves)

    def test_king_cannot_move_if_in_stalemate(self):
        board = Board('k7/8/8/8/8/2b5/1r6/K7 w - - 0 1')
        self.assertEqual(set(), board._legal_moves)

    def test_other_pieces_can_move_if_king_is_in_stalemate(self):
        board = Board('k7/8/8/8/8/2b5/1r6/K6P w - - 0 1')
        self.assertEqual({(7, 15, None)}, board._legal_moves)


class MakeMoveTestCase(unittest.TestCase):
    # piece tests
    def test_starting_pos_is_empty(self):
        board = Board('k7/8/8/8/8/8/K7/8 w - - 0 1')
        board.make_move((8, 16, None))
        self.assertRaises(ValueError, board._get_piece, 8)

    def test_legal_moves_change(self):
        board = Board('k7/8/8/8/8/8/K7/8 w - - 0 1')
        old_moves = board.legal_moves
        board.make_move((8, 16, None))
        self.assertNotEqual(old_moves, board.legal_moves)

    def test_piece_on_final_square(self):
        board = Board('7k/8/8/8/8/8/K7/8 w - - 0 1')
        king = board._get_piece(8)
        board.make_move((8, 16, None))
        self.assertIs(king, board._get_piece(16))

    def test_can_make_king_moves(self):
        board = Board('k7/8/8/8/8/8/1K6/8 w - - 0 1')
        king = board._get_piece(9)
        board.make_move((9, 10, None))
        self.assertIs(king, board._get_piece(10))

    def test_can_make_any_king_moves(self):
        board = Board('k7/8/8/8/8/8/1K6/8 w - - 0 1')
        king = board._get_piece(9)
        board.make_move((9, 8, None))
        self.assertIs(king, board._get_piece(8))

    def test_can_make_pawn_moves_as_white(self):
        board = Board('k7/8/8/8/8/8/P7/K7 w - - 0 1')
        pawn = board._get_piece(8)
        board.make_move((8, 16, None))
        self.assertIs(pawn, board._get_piece(16))

    def test_can_make_any_pawn_moves_as_white(self):
        board = Board('k7/8/8/8/8/8/1P6/K7 w - - 0 1')
        pawn = board._get_piece(9)
        board.make_move((9, 17, None))
        self.assertIs(pawn, board._get_piece(17))

    def test_can_make_pawn_moves_as_black(self):
        board = Board('8/p7/8/8/8/8/8/k6K b - - 0 1')
        pawn = board._get_piece(48)
        board.make_move((48, 40, None))
        self.assertIs(pawn, board._get_piece(40))

    def test_can_make_any_pawn_moves_as_black(self):
        board = Board('8/1p6/8/8/8/8/8/k6K b - - 0 1')
        pawn = board._get_piece(49)
        board.make_move((49, 41, None))
        self.assertIs(pawn, board._get_piece(41))

    def test_can_make_knight_moves(self):
        board = Board('K7/8/k7/8/8/8/8/N7 w - - 0 1')
        knight = board._get_piece(0)
        board.make_move((0, 17, None))
        self.assertIs(knight, board._get_piece(17))

    def test_can_make_any_knight_moves(self):
        board = Board('K7/8/k7/8/8/8/8/N7 w - - 0 1')
        knight = board._get_piece(0)
        board.make_move((0, 10, None))
        self.assertIs(knight, board._get_piece(10))

    def test_can_make_bishop_moves(self):
        board = Board('K7/8/k7/8/8/8/1B6/8 w - - 0 1')
        bishop = board._get_piece(9)
        board.make_move((9, 0, None))
        self.assertIs(bishop, board._get_piece(0))

    def test_can_make_any_bishop_moves(self):
        board = Board('K7/8/8/8/8/8/1B6/7k w - - 0 1')
        bishop = board._get_piece(9)
        board.make_move((9, 18, None))
        self.assertIs(bishop, board._get_piece(18))

    def test_can_make_rook_moves(self):
        board = Board('K7/8/8/8/8/8/1R6/k7 w - - 0 1')
        rook = board._get_piece(9)
        board.make_move((9, 8, None))
        self.assertIs(rook, board._get_piece(8))

    def test_can_make_any_rook_moves(self):
        board = Board('K7/8/8/8/8/8/1R6/k7 w - - 0 1')
        rook = board._get_piece(9)
        board.make_move((9, 10, None))
        self.assertIs(rook, board._get_piece(10))

    def test_can_make_queen_moves(self):
        board = Board('K7/8/8/8/k7/8/1Q6/8 w - - 0 1')
        queen = board._get_piece(9)
        board.make_move((9, 10, None))
        self.assertIs(queen, board._get_piece(10))

    def test_can_make_any_queen_moves(self):
        board = Board('K7/8/8/8/k7/8/1Q6/8 w - - 0 1')
        queen = board._get_piece(9)
        board.make_move((9, 8, None))
        self.assertIs(queen, board._get_piece(8))

    # capturing
    def test_captured_piece_is_not_in_active_pieces_set(self):
        board = Board('r7/8/8/8/8/7k/7K/R7 w - - 0 1')
        b_rook = board._get_piece(56)
        board.make_move((0, 56, None))
        self.assertNotIn(b_rook, board._get_active_pieces())

    def test_captured_piece_is_in_pieces_set(self):
        board = Board('r7/8/8/8/8/7k/7K/R7 w - - 0 1')
        b_rook = board._get_piece(56)
        board.make_move((0, 56, None))
        self.assertIn(b_rook, board._pieces)

    def test_capture_turn_correct_after_white_captures(self):
        board = Board('r7/8/8/8/8/7k/7K/R7 w - - 0 1')
        turn = board.turn_number
        b_rook = board._get_piece(56)
        board.make_move((0, 56, None))
        self.assertEqual(turn, b_rook._capture_data[0])

    def test_capture_turn_correct_after_black_captures(self):
        board = Board('r7/8/8/8/8/8/5K1k/R7 b - - 0 1')
        turn = board.turn_number
        w_rook = board._get_piece(0)
        board.make_move((56, 0, None))
        self.assertEqual(turn, w_rook._capture_data[0])

    def test_capture_color_correct_after_white_captures(self):
        board = Board('r7/8/8/8/7k/8/7K/R7 w - - 0 1')
        color = board._white_to_move
        b_rook = board._get_piece(56)
        board.make_move((0, 56, None))
        self.assertEqual(color, b_rook._capture_data[1])

    def test_capture_color_correct_after_black_captures(self):
        board = Board('r7/8/8/8/8/8/5K1k/R7 b - - 0 1')
        color = board._white_to_move
        w_rook = board._get_piece(0)
        board.make_move((56, 0, None))
        self.assertEqual(color, w_rook._capture_data[1])

    # castling moves
    def test_rook_moved_after_castling_kingside_as_white(self):
        board = Board('k7/8/8/8/8/8/8/4K2R w K - 0 1')
        king = board._get_piece(4)
        rook = board._get_piece(7)
        board.make_move((4, 6, None))
        self.assertIs(king, board._get_piece(6))
        self.assertIs(rook, board._get_piece(5))

    def test_rook_moved_after_castling_queenside_as_white(self):
        board = Board('7k/8/8/8/8/8/8/R3K3 w Q - 0 1')
        king = board._get_piece(4)
        rook = board._get_piece(0)
        board.make_move((4, 2, None))
        self.assertIs(king, board._get_piece(2))
        self.assertIs(rook, board._get_piece(3))

    def test_rook_moved_after_castling_kingside_as_black(self):
        board = Board('4k2r/8/8/8/8/8/8/K7 b k - 0 1')
        king = board._get_piece(60)
        rook = board._get_piece(63)
        board.make_move((60, 62, None))
        self.assertIs(king, board._get_piece(62))
        self.assertIs(rook, board._get_piece(61))

    def test_rook_moved_after_castling_queenside_as_black(self):
        board = Board('r3k3/8/8/8/8/8/8/7K b q - 0 1')
        king = board._get_piece(60)
        rook = board._get_piece(56)
        board.make_move((60, 58, None))
        self.assertIs(king, board._get_piece(58))
        self.assertIs(rook, board._get_piece(59))

    # en passant moves
    def test_removes_pawn_after_capturing_en_passant_right_as_white(self):
        board = Board('k7/8/8/Pp6/8/8/8/K7 w - b6 0 1')
        b_pawn = board._get_piece(33)
        board.make_move((32, 41, None))
        self.assertNotIn(b_pawn, board._get_active_pieces())

    def test_removes_pawn_after_capturing_en_passant_left_as_white(self):
        board = Board('k7/8/8/pP6/8/8/8/K7 w - a6 0 1')
        b_pawn = board._get_piece(32)
        board.make_move((33, 40, None))
        self.assertNotIn(b_pawn, board._get_active_pieces())

    def test_removes_pawn_after_capturing_en_passant_right_as_black(self):
        board = Board('8/8/8/8/8/pP6/8/k6K b - b2 0 1')
        w_pawn = board._get_piece(17)
        board.make_move((16, 9, None))
        self.assertNotIn(w_pawn, board._get_active_pieces())

    def test_removes_pawn_after_capturing_en_passant_left_as_black(self):
        board = Board('k7/8/8/8/8/Pp6/8/7K b - a2 0 1')
        w_pawn = board._get_piece(16)
        board.make_move((17, 8, None))
        self.assertNotIn(w_pawn, board._get_active_pieces())

    # promotion
    def test_pawn_will_be_promoted_to_a_queen_when_moving_to_the_last_row_as_white(self):
        board = Board('7k/P7/8/8/8/8/8/K7 w - - 0 1')
        board.make_move((48, 56, 'Q'))
        piece = board._get_piece(56)
        self.assertEqual(Queen, type(piece))
        self.assertTrue(piece._white_piece)

    def test_pawn_will_be_promoted_to_a_queen_when_moving_to_the_last_row_as_black(self):
        board = Board('k7/8/8/8/8/8/p7/7K b - - 0 1')
        board.make_move((8, 0, 'q'))
        piece = board._get_piece(0)
        self.assertEqual(Queen, type(piece))
        self.assertFalse(piece._white_piece)

    def test_pawn_remains_in_pieces_set(self):
        board = Board('7k/P7/8/8/8/8/8/K7 w - - 0 1')
        pawn = board._get_piece(48)
        board.make_move((48, 56, 'q'))
        self.assertEqual(Queen, type(board._get_piece(56)))
        self.assertIn(pawn, board._pieces)

    def test_pawn_will_be_removed_from_active_piece_set(self):
        board = Board('7k/P7/8/8/8/8/8/K7 w - - 0 1')
        pawn = board._get_piece(48)
        board.make_move((48, 56, 'Q'))
        self.assertEqual(Queen, type(board._get_piece(56)))
        self.assertNotIn(pawn, board._get_active_pieces())

    def test_queen_is_white_after_white_pawns_promotion(self):
        board = Board('7k/P7/8/8/8/8/8/K7 w - - 0 1')
        board.make_move((48, 56, 'Q'))
        piece = board._get_piece(56)
        self.assertEqual(Queen, type(piece))
        self.assertTrue(piece._white_piece)

    def test_queen_is_black_after_black_pawns_promotion(self):
        board = Board('k7/8/8/8/8/8/p7/7K b - - 0 1')
        board.make_move((8, 0, 'q'))
        piece = board._get_piece(0)
        self.assertEqual(Queen, type(piece))
        self.assertFalse(piece._white_piece)

    def test_can_promote_to_rook(self):
        board = Board('7k/P7/8/8/8/8/8/K7 w - - 0 1')
        board.make_move((48, 56, 'R'))
        piece = board._get_piece(56)
        self.assertEqual(Rook, type(piece))
        self.assertTrue(piece._white_piece)

    # board info except pieces
    # color to move
    def test_black_to_move_after_white_move(self):
        board = Board('k7/8/8/8/8/8/K7/8 w - - 0 1')
        board.make_move((8, 16, None))
        self.assertFalse(board.white_to_move)

    def test_white_to_move_after_black_move(self):
        board = Board('8/b7/8/8/8/8/8/k6K b - - 0 1')
        board.make_move((48, 40, None))
        self.assertTrue(board.white_to_move)

    # castling rights
    def test_castling_rights_do_not_change_after_unrelated_move(self):
        board = Board('r3k2r/8/8/8/8/4P3/8/R3K2R w KQkq - 0 1')
        board.make_move((20, 28, None))
        self.assertEqual([True, True, True, True], board.castling_rights)

    # white
    def test_white_looses_all_castling_rights_if_white_king_moves_away(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((4, 12, None))
        self.assertEqual([False, False, True, True], board.castling_rights)

    def test_white_cannot_regain_all_castling_rights_if_white_king_moves_back(self):
        board = Board('r3k2r/8/8/8/8/8/4K3/R6R w kq - 0 1')
        board.make_move((12, 4, None))
        self.assertEqual([False, False, True, True], board.castling_rights)

    def test_white_cannot_regain_all_castling_rights_if_black_king_moves_to_white_kings_starting_position(self):
        board = Board('r6r/8/8/8/4K3/R3P2R/4k3/8 w - - 0 1')
        board.make_move((12, 4, None))
        self.assertEqual([False, False, False, False], board.castling_rights)

    def test_white_looses_kingside_castling_right_if_kingside_rook_is_captured(self):
        board = Board('r3k2r/7r/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((55, 7, None))
        self.assertEqual([False, True, True, True], board.castling_rights)

    def test_white_looses_kingside_castling_right_if_kingside_rook_moves_away(self):
        board = Board('r3k2r/7r/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((7, 15, None))
        self.assertEqual([False, True, True, True], board.castling_rights)

    def test_white_cannot_regain_kingside_castling_right_if_kingside_rook_moves_back(self):
        board = Board('r3k2r/7r/8/8/8/8/7R/R3K3 w Qkq - 0 1')
        board.make_move((15, 7, None))
        self.assertEqual([False, True, True, True], board.castling_rights)

    def test_white_looses_queenside_castling_right_if_queenside_rook_is_captured(self):
        board = Board('r3k2r/r7/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((48, 0, None))
        self.assertEqual([True, False, True, True], board.castling_rights)

    def test_white_looses_queenside_castling_right_if_queenside_rook_moves_away(self):
        board = Board('r3k2r/r7/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((0, 8, None))
        self.assertEqual([True, False, True, True], board.castling_rights)

    def test_white_cannot_regain_queenside_castling_right_if_queenside_rook_moves_back(self):
        board = Board('r3k2r/r7/8/8/8/8/R7/4K2R w Kkq - 0 1')
        board.make_move((8, 0, None))
        self.assertEqual([True, False, True, True], board.castling_rights)

    # black
    def test_black_looses_all_castling_rights_if_black_king_moves_away(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((60, 52, None))
        self.assertEqual([True, True, False, False], board.castling_rights)

    def test_black_cannot_regain_all_castling_rights_if_black_king_moves_back(self):
        board = Board('r6r/4k3/8/8/8/8/8/R3K2R b KQ - 0 1')
        board.make_move((52, 60, None))
        self.assertEqual([True, True, False, False], board.castling_rights)

    def test_black_cannot_regain_all_castling_rights_if_white_king_moves_to_black_kings_starting_position(self):
        board = Board('8/4K3/r6r/4k3/8/8/8/R6R w - - 0 1')
        board.make_move((52, 60, None))
        self.assertEqual([False, False, False, False], board.castling_rights)

    def test_black_looses_kingside_castling_right_if_kingside_rook_is_captured(self):
        board = Board('r3k2r/8/8/8/8/8/7R/R3K2R w KQkq - 0 1')
        board.make_move((15, 63, None))
        self.assertEqual([True, True, False, True], board.castling_rights)

    def test_black_looses_kingside_castling_right_if_kingside_rook_moves_away(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((63, 55, None))
        self.assertEqual([True, True, False, True], board.castling_rights)

    def test_black_cannot_regain_kingside_castling_right_if_kingside_rook_moves_back(self):
        board = Board('r3k3/7r/8/8/8/8/8/R3K2R b KQq - 0 1')
        board.make_move((55, 63, None))
        self.assertEqual([True, True, False, True], board.castling_rights)

    def test_black_looses_queenside_castling_right_if_queenside_rook_is_captured(self):
        board = Board('r3k2r/8/8/8/8/8/R7/R3K2R w KQkq - 0 1')
        board.make_move((8, 56, None))
        self.assertEqual([True, True, True, False], board.castling_rights)

    def test_black_looses_queenside_castling_right_if_queenside_rook_moves_away(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((56, 48, None))
        self.assertEqual([True, True, True, False], board.castling_rights)

    def test_black_cannot_regain_queenside_castling_right_if_queenside_rook_moves_back(self):
        board = Board('4k2r/r7/8/8/8/8/8/R3K2R b KQk - 0 1')
        board.make_move((48, 56, None))
        self.assertEqual([True, True, True, False], board.castling_rights)

    # en passant target square
    def test_ep_target_square_is_none_after_unrelated_move(self):
        board = Board('k7/8/8/8/8/P7/8/K7 w - - 0 1')
        board.make_move((16, 24, None))
        self.assertIsNone(board.ep_target_square)

    def test_ep_target_square_is_none_after_unrelated_move_if_there_is_a_ep_target_square(self):
        board = Board('k7/8/8/p7/8/P7/8/K7 w - a6 0 1')
        board.make_move((16, 24, None))
        self.assertIsNone(board.ep_target_square)

    # white
    def test_sets_ep_target_square_after_double_pawn_push_as_white(self):
        board = Board('K7/8/8/8/8/8/P7/k7 w - - 0 1')
        board.make_move((8, 24, None))
        self.assertEqual(16, board.ep_target_square)

    def test_sets_ep_target_square_after_any_double_pawn_push_as_white(self):
        board = Board('K7/8/8/8/8/8/1P6/k7 w - - 0 1')
        board.make_move((9, 25, None))
        self.assertEqual(17, board.ep_target_square)

    # black
    def test_sets_ep_target_square_after_double_pawn_push_as_black(self):
        board = Board('8/p7/8/8/8/8/8/k6K b - - 0 1')
        board.make_move((48, 32, None))
        self.assertEqual(40, board.ep_target_square)

    def test_sets_ep_target_square_after_any_double_pawn_push_as_black(self):
        board = Board('8/1p6/8/8/8/8/8/k6K b - - 0 1')
        board.make_move((49, 33, None))
        self.assertEqual(41, board.ep_target_square)

    # half move clock
    def test_half_move_clock_increases_after_a_move(self):
        board = Board()
        board.make_move((1, 16, None))
        self.assertEqual(1, board.half_move_clock)

    def test_half_move_clock_resets_after_a_pawn_move(self):
        board = Board('k7/8/8/8/8/8/P7/K7 w - - 10 1')
        board.make_move((8, 16, None))
        self.assertEqual(0, board.half_move_clock)

    def test_half_move_clock_resets_after_capturing_a_piece(self):
        board = Board('7k/8/8/8/8/1p6/Q7/K7 w - - 10 1')
        board.make_move((8, 17, None))
        self.assertEqual(0, board.half_move_clock)

    # turn number
    def test_turn_number_does_not_increase_after_white_move(self):
        board = Board('K7/8/8/8/8/8/P7/k7 w - - 0 1')
        board.make_move((8, 16, None))
        self.assertEqual(1, board.turn_number)

    def test_turn_number_increases_after_black_move(self):
        board = Board('8/p7/8/8/8/8/8/k6K b - - 0 1')
        board.make_move((48, 40, None))
        self.assertEqual(2, board.turn_number)

    def test_adds_old_position_to_position_list(self):
        board = Board()
        board.make_move((8, 16, None))
        self.assertEqual([(True, [True, True, True, True], None, 0, 1)], board._data_log)

    def test_adds_any_old_position_to_position_list(self):
        board = Board('PPPPPPPP/rKqqQRRP/BBKpQnRq/nBbpQQRQ/bbbpbQRN/nppbKKRP/npQrbPKk/NNNkkkkk w - - 0 1')
        board.make_move((0, 17, None))
        self.assertEqual([(True, [False, False, False, False], None, 0, 1)], board._data_log)

    def test_two_positions_in_list_after_two_moves(self):
        board = Board()
        board.make_move((8, 16, None))
        board.make_move((48, 40, None))
        self.assertEqual([(True, [True, True, True, True], None, 0, 1), (False, [True, True, True, True], None, 0, 1)],
                         board._data_log)

    def test_adds_move_to_move_list(self):
        board = Board()
        board.make_move((8, 16, None))
        self.assertEqual([(8, 16, None)], board._moves_log)

    def test_adds_any_move_to_move_list(self):
        board = Board()
        board.make_move((8, 24, None))
        self.assertEqual([(8, 24, None)], board._moves_log)

    def test_adds_two_move_to_move_list(self):
        board = Board()
        board.make_move((8, 16, None))
        board.make_move((48, 40, None))
        self.assertEqual([(8, 16, None), (48, 40, None)], board._moves_log)

    def test_adds_positions_to_positions_log(self):
        board = Board('k7/8/8/8/8/8/P7/K7 w - - 0 1')
        board.make_move((8, 16, None))
        self.assertEqual([{('K', 0), ('P', 8), ('k', 56)}, {('K', 0), ('P', 16), ('k', 56)}], board._positions_log)

    def test_adds_any_positions_to_positions_log(self):
        board = Board('k7/8/8/8/8/8/P7/K7 w - - 0 1')
        board.make_move((0, 1, None))
        self.assertEqual([{('K', 0), ('P', 8), ('k', 56)}, {('K', 1), ('P', 8), ('k', 56)}], board._positions_log)

    def test_adds_multiple_positions_to_positions_log(self):
        board = Board('k7/8/8/8/8/8/P7/K7 w - - 0 1')
        board.make_move((0, 1, None))
        board.make_move((56, 57, None))
        self.assertEqual([{('K', 0), ('P', 8), ('k', 56)}, {('K', 1), ('P', 8), ('k', 56)},
                          {('K', 1), ('P', 8), ('k', 57)}], board._positions_log)

    def test_adds_only_positions_of_active_pieces_to_positions_log(self):
        board = Board('k7/P7/8/8/8/8/8/K7 b - - 0 1')
        board.make_move((56, 48, None))
        self.assertEqual([{('K', 0), ('P', 48), ('k', 56)}, {('K', 0), ('k', 48)}, ], board._positions_log)


class UndoMoveTestCase(unittest.TestCase):
    def test_removes_last_move_from_data_list(self):
        board = Board()
        board.make_move((1, 16, None))
        board._undo_move()
        self.assertEqual([], board._data_log)

    def test_legal_moves_change(self):
        board = Board('k7/8/8/8/8/8/K7/8 w - - 0 1')
        board.make_move((8, 16, None))
        old_moves = board.legal_moves
        board._undo_move()
        self.assertNotEqual(old_moves, board.legal_moves)

    # piece tests
    def test_starting_pos_is_not_empty(self):
        board = Board('k7/8/8/8/8/8/P7/K7 w - - 0 1')
        piece = board._get_piece(8)
        board.make_move((8, 16, None))
        board._undo_move()
        self.assertEqual(Pawn, type(piece))
        self.assertEqual(8, piece._pos)
        self.assertTrue(piece._white_piece)

    def test_not_piece_on_final_square(self):
        board = Board('k7/8/8/8/8/8/P7/K7 w - - 0 1')
        board.make_move((8, 16, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 16)

    def test_can_undo_king_move(self):
        board = Board('k7/8/8/8/8/8/1K6/8 w - - 0 1')
        board.make_move((9, 10, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 10)

    def test_can_undo_any_king_move(self):
        board = Board('k7/8/8/8/8/8/1K6/8 w - - 0 1')
        board.make_move((9, 8, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 8)

    def test_can_undo_white_pawn_move(self):
        board = Board('k7/8/8/8/8/8/P7/7K w - - 0 1')
        board.make_move((8, 16, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 16)

    def test_can_undo_any_white_pawn_move(self):
        board = Board('k7/8/8/8/8/8/1P6/7K w - - 0 1')
        board.make_move((9, 17, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 17)

    def test_can_undo_black_pawn_move(self):
        board = Board('8/p7/8/8/8/8/8/K6k b - - 0 1')
        board.make_move((48, 40, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 40)

    def test_can_undo_any_black_pawn_move(self):
        board = Board('8/1p6/8/8/8/8/8/K6k b - - 0 1')
        board.make_move((49, 41, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 41)

    def test_can_undo_knight_move(self):
        board = Board('7K/k7/8/8/8/8/8/N7 w - - 0 1')
        board.make_move((0, 17, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 17)

    def test_can_undo_any_knight_move(self):
        board = Board('7K/k7/8/8/8/8/8/N7 w - - 0 1')
        board.make_move((0, 10, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 10)

    def test_can_undo_bishop_move(self):
        board = Board('k7/8/8/8/8/8/1B6/7K w - - 0 1')
        board.make_move((9, 0, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 0)

    def test_can_undo_any_bishop_move(self):
        board = Board('k7/8/8/8/8/8/1B6/7K w - - 0 1')
        board.make_move((9, 18, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 18)

    def test_can_undo_rook_move(self):
        board = Board('k7/8/8/8/8/8/1R6/7K w - - 0 1')
        board.make_move((9, 8, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 8)

    def test_can_undo_any_rook_move(self):
        board = Board('k7/8/8/8/8/8/1R6/7K w - - 0 1')
        board.make_move((9, 10, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 10)

    def test_can_undo_queen_move(self):
        board = Board('k7/8/8/8/8/8/1Q6/7K w - - 0 1')
        board.make_move((9, 10, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 10)

    def test_can_undo_any_queen_move(self):
        board = Board('k7/8/8/8/8/8/1Q6/7K w - - 0 1')
        board.make_move((9, 8, None))
        board._undo_move()
        self.assertRaises(ValueError, board._get_piece, 8)

    # capturing
    def test_captured_piece_is_not_captured(self):
        board = Board('r7/8/8/8/7k/8/7K/R7 w - - 0 1')
        b_rook = board._get_piece(56)
        w_rook = board._get_piece(0)
        board.make_move((0, 56, None))
        board._undo_move()
        self.assertIs(b_rook, board._get_piece(56))
        self.assertIs(w_rook, board._get_piece(0))

    # castling moves
    def test_rook_moved_after_undoing_castling_kingside_as_white(self):
        board = Board('k7/8/8/8/8/8/8/4K2R w K - 0 1')
        king = board._get_piece(4)
        rook = board._get_piece(7)
        board.make_move((4, 6, None))
        board._undo_move()
        self.assertIs(king, board._get_piece(4))
        self.assertIs(rook, board._get_piece(7))

    def test_rook_moved_after_undoing_castling_queenside_as_white(self):
        board = Board('7k/8/8/8/8/8/8/R3K3 w Q - 0 1')
        king = board._get_piece(4)
        rook = board._get_piece(0)
        board.make_move((4, 2, None))
        board._undo_move()
        self.assertIs(king, board._get_piece(4))
        self.assertIs(rook, board._get_piece(0))

    def test_rook_moved_after_undoing_castling_kingside_as_black(self):
        board = Board('4k2r/8/8/8/8/8/8/K7 b k - 0 1')
        king = board._get_piece(60)
        rook = board._get_piece(63)
        board.make_move((60, 62, None))
        board._undo_move()
        self.assertIs(king, board._get_piece(60))
        self.assertIs(rook, board._get_piece(63))

    def test_rook_moved_after_castling_queenside_as_black(self):
        board = Board('r3k3/8/8/8/8/8/8/7K b q - 0 1')
        king = board._get_piece(60)
        rook = board._get_piece(56)
        board.make_move((60, 58, None))
        board._undo_move()
        self.assertIs(king, board._get_piece(60))
        self.assertIs(rook, board._get_piece(56))

    # en passant moves
    def test_restores_the_pawn_after_undoing_capturing_en_passant_right_as_white(self):
        board = Board('k7/8/8/Pp6/8/8/8/K7 w - b6 0 1')
        b_pawn = board._get_piece(33)
        board.make_move((32, 41, None))
        board._undo_move()
        self.assertIs(b_pawn, board._get_piece(33))

    def test_restores_the_pawn_after_undoing_capturing_en_passant_left_as_white(self):
        board = Board('k7/8/8/pP6/8/8/8/K7 w - a6 0 1')
        b_pawn = board._get_piece(32)
        board.make_move((33, 40, None))
        board._undo_move()
        self.assertIs(b_pawn, board._get_piece(32))

    def test_removes_pawn_after_capturing_en_passant_right_as_black(self):
        board = Board('8/8/8/8/8/pP6/8/k6K b - b2 0 1')
        w_pawn = board._get_piece(17)
        board.make_move((16, 9, None))
        board._undo_move()
        self.assertIs(w_pawn, board._get_piece(17))

    def test_removes_pawn_after_capturing_en_passant_left_as_black(self):
        board = Board('8/8/8/8/8/Pp6/8/k6K b - a2 0 1')
        w_pawn = board._get_piece(16)
        board.make_move((17, 8, None))
        board._undo_move()
        self.assertIs(w_pawn, board._get_piece(16))

    # promotion
    def test_can_undo_white_promotion(self):
        board = Board('8/P7/k7/8/8/8/8/K7 w - - 0 1')
        w_pawn = board._get_piece(48)
        board.make_move((48, 56, 'Q'))
        self.assertEqual(Queen, type(board._get_piece(56)))
        board._undo_move()
        self.assertIs(w_pawn, board._get_piece(48))

    def test_can_undo_black_promotion(self):
        board = Board('8/8/8/8/8/8/p7/5K1k b - - 0 1')
        b_pawn = board._get_piece(8)
        board.make_move((8, 0, 'q'))
        self.assertEqual(Queen, type(board._get_piece(0)))
        board._undo_move()
        self.assertIs(b_pawn, board._get_piece(8))

    # board info except pieces
    # color to move
    def test_can_recover_white_to_move(self):
        board1.make_move((1, 16, None))
        board1._undo_move()
        self.assertTrue(board1._white_to_move)

    def test_can_recover_black_to_move(self):
        board1.make_move((1, 16, None))
        board1.make_move((57, 48, None))
        board1._undo_move()
        self.assertFalse(board1._white_to_move)
        board1._undo_move()

    # castling rights
    def test_changes_nothing_if_no_rights_were_lost(self):
        board1.make_move((1, 16, None))
        board1._undo_move()
        self.assertEqual([True, True, True, True], board1._castling_rights)

    def test_can_recover_white_queenside_castling_right(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((0, 8, None))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_white_kingside_castling_right(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((7, 15, None))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_both_white_castling_rights(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((4, 12, None))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_black_queenside_castling_right(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((56, 48, None))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_black_kingside_castling_right(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((63, 55, None))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_both_black_castling_rights(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1')
        board.make_move((60, 52, None))
        board._undo_move()
        self.assertEqual([True, True, True, True], board._castling_rights)

    def test_can_recover_incomplete_castling_rights(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w Kq - 0 1')
        board.make_move((7, 15, None))
        board._undo_move()
        self.assertEqual([True, False, False, True], board._castling_rights)

    def test_can_recover_no_castling_rights(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w - - 0 1')
        board.make_move((7, 15, None))
        board._undo_move()
        self.assertEqual([False, False, False, False], board._castling_rights)

    # ep target square
    def test_can_recover_no_ep_target_square(self):
        board0 = Board()
        board0.make_move((1, 16, None))
        board0._undo_move()
        self.assertIsNone(board0._ep_target_square)

    def test_can_recover_ep_target_square(self):
        board = Board('rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR b KQkq a3 0 1')
        board.make_move((57, 48, None))
        board._undo_move()
        self.assertEqual(16, board._ep_target_square)

    def test_can_recover_any_ep_target_square(self):
        board = Board('rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR b KQkq b3 0 1')
        board.make_move((57, 48, None))
        board._undo_move()
        self.assertEqual(17, board._ep_target_square)

    # half move clock
    def test_can_recover_half_move_clock(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 10 1')
        board.make_move((60, 52, None))
        board._undo_move()
        self.assertEqual(10, board._half_move_clock)

    def test_can_recover_any_half_move_clock(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 25 1')
        board.make_move((60, 52, None))
        board._undo_move()
        self.assertEqual(25, board._half_move_clock)

    def test_can_recover_half_move_clock_after_reset(self):
        board = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 10 1')
        board.make_move((8, 16, None))
        board._undo_move()
        self.assertEqual(10, board._half_move_clock)

    def test_can_recover_any_half_move_clock_after_reset(self):
        board = Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 25 1')
        board.make_move((8, 16, None))
        board._undo_move()
        self.assertEqual(25, board._half_move_clock)

    # turn number
    def test_can_recover_turn_number_after_white_move(self):
        board = Board()  # board1
        board.make_move((1, 16, None))
        board._undo_move()
        self.assertEqual(1, board._turn_number)

    def test_can_recover_turn_number_after_black_move(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1')
        board.make_move((60, 52, None))
        board._undo_move()
        self.assertEqual(1, board._turn_number)

    def test_can_recover_any_turn_number_after_black_move(self):
        board = Board('r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 5')
        board.make_move((60, 52, None))
        board._undo_move()
        self.assertEqual(5, board._turn_number)

    def test_removes_last_positions_from_positions_log(self):
        board = Board('k7/8/8/8/8/8/8/K7 w - - 0 1')
        board.make_move((0, 1, None))
        board._undo_move()
        self.assertEqual([{('k', 56), ('K', 0)}], board._positions_log)

    def test_removes_any_last_positions_from_positions_log(self):
        board = Board('k7/8/8/8/8/8/8/K7 w - - 0 1')
        board.make_move((0, 8, None))
        board._undo_move()
        self.assertEqual([{('k', 56), ('K', 0)}], board._positions_log)


class EvaluationTestCase(unittest.TestCase):
    def test_value_is_zero_if_bother_players_have_the_same_pieces_on_equally_good_positions_on_the_board(self):
        board = Board('4k3/8/8/8/8/8/8/4K3 w - - 0 1')
        self.assertEqual(0, board.val)

    def test_only_considers_active_pieces(self):
        board = Board('4k3/8/8/8/8/8/P7/4K3 w - - 0 1')
        board._get_piece(8).capture(1, True)
        board._clear_active_pieces_cache()
        self.assertEqual(0, board.val)

    # if white to move
    def test_value_increases_correctly_if_white_pawn_is_added_with_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/P7/4K3 w - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_correctly_if_white_pawn_is_added_on_any_position_white_to_move(self):
        board = Board('4k3/P7/8/8/8/8/8/4K3 w - - 0 1')
        piece = board._get_piece(48)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_correctly_if_white_knight_is_added_with_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/N7/4K3 w - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_correctly_if_white_bishop_is_added_with_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/B7/4K3 w - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_correctly_if_white_rook_is_added_with_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/R7/4K3 w - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_correctly_if_white_queen_is_added_with_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/Q7/4K3 w - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_if_white_king_is_on_better_position_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/8/1K6 w - - 0 1')
        self.assertEqual(30, board.val)

    def test_value_decreases_if_white_king_is_on_worse_position_white_to_move(self):
        board = Board('4k2K/8/8/8/8/8/8/8 w - - 0 1')
        self.assertEqual(-30, board.val)

    def test_value_decreases_correctly_if_black_pawn_is_added_with_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/p7/4K3 w - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(-piece.pos_val, board.val)

    def test_value_decreases_correctly_if_black_knight_is_added_with_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/n7/4K3 w - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(-piece.pos_val, board.val)

    def test_value_decreases_correctly_if_black_bishop_is_added_with_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/b7/4K3 w - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(-piece.pos_val, board.val)

    def test_value_decreases_correctly_if_black_rook_is_added_with_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/r7/4K3 w - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(-piece.pos_val, board.val)

    def test_value_decreases_correctly_if_black_queen_is_added_with_white_to_move(self):
        board = Board('4k3/8/8/8/8/8/q7/4K3 w - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(-piece.pos_val, board.val)

    def test_value_decreases_if_black_king_is_on_better_position_white_to_move(self):
        board = Board('1k6/8/8/8/8/8/8/4K3 w - - 0 1')
        self.assertEqual(-30, board.val)

    def test_value_increases_if_black_king_is_on_worse_position_white_to_move(self):
        board = Board('8/8/8/8/8/8/8/k2K4 w - - 0 1')
        self.assertEqual(30, board.val)

    # if white to move
    def test_value_increases_correctly_if_black_pawn_is_added_with_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/p7/4K3 b - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_correctly_if_black_knight_is_added_with_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/n7/4K3 b - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_correctly_if_black_bishop_is_added_with_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/b7/4K3 b - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_correctly_if_black_rook_is_added_with_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/r7/4K3 b - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_correctly_if_black_queen_is_added_with_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/q7/4K3 b - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(piece.pos_val, board.val)

    def test_value_increases_if_black_king_is_on_better_position_black_to_move(self):
        board = Board('1k6/8/8/8/8/8/8/4K3 b - - 0 1')
        self.assertEqual(30, board.val)

    def test_value_decreases_if_black_king_is_on_worse_position_black_to_move(self):
        board = Board('8/8/8/8/8/8/8/k2K4 b - - 0 1')
        self.assertEqual(-30, board.val)

    def test_value_decreases_correctly_if_white_pawn_is_added_with_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/P7/4K3 b - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(-piece.pos_val, board.val)

    def test_value_decreases_correctly_if_white_knight_is_added_with_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/N7/4K3 b - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(-piece.pos_val, board.val)

    def test_value_decreases_correctly_if_white_bishop_is_added_with_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/B7/4K3 b - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(-piece.pos_val, board.val)

    def test_value_decreases_correctly_if_white_rook_is_added_with_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/R7/4K3 b - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(-piece.pos_val, board.val)

    def test_value_decreases_correctly_if_white_queen_is_added_with_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/Q7/4K3 b - - 0 1')
        piece = board._get_piece(8)
        self.assertEqual(-piece.pos_val, board.val)

    def test_value_decreases_if_white_king_is_on_better_position_black_to_move(self):
        board = Board('4k3/8/8/8/8/8/8/1K6 b - - 0 1')
        self.assertEqual(-30, board.val)

    def test_value_increases_if_white_king_is_on_worse_position_black_to_move(self):
        board = Board('4k2K/8/8/8/8/8/8/8 b - - 0 1')
        self.assertEqual(30, board.val)


"""
class BoardConversionTestCase(unittest.TestCase):
    # positions
    def test_can_convert_empty_board(self):
        self.assertEqual(set(), board1._pieces_to_board('8/8/8/8/8/8/8/8'))

    def test_can_convert_white_king_on_first_rank(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/K7'))[0]
        self.assertEqual(King, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_white_king_on_second_rank(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/K7/8'))[0]
        self.assertEqual(King, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(8, piece.pos)

    def test_can_convert_white_king_on_any_rank(self):
        piece = list(board1._pieces_to_board('8/8/8/K7/8/8/8/8'))[0]
        self.assertEqual(King, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(32, piece.pos)

    def test_can_convert_white_king_on_second_file(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/1K6'))[0]
        self.assertEqual(King, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(1, piece.pos)

    def test_can_convert_white_king_on_any_file(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/3K4'))[0]
        self.assertEqual(King, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(3, piece.pos)

    def test_can_convert_white_king_on_any_rank_and_any_file(self):
        piece = list(board1._pieces_to_board('8/8/8/8/6K1/8/8/8'))[0]
        self.assertEqual(King, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(30, piece.pos)

    def test_can_convert_white_queen(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/Q7'))[0]
        self.assertEqual(Queen, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_white_rook(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/R7'))[0]
        self.assertEqual(Rook, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_white_bishop(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/B7'))[0]
        self.assertEqual(Bishop, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_white_knight(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/N7'))[0]
        self.assertEqual(Knight, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_white_pawn(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/P7'))[0]
        self.assertEqual(Pawn, type(piece))
        self.assertTrue(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_black_pieces(self):
        piece = list(board1._pieces_to_board('8/8/8/8/8/8/8/k7'))[0]
        self.assertEqual(King, type(piece))
        self.assertFalse(piece.white_piece)
        self.assertEqual(0, piece.pos)

    def test_can_convert_multiple_pieces(self):
        pieces = board1._pieces_to_board('2k5/6r1/8/3B4/8/1Q4n1/8/7P')
        piece_data = [[7, True, Pawn], [17, True, Queen], [22, False, Knight], [35, True, Bishop], [54, False, Rook],
                      [58, False, King]]
        self.assertEqual(len(piece_data), len(pieces))
        for piece in pieces:
            if [piece.pos, piece.white_piece, type(piece)] in piece_data:
                piece_data.remove([piece.pos, piece.white_piece, type(piece)])
        self.assertEqual([], piece_data)

    def test_can_convert_complex_positions(self):
        pieces = board1._pieces_to_board('3r2k1/pp3rpp/2pR4/3bP3/1Bp1pPq1/4P3/PP5P/2K3R1')
        piece_data = [[2, True, King], [6, True, Rook], [8, True, Pawn], [9, True, Pawn], [15, True, Pawn],
                      [20, True, Pawn], [25, True, Bishop], [26, False, Pawn], [28, False, Pawn], [29, True, Pawn],
                      [30, False, Queen], [35, False, Bishop], [36, True, Pawn], [42, False, Pawn], [43, True, Rook],
                      [48, False, Pawn], [49, False, Pawn], [53, False, Rook], [54, False, Pawn], [55, False, Pawn],
                      [59, False, Rook], [62, False, King]]
        self.assertEqual(len(piece_data), len(pieces))
        for piece in pieces:
            if [piece.pos, piece.white_piece, type(piece)] in piece_data:
                piece_data.remove([piece.pos, piece.white_piece, type(piece)])
        self.assertEqual([], piece_data)

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
    def test_uses_active_pieces_set(self):
        board = Board('8/8/8/8/8/8/8/KP6 w - - 0 1')
        board._get_piece(1).capture(1, True)
        board._clear_active_pieces_cache()
        self.assertEqual('8/8/8/8/8/8/8/K7 w - - 0 1', board._board_to_fen())

    # positions
    def test_can_convert_empty_board(self):
        self.assertEqual('8/8/8/8/8/8/8/8', board1._pieces_to_fen(set()))

    def test_can_convert_white_king_on_first_rank(self):
        pieces = {board1._create_piece(0, 'K')}
        self.assertEqual('8/8/8/8/8/8/8/K7', board1._pieces_to_fen(pieces))

    def test_can_convert_white_king_on_second_rank(self):
        pieces = {board1._create_piece(8, 'K')}
        self.assertEqual('8/8/8/8/8/8/K7/8', board1._pieces_to_fen(pieces))

    def test_can_convert_white_king_on_any_rank(self):
        pieces = {board1._create_piece(32, 'K')}
        self.assertEqual('8/8/8/K7/8/8/8/8', board1._pieces_to_fen(pieces))

    def test_can_convert_white_king_on_second_file(self):
        pieces = {board1._create_piece(1, 'K')}
        self.assertEqual('8/8/8/8/8/8/8/1K6', board1._pieces_to_fen(pieces))

    def test_can_convert_white_king_on_any_file(self):
        pieces = {board1._create_piece(3, 'K')}
        self.assertEqual('8/8/8/8/8/8/8/3K4', board1._pieces_to_fen(pieces))

    def test_can_convert_white_king_on_any_rank_and_any_file(self):
        pieces = {board1._create_piece(30, 'K')}
        self.assertEqual('8/8/8/8/6K1/8/8/8', board1._pieces_to_fen(pieces))

    def test_can_convert_white_queen(self):
        pieces = {board1._create_piece(0, 'Q')}
        self.assertEqual('8/8/8/8/8/8/8/Q7', board1._pieces_to_fen(pieces))

    def test_can_convert_white_rook(self):
        pieces = {board1._create_piece(0, 'R')}
        self.assertEqual('8/8/8/8/8/8/8/R7', board1._pieces_to_fen(pieces))

    def test_can_convert_white_bishop(self):
        pieces = {board1._create_piece(0, 'B')}
        self.assertEqual('8/8/8/8/8/8/8/B7', board1._pieces_to_fen(pieces))

    def test_can_convert_white_knight(self):
        pieces = {board1._create_piece(0, 'N')}
        self.assertEqual('8/8/8/8/8/8/8/N7', board1._pieces_to_fen(pieces))

    def test_can_convert_white_pawn(self):
        pieces = {board1._create_piece(0, 'P')}
        self.assertEqual('8/8/8/8/8/8/8/P7', board1._pieces_to_fen(pieces))

    def test_can_convert_black_pieces(self):
        pieces = {board1._create_piece(0, 'k')}
        self.assertEqual('8/8/8/8/8/8/8/k7', board1._pieces_to_fen(pieces))

    def test_can_convert_multiple_pieces(self):
        piece_data = [[7, 'P'], [17, 'Q'], [22, 'n'], [35, 'B'], [54, 'r'], [58, 'k']]
        pieces = {board1._create_piece(p, t) for p, t in piece_data}
        self.assertEqual('2k5/6r1/8/3B4/8/1Q4n1/8/7P', board1._pieces_to_fen(pieces))

    def test_can_convert_complex_positions(self):
        piece_data = [[2, 'K'], [6, 'R'], [8, 'P'], [9, 'P'], [15, 'P'], [20, 'P'], [25, 'B'], [26, 'p'], [28, 'p'],
                      [29, 'P'], [30, 'q'], [35, 'b'], [36, 'P'], [42, 'p'], [43, 'R'], [48, 'p'], [49, 'p'], [53, 'r'],
                      [54, 'p'], [55, 'p'], [59, 'r'], [62, 'k']]
        pieces = {board1._create_piece(p, t) for p, t in piece_data}
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
"""

if __name__ == '__main__':
    unittest.main()
