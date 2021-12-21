from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Set, TYPE_CHECKING, Optional, Union, Tuple, Dict
if TYPE_CHECKING:
    from board import Board, MOVE


"""
base and position values from:
https://www.chessprogramming.org/Simplified_Evaluation_Function
"""


class Piece(ABC):
    _all_diffs: List[int] = [1, -1, 8, -8, 9, 7, -7, -9]  # differences between the square values
    # order of the differences :right, left, up, down, right up, left up, right down, left down

    def __init__(self, pos: int, white_piece: bool, board: Board, symbol: str, fen_symbol: str) -> None:
        # piece info
        self._pos: int = pos
        self._white_piece: bool = white_piece
        self._symbol: str = symbol
        self._fen_symbol: str = fen_symbol
        self._capture_data: Union[None, Tuple[int, bool]] = None
        # objects
        self._board: Board = board

    def __repr__(self) -> str:
        """
        :return: {color} {type} {pos}
        """
        return f'{"w" if self._white_piece else "b"} {self._fen_symbol} {self._pos}'

    """
    abstract class attributes
    """
    @property
    @abstractmethod
    def _base_val(self) -> int:
        pass

    @property
    @abstractmethod
    def _pos_val_mod(self) -> int:
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
    @abstractmethod
    def pos_val(self) -> int:
        """
        get the position value of the piece
        :return: position value
        """
        pass

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

    @property
    def _max_moves(self) -> List[int]:
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
        self._capture_data = turn_number, white_to_move

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
    def attacking_squares(self) -> Set[int]:
        """
        generate all squares the piece threatens
        only considers moves that could threaten the king
        :return: set of all squares the piece threatens
        """
        return {move[1] for move in self.pseudo_legal_moves}

    def _generate_sliding_moves(self, diffs: Optional[List[int]] = None, max_moves: Optional[List[int]] = None) \
            -> Set[MOVE]:
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
            for new_pos in range(self._pos + diff, self._pos + ((m + 1) * diff), diff):
                # cannot move any further when blocked by own piece
                if self._board.own_piece_on_square(new_pos, self._white_piece):
                    break
                moves.add((self._pos, new_pos))
                # cannot move any further after capturing an opponents piece
                if self._board.opponent_piece_on_square(new_pos, self._white_piece):
                    break
        return moves


class Pawn(Piece):
    _base_val: int = 100
    _pos_val_mod: Dict[bool, Tuple[int]] = {True:  ( 0,  0,  0,  0,  0,  0,  0,  0,
                                                     5, 10, 10,-20,-20, 10, 10,  5,
                                                     5, -5,-10,  0,  0,-10, -5,  5,
                                                     0,  0,  0, 20, 20,  0,  0,  0,
                                                     5,  5, 10, 25, 25, 10,  5,  5,
                                                    10, 10, 20, 30, 30, 20, 10, 10,
                                                    50, 50, 50, 50, 50, 50, 50, 50,
                                                     0,  0,  0,  0,  0,  0,  0,  0),
                                            False: ( 0,  0,  0,  0,  0,  0,  0,  0,
                                                    50, 50, 50, 50, 50, 50, 50, 50,
                                                    10, 10, 20, 30, 30, 20, 10, 10,
                                                     5,  5, 10, 25, 25, 10,  5,  5,
                                                     0,  0,  0, 20, 20,  0,  0,  0,
                                                     5, -5,-10,  0,  0,-10, -5,  5,
                                                     5, 10, 10,-20,-20, 10, 10,  5,
                                                     0,  0,  0,  0,  0,  0,  0,  0)}

    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♟', 'P') if white_piece else ('♙', 'p')
        super().__init__(pos, white_piece, board, symbol, fen_symbol)
        self._promotion_data: Union[None, Tuple[int, bool]] = None

    """
    attribute getters
    """
    @property
    def promotion_data(self) -> Union[None, Tuple[int, bool]]:
        """
        get the promotion data
        :return: Tuple[promotion turn, color of active player while promotion]
        """
        return self._promotion_data

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

    @property
    def pos_val(self) -> int:
        return self._base_val + self._pos_val_mod[self._white_piece][self._pos]

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
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_advances() | self._generate_diagonal_capturing_moves() | self._generate_en_passant_move()

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self._generate_diagonal_capturing_moves()}

    def _generate_advances(self) -> Set[MOVE]:
        pos_limit = 2 if (self._white_piece and self._rank == 1) or (not self._white_piece and self._rank == 6) else 1
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

    def _generate_en_passant_move(self) -> Set[MOVE]:
        limits, diffs = self._limits[1], self._diffs[1]
        for n in range(2):
            if limits[n] > 0 and self._pos + diffs[n] == self._board.ep_target_square:
                return {(self._pos, self._pos + diffs[n])}
        return set()

    @property
    def _limits(self) -> List[List[int]]:
        return [self._max_moves[2:3], self._max_moves[4:6]] if self._white_piece else \
            [self._max_moves[3:4], self._max_moves[6:]]

    @property
    def _diffs(self) -> List[List[int]]:
        return [self._all_diffs[2:3], self._all_diffs[4:6]] if self._white_piece else \
            [self._all_diffs[3:4], self._all_diffs[6:]]


