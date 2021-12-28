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
        self.assertEqual('a1b1', w_player._move_to_str((0, 1, None)))

    def test_converts_any_ints_to_move(self):
        self.assertEqual('e5h1', w_player._move_to_str((36, 7, None)))

    def test_converts_promotion_moves(self):
        self.assertEqual('a7a8Q', w_player._move_to_str((48, 56, 'Q')))

    def test_converts_any_promotion_move(self):
        self.assertEqual('h7h8R', w_player._move_to_str((55, 63, 'R')))

    def test_converts_black_promotion_moves_as_well(self):
        self.assertEqual('a2a1q', w_player._move_to_str((8, 0, 'q')))

    def test_converts_str_move_to_ints(self):
        self.assertEqual((0, 9, None), w_player._move_to_ints('a1b2'))

    def test_converts_any_str_move_to_ints(self):
        self.assertEqual((63, 34, None), w_player._move_to_ints('h8c5'))

    def test_converts_str_promotion_move_to_move(self):
        self.assertEqual((48, 56, 'Q'), w_player._move_to_ints('a7a8Q'))

    def test_converts_any_str_promotion_move_to_move(self):
        self.assertEqual((55, 63, 'R'), w_player._move_to_ints('h7h8R'))

    def test_converts_black_str_promotion_move_to_move(self):
        self.assertEqual((0, 8, 'q'), w_player._move_to_ints('a1a2q'))


def main() -> None:
    unittest.main()


if __name__ == '__main__':
    main()
