import pygame
pygame.init() #initializing pygame

#Create a window
win = pygame.display.set_mode((500, 500)) #window size

pygame.display.set_caption("First Game") #window name

x = 50
y = 425
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True
while(run):
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Enabling the close button
            run = False

    keys = pygame.key.get_pressed()

    # Navigating the character

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel: # Restricting within window along x-axis
        x += vel

    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height -vel: # Restricting within window along y-axis
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg #to bring the character down
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    # Drawing the character
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update() # Refresh the window

pygame.quit()