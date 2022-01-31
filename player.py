import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pg.Surface((64,64))
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pg.math.Vector2()
        self.speed = 5
        
    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w] or keys[pg.K_UP]:
            self.direction.y = -1
        elif keys[pg.K_s] or keys[pg.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.direction.x = -1
        elif keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center+= self.direction * speed
    
    def update(self):
        self.input()
        self.move(self.speed)
