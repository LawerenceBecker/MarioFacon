import pygame as pg

class UiOverlay():

    class InputOverlay(pg.sprite.Sprite):
        def __init__(self, prompt, group):
            super().__init__(group)
            display_surface = pg.display.get_surface()

            x = display_surface.get_size()[0] // 2
            y = display_surface.get_size()[1] // 2
            
            self.image = pg.image.load('assets/Prompt_Overlay.png')
            self.rect = self.image.get_rect(topleft = (x+24, y-28))

            font = pg.font.Font(None, 24)
            promptText = font.render(f'E     {prompt}' , True , (0,0,0)) # 13 Es

            self.image.blit(promptText, [5, 5])

            self.animPos = [-2, 2]
            self.animIndex = 0
            self.animTimer = 400
            self.prevTick = pg.time.get_ticks()

        def update(self):
            if pg.time.get_ticks() - self.prevTick >= self.animTimer:
                self.rect.y += self.animPos[self.animIndex]
                self.animIndex += 1
                if self.animIndex >= 2:
                    self.animIndex = 0
                self.prevTick = pg.time.get_ticks()

    class GainItem(pg.sprite.Sprite):
        itemList = []

        def __init__(self, item, group):
            super().__init__(group)

            self.itemList.append(self)

            self.prevTick = pg.time.get_ticks()
            self.fullTimer = 1000

            self.fade = False

            self.animTimer = 100

            display_surface = pg.display.get_surface()
            width = display_surface.get_size()[0]

            half_height = display_surface.get_size()[1] // 2

            self.image = pg.image.load('assets/Item_Add_Overlay.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (width-288, half_height-(len(self.itemList)*42)))

            font = pg.font.Font(None, 30)

            itemImage = item.icon
            itemNameText = font.render(f'You got 1x {item.name}' , True , (0,0,0))

            self.image.blit(itemImage, [3, 3])
            self.image.blit(itemNameText, [56,12])
            
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
