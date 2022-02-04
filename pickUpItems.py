import pygame as pg

class PickUpItem(pg.sprite.Sprite):
    def __init__(self, x, y, groups, name, itemId):
        super().__init__(groups)
        self.icon = pg.image.load(f'assets/{name}.png').convert_alpha()
        self.image = pg.image.load('assets/items/Item_Sprite_0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = ((x*64)+16, (y*64)+16))
        self.hitbox = self.rect.inflate(-6, -22)

        self.itemId = itemId

        self.animPos = [2,-2,-2,2]
        self.animTimer = 350
        self.prevTick = pg.time.get_ticks()

        self.animIndex = 0

        self.name = name

    def find_placement(self):

        return -1


    def update(self):
        if pg.time.get_ticks() - self.prevTick >= self.animTimer:
            self.animIndex += 1
            if self.animIndex >= len(self.animPos):
                self.animIndex = 0
            self.rect.y += self.animPos[self.animIndex]
            self.prevTick = pg.time.get_ticks()
