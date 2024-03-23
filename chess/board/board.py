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
                        
        # def pawn_moves():
        #     steps = 1 if piece.moved else 2
        #     start = row + piece.dir
        #     end = row + (piece.dir * (1 + steps))
            
        #     for posible_move_row in range(start, end, piece.dir):
        #         if Square.in_range(posible_move_row):
        #             if self.squares[posible_move_row][col].is_empty():
        #                 initial = Square(row, col)
        #                 final = Square(posible_move_row, col)
        #                 move = Move(initial, final)
        #                 piece.add_move(move)
        #             else:
        #                 break
        #         else:
        #             break
                
        #     posible_move_row = row + piece.dir
        #     posible_move_cols = [col - 1, col + 1]
            
        #     for posible_move_col in posible_move_cols:
        #         if Square.in_range(posible_move_row, posible_move_col):
        #             if self.squares[posible_move_row][posible_move_col].has_rival_piece(piece.color):
        #                 initial = Square(row, col)
        #                 final = Square(posible_move_row, posible_move_col)
        #                 move = Move(initial, final)
        #                 piece.add_move(move)
        
        # def straight_line_moves(incrs):
        #     for incr in incrs:
        #         row_incr, col_incr = incr
        #         posible_move_row = row + row_incr
        #         posible_move_col = col + col_incr
                
        #         while True:
        #             if Square.in_range(posible_move_row, posible_move_col):
        #                 initial = Square(row, col)
        #                 final = Square(posible_move_row, posible_move_col)
        #                 move = Move(initial, final)
                        
        #                 if self.squares[posible_move_row][posible_move_col].is_empty():
        #                     piece.add_move(move) 
                        
        #                 if self.squares[posible_move_row][posible_move_col].has_rival_piece(piece.color):
        #                     piece.add_move(move)
        #                     break
                        
        #                 if self.squares[posible_move_row][posible_move_col].has_team_piece(piece.color):
        #                     break
        #             else:
        #                 break
                        
        #             posible_move_row = posible_move_row + row_incr
        #             posible_move_col = posible_move_col + col_incr
                        
                        

        if isinstance(piece, Pawn):
            # pawn_moves()
            Pawn.piece_moves(row, col, piece, self.squares)
        elif isinstance(piece, Knight):
            # knight_moves()
            Knight.piece_moves(row, col, piece, self.squares)
        elif isinstance(piece, Bishop):
            # straight_line_moves([
            #     (-1, 1),
            #     (-1, -1),
            #     (1, 1),
            #     (1, -1)
            # ])
            Bishop.piece_moves(row, col, piece, self.squares)
        elif isinstance(piece, Rook):
            # straight_line_moves([
            #     (-1, 0),
            #     (0, 1),
            #     (1, 0),
            #     (0, -1)
            # ])
            Rook.piece_moves(row, col, piece, self.squares)
        elif isinstance(piece, Queen):
            # straight_line_moves([
            #     (-1, 1),
            #     (-1, -1),
            #     (1, 1),
            #     (1, -1),
            #     (-1, 0),
            #     (0, 1),
            #     (1, 0),
            #     (0, -1)
            # ])
            Queen.piece_moves(row, col, piece, self.squares)
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
        
        #
        self.squares[4][5] = Square(4, 5, Rook(color))
        self.squares[3][3] = Square(3, 3, Queen(color))
        self.squares[2][1] = Square(2, 1, Bishop(color))
        #

        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        self.squares[row_other][4] = Square(row_other, 4, King(color))
