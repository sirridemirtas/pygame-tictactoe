import pygame as pg

from game_interface import GameInterface
from game_state import GameState

class TicTacToe:
    def __init__(self):
        self.game_interface = GameInterface()
        self.game_state = GameState()

    def start(self):
        pg.init()
        pg.display.set_caption("Tic Tac Toe")

        running = True
        
        while running:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    running = False
                
                if e.type == pg.MOUSEBUTTONUP:
                    tile_index = self.game_interface.get_tile(e.pos)
                    if tile_index != -1:
                        self.game_interface.draw_x_to_tile(tile_index)
                
                if e.type == pg.KEYUP:
                    if e.key in [49, 50, 51, 52, 53, 54, 55, 56, 57]:
                        tile_index = e.key - 49
                        self.game_interface.draw_x_to_tile(tile_index)

                pg.display.update()
            
            self.game_interface.draw_grid()

        pg.quit()
