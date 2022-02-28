#!/usr/bin/env python3

import global_turtle

"""
This module contains functions related to drawing and moving a circle around the screen
"""

__author__ = 'Lacie Cruise'
__version__ = '1.0'
__copyright__ = 'Copyright 2022.03.04, Hot-Cold Game Assignment'
__github__ = 'https://github.com/Ljcruise/CSC365_Python.git'

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
    draw_circle(game_difficulty=50)


def move_left():
    """
    Subtract 20 from the x coordinate which will be used move the circle to the left
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x
    x -= 20  # move to the left of center
    draw_circle(game_difficulty=50)


def move_right():
    """
    Add 20 to the x coordinate which will be used move the circle to the right
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x
    x += 20  # move to the right of center
    draw_circle(game_difficulty=50)


def move_up():
    """
    Add 20 to the y coordinate which will be used move the circle up
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global y
    y += 20  # move top of center
    draw_circle(game_difficulty=50)


def move_down():
    """
    Subtract 20 from y coordinate which will be used move the circle to the down
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    Returns:
        None
    """

    global y
    y -= 20  # move down of center
    draw_circle(game_difficulty=50)


def setup_window(bg_color='white'):
    """
    Controls how the window looks.

    Args:
        bg_color (str): the background color of the window (default white)

    Returns:
        None
    """

    global_turtle.wn.tracer(False)  # turn animation off which causes screen flickering as the circle gets redrawn
    global_turtle.wn.title('Hot-Cold Turtle Game')  # title the title bar of the window
    global_turtle.wn.bgcolor(bg_color)  # set the window's background color
    global_turtle.wn.setup(800, 800)  # the size of the window

    # set up the keys to listen to and what function should be called
    global_turtle.wn.onkeypress(move_home, "h")
    global_turtle.wn.onkeypress(move_up, "Up")
    global_turtle.wn.onkeypress(move_down, "Down")
    global_turtle.wn.onkeypress(move_right, "Right")
    global_turtle.wn.onkeypress(move_left, "Left")
    global_turtle.wn.listen()  # start listening for keys being pressed


def draw_circle(game_difficulty):
    """
    clear the screen and draw the circle based on the x & y coordinates

    Args:
        #fill_color (str): the inside color of the circle (default red)
        game_difficulty (int): controls the size of the circle (default 50)

    Returns:
        None
    """

    global x, y, fill_color

    global_turtle.t.hideturtle()  # don't show the icon
    global_turtle.t.speed('fastest')  # draw quickly

    global_turtle.t.clear()  # clear the previous screen for the update circle location

    # write text on the screen
    global_turtle.t.penup()  # don't want to see icon moving on the screen
    global_turtle.t.goto(-350, 350)  # from the current position which is center after clear, move left 350 up 350
    global_turtle.t.pencolor('white')  # text color
    global_turtle.t.write("Use arrows to move, or press 'h' for home", font=("Verdana", 12, "bold"))

    # draw circle
    global_turtle.t.goto(x, y)  # move to the updated x (left-right) and y (up-down) location from center
    global_turtle.t.pendown()  # start drawing the outline of the circle
    global_turtle.t.fillcolor(fill_color)  # fill color of the circle
    global_turtle.t.begin_fill()  # start the fill of whatever is being drawn
    global_turtle.t.circle(game_difficulty)  # diameter of the circle
    global_turtle.t.end_fill()  # done drawing the object to complete the fill


def main():
    """
    The main function, used to test moving the user's object

    Returns:
        None
    """
    game_difficulty = int(input(f'{"Select the game difficulty (easy 75, medium 50, hard 25)":.<50s}: '))

    global_turtle.turtle_setup()  # set up the global window screen & turtle and bring window to front

    setup_window('black')  # configure how the turtle window screen will look like

    draw_circle(game_difficulty)  # draw the initial shape based on diameter

    global_turtle.wn.mainloop()  # keep the turtle window open until the user closes it


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
