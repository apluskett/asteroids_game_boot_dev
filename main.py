import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_rate = pygame.time.Clock()
    delta_time = 0
        
    print("Starting Asteroids!")
    print(
f'''Screen width: {SCREEN_WIDTH} 
Screen height: {SCREEN_HEIGHT}
'''
        )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        
        #goes at end
        pygame.display.flip()
        delta_time = frame_rate.tick(60) / 1000.0


if __name__ == "__main__":
    main()
    