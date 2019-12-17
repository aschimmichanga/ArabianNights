'''
    Ashna Srivastava

    Placid Scene

    This illustrates an artistic rendition of Arabian Nights using PyGame.
'''


import pygame
import sys
import math
import random
from pygame.locals import *


SCREEN_HEIGHT = 500
SCREEN_WIDTH = 400


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH), 0, 32)
    pygame.mixer.music.load('arabian_music.mp3')
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Arabian Nights")

    MIGNIGHT_PURPLE = (50, 23, 51)
    MIDNIGHT_BLUE = (18, 21, 47)

    MOON = (250, 231, 185)

    CLOUD = (141, 110, 138)
    CLOUD_LINE = (166, 144, 156)

    SPIRE_RED = (87, 29, 24)
    SPIRE_BLUE = (52, 75, 69)
    SPIRE_PURPLE = (67, 54, 65)
    SPIRE_GOLD = (155, 87, 75)
    SPIRE_BROWN = (57, 20, 6)
    SPIRE_PINK = (129,45,83)

    ROCK = (64, 42, 33)
    DARK_ROCK = (56, 31, 24)
    SAND = (134, 102, 97)
    DARK_SAND = (90, 50, 58)
    WALL = (103, 86, 63)
    DARK_WALL = (83, 57, 44)
    DARK_DARK_WALL = (100, 70, 71)
    DARK_DARK_DARK_WALL = (90, 64, 65)

    fill_gradient(DISPLAYSURF, MIGNIGHT_PURPLE, MIDNIGHT_BLUE)

    # moon
    pygame.draw.circle(DISPLAYSURF, MOON,
                       (int(SCREEN_HEIGHT/2), int(SCREEN_WIDTH/2)),
                       150, 0)

    # stars
    pixObj = pygame.PixelArray(DISPLAYSURF)

    for i in range(100):
        x = random.choice((list(range(SCREEN_HEIGHT))))
        y = random.choice((list(range(SCREEN_WIDTH))))
        pixObj[x][y] = random.choice((MOON, CLOUD))

    # cloud
    cloud_points = ((323, 138), (335, 134), (342, 138),
                    (356, 133), (382, 147), (406, 135),
                    (425, 138), (443, 135), (448, 131),
                    (440, 131), (421, 132), (410, 132),
                    (406, 131), (405, 123), (393, 113),
                    (383, 113), (377, 118), (376, 125),
                    (384, 127), (381, 126), (375, 120),
                    (360, 107), (344, 109), (334, 117),
                    (338, 121), (344, 125), (342, 125),
                    (317, 123), (318, 127), (321, 129),
                    (330, 133), (331, 135), (324, 138),
                    (317, 136), (311, 138), (309, 141),
                    (310, 142))
    pygame.draw.polygon(DISPLAYSURF, CLOUD, cloud_points)
    pygame.draw.lines(DISPLAYSURF, CLOUD_LINE, True, cloud_points, 3)

    # ----- castle -----
    # background buildings
    pygame.draw.rect(DISPLAYSURF, DARK_DARK_WALL, (140, 255, 50, 50), 0)
    pygame.draw.rect(DISPLAYSURF, DARK_ROCK, (140 + 11, 265, 6, 10), 0)
    pygame.draw.rect(DISPLAYSURF, DARK_ROCK, (190 - 13, 265, 6, 10), 0)

    pygame.draw.rect(DISPLAYSURF, DARK_DARK_WALL, (310, 260, 50, 40), 0)
    pygame.draw.rect(DISPLAYSURF, DARK_ROCK, (310 + 11, 270, 6, 10), 0)
    pygame.draw.rect(DISPLAYSURF, DARK_ROCK, (360 - 13, 270, 6, 10), 0)

    pillar_points = ((157, 255), (160, 230), (170, 230), (170, 255))
    pygame.draw.polygon(DISPLAYSURF, DARK_DARK_DARK_WALL, pillar_points)
    pygame.draw.ellipse(DISPLAYSURF, SPIRE_PURPLE, (140, 220, 50, 25), 0)
    draw_spire_point(DISPLAYSURF, SPIRE_BROWN, (140 + 25, 220), 20)

    pillar_points = ((330, 260), (330, 235), (340, 235), (343, 260))
    pygame.draw.polygon(DISPLAYSURF, DARK_DARK_DARK_WALL, pillar_points)
    pygame.draw.ellipse(DISPLAYSURF, SPIRE_PURPLE, (330 - 18, 225, 50, 25), 0)
    draw_spire_point(DISPLAYSURF, SPIRE_BROWN, (330 - 18 + 25, 225), 20)

    pillar_points = ((73, 310), (78, 200), (95, 200), (100, 310))
    pygame.draw.polygon(DISPLAYSURF, WALL, pillar_points)
    pygame.draw.ellipse(DISPLAYSURF, SPIRE_PINK, (70, 170, 33, 37), 0)
    draw_spire_point(DISPLAYSURF, SPIRE_GOLD, (70 + int(33/2), 170), 20)

    pillar_points = ((399, 310), (404, 200), (421, 200), (426, 310))
    pygame.draw.polygon(DISPLAYSURF, WALL, pillar_points)
    pygame.draw.ellipse(DISPLAYSURF, SPIRE_PINK, (396, 170, 33, 37), 0)
    draw_spire_point(DISPLAYSURF, SPIRE_GOLD, (396 + int(33/2), 170), 20)

    # platform
    platform_points = ((0, SCREEN_HEIGHT), (140, 300), (160, 275), (340, 275),
                       (360, 300), (SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.draw.polygon(DISPLAYSURF, DARK_ROCK, platform_points)
    platform_points = ((0, SCREEN_HEIGHT), (0, 330), (100, 300), (400, 300),
                       (SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.draw.polygon(DISPLAYSURF, ROCK, platform_points)

    # walls
    pygame.draw.rect(DISPLAYSURF, DARK_WALL, (200, 245, 100, 30), 0)
    pygame.draw.rect(DISPLAYSURF, DARK_ROCK, (200 + 21, 255, 6, 10), 0)
    pygame.draw.rect(DISPLAYSURF, DARK_ROCK, (300 - 23, 255, 6, 10), 0)

    wall_points = ((220, 245), (228, 200), (228, 195), (272, 195),
                   (272, 200), (280, 245))
    pygame.draw.polygon(DISPLAYSURF, WALL, wall_points)
    pygame.draw.rect(DISPLAYSURF, DARK_ROCK, (228 + 8, 207, 6, 10), 0)
    pygame.draw.rect(DISPLAYSURF, DARK_ROCK, (272 - 12, 207, 6, 10), 0)
    draw_arches(DISPLAYSURF, SPIRE_BROWN, (228, 200), 272-228)
    draw_arches(DISPLAYSURF, SPIRE_BROWN, (228, 220), 272-228)

    wall_points = ((145, 300), (141, 275), (118, 275), (114, 300))
    pygame.draw.polygon(DISPLAYSURF, WALL, wall_points)

    wall_points = ((351, 300), (355, 275), (378, 275), (382, 291))
    pygame.draw.polygon(DISPLAYSURF, WALL, wall_points)

    # pillars
    pillar_points = ((300, 275), (300, 240), (310, 240), (313, 275))
    pygame.draw.polygon(DISPLAYSURF, WALL, pillar_points)
    pillar_points = ((200, 275), (200, 240), (190, 240), (187, 275))
    pygame.draw.polygon(DISPLAYSURF, WALL, pillar_points)
    
    
    # spire
    pygame.draw.ellipse(DISPLAYSURF, SPIRE_RED, (190, 110, 120, 90), 0)
    draw_spire_point(DISPLAYSURF, SPIRE_GOLD, (190 + 60, 110), 20)

    pygame.draw.ellipse(DISPLAYSURF, SPIRE_RED, (300 - 3, 226, 18, 15), 0)
    draw_spire_point(DISPLAYSURF, SPIRE_BROWN, (297 + 9, 226), 10)

    pygame.draw.ellipse(DISPLAYSURF, SPIRE_RED, (190 - 3, 226, 18, 15), 0)
    draw_spire_point(DISPLAYSURF, SPIRE_BROWN, (187 + 9, 226), 10)

    pygame.draw.ellipse(DISPLAYSURF, SPIRE_BLUE, (114 - 10, 248, 50, 30), 0)
    draw_spire_point(DISPLAYSURF, SPIRE_GOLD, (104 + 25, 248), 10)

    pygame.draw.ellipse(DISPLAYSURF, SPIRE_BLUE, (351 - 10, 248, 50, 30), 0)
    draw_spire_point(DISPLAYSURF, SPIRE_GOLD, (341 + 25, 248), 10)

    # swirls
    swirl_points = ((256, 199), (274, 190), (284, 181), (292, 176),
                    (299, 165), (301, 160), (303, 147), (303, 139),
                    (297, 132), (294, 128), (287, 122))
    pygame.draw.lines(DISPLAYSURF, CLOUD, False, swirl_points, 1)
    swirl_points = ((223, 193), (225, 194), (226, 195), (231, 195),
                    (233, 195), (237, 195), (240, 194), (241, 194),
                    (242, 194), (244, 194), (247, 193), (249, 193),
                    (249, 193), (250, 191), (250, 190), (251, 188),
                    (252, 188), (252, 188), (253, 183), (253, 183),
                    (253, 181), (253, 178), (253, 178), (251, 173),
                    (251, 171), (243, 166), (242, 165), (238, 165),
                    (233, 165), (231, 165), (227, 168), (226, 169),
                    (225, 173), (226, 175), (227, 177), (230, 182),
                    (230, 182), (236, 183), (238, 184), (238, 184))
    pygame.draw.lines(DISPLAYSURF, CLOUD, False, swirl_points, 1)

    # sand dunes
    dune_points = ((122, 397), (175, 377), (289, 353), (361, 291),
                  (425, 265), (488, 272), (498, 290), (SCREEN_HEIGHT, 300),
                  (SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.draw.polygon(DISPLAYSURF, DARK_SAND, dune_points)
    dune_points = ((0, SCREEN_HEIGHT), (0, 369), (62, 331), (132, 302),
                  (177, 310), (236, 347), (299, 376), (337, 389),
                  (404, 396), (497, 399))
    pygame.draw.polygon(DISPLAYSURF, SAND, dune_points)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
            # key press and then print
        pygame.display.update()


def draw_spire_point(screen, color, start_pos, height):
    x, y = start_pos
    pygame.draw.lines(screen, color, False, (start_pos, (x, y-height)), 1)
    pygame.draw.circle(screen, color, (x, y - int(height/3)), int(height/5), 0)
    pygame.draw.circle(screen, color, (x, y - int(height/2) - int(height/6)),
                       int(height/7), 0)


def draw_arches(screen, color, start_pos, width):
    x, y = start_pos
    pygame.draw.lines(screen, color, False, (start_pos, (x+width, y)), 1)
    pygame.draw.lines(screen, color, False, ((x, y + width/8),
                                             (x+width, y + width/8)), 1)
    pygame.draw.arc(screen, color, (x, y, width/3, width/6),  0, math.pi, 1)
    pygame.draw.arc(screen, color, (x + width/3, y, width/3, width/6), 0,
                    math.pi, 1)
    pygame.draw.arc(screen, color, (x + 2 * width/3, y, width/3, width/6), 0,
                    math.pi, 1)


def fill_gradient(surface, first_color, second_color):
    rate = (float(second_color[0]-first_color[0])/SCREEN_WIDTH,
            float(second_color[1]-first_color[1])/SCREEN_WIDTH,
            float(second_color[2]-first_color[2])/SCREEN_WIDTH)
    fn_line = pygame.draw.line
    for line in range(SCREEN_WIDTH):
        temp = (min(max(first_color[0] + (rate[0]*(line)), 0), 255),
                min(max(first_color[1] + (rate[1]*(line)), 0), 255),
                min(max(first_color[2] + (rate[2]*(line)), 0), 255))
        fn_line(surface, temp, (0, line), (SCREEN_HEIGHT, line))


if __name__ == '__main__':
    main()
