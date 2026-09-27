"""
performance_analyzer.py
--------------------------
FUNCTIONAL MODULE 3: Performance Analytics
Computes class-wide statistics and rankings on top of the per-student
grades produced by grade_calculator.py. This is where the algorithms
from utils.py (sorting, counting, min/max) are put to use.
"""

from utils import find_highest, find_lowest, count_pass_fail, bubble_sort_desc, \
    letter_grade_distribution
from grade_calculator import build_grade_report, calculate_percentage


def class_statistics(students):
    """Returns overall class statistics as a dictionary."""
    if not students:
        return None

    grade_report = build_grade_report(students)
    percentages = [info["percentage"] for info in grade_report.values()]
    grades = [info["grade"] for info in grade_report.values()]

    class_average = round(sum(percentages) / len(percentages), 2)
    highest = find_highest(percentages)
    lowest = find_lowest(percentages)
    passed, failed = count_pass_fail(percentages)
    distribution = letter_grade_distribution(grades)

    return {
        "class_average": class_average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed,
        "failed": failed,
        "grade_distribution": distribution,
        "total_students": len(students),
    }


def rank_students(students):
    """
    Returns a list of (name, percentage) tuples sorted from
    highest to lowest performance, using the bubble-sort routine.
    """
    records = [
        (info["name"], calculate_percentage(info["marks"]))
        for info in students.values()
    ]
    return bubble_sort_desc(records)


def display_class_statistics(students):
    """Prints a readable statistics summary to the console."""
    stats = class_statistics(students)
    if stats is None:
        print("No data available for analysis.\n")
        return

    print("\n----- CLASS PERFORMANCE SUMMARY -----")
    print(f"Total Students : {stats['total_students']}")
    print(f"Class Average  : {stats['class_average']}%")
    print(f"Highest Score  : {stats['highest']}%")
    print(f"Lowest Score   : {stats['lowest']}%")
    print(f"Passed         : {stats['passed']}")
    print(f"Failed         : {stats['failed']}")
    print("Grade Distribution:")
    for grade, count in sorted(stats["grade_distribution"].items()):
        print(f"   {grade}: {count}")
    print()


def display_ranking(students):
    """Prints the class ranking (1st, 2nd, 3rd, ...)."""
    ranking = rank_students(students)
    if not ranking:
        print("No data available for ranking.\n")
        return

    print("\n----- CLASS RANKING -----")
    for position, (name, percentage) in enumerate(ranking, start=1):
        print(f"{position}. {name} - {percentage}%")
    print()
