from .piece import Piece
from .rook import Rook
from chess.board.square import Square
from chess.move import Move

class King(Piece):
    def __init__(self, color):
        self.left_rook = None 
        self.right_rook = None
        super().__init__('king', color, 10000.0)
        
        
    @staticmethod 
    def piece_moves(row, col, piece, squares):
        adjacents = [
            (row - 1, col + 0),
            (row - 1, col + 1),
            (row + 0, col + 1),
            (row + 1, col + 1),
            (row + 1, col + 0),
            (row + 1, col - 1),
            (row + 0, col - 1),
            (row - 1, col - 1)
        ]
        
        for possible_move in adjacents:
            possible_move_row, possible_move_col = possible_move
            
            if Square.in_range(possible_move_row, possible_move_col):
                if squares[possible_move_row][possible_move_col].is_empty_or_rival(piece.color):
                    initial = Square(row, col)
                    final = Square(possible_move_row, possible_move_col)
                    move = Move(initial, final)
                    piece.add_move(move)
        
        if not piece.moved:
                left_rook = squares[row][0].piece
                
                if isinstance(left_rook, Rook):
                    if not left_rook.moved:
                        for c in range(1, 4):
                            if squares[row][c].has_piece(): 
                                break
                            
                            if c == 3:
                                piece.left_rook = left_rook
                                
                                initial = Square(row, 0)
                                final = Square(row, 3)
                                move = Move(initial, final)
                                left_rook.add_move(move)
                                
                                initial = Square(row, col)
                                final = Square(row, 2)
                                move = Move(initial, final)
                                piece.add_move(move)
                                
                                
                right_rook = squares[row][7].piece
                
                if isinstance(right_rook, Rook):
                    if not right_rook.moved:
                        for c in range(5, 7):
                            if squares[row][c].has_piece(): 
                                break
                            
                            if c == 6:
                                piece.right_rook = right_rook
                                
                                initial = Square(row, 7)
                                final = Square(row, 5)
                                move = Move(initial, final)
                                right_rook.add_move(move)
                                
                                initial = Square(row, col)
                                final = Square(row, 6)
                                move = Move(initial, final)
                                piece.add_move(move)