import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problems.object_task import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12, task_13, task_14,
    task_15, task_16, task_17, task_18, task_19,
)


# --- task_0: Animal class ---

def test_task_0_create():
    Animal = task_0()
    a = Animal("Dog", "Woof")
    assert a.name == "Dog"
    assert a.sound == "Woof"

def test_task_0_speak():
    Animal = task_0()
    a = Animal("Cat", "Meow")
    assert a.speak() == "Cat says Meow"


# --- task_1: Counter class ---

def test_task_1_initial():
    Counter = task_1()
    c = Counter()
    assert c.get_count() == 0

def test_task_1_increment():
    Counter = task_1()
    c = Counter()
    c.increment()
    c.increment()
    assert c.get_count() == 2

def test_task_1_decrement():
    Counter = task_1()
    c = Counter()
    c.increment()
    c.increment()
    c.decrement()
    assert c.get_count() == 1


# --- task_2: Rectangle class ---

def test_task_2_area():
    Rectangle = task_2()
    r = Rectangle(5, 3)
    assert r.area() == 15

def test_task_2_perimeter():
    Rectangle = task_2()
    r = Rectangle(5, 3)
    assert r.perimeter() == 16

def test_task_2_str():
    Rectangle = task_2()
    r = Rectangle(5, 3)
    assert str(r) == "Rectangle(width=5, height=3)"


# --- task_3: BankAccount class ---

def test_task_3_deposit():
    BankAccount = task_3()
    acc = BankAccount("Alice")
    assert acc.deposit(100) == 100

def test_task_3_withdraw():
    BankAccount = task_3()
    acc = BankAccount("Bob", 200)
    assert acc.withdraw(50) == 150

def test_task_3_insufficient():
    BankAccount = task_3()
    acc = BankAccount("Charlie", 50)
    with pytest.raises(ValueError, match="Insufficient funds"):
        acc.withdraw(100)

def test_task_3_balance():
    BankAccount = task_3()
    acc = BankAccount("Dave", 500)
    acc.deposit(100)
    acc.withdraw(200)
    assert acc.get_balance() == 400


# --- task_4: Shape / Circle inheritance ---

def test_task_4_shape_raises():
    Shape, Circle = task_4()
    s = Shape()
    with pytest.raises(NotImplementedError):
        s.area()

def test_task_4_shape_description():
    Shape, Circle = task_4()
    s = Shape()
    assert s.description() == "I am a shape"

def test_task_4_circle_area():
    Shape, Circle = task_4()
    c = Circle(5)
    assert abs(c.area() - 78.53975) < 0.01

def test_task_4_circle_description():
    Shape, Circle = task_4()
    c = Circle(5)
    assert c.description() == "I am a circle with radius 5"

def test_task_4_isinstance():
    Shape, Circle = task_4()
    c = Circle(3)
    assert isinstance(c, Shape)


# --- task_5: Vehicle / ElectricVehicle inheritance ---

def test_task_5_vehicle():
    Vehicle, EV = task_5()
    v = Vehicle("Toyota", "Camry")
    assert v.info() == "Toyota Camry"

def test_task_5_ev():
    Vehicle, EV = task_5()
    ev = EV("Tesla", "Model 3", 75.0)
    assert ev.info() == "Tesla Model 3 (Electric, 75.0kWh)"

def test_task_5_isinstance():
    Vehicle, EV = task_5()
    ev = EV("Tesla", "Model 3", 75.0)
    assert isinstance(ev, Vehicle)


# --- task_6: Employee / Manager / Director multi-level inheritance ---

def test_task_6_employee():
    Employee, Manager, Director = task_6()
    e = Employee("Alice", 50000)
    assert e.get_pay() == 50000

def test_task_6_manager():
    Employee, Manager, Director = task_6()
    m = Manager("Bob", 60000, 10000)
    assert m.get_pay() == 70000

def test_task_6_director():
    Employee, Manager, Director = task_6()
    d = Director("Charlie", 80000, 20000, 50)
    assert d.get_pay() == 105000

