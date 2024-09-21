# Data Structures and Algorithms in Python

This repository contains Python implementations of various data structures and algorithms. Each implementation is accompanied by a detailed explanation of the underlying concepts, operations, and performance characteristics.

## Table of Contents

1. [Data Structures](#data-structures)
   - [Adjacency Matrix](#adjacency-matrix)
   - [Adjacency List](#adjacency-list)
   - [Binary Search Tree](#binary-search-tree)
   - [Deque (Double Linked List)](#deque-double-linked-list)
   - [Deque (List)](#deque-list)
   - [Linked Lists](#linked-lists)
   - [Heap](#heap)
   - [Queue](#queue)
   - [Stack](#stack)
   - [Priority Queue](#priority-queue)
2. [Sorting Algorithms](#sorting-algorithms)
   - [Insertion Sort](#insertion-sort)
   - [Merge Sort](#merge-sort)
   - [Quick Sort](#quick-sort)
   - [Selection Sort](#selection-sort)
   - [Bubble Sort](#bubble-sort)
   - [Heap Sort](#heap-sort)
3. [Recursion](#recursion)

---

## Data Structures

### Adjacency Matrix
- **File**: `Adjacency_Matrix_Implementation.py`
- **Description**: An adjacency matrix is a 2D array used to represent a graph. Each element in the matrix indicates whether there is an edge between the corresponding nodes. A value of `1` means there is an edge, while `0` means no edge.
- **Operations**:
  - **Space Complexity**: O(V²), where V is the number of vertices. This can be inefficient for sparse graphs.
  - **Time Complexity**: Checking if an edge exists between two vertices is O(1), but traversing all edges takes O(V²).
- **Use Case**: Suitable for dense graphs where most nodes are connected.

### Adjacency List
- **File**: `Adjacency_list_implementation.py`
- **Description**: An adjacency list is an efficient way to represent a graph. Each node stores a list of its adjacent nodes (neighbors). It saves space when representing sparse graphs.
- **Operations**:
  - **Space Complexity**: O(V + E), where V is the number of vertices and E is the number of edges.
  - **Time Complexity**: Checking for an edge between two nodes takes O(V), but traversal is O(E).
- **Use Case**: Ideal for sparse graphs with fewer connections between vertices.

### Binary Search Tree
- **Files**: `Binary_search_tree.py`, `Delation_in_Binary_Search_Tree.py`
- **Description**: A Binary Search Tree (BST) is a hierarchical data structure where each node has at most two children. The left child is smaller, and the right child is larger than the parent node.
- **Operations**:
  - **Insertion**: O(log n) on average, but can be O(n) if the tree is unbalanced.
  - **Deletion**: O(log n) on average.
  - **Traversal**: O(n) for in-order traversal, which prints nodes in a sorted order.
- **Use Case**: BST is efficient for search, insertion, and deletion when balanced, often used in search engines and databases.

### Deque (Double Linked List)
- **File**: `Deque_using_double_link_list.py`
- **Description**: A Deque (Double-Ended Queue) is a linear data structure that allows insertion and deletion at both ends (front and rear). This implementation uses a doubly linked list, where each node points to both its previous and next nodes.
- **Operations**:
  - **Insertion/Deletion at both ends**: O(1).
  - **Accessing elements**: O(n).
- **Use Case**: Useful in applications requiring dynamic resizing and fast access to both ends, such as sliding window problems.

### Deque (List)
- **File**: `Deque_using_list.py`
- **Description**: A simple Deque implemented using a Python list, allowing insertion and deletion from both ends.
- **Operations**:
  - **Insertion/Deletion at front or rear**: O(1) at the end but O(n) at the front, as shifting elements is required.
- **Use Case**: Suitable for smaller data sets where a simpler implementation is sufficient.

### Linked Lists
- **Files**: 
  - `Single_Link_List.py` - Singly Linked List
  - `Double_link_list.py` - Doubly Linked List
  - `circular_link_list.py` - Circular Linked List
  - `Double_circular_link_list.py` - Doubly Circular Linked List
- **Description**: A linked list is a linear data structure where each element (node) points to the next one. In singly linked lists, each node points to the next node only, while in doubly linked lists, nodes point both to the next and previous nodes.
- **Operations**:
  - **Insertion/Deletion**: O(1) when at the head or tail, O(n) otherwise.
  - **Traversal**: O(n).
- **Use Case**: Useful for dynamic memory allocation and for implementing stacks, queues, and other dynamic structures.

### Heap
- **File**: `Heep.py`
- **Description**: A max heap is a complete binary tree where the parent node is always greater than its children. It is commonly used to implement priority queues.
- **Operations**:
  - **Insertion**: O(log n).
  - **Deletion (extract max)**: O(log n).
  - **Heapify**: O(n) to create a heap from an unordered array.
- **Use Case**: Efficient for priority scheduling, such as in task scheduling or Dijkstra’s algorithm for shortest paths.

### Queue
- **Files**: 
  - `Queue_using_list.py` - Queue using List
  - `Queue_using_single_link_list.py` - Queue using Singly Linked List
- **Description**: A queue is a First-In-First-Out (FIFO) data structure where the first element to be inserted is the first to be removed.
- **Operations**:
  - **Enqueue (insert)**: O(1).
  - **Dequeue (remove)**: O(1).
- **Use Case**: Queues are used in task scheduling, buffering, and breadth-first search (BFS) algorithms.

### Stack
- **Files**: 
  - `Stack_using_list.py`
  - `Stack_using_single_link_list.py`
  - `Stack_using_inheriting_link_list.py`
- **Description**: A stack is a Last-In-First-Out (LIFO) data structure where the last inserted element is the first to be removed.
- **Operations**:
  - **Push (insert)**: O(1).
  - **Pop (remove)**: O(1).
- **Use Case**: Stacks are used in function call management, depth-first search (DFS), and expression evaluation.

### Priority Queue
- **Files**: 
  - `priority_queue_using_list.py`
  - `priority_queue_using_link_list.py`
- **Description**: A priority queue is a data structure where each element is associated with a priority, and the element with the highest priority is served first.
- **Operations**:
  - **Insertion**: O(n) for unsorted lists, O(log n) for heaps.
  - **Deletion**: O(1) for sorted lists.
- **Use Case**: Used in Dijkstra’s algorithm, task scheduling, and resource management.

---

## Sorting Algorithms

### Insertion Sort
- **Files**: `Insersion_sort_using_alg.py`, `Insertion_sort.py`
- **Description**: Insertion sort builds a sorted list one element at a time, placing each new element into its correct position.
- **Time Complexity**: O(n²) in worst case, O(n) in best case (already sorted).
- **Use Case**: Good for small datasets or nearly sorted data.

### Merge Sort
- **File**: `Merge_sort_alg.py`
- **Description**: Merge sort is a divide-and-conquer algorithm that divides the array into halves, sorts them recursively, and then merges the sorted halves.
- **Time Complexity**: O(n log n).
- **Use Case**: Efficient for large datasets and can be used for external sorting.

### Quick Sort
- **File**: `Quick_sort.py`
- **Description**: Quick sort is an efficient in-place sorting algorithm that uses a pivot to partition the array and recursively sort the partitions.
- **Time Complexity**: O(n log n) on average, but O(n²) in the worst case (when the pivot is poorly chosen).
- **Use Case**: Often the go-to sorting algorithm for practical purposes due to its speed and in-place nature.

### Selection Sort
- **File**: `Sorting_uisng_selection_sort.py`
- **Description**: Selection sort repeatedly selects the minimum element from the unsorted portion and places it in its correct position.
- **Time Complexity**: O(n²).
- **Use Case**: Rarely used in practice but useful when memory writes are expensive.

### Bubble Sort
- **File**: `Sorting_using_Bubble_sort.py`
- **Description**: Bubble sort repeatedly swaps adjacent elements if they are in the wrong order, "bubbling" the largest element to the end in each pass.
- **Time Complexity**: O(n²).
- **Use Case**: Mostly used for educational purposes, inefficient for large datasets.

### Heap Sort
- **File**: `Heep_sort_using_alg.py`
- **Description**: Heap sort is a comparison-based sorting algorithm that builds a heap and repeatedly extracts the maximum element to build the sorted array.
- **Time Complexity**: O(n log n).
- **Use Case**: Useful for implementing priority queues and scheduling algorithms.

---

## Recursion

- **Files**: 
  - `recursion.py`
- **Description**: Recursion is a technique where a function calls itself to solve smaller instances of a problem until it reaches a base case.
- **Use Case**: Commonly used in divide-and-conquer algorithms like merge sort, quick sort, and tree traversals.
