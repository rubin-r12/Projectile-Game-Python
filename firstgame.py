import pygame
pygame.init() #initializing pygame

#Create a window
win = pygame.display.set_mode((500, 480)) #window size

pygame.display.set_caption("First Game") #window name

walkRight = [pygame.image.load('sprites/R1.png'), pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png'), pygame.image.load('sprites/R4.png'), pygame.image.load('sprites/R5.png'), pygame.image.load('sprites/R6.png'), pygame.image.load('sprites/R7.png'), pygame.image.load('sprites/R8.png'), pygame.image.load('sprites/R9.png')]
walkLeft = [pygame.image.load('sprites/L1.png'), pygame.image.load('sprites/L2.png'), pygame.image.load('sprites/L3.png'), pygame.image.load('sprites/L4.png'), pygame.image.load('sprites/L5.png'), pygame.image.load('sprites/L6.png'), pygame.image.load('sprites/L7.png'), pygame.image.load('sprites/L8.png'), pygame.image.load('sprites/L9.png')]
bg = pygame.image.load('sprites/bg.jpg')
char = pygame.image.load('sprites/standing.png')

clock  = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 10

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0)) #filling background image
    
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    pygame.display.update() # Refresh the window

#mainloop
run = True
while(run):
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Enabling the close button
            run = False

    keys = pygame.key.get_pressed()

    # Navigating the character

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel: # Restricting within window along x-axis
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
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

    redrawGameWindow()

pygame.quit()