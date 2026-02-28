from typing import List, Optional, Any


# --- task_0 through task_3: Basic class creation ---

def task_0():
    """
        Define a class called Animal with:
        - __init__ that takes name (str) and sound (str) and stores them as attributes
        - a method speak() that returns "{name} says {sound}"
        Return the class itself (not an instance).
    """
    pass


def task_1():
    """
        Define a class called Counter with:
        - __init__ that sets an attribute count to 0
        - a method increment() that increases count by 1
        - a method decrement() that decreases count by 1
        - a method get_count() that returns the current count
        Return the class itself.
    """
    pass


def task_2():
    """
        Define a class called Rectangle with:
        - __init__ that takes width (float) and height (float)
        - a method area() that returns width * height
        - a method perimeter() that returns 2 * (width + height)
        - a __str__ method that returns "Rectangle(width={w}, height={h})"
        Return the class itself.
    """
    pass


def task_3():
    """
        Define a class called BankAccount with:
        - __init__ that takes owner (str) and optional balance (float, default 0)
        - a method deposit(amount) that adds to balance and returns new balance
        - a method withdraw(amount) that subtracts from balance and returns new balance
          If amount > balance, raise ValueError("Insufficient funds")
        - a method get_balance() that returns the current balance
        Return the class itself.
    """
    pass


# --- task_4 through task_6: Inheritance ---

def task_4():
    """
        Define a base class Shape with:
        - a method area() that raises NotImplementedError
        - a method description() that returns "I am a shape"

        Define a subclass Circle(Shape) with:
        - __init__ that takes radius (float)
        - area() that returns pi * radius ** 2 (use 3.14159)
        - description() that returns "I am a circle with radius {radius}"

        Return a tuple (Shape, Circle).
    """
    pass


def task_5():
    """
        Define a base class Vehicle with:
        - __init__ that takes make (str) and model (str)
        - a method info() that returns "{make} {model}"

        Define a subclass ElectricVehicle(Vehicle) with:
        - __init__ that takes make, model, and battery_capacity (float)
          Call the parent __init__ for make and model
        - Override info() to return "{make} {model} (Electric, {battery_capacity}kWh)"

        Return a tuple (Vehicle, ElectricVehicle).
    """
    pass


def task_6():
    """
        Define a class Employee with:
        - __init__ that takes name (str) and salary (float)
        - a method get_pay() that returns salary

        Define a class Manager(Employee) with:
        - __init__ that takes name, salary, and bonus (float)
          Call the parent __init__ for name and salary
        - Override get_pay() to return salary + bonus

        Define a class Director(Manager) with:
        - __init__ that takes name, salary, bonus, and stock_options (int)
          Call the parent __init__ for name, salary, and bonus
        - Override get_pay() to return salary + bonus + stock_options * 100

        Return a tuple (Employee, Manager, Director).
    """
    pass


# --- task_7 through task_9: Dunder / magic methods ---

def task_7():
    """
        Define a class called Vector with:
        - __init__ that takes x (float) and y (float)
        - __add__ that returns a new Vector with summed components
        - __sub__ that returns a new Vector with subtracted components
        - __eq__ that returns True if both x and y are equal
        - __repr__ that returns "Vector(x, y)"
        Return the class itself.
    """
    pass


def task_8():
    """
        Define a class called Temperature with:
        - __init__ that takes celsius (float)
        - __lt__ to compare temperatures (less than)
        - __le__ to compare temperatures (less than or equal)
        - __gt__ to compare temperatures (greater than)
        - __ge__ to compare temperatures (greater than or equal)
        - __eq__ to compare temperatures (equal)
        All comparisons are based on the celsius value.
        Return the class itself.
    """
    pass


def task_9():
    """
        Define a class called Inventory with:
        - __init__ that initializes an empty dict called items
        - __setitem__(key, value) to set items[key] = value
        - __getitem__(key) to return items[key]
        - __delitem__(key) to delete items[key]
        - __contains__(key) to check if key is in items
        - __len__ to return the number of items
        Return the class itself.
    """
    pass


