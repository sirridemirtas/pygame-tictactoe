import pygame as pg

from point import Point

class GameInterface:
    def __init__(self):
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 600

        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.fill((255, 255, 255))

        self.BASE_COLOR = (127, 127, 127)

    def draw_grid(self):
        for i in range(1, 3):
            pg.draw.line(self.screen, self.BASE_COLOR, (i * 200, 0), (i * 200, 600), 1)
            pg.draw.line(self.screen, self.BASE_COLOR, (0, i * 200), (600, i * 200), 1)

    def center_of_tile(self, index):
        CENTER_OF_TILES = [
            Point(100, 100), Point(300, 100), Point(500, 100),
            Point(100, 300), Point(300, 300), Point(500, 300),
            Point(100, 500), Point(300, 500), Point(500, 500)
        ]

        return CENTER_OF_TILES[index]

    def __draw_x(self, x, y):
        x1, y1 = x - 50, y - 50
        x2, y2 = x + 50, y + 50
        pg.draw.line(self.screen, self.BASE_COLOR, (x1, y1), (x2, y2), 1)
        pg.draw.line(self.screen, self.BASE_COLOR, (x2, y1), (x1, y2), 1)

    def __draw_o(self, x, y):
        pg.draw.circle(self.screen, self.BASE_COLOR, (x, y), 50, 1)

    def draw_x_to_tile(self, index):
        center = self.center_of_tile(index)
        self.__draw_x(center.x, center.y)

    def get_tile(self, point):
        pt = Point(point[0], point[1])

        if pt.x < 0 or pt.x > 600 or pt.y < 0 or pt.y > 600:
            return -1

        for i in range(9):
            if (    pt.x > self.center_of_tile(i).x - 100 
                and pt.x < self.center_of_tile(i).x + 100 
                and pt.y > self.center_of_tile(i).y - 100 
                and pt.y < self.center_of_tile(i).y + 100
            ):
                return i
        return -1
