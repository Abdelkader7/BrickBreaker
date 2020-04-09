# Import the pygame library and initialise the game engine
import pygame
from pygame.locals import *

from Paddle import Paddle
from Ball import Ball
from Image import Image
from TextBox import TextBox
from Square import Square
from Pouvoir import Pouvoir
from Brick import Brick


clock = pygame.time.Clock()
from Brick import Brick

pygame.init()


#Colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

#FALLING SPEED
POWER_FALLING_SPEED = 2
BONUS_FALLING_SPEED = 5

# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Brick Breaker")

background1 = pygame.image.load("Images/main1.png").convert()
background2 = pygame.image.load("Images/main2.png").convert()
background3 = pygame.image.load("Images/main3.png").convert()
background4 = pygame.image.load("Images/main4.png").convert()


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
    

        all_sprites_list.update()

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

  
     
     #rectangle vide à l'intérieur
     #pygame.draw.rect(screen,(255,255,255),(200,150,500,50),width=3)

     #screen.blit(test,(100,100))
    #Bloc transparent rule
     window_rule = pygame.Surface((630,120), pygame.SRCALPHA) 
     window_rule.fill((0,0,0,128))       
     screen.blit(window_rule, (100,80))
     text_instruction = pygame.font.Font("miami.ttf", 14)

     text = font.render("Regle du jeu : ", 1, (255, 255, 255))
     screen.blit(text, (350,100))
     rule = pygame.font.Font(None, 15)
     text = text_instruction.render("Il faut casser toutes les briques en faisant rebondir la balle sur la plateforme et sans la faire tomber. ", 1, (255, 255, 255))
     screen.blit(text, (110,130))
     live = Image("Images/PNG/60-Breakout-Tiles.png",30,30)
     live.rect.x = 110
     live.rect.y = 150
     text = font.render("x3 ", 1, (255, 255, 255))
     screen.blit(text, (145,160))
     text = text_instruction.render("Vous commencez le jeu avec 3 credits et tous les 10000pts vous gagnez une vie. ", 1, (255, 255, 255))
     screen.blit(text, (170,160))
     #Points
     brique = Image("Images/PNG/05-Breakout-Tiles.png",50,20)
     brique.rect.x = 185
     brique.rect.y = 175
     text = text_instruction.render("= 100pts ", 1, (255, 255, 255))
     screen.blit(text, (240,180))

     demi = Image("Images/PNG/23-Breakout-Tiles.png",20,20)
     demi.rect.x = 300
     demi.rect.y = 175
     text = text_instruction.render("= 200pts ", 1, (255, 255, 255))
     screen.blit(text, (330,180))

     capsule = Image("Images/PNG/40-Breakout-Tiles.png",60,20)
     capsule.rect.x = 390
     capsule.rect.y = 175
     text = text_instruction.render("= 500pts ", 1, (255, 255, 255))
     screen.blit(text, (475,180))
     
     


     #Bloc transparent power 
     window_transparent = pygame.Surface((590,350), pygame.SRCALPHA) 
     window_transparent.fill((0,0,0,128))       
     screen.blit(window_transparent, (200,230))

    #Instruction move
     text = text_instruction.render("Les fleches droite et gauche permettent de deplacer le paddle ", 1, (255, 255, 255))
     screen.blit(text, (200,250))
     text = text_instruction.render("dans le sens respective de la fleche. ", 1, (255, 255, 255))
     screen.blit(text, (200,265))


     keyright = Image("keyboardright.png",50,50)
     keyright.rect.x = 100
     keyright.rect.y = 230

     keyleft = Image("keyboardleft.png",50,50)
     keyleft.rect.x = 50
     keyleft.rect.y = 230

    #Instruction items
     itemagrandi = Image("Images/PNG/itemagrandi.png",100,25)
     itemagrandi.rect.x = 50
     itemagrandi.rect.y = 290
     text = text_instruction.render("Si votre paddle touche cet item, la taille du paddle augmente.", 1, (255, 255, 255))
     screen.blit(text, (200,300))

     itemretreci = Image("Images/PNG/itemretreci.png",100,25)
     itemretreci.rect.x = 50
     itemretreci.rect.y = 340
     text = text_instruction.render("Si votre paddle touche cet item, la taille du paddle retreci.", 1, (255, 255, 255))
     screen.blit(text, (200,350))

     itemfast = Image("Images/PNG/itemfast.png",100,25)
     itemfast.rect.x = 50
     itemfast.rect.y = 390
     text = text_instruction.render("Si votre paddle touche cet item, la vitesse de la balle augmente.", 1, (255, 255, 255))
     screen.blit(text, (200,400))

     itemslow = Image("Images/PNG/itemslow.png",100,25)
     itemslow.rect.x = 50
     itemslow.rect.y = 440
     text = text_instruction.render("Si votre paddle touche cet item, la vitesse du paddle retreci.", 1, (255, 255, 255))
     screen.blit(text, (200,450))

     itemlaser = Image("Images/PNG/itemlaser.png",100,25)
     itemlaser.rect.x = 50
     itemlaser.rect.y = 490
     text = text_instruction.render("Si votre paddle touche cet item, des lasers pouvant briser les briques sont ajoutes au paddle.", 1, (255, 255, 255))
     screen.blit(text, (200,500))

     itemaddball = Image("Images/PNG/itemaddball.png",100,25)
     itemaddball.rect.x = 50
     itemaddball.rect.y = 540
     text = text_instruction.render("Si votre paddle touche cet item, une balle supplementaire est ajoutee a l'ecran.", 1, (255, 255, 255))
     screen.blit(text, (200,550))

     all_item_list.add(keyright,keyleft,itemaddball,itemagrandi,itemfast,itemslow,itemlaser,itemretreci,live,brique,capsule,demi)
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
     background = "Images/background.png"
     Loadbackground = pygame.image.load(background).convert()
     Loadbackground = pygame.transform.scale(Loadbackground, size)
     screen.blit(Loadbackground, (0,0))
     all_custom_list = pygame.sprite.Group()

     imageball="Images/PNG/58-Breakout-Tiles.png"

     #input
     username = TextBox(300, 110, 200, 24, 24, 20, False)
     labelUsername = menu.render("Username:", 1, (255, 255, 255))
     indication = pygame.font.Font(None, 24)
     labelObligatoire = indication.render("(Obligatoire)", 1, (255, 255, 255))

     textboxes = [username]
     
     #Ball Choice
     draw_text('Choix de la balle :', indication, (255, 255, 255), screen, 70, 180)
     ball1 = Image("Images/PNG/58-Breakout-Tiles.png",50,50)
     ball1.rect.x = 90
     ball1.rect.y = 200
     text = font.render("Metal Ball", 1, (255, 255, 255))
     screen.blit(text, (70,265))
     ball2 = Image("Images/ball2.png",50,50)
     ball2.rect.x = 240
     ball2.rect.y = 200
     text = font.render("Foot Ball", 1, (255, 255, 255))
     screen.blit(text, (220,265))
     ball3 = Image("Images/ball5.png",50,50)
     ball3.rect.x = 390
     ball3.rect.y = 200
     text = font.render("Kirby Ball", 1, (255, 255, 255))
     screen.blit(text, (370,265))

     #Background Choice
     draw_text("Choix du fond d'ecran :", indication, (255, 255, 255), screen, 70, 350)

     background1 = Image("Images/background.png",200,150)
     background1.rect.x = 50
     background1.rect.y = 370
     text = font.render("Montagne", 1, (255, 255, 255))
     screen.blit(text, (100,550))

     background2 = Image("Images/Beach.gif",200,150)
     background2.rect.x = 300
     background2.rect.y = 370
     text = font.render("Plage", 1, (255, 255, 255))
     screen.blit(text, (350,550))

     background3 = Image("Images/Temple.png",200,150)
     background3.rect.x = 550
     background3.rect.y = 370
     text = font.render("Temple", 1, (255, 255, 255))
     screen.blit(text, (600,550))



     all_custom_list.add(ball1,ball2,ball3,background3,background1,background2)

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
                if ball1.rect.collidepoint(x,y):
                    imageball="Images/PNG/58-Breakout-Tiles.png"
                if ball2.rect.collidepoint(x,y):
                    imageball="Images/ball2.png"
                if ball3.rect.collidepoint(x,y):
                    imageball="Images/ball5.png"
                if background1.rect.collidepoint(x,y):
                    background="Images/background.png"
                if background2.rect.collidepoint(x,y):
                    background="Images/Beach.gif"
                if background3.rect.collidepoint(x,y):
                    background="Images/Temple.png"
                if cancelrect.collidepoint(x,y):
                    continuer = False
                if playrect.collidepoint(x,y) and (len(username.text)>0) :
                    continuer = False
                    game(imageball,background)
                    
                
        for textbox in textboxes:
            textbox.update()
            textbox.draw(screen)

        screen.blit(labelUsername, (80,100))
        screen.blit(labelObligatoire, (505,115))

        clock.tick(60)
        all_custom_list.draw(screen)

        pygame.display.flip()




