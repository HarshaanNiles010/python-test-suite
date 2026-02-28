import json
import math
from typing import List, Dict, Optional, Any, Tuple
from urllib.parse import urlencode, urlparse, parse_qs


def task_0(data: dict) -> str:
    """
        Write a program that converts a Python dictionary to a JSON string
        and returns it.
    """
    return json.dumps(data)


def task_1(json_string: str) -> dict:
    """
        Write a program that parses a JSON string and returns the resulting
        Python dictionary.
    """
    return json.loads(json_string)


def task_2(data: dict) -> str:
    """
        Write a program that converts a dictionary to a pretty-printed JSON
        string with an indent of 2 spaces.
    """
    return json.dumps(data, indent=2)


def task_3(json_string: str) -> Any:
    """
        Write a program that safely parses a JSON string.
        If the string is invalid JSON, return None.
    """
    try:
        return json.loads(json_string)
    except (json.JSONDecodeError, ValueError):
        return None


def task_4(data: dict) -> str:
    """
        Write a program that converts a dictionary to a JSON string with keys
        sorted alphabetically.
    """
    return json.dumps(data, sort_keys=True)


def task_5(url: str) -> Dict[str, str]:
    """
        Write a program that parses a URL and returns a dictionary with keys:
        "scheme", "netloc", "path".
    """
    parsed = urlparse(url)
    return {"scheme": parsed.scheme, "netloc": parsed.netloc, "path": parsed.path}


def task_6(params: Dict[str, str]) -> str:
    """
        Write a program that encodes a dictionary of parameters into a
        URL query string.
    """
    return urlencode(params)


def task_7(url: str) -> Dict[str, List[str]]:
    """
        Write a program that extracts query parameters from a URL.
    """
    parsed = urlparse(url)
    return parse_qs(parsed.query)


def task_8(base_url: str, params: Dict[str, str]) -> str:
    """
        Write a program that builds a complete URL by appending query parameters
        to a base URL.
    """
    return base_url + "?" + urlencode(params)


def task_9(headers: Dict[str, str]) -> Dict[str, str]:
    """
        Write a program that takes a dictionary of HTTP headers and returns
        a new dictionary with all header names converted to lowercase.
    """
    return {k.lower(): v for k, v in headers.items()}


def task_10(status_code: int) -> str:
    """
        Write a program that returns the category of an HTTP status code.
    """
    if 100 <= status_code < 200:
        return "informational"
    elif 200 <= status_code < 300:
        return "success"
    elif 300 <= status_code < 400:
        return "redirection"
    elif 400 <= status_code < 500:
        return "client_error"
    elif 500 <= status_code < 600:
        return "server_error"
    else:
        return "unknown"


def task_11(response_data: dict, fields: List[str]) -> dict:
    """
        Write a program that extracts only the specified fields from a
        response dictionary.
    """
    return {k: response_data[k] for k in fields if k in response_data}


def task_12(items: List[dict], page: int, per_page: int) -> Dict[str, Any]:
    """
        Write a program that paginates a list of items.
    """
    total = len(items)
    total_pages = math.ceil(total / per_page)
    start = (page - 1) * per_page
    end = start + per_page
    return {
        "items": items[start:end],
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
    }


def task_13(data: dict, required_fields: List[str]) -> Tuple[bool, List[str]]:
    """
        Write a program that validates that all required fields are present
        in the data dictionary.
    """
    missing = [f for f in required_fields if f not in data]
    return (len(missing) == 0, missing)


def task_14(records: List[dict], key: str, ascending: bool = True) -> List[dict]:
    """
        Write a program that sorts a list of dictionaries by the given key.
    """
    return sorted(records, key=lambda r: r[key], reverse=not ascending)


def task_15(data: dict, path: str) -> Any:
    """
        Write a program that retrieves a nested value from a dictionary using
        a dot-separated path.
    """
    current = data
    for part in path.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return None
    return current


def task_16(entries: List[dict], key: str) -> Dict[str, List[dict]]:
    """
        Write a program that groups a list of dictionaries by a shared key value.
    """
    groups = {}
    for entry in entries:
        val = entry[key]
        if val not in groups:
            groups[val] = []
        groups[val].append(entry)
    return groups


def task_17(data: Any) -> Any:
    """
        Write a program that performs a deep copy of the data by serializing
        to JSON and deserializing back.
    """
    return json.loads(json.dumps(data))


def task_18(dict1: dict, dict2: dict) -> dict:
    """
        Write a program that merges two dictionaries.
    """
    return {**dict1, **dict2}


def task_19(data: List[dict], key: str) -> List[Any]:
    """
        Write a program that extracts unique values for a given key across
        a list of dictionaries.
    """
    values = set()
    for d in data:
        if key in d:
            values.add(d[key])
    return sorted(values)
