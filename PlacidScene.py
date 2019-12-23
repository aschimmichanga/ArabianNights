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

# colors
MOON = (250, 231, 185)
CLOUD = (141, 110, 138)
CLOUD_LINE = (166, 144, 156)
SPIRE_RED = (87, 29, 24)
SPIRE_BLUE = (52, 75, 69)
SPIRE_PURPLE = (67, 54, 65)
SPIRE_GOLD = (155, 87, 75)
SPIRE_BROWN = (57, 20, 6)
SPIRE_PINK = (129,45,83)
CAMEL = (147,104,97)

ROCK = (64, 42, 33)
DARK_ROCK = (56, 31, 24)

SAND = (134, 102, 97)
DARK_SAND = (90, 50, 58)

WALL = (103, 86, 63)
DARK_WALL = (83, 57, 44)
DARK_DARK_WALL = (100, 70, 71)
DARK_DARK_DARK_WALL = (90, 64, 65)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH), 0, 32)
    # pygame.mixer.music.load('arabian_music.mp3')
    # pzazqygame.mixer.music.play(-1)
    # pygame.display.set_caption("Arabian Nights")
    counter = 0
    
    # pygame.draw.lines(screen, color, closed, pointlist, thickness)
    # pygame.draw.rect(screen, color, (x,y,width,height), thickness)
    # pygame.draw.circle(screen, color, (x,y), radius, thickness)
    # pygame.draw.arc(screen, color, (x,y,width,height), start_angle, stop_angle, thickness)
    # pygame.draw.polygon(surface,color,points,width)
    # pixObj = pygame.PixelArray(DISPLAYSURF)
    # pixObj[100][100] = BLACK

    while True:
        # erases the old drawing (e.g. screen.fill(white) or screen.fill(black))
        # draws the new drawing (e.g. using function calls starting with pygame.draw) in a different place than it was before!
        # calls pygame.display.update() to make all the changes appear

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
            # key press and then print

        # sky
        draw_sky(DISPLAYSURF, counter)
        draw_cloud(DISPLAYSURF)

        # background
        draw_bg_buildings(DISPLAYSURF)
        draw_purple_spires(DISPLAYSURF)
        draw_pink_spires(DISPLAYSURF)


        draw_main_buildings(DISPLAYSURF)
        draw_pillars(DISPLAYSURF)
        draw_red_spires(DISPLAYSURF)
        draw_blue_spires(DISPLAYSURF)
        draw_platforms(DISPLAYSURF,1)
         # camels
        counter = counter + 1
        draw_camels(DISPLAYSURF, counter)
        draw_swirls(DISPLAYSURF)

        draw_dune(DISPLAYSURF, 1)
        draw_platforms(DISPLAYSURF,2)
       

        # sand dunes
        draw_dune(DISPLAYSURF,  2)
        draw_dune(DISPLAYSURF, 3)
            
        clock.tick(30)
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


def draw_window(screen, x, y):
    LIGHT_ON = (247,183,54)
    #LIGHT_OFF = (56, 31, 24)
    pygame.draw.rect(screen, LIGHT_ON, (x, y, 6, 10), 0)

def draw_cloud(screen):
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
    CLOUD = (141, 110, 138)
    CLOUD_LINE = (166, 144, 156)
    pygame.draw.polygon(screen, CLOUD, cloud_points)
    pygame.draw.lines(screen, CLOUD_LINE, True, cloud_points, 3)

def draw_stars(screen):
    pixObj = pygame.PixelArray(screen)
    for i in range(400):
        x = random.choice((list(range(SCREEN_HEIGHT))))
        y = random.choice((list(range(SCREEN_WIDTH))))
        pixObj[x][y] = random.choice((MOON, CLOUD_LINE, CLOUD))
    
