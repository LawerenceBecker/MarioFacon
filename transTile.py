import pygame as pg

class TransTile(pg.sprite.Sprite):
    def __init__(self,x, y, groups, transType):
        super().__init__(groups)

        self.image = pg.Surface((64,64))
        self.rect = self.image.get_rect(topleft = (x*64,y*64))

        self.hitbox = self.rect

        self.transType = transType

    def find_placement(self):
        return -1