from typing import List, Optional, Any


def task_0():
    """
        Define a class called Animal with:
        - __init__ that takes name (str) and sound (str) and stores them as attributes
        - a method speak() that returns "{name} says {sound}"
        Return the class itself (not an instance).
    """
    class Animal:
        def __init__(self, name: str, sound: str):
            self.name = name
            self.sound = sound

        def speak(self):
            return f"{self.name} says {self.sound}"

    return Animal


def task_1():
    """
        Define a class called Counter with:
        - __init__ that sets an attribute count to 0
        - a method increment() that increases count by 1
        - a method decrement() that decreases count by 1
        - a method get_count() that returns the current count
        Return the class itself.
    """
    class Counter:
        def __init__(self):
            self.count = 0

        def increment(self):
            self.count += 1

        def decrement(self):
            self.count -= 1

        def get_count(self):
            return self.count

    return Counter


def task_2():
    """
        Define a class called Rectangle with:
        - __init__ that takes width (float) and height (float)
        - a method area() that returns width * height
        - a method perimeter() that returns 2 * (width + height)
        - a __str__ method that returns "Rectangle(width={w}, height={h})"
        Return the class itself.
    """
    class Rectangle:
        def __init__(self, width: float, height: float):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

        def __str__(self):
            return f"Rectangle(width={self.width}, height={self.height})"

    return Rectangle


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
    class BankAccount:
        def __init__(self, owner: str, balance: float = 0):
            self.owner = owner
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount
            return self.balance

        def withdraw(self, amount):
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount
            return self.balance

        def get_balance(self):
            return self.balance

    return BankAccount


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
    class Shape:
        def area(self):
            raise NotImplementedError

        def description(self):
            return "I am a shape"

    class Circle(Shape):
        def __init__(self, radius: float):
            self.radius = radius

        def area(self):
            return 3.14159 * self.radius ** 2

        def description(self):
            return f"I am a circle with radius {self.radius}"

    return (Shape, Circle)


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
    class Vehicle:
        def __init__(self, make: str, model: str):
            self.make = make
            self.model = model

        def info(self):
            return f"{self.make} {self.model}"

    class ElectricVehicle(Vehicle):
        def __init__(self, make: str, model: str, battery_capacity: float):
            super().__init__(make, model)
            self.battery_capacity = battery_capacity

        def info(self):
            return f"{self.make} {self.model} (Electric, {self.battery_capacity}kWh)"

    return (Vehicle, ElectricVehicle)


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
    class Employee:
        def __init__(self, name: str, salary: float):
            self.name = name
            self.salary = salary

        def get_pay(self):
            return self.salary

    class Manager(Employee):
        def __init__(self, name: str, salary: float, bonus: float):
            super().__init__(name, salary)
            self.bonus = bonus

        def get_pay(self):
            return self.salary + self.bonus

    class Director(Manager):
        def __init__(self, name: str, salary: float, bonus: float, stock_options: int):
            super().__init__(name, salary, bonus)
            self.stock_options = stock_options

        def get_pay(self):
            return self.salary + self.bonus + self.stock_options * 100

    return (Employee, Manager, Director)


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
    class Vector:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Vector(self.x - other.x, self.y - other.y)

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __repr__(self):
            return f"Vector({self.x}, {self.y})"

    return Vector


def task_8():
    """
        Define a class called Temperature with:
        - __init__ that takes celsius (float)
        - __lt__, __le__, __gt__, __ge__, __eq__
        All comparisons are based on the celsius value.
        Return the class itself.
    """
    class Temperature:
        def __init__(self, celsius: float):
            self.celsius = celsius

        def __lt__(self, other):
            return self.celsius < other.celsius

        def __le__(self, other):
            return self.celsius <= other.celsius

        def __gt__(self, other):
            return self.celsius > other.celsius

        def __ge__(self, other):
            return self.celsius >= other.celsius

        def __eq__(self, other):
            return self.celsius == other.celsius

    return Temperature


def task_9():
    """
        Define a class called Inventory with:
        - __init__ that initializes an empty dict called items
        - __setitem__, __getitem__, __delitem__, __contains__, __len__
        Return the class itself.
    """
    class Inventory:
        def __init__(self):
            self.items = {}

        def __setitem__(self, key, value):
            self.items[key] = value

        def __getitem__(self, key):
            return self.items[key]

        def __delitem__(self, key):
            del self.items[key]

        def __contains__(self, key):
            return key in self.items

        def __len__(self):
            return len(self.items)

    return Inventory


