from __future__ import annotations
import random as r
from typing import TYPE_CHECKING, Set
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from chess import MOVE


class Player(ABC):
    def __init__(self, white: bool, name: str) -> None:
        self._white: bool = white
        self._name: str = name

    def __repr__(self) -> str:
        return f'{"White" if self._white else "Black"} Player {self._name}'

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
    """

    @abstractmethod
    def get_move(self, moves: Set[MOVE]) -> MOVE:
        """
        let the player select a move
        :param moves: legal moves
        :return: selected move
        """
        pass

    """
    user interface
    """

    def _move_to_ints(self, s: str) -> MOVE:
        """
        convert str move to two ints
        :param s: str move to convert
        :return: starting pos and final pos as int
        """
        if len(s) == 5:
            move = (self._pos_to_int(s[0:2]), self._pos_to_int(s[2:4]), s[4])
        else:
            move = (self._pos_to_int(s[0:2]), self._pos_to_int(s[2:4]), None)
        return move

    @staticmethod
    def _pos_to_int(pos: str) -> int:
        """
        convert str pos to int
        :param pos: pos to convert
        :return: pos as int
        """
        return (ord(pos[0]) - 97) + ((int(pos[1]) - 1) * 8)

    def _move_to_str(self, move: MOVE):
        """
        convert ints move to str
        :param move: move to convert
        :return: starting pos and final pos as str
        """
        s = self._pos_to_str(move[0]) + self._pos_to_str(move[1])
        if move[2] is not None:
            s += move[2]
        return s

    @staticmethod
    def _pos_to_str(pos: int) -> str:
        """
        convert pos input to int
        :param pos: pos to convert
        :return: pos as str
        """
        return chr((pos % 8) + 97) + (str((pos // 8) + 1))


class HumanPlayer(Player):
    def __init__(self, color: bool, name: str) -> None:
        super().__init__(color, name)

    def get_move(self, moves: Set[MOVE]) -> MOVE:
        moves_str = [self._move_to_str(move) for move in moves]
        while True:
            print('> Available moves:', moves_str)
            try:
                move = input('> Enter your move (e.g.: "e2e4"): ')
                self._verify_input(move)
                move = self._move_to_ints(move)
                self._verify_move(move, moves)
            except ValueError:
                print('Input or move invalid.')
                continue
            print(f'> {self.name} selected the move: {self._move_to_str(move)}\n')
            return move

    @staticmethod
    def _verify_input(move: str) -> None:
        """
        verify that the player input is correct
        :param move: player input
        :raises ValueError if input is incorrect
        """
        if len(move) == 4:
            if move[0] in 'abcdefgh' and move[1] in '12345678' and move[2] in 'abcdefgh' and move[3] in '12345678':
                return
        elif len(move) == 5:
            if move[0] in 'abcdefgh' and move[1] in '12345678' and move[2] in 'abcdefgh' and move[3] in '12345678' \
                    and move[4] in 'QRBNqrbn':
                return
        raise ValueError

    @staticmethod
    def _verify_move(move: MOVE, moves: Set[MOVE]) -> None:
        """
        verify that the move is legal
        :param move: move
        :param moves: legal moves
        :raises ValueError if move is not legal
        """
        if move not in moves:
            raise ValueError


class ComPlayer(Player):
    def __init__(self, color: bool) -> None:
        super().__init__(color, 'White Com' if color else 'Black Com')

    def get_move(self, moves: Set[MOVE]) -> MOVE:
        move = self._get_random_move(moves)
        print(f'> {self.name} selected the move: {self._move_to_str(move)}\n')
        return move

    @staticmethod
    def _get_random_move(moves: Set[MOVE]) -> MOVE:
        """
        let the com player select a random move
        :param moves: legal moves
        :return: random move
        """
        return r.sample(moves, 1)[0]
