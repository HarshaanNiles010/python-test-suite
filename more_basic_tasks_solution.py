from typing import List, Tuple, Set, Dict, Optional, Any


# ── LIST SOLUTIONS ────────────────────────────────────────────────────────────

def task_0(input_list: List[int], element: int) -> List[int]:
    """Append element to input_list and return the resulting list."""
    input_list.append(element)
    return input_list


def task_1(input_list: List[int]) -> List[int]:
    """Remove duplicate values from input_list while preserving the original order."""
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def task_2(nums: List[int]) -> int:
    """Return the second largest distinct value in nums."""
    unique = sorted(set(nums), reverse=True)
    return unique[1]


def task_3(nested: List[List[int]]) -> List[int]:
    """Flatten a one-level nested list."""
    result = []
    for sublist in nested:
        for item in sublist:
            result.append(item)
    return result


def task_4(input_list: List[int]) -> List[int]:
    """Return elements at even indices (0, 2, 4, …)."""
    return input_list[::2]


def task_5(input_list: List[int], k: int) -> List[int]:
    """Rotate input_list to the left by k positions."""
    if not input_list:
        return input_list
    k = k % len(input_list)
    return input_list[k:] + input_list[:k]


def task_6(list_a: List[int], list_b: List[int]) -> List[int]:
    """Return a sorted list of elements common to both lists, without duplicates."""
    return sorted(set(list_a) & set(list_b))


def task_7(input_list: List[int]) -> List[int]:
    """Return the list reversed without using reverse() or negative step slicing."""
    result = []
    for i in range(len(input_list) - 1, -1, -1):
        result.append(input_list[i])
    return result


def task_8(input_list: List[Any], element: Any) -> int:
    """Count occurrences of element in input_list."""
    count = 0
    for item in input_list:
        if item == element:
            count += 1
    return count


def task_9(nums: List[int]) -> List[int]:
    """Return a new list where each element is squared."""
    return [x * x for x in nums]


def task_10(input_list: List[Any], value: Any) -> List[Any]:
    """Remove all occurrences of value from input_list."""
    return [item for item in input_list if item != value]


def task_11(input_list: List[int], n: int) -> List[List[int]]:
    """Split input_list into consecutive chunks of size n."""
    return [input_list[i:i + n] for i in range(0, len(input_list), n)]


def task_12(nums: List[int]) -> List[int]:
    """Return the running cumulative sum of nums."""
    result = []
    total = 0
    for x in nums:
        total += x
        result.append(total)
    return result


# ── SET SOLUTIONS ─────────────────────────────────────────────────────────────

def task_13(set_a: Set[int], set_b: Set[int]) -> Set[int]:
    """Return the union of set_a and set_b."""
    return set_a | set_b


def task_14(set_a: Set[int], set_b: Set[int]) -> Set[int]:
    """Return the intersection of set_a and set_b."""
    return set_a & set_b


def task_15(set_a: Set[int], set_b: Set[int]) -> Set[int]:
    """Return the difference set_a - set_b."""
    return set_a - set_b


def task_16(set_a: Set[int], set_b: Set[int]) -> Set[int]:
    """Return the symmetric difference of set_a and set_b."""
    return set_a ^ set_b


def task_17(set_a: Set[int], set_b: Set[int]) -> bool:
    """Return True if set_a is a subset of set_b."""
    return set_a.issubset(set_b)


def task_18(input_list: List[int]) -> List[int]:
    """Remove duplicates using a set, return sorted ascending."""
    return sorted(set(input_list))


def task_19(set_a: Set[int], set_b: Set[int]) -> bool:
    """Return True if set_a and set_b are disjoint."""
    return set_a.isdisjoint(set_b)


def task_20(input_set: Set[int]) -> List[Set[int]]:
    """Return the power set of input_set as a list of sets."""
    elements = list(input_set)
    n = len(elements)
    power_set = []
    for i in range(2 ** n):
        subset = set()
        for j in range(n):
            if i & (1 << j):
                subset.add(elements[j])
        power_set.append(subset)
    return power_set


