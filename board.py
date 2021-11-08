from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union, Tuple, Set, Optional, List

MOVE = Tuple[int, int]


class Piece(ABC):
    def __init__(self, pos: int, white_piece: bool, _type: int, board: Board) -> None:
        self._verify_params(pos, white_piece, _type)
        # piece info
        self._pos: int = pos
        self._white_piece: bool = white_piece
        self._type: int = _type
        # objects
        self._board: Board = board
        # misc data
        # order of the differences :right, left, up, down, right up, left up, right down, left down
        self._all_position_differences: List[int] = [1, -1, 8, -8, 9, 7, -7, -9]
        """
        0 -> Pawn
        1 -> Knight
        2 -> Bishop
        3 -> Rook
        4 -> Queen
        5 -> King
        """

    @staticmethod
    def _verify_params(pos: int, white_piece: bool, _type: int) -> None:
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

    @abstractmethod
    def __repr__(self) -> str:
        pass

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

    """
    other getters
    """
    @property
    def rank(self) -> int:
        """
        get the rank the piece stands on
        :return: the rank the piece stands on
        """
        return self._pos // 8

    @property
    def file(self) -> int:
        """
        get the file the piece stands on
        :return: the file the piece stands on
        """
        return self._pos % 8

    @property
    def _max_moves(self) -> List[int]:
        """
        get the number of squares in each direction starting from the pieces position
        :return:list of numbers of squares in each direction starting from the pieces position
        """
        r = self.rank
        f = self.file
        right = 7 - f
        left = f
        up = 7 - r
        down = r
        return [right, left, up, down, min(right, up), min(left, up), min(right, down), min(left, down)]

    """
    move generation
    """
    @property
    @abstractmethod
    def pseudo_legal_moves(self) -> Set[MOVE]:
        """
        generate all pseudo legal moves the piece can make
        :return: set of all legal moves available
        """
        pass

    def _generate_sliding_moves(self, position_differences: List[int] = None, max_moves: List[int] = None) -> Set[MOVE]:
        """

        """
        if not position_differences:
            position_differences = self._all_position_differences
        if not max_moves:
            max_moves = self._max_moves
        moves = set()

        for d, m in zip(position_differences, max_moves):
            for n, new_pos in enumerate(range(self._pos + d, self._pos + ((m + 1) * d), d)):
                if self._board.own_piece_on_square(new_pos, self._white_piece):
                    break
                moves.add((self._pos, new_pos))
                if self._board.opponent_piece_on_square(new_pos, self._white_piece):
                    break
        return moves


class Pawn(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 0, board)

    def __repr__(self) -> str:
        return '{} pawn on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        def generate_advances():
            nonlocal move_limit
            _moves = set()
            move_limit = min(move_limit, max_moves[0][0])
            d = position_differences[0][0]
            for n in range(move_limit):
                if not self._board.is_square_empty(self._pos + ((n + 1) * d)):
                    break
                _moves.add((self._pos, self._pos + ((n + 1) * d)))
            return _moves

        def generate_diagonal_capturing_moves():
            _moves = set()
            for n in range(2):
                if max_moves[1][n] > 0 and self._board.opponent_piece_on_square(self._pos + position_differences[1][n],
                                                                                self._white_piece):
                    _moves.add((self._pos, self._pos + position_differences[1][n]))
            return _moves

        move_limit = 2 if (self._white_piece and self.rank == 1) or (not self._white_piece and self.rank == 6) else 1
        if self._white_piece:
            position_differences = [self._all_position_differences[2:3], self._all_position_differences[4:6]]
            max_moves = [self._max_moves[2:3], self._max_moves[4:6]]
        else:
            position_differences = [self._all_position_differences[3:4], self._all_position_differences[6:]]
            max_moves = [self._max_moves[3:4], self._max_moves[6:]]
        moves = generate_advances()
        moves |= generate_diagonal_capturing_moves()
        return moves


class Knight(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 1, board)

    def __repr__(self) -> str:
        return '{} knight on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        moves = set()
        for d, off_set in ([17, 10, -6, -15, -17, -10, 6, 15], [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1),
                                                                (-2, 1), (-1, 2)]):
            new_pos = self._pos + d
            # new pos is beyond board
            if new_pos // 8 > 7 or new_pos // 8 < 0 or new_pos % 8 > 7 or new_pos % 8 < 0:
                continue
            if not self._board.own_piece_on_square(self._pos + d, self._white_piece):
                moves.add((self._pos, self._pos + d))
        return moves


class Bishop(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 2, board)

    def __repr__(self) -> str:
        return '{} bishop on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves(self._all_position_differences[4:], self._max_moves[4:])


class Rook(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 3, board)

    def __repr__(self) -> str:
        return '{} rook on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves(self._all_position_differences[:4], self._max_moves[:4])


class Queen(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 4, board)

    def __repr__(self) -> str:
        return '{} queen on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves()


class King(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 5, board)

    def __repr__(self) -> str:
        return '{} king on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        moves = set()
        for d, m in zip(self._all_position_differences, self._max_moves):
            if m == 0:
                continue
            if self._board.own_piece_on_square(self._pos + d, self._white_piece):
                continue
            moves.add((self._pos, self._pos + d))
        return moves


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
