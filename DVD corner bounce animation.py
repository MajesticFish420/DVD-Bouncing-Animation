import pygame
import random

def changeColour(logo, currentColour):
    logoColours = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    logo = pygame.PixelArray(logo)
    newColour = random.choice([i for i in logoColours if i != currentColour])
    logo.replace(currentColour, newColour)
    currentColour = newColour
    logo = logo.make_surface()
    return logo, currentColour
    
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect((375, 275, 200, 90))

logo = pygame.image.load("C:/Users/Alasdair/Desktop/Coding/Projects for jobs/DVD corner bounce animation/DVD_logo.jpg")
logo = pygame.transform.scale(logo, (200, 100))
currentColour = (0, 0, 0)
logo, currentColour = changeColour(logo, currentColour)

pygame.display.set_caption("DVD logo bounce")

horiMovement = random.choice((0.5, -0.5))/2
vertMovement = random.choice((0.5, -0.5))/2

horiPos = player[0] + horiMovement
vertPos = player[1] + vertMovement

run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 0, 0), player)
    screen.blit(logo, (horiPos, vertPos))

    horiPos = horiPos + horiMovement
    vertPos = vertPos + vertMovement
    player[0] = round(horiPos)
    player[1] = round(vertPos)

    # Border Wall
    # Left Side
    if player.left < 0:
        player.left = 1
        horiMovement = 0-horiMovement
        logo, currentColour = changeColour(logo, currentColour)

    # Right Side
    elif player.right > screen_width:
        player.right = screen_width - 1
        horiMovement = 0-horiMovement
        logo, currentColour = changeColour(logo, currentColour)

    # Top side
    if player.top < 0:
        player.top = 2
        vertMovement = 0-vertMovement
        logo, currentColour = changeColour(logo, currentColour)

    # Bottom side
    elif player.bottom > screen_height:
        player.bottom = screen_height - 2
        vertMovement = 0-vertMovement
        logo, currentColour = changeColour(logo, currentColour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()