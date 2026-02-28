from typing import List, Dict, Any, Callable, Optional, Tuple, Iterator, Generator
import functools
import itertools
import time
from contextlib import contextmanager


# --- task_0 through task_3: Generators ---

def task_0(n: int) -> Generator[int, None, None]:
    """
        Write a generator that yields the first n Fibonacci numbers.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def task_1(data: List[List[Any]]) -> Generator[Any, None, None]:
    """
        Write a generator that flattens a list of lists.
    """
    for sublist in data:
        for item in sublist:
            yield item


def task_2(n: int) -> Generator[int, None, None]:
    """
        Write a generator that yields prime numbers up to n (inclusive).
    """
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num


def task_3(iterable, size: int) -> Generator[tuple, None, None]:
    """
        Write a generator that yields successive chunks of the given size.
    """
    lst = list(iterable)
    for i in range(0, len(lst), size):
        yield tuple(lst[i:i + size])


# --- task_4 through task_7: Decorators ---

def task_4() -> Callable:
    """
        Write a decorator called 'timer' that measures execution time.
    """
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"Executed {func.__name__} in {elapsed:.4f}s")
            return result
        return wrapper
    return timer


def task_5() -> Callable:
    """
        Write a decorator called 'memoize' that caches function results.
    """
    def memoize(func):
        cache = {}

        @functools.wraps(func)
        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wrapper
    return memoize


def task_6() -> Callable:
    """
        Write a decorator called 'retry' that takes max_retries.
    """
    def retry(max_retries: int):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                for _ in range(max_retries):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                raise last_exception
            return wrapper
        return decorator
    return retry


def task_7() -> Callable:
    """
        Write a decorator called 'validate_types' that checks argument types.
    """
    def validate_types(*types):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for i, (arg, expected) in enumerate(zip(args, types)):
                    if not isinstance(arg, expected):
                        raise TypeError(f"Argument {i} must be {expected.__name__}")
                return func(*args, **kwargs)
            return wrapper
        return decorator
    return validate_types


# --- task_8 through task_10: Context Managers ---

def task_8():
    """
        Write a context manager class called Timer.
    """
    class Timer:
        def __enter__(self):
            self.start = time.perf_counter()
            return self

        def __exit__(self, *args):
            self.elapsed = time.perf_counter() - self.start
            return False

    return Timer


def task_9():
    """
        Write a context manager class called SuppressErrors.
    """
    class SuppressErrors:
        def __init__(self, *exception_types):
            self.exception_types = exception_types
            self.exception = None

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None and issubclass(exc_type, self.exception_types):
                self.exception = exc_val
                return True
            return False

    return SuppressErrors


def task_10():
    """
        Write a context manager using contextlib.contextmanager called 'temp_attr'.
    """
    @contextmanager
    def temp_attr(obj, attr_name, value):
        had_attr = hasattr(obj, attr_name)
        if had_attr:
            old_value = getattr(obj, attr_name)
        setattr(obj, attr_name, value)
        try:
            yield
        finally:
            if had_attr:
                setattr(obj, attr_name, old_value)
            else:
                delattr(obj, attr_name)

    return temp_attr


# --- task_11 through task_13: Closures and Higher-Order Functions ---

def task_11() -> Callable:
    """
        Write a function called 'make_counter' that returns a closure.
    """
    def make_counter():
        count = 0

        def counter():
            nonlocal count
            count += 1
            return count
        return counter
    return make_counter


def task_12() -> Callable:
    """
        Write a function called 'compose' that takes two functions f and g
        and returns f(g(x)).
    """
    def compose(f, g):
        def composed(*args, **kwargs):
            return f(g(*args, **kwargs))
        return composed
    return compose


def task_13() -> Callable:
    """
        Write a function called 'once' that takes a function and returns
        a new function that can only be called once.
    """
    def once(func):
        result = None
        called = False

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal result, called
            if not called:
                result = func(*args, **kwargs)
                called = True
            return result
        return wrapper
    return once


# --- task_14 through task_15: itertools usage ---

def task_14(iterables: List[list]) -> List[tuple]:
    """
        Return the Cartesian product of all provided iterables.
    """
    return list(itertools.product(*iterables))


def task_15(iterable: list, key: Callable) -> Dict[Any, List]:
    """
        Group elements of iterable by the result of key function.
    """
    sorted_data = sorted(iterable, key=key)
    result = {}
    for k, group in itertools.groupby(sorted_data, key=key):
        result[k] = list(group)
    return result


# --- task_16: functools ---

def task_16(func: Callable, *args, **kwargs) -> Callable:
    """
        Return a partial application of func.
    """
    return functools.partial(func, *args, **kwargs)


# --- task_17: Descriptors ---

def task_17():
    """
        Write a descriptor class called 'Validated' and a class 'Person'.
    """
    class Validated:
        def __init__(self, validator):
            self.validator = validator

        def __set_name__(self, owner, name):
            self.name = name

        def __get__(self, instance, owner):
            if instance is None:
                return self
            return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not self.validator(value):
                raise ValueError("Validation failed")
            instance.__dict__[self.name] = value

    class Person:
        name = Validated(lambda x: isinstance(x, str) and len(x) > 0)
        age = Validated(lambda x: isinstance(x, int) and x >= 0)

    return (Validated, Person)


# --- task_18: Dataclass-like behavior ---

def task_18():
    """
        Write a function called 'auto_repr' that is a class decorator.
    """
    def auto_repr(cls):
        def __repr__(self):
            attrs = sorted(self.__dict__.items())
            args = ", ".join(f"{k}={v!r}" for k, v in attrs)
            return f"{cls.__name__}({args})"
        cls.__repr__ = __repr__
        return cls
    return auto_repr


# --- task_19: Registry with __init_subclass__ ---

def task_19():
    """
        Write a base class called 'Registry' that uses __init_subclass__.
    """
    class Registry:
        _registry = {}

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            Registry._registry[cls.__name__] = cls

    return Registry
