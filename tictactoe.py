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
        self.init_game()
        self.game_loop()
        self.end_game()

    def init_game(self):
        pg.init()
        pg.display.set_caption("Tic Tac Toe")

    def game_loop(self):
        running = True

        while running:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    running = False

                self.handle_game_state(e)

            pg.display.update()
            self.game_interface.draw_grid()

    def handle_game_state(self, e):
        game_state = self.game_state.check()
        # 0: game is running
        # 1: player_1 win
        # 2: player_2 win
        # 3: draw

        if game_state == 0:
            self.handle_player_turn(e)
        elif game_state == 3:
            self.handle_draw()
        else:
            self.handle_win()

    def handle_player_turn(self, e):
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

    def handle_draw(self):
        print("It's a draw!")
        self.game_state.reset()
        self.game_interface.reset()

    def handle_win(self):
        player = self.players[self.turn]
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

    def end_game(self):
        pg.quit()
