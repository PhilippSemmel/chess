import unittest
from board import Queen, Piece, Board


board = Board()
queen1 = Queen(35, True, board)
queen2 = Queen(21, False, board)


class GeneralQueenConstructionTestCase(unittest.TestCase):
    def test_piece_pos_is_given_value(self):
        self.assertEqual(35, queen1._pos)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(21, queen2._pos)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, Queen, 64, True, board)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, Queen, -1, True, board)

    def test_piece_color_is_given_value(self):
        self.assertTrue(queen1._white_piece)

    def test_piece_color_is_any_given_value(self):
        self.assertFalse(queen2._white_piece)

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, Queen, True, True, board)

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, Queen, 1, 1, board)

    # def test_raises_type_error_if_board_is_not_board(self):
    #     self.assertRaises(TypeError, Queen, 1, True, 1)


class SpecificQueenConstructionTestCase(unittest.TestCase):
    def test_queen_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Queen, Piece))

    def test_piece_type_is_queen_code(self):
        self.assertEqual(4, queen1._type)


class GeneralQueenAttributeGetterTestCase(unittest.TestCase):
    def test_can_get_queen_pos(self):
        self.assertEqual(35, queen1.pos)

    def test_can_get_any_queen_pos(self):
        self.assertEqual(21, queen2.pos)

    def test_can_get_queen_color(self):
        self.assertTrue(queen1.color)

    def test_can_get_any_queen_color(self):
        self.assertFalse(queen2.color)


class QueenMoveGenerationTestCase(unittest.TestCase):
    def test_cannot_move_when_trapped_by_own_pieces(self):
        queen = Board('8/8/2PPP3/2PQP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual(set(), queen.pseudo_legal_moves)

    # vertical moves
    # to the right
    def test_can_move_one_step_to_the_right(self):
        queen = Board('8/8/2PPP3/2PQ1P2/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36)}, queen.pseudo_legal_moves)

    def test_can_move_two_steps_to_the_right(self):
        queen = Board('8/8/2PPP3/2PQ2P1/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36), (35, 37)}, queen.pseudo_legal_moves)

    def test_can_move_three_steps_to_the_right(self):
        queen = Board('8/8/2PPP3/2PQ3P/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36), (35, 37), (35, 38)}, queen.pseudo_legal_moves)

    def test_cannot_move_beyond_the_edge_of_the_board_to_the_right(self):
        queen = Board('8/8/2PPP3/2PQ4/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36), (35, 37), (35, 38), (35, 39)}, queen.pseudo_legal_moves)

    def test_can_move_from_any_position_to_the_right(self):
        queen = Board('8/8/8/8/8/1PPP4/1PQ5/1PPP4 w - - 0 1').get_piece(10)
        self.assertEqual({(10, 11), (10, 12), (10, 13), (10, 14), (10, 15)}, queen.pseudo_legal_moves)

    def test_can_capture_piece_one_step_to_the_right(self):
        queen = Board('8/8/2PPP3/2PQp3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36)}, queen.pseudo_legal_moves)


if __name__ == '__main__':
    unittest.main()
