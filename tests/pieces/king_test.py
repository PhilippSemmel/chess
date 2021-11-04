import unittest
from board import King, Piece, Board


board = Board()
king1 = King(35, True, board)
king2 = King(21, False, board)


class GeneralKingConstructionTestCase(unittest.TestCase):
    def test_piece_pos_is_given_value(self):
        self.assertEqual(35, king1._pos)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(21, king2._pos)

    def test_raises_value_error_if_pos_value_is_too_high(self):
        self.assertRaises(ValueError, King, 64, True, board)

    def test_raises_value_error_is_pos_value_is_too_low(self):
        self.assertRaises(ValueError, King, -1, True, board)

    def test_piece_color_is_given_value(self):
        self.assertTrue(king1._white_piece)

    def test_piece_color_is_any_given_value(self):
        self.assertFalse(king2._white_piece)

    def test_raises_type_error_if_pos_is_not_int(self):
        self.assertRaises(TypeError, King, True, True, board)

    def test_raises_type_error_if_white_piece_is_not_bool(self):
        self.assertRaises(TypeError, King, 1, 1, board)

    # def test_raises_type_error_if_board_is_not_board(self):
    #     self.assertRaises(TypeError, King, 1, True, 1)


class SpecificKingConstructionTestCase(unittest.TestCase):
    def test_queen_is_subclass_of_piece(self):
        self.assertTrue(issubclass(King, Piece))

    def test_piece_type_is_queen_code(self):
        self.assertEqual(5, king1._type)


class KingMoveGenerationTestCase(unittest.TestCase):
    # general
    def test_cannot_move_when_trapped_by_own_pieces(self):
        king = Board('8/8/2PPP3/2PKP3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual(set(), king.pseudo_legal_moves)

    # horizontal moves
    # right
    def test_can_move_one_step_right(self):
        king = Board('8/8/2PPP3/2PK1P2/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36)}, king.pseudo_legal_moves)

    def test_cannot_move_two_steps_right(self):
        king = Board('8/8/2PPP3/2PK2P1/2PPP3/8/8/8 w - - 0 1').get_piece(35)
        self.assertEqual({(35, 36)}, king.pseudo_legal_moves)

    # def test_can_move_from_any_position_right(self):
    #     queen = Board('8/8/8/8/8/1PPP4/1PQ5/1PPP4 w - - 0 1').get_piece(10)
    #     self.assertEqual({(10, 11), (10, 12), (10, 13), (10, 14), (10, 15)}, queen.pseudo_legal_moves)
    #
    # def test_can_capture_one_step_right(self):
    #     queen = Board('8/8/2PPP3/2PQp3/2PPP3/8/8/8 w - - 0 1').get_piece(35)
    #     self.assertEqual({(35, 36)}, queen.pseudo_legal_moves)
    #
    # def test_cannot_capture_two_steps_rights(self):
    #     pass
    #
    # def test_cannot_capture_beyond_the_board_right(self):
    #     queen = Board('8/8/p1PPP3/2PQ4/2PPP3/8/8/8 w - - 0 1').get_piece(35)
    #     self.assertEqual({(35, 36), (35, 37), (35, 38), (35, 39)}, queen.pseudo_legal_moves)


if __name__ == '__main__':
    unittest.main()
