import pytest
import time
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problems.advanced_task import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12, task_13, task_14,
    task_15, task_16, task_17, task_18, task_19,
)


# --- task_0: Fibonacci generator ---

def test_task_0_basic():
    assert list(task_0(7)) == [0, 1, 1, 2, 3, 5, 8]

def test_task_0_one():
    assert list(task_0(1)) == [0]

def test_task_0_zero():
    assert list(task_0(0)) == []

def test_task_0_is_generator():
    gen = task_0(3)
    assert hasattr(gen, "__next__")


# --- task_1: Flatten generator ---

def test_task_1():
    assert list(task_1([[1, 2], [3, 4], [5]])) == [1, 2, 3, 4, 5]

def test_task_1_empty():
    assert list(task_1([[], [], []])) == []

def test_task_1_mixed():
    assert list(task_1([["a"], [1, 2]])) == ["a", 1, 2]


# --- task_2: Prime generator ---

def test_task_2():
    assert list(task_2(20)) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_task_2_small():
    assert list(task_2(2)) == [2]

def test_task_2_below_two():
    assert list(task_2(1)) == []


# --- task_3: Chunking generator ---

def test_task_3():
    assert list(task_3([1, 2, 3, 4, 5], 2)) == [(1, 2), (3, 4), (5,)]

def test_task_3_exact():
    assert list(task_3([1, 2, 3, 4], 2)) == [(1, 2), (3, 4)]

def test_task_3_single():
    assert list(task_3([1, 2, 3], 1)) == [(1,), (2,), (3,)]

def test_task_3_large_chunk():
    assert list(task_3([1, 2], 5)) == [(1, 2)]


# --- task_4: Timer decorator ---

def test_task_4_returns_result(capsys):
    timer = task_4()

    @timer
    def add(a, b):
        return a + b

    result = add(1, 2)
    assert result == 3

def test_task_4_prints_timing(capsys):
    timer = task_4()

    @timer
    def slow():
        time.sleep(0.01)
        return 42

    slow()
    captured = capsys.readouterr()
    assert "Executed slow in" in captured.out
    assert "s" in captured.out


# --- task_5: Memoize decorator ---

def test_task_5_caches():
    memoize = task_5()
    call_count = 0

    @memoize
    def expensive(n):
        nonlocal call_count
        call_count += 1
        return n * 2

    assert expensive(5) == 10
    assert expensive(5) == 10
    assert call_count == 1  # only called once

def test_task_5_different_args():
    memoize = task_5()

    @memoize
    def square(n):
        return n ** 2

    assert square(3) == 9
    assert square(4) == 16


# --- task_6: Retry decorator ---

def test_task_6_succeeds():
    retry = task_6()

    @retry(max_retries=3)
    def always_works():
        return "ok"

    assert always_works() == "ok"

def test_task_6_retries_then_succeeds():
    retry = task_6()
    attempts = 0

    @retry(max_retries=3)
    def flaky():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("not yet")
        return "done"

    assert flaky() == "done"
    assert attempts == 3

def test_task_6_exhausts_retries():
    retry = task_6()

    @retry(max_retries=2)
    def always_fails():
        raise RuntimeError("fail")

    with pytest.raises(RuntimeError, match="fail"):
        always_fails()


# --- task_7: Type validation decorator ---

def test_task_7_valid():
    validate_types = task_7()

    @validate_types(int, str)
    def greet(age, name):
        return f"{name} is {age}"

    assert greet(25, "Alice") == "Alice is 25"

def test_task_7_invalid():
    validate_types = task_7()

    @validate_types(int, str)
    def greet(age, name):
        return f"{name} is {age}"

    with pytest.raises(TypeError, match="Argument 0 must be int"):
        greet("wrong", "Alice")

def test_task_7_second_arg_invalid():
    validate_types = task_7()

    @validate_types(int, str)
    def greet(age, name):
        return f"{name} is {age}"

    with pytest.raises(TypeError, match="Argument 1 must be str"):
        greet(25, 123)


# --- task_8: Timer context manager ---

def test_task_8_elapsed():
    Timer = task_8()
    with Timer() as t:
        time.sleep(0.01)
    assert t.elapsed >= 0.01

def test_task_8_fast():
    Timer = task_8()
    with Timer() as t:
        pass
    assert t.elapsed < 1.0


# --- task_9: SuppressErrors context manager ---

def test_task_9_suppresses():
    SuppressErrors = task_9()
    with SuppressErrors(ValueError) as s:
        raise ValueError("test")
    assert isinstance(s.exception, ValueError)

def test_task_9_no_error():
    SuppressErrors = task_9()
    with SuppressErrors(ValueError) as s:
        pass
    assert s.exception is None

def test_task_9_does_not_suppress_other():
    SuppressErrors = task_9()
    with pytest.raises(TypeError):
        with SuppressErrors(ValueError):
            raise TypeError("wrong type")

