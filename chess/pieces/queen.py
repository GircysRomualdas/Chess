from .piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)
    
    @staticmethod 
    def piece_moves(row, col, piece, squares):
        Piece.straight_line_moves(row, col, piece, squares, [
                (-1, 1),
                (-1, -1),
                (1, 1),
                (1, -1),
                (-1, 0),
                (0, 1),
                (1, 0),
                (0, -1)
            ])