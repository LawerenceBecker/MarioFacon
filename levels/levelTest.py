import pygame as pg
from player import Player
from debug import debug

class Level():
    def __init__(self):

        self.display_surface = pg.display.get_surface()

        self.sprites = pg.sprite.Group()

        self.player = Player((64,64), [self.sprites])

    def run(self):
        
        self.sprites.draw(self.display_surface)
        self.sprites.update()

        debug(self.player.direction)