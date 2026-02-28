import re
from typing import List, Optional, Dict, Tuple


def task_0(text: str) -> bool:
    """
        Write a program that returns True if the text contains the word "python"
        (case-insensitive), False otherwise. Use re.search.
    """
    return bool(re.search(r"python", text, re.IGNORECASE))


def task_1(text: str) -> List[str]:
    """
        Write a program that returns all email addresses found in the text.
    """
    return re.findall(r"\w+@\w+\.\w+", text)


def task_2(text: str) -> str:
    """
        Write a program that replaces all digits in the text with "#".
    """
    return re.sub(r"\d", "#", text)


def task_3(text: str) -> List[str]:
    """
        Write a program that splits the text by any whitespace character.
        Return the list of non-empty tokens.
    """
    return [t for t in re.split(r"\s+", text) if t]


def task_4(text: str) -> Optional[str]:
    """
        Write a program that extracts the first word from the text.
    """
    match = re.match(r"\w+", text)
    return match.group() if match else None


def task_5(text: str) -> List[str]:
    """
        Write a program that returns all words that start with a capital letter.
    """
    return re.findall(r"[A-Z][a-z]*", text)


def task_6(text: str) -> str:
    """
        Write a program that removes all non-alphanumeric characters from the text.
    """
    return re.sub(r"[^a-zA-Z0-9]", "", text)


def task_7(text: str) -> List[str]:
    """
        Write a program that returns all phone numbers in the format XXX-XXX-XXXX.
    """
    return re.findall(r"\d{3}-\d{3}-\d{4}", text)


def task_8(text: str) -> List[Tuple[str, str]]:
    """
        Write a program that extracts all HTML tags and their content.
    """
    return re.findall(r"<(\w+)>(.*?)</\1>", text)


def task_9(text: str) -> str:
    """
        Write a program that converts camelCase text to snake_case.
    """
    return re.sub(r"([A-Z])", r"_\1", text).lower()


def task_10(text: str) -> bool:
    """
        Write a program that validates whether the text is a valid IPv4 address.
    """
    return bool(re.fullmatch(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", text))


def task_11(text: str) -> List[str]:
    """
        Write a program that extracts all URLs from the text.
    """
    return re.findall(r"https?://\S+", text)


def task_12(text: str) -> Dict[str, int]:
    """
        Write a program that counts the occurrences of each word in the text.
    """
    words = re.findall(r"\w+", text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def task_13(text: str, old: str, new: str) -> str:
    """
        Write a program that replaces all occurrences of old with new,
        case-insensitively.
    """
    return re.sub(re.escape(old), new, text, flags=re.IGNORECASE)


def task_14(text: str) -> List[str]:
    """
        Write a program that extracts all text within double quotes.
    """
    return re.findall(r'"([^"]*)"', text)


def task_15(text: str) -> bool:
    """
        Write a program that validates a password string.
    """
    if len(text) < 8:
        return False
    if not re.search(r"[A-Z]", text):
        return False
    if not re.search(r"[a-z]", text):
        return False
    if not re.search(r"\d", text):
        return False
    return True


def task_16(text: str) -> str:
    """
        Write a program that censors all words that are 4 letters or longer.
    """
    return re.sub(r"\b\w{4,}\b", "****", text)


def task_17(text: str) -> List[str]:
    """
        Write a program that extracts all hashtags from the text.
    """
    return re.findall(r"#(\w+)", text)


def task_18(pattern: str, text: str) -> List[int]:
    """
        Write a program that returns the starting indices of all matches.
    """
    return [m.start() for m in re.finditer(pattern, text)]


def task_19(text: str) -> str:
    """
        Write a program that collapses multiple consecutive whitespace characters
        into a single space and strips leading/trailing whitespace.
    """
    return re.sub(r"\s+", " ", text).strip()
