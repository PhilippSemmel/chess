import unittest
from player import ComPlayer


w_player = ComPlayer(True, 'Hans-Wurst')
b_player = ComPlayer(False, 'Darth Vader')


class ConstructionTestCase(unittest.TestCase):
    def test_white_is_given_value(self):
        self.assertTrue(w_player._white)

    def test_white_is_any_given_value(self):
        self.assertFalse(b_player._white)

    def test_name_is_given_value(self):
        self.assertEqual('Hans-Wurst', w_player._name)

    def test_name_is_any_given_value(self):
        self.assertEqual('Darth Vader', b_player._name)


class RandomMoveSelectionTestCase(unittest.TestCase):
    def test_can_select_random_move_from_move_set(self):
        moves = set(zip(list(range(64)), list(range(63, -1, -1))))
        for i in range(1000):
            self.assertTrue(w_player._get_random_move(moves) in moves)

    def test_can_select_random_move_from_any_move_set(self):
        moves = set(zip(list(range(63, -1, -1)), list(range(64))))
        for i in range(1000):
            self.assertTrue(w_player._get_random_move(moves) in moves)
