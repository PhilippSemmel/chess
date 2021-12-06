import unittest
from board import Board


class Presentation(unittest.TestCase):
    def test_move_generation_rook(self):
        board = Board('8/1p6/8/5P2/1p2R2P/4P3/8/1P6 w - - 0 1')
        rook = board._get_piece(28)
        print(board)
        self.assertEqual({(28, 29), (28, 30), (28, 36), (28, 44), (28, 52), (28, 60), (28, 27), (28, 26), (28, 25)},
                         rook.pseudo_legal_moves)

    def test_mate_in_one(self):
        board = Board('8/8/8/8/q7/8/k7/n1K5 b - - 0 1')
        print(board)
        board.make_move((24, 10))
        print(board)
        print('Legal moves:', board.legal_moves)
        print('Checkmate:', board.checkmate)

    def test_stalemate_in_one(self):
        board = Board('8/8/8/8/q7/8/k7/n1K5 b - - 0 1')
        print(board)
        board.make_move((24, 27))
        print(board)
        print('Legal moves:', board.legal_moves)
        print('Stalemate:', board.stalemate)

    def test_castling(self):
        board = Board('4k3/8/8/8/8/8/r7/R3K2R w - - 0 1')
        print(board)
        print('Legal moves:', board.legal_moves)
        board.make_move((4, 6))
        print(board)

    def test_no_castling(self):
        board = Board('4kr2/8/8/8/8/8/r7/R3K2R w - - 0 1')
        print(board)
        print('Legal moves:', board.legal_moves)

    def test_capturing_a_piece(self):
        board = Board('3k4/8/6n1/4P3/8/8/8/3K4 b - - 0 1')
        print(board)
        board.make_move((46, 36))
        input()


"""
capturing
- object changes
- not in active pieces anymore
"""

"""
checkmate (mate in one)
- pseudo_legal_moves
- legal_moves
"""