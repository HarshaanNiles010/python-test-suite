from typing import List, Dict, Optional, Any

def task_0() -> None:
    """
        Write a program to print a simple string to the output
    """    
    pass

def task_1() -> None:
    """
        Write a program to take a user_input and print it out
    """
    pass

def task_2(num_1: int, num_2: int) -> int:
    """
        Write a program which returns the larger of two integers
    """
    pass

def task_3(num_1: int, num_2: int, num_3: int) -> int:
    """
        Write a program which returns the largest of three integers
    """
    pass

def task_4(string_1: str, string_2: str) -> str:
    """
        Write a program which concatenates two strings and returns the output
    """
    pass

def task_5(string_1: str, num_1: int) -> str:
    """
        There is an error in this program fix it
    """
    return string_1 + num_1
    pass

def task_6(string_1: str, num_1: int) -> str:
    """
        Write a program that concatenates the string_1 and num_1 and returns a str
    """
    pass

def task_7(string_1: str, num_1: int) -> int:
    """
        Write a program that converts a string to int and returns the sum 
    """
    pass

def task_8() -> None:
    """
        Write a program which declares a dict and print it out
    """
    pass

def task_9(user_keys: List[int], user_vals: List[int]) -> None:
    """
        Write a program which takes the user_keys & user_vals and prints a dictionary with them
    """
    pass

def task_10(user_input: List[int]) -> None:
    """
        Write a program which iterates over the input and prints its values
    """
    pass

def task_11(nums: List[int]) -> int:
    """
        Write a program which returns the largest value of the input list 
    """
    pass

def task_12(nums: List[int]) -> int:
    """
        Write a program which returns the smallest value of the input list
    """
    pass

def task_13(nums: List[int]) -> None:
    """
        Write a program which
        prints the word "Fizz" if a number in the input list is divisible by 3
        prints the word "Buzz" if a number in the input list is divisible by 5
        prints the word "Fizz Buzz" if a number in the input list is divisible by both 5 & 3
    """
    pass

def task_14(input_str: str) -> List[str]:
    """
        Write a program which returns a list of charachters between a-z (lowercase only)
    """
    pass

def task_15(input_str: str) -> List[int]:
    """
        Write a program which returns a list of integers filtered from the input_str
    """
    pass

def task_16(input_str: str) -> str:
    """
        Write a program which removes the trailing and leading white spaces from a string in python
    """
    pass

def task_17(input_str: str) -> Dict[str, int]:
    """
        Write a program which returns the frequency distribution of the characters in the input string
    """
    pass

def task_18(input_str: str) -> str:
    """
        Write a program which returns the charachter with the lowest ordinal value
    """
    pass

def task_19(input_str: str) -> int:
    """
        Write a program which returns the index of the most frequent charachter
    """
    pass

def task_20() -> None:
    """
        Write a list comprehension to convert all even numbers into odd numbers
    """
    pass

def task_21(input_list: List[int]) -> List[int]:
    """
        Write a program to remove duplicates from the list
    """
    pass

def task_22(input_list_1: List[int], input_list_2: List[int]) -> List[int]:
    """
        Write a program to merge 2 sorted lists
    """
    pass

def task_23(input_str: str) -> int:
    """
        Write a program which returns the least frequent element in the input_str
    """
    pass

def task_24(input_value: int, input_list = []) -> List[int]:
    """
       Fix the program,
       currently if I run this program, it generates the following output
       print(task_24(1)) -> [1]
       print(task_24(2)) -> [1,2] # This is erroneous I only want [2] as the output        
    """
    input_list.append(input_value)
    return input_list
    pass

