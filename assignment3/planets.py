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
    """
    This function gets the selected planet's distance from the sun.
    Args:
        no value
    Returns:
        distance
    """
    for planet_info in planets:
        planet, distance = planet_info
        if planet == selected_planet:
            return distance
    return -1


def display_distances(selected_planet, distance_list):
    """
    This function displays the generated list for each planet's distance
    from the selected planet
    Args:
        no value
    Returns:
        no value
    """
    for generated_list in distance_list:
        planet, distance = generated_list
        print(planet, ' is ', distance, ' million miles from ', selected_planet)


def distance_from_planet(selected_planet):
    """
    This function generates a list for each planet's distance from the
    selected planet
    Args:
        no value
    Returns:
        no value
    """
    distance_list = []

    selected_distance = get_planet_distance(selected_planet)

    if selected_distance == -1:
        print('Unable to locate ' + selected_planet + ' in the list.')
        return

    for planet_info in planets:
        planet, distance = planet_info
        if planet != selected_planet:
            distance_from_selected = abs(distance - selected_distance)
            distance_list.append([planet, distance_from_selected])

    distance_list.sort(key=lambda x: x[1])
    display_distances(selected_planet, distance_list)


def display_planets():
    """
    This function displays the plant's names from the tuple list on one line
    Args:
        no value
    Returns:
        no value
    """
    print('Planets:', end=' ')
    for planet_info in planets:
        planet, distance = planet_info
        print(planet, end=' ')


def main():
    """
    The main function, used to keep the program looping until the user enters q for quit
    Args:
        no value
    Returns:
        no value
    """
    while True:
        display_planets()   # display list of planets to choose from
        print()
        user_input = input('Please enter a planet name from above or q to quit: ')
        selected_planet = user_input.capitalize()
        break
    distance_from_planet(selected_planet)


if __name__ == '__main__':
    main()  # Call the main function
