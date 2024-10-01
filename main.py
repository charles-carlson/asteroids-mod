import pygame
from constants import *
from player import *
from asteroids import Asteroid
from asteroidfield import *
# from module import function

def main():
    #initialzing  game and screen
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #container
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    dt = 0

    #instances
    #rendering player and asteroids
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0)) 
        
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0
        
        for updateable in updatables:
            updateable.update(dt)
            
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("GAME OVER")
                return
            
if __name__ == "__main__":
    main()