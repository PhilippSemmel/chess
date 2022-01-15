from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Iterator, List, Optional, Set, Tuple, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from board import Board, MOVE

"""
base and position values from:
https://www.chessprogramming.org/Simplified_Evaluation_Function
"""


class Piece(ABC):
    _POS_DIFFS: List[int] = [1, -1, 8, -8, 9, 7, -7, -9]
    _MAX_MOVES: Dict[int, Dict[int, int]]

    def __init__(self, pos: int, white_piece: bool, board: Board, symbol: str, fen_symbol: str) -> None:
        self._pos: int = pos
        self._white_piece: bool = white_piece
        self._symbol: str = symbol
        self._fen_symbol: str = fen_symbol
        self._capture_info: Union[None, Tuple[int, bool]] = None
        self._MAX_MOVES = self._get_max_moves()
        self._board: Board = board

    def _get_max_moves(self) -> Dict[int, Dict[int, int]]:
        """
        :return: Dict[position, Dict[direction, max moves in direction]]
        """
        return {
            i: {
                j: k for j, k in zip(
                    (1, -1, 8, -8, 9, -9, 7, -7),
                    self._get_max_moves_on_position(i))
                } for i in range(64)
        }

    @staticmethod
    def _get_max_moves_on_position(pos) -> List[int]:
        return [7 - (pos % 8), pos % 8, 7 - ( pos // 8), pos // 8, min(7 - (pos // 8), 7 - (pos % 8)),
                min(pos // 8, pos % 8), min(7 - (pos // 8), pos % 8), min(pos // 8,7 - (pos % 8))]

    def __repr__(self) -> str:
        return f'{"w" if self._white_piece else "b"} {self._fen_symbol} {self._pos}'

    """
    abstract class attributes
    """

    @property
    @abstractmethod
    def _BASE_VAL(self) -> int:
        pass

    @property
    @abstractmethod
    def _POS_VAL_MOD(self) -> Dict[bool, List[int]]:
        pass

    """
    attribute getters
    """

    @property
    def pos(self) -> int:
        return self._pos

    @property
    def white_piece(self) -> bool:
        """
        :return: whether the piece is white
        """
        return self._white_piece

    @property
    def symbol(self) -> str:
        """
        :return: symbol for console representation
        """
        return self._symbol

    @property
    def fen_symbol(self) -> str:
        return self._fen_symbol

    @property
    def capture_info(self) -> Union[None, Tuple[int, bool]]:
        """
        :return: Tuple[turn number, white to move]
        """
        return self._capture_info

    """
    other getters
    """

    @property
    def on_board(self) -> bool:
        return self._capture_info is None

    @property
    def pos_val(self) -> int:
        """
        :return: value of the piece on its position
        """
        return self._BASE_VAL + self._POS_VAL_MOD[self._white_piece][self._pos]

    @property
    def rank(self) -> int:
        return self._pos // 8

    @property
    def file(self) -> int:
        return self._pos % 8

    """
    attribute setters
    """

    def move_to(self, new_pos: int) -> None:
        self._pos = new_pos

    def capture(self, turn_number: int, white_to_move: bool) -> None:
        """
        set the piece data to Tuple[turn_number, white_to_move]
        :param turn_number: turn number when the capture occurred
        :param white_to_move: color to move when to capture occurred
        """
        self._capture_info = turn_number, white_to_move

    def uncapture(self) -> None:
        """
        set the capture info to None
        """
        self._capture_info = None

    """
    move generation
    """

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._get_sliding_moves()

    @property
    def attacking_squares(self) -> Set[int]:
        """
        only considers moves that could threaten the opponents king
        """
        return {move[1] for move in self.pseudo_legal_moves}

    def _get_sliding_moves(self) -> Set[MOVE]:
        moves = set()
        for diff in self._POS_DIFFS:
            self._add_direction_moves(moves, diff)
        return moves

    def _add_direction_moves(self, moves_set: Set[MOVE], diff: int) -> None:
        for new_pos in self._possible_new_positions(diff):
            if self._board.own_piece_on_square(new_pos, self._white_piece):
                return
            self._add_move(moves_set, new_pos)
            if self._board.opponent_piece_on_square(new_pos, self._white_piece):
                return

    def _possible_new_positions(self, diff: int, limit: Optional[int] = 7) -> Iterator[int]:
        """
        generates all possible new positions for a direction
        :param diff: square index difference of direction
        :param limit: maximum moves in direction
        """
        return range(self._pos + diff, self._pos + ((min(self._MAX_MOVES[self._pos][diff], limit) + 1) * diff), diff)

    def _add_move(self, moves_set: Set[MOVE], new_pos: int, promotion_type: Optional[str] = None) -> None:
        moves_set.add((self._pos, new_pos, promotion_type))

    def _moves_in_direction_available(self, diff: int) -> bool:
        return self._MAX_MOVES[self._pos][diff] > 0


class Pawn(Piece):
    _BASE_VAL: int = 100
    _POS_VAL_MOD: Dict[bool, Tuple[int]] = {True:  ( 0,  0,  0,  0,  0,  0,  0,  0,
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
    _POS_DIFFS: List[int]
    _MAX_MOVES: Dict[int, Dict[int, int]]

    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♟', 'P') if white_piece else ('♙', 'p')
        super().__init__(pos, white_piece, board, symbol, fen_symbol)
        self._POS_DIFFS = self._get_pos_diffs()
        self._MAX_MOVES = self._get_max_moves()
        self._promotion_data: Union[None, Tuple[int, bool]] = None

    def _get_pos_diffs(self):
        return [8, 9, 7] if self._white_piece else [-8, -9, -7]

    def _get_max_moves(self):
        return {
            i: {
                j: k for j, k in zip(
                    self._POS_DIFFS,
                    self._get_max_moves_on_pos(i))
                } for i in range(64)
        }

    def _get_max_moves_on_pos(self, pos) -> List[int]:
        return [7 - (pos // 8), min(7 - (pos // 8), 7 - (pos % 8)), min(7 - (pos // 8), pos % 8)] if self._white_piece \
            else [pos // 8, min(pos // 8, pos % 8), min(pos // 8, 7 - (pos % 8))]

    """
    attribute getters
    """

    @property
    def promotion_data(self) -> Union[None, Tuple[int, bool]]:
        """
        :return: Tuple[turn number, white to move]
        """
        return self._promotion_data

    """
    other getters
    """

    @property
    def on_board(self) -> bool:
        return self._capture_info is None and self._promotion_data is None

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
        return self._get_advances() | self._get_diagonal_capturing_moves() | self._get_en_passant_move()

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self._get_diagonal_capturing_moves()}

    def _get_advances(self) -> Set[MOVE]:
        moves = set()
        move_limit = self._get_move_limit()
        diff = self._POS_DIFFS[0]
        self._add_advance_moves(moves, diff, move_limit)
        return moves

    def _get_diagonal_capturing_moves(self) -> Set[MOVE]:
        moves = set()
        for diff in self._POS_DIFFS[1:]:
            self._add_diagonal_capture_move(moves, diff)
        return moves

    def _get_en_passant_move(self) -> Set[MOVE]:
        move = set()
        for diff in self._POS_DIFFS[1:]:
            self._add_en_passant_move(move, diff)
        return move

    def _add_advance_moves(self, moves_set: Set[MOVE], diff: int, move_limit: int) -> None:
        for new_pos in self._possible_new_positions(diff, move_limit):
            if not self._board.is_square_empty(new_pos):
                return
            self._add_move(moves_set, new_pos)

    def _add_diagonal_capture_move(self, moves_set: Set[MOVE], diff) -> None:
        new_pos = self._pos + diff
        if not self._moves_in_direction_available(diff):
            return
        if self._board.opponent_piece_on_square(new_pos, self._white_piece):
            self._add_move(moves_set, new_pos)

    def _add_en_passant_move(self, moves_set, diff) -> None:
        new_pos = self._pos + diff
        if self._moves_in_direction_available(diff) and self._is_en_passant_move(new_pos):
            self._add_move(moves_set, new_pos)

    def _add_move(self, moves_set: Set[MOVE], new_pos: int, promotion_type: Optional[str] = None) -> None:
        if self._is_promotion_move(new_pos):
            self._add_promotion_moves(moves_set, new_pos)
            return
        super()._add_move(moves_set, new_pos)

    @staticmethod
    def _is_promotion_move(new_pos: int) -> bool:
        return (new_pos // 8) == 0 or (new_pos // 8) == 7

    def _add_promotion_moves(self, moves_set: Set[MOVE], new_pos) -> None:
        for type_ in self._get_promotion_types():
            super()._add_move(moves_set, new_pos, type_)

    def _get_promotion_types(self) -> str:
        return 'QRBN' if self._white_piece else 'qrbn'

    def _get_move_limit(self) -> int:
        return 2 if self._on_starting_position() else 1

    def _on_starting_position(self) -> bool:
        return (self._white_piece and self.rank == 1) or (not self._white_piece and self.rank == 6)

    def _is_en_passant_move(self, new_pos: int) -> bool:
        return new_pos == self._board.ep_target_square


class Knight(Piece):
    _BASE_VAL: int = 320
    _POS_VAL_MOD: Dict[bool, Tuple[int]] = {True: (-50,-40,-30,-30,-30,-30,-40,-50,
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
    _POS_DIFFS: List[int] = [17, 10, -6, -15, -17, -10, 6, 15]
    _JUMP_OFFSETS: Dict[int, Tuple[int, int]] = {17: (1, 2), 10: (2, 1), -6: (2, -1), -15: (1, -2), -17: (-1, -2),
                                                 -10: (-2, -1), 6: (-2, 1), 15: (-1, 2)}

    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♞', 'N') if white_piece else ('♘', 'n')
        super().__init__(pos, white_piece, board, symbol, fen_symbol)

    """
    moves generation
    """

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        moves = set()
        for diff in self._POS_DIFFS:
            self._add_direction_moves(moves, diff)
        return moves

    def _add_direction_moves(self, moves_set: Set[MOVE], diff: int) -> None:
        if self._moves_in_direction_available(diff):
            return
        new_pos = self._pos + diff
        if not self._board.own_piece_on_square(new_pos, self._white_piece):
            self._add_move(moves_set, new_pos)

    def _moves_in_direction_available(self, diff: int) -> bool:
        offset = self._JUMP_OFFSETS[diff]
        return self.file + offset[0] > 7 or self.file + offset[0] < 0 or self.rank + offset[1] > 7 or \
               self.rank + offset[1] < 0


class Bishop(Piece):
    _BASE_VAL: int = 330
    _POS_VAL_MOD: Dict[bool, Tuple[int]] = {True:  (-20,-10,-10,-10,-10,-10,-10,-20,
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
    _POS_DIFFS: List[int] = [9, -9, 7, -7]

    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♝', 'B') if white_piece else ('♗', 'b')
        super().__init__(pos, white_piece, board, symbol, fen_symbol)


class Rook(Piece):
    _BASE_VAL: int = 500
    _POS_VAL_MOD: Dict[bool, Tuple[int]] = {True:  ( 0,  0,  0,  5,  5,  0,  0,  0,
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
    _POS_DIFFS: List[int] = [1, -1, 8, -8]

    def __init__(self, pos: int, white_piece: bool, board: Board) -> None:
        symbol, fen_symbol = ('♜', 'R') if white_piece else ('♖', 'r')
        super().__init__(pos, white_piece, board, symbol, fen_symbol)


class Queen(Piece):
    _BASE_VAL: int = 900
    _POS_VAL_MOD: Dict[bool, Tuple[int]] = {True: (-20,-10,-10, -5, -5,-10,-10,-20,
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


class King(Piece):
    _BASE_VAL: int = 20_000
    _POS_VAL_MOD: Dict[bool, Tuple[int]] = {True:  ( 20, 30, 10,  0,  0, 10, 30, 20,
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
    moves generation
    """

    @property
    def pseudo_legal_moves(self) -> Set[MOVE]:
        return self._get_one_square_sliding_moves() | self._get_castling_moves()

    @property
    def attacking_squares(self) -> Set[int]:
        return {move[1] for move in self._get_one_square_sliding_moves()}

    def _get_one_square_sliding_moves(self) -> Set[MOVE]:
        moves = set()
        for diff in self._POS_DIFFS:
            self._add_direction_moves(moves, diff)
        return moves

    def _get_castling_moves(self) -> Set[MOVE]:
        moves = set()
        for n_move, pos_mod in enumerate((1, -1)):
            if self._castling_move_available(pos_mod, n_move):
                self._add_move(moves, self._pos + (2 * pos_mod), None)
        return moves

    def _add_direction_moves(self, moves_set: Set[MOVE], diff: int) -> None:
        if not self._moves_in_direction_available(diff):
            return
        new_pos = self._pos + diff
        if not self._board.own_piece_on_square(new_pos, self._white_piece):
            self._add_move(moves_set, new_pos)

    def _castling_move_available(self, pos_mod: int, n_move: int) -> bool:
        if not self._castling_rights_given(n_move):
            return False
        if not self._square_between_rook_and_king_empty(pos_mod, n_move):
            return False
        if self._king_threatened_one_own_square_or_square_to_move_over(pos_mod):
            return False
        return True

    def _castling_rights_given(self, n_move) -> bool:
        return self._board.castling_rights[n_move if self._white_piece else n_move + 2]

    def _square_between_rook_and_king_empty(self, pos_mod: int, n_move: int) -> bool:
        for square in range(self._pos + pos_mod, self._pos + ((3 + n_move) * pos_mod), pos_mod):
            if not self._board.is_square_empty(square):
                return False
        return True

    def _king_threatened_one_own_square_or_square_to_move_over(self, pos_mod: int):
        return self._board.is_king_attacked(self._white_piece) or \
                self._board.is_square_attacked(self._pos + pos_mod, self._white_piece)

