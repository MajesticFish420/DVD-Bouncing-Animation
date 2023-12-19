import pygame
import random

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect((375, 275, 50, 50))

horiMovement = random.randint(-1000, 1000)
vertMovement = 1000 - abs(horiMovement)
vertMovement = random.choice((vertMovement, 0-vertMovement))

#/1000 to make the movement smaller than 1. /2 to adjust the speed a bit
horiMovement, vertMovement = (horiMovement/1000)/2, (vertMovement/1000)/2
horiPos = player[0] + horiMovement
vertPos = player[1] + vertMovement

corner = 0

run = True
while run:

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    horiPos = horiPos + horiMovement
    vertPos = vertPos + vertMovement
    player[0] = round(horiPos)
    player[1] = round(vertPos)

    # Check for corners
    """
    if player.left < 10 and player.top < 10:
        corner += 1
        print(corner)
    elif player.left < 10 and player.bottom > screen_width - 10:
        corner += 1
        print(corner)
    elif player.right > screen_width - 10 and player.top < 10:
        corner += 1
        print(corner)
    elif player.right > screen_width - 10 and player.bottom > screen_width - 10:
        corner +=1
        print(corner)
    """

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

    """
    # Movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    if key[pygame.K_d] == True:
        player.move_ip(1, 0)
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)
    if key[pygame.K_s] == True:
        player.move_ip(0, 1)
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()