def test_task_9_multiple_types():
    SuppressErrors = task_9()
    with SuppressErrors(ValueError, KeyError) as s:
        raise KeyError("missing")
    assert isinstance(s.exception, KeyError)


# --- task_10: temp_attr context manager ---

def test_task_10_sets_and_restores():
    temp_attr = task_10()

    class Obj:
        x = 10

    obj = Obj()
    with temp_attr(obj, "x", 99):
        assert obj.x == 99
    assert obj.x == 10

def test_task_10_new_attr():
    temp_attr = task_10()

    class Obj:
        pass

    obj = Obj()
    with temp_attr(obj, "y", 42):
        assert obj.y == 42
    assert not hasattr(obj, "y")


# --- task_11: make_counter closure ---

def test_task_11():
    make_counter = task_11()
    counter = make_counter()
    assert counter() == 1
    assert counter() == 2
    assert counter() == 3

def test_task_11_independent():
    make_counter = task_11()
    c1 = make_counter()
    c2 = make_counter()
    c1()
    c1()
    assert c1() == 3
    assert c2() == 1


# --- task_12: compose ---

def test_task_12():
    compose = task_12()
    double = lambda x: x * 2
    inc = lambda x: x + 1
    double_then_inc = compose(inc, double)
    assert double_then_inc(3) == 7  # inc(double(3)) = inc(6) = 7

def test_task_12_strings():
    compose = task_12()
    upper = str.upper
    strip = str.strip
    clean = compose(upper, strip)
    assert clean("  hello  ") == "HELLO"


# --- task_13: once ---

def test_task_13():
    once = task_13()
    call_count = 0

    @once
    def init():
        nonlocal call_count
        call_count += 1
        return "initialized"

    assert init() == "initialized"
    assert init() == "initialized"
    assert call_count == 1

def test_task_13_with_args():
    once = task_13()

    @once
    def add(a, b):
        return a + b

    assert add(1, 2) == 3
    assert add(10, 20) == 3  # returns first call result


# --- task_14: Cartesian product ---

def test_task_14():
    result = task_14([[1, 2], ["a", "b"]])
    assert result == [(1, "a"), (1, "b"), (2, "a"), (2, "b")]

def test_task_14_three():
    result = task_14([[1], [2], [3]])
    assert result == [(1, 2, 3)]

def test_task_14_empty():
    result = task_14([[1, 2], []])
    assert result == []


# --- task_15: Group by key ---

def test_task_15():
    result = task_15([1, 2, 3, 4, 5, 6], lambda x: x % 2)
    assert result[0] == [2, 4, 6]
    assert result[1] == [1, 3, 5]

def test_task_15_strings():
    result = task_15(["apple", "banana", "avocado", "blueberry"], lambda x: x[0])
    assert result["a"] == ["apple", "avocado"]
    assert result["b"] == ["banana", "blueberry"]


# --- task_16: Partial application ---

def test_task_16():
    def power(base, exp):
        return base ** exp

    square = task_16(power, exp=2)
    assert square(3) == 9
    assert square(5) == 25

def test_task_16_positional():
    def greet(greeting, name):
        return f"{greeting}, {name}!"

    hello = task_16(greet, "Hello")
    assert hello("Alice") == "Hello, Alice!"


# --- task_17: Descriptor ---

def test_task_17_valid():
    Validated, Person = task_17()
    p = Person()
    p.name = "Alice"
    p.age = 30
    assert p.name == "Alice"
    assert p.age == 30

def test_task_17_invalid_name():
    Validated, Person = task_17()
    p = Person()
    with pytest.raises(ValueError, match="Validation failed"):
        p.name = ""

def test_task_17_invalid_age():
    Validated, Person = task_17()
    p = Person()
    with pytest.raises(ValueError, match="Validation failed"):
        p.age = -1

def test_task_17_wrong_type():
    Validated, Person = task_17()
    p = Person()
    with pytest.raises(ValueError, match="Validation failed"):
        p.name = 123


# --- task_18: auto_repr class decorator ---

def test_task_18():
    auto_repr = task_18()

    @auto_repr
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    p = Point(1, 2)
    assert repr(p) == "Point(x=1, y=2)"

def test_task_18_single_attr():
    auto_repr = task_18()

    @auto_repr
    class Name:
        def __init__(self, value):
            self.value = value

    assert repr(Name("hi")) == "Name(value='hi')"


# --- task_19: Registry with __init_subclass__ ---

def test_task_19_registers():
    Registry = task_19()

    class Alpha(Registry):
        pass

    class Beta(Registry):
        pass

    assert "Alpha" in Registry._registry
    assert "Beta" in Registry._registry
    assert Registry._registry["Alpha"] is Alpha
    assert Registry._registry["Beta"] is Beta

def test_task_19_empty_initially():
    Registry = task_19()
    # Before any subclasses, registry should be empty (or only contain
    # subclasses created after this call)
    initial_keys = set(Registry._registry.keys())

    class Gamma(Registry):
        pass

    assert "Gamma" in Registry._registry
