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
    class Stack:
        def __init__(self):
            self._items = []

        def push(self, val):
            self._items.append(val)

        def pop(self):
            if self.is_empty():
                raise IndexError("Stack is empty")
            return self._items.pop()

        def peek(self):
            if self.is_empty():
                raise IndexError("Stack is empty")
            return self._items[-1]

        def is_empty(self):
            return len(self._items) == 0

        def size(self):
            return len(self._items)

    return Stack


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
    class MinStack:
        def __init__(self):
            self._items = []
            self._min_stack = []

        def push(self, val):
            self._items.append(val)
            if not self._min_stack or val <= self._min_stack[-1]:
                self._min_stack.append(val)

        def pop(self):
            if self.is_empty():
                raise IndexError("Stack is empty")
            val = self._items.pop()
            if val == self._min_stack[-1]:
                self._min_stack.pop()
            return val

        def peek(self):
            if self.is_empty():
                raise IndexError("Stack is empty")
            return self._items[-1]

        def get_min(self):
            if self.is_empty():
                raise IndexError("Stack is empty")
            return self._min_stack[-1]

        def is_empty(self):
            return len(self._items) == 0

        def size(self):
            return len(self._items)

    return MinStack


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
    class Queue:
        def __init__(self):
            self._items = []

        def enqueue(self, val):
            self._items.append(val)

        def dequeue(self):
            if self.is_empty():
                raise IndexError("Queue is empty")
            return self._items.pop(0)

        def peek(self):
            if self.is_empty():
                raise IndexError("Queue is empty")
            return self._items[0]

        def is_empty(self):
            return len(self._items) == 0

        def size(self):
            return len(self._items)

    return Queue


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
    class StackQueue:
        def __init__(self):
            self._in_stack = []
            self._out_stack = []

        def _transfer(self):
            if not self._out_stack:
                while self._in_stack:
                    self._out_stack.append(self._in_stack.pop())

        def enqueue(self, val):
            self._in_stack.append(val)

        def dequeue(self):
            if self.is_empty():
                raise IndexError("Queue is empty")
            self._transfer()
            return self._out_stack.pop()

        def peek(self):
            if self.is_empty():
                raise IndexError("Queue is empty")
            self._transfer()
            return self._out_stack[-1]

        def is_empty(self):
            return len(self._in_stack) == 0 and len(self._out_stack) == 0

        def size(self):
            return len(self._in_stack) + len(self._out_stack)

    return StackQueue


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
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    class SinglyLinkedList:
        def __init__(self):
            self.head = None

        def append(self, val):
            new_node = Node(val)
            if self.head is None:
                self.head = new_node
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        def prepend(self, val):
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

        def to_list(self):
            result = []
            current = self.head
            while current:
                result.append(current.val)
                current = current.next
            return result

    return (Node, SinglyLinkedList)


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
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    class SinglyLinkedList:
        def __init__(self):
            self.head = None

        def append(self, val):
            new_node = Node(val)
            if self.head is None:
                self.head = new_node
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        def prepend(self, val):
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

        def delete(self, val):
            if self.head is None:
                raise ValueError("Value not found")
            if self.head.val == val:
                self.head = self.head.next
                return
            current = self.head
            while current.next:
                if current.next.val == val:
                    current.next = current.next.next
                    return
                current = current.next
            raise ValueError("Value not found")

        def search(self, val):
            current = self.head
            while current:
                if current.val == val:
                    return True
                current = current.next
            return False

        def __len__(self):
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next
            return count

        def to_list(self):
            result = []
            current = self.head
            while current:
                result.append(current.val)
                current = current.next
            return result

    return (Node, SinglyLinkedList)


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
    class DoublyNode:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    class DoublyLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def append(self, val):
            new_node = DoublyNode(val)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                return
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        def prepend(self, val):
            new_node = DoublyNode(val)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                return
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        def to_list(self):
            result = []
            current = self.head
            while current:
                result.append(current.val)
                current = current.next
            return result

        def to_list_reverse(self):
            result = []
            current = self.tail
            while current:
                result.append(current.val)
                current = current.prev
            return result

    return (DoublyNode, DoublyLinkedList)


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
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    class BST:
        def __init__(self):
            self.root = None

        def insert(self, val):
            if self.root is None:
                self.root = TreeNode(val)
                return
            self._insert_recursive(self.root, val)

        def _insert_recursive(self, node, val):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    self._insert_recursive(node.left, val)
            elif val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    self._insert_recursive(node.right, val)

        def search(self, val):
            return self._search_recursive(self.root, val)

        def _search_recursive(self, node, val):
            if node is None:
                return False
            if val == node.val:
                return True
            elif val < node.val:
                return self._search_recursive(node.left, val)
            else:
                return self._search_recursive(node.right, val)

    return (TreeNode, BST)


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
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    class BST:
        def __init__(self):
            self.root = None

        def insert(self, val):
            if self.root is None:
                self.root = TreeNode(val)
                return
            self._insert_recursive(self.root, val)

        def _insert_recursive(self, node, val):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    self._insert_recursive(node.left, val)
            elif val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    self._insert_recursive(node.right, val)

        def in_order(self):
            result = []
            self._in_order_recursive(self.root, result)
            return result

        def _in_order_recursive(self, node, result):
            if node:
                self._in_order_recursive(node.left, result)
                result.append(node.val)
                self._in_order_recursive(node.right, result)

        def pre_order(self):
            result = []
            self._pre_order_recursive(self.root, result)
            return result

        def _pre_order_recursive(self, node, result):
            if node:
                result.append(node.val)
                self._pre_order_recursive(node.left, result)
                self._pre_order_recursive(node.right, result)

        def post_order(self):
            result = []
            self._post_order_recursive(self.root, result)
            return result

        def _post_order_recursive(self, node, result):
            if node:
                self._post_order_recursive(node.left, result)
                self._post_order_recursive(node.right, result)
                result.append(node.val)

    return (TreeNode, BST)


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
    from collections import deque

    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    class BST:
        def __init__(self):
            self.root = None

        def insert(self, val):
            if self.root is None:
                self.root = TreeNode(val)
                return
            self._insert_recursive(self.root, val)

        def _insert_recursive(self, node, val):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    self._insert_recursive(node.left, val)
            elif val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    self._insert_recursive(node.right, val)

        def bfs(self):
            if self.root is None:
                return []
            result = []
            queue = deque([self.root])
            while queue:
                node = queue.popleft()
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return result

    return (TreeNode, BST)


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
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    class BST:
        def __init__(self):
            self.root = None

        def insert(self, val):
            if self.root is None:
                self.root = TreeNode(val)
                return
            self._insert_recursive(self.root, val)

        def _insert_recursive(self, node, val):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    self._insert_recursive(node.left, val)
            elif val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    self._insert_recursive(node.right, val)

        def dfs(self):
            if self.root is None:
                return []
            result = []
            stack = [self.root]
            while stack:
                node = stack.pop()
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return result

    return (TreeNode, BST)


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
    class HashMap:
        def __init__(self, size=16):
            self._size = size
            self._buckets = [[] for _ in range(size)]

        def _hash(self, key):
            return hash(key) % self._size

        def put(self, key, value):
            index = self._hash(key)
            bucket = self._buckets[index]
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    return
            bucket.append((key, value))

        def get(self, key):
            index = self._hash(key)
            bucket = self._buckets[index]
            for k, v in bucket:
                if k == key:
                    return v
            raise KeyError(key)

        def remove(self, key):
            index = self._hash(key)
            bucket = self._buckets[index]
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    return
            raise KeyError(key)

        def contains(self, key):
            index = self._hash(key)
            bucket = self._buckets[index]
            for k, v in bucket:
                if k == key:
                    return True
            return False

    return HashMap


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
    class HashMap:
        def __init__(self, initial_size=8):
            self._buckets = [[] for _ in range(initial_size)]
            self._count = 0

        def _hash(self, key):
            return hash(key) % len(self._buckets)

        def put(self, key, value):
            index = self._hash(key)
            bucket = self._buckets[index]
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    return
            bucket.append((key, value))
            self._count += 1
            if self._count / len(self._buckets) > 0.75:
                self._resize()

        def _resize(self):
            old_buckets = self._buckets
            new_size = len(self._buckets) * 2
            self._buckets = [[] for _ in range(new_size)]
            self._count = 0
            for bucket in old_buckets:
                for key, value in bucket:
                    self.put(key, value)

        def get(self, key):
            index = self._hash(key)
            bucket = self._buckets[index]
            for k, v in bucket:
                if k == key:
                    return v
            raise KeyError(key)

        def remove(self, key):
            index = self._hash(key)
            bucket = self._buckets[index]
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    self._count -= 1
                    return
            raise KeyError(key)

        def contains(self, key):
            index = self._hash(key)
            bucket = self._buckets[index]
            for k, v in bucket:
                if k == key:
                    return True
            return False

        def keys(self):
            result = []
            for bucket in self._buckets:
                for k, v in bucket:
                    result.append(k)
            return result

        def values(self):
            result = []
            for bucket in self._buckets:
                for k, v in bucket:
                    result.append(v)
            return result

        def size(self):
            return self._count

    return HashMap


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
    class DynamicArray:
        def __init__(self):
            self._capacity = 2
            self._data = [None] * self._capacity
            self._count = 0

        def _resize(self):
            self._capacity *= 2
            new_data = [None] * self._capacity
            for i in range(self._count):
                new_data[i] = self._data[i]
            self._data = new_data

        def append(self, val):
            if self._count == self._capacity:
                self._resize()
            self._data[self._count] = val
            self._count += 1

        def get(self, index):
            if index < 0 or index >= self._count:
                raise IndexError("Index out of bounds")
            return self._data[index]

        def set(self, index, val):
            if index < 0 or index >= self._count:
                raise IndexError("Index out of bounds")
            self._data[index] = val

        def size(self):
            return self._count

        def capacity(self):
            return self._capacity

    return DynamicArray


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
    class DynamicArray:
        def __init__(self):
            self._capacity = 2
            self._data = [None] * self._capacity
            self._count = 0

        def _resize(self):
            self._capacity *= 2
            new_data = [None] * self._capacity
            for i in range(self._count):
                new_data[i] = self._data[i]
            self._data = new_data

        def append(self, val):
            if self._count == self._capacity:
                self._resize()
            self._data[self._count] = val
            self._count += 1

        def get(self, index):
            if index < 0 or index >= self._count:
                raise IndexError("Index out of bounds")
            return self._data[index]

        def set(self, index, val):
            if index < 0 or index >= self._count:
                raise IndexError("Index out of bounds")
            self._data[index] = val

        def size(self):
            return self._count

        def capacity(self):
            return self._capacity

        def insert(self, index, val):
            if index < 0 or index > self._count:
                raise IndexError("Index out of bounds")
            if self._count == self._capacity:
                self._resize()
            for i in range(self._count, index, -1):
                self._data[i] = self._data[i - 1]
            self._data[index] = val
            self._count += 1

        def delete(self, index):
            if index < 0 or index >= self._count:
                raise IndexError("Index out of bounds")
            for i in range(index, self._count - 1):
                self._data[i] = self._data[i + 1]
            self._data[self._count - 1] = None
            self._count -= 1

        def __len__(self):
            return self._count

        def __getitem__(self, index):
            if index < 0 or index >= self._count:
                raise IndexError("Index out of bounds")
            return self._data[index]

    return DynamicArray


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

        Return the class itself.
    """
    class MinHeap:
        def __init__(self):
            self._data = []

        def insert(self, val):
            self._data.append(val)
            self._bubble_up(len(self._data) - 1)

        def _bubble_up(self, index):
            while index > 0:
                parent = (index - 1) // 2
                if self._data[index] < self._data[parent]:
                    self._data[index], self._data[parent] = self._data[parent], self._data[index]
                    index = parent
                else:
                    break

        def extract_min(self):
            if not self._data:
                raise IndexError("Heap is empty")
            if len(self._data) == 1:
                return self._data.pop()
            min_val = self._data[0]
            self._data[0] = self._data.pop()
            self._sift_down(0)
            return min_val

        def _sift_down(self, index):
            size = len(self._data)
            while True:
                smallest = index
                left = 2 * index + 1
                right = 2 * index + 2
                if left < size and self._data[left] < self._data[smallest]:
                    smallest = left
                if right < size and self._data[right] < self._data[smallest]:
                    smallest = right
                if smallest != index:
                    self._data[index], self._data[smallest] = self._data[smallest], self._data[index]
                    index = smallest
                else:
                    break

        def peek(self):
            if not self._data:
                raise IndexError("Heap is empty")
            return self._data[0]

        def size(self):
            return len(self._data)

    return MinHeap


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

        Return the class itself.
    """
    class MaxHeap:
        def __init__(self):
            self._data = []

        def insert(self, val):
            self._data.append(val)
            self._bubble_up(len(self._data) - 1)

        def _bubble_up(self, index):
            while index > 0:
                parent = (index - 1) // 2
                if self._data[index] > self._data[parent]:
                    self._data[index], self._data[parent] = self._data[parent], self._data[index]
                    index = parent
                else:
                    break

        def extract_max(self):
            if not self._data:
                raise IndexError("Heap is empty")
            if len(self._data) == 1:
                return self._data.pop()
            max_val = self._data[0]
            self._data[0] = self._data.pop()
            self._sift_down(0)
            return max_val

        def _sift_down(self, index):
            size = len(self._data)
            while True:
                largest = index
                left = 2 * index + 1
                right = 2 * index + 2
                if left < size and self._data[left] > self._data[largest]:
                    largest = left
                if right < size and self._data[right] > self._data[largest]:
                    largest = right
                if largest != index:
                    self._data[index], self._data[largest] = self._data[largest], self._data[index]
                    index = largest
                else:
                    break

        def peek(self):
            if not self._data:
                raise IndexError("Heap is empty")
            return self._data[0]

        def size(self):
            return len(self._data)

    return MaxHeap


