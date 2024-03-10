import pygame as pg

from game_interface import GameInterface
from game_state import GameState
from player import Player

class TicTacToe:
    def __init__(self, player_1, player_2):
        self.game_interface = GameInterface()
        self.game_state = GameState()
        self.players = [Player(player_1), Player(player_2)]
        self.turn = 0  # 0: player_1, 1: player_2

    def __switch_turn(self):
        self.turn = 1 - self.turn

    def start(self):
        pg.init()
        pg.display.set_caption("Tic Tac Toe")

        running = True

        while running:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    running = False

                if self.game_state.check() == 0:
                    if e.type == pg.MOUSEBUTTONUP and e.button == 1:
                        tile_index = self.game_interface.get_tile(e.pos)

                        if tile_index != -1 and self.game_state.is_empty(tile_index):
                            player = self.players[self.turn]

                            if player == self.players[0]:
                                self.game_interface.draw_x_to_tile(tile_index)
                                self.game_state.update(tile_index, 1)

                            elif player == self.players[1]:
                                self.game_interface.draw_o_to_tile(tile_index)
                                self.game_state.update(tile_index, 2)

                            self.__switch_turn()
                elif self.game_state.check() == 3:
                    print("It's a draw!")
                    self.game_state.reset()
                    self.game_interface.reset()
                else:
                    print(player.get_name() + " win!")
                    player.add_score()
                    self.game_state.reset()
                    self.game_interface.reset()

                    print(
                        self.players[0].get_name() + " " + 
                        str(self.players[0].get_score()) + " : " + 
                        str(self.players[1].get_score()) + " " + 
                        self.players[1].get_name()
                    )

            pg.display.update()

            self.game_interface.draw_grid()

        pg.quit()
