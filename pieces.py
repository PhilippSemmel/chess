from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Set, TYPE_CHECKING, Optional, Union, Tuple
if TYPE_CHECKING:
    from board import Board, MOVE


class Piece(ABC):
    def __init__(self, pos: int, white_piece: bool, _type: int, board: Board, symbol: str, fen_symbol: str) -> None:
        self._verify_params(pos, _type)
        # piece info
        self._pos: int = pos
        self._white_piece: bool = white_piece
        self._type: int = _type  # 0: Pawn, 1: Knight, 2: Bishop, 3: Rook, 4: Queen, 5: King
        self._symbol: str = symbol
        self._fen_symbol: str = fen_symbol
        self._capture_data: Union[None, Tuple[int, bool]] = None
        # objects
        self._board: Board = board
        # misc data
        self._all_diffs: List[int] = [1, -1, 8, -8, 9, 7, -7, -9]  # differences between the square values
        # order of the differences :right, left, up, down, right up, left up, right down, left down

    def __repr__(self) -> str:
        """
        :return: {color} {type} {pos}
        """
        return f'{"w" if self._white_piece else "b"} {self._fen_symbol} {self._pos}'

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

    @property
    def symbol(self) -> str:
        """
        get the symbol of the piece
        :return: symbol of the piece
        """
        return self._symbol

    @property
    def fen_symbol(self) -> str:
        """
        get the fen symbol of the piece
        :return: fen symbol of the piece
        """
        return self._fen_symbol

    @property
    def capture_data(self) -> Union[None, Tuple[int, bool]]:
        """
        data about the capture of the piece
        :return: Tuple[capture turn, color of active player while capture]
        """
        return self._capture_data

    """
    other getters
    """
    @property
    def on_board(self) -> bool:
        """
        test whether the piece is on the board
        :return: whether the piece is on the board
        """
        return self._capture_data is None

    @property
    def _rank(self) -> int:
        """
        get the rank the piece stands on
        :return: the rank the piece stands on
        """
        return self._pos // 8

    @property
    def _file(self) -> int:
        """
        get the file the piece stands on
        :return: the file the piece stands on
        """
        return self._pos % 8

    # @lru_cache(max_size=64)
    @property
    def _max_moves(self) -> List[int]:  # comments for algorithm
        """
        get the number of squares in each direction starting from the pieces position
        :return:list of numbers of squares in each direction starting from the pieces position
        """
        r = self._rank
        f = self._file
        right = 7 - f
        left = f
        up = 7 - r
        down = r
        return [right, left, up, down, min(right, up), min(left, up), min(right, down), min(left, down)]

    """
    attribute setters
    """
    def move_to(self, new_pos: int) -> None:
        """
        set a new position for the piece
        :param new_pos: new position of the piece
        """
        if new_pos > 63 or new_pos < 0:
            raise ValueError('Position value must be between 0 and 63.')
        if not type(new_pos) == int:
            raise TypeError('Position value must be an int.')
        self._pos = new_pos

    def capture(self, turn_number: int, white_to_move: bool) -> None:
        """
        set the piece data to Tuple[turn_number, white_to_move]
        :param turn_number: turn number when the capture occurred
        :param white_to_move: color to move when to capture occurred
        """
        self._capture_data = (turn_number, white_to_move)

    def uncapture(self) -> None:
        """
        set the capture data to None
        """
        self._capture_data = None

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

    @property
    @abstractmethod
    def attacking_squares(self) -> Set[int]:
        """
        generate all squares the piece threatens
        only considers moves that could threaten the king
        :return: set of all squares the piece threatens
        """
        pass

    def _generate_sliding_moves(self, diffs: Optional[List[int]] = None, max_moves: Optional[List[int]] = None) \
            -> Set[MOVE]:  # comments for algorithm
        """
        generate all long range sliding moves of a piece
        :param diffs: the square index value differences of every direction the piece can move to
        :param max_moves: list of squares in every direction the piece can move to
        :return: all long range sliding moves of a piece
        """
        if not diffs:
            diffs = self._all_diffs
        if not max_moves:
            max_moves = self._max_moves
        moves = set()

        for diff, m in zip(diffs, max_moves):
            for n, new_pos in enumerate(range(self._pos + diff, self._pos + ((m + 1) * diff), diff)):
                # cannot move any further when blocked by own piece
                if self._board.own_piece_on_square(new_pos, self._white_piece):
                    break
                moves.add((self._pos, new_pos))
                # cannot move any further after capturing an opponents piece
                if self._board.opponent_piece_on_square(new_pos, self._white_piece):
                    break
        return moves

    """
    misc
    """
    @staticmethod
    def _verify_params(pos: int, _type: int) -> None:
        """
        verify the validity of the values passed to the constructor
        :param pos: pos value of the piece
        :param _type: type value of the piece
        :raises TypeError if any value has a wrong type
        :raises ValueError if the pos or type value is wrong
        """
        if pos > 63 or pos < 0:
            raise ValueError('The position reach from value 0 to value 63 only.')
        if _type > 5 or _type < 0:
            raise ValueError('The type codes reach from 0 to 5 only.')


