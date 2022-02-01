import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pg.image.load('assets/Picket_Fence.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = pg.Rect(self.rect.x+4, self.rect.bottom-23, 60, 12)

        self.placement = self.rect.centery
