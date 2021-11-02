import unittest
from board import Board


class TestBoardConstruction(unittest.TestCase):
    board = Board()

    def test_color_to_move_is_white_after_construction(self):
        self.assertTrue(self.board._white_to_move)

    def test_turn_number_is_one_after_construction(self):
        self.assertEqual(self.board._turn_number, 1)

    def test_all_castling_rights_available_after_construction(self):
        self.assertEqual(self.board._castling_rights, 15)

    def test_ep_target_square_is_none_after_construction(self):
        self.assertIsNone(self.board._ep_target_square)

    def test_half_move_clock_is_zero(self):
        self.assertEqual(self.board._half_move_clock, 0)

    def test_moves_list_is_empty(self):
        self.assertEqual(self.board._moves, [])


if __name__ == '__main__':
    unittest.main()
