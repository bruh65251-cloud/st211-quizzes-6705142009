# Automated Software Testing

This repository contains my coursework and practice for the **Automated Software Testing** course.

The repository is organized by week to keep class activities, testing labs, and take-home assignments clearly separated. It will continue to grow as new testing concepts and tools are introduced throughout the course.

---

## Repository Structure

```text
Automated_Software_Testing_Course/
│
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
│
└── weeks/
    │
    ├── week_01/
    │   ├── README.md
    │   │
    │   ├── in_class/
    │   │   ├── string_utils.py
    │   │   ├── number_finder.py
    │   │   │
    │   │   └── testing_lab/
    │   │       └── test_basic_assertions.py
    │   │
    │   └── take_home/
    │       └── roman_numerals/
    │           ├── roman.py
    │           └── test_roman.py
    │
    └── week_02/
        ├── README.md
        │
        └── in_class/
            └── test_case_lab/
                ├── bank_account.py
                ├── grades.py
                ├── test_bank_account.py
                ├── test_grades.py
                ├── test_shared_state.py
                └── test_independent_state.py
```

Each weekly folder contains the work completed during that part of the course.

- `in_class/` contains exercises and labs completed during class.
- `take_home/` contains take-home assignments.
- `README.md` summarizes the main topics and activities for that week.

The structure will be expanded when new coursework is added.

---

## Current Course Progress

### Week 01 — Testing Fundamentals

Topics practiced:

- Introduction to automated software testing
- Setting up pytest
- Writing basic test functions
- Using assertions
- Interpreting passed and failed tests
- Testing simple Python functions
- Basic test organization

The take-home assignment for this week included testing a Roman numeral converter.

### Week 02 — Writing Effective Test Cases

Topics practiced:

- Writing clearer test cases
- Arrange-Act-Assert (AAA)
- Independent and dependent tests
- Testing different input conditions
- Organizing related tests
- Testing simple program behavior with pytest

More weeks will be added as the course progresses.

---

## Environment Setup

A Python virtual environment is recommended so that the packages used for this course are kept separate from other Python projects.

### Create the environment

```bash
python -m venv .venv
```

### Activate the environment

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### Install the required packages

```bash
pip install -r requirements.txt
```

The virtual environment itself is not stored in the repository. It can be recreated using `requirements.txt`.

---

## Running the Tests

Run all available tests from the root directory:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

A specific test file can also be executed:

```bash
pytest path/to/test_file.py
```

---

## Repository Files

### `requirements.txt`

Contains the Python packages required for the coursework.

### `pytest.ini`

Contains pytest configuration used across the repository.

### `.gitignore`

Prevents unnecessary local files from being committed, including:

- `.venv/`
- `venv/`
- `__pycache__/`
- `.pytest_cache/`
- generated cache files

### Weekly `README.md` Files

Each week contains a short README describing:

- topics covered
- class activities
- take-home work
- important testing concepts practiced

---

## Technologies

Currently used:

- Python
- pytest
- Git
- GitHub

Additional testing tools will be added when they are introduced during the course.

---

## Repository Progress

This repository is updated throughout the semester. New exercises, assignments, tests, and testing techniques will be added under their corresponding weekly folders.