def task_21(base_set: Set[int], elements: List[int]) -> Set[int]:
    """Add all elements from the list to base_set and return it."""
    base_set.update(elements)
    return base_set


def task_22(input_str: str) -> int:
    """Return the number of unique characters in input_str."""
    return len(set(input_str))


def task_23(input_list: List[int]) -> List[int]:
    """Return a sorted list of elements that appear more than once."""
    seen = set()
    duplicates = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return sorted(duplicates)


def task_24(input_set: Set[int]) -> int:
    """Return the largest element in input_set without using max()."""
    largest = None
    for item in input_set:
        if largest is None or item > largest:
            largest = item
    return largest


# ── TUPLE SOLUTIONS ───────────────────────────────────────────────────────────

def task_25(nums: List[int]) -> Tuple[int, int]:
    """Return a tuple of (min_value, max_value)."""
    return (min(nums), max(nums))


def task_26(t: Tuple[int, int, int]) -> int:
    """Unpack the three-element tuple t and return the sum."""
    a, b, c = t
    return a + b + c


def task_27(a: int, b: int) -> Tuple[int, int]:
    """Swap a and b using tuple unpacking."""
    a, b = b, a
    return (a, b)


def task_28(input_list: List[int]) -> Tuple:
    """Convert input_list to a tuple."""
    return tuple(input_list)


def task_29(t: Tuple, value: Any) -> int:
    """Return the index of the first occurrence of value in t, or -1."""
    for i, item in enumerate(t):
        if item == value:
            return i
    return -1


def task_30(t1: Tuple, t2: Tuple) -> Tuple:
    """Concatenate t1 and t2."""
    return t1 + t2


def task_31(n: int) -> Tuple[int, ...]:
    """Return a tuple of squares from 1 to n."""
    return tuple(i * i for i in range(1, n + 1))


def task_32(t: Tuple, index: int, val: Any) -> Tuple:
    """Return a new tuple with the element at index replaced by val."""
    lst = list(t)
    lst[index] = val
    return tuple(lst)


def task_33(t: Tuple, value: Any) -> int:
    """Return the number of times value appears in t."""
    return t.count(value)


def task_34(list_a: List, list_b: List) -> List[Tuple]:
    """Zip list_a and list_b into a list of tuples."""
    return list(zip(list_a, list_b))


def task_35(t: Tuple[int, ...]) -> Tuple[int, ...]:
    """Return t sorted in ascending order."""
    return tuple(sorted(t))


