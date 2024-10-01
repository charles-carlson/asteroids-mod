import pygame
from constants import *
from player import *
# from module import function

def main():
    #initialzing  game and screen
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #rendering player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    #groups
    updatables = pygame.sprite.Group(player)
    drawables = pygame.sprite.Group(player)
    #container
    Player.containers = (updatables, drawables)

    dt = 0

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

if __name__ == "__main__":
    main()