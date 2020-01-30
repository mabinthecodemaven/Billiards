### have watched the first two videos 1/22/20


import pygame
pygame.init()

win = pygame.display.set_mode((1400, 1000))
pygame.display.set_caption('Big Chungus')

x = 100
y = 80
width = 50
height = 100
vel = 5

isJump = False
jumpCount = 10
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit((255, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()


running = True
while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x + vel > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x + width + vel < 1400:
        x += vel

    if isJump:
        if jumpCount >= -10:
            if jumpCount >= 0:
                y -= (jumpCount **2) / 8
            else:
                y += (jumpCount **2) / 8
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    else:

        if keys[pygame.K_UP] and y + vel > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y + height + vel < 1000:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True


pygame.quit()
