import pygame

from config.constants import COLS, ROWS, SQUARE_COLOR_ONE, SQUARE_COLOR_TWO, SQUARE_SIZE

from .board.board import Board


class Game:
    def __init__(self):
        self.board = Board()


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
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2
                    piece.texture_rect = img.get_rect(center = img_center)
                    screen.blit(img, piece.texture_rect)


                