def task_10():
    """
        Define a class called Circle with:
        - __init__ that takes radius (float)
        - a @property called diameter that returns radius * 2
        - a @diameter.setter that sets radius to value / 2
        - a @property called area that returns 3.14159 * radius ** 2
        Return the class itself.
    """
    class Circle:
        def __init__(self, radius: float):
            self.radius = radius

        @property
        def diameter(self):
            return self.radius * 2

        @diameter.setter
        def diameter(self, value):
            self.radius = value / 2

        @property
        def area(self):
            return 3.14159 * self.radius ** 2

    return Circle


def task_11():
    """
        Define a class called User with:
        - a class attribute user_count initialized to 0
        - __init__ that takes username (str), increments User.user_count by 1
        - a @classmethod called get_user_count(cls) that returns cls.user_count
        - a @staticmethod called is_valid_username(username) that returns True
          if username is at least 3 characters and alphanumeric
        Return the class itself.
    """
    class User:
        user_count = 0

        def __init__(self, username: str):
            self.username = username
            User.user_count += 1

        @classmethod
        def get_user_count(cls):
            return cls.user_count

        @staticmethod
        def is_valid_username(username):
            return len(username) >= 3 and username.isalnum()

    return User


def task_12():
    """
        Define a class called Product with:
        - __init__ that takes name (str) and price (float)
        - a @property called price that returns _price
        - a @price.setter that raises ValueError if value <= 0
        - a @classmethod called from_string(cls, s) that parses "name-price"
        Return the class itself.
    """
    class Product:
        def __init__(self, name: str, price: float):
            self.name = name
            self.price = price

        @property
        def price(self):
            return self._price

        @price.setter
        def price(self, value):
            if value <= 0:
                raise ValueError("Price must be positive")
            self._price = value

        @classmethod
        def from_string(cls, s: str):
            name, price_str = s.rsplit("-", 1)
            return cls(name, float(price_str))

    return Product


def task_13():
    """
        Define Engine and Car classes using composition.
        Return a tuple (Engine, Car).
    """
    class Engine:
        def __init__(self, horsepower: int):
            self.horsepower = horsepower

        def start(self):
            return "Engine started"

    class Car:
        def __init__(self, make: str, horsepower: int):
            self.make = make
            self.engine = Engine(horsepower)

        def start(self):
            return f"Car started. {self.engine.start()}"

        def specs(self):
            return f"{self.make} with {self.engine.horsepower}hp engine"

    return (Engine, Car)


def task_14():
    """
        Define Address and Person classes using composition.
        Return a tuple (Address, Person).
    """
    class Address:
        def __init__(self, street: str, city: str, zipcode: str):
            self.street = street
            self.city = city
            self.zipcode = zipcode

        def __str__(self):
            return f"{self.street}, {self.city} {self.zipcode}"

    class Person:
        def __init__(self, name: str, address):
            self.name = name
            self.address = address

        def get_address(self):
            return str(self.address)

    return (Address, Person)


def task_15():
    """
        Define Serializable and JsonRecord classes.
        Return a tuple (Serializable, JsonRecord).
    """
    class Serializable:
        def serialize(self):
            raise NotImplementedError

        def deserialize(self, data):
            raise NotImplementedError

    class JsonRecord(Serializable):
        def __init__(self, data: dict):
            self.data = data

        def serialize(self):
            return str(self.data)

        @classmethod
        def deserialize(cls, data_str):
            return cls(eval(data_str))

    return (Serializable, JsonRecord)


def task_16():
    """
        Define Dog, Cat, Duck classes and animal_chorus function.
        Return a tuple (Dog, Cat, Duck, animal_chorus).
    """
    class Dog:
        def speak(self):
            return "Woof"

    class Cat:
        def speak(self):
            return "Meow"

    class Duck:
        def speak(self):
            return "Quack"

    def animal_chorus(animals):
        return [a.speak() for a in animals]

    return (Dog, Cat, Duck, animal_chorus)


def task_17():
    """
        Define Flyable, Swimmable, and FlyingFish (multiple inheritance).
        Return a tuple (Flyable, Swimmable, FlyingFish).
    """
    class Flyable:
        def fly(self):
            return "I can fly"

    class Swimmable:
        def swim(self):
            return "I can swim"

    class FlyingFish(Flyable, Swimmable):
        def __init__(self, name: str):
            self.name = name

        def describe(self):
            return f"{self.name}: {self.fly()} and {self.swim()}"

    return (Flyable, Swimmable, FlyingFish)


def task_18():
    """
        Define a class called Point with __slots__.
        Return the class itself.
    """
    class Point:
        __slots__ = ("x", "y")

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __repr__(self):
            return f"Point({self.x}, {self.y})"

    return Point


def task_19():
    """
        Define a class called Multiplier with __call__.
        Return the class itself.
    """
    class Multiplier:
        def __init__(self, factor: int):
            self.factor = factor

        def __call__(self, value):
            return self.factor * value

    return Multiplier
