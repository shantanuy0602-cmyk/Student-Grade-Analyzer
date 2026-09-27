# Problem Statement

## Problem Statement

Instructors and small class coordinators frequently record student marks
in ad-hoc spreadsheets, making it slow and error-prone to compute
percentages, assign letter grades, identify struggling students, and
compare performance across the class. There is a need for a light,
dependable tool that a single instructor (or a student handling class
records) can run on their own computer, without needing a database
server or internet access, to manage marks and instantly see class-wide
performance insights.

## Scope of the Project

The project is a **single-class, single-term** grade management and
analysis tool. It covers:

- Recording and maintaining a roster of students and their marks in
  three subjects
- Computing percentages, letter grades and pass/fail status
- Producing class-level statistics (average, highest, lowest, grade
  distribution) and a full ranking
- Exporting a plain-text performance report

It does **not** cover multi-class/multi-term tracking, user
authentication, a graphical interface, or networked/multi-user access —
these are noted as future enhancements.

## Target Users

- College/school instructors managing a single course section
- Teaching assistants or class representatives compiling grade summaries
- Students learning to apply Python fundamentals (data types, control
  flow, functions, collections, file I/O) to a realistic problem, in
  line with the CSE1021 course outcomes

## High-Level Features

1. **Student & Data Management** – add, view, update, delete, and search
   student records, persisted to a CSV file
2. **Grade Calculation** – convert marks into percentages and letter
   grades (A+ through F) with pass/fail status
3. **Performance Analytics & Reporting** – class average, highest/lowest
   scores, pass/fail counts, grade distribution, full class ranking, and
   an exportable text report
