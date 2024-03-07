import pygame as pg

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))

BASE_COLOR = (127, 127, 127)

def draw_grid(screen):
    for i in range(1, 3):
        pg.draw.line(screen, BASE_COLOR, (i * 200, 0), (i * 200, 600), 1)
        pg.draw.line(screen, BASE_COLOR, (0, i * 200), (600, i * 200), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def center_of_tile(index):
    CENTER_OF_TILES = [
        Point(100, 100), Point(300, 100), Point(500, 100),
        Point(100, 300), Point(300, 300), Point(500, 300),
        Point(100, 500), Point(300, 500), Point(500, 500)
    ]

    return CENTER_OF_TILES[index - 1]

def draw_x(x, y):
    x1, y1 = x - 50, y - 50
    x2, y2 = x + 50, y + 50
    pg.draw.line(screen, BASE_COLOR, (x1, y1), (x2, y2), 1)
    pg.draw.line(screen, BASE_COLOR, (x2, y1), (x1, y2), 1)

def draw_x_to_tile(index):
    center = center_of_tile(index)
    draw_x(center.x, center.y)

def draw_o(screen, x, y):
    pg.draw.circle(screen, BASE_COLOR, (x, y), 50, 1)

def get_tile(point):
    pt = Point(point[0], point[1])

    if pt.x < 0 or pt.x > 600 or pt.y < 0 or pt.y > 600:
        return -1

    for i in range(1, 10):
        if (    pt.x > center_of_tile(i).x - 100 
            and pt.x < center_of_tile(i).x + 100 
            and pt.y > center_of_tile(i).y - 100 
            and pt.y < center_of_tile(i).y + 100
        ):
            return i
    return -1

def main():
    pg.init()

    pg.display.set_caption("Tic Tac Toe")

    running = True
    
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            
            if e.type == pg.MOUSEBUTTONUP:
                tile_index = get_tile(e.pos)
                if tile_index != -1:
                    draw_x_to_tile(tile_index)

            pg.display.update()
        
        draw_grid(screen)

    pg.quit()

main()
