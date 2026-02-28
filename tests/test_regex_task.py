import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problems.regex_task import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12, task_13, task_14,
    task_15, task_16, task_17, task_18, task_19,
)


# --- task_0: contains "python" case-insensitive ---

def test_task_0_found():
    assert task_0("I love Python programming") is True

def test_task_0_not_found():
    assert task_0("I love Java programming") is False

def test_task_0_case():
    assert task_0("PYTHON is great") is True


# --- task_1: extract emails ---

def test_task_1():
    text = "Contact us at info@example.com or support@test.org"
    assert task_1(text) == ["info@example.com", "support@test.org"]

def test_task_1_no_emails():
    assert task_1("no emails here") == []


# --- task_2: replace digits with # ---

def test_task_2():
    assert task_2("abc123def456") == "abc###def###"

def test_task_2_no_digits():
    assert task_2("hello") == "hello"


# --- task_3: split on whitespace ---

def test_task_3():
    assert task_3("hello  world\tfoo\nbar") == ["hello", "world", "foo", "bar"]

def test_task_3_single():
    assert task_3("word") == ["word"]


# --- task_4: extract first word ---

def test_task_4():
    assert task_4("hello world") == "hello"

def test_task_4_none():
    assert task_4("  hello") is None


# --- task_5: capitalized words ---

def test_task_5():
    assert task_5("Hello World foo Bar") == ["Hello", "World", "Bar"]

def test_task_5_none():
    assert task_5("all lowercase") == []


# --- task_6: remove non-alphanumeric ---

def test_task_6():
    assert task_6("Hello, World! 123") == "HelloWorld123"

def test_task_6_already_clean():
    assert task_6("abc123") == "abc123"


# --- task_7: phone numbers XXX-XXX-XXXX ---

def test_task_7():
    text = "Call 123-456-7890 or 987-654-3210"
    assert task_7(text) == ["123-456-7890", "987-654-3210"]

def test_task_7_no_match():
    assert task_7("no phone here") == []


# --- task_8: HTML tags and content ---

def test_task_8():
    text = "<b>bold</b> and <i>italic</i>"
    assert task_8(text) == [("b", "bold"), ("i", "italic")]

def test_task_8_no_tags():
    assert task_8("no tags") == []


# --- task_9: camelCase to snake_case ---

def test_task_9():
    assert task_9("camelCaseText") == "camel_case_text"

def test_task_9_single():
    assert task_9("hello") == "hello"

def test_task_9_multiple():
    assert task_9("getHTTPResponse") == "get_h_t_t_p_response"


# --- task_10: IPv4 validation ---

def test_task_10_valid():
    assert task_10("192.168.1.1") is True

def test_task_10_invalid():
    assert task_10("999.999.999.999.999") is False

def test_task_10_not_ip():
    assert task_10("hello") is False


# --- task_11: extract URLs ---

def test_task_11():
    text = "Visit https://example.com and http://test.org/page"
    assert task_11(text) == ["https://example.com", "http://test.org/page"]

def test_task_11_no_urls():
    assert task_11("no urls here") == []


# --- task_12: word frequency ---

def test_task_12():
    assert task_12("the cat and the dog") == {"the": 2, "cat": 1, "and": 1, "dog": 1}

def test_task_12_single():
    assert task_12("hello") == {"hello": 1}


# --- task_13: case-insensitive replace ---

def test_task_13():
    assert task_13("Hello HELLO hello", "hello", "hi") == "hi hi hi"

def test_task_13_no_match():
    assert task_13("abc", "xyz", "123") == "abc"


# --- task_14: extract quoted strings ---

def test_task_14():
    assert task_14('She said "hello" and "goodbye"') == ["hello", "goodbye"]

def test_task_14_no_quotes():
    assert task_14("no quotes here") == []


# --- task_15: password validation ---

def test_task_15_valid():
    assert task_15("Abcdefg1") is True

def test_task_15_too_short():
    assert task_15("Ab1") is False

def test_task_15_no_upper():
    assert task_15("abcdefg1") is False

def test_task_15_no_lower():
    assert task_15("ABCDEFG1") is False

def test_task_15_no_digit():
    assert task_15("Abcdefgh") is False


# --- task_16: censor long words ---

def test_task_16():
    assert task_16("I am a developer now") == "I am a **** now"

def test_task_16_short():
    assert task_16("I am ok") == "I am ok"


# --- task_17: extract hashtags ---

def test_task_17():
    assert task_17("Love #python and #coding") == ["python", "coding"]

def test_task_17_no_hashtags():
    assert task_17("no tags") == []


# --- task_18: match start indices ---

def test_task_18():
    assert task_18("an", "banana") == [1, 3]

def test_task_18_no_match():
    assert task_18("xyz", "hello") == []


# --- task_19: collapse whitespace ---

def test_task_19():
    assert task_19("  hello   world  ") == "hello world"

def test_task_19_single_spaces():
    assert task_19("already clean") == "already clean"
