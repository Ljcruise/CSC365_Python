import turtle

"""
Objects & methods that all shapes uses to share one global turtle and window screen.
"""

__author__ = 'Lacie Cruise'
__version__ = '1.0'
__copyright__ = 'Copyright 2022.03.04, Hot-Cold Game Assignment'
__github__ = 'https://github.com/Ljcruise/CSC365_Python.git'

wn = None  # the global window screen that the game will use
t = None   # the global turtle that all shapes will share
hidden_obj = None  # the global hidden object for the game


def turtle_setup():
    """
    All shape need to share the same window screen & turtle objects
    Also, sets the newly open window screen on top of other windows

    Returns:
        None
    """
    global wn, t, hidden_obj
    wn = turtle.Screen()  # used to control the window
    t = turtle.Turtle()  # basically this is your cursor that you used to draw with
    hidden_obj = turtle.Turtle()

    # make sure the turtle window screen displays on top of other open windows
    root_window = wn.getcanvas().winfo_toplevel()  # get the top level turtle screen canvas
    root_window.call('wm', 'attributes', '.', '-topmost', '1')  # and make it have the top focus
