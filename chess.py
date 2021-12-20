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

    def _init_board(self) -> None:
        """
        let the player change the starting position if wanted
        """
        while True:
            input_ = input('> Do you want to change the starting positions? [y]es/[n]o: ')
            if input_ == 'y':
                self._set_board(input('> Enter the starting position as FEN-String: '))
                return
            elif input_ == 'n':
                return

    # def _set_board(self, fen: str) -> None:
    def _set_board(self, fen: str) -> None:
        """
        set the starting position
        :param fen: starting position as fen string
        """
        self._board = Board(fen)

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
    game
    """
    def main(self) -> None:  # tests & doc & new method: game_over -> bool
        """
        the main game loop
        """
        self._init_players()
        self._init_board()
        print(self._board)
        while True:
            if self._game_over:
                break
            moves = self._board.legal_moves
            move = self._active_player.get_move(moves)
            self._board.make_move(move)
            print(self._board)

    @property
    def _game_over(self) -> bool:
        """
        test if the game is over
        :return: whether the game is over
        game is over if one of the following situations is true:
        1. active player is in checkmate
        2. active player is in stalemate
        3. 50 consecutive moves have been made without moving a pawn or capturing
        4. only 2 pieces remain on the board
        """
        return self._board.checkmate \
            or self._board.stalemate \
            or self._board.half_move_clock >= 50 \
            or len(self._board.pieces) == 2


if __name__ == '__main__':
    game = Game()
    game.main()
