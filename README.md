# Automated Software Testing

This repository contains my coursework and practice for the **Automated Software Testing** course.

The repository is organized by week to keep class exercises, testing labs, and take-home assignments clearly separated. It is updated throughout the semester as new testing concepts and tools are introduced.

## Repository Structure

```text
st211-quizzes-6705142009/
│
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
│
└── weeks/
    ├── week_01/
    │   ├── README.md
    │   ├── in_class/
    │   │   ├── number_finder.py
    │   │   ├── string_utils.py
    │   │   └── testing_lab/
    │   └── take_home/
    │       └── roman_numerals/
    │
    ├── week_02/
    │   ├── README.md
    │   └── in_class/
    │       └── testcase_lab/
    │
    ├── week_03/
    │   └── in_class/
    │       ├── README.md
    │       ├── assertion_examples/
    │       ├── shopping_cart_lab/
    │       └── validation_lab/
    │
    └── week_04/
        ├── README.md
        └── in_class/
            ├── fixture-lab/
            └── marker-lab/
```

Each weekly folder contains the work completed during that part of the course.

* `in_class/` contains exercises and testing labs completed during class.
* `take_home/` contains take-home assignments when applicable.
* Weekly `README.md` files summarize the topics and activities covered.

The repository structure will be expanded as new coursework is added.

---

## Current Course Progress

### Week 01 — Testing Fundamentals

* Introduction to automated software testing
* Setting up pytest and writing basic test functions
* Using assertions and interpreting test results
* Testing simple Python functions
* Roman numeral conversion and testing

### Week 02 — Writing Effective Test Cases

* Arrange-Act-Assert (AAA) pattern
* Writing independent and dependent tests
* Positive, negative, and boundary-value testing
* Testing bank account operations and grade calculations

### Week 03 — Assertions and Test Organization

* Testing collections and floating-point values
* Writing positive and negative validation tests
* Testing class behavior using a shopping cart
* Organizing related tests into separate files

### Week 04 — Pytest Fixtures and Markers

* Creating reusable fixtures with `@pytest.fixture`
* Reusing the BankAccount class from Week 02
* Categorizing tests using custom pytest markers
* Running selected tests with the `-m` option
* Using `skip`, `skipif`, and `xfail`
* Understanding XFAIL and XPASS results
* Registering custom markers and enabling strict marker checking

---

## Environment Setup

A Python virtual environment is used to keep course dependencies separate from other projects.

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The virtual environment is not stored in the repository and can be recreated using `requirements.txt`.

---

## Running the Tests

All commands should be executed from the repository root.

Run the complete test suite:

```bash
python -m pytest
```

Run tests with detailed output:

```bash
python -m pytest -v
```

Run tests from a specific week:

```bash
python -m pytest weeks/week_04
```

Run tests from a specific lab:

```bash
python -m pytest weeks/week_04/in_class/fixture-lab
```

### Running Tests with Markers

The following custom markers are registered in the shared `pytest.ini`:

| Marker       | Purpose                           |
| ------------ | --------------------------------- |
| `smoke`      | Critical functionality tests      |
| `slow`       | Tests that take longer to execute |
| `regression` | Tests for previously fixed bugs   |

Run only smoke tests:

```bash
python -m pytest -m smoke
```

Run all tests except slow tests:

```bash
python -m pytest -m "not slow"
```

Run only Week 04 smoke tests:

```bash
python -m pytest weeks/week_04 -m smoke
```

The strict marker demonstration is kept outside normal test discovery because it intentionally uses an unregistered marker.

It can be executed separately:

```bash
python -m pytest weeks/week_04/in_class/marker-lab/strict_marker_demo.py
```

A collection error is expected when running this demonstration with `--strict-markers` enabled.

---

## Repository Configuration

### `requirements.txt`

Contains the Python packages required for the coursework.

### `pytest.ini`

Contains shared pytest settings, including test discovery rules, output options, and registered custom markers.

### `.gitignore`

Excludes unnecessary local files from version control, including virtual environments, Python cache files, and pytest cache files.

### Weekly README Files

Each week includes a short summary of the topics practiced, exercises completed, and key concepts learned.

---

## Technologies

Currently used:

* Python
* pytest
* Git
* GitHub

Additional tools will be added as they are introduced during the course.

---

## Repository Progress

This repository is updated throughout the semester. New exercises, assignments, tests, and testing techniques are added under their corresponding weekly folders.
