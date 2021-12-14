from __future__ import annotations

import cProfile
import contextlib
from pieces import Piece, Pawn, Knight, Bishop, Rook, Queen, King
from typing import Tuple, Optional, Union, Set, List, TYPE_CHECKING
from functools import *
if TYPE_CHECKING:
    from chess import MOVE


class Board:
    def __init__(self, fen: Optional[str] = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1') -> None:
        self._pieces: Set[Piece]
        self._white_to_move: bool
        self._castling_rights: List[bool]
        self._ep_target_square: Union[None, int]
        self._half_move_clock: int
        self._turn_number: int
        self._load_position(fen)
        # self._active_pieces = self._get_active_pieces()
        self._data: List[Tuple[bool, List[bool], Union[None, int], int, int]] = []
        self._moves: List[MOVE] = []
        self._legal_moves: Set[MOVE] = self._get_legal_moves()

    def __repr__(self) -> str:
        def positions_to_str() -> str:
            output = ''
            for row in range(7, -1, -1):
                output += ' ' + str(row + 1) + ' '
                for file in range(8):
                    try:
                        output += ' ' + self._get_piece((row * 8) + file).symbol + ' '
                    except ValueError:
                        output += ' - '
                output += ' ' + str(row + 1) + ' \n'
            return output

        return f'    a  b  c  d  e  f  g  h\n{positions_to_str()}    a  b  c  d  e  f  g  h\n\n> color to move: ' \
               f'{self._color_to_move_to_fen()}\n> castling rights: {self._castling_rights_to_fen()}\n> ep target: ' \
               f'{self._ep_target_square_to_fen()}\n> half move clock: {self._half_move_clock_to_fen()}\n> turn: ' \
               f'{self._turn_number_to_fen()}\n'

    """
    attribute getters
    """
    @property
    def pieces(self) -> Set[Piece]:
        """
        get the pieces_tests on the board
        :return: a set with all pieces_tests on the board
        """
        return self._pieces

    @property
    def white_to_move(self) -> bool:
        """
        get the player_tests to move
        :return: whether white to move
        """
        return self._white_to_move

    @property
    def castling_rights(self) -> List[bool]:
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

    @property
    def legal_moves(self) -> Set[MOVE]:
        """
        get the legal moves
        :return: legal moves
        """
        return self._legal_moves

    """
    other getters
    """
    @property
    def _get_active_pieces(self) -> Set[Piece]:
        """
        get all pieces_tests that are on the board and active
        :return: set of all active pieces_tests
        """
        return {piece for piece in self._pieces if piece.on_board}

    @property
    def checkmate(self) -> bool:
        """
        test whether the current board constellation is checkmate
        :return: whether its checkmate
        """
        return len(self._legal_moves) == 0 and \
               self.is_square_attacked(self._get_king(self._white_to_move).pos, self._white_to_move)

    @property
    def stalemate(self) -> bool:
        """
        test whether the current board constellation is stalemate
        :return: whether its stalemate
        """
        return len(self._legal_moves) == 0 and \
               not self.is_square_attacked(self._get_king(self._white_to_move).pos, self._white_to_move)

    @property
    def val(self) -> int:
        return 0

    """
    legal moves
    """
    def _get_legal_moves(self) -> Set[MOVE]:
        """
        generate all legal moves
        :return: set of all legal moves
        """
        moves = set()
        king = self._get_king(self._white_to_move)
        for piece in self._get_active_pieces:
            if not piece.white_piece == self._white_to_move:
                continue
            for move in piece.pseudo_legal_moves:
                with self._test_move(move):
                    if not self.is_square_attacked(king.pos, king.white_piece):
                        moves.add(move)
        return moves

    @contextlib.contextmanager
    def _test_move(self, move: MOVE):
        self.make_move(move)
        try:
            yield
        finally:
            self._undo_move()

    """
    make move
    """
    def make_move(self, move: MOVE) -> None:
        """
        make a given move
        :param move: the move to make
        """
        moving_piece = self._get_piece(move[0])
        self._log_data()
        self._log_move(move)
        self._adjust_half_move_clock(moving_piece, move)
        self._move_pieces(moving_piece, move)
        self._adjust_castling_rights()
        self._set_en_passant_target_square(moving_piece, move)
        self._increase_turn_number()
        self._alternate_color_to_move()
        self.is_square_empty.cache_clear()

    def _adjust_half_move_clock(self, moving_piece: Piece, move: MOVE) -> None:
        """
        adjust the half move clock according to the move
        :param moving_piece: piece to move
        :param move: move to make
        """
        if type(moving_piece) == Pawn or not self.is_square_empty(move[1]):  # pawn move or capture move
            self._half_move_clock = 0
        else:
            self._half_move_clock += 1

    def _move_pieces(self, moving_piece: Piece, move: MOVE) -> None:
        """
        move all pieces_tests according the move
        :param moving_piece: piece to move
        :param move: move to make
        """
        def capture_piece() -> None:
            with contextlib.suppress(ValueError):
                self._get_piece(move[1]).capture(self._turn_number, self._white_to_move)

        def move_castling_rook() -> None:
            if type(moving_piece) == King and abs(move[0] - move[1]) == 2:
                # castles queenside
                if (move[0] - move[1]) == abs(move[0] - move[1]):
                    # move queenside rook
                    self._get_piece(move[0] - 4).move_to(move[1] + 1)
                # castles kingside
                else:
                    # move queenside rook
                    self._get_piece(move[0] + 3).move_to(move[1] - 1)

        def capture_pawn_en_passant() -> None:
            if move[1] == self._ep_target_square and type(moving_piece) == Pawn:
                # remove piece from piece set
                self._get_piece(move[0] - ((move[0] % 8) - (move[1] % 8))).capture(self._turn_number,
                                                                                   self._white_to_move)

        def move_piece() -> None:
            moving_piece.move_to(move[1])

        def promote_pawn() -> None:
            nonlocal moving_piece
            if type(moving_piece) == Pawn and (move[1] // 8 == 7 or move[1] // 8 == 0):
                moving_piece.promote(self._turn_number, self._white_to_move)
                self._pieces.add(self._create_piece(moving_piece.pos, 'Q' if moving_piece.white_piece else 'q'))

        capture_piece()
        move_castling_rook()
        capture_pawn_en_passant()
        move_piece()
        promote_pawn()

    def _adjust_castling_rights(self) -> None:
        """
        adjust the castling rights according to the move
        """
        if self.is_square_empty(4) or not (type(self._get_piece(4)) == King and self._get_piece(4).white_piece):
            self._castling_rights[0] = False
            self._castling_rights[1] = False
        if self.is_square_empty(7) or not (type(self._get_piece(7)) == Rook and self._get_piece(7).white_piece):
            self._castling_rights[0] = False
        if self.is_square_empty(0) or not (type(self._get_piece(0)) == Rook and self._get_piece(0).white_piece):
            self._castling_rights[1] = False
        if self.is_square_empty(60) or not (type(self._get_piece(60)) == King and not self._get_piece(60).white_piece):
            self._castling_rights[2] = False
            self._castling_rights[3] = False
        if self.is_square_empty(63) or not (type(self._get_piece(63)) == Rook and not self._get_piece(63).white_piece):
            self._castling_rights[2] = False
        if self.is_square_empty(56) or not (type(self._get_piece(56)) == Rook and not self._get_piece(56).white_piece):
            self._castling_rights[3] = False

    def _set_en_passant_target_square(self, moving_piece: Piece, move: MOVE) -> None:
        """
        set the en passant target square according to the move
        :param moving_piece: piece to move
        :param move: move to make
        """
        if type(moving_piece) == Pawn and abs(move[0] - move[1]) == 16:
            self._ep_target_square = move[0] + 8 if self._white_to_move else move[0] - 8
        else:
            self._ep_target_square = None

    def _increase_turn_number(self) -> None:
        """
        increase the turn number according to the move
        """
        if not self._white_to_move:
            self._turn_number += 1

    def _alternate_color_to_move(self) -> None:
        """
        alternate the color to move
        """
        self._white_to_move = not self._white_to_move

    """
    undo move
    """
    def _undo_move(self) -> None:
        """
        restore the last board constellation
        """
        move = self._moves.pop()
        moved_piece = self._get_piece(move[1])
        data = self._data.pop()
        self._white_to_move = data[0]
        self._turn_number = data[4]
        self._undo_piece_moves(move, moved_piece)
        self._castling_rights = data[1]
        self._ep_target_square = data[2]
        self._half_move_clock = data[3]
        self.is_square_empty.cache_clear()

    def _undo_piece_moves(self, move: MOVE, moved_piece: Piece) -> None:
        """
        restore the last piece positions
        :param move: move to undo
        :param moved_piece: piece to move back
        """
        def uncastle() -> None:
            if not type(moved_piece) == King or not abs(move[0] - move[1]) == 2:
                return
            # castles queenside
            if (move[0] - move[1]) == abs(move[0] - move[1]):
                # move queenside rook
                self._get_piece(move[1] + 1).move_to(move[1] - 2)
            # castles kingside
            else:
                # move queenside rook
                self._get_piece(move[1] - 1).move_to(move[1] + 1)

        def unpromote() -> None:
            nonlocal moved_piece
            for piece in self._pieces:
                with contextlib.suppress(AttributeError):
                    if piece.promotion_data == (self._turn_number, self._white_to_move):
                        self._pieces.discard(moved_piece)
                        piece.unpromote()
                        moved_piece = piece
                        return

        def move_piece() -> None:
            moved_piece.move_to(move[0])

        def uncapture() -> None:
            for piece in self._pieces:
                if piece.capture_data == (self._turn_number, self._white_to_move):
                    piece.uncapture()
                    return

        uncastle()
        unpromote()
        move_piece()
        uncapture()

    """
    position state getter
    """
    @lru_cache(maxsize=64)
    def is_square_empty(self, pos: int) -> bool:
        """
        test whether there is a piece on the given position
        :param pos: position of the square to test
        :return: whether there is a piece at the given position
        """
        for piece in self._get_active_pieces:
            if piece.pos == pos:
                return False
        return True

    def own_piece_on_square(self, pos: int, white_piece: bool) -> bool:
        """
        test whether there is a piece on the given position the same color as given
        :param pos: positions of the square to test
        :param white_piece: own color
        :return: whether there is one of your own pieces_tests at the given position
        """
        for piece in self._get_active_pieces:
            if piece.pos == pos and piece.white_piece == white_piece:
                return True
        return False

    def opponent_piece_on_square(self, pos: int, white_piece: bool) -> bool:
        """
        test whether there is a piece on the given position a different color as given
        :param pos: positions of the square to test
        :param white_piece: own color
        :return: whether there is one of your opponent's own pieces_tests at the given position
        """
        for piece in self._get_active_pieces:
            if piece.pos == pos and not piece.white_piece == white_piece:
                return True
        return False

    def is_square_attacked(self, pos: int, white_piece: bool):  
        """
        test is a square is being threatened by a player_tests
        only considers moves that could threaten the king
        :param pos: position of the square
        :param white_piece: point of view of the test
        :return: whether a square is being threatened by a player_tests
        """
        for piece in self._get_active_pieces:
            if not piece.white_piece == white_piece:
                if pos in piece.attacking_squares:
                    return True
        return False

    """
    pieces_tests
    """
    def _get_piece(self, pos: int, pieces: Optional[Set[Piece]] = None) -> Piece:
        """
        get the piece on the given position
        :param pos: positions of the piece
        :param pieces: piece set to use
        :return: the piece on the given position
        :raises ValueError if there is no piece on the square
        """
        if pieces is None:
            pieces = self._get_active_pieces
        for piece in pieces:
            if piece.pos == pos:
                return piece
        raise ValueError('No piece found on given position.')

    def _get_king(self, white_piece: bool) -> Piece:
        """
        get the king with the given color
        :param white_piece: color of the king
        :return: king with given color
        """
        for piece in self._get_active_pieces:
            if type(piece) == King and piece.white_piece == white_piece:
                return piece
        raise ValueError('No king found.')

    def _create_piece(self, pos: int, symbol: str) -> Piece:
        """
        create a piece object
        :param pos: position of the piece
        :param symbol: symbol of the piece type
        :return: piece object with given attributes
        """
        white_piece = symbol.isupper()
        symbol = symbol.lower()
        if symbol == 'p':
            return Pawn(pos, white_piece, self)
        elif symbol == 'n':
            return Knight(pos, white_piece, self)
        elif symbol == 'b':
            return Bishop(pos, white_piece, self)
        elif symbol == 'r':
            return Rook(pos, white_piece, self)
        elif symbol == 'q':
            return Queen(pos, white_piece, self)
        elif symbol == 'k':
            return King(pos, white_piece, self)

    """
    logs
    """
    def _log_data(self) -> None:
        """
        save the board data
        """
        self._data.append((self._white_to_move, self._castling_rights.copy(), self._ep_target_square,
                           self._half_move_clock, self._turn_number))

    def _load_position(self, fen: str) -> None:
        """
        load the data of a fen string into the object's attributes
        :param fen: fen string to load
        only moves pieces_tests back if piece set is not empty
        """
        self._pieces, self._white_to_move, self._castling_rights, self._ep_target_square, self._half_move_clock, \
            self._turn_number = self._fen_to_board(fen)

    def _log_move(self, move: MOVE) -> None:
        """
        saves the last move
        """
        self._moves.append(move)

    """
    board conversion
    convert fen string data to board object data
    """
    def _fen_to_board(self, fen: str) -> Tuple[Set[Piece], bool, List[bool], Union[None, int], int, int]:
        """
        translate a fen string to the board object attribute data types
        :param fen: fen string to translate
        :return: piece objects on the board, color to move, castling rights, ep target square, half move clock, turn
                 number
        """
        fen = fen.strip().split()
        return self._pieces_to_board(fen[0]), self._color_to_move_to_board(fen[1]), \
            self._castling_rights_to_board(fen[2]), self._ep_target_square_to_board(fen[3]), \
            self._half_move_clock_to_board(fen[4]), self._turn_number_to_board(fen[5])

    def _pieces_to_board(self, positions: str) -> Set[Piece]:  
        """
        convert positions from fen data to board object data
        :param positions: fen positions
        :return: set of pieces_tests on the board
        """
        pieces = set()
        positions = positions.split('/')
        for r, rank in enumerate(positions):
            f = 0
            for symbol in rank:
                if symbol.isdigit():
                    f += int(symbol)
                    continue
                pieces.add(self._create_piece((7 - r) * 8 + f, symbol))
                f += 1
        return pieces

    @staticmethod
    def _color_to_move_to_board(color_to_move: str) -> bool:
        """
        convert color to move from fen data to board object data
        :param color_to_move: fen color to move
        :return: bool whether white or black to move
        """
        return color_to_move == 'w'

    @staticmethod
    def _castling_rights_to_board(castling_rights: str) -> List[bool]:
        """
        convert castling rights from fen data to board object data
        :param castling_rights: fen castling rights
        :return: list of all castling rights
        """
        rights = [False, False, False, False]
        if castling_rights == '-':
            return rights
        if 'K' in castling_rights:
            rights[0] = True
        if 'Q' in castling_rights:
            rights[1] = True
        if 'k' in castling_rights:
            rights[2] = True
        if 'q' in castling_rights:
            rights[3] = True
        return rights

    @staticmethod
    def _ep_target_square_to_board(ep_target_square: str) -> Union[None, int]:
        """
        convert ep target square from fen data to board object data
        :param ep_target_square: fen ep target square
        :return: ep target square value
        """
        if ep_target_square == '-':
            return None
        return ((int(ep_target_square[1]) - 1) * 8) + (ord(ep_target_square[0]) - 97)

    @staticmethod
    def _half_move_clock_to_board(half_move_clock: str) -> int:
        """
        convert half move clock from fen data to board object data
        :param half_move_clock: fen half move clock
        :return: half move clock value
        """
        return int(half_move_clock)

    @staticmethod
    def _turn_number_to_board(turn_number: str) -> int:
        """
        convert turn number from fen data to board object data
        :param turn_number: fen turn number
        :return: turn number value
        """
        return int(turn_number)

    """
    fen conversion
    convert board object data to fen string data
    """
    def _board_to_fen(self) -> str:
        """
        translate the board object attribute data type to a fen string
        :return: fen string of the current board
        """
        return f'{self._pieces_to_fen()} {self._color_to_move_to_fen()} {self._castling_rights_to_fen()} ' \
               f'{self._ep_target_square_to_fen()} {self._half_move_clock_to_fen()} {self._turn_number_to_fen()}'

    def _pieces_to_fen(self, pieces: Set[Piece] = None) -> str:  
        """
        convert positions from board object data to fen data
        :param pieces: board object piece set
        :return: fen positions
        """
        if pieces is None:
            pieces = self._get_active_pieces
        positions = ''
        for rank in range(7, -1, -1):
            n_empty_squares = 0
            for file in range(8):
                if not self.is_square_empty((rank * 8) + file, pieces):
                    if n_empty_squares:
                        positions += str(n_empty_squares)
                        n_empty_squares = 0
                    positions += self._get_piece((rank * 8) + file, pieces).fen_symbol
                else:
                    n_empty_squares += 1
            if n_empty_squares:
                positions += str(n_empty_squares)
            if rank:
                positions += '/'
        return positions

    def _color_to_move_to_fen(self, color_to_move: Optional[bool] = None) -> str:
        """
        convert color to move from board object data to fen data
        :param color_to_move: board object color to move
        :return: fen color to move
        """
        if color_to_move is None:
            color_to_move = self._white_to_move
        return 'w' if color_to_move else 'b'

    def _castling_rights_to_fen(self, castling_rights: Optional[List[bool]] = None) -> str:
        """
        convert castling rights from board object data to fen data
        :param castling_rights: board object castling rights
        :return: fen castling rights
        """
        if castling_rights is None:
            castling_rights = self._castling_rights
        rights = ''
        if castling_rights[0]:
            rights += 'K'
        if castling_rights[1]:
            rights += 'Q'
        if castling_rights[2]:
            rights += 'k'
        if castling_rights[3]:
            rights += 'q'
        if not rights:
            return '-'
        return rights

    def _ep_target_square_to_fen(self, ep_target_square: Optional[Union[None, int]] = None) -> str:
        """
        convert ep target square from board object data to fen data
        :param ep_target_square: board object ep target square
        :return: fen ep target square
        """
        if ep_target_square is None:
            ep_target_square = self._ep_target_square
        if ep_target_square:
            return chr(97 + (ep_target_square % 8)) + str((ep_target_square // 8) + 1)
        return '-'

    def _half_move_clock_to_fen(self, half_move_clock: Optional[int] = None) -> str:
        """
        convert half move clock from board object data to fen data
        :param half_move_clock: board object half move clock
        :return: fen half move clock
        """
        if half_move_clock is None:
            half_move_clock = self._half_move_clock
        return str(half_move_clock)

    def _turn_number_to_fen(self, turn_number: Optional[int] = None) -> str:
        """
        convert turn number from board object data to fen data
        :param turn_number: board object turn number
        :return: fen turn number
        """
        if turn_number is None:
            turn_number = self._turn_number
        return str(turn_number)


# board = Board()
# cProfile.run('board._get_legal_moves()', sort=2)
