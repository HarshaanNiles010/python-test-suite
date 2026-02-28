import re
from typing import List, Optional, Dict, Tuple


def task_0(text: str) -> bool:
    """
        Write a program that returns True if the text contains the word "python"
        (case-insensitive), False otherwise. Use re.search.
    """
    pass


def task_1(text: str) -> List[str]:
    """
        Write a program that returns all email addresses found in the text.
        An email pattern is: one or more word characters, @, one or more word
        characters, a dot, one or more word characters. Use re.findall.
    """
    pass


def task_2(text: str) -> str:
    """
        Write a program that replaces all digits in the text with "#".
        Use re.sub.
    """
    pass


def task_3(text: str) -> List[str]:
    """
        Write a program that splits the text by any whitespace character
        (spaces, tabs, newlines). Use re.split.
        Return the list of non-empty tokens.
    """
    pass


def task_4(text: str) -> Optional[str]:
    """
        Write a program that extracts the first word from the text.
        A word is one or more word characters (\\w+). Use re.match.
        Return the matched word, or None if no match.
    """
    pass


def task_5(text: str) -> List[str]:
    """
        Write a program that returns all words that start with a capital letter.
        A capitalized word matches [A-Z][a-z]*. Use re.findall.
    """
    pass


def task_6(text: str) -> str:
    """
        Write a program that removes all non-alphanumeric characters from the text
        (keep letters and digits only). Use re.sub.
    """
    pass


def task_7(text: str) -> List[str]:
    """
        Write a program that returns all phone numbers in the format XXX-XXX-XXXX
        from the text. Use re.findall.
    """
    pass


def task_8(text: str) -> List[Tuple[str, str]]:
    """
        Write a program that extracts all HTML tags and their content.
        Pattern: <tagname>content</tagname>
        Return a list of tuples (tagname, content). Use re.findall with groups.
    """
    pass


def task_9(text: str) -> str:
    """
        Write a program that converts camelCase text to snake_case.
        Insert an underscore before each uppercase letter and convert to lowercase.
        Use re.sub. Example: "camelCaseText" -> "camel_case_text"
    """
    pass


def task_10(text: str) -> bool:
    """
        Write a program that validates whether the text is a valid IPv4 address.
        Each octet is 1-3 digits separated by dots (simple validation, just check
        the pattern \\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3} matches the full string).
        Use re.fullmatch. Return True or False.
    """
    pass


def task_11(text: str) -> List[str]:
    """
        Write a program that extracts all URLs from the text.
        A URL starts with http:// or https:// followed by one or more non-whitespace
        characters. Use re.findall.
    """
    pass


def task_12(text: str) -> Dict[str, int]:
    """
        Write a program that counts the occurrences of each word in the text.
        A word is one or more word characters (\\w+). Convert to lowercase before
        counting. Return a dictionary of word -> count.
    """
    pass


def task_13(text: str, old: str, new: str) -> str:
    """
        Write a program that replaces all occurrences of old with new,
        case-insensitively. Use re.sub with the re.IGNORECASE flag.
    """
    pass


def task_14(text: str) -> List[str]:
    """
        Write a program that extracts all text within double quotes.
        Return the list of quoted strings (without the quotes themselves).
        Use re.findall with a capturing group.
    """
    pass


def task_15(text: str) -> bool:
    """
        Write a program that validates a password string.
        A valid password must:
        - Be at least 8 characters long
        - Contain at least one uppercase letter
        - Contain at least one lowercase letter
        - Contain at least one digit
        Use re.search for each check. Return True if all pass, False otherwise.
    """
    pass


def task_16(text: str) -> str:
    """
        Write a program that censors all words that are 4 letters or longer
        by replacing them with "****". A word is \\b\\w{4,}\\b. Use re.sub.
    """
    pass


def task_17(text: str) -> List[str]:
    """
        Write a program that extracts all hashtags from the text.
        A hashtag starts with # followed by one or more word characters.
        Return the list of hashtags without the # symbol. Use re.findall.
    """
    pass


def task_18(pattern: str, text: str) -> List[int]:
    """
        Write a program that returns the starting indices of all matches
        of the given pattern in the text. Use re.finditer.
    """
    pass


def task_19(text: str) -> str:
    """
        Write a program that collapses multiple consecutive whitespace characters
        into a single space and strips leading/trailing whitespace.
        Use re.sub.
    """
    pass
