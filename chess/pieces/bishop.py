from .piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.001)
        
    @staticmethod 
    def piece_moves(row, col, piece, squares):
        Piece.straight_line_moves(row, col, piece, squares, [
                (-1, 1),
                (-1, -1),
                (1, 1),
                (1, -1)
            ])