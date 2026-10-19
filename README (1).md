# Student Learning Portal

## Overview

The Student Learning Portal is a simple console-based Python application developed for the PROG211 Object-Oriented Programming 1 assignment.

The system demonstrates how Object-Oriented Programming (OOP) can be used to solve a simple education-related problem. It allows student learning records to be created, searched, displayed, updated, and counted.

## Project Domain

**Education**

## Main Features

- Register a student learning record
- Store basic student information
- Record a course name
- Generate a unique learning record ID
- Search for a learning record by ID
- Update learning status
- Display all learning records
- Display the total number of records created

## Learning Status

The system supports:

- Not Started
- In Progress
- Completed

## OOP Concepts Used

- Classes
- Objects
- Attributes
- Instance methods
- Class method
- Static method
- Object interaction

## Classes

### Student
Stores student information:
- `student_id`
- `name`
- `programme`
- `email`

### LearningRecord
Stores learning record information:
- `record_id`
- `student`
- `course_name`
- `learning_status`

### LearningPortal
Manages all learning records.

## Python Data Structure

The project uses one dictionary:

```python
self.learning_records = {}
```

Each record ID is used as the key and a `LearningRecord` object is stored as the value.

## Object Interaction

A `Student` object is created and passed into a `LearningRecord` object. The `LearningPortal` object then stores and manages the learning record.

## Method Types

### Instance Method

```python
def update_status(self, new_status):
    self.learning_status = new_status
```

### Class Method

```python
@classmethod
def get_total_records(cls):
    return cls.total_records
```

### Static Method

```python
@staticmethod
def validate_status(status):
```

## Digital Public Goods Alignment

### Open Source
The source code can be published on GitHub so it can be viewed, studied, and improved.

### Inclusive and Accessible Design
The system uses a simple numbered console menu with clear text prompts.

### Privacy-Respecting Design
The program stores only basic information needed to demonstrate student learning record management and does not connect to external systems.

### Modular and Reusable Design
Responsibilities are separated into `Student`, `LearningRecord`, and `LearningPortal` classes.

## SDG Alignment

The project supports **SDG 4: Quality Education** by demonstrating a simple digital method of organizing learning progress information.

## Requirements

- Python 3
- No external libraries required

## How to Run

```bash
python main.py
```

or on some systems:

```bash
python3 main.py
```

## Example

```text
Record ID: LRN001
Student: Denisha
Course: Information Technology
Learning Status: In Progress
```

## Repository Structure

```text
student-learning-portal/
├── main.py
├── README.md
└── screenshots/
```

## Course

**PROG211 - Object-Oriented Programming 1**

Limkokwing University of Creative Technology - Sierra Leone
