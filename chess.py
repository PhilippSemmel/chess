from board import Board
from player import Player, HumanPlayer, ComPlayer
from typing import Tuple, Union

MOVE = Tuple[int, int]


class Game:
    def __init__(self) -> None:
        self._board: Board = Board()
        self._w_player: Union[None, Player] = None
        self._b_player: Union[None, Player] = None

    """
    initialization
    """
    def _init_players(self) -> None:
        """
        initialize the player objects
        """
        self._w_player = self._create_player('white')
        self._b_player = self._create_player('black')

    @staticmethod
    def _create_player(color: str) -> Player:
        """
        create a new player object
        :param color: need to be "white" if player is supposed to be white otherwise "black"
        :return: player object
        """
        while True:
            input_ = input(f'> Is the {color} player a human player? [y]es/[n]o: ')
            if input_ == 'y':
                return HumanPlayer(color == 'white', input(f'> Enter the name of the {color} human player: '))
            elif input_ == 'n':
                return ComPlayer(color == 'white')

    """
    getters
    """
    @property
    def _active_player(self) -> Player:
        """
        get the active player
        :return: active player object
        """
        return self._w_player if self._board.white_to_move else self._b_player

    @property
    def _inactive_player(self) -> Player:
        """
        get the inactive player
        :return: inactive player object
        """
        return self._b_player if self._board.white_to_move else self._w_player

    """
    game loop
    """
    def main(self) -> None:  # tests & doc & new method: game_over -> bool
        self._init_players()
        print(self._board)
        while True:
            moves = self._board.legal_moves
            move = self._active_player.get_move(moves)
            self._board.make_move(move)
            print(self._board)
            if self._board.checkmate:
                print(self._inactive_player.name + ' wins.')
                break
            if self._board.stalemate:
                print('Stalemate.')
                break
            if self._board.half_move_clock >= 50:
                print('Reicht jetzt auch.')
                break
            if len(self._board.pieces) <= 2:
                print('REMIS!')
                break


if __name__ == '__main__':
    game = Game()
    game.main()
