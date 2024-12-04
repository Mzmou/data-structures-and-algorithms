# STACK,QUEUE and heap Problems



---

## Table of Contents
1. [Warm-Up Exercise](#warm-up-exercise)
2. [Michelangelo's Number](michelangelo-'s-Number)
3. [Donatello's Painting](#donatello-'s-painting)
4. [Leonardo’s Message](#leonardo-’s-message)

---

# Problem Descriptions

## Warm-Up Exercise

### Problem Statement
You are provided with partially implemented classes for common data structures like Stack, Queue, and Linked List. Your task is to complete the missing functions based on the specifications outlined in the provided template.

### Input Format
- Commands to create objects, such as:
  - `make queue q1` to create a Queue object named `q1`.
  - `make stack s1` to create a Stack object named `s1`.
- A series of function calls on the created objects, for example:
  - `call q1.enqueue(1)` or `call s1.push(2)`.

### Output Format
The output will consist of the results of the respective function calls on the data structure.

### Example
#### Input:
```
make queue q1
call q1.enqueue(1)
call q1.enqueue(2)
call q1.isEmpty()
call q1.getSize()
call q1.getInOneLine()
```
#### Output:
```
False
2
1 2
```

---

## Michelangelo's Number

### Problem Statement
Raphael is guessing a number \( x + 0.5 \), where \( x \) is an integer between \( 0 \) and \( N \). Using a predefined permutation, Raphael queries Michelangelo with integer values \( y \) and gets responses "greater" ("بز") or "smaller" ("کو"). Count how many times the phrase "بزکو" (greater followed by smaller) appears in the query-response sequence for each \( x \).

### Input Format
- Line 1: Integer \( N \) (1 ≤ \( N \) ≤ \( 200,000 \)).
- Line 2: A permutation of integers from \( 1 \) to \( N \).

### Output Format
Print \( N+1 \) integers. Each integer represents the count of "بزکو" occurrences for \( x = 0 \) to \( x = N \).

### Example
#### Input:
```
5
5 1 2 4 3
```
#### Output:
```
0
1
1
2
1
0
```

---

## Donatello's Painting

### Problem Statement
Donatello wants to paint a canvas with \( n \) cells. Each cell can only have one color, and he can paint at most one contiguous segment of a color per step. Determine the minimum time (in minutes) required to complete the painting or if it's not possible.

### Input Format
- Line 1: Integer \( n \) (1 ≤ \( n \) ≤ \( 100,000 \)).
- Next \( n \) lines: Integers representing the color of each cell (0 represents uncolored cells).

### Output Format
Print a single integer representing the minimum time required or `-1` if painting is not possible.

### Example
#### Input:
```
7
0
1
4
5
1
3
3
```
#### Output:
```
2
```

---

## Leonardo’s Message

### Problem Statement
Leonardo needs to deliver a message to Master Splinter by traversing a pipeline. The pipeline has constraints:
1. Each step must avoid sections with water levels exceeding the shoes' resistance.
2. Each shoe has a maximum range (number of positions Leonardo can step forward).

Determine which of Leonardo's shoes can be used to traverse the entire pipeline.

### Input Format
- Line 1: Two integers \( N \) (number of pipeline positions) and \( B \) (number of shoes) (1 ≤ \( N, B \) ≤ \( 100,000 \)).
- Line 2: \( N \) integers representing the water level \( f_i \) at each position.
- Next \( B \) lines: Each line contains two integers:
  - \( p_i \): Maximum water resistance of the shoe.
  - \( s_i \): Maximum step range of the shoe.

### Output Format
Print \( B \) lines. Each line contains `1` if the shoe can be used to traverse the pipeline and `0` otherwise.

### Example
#### Input:
```
8 7
0 3 8 5 6 9 0 0
0 5
0 6
6 2
8 1
10 1
5 3
150 7
```
#### Output:
```
0
1
1
0
1
1
1
```

---
## Repository Structure
- Each problem has a dedicated file with its solution implemented in Python.
- Example:
  - `Warm-Up Exercise.py`
  - `Michelangelo's Number.py`
  - `Leonardo’s Message.py`
  - `Donatello's Painting.py`

---

## How to Run
1. Clone this repository.
2. Navigate to the directory.
3. Run the desired script:
   ```bash
   python <script_name>.py
   ```

---
