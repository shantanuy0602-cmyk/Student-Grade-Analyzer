"""
main.py
--------
Entry point for the Student Grade & Performance Analyzer.
Presents a simple, menu-driven console interface (usability requirement)
that ties together the three functional modules:

    1) Student & Data Management  -> student_manager.py
    2) Grade Calculation          -> grade_calculator.py
    3) Performance Analytics      -> performance_analyzer.py / report_generator.py

Run with:  python main.py
"""

from student_manager import (
    add_student,
    view_all_students,
    update_student,
    delete_student,
    search_student,
)
from grade_calculator import build_grade_report
from performance_analyzer import display_class_statistics, display_ranking
from report_generator import generate_and_save_report
from file_handler import load_students, save_students

MENU = """
========== STUDENT GRADE & PERFORMANCE ANALYZER ==========
 1. Add Student
 2. View All Students
 3. Update Student Marks
 4. Delete Student
 5. Search Student
 6. View Grade Report (per student)
 7. View Class Statistics
 8. View Class Ranking
 9. Export Full Report to File
 0. Save & Exit
============================================================
"""


def display_grade_report(students):
    """Prints the computed grade / percentage / status for every student."""
    report = build_grade_report(students)
    if not report:
        print("No student records found.\n")
        return
    print(f"\n{'Roll No':<10}{'Name':<20}{'%':<8}{'Grade':<8}{'Status':<8}")
    print("-" * 55)
    for roll_no, info in report.items():
        print(f"{roll_no:<10}{info['name']:<20}{info['percentage']:<8}"
              f"{info['grade']:<8}{info['status']:<8}")
    print()


def main():
    students = load_students()
    print("Welcome! Loaded", len(students), "existing student record(s).")

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            search_student(students)
        elif choice == "6":
            display_grade_report(students)
        elif choice == "7":
            display_class_statistics(students)
        elif choice == "8":
            display_ranking(students)
        elif choice == "9":
            generate_and_save_report(students)
        elif choice == "0":
            if save_students(students):
                print("Data saved. Goodbye!")
            else:
                print("Warning: data may not have been saved.")
            break
        else:
            print("Invalid choice. Please select a valid menu option.\n")


if __name__ == "__main__":
    main()
