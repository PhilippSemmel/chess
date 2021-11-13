from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Set, TYPE_CHECKING
if TYPE_CHECKING:
    from board import Board, MOVE


class Piece(ABC):
    def __init__(self, pos: int, white_piece: bool, _type: int, board: Board) -> None:
        self._verify_params(pos, white_piece, _type, board)
        # piece info
        self._pos: int = pos
        self._white_piece: bool = white_piece
        self._type: int = _type
        """
        0 -> Pawn
        1 -> Knight
        2 -> Bishop
        3 -> Rook
        4 -> Queen
        5 -> King
        """
        # objects
        self._board: Board = board
        # misc data
        # differences between the square values
        # order of the differences :right, left, up, down, right up, left up, right down, left down
        self._all_diffs: List[int] = [1, -1, 8, -8, 9, 7, -7, -9]

    @staticmethod
    def _verify_params(pos: int, white_piece: bool, _type: int, board: Board) -> None:
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
        # if not isinstance(board, Board):
        #     raise ValueError('No board object as board attribute.')

    @abstractmethod
    def __repr__(self) -> str:
        """
        :return: {color} {type} on pos {pos}
        """
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
    def white_piece(self) -> bool:
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

    # @lru_cache(max_size=64)
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
        generate all long range sliding moves of a piece
        :param position_differences: the square index value differences of every direction the piece can move to
        :param max_moves: list of squares in every direction the piece can move to
        :return: all long range sliding moves of a piece
        """
        if not position_differences:
            position_differences = self._all_diffs
        if not max_moves:
            max_moves = self._max_moves
        moves = set()

        for diff, m in zip(position_differences, max_moves):
            for n, new_pos in enumerate(range(self._pos + diff, self._pos + ((m + 1) * diff), diff)):
                # cannot move any further when blocked by own piece
                if self._board.own_piece_on_square(new_pos, self._white_piece):
                    break
                moves.add((self._pos, new_pos))
                # cannot move any further after capturing a opponents piece
                if self._board.opponent_piece_on_square(new_pos, self._white_piece):
                    break
        return moves

    @property
    @abstractmethod
    def attacking_squares(self) -> Set[int]:
        """
        generate all squares the piece threatens
        only considers moves that could threaten the king
        :return: set of all squares the piece threatens
        """
        pass


class Pawn(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 0, board)

    def __repr__(self) -> str:
        return '{} pawn on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def _limits(self) -> List[List[int]]:
        return [self._max_moves[2:3], self._max_moves[4:6]] if self._white_piece else \
            [self._max_moves[3:4], self._max_moves[6:]]

    @property
    def _diffs(self):
        return [self._all_diffs[2:3], self._all_diffs[4:6]] if self._white_piece else \
            [self._all_diffs[3:4], self._all_diffs[6:]]

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        moves = self._generate_advances()
        moves |= self._generate_diagonal_capturing_moves()
        return moves

    def _generate_advances(self) -> Set[MOVE]:
        pos_limit = 2 if (self._white_piece and self.rank == 1) or (not self._white_piece and self.rank == 6) else 1
        limits, diffs = min(pos_limit, self._limits[0][0]), self._diffs[0][0]
        _moves = set()
        for n in range(limits):
            if not self._board.is_square_empty(self._pos + ((n + 1) * diffs)):
                break
            _moves.add((self._pos, self._pos + ((n + 1) * diffs)))
        return _moves

    def _generate_diagonal_capturing_moves(self) -> Set[MOVE]:
        limits, diffs = self._limits[1], self._diffs[1]
        _moves = set()
        for n in range(2):
            if limits[n] > 0 and self._board.opponent_piece_on_square(self._pos + diffs[n], self._white_piece):
                _moves.add((self._pos, self._pos + diffs[n]))
        return _moves

    # def _generate_en_passant_move(self) -> Set[MOVE]:
    #     if
    #     return {(34, 41)}

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self._generate_diagonal_capturing_moves()}


class Knight(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 1, board)

    def __repr__(self) -> str:
        return '{} knight on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        moves = set()
        for diff, off_set in zip([17, 10, -6, -15, -17, -10, 6, 15], [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2),
                                                                      (-2, -1), (-2, 1), (-1, 2)]):
            new_pos = self._pos + diff
            # new pos is beyond board
            if self.file + off_set[0] > 7 or self.file + off_set[0] < 0 or self.rank + off_set[1] > 7 or \
                    self.rank + off_set[1] < 0:
                continue
            if not self._board.own_piece_on_square(new_pos, self._white_piece):
                moves.add((self._pos, new_pos))
        return moves

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self.pseudo_legal_moves}


class Bishop(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 2, board)

    def __repr__(self) -> str:
        return '{} bishop on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves(self._all_diffs[4:], self._max_moves[4:])

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self.pseudo_legal_moves}


class Rook(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 3, board)

    def __repr__(self) -> str:
        return '{} rook on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves(self._all_diffs[:4], self._max_moves[:4])

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self.pseudo_legal_moves}


class Queen(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 4, board)

    def __repr__(self) -> str:
        return '{} queen on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves()

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self.pseudo_legal_moves}


class King(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        super().__init__(pos, white_piece, 5, board)

    def __repr__(self) -> str:
        return '{} king on pos {}'.format('white' if self._white_piece else 'black', self._pos)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        moves = self._generate_on_square_sliding_moves()
        moves |= self._generate_castling_moves()
        return moves

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self._generate_on_square_sliding_moves()}

    def _generate_on_square_sliding_moves(self) -> Set[MOVE]:
        moves = set()
        for diff, m in zip(self._all_diffs, self._max_moves):
            if m == 0:
                continue
            if self._board.own_piece_on_square(self._pos + diff, self._white_piece):
                continue
            moves.add((self._pos, self._pos + diff))
        return moves

    def _generate_castling_moves(self) -> Set[MOVE]:
        def generate_castling_move_for_one_side(dir_: int, n: int) -> Set[MOVE]:
            # testing castling right
            if not self._board.castling_rights[n if self._white_piece else n + 2]:
                return set()
            # test if squares in between king and rook are empty
            for pos in range(self._pos + dir_, self._pos + ((3 + n) * dir_), dir_):
                if not self._board.is_square_empty(pos):
                    return set()
            # test if king in checking or squares the king moves over is threatened
            if self._board.is_square_attacked(self._pos, self._white_piece) or \
                    self._board.is_square_attacked(self._pos + dir_, self._white_piece):
                return set()
            return {(self._pos, self._pos + (2 * dir_))}

        moves = generate_castling_move_for_one_side(1, 0)
        moves |= generate_castling_move_for_one_side(-1, 1)
        return moves
