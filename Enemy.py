import pygame


class Enemy(object):
    walkRight = [pygame.image.load("res/R1E.png"), pygame.image.load("res/R2E.png"), pygame.image.load("res/R3E.png"),
                 pygame.image.load("res/R4E.png"), pygame.image.load("res/R5E.png"), pygame.image.load("res/R6E.png"),
                 pygame.image.load("res/R7E.png"), pygame.image.load("res/R8E.png"), pygame.image.load("res/R9E.png"),
                 pygame.image.load("res/R10E.png"), pygame.image.load("res/R11E.png")]
    walkLeft = [pygame.image.load("res/L1E.png"), pygame.image.load("res/L2E.png"), pygame.image.load("res/L3E.png"),
                pygame.image.load("res/L4E.png"), pygame.image.load("res/L5E.png"), pygame.image.load("res/L6E.png"),
                pygame.image.load("res/L7E.png"), pygame.image.load("res/L8E.png"), pygame.image.load("res/L9E.png"),
                pygame.image.load("res/L10E.png"), pygame.image.load("res/L11E.png")]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0),
                             (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50 / 10) * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False

