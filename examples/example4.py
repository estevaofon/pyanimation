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

link = Animation("images/link.png")
link.create_animation(0, 525, 120, 132, "front", duration=90, rows=1)
link.create_animation(0, 782, 120, 132, "back", duration=90, rows=1)


screen.blit(surface, (0, 0))

if __name__ == '__main__':
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    link.run("back")
                if event.key == pygame.K_DOWN:
                    link.run("front")


        surface.fill((255,255,255))
        screen.blit(surface, (0,0))
        clock.tick(60)

        screen.blit(link.update_surface(), (link.x, link.y))
        pygame.display.flip()
        pygame.display.update()
