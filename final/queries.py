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
tab = '\t'


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

    for student_id, student_data in data.students.items():
        print('ID:', student_id,
              data.students[student_id]['first_name'],
              data.students[student_id]['last_name'])

        for groups in data.students[student_id]['groups']:
            print(tab, 'Groups: ', groups, end=', ')

        print()

        for subject, grades in data.grades.items():
            if student_id in data.grades[subject]:
                print(tab, subject, data.grades[subject][student_id])

        print()


def all_sports_list():
    print(line)
    print('All Sports')
    print(line)

    sports = list()

    for season, season_sports in data.sports.items():
        # append the sports list by converting the set to a list and using the extend
        # function to append it
        sports.extend(list(season_sports))

    sports.sort()   # sort list

    # for loop for displaying the list
    for sport in sports:
        print(sport)


def each_class_genders():
    print(line)
    print('Each Class Genders')
    print(line)

    class_gender = dict()

    for subject, grades in data.grades.items():
        # set male and female counters to 0
        male_count = 0
        female_count = 0

        for student_id, grades in data.grades.items():
            # get gender for the current student id (key) from the 2D data.students dict
            gender = data.students[student_id]['gender']
            print(gender)

            if gender == 'F':
                female_count += 1
            else:
                male_count += 1


        #	append to the class gender dict, using the class as the key, and...
        #   a dict with female and male counts (see above example)
        class_gender[subject].append(female_count)
        class_gender[subject].append(male_count)

        #for key(class), value (genders dict) in class gender 2D dict items
        for subject, genders in class_gender.items():
            print(subject,': ', genders)
            #display the course, and genders dict


def sue_smith_class_list():
    print(line)
    print('Sue Smith Class List')
    print(line)

    sue_smith_classes = list()

    for student_id, student_data in data.students.items():
        # get first and last names from the student data dict
        first_name = data.students[student_id]['first_name']
        last_name = data.students[student_id]['last_name']

        # if first and last name is Sue Smith, for each subject Sue Smith's student
        # id is in, append the empty list created above
        if first_name == 'Sue' and last_name == 'Smith':
            for subject, grades in data.grades.items():
                if student_id in data.grades[subject]:
                    sue_smith_classes.append(subject)

    sue_smith_classes.sort()   # sort the list

    print(*sue_smith_classes, sep=', ')   # print Sue Smiths classes, separated by a comma


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
    #student_information()                  # need to fix groups
    #all_sports_list()                      # done
    each_class_genders()
    #sue_smith_class_list()                 # done
    #students_in_science_not_math()
    #non_sports_groups()
    #all_seasons_sports_students()
    #student_classes_same_as_sue_smith()
    #students_with_low_grades()


if __name__ == '__main__':  # if this is the module where the program started from, then run the main function
    main()
