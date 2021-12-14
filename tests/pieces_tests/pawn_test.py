import unittest
from src.board import Pawn, Piece, Board


board = Board()
pawn1 = Pawn(35, True, board)
pawn2 = Pawn(21, False, board)


class ConstructionTestCase(unittest.TestCase):
    def test_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Pawn, Piece))

    def test_base_val_is_correct(self):
        self.assertEqual(100, pawn1._base_val)

    def test_base_val_is_always_correct(self):
        self.assertEqual(100, pawn2._base_val)

    def test_pos_val_mod_is_correct_as_white(self):
        self.assertEqual((0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 10, -20, -20, 10, 10, 5, 5, -5, -10, 0, 0, -10, -5, 5, 0, 0, 0,
                          20, 20, 0,  0, 0, 5, 5, 10, 25, 25, 10, 5, 5, 10, 10, 20, 30, 30, 20, 10, 10, 50, 50, 50, 50,
                          50, 50, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0), pawn2._pos_val_mod[True])

    def test_pos_val_mod_is_correct_as_black(self):
        self.assertEqual((0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 10, 10, 20, 30, 30, 20, 10, 10, 5, 5,
                          10, 25, 25, 10, 5, 5, 0, 0, 0, 20, 20, 0, 0, 0, 5, -5, -10, 0, 0, -10, -5, 5, 5, 10, 10, -20,
                          -20, 10, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0), pawn1._pos_val_mod[False])

    def test_pos_is_given_value(self):
        self.assertEqual(35, pawn1._pos)

    def test_pos_is_any_given_value(self):
        self.assertEqual(21, pawn2._pos)

    def test_color_is_given_value(self):
        self.assertTrue(pawn1._white_piece)

    def test_color_is_any_given_value(self):
        self.assertFalse(pawn2._white_piece)

    def test_capture_data_is_none(self):
        self.assertIsNone(pawn1._capture_data)

    def test_capture_data_is_always_none(self):
        self.assertIsNone(pawn2._capture_data)

    def test_promotion_data_is_none(self):
        self.assertIsNone(pawn1._promotion_data)

    def test_promotion_data_is_always_none(self):
        self.assertIsNone(pawn2._promotion_data)


class GetterTestCase(unittest.TestCase):
    def test_on_board_if_not_captured_nor_promoted(self):
        pawn = Pawn(0, True, board)
        self.assertTrue(pawn.on_board)

    def test_not_on_board_if_captured(self):
        pawn = Pawn(0, True, board)
        pawn.capture(3, True)
        self.assertFalse(pawn.on_board)

    def test_not_on_board_if_promoted(self):
        pawn = Pawn(0, True, board)
        pawn.promote(3, True)
        self.assertFalse(pawn.on_board)

    def test_not_on_board_if_captured_and_promoted(self):
        pawn = Pawn(0, True, board)
        pawn.capture(3, True)
        pawn.promote(3, True)
        self.assertFalse(pawn.on_board)

    def test_can_get_capture_data(self):
        self.assertIsNone(pawn1.promotion_data)

    def test_can_get_any_capture_data(self):
        pawn = Pawn(35, True, Board())
        pawn.promote(1, True)
        self.assertEqual((1, True), pawn.promotion_data)


class SetterTestCase(unittest.TestCase):
    def test_can_be_promoted(self):
        pawn1.promote(3, False)
        self.assertEqual((3, False), pawn1._promotion_data)

    def test_any_pawn_can_be_promoted(self):
        pawn2.promote(4, True)
        self.assertEqual((4, True), pawn2._promotion_data)

    def test_can_reset_promotion_data(self):
        pawn1.promote(3, False)
        pawn1.unpromote()
        self.assertIsNone(pawn1._promotion_data)


