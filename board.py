from __future__ import annotations
from pieces import Piece, Pawn, Knight, Bishop, Rook, Queen, King
from typing import Tuple, Optional, Union, Set, List

MOVE = Tuple[int, int]


class Board:
    def __init__(self, fen: Optional[str] = None) -> None:
        if fen:
            self._pieces, self._white_to_move, self._castling_rights, self._ep_target_square, self._half_move_clock, \
                self._turn_number = self._parse_fen(fen)
            return

        self._pieces: Set[Piece] = {Rook(0, True, self), Knight(1, True, self), Bishop(2, True, self),
                                    Queen(3, True, self), King(4, True, self), Bishop(5, True, self),
                                    Knight(6, True, self), Rook(7, True, self), Pawn(8, True, self),
                                    Pawn(9, True, self), Pawn(10, True, self), Pawn(11, True, self),
                                    Pawn(12, True, self), Pawn(13, True, self), Pawn(14, True, self),
                                    Pawn(15, True, self),
                                    Pawn(48, False, self), Pawn(49, False, self), Pawn(50, False, self),
                                    Pawn(51, False, self), Pawn(52, False, self), Pawn(53, False, self),
                                    Pawn(54, False, self), Pawn(55, False, self), Rook(56, False, self),
                                    Knight(57, False, self), Bishop(58, False, self), Queen(59, False, self),
                                    King(60, False, self), Bishop(61, False, self), Knight(62, False, self),
                                    Rook(63, False, self)}
        self._white_to_move: bool = True
        self._castling_rights: List[bool] = [True, True, True, True]
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

    def _parse_fen(self, fen: str) -> Tuple[Set[Piece], bool, List[bool], int, int, int]:
        """
        translate a fen string to the data the class needs for the board representation
        :param fen: the fen string to translate
        :return: piece objects on the board, color to move, castling rights, ep target square, half move clock, turn
                 number
        """
        def get_castling_rights() -> List[bool]:
            rights = []
            rights.append(True) if 'K' in fen[2] else rights.append(False)
            rights.append(True) if 'Q' in fen[2] else rights.append(False)
            rights.append(True) if 'k' in fen[2] else rights.append(False)
            rights.append(True) if 'q' in fen[2] else rights.append(False)
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

    def __repr__(self) -> str:
        white_pieces = {5: '♚', 4: '♛', 3: '♜', 2: '♝', 1: '♞', 0: '♟'}
        black_pieces = {5: '♔', 4: '♕', 3: '♖', 2: '♗', 1: '♘', 0: '♙'}
        output = ''
        for row in range(7, -1, -1):
            for file in range(8):
                try:
                    piece = self.get_piece((row * 8) + file)
                    symbol = white_pieces[piece.type] if piece.white_piece else black_pieces[piece.type]
                    output += ' ' + symbol + ' '
                except ValueError:
                    output += ' - '
            output += '\n'
        output += 'color to move: w\n' if self._white_to_move else 'color to move: b\n'
        if True not in self._castling_rights:
            output += '-'
        else:
            output += 'castling rights: '
            if self._castling_rights[0]:
                output += 'K'
            if self._castling_rights[1]:
                output += 'Q'
            if self._castling_rights[2]:
                output += 'k'
            if self._castling_rights[3]:
                output += 'q'
        output += '\n'
        if self._ep_target_square is None:
            output += 'ep target: -'
        else:
            output += 'ep target: ' + chr(97 + (self._ep_target_square % 8)) + str((self._ep_target_square // 8) + 1) +\
                      '\n'
        output += 'half moves clock: ' + str(self._half_move_clock) + '\n'
        output += 'turn: ' + str(self._turn_number)
        return output

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
    move generation
    """
    @property
    def legal_moves(self) -> Set[MOVE]:
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

    def is_square_attacked(self, pos: int, color: bool):
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
