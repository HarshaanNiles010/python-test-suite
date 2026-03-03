import pytest
from problems.sorting_task import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12, task_13, task_14,
    task_15, task_16, task_17, task_18, task_19,
)


# --- Bubble Sort Tests ---

def test_task_0_basic():
    assert task_0([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_0_empty():
    assert task_0([]) == []

def test_task_0_single():
    assert task_0([1]) == [1]

def test_task_0_already_sorted():
    assert task_0([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_task_0_duplicates():
    assert task_0([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

def test_task_0_no_modify():
    original = [5, 3, 1]
    task_0(original)
    assert original == [5, 3, 1]

def test_task_1_ascending():
    assert task_1([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_1_descending():
    assert task_1([5, 3, 8, 1, 2], reverse=True) == [8, 5, 3, 2, 1]

def test_task_1_empty():
    assert task_1([], reverse=True) == []

def test_task_1_single_descending():
    assert task_1([42], reverse=True) == [42]

def test_task_2_basic():
    assert task_2([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_2_already_sorted():
    assert task_2([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_task_2_empty():
    assert task_2([]) == []

def test_task_3_basic():
    result, swaps = task_3([5, 3, 8, 1, 2])
    assert result == [1, 2, 3, 5, 8]
    assert swaps > 0

def test_task_3_sorted():
    result, swaps = task_3([1, 2, 3])
    assert result == [1, 2, 3]
    assert swaps == 0

def test_task_3_reverse_sorted():
    result, swaps = task_3([3, 2, 1])
    assert result == [1, 2, 3]
    assert swaps == 3

def test_task_3_empty():
    result, swaps = task_3([])
    assert result == []
    assert swaps == 0

def test_task_4_basic():
    data = [(1, "b"), (3, "a"), (2, "c")]
    assert task_4(data, 0) == [(1, "b"), (2, "c"), (3, "a")]

def test_task_4_by_second_element():
    data = [(1, "b"), (3, "a"), (2, "c")]
    assert task_4(data, 1) == [(3, "a"), (1, "b"), (2, "c")]

def test_task_4_empty():
    assert task_4([], 0) == []

def test_task_4_no_modify():
    original = [(3, "a"), (1, "b")]
    task_4(original, 0)
    assert original == [(3, "a"), (1, "b")]


# --- Insertion Sort Tests ---

def test_task_5_basic():
    assert task_5([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_5_empty():
    assert task_5([]) == []

def test_task_5_single():
    assert task_5([1]) == [1]

def test_task_5_already_sorted():
    assert task_5([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_task_5_duplicates():
    assert task_5([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

def test_task_5_no_modify():
    original = [5, 3, 1]
    task_5(original)
    assert original == [5, 3, 1]

def test_task_6_ascending():
    assert task_6([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_6_descending():
    assert task_6([5, 3, 8, 1, 2], reverse=True) == [8, 5, 3, 2, 1]

def test_task_6_empty():
    assert task_6([], reverse=True) == []

def test_task_7_abs_key():
    assert task_7([-5, 3, -1, 2], key=abs) == [-1, 2, 3, -5]

def test_task_7_negate_key():
    assert task_7([5, 3, 8, 1], key=lambda x: -x) == [8, 5, 3, 1]

def test_task_7_empty():
    assert task_7([], key=abs) == []

def test_task_7_no_modify():
    original = [-5, 3, -1]
    task_7(original, key=abs)
    assert original == [-5, 3, -1]

def test_task_8_basic():
    result, comparisons = task_8([5, 3, 8, 1, 2])
    assert result == [1, 2, 3, 5, 8]
    assert comparisons > 0

def test_task_8_sorted():
    result, comparisons = task_8([1, 2, 3])
    assert result == [1, 2, 3]
    assert comparisons > 0

def test_task_8_empty():
    result, comparisons = task_8([])
    assert result == []
    assert comparisons == 0

def test_task_8_single():
    result, comparisons = task_8([42])
    assert result == [42]
    assert comparisons == 0

def test_task_9_basic():
    assert task_9([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_9_empty():
    assert task_9([]) == []

def test_task_9_single():
    assert task_9([1]) == [1]

def test_task_9_duplicates():
    assert task_9([4, 2, 4, 1, 3]) == [1, 2, 3, 4, 4]

def test_task_9_already_sorted():
    assert task_9([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_task_9_no_modify():
    original = [5, 3, 1]
    task_9(original)
    assert original == [5, 3, 1]


# --- Merge Sort Tests ---

def test_task_10_basic():
    assert task_10([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_10_empty():
    assert task_10([]) == []

def test_task_10_single():
    assert task_10([1]) == [1]

def test_task_10_already_sorted():
    assert task_10([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_task_10_duplicates():
    assert task_10([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

def test_task_10_no_modify():
    original = [5, 3, 1]
    task_10(original)
    assert original == [5, 3, 1]

def test_task_11_basic():
    assert task_11([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_task_11_one_empty():
    assert task_11([], [1, 2, 3]) == [1, 2, 3]
    assert task_11([1, 2, 3], []) == [1, 2, 3]

def test_task_11_both_empty():
    assert task_11([], []) == []

def test_task_11_duplicates():
    assert task_11([1, 3, 5], [1, 3, 5]) == [1, 1, 3, 3, 5, 5]

def test_task_11_unequal_lengths():
    assert task_11([1], [2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_task_12_ascending():
    assert task_12([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_12_descending():
    assert task_12([5, 3, 8, 1, 2], reverse=True) == [8, 5, 3, 2, 1]

def test_task_12_empty():
    assert task_12([], reverse=True) == []

def test_task_12_no_modify():
    original = [5, 3, 1]
    task_12(original)
    assert original == [5, 3, 1]

def test_task_13_basic():
    result, comparisons = task_13([5, 3, 8, 1, 2])
    assert result == [1, 2, 3, 5, 8]
    assert comparisons > 0

def test_task_13_sorted():
    result, comparisons = task_13([1, 2, 3])
    assert result == [1, 2, 3]
    assert comparisons > 0

def test_task_13_empty():
    result, comparisons = task_13([])
    assert result == []
    assert comparisons == 0

def test_task_13_single():
    result, comparisons = task_13([42])
    assert result == [42]
    assert comparisons == 0

def test_task_14_basic():
    assert task_14(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]

def test_task_14_empty():
    assert task_14([]) == []

def test_task_14_single():
    assert task_14(["hello"]) == ["hello"]

def test_task_14_case_sensitive():
    assert task_14(["Banana", "apple", "Cherry"]) == ["Banana", "Cherry", "apple"]

def test_task_14_no_modify():
    original = ["banana", "apple"]
    task_14(original)
    assert original == ["banana", "apple"]


# --- Quick Sort Tests ---

def test_task_15_basic():
    assert task_15([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_15_empty():
    assert task_15([]) == []

def test_task_15_single():
    assert task_15([1]) == [1]

def test_task_15_already_sorted():
    assert task_15([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_task_15_duplicates():
    assert task_15([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

def test_task_15_no_modify():
    original = [5, 3, 1]
    task_15(original)
    assert original == [5, 3, 1]

def test_task_16_basic():
    assert task_16([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_16_empty():
    assert task_16([]) == []

def test_task_16_single():
    assert task_16([1]) == [1]

def test_task_16_duplicates():
    assert task_16([4, 2, 4, 1, 3]) == [1, 2, 3, 4, 4]

def test_task_16_no_modify():
    original = [5, 3, 1]
    task_16(original)
    assert original == [5, 3, 1]

def test_task_17_ascending():
    assert task_17([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_17_descending():
    assert task_17([5, 3, 8, 1, 2], reverse=True) == [8, 5, 3, 2, 1]

def test_task_17_empty():
    assert task_17([], reverse=True) == []

def test_task_17_no_modify():
    original = [5, 3, 1]
    task_17(original)
    assert original == [5, 3, 1]

def test_task_18_basic():
    result, pivot_idx = task_18([3, 6, 8, 10, 1, 2, 1])
    pivot_val = result[pivot_idx]
    assert pivot_val == 1
    assert all(x <= pivot_val for x in result[:pivot_idx])
    assert all(x >= pivot_val for x in result[pivot_idx:])

def test_task_18_sorted():
    result, pivot_idx = task_18([1, 2, 3, 4, 5])
    pivot_val = result[pivot_idx]
    assert pivot_val == 5
    assert all(x <= pivot_val for x in result[:pivot_idx])
    assert all(x >= pivot_val for x in result[pivot_idx:])

def test_task_18_single():
    result, pivot_idx = task_18([42])
    assert result == [42]
    assert pivot_idx == 0

def test_task_18_two_elements():
    result, pivot_idx = task_18([2, 1])
    pivot_val = result[pivot_idx]
    assert pivot_val == 1
    assert all(x <= pivot_val for x in result[:pivot_idx])
    assert all(x >= pivot_val for x in result[pivot_idx:])

def test_task_18_no_modify():
    original = [3, 1, 2]
    task_18(original)
    assert original == [3, 1, 2]

def test_task_19_basic():
    assert task_19([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_19_empty():
    assert task_19([]) == []

def test_task_19_single():
    assert task_19([1]) == [1]

def test_task_19_duplicates():
    assert task_19([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

def test_task_19_already_sorted():
    assert task_19([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_task_19_no_modify():
    original = [5, 3, 1]
    task_19(original)
    assert original == [5, 3, 1]
