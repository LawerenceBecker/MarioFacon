import pygame as pg

class PickUpItem(pg.sprite.Sprite):
    def __init__(self, pos, groups, name):
        super().__init__(groups)
        self.icon = pg.image.load(f'assets/{name}.png').convert_alpha()
        self.image = pg.image.load('assets/items/Item_Sprite_0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (pos[0]+16, pos[1]+16))
        self.hitbox = self.rect.inflate(-6, -22)

        self.animations = ['assets/items/Item_Sprite_0.png', 'assets/items/Item_Sprite_1.png','assets/items/Item_Sprite_0.png',  'assets/items/Item_Sprite_2.png']
        self.animTimer = 350
        self.prevTick = pg.time.get_ticks()

        self.animIndex = 0

        self.placement = -1

        self.name = name

    def update(self):
        if pg.time.get_ticks() - self.prevTick >= self.animTimer:
            self.animIndex += 1
            if self.animIndex >= len(self.animations):
                self.animIndex = 0
            self.image = pg.image.load(self.animations[self.animIndex]).convert_alpha()
            self.prevTick = pg.time.get_ticks()
