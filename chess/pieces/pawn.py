from .piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
        
        super().__init__('pawn', color, 1.0)
        