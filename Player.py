import pygame


class Player(object):
    def __init__(self, x, y, width, height):
        self.hearth = pygame.transform.scale(pygame.image.load("res/heart_zivot.png"), (10, 10))
        self.walkRight = [pygame.image.load('res/R1.png'), pygame.image.load('res/R2.png'),
                          pygame.image.load('res/R3.png'),
                          pygame.image.load('res/R4.png'), pygame.image.load('res/R5.png'),
                          pygame.image.load('res/R6.png'),
                          pygame.image.load('res/R7.png'), pygame.image.load('res/R8.png'),
                          pygame.image.load('res/R9.png')]
        self.walkLeft = [pygame.image.load('res/L1.png'), pygame.image.load('res/L2.png'),
                         pygame.image.load('res/L3.png'),
                         pygame.image.load('res/L4.png'), pygame.image.load('res/L5.png'),
                         pygame.image.load('res/L6.png'),
                         pygame.image.load('res/L7.png'), pygame.image.load('res/L8.png'),
                         pygame.image.load('res/L9.png')]
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.maxJump = 7
        self.jumpCount = self.maxJump
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 5
        self.get_hit = pygame.time.get_ticks()

    def draw(self, win):

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        for i in range(self.health):
            win.blit(self.hearth, (self.x + i * 11, self.y))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        # pygame.draw.circle(win, (255,0,0), (self.x, self.y), 2)

    def hit(self, win):
        print(self.get_hit - pygame.time.get_ticks())
        if self.get_hit - pygame.time.get_ticks() < -2000:
            self.get_hit = pygame.time.get_ticks()
            self.health -= 1
            print(self.health)
            if self.health < 1:
                self.isJump = False
                self.jumpCount = self.maxJump
                self.health = 5
                self.walkCount = 0
                return True

        return False
