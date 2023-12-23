import pygame
import random

class logo:

    width = 200
    height = 100
    logoArray = []

    def __init__(self, logo, xPos, yPos, currentColour):
        self.logo = logo
        self.xPos = xPos
        self.yPos = yPos
        self.currentColour = currentColour
        self.horiMovement = horiMovement
        self.vertMovement = vertMovement
        logo.logoArray.append(self)

    def changeLogoColour(self):
        logoColours = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
        newColour = random.choice([i for i in logoColours if i != self.currentColour])
        self.logo = pygame.PixelArray(logo)
        self.logo.replace(self.currentColour, newColour)
        self.logo = self.logo.make_surface()
        self.currentColour = newColour

    def changeLogoPosition():
        for i in range(len(logo.logoArray)):
            logo.logoArray[i].xPos += logo.logoArray[i].horiMovement
            logo.logoArray[i].yPos += logo.logoArray[i].vertMovement

    def enforceScreenBorder():
        for i in range(len(logo.logoArray)):
            currentLogo = logo.logoArray[i]
            # Left border
            if currentLogo.xPos < 0:
                currentLogo.xPos = 1
                currentLogo.horiMovement = 0 - currentLogo.horiMovement
            # Right border
            elif currentLogo.xPos > screenWidth:
                currentLogo.xPos = screenWidth - 1
                currentLogo.horiMovement = 0 - currentLogo.horiMovement
            # Top border
            if currentLogo.yPos < 0:
                currentLogo.yPos = 1
                currentLogo.vertMovement = 0 - currentLogo.vertMovement
            # Bottom border
            elif currentLogo.yPos > screenHeight:
                currentLogo.yPos = screenHeight - 1
                currentLogo.vertMovement = 0 - currentLogo.vertMovement

def changeColour(logo, currentColour):
    logoColours = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
    newColour = random.choice([i for i in logoColours if i != currentColour])
    logo = pygame.PixelArray(logo)
    logo.replace(currentColour, newColour)
    logo = logo.make_surface()
    return logo, newColour

print("Please specify number of inputs: ")
quantity = None
while quantity == None:
    quantity = input()
    try:
        int(quantity)
    except:
        print("Must be a whole number")
        quantity = None
    else:
        if int(quantity) <= 0:
            print("Must be at least one")
            quantity = None

logoPositions = []

for i in range(int(quantity)):
    logoPositions.append([0, 0])

print(logoPositions)
    
pygame.init()
screenWidth = 1000
screenHeight = 800
hitboxWidth = 200
hitboxHeight = 90
screen = pygame.display.set_mode((screenWidth, screenHeight))

player = pygame.Rect((375, 275, hitboxWidth, hitboxHeight))

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

    pygame.draw.rect(screen, (255, 255, 255), player)
    screen.blit(logo, (horiPos, vertPos))

    horiPos = horiPos + horiMovement
    vertPos = vertPos + vertMovement
    player[0] = round(horiPos)
    player[1] = round(vertPos)

    # Border Wall
    # Left Side
    if player.left < 0:
        player.left = 1
        horiMovement = 0 - horiMovement
        logo, currentColour = changeColour(logo, currentColour)

    # Right Side
    elif player.right > screenWidth:
        player.right = screenWidth - 1
        horiMovement = 0 - horiMovement
        logo, currentColour = changeColour(logo, currentColour)

    # Top side
    if player.top < 0:
        player.top = 2
        vertMovement = 0 - vertMovement
        logo, currentColour = changeColour(logo, currentColour)

    # Bottom side
    elif player.bottom > screenHeight:
        player.bottom = screenHeight - 2
        vertMovement = 0 - vertMovement
        logo, currentColour = changeColour(logo, currentColour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()