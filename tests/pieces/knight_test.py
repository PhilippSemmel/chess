import unittest
from board import Knight, Piece, Board


board = Board()
knight1 = Knight(35, True, board)
knight2 = Knight(21, False, board)


class KnightConstructionTestCase(unittest.TestCase):
    def test_knight_is_subclass_of_piece(self):
        self.assertTrue(issubclass(Knight, Piece))

    def test_piece_type_is_knight_code(self):
        self.assertEqual(1, knight1._type)

    def test_piece_pos_is_given_value(self):
        self.assertEqual(35, knight1._pos)

    def test_piece_pos_is_any_given_value(self):
        self.assertEqual(21, knight2._pos)

    def test_piece_color_is_given_value(self):
        self.assertTrue(knight1._white_piece)

    def test_piece_color_is_any_given_value(self):
        self.assertFalse(knight2._white_piece)


class KingMoveGenerationTestCase(unittest.TestCase):
    # general
    def test_cannot_move_when_blocked_by_own_pieces(self):
        knight = Board('8/8/2P1P3/1P3P2/3N4/1P3P2/2P1P3/8 w - - 0 1').get_piece(27)
        self.assertEqual(set(), knight.pseudo_legal_moves)


if __name__ == '__main__':
    unittest.main()
