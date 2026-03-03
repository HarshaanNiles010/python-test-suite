import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problems.data_structure_task import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12, task_13, task_14,
    task_15, task_16, task_17, task_18, task_19,
)


# --- task_0: Stack ---

def test_task_0_push_and_size():
    Stack = task_0()
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.size() == 3

def test_task_0_pop():
    Stack = task_0()
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.pop() == 20
    assert s.pop() == 10

def test_task_0_peek():
    Stack = task_0()
    s = Stack()
    s.push(42)
    assert s.peek() == 42
    assert s.size() == 1

def test_task_0_is_empty():
    Stack = task_0()
    s = Stack()
    assert s.is_empty() is True
    s.push(1)
    assert s.is_empty() is False

def test_task_0_pop_empty():
    Stack = task_0()
    s = Stack()
    with pytest.raises(IndexError, match="Stack is empty"):
        s.pop()

def test_task_0_peek_empty():
    Stack = task_0()
    s = Stack()
    with pytest.raises(IndexError, match="Stack is empty"):
        s.peek()


# --- task_1: MinStack ---

def test_task_1_basic():
    MinStack = task_1()
    s = MinStack()
    s.push(5)
    s.push(3)
    s.push(7)
    assert s.get_min() == 3

def test_task_1_min_after_pop():
    MinStack = task_1()
    s = MinStack()
    s.push(5)
    s.push(2)
    s.push(8)
    assert s.get_min() == 2
    s.pop()
    assert s.get_min() == 2
    s.pop()
    assert s.get_min() == 5

def test_task_1_duplicate_min():
    MinStack = task_1()
    s = MinStack()
    s.push(3)
    s.push(3)
    s.pop()
    assert s.get_min() == 3

def test_task_1_empty_errors():
    MinStack = task_1()
    s = MinStack()
    with pytest.raises(IndexError, match="Stack is empty"):
        s.pop()
    with pytest.raises(IndexError, match="Stack is empty"):
        s.peek()
    with pytest.raises(IndexError, match="Stack is empty"):
        s.get_min()

def test_task_1_peek_and_size():
    MinStack = task_1()
    s = MinStack()
    s.push(10)
    s.push(20)
    assert s.peek() == 20
    assert s.size() == 2
    assert s.is_empty() is False


# --- task_2: Queue ---

def test_task_2_enqueue_dequeue():
    Queue = task_2()
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

def test_task_2_peek():
    Queue = task_2()
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.peek() == 10
    assert q.size() == 2

def test_task_2_is_empty():
    Queue = task_2()
    q = Queue()
    assert q.is_empty() is True
    q.enqueue(1)
    assert q.is_empty() is False

def test_task_2_dequeue_empty():
    Queue = task_2()
    q = Queue()
    with pytest.raises(IndexError, match="Queue is empty"):
        q.dequeue()

def test_task_2_peek_empty():
    Queue = task_2()
    q = Queue()
    with pytest.raises(IndexError, match="Queue is empty"):
        q.peek()


# --- task_3: StackQueue ---

def test_task_3_enqueue_dequeue():
    StackQueue = task_3()
    q = StackQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3

def test_task_3_interleaved():
    StackQueue = task_3()
    q = StackQueue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    assert q.dequeue() == 2
    assert q.dequeue() == 3

def test_task_3_peek():
    StackQueue = task_3()
    q = StackQueue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.peek() == 10
    assert q.size() == 2

def test_task_3_is_empty():
    StackQueue = task_3()
    q = StackQueue()
    assert q.is_empty() is True
    q.enqueue(1)
    assert q.is_empty() is False

def test_task_3_dequeue_empty():
    StackQueue = task_3()
    q = StackQueue()
    with pytest.raises(IndexError, match="Queue is empty"):
        q.dequeue()


# --- task_4: Singly Linked List (basic) ---

def test_task_4_append():
    Node, SLL = task_4()
    ll = SLL()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]

def test_task_4_prepend():
    Node, SLL = task_4()
    ll = SLL()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    assert ll.to_list() == [1, 2, 3]

def test_task_4_mixed():
    Node, SLL = task_4()
    ll = SLL()
    ll.append(2)
    ll.prepend(1)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]

