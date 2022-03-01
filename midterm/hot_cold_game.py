#!/usr/bin/env python3

import turtle
import random

"""
This module contains functions related to the hot cold game.
It imports modules already created for displaying a random
hidden object and the user's moving circle game piece.
"""

__author__ = 'Lacie Cruise'
__version__ = '1.0'
__copyright__ = 'Copyright 2022.03.04, Hot-Cold Game Assignment'
__github__ = 'https://github.com/Ljcruise/CSC365_Python.git'


s = None
t = None
num_moves = 0
circle_size = 50
move_size = 20
x = 0
y = 0
previous_x = 0
previous_y = 0
hidden_x = 0
hidden_y = 0
fill_color = 'blue'
hidden_color = 'black'


def setup_window():
    """
    Controls how the window looks.

    Args:

    Returns:
        None
    """
    global s
    s.tracer(False)  # turn animation off which causes screen flickering as the circle gets redrawn
    s.title('Hot-Cold Game')  # title the title bar of the window

    # set up the keys to listen to and what function should be called
    s.onkeypress(move_home, "h")
    s.onkeypress(move_up, "Up")
    s.onkeypress(move_down, "Down")
    s.onkeypress(move_right, "Right")
    s.onkeypress(move_left, "Left")
    s.listen()  # start listening for keys being pressed


def set_random_location():
    global hidden_x, hidden_y
    while True:
        hidden_x = random.randint(-420, 420)
        hidden_y = random.randint(-300, 300)
    #if not touching:
    #    break


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
    display_user_circle()
    display_hidden_circle()


def move_left():
    """
    Subtract 20 from the x coordinate which will be used move the circle to the left
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x
    x -= 20  # move to the left of center
    display_user_circle()
    display_hidden_circle()


def move_right():
    """
    Add 20 to the x coordinate which will be used move the circle to the right
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x
    x += 20  # move to the right of center
    display_user_circle()
    display_hidden_circle()


def move_up():
    """
    Add 20 to the y coordinate which will be used move the circle up
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global y
    y += 20  # move top of center
    display_user_circle()
    display_hidden_circle()


def move_down():
    """
    Subtract 20 from y coordinate which will be used move the circle to the down
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    Returns:
        None
    """

    global y
    y -= 20  # move down of center
    display_user_circle()
    display_hidden_circle()


def get_size():
    global circle_size, move_size

    circle_size = int(turtle.numinput('Circle', 'Size of circles', minval=10, maxval=100))
    move_size = int(turtle.numinput('Circle', 'Size of move', minval=10, maxval=100))


def set_fill_color():
    global hidden_color, fill_color, x, y, previous_x, previous_y, hidden_x, hidden_y

    overlap = circle_size / 100
    if abs(x - hidden_x) < (circle_size * 2 - overlap) and abs(y - hidden_y) < (circle_size * 2 - overlap):
        hidden_color = 'green yellow'
        fill_color = 'green yellow'
    else:
        if previous_x != x:
            if abs(previous_x - hidden_x) > abs(x - hidden_x):
                fill_color = 'red'
            else:
                fill_color = 'blue'

        if previous_y != y:
            if abs(previous_y - hidden_y) > abs(y - hidden_y):
                fill_color = 'red'
            else:
                fill_color = 'blue'

    previous_x = x
    previous_y = y


def display_instructions():
    # write text on the screen
    t.penup()            # don't want to see icon moving on the screen
    t.goto(-100, 300)  # from the current position which is center after clear, move left 350 up 350
    t.pendown()
    t.pencolor('black')  # text color
    t.write("Use arrows to move, or press 'h' for home", font=("Verdana", 12, "bold"))


def display_user_circle():
    global x, y, fill_color

    t.hideturtle()      # don't show the icon
    t.speed('fastest')  # draw quickly

    t.clear()  # clear the previous screen for the update circle location

    # draw circle
    t.penup()
    t.goto(x, y)             # move to the updated x (left-right) and y (up-down) location from center
    t.pendown()              # start drawing the outline of the circle
    t.fillcolor(fill_color)  # fill color of the circle
    t.begin_fill()           # start the fill of whatever is being drawn
    t.circle(50)             # diameter of the circle
    t.end_fill()             # done drawing the object to complete the fill


def display_hidden_circle():
    global hidden_x, hidden_y, hidden_color

    t.hideturtle()  # don't show the icon
    t.speed('fastest')  # draw quickly
    t.penup()

    # draw circle
    t.goto(hidden_x, hidden_y)  # move to the updated x (left-right) and y (up-down) location from center
    t.pendown()  # start drawing the outline of the circle
    t.fillcolor(hidden_color)  # fill color of the circle
    t.begin_fill()  # start the fill of whatever is being drawn
    t.circle(50)  # diameter of the circle
    t.end_fill()  # done drawing the object to complete the fill


def main():
    """
    The main function, used to run the program by displaying the main menu and options.
    Args:
        no value
    Returns:
        no value
    """
    setup_window()

    display_user_circle()
    display_hidden_circle()
    display_instructions()
    s.mainloop()


if __name__ == '__main__':
    s = turtle.Screen()
    t = turtle.Turtle(visible=False)
    main()  # Call the main function
