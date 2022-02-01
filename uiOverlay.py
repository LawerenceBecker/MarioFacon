import pygame as pg

class UiOverlay():

    class GainItem(pg.sprite.Sprite):
        itemList = []

        def __init__(self, item, group):
            super().__init__(group)

            self.itemList .append(self)

            self.prevTick = pg.time.get_ticks()
            self.fullTimer = 1000

            self.fade = False

            self.animTimer = 100

            display_surface = pg.display.get_surface()
            width = display_surface.get_size()[0] - (len(item.name)* 24) - 48

            half_height = display_surface.get_size()[1] //2

            self.image = pg.image.load('assets/Item_Add_Overlay.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (width,half_height-(len(self.itemList )*42)))

            font = pg.font.Font(None, 30)

            itemImage = item.image
            itemNameText = font.render(f'You got 1x {item.name}' , True , (255,255,255))

            self.image.blit(itemImage, [0, 2])
            self.image.blit(itemNameText, [38, 12])
            
        def update(self):
            if self.image.get_alpha() <= 0:
                self.kill()
            
            if self.fade == True:
                if pg.time.get_ticks() - self.prevTick >= self.animTimer:
                    self.image.set_alpha(self.image.get_alpha() - 5)
                    self.rect.y += 2

            if pg.time.get_ticks() - self.prevTick >= self.fullTimer:
                self.fade = True
                self.prevTick = pg.time.get_ticks()

                self.image.set_alpha(self.image.get_alpha() - 5)
                self.rect.y += 2
