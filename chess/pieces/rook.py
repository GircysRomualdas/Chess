from .piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)
        
    @staticmethod 
    def piece_moves(row, col, piece, squares):
        Piece.straight_line_moves(row, col, piece, squares, [
                (-1, 0),
                (0, 1),
                (1, 0),
                (0, -1)
            ])