#!/usr/bin/env python3

import turtle
import random

"""
This program creates a hot-cold game using turtle. The user will determine the size of the
circles for the game to decide difficulty. The goal is to find a hidden object in as few of
moves as possible. The color of the user's circle will change depending on how 'hot' or 'cold'
(close or far) the user is away from the hidden object.
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
    """
    The display_game function clears the turtle drawings, then calls different
    functions created below to set the colors, draw the user circle and hidden
    circle, and display the game instructions
    Args:
        no value
    Returns:
        no value
    """
    global t

    t.clear()
    set_fill_color()
    display_user_circle()
    display_hidden_circle()
    display_instructions()


def get_size():
    """
    This function gets the user's input for the size of the circles and the movement.
    If the user closes the prompt without entering a number, the default is 50 for both.

    Returns:
        None
    """
    global circle_size, move_size
    # get the user's input for the size of circles and the size of the move
    try:
        circle_size = int(turtle.numinput('Circle', 'Size of circles (10-100)', minval=10, maxval=100))
        move_size = int(turtle.numinput('Circle', 'Size of move (10-100)', minval=10, maxval=100))
    except:
        circle_size = 50
        move_size = 50


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


def setup_game():
    """
    The setup game function basically resets the program. It resets the number of moves,
    changes the color of the hidden circle back to black, clears the screen, resets the
    window, then prompts the user for the size of the shapes and moves, and sets the
    center location and hidden location.
    Args:
        no value
    Returns:
        no value
    """
    global s, t, num_moves, hidden_color

    num_moves = 0
    hidden_color = 'black'
    t.clear()
    setup_window()
    t.speed('fastest')  # draw quickly
    get_size()
    set_center_location()
    set_hidden_location()

    # set up the keys to listen to and what function should be called
    s.onkeypress(debug, 'd')
    s.onkeypress(move_home, 'h')
    s.onkeypress(start_game, 'r')
    s.onkeypress(move_up, "Up")
    s.onkeypress(move_down, "Down")
    s.onkeypress(move_right, "Right")
    s.onkeypress(move_left, "Left")
    s.listen()  # start listening for keys being pressed


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

    global x, num_moves
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

    global x, num_moves
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

    global y, num_moves
    y += move_size  # move up of center
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

    global y, num_moves
    y -= move_size  # move down of center
    num_moves += 1

    display_game()


def set_hidden_location():
    """
    This function generates a random location for the hidden circle based on the default
    screen size. It checks to see how close the random location is to the user circle
    starting location, ensuring that the hidden circle does not start too close to the
    user circle.
    Args:
        no value
    Returns:
        no value
    """
    global hidden_x, hidden_y
    too_close = 2 * circle_size + 10

    while True:
        # generate a random x and y location in the default screen size
        hidden_x = random.randint(-420, 420)
        hidden_y = random.randint(-300, 300)

        if abs(hidden_x) > too_close and abs(hidden_y) > too_close:
            break


def set_center_location():
    """
    The set center location function places the user's circle in the middle of the screen
    based on the circle's size.
    Args:
        no value
    Returns:
        no value
    """
    global x, y, user_color

    center_pos = int(circle_size / 2) * -1

    x = center_pos
    y = center_pos


def set_fill_color():
    """
    This function sets the amount the user's circle must overlap the hidden circle in order
    to 'win' the game. It also checks the distance the user's circle is from the hidden
    object to determine if the user is getting closer (red) or farther away (blue).
    Args:
        no value
    Returns:
        no value
    """
    global hidden_color, user_color, previous_x, previous_y

    overlap = circle_size * 2 - 10

    # if the circles overlap, then set both circles to a green shade
    if abs(x - hidden_x) < overlap and abs(y - hidden_y) < overlap:
        hidden_color = 'green yellow'
        user_color = 'yellow green'
    else:
        if previous_x != x:
            # if the previous location is closer to the hidden location change the
            # color to red, else change it to blue
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
    """
    The display instructions function displays the total number of user's moves in the right-hand
    corner, and displays the instructions in the left-hand corner.
    Args:
        no value
    Returns:
        no value
    """
    t.penup()
    t.goto(225, 300)  # from the center, move right 225 and up 300
    t.pendown()
    t.pencolor('white')  # text color
    t.write('Total moves= {}'.format(num_moves), font=('Verdana', 12, 'bold'))

    # write instructions on the screen
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

    t.hideturtle()  # don't show the icon
    t.speed('fastest')  # draw quickly
    t.penup()

    # draw circle
    t.goto(hidden_x, hidden_y)  # move to the hidden x and y location
    t.pencolor('black')
    t.pendown()  # start drawing the outline of the circle
    t.fillcolor(hidden_color)  # fill color of the circle
    t.begin_fill()  # start the fill of whatever is being drawn
    t.circle(circle_size)  # diameter of the circle
    t.end_fill()  # done drawing the object to complete the fill


def start_game():
    """
    The main function, used to run the program by displaying the main menu and options.
    Args:
        no value
    Returns:
        no value
    """
    setup_game()
    display_game()
    s.mainloop()


if __name__ == '__main__':
    s = turtle.Screen()
    t = turtle.Turtle(visible=False)
    start_game()  # Call the main function
