import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, spriteObjects, pickupSprites):
        super().__init__(groups)

        self.image = pg.image.load('assets/Player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = pg.Rect(self.rect.x+4, self.rect.bottom-42, 52, 22)

        self.spriteObjects = spriteObjects
        self.pickupSprites = pickupSprites

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
        
        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")

        self.rect.center = self.hitbox.center
    
    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.spriteObjects:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.spriteObjects:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

        for item in self.pickupSprites:
            if item.hitbox.colliderect(self.hitbox):
                print('E')

    def update(self):
        self.input()
        self.move(self.speed)