class Knight(Piece):
    _base_val: int = 320
    _pos_val_mod: Dict[bool, Tuple[int]] = {True: (-50,-40,-30,-30,-30,-30,-40,-50,
                                                   -40,-20,  0,  5,  5,  0,-20,-40,
                                                   -30,  5, 10, 15, 15, 10,  5,-30,
                                                   -30,  0, 15, 20, 20, 15,  0,-30,
                                                   -30,  5, 15, 20, 20, 15,  5,-30,
                                                   -30,  0, 10, 15, 15, 10,  0,-30,
                                                   -40,-20,  0,  0,  0,  0,-20,-40,
                                                   -50,-40,-30,-30,-30,-30,-40,-50),
                                            False: (-50,-40,-30,-30,-30,-30,-40,-50,
                                                    -40,-20,  0,  0,  0,  0,-20,-40,
                                                    -30,  0, 10, 15, 15, 10,  0,-30,
                                                    -30,  5, 15, 20, 20, 15,  5,-30,
                                                    -30,  0, 15, 20, 20, 15,  0,-30,
                                                    -30,  5, 10, 15, 15, 10,  5,-30,
                                                    -40,-20,  0,  5,  5,  0,-20,-40,
                                                    -50,-40,-30,-30,-30,-30,-40,-50)}

    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♞', 'N') if white_piece else ('♘', 'n')
        super().__init__(pos, white_piece, board, symbol, fen_symbol)

    """
    other getters
    """
    @property
    def pos_val(self) -> int:
        return self._base_val + self._pos_val_mod[self._white_piece][self._pos]

    """
    moves generation
    """

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
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


class Bishop(Piece):
    _base_val: int = 330
    _pos_val_mod: Dict[bool, Tuple[int]] = {True:  (-20,-10,-10,-10,-10,-10,-10,-20,
                                                    -10,  5,  0,  0,  0,  0,  5,-10,
                                                    -10, 10, 10, 10, 10, 10, 10,-10,
                                                    -10,  0, 10, 10, 10, 10,  0,-10,
                                                    -10,  5,  5, 10, 10,  5,  5,-10,
                                                    -10,  0,  5, 10, 10,  5,  0,-10,
                                                    -10,  0,  0,  0,  0,  0,  0,-10,
                                                    -20,-10,-10,-10,-10,-10,-10,-20),
                                            False: (-20,-10,-10,-10,-10,-10,-10,-20,
                                                    -10,  0,  0,  0,  0,  0,  0,-10,
                                                    -10,  0,  5, 10, 10,  5,  0,-10,
                                                    -10,  5,  5, 10, 10,  5,  5,-10,
                                                    -10,  0, 10, 10, 10, 10,  0,-10,
                                                    -10, 10, 10, 10, 10, 10, 10,-10,
                                                    -10,  5,  0,  0,  0,  0,  5,-10,
                                                    -20,-10,-10,-10,-10,-10,-10,-20)}

    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♝', 'B') if white_piece else ('♗', 'b')
        super().__init__(pos, white_piece, board, symbol, fen_symbol)

    """
    other getters
    """
    @property
    def pos_val(self) -> int:
        return self._base_val + self._pos_val_mod[self._white_piece][self._pos]

    """
    moves generation
    """
    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves(self._all_diffs[4:], self._max_moves[4:])


