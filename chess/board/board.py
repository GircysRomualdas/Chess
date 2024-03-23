from chess.pieces.bishop import Bishop
from chess.pieces.king import King
from chess.pieces.knight import Knight
from chess.pieces.pawn import Pawn
from chess.pieces.queen import Queen
from chess.pieces.rook import Rook
from chess.move import Move
from config.constants import COLS, ROWS

from .square import Square


class Board:
    def __init__(self):
        self.squares = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")

    def calc_moves(self, piece, row, col):
        if isinstance(piece, Pawn):
            Pawn.piece_moves(row, col, piece, self.squares)
        elif isinstance(piece, Knight):
            Knight.piece_moves(row, col, piece, self.squares)
        elif isinstance(piece, Bishop):
            Bishop.piece_moves(row, col, piece, self.squares)
        elif isinstance(piece, Rook):
            Rook.piece_moves(row, col, piece, self.squares)
        elif isinstance(piece, Queen):
            Queen.piece_moves(row, col, piece, self.squares)
        elif isinstance(piece, King):
            King.piece_moves(row, col, piece, self.squares)


    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        if color == "white":
            row_pawn, row_other = (6, 7)
        else:
            row_pawn, row_other = (1, 0)

        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        self.squares[row_other][4] = Square(row_other, 4, King(color))
