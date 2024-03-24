import os


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

    
    def clear_moves(self):
        self.moves = []
        

    def set_texture(self, size = 80):
        self.texture = os.path.join(f'assets/images/pieces/{size}px/{self.color}_{self.name}.png')

    def add_move(self, move):
        self.moves.append(move)
    


        

