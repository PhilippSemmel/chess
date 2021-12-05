import unittest
from player import Player

w_player = Player(True, 'Hans-Wurst')
b_player = Player(False, 'Darth Vader')


class ConstructionTestCase(unittest.TestCase):
    def test_white_is_given_value(self):
        self.assertTrue(w_player._white)

    def test_white_is_any_given_value(self):
        self.assertFalse(b_player._white)

    def test_name_is_given_value(self):
        self.assertEqual('Hans-Wurst', w_player._name)

    def test_name_is_any_given_value(self):
        self.assertEqual('Darth Vader', b_player._name)


class AttributeGetterTestCase(unittest.TestCase):
    def test_can_get_color(self):
        self.assertTrue(w_player.white)

    def test_can_get_any_color(self):
        self.assertFalse(b_player.white)

    def test_can_get_name(self):
        self.assertEqual('Hans-Wurst', w_player.name)

    def test_can_get_any_name(self):
        self.assertEqual('Darth Vader', b_player.name)


class MoveSelectionTestCase(unittest.TestCase):
    def test_converts_move_to_ints(self):
        self.assertEqual((0, 1), w_player._move_to_ints('a1-b1'))

    def test_converts_any_move_to_ints(self):
        self.assertEqual((36, 7), w_player._move_to_ints('e5-h1'))
