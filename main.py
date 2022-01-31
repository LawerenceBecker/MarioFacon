import pygame as pg
import sys


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1280,720))
        pg.display.set_caption('MarioStile')
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.QUIT
                    sys.exit()

            self.screen.fill('black')
            pg.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
