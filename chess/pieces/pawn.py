from .piece import Piece
from chess.board.square import Square
from chess.move import Move


class Pawn(Piece):
    def __init__(self, color):
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
        
        super().__init__('pawn', color, 1.0)
    
    @staticmethod 
    def piece_moves(row, col, piece, squares):
        steps = 1 if piece.moved else 2
        start = row + piece.dir
        end = row + (piece.dir * (1 + steps))
        
        for possible_move_row in range(start, end, piece.dir):
            if Square.in_range(possible_move_row):
                if squares[possible_move_row][col].is_empty():
                    initial = Square(row, col)
                    final = Square(possible_move_row, col)
                    move = Move(initial, final)
                    piece.add_move(move)
                else:
                    break
            else:
                break
            
        possible_move_row = row + piece.dir
        possible_move_cols = [col - 1, col + 1]
        
        for possible_move_col in possible_move_cols:
            if Square.in_range(possible_move_row, possible_move_col):
                if squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                    initial = Square(row, col)
                    final = Square(possible_move_row, possible_move_col)
                    move = Move(initial, final)
                    piece.add_move(move)
        