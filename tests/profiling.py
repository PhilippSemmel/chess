import cProfile

from board import Board
from board_tests.perft_test import perft_legal_moves

board: Board
search_depth: int


def profile_perft_starting_pos() -> None:
    global board, search_depth
    board = Board()
    search_depth = 3


def profile_perft_pos_2() -> None:
    global board, search_depth
    board = Board('r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1')
    search_depth = 2


if __name__ == '__main__':
    profile_perft_starting_pos()
    cProfile.run('perft_legal_moves(board, search_depth)', sort=1)