class Pawn(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♟', 'P') if white_piece else ('♙', 'p')
        super().__init__(pos, white_piece, 0, board, symbol, fen_symbol)
        self._promotion_data: Union[None, Tuple[int, bool]] = None

    """
    other getters
    """
    @property
    def on_board(self) -> bool:
        """
        test whether the piece is on the board
        :return: whether the piece is on the board
        """
        return self._capture_data is None and self._promotion_data is None

    """
    attribute setters
    """
    def promote(self, turn_number: int, white_to_move: bool) -> None:
        """
        set the promotion data to Tuple[turn_number, white_to_move]
        :param turn_number: turn number when the promotion occurred
        :param white_to_move: color to move when to promotion occurred
        """
        self._promotion_data = (turn_number, white_to_move)

    def unpromote(self) -> None:
        """
        set the promotion data to None
        """
        self._promotion_data = None

    """
    move generation
    """
    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:  # comments for algorithm
        moves = self._generate_advances()
        moves |= self._generate_diagonal_capturing_moves()
        moves |= self._generate_en_passant_move()
        return moves

    @property
    def attacking_squares(self) -> Set[int]:  # comments for algorithm
        return {move[1] for move in self._generate_diagonal_capturing_moves()}

    def _generate_advances(self) -> Set[MOVE]:  # comments for algorithm
        pos_limit = 2 if (self._white_piece and self._rank == 1) or (not self._white_piece and self._rank == 6) else 1
        limits, diffs = min(pos_limit, self._limits[0][0]), self._diffs[0][0]
        _moves = set()
        for n in range(limits):
            if not self._board.is_square_empty(self._pos + ((n + 1) * diffs)):
                break
            _moves.add((self._pos, self._pos + ((n + 1) * diffs)))
        return _moves

    def _generate_diagonal_capturing_moves(self) -> Set[MOVE]:  # comments for algorithm
        limits, diffs = self._limits[1], self._diffs[1]
        _moves = set()
        for n in range(2):
            if limits[n] > 0 and self._board.opponent_piece_on_square(self._pos + diffs[n], self._white_piece):
                _moves.add((self._pos, self._pos + diffs[n]))
        return _moves

    def _generate_en_passant_move(self) -> Set[MOVE]:  # comments for algorithm
        limits, diffs = self._limits[1], self._diffs[1]
        for n in range(2):
            if limits[n] > 0 and self._pos + diffs[n] == self._board.ep_target_square:
                return {(self._pos, self._pos + diffs[n])}
        return set()

    @property
    def _limits(self) -> List[List[int]]:  # comments for algorithm
        return [self._max_moves[2:3], self._max_moves[4:6]] if self._white_piece else \
            [self._max_moves[3:4], self._max_moves[6:]]

    @property
    def _diffs(self) -> List[List[int]]:  # comments for algorithm
        return [self._all_diffs[2:3], self._all_diffs[4:6]] if self._white_piece else \
            [self._all_diffs[3:4], self._all_diffs[6:]]


class Knight(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♞', 'N') if white_piece else ('♘', 'n')
        super().__init__(pos, white_piece, 1, board, symbol, fen_symbol)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:  # comments for algorithm
        moves = set()
        for diff, off_set in zip([17, 10, -6, -15, -17, -10, 6, 15], [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2),
                                                                      (-2, -1), (-2, 1), (-1, 2)]):
            new_pos = self._pos + diff
            # new pos is beyond board
            if self._file + off_set[0] > 7 or self._file + off_set[0] < 0 or self._rank + off_set[1] > 7 or \
                    self._rank + off_set[1] < 0:
                continue
            if not self._board.own_piece_on_square(new_pos, self._white_piece):
                moves.add((self._pos, new_pos))
        return moves

    @property
    def attacking_squares(self) -> Set[int]:  # comments for algorithm
        return {move[1] for move in self.pseudo_legal_moves}


class Bishop(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♝', 'B') if white_piece else ('♗', 'b')
        super().__init__(pos, white_piece, 2, board, symbol, fen_symbol)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves(self._all_diffs[4:], self._max_moves[4:])

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self.pseudo_legal_moves}


class Rook(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♜', 'R') if white_piece else ('♖', 'r')
        super().__init__(pos, white_piece, 3, board, symbol, fen_symbol)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves(self._all_diffs[:4], self._max_moves[:4])

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self.pseudo_legal_moves}


class Queen(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♛', 'Q') if white_piece else ('♕', 'q')
        super().__init__(pos, white_piece, 4, board, symbol, fen_symbol)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves()

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self.pseudo_legal_moves}


class King(Piece):
    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♚', 'K') if white_piece else ('♔', 'k')
        super().__init__(pos, white_piece, 5, board, symbol, fen_symbol)

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        moves = self._generate_one_square_sliding_moves()
        moves |= self._generate_castling_moves()
        return moves

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self._generate_one_square_sliding_moves()}

    def _generate_one_square_sliding_moves(self) -> Set[MOVE]:  # comments for algorithm
        moves = set()
        for diff, m in zip(self._all_diffs, self._max_moves):
            if m == 0:
                continue
            if self._board.own_piece_on_square(self._pos + diff, self._white_piece):
                continue
            moves.add((self._pos, self._pos + diff))
        return moves

    def _generate_castling_moves(self) -> Set[MOVE]:  # comments for algorithm
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
