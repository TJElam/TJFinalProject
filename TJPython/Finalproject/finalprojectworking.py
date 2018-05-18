# instructions from youtube channel Tech with Tim
import pygame

pygame.init()
# inicate pygame
win = pygame.display.set_mode((700,500))

pygame.display.set_caption("First Game")

screenwidth = 500

x = 50
y = 440
width = 30
height = 30
vel = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # list
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) ** 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    # character is created)

 

pygame.quit



# need module, create a from blank import blank
# need class
# need function
# needs to be organized
# submit something to disscussion 
# use readme 