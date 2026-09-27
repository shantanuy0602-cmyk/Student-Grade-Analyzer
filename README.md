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

*(Add screenshots of the running menu, class statistics, and ranking
output here before submission.)*

## Sample Data

`data/students.csv` ships with 5 sample students so the analytics
features can be explored immediately after cloning the repository.
