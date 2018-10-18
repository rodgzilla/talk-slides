import time

def print_mandel(f, max_iter, width, height):
    for y in range(height):
        for x in range(width):
            real = 3 * x / width - 2
            imag = 2 * y / height - 1
            c = complex(real, imag)
            z = c
            # The for ... else ... structure is a Python specificity.
            # else clause is only executed if the for ends without a
            # break.
            for _ in range(max_iter):
                z = f(z, c)
                if z.real ** 2 + z.imag ** 2 > 4:
                    print(' ', end = '')
                    break
            else:
                print('◼', end = '')
        print()

def print_mandel_seq(f_1, f_2, steps, sleep_time, max_iter, width, height):
    for step in range(steps):
        # We generate a new sequence function on the fly by computing a weighted
        # average of f_1 and f_2.
        f = lambda z, c: (1 - step / steps) * f_1(z, c) + step / steps * f_2(z, c)
        print('\n' * 30)
        print_mandel(
            f,
            max_iter,
            width,
            height
        )
        time.sleep(sleep_time)


if __name__ == '__main__':
    height     = 100
    width      = 150
    height     = 30
    max_iter   = 50
    # We define the start and the end function
    sequence_1 = lambda z, c: z + c
    sequence_2 = lambda z, c: z ** 2 + c
    # and the number of points for the interpolation
    steps      = 100
    sleep_time = 0.25

    print_mandel_seq(
        sequence_1,
        sequence_2,
        steps,
        sleep_time,
        max_iter,
        width,
        height
    )
