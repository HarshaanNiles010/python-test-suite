import sqlite3
from typing import List, Optional


def task_0(conn) -> None:
    """
        Create a table called `users` with columns:
        - id INTEGER PRIMARY KEY
        - name TEXT
        - age INTEGER
    """
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    conn.commit()


def task_1(conn, name: str, age: int) -> None:
    """
        Insert a single row into the `users` table with the given name and age.
    """
    conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()


def task_2(conn) -> List[tuple]:
    """
        Select and return all rows from the `users` table.
    """
    cursor = conn.execute("SELECT * FROM users")
    return cursor.fetchall()


def task_3(conn, name: str) -> Optional[tuple]:
    """
        Select and return a single user by name.
        Return None if the user does not exist.
    """
    cursor = conn.execute("SELECT * FROM users WHERE name = ?", (name,))
    return cursor.fetchone()


def task_4(conn, name: str, new_age: int) -> None:
    """
        Update a user's age by name.
    """
    conn.execute("UPDATE users SET age = ? WHERE name = ?", (new_age, name))
    conn.commit()


def task_5(conn, name: str) -> None:
    """
        Delete a user by name.
    """
    conn.execute("DELETE FROM users WHERE name = ?", (name,))
    conn.commit()


def task_6(conn) -> int:
    """
        Return the count of rows in the `users` table.
    """
    cursor = conn.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]


def task_7(conn) -> List[tuple]:
    """
        Select all users ordered by age ascending.
    """
    cursor = conn.execute("SELECT * FROM users ORDER BY age ASC")
    return cursor.fetchall()


def task_8(conn, min_age: int) -> List[tuple]:
    """
        Select all users where age >= min_age.
    """
    cursor = conn.execute("SELECT * FROM users WHERE age >= ?", (min_age,))
    return cursor.fetchall()


def task_9(conn) -> None:
    """
        Create a `products` table with columns:
        - id INTEGER PRIMARY KEY
        - name TEXT NOT NULL
        - price REAL
    """
    conn.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL)")
    conn.commit()


def task_10(conn, products: List[tuple]) -> None:
    """
        Insert multiple products using executemany.
        Each tuple in products is (name, price).
    """
    conn.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
    conn.commit()


def task_11(conn) -> float:
    """
        Return the average price from the `products` table.
    """
    cursor = conn.execute("SELECT AVG(price) FROM products")
    return cursor.fetchone()[0]


def task_12(conn) -> Optional[tuple]:
    """
        Return the most expensive product (entire row).
    """
    cursor = conn.execute("SELECT * FROM products ORDER BY price DESC LIMIT 1")
    return cursor.fetchone()


def task_13(conn) -> None:
    """
        Create an `orders` table with columns:
        - id INTEGER PRIMARY KEY
        - user_id INTEGER (foreign key referencing users(id))
        - product TEXT
        - quantity INTEGER
    """
    conn.execute(
        "CREATE TABLE orders ("
        "id INTEGER PRIMARY KEY, "
        "user_id INTEGER, "
        "product TEXT, "
        "quantity INTEGER, "
        "FOREIGN KEY (user_id) REFERENCES users(id))"
    )
    conn.commit()


def task_14(conn) -> List[tuple]:
    """
        Join `users` and `orders` tables.
        Return a list of (user name, product, quantity) for all orders.
    """
    cursor = conn.execute(
        "SELECT users.name, orders.product, orders.quantity "
        "FROM orders JOIN users ON orders.user_id = users.id"
    )
    return cursor.fetchall()


def task_15(conn) -> None:
    """
        Add a column `email TEXT` to the `users` table using ALTER TABLE.
    """
    conn.execute("ALTER TABLE users ADD COLUMN email TEXT")
    conn.commit()


def task_16(conn) -> None:
    """
        Create an index called `idx_users_name` on users(name).
    """
    conn.execute("CREATE INDEX idx_users_name ON users(name)")
    conn.commit()


def task_17(conn, names: List[str]) -> List[tuple]:
    """
        Select users whose name is IN the provided list.
        Use a parameterized query.
    """
    placeholders = ",".join("?" for _ in names)
    cursor = conn.execute(f"SELECT * FROM users WHERE name IN ({placeholders})", names)
    return cursor.fetchall()


def task_18(conn) -> None:
    """
        Drop the `users` table.
    """
    conn.execute("DROP TABLE users")
    conn.commit()


def task_19(conn) -> List[str]:
    """
        Return a list of all table names in the database.
    """
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return [row[0] for row in cursor.fetchall()]
