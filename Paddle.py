import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/PNG/50-Breakout-Tiles.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (x,y))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move_left(self):
        self.rect.x -= 20

    def move_right(self):
        self.rect.x += 20