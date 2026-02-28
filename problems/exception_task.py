from typing import List, Dict, Optional, Any


def task_0(a: int, b: int) -> float:
    """
        Write a program that divides a by b and returns the result.
        If b is zero, catch the ZeroDivisionError and return -1.
    """
    pass


def task_1(value: str) -> int:
    """
        Write a program that converts the value to an integer and returns it.
        If the conversion fails, catch the ValueError and return 0.
    """
    pass


def task_2(lst: List[int], index: int) -> int:
    """
        Write a program that returns the element at the given index from lst.
        If the index is out of range, catch the IndexError and return -1.
    """
    pass


def task_3(d: Dict[str, int], key: str) -> int:
    """
        Write a program that returns the value for the given key from the dict.
        If the key does not exist, catch the KeyError and return 0.
    """
    pass


def task_4(a: int, b: int) -> float:
    """
        Write a program that divides a by b and returns the result.
        Use a try/except/finally block. In the finally block, print "done".
        If b is zero, catch ZeroDivisionError and return -1.
    """
    pass


def task_5(value: Any) -> int:
    """
        Write a program that attempts to call int(value).
        Catch TypeError and ValueError using a single except clause
        handling both exception types. Return -1 if either occurs.
    """
    pass


def task_6(a: int, b: int) -> float:
    """
        Write a program that divides a by b.
        If b is zero, raise a ValueError with the message "Cannot divide by zero".
    """
    pass


def task_7(age: int) -> str:
    """
        Write a program that validates an age value.
        If age is negative, raise a ValueError with message "Age cannot be negative".
        If age > 150, raise a ValueError with message "Age is unrealistic".
        Otherwise return "Valid age".
    """
    pass


def task_8(value: str) -> int:
    """
        Write a program that converts value to an integer.
        If it fails, catch the ValueError and re-raise it with the message
        "Invalid input: {value}" using 'raise ValueError(...) from e'.
    """
    pass


class InvalidEmailError(Exception):
    """Custom exception for invalid email addresses."""
    pass


def task_9(email: str) -> str:
    """
        Write a program that validates an email address.
        If the email does not contain "@", raise an InvalidEmailError
        with the message "Missing @ symbol".
        If the email does not contain "." after the "@", raise an InvalidEmailError
        with the message "Missing domain".
        Otherwise return "Valid email".
    """
    pass


class InsufficientFundsError(Exception):
    """Custom exception for insufficient bank funds."""
    pass


def task_10(balance: float, amount: float) -> float:
    """
        Write a program that withdraws amount from balance.
        If amount > balance, raise an InsufficientFundsError with the message
        "Not enough funds".
        If amount < 0, raise a ValueError with the message "Amount must be positive".
        Otherwise return the new balance.
    """
    pass


def task_11(data: List[Dict[str, Any]], key: str) -> List[Any]:
    """
        Write a program that extracts the value for 'key' from each dict in data.
        If a dict is missing the key, skip it (catch KeyError and continue).
        Return the list of extracted values.
    """
    pass


def task_12(numbers: List[str]) -> List[int]:
    """
        Write a program that converts a list of strings to integers.
        Skip any strings that cannot be converted (catch ValueError and continue).
        Return the list of successfully converted integers.
    """
    pass


def task_13(filename: str) -> str:
    """
        Write a program that attempts to open and read the given filename.
        If the file does not exist, catch FileNotFoundError and return
        "File not found: {filename}".
    """
    pass


def task_14(a: int, b: int) -> str:
    """
        Write a program that divides a by b using try/except/else.
        In the else block (no exception), return "Result: {result}" where result
        is the division rounded to 2 decimal places.
        If ZeroDivisionError occurs, return "Cannot divide by zero".
    """
    pass


def task_15(values: List[Any]) -> int:
    """
        Write a program that sums all values in the list.
        Use try/except to catch TypeError for non-numeric values and skip them.
        Return the total sum of all numeric values.
    """
    pass


def task_16(text: str) -> Dict[str, int]:
    """
        Write a program that parses "key:value" pairs from a comma-separated string.
        Example input: "a:1,b:2,c:3"
        If a pair does not contain ":", skip it (catch ValueError from unpacking).
        If the value cannot be converted to int, skip it.
        Return a dict of the successfully parsed pairs.
    """
    pass


def task_17(func):
    """
        Write a decorator that wraps any function call in a try/except.
        If the wrapped function raises any exception, return the string
        "Error: {exception message}" instead of propagating the exception.
        Otherwise return the function's normal return value.
    """
    pass


def task_18(operations: List[tuple]) -> List[Any]:
    """
        Write a program that processes a list of math operations.
        Each tuple is (operator, a, b) where operator is "+", "-", "*", or "/".
        For each operation, compute the result and append it to the results list.
        If division by zero occurs, append "error: division by zero" instead.
        If the operator is unknown, append "error: unknown operator".
        Return the list of results.
    """
    pass


def task_19() -> str:
    """
        Write a program that demonstrates nested try/except blocks.
        In the outer try block, convert the string "abc" to an int.
        In the outer except (catching ValueError), enter an inner try block
        that divides 1 by 0.
        In the inner except (catching ZeroDivisionError), return
        "Caught both errors".
    """
    pass
