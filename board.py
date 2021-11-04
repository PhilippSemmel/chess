from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union, Tuple, Set, Optional

MOVE = Tuple[int, int]


class Piece(ABC):
    def __init__(self, pos: int, white_piece: bool, _type: int, board: Board) -> None:
        # self._verify_params(pos, white_piece, _type, board)
        self._verify_params(pos, white_piece, _type)
        self._pos: int = pos
        self._white_piece: bool = white_piece
        self._type: int = _type
        self._board: Board = board
        """
        0 -> Pawn
        1 -> Knight
        2 -> Bishop
        3 -> Rook
        4 -> Queen
        5 -> King
        """

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @staticmethod
    # def _verify_params(pos: int, white_piece: bool, _type: int, board: Board) -> None:
    def _verify_params(pos: int, white_piece: bool, _type: int) -> None:
        """
        verify the validity of the values passed to the constructor
        :param pos: pos value of the piece
        :param white_piece: color value of the piece
        :param _type: type value of the piece
        :param board: board object
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
        # if not type(board) == Board:
        #     raise ValueError('Invalid board object.')

    """
    attribute getters
    """
    @property
    def pos(self) -> int:
        """
        get the piece's positions
        :return: the piece's positions
        """
        return self._pos

    @property
    def color(self) -> bool:
        """
        get the piece's color
        :return: the piece's color
        """
        return self._white_piece

    @property
    def type(self) -> int:
        """
        get the piece's type
        :return: the piece's type
        """
        return self._type

    @property
    @abstractmethod
    def pseudo_legal_moves(self) -> Set[MOVE]:
        """
        generate all legal moves the piece can make
        :return: set of all legal moves
        """
        pass


class Pawn(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 0, board)

    def __repr__(self) -> str:
        return '{} pawn on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        pass


class Knight(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 1, board)

    def __repr__(self) -> str:
        return '{} knight on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        pass


class Bishop(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 2, board)

    def __repr__(self) -> str:
        return '{} bishop on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        pass


class Rook(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 3, board)

    def __repr__(self) -> str:
        return '{} rook on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        pass


class Queen(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 4, board)

    def __repr__(self) -> str:
        return '{} queen on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        moves = set()
        direction = [1, -1, 8, -8, 9]   # rights, left, up, down, right up
        direction_limiter = [7 - (self._pos % 8), self._pos % 8, 7 - self._pos // 8, self._pos // 8, min(7 - (self._pos % 8), 7 - self._pos // 8)]  # rights, left, up, down
        for d, l in zip(direction, direction_limiter):
            for pos in range(self._pos + d, self._pos + (d * l), d):
                if self._board.own_piece_on_square(pos, self._white_piece):
                    break
                moves.add((self._pos, pos))
                if self._board.opponent_piece_on_square(pos, self._white_piece):
                    break
        return moves


class King(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 5, board)

    def __repr__(self) -> str:
        return '{} king on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        pass


# class Piece(ABC):
#     def __init__(self, pos: int, color: COLOR, type_: int, board: Board):
#         self._pos: Union[int, None] = pos
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
#     def get_pos(self) -> int:
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


class Board(object):
    def __init__(self, fen: Optional[str] = None) -> None:
        if fen:
            self._pieces, self._white_to_move, self._castling_rights, self._ep_target_square, self._half_move_clock, \
                self._turn_number = self._parse_fen(fen)
            return

        self._pieces: Set[Piece] = set()
        self._white_to_move: bool = True
        self._castling_rights: int = 15
        """
        1 -> white kingside
        2 -> white queenside
        4 -> black kingside
        8 -> black queenside
        addition of the values in hexadecimal represents the current castling rights
        if there are no castling rights the value is 0
        """
        self._ep_target_square: Union[int, None] = None
        self._half_move_clock: int = 0
        self._turn_number: int = 1

    def _parse_fen(self, fen: str) -> Tuple[Set[Piece], bool, int, int, int, int]:
        """
        translate a fen string to the data the class needs for the board representation
        :param fen: the fen string to translate
        :return: piece objects on the board, color to move, castling rights, ep target square, half move clock, turn
                 number
        """
        def get_castling_rights() -> int:
            rights = 0
            if 'K' in fen[2]:
                rights += 1
            if 'Q' in fen[2]:
                rights += 2
            if 'k' in fen[2]:
                rights += 4
            if 'q' in fen[2]:
                rights += 8
            return rights

        def get_ep_target_square() -> Union[None, int]:
            if fen[3] == '-':
                return None
            return (ord(fen[3][0]) - 97) + (int(fen[3][1]) - 1) * 8

        fen = fen.strip().split(' ')
        positions = fen[0].split('/')
        pieces = set()
        for r, rank in enumerate(positions):
            f = 0
            for sq in rank:
                if sq.isdigit():
                    f += int(sq)
                    continue
                elif sq == 'p' or sq == 'P':
                    pieces.add(Pawn((7 - r) * 8 + f, sq.isupper(), self))
                elif sq == 'n' or sq == 'N':
                    pieces.add(Knight((7 - r) * 8 + f, sq.isupper(), self))
                elif sq == 'b' or sq == 'B':
                    pieces.add(Bishop((7 - r) * 8 + f, sq.isupper(), self))
                elif sq == 'r' or sq == 'R':
                    pieces.add(Rook((7 - r) * 8 + f, sq.isupper(), self))
                elif sq == 'q' or sq == 'Q':
                    pieces.add(Queen((7 - r) * 8 + f, sq.isupper(), self))
                elif sq == 'k' or sq == 'K':
                    pieces.add(King((7 - r) * 8 + f, sq.isupper(), self))
                f += 1
        white_to_move = fen[1] == 'w'
        castling_rights = get_castling_rights()
        ep_target_square = get_ep_target_square()
        half_move_clock = int(fen[4])
        turn_number = int(fen[5])
        return pieces, white_to_move, castling_rights, ep_target_square, half_move_clock, turn_number

    def __repr__(self):
        pass

    """
    attribute getters
    """
    @property
    def pieces(self) -> Set[Piece]:
        """
        get the pieces on the board
        :return: a set with all pieces on the board
        """
        return self._pieces

    @property
    def color_to_move(self) -> bool:
        """
        get the color to move
        :return: the color to move
        """
        return self._white_to_move

    @property
    def castling_rights(self) -> int:
        """
        get the castling rights
        :return: the castling rights
        """
        return self._castling_rights

    @property
    def ep_target_square(self) -> Union[int, None]:
        """
        get the en passant target square
        :return: the en passant target square
        """
        return self._ep_target_square

    @property
    def half_move_clock(self) -> int:
        """
        get the half move clock
        :return: the half move clock
        """
        return self._half_move_clock

    @property
    def turn_number(self) -> int:
        """
        get the turn number
        :return: the turn number
        """
        return self._turn_number

    """
    position state getter
    """
    def is_square_empty(self, pos: int) -> bool:
        """
        test whether there is a piece on the given position
        :param pos: position of the square to test
        :return: whether there is a piece at the given position
        """
        for piece in self._pieces:
            if piece.pos == pos:
                return False
        return True

    def own_piece_on_square(self, pos: int, color: bool) -> bool:
        """
        test whether there is a piece on the given position the the same color as given
        :param pos: positions of the square to test
        :param color: own color
        :return: whether there is one of your own pieces at the given position
        """
        for piece in self._pieces:
            if piece.pos == pos and piece.color == color:
                return True
        return False

    def opponent_piece_on_square(self, pos: int, color: bool) -> bool:
        """
        test whether there is a piece on the given position the a different color as given
        :param pos: positions of the square to test
        :param color: own color
        :return: whether there is one of your opponent's own pieces at the given position
        """
        for piece in self._pieces:
            if piece.pos == pos and not piece.color == color:
                return True
        return False

    """
    misc getters
    """
    def get_piece(self, pos: int) -> Piece:
        """
        get the piece on the given position
        :param pos: positions of the piece
        :return: the piece on the given position
        :raises ValueError if there is no piece on the square
        """
        for piece in self._pieces:
            if piece.pos == pos:
                return piece
        raise ValueError('No piece found on the given position.')