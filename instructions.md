# Python Skill Test

A collection of Python programming exercises organized by topic. Each task file contains stub functions with docstring instructions. Implement the function bodies to make the tests pass.

## Project Structure

```
python_skill_test/
├── problems/            # Task stubs (implement these)
│   ├── basic_task.py        # Fundamentals: variables, strings, lists, dicts, loops
│   ├── db_task.py           # SQLite: tables, CRUD, joins, indexes, aggregates
│   ├── exception_task.py    # Exceptions: try/except, raise, custom exceptions, decorators
│   ├── regex_task.py        # Regex: search, findall, sub, split, validation
│   ├── logging_task.py      # Logging: loggers, handlers, formatters, filters, levels
│   ├── api_task.py          # Data & APIs: JSON, URL parsing, pagination, validation
│   ├── object_task.py       # OOP: classes, inheritance, dunder methods, properties, composition
│   └── advanced_task.py     # Advanced: generators, decorators, context managers, descriptors, metaclasses
├── tests/               # Pytest test suites
│   ├── test_basic_task.py
│   ├── test_db_task.py
│   ├── test_exception_task.py
│   ├── test_regex_task.py
│   ├── test_logging_task.py
│   ├── test_api_task.py
│   ├── test_object_task.py
│   └── test_advanced_task.py
├── solutions/           # Reference solutions
│   ├── basic_task_solution.py
│   ├── db_task_solution.py
│   ├── exception_task_solution.py
│   ├── regex_task_solution.py
│   ├── logging_task_solution.py
│   ├── api_task_solution.py
│   ├── object_task_solution.py
│   └── advanced_task_solution.py
├── requirements.txt
└── instructions.md
```

## Setup

```bash
pip install -r requirements.txt
```

All task modules use Python standard library only (no additional packages required beyond pytest for testing).

## How to Use

1. Open a task file in `problems/` (e.g. `problems/basic_task.py`)
2. Read the docstring for each function — it describes what to implement
3. Replace `pass` with your solution
4. Run the corresponding tests to check your work

## Running Tests

Run all tests:
```bash
python -m pytest tests/ -v
```

Run tests for a specific topic:
```bash
python -m pytest tests/test_basic_task.py -v
python -m pytest tests/test_db_task.py -v
python -m pytest tests/test_exception_task.py -v
python -m pytest tests/test_regex_task.py -v
python -m pytest tests/test_logging_task.py -v
python -m pytest tests/test_api_task.py -v
python -m pytest tests/test_object_task.py -v
python -m pytest tests/test_advanced_task.py -v
```

## Task Summary

| File | Topic | Tasks | Tests |
|------|-------|-------|-------|
| `basic_task.py` | Python fundamentals | 25 | 21 |
| `db_task.py` | SQLite databases | 20 | 21 |
| `exception_task.py` | Exception handling | 20 | 47 |
| `regex_task.py` | Regular expressions | 20 | 47 |
| `logging_task.py` | Logging module | 20 | 21 |
| `api_task.py` | JSON & data processing | 20 | 30 |
| `object_task.py` | Object-oriented programming | 20 | 68 |
| `advanced_task.py` | Advanced Python | 20 | 53 |