def draw_sky(screen, counter):
    half_screen = int(SCREEN_WIDTH/2)

    # night
    PURPLE_PARADISE = ((29,43,100),(248,205,218))
    SEA_BLUE = ((78,67,118),(43,88,118))
    PINOT_NOIR = ((75,108,183),(24,40,72))
    EXPRESSO = ((60, 16, 83),(173, 83, 137))
    MAUVE = ((66, 39, 90),(115, 75, 109))
    DARK_PURPLE = ((47, 7, 67),(65, 41, 90))

    # eve
    KYOTO = ((194,21,0),(255,197,0))
    INFLUENZA = ((192,72,72),(72,0,72))
    PEACH = ((237,66,100),(255,237,188))
    SUNRISE = ((255,81,47),(240,152,25))
    PURPLE_LOVE = ((204,43,94),(117,58,136))
    EVENING_SUNSHINE = ((185,43,39),(21,101,192))
    TARAN_TADO = ((35,7,77),(204,83,51))

    # morn
    ALMOST = ((221,214,243),(250,172,168))
    BOURBON = ((236,111,102),(243,161,131))
    JUICY_ORANGE = ((255,128,8),(255,200,55))
    EVENING_NIGHT = ((0,90,167),(255,253,228))
    TELEGRAM = ((28,146,210),(242,252,254))
    SKY = ((18,69,128),(162,203,191))

    first_color = DARK_PURPLE
    second_color = TELEGRAM

    # night to dawn = 0
    # sunrise to day = 1
    # day to sunset = 2
    # dusk to night = 3

    if counter // half_screen % 4 == 0: # night to dawn
        y =  half_screen + counter % half_screen
        first_color = DARK_PURPLE
        second_color = TARAN_TADO
    elif counter // half_screen % 4 == 1: # sunrise to day
        y =  SCREEN_WIDTH - counter % half_screen
        first_color = TARAN_TADO
        second_color = SKY
    elif counter // half_screen % 4 == 2: # day to sunset
        y =  half_screen + counter % half_screen
        first_color = SKY
        second_color = BOURBON
    else: # dusk to night
        y = SCREEN_WIDTH - counter % half_screen
        first_color = BOURBON
        second_color = DARK_PURPLE

    rate1 = (float(second_color[0][0]-first_color[0][0])/half_screen,
            float(second_color[0][1]-first_color[0][1])/half_screen,
            float(second_color[0][2]-first_color[0][2])/half_screen)

    rate2 = (float(second_color[1][0]-first_color[1][0])/half_screen,
            float(second_color[1][1]-first_color[1][1])/half_screen,
            float(second_color[1][2]-first_color[1][2])/half_screen)

    line = counter % half_screen
    
    temp1 = (min(max(first_color[0][0] + int(rate1[0]*(line)), 0), 255),
             min(max(first_color[0][1] + int(rate1[1]*(line)), 0), 255),
             min(max(first_color[0][2] + int(rate1[2]*(line)), 0), 255))

    temp2 = (min(max(first_color[0][0] + int(rate2[0]*(line)), 0), 255),
             min(max(first_color[0][1] + int(rate2[1]*(line)), 0), 255),
             min(max(first_color[0][2] + int(rate2[2]*(line)), 0), 255))

    fill_gradient(screen, temp1, temp2)
    
    

    pygame.draw.circle(screen, MOON,
                       (int(SCREEN_HEIGHT/2), y),
                       150, 0)

def draw_dune(screen, seq_order):
    color = DARK_SAND
    if seq_order == 1:
        dune_points = ((0,SCREEN_HEIGHT),(0, 243),(42, 253),(66, 274),(108, 316))
    elif seq_order == 2:
        dune_points = ((122, 397), (175, 377), (289, 353), (361, 291),
                  (425, 265), (488, 272), (498, 290), (SCREEN_HEIGHT, 300),
                  (SCREEN_HEIGHT, SCREEN_WIDTH))
    elif seq_order == 3:
        color = SAND
        dune_points = ((0, SCREEN_HEIGHT), (0, 369), (62, 331), (132, 302),
                  (177, 310), (236, 347), (299, 376), (337, 389),
                  (404, 396), (497, 399))
    pygame.draw.polygon(screen, color, dune_points)

