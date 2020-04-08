import pygame

class Brick(pygame.sprite.Sprite):

    RESISTANCE = {
        1: pygame.image.load("Images/PNG/02-Breakout-Tiles.png"),
        2: pygame.image.load("Images/PNG/01-Breakout-Tiles.png"),
        3: pygame.image.load("Images/PNG/05-Breakout-Tiles.png")
    }

    def __init__(self, coup):
        pygame.sprite.Sprite.__init__(self)
        self.coup = coup
        self.width = 50
        self.height = 30
        self.image = Brick.RESISTANCE[self.coup].convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.width, self.height)


    def touche(self):
        self.coup -= 1
        if self.coup == 0:
            self.remove()
        else:
            self.image = Brick.RESISTANCE[self.coup].convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))





