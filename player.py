import pygame as pg

from uiOverlay import UiOverlay

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, spriteObjects, pickupSprites, playerUiSprites):
        super().__init__(groups)

        self.image = pg.image.load('assets/Player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = pg.Rect(self.rect.x+4, self.rect.bottom-42, 52, 22)

        self.overlayActive = False

        self.state = 'idle'

        self.aniamtions = {'idle': ['assets/player/idle/Player_idle_0.png','assets/player/idle/Player_idle_1.png']}
        self.animTimer = 300
        self.prevTick = pg.time.get_ticks()

        self.animIndex = 0

        self.placement = self.rect.centery

        self.sprites = groups[0]
        self.spriteObjects = spriteObjects
        self.pickupSprites = pickupSprites

        self.playerUiSprites = playerUiSprites
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

        if keys[pg.K_e]:
            for item in self.pickupSprites:
                if item.hitbox.colliderect(self.hitbox):
                    UiOverlay.GainItem(item, self.playerUiSprites)
                    item.kill()

                    self.overlayActive = False
                    for uiElem in self.playerUiSprites:
                            if isinstance(uiElem, UiOverlay.InputOverlay):
                                uiElem.kill()

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

        for sprite in self.pickupSprites:
            if sprite.hitbox.colliderect(self.hitbox):
                for uiElem in self.playerUiSprites:
                    if isinstance(uiElem, UiOverlay.InputOverlay):
                        uiElem.kill()
                UiOverlay.InputOverlay("Pick up Item", self.playerUiSprites)
                break
            else:
                for uiElem in self.playerUiSprites:
                    if isinstance(uiElem, UiOverlay.InputOverlay):
                        uiElem.kill()

    def update(self):
        self.input()
        self.move(self.speed)

        if self.state == 'idle':
            if pg.time.get_ticks() - self.prevTick >= self.animTimer:
                self.image = pg.image.load(self.aniamtions['idle'][self.animIndex]).convert_alpha()
                self.animIndex += 1
                if self.animIndex >= len(self.aniamtions["idle"]):
                    self.animIndex = 0
                self.prevTick = pg.time.get_ticks()
        