def draw_bg_buildings(screen):
    pygame.draw.rect(screen, DARK_DARK_WALL, (140, 255, 50, 50), 0)
    draw_window(screen, 140 + 11, 265)
    draw_window(screen, 190 - 13, 265)

    pygame.draw.rect(screen, DARK_DARK_WALL, (310, 260, 50, 40), 0)
    draw_window(screen, 310 + 11, 270)
    draw_window(screen, 360 - 13, 270)

def draw_purple_spires(screen):
    pillar_points = ((157, 255), (160, 230), (170, 230), (170, 255))
    pygame.draw.polygon(screen, DARK_DARK_DARK_WALL, pillar_points)
    pygame.draw.ellipse(screen, SPIRE_PURPLE, (140, 220, 50, 25), 0)
    draw_spire_point(screen, SPIRE_BROWN, (140 + 25, 220), 20)
    
    pillar_points = ((330, 260), (330, 235), (340, 235), (343, 260))
    pygame.draw.polygon(screen, DARK_DARK_DARK_WALL, pillar_points)
    pygame.draw.ellipse(screen, SPIRE_PURPLE, (330 - 18, 225, 50, 25), 0)
    draw_spire_point(screen, SPIRE_BROWN, (330 - 18 + 25, 225), 20)

def draw_pink_spires(screen):
    WALL = (103, 86, 63)
    SPIRE_PINK = (129,45,83)
    SPIRE_GOLD = (155, 87, 75)
    
    pillar_points = ((73, 310), (78, 200), (95, 200), (100, 310))
    pygame.draw.polygon(screen, WALL, pillar_points)
    pygame.draw.ellipse(screen, SPIRE_PINK, (70, 170, 33, 37), 0)
    draw_spire_point(screen, SPIRE_GOLD, (70 + int(33/2), 170), 20)
    draw_window(screen, 70 + 15, 220)

    pillar_points = ((399, 310), (404, 200), (421, 200), (426, 310))
    pygame.draw.polygon(screen, WALL, pillar_points)
    pygame.draw.ellipse(screen, SPIRE_PINK, (396, 170, 33, 37), 0)
    draw_spire_point(screen, SPIRE_GOLD, (396 + int(33/2), 170), 20)
    draw_window(screen, 396 + 15, 220)

def draw_red_spires(screen):
    SPIRE_RED = (87, 29, 24)
    SPIRE_GOLD = (155, 87, 75)
    SPIRE_BROWN = (57, 20, 6)
    
    pygame.draw.ellipse(screen, SPIRE_RED, (190, 110, 120, 90), 0)
    draw_spire_point(screen, SPIRE_GOLD, (190 + 60, 110), 20)

    pygame.draw.ellipse(screen, SPIRE_RED, (300 - 3, 226, 18, 15), 0)
    draw_spire_point(screen, SPIRE_BROWN, (297 + 9, 226), 10)

    pygame.draw.ellipse(screen, SPIRE_RED, (190 - 3, 226, 18, 15), 0)
    draw_spire_point(screen, SPIRE_BROWN, (187 + 9, 226), 10)

def draw_blue_spires(screen):
    pygame.draw.ellipse(screen, SPIRE_BLUE, (114 - 10, 248, 50, 30), 0)
    draw_spire_point(screen, SPIRE_GOLD, (104 + 25, 248), 10)

    pygame.draw.ellipse(screen, SPIRE_BLUE, (351 - 10, 248, 50, 30), 0)
    draw_spire_point(screen, SPIRE_GOLD, (341 + 25, 248), 10)

