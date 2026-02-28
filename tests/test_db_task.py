import sqlite3
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problems.db_task import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12, task_13, task_14,
    task_15, task_16, task_17, task_18, task_19,
)


@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")
    yield connection
    connection.close()


@pytest.fixture
def users_table(conn):
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    conn.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    conn.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
    conn.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")
    conn.commit()
    return conn


@pytest.fixture
def products_table(conn):
    conn.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL)")
    conn.execute("INSERT INTO products (name, price) VALUES ('Widget', 9.99)")
    conn.execute("INSERT INTO products (name, price) VALUES ('Gadget', 24.99)")
    conn.execute("INSERT INTO products (name, price) VALUES ('Doohickey', 4.99)")
    conn.commit()
    return conn


# --- Tests ---

def test_task_0(conn):
    task_0(conn)
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    assert cursor.fetchone() is not None, "users table should exist"
    # Verify column structure
    cursor = conn.execute("PRAGMA table_info(users)")
    columns = {row[1]: row[2] for row in cursor.fetchall()}
    assert "id" in columns
    assert "name" in columns
    assert "age" in columns


def test_task_1(conn):
    task_0(conn)
    task_1(conn, "Alice", 30)
    cursor = conn.execute("SELECT name, age FROM users")
    row = cursor.fetchone()
    assert row == ("Alice", 30)


def test_task_2(users_table):
    result = task_2(users_table)
    assert len(result) == 3
    names = {row[1] for row in result}
    assert names == {"Alice", "Bob", "Charlie"}


def test_task_3(users_table):
    result = task_3(users_table, "Bob")
    assert result is not None
    assert result[1] == "Bob"
    assert result[2] == 25


def test_task_3_not_found(users_table):
    result = task_3(users_table, "Nobody")
    assert result is None


def test_task_4(users_table):
    task_4(users_table, "Alice", 31)
    cursor = users_table.execute("SELECT age FROM users WHERE name='Alice'")
    assert cursor.fetchone()[0] == 31


def test_task_5(users_table):
    task_5(users_table, "Bob")
    cursor = users_table.execute("SELECT COUNT(*) FROM users WHERE name='Bob'")
    assert cursor.fetchone()[0] == 0


def test_task_6(users_table):
    result = task_6(users_table)
    assert result == 3


def test_task_7(users_table):
    result = task_7(users_table)
    ages = [row[2] for row in result]
    assert ages == [25, 30, 35]


def test_task_8(users_table):
    result = task_8(users_table, 30)
    assert len(result) == 2
    names = {row[1] for row in result}
    assert names == {"Alice", "Charlie"}


def test_task_9(conn):
    task_9(conn)
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
    assert cursor.fetchone() is not None
    cursor = conn.execute("PRAGMA table_info(products)")
    columns = {row[1]: row[2] for row in cursor.fetchall()}
    assert "id" in columns
    assert "name" in columns
    assert "price" in columns


def test_task_10(conn):
    task_9(conn)
    products = [("Widget", 9.99), ("Gadget", 24.99), ("Doohickey", 4.99)]
    task_10(conn, products)
    cursor = conn.execute("SELECT COUNT(*) FROM products")
    assert cursor.fetchone()[0] == 3


def test_task_11(products_table):
    result = task_11(products_table)
    expected = (9.99 + 24.99 + 4.99) / 3
    assert abs(result - expected) < 0.01


def test_task_12(products_table):
    result = task_12(products_table)
    assert result is not None
    assert result[1] == "Gadget"
    assert result[2] == 24.99


def test_task_13(users_table):
    task_13(users_table)
    cursor = users_table.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
    assert cursor.fetchone() is not None
    cursor = users_table.execute("PRAGMA table_info(orders)")
    columns = {row[1]: row[2] for row in cursor.fetchall()}
    assert "user_id" in columns
    assert "product" in columns
    assert "quantity" in columns


def test_task_14(users_table):
    task_13(users_table)
    users_table.execute("INSERT INTO orders (user_id, product, quantity) VALUES (1, 'Widget', 2)")
    users_table.execute("INSERT INTO orders (user_id, product, quantity) VALUES (2, 'Gadget', 1)")
    users_table.commit()
    result = task_14(users_table)
    assert len(result) == 2
    assert ("Alice", "Widget", 2) in result
    assert ("Bob", "Gadget", 1) in result


def test_task_15(users_table):
    task_15(users_table)
    cursor = users_table.execute("PRAGMA table_info(users)")
    columns = {row[1] for row in cursor.fetchall()}
    assert "email" in columns


def test_task_16(users_table):
    task_16(users_table)
    cursor = users_table.execute("SELECT name FROM sqlite_master WHERE type='index' AND name='idx_users_name'")
    assert cursor.fetchone() is not None


def test_task_17(users_table):
    result = task_17(users_table, ["Alice", "Charlie"])
    assert len(result) == 2
    names = {row[1] for row in result}
    assert names == {"Alice", "Charlie"}


def test_task_18(users_table):
    task_18(users_table)
    cursor = users_table.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    assert cursor.fetchone() is None


def test_task_19(users_table):
    task_9(users_table)
    result = task_19(users_table)
    assert "users" in result
    assert "products" in result
