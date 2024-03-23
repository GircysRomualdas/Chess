import os
from chess.board.square import Square
from chess.move import Move


class Piece:
    def __init__(self, name, color, value, texture = None, texture_rect = None):
        self.name = name
        self.color = color
        self.moves = []
        self.moved = False
        self.texture = texture
        self.texture_rect = texture_rect
        self.set_texture()

        if color == 'white':
            self.value = value * 1
        else:
            self.value = value * -1


    def set_texture(self, size = 80):
        self.texture = os.path.join(f'assets/images/pieces/{size}px/{self.color}_{self.name}.png')

    def add_move(self, move):
        self.moves.append(move)
        
    @staticmethod 
    def straight_line_moves(row, col, piece, squares, incrs):
        for incr in incrs:
            row_incr, col_incr = incr
            posible_move_row = row + row_incr
            posible_move_col = col + col_incr
            
            while True:
                if Square.in_range(posible_move_row, posible_move_col):
                    initial = Square(row, col)
                    final = Square(posible_move_row, posible_move_col)
                    move = Move(initial, final)
                    
                    if squares[posible_move_row][posible_move_col].is_empty():
                        piece.add_move(move) 
                    
                    if squares[posible_move_row][posible_move_col].has_rival_piece(piece.color):
                        piece.add_move(move)
                        break
                    
                    if squares[posible_move_row][posible_move_col].has_team_piece(piece.color):
                        break
                else:
                    break
                    
                posible_move_row = posible_move_row + row_incr
                posible_move_col = posible_move_col + col_incr


        

