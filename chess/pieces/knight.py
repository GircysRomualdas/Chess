from .piece import Piece
from chess.board.square import Square
from chess.move import Move

class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)
    
    @staticmethod 
    def piece_moves(row, col, piece, squares):
            possible_moves = [
                (row - 2, col + 1),
                (row - 1, col + 2),
                (row + 1, col + 2),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col - 2),
                (row + 1, col - 2),
                (row - 2, col - 1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if squares[possible_move_row][possible_move_col].is_empty_or_rival(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        
                        move = Move(initial, final)
                        piece.add_move(move)
                        