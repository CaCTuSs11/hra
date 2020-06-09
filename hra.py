import pygame

from Enemy import Enemy
from Player import Player
from Projectile import Projectile

pygame.init()
S_WIDTH = 1600
S_HEIGHT = 900
win = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("First_Game")

bg = pygame.image.load('res/bg.jpg')
bg = pygame.transform.scale(bg, (S_WIDTH, S_HEIGHT))
char = pygame.image.load('res/standing.png')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('res/bullet.wav')
hitSound = pygame.mixer.Sound('res/hit.wav')
music = pygame.mixer.music.load('res/music.mp3')
pygame.mixer.music.play(-1)

score = 0

# mainloop
font = pygame.font.SysFont("comicsans", 30, True)
man = Player(300, S_HEIGHT - 74, 64, 64)
goblin = Enemy(100, S_HEIGHT - 74, 64, 64, 450)
shootLoop = 0
bullets = []
run = True


def update():
    global score, shootLoop
    if goblin.visible:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                if man.hit(win):
                    man.x = 300
                    man.y = S_HEIGHT - 74

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for bullet in bullets:
        if goblin.visible:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > \
                    goblin.hitbox[
                        1]:
                if goblin.hitbox[0] < bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    hitSound.play()
                    goblin.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
        if S_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


def render():
    win.blit(bg, (0, 0))  # pozadie
    text = font.render('score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (S_WIDTH / 2, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


def event_handler():
    global shootLoop, run
    keys = pygame.key.get_pressed()  # drzanie klaves
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # vypnutie hry

    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))
        shootLoop = 1
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < S_WIDTH - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount > 0:
            man.y -= (man.jumpCount ** 2)
            man.jumpCount -= 1
        elif man.jumpCount >= -man.maxJump:
            man.y -= -(man.jumpCount ** 2)
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = man.maxJump


while run:
    clock.tick(27)  # pustena hra
    event_handler()
    update()
    render()

pygame.quit()
# alt+enter= chyba
# alt+ctrl+l=formatovanie
