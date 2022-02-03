import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, x, y, groups, tileImage, typeTile="wall"):
        super().__init__(groups)

        self.image = pg.image.load(f'assets/{tileImage}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (x*64,y*64))
        
        self.hitbox = self.rect.inflate(-6,-18)
        
        self.typeTile = typeTile

    def find_placement(self):
        return self.rect.centery
