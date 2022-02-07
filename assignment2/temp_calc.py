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

while True:

    while True:
        temp_conversion = str(input('Would you like to convert to fahrenheit (f) or celsius (c)?: '))
        if temp_conversion == 'f' or 'c':
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
            is_valid = False
        else:
            print('Entry must be between -35 and 400. Please try again.')

    is_valid = True
    while is_valid:
        years = int(input("Enter number of years:\t\t"))
        if 0 < years <= 50:
            is_valid = False
        else:
            print("Entry must be greater than 0 and less than or equal to 50.",
                  "Please try again.")

    print()

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(1, months + 1):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

        # display the results for each year
        if i % 12 == 0:
            print("Year = ", i // 12,
                  "\tFuture Value = ", round(future_value, 2))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    if choice != 'y':
        break

    print()

print("Bye!")
