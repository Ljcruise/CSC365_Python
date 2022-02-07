#!/usr/bin/env python3

# Programmer: Lacie Cruise
# Date: February 7, 2022
# Description: This program is a temperature calculator that converts fahrenheit to celsius
# or celsius to fahrenheit. It will continue asking the user if they want to continue
# converting until they decide not to.
# GitHub URL: https://github.com/Ljcruise/CSC365_Python.git

# display a welcome message
print('Welcome to the Temperature Calculator')
print()

while True:
    temp_conversion = str(input('Would you like to convert to fahrenheit (f) or celsius (c)?: '))

    is_valid = True
    while is_valid:
        if temp_conversion == 'f':
            print('Enter the degrees in celsius: ')
            is_valid = False
        else:
            print('Enter the degrees in fahrenheit: ')

    is_valid = True
    while is_valid == True:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            is_valid = False
        else:
            print("Entry must be greater than 0 and less than or equal to 15.",
                  "Please try again.")

    is_valid = True
    while is_valid == True:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
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
