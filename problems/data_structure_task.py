from typing import List, Optional, Any, Tuple


# --- task_0 through task_1: Stack ---

def task_0():
    """
        Define a class called Stack with:
        - __init__ that initializes an empty list as internal storage
        - push(val) that adds val to the top of the stack
        - pop() that removes and returns the top element; raises IndexError("Stack is empty") if empty
        - peek() that returns the top element without removing it; raises IndexError("Stack is empty") if empty
        - is_empty() that returns True if the stack has no elements
        - size() that returns the number of elements
        Return the class itself.
    """
    pass


def task_1():
    """
        Define a class called MinStack with:
        - __init__ that initializes internal storage for values and for tracking minimums
        - push(val) that adds val to the stack and updates the minimum tracking
        - pop() that removes and returns the top element (and updates min tracking);
          raises IndexError("Stack is empty") if empty
        - peek() that returns the top element without removing it;
          raises IndexError("Stack is empty") if empty
        - get_min() that returns the current minimum element in O(1) time;
          raises IndexError("Stack is empty") if empty
        - is_empty() that returns True if the stack has no elements
        - size() that returns the number of elements
        Return the class itself.
    """
    pass


# --- task_2 through task_3: Queue ---

def task_2():
    """
        Define a class called Queue with:
        - __init__ that initializes an empty list as internal storage
        - enqueue(val) that adds val to the back of the queue
        - dequeue() that removes and returns the front element; raises IndexError("Queue is empty") if empty
        - peek() that returns the front element without removing it; raises IndexError("Queue is empty") if empty
        - is_empty() that returns True if the queue has no elements
        - size() that returns the number of elements
        Return the class itself.
    """
    pass


def task_3():
    """
        Define a class called StackQueue that implements a queue using two stacks (lists).
        It must have the same interface as the Queue in task_2:
        - __init__ that initializes two empty lists (in_stack and out_stack)
        - enqueue(val) that adds val to in_stack
        - dequeue() that removes and returns the front element using the two-stack approach;
          raises IndexError("Queue is empty") if empty
        - peek() that returns the front element without removing it;
          raises IndexError("Queue is empty") if empty
        - is_empty() that returns True if both stacks are empty
        - size() that returns the total number of elements across both stacks
        Return the class itself.
    """
    pass


# --- task_4 through task_6: Linked List ---

def task_4():
    """
        Define a class Node with:
        - __init__ that takes val and sets self.val = val, self.next = None

        Define a class SinglyLinkedList with:
        - __init__ that sets self.head = None
        - append(val) that adds a new node with val at the end
        - prepend(val) that adds a new node with val at the beginning
        - to_list() that returns a Python list of all values from head to tail

        Return a tuple (Node, SinglyLinkedList).
    """
    pass


def task_5():
    """
        Define a class Node with:
        - __init__ that takes val and sets self.val = val, self.next = None

        Define a class SinglyLinkedList with:
        - __init__ that sets self.head = None
        - append(val) that adds a new node with val at the end
        - prepend(val) that adds a new node with val at the beginning
        - delete(val) that removes the first node with the given val;
          raises ValueError("Value not found") if val is not in the list
        - search(val) that returns True if val exists in the list, False otherwise
        - __len__() that returns the number of nodes
        - to_list() that returns a Python list of all values from head to tail

        Return a tuple (Node, SinglyLinkedList).
    """
    pass


def task_6():
    """
        Define a class DoublyNode with:
        - __init__ that takes val and sets self.val = val, self.prev = None, self.next = None

        Define a class DoublyLinkedList with:
        - __init__ that sets self.head = None and self.tail = None
        - append(val) that adds a new node at the end
        - prepend(val) that adds a new node at the beginning
        - to_list() that returns a Python list of all values from head to tail
        - to_list_reverse() that returns a Python list of all values from tail to head

        Return a tuple (DoublyNode, DoublyLinkedList).
    """
    pass


# --- task_7 through task_10: Binary Search Tree ---

def task_7():
    """
        Define a class TreeNode with:
        - __init__ that takes val and sets self.val = val, self.left = None, self.right = None

        Define a class BST with:
        - __init__ that sets self.root = None
        - insert(val) that inserts a value into the BST (no duplicates — ignore if already present)
        - search(val) that returns True if val exists in the BST, False otherwise

        Return a tuple (TreeNode, BST).
    """
    pass


def task_8():
    """
        Define a class TreeNode with:
        - __init__ that takes val and sets self.val = val, self.left = None, self.right = None

        Define a class BST with:
        - __init__ that sets self.root = None
        - insert(val) that inserts a value into the BST (no duplicates)
        - in_order() that returns a list of values in in-order traversal (left, root, right)
        - pre_order() that returns a list of values in pre-order traversal (root, left, right)
        - post_order() that returns a list of values in post-order traversal (left, right, root)

        Return a tuple (TreeNode, BST).
    """
    pass


def task_9():
    """
        Define a class TreeNode with:
        - __init__ that takes val and sets self.val = val, self.left = None, self.right = None

        Define a class BST with:
        - __init__ that sets self.root = None
        - insert(val) that inserts a value into the BST (no duplicates)
        - bfs() that returns a list of values in level-order (breadth-first) traversal
          Use a queue (collections.deque or list) internally.

        Return a tuple (TreeNode, BST).
    """
    pass


