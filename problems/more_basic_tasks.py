from typing import List, Tuple, Set, Dict, Optional, Any


# ── LIST TASKS (task_0 – task_12) ────────────────────────────────────────────

def task_0(input_list: List[int], element: int) -> List[int]:
    """
        Append element to input_list and return the resulting list.
    """
    pass


def task_1(input_list: List[int]) -> List[int]:
    """
        Remove duplicate values from input_list while preserving the original order,
        then return the deduplicated list.
    """
    pass


def task_2(nums: List[int]) -> int:
    """
        Return the second largest distinct value in nums.
        You may assume the list has at least two distinct values.
    """
    pass


def task_3(nested: List[List[int]]) -> List[int]:
    """
        Flatten a one-level nested list and return the flat list.
        e.g. [[1, 2], [3, 4]] -> [1, 2, 3, 4]
    """
    pass


def task_4(input_list: List[int]) -> List[int]:
    """
        Return a new list containing only the elements at even indices (0, 2, 4, …).
    """
    pass


def task_5(input_list: List[int], k: int) -> List[int]:
    """
        Rotate input_list to the left by k positions and return the result.
        e.g. [1, 2, 3, 4, 5] rotated left by 2 -> [3, 4, 5, 1, 2]
    """
    pass


def task_6(list_a: List[int], list_b: List[int]) -> List[int]:
    """
        Return a sorted list of elements that appear in both list_a and list_b
        (i.e. the intersection), without duplicates.
    """
    pass


def task_7(input_list: List[int]) -> List[int]:
    """
        Return the list reversed without using the built-in reverse() method
        or slicing with a negative step.
    """
    pass


def task_8(input_list: List[Any], element: Any) -> int:
    """
        Count and return the number of times element appears in input_list.
    """
    pass


def task_9(nums: List[int]) -> List[int]:
    """
        Return a new list where each element is the square of the corresponding
        element in nums.
    """
    pass


def task_10(input_list: List[Any], value: Any) -> List[Any]:
    """
        Remove all occurrences of value from input_list and return the result.
    """
    pass


def task_11(input_list: List[int], n: int) -> List[List[int]]:
    """
        Split input_list into consecutive chunks of size n and return a list of those chunks.
        The last chunk may be smaller than n if the list does not divide evenly.
        e.g. [1,2,3,4,5], n=2 -> [[1,2],[3,4],[5]]
    """
    pass


def task_12(nums: List[int]) -> List[int]:
    """
        Return the running (cumulative) sum of nums.
        e.g. [1, 2, 3, 4] -> [1, 3, 6, 10]
    """
    pass


# ── SET TASKS (task_13 – task_24) ────────────────────────────────────────────

def task_13(set_a: Set[int], set_b: Set[int]) -> Set[int]:
    """
        Return the union of set_a and set_b.
    """
    pass


def task_14(set_a: Set[int], set_b: Set[int]) -> Set[int]:
    """
        Return the intersection of set_a and set_b.
    """
    pass


def task_15(set_a: Set[int], set_b: Set[int]) -> Set[int]:
    """
        Return the difference set_a - set_b (elements in set_a but not in set_b).
    """
    pass


def task_16(set_a: Set[int], set_b: Set[int]) -> Set[int]:
    """
        Return the symmetric difference of set_a and set_b
        (elements in either set but not both).
    """
    pass


def task_17(set_a: Set[int], set_b: Set[int]) -> bool:
    """
        Return True if set_a is a subset of set_b, otherwise False.
    """
    pass


def task_18(input_list: List[int]) -> List[int]:
    """
        Remove duplicates from input_list using a set, then return the values
        in sorted ascending order.
    """
    pass


def task_19(set_a: Set[int], set_b: Set[int]) -> bool:
    """
        Return True if set_a and set_b are disjoint (share no elements), otherwise False.
    """
    pass


def task_20(input_set: Set[int]) -> List[Set[int]]:
    """
        Return the power set of input_set as a list of sets (including the empty set
        and the set itself). Order of the subsets in the list does not matter.
    """
    pass


