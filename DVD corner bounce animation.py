import pygame
import random

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect((375, 275, 200, 100))
logo = pygame.image.load("DVD_logo.jpg")
logo = pygame.transform.scale(logo, (200, 100))

pygame.display.set_caption("DVD logo bounce")

horiMovement = random.choice((0.5, -0.5))
vertMovement = random.choice((0.5, -0.5))

#/1000 to make the movement smaller than 1. /2 to adjust the speed a bit
horiMovement, vertMovement = horiMovement/3, vertMovement/3
horiPos = player[0] + horiMovement
vertPos = player[1] + vertMovement


run = True
while run:

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 255, 255), player)
    screen.blit(logo, (horiPos, vertPos))

    horiPos = horiPos + horiMovement
    vertPos = vertPos + vertMovement
    player[0] = round(horiPos)
    player[1] = round(vertPos)

    # Border Wall
    if player.left < 0:
        player.left = 0
        horiMovement = 0-horiMovement
    elif player.right > screen_width:
        player.right = screen_width
        horiMovement = 0-horiMovement
    if player.top < 0:
        player.top = 0
        vertMovement = 0-vertMovement
    elif player.bottom > screen_height:
        player.bottom = screen_height
        vertMovement = 0-vertMovement

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()