import time
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
from tests.board_tests import board_test
# game tests
import game_test


failed_tests: int


def main() -> None:
    """
    run all tests
    """
    global failed_tests
    failed_tests = 0
    test_piece_classes()
    test_player_classes()
    test_board_classes()
    test_game_classes()
    print_final_message()


def test_piece_classes() -> None:
    """
    run all piece tests
    """
    global failed_tests
    for test_suite in [bishop_test, king_test, knight_test, pawn_test, piece_test, queen_test, rook_test]:
        test = unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromModule(test_suite))
        failed_tests += len(test.failures)
        failed_tests += len(test.errors)


def test_player_classes() -> None:
    """
    run all player tests
    """
    global failed_tests
    for test_suite in [com_player_test, human_player_test, player_test]:
        test = unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromModule(test_suite))
        failed_tests += len(test.failures)
        failed_tests += len(test.errors)


def test_board_classes() -> None:
    """
    run all board tests
    """
    global failed_tests
    board_tests = unittest.TestLoader().loadTestsFromModule(board_test)
    test = unittest.TextTestRunner(verbosity=0).run(board_tests)
    failed_tests += len(test.failures)
    failed_tests += len(test.errors)


def test_game_classes() -> None:
    """
    run all game tests
    """
    global failed_tests
    game_construction_tests = unittest.TestLoader().loadTestsFromTestCase(game_test.ConstructionTestCase)
    game_getter_tests = unittest.TestLoader().loadTestsFromTestCase(game_test.GetterTestCase)
    # test is commented out due to required user input
    # please run this test case in the game_test module
    # game_tests = unittest.TestLoader().loadTestsFromTestCase(game_test.CreatePlayerTestCase)
    test = unittest.TextTestRunner(verbosity=0).run(game_construction_tests)
    failed_tests += len(test.failures)
    failed_tests += len(test.errors)
    test = unittest.TextTestRunner(verbosity=0).run(game_getter_tests)
    failed_tests += len(test.failures)
    failed_tests += len(test.errors)


def print_final_message() -> None:
    time.sleep(0.01)
    if not failed_tests:
        print('> All tests passed! ヽ(^o^)ノ')
    elif failed_tests == 1:
        print(f'> {failed_tests} test failed. Try again. t(ツ)_/¯')
    else:
        print(f'> {failed_tests} tests failed. Try again. t(ツ)_/¯')


if __name__ == '__main__':
    # cProfile.run('main()', sort=2)
    main()
