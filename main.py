#Importing Libraries
import pygame
import sys
#Importing Modules
from logger import log_state, log_event
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS




def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #init game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #creating blank clock object
    game_clock, dt = pygame.time.Clock(), 0
    #Creating Screen size
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    #creating groups for easier object management
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Assigning class objects to the created groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    #init game objects
    player1 = Player(x, y, PLAYER_RADIUS)
    AsteroidField()
    
    #Starting game 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
     
        #adding fps
        time_delta = game_clock.tick(60)
        dt = time_delta / 1000
        #updating player
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player1):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