def test_task_4_empty():
    Node, SLL = task_4()
    ll = SLL()
    assert ll.to_list() == []

def test_task_4_node():
    Node, SLL = task_4()
    n = Node(42)
    assert n.val == 42
    assert n.next is None


# --- task_5: Singly Linked List (extended) ---

def test_task_5_delete():
    Node, SLL = task_5()
    ll = SLL()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.delete(2)
    assert ll.to_list() == [1, 3]

def test_task_5_delete_head():
    Node, SLL = task_5()
    ll = SLL()
    ll.append(1)
    ll.append(2)
    ll.delete(1)
    assert ll.to_list() == [2]

def test_task_5_delete_not_found():
    Node, SLL = task_5()
    ll = SLL()
    ll.append(1)
    with pytest.raises(ValueError, match="Value not found"):
        ll.delete(99)

def test_task_5_search():
    Node, SLL = task_5()
    ll = SLL()
    ll.append(10)
    ll.append(20)
    assert ll.search(10) is True
    assert ll.search(30) is False

def test_task_5_len():
    Node, SLL = task_5()
    ll = SLL()
    assert len(ll) == 0
    ll.append(1)
    ll.append(2)
    assert len(ll) == 2


# --- task_6: Doubly Linked List ---

def test_task_6_append():
    DoublyNode, DLL = task_6()
    ll = DLL()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]

def test_task_6_prepend():
    DoublyNode, DLL = task_6()
    ll = DLL()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    assert ll.to_list() == [1, 2, 3]

def test_task_6_reverse():
    DoublyNode, DLL = task_6()
    ll = DLL()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list_reverse() == [3, 2, 1]

def test_task_6_empty():
    DoublyNode, DLL = task_6()
    ll = DLL()
    assert ll.to_list() == []
    assert ll.to_list_reverse() == []

def test_task_6_node():
    DoublyNode, DLL = task_6()
    n = DoublyNode(42)
    assert n.val == 42
    assert n.prev is None
    assert n.next is None


# --- task_7: BST insert and search ---

def test_task_7_insert_search():
    TreeNode, BST = task_7()
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.search(5) is True
    assert bst.search(3) is True
    assert bst.search(7) is True
    assert bst.search(99) is False

def test_task_7_empty_search():
    TreeNode, BST = task_7()
    bst = BST()
    assert bst.search(1) is False

def test_task_7_duplicate():
    TreeNode, BST = task_7()
    bst = BST()
    bst.insert(5)
    bst.insert(5)
    assert bst.search(5) is True


# --- task_8: BST traversals ---

def test_task_8_in_order():
    TreeNode, BST = task_8()
    bst = BST()
    for v in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(v)
    assert bst.in_order() == [1, 3, 4, 5, 6, 7, 8]

def test_task_8_pre_order():
    TreeNode, BST = task_8()
    bst = BST()
    for v in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(v)
    assert bst.pre_order() == [5, 3, 1, 4, 7, 6, 8]

def test_task_8_post_order():
    TreeNode, BST = task_8()
    bst = BST()
    for v in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(v)
    assert bst.post_order() == [1, 4, 3, 6, 8, 7, 5]

def test_task_8_empty():
    TreeNode, BST = task_8()
    bst = BST()
    assert bst.in_order() == []
    assert bst.pre_order() == []
    assert bst.post_order() == []


# --- task_9: BST BFS ---

def test_task_9_bfs():
    TreeNode, BST = task_9()
    bst = BST()
    for v in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(v)
    assert bst.bfs() == [5, 3, 7, 1, 4, 6, 8]

def test_task_9_bfs_empty():
    TreeNode, BST = task_9()
    bst = BST()
    assert bst.bfs() == []

def test_task_9_bfs_single():
    TreeNode, BST = task_9()
    bst = BST()
    bst.insert(10)
    assert bst.bfs() == [10]


# --- task_10: BST DFS (iterative) ---

def test_task_10_dfs():
    TreeNode, BST = task_10()
    bst = BST()
    for v in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(v)
    assert bst.dfs() == [5, 3, 1, 4, 7, 6, 8]

def test_task_10_dfs_empty():
    TreeNode, BST = task_10()
    bst = BST()
    assert bst.dfs() == []

