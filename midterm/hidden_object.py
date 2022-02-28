#!/usr/bin/env python3

import global_turtle
from random import randint


def hidden_obj_setup():
    """
    Create the hidden object to place in the game at a random location

    Returns:
        None
    """
    global_turtle.hidden_obj.speed(0)
    global_turtle.hidden_obj.shape('square')  # change the shape to a square
    global_turtle.hidden_obj.color('blue')
    global_turtle.hidden_obj.penup()
    global_turtle.hidden_obj.shapesize(1, 1)
    global_turtle.hidden_obj.goto(randint(-400, 0), randint(0, 400))


def main():
    """
    The main function, used to test drawing a square

    Returns:
        None
    """
    global_turtle.turtle_setup()
    hidden_obj_setup()
    global_turtle.wn.mainloop()        # keep the turtle running until the user closes it


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
