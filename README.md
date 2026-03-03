# Python Skill Test

A test-driven Python exercise suite designed to assess and sharpen core Python skills. Each topic contains a file of stub functions with docstring instructions — your job is to implement them until all the tests pass.

## Purpose

This project serves as a structured skill assessment and practice environment for Python developers. It covers 8 core topics through 165 tasks and 342 automated tests, all using the Python standard library (no third-party packages beyond pytest).

It is useful for:

- **Self-assessment** — Gauge your Python proficiency across multiple domains
- **Interview prep** — Practice the kinds of tasks commonly seen in technical screens
- **Teaching** — Assign specific topic modules as homework or lab exercises
- **Onboarding** — Verify baseline Python skills for new team members

## Topics Covered

| Module | Topic | Tasks | Tests | What You'll Practice |
|--------|-------|-------|-------|----------------------|
| `basic_task.py` | Fundamentals | 25 | 21 | Variables, strings, lists, dicts, loops, FizzBuzz, list comprehensions, bug fixes |
| `db_task.py` | SQLite Databases | 20 | 21 | Table creation, CRUD operations, joins, indexes, aggregates, schema introspection |
| `exception_task.py` | Exception Handling | 20 | 47 | try/except/finally/else, raise, custom exceptions, chaining, decorators, nested handling |
| `regex_task.py` | Regular Expressions | 20 | 47 | search, findall, sub, split, match, fullmatch, finditer, groups, flags, validation |
| `logging_task.py` | Logging | 20 | 21 | Loggers, handlers, formatters, filters, levels, child loggers, file logging, propagation |
| `api_task.py` | JSON & Data Processing | 20 | 30 | json.dumps/loads, URL parsing, pagination, validation, sorting, grouping, nested access |
| `object_task.py` | Object-Oriented Programming | 20 | 68 | Classes, inheritance, dunder methods, properties, classmethods, composition, slots, MRO |
| `data_structure_task.py` | Data Structures & Algorithms | 20 | 87 | Stack, queue, linked list, BST, hashmap, dynamic array, heap, heapify, heap sort |

## Prerequisites

- Python 3.8+
- pip

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd python_skill_test

# Install dependencies
pip install -r requirements.txt
```

The only dependency is `pytest`. All task modules use the Python standard library exclusively.

## How It Works

1. **Open a task file** in `problems/` (e.g. `problems/basic_task.py`)
2. **Read the docstring** for each function — it describes exactly what to implement
3. **Replace `pass`** with your solution
4. **Run the tests** to verify your implementation

Each function starts as an unimplemented stub:

```python
def task_2(num_1: int, num_2: int) -> int:
    """
        Write a program which returns the larger of two integers
    """
    pass
```

Your job is to write the implementation:

```python
def task_2(num_1: int, num_2: int) -> int:
    """
        Write a program which returns the larger of two integers
    """
    return max(num_1, num_2)
```

## Running Tests

Run all tests across every module:

```bash
python -m pytest tests/ -v
```

Run tests for a single topic:

```bash
python -m pytest tests/test_basic_task.py -v
python -m pytest tests/test_db_task.py -v
python -m pytest tests/test_exception_task.py -v
python -m pytest tests/test_regex_task.py -v
python -m pytest tests/test_logging_task.py -v
python -m pytest tests/test_api_task.py -v
python -m pytest tests/test_object_task.py -v
python -m pytest tests/test_data_structure_task.py -v
```

Run a single test:

```bash
python -m pytest tests/test_basic_task.py::test_task_2 -v
```

## Project Structure

```
python_skill_test/
├── problems/              # Task stubs — implement these
│   ├── basic_task.py
│   ├── db_task.py
│   ├── exception_task.py
│   ├── regex_task.py
│   ├── logging_task.py
│   ├── api_task.py
│   ├── object_task.py
│   └── data_structure_task.py
├── tests/                 # Pytest test suites
│   ├── test_basic_task.py
│   ├── test_db_task.py
│   ├── test_exception_task.py
│   ├── test_regex_task.py
│   ├── test_logging_task.py
│   ├── test_api_task.py
│   ├── test_object_task.py
│   └── test_data_structure_task.py
├── solutions/             # Reference solutions (don't peek!)
│   ├── basic_task_solution.py
│   ├── db_task_solution.py
│   ├── exception_task_solution.py
│   ├── regex_task_solution.py
│   ├── logging_task_solution.py
│   ├── api_task_solution.py
│   ├── object_task_solution.py
│   └── data_structure_task_solution.py
├── requirements.txt
├── instructions.md
└── README.md
```

## Solutions

Reference solutions are provided in the `solutions/` directory. Try to solve the tasks on your own first — the tests will tell you exactly what's expected. Use the solutions only to check your approach or if you're stuck.
