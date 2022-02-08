#!/usr/bin/env python3

# Programmer: Lacie Cruise
# Date: February 7, 2022
# Description: This program is a temperature calculator that converts fahrenheit to celsius
# or celsius to fahrenheit. It will continue asking the user if they want to continue
# converting until they decide not to.
# GitHub URL: https://github.com/Ljcruise/CSC365_Python.git

line_length = 65

# display a welcome message
print(' ' * 14 + 'Welcome to the Temperature Calculator')
print('=' * line_length)
print()

# outer while loop to continue looping as long as the user wants
while True:
    # while loop to get the user's temperature conversion input until it is f or c
    while True:
        # if they enter f, they want to convert to celsius
        user_input = input('Would you like to convert to fahrenheit (f) or to celsius (c)?: ')
        temp_conversion = user_input[0].lower()
        if temp_conversion in ['f', 'c']:
            break
        else:
            print('Input must be an f or c. Please try again.')

    while True:
        starting_temp = int(input('Enter the starting temp (-35 to 400): '))
        if -35 <= starting_temp <= 400:
            break
        else:
            print('Entry must be between -35 and 400. Please try again.')

    while True:
        ending_temp = int(input('Enter the ending temp (-35 to 400): '))
        if -35 <= ending_temp <= 400:
            break
        else:
            print('Entry must be between -35 and 400. Please try again.')

    while True:
        step_temp = int(input('Enter the temperature step of your choice (5, 10, 15): '))
        if step_temp in [5, 10, 15]:
            break
        else:
            print("Entry must be 5 or 10. Please try again.")

    print(f"{'-' * line_length}")
    print(f"{'F' : ^30}{'C' : ^30}")
    print('=' * line_length)

    for temp in range(starting_temp, ending_temp, step_temp):
        if temp_conversion == 'f':
            conv_temp = round(temp * 9 / 5 + 32)  # converting to fahrenheit
        else:
            conv_temp = round((temp - 32) * 5 / 9)  # converting to celsius

        print(f'{temp: >15} {conv_temp: >29}')

    print('=' * line_length)
    print()

    # see if the user wants to continue
    while True:
        choice = input("Would you like to continue (y or n)? ")
        print('=' * line_length)
        if choice != 'y':
            break

    print()

print("Bye!")
