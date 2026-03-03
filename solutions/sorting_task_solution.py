from typing import List, Tuple, Callable

# --- task_0 through task_4: Bubble Sort ---

def task_0(arr: List[int]) -> List[int]:
    """
        Implement bubble sort to sort a list of integers in ascending order.
        Return the sorted list. Do not modify the original list.
    """
    result = arr[:]
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def task_1(arr: List[int], reverse: bool = False) -> List[int]:
    """
        Implement bubble sort with a reverse flag.
        When reverse is False, sort in ascending order.
        When reverse is True, sort in descending order.
        Return the sorted list. Do not modify the original list.
    """
    result = arr[:]
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if reverse:
                if result[j] < result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
            else:
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
    return result

def task_2(arr: List[int]) -> List[int]:
    """
        Implement an optimized bubble sort that stops early if no swaps
        occur during a pass (the list is already sorted).
        Return the sorted list in ascending order. Do not modify the original list.
    """
    result = arr[:]
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result

def task_3(arr: List[int]) -> Tuple[List[int], int]:
    """
        Implement bubble sort and count the number of swaps performed.
        Return a tuple of (sorted_list, swap_count).
        Sort in ascending order. Do not modify the original list.
    """
    result = arr[:]
    n = len(result)
    swap_count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swap_count += 1
    return result, swap_count

def task_4(arr: List[Tuple], key_index: int) -> List[Tuple]:
    """
        Implement bubble sort to sort a list of tuples by the element
        at the given key_index.
        Sort in ascending order. Do not modify the original list.
    """
    result = list(arr)
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j][key_index] > result[j + 1][key_index]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

# --- task_5 through task_9: Insertion Sort ---

def task_5(arr: List[int]) -> List[int]:
    """
        Implement insertion sort to sort a list of integers in ascending order.
        Return the sorted list. Do not modify the original list.
    """
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result

def task_6(arr: List[int], reverse: bool = False) -> List[int]:
    """
        Implement insertion sort with a reverse flag.
        When reverse is False, sort in ascending order.
        When reverse is True, sort in descending order.
        Return the sorted list. Do not modify the original list.
    """
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        if reverse:
            while j >= 0 and result[j] < key:
                result[j + 1] = result[j]
                j -= 1
        else:
            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1
        result[j + 1] = key
    return result

def task_7(arr: List[int], key: Callable) -> List[int]:
    """
        Implement insertion sort with a custom key function.
        Sort elements based on the value returned by key(element).
        Return the sorted list in ascending order of the key values.
        Do not modify the original list.
    """
    result = arr[:]
    for i in range(1, len(result)):
        current = result[i]
        current_key = key(current)
        j = i - 1
        while j >= 0 and key(result[j]) > current_key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result

def task_8(arr: List[int]) -> Tuple[List[int], int]:
    """
        Implement insertion sort and count the number of comparisons made.
        A comparison occurs each time two elements are compared.
        Return a tuple of (sorted_list, comparison_count).
        Sort in ascending order. Do not modify the original list.
    """
    result = arr[:]
    comparisons = 0
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if result[j] > key:
                result[j + 1] = result[j]
                j -= 1
            else:
                break
        result[j + 1] = key
    return result, comparisons

def task_9(arr: List[int]) -> List[int]:
    """
        Implement binary insertion sort.
        Use binary search to find the correct insertion position for each element,
        then insert it at that position.
        Return the sorted list in ascending order. Do not modify the original list.
    """
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        lo, hi = 0, i
        while lo < hi:
            mid = (lo + hi) // 2
            if result[mid] > key:
                hi = mid
            else:
                lo = mid + 1
        for j in range(i, lo, -1):
            result[j] = result[j - 1]
        result[lo] = key
    return result

# --- task_10 through task_14: Merge Sort ---

def task_10(arr: List[int]) -> List[int]:
    """
        Implement merge sort to sort a list of integers in ascending order.
        Return the sorted list. Do not modify the original list.
    """
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = task_10(arr[:mid])
    right = task_10(arr[mid:])
    return _merge(left, right)