def game(imageball,background):
    background = pygame.image.load(background).convert()
    background = pygame.transform.scale(background, size)


    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    #Create the Paddle
    paddle = Paddle(100, 20)
    paddle.rect.x = 350
    paddle.rect.y = 560

    #Create the ball
    ball = Ball(imageball,25,25)
    ball.rect.x = 400
    ball.rect.y = 250

    all_bricks = pygame.sprite.Group()

    for i in range(8):
        brick = Brick(3, 70, 30)
        brick.rect.x = 20 + i * 100
        brick.rect.y = 60
        all_sprites_list.add(brick)
        all_bricks.add(brick)

    for i in range(8):
        brick = Brick(2, 70, 30)
        brick.rect.x = 20 + i * 100
        brick.rect.y = 100
        all_sprites_list.add(brick)
        all_bricks.add(brick)

    for i in range(8):
        brick = Brick(1, 70, 30)
        brick.rect.x = 20 + i * 100
        brick.rect.y = 140
        all_sprites_list.add(brick)
        all_bricks.add(brick)

    #
    # for i in range(7):
    #     square = Square(3, 30, 30)
    #     square.rect.x = 60 + i * 100
    #     square.rect.y = 190
    #     all_sprites_list.add(square)
    #     all_bricks.add(square)
    #
    # for i in range(7):
    #     square = Square(3, 30, 30)
    #     square.rect.x = 110 + i * 100
    #     square.rect.y = 190
    #     all_sprites_list.add(square)
    #     all_bricks.add(square)



    # Add the paddle to the list of sprites
    all_sprites_list.add(paddle)
    all_sprites_list.add(ball)
    continuer = True

    def pause():
        paused = True 
        #Button Jouer
        RR = menu.render('Jouer', 1, (0, 0, 255))
        playRrect = RR.get_rect()
        playRrect.topleft = (600, 30)
        screen.blit(RR, playRrect)

        while paused:
            for event in pygame.event.get():
              # Infinite loop that will be broken when the user press the space bar again
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
            test = pygame.Surface((800,600), pygame.SRCALPHA) 
            test.fill((255,255,255))
            screen.blit(test, (0,0))
            draw_text('PAUSE', menu, (0, 0, 0), screen, 300, 200)
            draw_text('REPRENDRE LA PARTIE', menu, (0, 0, 0), screen, 300, 300)
            draw_text('QUITTER LA PARTIE', menu, (0, 0, 0), screen, 300, 400)
            pygame.display.update()
            clock.tick(5)
            #event = pygame.event.wait()
               #     draw_text('PAUSE', menu, (255, 255, 255), screen, 300, 100)
                #    if event.type == pygame.KEYDOWN and 
                #        break  # Exit infinite loop
    pygame.display.flip() 

    score = 0
    lives = 50

    liste_pouvoir = []
    ball_2_active = False

    # pouvoir = Pouvoir()
    # pouvoir.rect.x = 500
    # pouvoir.rect.y = 350
    # all_sprites_list.add(pouvoir)

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

        #all_sprites_list.update()

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                continuer = False # Flag that we are done so we exit this loop
                # PAUSE
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause()
                #while True:  # Infinite loop that will be broken when the user press the space bar again
                    #event = pygame.event.wait()
                    #draw_text('PAUSE', menu, (255, 255, 255), screen, 300, 100)
                   # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                      #  break  # Exit infinite loop
    
       
        # --- Game logic should go here

        ball.move()


        for pouvoir in liste_pouvoir:
            if pouvoir.rect.y <= 530:
                pouvoir.rect.y += POWER_FALLING_SPEED
            else:
                liste_pouvoir.pop(liste_pouvoir.index(pouvoir))
                pouvoir.kill()

            if pygame.sprite.collide_mask(pouvoir, paddle):
                if pouvoir.rand_pouvoir == 1:
                    pouvoir.agrandir(paddle)
                    pouvoir.kill()
                elif pouvoir.rand_pouvoir == 2:
                    pouvoir.accelerer(ball)
                    pouvoir.kill()
                elif pouvoir.rand_pouvoir == 3:
                    pouvoir.ralenti(ball)
                    pouvoir.kill()
                elif pouvoir.rand_pouvoir == 4:
                    pouvoir.retrecissement(paddle)
                    pouvoir.kill()
                elif pouvoir.rand_pouvoir == 5:
                    if ball_2_active is False:
                        ball_2_active = True
                        extra_ball = Ball(imageball, 25, 25)
                        extra_ball.rect.x = 400
                        extra_ball.rect.y = 250
                        all_sprites_list.add(extra_ball)
                        pouvoir.kill()
                elif pouvoir.rand_pouvoir == 6:
                    pouvoir.laser(paddle)
                    pouvoir.kill()
                elif pouvoir.rand_pouvoir == 7:
                    score = score + 50
                    pouvoir.kill()

               # elif pouvoir.rand_pouvoir == 5:
                #elif pouvoir.rand_pouvoir == 6:
                #elif pouvoir.rand_pouvoir == 7:

        if 'extra_ball' in globals():
            if extra_ball.lose():
                extra_ball.kill()

        if ball_2_active:
            if pygame.sprite.collide_mask(extra_ball, paddle):
                extra_ball.flip_direction_y()
            extra_ball.move()
            extra_ball.leaves_screen()

            element_collision_list = pygame.sprite.spritecollide(extra_ball, all_bricks, False)
            for element in element_collision_list:
                ball.flip_direction_y()
                # ball.flip_direction_x()

                if element.touche():
                    if isinstance(element, Brick):
                        score += 100
                        pouvoir = Pouvoir()
                        pouvoir.rect.x = element.rect.x
                        pouvoir.rect.y = element.rect.y
                        liste_pouvoir.append(pouvoir)

                        # DROP POUVOIR

                        # if hasattr(element, 'pouvoir') and element.pouvoir != 0:
                        # DROP BONUS
                        # if hasattr(element, 'bonus') and element.bonus != 0:
                        #     element.bonus.rect.y = element.rect.y
                        #     element.bonus.rect.y = element.bonus.rect.y + BONUS_FALLING_SPEED
                    if isinstance(element, Square):
                        score += 200

                if len(all_bricks) == 0:
                    # Display Level Complete Message for 3 seconds
                    # font = pygame.font.Font(None, 74)
                    text = font.render("LEVEL COMPLETE", 1, WHITE)
                    screen.blit(text, (200, 300))
                    pygame.display.flip()
                    pygame.time.wait(3000)

                    # Stop the Game
                    continuer = False

        for pouvoir in liste_pouvoir:
            all_sprites_list.add(pouvoir)

        if pygame.sprite.collide_mask(ball, paddle):
            ball.flip_direction_y()




        #if ball.leaves_screen_bottom():
        # reset the ball position
          #  ball.rect.x = 200
         #   ball.rect.y = 300

        #for brick in liste_brick:
         #   if pygame.sprite:
          #      ball.flip_direction_x()
        all_sprites_list.update()
        

        #Bloque le paddle
        paddle.leaves_screen_sides()

        #print(ball.rect.y)




        if ball.lose():
            ball.reinitialiser_position()
            paddle.reinitialiser_position()
            for pouvoir in liste_pouvoir:
                pouvoir.kill()
            liste_pouvoir = []
            ball.move()

            while True:  # Infinite loop that will be broken when the user press the space bar again
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    break  # Exit infinite loop

            lives -= 1
            ball_2_active = False


        ball.leaves_screen()

        # Check if there is a car collision
        element_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
        for element in element_collision_list:
            ball.flip_direction_y()
            # ball.flip_direction_x()

            if element.touche():
                if isinstance(element, Brick):
                    score += 100
                    pouvoir = Pouvoir()
                    pouvoir.rect.x = element.rect.x
                    pouvoir.rect.y = element.rect.y
                    liste_pouvoir.append(pouvoir)

                    # DROP POUVOIR

                    #if hasattr(element, 'pouvoir') and element.pouvoir != 0:
                    # DROP BONUS
                    # if hasattr(element, 'bonus') and element.bonus != 0:
                    #     element.bonus.rect.y = element.rect.y
                    #     element.bonus.rect.y = element.bonus.rect.y + BONUS_FALLING_SPEED
                if isinstance(element, Square):
                    score += 200

            if len(all_bricks) == 0:
                # Display Level Complete Message for 3 seconds
                #font = pygame.font.Font(None, 74)
                text = font.render("LEVEL COMPLETE", 1, WHITE)
                screen.blit(text, (200, 300))
                pygame.display.flip()
                pygame.time.wait(3000)

                # Stop the Game
                continuer = False




        # --- Drawing code should go here
        # First, clear the screen to dark blue.
        screen.blit(background, (0, 0))
      

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