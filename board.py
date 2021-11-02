from __future__ import annotations
from abc import ABC, abstractmethod
from typing import NewType, Union, Tuple, Set, Optional, List

POS = NewType('POS', int)
MOVE = Tuple[POS, POS]


class Piece(ABC):
    # def __init__(self, pos: POS, white_piece: bool, _type: int, board: Board) -> None:
    def __init__(self, pos: POS, white_piece: bool, _type: int) -> None:
        self._verify_params(pos, white_piece, _type)
        self._pos: POS = pos
        self._white_piece: bool = white_piece
        self._type: int = _type
        # self._board: Board = board
        """
        0 -> Pawn
        1 -> Knight
        2 -> Bishop
        3 -> Rook
        4 -> Queen
        5 -> King
        """

    @abstractmethod
    def __repr__(self):
        pass

    @staticmethod
    def _verify_params(pos: POS, white_piece: bool, _type: int) -> None:
        """
        verify the validity of the values passed to the constructor
        :param pos: pos value of the piece
        :param white_piece: color value of the piece
        :param _type: type value of the piece
        :raises TypeError if any value has a wrong type
        :raises ValueError if the pos or type value is wrong
        """
        if not type(pos) == int:
            raise TypeError('Positions value must be int.')
        if pos > 63 or pos < 0:
            raise ValueError('The position reach from value 0 to value 63 only.')
        if not type(white_piece) == bool:
            raise TypeError('white_piece values must be bool.')
        if not type(_type) == int:
            raise TypeError('type value must be int.')
        if _type > 5 or _type < 0:
            raise ValueError('The type codes reach from 0 to 5 only.')

    @property
    @abstractmethod
    def legal_moves(self) -> Set[MOVE]:
        """
        generate all legal moves the piece can make
        :return: set of all legal moves
        """
        pass


class Pawn(Piece):
    def __init__(self, pos: POS, white_piece: bool) -> None:
        super().__init__(pos, white_piece, 0)

    def __repr__(self):
        return '{}, pawn on pos {}'.format('white' if self._white_piece else 'black', self._pos)


class Knight(Piece):
    def __init__(self, pos: POS, white_piece: bool) -> None:
        super().__init__(pos, white_piece, 1)

    def __repr__(self):
        return '{}, knight on pos {}'.format('white' if self._white_piece else 'black', self._pos)


class Bishop(Piece):
    def __init__(self, pos: POS, white_piece: bool) -> None:
        super().__init__(pos, white_piece, 2)

    def __repr__(self):
        return '{}, bishop on pos {}'.format('white' if self._white_piece else 'black', self._pos)


class Rook(Piece):
    def __init__(self, pos: POS, white_piece: bool) -> None:
        super().__init__(pos, white_piece, 3)

    def __repr__(self):
        return '{}, rook on pos {}'.format('white' if self._white_piece else 'black', self._pos)


class Queen(Piece):
    def __init__(self, pos: POS, white_piece: bool) -> None:
        super().__init__(pos, white_piece, 4)

    def __repr__(self):
        return '{}, queen on pos {}'.format('white' if self._white_piece else 'black', self._pos)


class King(Piece):
    def __init__(self, pos: POS, white_piece: bool) -> None:
        super().__init__(pos, white_piece, 5)

    def __repr__(self):
        return '{}, king on pos {}'.format('white' if self._white_piece else 'black', self._pos)


