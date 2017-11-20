import pygame
import sys
from pyanimation import Animation
import time

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255,255,255))
clock = pygame.time.Clock()
goku = Animation("images/goku-ss4.png")

# automatic creatin stand by position
goku.create_animation(0, 0, 48, 70, 4, "down", repeat=True, duration=250)

# manual creation frame by frame
#kick
goku.insert_frame(113, 443, 57, 60)
goku.insert_frame(166, 443, 60, 60)
goku.insert_frame(235, 443, 66, 60)
goku.insert_frame(303, 443, 66, 60)
goku.insert_frame(375, 443, 68, 60)
goku.insert_frame(448, 443, 68, 60)
goku.insert_frame(375, 443, 58, 60)
goku.build_animation("kick", repeat=False, duration=83)

# Big-combo
goku.insert_frame(119, 1653, 50, 80)
goku.insert_frame(167, 1653, 47, 80)
goku.insert_frame(114, 1728, 50, 80)
goku.insert_frame(168, 1730, 50, 80)
goku.insert_frame(217, 1730, 70, 80)
goku.insert_frame(284, 1730, 70, 80)
goku.insert_frame(349, 1730, 50, 80)
goku.insert_frame(402, 1730, 50, 80)
goku.insert_frame(120, 367, 58, 60)
goku.insert_frame(180, 367, 58, 60)
goku.insert_frame(211, 1674, 65, 60)
goku.insert_frame(249, 367, 65, 60)
goku.insert_frame(113, 443, 57, 60)
goku.insert_frame(166, 443, 60, 60)
goku.insert_frame(235, 443, 66, 60)
goku.insert_frame(303, 443, 66, 60)
goku.insert_frame(375, 443, 68, 60)
goku.insert_frame(448, 443, 68, 60)
goku.insert_frame(375, 443, 58, 60)
goku.insert_frame(454, 1730, 50, 80)
goku.build_animation("combo", repeat=False, duration=83)

# loading
goku.insert_frame(115, 1400, 83, 90)
goku.insert_frame(195, 1400, 83, 90)
goku.build_animation("load", repeat=False, duration=250)


screen.blit(surface, (0,0))
pressed_time = time.time()

if __name__ == '__main__':
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    goku.run("down")
                    pressed_time = time.time()
                if event.key == pygame.K_DOWN:
                    goku.run("load")
                    pressed_time = time.time()
                if event.key == pygame.K_LEFT:
                    goku.run("kick")
                    pressed_time = time.time()
                    goku.facing_right = False
                if event.key == pygame.K_RIGHT:
                    goku.run("combo")
                    pressed_time = time.time()
                    goku.facing_right = True

        if time.time() - pressed_time > 1:
            goku.run("down")
        surface.fill((255,255,255))
        screen.blit(surface, (0,0))
        clock.tick(60)

        #goku.update(screen)
        screen.blit(goku.update_surface(), (goku.x, goku.y))
        pygame.display.flip()
        pygame.display.update()
