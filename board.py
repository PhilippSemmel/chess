from __future__ import annotations
import contextlib
from pieces import Piece, Pawn, Knight, Bishop, Rook, Queen, King
from typing import Tuple, Optional, Union, Set, List

MOVE = Tuple[int, int]


class Board:
    def __init__(self, fen: Optional[str] = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1') -> None:
        self._pieces, self._white_to_move, self._castling_rights, self._ep_target_square, self._half_move_clock, \
            self._turn_number = self._fen_to_board(fen)
        self._positions: List[str] = []

    def __repr__(self) -> str:
        def positions_to_str() -> str:
            output = ''
            for row in range(7, -1, -1):
                for file in range(8):
                    try:
                        output += ' ' + self._get_piece((row * 8) + file).symbol + ' '
                    except ValueError:
                        output += ' - '
                output += '\n'
            return output

        return f'{positions_to_str()}\ncolor to move: {self._color_to_move_to_fen()}\ncastling rights:' \
               f'{self._castling_rights_to_fen()}\nep target: {self._ep_target_square_to_fen()}\nhalf move clock: ' \
               f'{self._half_move_clock_to_fen()}\nturn: {self._turn_number_to_fen()}\n'

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

    """
    moves
    """
    @property
    def legal_moves(self) -> Set[MOVE]:  # comments for algorithm
        """
        generate all legal moves
        :return: set of all legal moves
        """
        moves = set()
        for piece in self._pieces:
            if not piece.white_piece == self._white_to_move:
                continue
            moves |= piece.pseudo_legal_moves
        return moves

    def make_move(self, move: MOVE) -> None:  # comments for algorithm
        """
        make a given move
        :param move: tuple of the starting position and the final position
        """
        def move_pieces() -> None:
            def capture_piece() -> None:
                with contextlib.suppress(ValueError):
                    self._pieces.discard(self._get_piece(move[1]))

            def castle() -> None:
                if piece.type == 5 and abs(move[0] - move[1]) == 2:
                    # castles queenside
                    if (move[0] - move[1]) == abs(move[0] - move[1]):
                        # move queenside rook
                        self._get_piece(move[0] - 4).move_to(move[1] + 1)
                    # castles kingside
                    else:
                        # move queenside rook
                        self._get_piece(move[0] + 3).move_to(move[1] - 1)

            def capture_en_passant() -> None:
                if move[1] == self._ep_target_square and piece.type == 0:
                    # remove piece from piece set
                    self._pieces.discard(self._get_piece(move[0] - ((move[0] % 8) - (move[1] % 8))))

            def promote_pawn() -> None:
                nonlocal piece
                if piece.type == 0 and (move[1] // 8 == 7 or move[1] // 8 == 0):
                    self._pieces.discard(piece)
                    piece = Queen(piece.pos, piece.white_piece, self)
                    self._pieces.add(piece)

            def move_piece() -> None:
                piece.move_to(move[1])

            capture_piece()
            castle()
            capture_en_passant()
            promote_pawn()
            move_piece()

        def alternate_color_to_move() -> None:
            self._white_to_move = not self._white_to_move

        def adjust_castling_rights() -> None:
            if self.is_square_empty(4) or not (self._get_piece(4).type == 5 and self._get_piece(4).white_piece):
                self._castling_rights[0] = False
                self._castling_rights[1] = False
            if self.is_square_empty(7) or not (self._get_piece(7).type == 3 and self._get_piece(7).white_piece):
                self._castling_rights[0] = False
            if self.is_square_empty(0) or not (self._get_piece(0).type == 3 and self._get_piece(0).white_piece):
                self._castling_rights[1] = False
            if self.is_square_empty(60) or not (self._get_piece(60).type == 5 and not self._get_piece(60).white_piece):
                self._castling_rights[2] = False
                self._castling_rights[3] = False
            if self.is_square_empty(63) or not (self._get_piece(63).type == 3 and not self._get_piece(63).white_piece):
                self._castling_rights[2] = False
            if self.is_square_empty(56) or not (self._get_piece(56).type == 3 and not self._get_piece(56).white_piece):
                self._castling_rights[3] = False

        def set_en_passant_target_square() -> None:
            if piece.type == 0 and abs(move[0] - move[1]) == 16:
                self._ep_target_square = move[0] + 8 if self._white_to_move else move[0] - 8
            else:
                self._ep_target_square = None

        def adjust_half_move_clock() -> None:
            if piece.type == 0 or not self.is_square_empty(move[1]):  # pawn move or capture move
                self._half_move_clock = 0
            else:
                self._half_move_clock += 1

        def increase_turn_number() -> None:
            if not self._white_to_move:
                self._turn_number += 1

        piece = self._get_piece(move[0])
        self._save_position()
        adjust_half_move_clock()
        move_pieces()
        adjust_castling_rights()
        set_en_passant_target_square()
        increase_turn_number()
        alternate_color_to_move()

    """
    position state getter
    """
    def is_square_empty(self, pos: int, pieces: Optional[Set[Piece]] = None) -> bool:
        """
        test whether there is a piece on the given position
        :param pos: position of the square to test
        :param pieces: pieces to reference
        :return: whether there is a piece at the given position
        """
        if pieces is None:
            pieces = self._pieces
        for piece in pieces:
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
            if piece.pos == pos and piece.white_piece == color:
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
            if piece.pos == pos and not piece.white_piece == color:
                return True
        return False

    def is_square_attacked(self, pos: int, color: bool):  # comments for algorithm
        """
        test is a square is being threatened by a player
        only considers moves that could threaten the king
        :param pos: position of the square
        :param color: point of view of the test
        :return: whether a square is being threatened by a player
        """
        squares = set()
        for piece in self._pieces:
            if not piece.white_piece == color:
                squares |= piece.attacking_squares
        return pos in squares

    """
    pieces
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
            pieces = self._pieces
        for piece in pieces:
            if piece.pos == pos:
                return piece
        raise ValueError('No piece found on the given position.')

    def _create_piece(self, pos: int, white_piece: bool, _type: int) -> Piece:
        """
        create a piece object
        :param pos: position of the piece
        :param white_piece: whether the piece is white
        :param _type: type of the piece
        :return: piece object with given attributes
        """
        if _type == 0:
            return Pawn(pos, white_piece, self)
        elif _type == 1:
            return Knight(pos, white_piece, self)
        elif _type == 2:
            return Bishop(pos, white_piece, self)
        elif _type == 3:
            return Rook(pos, white_piece, self)
        elif _type == 4:
            return Queen(pos, white_piece, self)
        elif _type == 5:
            return King(pos, white_piece, self)

    """
    positions log
    """
    def _save_position(self) -> None:
        """
        save a board state as fen string
        """
        self._positions.append(self._board_to_fen())

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
        fen = fen.strip().split(' ')
        return self._positions_to_board(fen[0]), self._color_to_move_to_board(fen[1]), \
            self._castling_rights_to_board(fen[2]), self._ep_target_square_to_board(fen[3]), \
            self._half_move_clock_to_board(fen[4]), self._turn_number_to_board(fen[5])

    def _positions_to_board(self, positions: str) -> Set[Piece]:  # comments for algorithm
        """
        convert positions from fen data to board object data
        :param positions: fen positions
        :return: set of pieces on the board
        """
        symbols = 'pnbrqk'
        pieces = set()
        positions = positions.split('/')
        for r, rank in enumerate(positions):
            f = 0
            for symbol in rank:
                if symbol.isdigit():
                    f += int(symbol)
                    continue
                pieces.add(self._create_piece((7 - r) * 8 + f, symbol.isupper(), symbols.find(symbol.lower())))
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
        return f'{self._positions_to_fen()} {self._color_to_move_to_fen()} {self._castling_rights_to_fen()} ' \
               f'{self._ep_target_square_to_fen()} {self._half_move_clock_to_fen()} {self._turn_number_to_fen()}'

    def _positions_to_fen(self, pieces: Set[Piece] = None) -> str:  # comments for algorithm
        """
        convert positions from board object data to fen data
        :param pieces: board object piece set
        :return: fen positions
        """
        if pieces is None:
            pieces = self._pieces
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
