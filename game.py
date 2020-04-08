# Import the pygame library and initialise the game engine
import pygame
from pygame.locals import *

from Paddle import Paddle
from Ball import Ball
from Image import Image
from TextBox import TextBox
from Brick import Brick


pygame.init()
clock = pygame.time.Clock()

#Colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)


# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ipssi Brick Breaker")

background1 = pygame.image.load("Images/main1.png").convert_alpha()
background2 = pygame.image.load("Images/main2.png").convert_alpha()
background3 = pygame.image.load("Images/main3.png").convert_alpha()
background4 = pygame.image.load("Images/main4.png").convert_alpha()


#Adapt background size
background1 = pygame.transform.scale(background1, size)
background2 = pygame.transform.scale(background2, size)
background3 = pygame.transform.scale(background3, size)
background4 = pygame.transform.scale(background4, size)

font = pygame.font.Font("snes.ttf", 30)
menu = pygame.font.Font("miami.ttf", 40)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
     all_sprites_list = pygame.sprite.Group()

    #Logo creation
     image = Image("logo.png",700,400)
     image.rect.x = 50
     image.rect.y = 0
     all_sprites_list.add(image)

     CurrentBackground = 1

     continuer = True

     while continuer:
 
        if(CurrentBackground==1):
            screen.blit(background1,(0,0))
        if(CurrentBackground==2):
            screen.blit(background2,(0,0))
        if(CurrentBackground==3):
            screen.blit(background3,(0,0))
        if(CurrentBackground==4):
            screen.blit(background4,(0,0))
        if(CurrentBackground==4):
            CurrentBackground=1
        else:
            CurrentBackground+=1 

        #Button Jouer
        game_selected = menu.render('Jouer', 1, (255, 255, 255))
        game_pos = game_selected.get_rect()
        game_pos.topleft = (340, 340)
        screen.blit(game_selected, game_pos)
        
        #Button Instruction
        instruction_selected = menu.render('Instruction', 1, (255, 255, 255))
        instruction_pos = instruction_selected.get_rect()
        instruction_pos.topleft = (340, 390)
        screen.blit(instruction_selected, instruction_pos)

        #Button Stat
        stat_selected = menu.render('Stats', 1, (255, 255, 255))
        stat_pos = stat_selected.get_rect()
        stat_pos.topleft = (340, 440)
        screen.blit(stat_selected, stat_pos)

        #Button About
        about_selected = menu.render('A propos', 1, (255, 255, 255))
        about_pos = about_selected.get_rect()
        about_pos.topleft = (340, 490)
        screen.blit(about_selected, about_pos)

        #Button Quit
        quit_selected = menu.render('Quitter', 1, (255, 255, 255))
        quit_pos = quit_selected.get_rect()
        quit_pos.topleft = (340, 540)
        screen.blit(quit_selected, quit_pos)
        

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
                x, y = event.pos
                if game_pos.collidepoint(x,y):
                    custom()
                if instruction_pos.collidepoint(x,y):
                    instruction()
                if stat_pos.collidepoint(x,y):
                    stat()
                if about_pos.collidepoint(x,y):
                    about()
                if quit_pos.collidepoint(x,y):
                    continuer = False
        
        clock.tick(5)

 
        all_sprites_list.draw(screen)
        pygame.display.flip()