def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def task_11(left: List[int], right: List[int]) -> List[int]:
    """
        Implement the merge step of merge sort.
        Given two already-sorted lists (ascending), merge them into a single
        sorted list in ascending order and return it.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def task_12(arr: List[int], reverse: bool = False) -> List[int]:
    """
        Implement merge sort with a reverse flag.
        When reverse is False, sort in ascending order.
        When reverse is True, sort in descending order.
        Return the sorted list. Do not modify the original list.
    """
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = task_12(arr[:mid], reverse=reverse)
    right = task_12(arr[mid:], reverse=reverse)
    return _merge_with_order(left, right, reverse)

def _merge_with_order(left: List[int], right: List[int], reverse: bool) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if reverse:
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def task_13(arr: List[int]) -> Tuple[List[int], int]:
    """
        Implement merge sort and count the total number of comparisons made
        during the merge steps.
        A comparison occurs each time two elements are compared in the merge step.
        Return a tuple of (sorted_list, comparison_count).
        Sort in ascending order. Do not modify the original list.
    """
    if len(arr) <= 1:
        return arr[:], 0
    mid = len(arr) // 2
    left, left_count = task_13(arr[:mid])
    right, right_count = task_13(arr[mid:])
    merged, merge_count = _merge_count(left, right)
    return merged, left_count + right_count + merge_count

def _merge_count(left: List[int], right: List[int]) -> Tuple[List[int], int]:
    result = []
    comparisons = 0
    i = j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, comparisons

def task_14(arr: List[str]) -> List[str]:
    """
        Implement merge sort to sort a list of strings in lexicographic
        (alphabetical) order.
        Return the sorted list. Do not modify the original list.
    """
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = task_14(arr[:mid])
    right = task_14(arr[mid:])
    return _merge_strings(left, right)

def _merge_strings(left: List[str], right: List[str]) -> List[str]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- task_15 through task_19: Quick Sort ---

def task_15(arr: List[int]) -> List[int]:
    """
        Implement quick sort to sort a list of integers in ascending order.
        Use the first element as the pivot.
        Return the sorted list. Do not modify the original list.
    """
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return task_15(less) + [pivot] + task_15(greater)

def task_16(arr: List[int]) -> List[int]:
    """
        Implement quick sort using the last element as the pivot.
        Return the sorted list in ascending order. Do not modify the original list.
    """
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    return task_16(less) + [pivot] + task_16(greater)

def task_17(arr: List[int], reverse: bool = False) -> List[int]:
    """
        Implement quick sort with a reverse flag.
        Use the first element as the pivot.
        When reverse is False, sort in ascending order.
        When reverse is True, sort in descending order.
        Return the sorted list. Do not modify the original list.
    """
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[0]
    if reverse:
        less = [x for x in arr[1:] if x >= pivot]
        greater = [x for x in arr[1:] if x < pivot]
    else:
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
    return task_17(less, reverse=reverse) + [pivot] + task_17(greater, reverse=reverse)

def task_18(arr: List[int]) -> Tuple[List[int], int]:
    """
        Implement the partition step of quick sort.
        Use the last element as the pivot.
        Rearrange elements so that all elements less than the pivot come before it,
        and all elements greater come after it.
        Return a tuple of (partitioned_list, pivot_index).
        Do not modify the original list.
    """
    result = arr[:]
    n = len(result)
    pivot = result[n - 1]
    i = -1
    for j in range(n - 1):
        if result[j] <= pivot:
            i += 1
            result[i], result[j] = result[j], result[i]
    i += 1
    result[i], result[n - 1] = result[n - 1], result[i]
    return result, i

def task_19(arr: List[int]) -> List[int]:
    """
        Implement quick sort with median-of-three pivot selection.
        The median-of-three chooses the median of the first, middle, and last elements
        as the pivot.
        Return the sorted list in ascending order. Do not modify the original list.
    """
    if len(arr) <= 1:
        return arr[:]
    result = arr[:]
    first, mid_idx, last = result[0], result[len(result) // 2], result[-1]
    pivot = sorted([first, mid_idx, last])[1]
    less = [x for x in result if x < pivot]
    equal = [x for x in result if x == pivot]
    greater = [x for x in result if x > pivot]
    return task_19(less) + equal + task_19(greater)
