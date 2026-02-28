import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problems.exception_task import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12, task_13, task_14,
    task_15, task_16, task_17, task_18, task_19,
    InvalidEmailError, InsufficientFundsError,
)


# --- task_0: ZeroDivisionError ---

def test_task_0_normal():
    assert task_0(10, 2) == 5.0


def test_task_0_zero_division():
    assert task_0(10, 0) == -1


# --- task_1: ValueError on int conversion ---

def test_task_1_valid():
    assert task_1("42") == 42


def test_task_1_invalid():
    assert task_1("abc") == 0


# --- task_2: IndexError ---

def test_task_2_valid():
    assert task_2([10, 20, 30], 1) == 20


def test_task_2_out_of_range():
    assert task_2([10, 20], 5) == -1


# --- task_3: KeyError ---

def test_task_3_valid():
    assert task_3({"a": 1, "b": 2}, "a") == 1


def test_task_3_missing_key():
    assert task_3({"a": 1}, "z") == 0


# --- task_4: try/except/finally ---

def test_task_4_normal(capsys):
    assert task_4(10, 2) == 5.0
    captured = capsys.readouterr()
    assert "done" in captured.out


def test_task_4_zero(capsys):
    assert task_4(10, 0) == -1
    captured = capsys.readouterr()
    assert "done" in captured.out


# --- task_5: catch multiple exception types ---

def test_task_5_valid():
    assert task_5("5") == 5


def test_task_5_type_error():
    assert task_5([1, 2]) == -1


def test_task_5_value_error():
    assert task_5("abc") == -1


# --- task_6: raise ValueError ---

def test_task_6_normal():
    assert task_6(10, 2) == 5.0


def test_task_6_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        task_6(10, 0)


# --- task_7: age validation ---

def test_task_7_valid():
    assert task_7(25) == "Valid age"


def test_task_7_negative():
    with pytest.raises(ValueError, match="Age cannot be negative"):
        task_7(-1)


def test_task_7_too_high():
    with pytest.raises(ValueError, match="Age is unrealistic"):
        task_7(200)


# --- task_8: raise from ---

def test_task_8_valid():
    assert task_8("10") == 10


def test_task_8_invalid():
    with pytest.raises(ValueError, match="Invalid input: abc"):
        task_8("abc")


def test_task_8_chained():
    with pytest.raises(ValueError) as exc_info:
        task_8("xyz")
    assert exc_info.value.__cause__ is not None


# --- task_9: custom InvalidEmailError ---

def test_task_9_valid():
    assert task_9("user@example.com") == "Valid email"


def test_task_9_missing_at():
    with pytest.raises(InvalidEmailError, match="Missing @ symbol"):
        task_9("userexample.com")


def test_task_9_missing_domain():
    with pytest.raises(InvalidEmailError, match="Missing domain"):
        task_9("user@examplecom")


# --- task_10: custom InsufficientFundsError ---

def test_task_10_valid():
    assert task_10(100.0, 50.0) == 50.0


def test_task_10_insufficient():
    with pytest.raises(InsufficientFundsError, match="Not enough funds"):
        task_10(50.0, 100.0)


def test_task_10_negative_amount():
    with pytest.raises(ValueError, match="Amount must be positive"):
        task_10(100.0, -10.0)


# --- task_11: skip missing keys ---

def test_task_11():
    data = [{"a": 1}, {"b": 2}, {"a": 3}]
    assert task_11(data, "a") == [1, 3]


def test_task_11_all_missing():
    data = [{"x": 1}, {"y": 2}]
    assert task_11(data, "a") == []


# --- task_12: convert strings to ints, skip failures ---

def test_task_12():
    assert task_12(["1", "abc", "3", "4.5"]) == [1, 3]


def test_task_12_all_valid():
    assert task_12(["10", "20"]) == [10, 20]


def test_task_12_none_valid():
    assert task_12(["abc", "xyz"]) == []


# --- task_13: FileNotFoundError ---

def test_task_13_not_found():
    assert task_13("nonexistent_file.txt") == "File not found: nonexistent_file.txt"


def test_task_13_exists(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("hello")
    assert task_13(str(f)) == "hello"


# --- task_14: try/except/else ---

def test_task_14_normal():
    assert task_14(10, 3) == "Result: 3.33"


def test_task_14_zero():
    assert task_14(10, 0) == "Cannot divide by zero"


# --- task_15: sum numeric values, skip non-numeric ---

def test_task_15():
    assert task_15([1, 2, "three", 4, None]) == 7


def test_task_15_all_numeric():
    assert task_15([1, 2, 3]) == 6


def test_task_15_none_numeric():
    assert task_15(["a", "b"]) == 0


# --- task_16: parse key:value pairs ---

def test_task_16():
    assert task_16("a:1,b:2,c:3") == {"a": 1, "b": 2, "c": 3}


def test_task_16_skip_bad_pairs():
    assert task_16("a:1,bad,c:xyz,d:4") == {"a": 1, "d": 4}


def test_task_16_empty():
    assert task_16("") == {}


# --- task_17: exception-catching decorator ---

def test_task_17_no_error():
    @task_17
    def add(a, b):
        return a + b
    assert add(1, 2) == 3


def test_task_17_with_error():
    @task_17
    def fail():
        raise RuntimeError("something broke")
    assert fail() == "Error: something broke"


# --- task_18: process math operations ---

def test_task_18():
    ops = [("+", 1, 2), ("-", 5, 3), ("*", 2, 4), ("/", 10, 3)]
    result = task_18(ops)
    assert result[0] == 3
    assert result[1] == 2
    assert result[2] == 8
    assert round(result[3], 2) == 3.33


def test_task_18_errors():
    ops = [("/", 1, 0), ("%", 1, 2)]
    result = task_18(ops)
    assert result[0] == "error: division by zero"
    assert result[1] == "error: unknown operator"


# --- task_19: nested try/except ---

def test_task_19():
    assert task_19() == "Caught both errors"