def instruction():

     

     background = pygame.image.load("Images/background.png").convert()
     background = pygame.transform.scale(background, size)
     screen.blit(background, (0,0))
     all_item_list = pygame.sprite.Group()

     #Bloc transparent
     s = pygame.Surface((590,350), pygame.SRCALPHA) 
     s.fill((0,0,0,128))       
     screen.blit(s, (200,200))

    #Instruction move
     text_instruction = pygame.font.Font("miami.ttf", 14)
     text = text_instruction.render("Les fleches droite et gauche permettent de deplacer le paddle ", 1, (255, 255, 255))
     screen.blit(text, (200,220))
     text = text_instruction.render("dans le sens respective de la fleche. ", 1, (255, 255, 255))
     screen.blit(text, (200,235))


     keyright = Image("keyboardright.png",50,50)
     keyright.rect.x = 100
     keyright.rect.y = 200

     keyleft = Image("keyboardleft.png",50,50)
     keyleft.rect.x = 50
     keyleft.rect.y = 200

    #Instruction items
     itemagrandi = Image("Images/PNG/itemagrandi.png",100,25)
     itemagrandi.rect.x = 50
     itemagrandi.rect.y = 260
     text = text_instruction.render("Si votre paddle touche cet item, la taille du paddle augmente.", 1, (255, 255, 255))
     screen.blit(text, (200,270))

     itemretreci = Image("Images/PNG/itemretreci.png",100,25)
     itemretreci.rect.x = 50
     itemretreci.rect.y = 310
     text = text_instruction.render("Si votre paddle touche cet item, la taille du paddle retreci.", 1, (255, 255, 255))
     screen.blit(text, (200,320))

     itemfast = Image("Images/PNG/itemfast.png",100,25)
     itemfast.rect.x = 50
     itemfast.rect.y = 360
     text = text_instruction.render("Si votre paddle touche cet item, la vitesse de la balle augmente.", 1, (255, 255, 255))
     screen.blit(text, (200,370))

     itemslow = Image("Images/PNG/itemslow.png",100,25)
     itemslow.rect.x = 50
     itemslow.rect.y = 410
     text = text_instruction.render("Si votre paddle touche cet item, la vitesse du paddle retreci.", 1, (255, 255, 255))
     screen.blit(text, (200,420))

     itemlaser = Image("Images/PNG/itemlaser.png",100,25)
     itemlaser.rect.x = 50
     itemlaser.rect.y = 460
     text = text_instruction.render("Si votre paddle touche cet item, des lasers pouvant briser les briques sont ajoutes au paddle.", 1, (255, 255, 255))
     screen.blit(text, (200,470))

     itemaddball = Image("Images/PNG/itemaddball.png",100,25)
     itemaddball.rect.x = 50
     itemaddball.rect.y = 510
     text = text_instruction.render("Si votre paddle touche cet item, une balle supplementaire est ajoutee a l'ecran.", 1, (255, 255, 255))
     screen.blit(text, (200,520))

     all_item_list.add(keyright,keyleft,itemaddball,itemagrandi,itemfast,itemslow,itemlaser,itemretreci)
     continuer = True

     #TITLE
     draw_text('Instructions', menu, (255, 255, 255), screen, 300, 30)
    
     while continuer: 

        cancel_selected = menu.render('Retour', 1, (255, 255, 255))
        cancelrect = cancel_selected.get_rect()
        cancelrect.topleft = (30, 30)
        screen.blit(cancel_selected, cancelrect)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                    continuer = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
                x, y = event.pos
                if cancelrect.collidepoint(x,y):
                    continuer = False
        
        clock.tick(60)

        all_item_list.draw(screen)


        pygame.display.flip()

def stat():

     #Background
     background = pygame.image.load("Images/background.png").convert()
     background = pygame.transform.scale(background, size)
     screen.blit(background, (0,0))

     #TITLE
     draw_text('Mes statistiques', menu, (255, 255, 255), screen, 300, 30)

     continuer = True

     while continuer: 

        cancel_selected = menu.render('Retour', 1, (255, 255, 255))
        cancelrect = cancel_selected.get_rect()
        cancelrect.topleft = (30, 30)
        screen.blit(cancel_selected, cancelrect)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
                x, y = event.pos
                if cancelrect.collidepoint(x,y):
                    continuer = False
        
        clock.tick(60)
        
        pygame.display.flip()

def about():

     background = pygame.image.load("Images/background.png").convert()
     background = pygame.transform.scale(background, size)
     screen.blit(background, (0,0))

     continuer = True
     #TITLE
     draw_text('A propos de Brick Breaker', menu, (255, 255, 255), screen, 200, 30)


     while continuer: 

        cancel_selected = menu.render('Retour', 1, (255, 255, 255))
        cancelrect = cancel_selected.get_rect()
        cancelrect.topleft = (30, 30)
        screen.blit(cancel_selected, cancelrect)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
                x, y = event.pos
                if cancelrect.collidepoint(x,y):
                    continuer = False
        
        clock.tick(60)
        
        pygame.display.flip()