class Rook(Piece):
    _base_val: int = 500
    _pos_val_mod: Dict[bool, Tuple[int]] = {True:  ( 0,  0,  0,  5,  5,  0,  0,  0,
                                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                                     5, 10, 10, 10, 10, 10, 10,  5,
                                                     0,  0,  0,  0,  0,  0,  0,  0),
                                            False: ( 0,  0,  0,  0,  0,  0,  0,  0,
                                                     5, 10, 10, 10, 10, 10, 10,  5,
                                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                                     0,  0,  0,  5,  5,  0,  0,  0)}

    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♜', 'R') if white_piece else ('♖', 'r')
        super().__init__(pos, white_piece, board, symbol, fen_symbol)

    """
    other getters
    """
    @property
    def pos_val(self) -> int:
        return self._base_val + self._pos_val_mod[self._white_piece][self._pos]

    """
    moves generation
    """
    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves(self._all_diffs[:4], self._max_moves[:4])


class Queen(Piece):
    _base_val: int = 900
    _pos_val_mod: Dict[bool, Tuple[int]] = {True: (-20,-10,-10, -5, -5,-10,-10,-20,
                                                   -10,  0,  5,  0,  0,  0,  0,-10,
                                                   -10,  5,  5,  5,  5,  5,  0,-10,
                                                     0,  0,  5,  5,  5,  5,  0, -5,
                                                    -5,  0,  5,  5,  5,  5,  0, -5,
                                                   -10,  0,  5,  5,  5,  5,  0,-10,
                                                   -10,  0,  0,  0,  0,  0,  0,-10,
                                                   -20,-10,-10, -5, -5,-10,-10,-20),
                                            False: (-20,-10,-10, -5, -5,-10,-10,-20,
                                                    -10,  0,  0,  0,  0,  0,  0,-10,
                                                    -10,  0,  5,  5,  5,  5,  0,-10,
                                                     -5,  0,  5,  5,  5,  5,  0, -5,
                                                      0,  0,  5,  5,  5,  5,  0, -5,
                                                    -10,  5,  5,  5,  5,  5,  0,-10,
                                                    -10,  0,  5,  0,  0,  0,  0,-10,
                                                    -20,-10,-10, -5, -5,-10,-10,-20)}

    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♛', 'Q') if white_piece else ('♕', 'q')
        super().__init__(pos, white_piece, board, symbol, fen_symbol)

    """
    other getters
    """
    @property
    def pos_val(self) -> int:
        return self._base_val + self._pos_val_mod[self._white_piece][self._pos]

    """
    moves generation
    """
    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_sliding_moves()


class King(Piece):
    _base_val: int = 20_000
    _pos_val_mod: Dict[bool, Tuple[int]] = {True:  ( 20, 30, 10,  0,  0, 10, 30, 20,
                                                     20, 20,  0,  0,  0,  0, 20, 20,
                                                    -10,-20,-20,-20,-20,-20,-20,-10,
                                                    -20,-30,-30,-40,-40,-30,-30,-20,
                                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                                    -30,-40,-40,-50,-50,-40,-40,-30),
                                            False: (-30,-40,-40,-50,-50,-40,-40,-30,
                                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                                    -20,-30,-30,-40,-40,-30,-30,-20,
                                                    -10,-20,-20,-20,-20,-20,-20,-10,
                                                     20, 20,  0,  0,  0,  0, 20, 20,
                                                     20, 30, 10,  0,  0, 10, 30, 20)}

    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♚', 'K') if white_piece else ('♔', 'k')
        super().__init__(pos, white_piece, board, symbol, fen_symbol)

    """
    other getters
    """
    @property
    def pos_val(self) -> int:
        return self._base_val + self._pos_val_mod[self._white_piece][self._pos]

    """
    moves generation
    """
    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._generate_one_square_sliding_moves() | self._generate_castling_moves()

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self._generate_one_square_sliding_moves()}

    def _generate_one_square_sliding_moves(self) -> Set[MOVE]:
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
            if self._board.is_king_attacked(self._white_piece) or \
                    self._board.is_square_attacked(self._pos + dir_, self._white_piece):
                return set()
            return {(self._pos, self._pos + (2 * dir_))}

        return generate_castling_move_for_one_side(1, 0) | generate_castling_move_for_one_side(-1, 1)
