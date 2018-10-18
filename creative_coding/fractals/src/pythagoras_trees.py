from turtle import goto, pu, pd, color, done, right, left, forward, speed, setposition
import math

def draw(size, depth, replace_top = True):
    """
    The drawing of squares is done is the following order:
      __2__
     |     |
     |     |
    1|     |3
     |     |
     |_____|
        4
    """
    # If depth = 0, by definition we have nothing to draw
    if depth == 0:
        return

    # An application of the Pythagorean theorem tells us that the new
    # side will be smaller by a factor of sqrt(2).
    new_size = size / math.sqrt(2)
    # Draw the "left" side of the square.
    forward(size)

    # Now we have two options: either we want the recursion to happen
    # on the "top" side or on the left side, depending on where we are
    # on the figure.
    if replace_top:
        # We simply to a left rotation to properly align the turtle
        # for the new square, and then make a recursive call.
        left(45)
        draw(new_size, depth - 1, True)
        right(135)
        # Now that the recursive drawing is done, we can draw the top
        # side of the square.
        forward(size)
        # Once again, we rotate the turtle to align it for the new
        # square.
        left(135)
        draw(new_size, depth - 1, False)
        right(225)
        # Once the recursive drawing is done, we can draw the "right"
        # side of the square.
        forward(size)
        right(90)
    else:
        # If we don't make recursive calls on the "top" side, then we
        # just draw it.
        right(90)
        forward(size)
        # We now draw recursively starting from the "right" side.
        left(45)
        draw(new_size, depth - 1, True)
        right(135)
        # Now that the recursive drawing is done, we can draw the
        # "top" side of the square.
        forward(size)
        # Once again, we rotate the turtle to align it for the new
        # square.
        left(135)
        draw(new_size, depth - 1, False)
        right(225)
    # Finally, we draw the ""bottom"" side of the square.
    forward(size)
    right(90)

if __name__ == '__main__':
    # speed(0)
    speed(10)
    color('red', 'black')
    left(90)
    draw(100, 6)
    done()