def task_36(pairs: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """Sort a list of (name, score) tuples by score in descending order."""
    return sorted(pairs, key=lambda x: x[1], reverse=True)


# ── DICT SOLUTIONS ────────────────────────────────────────────────────────────

def task_37(dict_a: Dict, dict_b: Dict) -> Dict:
    """Merge dict_a and dict_b; dict_b values take precedence."""
    result = dict_a.copy()
    result.update(dict_b)
    return result


def task_38(input_dict: Dict) -> Dict:
    """Return a new dict with keys and values swapped."""
    return {v: k for k, v in input_dict.items()}


def task_39(input_dict: Dict[str, int]) -> Dict[str, int]:
    """Return a new dict sorted by values in ascending order."""
    return dict(sorted(input_dict.items(), key=lambda x: x[1]))


def task_40(words: List[str]) -> Dict[str, int]:
    """Count the frequency of each word."""
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def task_41(input_dict: Dict[str, int], threshold: int) -> List[str]:
    """Return sorted list of keys whose value is strictly greater than threshold."""
    return sorted(k for k, v in input_dict.items() if v > threshold)


def task_42(input_dict: Dict, key: str) -> Dict:
    """Remove key from input_dict if it exists and return the dict."""
    input_dict.pop(key, None)
    return input_dict


def task_43(nested_dict: Dict, keys: List[str]) -> Any:
    """Retrieve a value from a nested dict by traversing the key path."""
    current = nested_dict
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def task_44(input_dict: Dict[str, Any], prefix: str) -> Dict[str, Any]:
    """Return only items whose key starts with prefix."""
    return {k: v for k, v in input_dict.items() if k.startswith(prefix)}


def task_45(records: List[Dict], group_key: str) -> Dict[str, List[Dict]]:
    """Group a list of dicts by the value of group_key."""
    result = {}
    for record in records:
        key = record[group_key]
        result.setdefault(key, []).append(record)
    return result


def task_46(input_dict: Dict[str, int]) -> str:
    """Return the key with the maximum value."""
    return max(input_dict, key=input_dict.get)


def task_47(input_dict: Dict[str, int]) -> Dict[str, int]:
    """Return a new dict with every value doubled."""
    return {k: v * 2 for k, v in input_dict.items()}


def task_48(n: int) -> Dict[int, int]:
    """Return a dict mapping i -> i^2 for i in 1..n using a comprehension."""
    return {i: i * i for i in range(1, n + 1)}


def task_49(dict_a: Dict, dict_b: Dict) -> bool:
    """Return True if dict_a and dict_b have exactly the same set of keys."""
    return set(dict_a.keys()) == set(dict_b.keys())


# ── IF-ELSE SOLUTIONS ─────────────────────────────────────────────────────────

def task_50(n: int) -> str:
    """Return 'positive', 'negative', or 'zero'."""
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"


def task_51(score: int) -> str:
    """Return a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def task_52(year: int) -> bool:
    """Return True if year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def task_53(n: int) -> int:
    """Return the absolute value of n without using abs()."""
    if n < 0:
        return -n
    return n


def task_54(n: int) -> str:
    """Return 'even' or 'odd'."""
    if n % 2 == 0:
        return "even"
    return "odd"


def task_55(n: int) -> int:
    """Return the sign of n: 1, -1, or 0."""
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0


def task_56(bmi: float) -> str:
    """Return the BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


def task_57(a: int, b: int, c: int) -> str:
    """Classify a triangle as equilateral, isosceles, or scalene."""
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"


def task_58(n: int) -> str:
    """Return fizzbuzz, fizz, buzz, or str(n) for a single integer."""
    if n % 15 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


def task_59(a: int, b: int, c: int) -> int:
    """Return the maximum of three integers without using max()."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def task_60(n: int, lo: int, hi: int) -> bool:
    """Return True if lo <= n <= hi."""
    return lo <= n <= hi


def task_61(month: int) -> str:
    """Return the season for a given month number."""
    if month in (12, 1, 2):
        return "Winter"
    elif month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    else:
        return "Autumn"


# ── FOR LOOP SOLUTIONS ────────────────────────────────────────────────────────

def task_62(nums: List[int]) -> int:
    """Return the sum of all numbers using a for loop."""
    total = 0
    for n in nums:
        total += n
    return total


def task_63(n: int) -> int:
    """Return the factorial of n using a for loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def task_64(n: int) -> List[int]:
    """Return the first n Fibonacci numbers."""
    if n == 0:
        return []
    fibs = [0]
    if n == 1:
        return fibs
    fibs.append(1)
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def task_65(s: str) -> bool:
    """Return True if s is a palindrome using a for loop."""
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True


def task_66(s: str) -> int:
    """Count vowels in s using a for loop."""
    vowels = set("aeiouAEIOU")
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


def task_67(n: int) -> List[int]:
    """Return all prime numbers up to and including n."""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def task_68(nums: List[int]) -> int:
    """Return the product of all elements using a for loop."""
    result = 1
    for n in nums:
        result *= n
    return result


def task_69(s: str) -> Dict[str, int]:
    """Return a dict mapping each character to its last index."""
    result = {}
    for i, ch in enumerate(s):
        result[ch] = i
    return result


def task_70(n: int) -> int:
    """Return the sum of the digits of n."""
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


def task_71(n: int) -> List[int]:
    """Return all Armstrong numbers from 1 to n."""
    result = []
    for num in range(1, n + 1):
        digits = str(num)
        power = len(digits)
        if sum(int(d) ** power for d in digits) == num:
            result.append(num)
    return result


def task_72(nums: List[int]) -> List[int]:
    """Return each element multiplied by its index."""
    return [i * v for i, v in enumerate(nums)]


def task_73(nums: List[int]) -> List[Tuple[int, int]]:
    """Return a list of (element, index) tuples."""
    return [(v, i) for i, v in enumerate(nums)]


# ── WHILE LOOP SOLUTIONS ──────────────────────────────────────────────────────

def task_74(n: int) -> int:
    """Return the number of digits in n using a while loop."""
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


def task_75(n: int) -> int:
    """Reverse the digits of n using a while loop."""
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return reversed_n


def task_76(n: int) -> int:
    """Compute the digital root of n."""
    while n >= 10:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        n = total
    return n


def task_77(a: int, b: int) -> int:
    """Return GCD using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def task_78(n: int) -> bool:
    """Return True if n is a power of 2 using a while loop."""
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True


def task_79(n: float) -> int:
    """Return how many times n can be halved before it becomes < 1."""
    count = 0
    while n > 1:
        n /= 2
        count += 1
    return count


def task_80(n: int) -> List[int]:
    """Return the Collatz sequence starting from n."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def task_81(n: int) -> int:
    """Return the integer square root of n using a while loop."""
    if n == 0:
        return 0
    x = 1
    while x * x <= n:
        x += 1
    return x - 1


def task_82(n: int) -> List[int]:
    """Return the first n perfect squares using a while loop."""
    result = []
    i = 1
    while i <= n:
        result.append(i * i)
        i += 1
    return result


def task_83(n: int) -> List[int]:
    """Return a countdown from n to 0 using a while loop."""
    result = []
    while n >= 0:
        result.append(n)
        n -= 1
    return result


def task_84(n: int) -> int:
    """Return the number of steps to reduce n to 1 (Collatz)."""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def task_85(n: float) -> int:
    """Return the number of times n is divided by 3 before n < 1."""
    count = 0
    while n > 1:
        n /= 3
        count += 1
    return count


# ── DATA TYPE SOLUTIONS ───────────────────────────────────────────────────────

def task_86(f: float) -> int:
    """Truncate float to int using floor division."""
    return int(f // 1)


def task_87(f: float, n: int) -> float:
    """Round f to n decimal places."""
    return round(f, n)


def task_88(s: str) -> bool:
    """Return True if s represents a valid integer without try/except."""
    if not s:
        return False
    start = 1 if s[0] == '-' else 0
    if start == 1 and len(s) == 1:
        return False
    return all(ch.isdigit() for ch in s[start:])


def task_89(s: str) -> bool:
    """Return True if s can be converted to a float using try/except."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def task_90(n: int) -> str:
    """Convert n to binary string without '0b' prefix."""
    return bin(n)[2:]


def task_91(n: int) -> str:
    """Convert n to hex string without '0x' prefix."""
    return hex(n)[2:]


def task_92(c: str) -> int:
    """Return the ASCII value of character c."""
    return ord(c)


def task_93(code: int) -> str:
    """Return the character for ASCII value code."""
    return chr(code)


def task_94(s: str, n: int) -> str:
    """Return s repeated n times."""
    return s * n


def task_95(s: str) -> str:
    """Capitalize the first letter of each word."""
    return s.title()


def task_96(s: str) -> bool:
    """Return True if every character in s is a digit (without isdigit())."""
    for ch in s:
        if ch < '0' or ch > '9':
            return False
    return True


def task_97(s: str) -> str:
    """Return s with all vowels removed."""
    vowels = set("aeiouAEIOU")
    return "".join(ch for ch in s if ch not in vowels)


def task_98(f: float) -> str:
    """Return f formatted to exactly 2 decimal places."""
    return f"{f:.2f}"


def task_99(n: int) -> bool:
    """Return True if n is a perfect square."""
    if n == 0:
        return True
    x = 1
    while x * x <= n:
        if x * x == n:
            return True
        x += 1
    return False
