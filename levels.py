import pygame as pg
from player import Player
from tile import Tile
from pickUpItems import PickUpItem
from transTile import TransTile
from maps import *

from debug import debug


class Level():
    def __init__(self, map, game):

        self.game = game
        self.player = None

        self.display_surface = pg.display.get_surface()

        self.pickupSprites = pg.sprite.Group()
        self.sprites = YSortCameraGroup()
        self.objectSprites = pg.sprite.Group()
        self.playerUiSprites = pg.sprite.Group()
        self.transSprites = pg.sprite.Group()

        self.northTran = map[0][0]
        self.eastTran = map[0][1]
        self.southTran = map[0][2]
        self.westTran = map[0][3]
        
        self.create_map(map)


    def create_map(self, map):
        for row_index, row in enumerate(map[1]):
            for col_index, col in enumerate(row):
                x = col_index
                y = row_index
                if col == 'f':
                    
                    Tile(x, y, [self.sprites,self.objectSprites], 'Picket_Fence')
                elif col == 'b':
                    Tile(x, y, [self.sprites,self.objectSprites], 'Picket_Fence', "break")
                elif col == 'p'and self.player == None:
                    self.player = Player(x, y, [self.sprites], self.objectSprites, self.pickupSprites, self.playerUiSprites, self.transSprites, self)
                elif col == 'S':
                    PickUpItem(x, y, [self.sprites,self.pickupSprites], 'Strawberry', 1)
                elif col == 'C':
                    PickUpItem(x, y, [self.sprites,self.pickupSprites], 'Carrot', 1)

                elif col == 'e':
                    TransTile(x, y, [self.transSprites, self.sprites], 'e')
                elif col == 'w':
                    TransTile(x, y, [self.transSprites, self.sprites], 'w')
                    
                    

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

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.find_placement()):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