def custom():
     background = pygame.image.load("Images/background.png").convert()
     background = pygame.transform.scale(background, size)
     screen.blit(background, (0,0))
     all_custom_list = pygame.sprite.Group()

     imageball="Images/PNG/58-Breakout-Tiles.png"

     #input
     username = TextBox(300, 110, 200, 24, 24, 20, False)
     labelUsername = menu.render("Username:", 1, (255, 255, 255))
     indication = pygame.font.Font(None, 24)
     labelObligatoire = indication.render("(Obligatoire)", 1, (255, 255, 255))

     textboxes = [username]


     ball1 = Image("Images/ball2.png",50,50)
     ball1.rect.x = 200
     ball1.rect.y = 300
     text = font.render("Foot Ball", 1, (255, 255, 255))
     screen.blit(text, (200,400))
     all_custom_list.add(ball1)

     #TITLE
     draw_text('Personnalisation', menu, (255, 255, 255), screen, 250, 30)


     #Button Cancel 
     cancel_selected = menu.render('Retour', 1, (255, 255, 255))
     cancelrect = cancel_selected.get_rect()
     cancelrect.topleft = (30, 30)
     screen.blit(cancel_selected, cancelrect)

     #Button Jouer
     play_selected = menu.render('Jouer', 1, (255, 255, 255))
     playrect = play_selected.get_rect()
     playrect.topleft = (600, 30)
     screen.blit(play_selected, playrect)
     
     continuer = True

     while continuer: 

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                continuer=False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer=False
            for textbox in textboxes:
                textbox.handle_event(event)

            if event.type == MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
                x, y = event.pos
                if cancelrect.collidepoint(x,y):
                    continuer = False
                if playrect.collidepoint(x,y) and (len(username.text)>0) :
                    continuer = False
                    game(imageball)
                if ball1.rect.collidepoint(x,y):
                    imageball="Images/ball2.png"
                    print("selected")

        for textbox in textboxes:
            textbox.update()
            textbox.draw(screen)

        screen.blit(labelUsername, (80,100))
        screen.blit(labelObligatoire, (505,115))

        clock.tick(60)
        all_custom_list.draw(screen)

        pygame.display.flip()

def game(imageball):
    background = pygame.image.load("Images/background.png").convert()
    background = pygame.transform.scale(background, size)


    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    #Create the Paddle
    paddle = Paddle(100, 20)
    paddle.rect.x = 350
    paddle.rect.y = 560

    #Create the ball
    ball = Ball(imageball,20,20)
    ball.rect.x = 400
    ball.rect.y = 561

    all_bricks = pygame.sprite.Group()

    for i in range(7):
        brick = Brick(3, 80, 30)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 60
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(7):
        brick = Brick(2, 80, 30)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 100
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(7):
        brick = Brick(1, 80, 30)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 140
        all_sprites_list.add(brick)
        all_bricks.add(brick)

    # Add the paddle to the list of sprites
    all_sprites_list.add(paddle)
    all_sprites_list.add(ball)
    continuer = True

    score = 0
    lives = 3
    
    # -------- Main Program Loop -----------
    while continuer:

        if lives == 0:
            continuer = False
        # --- Main event looP
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left()

        if keys[pygame.K_RIGHT]:
            paddle.move_right()

        all_sprites_list.update()

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                #PARA INSERT DATA
                continuer = False # Flag that we are done so we exit this loop

            # PAUSE
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                while True:  # Infinite loop that will be broken when the user press the space bar again
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        break  # Exit infinite loop

        if pygame.sprite.collide_mask(ball, paddle):
            ball.flip_direction_y()


        ball.move()
            #ball.rect.x -= ball.velocity[0]
            #ball.rect.y -= ball.velocity[1]
            #ball.bounce()

        #Bloque le paddle
        paddle.leaves_screen_sides()

        #print(ball.rect.y)

        if ball.lose():
            ball.rect.x = 350
            ball.rect.y = 200
            ball.move()

            while True:  # Infinite loop that will be broken when the user press the space bar again
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    break  # Exit infinite loop

            lives -= 1


        if ball.leaves_screen():
        # reset the ball position
            ball.rect.x = 200
            ball.rect.y = 300

        # Check if there is a car collision
        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
        for brick in brick_collision_list:
            ball.flip_direction_y()
            #ball.flip_direction_x()
            score += 1

            if brick.coup <= 0:
                brick.kill()
            else:
                brick.touche()

            if len(all_bricks) == 0:
                # Display Level Complete Message for 3 seconds
                #font = pygame.font.Font(None, 74)
                #text = font.render("LEVEL COMPLETE", 1, WHITE)
                #screen.blit(text, (200, 300))
                pygame.display.flip()
                pygame.time.wait(3000)

                # Stop the Game
                continuer = False

        # if ball.rect.x >= 760:
        #     ball.velocity[0] = -ball.velocity[0]
        # if ball.rect.x <= 0:
        #     ball.velocity[0] = -ball.velocity[0]
        # if ball.rect.y > 590:
        #     ball.velocity[1] = -ball.velocity[1]
        # if ball.rect.y < 60:
        #     ball.velocity[1] = -ball.velocity[1]

        # --- Drawing code should go here
        # First, clear the screen to dark blue. 
        screen.blit(background, (0,0))
      

        pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
    
        #Display the score and the number of lives at the top of the screen
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
main()
    #Once we have exited the main program loop we can stop the game engine:
pygame.quit()