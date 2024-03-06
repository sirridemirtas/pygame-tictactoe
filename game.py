import pygame as pg

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def main():
    pg.init()

    pg.display.set_caption("Tic Tac Toe")

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    
    while running:
        for e in pg.event.get():
            print(e)
            if e.type == pg.QUIT:
                running = False

        screen.fill((255, 255, 255))
        pg.display.flip()

    pg.quit()

main()