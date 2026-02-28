from typing import List, Dict, Optional, Any

def task_0() -> None:
    """
        Write a program to print a simple string to the output
    """
    print("Hello, World!")

def task_1() -> None:
    """
        Write a program to take a user_input and print it out
    """
    user_input = input()
    print(user_input)

def task_2(num_1: int, num_2: int) -> int:
    """
        Write a program which returns the larger of two integers
    """
    return max(num_1, num_2)

def task_3(num_1: int, num_2: int, num_3: int) -> int:
    """
        Write a program which returns the largest of three integers
    """
    return max(num_1, num_2, num_3)

def task_4(string_1: str, string_2: str) -> str:
    """
        Write a program which concatenates two strings and returns the output
    """
    return string_1 + string_2

def task_5(string_1: str, num_1: int) -> str:
    """
        There is an error in this program fix it
    """
    return string_1 + str(num_1)

def task_6(string_1: str, num_1: int) -> str:
    """
        Write a program that concatenates the string_1 and num_1 and returns a str
    """
    return string_1 + str(num_1)

def task_7(string_1: str, num_1: int) -> int:
    """
        Write a program that converts a string to int and returns the sum
    """
    return int(string_1) + num_1

def task_8() -> None:
    """
        Write a program which declares a dict and print it out
    """
    d = {"key": "value"}
    print(d)

def task_9(user_keys: List[int], user_vals: List[int]) -> None:
    """
        Write a program which takes the user_keys & user_vals and prints a dictionary with them
    """
    d = dict(zip(user_keys, user_vals))
    print(d)

def task_10(user_input: List[int]) -> None:
    """
        Write a program which iterates over the input and prints its values
    """
    for item in user_input:
        print(item)

def task_11(nums: List[int]) -> int:
    """
        Write a program which returns the largest value of the input list
    """
    return max(nums)

def task_12(nums: List[int]) -> int:
    """
        Write a program which returns the smallest value of the input list
    """
    return min(nums)

def task_13(nums: List[int]) -> None:
    """
        Write a program which
        prints the word "Fizz" if a number in the input list is divisible by 3
        prints the word "Buzz" if a number in the input list is divisible by 5
        prints the word "Fizz Buzz" if a number in the input list is divisible by both 5 & 3
    """
    for num in nums:
        if num % 3 == 0 and num % 5 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")

def task_14(input_str: str) -> List[str]:
    """
        Write a program which returns a list of charachters between a-z (lowercase only)
    """
    return [c for c in input_str if c.islower()]

def task_15(input_str: str) -> List[int]:
    """
        Write a program which returns a list of integers filtered from the input_str
    """
    return [int(c) for c in input_str if c.isdigit()]

def task_16(input_str: str) -> str:
    """
        Write a program which removes the trailing and leading white spaces from a string in python
    """
    return input_str.strip()

def task_17(input_str: str) -> Dict[str, int]:
    """
        Write a program which returns the frequency distribution of the characters in the input string
    """
    freq = {}
    for c in input_str:
        freq[c] = freq.get(c, 0) + 1
    return freq

def task_18(input_str: str) -> str:
    """
        Write a program which returns the charachter with the lowest ordinal value
    """
    return min(input_str)

def task_19(input_str: str) -> int:
    """
        Write a program which returns the index of the most frequent charachter
    """
    freq = {}
    for c in input_str:
        freq[c] = freq.get(c, 0) + 1
    most_frequent = max(freq, key=freq.get)
    return input_str.index(most_frequent)

def task_20() -> None:
    """
        Write a list comprehension to convert all even numbers into odd numbers
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = [n + 1 if n % 2 == 0 else n for n in numbers]
    print(result)

def task_21(input_list: List[int]) -> List[int]:
    """
        Write a program to remove duplicates from the list
    """
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def task_22(input_list_1: List[int], input_list_2: List[int]) -> List[int]:
    """
        Write a program to merge 2 sorted lists
    """
    result = []
    i, j = 0, 0
    while i < len(input_list_1) and j < len(input_list_2):
        if input_list_1[i] <= input_list_2[j]:
            result.append(input_list_1[i])
            i += 1
        else:
            result.append(input_list_2[j])
            j += 1
    result.extend(input_list_1[i:])
    result.extend(input_list_2[j:])
    return result

def task_23(input_str: str) -> int:
    """
        Write a program which returns the least frequent element in the input_str
    """
    freq = {}
    for c in input_str:
        freq[c] = freq.get(c, 0) + 1
    least_frequent = min(freq, key=freq.get)
    return input_str.index(least_frequent)

def task_24(input_value: int, input_list=None) -> List[int]:
    """
       Fix the program,
       currently if I run this program, it generates the following output
       print(task_24(1)) -> [1]
       print(task_24(2)) -> [1,2] # This is erroneous I only want [2] as the output
    """
    if input_list is None:
        input_list = []
    input_list.append(input_value)
    return input_list
