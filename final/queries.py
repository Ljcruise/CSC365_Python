#!/usr/bin/env python3

"""
This module contains the functions that will be called in the main menu.
The functions all do similar, yet different things by using the student_data
module to get different information based on what the function is looking for.
"""

__author__ = 'Lacie Cruise'
__version__ = '1.0'
__copyright__ = 'CSC365_Python/final'
__github__ = 'https://github.com/Ljcruise/CSC365_Python.git'

import student_data as data

line = ('=' * 80)
line2 = ('-' * 80)


def list_students(student_ids):
    """
    The list students function is used to display a list of student's ids and names
    Args:
        no value
    Returns:
        student_ids (int): unique id given to each student
    """

    for student_id in student_ids:
        print('#', student_id,
              data.students.get(student_id).get('first_name'),
              data.students.get(student_id).get('last_name'))


def student_information():
    """
    The student information function uses information from the student's dictionary
    to print a report for each student using their id, the groups they are a part of,
    and their classes and grades.
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('Student Information')
    print(line2)

    # print the student's id and first and last name
    for student_id, student_data in data.students.items():
        print('ID:', student_id,
              student_data.get('first_name'),
              student_data.get('last_name'))

        print('\t', 'Groups: ', end='')
        # print the groups the student is involved in
        print(*student_data.get('groups'), sep=', ')

        # print the students grades for each class
        for subject, grades in data.grades.items():
            if student_id in grades:
                print('\t', subject, grades.get(student_id))
        print()


def all_sports_list():
    """
    The all sports list function displays all the sports students can be a part of
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('All Sports')
    print(line2)

    sports = list()

    for season, season_sports in data.sports.items():
        # append the sports list by converting the set to a list and using the extend
        # function to append it
        sports.extend(list(season_sports))

    sports.sort()  # sort list

    print(*sports)


def each_class_genders():
    """
    The class genders function displays the number of males and females in each class
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('Each Class Genders')
    print(line2)

    class_gender = dict()
    # 'math': {'Female': 3, 'Male': 1}
    # 'english': {'Female': 3, 'Male': 2}
    # 'science': {'Female': 3, 'Male': 2}

    for subject, grades in data.grades.items():
        # set male and female counters to 0
        male_count = 0
        female_count = 0

        for student_id, student_grades in grades.items():
            # get gender for the current student id from the 2D data.students dict
            gender = data.students[student_id]['gender']

            if gender == 'F':
                female_count += 1
            if gender == 'M':
                male_count += 1

        # append to the class gender dict, using the class as the key, and...
        # a dict with female and male counts (see above example)
        class_gender[subject] = {'male': male_count, 'female': female_count}

    for subject, genders in class_gender.items():
        print(subject + ':', 'Male =', genders.get('male'), 'Female =', genders.get('female'))


def sue_smith_class_list():
    """
    This function displays all of Sue Smiths classes
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('Sue Smith Class List')
    print(line2)

    sue_smith_classes = list()

    for student_id, student_data in data.students.items():
        # get first and last names from the student data dict
        first_name = student_data.get('first_name')
        last_name = student_data.get('last_name')

        # if first and last name is Sue Smith, for each subject Sue Smith's student
        # id is in, append the empty list created above
        if first_name == 'Sue' and last_name == 'Smith':
            for subject, grades in data.grades.items():
                if student_id in data.grades[subject]:
                    sue_smith_classes.append(subject)

    sue_smith_classes.sort()  # sort the list

    print(*sue_smith_classes, sep=', ')  # print Sue Smiths classes, separated by a comma


def students_in_science_not_math():
    """
    This function calls the list students function to display the students who
    are taking a science class and not a math class.
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('Students in Science but not in Math')
    print(line2)

    science_not_math = list()

    for student_id in data.students.keys():
        # check if the student's id is in the grades dictionary under Science and not Math
        if student_id in data.grades['Science'] and student_id not in data.grades['Math']:
            science_not_math.append(student_id)

    science_not_math.sort()   # sort the list

    list_students(science_not_math)   # call list students to display the students id and name


def non_sports_groups():
    """
    The non-sport group function displays the activities that are not
    part of the sports dictionary
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('Non-Sports Groups')
    print(line2)

    sports = set()
    non_sports = list()

    # build the sports set
    for season, season_sports in data.sports.items():
        # append the season sports set to the sports set using update method
        sports.update(season_sports)

    # build the non_sports list
    for student_id, student_data in data.students.items():
        student_groups = student_data.get('groups')
        leftover = student_groups - sports

        if len(leftover) != 0:
            non_sports.append(*leftover)  # use the * to convert the set to a tuple

    non_sports.sort()

    print(*non_sports, sep='\n')


def all_seasons_sports_students():
    """
    This function calls the list students function to display the students who
    are in sports for all four seasons.
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('Students in All Four Seasons of Sports')
    print(line2)

    all_seasons = list()

    for student_id, student_data in data.students.items():
        student_groups = student_data.get('groups')

        if student_groups & data.sports.get('fall') \
                and student_groups & data.sports.get('winter') \
                and student_groups & data.sports.get('spring') \
                and student_groups & data.sports.get('summer'):
            all_seasons.append(student_id)

    all_seasons.sort()

    list_students(all_seasons)


def student_classes_same_as_sue_smith():
    """
    This function calls the list students function to display the students who
    are taking the same classes as Sue Smith
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('Students in Same Classes as Sue Smith')
    print(line2)

    sue_smith_classes = set()
    same_as_sue_smith = list()
    students_classes = dict()

    # build the sue_smith_classes set and students_classes dictionary
    for student_id, student_data in data.students.items():
        student_classes = set()
        first_name = student_data.get('first_name')
        last_name = student_data.get('last_name')

        for subject, grades in data.grades.items():
            if student_id in grades:
                student_classes.add(subject)

        if (first_name + last_name) == 'SueSmith':
            sue_smith_classes = student_classes
        else:
            # add the student id students_classes value to student_classes
            students_classes[student_id] = student_classes

    # for loop to build same_as_sue_smith list
    for student_id, subject in students_classes.items():
        if subject == sue_smith_classes:
            same_as_sue_smith.append(student_id)

    same_as_sue_smith.sort()   # sort list

    list_students(same_as_sue_smith)   # display student's id and name


def students_with_low_grades():
    """
    This function calls the list students function to display the students who
    have average grades below 70.
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('Students with Low Grades')
    print(line2)

    low_grades = set()

    # build the low_grades set
    for student_id, student_data in data.students.items():
        for subject, grades in data.grades.items():
            if student_id in data.grades[subject]:

                grade_total = sum(grades.get(student_id))
                grade_count = len(grades.get(student_id))

                # calculate average
                average = grade_total / grade_count
                if average < 70:
                    low_grades.add(student_id)

    # convert to list and sort
    low_grades_list = list(low_grades)

    list_students(low_grades_list)


def main():
    """
    The main function in this module is used for testing different logic without going through
    the main menu.
    Args:
        no value
    Returns:
        no value
    """

    # student_information()
    # all_sports_list()
    # each_class_genders()
    # sue_smith_class_list()
    # students_in_science_not_math()
    # non_sports_groups()
    # all_seasons_sports_students()
    # student_classes_same_as_sue_smith()
    # students_with_low_grades()


if __name__ == '__main__':  # if this is the module where the program started from, then run the main function
    main()
