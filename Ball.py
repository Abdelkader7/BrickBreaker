import pygame

class Ball(pygame.sprite.Sprite):
    BALL_SPEED = 8

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.direction_x = 1
        self.direciton_y = 1
        self.image = pygame.image.load("Images/PNG/58-Breakout-Tiles.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (x,y))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def flip_direction_x(self):
        self.direction_x *= -1

    def flip_direction_y(self):
        self.direciton_y *= -1

    def leaves_screen_bottom(self):
        if self.rect.x < 0 or self.rect.x > 754:
            self.flip_direction_x()
        if self.rect.y < 0:
            self.flip_direction_y()

        return self.rect.y > 600

    def move(self):
        self.rect.x += self.BALL_SPEED * self.direction_x
        self.rect.y += self.BALL_SPEED * self.direciton_y