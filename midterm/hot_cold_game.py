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

# global variables used to control the game
s = None
t = None
num_moves = 0
circle_size = 100
move_size = 100
# current location of the user's circles
x = 0
y = 0
# previous location of the user's circle to determine if the user is getting closer or further away
previous_x = 0
previous_y = 0
# used to control the hidden circle location
hidden_x = 0
hidden_y = 0
user_color = 'blue'  # color of the user's circle
hidden_color = 'black'  # default color for the hidden circle


def display_game():
    global t

    t.clear()
    #set_fill_color()
    display_user_circle()
    display_hidden_circle()
    display_instructions()


def debug():
    """
    The debug function toggles debug mode so the game is easier to test.
    Args:
        no value
    Returns:
        no value
    """
    global hidden_color

    # if the hidden color is the same as the screen color (black) change the color to gray
    if hidden_color == 'black':
        hidden_color = 'gray'
    else:
        hidden_color = 'black'

    display_game()


def move_home():
    """
    Reset the x and y back to zero coordinate which will be used position the circle in the center
    then call display_game to clear and redraw the screen with the user's updated location

    Returns:
        None
    """

    global x, y
    x = 0  # center of screen moving right or left
    y = 0  # center of screen moving up or down

    display_game()


def move_left():
    """
    Subtract move_size from the x coordinate which will move the circle to the left,
    add one to num_moves, then call display_game to clear and redraw the screen with
    the user's updated location

    Returns:
        None
    """

    global x, num_moves, move_size
    x -= move_size  # move to the left of center
    num_moves += 1

    display_game()


def move_right():
    """
    Add move_size to the x coordinate which will move the circle to the right,
    add one to num_moves, then call display_game to clear and redraw the screen with
    the user's updated location

    Returns:
        None
    """

    global x, num_moves, move_size
    x += move_size  # move to the right of center
    num_moves += 1

    display_game()


def move_up():
    """
    Add move_size to the y coordinate which will move the circle up, add one to num_moves,
    then call display_game to clear and redraw the screen with the user's updated location

    Returns:
        None
    """

    global y, move_size, num_moves
    y += move_size  # move top of center
    num_moves += 1

    display_game()


def move_down():
    """
    Subtract move_size from the y coordinate which will move the circle down,
    add one to num_moves, then call display_game to clear and redraw the screen with
    the user's updated location

    Returns:
        None
    """

    global y, move_size, num_moves
    y -= move_size  # move down of center
    num_moves += 1

    display_game()


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
    s.bgcolor('black')

    # set up the keys to listen to and what function should be called
    s.onkeypress(debug, 'd')
    s.onkeypress(move_home, 'h')
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
    # if not touching:
    #    break


def get_size():
    global circle_size, move_size

    try:
        circle_size = int(turtle.numinput('Circle', 'Size of circles', minval=10, maxval=100))
        move_size = int(turtle.numinput('Circle', 'Size of move', minval=10, maxval=100))
    except:
        circle_size = 50
        move_size = 50


def set_fill_color():
    global hidden_color, user_color, x, y, previous_x, previous_y, hidden_x, hidden_y

    overlap = circle_size * 2 - 10

    # if the circles overlap, then set both circles to a green
    if abs(x - hidden_x) < overlap and abs(y - hidden_y) < overlap:
        hidden_color = 'green yellow'
        user_color = 'green yellow'
    else:
        if previous_x != x:
            if abs(previous_x - hidden_x) > abs(x - hidden_x):
                user_color = 'red'
            else:
                user_color = 'blue'

        if previous_y != y:
            if abs(previous_y - hidden_y) > abs(y - hidden_y):
                user_color = 'red'
            else:
                user_color = 'blue'

    previous_x = x
    previous_y = y


def display_instructions():
    global num_moves

    # write text on the screen
    t.penup()  # don't want to see icon moving on the screen
    t.goto(-375, 300)  # from the current position which is center after clear, move left 375 up 300
    t.pendown()
    t.pencolor('white')  # text color
    t.write('Use arrows to move', font=('Verdana', 12, 'bold'))
    t.penup()
    t.goto(-375, 280)
    t.pendown()
    t.pencolor('white')  # text color
    t.write('d = debug', font=('Verdana', 12, 'bold'))
    t.penup()
    t.goto(-375, 260)
    t.pendown()
    t.pencolor('white')  # text color
    t.write('h = home', font=('Verdana', 12, 'bold'))
    t.penup()
    t.goto(-375, 240)
    t.pendown()
    t.pencolor('white')  # text color
    t.write('r = reset', font=('Verdana', 12, 'bold'))


def display_user_circle():
    """
    This function displays the user's circle based on the circle size,
    x and y location, and the user's color

    Returns:
        None
    """
    global x, y, user_color, circle_size

    t.hideturtle()  # don't show the icon
    t.speed('fastest')  # draw quickly

    t.clear()  # clear the previous screen for the update circle location

    # draw circle
    t.penup()
    t.goto(x, y)  # move to the updated x (left-right) and y (up-down) location from center
    t.pencolor('black')
    t.pendown()  # start drawing the outline of the circle
    t.fillcolor(user_color)  # fill color of the circle
    t.begin_fill()  # start the fill of whatever is being drawn
    t.circle(circle_size)  # diameter of the circle
    t.end_fill()  # done drawing the object to complete the fill

    display_instructions()


def display_hidden_circle():
    """
    This function displays the hidden circle based on the circle size,
    hidden x and y location, and the hidden color

    Returns:
        None
    """
    global hidden_x, hidden_y, hidden_color, circle_size

    t.hideturtle()  # don't show the icon
    t.speed('fastest')  # draw quickly
    t.penup()

    # draw circle
    t.goto(300, 200)  # move to the updated x (left-right) and y (up-down) location from center
    t.pencolor('black')
    t.pendown()  # start drawing the outline of the circle
    t.fillcolor(hidden_color)  # fill color of the circle
    t.begin_fill()  # start the fill of whatever is being drawn
    t.circle(circle_size)  # diameter of the circle
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
    display_game()
    s.mainloop()


if __name__ == '__main__':
    s = turtle.Screen()
    t = turtle.Turtle(visible=False)
    main()  # Call the main function
