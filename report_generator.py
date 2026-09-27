"""
report_generator.py
----------------------
Builds a formatted, exportable text report combining per-student grades
and class-wide analytics. Kept separate from performance_analyzer.py so
"analysis" and "presentation/export" stay independently maintainable.
"""

from datetime import datetime

from grade_calculator import build_grade_report
from performance_analyzer import class_statistics, rank_students
from file_handler import export_report


def generate_report_text(students):
    """Builds the full report as a single string."""
    if not students:
        return "No student data available to generate a report."

    grade_report = build_grade_report(students)
    stats = class_statistics(students)
    ranking = rank_students(students)

    lines = []
    lines.append("STUDENT GRADE & PERFORMANCE ANALYZER - REPORT")
    lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 55)

    lines.append("\nPER-STUDENT RESULTS")
    lines.append(f"{'Roll No':<10}{'Name':<20}{'%':<8}{'Grade':<8}{'Status':<8}")
    for roll_no, info in grade_report.items():
        lines.append(
            f"{roll_no:<10}{info['name']:<20}{info['percentage']:<8}"
            f"{info['grade']:<8}{info['status']:<8}"
        )

    lines.append("\nCLASS SUMMARY")
    lines.append(f"Total Students : {stats['total_students']}")
    lines.append(f"Class Average  : {stats['class_average']}%")
    lines.append(f"Highest Score  : {stats['highest']}%")
    lines.append(f"Lowest Score   : {stats['lowest']}%")
    lines.append(f"Passed / Failed: {stats['passed']} / {stats['failed']}")

    lines.append("\nCLASS RANKING")
    for position, (name, percentage) in enumerate(ranking, start=1):
        lines.append(f"  {position}. {name} - {percentage}%")

    return "\n".join(lines)


def generate_and_save_report(students):
    """Generates the report text and writes it to data/performance_report.txt."""
    text = generate_report_text(students)
    print("\n" + text + "\n")
    path = export_report(text)
    if path:
        print(f"Report exported to: {path}\n")
