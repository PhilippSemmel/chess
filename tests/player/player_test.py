import unittest
from player import Player


class TestPlayer(Player):
    def __init__(self, *args):
        super().__init__(*args)
    
    def get_move(self, *args):
        pass


w_player = TestPlayer(True, 'Hans-Wurst')
b_player = TestPlayer(False, 'Darth Vader')


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


class UIConversionTestCase(unittest.TestCase):
    def test_converts_ints_to_move(self):
        self.assertEqual('a1b1', w_player._move_to_str((0, 1)))

    def test_converts_any_ints_to_move(self):
        self.assertEqual('e5h1', w_player._move_to_str((36, 7)))

    def test_converts_str_move_to_ints(self):
        self.assertEqual((0, 9), w_player._move_to_ints('a1b2'))

    def test_converts_any_str_move_to_ints(self):
        self.assertEqual((63, 34), w_player._move_to_ints('h8c5'))
