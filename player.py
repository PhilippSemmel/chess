from __future__ import annotations
from typing import TYPE_CHECKING, Set, Tuple
if TYPE_CHECKING:
    from chess import MOVE


class Player:
    def __init__(self, white: bool, name: str) -> None:
        self._white: bool = white
        self._name: str = name

    def __repr__(self):
        output = 'White' if self._white else 'Black'
        output += ' Player ' + self._name
        return output

    """
    Attribute getters
    """
    @property
    def white(self) -> bool:
        """
        get the color of the player
        :return: whether the player is white
        """
        return self._white

    @property
    def name(self) -> str:
        """
        get the name of the player
        :return: player name
        """
        return self._name

    """
    move selection
    user interface
    """
    def get_move(self, moves: Set[MOVE]):
        """
        let the player select a move
        :param moves: legal moves
        :return: selected move
        """
        moves_str = [self._move_to_str(move) for move in moves]
        while True:
            print('> Available moves:', moves_str)
            move = input('> Enter your move (e.g.: "e2e4"): ')
            if not self._correct_input(move):
                continue
            move = self._move_to_ints(move)
            if move not in moves:
                continue
            return move

    @staticmethod
    def _correct_input(move: str) -> bool:
        return len(move) == 5 and move[0] in 'abcdefgh' and move[1] in '12345678' and \
               move[2] in 'abcdefgh' and move[3] in '12345678'

    def _move_to_ints(self, move: str) -> MOVE:
        """
        convert str move to two ints
        :param move: move to convert
        :return: starting pos and final pos as int
        """
        move = move.split('-')
        return self._pos_to_int(move[0]), self._pos_to_int(move[1])

    @staticmethod
    def _pos_to_int(pos: str) -> int:
        """
        convert str pos to int
        :param pos: pos to convert
        :return: pos as int
        """
        return (ord(pos[0]) - 97) + ((int(pos[1]) - 1) * 8)

    def _moves_to_str(self, moves: Set[MOVE]):
        """
        convert all int moves to str
        :param moves: moves to convert
        :return: starting pos and final pos as str
        """
        return [self._move_to_str(move) for move in moves]

    def _move_to_str(self, move: MOVE):
        """
        convert ints move to str
        :param move: move to convert
        :return: starting pos and final pos as str
        """
        return self._pos_to_str(move[0]) + self._pos_to_str(move[1])

    @staticmethod
    def _pos_to_str(pos: int) -> str:
        """
        convert pos input to int
        :param pos: pos to convert
        :return: pos as str
        """
        return chr((pos % 8) + 97) + (str((pos // 8) + 1))
