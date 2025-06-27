import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_rate = pygame.time.Clock()
    delta_time = 0
    player_object = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        
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
        player_object.update(delta_time)
        player_object.draw(screen)
        
        #goes at end
        pygame.display.flip()
        delta_time = frame_rate.tick(60) / 1000.0


if __name__ == "__main__":
    main()
