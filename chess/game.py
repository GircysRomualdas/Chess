import pygame

from config.constants import COLS, ROWS, SQUARE_COLOR_ONE, SQUARE_COLOR_TWO, SQUARE_SIZE


class Game:
    def __init__(self):
        pass 


    def show_background(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = SQUARE_COLOR_ONE
                else:
                    color = SQUARE_COLOR_TWO

                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) )


                