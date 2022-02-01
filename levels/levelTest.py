import pygame as pg
from player import Player
from tile import Tile
from pickUpItems import PickUpItem


class Level():
    def __init__(self):

        self.display_surface = pg.display.get_surface()

        self.pickupSprites = pg.sprite.Group()
        self.sprites = YSortCameraGroup()
        self.objectSprites = pg.sprite.Group()
        self.playerUiSprites = pg.sprite.Group()

        self.player = Player((64,64), [self.sprites], self.objectSprites, self.pickupSprites, self.playerUiSprites)
        Tile((196, 196), [self.sprites,self.objectSprites])
        Tile((260, 196), [self.sprites,self.objectSprites])
        Tile((324, 196), [self.sprites,self.objectSprites])

        PickUpItem((260, 260), [self.sprites,self.pickupSprites], 'Strawberry')
        PickUpItem((324, 260), [self.sprites,self.pickupSprites], 'Strawberry')

    def run(self):
        
        self.sprites.custom_draw(self.player)
        self.sprites.update()
        self.playerUiSprites.draw(self.display_surface)
        self.playerUiSprites.update()

class YSortCameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.placement):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

