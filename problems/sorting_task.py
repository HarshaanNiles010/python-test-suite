from typing import List, Tuple, Callable

# --- task_0 through task_4: Bubble Sort ---

def task_0(arr: List[int]) -> List[int]:
    """
        Implement bubble sort to sort a list of integers in ascending order.
        Return the sorted list. Do not modify the original list.
    """
    pass

def task_1(arr: List[int], reverse: bool = False) -> List[int]:
    """
        Implement bubble sort with a reverse flag.
        When reverse is False, sort in ascending order.
        When reverse is True, sort in descending order.
        Return the sorted list. Do not modify the original list.
    """
    pass

def task_2(arr: List[int]) -> List[int]:
    """
        Implement an optimized bubble sort that stops early if no swaps
        occur during a pass (the list is already sorted).
        Return the sorted list in ascending order. Do not modify the original list.
    """
    pass

def task_3(arr: List[int]) -> Tuple[List[int], int]:
    """
        Implement bubble sort and count the number of swaps performed.
        Return a tuple of (sorted_list, swap_count).
        Sort in ascending order. Do not modify the original list.
    """
    pass

def task_4(arr: List[Tuple], key_index: int) -> List[Tuple]:
    """
        Implement bubble sort to sort a list of tuples by the element
        at the given key_index.
        Sort in ascending order. Do not modify the original list.
    """
    pass

# --- task_5 through task_9: Insertion Sort ---

def task_5(arr: List[int]) -> List[int]:
    """
        Implement insertion sort to sort a list of integers in ascending order.
        Return the sorted list. Do not modify the original list.
    """
    pass

def task_6(arr: List[int], reverse: bool = False) -> List[int]:
    """
        Implement insertion sort with a reverse flag.
        When reverse is False, sort in ascending order.
        When reverse is True, sort in descending order.
        Return the sorted list. Do not modify the original list.
    """
    pass

def task_7(arr: List[int], key: Callable) -> List[int]:
    """
        Implement insertion sort with a custom key function.
        Sort elements based on the value returned by key(element).
        Return the sorted list in ascending order of the key values.
        Do not modify the original list.
    """
    pass

def task_8(arr: List[int]) -> Tuple[List[int], int]:
    """
        Implement insertion sort and count the number of comparisons made.
        A comparison occurs each time two elements are compared.
        Return a tuple of (sorted_list, comparison_count).
        Sort in ascending order. Do not modify the original list.
    """
    pass

def task_9(arr: List[int]) -> List[int]:
    """
        Implement binary insertion sort.
        Use binary search to find the correct insertion position for each element,
        then insert it at that position.
        Return the sorted list in ascending order. Do not modify the original list.
    """
    pass

# --- task_10 through task_14: Merge Sort ---

def task_10(arr: List[int]) -> List[int]:
    """
        Implement merge sort to sort a list of integers in ascending order.
        Return the sorted list. Do not modify the original list.
    """
    pass

def task_11(left: List[int], right: List[int]) -> List[int]:
    """
        Implement the merge step of merge sort.
        Given two already-sorted lists (ascending), merge them into a single
        sorted list in ascending order and return it.
    """
    pass

def task_12(arr: List[int], reverse: bool = False) -> List[int]:
    """
        Implement merge sort with a reverse flag.
        When reverse is False, sort in ascending order.
        When reverse is True, sort in descending order.
        Return the sorted list. Do not modify the original list.
    """
    pass

def task_13(arr: List[int]) -> Tuple[List[int], int]:
    """
        Implement merge sort and count the total number of comparisons made
        during the merge steps.
        A comparison occurs each time two elements are compared in the merge step.
        Return a tuple of (sorted_list, comparison_count).
        Sort in ascending order. Do not modify the original list.
    """
    pass

def task_14(arr: List[str]) -> List[str]:
    """
        Implement merge sort to sort a list of strings in lexicographic
        (alphabetical) order.
        Return the sorted list. Do not modify the original list.
    """
    pass

# --- task_15 through task_19: Quick Sort ---

def task_15(arr: List[int]) -> List[int]:
    """
        Implement quick sort to sort a list of integers in ascending order.
        Use the first element as the pivot.
        Return the sorted list. Do not modify the original list.
    """
    pass

def task_16(arr: List[int]) -> List[int]:
    """
        Implement quick sort using the last element as the pivot.
        Return the sorted list in ascending order. Do not modify the original list.
    """
    pass

def task_17(arr: List[int], reverse: bool = False) -> List[int]:
    """
        Implement quick sort with a reverse flag.
        Use the first element as the pivot.
        When reverse is False, sort in ascending order.
        When reverse is True, sort in descending order.
        Return the sorted list. Do not modify the original list.
    """
    pass

def task_18(arr: List[int]) -> Tuple[List[int], int]:
    """
        Implement the partition step of quick sort.
        Use the last element as the pivot.
        Rearrange elements so that all elements less than the pivot come before it,
        and all elements greater come after it.
        Return a tuple of (partitioned_list, pivot_index).
        Do not modify the original list.
    """
    pass

def task_19(arr: List[int]) -> List[int]:
    """
        Implement quick sort with median-of-three pivot selection.
        The median-of-three chooses the median of the first, middle, and last elements
        as the pivot.
        Return the sorted list in ascending order. Do not modify the original list.
    """
    pass