# class Piece(ABC):
#     def __init__(self, pos: POS, color: COLOR, type_: int, board: Board):
#         self._pos: Union[POS, None] = pos
#         self._white_piece: COLOR = color
#         self._type: int = type_
#         self._board = board
#         self._all_directions: List[int] = [1, -1, 8, -8, 7, -7, 9, -9]
#         """
#         0 -> Pawn
#         1 -> Knight
#         2 -> Bishop
#         3 -> Rook
#         4 -> Queen
#         5 -> King
#         """
#
#     @property
#     def rank(self) -> int:
#         """
#         :return: number of the rank (vertical line)
#         """
#         return (self._pos // 8) + 1
#
#     def get_pos(self) -> POS:
#         return self._pos
#
#     def is_white_piece(self) -> COLOR:
#         return self._white_piece
#
#     def _squares_in_vertical_and_horizontal_directions(self) -> List[int]:
#         pass
#
#     @property
#     @abstractmethod
#     def attacking_squares(self) -> Set[MOVE]:
#         """
#         :return: a set of squares the piece attacks
#         """
#         pass
#
#     @property
#     @abstractmethod
#     def pseudo_legal_moves(self) -> Set[MOVE]:
#         """
#         :return: a set of squares the piece can move to in this turn
#         """
#         pass
#
#     def get_sliding_moves(self, directions: List[int], squares_in_directions: List[int], limiter: Optional[int] = 7) \
#             -> Set[MOVE]:
#         """
#         generate the moves of king, queen, rook, bishop and pawn except castling and en passant
#         :param directions: directions the piece can move
#         :param squares_in_directions: number of squares the piece can move into a direction
#         :param limiter: limits the squares a piece can move
#         :return: a set of squares a piece can move to by sliding
#         """
#         for direction, squares_in_direction in zip(directions, squares_in_directions):
#             pos = self._pos
#             for i in range(min(limiter, squares_in_direction)):
#                 pos += direction
#                 if self._board.piece_on(pos, self._white_piece):
#                     pass


class Board:
    def __init__(self) -> None:
        self._pieces: Set[Piece] = set()
        self._white_to_move: bool = True
        self._turn_number: int = 1
        self._castling_rights: int = 0xF
        """
        1 -> white kingside
        2 -> white queenside
        4 -> black kingside
        8 -> black queenside
        addition of the values in hexadecimal represents the current castling rights
        if there are no castling rights the value is 0
        """
        self._ep_target_square: Union[POS, None] = None
        self._half_move_clock: int = 0
        self._moves: List = []

    def parse_fen(self, fen: str) -> None:
        fen = fen.strip().split(' ')
        positions = fen[0].split('/')
        for r, rank in enumerate(positions):
            f = 0
            for sq in rank:
                if sq.isdigit():
                    f += int(sq)
                    continue
                elif sq == 'p' or sq == 'P':
                    self._pieces.add(Pawn(POS((7 - r) * 8 + f), sq.isupper()))
                elif sq == 'n' or sq == 'N':
                    self._pieces.add(Knight(POS((7 - r) * 8 + f), sq.isupper()))
                elif sq == 'b' or sq == 'B':
                    self._pieces.add(Bishop(POS((7 - r) * 8 + f), sq.isupper()))
                elif sq == 'r' or sq == 'R':
                    self._pieces.add(Rook(POS((7 - r) * 8 + f), sq.isupper()))
                elif sq == 'q' or sq == 'Q':
                    self._pieces.add(Queen(POS((7 - r) * 8 + f), sq.isupper()))
                elif sq == 'k' or sq == 'K':
                    self._pieces.add(King(POS((7 - r) * 8 + f), sq.isupper()))
                f += 1
        self._white_to_move = fen[1] == 'w'
        self._castling_rights = 0xF  # NotImplementedYet
        self._ep_target_square = None  # NotImplementedYet
        self._half_move_clock = int(fen[4])
        self._turn_number = int(fen[5])

    # def piece_on(self, pos: POS, is_white_piece: Optional[COLOR] = None) -> bool:
    #     """
    #     test whether a piece is on the given square
    #     :param pos: position of the square
    #     :param is_white_piece: tests only pieces with this color
    #     :return: whether a piece is on the given square
    #     """
    #     for piece in self._pieces:
    #         if is_white_piece is not None and is_white_piece != piece.is_white_piece():
    #             continue
    #         if piece.get_pos() == pos:
    #             return True
    #     return False


if __name__ == '__main__':
    board = Board()
    board.parse_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkg - 0 1')
