from turtle import goto, pu, pd, color, done, right, left, forward, speed, setposition

def draw(size_len, depth, angle_1 = 60, angle_2 = 120, angle_3 = 60):
    if depth == 0:
        forward(size_len)
        return

    third = size_len / 3
    draw(third, depth - 1)
    right(angle_1)
    draw(third, depth - 1)
    left(angle_2)
    draw(third, depth - 1)
    right(angle_3)
    draw(third, depth - 1)

if __name__ == '__main__':
    speed(0)
    # setposition(-500)
    color('red', 'yellow')
    draw(400, 4, 60, 120, -60)
    done()
