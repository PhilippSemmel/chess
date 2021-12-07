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
    def test_input_longer_than_four_characters_is_not_correct(self):
        self.assertFalse(w_player._input_correct('e2e4 '))

    def test_input_shorter_than_four_characters_is_not_correct(self):
        self.assertFalse(w_player._input_correct('e2e'))

    def test_input_correct_if_four_characters_long(self):
        self.assertTrue(w_player._input_correct('e2e4'))

    def test_inputs_first_character_is_not_one_of_the_first_eight_letters_in_the_alphabet(self):
        self.assertFalse(w_player._input_correct('i2e4'))

    def test_inputs_first_character_is_one_of_the_first_eight_letters_in_the_alphabet(self):
        self.assertTrue(w_player._input_correct('e2e4'))

    def test_inputs_second_character_is_not_one_of_the_first_eight_digits(self):
        self.assertFalse(w_player._input_correct('e9e4'))

    def test_inputs_second_character_is_one_of_the_first_eight_letters_digits(self):
        self.assertTrue(w_player._input_correct('e2e4'))

    def test_inputs_third_character_is_not_one_of_the_first_eight_letters_in_the_alphabet(self):
        self.assertFalse(w_player._input_correct('e2i4'))

    def test_inputs_third_character_is_one_of_the_first_eight_letters_in_the_alphabet(self):
        self.assertTrue(w_player._input_correct('e2e4'))

    def test_inputs_forth_character_is_not_one_of_the_first_eight_digits(self):
        self.assertFalse(w_player._input_correct('e2e9'))

    def test_inputs_forth_character_is_one_of_the_first_eight_letters_digits(self):
        self.assertTrue(w_player._input_correct('e2e4'))

    def test_converts_move_to_ints(self):
        self.assertEqual((0, 1), w_player._move_to_ints('a1b1'))

    def test_converts_any_move_to_ints(self):
        self.assertEqual((36, 7), w_player._move_to_ints('e5h1'))

    def test_converts_ints_to_move(self):
        self.assertEqual('a1b1', w_player._move_to_str((0, 1)))

    def test_converts_any_ints_to_move(self):
        self.assertEqual('e5h1', w_player._move_to_str((36, 7)))
