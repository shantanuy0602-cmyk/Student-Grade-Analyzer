"""
student_manager.py
--------------------
FUNCTIONAL MODULE 1: Student & Data Management
Provides CRUD (Create, Read, Update, Delete) operations on the in-memory
student dictionary, which is the core data structure of the whole system:

    students = {
        "CS101": {"name": "Asha Verma", "marks": [78.0, 88.5, 91.0]},
        ...
    }

Dictionaries, lists and tuples (as required by the syllabus unit on
"Python Lists / Tuples / Dictionaries") are used throughout.
"""

from validators import (
    is_valid_roll_number,
    is_valid_name,
    get_valid_float,
    get_non_empty_string,
)


def add_student(students):
    """Adds a new student record after validating all inputs."""
    roll_no = get_non_empty_string("Enter roll number: ").upper()
    if not is_valid_roll_number(roll_no):
        print("Invalid roll number. Use letters/digits only.")
        return
    if roll_no in students:
        print(f"A student with roll number {roll_no} already exists.")
        return

    name = get_non_empty_string("Enter student name: ").title()
    if not is_valid_name(name):
        print("Invalid name. Use letters and spaces only.")
        return

    marks = []
    for subject_number in (1, 2, 3):
        mark = get_valid_float(f"Enter marks for Subject {subject_number} (0-100): ")
        marks.append(mark)

    students[roll_no] = {"name": name, "marks": marks}
    print(f"Student {name} ({roll_no}) added successfully.\n")


def view_all_students(students):
    """Displays every student record in a simple tabular layout."""
    if not students:
        print("No student records found.\n")
        return

    print(f"\n{'Roll No':<10}{'Name':<20}{'Marks':<25}")
    print("-" * 55)
    for roll_no, info in students.items():
        marks_str = ", ".join(str(m) for m in info["marks"])
        print(f"{roll_no:<10}{info['name']:<20}{marks_str:<25}")
    print()


def update_student(students):
    """Updates the marks of an existing student."""
    roll_no = get_non_empty_string("Enter roll number to update: ").upper()
    if roll_no not in students:
        print("No such student found.\n")
        return

    print(f"Updating marks for {students[roll_no]['name']}")
    marks = []
    for subject_number in (1, 2, 3):
        mark = get_valid_float(f"Enter new marks for Subject {subject_number} (0-100): ")
        marks.append(mark)
    students[roll_no]["marks"] = marks
    print("Record updated successfully.\n")


def delete_student(students):
    """Removes a student record."""
    roll_no = get_non_empty_string("Enter roll number to delete: ").upper()
    if roll_no in students:
        removed = students.pop(roll_no)
        print(f"Removed {removed['name']} ({roll_no}).\n")
    else:
        print("No such student found.\n")


def search_student(students):
    """Looks up and displays a single student's record."""
    roll_no = get_non_empty_string("Enter roll number to search: ").upper()
    if roll_no in students:
        info = students[roll_no]
        print(f"\nName : {info['name']}")
        print(f"Marks: {info['marks']}\n")
    else:
        print("No student found with that roll number.\n")