class MoveGenerationTestCase(unittest.TestCase):
    # white
    def test_cannot_move_when_blocked_by_own_pieces_as_white(self):
        pawn = Board('K7/8/8/8/8/1PPP4/2P5/8 w - - 0 1')._get_piece(10)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_move_in_multiple_directions_as_white(self):
        pawn = Board('K7/8/8/8/2p5/3P4/8/8 w - - 0 1')._get_piece(19)
        self.assertEqual({(19, 27), (19, 26)}, pawn.pseudo_legal_moves)

    def test_attacking_squares_equal_diagonal_capture_move_target_squares_as_white(self):
        pawn = Board('K7/8/8/8/2p5/3P4/8/8 w - - 0 1')._get_piece(19)
        self.assertEqual({26}, pawn.attacking_squares)

    # advance
    def test_can_move_one_step_up_as_white(self):
        pawn = Board('K7/8/8/8/2P5/1P1P4/2P5/8 w - - 0 1')._get_piece(10)
        self.assertEqual({(10, 18)}, pawn.pseudo_legal_moves)

    def test_can_move_two_steps_up_on_second_row_as_white(self):
        pawn = Board('K7/8/8/2P5/8/1P1P4/2P5/8 w - - 0 1')._get_piece(10)
        self.assertEqual({(10, 18), (10, 26)}, pawn.pseudo_legal_moves)

    def test_cannot_move_more_than_two_steps_up_on_second_row_as_white(self):
        pawn = Board('K7/8/8/8/8/1P1P4/2P5/8 w - - 0 1')._get_piece(10)
        self.assertEqual({(10, 18), (10, 26)}, pawn.pseudo_legal_moves)

    def test_can_move_one_step_up_anywhere_as_white(self):
        pawn = Board('K7/8/8/1P6/8/8/8/8 w - - 0 1')._get_piece(33)
        self.assertEqual({(33, 41)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_one_step_up_as_white(self):
        pawn = Board('K7/8/8/8/8/1PpP4/2P5/8 w - - 0 1')._get_piece(10)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_up_as_white(self):
        pawn = Board('K7/8/8/8/2p5/1P1P4/2P5/8 w - - 0 1')._get_piece(10)
        self.assertEqual({(10, 18)}, pawn.pseudo_legal_moves)

    def test_cannot_move_two_steps_up_anywhere_not_on_second_row_as_white(self):
        pawn = Board('K7/8/8/1P6/8/8/8/8 w - - 0 1')._get_piece(33)
        self.assertEqual({(33, 41)}, pawn.pseudo_legal_moves)

    def test_cannot_move_up_beyond_the_board_as_white(self):
        pawn = Board('1P6/8/8/8/8/8/8/K7 w - - 0 1')._get_piece(57)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_move_right_up_as_white(self):
        pawn = Board('8/8/8/1P6/8/8/8/K7 w - - 0 1')._get_piece(33)
        self.assertEqual({(33, 41)}, pawn.pseudo_legal_moves)

    def test_cannot_move_left_up_as_white(self):
        pawn = Board('8/8/8/1P6/8/8/8/K7 w - - 0 1')._get_piece(33)
        self.assertEqual({(33, 41)}, pawn.pseudo_legal_moves)

    # capturing sideways
    # right up
    def test_can_capture_one_step_right_up_as_white(self):
        pawn = Board('8/8/8/3Pp3/3P4/8/8/K7 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 36)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_right_up_as_white(self):
        pawn = Board('8/8/5p2/3P4/3P4/8/8/K7 w - - 0 1')._get_piece(27)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_anywhere_one_step_right_up_as_white(self):
        pawn = Board('8/8/8/4Pp2/4P3/8/8/K7 w - - 0 1')._get_piece(28)
        self.assertEqual({(28, 37)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_right_up_beyond_the_edge_of_the_board_as_white(self):
        pawn = Board('8/8/p7/7P/7P/8/8/K7 w - - 0 1')._get_piece(31)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    # left up
    def test_can_capture_one_step_left_up_as_white(self):
        pawn = Board('8/8/8/2pP4/3P4/8/8/K7 w - - 0 1')._get_piece(27)
        self.assertEqual({(27, 34)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_left_up_as_white(self):
        pawn = Board('8/8/1p6/3P4/3P4/8/8/K7 w - - 0 1')._get_piece(27)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_anywhere_one_step_left_up_as_white(self):
        pawn = Board('8/8/8/3pP3/4P3/8/8/K7 w - - 0 1')._get_piece(28)
        self.assertEqual({(28, 35)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_left_up_beyond_the_edge_of_the_board_as_white(self):
        pawn = Board('8/8/8/P7/P6p/8/8/K7 w - - 0 1')._get_piece(24)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    # en passant
    def test_cannot_capture_en_passant_if_not_available_as_white(self):
        pawn = Board('8/8/1P6/1P6/8/8/8/K7 w - - 0 1')._get_piece(33)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_capture_en_passant_if_not_in_range_as_white(self):
        pawn = Board('8/8/P7/P1p5/8/8/8/K7 w - c6 0 1')._get_piece(32)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_en_passant_left_if_available_as_white(self):
        pawn = Board('8/8/1P6/1Pp5/8/8/8/K7 w - c6 0 1')._get_piece(33)
        self.assertEqual({(33, 42)}, pawn.pseudo_legal_moves)

    def test_can_capture_en_passant_left_anywhere_if_available_as_white(self):
        pawn = Board('8/8/2P5/2Pp4/8/8/8/K7 w - d6 0 1')._get_piece(34)
        self.assertEqual({(34, 43)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_en_passant_left_beyond_the_board_as_white(self):
        pawn = Board('8/8/8/p6P/7P/8/8/K7 w - a6 0 1')._get_piece(31)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_en_passant_right_if_available_as_white(self):
        pawn = Board('8/8/1P6/pP6/8/8/8/K7 w - a6 0 1')._get_piece(33)
        self.assertEqual({(33, 40)}, pawn.pseudo_legal_moves)

    def test_can_capture_en_passant_right_anywhere_if_available_as_white(self):
        pawn = Board('8/8/2P5/1pP5/8/8/8/K7 w - b6 0 1')._get_piece(34)
        self.assertEqual({(34, 41)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_en_passant_right_beyond_the_board_as_white(self):
        pawn = Board('P7/P7/7p/8/8/8/8/K7 w - h6 0 1')._get_piece(48)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    # black
    def test_cannot_move_when_blocked_by_own_pieces_as_black(self):
        pawn = Board('8/4p3/3ppp2/8/8/8/8/k7 b - - 0 1')._get_piece(52)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_make_multiple_moves(self):
        pawn = Board('8/8/8/8/2p5/3P4/8/k7 b - - 0 1')._get_piece(26)
        self.assertEqual({(26, 18), (26, 19)}, pawn.pseudo_legal_moves)

    def test_attacking_squares_equal_diagonal_capture_move_target_squares_as_black(self):
        pawn = Board('8/8/8/8/2p5/3P4/8/k7 b - - 0 1')._get_piece(26)
        self.assertEqual({19}, pawn.attacking_squares)

    # advance
    def test_can_move_one_step_down_as_black(self):
        pawn = Board('8/4p3/3p1p2/4p3/8/8/8/k7 b - - 0 1')._get_piece(52)
        self.assertEqual({(52, 44)}, pawn.pseudo_legal_moves)

    def test_can_move_two_steps_down_on_seventh_row_as_black(self):
        pawn = Board('8/4p3/3p1p2/8/4p3/8/8/k7 b - - 0 1')._get_piece(52)
        self.assertEqual({(52, 44), (52, 36)}, pawn.pseudo_legal_moves)

    def test_cannot_move_more_than_two_steps_down_on_seventh_row_as_black(self):
        pawn = Board('8/4p3/3p1p2/8/8/4p3/8/k7 b - - 0 1')._get_piece(52)
        self.assertEqual({(52, 44), (52, 36)}, pawn.pseudo_legal_moves)

    def test_can_move_one_step_down_anywhere_as_black(self):
        pawn = Board('8/8/3p4/2p1p3/8/8/8/k7 b - - 0 1')._get_piece(43)
        self.assertEqual({(43, 35)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_one_step_down_as_black(self):
        pawn = Board('8/4p3/3pPp2/8/8/8/8/k7 b - - 0 1')._get_piece(52)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_down_as_black(self):
        pawn = Board('8/4p3/3p1p2/4P3/8/8/8/k7 b - - 0 1')._get_piece(52)
        self.assertEqual({(52, 44)}, pawn.pseudo_legal_moves)

    def test_cannot_move_two_steps_down_anywhere_not_on_seventh_row_as_black(self):
        pawn = Board('8/8/8/1p6/8/8/8/k7 b - - 0 1')._get_piece(33)
        self.assertEqual({(33, 25)}, pawn.pseudo_legal_moves)

    def test_cannot_move_down_beyond_the_board_as_black(self):
        pawn = Board('k7/8/8/8/8/8/8/1p6 b - - 0 1')._get_piece(1)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_move_right_down_as_black(self):
        pawn = Board('8/4p3/3p1p2/4p3/8/8/8/k7 b - - 0 1')._get_piece(52)
        self.assertEqual({(52, 44)}, pawn.pseudo_legal_moves)

    def test_cannot_move_left_down_as_black(self):
        pawn = Board('8/4p3/3p1p2/4p3/8/8/8/k7 b - - 0 1')._get_piece(52)
        self.assertEqual({(52, 44)}, pawn.pseudo_legal_moves)

    # capturing sideways
    # right down
    def test_can_capture_one_step_right_down_as_black(self):
        pawn = Board('8/8/8/3p4/3pP3/8/8/k7 b - - 0 1')._get_piece(35)
        self.assertEqual({(35, 28)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_right_down_as_black(self):
        pawn = Board('8/8/8/3p4/3p4/5P2/8/k7 b - - 0 1')._get_piece(35)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_anywhere_one_step_right_down_as_black(self):
        pawn = Board('8/8/8/4p3/4pP2/8/8/k7 b - - 0 1')._get_piece(36)
        self.assertEqual({(36, 29)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_right_down_beyond_the_edge_of_the_board_as_black(self):
        pawn = Board('8/8/8/P6p/7p/8/8/k7 b - - 0 1')._get_piece(39)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    # left down
    def test_can_capture_one_step_left_down_as_black(self):
        pawn = Board('8/8/8/4p3/3Pp3/8/8/k7 b - - 0 1')._get_piece(36)
        self.assertEqual({(36, 27)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_two_steps_left_down_as_black(self):
        pawn = Board('8/8/8/4p3/4p3/2P5/8/k7 b - - 0 1')._get_piece(36)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_anywhere_one_step_left_down_as_black(self):
        pawn = Board('8/8/8/3p4/2Pp4/8/8/k7 b - - 0 1')._get_piece(35)
        self.assertEqual({(35, 26)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_left_down_beyond_the_edge_of_the_board_as_black(self):
        pawn = Board('8/8/8/p7/p7/7P/8/k7 b - - 0 1')._get_piece(32)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    # en passant
    def test_cannot_capture_en_passant_if_not_available_as_black(self):
        pawn = Board('8/8/8/8/6p1/6p1/8/k7 b - - 0 1')._get_piece(30)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_cannot_capture_en_passant_if_not_in_range_as_black(self):
        pawn = Board('8/8/P7/P1p5/8/8/8/K7 w - c6 0 1')._get_piece(32)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_en_passant_left_if_available_as_black(self):
        pawn = Board('8/8/8/8/5Pp1/6p1/8/k7 b - f3 0 1')._get_piece(30)
        self.assertEqual({(30, 21)}, pawn.pseudo_legal_moves)

    def test_can_capture_en_passant_left_anywhere_if_available_as_black(self):
        pawn = Board('8/8/8/8/4Pp2/5p2/8/k7 b - e3 0 1')._get_piece(29)
        self.assertEqual({(29, 20)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_en_passant_left_beyond_the_board_as_black(self):
        pawn = Board('8/8/8/p7/p6P/8/8/k7 b - h3 0 1')._get_piece(32)
        self.assertEqual(set(), pawn.pseudo_legal_moves)

    def test_can_capture_en_passant_right_if_available_as_black(self):
        pawn = Board('8/8/8/8/1pP5/1p6/8/k7 b - c3 0 1')._get_piece(25)
        self.assertEqual({(25, 18)}, pawn.pseudo_legal_moves)

    def test_can_capture_en_passant_right_anywhere_if_available_as_black(self):
        pawn = Board('8/8/8/8/2pP4/2p5/8/k7 b - d3 0 1')._get_piece(26)
        self.assertEqual({(26, 19)}, pawn.pseudo_legal_moves)

    def test_cannot_capture_en_passant_right_beyond_the_board_as_black(self):
        pawn = Board('k7/8/8/8/8/P7/7p/7p b - a3 0 1')._get_piece(15)
        self.assertEqual(set(), pawn.pseudo_legal_moves)


class PositionValueTestCase(unittest.TestCase):
    def test_can_generate_pos_value_as_white(self):
        for n, mod in enumerate((0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 10, -20, -20, 10, 10, 5, 5, -5, -10, 0, 0, -10, -5, 5,
                                 0, 0, 0, 20, 20, 0, 0, 0, 5, 5, 10, 25, 25, 10, 5, 5, 10, 10, 20, 30, 30, 20, 10, 10,
                                 50, 50, 50, 50, 50, 50, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0)):
            pawn1.move_to(n)
            self.assertEqual(Pawn._base_val + mod, pawn1.pos_val)

    def test_can_generate_pos_value_as_black(self):
        for n, mod in enumerate((0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 10, 10, 20, 30, 30, 20, 10, 10,
                                 5, 5, 10, 25, 25, 10, 5, 5, 0, 0, 0, 20, 20, 0, 0, 0, 5, -5, -10, 0, 0, -10, -5, 5, 5,
                                 10, 10,-20,-20, 10, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0)):
            pawn2.move_to(n)
            self.assertEqual(Pawn._base_val + mod, pawn2.pos_val)


def main() -> None:
    unittest.main()


if __name__ == '__main__':
    main()
