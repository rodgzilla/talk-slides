import pygame
from pygame import gfxdraw
from pygame import Color
import sys
import time
import cmath

def draw_mandelbrot(window, f, max_iter, width, height):
    for y in range(height):
        for x in range(width):
            real = 3 * x / width - 2
            imag = 2 * y / height - 1
            c = complex(real, imag)
            z = c
            # The for ... else ... structure is a Python specificity.
            # else clause is only executed if the for ends without a
            # break.
            for i in range(max_iter):
                z = f(z, c)
                if z.real ** 2 + z.imag ** 2 > 4:
                    c = round(i * 255 / max_iter)
                    gfxdraw.pixel(window, x, y, Color(c, 0, 0, 255))
                    # gfxdraw.pixel(window, x, y, Color(255, 255, 255, 255))
                    break
            else:
                gfxdraw.pixel(window, x, y, Color(0, 0, 0, 255))


if __name__ == '__main__':
    pygame.init()
    width, height        = 900, 600
    max_iter             = 30
    window               = pygame.display.set_mode((width, height))
    mandelbrot_functions = [
        lambda z, c: z ** 2 + c,
        lambda z, c: z ** 3 + c,
        lambda z, c: z ** 3 + z ** 2 + c,
        lambda z, c: z ** 2 + cmath.sin(c),
        lambda z, c: z ** 2 + cmath.sin(c) - cmath.cos((c + z) ** 2),
        lambda z, c: z ** 2 + c * cmath.sin(cmath.cos(c)) + 1,
        lambda z, c: z ** 2 + c + 0.5,
        lambda z, c: z ** 2 + c / 2,
    ]
    draw_mandelbrot(
        window,
        mandelbrot_functions[int(sys.argv[1])],
        max_iter,
        width,
        height
    )
    pygame.display.flip()
    print('done')

    # The window stays open until it is closed manually by the user.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
