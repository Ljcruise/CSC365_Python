#!/usr/bin/env python3

import user_object

"""
This module contains functions related to the hot cold game.
It imports modules already created for displaying a random
hidden object and the user's moving circle game piece.
"""

__author__ = 'Lacie Cruise'
__version__ = '1.0'
__copyright__ = 'Copyright 2022.03.04, Hot-Cold Game Assignment'
__github__ = 'https://github.com/Ljcruise/CSC365_Python.git'

def start_game():
    user_object.main()

def main():
    """
    The main function, used to run the program by displaying the main menu and options.
    Args:
        no value
    Returns:
        no value
    """

    start_game()


if __name__ == '__main__':
    main()  # Call the main function
