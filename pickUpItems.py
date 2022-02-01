import pygame as pg

class PickUpItem(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pg.image.load('assets/Strawberry.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (pos[0]+16, pos[1]+16))
        self.hitbox = pg.Rect(self.rect.x+6, self.rect.top+3, 19, 25)
