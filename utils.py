"""
utils.py
--------
Small, hand-written algorithms that map directly to the "Fundamental
Algorithms" unit of the course (summation, counting, exchange of values,
searching and sorting) instead of relying purely on built-in shortcuts.
"""


def calculate_average(marks_list):
    """Summation algorithm: total / count."""
    if not marks_list:
        return 0.0
    total = 0
    for mark in marks_list:
        total += mark
    return total / len(marks_list)


def find_highest(marks_list):
    """Linear search for the maximum value."""
    highest = marks_list[0]
    for mark in marks_list[1:]:
        if mark > highest:
            highest = mark
    return highest


def find_lowest(marks_list):
    """Linear search for the minimum value."""
    lowest = marks_list[0]
    for mark in marks_list[1:]:
        if mark < lowest:
            lowest = mark
    return lowest


def count_pass_fail(marks_list, pass_mark=40):
    """Counting algorithm: how many pass vs fail."""
    passed = 0
    failed = 0
    for mark in marks_list:
        if mark >= pass_mark:
            passed += 1
        else:
            failed += 1
    return passed, failed


def bubble_sort_desc(records):
    """
    Sorts a list of (name, average) tuples in descending order of average,
    using the exchange/swap technique (bubble sort) taught in the unit
    'Introduction to Computer Problem Solving / Fundamental Algorithms'.
    """
    data = records[:]  # work on a copy - do not mutate the caller's list
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]  # exchange values
    return data


def letter_grade_distribution(grades_list):
    """Returns a dictionary counting how many students received each grade."""
    distribution = {}
    for grade in grades_list:
        distribution[grade] = distribution.get(grade, 0) + 1
    return distribution