def draw_platforms(screen, seq_num):
    if seq_num == 1:
        platform_points = ((0, SCREEN_HEIGHT), (140, 300), (160, 275), (340, 275),
                        (360, 300), (SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.draw.polygon(screen, DARK_ROCK, platform_points)
    else:
        platform_points = ((0, SCREEN_HEIGHT), (0, 330), (100, 300), (400, 300),
                       (SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.draw.polygon(screen, ROCK, platform_points)

def draw_main_buildings(screen):
    pygame.draw.rect(screen, DARK_WALL, (200, 245, 100, 30), 0)
    draw_window(screen, 200 + 21, 255)
    draw_window(screen, 300 - 23, 255)

    wall_points = ((220, 245), (228, 200), (228, 195), (272, 195),
                   (272, 200), (280, 245))
    pygame.draw.polygon(screen, WALL, wall_points)
    draw_window(screen, 228 + 8, 207)
    draw_window(screen, 272 - 12, 207)
    draw_arches(screen, SPIRE_BROWN, (228, 200), 272-228)
    draw_arches(screen, SPIRE_BROWN, (228, 220), 272-228)

    wall_points = ((145, 300), (141, 275), (118, 275), (114, 300))
    pygame.draw.polygon(screen, WALL, wall_points)

    wall_points = ((351, 300), (355, 275), (378, 275), (382, 291))
    pygame.draw.polygon(screen, WALL, wall_points)

def draw_pillars(screen):
    pillar_points = ((300, 275), (300, 240), (310, 240), (313, 275))
    pygame.draw.polygon(screen, WALL, pillar_points)
    pillar_points = ((200, 275), (200, 240), (190, 240), (187, 275))
    pygame.draw.polygon(screen, WALL, pillar_points)

def draw_swirls(screen):
    swirl_points = ((256, 199), (274, 190), (284, 181), (292, 176),
                    (299, 165), (301, 160), (303, 147), (303, 139),
                    (297, 132), (294, 128), (287, 122))
    pygame.draw.lines(screen, CLOUD, False, swirl_points, 1)
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
    pygame.draw.lines(screen, CLOUD, False, swirl_points, 1)

def draw_camels(screen, count):
    for i in range(50):
        pixels = i * 45 - (count % SCREEN_WIDTH)
        pygame.draw.ellipse(screen, CAMEL, (181+pixels,285,20,10))
        camel_points = ((184+pixels, 303),(185+pixels, 294),(186+pixels, 300))
        pygame.draw.lines(screen, CAMEL, True, camel_points, 2)
        camel_points = ((194+pixels, 291),(196+pixels, 302),(194+pixels, 302))
        pygame.draw.lines(screen, CAMEL, True, camel_points, 2)
        pygame.draw.ellipse(screen, CAMEL, (185+pixels,282,5,7))
        pygame.draw.ellipse(screen, CAMEL, (190+pixels,282,5,7))
        pygame.draw.line(screen, CAMEL, (200+pixels,290),(205+pixels,295),2)
        pygame.draw.ellipse(screen, CAMEL, (175+pixels,290,5,3), 0)
        pygame.draw.ellipse(screen, CAMEL, (177+pixels,286,5,5), 0)

        pygame.draw.arc(screen, SPIRE_RED, (195+pixels, 280, 30, 20),  math.pi, 0, 3)

def fill_gradient(screen, first_color, second_color, is_night=False):
    rate = (float(second_color[0]-first_color[0])/SCREEN_WIDTH,
            float(second_color[1]-first_color[1])/SCREEN_WIDTH,
            float(second_color[2]-first_color[2])/SCREEN_WIDTH)

    fn_line = pygame.draw.line
    for line in range(SCREEN_WIDTH):
        temp = (min(max(first_color[0] + (rate[0]*(line)), 0), 255),
                min(max(first_color[1] + (rate[1]*(line)), 0), 255),
                min(max(first_color[2] + (rate[2]*(line)), 0), 255))
        fn_line(screen, temp, (0, line), (SCREEN_HEIGHT, line))
    
    if is_night:
        draw_stars(screen)


if __name__ == '__main__':
    main()
