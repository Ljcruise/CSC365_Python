#!/usr/bin/env python3

"""
This module validates all numeric input
"""

__author__ = 'Lacie Cruise'
__version__ = '1.0'
__copyright__ = 'CSC365_Python/final'
__github__ = 'https://github.com/Ljcruise/CSC365_Python.git'

import student_data as data

line = ('=' * 80)


def list_students(student_ids):
    """
    The list students function is used to display a list of student's ids and names
    Args:
        no value
    Returns:
        student_ids (int):
    """
    for student_id in student_ids:
        print(student_id,
              data.students[student_id]['firstName'],
              data.students[student_id]['lastName'])


def student_information():
    print(line)
    print('Student Information')
    print(line)

    for student_id in data.students:
        print('ID:', student_id,
              data.students[student_id]['firstName'],
              data.students[student_id]['lastName'])

        for group in data.students[student_id]['groups']:
            print('Groups: ',group, end=', ')

        for subject in data.grades:
            if student_id in data.grades:
                print(data.grades['English'][31])

        print()


def all_sports_list():
    print(line)
    print('All Sports')
    print(line)

    sports = list()


def each_class_genders():
    print(line)
    print('Each Class Genders')
    print(line)

    class_genders = dict()


def sue_smith_class_list():
    print(line)
    print('Sue Smith Class List')
    print(line)

    sue_smith_classes = list()


def students_in_science_not_math():
    print(line)
    print('Students in Science but not in Math')
    print(line)

    science_not_math = list()


def non_sports_groups():
    print(line)
    print('NonSports Groups')
    print(line)

    sports = set()
    non_sports = list()


def all_seasons_sports_students():
    print(line)
    print('All Seasons Sports Students')
    print(line)

    all_seasons = list()


def student_classes_same_as_sue_smith():
    print(line)
    print('Students Classes same as Sue Smith')
    print(line)

    sue_smith_classes = set()
    same_as_sue_smith = list()
    students_classes = dict()


def students_with_low_grades():
    print(line)
    print('Students with Low Grades')
    print(line)

    low_grades = set()


def main():
    """
    The main function in this module is used for testing different logic without going through
     the main menu.
    Args:
        no value
    Returns:
        no value
    """
    student_information()


if __name__ == '__main__':  # if this is the module where the program started from, then run the main function
    main()
