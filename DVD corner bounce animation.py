import pygame
import random

class Logo:

    logoWidth = 195
    logoHeight = 90
    screenWidth = 0
    screenHeight = 0
    
    def __init__(self, logoImage, xPos, yPos, currentColour, horiMovement, vertMovement):
        self.logoImage = logoImage
        self.xPos = xPos
        self.yPos = yPos
        self.currentColour = currentColour
        self.horiMovement = horiMovement
        self.vertMovement = vertMovement

    def changeLogoPosition(self):
        self.xPos += self.horiMovement
        self.yPos += self.vertMovement

    def randomColour(self):
        #RGB values
        logoColours = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
        return random.choice([i for i in logoColours if i != self.currentColour])

    def changeLogoColour(self):
        newColour = self.randomColour()
        newImage = pygame.PixelArray(self.logoImage)
        newImage.replace(self.currentColour, newColour)
        self.logoImage = newImage.make_surface()
        self.currentColour = newColour
            
    def enforcedScreenBorder(self):
        value = False
        # Left and Right borders
        if self.xPos < 0:
            self.xPos = 1
            self.horiMovement = -self.horiMovement
            value = True
        elif self.xPos > Logo.screenWidth - Logo.logoWidth:
            self.xPos = Logo.screenWidth - Logo.logoWidth - 1
            self.horiMovement = -self.horiMovement
            value = True
        # Top and Bottom borders
        if self.yPos < 0:
            self.yPos = 1
            self.vertMovement = -self.vertMovement
            value = True
        elif self.yPos > Logo.screenHeight - Logo.logoHeight:
            self.yPos = Logo.screenHeight - Logo.logoHeight - 1
            self.vertMovement = -self.vertMovement
            value = True
        return value

Logo.screenWidth = 1000
Logo.screenHeight = 800
logoArray = []
pygame.init()
pygame.event.set_allowed([pygame.QUIT])

clock = pygame.time.Clock()

logoImage = pygame.image.load("DVD_logo.jpg")
logoScaled = pygame.transform.scale(logoImage, (200, 100))
logoPixel = pygame.PixelArray(logoScaled)
# Could do .replace but this method removes the edges that were not changed. It changes it to white
for i in range(len(logoPixel)):
    for n in range(len(logoPixel[i])):
        if logoPixel[i][n] != 0:
            logoPixel[i][n] = -1

print("Please specify number: ", end="")
quantity = None
while quantity == None:
    quantity = input()
    try:
        int(quantity)
    except:
        print("Must be a whole number!")
        quantity = None
    else:
        if int(quantity) <= 0:
            print("Must be larger than 0!")
            quantity = None

screen = pygame.display.set_mode((Logo.screenWidth, Logo.screenHeight), vsync=1)
pygame.display.set_caption("DVD logo bounce")

for i in range(int(quantity)):
    horiMovement = random.choice((0.25, -0.25))
    vertMovement = random.choice((0.25, -0.25))
    randomX = random.randint(0, Logo.screenWidth - Logo.logoWidth)
    randomY = random.randint(0, Logo.screenHeight - Logo.logoHeight)
    logoFinal = logoPixel.make_surface().convert_alpha()
    logoArray.append(Logo(logoFinal, randomX, randomY, (255, 255, 255), horiMovement, vertMovement))

run = True
frameCounter = 0
while run:
    screen.fill((0, 0, 0))

    for x in logoArray:
        x.changeLogoPosition()

    if frameCounter == 10:
        for x in logoArray:
            if x.enforcedScreenBorder():
                x.changeLogoColour()
        frameCounter = 0
        print(round(clock.get_fps()))

    for x in logoArray:
        screen.blit(x.logoImage, (x.xPos, x.yPos))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    clock.tick()
    
    frameCounter += 1

pygame.quit()