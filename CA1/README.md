
# Competitive Programming Problems

This repository contains solutions to a series of competitive programming problems regarding time complexity. Each problem includes a detailed description, input and output formats, and constraints.

---

## Table of Contents
1. [Interesting Word](#interesting-word)
2. [Meeting Time Validation](#meeting-time-validation)
3. [Longest Unique Substring](#longest-unique-substring)
4. [Misagh Sequence](#misagh-sequence)

---

## Interesting Word

### Problem Description
An "interesting word" is defined as a word where at most one character occurs an odd number of times. Given a string consisting of the first ten English alphabet letters (`'a'` to `'j'`), count all non-empty contiguous substrings that are "interesting."

### Input
- A single string `S` of length `L` where `1 ≤ L ≤ 10^5`.

### Output
- Print the count of all "interesting" substrings.

### Example
#### Input
```
aabb
```

#### Output
```
9
```

---

## Meeting Time Validation

### Problem Description
Asghar plans a meeting at a specific time `P` in the format `"HH:MM AM/PM"`. He has `N` friends, each available within a time range `[Li, Ri]`. Determine which friends can attend the meeting.

### Input
- An integer `T` (number of test cases).
- For each test case:
  - Time `P` in the format `"HH:MM AM/PM"`.
  - An integer `N` (number of friends).
  - `N` lines, each containing the availability range `[Li, Ri]`.

### Output
- For each test case, print a binary string of length `N`. `1` indicates the friend can attend, and `0` otherwise.

### Example
#### Input
```
1
12:50 AM
3
12:00 AM 11:22 PM
12:01 AM 11:29 AM
12:29 AM 12:00 PM
```

#### Output
```
111
```

---

## Longest Unique Substring

### Problem Description
Determine the length of the longest contiguous substring of a given string that contains only unique characters.

### Input
- A single string `S` of length `1 ≤ len(S) ≤ 10^3`.

### Output
- Print the length of the longest substring with unique characters.

### Example
#### Input
```
meeowe
```

#### Output
```
3
```

---

## Misagh Sequence

### Problem Description
A "Misagh sequence" is a Fibonacci-like sequence where the first two numbers are arbitrary, and each subsequent number is the sum of the previous two. Determine if a given numeric string can be split into a valid Misagh sequence.

### Input
- A numeric string `S` of length `1 ≤ len(S) ≤ 10^3`.

### Output
- Print `YES` if the string can be split into a Misagh sequence; otherwise, print `NO`.

### Constraints
- The sequence must have at least three numbers.
- Numbers cannot start with `0`.

### Example
#### Input
```
112358
```

#### Output
```
YES
```

#### Explanation
The sequence is `1, 1, 2, 3, 5, 8`.

---

## Repository Structure
- Each problem has a dedicated file with its solution implemented in Python.
- Example:
  - `interesting_word.py`
  - `meeting_time_validation.py`
  - `longest_unique_substring.py`
  - `misagh_sequence.py`

---

## How to Run
1. Clone this repository.
2. Navigate to the directory.
3. Run the desired script:
   ```bash
   python <script_name>.py
   ```

---

