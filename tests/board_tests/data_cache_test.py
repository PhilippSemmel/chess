import unittest
from board import Board

board = Board('8/8/8/8/8/8/7r/K7 w - - 0 1')
move_cache = Board._DataCache(board._get_legal_moves)
piece_cache = Board._DataCache(board._get_active_pieces)


class ConstructionTestCase(unittest.TestCase):
    def test_data_is_none(self):
        self.assertIsNone(move_cache._data)

    def test_data_is_always_none(self):
        self.assertIsNone(piece_cache._data)

    def test_func_is_given_function(self):
        self.assertEqual(board._get_legal_moves, move_cache._func)

    def test_func_is_always_given_function(self):
        self.assertEqual(board._get_active_pieces, piece_cache._func)


class GetDataTestCase(unittest.TestCase):
    def test_can_get_correct_function_data(self):
        self.assertEqual(move_cache.get(), {(0, 1)})

    def test_can_get_any_correct_function_data(self):
        self.assertEqual(piece_cache.get(), {board._get_piece(0)} | {board._get_piece(15)})

    def test_does_not_recalculate_the_data(self):
        self.assertIs(move_cache.get(), move_cache.get())

    def test_does_never_recalculate_the_data(self):
        self.assertIs(piece_cache.get(), piece_cache.get())


class ClearDataTestCase(unittest.TestCase):
    def test_data_is_non_after_clearing(self):
        move_cache.clear()
        self.assertIsNone(move_cache._data)

    def test_data_is_always_non_after_clearing(self):
        piece_cache.clear()
        self.assertIsNone(piece_cache._data)


def main() -> None:
    unittest.main()


if __name__ == '__main__':
    main()
