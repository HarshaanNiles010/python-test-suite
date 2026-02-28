import pytest
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problems.api_task import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12, task_13, task_14,
    task_15, task_16, task_17, task_18, task_19,
)


# --- task_0: dict to JSON string ---

def test_task_0():
    result = task_0({"a": 1})
    assert json.loads(result) == {"a": 1}

def test_task_0_empty():
    result = task_0({})
    assert json.loads(result) == {}


# --- task_1: JSON string to dict ---

def test_task_1():
    assert task_1('{"a": 1}') == {"a": 1}

def test_task_1_nested():
    assert task_1('{"a": {"b": 2}}') == {"a": {"b": 2}}


# --- task_2: pretty-printed JSON ---

def test_task_2():
    result = task_2({"a": 1})
    assert "  " in result  # indented
    assert json.loads(result) == {"a": 1}


# --- task_3: safe JSON parse ---

def test_task_3_valid():
    assert task_3('{"a": 1}') == {"a": 1}

def test_task_3_invalid():
    assert task_3("not json{") is None


# --- task_4: sorted keys JSON ---

def test_task_4():
    result = task_4({"b": 2, "a": 1})
    keys = list(json.loads(result).keys())
    assert keys == ["a", "b"]


# --- task_5: parse URL ---

def test_task_5():
    result = task_5("https://example.com/path")
    assert result["scheme"] == "https"
    assert result["netloc"] == "example.com"
    assert result["path"] == "/path"


# --- task_6: urlencode ---

def test_task_6():
    result = task_6({"name": "alice", "age": "30"})
    assert "name=alice" in result
    assert "age=30" in result


# --- task_7: parse query params ---

def test_task_7():
    result = task_7("https://example.com?name=alice&age=30")
    assert result["name"] == ["alice"]
    assert result["age"] == ["30"]


# --- task_8: build URL with params ---

def test_task_8():
    result = task_8("https://api.example.com/users", {"page": "1"})
    assert result.startswith("https://api.example.com/users?")
    assert "page=1" in result


# --- task_9: lowercase header names ---

def test_task_9():
    result = task_9({"Content-Type": "application/json", "X-Api-Key": "abc"})
    assert result["content-type"] == "application/json"
    assert result["x-api-key"] == "abc"


# --- task_10: HTTP status categories ---

def test_task_10():
    assert task_10(200) == "success"
    assert task_10(301) == "redirection"
    assert task_10(404) == "client_error"
    assert task_10(500) == "server_error"
    assert task_10(100) == "informational"
    assert task_10(600) == "unknown"


# --- task_11: extract fields ---

def test_task_11():
    data = {"id": 1, "name": "alice", "email": "a@b.com", "age": 30}
    result = task_11(data, ["name", "email"])
    assert result == {"name": "alice", "email": "a@b.com"}

def test_task_11_missing_field():
    data = {"id": 1, "name": "alice"}
    result = task_11(data, ["name", "phone"])
    assert result == {"name": "alice"}


# --- task_12: pagination ---

def test_task_12():
    items = [{"id": i} for i in range(10)]
    result = task_12(items, page=2, per_page=3)
    assert result["items"] == [{"id": 3}, {"id": 4}, {"id": 5}]
    assert result["page"] == 2
    assert result["per_page"] == 3
    assert result["total"] == 10
    assert result["total_pages"] == 4

def test_task_12_last_page():
    items = [{"id": i} for i in range(5)]
    result = task_12(items, page=2, per_page=3)
    assert result["items"] == [{"id": 3}, {"id": 4}]
    assert result["total_pages"] == 2


# --- task_13: validate required fields ---

def test_task_13_valid():
    is_valid, missing = task_13({"name": "a", "age": 1}, ["name", "age"])
    assert is_valid is True
    assert missing == []

def test_task_13_missing():
    is_valid, missing = task_13({"name": "a"}, ["name", "age", "email"])
    assert is_valid is False
    assert sorted(missing) == ["age", "email"]


# --- task_14: sort records ---

def test_task_14_ascending():
    records = [{"name": "c"}, {"name": "a"}, {"name": "b"}]
    result = task_14(records, "name")
    assert [r["name"] for r in result] == ["a", "b", "c"]

def test_task_14_descending():
    records = [{"val": 1}, {"val": 3}, {"val": 2}]
    result = task_14(records, "val", ascending=False)
    assert [r["val"] for r in result] == [3, 2, 1]


# --- task_15: nested value by dot path ---

def test_task_15():
    data = {"user": {"address": {"city": "NYC"}}}
    assert task_15(data, "user.address.city") == "NYC"

def test_task_15_missing():
    data = {"user": {"name": "alice"}}
    assert task_15(data, "user.address.city") is None

def test_task_15_top_level():
    data = {"name": "alice"}
    assert task_15(data, "name") == "alice"


# --- task_16: group by key ---

def test_task_16():
    entries = [
        {"type": "a", "val": 1},
        {"type": "b", "val": 2},
        {"type": "a", "val": 3},
    ]
    result = task_16(entries, "type")
    assert len(result["a"]) == 2
    assert len(result["b"]) == 1


# --- task_17: deep copy via JSON ---

def test_task_17():
    original = {"a": [1, 2, 3], "b": {"c": 4}}
    copy = task_17(original)
    assert copy == original
    copy["a"].append(4)
    assert len(original["a"]) == 3  # original unchanged


# --- task_18: merge dicts ---

def test_task_18():
    result = task_18({"a": 1, "b": 2}, {"b": 3, "c": 4})
    assert result == {"a": 1, "b": 3, "c": 4}

def test_task_18_no_overlap():
    result = task_18({"a": 1}, {"b": 2})
    assert result == {"a": 1, "b": 2}


# --- task_19: unique values for key ---

def test_task_19():
    data = [{"color": "red"}, {"color": "blue"}, {"color": "red"}, {"color": "green"}]
    assert task_19(data, "color") == ["blue", "green", "red"]

def test_task_19_missing_keys():
    data = [{"color": "red"}, {"size": "large"}, {"color": "blue"}]
    assert task_19(data, "color") == ["blue", "red"]
