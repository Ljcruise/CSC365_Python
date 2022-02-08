#!/usr/bin/env python3

# Programmer: Lacie Cruise
# Date: February 8, 2022
# Description: This program is a temperature calculator that converts fahrenheit to celsius
# or celsius to fahrenheit. It will continue asking the user if they want to continue
# converting until they decide not to. The user gets to enter the starting and ending
# values and the amount they want to increase by each loop.
# GitHub URL: https://github.com/Ljcruise/CSC365_Python.git

line_length = 70

# display a welcome message
print(f"{'Welcome to the Temperature Calculator': ^70}")

# outer while loop to continue looping as long as the user wants
while True:
    print('=' * line_length)

    # while loop to get the user's temperature conversion input until it is f or c
    while True:
        # if they enter f, they want to convert to celsius
        user_input = input(f'{"Would you like to convert to fahrenheit (f) or to celsius (c)?: ":<65s} ')
        temp_conversion = user_input[0].lower()
        if temp_conversion in ['f', 'c']:
            break
        else:
            print('Input must be an f or c. Please try again.')

    # while loop to get the user's temperature they want to start at
    while True:
        starting_temp = int(input(f'{"Enter the starting temperature (-35 to 400)":<65s} '))
        if -35 <= starting_temp <= 400:
            break
        else:
            print('Entry must be between -35 and 400. Please try again.')

    # while loop to get the temperature the user wants to stop at
    while True:
        ending_temp = int(input(f'{"Enter the ending temperature (-35 to 400)":<65s} '))
        if -35 <= ending_temp <= 400:
            break
        else:
            print('Entry must be between -35 and 400. Please try again.')

    # while loop to get the step the user wants to increase the temp
    while True:
        step_temp = int(input(f'{"Enter the temperature step of your choice (1 to 20)":<65s} '))
        if 1 <= step_temp <= 20:
            break
        else:
            print('Entry must be between 1 and 20. Please try again.')

    # formatting for the start of the conversion table
    print(f'{"":=<13}')
    print(f"|{'F':^5}|{'C':^5}|")
    print(f'{"":=<13}')

    # for loop that compares the starting and ending temp as well as the step to know
    # how many times to loop through the conversions.
    for temp in range(starting_temp, ending_temp, step_temp):
        if temp_conversion == 'f':
            conv_temp = round(temp * 9 / 5 + 32)  # converting to fahrenheit
        else:
            conv_temp = round((temp - 32) * 5 / 9)  # converting to celsius

        print(f'| {temp:3.0f} | {conv_temp:3.0f} |')

    print(f'{"":=<13}')
    print()

    # see if the user wants to continue
    choice = input('Would you like to continue (y or n)? ')
    if choice != 'y':
        break

    print()

print("Bye!")
