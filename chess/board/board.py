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

        # def knight_moves():
        #     possible_moves = [
        #         (row - 2, col + 1),
        #         (row - 1, col + 2),
        #         (row + 1, col + 2),
        #         (row + 2, col + 1),
        #         (row + 2, col - 1),
        #         (row + 1, col - 2),
        #         (row + 1, col - 2),
        #         (row - 2, col - 1),
        #     ]

        #     for possible_move in possible_moves:
        #         possible_move_row, possible_move_col = possible_move

        #         if Square.in_range(possible_move_row, possible_move_col):
        #             if self.squares[possible_move_row][possible_move_col].is_empty_or_rival(piece.color):
        #                 initial = Square(row, col)
        #                 final = Square(possible_move_row, possible_move_col)
                        
        #                 move = Move(initial, final)
        #                 piece.add_move(move)
                        
        def pawn_moves():
            steps = 1 if piece.moved else 2
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps))
            
            for move_row in range(start, end, piece.dir):
                pass

        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            # knight_moves()
            Knight.piece_moves(row, col, piece, self.squares)
        elif isinstance(piece, Bishop):
            pass
        elif isinstance(piece, Rook):
            pass
        elif isinstance(piece, Queen):
            pass
        elif isinstance(piece, King):
            pass

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
