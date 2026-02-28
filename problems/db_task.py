import sqlite3
from typing import List, Optional


def task_0(conn) -> None:
    """
        Create a table called `users` with columns:
        - id INTEGER PRIMARY KEY
        - name TEXT
        - age INTEGER
    """
    pass


def task_1(conn, name: str, age: int) -> None:
    """
        Insert a single row into the `users` table with the given name and age.
    """
    pass


def task_2(conn) -> List[tuple]:
    """
        Select and return all rows from the `users` table.
    """
    pass


def task_3(conn, name: str) -> Optional[tuple]:
    """
        Select and return a single user by name.
        Return None if the user does not exist.
    """
    pass


def task_4(conn, name: str, new_age: int) -> None:
    """
        Update a user's age by name.
    """
    pass


def task_5(conn, name: str) -> None:
    """
        Delete a user by name.
    """
    pass


def task_6(conn) -> int:
    """
        Return the count of rows in the `users` table.
    """
    pass


def task_7(conn) -> List[tuple]:
    """
        Select all users ordered by age ascending.
    """
    pass


def task_8(conn, min_age: int) -> List[tuple]:
    """
        Select all users where age >= min_age.
    """
    pass


def task_9(conn) -> None:
    """
        Create a `products` table with columns:
        - id INTEGER PRIMARY KEY
        - name TEXT NOT NULL
        - price REAL
    """
    pass


def task_10(conn, products: List[tuple]) -> None:
    """
        Insert multiple products using executemany.
        Each tuple in products is (name, price).
    """
    pass


def task_11(conn) -> float:
    """
        Return the average price from the `products` table.
    """
    pass


def task_12(conn) -> Optional[tuple]:
    """
        Return the most expensive product (entire row).
    """
    pass


def task_13(conn) -> None:
    """
        Create an `orders` table with columns:
        - id INTEGER PRIMARY KEY
        - user_id INTEGER (foreign key referencing users(id))
        - product TEXT
        - quantity INTEGER
    """
    pass


def task_14(conn) -> List[tuple]:
    """
        Join `users` and `orders` tables.
        Return a list of (user name, product, quantity) for all orders.
    """
    pass


def task_15(conn) -> None:
    """
        Add a column `email TEXT` to the `users` table using ALTER TABLE.
    """
    pass


def task_16(conn) -> None:
    """
        Create an index called `idx_users_name` on users(name).
    """
    pass


def task_17(conn, names: List[str]) -> List[tuple]:
    """
        Select users whose name is IN the provided list.
        Use a parameterized query.
    """
    pass


def task_18(conn) -> None:
    """
        Drop the `users` table.
    """
    pass


def task_19(conn) -> List[str]:
    """
        Return a list of all table names in the database.
    """
    pass
