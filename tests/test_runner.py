import unittest
from typing import List

# game tests
import game_test
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
import tests.board_tests.board_test as board_test


def test_piece_classes() -> None:
    run_test_modules([bishop_test, king_test, knight_test, pawn_test, piece_test, queen_test, rook_test])


def test_player_classes() -> None:
    run_test_modules([com_player_test, human_player_test, player_test])


def test_board_classes() -> None:
    run_test_modules([board_test])


def test_game_classes() -> None:
    # does not test construction due to required user input
    run_test_modules([game_test])


def run_test_modules(test_modules: List) -> None:
    for test_module in test_modules:
        unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromModule(test_module))