def test_task_10_dfs_single():
    TreeNode, BST = task_10()
    bst = BST()
    bst.insert(42)
    assert bst.dfs() == [42]


# --- task_11: HashMap (basic) ---

def test_task_11_put_get():
    HashMap = task_11()
    hm = HashMap()
    hm.put("a", 1)
    hm.put("b", 2)
    assert hm.get("a") == 1
    assert hm.get("b") == 2

def test_task_11_update():
    HashMap = task_11()
    hm = HashMap()
    hm.put("a", 1)
    hm.put("a", 10)
    assert hm.get("a") == 10

def test_task_11_remove():
    HashMap = task_11()
    hm = HashMap()
    hm.put("x", 42)
    hm.remove("x")
    assert hm.contains("x") is False

def test_task_11_get_missing():
    HashMap = task_11()
    hm = HashMap()
    with pytest.raises(KeyError):
        hm.get("missing")

def test_task_11_remove_missing():
    HashMap = task_11()
    hm = HashMap()
    with pytest.raises(KeyError):
        hm.remove("missing")

def test_task_11_contains():
    HashMap = task_11()
    hm = HashMap()
    hm.put("key", "val")
    assert hm.contains("key") is True
    assert hm.contains("nope") is False


# --- task_12: HashMap (extended with resize) ---

def test_task_12_put_get():
    HashMap = task_12()
    hm = HashMap()
    hm.put("a", 1)
    hm.put("b", 2)
    assert hm.get("a") == 1
    assert hm.get("b") == 2

def test_task_12_keys_values():
    HashMap = task_12()
    hm = HashMap()
    hm.put("x", 10)
    hm.put("y", 20)
    assert sorted(hm.keys()) == ["x", "y"]
    assert sorted(hm.values()) == [10, 20]

def test_task_12_size():
    HashMap = task_12()
    hm = HashMap()
    assert hm.size() == 0
    hm.put("a", 1)
    hm.put("b", 2)
    assert hm.size() == 2
    hm.remove("a")
    assert hm.size() == 1

def test_task_12_resize():
    HashMap = task_12()
    hm = HashMap(initial_size=4)
    for i in range(10):
        hm.put(f"key{i}", i)
    assert hm.size() == 10
    for i in range(10):
        assert hm.get(f"key{i}") == i


# --- task_13: DynamicArray (basic) ---

def test_task_13_append_and_get():
    DA = task_13()
    arr = DA()
    arr.append(10)
    arr.append(20)
    arr.append(30)
    assert arr.get(0) == 10
    assert arr.get(1) == 20
    assert arr.get(2) == 30

def test_task_13_size_and_capacity():
    DA = task_13()
    arr = DA()
    assert arr.size() == 0
    assert arr.capacity() == 2
    arr.append(1)
    arr.append(2)
    assert arr.size() == 2
    assert arr.capacity() == 2
    arr.append(3)
    assert arr.size() == 3
    assert arr.capacity() == 4

def test_task_13_set():
    DA = task_13()
    arr = DA()
    arr.append(1)
    arr.append(2)
    arr.set(1, 99)
    assert arr.get(1) == 99

def test_task_13_index_error():
    DA = task_13()
    arr = DA()
    with pytest.raises(IndexError, match="Index out of bounds"):
        arr.get(0)
    with pytest.raises(IndexError, match="Index out of bounds"):
        arr.set(0, 1)


# --- task_14: DynamicArray (extended) ---

def test_task_14_insert():
    DA = task_14()
    arr = DA()
    arr.append(1)
    arr.append(3)
    arr.insert(1, 2)
    assert arr.get(0) == 1
    assert arr.get(1) == 2
    assert arr.get(2) == 3

def test_task_14_insert_at_end():
    DA = task_14()
    arr = DA()
    arr.append(1)
    arr.insert(1, 2)
    assert arr.get(1) == 2

def test_task_14_delete():
    DA = task_14()
    arr = DA()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.delete(1)
    assert arr.get(0) == 1
    assert arr.get(1) == 3
    assert arr.size() == 2

def test_task_14_len():
    DA = task_14()
    arr = DA()
    assert len(arr) == 0
    arr.append(1)
    arr.append(2)
    assert len(arr) == 2

