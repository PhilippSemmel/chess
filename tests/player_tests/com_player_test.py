import unittest

from chess import Board
from player import ComPlayer

w_player = ComPlayer(True)
b_player = ComPlayer(False)


class ConstructionTestCase(unittest.TestCase):
    def test_white_is_given_value(self):
        self.assertTrue(w_player._white)

    def test_white_is_any_given_value(self):
        self.assertFalse(b_player._white)

    def test_name_of_white_is_standard_name(self):
        self.assertEqual('White Com', w_player._name)

    def test_name_of_black_is_standard_name(self):
        self.assertEqual('Black Com', b_player._name)


class RandomMoveSelectionTestCase(unittest.TestCase):
    def test_can_select_random_move_from_move_set(self):
        board = Board('K7/8/8/8/8/8/1Q6/7k w - - 0 1')
        for i in range(1000):
            self.assertTrue(w_player._get_random_move(board) in board.legal_moves)

    def test_can_select_random_move_from_any_move_set(self):
        board = Board('k7/8/8/8/8/8/1q6/7K b - - 0 1')
        for i in range(1000):
            self.assertTrue(w_player._get_random_move(board) in board.legal_moves)


def main() -> None:
    unittest.main()


if __name__ == '__main__':
    main()