def task_10():
    """
        Define a class TreeNode with:
        - __init__ that takes val and sets self.val = val, self.left = None, self.right = None

        Define a class BST with:
        - __init__ that sets self.root = None
        - insert(val) that inserts a value into the BST (no duplicates)
        - dfs() that returns a list of values in depth-first traversal (pre-order)
          using an explicit stack (not recursion).

        Return a tuple (TreeNode, BST).
    """
    pass


# --- task_11 through task_12: HashMap ---

def task_11():
    """
        Define a class called HashMap with:
        - __init__ that takes an optional size parameter (default 16) and creates
          a list of empty lists (buckets) of that size
        - _hash(key) that returns an index for the given key using hash(key) % size
        - put(key, value) that stores a key-value pair; updates value if key exists
        - get(key) that returns the value for a key; raises KeyError(key) if not found
        - remove(key) that removes a key-value pair; raises KeyError(key) if not found
        - contains(key) that returns True if the key exists, False otherwise

        Return the class itself.
    """
    pass


def task_12():
    """
        Define a class called HashMap with:
        - __init__ that takes an optional initial_size parameter (default 8) and creates
          a list of empty lists (buckets) of that size; tracks the count of stored pairs
        - _hash(key) that returns an index for the given key using hash(key) % len(buckets)
        - put(key, value) that stores a key-value pair; updates value if key exists;
          if the load factor (count / len(buckets)) exceeds 0.75 after insertion, resize
          the bucket array to double its current length and rehash all entries
        - get(key) that returns the value for a key; raises KeyError(key) if not found
        - remove(key) that removes a key-value pair; raises KeyError(key) if not found
        - contains(key) that returns True if the key exists, False otherwise
        - keys() that returns a list of all keys
        - values() that returns a list of all values
        - size() that returns the number of stored key-value pairs

        Return the class itself.
    """
    pass


# --- task_13 through task_14: Dynamic Array ---

def task_13():
    """
        Define a class called DynamicArray with:
        - __init__ that initializes with capacity 2, an internal fixed-size list
          (e.g. [None, None]), and a count of 0
        - append(val) that adds val at the end; if count == capacity, double the capacity
          by creating a new internal list and copying elements over
        - get(index) that returns the element at index; raises IndexError("Index out of bounds")
          if index < 0 or index >= count
        - set(index, val) that sets the element at index to val; raises IndexError("Index out of bounds")
          if index < 0 or index >= count
        - size() that returns the number of elements (count)
        - capacity() that returns the current capacity

        Return the class itself.
    """
    pass


def task_14():
    """
        Define a class called DynamicArray with:
        - All methods from task_13 (append, get, set, size, capacity with the same behavior)
        - insert(index, val) that inserts val at the given index, shifting subsequent elements right;
          raises IndexError("Index out of bounds") if index < 0 or index > count
          (note: inserting at index == count is allowed, like append)
          If count == capacity before inserting, double the capacity first.
        - delete(index) that removes the element at index, shifting subsequent elements left;
          raises IndexError("Index out of bounds") if index < 0 or index >= count
        - __len__() that returns the number of elements
        - __getitem__(index) that returns the element at index; raises IndexError("Index out of bounds")
          if index < 0 or index >= count

        Return the class itself.
    """
    pass


# --- task_15 through task_19: Heap ---

def task_15():
    """
        Define a class called MinHeap with:
        - __init__ that initializes an empty list as internal storage
        - insert(val) that adds val and bubbles it up to maintain the min-heap property
        - extract_min() that removes and returns the minimum element (root);
          raises IndexError("Heap is empty") if empty
        - peek() that returns the minimum element without removing it;
          raises IndexError("Heap is empty") if empty
        - size() that returns the number of elements

        The heap should be array-based where for index i:
        - parent is at (i - 1) // 2
        - left child is at 2 * i + 1
        - right child is at 2 * i + 2

        Return the class itself.
    """
    pass


def task_16():
    """
        Define a class called MaxHeap with:
        - __init__ that initializes an empty list as internal storage
        - insert(val) that adds val and bubbles it up to maintain the max-heap property
        - extract_max() that removes and returns the maximum element (root);
          raises IndexError("Heap is empty") if empty
        - peek() that returns the maximum element without removing it;
          raises IndexError("Heap is empty") if empty
        - size() that returns the number of elements

        The heap should be array-based where for index i:
        - parent is at (i - 1) // 2
        - left child is at 2 * i + 1
        - right child is at 2 * i + 2

        Return the class itself.
    """
    pass


def task_17():
    """
        Define a function called heapify_min(arr) that:
        - Takes a list and rearranges it in-place into a valid min-heap
        - Returns the modified list
        - Uses the sift-down approach starting from the last non-leaf node

        Return the function itself.
    """
    pass


def task_18():
    """
        Define a function called heapify_max(arr) that:
        - Takes a list and rearranges it in-place into a valid max-heap
        - Returns the modified list
        - Uses the sift-down approach starting from the last non-leaf node

        Return the function itself.
    """
    pass


def task_19():
    """
        Define a function called heap_sort(arr) that:
        - Takes a list and returns a new list sorted in ascending order
        - Uses a heap-based approach: build a min-heap, then extract elements one by one
        - Does NOT modify the original list

        Return the function itself.
    """
    pass