# --- task_10 through task_12: Class methods, static methods, properties ---

def task_10():
    """
        Define a class called Circle with:
        - __init__ that takes radius (float)
        - a @property called diameter that returns radius * 2
        - a @diameter.setter that sets radius to value / 2
        - a @property called area that returns 3.14159 * radius ** 2
        Return the class itself.
    """
    pass


def task_11():
    """
        Define a class called User with:
        - a class attribute user_count initialized to 0
        - __init__ that takes username (str), increments User.user_count by 1,
          and stores username
        - a @classmethod called get_user_count(cls) that returns cls.user_count
        - a @staticmethod called is_valid_username(username) that returns True
          if username is at least 3 characters and alphanumeric, False otherwise
        Return the class itself.
    """
    pass


def task_12():
    """
        Define a class called Product with:
        - __init__ that takes name (str) and price (float)
        - a @property called price that returns _price
        - a @price.setter that sets _price, but raises ValueError("Price must be positive")
          if value <= 0
        - a @classmethod called from_string(cls, s) that creates a Product from a string
          in format "name-price" (e.g. "Widget-9.99")
        Return the class itself.
    """
    pass


# --- task_13 through task_14: Composition ---

def task_13():
    """
        Define a class called Engine with:
        - __init__ that takes horsepower (int)
        - a method start() that returns "Engine started"

        Define a class called Car with:
        - __init__ that takes make (str) and horsepower (int)
          Store an Engine instance as self.engine
        - a method start() that returns "Car started. {engine.start()}"
        - a method specs() that returns "{make} with {horsepower}hp engine"

        Return a tuple (Engine, Car).
    """
    pass


def task_14():
    """
        Define a class called Address with:
        - __init__ that takes street (str), city (str), and zipcode (str)
        - __str__ that returns "{street}, {city} {zipcode}"

        Define a class called Person with:
        - __init__ that takes name (str) and address (Address)
        - a method get_address() that returns str(self.address)

        Return a tuple (Address, Person).
    """
    pass


# --- task_15 through task_16: Abstract-like patterns and polymorphism ---

def task_15():
    """
        Define an abstract-style base class called Serializable with:
        - a method serialize() that raises NotImplementedError
        - a method deserialize(data) that raises NotImplementedError

        Define a class called JsonRecord(Serializable) with:
        - __init__ that takes data (dict)
        - serialize() that returns a string representation using str(self.data)
        - a @classmethod deserialize(cls, data_str) that creates a JsonRecord
          from eval(data_str) — for simplicity

        Return a tuple (Serializable, JsonRecord).
    """
    pass


def task_16():
    """
        Define a class called Dog with a method speak() that returns "Woof"
        Define a class called Cat with a method speak() that returns "Meow"
        Define a class called Duck with a method speak() that returns "Quack"

        Define a function called animal_chorus(animals) that takes a list of
        animal objects and returns a list of their speak() results.

        Return a tuple (Dog, Cat, Duck, animal_chorus).
    """
    pass


# --- task_17: Multiple inheritance / MRO ---

def task_17():
    """
        Define a class Flyable with a method fly() that returns "I can fly"
        Define a class Swimmable with a method swim() that returns "I can swim"
        Define a class FlyingFish(Flyable, Swimmable) that inherits from both.
        - FlyingFish should have an __init__ that takes name (str)
        - FlyingFish should have a method describe() that returns
          "{name}: {self.fly()} and {self.swim()}"

        Return a tuple (Flyable, Swimmable, FlyingFish).
    """
    pass


# --- task_18: __slots__ ---

def task_18():
    """
        Define a class called Point with:
        - __slots__ = ("x", "y")
        - __init__ that takes x and y
        - __eq__ that compares x and y
        - __repr__ that returns "Point(x, y)"
        Return the class itself.
    """
    pass


# --- task_19: Callable objects ---

def task_19():
    """
        Define a class called Multiplier with:
        - __init__ that takes factor (int)
        - __call__(value) that returns factor * value
        Return the class itself.
    """
    pass
