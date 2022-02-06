import pygame as pg

class EventTile(pg.sprite.Sprite):
    def __init__(self,x, y, groups, event):
        super().__init__(groups)

        self.image = pg.Surface((64,64))
        self.image.fill('#9edb64')
        self.rect = self.image.get_rect(topleft = (x*64,y*64))

        self.hitbox = self.rect

        self.event = event

    def find_placement(self):
        return -1
    
    def combat_Tut(self):
        print(wow)