def task_21(base_set: Set[int], elements: List[int]) -> Set[int]:
    """
        Add all elements from the list to base_set and return the updated set.
    """
    pass


def task_22(input_str: str) -> int:
    """
        Return the number of unique characters in input_str using a set.
    """
    pass


def task_23(input_list: List[int]) -> List[int]:
    """
        Return a sorted list of elements that appear more than once in input_list.
    """
    pass


def task_24(input_set: Set[int]) -> int:
    """
        Return the largest element in input_set.
        You may not use the built-in max() function.
    """
    pass


# ── TUPLE TASKS (task_25 – task_36) ──────────────────────────────────────────

def task_25(nums: List[int]) -> Tuple[int, int]:
    """
        Return a tuple of (min_value, max_value) of the given list.
    """
    pass


def task_26(t: Tuple[int, int, int]) -> int:
    """
        Unpack the three-element tuple t and return the sum of its elements.
    """
    pass


def task_27(a: int, b: int) -> Tuple[int, int]:
    """
        Swap the values of a and b using tuple unpacking and return them as (b, a).
    """
    pass


def task_28(input_list: List[int]) -> Tuple:
    """
        Convert input_list to a tuple and return it.
    """
    pass


def task_29(t: Tuple, value: Any) -> int:
    """
        Return the index of the first occurrence of value in tuple t.
        Return -1 if value is not found.
    """
    pass


def task_30(t1: Tuple, t2: Tuple) -> Tuple:
    """
        Concatenate t1 and t2 and return the resulting tuple.
    """
    pass


def task_31(n: int) -> Tuple[int, ...]:
    """
        Return a tuple containing the squares of integers from 1 to n inclusive.
        e.g. n=4 -> (1, 4, 9, 16)
    """
    pass


def task_32(t: Tuple, index: int, val: Any) -> Tuple:
    """
        Return a new tuple identical to t except the element at position index
        is replaced by val. Tuples are immutable, so construct a new one.
    """
    pass


def task_33(t: Tuple, value: Any) -> int:
    """
        Return the number of times value appears in tuple t.
    """
    pass


def task_34(list_a: List, list_b: List) -> List[Tuple]:
    """
        Zip list_a and list_b together and return a list of tuples.
        e.g. [1,2], ['a','b'] -> [(1,'a'), (2,'b')]
    """
    pass


def task_35(t: Tuple[int, ...]) -> Tuple[int, ...]:
    """
        Return a new tuple that is t sorted in ascending order.
    """
    pass


