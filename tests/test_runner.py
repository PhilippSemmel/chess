import unittest
# pieces tests
import pieces_tests.bishop_test as bishop_test
import pieces_tests.king_test as king_test
import pieces_tests.knight_test as knight_test
import pieces_tests.pawn_test as pawn_test
import pieces_tests.piece_test as piece_test
import pieces_tests.queen_test as queen_test
import pieces_tests.rook_test as rook_test
# player tests
import player_tests.com_player_test as com_player_test
import player_tests.human_player_test as human_player_test
import player_tests.player_test as player_test
# board tests
import board_test
# game tests
import game_test


def main() -> None:
    """
    run all tests
    """
    test_piece_classes()
    test_player_classes()
    test_board_classes()
    test_game_classes()


def test_piece_classes() -> None:
    """
    run all piece tests
    """
    for test_suite in [bishop_test, king_test, knight_test, pawn_test, piece_test, queen_test, rook_test]:
        i = unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromModule(test_suite))


def test_player_classes() -> None:
    """
    run all player tests
    """
    for test_suite in [com_player_test, human_player_test, player_test]:
        unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromModule(test_suite))


def test_board_classes() -> None:
    """
    run all board tests
    """
    board_tests = unittest.TestLoader().loadTestsFromModule(board_test)
    unittest.TextTestRunner(verbosity=0).run(board_tests)


def test_game_classes() -> None:
    """
    run all game tests
    """
    game_construction_tests = unittest.TestLoader().loadTestsFromTestCase(game_test.ConstructionTestCase)
    game_getter_tests = unittest.TestLoader().loadTestsFromTestCase(game_test.GetterTestCase)
    # test is commented out due to required user input
    # please run this test case in the game_test module
    # game_tests = unittest.TestLoader().loadTestsFromTestCase(game_test.CreatePlayerTestCase)
    unittest.TextTestRunner(verbosity=0).run(game_construction_tests)
    unittest.TextTestRunner(verbosity=0).run(game_getter_tests)


if __name__ == '__main__':
    main()
