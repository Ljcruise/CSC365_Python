#!/usr/bin/env python3

# Programmer: Lacie Cruise
# Date: February 7, 2022
# Description: This program is a temperature calculator that converts fahrenheit to celsius
# or celsius to fahrenheit. It will continue asking the user if they want to continue
# converting until they decide not to.
# GitHub URL: https://github.com/Ljcruise/CSC365_Python.git

# display a welcome message
print(' ' * 13 + 'Welcome to the Temperature Calculator')
print('=' * 62)
print()
# outer while loop to continue looping as long as the user wants
while True:
    # while loop to get the user's temperature conversion input until it is f or c
    while True:
        user_input = input('Would you like to convert to fahrenheit (f) or celsius (c)?: ')
        temp_conversion = user_input[0].lower()
        if temp_conversion in ['f', 'c']:
            break
        else:
            print('Input must be an f or c. Please try again.')

    is_valid = True
    while is_valid:
        starting_temp = int(input('Enter the starting temp (-35 to 400): '))
        if -35 <= starting_temp <= 400:
            break
        else:
            print('Entry must be between -35 and 400. Please try again.')

    is_valid = True
    while is_valid:
        ending_temp = int(input('Enter the ending temp (-35 to 400): '))
        if -35 <= ending_temp <= 400:
            break
        else:
            print('Entry must be between -35 and 400. Please try again.')

    is_valid = True
    while is_valid:
        temp_step = int(input('Enter the temperature step of your choice (5 or 10): '))
        if temp_step in [5, 10]:
            break
        else:
            print("Entry must be 5 or 10. Please try again.")

    # code for conversion table

    print()

    # see if the user wants to continue
    choice = input("Would you like to continue (y or n)? ")
    print('=' * 62)
    if choice != 'y':
        break

    print()

print("Bye!")
