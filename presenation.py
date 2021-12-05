import unittest
from board import Board


class Presentation(unittest.TestCase):
    def test_move_generation_rook(self):
        board = Board('8/1p6/8/5P2/1p2R2P/4P3/8/1P6 w - - 0 1')
        rook = board._get_piece(28)
        print(board)
        self.assertEqual({(28, 29), (28, 30), (28, 36), (28, 44), (28, 52), (28, 60), (28, 27), (28, 26), (28, 25)},
                         rook.pseudo_legal_moves)

    # def test_capturing_a_piece(self):
    #

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