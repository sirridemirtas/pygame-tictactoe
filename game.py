import pygame as pg

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BASE_COLOR = (127, 127, 127)

def draw_grid(screen):
    for i in range(1, 3):
        pg.draw.line(screen, BASE_COLOR, (i * 200, 0), (i * 200, 600), 1)
        pg.draw.line(screen, BASE_COLOR, (0, i * 200), (600, i * 200), 1)

CENTER_OF_TILES = [ (100, 100), (300, 100), (500, 100),
                    (100, 300), (300, 300), (500, 300),
                    (100, 500), (300, 500), (500, 500) ]

def draw_x(screen, x, y):
    pg.draw.line(screen, BASE_COLOR, (x - 50, y - 50), (x + 50, y + 50), 1)
    pg.draw.line(screen, BASE_COLOR, (x + 50, y - 50), (x - 50, y + 50), 1)

def draw_o(screen, x, y):
    pg.draw.circle(screen, BASE_COLOR, (x, y), 50, 1)

def get_tile(x, y):
    if x < 0 or x > 600 or y < 0 or y > 600:
        return -1

    for i in range(9):
        if ( x > CENTER_OF_TILES[i][0] - 100 
            and x < CENTER_OF_TILES[i][0] + 100 
            and y > CENTER_OF_TILES[i][1] - 100 
            and y < CENTER_OF_TILES[i][1] + 100
        ):
            return i
    return -1

def main():
    pg.init()

    pg.display.set_caption("Tic Tac Toe")

    running = True
    
    while running:
        for e in pg.event.get():
            #print(e)
            if e.type == pg.QUIT:
                running = False

        screen.fill((255, 255, 255))
        draw_grid(screen)

        for i in range(9):
            draw_x(screen, CENTER_OF_TILES[i][0], CENTER_OF_TILES[i][1])
        
        # üzerine gelme eventi varsa çalışır
        if e.type == pg.MOUSEMOTION:
            print(get_tile(e.pos[0], e.pos[1]), end =" ")

        pg.display.flip()

    pg.quit()

main()
