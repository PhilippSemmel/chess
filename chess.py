from board import Board
from player import Player, HumanPlayer, ComPlayer
from typing import Tuple, Union

MOVE = Tuple[int, int, Union[str, None]]


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

    def main(self) -> None:
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
        """
        return self._board.checkmate or self._board.is_draw

    def _get_game_over_message(self) -> str:
        """
        get the game over message
        :return: a message according to the end of the game
        :raises ValueError if game is not over
        """
        if self._board.checkmate:
            return f'Checkmate! {self._inactive_player.name} wins.'
        elif self._board.stalemate:
            return 'Draw due to stalemate.'
        elif self._board.seventy_five_move_rule_applies:
            return 'Draw due to the applying seventy-five-move rule.'
        elif self._board.fivefold_repetition_rule_applies:
            return 'Draw due to the applying fivefold repetition rule.'
        elif self._board.is_dead_position:
            return 'Draw due to dead position.'
        raise ValueError('Game is not over.')


if __name__ == '__main__':
    game = Game()
    game.main()
