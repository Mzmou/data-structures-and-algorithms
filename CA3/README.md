
# Advanced Data Structures and Algorithmic Challenges

---

## Table of Contents
1. [Heap Problems](#heap-problems)
2. [Huffman Tree Problems](#huffman-tree-problems)
3. [Binary Search Tree (BST) Problems](#binary-search-tree-bst-problems)
4. [Special Challenges](#special-challenges)

---

## Heap Problems

### Problem Description
Work with `min_heap` and perform the following operations:
1. **Heapify**: Initialize the heap with given values.
2. **Find Minimum Child**: Retrieve the smallest child of a given node.
3. **Pop**: Remove the smallest element from the heap.

### Input Format
- Create a `min_heap` object:
  ```
  make min_heap <heap_name>
  ```
- Perform operations:
  ```
  call <heap_name>.heapify(values)
  call <heap_name>.find_min_child(index)
  call <heap_name>.heap_pop()
  ```

### Example
#### Input:
```
make min_heap m1
call m1.heapify(10,5,30,50)
call m1.find_min_child(0)
call m1.heap_pop()
call m1.find_min_child(1)
```
#### Output:
```
1
5
10
out of range index
```

---

## Huffman Tree Problems

### Problem Description
Implement and test functions for Huffman Tree construction and usage:
1. **Set Letters and Repetitions**: Define the characters and their frequencies.
2. **Build Tree**: Construct the Huffman Tree.
3. **Calculate Encoding Cost**: Get the cost of encoding a text using the tree.
4. **Text Encoding**: Encode a given text using the Huffman Tree.

### Input Format
- Create a `huffman_tree` object:
  ```
  make huffman_tree <tree_name>
  ```
- Perform operations:
  ```
  call <tree_name>.set_letters(characters)
  call <tree_name>.set_repetitions(frequencies)
  call <tree_name>.build_huffman_tree()
  call <tree_name>.text_encoding(text)
  ```

### Example
#### Input:
```
make huffman_tree h1
call h1.set_letters('a','b','c','d')
call h1.set_repetitions(1,3,5,7)
call h1.build_huffman_tree()
call h1.get_huffman_code_cost()
```
#### Output:
```
1139
```

---

## Binary Search Tree (BST) Problems

### Problem Description
Perform operations on a BST:
1. **Insertion**: Insert values while maintaining BST properties.
2. **Traversal**: Perform in-order traversal of the tree.
3. **Find Common Ancestor**: Determine the first common ancestor of two nodes.

### Input Format
- Create a `bst` object:
  ```
  make bst <tree_name>
  ```
- Perform operations:
  ```
  call <tree_name>.insert(value)
  call <tree_name>.inorder()
  call <tree_name>.find_common_ancestor(node_a, node_b)
  ```

### Example
#### Input:
```
make bst b1
call b1.insert(50)
call b1.insert(30)
call b1.insert(70)
call b1.inorder()
```
#### Output:
```
30 50 70
```

---

### First Common Ancestor in BST and Parent Output

**Problem**:  
Given a sequence of numbers inserted into a BST, determine:  
1. The parent of each node during insertion (for nodes 2 to \( n \)).  
2. The first common ancestor of two specified nodes \( a \) and \( b \) (given as their order of insertion).  

#### Input Format:
1. Line 1: Integer \( n \), the number of nodes to be inserted.  
2. Line 2: Sequence of \( n \) integers representing the insertion order into the BST.  
3. Line 3: Two integers \( a \) and \( b \), representing the \( a \)-th and \( b \)-th inserted nodes.

#### Output Format:
1. \( n - 1 \) integers, where the \( i \)-th value is the parent of the \( i+1 \)-th node during insertion.  
2. The number of the first common ancestor of \( a \)-th and \( b \)-th nodes.

#### Example:
Input:
```
5
3 1 5 4 5
2 3
```
Output:
```
3 3 5 5
1
```

---

## Special Challenges

### 1. **Tree Coin Game**
**Problem**: Given a tree structure where each node contains a coin, calculate the minimum steps to flip all coins to a specific state.

#### Input Format:
- Line 1: Number of nodes \( n \) and queries \( q \).
- Line 2: Parent list for the tree.
- Next \( q \) lines: Sets of nodes in a specific state.

#### Example:
Input:
```
5 2
1 1 3 2
1 5
2 3 5
```
Output:
```
1
3
```

### 2. **Anger Minimization**
**Problem**: Optimize a schedule to minimize the anger of teachers based on their availability and requirements.

#### Input Format:
- Line 1: Number of days \( d \) and teachers \( n \).
- Next \( n \) lines: Availability, required days, and anger coefficient.

#### Example:
Input:
```
2 3
1 2 300
2 2 100
```
Output:
```
100
```

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Run the script:
   ```bash
   python <script_name>.py
   ```

---
## Repository Structure
- Each problem has a dedicated file with its solution implemented in Python.
- Example:
  - `Warm-Up Exercise.py`
  - `Find Common Ancestor.py`
  - `Tree Coin Game.py`
  - `Anger Minimization.py`

---
This repository contains Python implementations for all problems. Each file is well-commented and includes test cases for better understanding. Happy coding! 😊
