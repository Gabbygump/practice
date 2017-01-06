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
BLUE = (75, 200, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
BROWN = (102, 51 , 0)
GREY = (210, 210, 210)
DARKGREY = ( 125, 125, 125)
YELLOW = (253,253,0)
DARKBLUE = (0,153,255)
def draw_cloud(x, y):
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])

''' make clouds '''
clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,300)
    clouds.append([x, y])

''' make stars '''
stars = []
for n in range(800):
    x = random.randrange(0, 1600)
    y = random.randrange(0, 800)
    r = random.randrange(1, 5)
    stars.append([x, y, r, r])
    
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

    ''' move stars '''
    for s in stars:
        s[1] += 6

        if s[1] > 700:
          
            s[0] = random.randrange(50, 2000)
            s[1] = random.randrange (-200,0)

            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(DARKGREY)
    '''TREE/GRASS'''
    pygame.draw.rect(screen, BROWN, [100, 410, 40, 300])
    pygame.draw.rect(screen, GREEN, [0, 580, 800, 50])
    pygame.draw.ellipse(screen, GREEN, [20, 330, 210, 180])
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
    pygame.draw.ellipse(screen, RED, [100, 380, 20, 20])

    '''sun'''
    pygame.draw.ellipse(screen, DARKGREY, [650, 0, 150, 150])
    
    ''' clouds '''
    for c in clouds:
        draw_cloud(c[0], c[1])

    ''' fence '''
    y = 540
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 570], [800, 570], 5)
    pygame.draw.line(screen, WHITE, [0, 560], [800, 560], 5)
    
    ''' fence 2 '''
    y = 540
    for x in range(5, 335, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 570], [320, 570], 5)
    pygame.draw.line(screen, WHITE, [0, 560], [320, 560], 5)

    '''house'''
    pygame.draw.rect(screen, GREY, [320, 390, 280, 620])
    pygame.draw.rect(screen, DARKGREY, [420, 440, 80, 180])
    pygame.draw.rect(screen, WHITE, [330, 420, 60, 60])
    pygame.draw.rect(screen, DARKGREY, [560, 330, 40, 60])
    pygame.draw.polygon(screen,BLACK, [[320, 390], [460,240], [600, 390]],)
    pygame.draw.ellipse(screen, BLACK, [480, 510, 20, 20])
    pygame.draw.rect(screen, WHITE, [330, 500, 60, 60])
    pygame.draw.rect(screen, WHITE, [530, 500, 60, 60])
    pygame.draw.rect(screen, WHITE, [530, 420, 60, 60])
    pygame.draw.rect(screen, GREEN, [0, 580, 800, 50])

    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, DARKBLUE, s)


    
    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
