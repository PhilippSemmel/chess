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
import tests.board_test as board_test
# game tests
import game_test

failed_tests: int


def main() -> None:
    """
    run all tests
    """
    global failed_tests
    failed_tests = test_piece_classes()
    failed_tests += test_player_classes()
    failed_tests += test_board_classes()
    failed_tests += test_game_classes()


def test_piece_classes() -> int:
    """
    run all piece tests
    """
    fails: int = 0
    for test_suite in [bishop_test, king_test, knight_test, pawn_test, piece_test, queen_test, rook_test]:
        test = unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromModule(test_suite))
        fails += len(test.failures)
        fails += len(test.errors)
    return fails


def test_player_classes() -> int:
    """
    run all player tests
    """
    fails: int = 0
    for test_suite in [com_player_test, human_player_test, player_test]:
        test = unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromModule(test_suite))
        fails += len(test.failures)
        fails += len(test.errors)
    return fails


def test_board_classes() -> int:
    """
    run all board tests
    """
    fails: int = 0
    for test_suite in [board_test]:
        test = unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromModule(test_suite))
        fails += len(test.failures)
        fails += len(test.errors)
    return fails


def test_game_classes() -> int:
    """
    run all game tests
    """
    # does not test player creation due to required user input
    # please run this test case in the game_test module
    fails: int = 0
    for test_suite in [game_test.ConstructionTestCase, game_test.GetterTestCase]:
        test = unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromTestCase(test_suite))
        fails += len(test.failures)
        fails += len(test.errors)
    return fails


def print_final_message() -> None:
    time.sleep(0.01)
    if not failed_tests:
        print('> All tests passed! ヽ(^o^)ノ')
    elif failed_tests == 1:
        print(f'> {failed_tests} test failed. Try again. t(ツ)_/¯')
    else:
        print(f'> {failed_tests} tests failed. Try again. t(ツ)_/¯')


if __name__ == '__main__':
    unittest.main()
    print_final_message()
