import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    VERSION = pygame.version.ver
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    asteroids_field = AsteroidField()

    print(f"Starting Asteroids with pygame version:{VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   

    while True:
        log_state()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000.0
        updatable.update(dt)
        
        
    

if __name__ == "__main__":
    main()

