"""
grade_calculator.py
---------------------
FUNCTIONAL MODULE 2: Grade Calculation
Converts raw marks into percentages and letter grades using simple
conditional logic (if / elif / else), matching the "Python Control Flow"
unit of the syllabus.
"""

from utils import calculate_average

# Grade boundaries kept as a list of tuples: (minimum_percentage, letter)
GRADE_SCALE = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (40, "E"),
    (0, "F"),
]


def calculate_percentage(marks):
    """Percentage here is simply the average of the three subject marks."""
    return round(calculate_average(marks), 2)


def get_letter_grade(percentage):
    """Maps a percentage to a letter grade using the GRADE_SCALE table."""
    for minimum, letter in GRADE_SCALE:
        if percentage >= minimum:
            return letter
    return "F"  # safety fallback, should not normally be reached


def is_passing(percentage, pass_mark=40):
    return percentage >= pass_mark


def build_grade_report(students):
    """
    Given the students dictionary, returns a new dictionary of computed
    results keyed by roll number:
        {"CS101": {"name": ..., "percentage": ..., "grade": ..., "status": ...}}
    """
    results = {}
    for roll_no, info in students.items():
        percentage = calculate_percentage(info["marks"])
        grade = get_letter_grade(percentage)
        status = "Pass" if is_passing(percentage) else "Fail"
        results[roll_no] = {
            "name": info["name"],
            "percentage": percentage,
            "grade": grade,
            "status": status,
        }
    return results