def task_17():
    """
        Define a function called heapify_min(arr) that:
        - Takes a list and rearranges it in-place into a valid min-heap
        - Returns the modified list
        - Uses the sift-down approach starting from the last non-leaf node

        Return the function itself.
    """
    def heapify_min(arr):
        def sift_down(arr, n, i):
            while True:
                smallest = i
                left = 2 * i + 1
                right = 2 * i + 2
                if left < n and arr[left] < arr[smallest]:
                    smallest = left
                if right < n and arr[right] < arr[smallest]:
                    smallest = right
                if smallest != i:
                    arr[i], arr[smallest] = arr[smallest], arr[i]
                    i = smallest
                else:
                    break

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            sift_down(arr, n, i)
        return arr

    return heapify_min


def task_18():
    """
        Define a function called heapify_max(arr) that:
        - Takes a list and rearranges it in-place into a valid max-heap
        - Returns the modified list
        - Uses the sift-down approach starting from the last non-leaf node

        Return the function itself.
    """
    def heapify_max(arr):
        def sift_down(arr, n, i):
            while True:
                largest = i
                left = 2 * i + 1
                right = 2 * i + 2
                if left < n and arr[left] > arr[largest]:
                    largest = left
                if right < n and arr[right] > arr[largest]:
                    largest = right
                if largest != i:
                    arr[i], arr[largest] = arr[largest], arr[i]
                    i = largest
                else:
                    break

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            sift_down(arr, n, i)
        return arr

    return heapify_max


def task_19():
    """
        Define a function called heap_sort(arr) that:
        - Takes a list and returns a new list sorted in ascending order
        - Uses a heap-based approach: build a min-heap, then extract elements one by one
        - Does NOT modify the original list

        Return the function itself.
    """
    def heap_sort(arr):
        data = list(arr)

        def sift_down(data, n, i):
            while True:
                smallest = i
                left = 2 * i + 1
                right = 2 * i + 2
                if left < n and data[left] < data[smallest]:
                    smallest = left
                if right < n and data[right] < data[smallest]:
                    smallest = right
                if smallest != i:
                    data[i], data[smallest] = data[smallest], data[i]
                    i = smallest
                else:
                    break

        n = len(data)
        for i in range(n // 2 - 1, -1, -1):
            sift_down(data, n, i)

        result = []
        for _ in range(n):
            result.append(data[0])
            data[0] = data[len(data) - 1]
            data.pop()
            if data:
                sift_down(data, len(data), 0)

        return result

    return heap_sort
