#!/usr/bin/env python3

import turtle
from random import randint

"""
This module contains functions related to drawing and moving a circle around the screen
"""

__author__ = 'Lacie Cruise'
__version__ = '1.0'
__copyright__ = ""
__github__ = "https://github.com/Ljcruise/CSC365_Python.git"

wn = None  # the global window screen that all shapes will share
t = None   # the global turtle that all shapes will share


def turtle_setup():
    """
    All shape need to share the same window screen & turtle objects
    Also, sets the newly open window screen on top of other windows

    Returns:
        None
    """
    global wn, t
    wn = turtle.Screen()  # used to control the window
    t = turtle.Turtle()  # basically this is your cursor that you used to draw with
    t.shape("turtle")

    # make sure the turtle window screen displays on top of other open windows
    root_window = wn.getcanvas().winfo_toplevel()  # get the top level turtle screen canvas
    root_window.call('wm', 'attributes', '.', '-topmost', '1')  # and make it have the top focus



# position where the turtle will be drawn at
# these values will change by plus/minus 20 as arrows are pressed
x = 0  # center of screen moving right or left
y = 0  # center of screen moving up or down
fill_color = 'white'  # the color of the circle

def move_home():
    """
    Reset the x and y back to zero coordinate which will be used position the circle in the center
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x, y
    x = 0  # center of screen moving right or left
    y = 0  # center of screen moving up or down
    # draw_circle()


def rand_int():

    t.penup()
    t.goto(random.randint(-300, 0), randint(0, 300))

    t.done()


def main():
    """
    The main function, used to test drawing a square

    Returns:
        None
    """
    global fill_color

    fill_color = 'pink'  # override the default red color

    # t.turtle_setup()  # set up the global window screen & turtle and bring window to front

    # setup_window('black')  # configure how the turtle window screen will look like

    # draw_circle(50)  # draw the initial shape based on diameter
    rand_int()

    # t.wn.mainloop()  # keep the turtle window open until the user closes it

    # t.screen_recreation()  # recreate the window screen so it's ready for the next drawing


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()

