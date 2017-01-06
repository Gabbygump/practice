# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (153, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
BROWN = (102, 51 , 0)
GREY = (210, 210, 210)
DARKGREY = ( 125, 125, 125)
YELLOW = (253,253,0)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

''' make clouds '''
clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    clouds.append([x, y])
    
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' move clouds '''
    for c in clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREY, [320, 390, 280, 620])
    pygame.draw.rect(screen, BROWN, [100, 410, 40, 300])
    pygame.draw.rect(screen, DARKGREY, [420, 440, 80, 180])
    pygame.draw.rect(screen, WHITE, [330, 420, 60, 60])
    pygame.draw.rect(screen, DARKGREY, [560, 330, 40, 60])
    pygame.draw.rect(screen, WHITE, [330, 500, 60, 60])
    pygame.draw.rect(screen, WHITE, [530, 500, 60, 60])
    pygame.draw.rect(screen, WHITE, [530, 420, 60, 60])
    pygame.draw.rect(screen, GREEN, [0, 580, 800, 50])
    pygame.draw.ellipse(screen, GREEN, [20, 330, 210, 180])
    pygame.draw.polygon(screen, BLACK, [[320, 390], [460,240], [600, 390]],)
    pygame.draw.ellipse(screen, BLACK, [480, 510, 20, 20])
    pygame.draw.ellipse(screen, YELLOW, [650, 0, 150, 150])
    pygame.draw.ellipse(screen, RED, [100, 440, 20, 20])
    pygame.draw.ellipse(screen, RED, [50, 430, 20, 20])
    pygame.draw.ellipse(screen, RED, [60, 460, 20, 20])
    pygame.draw.ellipse(screen, RED, [80, 420, 20, 20])
    pygame.draw.ellipse(screen, RED, [120, 420, 20, 20])
    pygame.draw.ellipse(screen, RED, [80, 390, 20, 20])
    pygame.draw.ellipse(screen, RED, [120, 390, 20, 20])
    pygame.draw.ellipse(screen, RED, [120, 390, 20, 20])
    pygame.draw.ellipse(screen, RED, [120, 345, 20, 20])
    pygame.draw.ellipse(screen, RED, [80, 345, 20, 20])
    pygame.draw.ellipse(screen, RED, [200, 420, 20, 20])
    ''' clouds '''
    for c in clouds:
        draw_cloud(c[0], c[1])

    '''fence'''
    
    
    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
