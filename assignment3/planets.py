#!/usr/bin/env python3

"""
This program
"""

__author__ = 'Lacie Cruise'
__version__ = '1.0'
__copyright__ = 'Copyright 2022.03.17, Planet Assignment'
__github__ = 'https://github.com/Ljcruise/CSC365_Python.git'


# define a global 2D tuple to store the closest distance each plant is from the sun
# in millions of a mile
planets = (('Mercury', 29), ('Venus', 66), ('Earth', 91), ('Mars', 127),
           ('Jupiter', 460), ('Saturn', 839), ('Uranus', 1710), ('Neptune', 2770))


def get_planet_distance(selected_planet):
    for planet_info in planets:
        planet, distance = planet_info
        print(planet, '|', distance)
        #if current_planet == selected_planet:
            #return distance
        #else:
            #return -1


def distance_from_planet(selected_planet):
    empty_list = []

    get_planet_distance(selected_planet)


def display_planets():
    print('Planets:', end=' ')
    for planet_info in planets:
        planet, distance = planet_info
        print(planet, '|', distance)


def main():
    """
    The main function, used to run the program by displaying the main menu and options.
    Args:
        no value
    Returns:
        no value
    """
    #get_planet_distance()
    display_planets()


if __name__ == '__main__':
    main()  # Call the main function
