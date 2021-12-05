from board import Board
from UI import Display
from player import Player
from typing import Tuple

MOVE = Tuple[int, int]


board = Board()
print(board)
w_player = Player(True, input('> Enter the name for the white player: '))
b_player = Player(False, input('> Enter the name for the black player: '))
active_player, inactive_player = (w_player, b_player) if board.white_to_move else (b_player, w_player)


def main():
    while True:
        moves = board.legal_moves
        move = active_player.get_move(moves)
        board.make_move(move)
        print(board)
        if board.checkmate:
            print(active_player.name + ' wins.')
            break
        if board.stalemate:
            print('Stalemate.')
            break
        new_turn()


def new_turn():
    global active_player, inactive_player
    active_player, inactive_player = inactive_player, active_player


if __name__ == '__main__':
    main()
