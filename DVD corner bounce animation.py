import pygame
import random

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect((375, 275, 50, 50))

horiMovement = random.randint(-1000, 1000)
vertMovement = 1000 - abs(horiMovement)
horiMovement, vertMovement = horiMovement/1000, vertMovement/1000
horiPos = player[0] + horiMovement

run = True
while run:

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    horiPos = horiPos + horiMovement
    player[0] = round(horiPos)
    print(player[0])
    print(horiPos)

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

    # Border Wall 
    if player.left < 0:
        player.left = 0
    elif player.right > screen_width:
        player.right = screen_width
    if player.top < 0:
        player.top = 0
    elif player.bottom > screen_height:
        player.bottom = screen_height

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()