def test_task_6_isinstance():
    Employee, Manager, Director = task_6()
    d = Director("Charlie", 80000, 20000, 50)
    assert isinstance(d, Manager)
    assert isinstance(d, Employee)


# --- task_7: Vector dunder methods ---

def test_task_7_add():
    Vector = task_7()
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3 == Vector(4, 6)

def test_task_7_sub():
    Vector = task_7()
    v1 = Vector(5, 7)
    v2 = Vector(2, 3)
    v3 = v1 - v2
    assert v3 == Vector(3, 4)

def test_task_7_eq():
    Vector = task_7()
    assert Vector(1, 2) == Vector(1, 2)
    assert not (Vector(1, 2) == Vector(3, 4))

def test_task_7_repr():
    Vector = task_7()
    v = Vector(1, 2)
    assert repr(v) == "Vector(1, 2)"


# --- task_8: Temperature comparisons ---

def test_task_8_lt():
    Temperature = task_8()
    assert Temperature(20) < Temperature(30)
    assert not Temperature(30) < Temperature(20)

def test_task_8_le():
    Temperature = task_8()
    assert Temperature(20) <= Temperature(20)
    assert Temperature(20) <= Temperature(30)

def test_task_8_gt():
    Temperature = task_8()
    assert Temperature(30) > Temperature(20)

def test_task_8_ge():
    Temperature = task_8()
    assert Temperature(30) >= Temperature(30)

def test_task_8_eq():
    Temperature = task_8()
    assert Temperature(25) == Temperature(25)
    assert not Temperature(25) == Temperature(30)


# --- task_9: Inventory container dunder methods ---

def test_task_9_setget():
    Inventory = task_9()
    inv = Inventory()
    inv["apples"] = 5
    assert inv["apples"] == 5

def test_task_9_del():
    Inventory = task_9()
    inv = Inventory()
    inv["bananas"] = 3
    del inv["bananas"]
    assert "bananas" not in inv

def test_task_9_contains():
    Inventory = task_9()
    inv = Inventory()
    inv["milk"] = 2
    assert "milk" in inv
    assert "bread" not in inv

def test_task_9_len():
    Inventory = task_9()
    inv = Inventory()
    inv["a"] = 1
    inv["b"] = 2
    assert len(inv) == 2


# --- task_10: Circle with properties ---

def test_task_10_diameter():
    Circle = task_10()
    c = Circle(5)
    assert c.diameter == 10

def test_task_10_diameter_setter():
    Circle = task_10()
    c = Circle(5)
    c.diameter = 20
    assert c.radius == 10

def test_task_10_area():
    Circle = task_10()
    c = Circle(5)
    assert abs(c.area - 78.53975) < 0.01


# --- task_11: User with classmethod and staticmethod ---

def test_task_11_user_count():
    User = task_11()
    User.user_count = 0  # reset for test isolation
    User("alice")
    User("bob")
    assert User.get_user_count() == 2

def test_task_11_valid_username():
    User = task_11()
    assert User.is_valid_username("alice123") is True
    assert User.is_valid_username("ab") is False
    assert User.is_valid_username("no spaces") is False


# --- task_12: Product with property validation and classmethod factory ---

def test_task_12_price():
    Product = task_12()
    p = Product("Widget", 9.99)
    assert p.price == 9.99

def test_task_12_price_invalid():
    Product = task_12()
    with pytest.raises(ValueError, match="Price must be positive"):
        Product("Widget", -5)

def test_task_12_from_string():
    Product = task_12()
    p = Product.from_string("Gadget-24.99")
    assert p.name == "Gadget"
    assert p.price == 24.99


# --- task_13: Engine / Car composition ---

def test_task_13_engine():
    Engine, Car = task_13()
    e = Engine(200)
    assert e.start() == "Engine started"

def test_task_13_car_start():
    Engine, Car = task_13()
    c = Car("Toyota", 180)
    assert c.start() == "Car started. Engine started"