def task_36(pairs: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
        Sort a list of (name, score) tuples by score in descending order and return it.
    """
    pass


# ── DICT TASKS (task_37 – task_49) ───────────────────────────────────────────

def task_37(dict_a: Dict, dict_b: Dict) -> Dict:
    """
        Merge dict_a and dict_b into a single dict and return it.
        If a key exists in both, the value from dict_b should take precedence.
    """
    pass


def task_38(input_dict: Dict) -> Dict:
    """
        Return a new dict where keys and values from input_dict are swapped.
        You may assume all values are unique and hashable.
    """
    pass


def task_39(input_dict: Dict[str, int]) -> Dict[str, int]:
    """
        Return a new dict sorted by values in ascending order.
    """
    pass


def task_40(words: List[str]) -> Dict[str, int]:
    """
        Count the frequency of each word in the list and return a dict
        mapping word -> count.
    """
    pass


def task_41(input_dict: Dict[str, int], threshold: int) -> List[str]:
    """
        Return a sorted list of keys from input_dict whose value is strictly
        greater than threshold.
    """
    pass


def task_42(input_dict: Dict, key: str) -> Dict:
    """
        Remove key from input_dict if it exists (do nothing if it doesn't) and
        return the modified dict.
    """
    pass


def task_43(nested_dict: Dict, keys: List[str]) -> Any:
    """
        Retrieve a value from a nested dict by traversing the list of keys in order.
        Return None if any key in the path does not exist.
        e.g. {"a": {"b": 1}}, ["a", "b"] -> 1
    """
    pass


def task_44(input_dict: Dict[str, Any], prefix: str) -> Dict[str, Any]:
    """
        Return a new dict containing only items from input_dict whose key
        starts with prefix.
    """
    pass


def task_45(records: List[Dict], group_key: str) -> Dict[str, List[Dict]]:
    """
        Group a list of dicts by the value of group_key and return a dict mapping
        each group value to the list of records that share it.
        e.g. [{"type":"a","v":1},{"type":"b","v":2},{"type":"a","v":3}], "type"
             -> {"a": [{"type":"a","v":1},{"type":"a","v":3}], "b": [...]}
    """
    pass


def task_46(input_dict: Dict[str, int]) -> str:
    """
        Return the key associated with the maximum value in input_dict.
    """
    pass


def task_47(input_dict: Dict[str, int]) -> Dict[str, int]:
    """
        Return a new dict where every value from input_dict is doubled.
    """
    pass


def task_48(n: int) -> Dict[int, int]:
    """
        Using a dict comprehension, return a dict mapping each integer i in
        range 1..n (inclusive) to i squared.
        e.g. n=3 -> {1:1, 2:4, 3:9}
    """
    pass


def task_49(dict_a: Dict, dict_b: Dict) -> bool:
    """
        Return True if dict_a and dict_b have exactly the same set of keys,
        otherwise False.
    """
    pass


# ── IF-ELSE TASKS (task_50 – task_61) ────────────────────────────────────────

def task_50(n: int) -> str:
    """
        Return "positive" if n > 0, "negative" if n < 0, or "zero" if n == 0.
    """
    pass


def task_51(score: int) -> str:
    """
        Return a letter grade based on score:
          90-100 -> "A"
          80-89  -> "B"
          70-79  -> "C"
          60-69  -> "D"
          below 60 -> "F"
    """
    pass


def task_52(year: int) -> bool:
    """
        Return True if year is a leap year, otherwise False.
        A leap year is divisible by 4, except for century years which must be divisible by 400.
    """
    pass


def task_53(n: int) -> int:
    """
        Return the absolute value of n without using the built-in abs() function.
    """
    pass


def task_54(n: int) -> str:
    """
        Return "even" if n is even, or "odd" if n is odd.
    """
    pass


def task_55(n: int) -> int:
    """
        Return the sign of n: 1 if n > 0, -1 if n < 0, 0 if n == 0.
    """
    pass


def task_56(bmi: float) -> str:
    """
        Return the BMI category based on the given bmi value:
          bmi < 18.5            -> "Underweight"
          18.5 <= bmi < 25.0   -> "Normal"
          25.0 <= bmi < 30.0   -> "Overweight"
          bmi >= 30.0           -> "Obese"
    """
    pass


def task_57(a: int, b: int, c: int) -> str:
    """
        Given three side lengths of a triangle, return:
          "equilateral" if all three sides are equal
          "isosceles"   if exactly two sides are equal
          "scalene"     if all sides are different
    """
    pass


def task_58(n: int) -> str:
    """
        For a single integer n, return:
          "fizzbuzz" if divisible by both 3 and 5
          "fizz"     if divisible by 3 only
          "buzz"     if divisible by 5 only
          str(n)     otherwise
    """
    pass


def task_59(a: int, b: int, c: int) -> int:
    """
        Return the maximum of three integers without using the built-in max() function.
    """
    pass


def task_60(n: int, lo: int, hi: int) -> bool:
    """
        Return True if lo <= n <= hi, otherwise False.
    """
    pass


def task_61(month: int) -> str:
    """
        Return the season for a given month number (1-12) in the Northern Hemisphere:
          December, January, February   -> "Winter"
          March, April, May             -> "Spring"
          June, July, August            -> "Summer"
          September, October, November  -> "Autumn"
    """
    pass


# ── FOR LOOP TASKS (task_62 – task_73) ───────────────────────────────────────

def task_62(nums: List[int]) -> int:
    """
        Using a for loop, return the sum of all numbers in nums.
        Do not use the built-in sum() function.
    """
    pass


def task_63(n: int) -> int:
    """
        Using a for loop, return the factorial of n.
        You may assume n >= 0. factorial(0) == 1.
    """
    pass


def task_64(n: int) -> List[int]:
    """
        Return a list of the first n Fibonacci numbers (starting from 0).
        e.g. n=6 -> [0, 1, 1, 2, 3, 5]
    """
    pass


def task_65(s: str) -> bool:
    """
        Using a for loop (no slicing), return True if s is a palindrome,
        otherwise False. Comparison is case-sensitive.
    """
    pass


def task_66(s: str) -> int:
    """
        Using a for loop, return the count of vowels (a, e, i, o, u — both cases)
        in the string s.
    """
    pass


def task_67(n: int) -> List[int]:
    """
        Return a list of all prime numbers up to and including n.
    """
    pass


def task_68(nums: List[int]) -> int:
    """
        Using a for loop, return the product of all elements in nums.
        Return 1 for an empty list.
    """
    pass


def task_69(s: str) -> Dict[str, int]:
    """
        Using a for loop, return a dict mapping each character in s to its
        last (rightmost) index of occurrence.
    """
    pass


def task_70(n: int) -> int:
    """
        Return the sum of the digits of the non-negative integer n.
        e.g. 123 -> 6
    """
    pass


def task_71(n: int) -> List[int]:
    """
        Return a list of all Armstrong numbers from 1 to n inclusive.
        An Armstrong number equals the sum of its own digits each raised to the
        power of the number of digits. e.g. 153 = 1^3 + 5^3 + 3^3.
    """
    pass


def task_72(nums: List[int]) -> List[int]:
    """
        Return a new list where each element is multiplied by its index.
        e.g. [5, 3, 2] -> [0, 3, 4]
    """
    pass


def task_73(nums: List[int]) -> List[Tuple[int, int]]:
    """
        Return a list of (element, index) tuples for each element in nums.
        e.g. [10, 20, 30] -> [(10, 0), (20, 1), (30, 2)]
    """
    pass


# ── WHILE LOOP TASKS (task_74 – task_85) ─────────────────────────────────────

def task_74(n: int) -> int:
    """
        Using a while loop, return the number of digits in the non-negative integer n.
        e.g. 0 -> 1, 123 -> 3
    """
    pass


def task_75(n: int) -> int:
    """
        Using a while loop, reverse the digits of the non-negative integer n and return it.
        e.g. 1234 -> 4321, 100 -> 1
    """
    pass


def task_76(n: int) -> int:
    """
        Compute the digital root of a positive integer: repeatedly sum its digits
        until the result is a single digit, then return it.
        e.g. 493 -> 4+9+3=16 -> 1+6=7
    """
    pass


def task_77(a: int, b: int) -> int:
    """
        Return the greatest common divisor of a and b using the Euclidean algorithm
        implemented with a while loop.
    """
    pass


def task_78(n: int) -> bool:
    """
        Using a while loop, return True if n is a power of 2, otherwise False.
        You may assume n >= 1.
    """
    pass


def task_79(n: float) -> int:
    """
        Return how many times you can halve n (n = n / 2) while n > 1.
        Stop when n reaches 1 (do not count the halving that would produce <1).
        e.g. n=8 -> 3  (8->4->2->1, three halvings)
    """
    pass


def task_80(n: int) -> List[int]:
    """
        Return the Collatz sequence starting from n as a list.
        If n is even, the next term is n // 2.
        If n is odd, the next term is 3 * n + 1.
        Stop when the sequence reaches 1 (include 1 in the list).
        e.g. n=6 -> [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    pass


def task_81(n: int) -> int:
    """
        Return the integer (floor) square root of n without using math.sqrt, **.5,
        or the math module. Use a while loop.
        e.g. 16 -> 4, 17 -> 4, 9 -> 3
    """
    pass


def task_82(n: int) -> List[int]:
    """
        Using a while loop, return a list of the first n perfect squares (starting from 1).
        e.g. n=4 -> [1, 4, 9, 16]
    """
    pass


def task_83(n: int) -> List[int]:
    """
        Using a while loop, return a countdown list from n down to 0 inclusive.
        e.g. n=4 -> [4, 3, 2, 1, 0]
    """
    pass


def task_84(n: int) -> int:
    """
        Return the number of steps to reduce n to 1 using the following rule:
          If n is even: n = n // 2
          If n is odd:  n = 3 * n + 1
        (This is the Collatz conjecture step count.)
    """
    pass


def task_85(n: float) -> int:
    """
        Starting from n, keep dividing by 3 (n = n / 3) while n > 1.
        Stop when n reaches 1 (do not count the division that would produce <1).
        Return the number of divisions performed.
        e.g. n=9 -> 2  (9->3->1, two divisions)
    """
    pass


# ── DATA TYPES — int, float, str (task_86 – task_99) ─────────────────────────

def task_86(f: float) -> int:
    """
        Convert the float f to an integer by truncating (floor towards zero)
        without using int() or math.floor(). Use the // operator.
        e.g. 3.9 -> 3, -2.7 -> -2 (truncate, not floor)
        Hint: for negative numbers, use math.ceil equivalent logic or just use //
        For simplicity: return int(f) is NOT allowed; use f // 1 cast approach
        Actually: return the integer part by truncating towards zero.
        Simplest allowed: f // 1 for positives. For this task just return int(f // 1).
    """
    pass


def task_87(f: float, n: int) -> float:
    """
        Return f rounded to n decimal places.
    """
    pass


def task_88(s: str) -> bool:
    """
        Return True if s represents a valid integer (possibly with a leading '-' sign),
        otherwise False. Do not use try/except.
        e.g. "123" -> True, "-45" -> True, "12.3" -> False, "abc" -> False
    """
    pass


def task_89(s: str) -> bool:
    """
        Return True if s can be converted to a float, otherwise False.
        Use a try/except block.
        e.g. "3.14" -> True, "42" -> True, "abc" -> False
    """
    pass


def task_90(n: int) -> str:
    """
        Convert the non-negative integer n to its binary representation as a string,
        without the '0b' prefix.
        e.g. 10 -> "1010", 0 -> "0"
    """
    pass


def task_91(n: int) -> str:
    """
        Convert the non-negative integer n to its hexadecimal representation as a
        lowercase string, without the '0x' prefix.
        e.g. 255 -> "ff", 16 -> "10"
    """
    pass


def task_92(c: str) -> int:
    """
        Return the ASCII (Unicode code point) value of the single character c.
    """
    pass


def task_93(code: int) -> str:
    """
        Return the character corresponding to the ASCII value code.
    """
    pass


def task_94(s: str, n: int) -> str:
    """
        Return the string s repeated n times.
        e.g. "ab", 3 -> "ababab"
    """
    pass


def task_95(s: str) -> str:
    """
        Capitalize the first letter of each word in s and return the result.
        e.g. "hello world" -> "Hello World"
    """
    pass


def task_96(s: str) -> bool:
    """
        Return True if every character in s is a digit (0-9), otherwise False.
        Do not use str.isdigit(); check each character manually.
    """
    pass


def task_97(s: str) -> str:
    """
        Return a copy of s with all vowels (a, e, i, o, u — both cases) removed.
        e.g. "Hello World" -> "Hll Wrld"
    """
    pass


def task_98(f: float) -> str:
    """
        Return f formatted as a string with exactly 2 decimal places.
        e.g. 3.14159 -> "3.14", 5.0 -> "5.00"
    """
    pass


def task_99(n: int) -> bool:
    """
        Return True if n is a perfect square (i.e. some integer k satisfies k*k == n),
        otherwise False. You may assume n >= 0.
        e.g. 0 -> True, 1 -> True, 4 -> True, 8 -> False
    """
    pass
