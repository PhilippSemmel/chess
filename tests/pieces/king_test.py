import unittest
from board import King, Piece, Board


board = Board()
king1 = King(35, True, board)
king2 = King(21, False, board)


class GeneralKingConstructionTestCase(unittest.TestCase):
    def test_king_is_subclass_of_piece(self):
        self.assertTrue(issubclass(King, Piece))

    def test_piece_type_is_king_code(self):
        self.assertEqual(5, king1._type)

    def test_piece_pos_is_given_value(self):
        self.assertEqual(35, king1._pos)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(21, king2._pos)

    def test_piece_color_is_given_value(self):
        self.assertTrue(king1._white_piece)

    def test_piece_color_is_any_given_value(self):
        self.assertFalse(king2._white_piece)


class KingMoveGenerationTestCase(unittest.TestCase):
    # general
    def test_cannot_move_when_blocked_by_own_pieces(self):
        king = Board('8/8/2PPP3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual(set(), king.pseudo_legal_moves)

    def test_can_move_in_multiple_directions(self):
        king = Board('8/1p1p4/4p3/2PKp3/4P3/1P1P4/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36), (35, 44), (35, 43), (35, 42), (35, 26), (35, 27)}, king.pseudo_legal_moves)

    # horizontal moves
    # right
    def test_can_move_one_step_right(self):
        king = Board('8/8/2PPP3/2PK1P2/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36)}, king.pseudo_legal_moves)

    def test_cannot_move_two_steps_right(self):
        king = Board('8/8/2PPP3/2PK2P1/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36)}, king.pseudo_legal_moves)

    def test_can_move_from_any_position_right(self):
        king = Board('8/8/8/8/3PPP2/3PK3/3PPP2/8 w - - 0 1').get_piece(20)
        self.assertEqual({(20, 21)}, king.pseudo_legal_moves)

    def test_can_capture_one_step_right(self):
        king = Board('8/8/2PPP3/2PKp3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36)}, king.pseudo_legal_moves)

    def test_cannot_capture_two_steps_right(self):
        king = Board('8/8/2PPP3/2PK1p2/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36)}, king.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right(self):
        king = Board('8/P7/6PP/P5PK/6PP/8/8/8 w - - 0 1').get_piece(39)
        self.assertEqual(set(), king.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right(self):
        king = Board('8/P7/p5PP/P5PK/6PP/8/8/8 w - - 0 1').get_piece(39)
        self.assertEqual(set(), king.pseudo_legal_moves)

    # left
    def test_can_move_one_step_left(self):
        king = Board('8/8/2PPP3/1P1KP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 34)}, king.pseudo_legal_moves)

    def test_cannot_move_two_steps_left(self):
        king = Board('8/8/2PPP3/P2KP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 34)}, king.pseudo_legal_moves)

    def test_can_move_from_any_position_left(self):
        king = Board('8/8/8/8/3PPP2/4KP2/3PPP2/8 w - - 0 1').get_piece(20)
        self.assertEqual({(20, 19)}, king.pseudo_legal_moves)

    def test_can_capture_one_step_left(self):
        king = Board('8/8/2PPP3/2pKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 34)}, king.pseudo_legal_moves)

    def test_cannot_capture_two_steps_left(self):
        king = Board('8/8/2PPP3/1p1KP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 34)}, king.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left(self):
        king = Board('8/8/PP6/KP5P/PP6/7P/8/8 w - - 0 1').get_piece(32)
        self.assertEqual(set(), king.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left(self):
        king = Board('8/8/PP6/KP5P/PP5p/7P/8/8 w - - 0 1').get_piece(32)
        self.assertEqual(set(), king.pseudo_legal_moves)

    # vertical moves
    # up
    def test_can_move_one_step_up(self):
        king = Board('8/3P4/2P1P3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 43)}, king.pseudo_legal_moves)

    def test_cannot_move_two_steps_up(self):
        king = Board('3P4/8/2P1P3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 43)}, king.pseudo_legal_moves)

    def test_can_capture_one_step_up(self):
        king = Board('8/8/2PpP3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 43)}, king.pseudo_legal_moves)

    def test_cannot_capture_two_steps_ups(self):
        king = Board('8/3p4/2P1P3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 43)}, king.pseudo_legal_moves)

    def test_can_move_from_any_position_up(self):
        king = Board('8/8/8/8/8/5P1P/5PKP/5PPP w - - 0 1').get_piece(14)
        self.assertEqual({(14, 22)}, king.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_up(self):
        king = Board('3PKP2/3PPP2/8/8/8/8/8/8 w - - 0 1').get_piece(60)
        self.assertEqual(set(), king.pseudo_legal_moves)

    # down
    def test_can_move_one_step_down(self):
        king = Board('8/8/2PPP3/2PKP3/2P1P3/3P4/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 27)}, king.pseudo_legal_moves)

    def test_cannot_move_two_steps_down(self):
        king = Board('8/8/2PPP3/2PKP3/2P1P3/8/3P4/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 27)}, king.pseudo_legal_moves)

    def test_can_capture_one_step_down(self):
        king = Board('8/8/2PPP3/2PKP3/2PpP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 27)}, king.pseudo_legal_moves)

    def test_cannot_capture_two_steps_downs(self):
        king = Board('8/8/2PPP3/2PKP3/2P1P3/3p4/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 27)}, king.pseudo_legal_moves)

    def test_can_move_from_any_position_down(self):
        king = Board('5PPP/5PKP/5P1P/8/8/8/8/8 w - - 0 1').get_piece(54)
        self.assertEqual({(54, 46)}, king.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_down(self):
        king = Board('8/8/8/8/8/8/PPP5/PKP5 w - - 0 1').get_piece(1)
        self.assertEqual(set(), king.pseudo_legal_moves)

    # diagonal moves
    # right up
    def test_can_move_one_step_right_up(self):
        king = Board('8/5P2/2PP4/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 44)}, king.pseudo_legal_moves)

    def test_cannot_move_two_steps_right_up(self):
        king = Board('6P1/8/2PP4/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 44)}, king.pseudo_legal_moves)

    def test_can_capture_one_step_right_up(self):
        king = Board('8/8/2PPp3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 44)}, king.pseudo_legal_moves)

    def test_cannot_capture_two_steps_right_up(self):
        king = Board('6p1/8/2PP4/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 44)}, king.pseudo_legal_moves)

    def test_can_move_from_any_position_right_up(self):
        king = Board('8/8/8/8/8/PP6/PKP5/PPP5 w - - 0 1').get_piece(9)
        self.assertEqual({(9, 18)}, king.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right_up(self):
        king = Board('8/8/P5PP/P5PK/6PP/8/8/8 w - - 0 1').get_piece(39)
        self.assertEqual(set(), king.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right_up(self):
        king = Board('8/p7/P5PP/P5PK/6PP/8/8/8 w - - 0 1').get_piece(39)
        self.assertEqual(set(), king.pseudo_legal_moves)

    # right down
    def test_can_move_one_step_right_down(self):
        king = Board('8/8/2PPP3/2PKP3/2PP4/5P2/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 28)}, king.pseudo_legal_moves)

    def test_cannot_move_two_steps_right_down(self):
        king = Board('8/8/2PPP3/2PKP3/2PP4/8/6P1/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 28)}, king.pseudo_legal_moves)

    def test_can_capture_one_step_right_down(self):
        king = Board('8/8/2PPP3/2PKP3/2PPp3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 28)}, king.pseudo_legal_moves)

    def test_cannot_capture_two_steps_right_down(self):
        king = Board('8/8/2PPP3/2PKP3/2PP4/5p2/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 28)}, king.pseudo_legal_moves)

    def test_can_move_from_any_position_right_down(self):
        king = Board('PPP5/PKP5/PP6/8/8/8/8/8 w - - 0 1').get_piece(49)
        self.assertEqual({(49, 42)}, king.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_right_down(self):
        king = Board('8/P7/P5PP/6PK/6PP/8/8/8 w - - 0 1').get_piece(39)
        self.assertEqual(set(), king.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_right_down(self):
        king = Board('8/P7/P5PP/p5PK/6PP/8/8/8 w - - 0 1').get_piece(39)
        self.assertEqual(set(), king.pseudo_legal_moves)

    # left up
    def test_can_move_one_step_left_up(self):
        king = Board('8/1P6/3PP3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 42)}, king.pseudo_legal_moves)

    def test_cannot_move_two_steps_left_up(self):
        king = Board('P7/8/3PP3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 42)}, king.pseudo_legal_moves)

    def test_can_capture_one_step_left_up(self):
        king = Board('8/8/2pPP3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 42)}, king.pseudo_legal_moves)

    def test_cannot_capture_two_steps_left_up(self):
        king = Board('8/1p6/3PP3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 42)}, king.pseudo_legal_moves)

    def test_can_move_from_any_position_left_up(self):
        king = Board('8/8/8/8/8/6PP/5PKP/5PPP w - - 0 1').get_piece(14)
        self.assertEqual({(14, 21)}, king.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left_up(self):
        king = Board('8/8/PP6/KP6/PP5P/7P/8/8 w - - 0 1').get_piece(32)
        self.assertEqual(set(), king.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left_up(self):
        king = Board('8/8/PP6/KP5p/PP5P/7P/8/8 w - - 0 1').get_piece(32)
        self.assertEqual(set(), king.pseudo_legal_moves)

    # left down
    def test_can_move_one_step_left_down(self):
        king = Board('8/8/2PPP3/2PKP3/3PP3/1P6/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 26)}, king.pseudo_legal_moves)

    def test_cannot_move_two_steps_left_down(self):
        king = Board('8/8/2PPP3/2PKP3/3PP3/8/P7/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 26)}, king.pseudo_legal_moves)

    def test_can_capture_one_step_left_down(self):
        king = Board('8/8/2PPP3/2PKP3/2pPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 26)}, king.pseudo_legal_moves)

    def test_cannot_capture_two_steps_left_down(self):
        king = Board('8/8/2PPP3/2PKP3/3PP3/1p6/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 26)}, king.pseudo_legal_moves)

    def test_can_move_from_any_position_left_down(self):
        king = Board('5PPP/5PKP/6PP/8/8/8/8/8 w - - 0 1').get_piece(54)
        self.assertEqual({(54, 45)}, king.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_left_down(self):
        king = Board('8/8/PP6/KP5P/PP5P/8/8/8 w - - 0 1').get_piece(32)
        self.assertEqual(set(), king.pseudo_legal_moves)

    def test_cannot_capture_beyond_the_board_left_down(self):
        king = Board('8/8/PP6/KP5P/PP5P/7p/8/8 w - - 0 1').get_piece(32)
        self.assertEqual(set(), king.pseudo_legal_moves)


if __name__ == '__main__':
    unittest.main()
