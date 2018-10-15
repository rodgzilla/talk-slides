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

def draw_tree_scaling(window, x1, y1, x2, y2, scaling, depth):
    if depth == 0:
        return

    x3, y3 = rotate(x1, y1, x2, y2, -90)
    x4, y4 = rotate(x2, y2, x1, y1, 90)

    gfxdraw.line(window, x1, y1, x2, y2, Color(255, 0, 0,255))
    gfxdraw.line(window, x1, y1, x3, y3, Color(255, 0, 0,255))
    gfxdraw.line(window, x2, y2, x4, y4, Color(255, 0, 0,255))
    gfxdraw.line(window, x3, y3, x4, y4, Color(255, 0, 0,255))

    angle        = math.acos(scaling) * 180 / math.pi
    to_rot_x     = x3 * (1 - scaling) + x4 * scaling
    to_rot_y     = y3 * (1 - scaling) + y4 * scaling
    new_x, new_y = rotate(x3, y3, to_rot_x, to_rot_y, -angle)
    draw_tree_scaling(window, x3, y3, new_x, new_y, scaling, depth - 1)
    draw_tree_scaling(window, new_x, new_y, x4, y4, scaling, depth - 1)


if __name__ == '__main__':
    pygame.init()
    delay              = 0.002
    scaling_step       = 0.005
    # width, height      = 1000, 1000
    width, height      = 1920, 1080
    size               = 150
    x_center, y_center = width // 2, height // 2
    x1, y1             = x_center - (size // 2), y_center + 3 * size
    x2, y2             = x_center + (size // 2), y_center + 3 * size
    window             = pygame.display.set_mode((width, height))

    scalings = np.concatenate(
        (
            np.arange(0, 1, scaling_step),
            np.arange(1, 0, -scaling_step)
        )
    )
    while True:
        for scaling in scalings:
            draw_tree_scaling(window, x1, y1, x2, y2, scaling, 9)
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
