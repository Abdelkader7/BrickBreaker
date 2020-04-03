import pygame
from pygame.locals import *

#Ecran de jeu 
#Resizable permet de pouvoir redimensionner la taille de la fenêtre 
display = pygame.display.set_mode((768,544), RESIZABLE)

#Background et conversion de l'image pour garder le même format de pixels
fond = pygame.image.load("Images/background.png").convert()
display.blit(fond, (0,0))

#Chargement et collage de la barre
paddle = pygame.image.load("Images/PNG/50-Breakout-Tiles.png").convert_alpha()
display.blit(paddle, (150,400))

position_paddle = paddle.get_rect()
display.blit(paddle, position_paddle)

Y=400

#Rafraîchissement de l'écran
pygame.display.flip()
continuer = 1

#Boucle infinie pour ne pas fermer la fenêtre
while continuer:
    for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
        
        if event.type == KEYLEFT: 
            if event.key == K_LEFT:
                Y=Y+3
				position_paddle = position_paddle.move(0,Y)

    #Re-collage
	display.blit(fond, (0,0))	
	display.blit(paddle, position_paddle)
	#Rafraichissement
	pygame.display.flip()
pygame.init()
