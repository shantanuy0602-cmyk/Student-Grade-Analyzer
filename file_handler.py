"""
file_handler.py
----------------
Handles reading and writing student records to a CSV file so that data
persists between program runs. Kept separate from student_manager.py so
storage logic can change (e.g. to JSON or a database) without touching
the rest of the application - a maintainability / modularity requirement.
"""

import csv
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "students.csv")

FIELDNAMES = ["roll_no", "name", "subject1", "subject2", "subject3"]


def load_students():
    """
    Loads student records from the CSV file into a dictionary keyed by
    roll number, e.g.:
        {"CS101": {"name": "Asha", "marks": [78, 88, 91]}, ...}
    Returns an empty dictionary if the file does not exist yet.
    """
    students = {}
    if not os.path.exists(DATA_FILE):
        return students

    try:
        with open(DATA_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                marks = [
                    float(row["subject1"]),
                    float(row["subject2"]),
                    float(row["subject3"]),
                ]
                students[row["roll_no"]] = {"name": row["name"], "marks": marks}
    except (OSError, ValueError, KeyError) as error:
        print(f"Warning: could not fully read data file ({error}). "
              f"Starting with whatever records were successfully loaded.")
    return students


def save_students(students):
    """Writes the full students dictionary back to the CSV file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    try:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            for roll_no, info in students.items():
                writer.writerow({
                    "roll_no": roll_no,
                    "name": info["name"],
                    "subject1": info["marks"][0],
                    "subject2": info["marks"][1],
                    "subject3": info["marks"][2],
                })
        return True
    except OSError as error:
        print(f"Error saving data: {error}")
        return False


def export_report(text, filename="performance_report.txt"):
    """Writes a plain-text analytics report to disk."""
    path = os.path.join(os.path.dirname(__file__), "data", filename)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return path
    except OSError as error:
        print(f"Error exporting report: {error}")
        return None
