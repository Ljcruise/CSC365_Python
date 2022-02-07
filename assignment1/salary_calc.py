#!/usr/bin/env python3

# Programmer: Lacie Cruise
# Date: January 25, 2022
# Description: This program calculates annual salary based on hours
# GitHub URL: https://github.com/Ljcruise/Salary_Calculator_A1.git

# display a welcome message
print('The Salary Calculator program')
print('=' * 29)
print()

# get input from the user
salary_amount = float(input('Enter salary amount per hour: $'))
hours_per_week = float(input('Enter hours worked per week: '))
days_per_week = float(input('Enter days worked per week: '))
holidays = float(input('Enter holidays per year: '))
vacation = float(input('Enter vacation days per year: '))

# calculate adjustments and annual salary
workday_per_year = 52 * days_per_week
hours_per_day = (hours_per_week / days_per_week)
unadj_salary = round(workday_per_year * hours_per_day * salary_amount, 2)
annual_salary = round(((workday_per_year - (holidays + vacation)) * hours_per_day) * salary_amount, 2)

# display the result
print()
print(f'Unadjusted Salary: {unadj_salary}')
print(f'Adjusted Annual Salary: {annual_salary}')
print()
print('=' * 29)
print('Come back soon!')
