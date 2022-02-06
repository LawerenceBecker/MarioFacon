import pygame as pg

class UiOverlay():

    class ScreenText(pg.sprite.Sprite):
        def __init__(self, text, groups):
            super().__init__(groups)
            display_surface = pg.display.get_surface()

            # Grahpic setup
            self.font = pg.font.Font(None, 128)

            self.prevTick = pg.time.get_ticks()
            self.animTimer = 1000

            self.image = self.font.render(text, False, (0,0,0)).convert_alpha()

            # Position Finding
            half_text_width = self.image.get_width() // 2
            half_text_height = self.image.get_height() // 2

            half_screen_width = display_surface.get_size()[0] // 2
            half_screen_height = display_surface.get_size()[1] // 2

            x = half_screen_width - half_text_width
            y = half_screen_height - half_text_height

            self.rect = self.image.get_rect(topleft = (x,y))

        def update(self):
            if self.image.get_alpha() <= 0:
                self.kill()
            if pg.time.get_ticks() - self.prevTick >= self.animTimer:
                self.image.set_alpha(self.image.get_alpha() - 10)

    class InputOverlay(pg.sprite.Sprite):
        def __init__(self, prompt, group):
            super().__init__(group)
            display_surface = pg.display.get_surface()

            x = display_surface.get_size()[0] // 2
            y = display_surface.get_size()[1] // 2
            
            # Graphic Setup
            self.image = pg.image.load('assets/Prompt_Overlay.png')
            self.rect = self.image.get_rect(topleft = (x+24, y-28))

            font = pg.font.Font(None, 24)
            promptText = font.render(f'E     {prompt}' , False , (0,0,0)) # 13 Es

            self.image.blit(promptText, [5, 5])

            # Animation Setup
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

        def __init__(self, item, group):
            super().__init__(group)

            # Animation Setup
            self.animTimer = 10
            self.prevTick = pg.time.get_ticks()
            self.fullTimer = 1000

            self.fadeIn =  True
            self.fadeOut = False

            # Graphic Setup
            display_surface = pg.display.get_surface()
            self.width = display_surface.get_size()[0]

            half_height = display_surface.get_size()[1] // 2

            self.image = pg.image.load('assets/Item_Add_Overlay.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (self.width, half_height))

            font = pg.font.Font(None, 30)

            itemImage = item.icon
            itemNameText = font.render(f'You got 1x {item.name}' , False , (0,0,0))

            self.image.blit(itemImage, [3, 3])
            self.image.blit(itemNameText, [56,12])
            
        def update(self):
            if self.fadeIn:
                if pg.time.get_ticks() - self.prevTick >= self.animTimer:
                    if self.rect.x <= self.width-self.image.get_width():
                        self.rect.x = self.width-self.image.get_width()
                        self.fadeIn = False
                    else:
                        self.rect.x -= 12
                    self.prevTick =  pg.time.get_ticks()

            else:
                if self.image.get_alpha() <= 0:
                    self.kill()
                
                if self.fadeOut:
                    if pg.time.get_ticks() - self.prevTick >= self.animTimer:
                        self.image.set_alpha(self.image.get_alpha() - 5)
                        self.rect.y += 2

                if pg.time.get_ticks() - self.prevTick >= self.fullTimer and self.fadeOut == False:
                    self.fadeOut = True
                    self.prevTick = pg.time.get_ticks()

                    self.image.set_alpha(self.image.get_alpha() - 5)
                    self.rect.y += 2
