
class Piece:
    def __init__(self, name, color, value, texture = None, texture_rect = None):
        self.name = name
        self.color = color
        self.texture = texture
        self.texture_rect = texture_rect
        self.set_texture()

        if color == 'white':
            self.value = value * 1
        else:
            self.value = value * -1


    def set_texture(self):
        pass

        

