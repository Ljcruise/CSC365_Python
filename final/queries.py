#!/usr/bin/env python3

"""
This module
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
        student_ids (int): unique id given to each student
    """

    for student_id in student_ids:
        print('#', student_id,
              data.students[student_id]['first_name'],
              data.students[student_id]['last_name'])


def student_information():
    """
    The student information function uses information from the students dictionary
    to print a report for each student using their id, the groups they are apart of,
    and their classes and grades.
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('Student Information')
    print(line)

    # print the student's id and first and last name
    for student_id, student_data in data.students.items():
        print('ID:', student_id,
              data.students[student_id]['first_name'],
              data.students[student_id]['last_name'])

        # print the groups the student is involved in
        for groups in data.students[student_id]['groups']:
            print(tab, 'Groups: ', groups, end=', ')
        print()

        # print the students grades for each class
        for subject, grades in data.grades.items():
            if student_id in data.grades[subject]:
                print(tab, subject, data.grades[subject][student_id])
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
    print(line)

    sports = list()

    for season, season_sports in data.sports.items():
        # append the sports list by converting the set to a list and using the extend
        # function to append it
        sports.extend(list(season_sports))

    sports.sort()  # sort list

    # for loop for displaying the list
    for sport in sports:
        print(sport)


def each_class_genders():
    """
    The each class genders function displays each class with the number of
    males and females in each.
    Args:
        no value
    Returns:
        no value
    """

    print(line)
    print('Each Class Genders')
    print(line)

    class_gender = dict()
    # 'math': {'Female': 3, 'Male': 1}
    # 'english': {'Female': 3, 'Male': 2}
    # 'science': {'Female': 3, 'Male': 2}

    for subject, grades in data.grades.items():
        # set male and female counters to 0
        male_count = 0
        female_count = 0

        for student_id, grades in data.grades.items():
            # get gender for the current student id from the 2D data.students dict
            gender = data.students[student_id]['gender']

            if gender == 'F':
                female_count += 1
            else:
                male_count += 1

        #	append to the class gender dict, using the class as the key, and...
        #   a dict with female and male counts (see above example)
        class_gender[subject].append(female_count)
        class_gender[subject].append(male_count)

        for subject, genders in class_gender.items():
            print(subject, genders)


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
    print(line)

    science_not_math = list()

    for student_id, student_data in data.students.items():
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
    print('NonSports Groups')
    print(line)

    sports = set()
    non_sports = list()

    # build the sports set
    for season, season_sports in data.sports.items():
        # append the season sports set to the sports set using update method
        sports.update(season_sports)

    # build the non_sports list
    for student_id, student_data in data.students.items():
        student_groups = data.students[student_id]['groups']
        leftover = student_groups - sports
        if leftover != 0:
            non_sports.append(*leftover)  # use the * to convert the set to a tuple

    non_sports.sort()

    for non_sport in non_sports:
        print(non_sport)


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
    print(line)

    all_seasons = list()

    for student_id, student_data in data.students.items():
        student_groups = data.students[student_id]['groups']

        if student_groups & data.sports['fall'] \
                and student_groups & data.sports['winter'] \
                and student_groups & data.sports['spring'] \
                and student_groups & data.sports['summer']:
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
    print(line)

    sue_smith_classes = set()
    same_as_sue_smith = list()
    students_classes = dict()

    # build the sue_smith_classes set and students_classes dictionary
    for student_id, student_data in data.students.items():
        student_classes = set()
        first_name = data.students[student_id]['first_name']
        last_name = data.students[student_id]['last_name']
        name = first_name + ' ' + last_name   # combine first and last name

        for subject, grades in data.grades.items():
            if student_id in data.grades[subject]:
                student_classes.add(subject)

        if name == 'Sue Smith':
            sue_smith_classes = list(student_classes)
        else:
            student_classes.add({student_id: students_classes})
            print(student_classes)

    # for loop to build same_as_sue_smith list
    for student_id, classes in students_classes.items():
        if classes == sue_smith_classes:
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
    print(line)

    low_grades = set()

    # build the low_grades set
    for student_id, student_data in data.students.items():
        for subject, grades in data.grades.items():
            if student_id in data.grades:
                print()
        # grade total = sum of student grades student_id (outer key) to grade total
        # grade count = len of student grades student_id (outer key) to grade count
        # calculate average
        # if average < 70
            # low_grades.add(student_id)

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
    student_information()                  # need to fix groups
    # all_sports_list()                      # done
    # each_class_genders()                   # errors
    # sue_smith_class_list()                 # done
    # students_in_science_not_math()         # done
    # non_sports_groups()                    # fix append
    # all_seasons_sports_students()          # done
    # student_classes_same_as_sue_smith()    # fix add function in if else statement
    # students_with_low_grades()


if __name__ == '__main__':  # if this is the module where the program started from, then run the main function
    main()
