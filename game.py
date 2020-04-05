# Import the pygame library and initialise the game engine
import pygame
from pygame.locals import *

from Paddle import Paddle
from Ball import Ball

pygame.init()
 
#Colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
 

score = 0
lives = 3
 
# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size, RESIZABLE)

pygame.display.set_caption("Ipssi Brick Breaker")

background = pygame.image.load("Images/background.png").convert()
#Adapt background size
background = pygame.transform.scale(background, size)

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

#Create the Paddle
paddle = Paddle(100, 20)
paddle.rect.x = 350
paddle.rect.y = 560

#Create the ball
ball = Ball(30,30)
ball.rect.x = 400
ball.rect.y = 561


# Add the paddle to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
continuer = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while continuer:
    # --- Main event looP
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left()

    if keys[pygame.K_RIGHT]:
        paddle.move_right()

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              continuer = False # Flag that we are done so we exit this loop
 
    if pygame.sprite.collide_mask(ball, paddle):
            ball.flip_direction_y()
    # --- Game logic should go here
    ball.move()
    if ball.leaves_screen_bottom():
    # reset the ball position
        ball.rect.x = 200
        ball.rect.y = 300
    all_sprites_list.update()

 
    # --- Drawing code should go here
    # First, clear the screen to dark blue. 
    #screen.fill(DARKBLUE)
    screen.blit(background, (0, 0))

    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
 
    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font("snes.ttf", 30)
    text = font.render("Score: " + str(score) +" | Lives:" + str(lives), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Stage: 1", 1, WHITE)
    screen.blit(text, (350,10))
    text = font.render("Playtime : 00:01", 1, WHITE)
    screen.blit(text, (600,10))
 
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()