def test_task_14_getitem():
    DA = task_14()
    arr = DA()
    arr.append(10)
    arr.append(20)
    assert arr[0] == 10
    assert arr[1] == 20

def test_task_14_index_errors():
    DA = task_14()
    arr = DA()
    with pytest.raises(IndexError, match="Index out of bounds"):
        arr.insert(-1, 1)
    with pytest.raises(IndexError, match="Index out of bounds"):
        arr.delete(0)
    with pytest.raises(IndexError, match="Index out of bounds"):
        _ = arr[0]


# --- task_15: MinHeap ---

def test_task_15_insert_extract():
    MinHeap = task_15()
    h = MinHeap()
    h.insert(5)
    h.insert(3)
    h.insert(7)
    h.insert(1)
    assert h.extract_min() == 1
    assert h.extract_min() == 3
    assert h.extract_min() == 5
    assert h.extract_min() == 7

def test_task_15_peek():
    MinHeap = task_15()
    h = MinHeap()
    h.insert(10)
    h.insert(5)
    assert h.peek() == 5
    assert h.size() == 2

def test_task_15_empty_errors():
    MinHeap = task_15()
    h = MinHeap()
    with pytest.raises(IndexError, match="Heap is empty"):
        h.extract_min()
    with pytest.raises(IndexError, match="Heap is empty"):
        h.peek()


# --- task_16: MaxHeap ---

def test_task_16_insert_extract():
    MaxHeap = task_16()
    h = MaxHeap()
    h.insert(5)
    h.insert(3)
    h.insert(7)
    h.insert(1)
    assert h.extract_max() == 7
    assert h.extract_max() == 5
    assert h.extract_max() == 3
    assert h.extract_max() == 1

def test_task_16_peek():
    MaxHeap = task_16()
    h = MaxHeap()
    h.insert(10)
    h.insert(15)
    assert h.peek() == 15
    assert h.size() == 2

def test_task_16_empty_errors():
    MaxHeap = task_16()
    h = MaxHeap()
    with pytest.raises(IndexError, match="Heap is empty"):
        h.extract_max()
    with pytest.raises(IndexError, match="Heap is empty"):
        h.peek()


# --- task_17: heapify_min ---

def test_task_17_basic():
    heapify_min = task_17()
    arr = [5, 3, 8, 1, 2]
    result = heapify_min(arr)
    assert result is arr
    assert arr[0] == min(arr)

def test_task_17_valid_heap():
    heapify_min = task_17()
    arr = [9, 7, 5, 3, 1, 8, 6, 4, 2]
    heapify_min(arr)
    for i in range(len(arr)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr):
            assert arr[i] <= arr[left]
        if right < len(arr):
            assert arr[i] <= arr[right]

def test_task_17_empty():
    heapify_min = task_17()
    arr = []
    result = heapify_min(arr)
    assert result == []

def test_task_17_single():
    heapify_min = task_17()
    arr = [42]
    result = heapify_min(arr)
    assert result == [42]


# --- task_18: heapify_max ---

def test_task_18_basic():
    heapify_max = task_18()
    arr = [5, 3, 8, 1, 2]
    result = heapify_max(arr)
    assert result is arr
    assert arr[0] == max(arr)

def test_task_18_valid_heap():
    heapify_max = task_18()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    heapify_max(arr)
    for i in range(len(arr)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr):
            assert arr[i] >= arr[left]
        if right < len(arr):
            assert arr[i] >= arr[right]

def test_task_18_empty():
    heapify_max = task_18()
    arr = []
    result = heapify_max(arr)
    assert result == []


# --- task_19: heap_sort ---

def test_task_19_sort():
    heap_sort = task_19()
    assert heap_sort([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

def test_task_19_no_modify():
    heap_sort = task_19()
    original = [5, 3, 8, 1, 2]
    copy = list(original)
    heap_sort(original)
    assert original == copy

def test_task_19_empty():
    heap_sort = task_19()
    assert heap_sort([]) == []

def test_task_19_duplicates():
    heap_sort = task_19()
    assert heap_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

def test_task_19_sorted():
    heap_sort = task_19()
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
