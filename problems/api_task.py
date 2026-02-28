import json
from typing import List, Dict, Optional, Any, Tuple
from urllib.parse import urlencode, urlparse, parse_qs


def task_0(data: dict) -> str:
    """
        Write a program that converts a Python dictionary to a JSON string
        and returns it. Use json.dumps.
    """
    pass


def task_1(json_string: str) -> dict:
    """
        Write a program that parses a JSON string and returns the resulting
        Python dictionary. Use json.loads.
    """
    pass


def task_2(data: dict) -> str:
    """
        Write a program that converts a dictionary to a pretty-printed JSON
        string with an indent of 2 spaces. Use json.dumps with indent parameter.
    """
    pass


def task_3(json_string: str) -> Any:
    """
        Write a program that safely parses a JSON string.
        If the string is invalid JSON, return None instead of raising an exception.
    """
    pass


def task_4(data: dict) -> str:
    """
        Write a program that converts a dictionary to a JSON string with keys
        sorted alphabetically. Use json.dumps with sort_keys parameter.
    """
    pass


def task_5(url: str) -> Dict[str, str]:
    """
        Write a program that parses a URL and returns a dictionary with keys:
        "scheme", "netloc", "path". Use urllib.parse.urlparse.
    """
    pass


def task_6(params: Dict[str, str]) -> str:
    """
        Write a program that encodes a dictionary of parameters into a
        URL query string. Use urllib.parse.urlencode.
        Example: {"name": "alice", "age": "30"} -> "name=alice&age=30"
    """
    pass


def task_7(url: str) -> Dict[str, List[str]]:
    """
        Write a program that extracts query parameters from a URL.
        Return a dictionary mapping parameter names to lists of values.
        Use urllib.parse.urlparse and urllib.parse.parse_qs.
    """
    pass


def task_8(base_url: str, params: Dict[str, str]) -> str:
    """
        Write a program that builds a complete URL by appending query parameters
        to a base URL. Return the full URL string.
        Example: ("https://api.example.com/users", {"page": "1"})
                 -> "https://api.example.com/users?page=1"
    """
    pass


def task_9(headers: Dict[str, str]) -> Dict[str, str]:
    """
        Write a program that takes a dictionary of HTTP headers and returns
        a new dictionary with all header names converted to lowercase.
    """
    pass


def task_10(status_code: int) -> str:
    """
        Write a program that returns the category of an HTTP status code:
        - 1xx -> "informational"
        - 2xx -> "success"
        - 3xx -> "redirection"
        - 4xx -> "client_error"
        - 5xx -> "server_error"
        - anything else -> "unknown"
    """
    pass


def task_11(response_data: dict, fields: List[str]) -> dict:
    """
        Write a program that extracts only the specified fields from a
        response dictionary. Return a new dict with only those keys.
        If a field doesn't exist in the response, skip it.
    """
    pass


def task_12(items: List[dict], page: int, per_page: int) -> Dict[str, Any]:
    """
        Write a program that paginates a list of items.
        Return a dictionary with:
        - "items": the slice of items for the given page (1-indexed)
        - "page": current page number
        - "per_page": items per page
        - "total": total number of items
        - "total_pages": total number of pages (ceiling division)
    """
    pass


def task_13(data: dict, required_fields: List[str]) -> Tuple[bool, List[str]]:
    """
        Write a program that validates that all required fields are present
        in the data dictionary. Return a tuple of (is_valid, missing_fields)
        where is_valid is True if all fields are present, and missing_fields
        is a list of field names that are missing.
    """
    pass


def task_14(records: List[dict], key: str, ascending: bool = True) -> List[dict]:
    """
        Write a program that sorts a list of dictionaries by the given key.
        Sort ascending if ascending=True, descending otherwise.
    """
    pass


def task_15(data: dict, path: str) -> Any:
    """
        Write a program that retrieves a nested value from a dictionary using
        a dot-separated path. Example: path="user.address.city" retrieves
        data["user"]["address"]["city"]. Return None if any key is missing.
    """
    pass


def task_16(entries: List[dict], key: str) -> Dict[str, List[dict]]:
    """
        Write a program that groups a list of dictionaries by a shared key value.
        Return a dictionary mapping each unique value of 'key' to the list of
        entries that have that value.
    """
    pass


def task_17(data: Any) -> Any:
    """
        Write a program that performs a deep copy of the data by serializing
        to JSON and deserializing back. Use json.dumps and json.loads.
    """
    pass


def task_18(dict1: dict, dict2: dict) -> dict:
    """
        Write a program that merges two dictionaries. If both have the same key,
        the value from dict2 takes precedence. Return the merged dictionary.
    """
    pass


def task_19(data: List[dict], key: str) -> List[Any]:
    """
        Write a program that extracts unique values for a given key across
        a list of dictionaries. Return a sorted list of unique values.
        Skip entries where the key is missing.
    """
    pass
