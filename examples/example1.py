import pygame
import sys
from pyanimation import Animation

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255,255,255))
clock = pygame.time.Clock()

girl = Animation("images/spritesheet.png")
girl.create_animation(0, 0, 125, 125, 4, "run", duration=50, rows=4)

screen.blit(surface, (0, 0))

if __name__ == '__main__':
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        surface.fill((255,255,255))
        screen.blit(surface, (0,0))
        clock.tick(60)

        screen.blit(girl.update_surface(), (girl.x, girl.y))
        pygame.display.flip()
        pygame.display.update()
