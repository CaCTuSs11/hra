import pygame
pygame.init()

win=pygame.display.set_mode((500,500))
pygame.display.set_caption("First")
screenWidth=500
screenHeight=500


x= 50
y= 450
width=40
height=60
vel=10           #postavičaka


isJump= False
jumpCount=10




run= True
while run:
    pygame.time.delay(30) #pustena hra

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run= False          #vypnutie hry

    keys=pygame.key.get_pressed()#drzanie klaves
    if keys[pygame.K_LEFT]and x>vel:
        x-= vel
    if keys[pygame.K_RIGHT]and x<screenWidth-width-vel:
        x+=vel
    if not(isJump):     
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount > 0:
            y -= (jumpCount **2)
            jumpCount -=1
        elif jumpCount>=-10:
            y -= -(jumpCount **2)
            jumpCount -=1
        else:
            isJump= False
            jumpCount= 10
    win.fill((0,0,0))#nerobi farebnu ciaru
    pygame.draw.rect(win, (255,0,0),(x,y,width,height))
    pygame.display.update()
    
pygame.quit()
