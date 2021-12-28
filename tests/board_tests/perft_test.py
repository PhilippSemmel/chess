"""
a set of tests that test the move generation thoroughly
"""
import unittest
from typing import List

from board import Board


# if board.checkmate or board.stalemate return 0 or len(board.legal_moves)
def perft_legal_moves(board: Board, depth: int) -> int:
    if depth == 1:
        return len(board.legal_moves)
    nodes: int = 0
    for move in board.legal_moves:
        with board.make_move_and_undo_move_afterwards(move):
            nodes += perft_legal_moves(board, depth - 1)
    return nodes


class LegalMovesPerftAlgorithmTestCase(unittest.TestCase):
    def test_at_depth_one_returns_the_number_of_legal_moves(self):
        self.assertEqual(20, perft_legal_moves(Board(), 1))

    def test_at_depth_one_returns_the_number_of_legal_moves_with_every_board(self):
        board = Board('kq6/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertEqual(1, perft_legal_moves(board, 1))

    def test_at_depth_two_returns_number_of_legal_positions_after_two_moves(self):
        board = Board('kp6/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertEqual(9, perft_legal_moves(board, 2))

    def test_at_depth_three_returns_number_of_legal_positions_after_three_moves(self):
        board = Board('kp6/8/8/8/8/8/8/K7 w - - 0 1')
        self.assertEqual(54, perft_legal_moves(board, 3))

    def test_considers_different_promotion_options_as_individual_move(self):
        board = Board('7k/P7/8/8/8/2b5/1r6/K7 w - - 0 1')
        self.assertEqual(4, perft_legal_moves(board, 1))


class PerftPositionsTestCase(unittest.TestCase):
    def test_starting_position(self):
        search_depth: int = 3  # min: 1; max: 15
        results: List[int] = [20, 400, 8_902, 197_281, 4_865_609, 119_060_324, 3_195_901_860, 84_998_978_956,
                              2_439_530_234_167, 69_352_859_712_417, 2_097_651_003_696_806, 62_854_969_236_701_747,
                              1_981_066_775_000_396_239, 61_885_021_521_585_529_237, 2_015_099_950_053_364_471_960]
        self.assertEqual(results[search_depth - 1], perft_legal_moves(Board(), search_depth))

    def test_position_2(self):
        search_depth: int = 2  # min: 1; max: 6
        results: List[int] = [48, 2_039, 97_862, 4_085_603, 193_690_690, 8_031_647_685]
        board = Board('r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1')
        self.assertEqual(results[search_depth - 1], perft_legal_moves(board, search_depth))

    def test_position_3(self):
        search_depth: int = 3  # min: 1; max: 8
        results: List[int] = [14, 191, 2_812, 43_238, 674_624, 11_030_083, 178_633_661, 3_009_794_393]
        board = Board('8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1')
        self.assertEqual(results[search_depth - 1], perft_legal_moves(board, search_depth))

    def test_position_4(self):
        search_depth: int = 3  # min: 1; max: 6
        results: List[int] = [6, 264, 9_467, 422_333, 15_833_292, 706_045_033]
        board = Board('r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1')
        self.assertEqual(results[search_depth - 1], perft_legal_moves(board, search_depth))

    def test_position_4_5(self):
        search_depth: int = 3  # min: 1; max: 6
        results: List[int] = [6, 264, 9_467, 422_333, 15_833_292, 706_045_033]
        board = Board('r2q1rk1/pP1p2pp/Q4n2/bbp1p3/Np6/1B3NBn/pPPP1PPP/R3K2R b KQ - 0 1')
        self.assertEqual(results[search_depth - 1], perft_legal_moves(board, search_depth))

    def test_position_5(self):
        search_depth: int = 2  # min: 1; max: 5
        results: List[int] = [44, 1_486,  62_379, 2_103_487, 89_941_194]
        board = Board('rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8')
        self.assertEqual(results[search_depth - 1], perft_legal_moves(board, search_depth))

    def test_position_6(self):
        search_depth: int = 2  # min: 1; max: 9
        results: List[int] = [46, 2_079,  89_890, 3_894_594, 164_075_551, 6_923_051_137, 287_188_994_746,
                              11_923_589_843_526, 490_154_852_788_714]
        board = Board('r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10')
        self.assertEqual(results[search_depth - 1], perft_legal_moves(board, search_depth))


if __name__ == '__main__':
    unittest.main()
