import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First_Game")
screenWidth = 500
screenHeight = 480

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))  # pozadie
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()


run = True
while run:
    clock.tick(27)  # pustena hra

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # vypnutie hry

    keys = pygame.key.get_pressed()  # drzanie klaves
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount > 0:
            y -= (jumpCount ** 2)
            jumpCount -= 1
        elif jumpCount >= -10:
            y -= -(jumpCount ** 2)
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    redrawGameWindow()

pygame.quit()
# alt+enter= chyba
# alt+ctrl+l=formatovanie
