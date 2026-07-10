# The Complete Array Handbook


---

---

# Table of Contents

1. [Introduction to Arrays](#chapter-1-introduction-to-arrays)
   - [1.1 What is an Array?](#11-what-is-an-array)
   - [1.2 History and Evolution](#12-history-and-evolution)
   - [1.3 Why Arrays Exist](#13-why-arrays-exist)
   - [1.4 Characteristics and Properties](#14-characteristics-and-properties)
   - [1.5 Advantages](#15-advantages)
   - [1.6 Disadvantages](#16-disadvantages)
   - [1.7 Real World Applications](#17-real-world-applications)
   - [1.8 Common Misconceptions](#18-common-misconceptions)
   - [Chapter 1 Summary & Cheat Sheet](#chapter-1-summary--cheat-sheet)

2. [Python Arrays](#chapter-2-python-arrays)
   - [2.1 Python Lists vs the `array` Module vs NumPy](#21-python-lists-vs-the-array-module-vs-numpy)
   - [2.2 Creating Arrays](#22-creating-arrays)
   - [2.3 Nested Lists — 2D and 3D Arrays](#23-nested-lists--2d-and-3d-arrays)
   - [2.4 Accessing and Updating Elements](#24-accessing-and-updating-elements)
   - [2.5 Traversal](#25-traversal)
   - [2.6 Indexing and Negative Indexing](#26-indexing-and-negative-indexing)
   - [2.7 Slicing and Extended Slicing](#27-slicing-and-extended-slicing)
   - [2.8 Adding Elements](#28-adding-elements)
   - [2.9 Removing Elements](#29-removing-elements)
   - [2.10 Reversing](#210-reversing)
   - [2.11 Copying — Aliasing, Shallow Copy, Deep Copy](#211-copying--aliasing-shallow-copy-deep-copy)
   - [Chapter 2 Summary & Cheat Sheet](#chapter-2-summary--cheat-sheet)

3. [Memory Model](#chapter-3-memory-model)
   - [3.1 RAM and Memory Addresses](#31-ram-and-memory-addresses)
   - [3.2 Contiguous Memory and Cache Locality](#32-contiguous-memory-and-cache-locality)
   - [3.3 How CPython Lists Really Work](#33-how-cpython-lists-really-work)
   - [3.4 Dynamic Resizing and Over-Allocation](#34-dynamic-resizing-and-over-allocation)
   - [3.5 Amortized Analysis of Append](#35-amortized-analysis-of-append)
   - [Chapter 3 Summary & Cheat Sheet](#chapter-3-summary--cheat-sheet)

4. [Array Operations](#chapter-4-array-operations)
   - [4.1 Access, Update, Traversal](#41-access-update-traversal)
   - [4.2 Insertion](#42-insertion)
   - [4.3 Deletion](#43-deletion)
   - [4.4 Searching](#44-searching-array-perspective-only)
   - [4.5 Swap, Move, Shift](#45-swap-move-shift)
   - [4.6 Merge and Concatenate](#46-merge-and-concatenate)
   - [4.7 Split and Partition](#47-split-and-partition)
   - [4.8 Reverse](#48-reverse)
   - [4.9 Rotate](#49-rotate)
   - [4.10 Filtering and Mapping](#410-filtering-and-mapping)
   - [4.11 Frequency Counting](#411-frequency-counting)
   - [4.12 Duplicate Detection](#412-duplicate-detection)
   - [4.13 Missing Number Detection](#413-missing-number-detection)
   - [4.14 Finding Unique Elements](#414-finding-unique-elements)
   - [Chapter 4 Summary & Cheat Sheet](#chapter-4-summary--cheat-sheet)

5. [Complexity Analysis](#chapter-5-complexity-analysis)
   - [5.1 Big-O, Big-Theta, Big-Omega Refresher](#51-big-o-big-theta-big-omega-refresher)
   - [5.2 Complexity of Every List Operation](#52-complexity-of-every-list-operation)
   - [5.3 Amortized vs Worst Case](#53-amortized-vs-worst-case)
   - [5.4 Space Complexity](#54-space-complexity)
   - [Chapter 5 Summary & Cheat Sheet](#chapter-5-summary--cheat-sheet)

6. [Array Patterns](#chapter-6-array-patterns)
   - [6.1 Traversal Patterns (Two Pointers, Sliding Window)](#61-traversal-patterns-two-pointers-sliding-window)
   - [6.2 Prefix Sum](#62-prefix-sum)
   - [6.3 Suffix Sum](#63-suffix-sum)
   - [6.4 Difference Array](#64-difference-array)
   - [6.5 Frequency / Counting Array](#65-frequency--counting-array)
   - [6.6 Index Marking / Sign Marking](#66-index-marking--sign-marking)
   - [6.7 Cyclic Sort](#67-cyclic-sort)
   - [6.8 Array Rotation](#68-array-rotation)
   - [6.9 Array Reversal Patterns](#69-array-reversal-patterns)
   - [6.10 Kadane's Algorithm](#610-kadanes-algorithm)
   - [6.11 Majority Element (Boyer-Moore Voting)](#611-majority-element-boyer-moore-voting)
   - [6.12 Dutch National Flag / Partitioning](#612-dutch-national-flag--partitioning)
   - [6.13 Bucket Counting](#613-bucket-counting)
   - [Chapter 6 Summary & Cheat Sheet](#chapter-6-summary--cheat-sheet)

7. [Subarrays](#chapter-7-subarrays)
   - [7.1 Definition and Properties](#71-definition-and-properties)
   - [7.2 Generating All Subarrays](#72-generating-all-subarrays)
   - [7.3 Counting Subarrays](#73-counting-subarrays)
   - [7.4 Fixed-Length Subarray Problems](#74-fixed-length-subarray-problems)
   - [7.5 Variable-Length Subarray Problems](#75-variable-length-subarray-problems)
   - [7.6 Maximum / Minimum Sum Subarray](#76-maximum--minimum-sum-subarray)
   - [7.7 Contribution Technique](#77-contribution-technique)
   - [Chapter 7 Summary & Cheat Sheet](#chapter-7-summary--cheat-sheet)

8. [Matrices (Arrays of Arrays)](#chapter-8-matrices-arrays-of-arrays)
   - [8.1 Representation](#81-representation)
   - [8.2 Traversal](#82-traversal)
   - [8.3 Transpose](#83-transpose)
   - [8.4 Rotation](#84-rotation)
   - [8.5 Boundary Traversal](#85-boundary-traversal)
   - [8.6 Diagonal Traversal](#86-diagonal-traversal)
   - [8.7 Spiral Traversal](#87-spiral-traversal)
   - [8.8 Snake / Zigzag Traversal](#88-snake--zigzag-traversal)
   - [8.9 2D Prefix Sum](#89-2d-prefix-sum)
   - [8.10 2D Difference Array](#810-2d-difference-array)
   - [Chapter 8 Summary & Cheat Sheet](#chapter-8-summary--cheat-sheet)

9. [Dry Run Framework](#chapter-9-dry-run-framework)
   - [9.1 How to Trace Variables and Indexes](#91-how-to-trace-variables-and-indexes)
   - [9.2 Tracing Prefix Sums and Difference Arrays](#92-tracing-prefix-sums-and-difference-arrays)
   - [9.3 Tracing Kadane's Algorithm](#93-tracing-kadanes-algorithm)
   - [9.4 Whiteboard Debugging Techniques](#94-whiteboard-debugging-techniques)
   - [Chapter 9 Summary & Cheat Sheet](#chapter-9-summary--cheat-sheet)

10. [Problem Recognition](#chapter-10-problem-recognition)
    - [10.1 Recognition Decision Tree](#101-recognition-decision-tree)
    - [10.2 Keyword-to-Pattern Mapping](#102-keyword-to-pattern-mapping)
    - [10.3 Building Observations](#103-building-observations)
    - [Chapter 10 Summary & Cheat Sheet](#chapter-10-summary--cheat-sheet)

11. [Optimization](#chapter-11-optimization)
    - [11.1 Brute Force → Better → Optimal](#111-brute-force--better--optimal)
    - [11.2 In-Place Optimization](#112-in-place-optimization)
    - [11.3 Space Optimization Tricks](#113-space-optimization-tricks)
    - [Chapter 11 Summary & Cheat Sheet](#chapter-11-summary--cheat-sheet)

12. [Interview Preparation](#chapter-12-interview-preparation)
    - [12.1 Top Array Interview Questions by Difficulty](#121-top-array-interview-questions-by-difficulty)
    - [12.2 Pattern-Wise Question Bank](#122-pattern-wise-question-bank)
    - [12.3 Company-Wise Notes](#123-company-wise-notes)
    - [12.4 Interview Tricks](#124-interview-tricks)
    - [Chapter 12 Summary & Cheat Sheet](#chapter-12-summary--cheat-sheet)

13. [Python Tips for Array Problems](#chapter-13-python-tips-for-array-problems)
    - [13.1 Built-in Functions](#131-built-in-functions)
    - [13.2 `collections` Utilities](#132-collections-utilities)
    - [13.3 `itertools` Utilities](#133-itertools-utilities)
    - [13.4 Idioms and Performance Tips](#134-idioms-and-performance-tips)
    - [Chapter 13 Summary & Cheat Sheet](#chapter-13-summary--cheat-sheet)

14. [Common Mistakes](#chapter-14-common-mistakes)
    - [14.1 Index Errors](#141-index-errors)
    - [14.2 Aliasing and Copy Bugs](#142-aliasing-and-copy-bugs)
    - [14.3 Prefix Sum & Difference Array Mistakes](#143-prefix-sum--difference-array-mistakes)
    - [14.4 Rotation and Matrix Boundary Errors](#144-rotation-and-matrix-boundary-errors)
    - [14.5 Modification During Traversal](#145-modification-during-traversal)
    - [Chapter 14 Summary & Cheat Sheet](#chapter-14-summary--cheat-sheet)

15. [Cheat Sheets](#chapter-15-cheat-sheets)
    - [15.1 Complexity Cheat Sheet](#151-complexity-cheat-sheet)
    - [15.2 Formula Sheet](#152-formula-sheet)
    - [15.3 Pattern Cheat Sheet](#153-pattern-cheat-sheet)
    - [15.4 Python Syntax Cheat Sheet](#154-python-syntax-cheat-sheet)

16. [Practice Problems](#chapter-16-practice-problems)
    - [16.1 By Topic](#161-by-topic)
    - [16.2 By Difficulty](#162-by-difficulty)
    - [16.3 By Platform](#163-by-platform)

17. [Final Revision](#chapter-17-final-revision)
    - [17.1 One-Page Revision](#171-one-page-revision)
    - [17.2 Pattern Map](#172-pattern-map)
  

---

# Chapter 1: Introduction to Arrays

**Learning Objectives:** Understand what an array is at a conceptual level, why the data structure exists, and where it fits among other structures.
**Prerequisites:** None.
**Estimated Reading Time:** 15 minutes
**Difficulty Level:** Beginner
**Topics Covered:** Definition, history, motivation, properties, pros/cons, applications, misconceptions.
**Real World Applications:** Spreadsheets, image pixels, audio buffers, database pages, matrices, game boards.
**Interview Relevance:** Low direct relevance, high conceptual relevance — interviewers expect you to justify *why* you chose an array over another structure.

---

## 1.1 What is an Array?

An **array** is a collection of elements, all of the same conceptual type, stored so that each element can be located using a single index in constant time. The defining property of a classical array is **contiguous storage combined with O(1) random access** — given an index `i`, the address of the element is computed directly using arithmetic, not by walking through the structure.

> **Definition (formal):** An array is a finite, ordered, fixed-arity mapping from an index set `{0, 1, ..., n-1}` to a set of values, physically realized so that `address(i) = base_address + i * element_size`.

In Python, the built-in `list` is *not* a classical fixed-size array — it is a dynamic array (covered in depth in Chapter 3). For this handbook, whenever we say "array," we mean the abstract data structure; whenever we say "Python list," we mean the concrete implementation we use to realize it.

### 1.1.1 Visual Explanation

```
Index:      0     1     2     3     4
          +-----+-----+-----+-----+-----+
Array:    | 10  | 25  | 33  | 47  | 52  |
          +-----+-----+-----+-----+-----+
Address:  1000  1004  1008  1012  1016   (assuming 4-byte elements)
```

Notice that moving from index `i` to `i+1` always advances the address by a fixed amount (`element_size`). This is what makes `address(i) = base + i * element_size` possible, and it is the single most important fact about arrays — everything else in this handbook builds on it.

---

## 1.2 History and Evolution

Arrays are among the oldest data structures in computing, predating high-level languages entirely.

- **1940s–1950s:** Early machine code and assembly used contiguous memory blocks addressed by offset — the array is essentially a direct reflection of how RAM itself works.
- **1957 (Fortran):** One of the first high-level languages to expose arrays as a first-class construct, including multi-dimensional arrays for scientific computing.
- **1970s (C):** Solidified the array as a thin abstraction over pointer arithmetic (`a[i]` is literally `*(a + i)`), a design still visible in how we reason about arrays today.
- **1990s onward (Python, Java, JavaScript):** Introduced **dynamic arrays** — arrays that can grow — trading a small amount of memory overhead for enormous convenience. Python's `list` is a dynamic array under the hood.

### Evolution Summary Table

| Era | Structure | Key Idea |
|---|---|---|
| Machine code | Raw memory block | Index = offset from base address |
| Fortran/C | Static array | Fixed size, compiler-checked bounds (sometimes) |
| Python/Java/JS | Dynamic array | Automatic resizing, amortized O(1) append |
| NumPy | N-dimensional array | Vectorized operations, fixed dtype, contiguous buffer |

---

## 1.3 Why Arrays Exist

Arrays exist because **most computation needs fast, predictable access to a sequence of values**. Before arrays, you would need to explicitly track the location of every value. Arrays solve three problems simultaneously:

1. **Locality:** Elements are stored next to each other, which is exactly how physical RAM and CPU caches are optimized to be read.
2. **Predictable addressing:** No pointers or search needed to find element `i` — just arithmetic.
3. **Simplicity of iteration:** A single loop variable can walk the entire structure.

> **Analogy:** Think of an array as a street of houses with sequential numbers. If you know the street starts at house #100 and each house is 10 meters apart, you can walk directly to house #107 without checking every house along the way. A linked structure, by contrast, is like a treasure hunt where each house only tells you the address of the next one.

---

## 1.4 Characteristics and Properties

| Property | Description |
|---|---|
| **Ordered** | Elements have a defined position (index). |
| **Indexed** | Every element is reachable via an integer index in O(1). |
| **Homogeneous (classically)** | Traditionally all elements share a type/size. Python lists relax this by storing *references*, not raw values. |
| **Contiguous** | Elements (or their references) are laid out in one continuous memory block. |
| **Fixed arity per operation** | Insertion/deletion at arbitrary positions requires shifting elements. |
| **Mutable (in Python)** | Elements can be reassigned after creation. |

---

## 1.5 Advantages

- **O(1) random access** by index — the single biggest reason arrays are the default choice.
- **Cache-friendly:** Sequential access patterns exploit CPU prefetching and cache lines.
- **Simple mental model:** Easy to reason about, easy to visualize, easy to debug.
- **Low memory overhead per element** compared to node-based structures (no extra pointers per element, except in the reference-based Python list, which stores one pointer per element).
- **Foundation for other structures:** Stacks, queues, heaps, hash tables, and matrices are commonly *implemented* using arrays underneath.

## 1.6 Disadvantages

- **Costly insertion/deletion in the middle:** Requires shifting up to O(n) elements.
- **Fixed size in classical arrays:** Growing beyond capacity requires reallocation (Python lists hide this from you, but it still happens internally — see Chapter 3).
- **Wasted space possible:** Dynamic arrays over-allocate to amortize growth, which uses extra memory.
- **Homogeneous assumption breaks down in Python:** A Python list is really an array of *pointers*, so it does not give you the same cache-locality benefits as a true primitive array (e.g., a NumPy array of `int64`).

---

## 1.7 Real World Applications

- **Spreadsheets:** Rows/columns are literally a 2D array.
- **Images:** A bitmap is a 2D (or 3D with color channels) array of pixel values.
- **Audio:** A waveform is a 1D array of amplitude samples.
- **Database pages / buffers:** Fixed-size contiguous blocks of records.
- **Game boards:** Chess boards, Sudoku grids, tic-tac-toe — all naturally modeled as 2D arrays.
- **Scientific computing:** Vectors and matrices in physics/ML simulations (NumPy arrays).

---

## 1.8 Common Misconceptions

> **Misconception 1:** "A Python list is a classical fixed-size array like in C."
> **Reality:** A Python list is a **dynamic array of references** to objects, not a contiguous block of raw values. This has real complexity implications covered in Chapter 3.

> **Misconception 2:** "Arrays and lists are the same everywhere."
> **Reality:** Terminology varies by language. In Python specifically, "array" usually refers to the abstract concept or the `array` module, while `list` is the everyday dynamic array type.

> **Misconception 3:** "Accessing any array element is always exactly as fast as any other."
> **Reality:** True in terms of *asymptotic* complexity (O(1)), but cache effects mean elements accessed sequentially are often faster in practice than random access due to CPU cache locality.

---

## Chapter 1 Summary & Cheat Sheet

- An array maps indices to values using direct address arithmetic → **O(1) access**.
- Arrays exist to provide fast, predictable, cache-friendly access to sequential data.
- Python's `list` is a **dynamic array of object references**, not a raw fixed-size array.
- Strength: random access. Weakness: middle insertion/deletion.

### Complexity Summary (Preview)

| Operation | Classical Array |
|---|---|
| Access by index | O(1) |
| Search (unsorted) | O(n) |
| Insert/Delete at end | O(1) |
| Insert/Delete at middle | O(n) |

### Common Mistakes
- Assuming Python lists behave like raw C arrays in terms of memory layout.
- Assuming insertion at an arbitrary index is O(1) — it is O(n).

### Frequently Asked Questions

**Q: Is a Python list an array?**
A: It behaves like a dynamic array in terms of interface (indexing, iteration), but internally it stores pointers to objects rather than raw values.

**Q: When should I NOT use an array?**
A: When you need frequent insertions/deletions at arbitrary positions and don't need random access — a different structure (covered in its own handbook) may be more appropriate.

### Practice Problems
1. Explain, in your own words, why array access is O(1). (Conceptual)
2. List three real-world systems that rely on array-like structures.
3. Give an example where a linked structure would outperform an array, and explain why.

---

# Chapter 2: Python Arrays

**Learning Objectives:** Master every way to create, access, modify, and traverse arrays in Python.
**Prerequisites:** Chapter 1.
**Estimated Reading Time:** 40 minutes
**Difficulty Level:** Beginner → Intermediate
**Topics Covered:** Lists, `array` module, creation, indexing, slicing, insertion, deletion, copying.
**Real World Applications:** Every Python program that processes sequential data.
**Interview Relevance:** Very High — syntax fluency here is assumed in every interview.

---

## 2.1 Python Lists vs the `array` Module vs NumPy

| Feature | `list` | `array.array` | `numpy.ndarray` |
|---|---|---|---|
| Element type | Any object (heterogeneous) | Single primitive type (homogeneous) | Single dtype (homogeneous) |
| Memory layout | Array of pointers | Contiguous raw values | Contiguous raw values |
| Resizable | Yes | Yes | No (fixed at creation, but can create new) |
| Built-in | Yes | Yes (`import array`) | No (`pip install numpy`) |
| Typical use | General purpose | Memory-efficient primitive storage | Numerical / scientific computing |

```python
import array

# Python list — heterogeneous, general purpose
a = [1, 2, 3, "four", 5.0]

# array module — homogeneous, typed, more memory-efficient
b = array.array('i', [1, 2, 3, 4, 5])  # 'i' = signed int
```

> **Interview Note:** Unless a question explicitly mentions `numpy` or memory efficiency, always default to Python's built-in `list` — it is what interviewers expect.

---

## 2.2 Creating Arrays

### 2.2.1 Python Syntax

```python
empty = []                     # empty list
literal = [1, 2, 3, 4, 5]      # list literal
filled = [0] * 5               # [0, 0, 0, 0, 0] — fixed-size initialization
ranged = list(range(5))        # [0, 1, 2, 3, 4]
comprehension = [x * x for x in range(5)]  # [0, 1, 4, 9, 16]
```

### 2.2.2 Dry Run — `[0] * 5`

| Step | Expression | Result | Explanation |
|---|---|---|---|
| 1 | `[0]` | `[0]` | A single-element list is created |
| 2 | `[0] * 5` | `[0, 0, 0, 0, 0]` | The list is repeated 5 times, producing new references to the same immutable `0` |

> **⚠️ Warning:** `[[0] * 3] * 3` does **NOT** create an independent 2D array — see Section 2.3 for why this is one of the most common Python array bugs.

### 2.2.3 Fixed-Size vs Dynamic Arrays

Python lists are always dynamic (resizable), but you can *simulate* a fixed-size array by pre-allocating with `[0] * n` and never calling `append`/`pop`. This is a common competitive-programming trick to avoid repeated resizing overhead when the final size is known in advance.

---

## 2.3 Nested Lists — 2D and 3D Arrays

### 2.3.1 The Aliasing Trap

```python
# WRONG — all rows are the SAME list object
wrong = [[0] * 3] * 3
wrong[0][0] = 9
print(wrong)   # [[9, 0, 0], [9, 0, 0], [9, 0, 0]]  <-- bug!

# RIGHT — each row is an independent list
right = [[0] * 3 for _ in range(3)]
right[0][0] = 9
print(right)   # [[9, 0, 0], [0, 0, 0], [0, 0, 0]]
```

**Why this happens:** `[[0] * 3] * 3` creates one inner list, then the outer `* 3` copies the *reference* to that same inner list three times. Mutating through one row mutates all rows because they all point to the same object in memory.

### 2.3.2 ASCII Diagram — Aliased vs Independent Rows

```
Aliased (WRONG):                Independent (RIGHT):
wrong ---> [ref, ref, ref]      right ---> [ref_A, ref_B, ref_C]
              |    |    |                     |      |      |
              v    v    v                     v      v      v
           [0,0,0] (ONE shared list)      [0,0,0] [0,0,0] [0,0,0]
                                           (three separate lists)
```

### 2.3.3 3D Arrays and Jagged Arrays

```python
# 3D array: 2 x 3 x 4
cube = [[[0] * 4 for _ in range(3)] for _ in range(2)]

# Jagged array — rows of different lengths (perfectly valid in Python)
jagged = [[1], [2, 3], [4, 5, 6]]
```

> **Tip:** A "jagged array" is simply a list of lists where inner lists differ in length. Python has no problem with this since lists just hold references.

---

## 2.4 Accessing and Updating Elements

```python
arr = [10, 20, 30, 40, 50]

x = arr[2]        # Access: x = 30
arr[2] = 99        # Update: arr = [10, 20, 99, 40, 50]

# 2D access
matrix = [[1, 2], [3, 4]]
val = matrix[1][0]     # 3
matrix[1][0] = 100      # matrix = [[1, 2], [100, 4]]
```

**Complexity:** Access and update are both **O(1)** because Python lists support direct address computation for the pointer array, regardless of what the referenced object is.

---

## 2.5 Traversal

### 2.5.1 Forward Traversal

```python
arr = [10, 20, 30]

# Method 1 — by index
for i in range(len(arr)):
    print(i, arr[i])

# Method 2 — by value (Pythonic)
for val in arr:
    print(val)

# Method 3 — index + value together
for i, val in enumerate(arr):
    print(i, val)
```

### 2.5.2 Backward Traversal

```python
arr = [10, 20, 30]

for i in range(len(arr) - 1, -1, -1):
    print(arr[i])

# Pythonic reverse traversal
for val in reversed(arr):
    print(val)
```

### 2.5.3 Dry Run — Backward Traversal with `range(len(arr)-1, -1, -1)`

| Step | i | arr[i] | Explanation |
|---|---|---|---|
| 1 | 2 | 30 | Start at last index (`len(arr)-1 = 2`) |
| 2 | 1 | 20 | Decrement by 1 |
| 3 | 0 | 10 | Decrement by 1 |
| — | -1 | stop | Loop stops before reaching -1 |

---

## 2.6 Indexing and Negative Indexing

```
Index:      0     1     2     3     4
          +-----+-----+-----+-----+-----+
Array:    | 10  | 25  | 33  | 47  | 52  |
          +-----+-----+-----+-----+-----+
Neg Idx:   -5    -4    -3    -2    -1
```

```python
arr = [10, 25, 33, 47, 52]
arr[0]    # 10  (first element)
arr[-1]   # 52  (last element)
arr[-2]   # 47  (second-to-last)
```

> **Formula:** `arr[-k]` is equivalent to `arr[len(arr) - k]`.

> **⚠️ Common Mistake:** `arr[len(arr)]` raises `IndexError` — valid positive indices go from `0` to `len(arr) - 1`.

---

## 2.7 Slicing and Extended Slicing

### 2.7.1 Syntax

```python
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr[2:5]     # [2, 3, 4]        start=2, stop=5
arr[:4]      # [0, 1, 2, 3]     start defaults to 0
arr[6:]      # [6, 7, 8, 9]     stop defaults to len(arr)
arr[:]       # full shallow copy
arr[::2]     # [0, 2, 4, 6, 8]  every 2nd element
arr[::-1]    # [9, 8, 7, ..., 0] reversed copy
arr[1:8:2]   # [1, 3, 5, 7]     start, stop, step
```

### 2.7.2 Dry Run — `arr[1:8:2]`

| Step | Index visited | Included? | Running result |
|---|---|---|---|
| 1 | 1 | Yes (< 8) | [1] |
| 2 | 3 | Yes | [1, 3] |
| 3 | 5 | Yes | [1, 3, 5] |
| 4 | 7 | Yes | [1, 3, 5, 7] |
| 5 | 9 | No (9 ≥ 8) | stop |

### 2.7.3 Slice Assignment

```python
arr = [1, 2, 3, 4, 5]
arr[1:3] = [20, 30, 40]   # replaces 2 elements with 3
print(arr)                # [1, 20, 30, 40, 4, 5]  — list grows!

arr[1:4] = []              # deletes elements 1..3
print(arr)                 # [1, 4, 5]
```

> **Interview Tip:** Slicing always returns a **new list** (shallow copy), never a view, unlike NumPy. This means `arr[:]` is a cheap and idiomatic way to clone a flat list.

---

## 2.8 Adding Elements

| Method | Position | Complexity | Example |
|---|---|---|---|
| `append(x)` | End | O(1) amortized | `arr.append(6)` |
| `insert(i, x)` | Arbitrary index | O(n) | `arr.insert(2, 99)` |
| `extend(iterable)` | End (multiple) | O(k) amortized | `arr.extend([7, 8])` |
| `arr + other` | New list | O(n + m) | `arr = arr + [9, 10]` |
| `arr[i:i] = [x]` | Arbitrary index | O(n) | `arr[2:2] = [99]` |

### Dry Run — `insert`

```python
arr = [1, 2, 4, 5]
arr.insert(2, 3)
```

| Step | Action | Array State |
|---|---|---|
| 1 | Shift elements from index 2 onward right by 1 | `[1, 2, _, 4, 5]` (conceptually) |
| 2 | Place `3` at index 2 | `[1, 2, 3, 4, 5]` |

---

## 2.9 Removing Elements

| Method | Behavior | Complexity |
|---|---|---|
| `pop()` | Removes & returns last element | O(1) |
| `pop(i)` | Removes & returns element at index `i` | O(n) |
| `remove(x)` | Removes first occurrence of value `x` | O(n) |
| `del arr[i]` | Deletes element at index `i` | O(n) |
| `del arr[i:j]` | Deletes a slice | O(n) |
| `clear()` | Removes all elements | O(n) |

```python
arr = [1, 2, 3, 4, 5]
arr.pop()        # removes 5  -> [1, 2, 3, 4]
arr.pop(0)        # removes 1  -> [2, 3, 4]
arr.remove(3)      # removes value 3 -> [2, 4]
del arr[0]          # -> [4]
```

> **⚠️ Warning:** `remove(x)` raises `ValueError` if `x` is not present. Always guard with `if x in arr` or use `try/except` when the presence isn't guaranteed.

---

## 2.10 Reversing

```python
arr = [1, 2, 3, 4, 5]

arr.reverse()          # in-place, O(n), returns None
reversed_copy = arr[::-1]   # new list, O(n)
it = reversed(arr)          # returns an iterator, O(1) to create
```

> **Common Mistake:** Writing `arr = arr.reverse()` — this sets `arr` to `None` because `reverse()` mutates in place and returns `None`.

---

## 2.11 Copying — Aliasing, Shallow Copy, Deep Copy

### 2.11.1 Aliasing (no copy at all)

```python
a = [1, 2, 3]
b = a          # b is just another name for the SAME list
b.append(4)
print(a)       # [1, 2, 3, 4]  <-- a changed too!
```

### 2.11.2 Shallow Copy

```python
import copy

a = [[1, 2], [3, 4]]
b = a.copy()            # or list(a) or a[:]
b[0] = [9, 9]             # top-level replace — does NOT affect a
b[1][0] = 100              # mutates SHARED inner list — DOES affect a!

print(a)   # [[1, 2], [100, 4]]
print(b)   # [[9, 9], [100, 4]]
```

### 2.11.3 Deep Copy

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[1][0] = 100
print(a)   # [[1, 2], [3, 4]]   <-- untouched
print(b)   # [[1, 2], [100, 4]]
```

### 2.11.4 ASCII Diagram — Shallow vs Deep Copy

```
Original a:  a ---> [ref1, ref2] ---> [1,2]   [3,4]

Shallow b:   b ---> [ref1, ref2]   (new outer list,
                        |     |      same inner list refs)
                        v     v
                     [1,2]  [3,4]     <-- SHARED with a

Deep b:      b ---> [ref1', ref2']  (new outer list,
                        |      |      brand-new inner lists)
                        v      v
                     [1,2]   [3,4]    <-- INDEPENDENT of a
```

### 2.11.5 Copy Method Comparison Table

| Method | Copies outer list? | Copies nested objects? | Speed |
|---|---|---|---|
| `b = a` | No (alias) | No | O(1) |
| `b = a.copy()` / `a[:]` / `list(a)` | Yes | No (shares references) | O(n) |
| `b = copy.deepcopy(a)` | Yes | Yes, recursively | O(n) but slower (recursive) |

> **Interview Tip:** If a problem says "do not modify the input" and the input is a matrix (list of lists), a shallow copy is usually **not enough** — you need to copy each row too, e.g., `[row[:] for row in matrix]`, or use `deepcopy`.

---

## Chapter 2 Summary & Cheat Sheet

- `list` is Python's general-purpose dynamic array; `array.array` is a typed, memory-efficient alternative.
- Negative indices count from the end: `arr[-1]` is the last element.
- Slicing `arr[start:stop:step]` always returns a new list.
- `append` is O(1) amortized; `insert`/`pop(i)`/`remove` are O(n).
- `[[0]*n]*m` aliases rows — always use a list comprehension for 2D initialization.
- Shallow copies share nested objects; use `deepcopy` for full independence.

### Python Syntax Cheat Sheet

```python
arr[i]                # access
arr[i] = x              # update
arr[a:b]                # slice
arr[a:b:c]               # extended slice
arr.append(x)             # add to end
arr.insert(i, x)           # add at index
arr.extend(iterable)        # add many to end
arr.pop()                    # remove last
arr.pop(i)                    # remove at index
arr.remove(x)                  # remove by value
arr.reverse()                    # reverse in place
arr[::-1]                         # reversed copy
arr.copy() / arr[:] / list(arr)    # shallow copy
copy.deepcopy(arr)                   # deep copy
```

### Common Mistakes
- Using `[[0]*n]*m` for 2D arrays (aliasing bug).
- Forgetting `remove()` raises `ValueError` if value absent.
- Assuming `arr.reverse()` returns the reversed list (it returns `None`).
- Confusing shallow copy with deep copy for nested structures.

### Frequently Asked Questions

**Q: What's the difference between `remove()` and `del`?**
A: `remove(x)` searches by value; `del arr[i]` deletes by index.

**Q: Is `arr[:]` a deep copy?**
A: No — it is a shallow copy. Nested mutable objects are still shared.

### Practice Problems
1. Write a function to create an `n x m` 2D array filled with zeros without the aliasing bug.
2. Given a matrix, write a function that returns a fully independent deep copy without using `copy.deepcopy`.
3. Explain why `arr = arr.reverse()` is a bug.

---

# Chapter 3: Memory Model

**Learning Objectives:** Understand how arrays are physically represented in memory and why this affects performance.
**Prerequisites:** Chapters 1–2.
**Estimated Reading Time:** 25 minutes
**Difficulty Level:** Intermediate
**Topics Covered:** RAM, addresses, contiguity, cache locality, CPython internals, resizing, amortized analysis.
**Real World Applications:** Performance tuning, understanding why `append` is fast but `insert(0, x)` is slow.
**Interview Relevance:** High — "Why is append O(1) but insert O(n)?" is a classic follow-up question.

---

## 3.1 RAM and Memory Addresses

RAM is a giant array of bytes, each with its own address. Every data structure is ultimately built on top of this. An array's core trick is aligning its own indexing scheme with RAM's native addressing scheme.

```
RAM (simplified):
Address:  1000  1001  1002  1003  1004  1005  ...
Byte:     [ ]   [ ]   [ ]   [ ]   [ ]   [ ]
```

## 3.2 Contiguous Memory and Cache Locality

A classical array of 4-byte integers occupies one unbroken block of memory:

```
Address:  2000       2004       2008       2012
Element:  [ 7 ]      [ 3 ]      [ 9 ]      [ 1 ]
           idx 0      idx 1      idx 2      idx 3
```

Because the elements are adjacent, when the CPU loads `arr[0]` it typically pulls a whole **cache line** (e.g., 64 bytes) into fast cache memory — which often includes `arr[1]`, `arr[2]`, etc. for free. This is why **sequential traversal is faster in practice** than the same number of random accesses, even though both are "O(1) per access" in theory.

> **Analogy:** Reading a contiguous array is like reading a book page by page. Reading scattered nodes (as in a linked list) is like following footnotes to different books scattered across a library — same number of "reads," vastly different real-world speed.

## 3.3 How CPython Lists Really Work

A Python `list` is **not** a contiguous array of values — it is a contiguous array of **pointers (references)** to Python objects that may live anywhere in memory.

```
Python list [10, "hello", 3.14]:

list object ---> [ptr0, ptr1, ptr2]   (contiguous array of pointers)
                    |     |     |
                    v     v     v
                  [10]  ["hello"]  [3.14]   (objects scattered in heap memory)
```

This is *why* Python lists can hold mixed types — each slot is just a pointer, regardless of what it points to. The cost is an extra indirection (pointer dereference) on every access, and worse cache locality than a true primitive array (like a NumPy array or C array).

## 3.4 Dynamic Resizing and Over-Allocation

Python lists grow dynamically. When you `append` past the current capacity, CPython allocates a **larger** block (not just one more slot) and copies existing pointers over. This over-allocation is what makes `append` fast on average.

```
Capacity growth (conceptual, CPython uses roughly a 1.125x growth factor with
a small constant added, not simple doubling):

len=0 cap=0
len=1 cap=4
len=5 cap=8
len=9 cap=16
...
```

### ASCII Diagram — Growth on Append

```
Before append (len=4, cap=4):        [10][20][30][40]           <- full!
append(50) triggers reallocation:
Step 1: allocate new bigger block:    [__][__][__][__][__][__][__][__]
Step 2: copy old pointers over:       [10][20][30][40][__][__][__][__]
Step 3: insert new element:           [10][20][30][40][50][__][__][__]
                                       len=5, cap=8 (extra capacity reserved)
```

## 3.5 Amortized Analysis of Append

Even though a resize costs O(n) when it happens, resizes become exponentially rarer as the list grows, so the **average** cost per `append` over a long sequence of appends is O(1). This is called **amortized O(1)**.

### Dry Run — Cost of 8 Appends into an Empty List

| Append # | Capacity Before | Resize? | Cost |
|---|---|---|---|
| 1 | 0 | Yes | 1 (copy 0 + insert 1) |
| 2 | 4 | No | 1 |
| 3 | 4 | No | 1 |
| 4 | 4 | No | 1 |
| 5 | 4 | Yes | 5 (copy 4 + insert 1) |
| 6 | 8 | No | 1 |
| 7 | 8 | No | 1 |
| 8 | 8 | No | 1 |

Total cost ≈ 12 for 8 appends → average ≈ 1.5 per append, which stays bounded by a constant no matter how large `n` gets — hence **amortized O(1)**.

> **Interview Tip:** If asked "why is `insert(0, x)` O(n) but `append(x)` O(1) amortized?" — the answer is that `insert(0, x)` must shift **every** existing element right by one position (O(n) work every single time), while `append` only occasionally triggers a resize.

---

## Chapter 3 Summary & Cheat Sheet

- RAM is addressable byte-by-byte; arrays map indices to addresses via arithmetic.
- Python lists store **pointers**, not raw values — an extra indirection versus a true primitive array.
- Lists over-allocate capacity so that `append` is amortized O(1).
- `insert(0, x)` and `pop(0)` are O(n) because they shift every remaining element.

### Complexity Summary

| Operation | Complexity | Why |
|---|---|---|
| `append(x)` | O(1) amortized | Over-allocated capacity absorbs most appends |
| `arr[i]` | O(1) | Direct pointer arithmetic |
| `insert(0, x)` | O(n) | Must shift all elements right |
| `pop(0)` | O(n) | Must shift all elements left |
| `pop()` | O(1) | No shifting needed |

### Common Mistakes
- Assuming Python lists have the same cache performance as C arrays or NumPy arrays.
- Assuming all insertions are O(1) because "append is O(1)."

### Frequently Asked Questions

**Q: Why does NumPy outperform lists for numeric work?**
A: NumPy arrays store raw values contiguously (no pointer indirection) and use vectorized, compiled operations instead of Python-level loops.

### Practice Problems
1. Explain, using the amortized analysis idea, why 1000 appends cost roughly O(1000) total, not O(1000²).
2. Why is inserting at the front of a list fundamentally more expensive than at the back?

---

# Chapter 4: Array Operations

**Learning Objectives:** Implement and analyze every fundamental array operation.
**Prerequisites:** Chapters 1–3.
**Estimated Reading Time:** 45 minutes
**Difficulty Level:** Beginner → Intermediate
**Topics Covered:** Access, insertion, deletion, searching, swap, merge, split, reverse, rotate, filter, frequency, duplicates, missing values, uniques.
**Real World Applications:** Building block for virtually every array-based interview question.
**Interview Relevance:** Extremely High.

---

## 4.1 Access, Update, Traversal

Already covered in depth in Chapter 2 (Sections 2.4–2.5). Quick reference:

```python
arr[i]            # access — O(1)
arr[i] = x          # update — O(1)
for v in arr: ...     # traversal — O(n)
```

## 4.2 Insertion

### Problem Statement
Insert a value `x` at position `i` in an array, shifting subsequent elements right.

### Approach
Shift all elements from index `i` to the end one position to the right, then place `x` at index `i`.

### Python Code

```python
def insert_at(arr, i, x):
    arr.append(None)                  # make room — O(1) amortized
    for j in range(len(arr) - 1, i, -1):
        arr[j] = arr[j - 1]             # shift right
    arr[i] = x
    return arr
```

### Line-by-Line Explanation
1. `arr.append(None)` — grows the array by one slot to make room for the shift.
2. The `for` loop walks backward from the last index down to `i+1`, copying each element one position to the right.
3. After the loop, index `i` is free, and `x` is placed there.

### Dry Run — `insert_at([1, 2, 4, 5], 2, 3)`

| Step | j | Action | Array State |
|---|---|---|---|
| 0 | — | `arr.append(None)` | `[1, 2, 4, 5, None]` |
| 1 | 4 | `arr[4] = arr[3]` (5) | `[1, 2, 4, 5, 5]` |
| 2 | 3 | `arr[3] = arr[2]` (4) | `[1, 2, 4, 4, 5]` |
| 3 | loop ends (j=2 == i) | — | — |
| 4 | — | `arr[2] = 3` | `[1, 2, 3, 4, 5]` |

### Complexity Analysis
- Time: O(n) worst case (insert at front), O(1) if inserting at the end.
- Space: O(1) extra (in-place, excluding the growth slot).

### Alternative Approach
```python
arr.insert(i, x)          # built-in, same O(n) complexity
arr[i:i] = [x]              # slice assignment, also O(n)
```

### When to Use / When NOT to Use
- Use built-in `insert`/slice-assignment for clarity in interviews.
- Avoid frequent middle insertions in performance-critical code — consider whether the problem truly needs an array, or whether a different structure (outside this handbook's scope) fits better.

### Edge Cases
- Inserting at `i == len(arr)` — equivalent to `append`.
- Inserting at `i == 0` — worst case, shifts everything.
- Empty array — only valid insertion index is 0.

---

## 4.3 Deletion

### Python Code

```python
def delete_at(arr, i):
    for j in range(i, len(arr) - 1):
        arr[j] = arr[j + 1]        # shift left
    arr.pop()                        # remove now-duplicated last element
    return arr
```

### Dry Run — `delete_at([1, 2, 3, 4, 5], 1)`

| Step | j | Action | Array State |
|---|---|---|---|
| 1 | 1 | `arr[1] = arr[2]` (3) | `[1, 3, 3, 4, 5]` |
| 2 | 2 | `arr[2] = arr[3]` (4) | `[1, 3, 4, 4, 5]` |
| 3 | 3 | `arr[3] = arr[4]` (5) | `[1, 3, 4, 5, 5]` |
| 4 | — | `arr.pop()` | `[1, 3, 4, 5]` |

**Complexity:** O(n) time (worst case, deleting near the front), O(1) space.

> **Interview Tip:** If order doesn't matter, you can delete in O(1) by swapping the target with the last element and popping:
> ```python
> def delete_unordered(arr, i):
>     arr[i] = arr[-1]
>     arr.pop()
> ```

---

## 4.4 Searching (Array Perspective Only)

Linear search is the array-native search technique (binary search belongs to its own handbook, so only briefly noted here for context).

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

**Complexity:** O(n) time, O(1) space. Works on unsorted data, unlike binary search.

---

## 4.5 Swap, Move, Shift

```python
# Swap — Pythonic tuple unpacking, no temp variable needed
arr[i], arr[j] = arr[j], arr[i]

# Shift all elements left by k positions (simple, non-circular)
def shift_left(arr, k):
    n = len(arr)
    result = [0] * n
    for i in range(n):
        if i + k < n:
            result[i] = arr[i + k]
    return result
```

### ASCII Diagram — Swap

```
Before:  [ 10 | 20 | 30 | 40 ]
                i         j
Swap arr[1] and arr[3]:
After:   [ 10 | 40 | 30 | 20 ]
```

---

## 4.6 Merge and Concatenate

```python
a = [1, 3, 5]
b = [2, 4, 6]

concat = a + b            # [1, 3, 5, 2, 4, 6] — O(n+m), new list
a.extend(b)                 # a becomes [1, 3, 5, 2, 4, 6] — O(m) amortized, in-place

# Merge two SORTED arrays into one sorted array (two-pointer)
def merge_sorted(a, b):
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged
```

### Dry Run — `merge_sorted([1, 3, 5], [2, 4, 6])`

| Step | i | j | Comparison | merged |
|---|---|---|---|---|
| 1 | 0 | 0 | 1 ≤ 2 → take a[0] | [1] |
| 2 | 1 | 0 | 3 > 2 → take b[0] | [1, 2] |
| 3 | 1 | 1 | 3 ≤ 4 → take a[1] | [1, 2, 3] |
| 4 | 2 | 1 | 5 > 4 → take b[1] | [1, 2, 3, 4] |
| 5 | 2 | 2 | 5 ≤ 6 → take a[2] | [1, 2, 3, 4, 5] |
| 6 | 3 | 2 | i out of range → extend with b[2:] | [1, 2, 3, 4, 5, 6] |

**Complexity:** O(n + m) time, O(n + m) space.

---

## 4.7 Split and Partition

```python
arr = [1, 2, 3, 4, 5, 6]

# Split into two halves
mid = len(arr) // 2
left, right = arr[:mid], arr[mid:]

# Partition around a pivot value (Lomuto-style, array-native)
def partition(arr, pivot):
    less, equal, greater = [], [], []
    for x in arr:
        if x < pivot: less.append(x)
        elif x == pivot: equal.append(x)
        else: greater.append(x)
    return less + equal + greater
```

---

## 4.8 Reverse

Covered in Section 2.10. In-place two-pointer version (the technique interviewers actually want to see):

```python
def reverse_inplace(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

### Dry Run — `reverse_inplace([1, 2, 3, 4, 5])`

| Step | left | right | Array State |
|---|---|---|---|
| 0 | 0 | 4 | [1, 2, 3, 4, 5] |
| 1 | 1 | 3 | [5, 2, 3, 4, 1] |
| 2 | 2 | 2 | [5, 4, 3, 2, 1] |
| 3 | loop ends (left == right) | — | [5, 4, 3, 2, 1] |

**Complexity:** O(n) time, O(1) space (true in-place, unlike slicing `arr[::-1]` which is O(n) space).

---

## 4.9 Rotate

(Full treatment with three approaches in Chapter 6, Section 6.8 — brief operation-level view here.)

```python
def rotate_right_bruteforce(arr, k):
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k]
```

---

## 4.10 Filtering and Mapping

```python
arr = [1, 2, 3, 4, 5, 6]

evens = [x for x in arr if x % 2 == 0]        # filter
evens_builtin = list(filter(lambda x: x % 2 == 0, arr))

squares = [x * x for x in arr]                  # map
squares_builtin = list(map(lambda x: x * x, arr))
```

> **Interview Tip:** List comprehensions are almost always preferred over `map`/`filter` in Python interviews for readability, and are often marginally faster too.

---

## 4.11 Frequency Counting

```python
from collections import Counter

arr = [1, 1, 2, 3, 3, 3]

freq_manual = {}
for x in arr:
    freq_manual[x] = freq_manual.get(x, 0) + 1

freq_counter = Counter(arr)     # Counter({3: 3, 1: 2, 2: 1})
```

**Complexity:** O(n) time, O(k) space where `k` = number of distinct elements.

---

## 4.12 Duplicate Detection

```python
def has_duplicate(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False

# One-liner using set size comparison
def has_duplicate_v2(arr):
    return len(set(arr)) != len(arr)
```

**Complexity:** O(n) time, O(n) space.

> **Edge Case:** An empty array or single-element array trivially has no duplicates.

---

## 4.13 Missing Number Detection

### Problem: Array of `n` distinct numbers from `0` to `n`, find the missing one.

```python
def find_missing(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
```

### Dry Run — `find_missing([3, 0, 1])` (n=3, expect range 0..3)

| Step | Value | Explanation |
|---|---|---|
| 1 | `expected_sum = 3*4//2 = 6` | Sum of 0..3 |
| 2 | `actual_sum = 3+0+1 = 4` | Sum of given array |
| 3 | `6 - 4 = 2` | Missing number is 2 |

**Complexity:** O(n) time, O(1) space.

> **Alternative (XOR trick):** XOR all indices `0..n` with all array values; duplicates cancel out, leaving the missing number. Useful when sums risk overflow (not a Python concern, but a common interview follow-up).

---

## 4.14 Finding Unique Elements

```python
arr = [4, 5, 4, 6, 5, 7]

unique_values = list(set(arr))                 # order not preserved
unique_ordered = list(dict.fromkeys(arr))         # order preserved (Python 3.7+)
```

---

## Chapter 4 Summary & Cheat Sheet

| Operation | Time | Space |
|---|---|---|
| Access/Update | O(1) | O(1) |
| Insert (middle) | O(n) | O(1) |
| Insert (end) | O(1) amortized | O(1) |
| Delete (middle) | O(n) | O(1) |
| Delete (end) | O(1) | O(1) |
| Linear search | O(n) | O(1) |
| Merge sorted | O(n+m) | O(n+m) |
| Reverse (two-pointer) | O(n) | O(1) |
| Frequency count | O(n) | O(k) |
| Duplicate detection | O(n) | O(n) |
| Missing number (sum trick) | O(n) | O(1) |

### Common Mistakes
- Forgetting to `pop()` the leftover duplicate element after a manual shift-based delete.
- Using `arr.remove(x)` inside a loop that also iterates `arr` (see Chapter 14).
- Off-by-one errors in shift loops (`range(i, len(arr)-1)` vs `range(i, len(arr))`).

### Frequently Asked Questions

**Q: Why not always use built-in `insert`/`remove`?**
A: You should, in real code. Manual shift implementations are taught so you understand *why* they're O(n), which interviewers frequently probe.

### Practice Problems
1. Implement `delete_at` without using `pop()`.
2. Modify `merge_sorted` to remove duplicates while merging.
3. Find the missing number when the array can contain values from `1` to `n` instead of `0` to `n`.
4. Find **two** missing numbers instead of one (harder variant).

---

# Chapter 5: Complexity Analysis

**Learning Objectives:** Precisely state and justify the complexity of every array operation.
**Prerequisites:** Chapters 1–4.
**Estimated Reading Time:** 15 minutes
**Difficulty Level:** Beginner → Intermediate
**Topics Covered:** Big-O refresher, complete complexity table, amortized vs worst case, space complexity.
**Real World Applications:** Justifying design decisions in system design and interviews.
**Interview Relevance:** Extremely High.

---

## 5.1 Big-O, Big-Theta, Big-Omega Refresher

| Notation | Meaning | Plain English |
|---|---|---|
| O(f(n)) | Upper bound | "At most this much work" (worst case, typically) |
| Ω(f(n)) | Lower bound | "At least this much work" (best case, typically) |
| Θ(f(n)) | Tight bound | "Exactly this much work," both bounds match |

> **Note:** This handbook uses "Big-O" colloquially to mean "the commonly cited worst-case (or amortized) complexity," matching standard interview usage.

## 5.2 Complexity of Every List Operation

| Operation | Time Complexity | Notes |
|---|---|---|
| `arr[i]` (access) | O(1) | Direct address computation |
| `arr[i] = x` (update) | O(1) | Direct address computation |
| `len(arr)` | O(1) | Length is cached, not computed by counting |
| `x in arr` | O(n) | Linear scan |
| `arr.append(x)` | O(1) amortized | Occasional O(n) resize |
| `arr.pop()` | O(1) | No shifting |
| `arr.pop(0)` | O(n) | Shifts all remaining elements |
| `arr.insert(i, x)` | O(n) | Shifts elements from `i` onward |
| `arr.remove(x)` | O(n) | Linear search + shift |
| `arr.reverse()` | O(n) | Full traversal, in-place |
| `arr[::-1]` | O(n) time, O(n) space | Creates new list |
| `arr.sort()` | O(n log n) | Timsort (out of scope beyond mention) |
| `arr.copy()` / `arr[:]` | O(n) | Shallow copy |
| `copy.deepcopy(arr)` | O(n) (recursive) | Deep copy, slower constant factor |
| slicing `arr[a:b]` | O(b-a) | Proportional to slice length |
| `min(arr)` / `max(arr)` | O(n) | Linear scan |
| `sum(arr)` | O(n) | Linear scan |

## 5.3 Amortized vs Worst Case

Amortized complexity describes the *average* cost per operation over a long sequence, even if individual operations occasionally cost more. `append` is the textbook example: most calls are O(1), but a resize is O(n) — amortized over many calls, this averages to O(1) (see Chapter 3, Section 3.5 for the full derivation).

> **Interview Tip:** If asked "is `append` always O(1)?" the precise answer is: "No — it's O(1) *amortized*; a single call can be O(n) when a resize is triggered, but this happens rarely enough that the long-run average is O(1)."

## 5.4 Space Complexity

| Approach | Extra Space |
|---|---|
| In-place two-pointer reversal | O(1) |
| Reversal using slicing (`arr[::-1]`) | O(n) |
| Prefix sum array | O(n) |
| Frequency map | O(k) distinct elements |
| Recursive array algorithms | O(depth) call stack (mentioned only for context — recursion is its own handbook) |

---

## Chapter 5 Summary & Cheat Sheet

- Access/update = O(1). Search/insert-middle/delete-middle = O(n). Append/pop-end = O(1) amortized.
- Always distinguish "amortized" from "worst case" when discussing `append`.
- Space complexity matters as much as time — an O(1)-space in-place solution is often preferred over an O(n)-space one when both are O(n) time.

### Common Mistakes
- Saying "array access is O(n)" (it's O(1) — a very common beginner slip when confusing arrays with linked lists).
- Ignoring space complexity trade-offs when a brute-force and optimal solution have the same time complexity.

### Frequently Asked Questions

**Q: Is Python's `len()` O(1) or O(n)?**
A: O(1) — CPython lists store their length as a field on the object, they don't count elements each call.

### Practice Problems
1. State the time and space complexity of `merge_sorted` from Chapter 4.
2. Compare the space complexity of in-place reversal vs slice-based reversal.

---

# Chapter 6: Array Patterns

**Learning Objectives:** Recognize and implement every core array-specific algorithmic pattern.
**Prerequisites:** Chapters 1–5.
**Estimated Reading Time:** 90 minutes
**Difficulty Level:** Intermediate → Advanced
**Topics Covered:** Two pointers, sliding window, prefix/suffix sum, difference array, frequency arrays, index/sign marking, cyclic sort, rotation, reversal patterns, Kadane's algorithm, majority element, Dutch flag, bucket counting.
**Real World Applications:** Analytics dashboards (running totals), calendar booking systems (difference arrays), stock analysis (Kadane's), voting systems (majority element).
**Interview Relevance:** This is the single highest-yield chapter in the entire handbook.

---

## 6.1 Traversal Patterns (Two Pointers, Sliding Window)

### 6.1.1 Two Pointers — Definition

Two indices traverse the array, either moving toward each other (opposite ends) or in the same direction, to avoid nested loops (O(n²) → O(n)).

### 6.1.2 Recognition
Look for: sorted array + pair/triplet sum problems, palindrome checks, removing duplicates in-place, or "meet in the middle" phrasing.

### ASCII Diagram — Opposite-Direction Two Pointers

```
arr = [1, 3, 5, 7, 9, 11]   target sum = 12

left ->                          <- right
 [1,   3,   5,   7,   9,   11]
  1 + 11 = 12  -> FOUND
```

### Python Implementation — Pair with Target Sum (sorted array)

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return (left, right)
        elif s < target:
            left += 1
        else:
            right -= 1
    return (-1, -1)
```

### Dry Run — `two_sum_sorted([1, 3, 5, 7, 9, 11], 12)`

| Step | left | right | arr[left]+arr[right] | Action |
|---|---|---|---|---|
| 1 | 0 | 5 | 1+11=12 | Match found → return (0, 5) |

### Dry Run 2 — `two_sum_sorted([1, 2, 4, 7, 11], 10)`

| Step | left | right | Sum | Action |
|---|---|---|---|---|
| 1 | 0 | 4 | 1+11=12 | 12 > 10 → right -= 1 |
| 2 | 0 | 3 | 1+7=8 | 8 < 10 → left += 1 |
| 3 | 1 | 3 | 2+7=9 | 9 < 10 → left += 1 |
| 4 | 2 | 3 | 4+7=11 | 11 > 10 → right -= 1 |
| 5 | 2 | 2 | loop ends | left == right → return (-1,-1) |

**Complexity:** O(n) time, O(1) space.

### 6.1.3 Sliding Window — Definition

Maintain a contiguous window `[left, right]` and slide it across the array, expanding/shrinking based on a condition, avoiding recomputation from scratch.

### ASCII Diagram — Fixed-Size Sliding Window (k=3)

```
arr = [2, 1, 5, 1, 3, 2]

Window 1: [2 1 5] 1 3 2   sum=8
Window 2:  2 [1 5 1] 3 2   sum=7
Window 3:  2 1 [5 1 3] 2   sum=9
Window 4:  2 1 5 [1 3 2]   sum=6
```

### Python Implementation — Max Sum Subarray of Size k

```python
def max_sum_window(arr, k):
    window_sum = sum(arr[:k])
    best = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]     # slide: add new, remove old
        best = max(best, window_sum)
    return best
```

### Dry Run — `max_sum_window([2, 1, 5, 1, 3, 2], 3)`

| Step | i | Add | Remove | window_sum | best |
|---|---|---|---|---|---|
| init | — | — | — | 8 (2+1+5) | 8 |
| 1 | 3 | arr[3]=1 | arr[0]=2 | 8+1-2=7 | 8 |
| 2 | 4 | arr[4]=3 | arr[1]=1 | 7+3-1=9 | 9 |
| 3 | 5 | arr[5]=2 | arr[2]=5 | 9+2-5=6 | 9 |

**Complexity:** O(n) time, O(1) space — vastly better than the brute-force O(n·k).

> **Interview Tip:** Sliding window turns an O(n·k) brute force into O(n) by reusing the previous window's sum instead of recomputing it.

---

## 6.2 Prefix Sum

### Definition
`prefix[i]` = sum of `arr[0..i]`. Enables O(1) range-sum queries after O(n) preprocessing.

### Why It Exists
Answering many "sum of range [l, r]" queries naively costs O(n) each; prefix sums reduce each query to O(1) after one O(n) pass.

### ASCII Diagram

```
arr:      [ 3,  1,  4,  1,  5,  9 ]
prefix:   [ 3,  4,  8,  9, 14, 23 ]
           (prefix[i] = prefix[i-1] + arr[i])

Range sum query [l=1, r=4] (inclusive):
sum = prefix[4] - prefix[0] = 14 - 3 = 11
Check: arr[1]+arr[2]+arr[3]+arr[4] = 1+4+1+5 = 11 ✓
```

### Python Implementation

```python
def build_prefix(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

def range_sum(prefix, l, r):
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l - 1]
```

### Dry Run — Build + Query

| Step | i | prefix[i] = prefix[i-1] + arr[i] | prefix array |
|---|---|---|---|
| 0 | 0 | base case = arr[0] = 3 | [3] |
| 1 | 1 | 3 + 1 = 4 | [3, 4] |
| 2 | 2 | 4 + 4 = 8 | [3, 4, 8] |
| 3 | 3 | 8 + 1 = 9 | [3, 4, 8, 9] |
| 4 | 4 | 9 + 5 = 14 | [3, 4, 8, 9, 14] |
| 5 | 5 | 14 + 9 = 23 | [3, 4, 8, 9, 14, 23] |

**Complexity:** Build O(n), query O(1), space O(n).

### Edge Cases
- `l = 0` must be handled specially (no `prefix[l-1]` to subtract).
- Empty array — no valid queries.

### Common Mistakes
- Off-by-one: forgetting the `l == 0` special case causes an `IndexError` or wrong result with `prefix[-1]`.
- Using prefix sums to answer *range update* queries directly — that's the job of a difference array (next section), not a prefix sum.

---

## 6.3 Suffix Sum

### Definition
`suffix[i]` = sum of `arr[i..n-1]`. Mirror image of prefix sum, built right-to-left.

### Python Implementation

```python
def build_suffix(arr):
    n = len(arr)
    suffix = [0] * n
    suffix[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]
    return suffix
```

### ASCII Diagram

```
arr:      [ 3,  1,  4,  1,  5,  9 ]
suffix:   [23, 20, 19, 15, 14,  9 ]
```

> **Use Case:** Problems needing both "everything to the left" and "everything to the right" of each index simultaneously (e.g., "product of array except self," "check if index splits array into two equal-sum halves").

---

## 6.4 Difference Array

### Definition
A difference array `diff` lets you apply **range updates** (add a value to every element in `[l, r]`) in O(1) each, then recover the final array with one O(n) prefix-sum pass.

### Why It Exists
Without it, applying `m` range updates directly costs O(n) each → O(n·m) total. With a difference array, it's O(1) per update → O(n + m) total.

### ASCII Diagram

```
Goal: add +5 to arr[1..3] where arr = [0,0,0,0,0,0]

diff array trick:
diff[l]   += value      -> diff[1] += 5
diff[r+1] -= value      -> diff[4] -= 5

diff:    [0, 5, 0, 0, -5, 0]
prefix-sum diff to recover actual array:
result:  [0, 5, 5, 5,  0, 0]
                ^  ^  ^
           indices 1,2,3 got +5, exactly as intended
```

### Python Implementation

```python
def build_diff(n):
    return [0] * (n + 1)

def range_update(diff, l, r, value):
    diff[l] += value
    diff[r + 1] -= value        # requires diff to have size n+1

def apply_diff(diff, n):
    result = [0] * n
    result[0] = diff[0]
    for i in range(1, n):
        result[i] = result[i - 1] + diff[i]
    return result
```

### Dry Run — Two Range Updates on `n=6` array

```
Start: diff = [0,0,0,0,0,0,0]
Update 1: range_update(diff, 1, 3, +5)  -> diff[1]+=5, diff[4]-=5
          diff = [0,5,0,0,-5,0,0]
Update 2: range_update(diff, 2, 5, +3)  -> diff[2]+=3, diff[6]-=3
          diff = [0,5,3,0,-5,0,-3]

apply_diff -> prefix sum of diff[0..5]:
i=0: 0
i=1: 0+5=5
i=2: 5+3=8
i=3: 8+0=8
i=4: 8+(-5)=3
i=5: 3+0=3

Final array: [0, 5, 8, 8, 3, 3]
```

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Update 1 contributes | 0 | 5 | 5 | 5 | 0 | 0 |
| Update 2 contributes | 0 | 0 | 3 | 3 | 3 | 3 |
| **Total** | **0** | **5** | **8** | **8** | **3** | **3** |

**Complexity:** O(1) per update, O(n) to materialize final array — vs O(n) per update naively.

### Common Mistakes
- Allocating `diff` with size `n` instead of `n+1` → `IndexError` when `r == n-1` (since `r+1 == n`).
- Forgetting to run the final prefix-sum pass — the `diff` array itself is **not** the answer.

---

## 6.5 Frequency / Counting Array

### Definition
An auxiliary array (or hash map) where `count[v]` stores how many times value `v` appears.

```python
def counting_array(arr, max_val):
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1
    return count
```

> **When to use an array vs a `dict`/`Counter`:** Use a plain array when values are bounded and small (e.g., `0..255` for byte values); use `Counter`/`dict` when values are large, negative, or sparse.

### Use Case: Counting Sort (mentioned for context only — sorting algorithms are covered in their own handbook)

---

## 6.6 Index Marking / Sign Marking

### Definition
An in-place technique that uses the **sign** of existing array values as a marker (0 extra space), commonly used for "find all duplicates/missing numbers in range `[1, n]`" problems.

### ASCII Diagram

```
arr = [4, 3, 2, 7, 8, 2, 3, 1]     (values in range 1..8)

For each value v, mark index (|v|-1) as visited by negating it:

Visit 4 -> negate arr[3]:     [4, 3, 2, -7, 8, 2, 3, 1]
Visit 3 -> negate arr[2]:     [4, 3, -2, -7, 8, 2, 3, 1]
Visit 2 -> negate arr[1]:     [4, -3, -2, -7, 8, 2, 3, 1]
Visit 7 -> negate arr[6]:     [4, -3, -2, -7, 8, 2, -3, 1]
Visit 8 -> negate arr[7]:     [4, -3, -2, -7, 8, 2, -3, -1]
Visit 2 -> arr[1] ALREADY negative -> 2 is a DUPLICATE!
...
```

### Python Implementation — Find All Duplicates in `1..n`

```python
def find_duplicates(arr):
    duplicates = []
    for x in arr:
        idx = abs(x) - 1
        if arr[idx] < 0:
            duplicates.append(abs(x))
        else:
            arr[idx] = -arr[idx]
    # restore array if needed
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    return duplicates
```

**Complexity:** O(n) time, O(1) extra space (output list aside).

> **⚠️ Warning:** This technique mutates the array temporarily. Always restore signs afterward if the original array must remain unmodified for the caller.

---

## 6.7 Cyclic Sort

### Definition
For arrays containing values `1..n` (or `0..n-1`) with possible duplicates/missing values, cyclic sort places each value at its "correct" index in O(n) time using swaps, without extra space.

### ASCII Diagram

```
arr = [3, 1, 5, 4, 2]    (values 1..5, target: arr[i] == i+1)

i=0: arr[0]=3, correct home is index 2 -> swap(0,2)
     [5, 1, 3, 4, 2]
i=0: arr[0]=5, correct home is index 4 -> swap(0,4)
     [2, 1, 3, 4, 5]
i=0: arr[0]=2, correct home is index 1 -> swap(0,1)
     [1, 2, 3, 4, 5]
i=0: arr[0]=1 == index+1 -> move to i=1
i=1: arr[1]=2 == index+1 -> move to i=2
... all correctly placed, done.
```

### Python Implementation

```python
def cyclic_sort(arr):
    i = 0
    n = len(arr)
    while i < n:
        correct_idx = arr[i] - 1
        if arr[i] != arr[correct_idx]:
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
        else:
            i += 1
    return arr
```

### Dry Run — `cyclic_sort([3, 1, 5, 4, 2])`

| Step | i | arr[i] | correct_idx | Action | Array State |
|---|---|---|---|---|---|
| 1 | 0 | 3 | 2 | swap(0,2) | [5, 1, 3, 4, 2] |
| 2 | 0 | 5 | 4 | swap(0,4) | [2, 1, 3, 4, 5] |
| 3 | 0 | 2 | 1 | swap(0,1) | [1, 2, 3, 4, 5] |
| 4 | 0 | 1 | 0 | already correct, i=1 | [1, 2, 3, 4, 5] |
| 5-8 | 1..4 | matches | — | i increments | [1, 2, 3, 4, 5] |

**Complexity:** O(n) time (each element is swapped at most once into place), O(1) space.

> **Interview Tip:** Cyclic sort is the go-to technique for "find missing/duplicate number(s) in range `[1,n]`" problems as an alternative to sign marking — it's often considered cleaner to explain on a whiteboard.

---

## 6.8 Array Rotation

### Definition
Shifting all elements by `k` positions, with elements that fall off one end reappearing on the other (circular shift).

### ASCII Diagram — Right Rotation by k=2

```
Original:  [1, 2, 3, 4, 5, 6, 7]
Rotate right by 2:
Last 2 elements move to front:
           [6, 7, 1, 2, 3, 4, 5]
```

### Approach 1 — Brute Force (extra array)

```python
def rotate_bruteforce(arr, k):
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k]
```
**Complexity:** O(n) time, O(n) space.

### Approach 2 — One Rotation at a Time (k passes)

```python
def rotate_one_at_a_time(arr, k):
    n = len(arr)
    for _ in range(k % n):
        last = arr.pop()
        arr.insert(0, last)
    return arr
```
**Complexity:** O(n·k) time (each `insert(0,x)` is O(n)), O(1) extra space. Inefficient for large `k`.

### Approach 3 — Reversal Algorithm (Optimal, In-Place)

```python
def reverse_range(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def rotate_optimal(arr, k):
    n = len(arr)
    k %= n
    reverse_range(arr, 0, n - 1)      # reverse whole array
    reverse_range(arr, 0, k - 1)        # reverse first k
    reverse_range(arr, k, n - 1)          # reverse remaining n-k
    return arr
```

### Dry Run — `rotate_optimal([1,2,3,4,5,6,7], 2)`

| Step | Operation | Array State |
|---|---|---|
| 0 | Initial | [1,2,3,4,5,6,7] |
| 1 | Reverse whole array (0,6) | [7,6,5,4,3,2,1] |
| 2 | Reverse first k=2 (0,1) | [6,7,5,4,3,2,1] |
| 3 | Reverse remaining (2,6) | [6,7,1,2,3,4,5] |

**Why this works:** Reversing the whole array puts elements in reverse order globally; reversing the two segments independently "un-reverses" each segment locally while preserving the global rotation.

**Complexity:** O(n) time, O(1) space — this is the answer interviewers want.

### Rotation Approach Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| Extra array (slicing) | O(n) | O(n) | Simple, not in-place |
| One-at-a-time | O(n·k) | O(1) | Simple but slow for large k |
| Reversal algorithm | O(n) | O(1) | Optimal — preferred in interviews |

### Edge Cases
- `k == 0` or `k` is a multiple of `n` — no visible change.
- `k > n` — always reduce with `k %= n` first.
- Negative `k` (rotate left instead) — normalize with `k = k % n` (Python's `%` already returns non-negative for positive `n`).

---

## 6.9 Array Reversal Patterns

Beyond whole-array reversal (Section 4.8), reversal is also used as a **building block** — e.g., in rotation (above) and in "reverse words in a sentence"-style array-of-tokens problems.

### Reverse in Segments (k-group reversal)

```python
def reverse_in_k_groups(arr, k):
    n = len(arr)
    for start in range(0, n, k):
        end = min(start + k, n) - 1
        l, r = start, end
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return arr
```

### ASCII Diagram — Reverse in Groups of 3

```
arr = [1,2,3,4,5,6,7,8]
Group [1,2,3] -> [3,2,1]
Group [4,5,6] -> [6,5,4]
Group [7,8]   -> [8,7]     (partial group still reversed)
Result: [3,2,1,6,5,4,8,7]
```

---

## 6.10 Kadane's Algorithm

### Definition
Finds the maximum sum of a **contiguous** subarray in O(n) time by tracking, at each index, the best sum of a subarray *ending* at that index.

### Why It Exists
Brute force checks all O(n²) subarrays; Kadane's realizes that the best subarray ending at `i` is either `arr[i]` alone, or `arr[i]` extending the best subarray ending at `i-1` — a classic "local optimum builds global optimum" (DP-flavored, but taught here purely as an array pattern).

### ASCII Diagram

```
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_max at each index (reset to arr[i] if negative running sum):
idx:     0   1   2   3   4   5   6   7   8
val:    -2   1  -3   4  -1   2   1  -5   4
curmax: -2   1  -2   4   3   5   6   1   5
global:  -2   1   1   4   4   5   6   6   6

Best subarray: [4, -1, 2, 1] -> sum = 6
```

### Python Implementation

```python
def kadane(arr):
    current_max = global_max = arr[0]
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        global_max = max(global_max, current_max)
    return global_max
```

### Line-by-Line Explanation
1. Initialize both trackers to `arr[0]` — the smallest valid subarray is a single element.
2. At each step, decide: does extending the previous subarray help, or is starting fresh at `arr[i]` better? Take the max.
3. Update the global best seen so far.

### Dry Run — `kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])`

| i | arr[i] | current_max = max(arr[i], current_max+arr[i]) | global_max |
|---|---|---|---|
| 0 | -2 | -2 (init) | -2 |
| 1 | 1 | max(1, -2+1=-1) = 1 | 1 |
| 2 | -3 | max(-3, 1-3=-2) = -2 | 1 |
| 3 | 4 | max(4, -2+4=2) = 4 | 4 |
| 4 | -1 | max(-1, 4-1=3) = 3 | 4 |
| 5 | 2 | max(2, 3+2=5) = 5 | 5 |
| 6 | 1 | max(1, 5+1=6) = 6 | 6 |
| 7 | -5 | max(-5, 6-5=1) = 1 | 6 |
| 8 | 4 | max(4, 1+4=5) = 5 | 6 |

**Final answer:** 6

**Complexity:** O(n) time, O(1) space.

### Variation — Also Return the Subarray Itself

```python
def kadane_with_indices(arr):
    current_max = global_max = arr[0]
    start = end = temp_start = 0
    for i in range(1, len(arr)):
        if arr[i] > current_max + arr[i]:
            current_max = arr[i]
            temp_start = i
        else:
            current_max += arr[i]
        if current_max > global_max:
            global_max = current_max
            start, end = temp_start, i
    return global_max, arr[start:end + 1]
```

### Variation — Minimum Subarray Sum
Flip the comparison (`min` instead of `max`), or negate all values and reuse `kadane`.

```python
def min_subarray_sum(arr):
    return -kadane([-x for x in arr])
```

### Edge Cases
- All negative numbers — the answer is the single largest (least negative) element, which the algorithm handles correctly because it always starts `current_max` from `arr[0]`.
- Single-element array — trivially returns that element.
- Empty array — undefined; guard explicitly if required by the problem.

### Common Mistakes
- Initializing `current_max`/`global_max` to `0` instead of `arr[0]` — breaks on all-negative arrays.
- Forgetting Kadane's finds *contiguous* subarrays only (not arbitrary subsets).

---

## 6.11 Majority Element (Boyer-Moore Voting)

### Definition
Find the element that appears more than `n/2` times, in O(n) time and O(1) space.

### ASCII Diagram

```
arr = [2, 2, 1, 1, 1, 2, 2]

candidate=None, count=0
2: candidate=2, count=1
2: count=2
1: count=1
1: count=0
1: candidate=1, count=1
2: count=0
2: candidate=2, count=1

Final candidate: 2  (verify: 2 appears 4 times > 7/2 = 3.5 ✓)
```

### Python Implementation

```python
def majority_element(arr):
    candidate, count = None, 0
    for x in arr:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate    # verify separately if majority isn't guaranteed to exist
```

**Complexity:** O(n) time, O(1) space.

> **Interview Tip:** This algorithm assumes a majority element *exists*. If not guaranteed, add a second pass to verify `arr.count(candidate) > len(arr) // 2`.

---

## 6.12 Dutch National Flag / Partitioning

### Definition
Partition an array into three regions (e.g., 0s, 1s, 2s) in a single O(n) pass using three pointers, without extra space.

### ASCII Diagram

```
arr = [2, 0, 2, 1, 1, 0]

low, mid, high pointers partition into:
[ 0s region | 1s region | unprocessed | 2s region ]
      low          mid          ^          high
```

### Python Implementation

```python
def dutch_flag_sort(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # mid NOT incremented — must re-examine swapped-in value
    return arr
```

### Dry Run — `dutch_flag_sort([2, 0, 2, 1, 1, 0])`

| Step | low | mid | high | arr[mid] | Action | Array State |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 5 | 2 | swap(mid,high), high-- | [0,0,2,1,1,2] |
| 1 | 0 | 0 | 4 | 0 | swap(low,mid), low++, mid++ | [0,0,2,1,1,2] |
| 2 | 1 | 1 | 4 | 0 | swap(low,mid), low++, mid++ | [0,0,2,1,1,2] |
| 3 | 2 | 2 | 4 | 2 | swap(mid,high), high-- | [0,0,1,1,2,2] |
| 4 | 2 | 2 | 3 | 1 | mid++ | [0,0,1,1,2,2] |
| 5 | 2 | 3 | 3 | 1 | mid++ | [0,0,1,1,2,2] |
| 6 | 2 | 4 | 3 | loop ends (mid > high) | — | [0,0,1,1,2,2] |

**Complexity:** O(n) time, O(1) space, single pass.

> **Common Mistake:** Incrementing `mid` after swapping with `high` — you must re-check the newly swapped-in value at `mid`, since it hasn't been classified yet.

---

## 6.13 Bucket Counting

### Definition
Distribute elements into fixed "buckets" based on a computed key (e.g., value range, digit, remainder) to enable O(n) counting-based solutions.

### Python Example — Group Numbers by Remainder mod k

```python
def bucket_by_mod(arr, k):
    buckets = [[] for _ in range(k)]
    for x in arr:
        buckets[x % k].append(x)
    return buckets
```

### ASCII Diagram

```
arr = [1,2,3,4,5,6,7,8,9], k=3

bucket[0]: 3, 6, 9
bucket[1]: 1, 4, 7
bucket[2]: 2, 5, 8
```

> **Use Case:** Basis for counting sort and radix sort (mentioned only for context — sorting itself is out of scope for this handbook).

---

## Chapter 6 Summary & Cheat Sheet

| Pattern | Recognition Trigger | Time | Space |
|---|---|---|---|
| Two Pointers | Sorted array, pair/triplet sum | O(n) | O(1) |
| Sliding Window | Contiguous subarray, fixed/variable size | O(n) | O(1) |
| Prefix Sum | Many range-sum queries | O(n) build, O(1) query | O(n) |
| Suffix Sum | "Everything to the right" queries | O(n) | O(n) |
| Difference Array | Many range-update queries | O(1) update | O(n) |
| Frequency Array | Bounded-value counting | O(n) | O(k) |
| Sign Marking | Find duplicates/missing in `1..n`, in-place | O(n) | O(1) |
| Cyclic Sort | Values `1..n`, find missing/duplicate | O(n) | O(1) |
| Rotation (reversal algo) | Rotate array by k | O(n) | O(1) |
| Kadane's | Max/min contiguous subarray sum | O(n) | O(1) |
| Majority Vote | Element appearing > n/2 times | O(n) | O(1) |
| Dutch Flag | 3-way partition | O(n) | O(1) |
| Bucket Counting | Grouping by computed key | O(n) | O(n) |

### Formula Sheet

```
prefix[i] = prefix[i-1] + arr[i]
range_sum(l, r) = prefix[r] - prefix[l-1]   (prefix[r] if l == 0)

diff[l] += val ; diff[r+1] -= val           (range update)
result[i] = result[i-1] + diff[i]            (recover array)

rotate right by k:
    reverse(0, n-1); reverse(0, k-1); reverse(k, n-1)

kadane: current_max = max(arr[i], current_max + arr[i])
```

### Common Mistakes
- Off-by-one in prefix sum range queries (forgetting the `l==0` case).
- Difference array sized `n` instead of `n+1`.
- Forgetting sign-marking mutates the array — restore it if required.
- Incrementing `mid` after a high-swap in Dutch flag partitioning.
- Initializing Kadane's trackers to 0 instead of `arr[0]`.

### Frequently Asked Questions

**Q: When do I use prefix sum vs difference array?**
A: Prefix sum answers *range sum queries* fast after the array is fixed. Difference array answers *range update* operations fast, before finally materializing the array once.

**Q: Is cyclic sort the same as sign marking?**
A: Both solve similar "missing/duplicate in `1..n`" problems in O(1) space, but cyclic sort physically rearranges the array into sorted order as a side effect, while sign marking only flips signs as visited markers.

### Practice Problems
1. Implement a variable-size sliding window to find the smallest subarray with sum ≥ target.
2. Use a difference array to process `m` "add value to range" queries efficiently, then print the final array.
3. Find all numbers in `[1, n]` missing from an array of size `n` using cyclic sort.
4. Modify Kadane's algorithm to also return the maximum product subarray (note: requires tracking both max and min due to negative numbers).
5. Implement 3-way partitioning without Dutch flag, using extra arrays, and compare space complexity.

---

# Chapter 7: Subarrays

**Learning Objectives:** Master generating, counting, and optimizing over subarrays.
**Prerequisites:** Chapters 1–6.
**Estimated Reading Time:** 35 minutes
**Difficulty Level:** Intermediate
**Topics Covered:** Definition, generation, counting, fixed/variable-length problems, contribution technique.
**Real World Applications:** Time-series window analysis, log-segment analytics.
**Interview Relevance:** Very High.

---

## 7.1 Definition and Properties

A **subarray** is a **contiguous** slice of an array — `arr[i..j]` for `0 ≤ i ≤ j < n`. This is different from a **subsequence**, which need not be contiguous (subsequences belong to a different topic and are only mentioned here for contrast).

```
arr = [1, 2, 3]

Subarrays:      [1], [2], [3], [1,2], [2,3], [1,2,3]     -> 6 total
Subsequences:   [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3], []  -> 8 total (NOT covered here)
```

### Count of Subarrays
For an array of length `n`, the number of non-empty subarrays is:

```
n * (n + 1) / 2
```

This comes from choosing a start `i` and end `j ≥ i`: for each of the `n` possible starts, there are `n - i` valid ends, and summing `n + (n-1) + ... + 1` gives `n(n+1)/2`.

---

## 7.2 Generating All Subarrays

```python
def all_subarrays(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(i, n):
            result.append(arr[i:j + 1])
    return result
```

### Dry Run — `all_subarrays([1, 2, 3])`

| i | j | arr[i:j+1] |
|---|---|---|
| 0 | 0 | [1] |
| 0 | 1 | [1, 2] |
| 0 | 2 | [1, 2, 3] |
| 1 | 1 | [2] |
| 1 | 2 | [2, 3] |
| 2 | 2 | [3] |

**Complexity:** O(n²) subarrays generated, O(n³) total if you sum each with a naive inner loop (O(n²) generation × O(n) copy), O(n²) if avoiding explicit slicing.

---

## 7.3 Counting Subarrays (Without Generating Them)

### Example: Count Subarrays with Sum Exactly K

```python
from collections import defaultdict

def count_subarrays_with_sum_k(arr, k):
    count = 0
    prefix_sum = 0
    freq = defaultdict(int)
    freq[0] = 1                        # empty prefix
    for x in arr:
        prefix_sum += x
        count += freq[prefix_sum - k]     # how many earlier prefixes make sum==k
        freq[prefix_sum] += 1
    return count
```

### Why This Works
If `prefix_sum[j] - prefix_sum[i] == k`, then the subarray `(i, j]` sums to `k`. Rearranging: `prefix_sum[i] == prefix_sum[j] - k`. So at each step we ask "how many earlier prefix sums equal `current_prefix_sum - k`?"

### Dry Run — `count_subarrays_with_sum_k([1, 2, 3, -2, 5], 3)`

| Step | x | prefix_sum | freq[prefix_sum-k] (before update) | count | freq after update |
|---|---|---|---|---|---|
| init | — | 0 | — | 0 | {0:1} |
| 1 | 1 | 1 | freq[1-3=-2]=0 | 0 | {0:1, 1:1} |
| 2 | 2 | 3 | freq[3-3=0]=1 | 1 | {0:1,1:1,3:1} |
| 3 | 3 | 6 | freq[6-3=3]=1 | 2 | {0:1,1:1,3:1,6:1} |
| 4 | -2 | 4 | freq[4-3=1]=1 | 3 | {...,4:1} |
| 5 | 5 | 9 | freq[9-3=6]=1 | 4 | {...,9:1} |

**Answer: 4** subarrays sum to 3. **Complexity:** O(n) time, O(n) space — a huge improvement over the O(n²) brute force of checking every subarray sum directly.

---

## 7.4 Fixed-Length Subarray Problems

Solved with a fixed-size sliding window (see Section 6.1.3). Classic examples: "max sum of any `k` consecutive elements," "average of every window of size `k`."

---

## 7.5 Variable-Length Subarray Problems

Solved with a variable-size sliding window that expands/shrinks based on a condition.

### Example: Smallest Subarray with Sum ≥ Target

```python
def smallest_subarray_ge_target(arr, target):
    left = 0
    window_sum = 0
    best_len = float('inf')
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum >= target:
            best_len = min(best_len, right - left + 1)
            window_sum -= arr[left]
            left += 1
    return best_len if best_len != float('inf') else 0
```

### Dry Run — `smallest_subarray_ge_target([2, 1, 5, 2, 3, 2], 7)`

| right | arr[right] | window_sum | Shrink? | left | best_len |
|---|---|---|---|---|---|
| 0 | 2 | 2 | No (2<7) | 0 | inf |
| 1 | 1 | 3 | No | 0 | inf |
| 2 | 5 | 8 | Yes (8≥7) | shrink to left=1, sum=6 | 3 |
| 3 | 2 | 8 | Yes (8≥7) | shrink to left=2, sum=7... continue shrinking while ≥7 | keep shrinking |
| — | — | — | after shrinking fully | left=3, sum=2 | best_len=2 (window [5,2]) |
| 4 | 3 | 5 | No | 3 | 2 |
| 5 | 2 | 7 | Yes | shrink | best_len stays 2 |

**Final answer: 2** (subarray `[5, 2]`). **Complexity:** O(n) — each element is added and removed from the window at most once, giving amortized O(n) despite the nested-looking `while`.

---

## 7.6 Maximum / Minimum Sum Subarray

Covered in full via Kadane's algorithm (Section 6.10). Brute force alternative for comparison:

```python
def max_subarray_bruteforce(arr):
    n = len(arr)
    best = float('-inf')
    for i in range(n):
        current = 0
        for j in range(i, n):
            current += arr[j]
            best = max(best, current)
    return best
```

**Complexity:** O(n²) time, O(1) space — always mention this as the "brute force to beat" before presenting Kadane's O(n) solution in an interview.

---

## 7.7 Contribution Technique

### Definition
Instead of summing over subarrays, sum over **elements**, computing how many subarrays each element contributes to (and its total contribution), then combine.

### Example: Sum of Minimums of All Subarrays (conceptual overview)
For each element `arr[i]`, count how many subarrays have `arr[i]` as their minimum, using the distance to the nearest smaller element on the left and right. This turns an O(n²) or O(n³) brute force into O(n) using a monotonic-stack-assisted count (the stack mechanics themselves belong to a separate handbook; here we focus on the array-side idea: **total contribution = value × count of subarrays where it's the extremal element**).

```
arr = [3, 1, 2, 4]

Contribution of value 1 (index 1): it's the minimum of every subarray
that includes index 1 without crossing another 1 — here, all subarrays
spanning index 1: [3,1],[1],[1,2],[3,1,2],[1,2,4],[3,1,2,4] etc.
```

> **Interview Tip:** The contribution technique is a mindset shift: "how much does *this element* contribute across all valid subarrays?" rather than "what is the answer *for this subarray*?" It's especially powerful for sum-of-min / sum-of-max / sum-of-products style aggregate questions.

---

## Chapter 7 Summary & Cheat Sheet

- Number of non-empty subarrays of length `n` = `n(n+1)/2`.
- Subarrays are **contiguous**; subsequences are not (out of scope here).
- Prefix-sum + hashmap turns "count subarrays with sum K" from O(n²) to O(n).
- Variable-size sliding window solves "smallest/largest subarray satisfying a condition" in O(n).
- Contribution technique reframes subarray aggregation problems around individual elements.

### Common Mistakes
- Confusing subarrays (contiguous) with subsequences (not necessarily contiguous).
- Forgetting `freq[0] = 1` when counting subarrays with sum K (accounts for a prefix that itself equals K).
- Using a fixed-size window template for a variable-length problem, or vice versa.

### Frequently Asked Questions

**Q: How many subarrays does an array of length `n` have, including the empty one?**
A: `n(n+1)/2 + 1` if you count the empty subarray; most interview problems only count non-empty subarrays (`n(n+1)/2`).

### Practice Problems
1. Count the number of subarrays with an even sum.
2. Find the longest subarray with sum exactly K (not just count — return length).
3. Find the maximum length of a subarray with equal number of 0s and 1s.
4. Using the contribution technique, compute the sum of subarray minimums for a small example array by hand.

---

# Chapter 8: Matrices (Arrays of Arrays)

**Learning Objectives:** Treat 2D structures purely as an extension of array concepts — traversal, transformation, and simulation.
**Prerequisites:** Chapters 1–7.
**Estimated Reading Time:** 45 minutes
**Difficulty Level:** Intermediate
**Topics Covered:** Representation, traversal, transpose, rotation, boundary/diagonal/spiral/zigzag traversal, 2D prefix sum, 2D difference array.
**Real World Applications:** Image processing, game boards, spreadsheet engines, heatmaps.
**Interview Relevance:** High — matrix problems are a recurring interview category.

---

## 8.1 Representation

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
rows, cols = len(matrix), len(matrix[0])
```

```
Row 0: [1, 2, 3]
Row 1: [4, 5, 6]
Row 2: [7, 8, 9]

matrix[r][c] -> row r, column c
matrix[1][2] -> 6
```

## 8.2 Traversal

```python
# Row-major traversal
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c])

# Column-major traversal
for c in range(cols):
    for r in range(rows):
        print(matrix[r][c])
```

## 8.3 Transpose

### Definition
Flip a matrix over its main diagonal: `transposed[c][r] = matrix[r][c]`.

```
Original:        Transposed:
1 2 3            1 4 7
4 5 6    -->     2 5 8
7 8 9            3 6 9
```

### Python Implementation

```python
def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            result[c][r] = matrix[r][c]
    return result

# Pythonic one-liner using zip (for rectangular matrices)
def transpose_zip(matrix):
    return [list(row) for row in zip(*matrix)]
```

**Complexity:** O(rows × cols) time, O(rows × cols) space.

## 8.4 Rotation

### 90° Clockwise Rotation — Transpose + Reverse Each Row

```
1 2 3        1 4 7        7 4 1
4 5 6  --->  2 5 8  --->  8 5 2   (transpose, then reverse each row)
7 8 9        3 6 9        9 6 3
```

```python
def rotate_90_clockwise(matrix):
    n = len(matrix)
    # transpose in place
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    # reverse each row
    for row in matrix:
        row.reverse()
    return matrix
```

### Dry Run — `rotate_90_clockwise([[1,2,3],[4,5,6],[7,8,9]])`

| Step | Operation | Matrix State |
|---|---|---|
| 0 | Initial | [[1,2,3],[4,5,6],[7,8,9]] |
| 1 | Transpose (swap upper/lower triangle) | [[1,4,7],[2,5,8],[3,6,9]] |
| 2 | Reverse each row | [[7,4,1],[8,5,2],[9,6,3]] |

**Complexity:** O(n²) time, O(1) extra space (in-place for square matrices).

> **Interview Tip:** 90° counter-clockwise rotation is "reverse each row first, then transpose" (or equivalently, transpose then reverse each column) — memorize the transpose+reverse trick and derive the direction rather than memorizing four separate cases.

## 8.5 Boundary Traversal

### ASCII Diagram

```
 1   2   3   4
 5   6   7   8
 9  10  11  12
13  14  15  16

Boundary order: 1,2,3,4, 8,12,16, 15,14,13, 9,5
(top row L->R, right col top->bottom skipping corner,
 bottom row R->L skipping corner, left col bottom->top skipping both corners)
```

```python
def boundary_traversal(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = []
    if rows == 1:
        return matrix[0][:]
    if cols == 1:
        return [row[0] for row in matrix]

    # top row
    result.extend(matrix[0])
    # right column (excluding top-right corner already added)
    for r in range(1, rows):
        result.append(matrix[r][cols - 1])
    # bottom row, right to left (excluding bottom-right corner already added)
    for c in range(cols - 2, -1, -1):
        result.append(matrix[rows - 1][c])
    # left column, bottom to top (excluding both corners already added)
    for r in range(rows - 2, 0, -1):
        result.append(matrix[r][0])
    return result
```

**Complexity:** O(rows + cols) time — not O(rows × cols), since only boundary cells are visited.

## 8.6 Diagonal Traversal

```
1  2  3
4  5  6
7  8  9

Main diagonal (top-left to bottom-right): 1, 5, 9
Anti-diagonal (top-right to bottom-left): 3, 5, 7
```

```python
def main_diagonal(matrix):
    return [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]

def anti_diagonal(matrix):
    n = len(matrix)
    return [matrix[i][n - 1 - i] for i in range(n)]
```

## 8.7 Spiral Traversal

### ASCII Diagram

```
 1   2   3   4
 5   6   7   8
 9  10  11  12
13  14  15  16

Spiral order: 1,2,3,4, 8,12,16, 15,14,13, 9,5, 6,7, 11,10
```

```python
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for c in range(left, right + 1):          # move right along top row
            result.append(matrix[top][c])
        top += 1

        for r in range(top, bottom + 1):            # move down along right column
            result.append(matrix[r][right])
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):      # move left along bottom row
                result.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):        # move up along left column
                result.append(matrix[r][left])
            left += 1

    return result
```

### Dry Run — `spiral_order` on the 4x4 matrix above

| Round | top | bottom | left | right | Elements Added |
|---|---|---|---|---|---|
| 1 | 0 | 3 | 0 | 3 | 1,2,3,4 (top row) → top=1 |
| 1 | 1 | 3 | 0 | 3 | 8,12,16 (right col) → right=2 |
| 1 | 1 | 3 | 0 | 2 | 15,14,13 (bottom row) → bottom=2 |
| 1 | 1 | 2 | 0 | 2 | 9,5 (left col) → left=1 |
| 2 | 1 | 2 | 1 | 2 | 6,7 (top row) → top=2 |
| 2 | 2 | 2 | 1 | 2 | 11 (right col) → right=1 |
| 2 | 2 | 2 | 1 | 1 | 10 (bottom row, since top<=bottom) → bottom=1 |
| — | loop ends (top > bottom) | | | | |

**Final:** `[1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]`. **Complexity:** O(rows × cols) time, O(1) extra space (excluding output).

## 8.8 Snake / Zigzag Traversal

```
1  2  3
4  5  6
7  8  9

Snake order: 1,2,3, 6,5,4, 7,8,9   (alternate row direction each row)
```

```python
def snake_traversal(matrix):
    result = []
    for r, row in enumerate(matrix):
        result.extend(row if r % 2 == 0 else row[::-1])
    return result
```

**Complexity:** O(rows × cols) time and space.

## 8.9 2D Prefix Sum

### Definition
`prefix[r][c]` = sum of all elements in the rectangle from `(0,0)` to `(r,c)` inclusive. Enables O(1) rectangular range-sum queries.

### Formula

```
prefix[r][c] = matrix[r][c]
             + prefix[r-1][c]        (sum above)
             + prefix[r][c-1]         (sum to the left)
             - prefix[r-1][c-1]        (remove double-counted overlap)
```

### ASCII Diagram — Inclusion-Exclusion

```
+-------------------+---+
|                    |   |
|   prefix[r-1][c-1] |also counted in
|   double-counted   | prefix[r][c-1]|
+--------------------+---+
| prefix[r-1][c]     | matrix[r][c] |
| (also counted in   |              |
|  prefix[r][c-1])   |              |
+--------------------+--------------+
```

### Python Implementation

```python
def build_2d_prefix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            prefix[r][c] = (matrix[r-1][c-1]
                             + prefix[r-1][c]
                             + prefix[r][c-1]
                             - prefix[r-1][c-1])
    return prefix

def region_sum(prefix, r1, c1, r2, c2):
    # inclusive 0-indexed rectangle (r1,c1) to (r2,c2) on the ORIGINAL matrix
    r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
    return (prefix[r2][c2] - prefix[r1-1][c2]
            - prefix[r2][c1-1] + prefix[r1-1][c1-1])
```

**Complexity:** Build O(rows×cols), query O(1), space O(rows×cols).

> **Interview Tip:** Using a `(rows+1) x (cols+1)` prefix grid (with a padding row/column of zeros) eliminates all boundary special-casing — always do this instead of hand-checking `r==0`/`c==0`.

## 8.10 2D Difference Array

### Definition
The 2D analogue of Section 6.4 — apply O(1) rectangular range updates, then recover the final matrix with a 2D prefix-sum pass.

```python
def build_2d_diff(rows, cols):
    return [[0] * (cols + 1) for _ in range(rows + 1)]

def range_update_2d(diff, r1, c1, r2, c2, value):
    diff[r1][c1] += value
    diff[r1][c2 + 1] -= value
    diff[r2 + 1][c1] -= value
    diff[r2 + 1][c2 + 1] += value

def apply_2d_diff(diff, rows, cols):
    result = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            result[r][c] = diff[r][c]
            if r > 0: result[r][c] += result[r-1][c]
            if c > 0: result[r][c] += result[r][c-1]
            if r > 0 and c > 0: result[r][c] -= result[r-1][c-1]
    return result
```

**Complexity:** O(1) per rectangular update, O(rows×cols) to materialize the final matrix.

---

## Chapter 8 Summary & Cheat Sheet

| Operation | Time | Space |
|---|---|---|
| Traversal (row/col major) | O(rows×cols) | O(1) extra |
| Transpose | O(rows×cols) | O(1) in-place (square) |
| 90° Rotation | O(n²) | O(1) in-place (square) |
| Boundary traversal | O(rows+cols) | O(1) extra |
| Spiral traversal | O(rows×cols) | O(1) extra |
| 2D prefix sum build | O(rows×cols) | O(rows×cols) |
| 2D prefix sum query | O(1) | — |
| 2D difference update | O(1) | — |

### Formula Sheet

```
Transpose: result[c][r] = matrix[r][c]
Rotate 90° CW: transpose, then reverse each row
Rotate 90° CCW: reverse each row, then transpose

2D prefix:
prefix[r][c] = matrix[r-1][c-1] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]

2D region sum (1-indexed prefix grid):
region = prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]
```

### Common Mistakes
- Forgetting the `-prefix[r-1][c-1]` correction term (double-counting the overlap region).
- Using a non-padded prefix array and mishandling `r==0`/`c==0` edge cases.
- Rotating a **non-square** matrix in place (only square matrices support true in-place rotation — rectangular matrices need a new array).
- Mixing up row-major vs column-major loop order, causing `IndexError` on jagged/ragged input.

### Frequently Asked Questions

**Q: Can I rotate a rectangular (non-square) matrix in place?**
A: Not directly — in-place transpose-then-reverse relies on `rows == cols`. For rectangular matrices, build a new `cols x rows` result matrix instead.

### Practice Problems
1. Implement 180° rotation (two different ways: two 90° rotations, or direct reversal of both rows and columns).
2. Given `q` rectangular sum queries on a fixed matrix, answer all of them in O(rows×cols + q) total.
3. Implement anti-diagonal (bottom-left to top-right) traversal for a non-square matrix.
4. Given `q` "add value to submatrix" updates, output the final matrix efficiently using a 2D difference array.

---

# Chapter 9: Dry Run Framework

**Learning Objectives:** Develop a repeatable method for manually tracing any array algorithm.
**Prerequisites:** Chapters 1–8.
**Estimated Reading Time:** 20 minutes
**Difficulty Level:** Beginner → Intermediate
**Topics Covered:** Variable tracing, index tracing, prefix/diff tracing, Kadane tracing, whiteboard technique.
**Real World Applications:** Debugging, code review, interview whiteboarding.
**Interview Relevance:** Extremely High — interviewers grade *how* you verify your solution as much as the solution itself.

---

## 9.1 How to Trace Variables and Indexes

A disciplined dry run always uses a table with these columns:

```
| Step | Loop Variable(s) | Relevant Array State | Other Tracked Variables | Notes/Decision |
```

**Method:**
1. Write the initial state of every variable **before** the loop starts (this catches initialization bugs immediately).
2. For each iteration, update exactly one row — never skip iterations, even "obvious" ones, until you've built the habit.
3. Explicitly write out **why** a branch was taken (e.g., "8 ≥ 7 → shrink window") rather than just the resulting numbers.
4. After the loop, write a final row confirming the **exit condition** that was hit — this is where off-by-one bugs hide.

> **Tip:** In an interview, narrate your dry run out loud even if you're not literally drawing the table — interviewers are listening for this structured reasoning.

## 9.2 Tracing Prefix Sums and Difference Arrays

When tracing prefix-sum-based code, always keep the **original array** visible alongside the prefix array so you can sanity-check with a direct sum. When tracing difference arrays, remember the array itself is not meaningful until the final prefix-sum recovery pass — dry run the *updates* first, then the *recovery* pass, as two separate phases (see Section 6.4 for a full worked example of exactly this two-phase tracing).

## 9.3 Tracing Kadane's Algorithm

Kadane's has exactly two state variables (`current_max`, `global_max`) — always dedicate one column to each, plus a column showing the max(...) decision explicitly, as demonstrated in Section 6.10's dry run table. This prevents the single most common Kadane's bug: silently dropping the "reset vs extend" decision from your trace.

## 9.4 Whiteboard Debugging Techniques

- **Trace with a small, deliberately tricky input** — include a negative number, a duplicate, and a boundary value (0 or the last valid index) rather than a "nice" all-positive array.
- **Trace the *empty* and *single-element* cases mentally first** — many array bugs (division by zero, `arr[0]` on an empty list) only appear here.
- **When a loop uses two pointers, always trace what happens the moment they become equal or cross** — this is where most `<` vs `<=` bugs live.
- **After finishing code, re-derive the invariant** (a one-sentence claim that's true at the top of every loop iteration) and check it against your dry run row by row.

---

## Chapter 9 Summary & Cheat Sheet

- Standard dry-run table: Step | Loop Variables | Array State | Other Variables | Decision/Notes.
- Always dry-run the empty case, single-element case, and a boundary-crossing case explicitly.
- State the loop invariant and verify it holds at every traced step.

### Common Mistakes
- Skipping "obvious" iterations, hiding off-by-one bugs.
- Not tracing the exact loop-exit condition.
- Dry-running only "nice" positive, duplicate-free inputs.

### Frequently Asked Questions

**Q: How much dry-running is "enough" in an interview?**
A: Enough to walk through at least one full non-trivial iteration and the loop's exit condition — you don't need to trace every single index of a large array, just enough to convince the interviewer (and yourself) the logic is correct.

### Practice Problems
1. Dry run `rotate_optimal` (Section 6.8) on an array of length 1.
2. Dry run `dutch_flag_sort` (Section 6.12) on an already-sorted input `[0,1,2]`.
3. Write the loop invariant for `two_sum_sorted` (Section 6.1.2) in one sentence.

---

# Chapter 10: Problem Recognition

**Learning Objectives:** Rapidly map a new problem statement to the correct array pattern.
**Prerequisites:** Chapters 1–9.
**Estimated Reading Time:** 15 minutes
**Difficulty Level:** Intermediate
**Topics Covered:** Decision tree, keyword mapping, observation building.
**Real World Applications:** Speeding up interview problem-solving.
**Interview Relevance:** Extremely High.

---

## 10.1 Recognition Decision Tree

```
Is the array sorted (or can be sorted without breaking the problem)?
├── Yes, and problem involves pairs/triplets summing to a target
│     -> Two Pointers
├── Yes, and problem involves searching -> (binary search; separate handbook)
│
Is the problem about a CONTIGUOUS range/window?
├── Fixed window size given ("every k consecutive elements")
│     -> Fixed Sliding Window
├── Window size unknown, must grow/shrink based on a condition
│     -> Variable Sliding Window
│
Does the problem ask for REPEATED range-sum queries on a static array?
│     -> Prefix Sum (2D Prefix Sum if it's a matrix)
│
Does the problem ask to apply MANY range updates then read the final array?
│     -> Difference Array (2D if it's a matrix)
│
Are array values bounded within [1, n] and does the problem mention
"missing" or "duplicate"?
│     -> Cyclic Sort or Sign Marking
│
Does the problem ask for MAXIMUM/MINIMUM SUM of a CONTIGUOUS subarray?
│     -> Kadane's Algorithm
│
Does the problem mention an element appearing "more than n/2 times"?
│     -> Boyer-Moore Majority Voting
│
Does the problem ask to sort into exactly 3 known categories in one pass?
│     -> Dutch National Flag
│
Does the problem involve rotating or shifting the array circularly?
│     -> Rotation (reversal algorithm)
│
Does the problem involve a 2D grid with directional movement
(spiral/boundary/diagonal/zigzag)?
│     -> Matrix Traversal Patterns (Chapter 8)
```

## 10.2 Keyword-to-Pattern Mapping

| Keyword / Phrase in Problem | Likely Pattern |
|---|---|
| "sorted array," "pair sum," "triplet" | Two Pointers |
| "subarray of size k," "window" | Sliding Window |
| "smallest/longest subarray with..." | Variable Sliding Window |
| "range sum query," "sum between indices" | Prefix Sum |
| "apply updates to a range," "add to interval" | Difference Array |
| "numbers from 1 to n," "find missing/duplicate" | Cyclic Sort / Sign Marking |
| "maximum subarray sum," "best time to buy/sell" | Kadane's |
| "appears more than n/2 times" | Majority Voting |
| "sort colors," "three categories" | Dutch National Flag |
| "rotate array," "shift by k" | Rotation |
| "spiral," "clockwise," "boundary," "diagonal" | Matrix Traversal |
| "in-place," "O(1) extra space" | Look for sign-marking, two-pointer, or reversal-based tricks |

## 10.3 Building Observations

When a problem doesn't map cleanly to a memorized pattern:

1. **Restate constraints precisely** — array size bounds, value ranges, sorted or not, duplicates allowed or not. Constraints eliminate wrong patterns fast (e.g., `10^5` size rules out O(n²)).
2. **Solve a tiny example by hand** and watch what information you keep re-deriving — that's usually the thing to precompute (prefix sum, frequency map, etc.).
3. **Ask what changes between consecutive states** — if moving from index `i` to `i+1` only requires a small update, a sliding-window or prefix-based incremental approach likely applies.
4. **Identify the brute force first**, then ask specifically *why* it's slow — the answer usually points directly at the optimization pattern (repeated summation → prefix sum; repeated scanning → hashmap/frequency array; repeated comparisons → two pointers).

---

## Chapter 10 Summary & Cheat Sheet

- Use constraints to eliminate impossible complexities before choosing an approach.
- Match keywords in the problem statement to the pattern table above as a first guess, then verify against a hand-worked example.
- If nothing matches, ask "why is my brute force slow?" — the bottleneck usually names the pattern.

### Frequently Asked Questions

**Q: What if a problem seems to fit two patterns?**
A: Try the simpler one first (e.g., two pointers before difference array) and check whether it satisfies all constraints — many "hard" problems are actually a single well-known pattern with an extra observation layered on top.

### Practice Problems
1. For each of these problem titles, name the likely pattern: "Maximum Sum Circular Subarray," "Range Sum Query - Immutable," "Corporate Flight Bookings," "Find All Duplicates in an Array."
2. Practice writing your own keyword-to-pattern table entry for a problem you've solved before.

---

# Chapter 11: Optimization

**Learning Objectives:** Systematically move from brute force to optimal solutions.
**Prerequisites:** Chapters 1–10.
**Estimated Reading Time:** 20 minutes
**Difficulty Level:** Intermediate → Advanced
**Topics Covered:** Brute force → better → optimal progression, in-place tricks, space optimization.
**Real World Applications:** Performance-critical systems, interview follow-up questions ("can you do better?").
**Interview Relevance:** Extremely High.

---

## 11.1 Brute Force → Better → Optimal

### Worked Example: "Two Sum" (unsorted array, return indices)

**Brute Force — O(n²) time, O(1) space**
```python
def two_sum_brute(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
    return (-1, -1)
```

**Better — Sort + Two Pointers — O(n log n) time, O(n) space (if indices needed, must track original positions)**
```python
def two_sum_sorted_indices(arr, target):
    indexed = sorted(enumerate(arr), key=lambda p: p[1])
    left, right = 0, len(indexed) - 1
    while left < right:
        s = indexed[left][1] + indexed[right][1]
        if s == target:
            return (indexed[left][0], indexed[right][0])
        elif s < target:
            left += 1
        else:
            right -= 1
    return (-1, -1)
```

**Optimal — Hash Map — O(n) time, O(n) space**
```python
def two_sum_optimal(arr, target):
    seen = {}
    for i, x in enumerate(arr):
        complement = target - x
        if complement in seen:
            return (seen[complement], i)
        seen[x] = i
    return (-1, -1)
```

### Progression Table

| Approach | Time | Space | Key Idea |
|---|---|---|---|
| Brute Force | O(n²) | O(1) | Check every pair |
| Sort + Two Pointers | O(n log n) | O(n) | Sorting enables pointer convergence |
| Hash Map | O(n) | O(n) | Trade space for a single O(1) lookup per element |

> **Interview Tip:** Always state the brute force explicitly, even if you plan to jump straight to the optimal solution — it demonstrates you understand the trade-off you're making, and it's a real fallback if you get stuck mid-optimization.

## 11.2 In-Place Optimization

"In-place" means O(1) extra space (beyond the input and a few scalar variables). Common tricks:

- **Two pointers** to avoid a second array (reversal, partitioning).
- **Sign marking** to reuse the input array itself as a visited-set (Section 6.6).
- **Cyclic sort** to physically place elements at their correct index (Section 6.7).
- **Swap-with-last + pop** for O(1) unordered deletion (Section 4.3).

## 11.3 Space Optimization Tricks

| Technique | Saves | Trade-off |
|---|---|---|
| Reuse input array via sign marking | O(n) auxiliary array | Mutates caller's input (must restore if disallowed) |
| Two-pointer instead of extra array | O(n) space | Sometimes requires sorted input |
| Rolling variables instead of full DP-style array (e.g., Kadane's two scalars) | O(n) → O(1) | Only works when only the previous state is needed |
| Difference array instead of repeated range updates | O(n·m) time | Requires a final materialization pass |

---

## Chapter 11 Summary & Cheat Sheet

- Always articulate three tiers: brute force, better, optimal — and their time/space trade-offs.
- In-place tricks (two pointers, sign marking, cyclic sort, swap-and-pop) are the array toolkit's answer to "can you do this in O(1) space?"
- Space optimization often trades mutability or restoration cost for reduced memory.

### Common Mistakes
- Jumping straight to an "optimal" solution in an interview without stating the brute force baseline first.
- Applying an in-place trick that mutates input the interviewer explicitly said must remain unmodified.

### Frequently Asked Questions

**Q: Is O(n) space always acceptable if it gets O(n) time?**
A: Usually yes for interviews, but always ask/clarify constraints — some problems explicitly require O(1) extra space, which should change your approach (e.g., prefer cyclic sort/sign marking over a hash set).

### Practice Problems
1. Take the brute-force `max_subarray_bruteforce` (Chapter 7) and write out the "better" and "optimal" tiers explicitly, as done for Two Sum above.
2. Convert a hash-set-based duplicate detection solution into an O(1)-space version using sign marking, and state the trade-off.

---

# Chapter 12: Interview Preparation

**Learning Objectives:** Build a targeted, prioritized list of interview questions organized by difficulty, pattern, and company.
**Prerequisites:** Chapters 1–11.
**Estimated Reading Time:** 25 minutes
**Difficulty Level:** All levels
**Topics Covered:** Question bank, pattern index, company notes, interview tricks.
**Real World Applications:** Interview preparation.
**Interview Relevance:** This chapter *is* interview prep.

---

## 12.1 Top Array Interview Questions by Difficulty

### Easy
1. Find the maximum/minimum element in an array.
2. Reverse an array in place.
3. Check if an array is sorted.
4. Move all zeros to the end (in place).
5. Find the second largest element.
6. Remove duplicates from a sorted array (in place).
7. Two Sum (unsorted, return indices).
8. Find the missing number in `[0, n]`.
9. Best Time to Buy and Sell Stock (single transaction).
10. Plus One (increment a number represented as a digit array).

### Medium
1. Maximum Subarray (Kadane's).
2. Product of Array Except Self.
3. Rotate Array by k.
4. 3Sum.
5. Container With Most Water.
6. Subarray Sum Equals K.
7. Set Matrix Zeroes.
8. Spiral Matrix.
9. Rotate Image (matrix 90°).
10. Find All Duplicates in an Array.
11. Gas Station.
12. Sort Colors (Dutch National Flag).
13. Range Sum Query 2D - Immutable.
14. Corporate Flight Bookings (difference array).
15. Minimum Size Subarray Sum.

### Hard
1. Trapping Rain Water.
2. Maximum Sum Circular Subarray.
3. First Missing Positive.
4. Median of Two Sorted Arrays (array perspective only — the merge-based intuition, not the full binary search treatment).
5. Sliding Window Maximum (conceptually — full solution needs a monotonic deque, out of scope here).
6. Longest Consecutive Sequence.

## 12.2 Pattern-Wise Question Bank

| Pattern | Example Problems |
|---|---|
| Two Pointers | Two Sum II, 3Sum, Container With Most Water, Trapping Rain Water |
| Sliding Window | Minimum Size Subarray Sum, Maximum Sum Subarray of Size K, Longest Substring-style array analogues |
| Prefix Sum | Subarray Sum Equals K, Range Sum Query, Product of Array Except Self |
| Difference Array | Corporate Flight Bookings, Range Addition |
| Cyclic Sort / Sign Marking | Find All Duplicates, First Missing Positive, Find the Duplicate Number |
| Kadane's | Maximum Subarray, Maximum Sum Circular Subarray, Best Time to Buy/Sell Stock |
| Majority Voting | Majority Element, Majority Element II |
| Dutch National Flag | Sort Colors |
| Rotation | Rotate Array, Rotate Image |
| Matrix Traversal | Spiral Matrix, Set Matrix Zeroes, Diagonal Traverse |

## 12.3 Company-Wise Notes

> **General Note:** Exact question sets change constantly and are typically under NDA; below are widely known **pattern emphases**, not guaranteed question lists.

| Company (general trend) | Common Emphasis |
|---|---|
| Large tech / FAANG-tier | Optimal time AND space complexity; strong emphasis on clean dry runs and edge cases |
| Fintech / trading firms | Numerical correctness, overflow-style edge cases, performance under scale |
| Startups | Practical problem-solving, working code over perfect asymptotic optimality |

> **Interview Tip:** Don't over-index on "which company asks which exact question" — patterns transfer across companies far more reliably than memorized question lists.

## 12.4 Interview Tricks

- **Always clarify constraints first:** array size, value range, sorted or not, duplicates allowed, negative numbers allowed, can you modify the input.
- **State assumptions out loud** before coding — this converts silent mistakes into a two-second clarifying exchange.
- **Write the brute force signature first**, even in comments, then optimize — it keeps you from getting stuck with a blank editor.
- **Use meaningful variable names** (`left`/`right`, `window_sum`, `prefix`) — interviewers read your dry run through your variable names.
- **Test with edge cases out loud:** empty array, one element, all duplicates, all negative, already sorted/reverse sorted.

---

## Chapter 12 Summary & Cheat Sheet

- Easy tier tests fundamentals; medium tier tests pattern recognition; hard tier tests combining multiple patterns.
- Pattern fluency generalizes far better than memorizing individual questions.
- Always clarify constraints and state the brute force before optimizing.

### Frequently Asked Questions

**Q: How many array problems should I practice before an interview?**
A: Prioritize breadth across patterns (Chapter 6) over sheer volume — roughly 3–5 well-understood problems per pattern is more valuable than 50 problems solved shallowly.

### Practice Problems
Work through at least one problem from each row of the Section 12.2 pattern table, writing the brute force AND optimal solution for each, following the Chapter 11 progression.

---

# Chapter 13: Python Tips for Array Problems

**Learning Objectives:** Use Python's standard library fluently to write faster, cleaner array solutions.
**Prerequisites:** Chapters 1–12.
**Estimated Reading Time:** 20 minutes
**Difficulty Level:** Beginner → Intermediate
**Topics Covered:** Built-ins, `collections`, `itertools`, idioms, performance tips.
**Real World Applications:** Writing production-quality, idiomatic Python.
**Interview Relevance:** High — fluency here saves precious interview minutes.

---

## 13.1 Built-in Functions

```python
arr = [4, 2, 7, 1, 9, 2]

len(arr)                      # 6
sum(arr)                       # 25
min(arr), max(arr)              # 1, 9
sorted(arr)                      # [1,2,2,4,7,9] — new list, O(n log n)
sorted(arr, reverse=True)          # descending
list(enumerate(arr))                # [(0,4),(1,2),(2,7),(3,1),(4,9),(5,2)]
list(zip(arr, arr[1:]))              # adjacent pairs: [(4,2),(2,7),(7,1),(1,9),(9,2)]
all(x > 0 for x in arr)               # True — every element positive
any(x > 8 for x in arr)                # True — at least one element > 8
```

> **Interview Tip:** `zip(arr, arr[1:])` is an extremely handy idiom for "compare each element with the next one" problems without manual index arithmetic.

## 13.2 `collections` Utilities

```python
from collections import Counter, defaultdict, deque

# Counter — frequency counting (Section 4.11)
freq = Counter(arr)
most_common_2 = freq.most_common(2)     # [(2, 2), (4, 1)] top-2 by frequency

# defaultdict — avoids KeyError boilerplate when grouping/counting
groups = defaultdict(list)
for x in arr:
    groups[x % 2].append(x)

# deque — only mentioned here for O(1) append/pop from BOTH ends
# (full usage as a queue/stack belongs to its own handbook)
```

## 13.3 `itertools` Utilities

```python
from itertools import accumulate, combinations, pairwise

list(accumulate(arr))              # running prefix sum! [4,6,13,14,23,25]
list(accumulate(arr, max))          # running maximum: [4,4,7,7,9,9]
list(combinations(arr, 2))           # all pairs (for brute-force pair problems)
list(pairwise(arr))                   # (Python 3.10+) same as zip(arr, arr[1:])
```

> **Interview Tip:** `itertools.accumulate(arr)` computes a prefix sum array in one line — extremely useful once you already understand the underlying algorithm from Section 6.2, but be ready to implement it manually if asked.

## 13.4 Idioms and Performance Tips

```python
# Prefer list comprehensions over manual append loops (faster + more readable)
squares = [x * x for x in arr]              # preferred
squares = []                                   # slower, more verbose
for x in arr:
    squares.append(x * x)

# Avoid repeated len(arr) calls inside hot loops — cache it
n = len(arr)
for i in range(n):
    ...

# Avoid `arr = arr + [x]` in a loop (creates a new list every time, O(n) each) —
# use arr.append(x) instead (O(1) amortized)

# Unpacking for swaps — no temp variable needed
arr[i], arr[j] = arr[j], arr[i]

# Use `in` on a set, not a list, for repeated membership checks
lookup = set(arr)          # O(1) average membership check
if x in lookup: ...          # vs O(n) for `x in arr` on a list
```

---

## Chapter 13 Summary & Cheat Sheet

```python
sum(arr); min(arr); max(arr); sorted(arr)
enumerate(arr); zip(arr, arr[1:]); itertools.pairwise(arr)
Counter(arr); Counter(arr).most_common(k)
itertools.accumulate(arr)              # instant prefix sum
set(arr)                                 # O(1) average membership
```

### Common Mistakes
- Using `arr = arr + [x]` inside a loop instead of `arr.append(x)`.
- Checking membership repeatedly with `x in arr` (O(n) each) instead of converting to a `set` first.
- Recomputing `len(arr)` unnecessarily inside tight loops (minor, but adds up in very hot code).

### Frequently Asked Questions

**Q: Is it acceptable to use `itertools.accumulate` in an interview instead of writing prefix sum manually?**
A: Usually yes for straightforward cases, but be prepared to write it manually if the interviewer wants to see you understand the underlying mechanics.

### Practice Problems
1. Rewrite `build_prefix` (Section 6.2) using `itertools.accumulate` in one line.
2. Use `Counter.most_common()` to solve the Majority Element problem (Section 6.11) and compare its complexity to Boyer-Moore voting.

---

# Chapter 14: Common Mistakes

**Learning Objectives:** Recognize and avoid the most frequent array-related bugs.
**Prerequisites:** Chapters 1–13.
**Estimated Reading Time:** 15 minutes
**Difficulty Level:** All levels
**Topics Covered:** Index errors, aliasing, prefix/diff mistakes, matrix boundary errors, mutation-during-traversal.
**Real World Applications:** Debugging real code, avoiding interview pitfalls.
**Interview Relevance:** Extremely High — these are the bugs interviewers specifically watch for.

---

## 14.1 Index Errors

```python
arr = [1, 2, 3]
arr[3]           # IndexError — valid indices are 0..2
arr[-4]           # IndexError — valid negative indices are -1..-3

# Off-by-one in ranges
for i in range(len(arr)):        # correct: visits 0,1,2
    ...
for i in range(len(arr) + 1):     # WRONG: visits 0,1,2,3 -> IndexError
    ...
```

> **Rule of Thumb:** Valid indices for an array of length `n` are always `0` to `n-1` (positive) and `-1` to `-n` (negative). Any access outside this range raises `IndexError`.

## 14.2 Aliasing and Copy Bugs

Already covered fully in Section 2.11 and Section 2.3.1 — the two highest-frequency bugs:
- `[[0] * n] * m` creates aliased rows.
- `b = a` creates an alias, not a copy; mutating `b` mutates `a`.

```python
# Bug
def process(matrix):
    result = matrix              # ALIAS, not a copy!
    result[0][0] = -1              # mutates the CALLER's matrix too

# Fix
def process(matrix):
    result = [row[:] for row in matrix]    # independent rows
    result[0][0] = -1                         # caller's matrix untouched
```

## 14.3 Prefix Sum & Difference Array Mistakes

- Forgetting the `l == 0` special case in `range_sum` (Section 6.2) — causes wrong results via `prefix[-1]` silently wrapping to the last element instead of raising an error.
- Sizing a difference array as `n` instead of `n+1` (Section 6.4) — causes `IndexError` when updating a range ending at the last index.
- Forgetting to run the final prefix-sum recovery pass on a difference array before reading "the answer."

## 14.4 Rotation and Matrix Boundary Errors

- Not reducing `k %= n` before rotating — causes unnecessary work or, in manual implementations, incorrect results if `k > n`.
- Attempting in-place 90° rotation on a non-square matrix (Section 8.4) — only works when `rows == cols`.
- Off-by-one in spiral/boundary traversal loop bounds (`top <= bottom`, `left <= right`) — the two guard checks inside the down/left passes in `spiral_order` (Section 8.7) exist specifically to prevent re-visiting cells on the final ring.

## 14.5 Modification During Traversal

```python
# Bug — modifying a list while iterating over it directly
arr = [1, 2, 3, 4, 5]
for x in arr:
    if x % 2 == 0:
        arr.remove(x)          # skips elements! iterator gets confused

# Fix 1 — iterate over a copy
for x in arr[:]:
    if x % 2 == 0:
        arr.remove(x)

# Fix 2 — build a new list instead (preferred, clearer)
arr = [x for x in arr if x % 2 != 0]
```

### Why the Bug Happens
Python's list iterator tracks a numeric position internally. When you remove an element, everything after it shifts left by one, but the iterator's position still advances by one — so it silently skips the element that shifted into the just-vacated slot.

### Dry Run — The Bug in Action

| Step | Iterator Position | arr (live) | x | Action |
|---|---|---|---|---|
| 1 | 0 | [1,2,3,4,5] | 1 | odd, skip |
| 2 | 1 | [1,2,3,4,5] | 2 | even, `remove(2)` → [1,3,4,5] |
| 3 | 2 | [1,3,4,5] | **4** (NOT 3!) | iterator jumped past 3 — bug! |
| 4 | 3 | [1,3,4,5] | 5 | odd, skip |

**Result:** `[1, 3, 4]` — but `4` should have been removed too! This is exactly why Fix 1 or Fix 2 above is required.

---

## Chapter 14 Summary & Cheat Sheet

| Mistake | Fix |
|---|---|
| `arr[n]` / `arr[-n-1]` access | Always validate `0 ≤ i < n` |
| `[[0]*n]*m` | Use `[[0]*n for _ in range(m)]` |
| `b = a` for "copying" | Use `a.copy()`/`a[:]` or `deepcopy` for nested |
| Prefix sum `l==0` case | Special-case it or pad the prefix array |
| Difference array sized `n` | Size it `n+1` |
| In-place rotate rectangular matrix | Build a new matrix instead |
| Mutating list while iterating | Iterate a copy, or build a new filtered list |

### Frequently Asked Questions

**Q: Why doesn't Python raise an error when I mutate a list during iteration?**
A: It's legal Python — lists don't lock during iteration — but it silently produces logically wrong results, which is far more dangerous than a crash.

### Practice Problems
1. Predict the (buggy) output of removing all elements equal to 3 from `[3, 3, 1, 3, 2]` using the "modification during traversal" anti-pattern, then fix it.
2. Find and fix the bug: `def clone_matrix(m): return m[:]` when `m` is a list of lists.
3. Write a difference-array based range-update function and deliberately test the boundary case `r == n - 1` to confirm no `IndexError` occurs.

---

# Chapter 15: Cheat Sheets

## 15.1 Complexity Cheat Sheet

| Operation | Time | Space |
|---|---|---|
| Access / Update | O(1) | O(1) |
| Append (end) | O(1) amortized | O(1) |
| Insert / Delete (middle) | O(n) | O(1) |
| Insert / Delete (front) | O(n) | O(1) |
| Linear Search | O(n) | O(1) |
| Reverse (two-pointer) | O(n) | O(1) |
| Reverse (slicing) | O(n) | O(n) |
| Sort | O(n log n) | O(n) (Timsort) |
| Prefix Sum (build/query) | O(n) / O(1) | O(n) |
| Difference Array (update/materialize) | O(1) / O(n) | O(n) |
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(1) |
| Kadane's | O(n) | O(1) |
| Cyclic Sort | O(n) | O(1) |
| Matrix Traversal | O(rows×cols) | O(1) extra |
| 2D Prefix Sum (build/query) | O(rows×cols) / O(1) | O(rows×cols) |

## 15.2 Formula Sheet

```
Number of subarrays of length n:          n(n+1)/2
Negative index equivalence:                arr[-k] == arr[len(arr)-k]
Prefix sum:                                 prefix[i] = prefix[i-1] + arr[i]
Range sum (1D, l>0):                         prefix[r] - prefix[l-1]
Difference array update:                      diff[l]+=v ; diff[r+1]-=v
Rotate right by k (reversal algo):             reverse(0,n-1); reverse(0,k-1); reverse(k,n-1)
Kadane's recurrence:                            current_max = max(arr[i], current_max+arr[i])
2D prefix sum:                                   prefix[r][c] = mat[r-1][c-1]+prefix[r-1][c]+prefix[r][c-1]-prefix[r-1][c-1]
2D region sum:                                    prefix[r2][c2]-prefix[r1-1][c2]-prefix[r2][c1-1]+prefix[r1-1][c1-1]
```

## 15.3 Pattern Cheat Sheet

| Trigger Phrase | Pattern | Chapter |
|---|---|---|
| Sorted + pair/triplet sum | Two Pointers | 6.1 |
| Fixed-size contiguous window | Sliding Window (fixed) | 6.1 |
| Smallest/longest valid subarray | Sliding Window (variable) | 6.1, 7.5 |
| Many range-sum queries | Prefix Sum | 6.2 |
| Many range-update operations | Difference Array | 6.4 |
| Values in `1..n`, missing/duplicate | Cyclic Sort / Sign Marking | 6.6, 6.7 |
| Max/min contiguous subarray sum | Kadane's | 6.10 |
| Element appears > n/2 times | Majority Voting | 6.11 |
| 3-way in-place partition | Dutch National Flag | 6.12 |
| Circular shift by k | Rotation | 6.8 |
| Grid movement (spiral/diagonal/zigzag) | Matrix Traversal | 8 |

## 15.4 Python Syntax Cheat Sheet

```python
# Creation
arr = [0] * n
arr = [x for x in range(n)]
matrix = [[0]*cols for _ in range(rows)]     # NEVER [[0]*cols]*rows

# Access / Slice
arr[i]; arr[-1]; arr[a:b]; arr[a:b:c]; arr[::-1]

# Mutation
arr.append(x); arr.insert(i,x); arr.extend(it)
arr.pop(); arr.pop(i); arr.remove(x); del arr[i]

# Copy
arr.copy(); arr[:]; list(arr)     # shallow
copy.deepcopy(arr)                  # deep

# Traversal
for v in arr: ...
for i, v in enumerate(arr): ...
for v in reversed(arr): ...

# Utilities
sum(arr); min(arr); max(arr); sorted(arr)
Counter(arr); itertools.accumulate(arr)
```

---

# Chapter 16: Practice Problems

## 16.1 By Topic

**Traversal & Basics:** Reverse Array, Move Zeroes, Find Second Largest, Check Sorted Array.

**Prefix Sum:** Range Sum Query - Immutable, Subarray Sum Equals K, Product of Array Except Self, Find the Middle Index (Pivot Index).

**Difference Array:** Corporate Flight Bookings, Range Addition.

**Frequency / Counting:** Majority Element, Top K Frequent Elements, Find All Duplicates in an Array.

**Matrix:** Spiral Matrix, Rotate Image, Set Matrix Zeroes, Diagonal Traverse, Transpose Matrix.

**Rotation:** Rotate Array, Rotate Image.

**Subarrays:** Maximum Subarray, Maximum Product Subarray, Subarray Sum Equals K, Minimum Size Subarray Sum.

**Kadane's / DP-adjacent (array framing only):** Maximum Subarray, Best Time to Buy and Sell Stock, Maximum Sum Circular Subarray.

**Simulation:** Spiral Matrix, Game of Life, Candy (array-greedy framing).

## 16.2 By Difficulty

**Easy:** Two Sum, Move Zeroes, Best Time to Buy and Sell Stock, Remove Duplicates from Sorted Array, Plus One, Majority Element.

**Medium:** 3Sum, Rotate Array, Spiral Matrix, Product of Array Except Self, Subarray Sum Equals K, Sort Colors, Set Matrix Zeroes, Gas Station, Minimum Size Subarray Sum.

**Hard:** Trapping Rain Water, First Missing Positive, Maximum Sum Circular Subarray, Median of Two Sorted Arrays.

## 16.3 By Platform

| Platform | Notes |
|---|---|
| LeetCode | Best-organized by tag ("Array") and difficulty; use the Blind 75 / NeetCode 150 lists as curated subsets. |
| GeeksforGeeks | Strong for fundamentals and Indian-placement-style array questions. |
| Codeforces | Div 2 A/B problems are excellent array-pattern drills (implementation-heavy). |
| CodeChef | Good for beginner-to-intermediate simulation-style array problems. |
| AtCoder | Beginner Contest (ABC) A/B/C problems are clean, well-specified array drills. |
| HackerRank | Good structured "Arrays" track for absolute beginners. |
| InterviewBit | Curated array section aligned closely with interview-style questions. |

> **Note:** Specific problem sets and rankings on these platforms change over time — search each platform's own "Array" tag/category for the current list rather than relying on a static snapshot.

---

# Chapter 17: Final Revision

## 17.1 One-Page Revision

- Array = index → O(1) address arithmetic. Python `list` = dynamic array of **references**.
- `append` O(1) amortized; middle insert/delete O(n).
- Negative indices: `arr[-k] == arr[len(arr)-k]`.
- `[[0]*n for _ in range(m)]` for 2D — never `[[0]*n]*m`.
- Prefix sum → fast range-sum queries. Difference array → fast range updates.
- Two pointers / sliding window → O(n²) → O(n) for pair/contiguous problems.
- Kadane's → max/min contiguous subarray sum, trackers init to `arr[0]`, never 0.
- Cyclic sort / sign marking → O(1)-space missing/duplicate detection for values in `1..n`.
- Matrix = array of arrays; rotate = transpose + reverse rows (square only).
- Always state brute force → optimize → verify with a dry run including edge cases.

## 17.2 Pattern Map

```
                     ARRAY PROBLEM
                          |
      -----------------------------------------------
      |            |             |            |      |
  Contiguous?   Sorted/Pairs? Range Queries? Values  Grid?
      |            |             |         in 1..n?   |
   Sliding      Two Pointers   Prefix Sum/   Cyclic   Matrix
   Window                      Diff Array    Sort/    Traversal
      |                                      Sign     Patterns
  Kadane's (if                               Marking
  "max/min sum")
```



---

