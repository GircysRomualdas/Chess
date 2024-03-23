import pygame

from config.constants import COLS, ROWS, SQUARE_COLOR_ONE, SQUARE_COLOR_TWO, SQUARE_SIZE

from .board.board import Board
from .dragger import Dragger


class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.next_player = 'white'


    def show_background(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = SQUARE_COLOR_ONE
                else:
                    color = SQUARE_COLOR_TWO

                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) )


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
        if self.dragger.dragging:
            piece = self.dragger.piece
            
            for move in piece.moves:
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                rect = (move.final.col * SQUARE_SIZE, move.final.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, color, rect)
    
    
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black' 


                