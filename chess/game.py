import pygame
from config.constants import COLS, ROWS, SQUARE_COLOR_ONE, SQUARE_COLOR_TWO, SQUARE_SIZE, HEIGHT
from .board.board import Board
from .dragger import Dragger
from config.config import Config
from .board.square import Square


class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.next_player = 'white'
        self.hoverd_square = None
        self.config = Config()


    def show_background(self, screen):
        theme = self.config.theme
        
        for row in range(ROWS):
            for col in range(COLS):
                color = theme.background.light if (row + col) % 2 == 0 else theme.background.dark
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) )
                if col == 0:
                    color = theme.background.dark if row % 2 == 0 else theme.background.light
                    labale = self.config.font.render(str(ROWS - row), 1, color)
                    labale_pos = (5, 5 + row * SQUARE_SIZE)
                    screen.blit(labale, labale_pos)
                
                if row == 7:
                    color = theme.background.dark if (row + col) % 2 == 0 else theme.background.light
                    labale = self.config.font.render(Square.get_alphacol(col), 1, color)
                    labale_pos = (col * SQUARE_SIZE + SQUARE_SIZE - 20, HEIGHT - 20)
                    screen.blit(labale, labale_pos)

    def show_pieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2
                        piece.texture_rect = img.get_rect(center = img_center)
                        screen.blit(img, piece.texture_rect)
                        
    
    def show_moves(self, screen):
        theme = self.config.theme
        
        if self.dragger.dragging:
            piece = self.dragger.piece
            
            for move in piece.moves:
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                rect = (move.final.col * SQUARE_SIZE, move.final.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, color, rect)
    
    
    def show_last_move(self, screen):
        theme = self.config.theme
        
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            
            for pos in [initial, final]:
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                rect = (pos.col * SQUARE_SIZE, pos.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, color, rect)
    
    
    def show_hover(self, screen):
        if self.hoverd_square:
            color = (0, 0, 204)
            rect = (self.hoverd_square.col * SQUARE_SIZE, self.hoverd_square.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect, width = 3)
    
    
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black' 


    def set_hover(self, row, col):
        if Square.in_range(row, col):
            self.hoverd_square = self.board.squares[row][col]
        
        
    def change_theme(self):
        self.config.change_theme()
        
    
    def play_sound(self, captured = False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()
            
            
    def reset(self):
        self.__init__()