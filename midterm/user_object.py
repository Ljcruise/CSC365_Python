#!/usr/bin/env python3

import turtle
from random import randint

"""
This module contains functions related to drawing and moving a circle around the screen
"""

__author__ = 'Lacie Cruise'
__version__ = '1.0'
__copyright__ = 'Copyright 2022.03.04, Hot-Cold Game Assignment'
__github__ = 'https://github.com/Ljcruise/CSC365_Python.git'

wn = None  # the global window screen that all shapes will share
t = None  # the global turtle for the user's moving object
hidden_obj = None  # the global hidden object for the game


def turtle_setup():
    """
    All shape need to share the same window screen & turtle objects
    Also, sets the newly open window screen on top of other windows

    Returns:
        None
    """
    global wn, t
    wn = turtle.Screen()  # used to control the window
    t = turtle.Turtle()  # this will be the circle that is moved around by the user once drawn

    # make sure the turtle window screen displays on top of other open windows
    root_window = wn.getcanvas().winfo_toplevel()  # get the top level turtle screen canvas
    root_window.call('wm', 'attributes', '.', '-topmost', '1')  # and make it have the top focus


# position where the turtle will be drawn at
# these values will change by plus/minus 20 as arrows are pressed
x = 0  # center of screen moving right or left
y = 0  # center of screen moving up or down
fill_color = 'white'  # the color of the circle


def hidden_obj_setup():
    """
    Create the hidden object to place in the game at a random location

    Returns:
        None
    """
    global wn, hidden_obj
    wn = turtle.Screen()
    hidden_obj = turtle.Turtle()  # create the hidden object turtle
    hidden_obj.speed(0)
    hidden_obj.shape('square')  # change the shape to a square
    hidden_obj.color('blue')
    hidden_obj.penup()
    hidden_obj.shapesize(1, 1)
    hidden_obj.goto(randint(-400, 0), randint(0, 400))
    turtle.done()


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
    draw_circle()


def move_left():
    """
    Subtract 20 from the x coordinate which will be used move the circle to the left
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x
    x -= 20  # move to the left of center
    draw_circle()


def move_right():
    """
    Add 20 to the x coordinate which will be used move the circle to the right
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x
    x += 20  # move to the right of center
    draw_circle()


def move_up():
    """
    Add 20 to the y coordinate which will be used move the circle up
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global y
    y += 20  # move top of center
    draw_circle()


def move_down():
    """
    Subtract 20 from y coordinate which will be used move the circle to the down
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    Returns:
        None
    """

    global y
    y -= 20  # move down of center
    draw_circle()


def setup_window(bg_color='white'):
    """
    Controls how the window looks.

    Args:
        bg_color (str): the background color of the window (default white)

    Returns:
        None
    """
    global wn

    wn.tracer(False)  # turn animation off which causes screen flickering as the circle gets redrawn
    wn.title('Hot-Cold Turtle Game')  # title the title bar of the window
    wn.bgcolor(bg_color)  # set the window's background color
    wn.setup(800, 800)  # the size of the window

    # set up the keys to listen to and what function should be called
    wn.onkeypress(move_home, "h")
    wn.onkeypress(move_up, "Up")
    wn.onkeypress(move_down, "Down")
    wn.onkeypress(move_right, "Right")
    wn.onkeypress(move_left, "Left")
    wn.listen()  # start listening for keys being pressed


def draw_circle(game_difficulty):
    """
    clear the screen and draw the circle based on the x & y coordinates

    Args:
        diameter (int): the diameter size of the circle (default 10)
        fill_color (str): the inside color of the circle (default red)
        game_difficulty (int): controls the size of the circle

    Returns:
        None
    """

    global t, x, y, fill_color

    t.hideturtle()  # don't show the icon
    t.speed('fastest')  # draw quickly

    t.clear()  # clear the previous screen for the update circle location

    # write text on the screen
    t.penup()  # don't want to see icon moving on the screen
    t.goto(-350, 350)  # from the current position which is center after clear, move left 350 up 350
    t.pencolor('white')  # text color
    t.write("Use arrows to move, or press 'h' for home", font=("Verdana", 12, "bold"))

    # draw circle
    t.goto(x, y)  # move to the updated x (left-right) and y (up-down) location from center
    t.pendown()  # start drawing the outline of the circle
    t.fillcolor(fill_color)  # fill color of the circle
    t.begin_fill()  # start the fill of whatever is being drawn
    t.circle(game_difficulty)  # diameter of the circle
    t.end_fill()  # done drawing the object to complete the fill


def main():
    """
    The main function, used to test drawing a square

    Returns:
        None
    """
    game_difficulty = int(input(f'{"Select the game difficulty (easy 75, medium 50, hard 25)":.<50s}: '))

    turtle_setup()  # set up the global window screen & turtle and bring window to front

    setup_window('black')  # configure how the turtle window screen will look like

    draw_circle(game_difficulty)  # draw the initial shape based on diameter

    #hidden_obj_setup()  # place the hidden object

    wn.mainloop()  # keep the turtle window open until the user closes it


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
