import pygame as pg

from uiOverlay import UiOverlay
from maps import *

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, groups, spriteObjects, pickupSprites, playerUiSprites, transSprites, l):
        super().__init__(groups)

        self.game = l.game

        self.image = pg.image.load('assets/Player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (x*64,y*64))
        self.hitbox = pg.Rect(self.rect.x+4, self.rect.bottom-42, 52, 22)

        self.overlayActive = False

        self.state = 'idle'

        self.aniamtions = {'idle': ['assets/player/idle/Player_idle_0.png','assets/player/idle/Player_idle_1.png']}
        self.animTimer = 300
        self.prevTick = pg.time.get_ticks()

        self.animIndex = 0

        self.sprites = groups[0]
        self.spriteObjects = spriteObjects
        self.pickupSprites = pickupSprites
        self.transSprites =  transSprites
        self.breakableObj = None

        self.playerUiSprites = playerUiSprites
        self.direction = pg.math.Vector2()
        self.speed = 5

        self.inventory = []

    def find_placement(self):
        return self.rect.centery
        
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
    
        if keys[pg.K_TAB]:
            print(self.inventory)

        if keys[pg.K_e]:
            for item in self.pickupSprites:
                if item.hitbox.colliderect(self.hitbox):
                    UiOverlay.GainItem(item, self.playerUiSprites)
                    found = False
                    for items in self.inventory:
                        if items[0] == item.name:
                            items[1] += 1
                            found  = True
                    if found == False:
                        self.inventory.append([item.name, item.amount])
                    item.kill()

                    self.overlayActive = False
                    for uiElem in self.playerUiSprites:
                            if isinstance(uiElem, UiOverlay.InputOverlay):
                                uiElem.kill()

            if self.breakableObj:
                self.breakableObj.kill()

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
                        

        for transitions in self.transSprites:
            if transitions.hitbox.colliderect(self.hitbox):
                self.sprites.empty()
                self.spriteObjects.empty()
                self.pickupSprites.empty()
                self.transSprites.empty()

                if transitions.transType == 'n':
                    self.game.level.create_map(maps[self.game.level.northTran])
                    self.game.level.eastTran = maps[self.game.level.northTran][0][1]
                    self.game.level.southTran = maps[self.game.level.northTran][0][2]
                    self.game.level.westTran = maps[self.game.level.northTran][0][3]
                    self.game.level.northTran = maps[self.game.level.northTran][0][0]
                elif transitions.transType == 'e':
                    self.game.level.create_map(maps[self.game.level.eastTran])
                    self.game.level.northTran = maps[self.game.level.eastTran][0][0]
                    self.game.level.southTran = maps[self.game.level.eastTran][0][2]
                    self.game.level.westTran = maps[self.game.level.eastTran][0][3]
                    self.game.level.eastTran = maps[self.game.level.eastTran][0][1]
                elif transitions.transType == 's':
                    self.game.level.create_map(maps[self.game.level.southTran])
                    self.game.level.northTran = maps[self.game.level.southTran][0][0]
                    self.game.level.eastTran = maps[self.game.level.southTran][0][1]
                    self.game.level.westTran = maps[self.game.level.southTran][0][3]
                    self.game.level.southTran = maps[self.game.level.southTran][0][2]
                elif transitions.transType == 'w':
                    self.game.level.create_map(maps[self.game.level.westTran])
                    self.game.level.northTran = maps[self.game.level.westTran][0][0]
                    self.game.level.eastTran = maps[self.game.level.westTran][0][1]
                    self.game.level.southTran = maps[self.game.level.westTran][0][2]
                    self.game.level.westTran = maps[self.game.level.westTran][0][3]
                for transitions in self.transSprites:
                    if transitions.transType == 'n':
                        self.hitbox.center = transitions.rect.center
                        self.hitbox.y -= 64
                    elif transitions.transType == 'e':
                        self.hitbox.center = transitions.rect.center
                        self.hitbox.x -= 64
                    elif transitions.transType == 's':
                        self.hitbox.center = transitions.rect.center
                        self.hitbox.y += 64
                    elif transitions.transType == 'w':
                        self.hitbox.center = transitions.rect.center
                        self.hitbox.x += 64
                self.sprites.add(self)
                
                    

        for sprite in self.spriteObjects:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.typeTile == "break":
                        self.breakableObj = sprite
                        for uiElem in self.playerUiSprites:
                            if isinstance(uiElem, UiOverlay.InputOverlay):
                                return
                        UiOverlay.InputOverlay("Interact with Wall", self.playerUiSprites)
                        return
        self.breakableObj = None
        

        for sprite in self.pickupSprites:
            if sprite.hitbox.colliderect(self.hitbox):
                for uiElem in self.playerUiSprites:
                    if isinstance(uiElem, UiOverlay.InputOverlay):
                        return
                UiOverlay.InputOverlay("Pick up Item", self.playerUiSprites)
                return

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
        
