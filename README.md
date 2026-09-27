# Student Grade & Performance Analyzer

A console-based Python application built for **CSE1021 – Introduction to
Problem Solving and Programming**, applying core concepts from the
syllabus: data types, control flow, functions, lists/tuples/dictionaries,
searching, sorting, and basic file handling.

## Overview

Teachers often manage student marks in scattered spreadsheets with no
easy way to see class-wide trends. This project reads a small class's
subject marks, calculates percentages and letter grades, ranks students,
and produces a class performance summary — all through a simple,
menu-driven command-line interface.

## Features

- **Add / View / Update / Delete / Search** student records (CRUD)
- Automatic **percentage and letter-grade calculation** (A+ to F)
- **Pass/Fail** classification against a configurable pass mark
- **Class statistics**: average, highest, lowest, pass/fail count, grade
  distribution
- **Ranking** of students from highest to lowest performer (hand-written
  bubble sort, no built-in `sort()` used)
- **Export** a full text report to a file
- Data is **persisted to CSV** between runs
- Input validation and error handling throughout

## Technologies / Tools Used

- Python 3 (standard library only — `csv`, `os`, `datetime`, `unittest`)
- CSV file storage (no external database required)

## Project Structure

```
StudentGradeAnalyzer/
├── main.py                   # Menu-driven entry point
├── student_manager.py        # Module 1: Student & data management (CRUD)
├── grade_calculator.py       # Module 2: Percentage & letter-grade logic
├── performance_analyzer.py   # Module 3: Class statistics & ranking
├── report_generator.py       # Builds and exports the full text report
├── file_handler.py           # CSV load/save + report export
├── validators.py             # Input validation helpers
├── utils.py                  # Core algorithms (average, min/max, sort, count)
├── data/
│   └── students.csv          # Sample dataset (5 students)
├── tests/
│   └── test_analyzer.py      # Unit tests (unittest)
└── diagrams/                 # Architecture / workflow / UML diagrams
```

## Steps to Install & Run

1. Make sure Python 3.8+ is installed.
2. Clone or download this repository.
3. From the project root, run:
   ```bash
   python main.py
   ```
4. Follow the on-screen menu to add students, view grades, and generate
   reports. Data is automatically saved to `data/students.csv` on exit
   (menu option `0`).

No external packages are required — the project only uses Python's
standard library, so there is nothing to `pip install`.

## Instructions for Testing

Run the unit test suite from the project root:

```bash
python -m unittest discover tests -v
```

All tests should report `OK`. The tests cover the averaging, min/max,
counting and sorting algorithms in `utils.py`, and the grade/percentage
logic in `grade_calculator.py`.

## Screenshots
1.Main menu
<img width="1919" height="1004" alt="Screenshot 2026-09-27 230845" src="https://github.com/user-attachments/assets/81011a9c-9684-4bd1-a8db-8892fde54e77" />



 1. Add Student
 <img width="1915" height="522" alt="Screenshot 2026-09-27 231155" src="https://github.com/user-attachments/assets/390ec526-e1f0-4ef6-9c7e-6777741a9323" />

 2. View All Students
<img width="1902" height="630" alt="Screenshot 2026-09-27 231253" src="https://github.com/user-attachments/assets/1662ba4b-e4b6-4a06-bea0-7b45cb05acf6" />


 3. Update Student Marks
<img width="1919" height="572" alt="Screenshot 2026-09-27 231512" src="https://github.com/user-attachments/assets/db279c3b-567e-42cc-99dc-44f187e1b698" />

 4. Delete Student
<img width="1919" height="500" alt="Screenshot 2026-09-27 231538" src="https://github.com/user-attachments/assets/80e987be-7e5c-4891-8e63-96c0a0056609" />


 5. Search Student
<img width="1919" height="675" alt="Screenshot 2026-09-27 231618" src="https://github.com/user-attachments/assets/710aee94-204f-4ac4-a8ff-bfbd11069a58" />

 6. View Grade Report (per student)
<img width="1919" height="721" alt="Screenshot 2026-09-27 231637" src="https://github.com/user-attachments/assets/2114a0ca-6ba2-4605-ae98-00d8f251ea98" />


 7. View Class Statistics
<img width="1919" height="719" alt="Screenshot 2026-09-27 231706" src="https://github.com/user-attachments/assets/56b918f6-c039-4c94-b887-f43afea825ec" />

 8. View Class Ranking
<img width="1914" height="728" alt="Screenshot 2026-09-27 231720" src="https://github.com/user-attachments/assets/b0c19b85-e17e-46f6-83c1-cd875e3ddbf1" />

 9. Export Full Report to File
<img width="1919" height="669" alt="Screenshot 2026-09-27 231741" src="https://github.com/user-attachments/assets/c208a8e8-20d4-4f81-941b-8768f0428ade" />

 10. Save & Exit
<img width="1919" height="963" alt="Screenshot 2026-09-27 231756" src="https://github.com/user-attachments/assets/d417fdab-30a2-439c-b779-084e599b3ec2" />

## Sample Data

`data/students.csv` ships with 5 sample students so the analytics
features can be explored immediately after cloning the repository.
