import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_rate = pygame.time.Clock()
    delta_time = 0
    
    # Initialize sprite groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Set up class containers
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    
    # Create game objects
    player_object = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    
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
        updateable.update(delta_time)
        for obj in drawable:
            obj.draw(screen)
        for asteroid in asteroids:
            if player_object.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return
             
        #goes at end
        pygame.display.flip()
        delta_time = frame_rate.tick(60) / 1000.0


if __name__ == "__main__":
    main()
