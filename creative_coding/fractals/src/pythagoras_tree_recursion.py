import math
import sys
import pygame
from pygame import gfxdraw
from pygame import Color
import math
import numpy as np
import time

def rotate_image(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image  = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect           = rotated_image.get_rect(center = pivot + rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.


def rotate(x_center, y_center, x, y, angle):
    angle_radian = angle * math.pi / 180
    cos          = math.cos(angle_radian)
    sin          = math.sin(angle_radian)
    x_rot        = cos * (x - x_center) - sin * (y - y_center) + x_center
    y_rot        = sin * (x - x_center) + cos * (y - y_center) + y_center

    return int(round(x_rot)), int(round(y_rot))

def draw_tree_scaling_image(image, window, x1, y1, x2, y2, scaling, depth):
    def draw_tree_scaling(window, x1, y1, x2, y2, scaling, depth):
        if depth == 0:
            return

        if x1 == x2 and y1 == y2:
            return

        x3, y3 = rotate(x1, y1, x2, y2, -90)
        x4, y4 = rotate(x2, y2, x1, y1, 90)
        new_size = round(math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2))
        resized_image = pygame.transform.scale(image, (new_size, new_size))

        # pygame.transform.scale()
        # resize to new resolution
        # scale(Surface, (width, height), DestSurface = None) -> Surface
        # angle_rad = math.atan((x3 - x1) / (y3 - y1)) if y3 != y1 else 0
        # swap      = 1 if y3 <= y1 else -1
        angle_rad = math.asin((x3 - x1) / new_size)
        angle     = angle_rad * 180 / math.pi
        if y3 > y1:
            angle = 180 - angle
        if depth == 1:
            print('##############')
            print(f'(x1, y1) = {(x1, y1)}')
            print(f'(x2, y2) = {(x2, y2)}')
            print(f'(x3, y3) = {(x3, y3)}')
            print(f'(x4, y4) = {(x4, y4)}')
            # print(f'{x1} {x2} {x3} {x4}')
            # print(f'{y1} {y2} {y3} {y4}')
            print(x3 - x1, angle)
        # angle = 0
        # rot_img, rect = rotate_image(image, angle, (x3, y3), pygame.Vector2(-112.5, 112.5))
        # rot_img, rect = rotate_image(image, angle, (x3, y3), pygame.Vector2(112.5, 112.5))
        rot_img, rect = rotate_image(
            resized_image,
            angle,
            (x3, y3),
            pygame.Vector2(new_size / 2, new_size / 2)
        )
        # window.blit(image, (x3, y3))
        window.blit(rot_img, rect)
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

    draw_tree_scaling(window, x1, y1, x2, y2, scaling, depth)

if __name__ == '__main__':
    pygame.init()
    delay              = 0.002
    scaling_step       = 0.005
    # width, height      = 1000, 1000
    width, height      = 900, 900
    size               = 125
    x_center, y_center = width // 2, height // 2
    x1, y1             = x_center - (size // 2), y_center + 3 * size
    x2, y2             = x_center + (size // 2), y_center + 3 * size
    window             = pygame.display.set_mode((width, height))
    image              = pygame.image.load('xzibit_small.png')

    # scalings = np.concatenate(
    #     (
    #         np.arange(0, 1, scaling_step),
    #         np.arange(1, 0, -scaling_step)
    #     )
    # )
    # while True:
    #     for scaling in scalings:
    #         # draw_tree_scaling(window, x1, y1, x2, y2, scaling, 9)
    #         draw_tree_scaling_image(image, window, x1, y1, x2, y2, scaling, 8)
    #         pygame.display.flip()
    #         time.sleep(delay)
    #         window.fill((0, 0, 0))

    draw_tree_scaling_image(image, window, x1, y1, x2, y2, math.sqrt(2) / 2, 7)
    pygame.display.flip()

    # # We save the picture.
    # pygame.image.save(window, 'render.png')

    # The window stays open until it is closed manually by the user.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
