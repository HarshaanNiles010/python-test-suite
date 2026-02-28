import pytest
from problems.basic_task import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12, task_13, task_14,
    task_15, task_16, task_17, task_18, task_19, task_20,
)


def test_task_0(capsys):
    task_0()
    captured = capsys.readouterr()
    assert len(captured.out.strip()) > 0


def test_task_1(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda *args: "test_input")
    task_1()
    captured = capsys.readouterr()
    assert "test_input" in captured.out


def test_task_2():
    assert task_2(3, 5) == 5
    assert task_2(7, 2) == 7
    assert task_2(4, 4) == 4


def test_task_3():
    assert task_3(1, 2, 3) == 3
    assert task_3(3, 2, 1) == 3
    assert task_3(2, 3, 1) == 3
    assert task_3(5, 5, 5) == 5


def test_task_4():
    assert task_4("hello", " world") == "hello world"
    assert task_4("", "abc") == "abc"


def test_task_5():
    assert task_5("age: ", 25) == "age: 25"
    assert task_5("val: ", 0) == "val: 0"


def test_task_6():
    assert task_6("num: ", 5) == "num: 5"
    assert task_6("count: ", 100) == "count: 100"


def test_task_7():
    assert task_7("10", 5) == 15
    assert task_7("0", 0) == 0


def test_task_8(capsys):
    task_8()
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert "{" in output and "}" in output


def test_task_9(capsys):
    task_9([1, 2], [10, 20])
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert "1" in output and "10" in output
    assert "2" in output and "20" in output


def test_task_10(capsys):
    task_10([1, 2, 3])
    captured = capsys.readouterr()
    output = captured.out
    assert "1" in output
    assert "2" in output
    assert "3" in output


def test_task_11():
    assert task_11([1, 5, 3]) == 5
    assert task_11([10]) == 10
    assert task_11([-1, -5, -3]) == -1


def test_task_12():
    assert task_12([1, 5, 3]) == 1
    assert task_12([10]) == 10
    assert task_12([-1, -5, -3]) == -5


def test_task_13(capsys):
    task_13([3, 5, 15, 7])
    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")
    assert "Fizz" in lines[0]
    assert "Buzz" in lines[1]
    assert "Fizz Buzz" in lines[2]


def test_task_14():
    assert task_14("Hello123World") == ["e", "l", "l", "o", "o", "r", "l", "d"]
    assert task_14("ABC") == []
    assert task_14("abc") == ["a", "b", "c"]


def test_task_15():
    assert task_15("abc1def2") == [1, 2]
    assert task_15("abc") == []
    assert task_15("123") == [1, 2, 3]


def test_task_16():
    assert task_16("  hello  ") == "hello"
    assert task_16("no_spaces") == "no_spaces"
    assert task_16("  leading") == "leading"


def test_task_17():
    assert task_17("aab") == {"a": 2, "b": 1}
    assert task_17("x") == {"x": 1}


def test_task_18():
    assert task_18("bca") == "a"
    assert task_18("z") == "z"
    assert task_18("ba") == "a"


def test_task_19():
    assert task_19("aab") == 0
    assert task_19("bba") == 0


def test_task_20(capsys):
    task_20()
    captured = capsys.readouterr()
    output = captured.out.strip()
    # Parse the printed list and verify all numbers are odd
    assert "[" in output
    numbers = [int(x.strip()) for x in output.strip("[]").split(",")]
    assert all(n % 2 == 1 for n in numbers)
