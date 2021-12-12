import unittest
from player import HumanPlayer

w_player = HumanPlayer(True, 'Hans-Wurst')
b_player = HumanPlayer(False, 'Darth Vader')


class ConstructionTestCase(unittest.TestCase):
    def test_white_is_given_value(self):
        self.assertTrue(w_player._white)

    def test_white_is_any_given_value(self):
        self.assertFalse(b_player._white)

    def test_name_is_given_value(self):
        self.assertEqual('Hans-Wurst', w_player._name)

    def test_name_is_any_given_value(self):
        self.assertEqual('Darth Vader', b_player._name)


class InputVerificationTestCase(unittest.TestCase):
    def test_input_longer_than_four_characters_is_not_correct(self):
        self.assertRaises(ValueError, w_player._verify_input, 'e2e4 ')

    def test_input_shorter_than_four_characters_is_not_correct(self):
        self.assertRaises(ValueError, w_player._verify_input, 'e2e')

    def test_input_correct_if_four_characters_long(self):
        self.assertIsNone(w_player._verify_input('e2e4'))

    def test_inputs_first_character_is_not_one_of_the_first_eight_letters_in_the_alphabet(self):
        self.assertRaises(ValueError, w_player._verify_input, 'i2e4')

    def test_inputs_first_character_is_one_of_the_first_eight_letters_in_the_alphabet(self):
        self.assertIsNone(w_player._verify_input('e2e4'))

    def test_inputs_second_character_is_not_one_of_the_first_eight_digits(self):
        self.assertRaises(ValueError, w_player._verify_input, 'e9e4')

    def test_inputs_second_character_is_one_of_the_first_eight_letters_digits(self):
        self.assertIsNone(w_player._verify_input('e2e4'))

    def test_inputs_third_character_is_not_one_of_the_first_eight_letters_in_the_alphabet(self):
        self.assertRaises(ValueError, w_player._verify_input, 'e2i4')

    def test_inputs_third_character_is_one_of_the_first_eight_letters_in_the_alphabet(self):
        self.assertIsNone(w_player._verify_input('e2e4'))

    def test_inputs_forth_character_is_not_one_of_the_first_eight_digits(self):
        self.assertRaises(ValueError, w_player._verify_input, 'e2e9')

    def test_inputs_forth_character_is_one_of_the_first_eight_letters_digits(self):
        self.assertIsNone(w_player._verify_input('e2e4'))


class MoveVerificationTestCase(unittest.TestCase):
    moves = {(0, 1)}

    def test_move_correct_if_in_legal_moves(self):
        self.assertIsNone(w_player._verify_move((0, 1), self.moves))

    def test_raises_value_error_if_move_not_in_legal_moves(self):
        self.assertRaises(ValueError, w_player._verify_move, (63, 62), self.moves)

    def test_raises_value_error_if_any_move_not_in_legal_moves(self):
        self.assertRaises(ValueError, w_player._verify_move, (63, 61), self.moves)

    def test_raises_value_if_move_not_in_any_moves_set(self):
        self.assertRaises(ValueError, w_player._verify_move, (0, 1), {})