def test_task_13_car_specs():
    Engine, Car = task_13()
    c = Car("Honda", 150)
    assert c.specs() == "Honda with 150hp engine"


# --- task_14: Address / Person composition ---

def test_task_14_address_str():
    Address, Person = task_14()
    a = Address("123 Main St", "Springfield", "62704")
    assert str(a) == "123 Main St, Springfield 62704"

def test_task_14_person_address():
    Address, Person = task_14()
    a = Address("456 Oak Ave", "Shelbyville", "62705")
    p = Person("Alice", a)
    assert p.get_address() == "456 Oak Ave, Shelbyville 62705"


# --- task_15: Serializable / JsonRecord ---

def test_task_15_serializable_raises():
    Serializable, JsonRecord = task_15()
    s = Serializable()
    with pytest.raises(NotImplementedError):
        s.serialize()

def test_task_15_json_record_serialize():
    Serializable, JsonRecord = task_15()
    r = JsonRecord({"key": "value"})
    result = r.serialize()
    assert "key" in result and "value" in result

def test_task_15_json_record_deserialize():
    Serializable, JsonRecord = task_15()
    r = JsonRecord({"a": 1})
    serialized = r.serialize()
    r2 = JsonRecord.deserialize(serialized)
    assert r2.data == {"a": 1}

def test_task_15_isinstance():
    Serializable, JsonRecord = task_15()
    r = JsonRecord({"a": 1})
    assert isinstance(r, Serializable)


# --- task_16: Polymorphism / duck typing ---

def test_task_16_dog():
    Dog, Cat, Duck, animal_chorus = task_16()
    assert Dog().speak() == "Woof"

def test_task_16_cat():
    Dog, Cat, Duck, animal_chorus = task_16()
    assert Cat().speak() == "Meow"

def test_task_16_duck():
    Dog, Cat, Duck, animal_chorus = task_16()
    assert Duck().speak() == "Quack"

def test_task_16_chorus():
    Dog, Cat, Duck, animal_chorus = task_16()
    animals = [Dog(), Cat(), Duck(), Dog()]
    assert animal_chorus(animals) == ["Woof", "Meow", "Quack", "Woof"]


# --- task_17: Multiple inheritance ---

def test_task_17_fly():
    Flyable, Swimmable, FlyingFish = task_17()
    ff = FlyingFish("Nemo")
    assert ff.fly() == "I can fly"

def test_task_17_swim():
    Flyable, Swimmable, FlyingFish = task_17()
    ff = FlyingFish("Nemo")
    assert ff.swim() == "I can swim"

def test_task_17_describe():
    Flyable, Swimmable, FlyingFish = task_17()
    ff = FlyingFish("Nemo")
    assert ff.describe() == "Nemo: I can fly and I can swim"

def test_task_17_isinstance():
    Flyable, Swimmable, FlyingFish = task_17()
    ff = FlyingFish("Nemo")
    assert isinstance(ff, Flyable)
    assert isinstance(ff, Swimmable)


# --- task_18: __slots__ ---

def test_task_18_attrs():
    Point = task_18()
    p = Point(3, 4)
    assert p.x == 3
    assert p.y == 4

def test_task_18_eq():
    Point = task_18()
    assert Point(1, 2) == Point(1, 2)
    assert not Point(1, 2) == Point(3, 4)

def test_task_18_repr():
    Point = task_18()
    assert repr(Point(1, 2)) == "Point(1, 2)"

def test_task_18_no_dict():
    Point = task_18()
    p = Point(1, 2)
    assert not hasattr(p, "__dict__")


# --- task_19: Callable objects ---

def test_task_19_call():
    Multiplier = task_19()
    double = Multiplier(2)
    assert double(5) == 10
    assert double(3) == 6

def test_task_19_different_factors():
    Multiplier = task_19()
    triple = Multiplier(3)
    assert triple(4) == 12
    negate = Multiplier(-1)
    assert negate(7) == -7
