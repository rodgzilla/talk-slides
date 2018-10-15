import math
import sys
import pygame
from pygame import gfxdraw
from pygame import Color
import math
import numpy as np
import time

def rotate(x_center, y_center, x, y, angle):
    angle_radian = angle * math.pi / 180
    cos          = math.cos(angle_radian)
    sin          = math.sin(angle_radian)
    x_rot        = cos * (x - x_center) - sin * (y - y_center) + x_center
    y_rot        = sin * (x - x_center) + cos * (y - y_center) + y_center

    return int(round(x_rot)), int(round(y_rot))

def draw_tree_angle(window, x1, y1, x2, y2, depth, angle):
    if depth == 0:
        return

    x3, y3 = rotate(x1, y1, x2, y2, -90)
    x4, y4 = rotate(x2, y2, x1, y1, 90)

    # color = Color(255, 0, 0, 255) if depth % 2 == 0 else Color(255, 255, 255, 255)
    colors = [
        Color(255, 0, 0, 255),
        Color(255, 255, 255, 255),
    ]
    color = colors[depth % len(colors)]

    gfxdraw.line(window, x1, y1, x2, y2, color)
    gfxdraw.line(window, x1, y1, x3, y3, color)
    gfxdraw.line(window, x2, y2, x4, y4, color)
    gfxdraw.line(window, x3, y3, x4, y4, color)

    new_x, new_y = rotate(x3, y3, x4, y4, -angle)
    draw_tree_angle(window, x3, y3, new_x, new_y, depth - 1, angle)
    draw_tree_angle(window, new_x, new_y, x4, y4, depth - 1, angle)

if __name__ == '__main__':
    pygame.init()
    delay              = 0.01
    scaling_step       = 0.01
    # width, height      = 1000, 1000
    width, height      = 1920, 1080
    size               = 45
    x_center, y_center = width // 2, height // 2
    x1, y1             = x_center - (size // 2), y_center + 4 * size
    x2, y2             = x_center + (size // 2), y_center + 4 * size
    window             = pygame.display.set_mode((width, height))

    angles = np.arange(0, 360, 0.5)
    while True:
        for angle in angles:
            draw_tree_angle(window, x1, y1, x2, y2, 8, angle)
            pygame.display.flip()
            time.sleep(delay)
            window.fill((0, 0, 0))

    # # We save the picture.
    # pygame.image.save(window, 'render.png')

    # The window stays open until it is closed manually by the user.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
