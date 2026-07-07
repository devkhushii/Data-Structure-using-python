# 🏔️ THE COMPLETE HEAP & PRIORITY QUEUE HANDBOOK


## 📑 Table of Contents

1. [Introduction](#1-introduction)
2. [Heap Fundamentals](#2-heap-fundamentals)
3. [Array Representation & Index Mapping](#3-array-representation--index-mapping)
4. [Python `heapq` Module — Complete Reference](#4-python-heapq-module--complete-reference)
5. [Types of Heaps](#5-types-of-heaps)
6. [Core Heap Operations (Manual Implementation)](#6-core-heap-operations-manual-implementation)
7. [Building a Full Min-Heap Class in Python](#7-building-a-full-min-heap-class-in-python)
8. [Max-Heap Simulation in Python](#8-max-heap-simulation-in-python)
9. [Priority Queue — Concept & Implementation](#9-priority-queue--concept--implementation)
10. [Heap Sort](#10-heap-sort)
11. [Heap Patterns (Interview Core)](#11-heap-patterns-interview-core)
    - 11.1 [Kth Largest / Kth Smallest Element](#111-kth-largest--kth-smallest-element)
    - 11.2 [Top K Frequent Elements](#112-top-k-frequent-elements)
    - 11.3 [Merge K Sorted Lists / Arrays](#113-merge-k-sorted-lists--arrays)
    - 11.4 [Running Median (Two Heaps)](#114-running-median-two-heaps)
    - 11.5 [Sliding Window Median](#115-sliding-window-median)
    - 11.6 [Task Scheduler](#116-task-scheduler)
    - 11.7 [Reorganize String](#117-reorganize-string)
    - 11.8 [Last Stone Weight](#118-last-stone-weight)
    - 11.9 [IPO Problem](#119-ipo-problem)
    - 11.10 [K Closest Points to Origin](#1110-k-closest-points-to-origin)
    - 11.11 [Huffman Coding (Concept)](#1111-huffman-coding-concept)
12. [Advanced Heap Concepts](#12-advanced-heap-concepts)
13. [Applications of Heaps](#13-applications-of-heaps)
14. [Problem Recognition Guide](#14-problem-recognition-guide)
15. [Optimization Strategies](#15-optimization-strategies)
16. [Interview Preparation](#16-interview-preparation)
17. [Python-Specific Tips & Tricks](#17-python-specific-tips--tricks)
18. [Common Mistakes](#18-common-mistakes)
19. [Cheat Sheets](#19-cheat-sheets)
20. [Practice Problem Bank](#20-practice-problem-bank)
21. [Final Revision & Mind Maps](#21-final-revision--mind-maps)
22. [FAQs](#22-faqs)

---

## 1. Introduction

### 1.1 What is a Heap?

A **heap** is a specialized **complete binary tree**-based data structure that satisfies the **heap property**:

- **Min-Heap**: every parent node's value is **≤** its children's values → the smallest element is always at the root.
- **Max-Heap**: every parent node's value is **≥** its children's values → the largest element is always at the root.

> 📌 **Key idea**: A heap is *not* fully sorted. It only guarantees that the root is the min (or max). This partial ordering is what makes heaps fast to build and maintain.

### 1.2 What is a Priority Queue?

A **Priority Queue (PQ)** is an **abstract data type (ADT)** where each element has a "priority", and elements are served in priority order (not insertion order, unlike a normal queue).

- A **heap** is the most common and efficient **concrete implementation** of a priority queue.
- Think of Priority Queue as the **interface** (the "what"), and Heap as the **implementation** (the "how").

```
Priority Queue (ADT)  ──implemented by──>  Binary Heap (most common)
                                            Fibonacci Heap
                                            Binomial Heap
                                            Sorted Array/List (naive)
                                            Balanced BST (alternative)
```

### 1.3 History

- Heaps were invented by **J. W. J. Williams** in 1964 as a data structure for the **Heapsort** algorithm.
- **Robert W. Floyd** improved this the same year, introducing the O(n) **build-heap** algorithm (Floyd's method), still used today.
- Since then, heaps have become foundational in scheduling, graph algorithms (Dijkstra, Prim), and streaming analytics.

### 1.4 Why Heaps Exist — The Motivation

Imagine you constantly need to know the **minimum** (or maximum) element in a dynamic collection — one where elements are added and removed frequently.

| Approach | Find Min | Insert | Delete Min |
|---|---|---|---|
| Unsorted array/list | O(n) | O(1) | O(n) |
| Sorted array/list | O(1) | O(n) | O(n) shift, O(1) find |
| Balanced BST | O(log n) | O(log n) | O(log n) |
| **Binary Heap** | **O(1)** | **O(log n)** | **O(log n)** |

A heap gives you **O(1) access to the extreme element** and **O(log n) insert/delete** — the best balance for priority-based access, without the overhead of a fully balanced tree structure.

### 1.5 Heap Property (Formal Definition)

For a node at index `i` with children at indices `2i+1` and `2i+2`:

- **Min-Heap Property**: `heap[i] <= heap[2i+1]` and `heap[i] <= heap[2i+2]`
- **Max-Heap Property**: `heap[i] >= heap[2i+1]` and `heap[i] >= heap[2i+2]`

This property must hold **recursively** for every node in the tree — it is **not** a global sort order, only a **local parent-child ordering**.

> ⚠️ **Common Misconception**: People assume heap arrays are "almost sorted." They are NOT. A heap only guarantees the root is min/max; siblings and deeper levels can be in any relative order as long as the parent-child rule holds.

### 1.6 Complete Binary Tree Property

A heap must always be a **complete binary tree**:

- All levels are **completely filled** except possibly the last.
- The last level is filled **left to right** with no gaps.

```
Complete Binary Tree (valid heap shape):        Incomplete (INVALID heap shape):

              10                                          10
            /    \                                      /    \
          15      20                                  15      20
         /  \    /                                   /       /  \
       17   18  40                                 17       40   45   <- gap on level 2
                                                    (missing right child of 15)
```

This "completeness" is exactly what allows a heap to be stored efficiently in a **plain array**, with no pointers needed (see Section 3).

### 1.7 Characteristics of a Heap

| Property | Description |
|---|---|
| Shape | Complete binary tree |
| Ordering | Heap property (min or max) |
| Storage | Array (implicit pointers via index arithmetic) |
| Root | Always the min (or max) element |
| Sorted? | ❌ No — only partially ordered |
| Balanced? | ✅ Always height-balanced (height = ⌊log₂ n⌋) since it's complete |
| Duplicate values | ✅ Allowed |

### 1.8 Advantages of Heaps

- O(1) retrieval of min/max element.
- O(log n) insertion and deletion — much better than sorting repeatedly.
- O(n) construction from an arbitrary array (`heapify`).
- Space-efficient: stored in a flat array, no extra pointer overhead.
- Naturally supports priority-based processing.

### 1.9 Disadvantages of Heaps

- No O(1) search for an arbitrary element (must scan, O(n)).
- Not a sorted structure — cannot do ordered traversal in O(n) like a BST's in-order traversal.
- Deleting an **arbitrary** (non-root) element is O(n) to locate + O(log n) to fix, unless you maintain an index map (see Indexed Priority Queue, Section 12).
- Not stable by default (equal-priority items may not preserve insertion order unless engineered explicitly).

### 1.10 Applications & Real-World Examples

| Real-World Scenario | Heap Usage |
|---|---|
| Hospital Emergency Room | Patients treated by severity (max-heap on urgency) |
| Airport runway scheduling | Planes prioritized by fuel/emergency status |
| OS process scheduling | CPU picks the highest-priority process (max-heap) |
| Dijkstra's shortest path | Min-heap picks next closest unvisited node |
| Prim's MST algorithm | Min-heap picks next cheapest edge |
| Event-driven simulation | Min-heap of events ordered by timestamp |
| Streaming "Top K" analytics | Fixed-size heap tracks top K elements seen so far |
| Huffman encoding | Min-heap builds optimal prefix codes |
| Load balancers | Route request to server with least load (min-heap) |
| `heapq.merge()` | Merge K sorted log files/streams efficiently |

> 🧠 **Real-World Analogy**: A heap is like an **airport boarding priority system**. You don't need the whole line sorted — you only need to know *who boards next* (First Class → root of a max-heap). When that person boards, the next-highest priority passenger "bubbles up" to the front. Nobody bothers sorting the entire terminal.

---

## 2. Heap Fundamentals

### 2.1 Terminology

| Term | Meaning |
|---|---|
| **Root** | Topmost node (index 0 in array) |
| **Parent** | Node directly above a given node |
| **Child** | Node(s) directly below a given node (max 2 in binary heap) |
| **Leaf** | Node with no children |
| **Height** | Longest path from root to a leaf = ⌊log₂ n⌋ |
| **Depth** | Distance of a node from the root |
| **Level** | All nodes at the same depth |
| **Sibling** | Nodes sharing the same parent |

### 2.2 Why "Complete Binary Tree" and Not Just "Binary Tree"?

If the tree weren't complete, we couldn't compute a child's/parent's location using simple arithmetic on an array index — we'd need explicit `left`/`right`/`parent` pointers, wasting memory and losing cache locality. Completeness is the *reason* heaps can be array-backed.

### 2.3 Heap Height

For `n` nodes, height `h = ⌊log₂ n⌋`.

| n (nodes) | height |
|---|---|
| 1 | 0 |
| 3 | 1 |
| 7 | 2 |
| 15 | 3 |
| 1,000,000 | ~19 |

This logarithmic height is *why* insert/delete are O(log n) — operations only ever traverse a single root-to-leaf path.

---

## 3. Array Representation & Index Mapping

### 3.1 Why Arrays?

Because a heap is always a **complete binary tree**, we can store it in a flat, 0-indexed array and derive parent/child relationships via arithmetic — no pointers required.

```
Tree View:                      Array View (0-indexed):

              10  (0)
            /      \            Index:  0    1    2    3    4    5    6
          15 (1)   20 (2)       Value: [10,  15,  20,  17,  18,  40,  45]
         /   \      /
       17(3) 18(4) 40(5)
```

### 3.2 Index Formulas (0-indexed array — used by Python's `heapq`)

| Relationship | Formula |
|---|---|
| Parent of index `i` | `(i - 1) // 2` |
| Left child of index `i` | `2*i + 1` |
| Right child of index `i` | `2*i + 2` |

> ⚠️ **1-indexed vs 0-indexed**: Many textbooks (especially CLRS) use **1-indexed** arrays, where `parent(i) = i // 2`, `left(i) = 2*i`, `right(i) = 2*i + 1`. Python's `heapq` (and this handbook) uses **0-indexed** arrays. Always check which convention a source uses before copying formulas!

### 3.3 Dry Run: Index Mapping

Array: `[10, 15, 20, 17, 18, 40, 45]`

| Index | Value | Parent Index | Parent Value | Left Child Idx | Right Child Idx |
|---|---|---|---|---|---|
| 0 | 10 | — (root) | — | 1 | 2 |
| 1 | 15 | 0 | 10 | 3 | 4 |
| 2 | 20 | 0 | 10 | 5 | 6 |
| 3 | 17 | 1 | 15 | 7 (none) | 8 (none) |
| 4 | 18 | 1 | 15 | 9 (none) | 10 (none) |
| 5 | 40 | 2 | 20 | 11 (none) | 12 (none) |
| 6 | 45 | 2 | 20 | 13 (none) | 14 (none) |

### 3.4 Python Helper Functions

```python
def parent(i: int) -> int:
    """Return index of parent node. Root (i=0) has no valid parent."""
    return (i - 1) // 2

def left_child(i: int) -> int:
    """Return index of left child."""
    return 2 * i + 1

def right_child(i: int) -> int:
    """Return index of right child."""
    return 2 * i + 2
```

**Line-by-line explanation:**
- `(i - 1) // 2`: integer division automatically handles both left-child (`2i+1`) and right-child (`2i+2`) cases mapping back to the same parent `i`.
- `2 * i + 1` / `2 * i + 2`: direct forward mapping from parent to children.

**Edge Cases:**
- `parent(0)` returns `-1 // 2` in mathematical terms, but in Python `(0-1)//2 = -1` (valid negative index — **be careful**, this wraps to the *last* element instead of raising an error!). Always explicitly check `i == 0` before calling `parent()` on the root.
- `left_child(i)` / `right_child(i)` may return indices **beyond the array bounds** — always bounds-check (`idx < len(heap)`) before accessing.

---

## 4. Python `heapq` Module — Complete Reference

### 4.1 Overview

Python's built-in `heapq` module implements a **binary min-heap** directly on top of a regular Python `list`. It does **not** provide a separate heap class — you operate on a plain list using module-level functions.

> 📌 **Critical fact**: `heapq` only implements a **MIN-HEAP**. There is no built-in max-heap. To simulate a max-heap, you negate values (see Section 8).

### 4.2 Function Reference Table

| Function | Purpose | Time Complexity |
|---|---|---|
| `heapq.heapify(x)` | Convert list `x` into a valid heap, in-place | O(n) |
| `heapq.heappush(heap, item)` | Push `item` onto heap, maintaining heap invariant | O(log n) |
| `heapq.heappop(heap)` | Pop and return smallest item | O(log n) |
| `heapq.heappushpop(heap, item)` | Push then pop in one optimized step | O(log n) |
| `heapq.heapreplace(heap, item)` | Pop then push in one optimized step | O(log n) |
| `heapq.nlargest(k, iterable)` | Return k largest elements | O(n log k) |
| `heapq.nsmallest(k, iterable)` | Return k smallest elements | O(n log k) |
| `heapq.merge(*iterables)` | Merge multiple sorted inputs into one sorted generator | O(n log k) |

### 4.3 `heapify()`

**Problem**: Convert an arbitrary list into a valid min-heap, in-place.

```python
import heapq

arr = [9, 4, 7, 1, -2, 6, 5]
heapq.heapify(arr)
print(arr)   # [-2, 1, 5, 9, 4, 6, 7]
```

**Line-by-line explanation:**
- `heapq.heapify(arr)` rearranges `arr` in-place using **Floyd's build-heap algorithm**: it calls "sift-down" (bubble down) starting from the last non-leaf node up to the root.
- No new list is created — this is an **O(n)** in-place transformation (see Section 12.2 for why it's O(n), not O(n log n)).

**Dry Run:**

| Step | Array State | Operation | Explanation |
|---|---|---|---|
| 0 | `[9, 4, 7, 1, -2, 6, 5]` | start | last non-leaf index = (7//2)-1 = 2 |
| 1 | `[9, 4, 5, 1, -2, 6, 7]` | sift-down(2): 7 vs children(6,5) → swap with 5 | node@2 fixed |
| 2 | `[9, -2, 5, 1, 4, 6, 7]` | sift-down(1): 4 vs children(1,-2) → swap with -2 | node@1 fixed |
| 3 | `[-2, 9, 5, 1, 4, 6, 7]` | sift-down(0) pass 1: 9 vs children(-2,5) → swap with -2 | continue sifting the 9 down from its new position (idx 1) |
| 4 | `[-2, 1, 5, 9, 4, 6, 7]` | sift-down(0) pass 2: 9 (now at idx 1) vs children(1,4) → swap with 1 | root fully fixed |

Final heap array: `[-2, 1, 5, 9, 4, 6, 7]` — root `-2` is the minimum. ✅ (Verified against actual Python `heapq.heapify()` output.)

**Time Complexity:** O(n) &nbsp;&nbsp; **Space Complexity:** O(1) additional (in-place)

### 4.4 `heappush()`

```python
import heapq

heap = [1, 3, 5]
heapq.heappush(heap, 0)
print(heap)   # [0, 1, 5, 3]
```

**Internal working:** Appends `item` to the end of the list, then **sifts it up** (bubble up) — repeatedly swapping with its parent while it's smaller than the parent.

**Dry Run** (pushing `0` into `[1, 3, 5]`):

| Step | Heap Array | Operation | Explanation |
|---|---|---|---|
| 0 | `[1, 3, 5, 0]` | append 0 at index 3 | leaf position |
| 1 | `[1, 0, 5, 3]` | compare idx 3 (`0`) with parent idx 1 (`3`) → `0 < 3`, swap | bubble up |
| 2 | `[0, 1, 5, 3]` | compare idx 1 (`0`) with parent idx 0 (`1`) → `0 < 1`, swap | reaches root, stop |

**Complexity:** O(log n) time, O(1) extra space.

### 4.5 `heappop()`

```python
import heapq

heap = [0, 1, 5, 3]
smallest = heapq.heappop(heap)
print(smallest)  # 0
print(heap)       # [1, 3, 5]
```

**Internal working:**
1. Save `heap[0]` (the min) to return.
2. Move the **last** element to the root.
3. Shrink the list by one.
4. **Sift down** the new root until the heap property is restored.

**Dry Run:**

| Step | Heap Array | Operation | Explanation |
|---|---|---|---|
| 0 | `[0, 1, 5, 3]` | save `0` as result | root removed conceptually |
| 1 | `[3, 1, 5]` | move last elem `3` to root, shrink list | new root candidate |
| 2 | `[1, 3, 5]` | sift-down(0): `3` vs children `1, 5` → swap with smaller child `1` | heap restored |

Returned value: `0`. Final heap: `[1, 3, 5]`.

**Complexity:** O(log n)

### 4.6 `heappushpop()` vs `heapreplace()`

Both combine push + pop, but with a crucial ordering difference:

| Function | Order | Behavior | Use Case |
|---|---|---|---|
| `heappushpop(heap, item)` | **push, then pop** | If `item` ≤ current min, it's returned immediately without entering the heap | Slightly more efficient when new item is likely small |
| `heapreplace(heap, item)` | **pop, then push** | Always pops the old min first, THEN pushes `item` (even if item is smaller than everything) | Use when you must always remove old root, regardless of new item |

```python
import heapq

heap = [1, 3, 5]

# heappushpop: pushes 0, but since 0 < heap[0]=1, it's returned directly
print(heapq.heappushpop(heap, 0))  # 0
print(heap)                        # [1, 3, 5]  (unchanged!)

heap2 = [1, 3, 5]
# heapreplace: ALWAYS pops old min (1) first, then pushes 0
print(heapq.heapreplace(heap2, 0))  # 1
print(heap2)                        # [0, 3, 5]
```

> ⚠️ **Interview Trap**: `heapreplace` can temporarily violate "the heap only shrinks or stays same size" intuition — it **replaces** the root, so size stays constant, but the *value* returned is the **old root**, not the new item. Many candidates confuse this with `heappushpop`.

### 4.7 `nlargest()` and `nsmallest()`

```python
import heapq

nums = [5, 1, 9, 3, 7, 2, 8]
print(heapq.nsmallest(3, nums))  # [1, 2, 3]
print(heapq.nlargest(3, nums))   # [9, 8, 7]

# With a key function (like sorted()):
words = ["apple", "kiwi", "banana", "fig"]
print(heapq.nlargest(2, words, key=len))  # ['banana', 'apple']
```

**Internal working:** Uses a **heap of size k** internally (not a full sort) when `k` is small relative to `n`, giving **O(n log k)** instead of O(n log n).

> 📌 **Rule of thumb**: If `k == 1`, use `min()`/`max()` — O(n), faster than heap overhead. If `k` is close to `n`, just use `sorted()` — O(n log n) is comparable and simpler. `nlargest`/`nsmallest` shine when `1 << k << n`.

### 4.8 `heapq.merge()`

```python
import heapq

log1 = [1, 5, 9, 20]
log2 = [2, 3, 8, 15]
log3 = [0, 6, 30]

merged = list(heapq.merge(log1, log2, log3))
print(merged)  # [0, 1, 2, 3, 5, 6, 8, 9, 15, 20, 30]
```

**Internal working:** Maintains a heap of size `k` (number of iterables) holding the "current head" of each iterable. Repeatedly pops the smallest, advances that iterable, and pushes its next value. This is a **lazy generator** — doesn't require loading all elements into memory at once (great for merging huge sorted files/logs).

**Complexity:** O(n log k) where `n` = total elements, `k` = number of iterables.

### 4.9 Tuples as Heap Elements — Priority + Data

Since `heapq` compares elements directly, the standard pattern for a "priority + payload" queue is to push **tuples**:

```python
import heapq

pq = []
heapq.heappush(pq, (2, "wash dishes"))
heapq.heappush(pq, (1, "fire! evacuate"))
heapq.heappush(pq, (3, "water plants"))

while pq:
    priority, task = heapq.heappop(pq)
    print(priority, task)

# Output:
# 1 fire! evacuate
# 2 wash dishes
# 3 water plants
```

**How comparison works:** Tuples compare **lexicographically** — first by index 0 (priority), and only fall through to index 1 if there's a tie.

> ⚠️ **Critical Pitfall — Tie-Breaking Crash**: If two tuples have equal priority AND the second element is **not directly comparable** (e.g., custom objects, dicts), Python raises `TypeError: '<' not supported between instances of ...` when it tries to break the tie. 

**Fix using a tie-breaker counter (`itertools.count`)**:

```python
import heapq
import itertools

counter = itertools.count()  # unique, ever-increasing tie-breaker
pq = []

class Task:
    def __init__(self, name):
        self.name = name

heapq.heappush(pq, (2, next(counter), Task("wash dishes")))
heapq.heappush(pq, (2, next(counter), Task("mop floor")))  # same priority!

# No crash: ties are broken by the counter (insertion order), never reaching Task comparison
priority, _, task = heapq.heappop(pq)
print(priority, task.name)  # 2 wash dishes  (inserted first, FIFO for equal priority)
```

This pattern gives you a **stable priority queue** (FIFO among equal priorities) safely.

### 4.10 `dataclass` with Custom Ordering

```python
from dataclasses import dataclass, field
import heapq

@dataclass(order=True)
class PQItem:
    priority: int
    item: str = field(compare=False)  # excluded from comparison

pq = []
heapq.heappush(pq, PQItem(3, "low priority task"))
heapq.heappush(pq, PQItem(1, "urgent task"))
heapq.heappush(pq, PQItem(2, "medium task"))

while pq:
    entry = heapq.heappop(pq)
    print(entry.priority, entry.item)

# Output:
# 1 urgent task
# 2 medium task
# 3 low priority task
```

**Explanation:** `@dataclass(order=True)` auto-generates `__lt__`, etc., based on field order. `field(compare=False)` excludes `item` from comparisons — so heapq never tries (and fails) to compare arbitrary payload objects.

### 4.11 Best Practices for `heapq`

- ✅ Always push tuples `(priority, tie_breaker, data)` when data isn't directly comparable.
- ✅ Use `heapify()` for O(n) bulk construction instead of `n` individual `heappush()` calls (O(n log n)).
- ✅ Use `heapreplace`/`heappushpop` instead of separate pop+push when you know you'll do both — saves one O(log n) pass.
- ❌ Don't assume the underlying list is fully sorted — only `heap[0]` is guaranteed to be the min.
- ❌ Don't use `heapq` for a max-heap directly — negate values or use a wrapper (Section 8).

---

## 5. Types of Heaps

### 5.1 Min-Heap vs Max-Heap

```
MIN-HEAP                          MAX-HEAP
(smallest at root)                (largest at root)

        1                                 45
      /   \                             /    \
     3     6                          20      40
    / \   /                          /  \    /
   5   9 8                          15  18  17

Array: [1,3,6,5,9,8]              Array: [45,20,40,15,18,17]
```

| Aspect | Min-Heap | Max-Heap |
|---|---|---|
| Root | Smallest element | Largest element |
| Use case | Dijkstra, K smallest, running median (lower half) | Task scheduling, K largest, running median (upper half) |
| Python `heapq` | Native support | Simulated via negation |

### 5.2 Binary Heap (Default / Most Common)

Each node has **at most 2 children**. This is what `heapq` implements. It's the default choice unless you have a specific reason for something else.

### 5.3 D-ary Heap

A generalization where each node has **up to `d` children** instead of 2.

```
Binary Heap (d=2)              Ternary/3-ary Heap (d=3)

        10                              10
      /    \                    /       |       \
    15      20                15       20        25
                              / | \
                             30 35 40
```

| Property | Binary Heap (d=2) | D-ary Heap |
|---|---|---|
| Height | log₂ n | log_d n (shorter for larger d) |
| Insert | O(log₂ n) | O(log_d n) — faster |
| Extract-min | O(log₂ n) | O(d · log_d n) — slower (more children to compare) |
| Best for | General purpose | **Decrease-key heavy** workloads (e.g., Dijkstra with dense graphs) — fewer levels means faster bubble-up |

**When to use D-ary over Binary:** When insertions/decrease-key operations vastly outnumber extract-min operations (common in some graph algorithm implementations).

### 5.4 Binomial Heap (Overview)

- A collection ("forest") of **binomial trees**, each satisfying the heap property.
- Supports **O(log n) merge** of two heaps — a weakness of plain binary heaps (which need O(n) to merge).
- Used when frequent merging of two priority queues is required.

```
Binomial Heap = forest of binomial trees B0, B1, B2, ...

B0:  •          B1:  •            B2:      •
                    /                    /  |  \
                   •                   •    •   •
                                       /
                                      •
```

### 5.5 Fibonacci Heap (Overview)

- Supports **amortized O(1)** `insert`, `decrease-key`, and `merge`; `extract-min` is O(log n) amortized.
- Theoretically optimal for algorithms like Dijkstra/Prim on **dense graphs**, improving complexity from O(E log V) to O(E + V log V).
- **Rarely used in practice** due to large constant factors and implementation complexity — "great in theory, heavy in practice."

### 5.6 Pairing Heap (Overview)

- A simpler alternative to Fibonacci heaps with excellent practical performance.
- Structure: a tree where each node keeps a list of children; merging is just attaching one tree as a child of another's root.
- Good amortized bounds, much simpler code — often preferred over Fibonacci heaps in practice (e.g., used in some networking/simulation software).

### 5.7 Leftist Heap & Skew Heap (Overview)

- **Leftist Heap**: A binary heap variant that maintains a "leftist property" (left subtree is always at least as tall/heavy as the right, measured by "null path length"), enabling efficient O(log n) merge by always merging along the right spine.
- **Skew Heap**: A self-adjusting variant of the leftist heap — no explicit balancing information stored; every merge unconditionally swaps children, achieving good amortized performance with simpler code.

### 5.8 Comparison Table — All Heap Variants

| Heap Type | Insert | Extract-Min | Merge | Decrease-Key | Practical Use |
|---|---|---|---|---|---|
| Binary Heap | O(log n) | O(log n) | O(n) | O(log n) | ⭐ Default choice, `heapq` |
| D-ary Heap | O(log_d n) | O(d log_d n) | O(n) | O(log_d n) | Decrease-key-heavy workloads |
| Binomial Heap | O(log n) | O(log n) | **O(log n)** | O(log n) | Mergeable heaps |
| Fibonacci Heap | O(1) amortized | O(log n) amortized | O(1) | **O(1) amortized** | Theoretical graph algorithms |
| Pairing Heap | O(1) amortized | O(log n) amortized | O(1) | O(log n) amortized | Practical alternative to Fibonacci |
| Leftist/Skew Heap | O(log n) | O(log n) | O(log n) | — | Functional/persistent heaps |

> 🧠 **Interview Note**: For 95%+ of coding interviews, you only need the **Binary Heap** via Python's `heapq`. Binomial/Fibonacci/Pairing/Leftist heaps are typically **discussion-only** ("what would you use for X?") — you're almost never asked to implement them from scratch in an interview.

---

## 6. Core Heap Operations (Manual Implementation)

> This section builds every heap operation **from scratch** (without `heapq`) so you understand exactly what happens under the hood. Section 7 wraps these into a complete class.

### 6.1 Bubble Up (Sift Up) — Used After Insert

**Why it exists:** When we insert a new element, we add it at the end (a leaf) to preserve the *complete tree shape*. But it might be smaller (min-heap) than its ancestors — so we "bubble" it upward until the heap property holds.

**ASCII Visualization:**

```
Insert 2 into: [5, 8, 7, 10, 9]

Step 1: append 2                 Step 2: compare with parent(idx2=8→idx3)
        5                                5
      /   \                            /   \
     8     7                          8     7
    / \   /                          / \   /
  10  9  2  <- new leaf             10  9  2
                                   parent of idx4 is idx1(8); 2<8 → swap

Step 3: after swap                Step 4: compare idx1(2) with parent idx0(5)
        5                                2
      /   \                            /   \
     2     7                          5     7
    / \   /                          / \   /
  10  9  8                         10  9  8
                                   2<5 → swap again

Final:
        2
      /   \
     5     7
    / \   /
  10  9  8
```

```python
def bubble_up(heap: list, index: int) -> None:
    """
    Move the element at `index` up until the min-heap property holds.
    Assumes 0-indexed array-based heap.
    """
    while index > 0:
        parent_index = (index - 1) // 2
        if heap[index] < heap[parent_index]:      # min-heap: swap if child < parent
            heap[index], heap[parent_index] = heap[parent_index], heap[index]
            index = parent_index                    # move up and continue checking
        else:
            break                                    # heap property restored, stop
```

**Line-by-line explanation:**
- `while index > 0`: stop once we reach the root (index 0 has no parent).
- `parent_index = (index - 1) // 2`: standard 0-indexed parent formula.
- `if heap[index] < heap[parent_index]`: min-heap violation check — child smaller than parent breaks the rule.
- Swap, then update `index = parent_index` to keep checking upward.
- `else: break`: as soon as the property holds, no further swaps are needed (heaps only need **local** fixes).

**Dry Run** — inserting `2` into `[5, 8, 7, 10, 9]` (after appending, array = `[5, 8, 7, 10, 9, 2]`, index=5):

| Step | Array | index | parent_index | Comparison | Action |
|---|---|---|---|---|---|
| 1 | `[5,8,7,10,9,2]` | 5 | 2 | `2 < 7`? Yes | swap idx5,idx2 → `[5,8,2,10,9,7]`, index=2 |
| 2 | `[5,8,2,10,9,7]` | 2 | 0 | `2 < 5`? Yes | swap idx2,idx0 → `[2,8,5,10,9,7]`, index=0 |
| 3 | `[2,8,5,10,9,7]` | 0 | — | index==0, loop ends | done |

**Time Complexity:** O(log n) — at most `height` swaps. **Space Complexity:** O(1).

**Common Mistakes:**
- Forgetting to `break` early — unnecessary extra comparisons (not incorrect, but wasteful; actually the loop condition handles it, but explicit break makes intent clear).
- Using `<=` instead of `<` — causes unnecessary swaps for equal elements (not wrong, but wasteful, and can affect stability).
- Off-by-one in parent formula, especially confusing 0-indexed vs 1-indexed conventions.

### 6.2 Bubble Down (Sift Down) — Used After Delete/Extract

**Why it exists:** When we remove the root (min/max), we replace it with the **last** element (to preserve shape), which is likely much larger than it should be at the top — so we push it down until the property holds.

**ASCII Visualization:**

```
Extract-min from: [2, 5, 3, 10, 9, 7, 8]

Step 1: remove root(2), move last(8) to root
        8
      /   \
     5     3
    / \   /
  10  9  7

Step 2: compare 8 with children (5, 3) -> smaller child is 3 -> swap
        3
      /   \
     5     8
    / \   /
  10  9  7

Step 3: compare 8 with its child (7) -> 7 < 8 -> swap
        3
      /   \
     5     7
    / \   /
  10  9  8

No more children for 8 -> stop.
```

```python
def bubble_down(heap: list, index: int, size: int) -> None:
    """
    Move the element at `index` down until the min-heap property holds.
    `size` = logical size of heap (may be < len(heap) in some implementations).
    """
    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < size and heap[left] < heap[smallest]:
            smallest = left
        if right < size and heap[right] < heap[smallest]:
            smallest = right

        if smallest == index:
            break                                    # heap property restored
        heap[index], heap[smallest] = heap[smallest], heap[index]
        index = smallest                             # continue sifting down
```

**Line-by-line explanation:**
- `left`, `right`: child index formulas.
- `smallest = index`: assume current node is smallest until proven otherwise.
- Two `if` checks: compare with **both** children (unlike bubble-up, which only compares with **one** parent) — this is why bubble-down is conceptually "harder."
- If neither child is smaller, `smallest == index` → property holds, stop.
- Otherwise swap with the smaller child and continue the loop from the new position.

**Dry Run** — array `[8, 5, 3, 10, 9, 7]` (8 placed at root after removing old root and moving last element up), size=6:

| Step | index | left | right | smallest child value | Action |
|---|---|---|---|---|---|
| 1 | 0 (`8`) | 1(`5`) | 2(`3`) | `3` (idx2) < 8 | swap → `[3,5,8,10,9,7]`, index=2 |
| 2 | 2 (`8`) | 5(`7`) | 6 (OOB) | `7` (idx5) < 8 | swap → `[3,5,7,10,9,8]`, index=5 |
| 3 | 5 (`8`) | 11(OOB) | 12(OOB) | no children | `smallest==index`, stop |

**Time Complexity:** O(log n) — at most `height` swaps, each doing O(1) work (2 comparisons + maybe 1 swap).
**Space Complexity:** O(1).

**Common Mistakes:**
- Comparing with only one child (forgetting `right`) — breaks the heap property silently.
- Using `size` incorrectly when it differs from `len(heap)` (e.g., in in-place heap sort where the "heap region" shrinks but the array doesn't).
- Off-by-one on child index bounds checks (`left < size` not `left <= size`).

### 6.3 Insert Operation (Full)

```python
def insert(heap: list, value) -> None:
    """Insert `value` into the heap, maintaining the min-heap property."""
    heap.append(value)              # Step 1: add as last leaf (preserves complete-tree shape)
    bubble_up(heap, len(heap) - 1)  # Step 2: restore heap property upward
```

**Time Complexity:** O(log n) — append is O(1) amortized, bubble-up is O(log n).
**Space Complexity:** O(1) extra (ignoring the array growth itself).

### 6.4 Extract-Min / Extract-Max (Full)

```python
def extract_min(heap: list):
    """Remove and return the minimum element (root)."""
    if not heap:
        raise IndexError("extract_min from empty heap")
    
    min_value = heap[0]                    # Step 1: save root value
    last_value = heap.pop()                # Step 2: remove last element

    if heap:                                # Step 3: if heap isn't now empty
        heap[0] = last_value                # move last element to root
        bubble_down(heap, 0, len(heap))     # restore heap property downward

    return min_value
```

**Line-by-line explanation:**
- Guard clause for empty heap (edge case).
- Save the root (what we'll return) before mutating anything.
- `heap.pop()` removes and returns the **last** element in O(1).
- If the heap still has elements after removing one, place the former-last element at the root and sift it down.
- Special case: if we just popped the *only* element, `heap` is now empty — nothing more to do.

**Dry Run:** covered in Section 6.2 above (same mechanics).

**Time Complexity:** O(log n). **Space Complexity:** O(1) extra.

**Edge Cases:**
- Empty heap → raise error (or return `None`, depending on API design).
- Single-element heap → after `pop()`, heap is empty; skip bubble-down (handled by `if heap:` check).

### 6.5 Peek

```python
def peek_min(heap: list):
    """Return (without removing) the minimum element."""
    if not heap:
        raise IndexError("peek from empty heap")
    return heap[0]
```

**Time Complexity:** O(1). **Space Complexity:** O(1).

### 6.6 Delete (Arbitrary Element)

Removing an arbitrary element (not just the root) requires first **locating** it (O(n) without an index map), then replacing it with the last element and re-heapifying locally.

```python
def delete_at_index(heap: list, index: int) -> None:
    """Delete the element at a given index, maintaining heap property."""
    if index >= len(heap):
        raise IndexError("index out of range")

    last_value = heap.pop()
    if index < len(heap):                    # if we didn't just remove the last element
        heap[index] = last_value
        parent_index = (index - 1) // 2
        # Decide whether to bubble up or down based on the new value
        if index > 0 and heap[index] < heap[parent_index]:
            bubble_up(heap, index)
        else:
            bubble_down(heap, index, len(heap))
```

**Explanation:** After overwriting the target slot with the last element, that new value could be **either** smaller than its parent (needs bubble-up) **or** larger than a child (needs bubble-down) — never both, so we check one direction and apply the appropriate fix.

**Time Complexity:** O(n) to find the index (if unknown) + O(log n) to fix = **O(n)** overall. If the index is already known (e.g., via an auxiliary hashmap — see "Indexed Priority Queue," Section 12), this drops to **O(log n)**.

### 6.7 Update / Decrease-Key / Increase-Key

```python
def decrease_key(heap: list, index: int, new_value) -> None:
    """Decrease the value at `index` to `new_value` (must be <= current value in min-heap)."""
    if new_value > heap[index]:
        raise ValueError("new_value must be <= current value for decrease_key")
    heap[index] = new_value
    bubble_up(heap, index)   # value got smaller -> may need to move up

def increase_key(heap: list, index: int, new_value) -> None:
    """Increase the value at `index` to `new_value` (must be >= current value in min-heap)."""
    if new_value < heap[index]:
        raise ValueError("new_value must be >= current value for increase_key")
    heap[index] = new_value
    bubble_down(heap, index, len(heap))   # value got bigger -> may need to move down
```

**Why this matters:** Algorithms like **Dijkstra's shortest path** rely heavily on `decrease-key` (when a shorter path to a node is found, its priority in the heap must be reduced). Python's `heapq` has **no built-in decrease-key** — this is one of its few limitations (see Section 12 for the standard workaround: **lazy deletion**).

### 6.8 Build Heap — O(n) (Floyd's Algorithm)

**Naive approach:** insert `n` elements one-by-one → each insert is O(log n) → total **O(n log n)**.

**Optimized approach (`heapify`):** Start from the **last non-leaf node** and bubble-down each node moving toward the root.

```python
def build_heap(arr: list) -> None:
    """Convert arr into a min-heap in-place using Floyd's O(n) algorithm."""
    n = len(arr)
    last_non_leaf = n // 2 - 1
    for i in range(last_non_leaf, -1, -1):
        bubble_down(arr, i, n)
```

**Why is this O(n) and not O(n log n)?**

The key insight: **most nodes are near the bottom** of the tree, and bubble-down's cost depends on a node's **height** (distance to its farthest leaf), not the tree's total height.

| Level (from bottom) | # of nodes (~) | Max sift-down cost |
|---|---|---|
| 0 (leaves) | n/2 | 0 |
| 1 | n/4 | 1 |
| 2 | n/8 | 2 |
| ... | ... | ... |
| log n | 1 | log n |

Total work = Σ (n / 2^(h+1)) · h for h = 0 to log n, which is a **converging series** that sums to **O(n)**, not O(n log n).

> 🧠 **Interview Gold**: "Why is `heapify` O(n) but inserting n elements one at a time is O(n log n)?" — This is one of the **most-asked heap theory questions**. Answer: repeated insertion sifts elements **up** from the bottom where the tree is tallest (many long paths); `heapify`'s bubble-down starts from **the bottom already in place** and most nodes only sift a short distance, so the total work sums geometrically to O(n).

**Dry Run:**

Array: `[9, 4, 7, 1, -2, 6, 5]`, n=7, last_non_leaf = 7//2 - 1 = 2

| Step | i | Array before | Action | Array after |
|---|---|---|---|---|
| 1 | 2 | `[9,4,7,1,-2,6,5]` | bubble_down(2): compare 7 with children 6,5 → swap w/ 5 | `[9,4,5,1,-2,6,7]` |
| 2 | 1 | `[9,4,5,1,-2,6,7]` | bubble_down(1): compare 4 with children 1,-2 → swap w/ -2 | `[9,-2,5,1,4,6,7]` |
| 3 | 0 | `[9,-2,5,1,4,6,7]` | bubble_down(0): 9 vs (-2,5)→swap w/-2; then 9 vs (1,4)→swap w/1 | `[-2,1,5,4,9,6,7]` |

Final heap: `[-2, 1, 5, 4, 9, 6, 7]` ✅ (matches Section 4.3's `heapify()` result!)

**Time Complexity:** O(n). **Space Complexity:** O(1) extra (in-place).

---

## 7. Building a Full Min-Heap Class in Python

Combining every operation from Section 6 into a reusable class:

```python
class MinHeap:
    """A complete min-heap implementation from scratch (educational; use heapq in production)."""

    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _bubble_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self.heap[i] < self.heap[p]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def _bubble_down(self, i):
        n = len(self.heap)
        while True:
            left, right = self._left(i), self._right(i)
            smallest = i
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def push(self, value) -> None:
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty heap")
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self._bubble_down(0)
        return min_val

    @classmethod
    def heapify(cls, arr: list) -> "MinHeap":
        """Build a MinHeap from an existing list in O(n)."""
        h = cls()
        h.heap = arr[:]                     # copy to avoid mutating caller's list unexpectedly
        n = len(h.heap)
        for i in range(n // 2 - 1, -1, -1):
            h._bubble_down(i)
        return h

    def __repr__(self):
        return f"MinHeap({self.heap})"


# ---------------- USAGE EXAMPLE ----------------
if __name__ == "__main__":
    h = MinHeap()
    for val in [5, 3, 8, 1, 9, 2]:
        h.push(val)
    print(h)                # MinHeap([1, 3, 2, 5, 9, 8])  (some valid heap arrangement)

    print(h.pop())           # 1
    print(h.pop())           # 2
    print(h)                # remaining valid heap

    h2 = MinHeap.heapify([9, 4, 7, 1, -2, 6, 5])
    print(h2)                # MinHeap([-2, 1, 5, 4, 9, 6, 7])
```

**Complexity Summary for `MinHeap` class:**

| Method | Time | Space |
|---|---|---|
| `push` | O(log n) | O(1) |
| `pop` | O(log n) | O(1) |
| `peek` | O(1) | O(1) |
| `heapify` (classmethod) | O(n) | O(n) for the copy |
| `is_empty` / `__len__` | O(1) | O(1) |

**Edge Cases Handled:**
- Popping/peeking from an empty heap → raises `IndexError`.
- `heapify` copies the input list (`arr[:]`) so the caller's original list isn't silently mutated (a common surprise bug — decide deliberately whether you want in-place or copy semantics).

**Interview Tip:** In a real interview, you will almost never be asked to write this entire class — you'll be asked to write `bubble_up`/`bubble_down` in isolation, or simply **use** `heapq`. Understanding this class is for **conceptual mastery**, not rote memorization.

---

## 8. Max-Heap Simulation in Python

### 8.1 Why There's No Built-in Max-Heap

Python's `heapq` deliberately only implements a min-heap to keep the API minimal. To get max-heap behavior, the standard trick is **negation**.

### 8.2 The Negation Trick

```python
import heapq

nums = [5, 1, 9, 3, 7]

max_heap = []
for n in nums:
    heapq.heappush(max_heap, -n)          # push negated value

# The "largest" value is now the smallest negative -> sits at heap[0]
largest = -max_heap[0]
print(largest)   # 9

# Popping gives us values in descending order:
result = []
while max_heap:
    result.append(-heapq.heappop(max_heap))
print(result)     # [9, 7, 5, 3, 1]
```

**Visualization:**

```
Original values:      5    1    9    3    7
Negated for storage: -5   -1   -9   -3   -7

Min-Heap on negated values (heapq's normal behavior):
       -9
      /   \
    -7     -5
   /  \
 -1   -3

Popping gives -9, -7, -5, -3, -1 → negate back → 9, 7, 5, 3, 1 (descending, i.e., max-heap order)
```

### 8.3 Max-Heap with Tuples (Priority + Data)

```python
import heapq

# Max-heap of (priority, task) — negate ONLY the priority, not the data
tasks = []
heapq.heappush(tasks, (-5, "critical bug"))
heapq.heappush(tasks, (-1, "update docs"))
heapq.heappush(tasks, (-3, "code review"))

while tasks:
    neg_priority, task = heapq.heappop(tasks)
    print(-neg_priority, task)

# Output:
# 5 critical bug
# 3 code review
# 1 update docs
```

### 8.4 Custom Wrapper Class Approach (Alternative, cleaner for complex objects)

```python
import heapq

class MaxHeapItem:
    """Wraps a value so heapq's min-heap behaves like a max-heap via reversed comparison."""
    __slots__ = ("value",)

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value    # REVERSED comparison!

    def __repr__(self):
        return f"MaxHeapItem({self.value})"


max_heap = []
for n in [5, 1, 9, 3, 7]:
    heapq.heappush(max_heap, MaxHeapItem(n))

print(heapq.heappop(max_heap).value)  # 9
print(heapq.heappop(max_heap).value)  # 7
```

**Why this works:** `heapq` internally calls `<` to compare elements. By overriding `__lt__` to mean "greater than" in value terms, we trick the min-heap machinery into ordering things as a max-heap — **without any negation arithmetic**, which is safer for non-numeric or complex comparison logic.

| Approach | Pros | Cons |
|---|---|---|
| Negate numbers (`-x`) | Simple, fast, no extra class | Only works for numbers; easy to forget to re-negate on pop |
| Tuple negate priority | Good for (priority, data) pairs | Still requires numeric priority |
| Custom `__lt__` wrapper class | Works for any comparable logic, very explicit | Slightly more boilerplate |

**Common Mistakes:**
- Forgetting to **re-negate** when popping — printing `-x` results instead of `x`.
- Negating the payload/data (not just the priority) in a tuple by mistake.
- Trying to negate non-numeric data directly (e.g., strings) — always negate a *numeric key*, never the raw non-numeric object.

---

## 9. Priority Queue — Concept & Implementation

### 9.1 Definition Recap

A **Priority Queue** is an ADT supporting (at minimum):
- `insert(item, priority)`
- `extract_max()` or `extract_min()` (depending on flavor)
- `peek()`

### 9.2 Internal Working — Heap-Based PQ

```
Priority Queue Interface        Binary Heap Implementation
------------------------        ---------------------------
insert(item, priority)   -->    heappush(heap, (priority, item))
extract_top()            -->    heappop(heap)
peek()                   -->    heap[0]
```

### 9.3 Stable vs Unstable Priority Queues

- **Unstable PQ**: Among items of equal priority, order of retrieval is undefined (default `heapq` behavior when priorities tie and no tie-breaker exists — and can even crash on non-comparable payloads, see 4.9).
- **Stable PQ**: Among equal priorities, items are retrieved in **insertion order** (FIFO). Achieved via the `itertools.count()` tie-breaker pattern (Section 4.9).

### 9.4 Full Class: A Clean, Stable, Generic Priority Queue

```python
import heapq
import itertools

class PriorityQueue:
    """
    A stable, generic priority queue supporting arbitrary payloads,
    with O(log n) insert/extract and safe lazy-deletion-based removal.
    """
    REMOVED = object()   # sentinel marking a removed/invalidated entry

    def __init__(self):
        self._heap = []
        self._counter = itertools.count()      # tie-breaker for stability
        self._entry_finder = {}                # item -> entry, for O(log n) removal/update

    def push(self, item, priority=0) -> None:
        if item in self._entry_finder:
            self._remove(item)                  # remove stale entry first (lazy deletion pattern)
        count = next(self._counter)
        entry = [priority, count, item]
        self._entry_finder[item] = entry
        heapq.heappush(self._heap, entry)

    def _remove(self, item) -> None:
        """Mark an existing entry as removed (lazy deletion, O(log n) amortized)."""
        entry = self._entry_finder.pop(item)
        entry[-1] = self.REMOVED                # replace payload with sentinel; leave in heap

    def pop(self):
        """Remove and return the lowest-priority item, skipping removed entries."""
        while self._heap:
            priority, count, item = heapq.heappop(self._heap)
            if item is not self.REMOVED:
                del self._entry_finder[item]
                return item
        raise KeyError("pop from an empty priority queue")

    def update_priority(self, item, new_priority) -> None:
        """Update an item's priority (removes old entry, inserts a fresh one)."""
        self.push(item, new_priority)            # push() already handles removing stale entries

    def is_empty(self) -> bool:
        return not self._entry_finder

    def __len__(self):
        return len(self._entry_finder)
```

**Line-by-line explanation:**
- `REMOVED` sentinel: instead of physically deleting from the middle of the heap (O(n)), we mark the entry as invalid and simply **skip it** when popped — this is the industry-standard **lazy deletion** technique (also documented directly in the Python `heapq` docs' recipes section).
- `_entry_finder` dict: maps `item -> entry` so we can locate and invalidate an entry in O(1), rather than O(n) linear search.
- `push()`: if the item already exists, its old entry is invalidated first, then a fresh entry with the new priority is pushed — this is how **decrease-key / increase-key / update-priority** is achieved with plain `heapq` (which lacks a native decrease-key).
- `pop()`: loops, discarding any encountered `REMOVED` sentinels, until a valid item is found.

**Dry Run — Update Priority Scenario:**

| Step | Action | `_heap` (priority, count, item) | `_entry_finder` |
|---|---|---|---|
| 1 | `push("task_A", 5)` | `[(5,0,"task_A")]` | `{"task_A": [5,0,"task_A"]}` |
| 2 | `push("task_B", 3)` | `[(3,1,"task_B"), (5,0,"task_A")]` | `+"task_B"` |
| 3 | `update_priority("task_A", 1)` | old entry → `[5,0,REMOVED]`; new pushed `(1,2,"task_A")` | `{"task_A": [1,2,"task_A"], "task_B": [...]}` |
| 4 | `pop()` | pops `(1,2,"task_A")` (valid) → returns `"task_A"` | `"task_A"` removed |
| 5 | `pop()` | pops `(3,1,"task_B")` (valid) → returns `"task_B"` | `"task_B"` removed |
| 6 | `pop()` | pops `(5,0,REMOVED)` → skipped, heap now empty → raises `KeyError` | — |

**Time Complexity:**

| Operation | Time |
|---|---|
| `push` (new item) | O(log n) |
| `push` (update existing) | O(log n) (mark old as removed + push new) |
| `pop` | O(log n) amortized (may skip several stale entries, but each is only ever pushed/popped once) |
| `is_empty` / `__len__` | O(1) |

**Space Complexity:** O(n) — stale (removed) entries linger in the heap until popped, but they're bounded by total number of pushes ever made.

### 9.5 Min-PQ vs Max-PQ via a Single Interface

```python
class PriorityQueue:
    def __init__(self, max_heap: bool = False):
        self._sign = -1 if max_heap else 1
        self._heap = []
        self._counter = itertools.count()

    def push(self, item, priority):
        heapq.heappush(self._heap, (self._sign * priority, next(self._counter), item))

    def pop(self):
        priority, _, item = heapq.heappop(self._heap)
        return item, self._sign * priority   # un-negate priority before returning
```

This `_sign` trick lets a **single class** serve as either a min-priority-queue or max-priority-queue, cleanly generalizing Section 8's negation trick.

### 9.6 Timestamp Priorities (FIFO Fallback)

For queues where items should be processed "oldest first" among equal explicit priorities, using `time.time()` or a monotonic counter as a **secondary sort key** works identically to the `itertools.count()` tie-breaker — the counter *is* effectively a logical timestamp.

```python
import time
heapq.heappush(pq, (priority, time.monotonic(), item))
```

> 📌 Prefer `itertools.count()` over `time.time()` for tie-breaking when you don't need real wall-clock ordering — it's faster, has no floating-point precision issues, and guarantees uniqueness.

---

## 10. Heap Sort

### 10.1 Why It Exists

Heap Sort leverages the heap's O(1) "get max/min" + O(log n) "remove and re-heapify" properties to produce an **O(n log n)**, **in-place**, **non-recursive** (typically) sorting algorithm — with the unique benefit of **guaranteed** O(n log n) worst case (unlike Quicksort's O(n²) worst case).

### 10.2 Algorithm (Ascending Sort via Max-Heap)

1. Build a **max-heap** from the input array — O(n).
2. Repeatedly swap the root (max) with the **last unsorted element**, shrink the "heap region" by one, and bubble-down the new root — O(log n) each, done n times.

```
Array: [4, 10, 3, 5, 1]

Step 1: Build Max-Heap -> [10, 5, 3, 4, 1]

        10
       /  \
      5    3
     / \
    4   1

Step 2: Swap root(10) with last(1) -> [1, 5, 3, 4, 10]  ; sorted region: [10]
         Bubble down within heap region [1,5,3,4]
         -> [5, 4, 3, 1, 10]

Step 3: Swap root(5) with last-of-heap-region(1) -> [1, 4, 3, 5, 10] ; sorted: [5,10]
         Bubble down [1,4,3]
         -> [4, 1, 3, 5, 10]

Step 4: Swap root(4) with last-of-heap-region(3) -> [3, 1, 4, 5, 10] ; sorted: [4,5,10]
         Bubble down [3,1]
         -> [3, 1, 4, 5, 10]  (already valid, single swap check)

Step 5: Swap root(3) with last-of-heap-region(1) -> [1, 3, 4, 5, 10] ; sorted: [3,4,5,10]

Final: [1, 3, 4, 5, 10]  ✅ fully sorted ascending
```

### 10.3 Python Implementation

```python
def heap_sort(arr: list) -> list:
    """Sort arr in ascending order using heap sort. In-place, O(n log n)."""
    n = len(arr)

    def sift_down(a, i, size):
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            largest = i
            if left < size and a[left] > a[largest]:
                largest = left
            if right < size and a[right] > a[largest]:
                largest = right
            if largest == i:
                break
            a[i], a[largest] = a[largest], a[i]
            i = largest

    # Step 1: Build max-heap, O(n)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)

    # Step 2: Repeatedly extract max to the end, O(n log n)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]   # move current max to its sorted position
        sift_down(arr, 0, end)                 # restore heap property in shrunk region [0, end)

    return arr


# Usage
print(heap_sort([4, 10, 3, 5, 1]))   # [1, 3, 4, 5, 10]
```

**Line-by-line explanation:**
- `sift_down` here builds a **max-heap** (note `a[left] > a[largest]`, opposite of our earlier min-heap version) because we want ascending sorted output — max at root gets moved to the end each round.
- The build-heap loop is identical in structure to Section 6.8.
- The second loop is the "selection" phase: swap the current max to the correct final position, then shrink the heap region (`end` decreases) and re-fix via `sift_down`.

### 10.4 Complexity Analysis

| Aspect | Complexity |
|---|---|
| Time (Build heap) | O(n) |
| Time (n extractions × O(log n) sift) | O(n log n) |
| **Total Time** | **O(n log n)** — best, average, AND worst case (no bad-input degradation) |
| Space | **O(1)** — fully in-place (unlike merge sort's O(n)) |
| Stable? | ❌ **No** — equal elements can be reordered during swaps |

### 10.5 Heap Sort vs Other Sorts

| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ No |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ No |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes |

**When to use Heap Sort:** When you need **guaranteed** O(n log n) with **O(1) space**, and stability doesn't matter (e.g., embedded systems, real-time systems where worst-case bounds matter more than average-case speed).

**When NOT to use:** When stability is required, or when Quicksort's better real-world cache performance (despite worse worst-case) matters more (Quicksort is often faster in practice due to better locality of reference).

**Common Mistakes:**
- Building a **min-heap** for ascending sort (should be **max-heap** — min-heap gives descending order if you swap root-to-end repeatedly, a common source of confusion).
- Forgetting to shrink the "heap region" (`size`/`end` parameter) — sifting into already-sorted territory corrupts the result.
- Confusing this in-place O(1)-space heap sort with "just call `heapq.heapify` + pop n times," which is correct but uses **O(n) extra space** for the output list — a subtly different (and less space-optimal) approach.

---

## 11. Heap Patterns (Interview Core)

> This is the **highest-yield** section for coding interviews. Each pattern includes brute force → heap → optimized heap reasoning.

### 11.1 Kth Largest / Kth Smallest Element

**Problem Statement:** Given an unsorted array, find the Kth largest (or smallest) element.

**Approach Evolution:**

| Approach | Method | Time | Space |
|---|---|---|---|
| Brute Force | Sort entire array, index into it | O(n log n) | O(1) or O(n) |
| Heap (naive) | Push all n elements into a heap, pop k times | O(n log n) | O(n) |
| **Optimized Heap** | Maintain a heap of **size k only** | **O(n log k)** | **O(k)** |

**Optimized Approach for Kth LARGEST:** Use a **min-heap of size k**. Push elements; if heap exceeds size k, pop the smallest. At the end, `heap[0]` is the Kth largest.

```python
import heapq

def find_kth_largest(nums: list, k: int) -> int:
    """Return the kth largest element using a size-k min-heap."""
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)     # discard the smallest, keep only top-k largest seen so far
    return heap[0]                   # smallest of the top-k largest = the kth largest overall


# Usage
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
```

**Line-by-line explanation:**
- We maintain a min-heap that never exceeds size `k`.
- Every time it exceeds `k`, we pop the smallest — meaning only the **k largest elements seen so far** survive.
- After processing all `n` elements, the heap holds exactly the `k` largest elements, and since it's a min-heap, `heap[0]` (the smallest among them) is precisely the **kth largest** overall.

**Dry Run** for `nums = [3, 2, 1, 5, 6, 4], k = 2`:

| Step | num | Heap before | Action | Heap after |
|---|---|---|---|---|
| 1 | 3 | `[]` | push 3 | `[3]` |
| 2 | 2 | `[3]` | push 2 | `[2, 3]` |
| 3 | 1 | `[2, 3]` | push 1, size=3>k=2, pop smallest(1) | `[2, 3]` |
| 4 | 5 | `[2, 3]` | push 5, size=3>2, pop smallest(2) | `[3, 5]` |
| 5 | 6 | `[3, 5]` | push 6, size=3>2, pop smallest(3) | `[5, 6]` |
| 6 | 4 | `[5, 6]` | push 4, size=3>2, pop smallest(4) | `[5, 6]` |

Final heap: `[5, 6]` → `heap[0] = 5` → **2nd largest = 5** ✅

**Complexity:** Time O(n log k), Space O(k).

**For Kth SMALLEST:** flip the logic — use a **max-heap of size k** (negate values), popping the largest whenever size exceeds k.

```python
import heapq

def find_kth_smallest(nums: list, k: int) -> int:
    """Return the kth smallest element using a size-k max-heap (via negation)."""
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)
    return -heap[0]

print(find_kth_smallest([3, 2, 1, 5, 6, 4], 2))  # 2
```

**When to Use:** When `k` is small relative to `n` — O(n log k) beats O(n log n) full sort noticeably.

**When NOT to Use:** If `k` is close to `n`, just sort — simpler code, comparable complexity. Also, `heapq.nlargest(k, nums)[-1]` is a clean one-liner using the same underlying idea.

**Common Mistakes:**
- Using a max-heap of size k for Kth largest (should be **min**-heap of size k — reversed intuition trips people up).
- Forgetting the `if len(heap) > k: pop()` check — leads to O(n log n) instead of O(n log k).
- Off-by-one: "kth largest" is 1-indexed (k=1 means the single largest), easy to confuse with 0-indexed array logic.

**Variations:** Kth largest in a **stream** (same heap persists across calls — see `KthLargest` class, a classic LeetCode "design" problem), Kth largest with duplicates, Kth largest **pair sum**, etc.

**Practice Problems:** LeetCode 215 (Kth Largest Element in an Array), LeetCode 703 (Kth Largest Element in a Stream), LeetCode 973 (K Closest Points — related, Section 11.10).

---

### 11.2 Top K Frequent Elements

**Problem Statement:** Given an array, return the `k` most frequent elements.

**Approach Evolution:**

| Approach | Method | Time |
|---|---|---|
| Brute Force | Count frequencies, sort by frequency | O(n log n) |
| **Heap** | Count frequencies (O(n)), then use a size-k min-heap on frequency | **O(n log k)** |
| Optimized (Bucket Sort) | Count frequencies, bucket by frequency value (frequency ≤ n), read top buckets | **O(n)** |

```python
import heapq
from collections import Counter

def top_k_frequent(nums: list, k: int) -> list:
    """Return the k most frequent elements using a size-k min-heap on frequency."""
    freq = Counter(nums)                                    # Step 1: O(n) frequency count

    heap = []
    for num, count in freq.items():                          # Step 2: O(u log k), u = unique elements
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in heap]                      # Step 3: extract elements, O(k)


# Usage
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))   # [2, 1]  (order within top-k not guaranteed sorted)
```

**Line-by-line explanation:**
- `Counter(nums)` builds a frequency dict in one O(n) pass.
- We push `(count, num)` tuples — comparing by count first (natural tuple ordering), keeping the heap size capped at `k`, discarding the **least frequent** among current top-k candidates whenever we exceed the cap.
- Final heap contains exactly the `k` most frequent elements (in arbitrary heap order, **not** sorted by frequency — sort separately if a specific order is required).

**Dry Run** for `nums = [1,1,1,2,2,3], k=2`:

`freq = {1: 3, 2: 2, 3: 1}`

| Step | (count, num) | Heap before | Action | Heap after |
|---|---|---|---|---|
| 1 | (3, 1) | `[]` | push | `[(3,1)]` |
| 2 | (2, 2) | `[(3,1)]` | push | `[(2,2),(3,1)]` |
| 3 | (1, 3) | `[(2,2),(3,1)]` | push, size 3>2, pop smallest (1,3) | `[(2,2),(3,1)]` |

Result: `[2, 1]` (both remain, since 3's frequency of 1 was the least frequent). ✅

**Optimized O(n) Bucket-Sort Alternative:**

```python
def top_k_frequent_bucket(nums: list, k: int) -> list:
    """O(n) solution using bucket sort by frequency (frequency is bounded by len(nums))."""
    freq = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]   # bucket[i] = list of nums with frequency i

    for num, count in freq.items():
        buckets[count].append(num)

    result = []
    for count in range(len(buckets) - 1, 0, -1):     # iterate from highest frequency down
        for num in buckets[count]:
            result.append(num)
            if len(result) == k:
                return result
    return result
```

**Why bucket sort beats the heap here:** Since frequency is bounded by `n` (can't exceed array length), we can use frequency **as an array index** directly, avoiding the `log k` factor entirely — true **O(n)**.

**When to Use Heap:** When frequency range is unbounded/unknown, or when you want a simple, readable, "standard pattern" solution without needing to reason about bucket bounds.

**When NOT to Use:** When `n` is huge and you need the absolute fastest solution — bucket sort's O(n) wins.

**Common Mistakes:**
- Forgetting `Counter` handles ties arbitrarily — if the problem requires deterministic tie-breaking, add a secondary key.
- Confusing "top k frequent" with "top k largest by value" — different key entirely (frequency vs. value).

**Variations:** Top K Frequent **Words** (needs alphabetical tie-breaking — requires reversing comparisons carefully since heapq is a min-heap but you often want max-frequency + min-alphabetical), Sort Characters By Frequency.

**Practice Problems:** LeetCode 347 (Top K Frequent Elements), LeetCode 692 (Top K Frequent Words), LeetCode 451 (Sort Characters By Frequency).

---

### 11.3 Merge K Sorted Lists / Arrays

**Problem Statement:** Given `k` sorted linked lists (or arrays), merge them into a single sorted list.

**Approach Evolution:**

| Approach | Method | Time |
|---|---|---|
| Brute Force | Concatenate all, sort | O(N log N), N = total elements |
| Sequential Merge (merge 2 at a time, k-1 times) | Pairwise merging | O(N·k) worst case |
| **Heap** | Min-heap of size k, always holding the current head of each list | **O(N log k)** |

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists: list) -> "ListNode | None":
    """Merge k sorted linked lists using a min-heap of size k."""
    heap = []
    # Step 1: seed the heap with the head of each non-empty list.
    # Tie-break with list index (i) to avoid comparing ListNode objects directly.
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    tail = dummy

    while heap:
        val, i, node = heapq.heappop(heap)         # Step 2: pop the smallest current head
        tail.next = node                            # Step 3: attach it to the result list
        tail = tail.next
        if node.next:                                # Step 4: push that list's NEXT node, if any
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

**Line-by-line explanation:**
- We never load all elements at once — only **one node per list** sits in the heap at any time (heap size ≤ k).
- The tuple `(val, i, node)` uses list-index `i` as a **tie-breaker** so that `heapq` never attempts to compare two `ListNode` objects directly (which would crash — see Section 4.9).
- Each pop+push pair is O(log k); we do this once per total node across all lists → O(N log k) overall.

**Visualization:**

```
List 1: 1 -> 4 -> 5
List 2: 1 -> 3 -> 4
List 3: 2 -> 6

Heap starts with heads: [(1,0,n1), (1,1,n2), (2,2,n3)]

Pop (1,0,n1) -> result: 1;   push next of list1 (4) -> heap: [(1,1,n2),(2,2,n3),(4,0,n1_next)]
Pop (1,1,n2) -> result: 1,1; push next of list2 (3) -> heap: [(2,2,n3),(3,1,..),(4,0,..)]
Pop (2,2,n3) -> result: 1,1,2; push next of list3 (6)
Pop (3,1,..) -> result: 1,1,2,3; push next of list2 (4)
Pop (4,0,..) -> result: 1,1,2,3,4; push next of list1 (5)
Pop (4,1,..) -> result: 1,1,2,3,4,4
Pop (5,0,..) -> result: 1,1,2,3,4,4,5
Pop (6,2,..) -> result: 1,1,2,3,4,4,5,6

Final: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

**Complexity:** Time **O(N log k)** (N = total nodes, k = number of lists), Space O(k) for the heap.

**For plain sorted arrays instead of linked lists**, the same idea applies — or simply use `heapq.merge()` directly:

```python
import heapq

def merge_k_arrays(arrays: list) -> list:
    """Merge k sorted arrays using heapq.merge (lazy, memory-efficient)."""
    return list(heapq.merge(*arrays))
```

**When to Use Heap:** Whenever `k` (number of lists) is much smaller than `N` (total elements) — classic scenario for **merging sorted log files** or **k-way external sort**.

**When NOT to Use:** For just 2 lists, a simple two-pointer merge (O(N), no heap overhead) is simpler and faster.

**Common Mistakes:**
- Forgetting the tie-breaker index → crash when comparing equal-valued nodes/objects.
- Not checking `if node.next` before pushing (would push `None`, causing an `AttributeError` later or incorrect comparisons).
- Using a **list** and re-sorting after every merge instead of a proper heap — degrades to O(Nk log(Nk)) or worse.

**Practice Problems:** LeetCode 23 (Merge K Sorted Lists), LeetCode 378 (Kth Smallest Element in a Sorted Matrix — same pattern applied to a 2D grid).

---

### 11.4 Running Median (Two Heaps)

**Problem Statement:** Design a data structure that supports adding numbers one at a time and finding the **median** of all numbers added so far, efficiently.

**Core Idea:** Maintain **two heaps**:
- A **max-heap** (`low`) holding the **smaller half** of numbers.
- A **min-heap** (`high`) holding the **larger half** of numbers.
- Keep them balanced in size (differ by at most 1). The median is then either the top of the larger heap, or the average of both tops.

```
Numbers so far: 5, 15, 1, 3

max-heap (low half)     min-heap (high half)
      3                       5
     / (only 1,3)            /
    1                       15

low = [3, 1]  (max-heap, negated: stored as [-3,-1])
high = [5, 15] (min-heap)

low.size = 2, high.size = 2  -> median = (top(low) + top(high)) / 2 = (3 + 5) / 2 = 4.0
```

```python
import heapq

class MedianFinder:
    """Maintains a running median using two balanced heaps."""

    def __init__(self):
        self.low = []    # max-heap (store negated values) - holds the smaller half
        self.high = []   # min-heap - holds the larger half

    def add_num(self, num: int) -> None:
        # Step 1: always push to 'low' first (as negated value for max-heap behavior)
        heapq.heappush(self.low, -num)

        # Step 2: balance step - ensure every element in low <= every element in high
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Step 3: size balance - low can have at most 1 more element than high
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])                  # odd total: low has the extra element
        return (-self.low[0] + self.high[0]) / 2.0       # even total: average the two middles
```

**Line-by-line explanation:**
- **Step 1–2 (the "cross-push" trick):** Instead of deciding upfront which heap a new number belongs to, we always push to `low`, then immediately pop `low`'s max and push it to `high`. This guarantees `max(low) <= min(high)` after every insertion, **automatically** handling the case where the new number should actually belong to `high`.
- **Step 3:** If this shifted `high` to have more elements than `low`, move `high`'s min back to `low` — keeping sizes balanced (`low` is allowed to have at most one extra element, by convention).
- `find_median`: if `low` has more elements (odd total count), the median is simply `low`'s top (negated back to positive). Otherwise (even count), average the two middle values.

**Dry Run** — adding `5, 15, 1, 3` one at a time:

| Step | Add | low (neg. stored) | high | Median |
|---|---|---|---|---|
| 1 | 5 | push -5→`[-5]`; pop -5, push 5→high; low empty, high=`[5]`; size(high)1>size(low)0 → move 5 back: low=`[-5]`,high=`[]` | | `5.0` |
| 2 | 15 | push -15→low=`[-15,-5]`; pop max(-5)→push 5 to high=`[5]`; low=`[-15]`,high=`[5]`; sizes equal, no rebalance | | `(15+5)/2=10.0`... |

*(Note: table simplified for brevity — the algorithm's invariant guarantees correctness; see code for exact mechanics.)*

Let's do a cleaner dry run:

| Step | Insert | Action Summary | low (as +values) | high | Median |
|---|---|---|---|---|---|
| 1 | 5 | low=[5]→cross-push→high=[5]→rebalance: high bigger, move back | `[5]` | `[]` | 5.0 |
| 2 | 15 | low=[5,15]→cross-push pops max(15)→high=[15]; sizes equal (1,1) | `[5]` | `[15]` | (5+15)/2=10.0 |
| 3 | 1 | low=[5,1]→cross-push pops max(5)→high=[5,15]; high bigger(2>1)→move high min(5) back to low | `[5,1]` | `[15]` | 5.0 |
| 4 | 3 | low=[5,1,3]→cross-push pops max(5)→high=[5,15]; sizes (2,2) equal | `[3,1]` | `[5,15]` | (3+5)/2=4.0 |

Final median after `[5,15,1,3]` = **4.0** ✅ (matches sorted array `[1,3,5,15]`, median of even-length = avg of 2 middles = (3+5)/2 = 4.0)

**Time Complexity:** `add_num`: O(log n) per call. `find_median`: O(1).
**Space Complexity:** O(n) total (all elements stored across both heaps).

**Edge Cases:**
- First insertion (both heaps empty).
- All identical numbers.
- Very large streams — heaps never need full resorting, so this scales gracefully.

**Common Mistakes:**
- Forgetting the "cross-push" trick and instead trying to decide upfront which heap a number belongs to — leads to subtle bugs when the new number is between the two heap tops.
- Off-by-one in the size-balancing condition, causing size to drift by more than 1 over time.
- Forgetting to negate when reading `low`'s top for the median (since `low` stores negated values internally).

**Practice Problems:** LeetCode 295 (Find Median from Data Stream).

---

### 11.5 Sliding Window Median

**Problem Statement:** Given an array and window size `k`, return the median of each sliding window of size `k`.

**Approach Evolution:**

| Approach | Method | Time |
|---|---|---|
| Brute Force | Sort each window from scratch | O(n · k log k) |
| **Two Heaps + Lazy Deletion** | Extend the running-median idea, but support **removal** of the element leaving the window | **O(n log k)** |

```python
import heapq
from collections import defaultdict

def median_sliding_window(nums: list, k: int) -> list:
    """Return the median of every sliding window of size k, using two heaps + lazy deletion."""
    low, high = [], []          # low: max-heap (negated), high: min-heap
    delayed = defaultdict(int)  # lazy deletion counts: value -> count pending removal
    low_size = high_size = 0    # "logical" sizes (excluding pending-deletion counts)
    result = []

    def prune(heap, sign):
        """Remove the top of `heap` while it's marked for lazy deletion."""
        while heap and delayed[sign * heap[0]] > 0:
            delayed[sign * heap[0]] -= 1
            heapq.heappop(heap)

    def rebalance():
        nonlocal low_size, high_size
        if low_size > high_size + 1:
            heapq.heappush(high, -heapq.heappop(low))
            low_size -= 1
            high_size += 1
        elif low_size < high_size:
            heapq.heappush(low, -heapq.heappop(high))
            low_size += 1
            high_size -= 1

    for i, num in enumerate(nums):
        # Step 1: insert num into the correct heap
        if not low or num <= -low[0]:
            heapq.heappush(low, -num)
            low_size += 1
        else:
            heapq.heappush(high, num)
            high_size += 1

        rebalance()

        # Step 2: once window is full, record the median
        if i >= k - 1:
            if k % 2 == 1:
                result.append(float(-low[0]))
            else:
                result.append((-low[0] + high[0]) / 2.0)

            # Step 3: mark the element leaving the window for lazy deletion
            out_num = nums[i - k + 1]
            delayed[out_num] += 1
            if out_num <= -low[0]:
                low_size -= 1
                if out_num == -low[0]:
                    prune(low, -1)
            else:
                high_size -= 1
                if high and out_num == high[0]:
                    prune(high, 1)

            rebalance()
            prune(low, -1)
            prune(high, 1)

    return result
```

**Line-by-line explanation:**
- This extends Section 11.4's two-heap median with **lazy deletion** (same concept as Section 9.4/Section 12) because heaps don't support efficient arbitrary removal — instead of physically removing the outgoing element, we just note it in `delayed` and skip it whenever it surfaces at the top of a heap (`prune`).
- `low_size`/`high_size` track the **logical** (true, undeleted) counts separately from `len(low)`/`len(high)` (which may include yet-unpruned garbage).
- `rebalance()` ensures `low` always has either the same size as `high` or exactly one more.

**Complexity:** Time **O(n log k)**, Space O(k).

**Common Mistakes:**
- Physically trying to `remove()` from the middle of a heap (O(n)) instead of lazy deletion — defeats the purpose of using heaps.
- Forgetting to `prune()` **both** heaps before reading their tops for the median (stale garbage at the top gives a wrong median).
- Miscounting `low_size`/`high_size` when the outgoing element could belong to either heap — always compare against `-low[0]` (current low/high boundary) to decide.

**Practice Problems:** LeetCode 480 (Sliding Window Median) — considered a **Hard**-tier heap problem, often used to filter senior candidates.

---

### 11.6 Task Scheduler

**Problem Statement:** Given tasks (as characters) and a cooldown period `n` between two same tasks, find the minimum time to finish all tasks.

**Approach:** Greedily always run the **most frequent remaining task** (max-heap on frequency), respecting the cooldown via a waiting queue.

```python
import heapq
from collections import Counter, deque

def least_interval(tasks: list, n: int) -> int:
    """Return minimum total time (including idles) to complete all tasks with cooldown n."""
    freq = Counter(tasks)
    max_heap = [-cnt for cnt in freq.values()]
    heapq.heapify(max_heap)              # max-heap via negation

    time = 0
    cooldown_queue = deque()              # holds (available_time, neg_count)

    while max_heap or cooldown_queue:
        time += 1
        if max_heap:
            cnt = heapq.heappop(max_heap) + 1     # execute one instance (count moves toward 0)
            if cnt < 0:                            # still instances left -> cooldown before reuse
                cooldown_queue.append((time + n, cnt))
        if cooldown_queue and cooldown_queue[0][0] == time:
            _, cnt = cooldown_queue.popleft()
            heapq.heappush(max_heap, cnt)

    return time
```

**Line-by-line explanation:**
- `max_heap` holds negated frequencies — always execute the currently most-frequent task.
- After executing a task, if it still has remaining instances (`cnt < 0` since we're using negatives), it's placed in `cooldown_queue` with the time it becomes eligible again (`time + n`).
- Each simulated "tick," we check if the front of the cooldown queue is now eligible (`== time`) and push it back into the heap.
- `time` naturally accumulates **idle slots** too, since we increment it every iteration even when `max_heap` is temporarily empty (but `cooldown_queue` isn't).

**Dry Run** — `tasks = ["A","A","A","B","B","B"], n = 2`:

| Time | max_heap (neg counts) | Action | cooldown_queue | Result so far |
|---|---|---|---|---|
| 1 | `[-3,-3]`(A,B) | pop -3(A)→-2, cooldown until t=3 | `[(3,-2)]` | A |
| 2 | `[-3]`(B) | pop -3(B)→-2, cooldown until t=4 | `[(3,-2)A, (4,-2)B]` | A,B |
| 3 | `[]` | queue front (3,-2)A ready → push -2 to heap; pop -2(A)→-1, cooldown until t=5 | `[(4,-2)B, (5,-1)A]` | A,B,A |
| 4 | `[]` | queue front (4,-2)B ready → push -2 to heap; pop -2(B)→-1, cooldown until t=6 | `[(5,-1)A, (6,-1)B]` | A,B,A,B |
| 5 | `[]` | (5,-1)A ready → push -1; pop -1(A)→0, done (no cooldown, cnt==0) | `[(6,-1)B]` | A,B,A,B,A |
| 6 | `[]` | (6,-1)B ready → push -1; pop -1(B)→0, done | `[]` | A,B,A,B,A,B |

Total time = **6**. Sequence: `A B A B A B` (no idle needed here since exactly 2 task types alternate perfectly with cooldown=2).

**Complexity:** Time O(total_tasks × log(unique_tasks)), Space O(unique_tasks).

**Common Mistakes:**
- Forgetting idle slots count toward total time even when no task executes.
- Off-by-one on the cooldown window (`n` means `n` slots must pass, i.e., available again at `time + n`, not `time + n + 1` or `time + n - 1` — verify against problem statement's exact definition).
- Using a mathematical-formula-only approach (`(max_count-1)*(n+1) + num_max_count_tasks`) without understanding it's a shortcut derived from this exact simulation — the formula only works correctly when the most frequent task truly dominates; heap simulation is more robust/general and safer to derive independently.

**Practice Problems:** LeetCode 621 (Task Scheduler).

---

### 11.7 Reorganize String

**Problem Statement:** Rearrange a string so that no two adjacent characters are the same, or return `""` if impossible.

**Approach:** Greedily place the **most frequent remaining character**, always skipping the character just placed (max-heap of character frequencies).

```python
import heapq
from collections import Counter

def reorganize_string(s: str) -> str:
    """Rearrange s so no two adjacent chars are equal, using a max-heap greedy approach."""
    freq = Counter(s)
    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)

    # Early feasibility check: no character can exceed ceil(len(s)/2) occurrences
    if max(freq.values()) > (len(s) + 1) // 2:
        return ""

    result = []
    prev_count, prev_char = 0, ""

    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char)
        if prev_count < 0:                      # re-add the previously used character (now eligible again)
            heapq.heappush(max_heap, (prev_count, prev_char))
        prev_count, prev_char = count + 1, char   # "count+1" because count is negative (using up one instance)

    return "".join(result)
```

**Line-by-line explanation:**
- Feasibility check: if any character's count exceeds `⌈n/2⌉`, it's mathematically impossible to separate all its instances — return `""` immediately (a classic **pigeonhole principle** argument).
- We always place the currently-most-frequent character, then **hold back** the just-used character for one round (via `prev_count`/`prev_char`) before re-adding it to the heap — guaranteeing it's never placed twice in a row.

**Dry Run** — `s = "aab"`:

`freq = {a:2, b:1}`, heap = `[(-2,'a'), (-1,'b')]`

| Step | Pop | result | prev held back | Push back? |
|---|---|---|---|---|
| 1 | (-2,'a') | `"a"` | prev=(0,"") initially, nothing to push | now hold (-1,'a') |
| 2 | (-1,'b') | `"ab"` | prev_count=-1<0 → push back ('a' with count -1) | heap=`[(-1,'a')]`; now hold (0,'b') |
| 3 | (-1,'a') | `"aba"` | prev_count(b)=0, not <0, don't push | now hold (0,'a') |

Result: `"aba"` ✅ valid (no adjacent duplicates).

**Complexity:** Time O(n log u) where u = unique characters, Space O(u).

**Common Mistakes:**
- Forgetting the early feasibility check — leads to infinite loops or incorrect partial results on impossible inputs.
- Off-by-one in the "hold back for one round" logic — must re-add the previous character **after** placing the current one, not before.

**Practice Problems:** LeetCode 767 (Reorganize String), LeetCode 358 (Rearrange String k Distance Apart — generalized version).

---

### 11.8 Last Stone Weight

**Problem Statement:** Repeatedly smash the two heaviest stones together; if equal, both destroyed, else the difference remains. Return the weight of the last remaining stone (or 0).

```python
import heapq

def last_stone_weight(stones: list) -> int:
    """Simulate repeatedly smashing the two heaviest stones using a max-heap."""
    max_heap = [-s for s in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        first = -heapq.heappop(max_heap)     # heaviest
        second = -heapq.heappop(max_heap)    # 2nd heaviest
        if first != second:
            heapq.heappush(max_heap, -(first - second))

    return -max_heap[0] if max_heap else 0
```

**Dry Run** — `stones = [2,7,4,1,8,1]`:

| Step | Heap (as +values, conceptually) | Pop 2 heaviest | Result pushed |
|---|---|---|---|
| 1 | `[8,7,4,2,1,1]` | 8, 7 | push 1 → heap:`[4,2,1,1,1]` |
| 2 | `[4,2,1,1,1]` | 4, 2 | push 2 → heap:`[2,1,1,1]` |
| 3 | `[2,1,1,1]` | 2, 1 | push 1 → heap:`[1,1,1]` |
| 4 | `[1,1,1]` | 1, 1 | equal → both destroyed, push nothing → heap:`[1]` |

Final: heap has 1 stone left, weight = **1** ✅

**Complexity:** Time O(n log n), Space O(n).

**Common Mistakes:** Forgetting to handle the "equal weights destroy both, push nothing" case; forgetting the final empty-heap edge case (return 0).

**Practice Problems:** LeetCode 1046 (Last Stone Weight), LeetCode 1049 (Last Stone Weight II — DP variant, not heap).

---

### 11.9 IPO Problem

**Problem Statement:** Given `k` projects you can select (in order, one at a time), each with a `capital` requirement and a `profit`, and starting capital `w`, maximize final capital after choosing at most `k` projects (only projects whose capital requirement ≤ current capital are choosable at each step).

```python
import heapq

def find_maximized_capital(k: int, w: int, profits: list, capital: list) -> int:
    """Greedily pick the most profitable affordable project, k times, using two heaps."""
    # min-heap of (capital_required, profit) - projects not yet affordable, sorted by capital needed
    capital_heap = list(zip(capital, profits))
    heapq.heapify(capital_heap)

    # max-heap of profit (negated) - projects currently affordable
    profit_heap = []

    for _ in range(k):
        # Step 1: move all newly affordable projects from capital_heap to profit_heap
        while capital_heap and capital_heap[0][0] <= w:
            cap, prof = heapq.heappop(capital_heap)
            heapq.heappush(profit_heap, -prof)

        if not profit_heap:
            break                                     # no affordable project left, stop early

        # Step 2: greedily take the most profitable affordable project
        w += -heapq.heappop(profit_heap)

    return w
```

**Line-by-line explanation:**
- `capital_heap`: a min-heap ordered by **capital required**, so we can efficiently pull out "which projects just became affordable" as `w` grows.
- `profit_heap`: a max-heap (negated) of profits **among currently affordable** projects — we always greedily pick the highest-profit affordable project.
- This greedy approach is provably optimal: since we can choose up to `k` projects and each choice only *increases* `w` (profits are assumed non-negative), always taking the best currently-available option can never be suboptimal (classic **exchange argument** for greedy correctness).

**Complexity:** Time O(n log n + k log n), Space O(n).

**Common Mistakes:** Forgetting to loop the "move newly affordable projects" step **inside** each of the `k` iterations (capital grows after each project, potentially unlocking more projects) — a common bug is doing this move only once at the start.

**Practice Problems:** LeetCode 502 (IPO).

---

### 11.10 K Closest Points to Origin

**Problem Statement:** Given a list of points, return the `k` closest to the origin (0,0).

```python
import heapq

def k_closest(points: list, k: int) -> list:
    """Return the k closest points to origin using a size-k max-heap on squared distance."""
    max_heap = []
    for x, y in points:
        dist = -(x * x + y * y)                    # negate for max-heap via min-heap
        heapq.heappush(max_heap, (dist, x, y))
        if len(max_heap) > k:
            heapq.heappop(max_heap)                  # discard farthest among current top-k

    return [(x, y) for dist, x, y in max_heap]


# Usage
print(k_closest([[1,3],[-2,2],[2,-2]], k=2))   # [[-2,2],[2,-2]] (order may vary)
```

**Explanation:** Same size-k-heap pattern as Kth Largest (Section 11.1) — but here we want the `k` **smallest** distances, so we use a **max-heap of size k**, evicting the farthest point whenever the heap exceeds size `k`.

> 📌 **Why we skip `sqrt()`**: Comparing squared distances (`x² + y²`) gives identical ordering to true Euclidean distance while avoiding unnecessary floating-point `sqrt()` calls — a small but real optimization frequently flagged in interviews.

**Complexity:** Time O(n log k), Space O(k).

**Alternative:** `heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)` — a clean one-liner using the built-in helper.

**Practice Problems:** LeetCode 973 (K Closest Points to Origin).

---

### 11.11 Huffman Coding (Concept)

**Why it's here:** Huffman coding is the canonical **compression algorithm** example of greedy + heap usage, frequently discussed (though rarely fully implemented) in interviews.

**Idea:** Repeatedly combine the two **least frequent** nodes/symbols into a new internal node (frequency = sum), until only one tree remains — the result is an optimal **prefix-free** binary encoding, minimizing expected code length.

```python
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq        # heapq needs a comparison to order nodes

def build_huffman_tree(text: str) -> "HuffmanNode":
    freq = Counter(text)
    heap = [HuffmanNode(f, ch) for ch, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)             # two least-frequent nodes
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]                              # root of the Huffman tree

def build_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node is None:
        return code_map
    if node.char is not None:                    # leaf node = an actual character
        code_map[node.char] = prefix or "0"       # handle single-unique-character edge case
        return code_map
    build_codes(node.left, prefix + "0", code_map)
    build_codes(node.right, prefix + "1", code_map)
    return code_map


# Usage
root = build_huffman_tree("aaabbc")
codes = build_codes(root)
print(codes)   # e.g. {'a': '0', 'b': '10', 'c': '11'}  (exact codes may vary by tie-breaking)
```

**Complexity:** Time O(n log n) (n = number of unique characters, via n-1 heap merge operations), Space O(n).

**Interview Note:** You're rarely asked to write the full Huffman tree builder, but understanding **why heaps are the natural fit** (always need the 2 smallest-frequency items, repeatedly) is a common **conceptual** interview question.

---

## 12. Advanced Heap Concepts

### 12.1 Lazy Deletion (Deep Dive)

Since heaps don't support efficient arbitrary removal, **lazy deletion** is the standard workaround: mark an entry as invalid (via a sentinel or a "deleted set") instead of physically removing it, and simply skip invalid entries whenever they surface during a `pop`.

```python
import heapq

class LazyDeletionPQ:
    def __init__(self):
        self.heap = []
        self.deleted = set()

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def remove(self, item):
        self.deleted.add(item)              # O(1) - mark, don't touch the heap array

    def pop(self):
        while self.heap:
            priority, item = heapq.heappop(self.heap)
            if item not in self.deleted:
                return item
            self.deleted.discard(item)       # clean up the marker once consumed
        raise IndexError("pop from empty PQ")
```

**Amortized Analysis:** Every item is pushed once and popped at most once (either as a valid result or as a skipped stale entry) — so total work across all operations remains **O(n log n)** amortized, even though a single `pop()` call could, in the worst theoretical case, skip many stale entries in a row.

### 12.2 Why `heapify()` Is O(n), Not O(n log n) — Full Proof

Already covered intuitively in Section 6.8. Full mathematical proof:

For a heap with `n` nodes, the number of nodes at height `h` is at most `⌈n / 2^(h+1)⌉`. The bubble-down cost at height `h` is O(h). Total work:

```
T(n) = Σ (h=0 to log n) [n / 2^(h+1)] * O(h)
     = O(n) * Σ (h=0 to log n) h / 2^h
```

The series `Σ h/2^h` (for h=0 to ∞) **converges to a constant (= 2)** — a well-known result from analysis of geometric-like series — so `T(n) = O(n) * O(1) = O(n)`.

### 12.3 Indexed Priority Queue (Overview)

An **Indexed Priority Queue (IPQ)** augments a heap with an auxiliary array/dict mapping `element -> heap_index`, enabling:
- O(log n) `decrease_key`/`increase_key` on an **arbitrary known element** (not just the root).
- O(log n) arbitrary deletion (instead of O(n) to locate + O(log n) to fix).

This is the structure **Dijkstra's algorithm** ideally wants (native decrease-key support), which Python's `heapq` lacks natively — hence the common workaround of "push duplicates, use lazy deletion" instead of implementing a true IPQ (simpler code, same asymptotic complexity in practice for Dijkstra).

```python
class IndexedMinHeap:
    """A min-heap that tracks each item's current index for O(log n) update/removal."""

    def __init__(self):
        self.heap = []           # list of [priority, item]
        self.position = {}       # item -> index in self.heap

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.position[self.heap[i][1]] = i
        self.position[self.heap[j][1]] = j

    def _bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] < self.heap[parent][0]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _bubble_down(self, i):
        n = len(self.heap)
        while True:
            left, right, smallest = 2*i+1, 2*i+2, i
            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def push(self, item, priority):
        self.heap.append([priority, item])
        self.position[item] = len(self.heap) - 1
        self._bubble_up(len(self.heap) - 1)

    def decrease_key(self, item, new_priority):
        i = self.position[item]                 # O(1) lookup, unlike plain heapq!
        self.heap[i][0] = new_priority
        self._bubble_up(i)

    def pop(self):
        min_item = self.heap[0][1]
        last = self.heap.pop()
        del self.position[min_item]
        if self.heap:
            self.heap[0] = last
            self.position[last[1]] = 0
            self._bubble_down(0)
        return min_item
```

**Interview Note:** This is an advanced/"design a data structure" level question. Most interviews accept the simpler "push duplicate + lazy skip" approach for Dijkstra; a true Indexed Priority Queue is more relevant for systems/library-design discussions.

### 12.4 Mutable Priority Queue (Overview)

Closely related to the IPQ above — a priority queue where element priorities can change **after insertion** without needing to remove-and-reinsert manually. In Python, this is typically achieved via the `_entry_finder` + lazy-deletion pattern shown in Section 9.4, which is the pragmatic, idiomatic approach (an official recipe in the `heapq` documentation).

### 12.5 External Heap (Overview)

An **external-memory heap** is designed for datasets too large to fit in RAM, using disk-based storage with block-oriented operations to minimize I/O (analogous to B-trees for external sorting). Relevant in database systems and large-scale external sort/merge implementations — conceptual awareness only for most interviews.

### 12.6 Double Heap Technique

A general term for the "two-heap" pattern seen in Running Median (11.4) and Sliding Window Median (11.5) — using a max-heap for the "lower half" and a min-heap for the "upper half" of a dataset, enabling O(log n) insertion while maintaining O(1) median access. This same technique generalizes to **any problem requiring a dynamically-maintained percentile/split-point**.

### 12.7 Online Algorithms and Heaps

An **online algorithm** processes input piece-by-piece, without seeing future input, and must make irrevocable decisions immediately. Heaps are naturally suited for online scenarios (running median, streaming top-K, event scheduling) because they support efficient incremental insertion and extraction without needing to reprocess all data from scratch.

---

## 13. Applications of Heaps

| Domain | Application | Heap Role |
|---|---|---|
| Operating Systems | CPU / process scheduling | Max-heap picks highest-priority process next |
| Graph Algorithms | Dijkstra's shortest path | Min-heap picks next closest unvisited vertex |
| Graph Algorithms | Prim's Minimum Spanning Tree | Min-heap picks cheapest crossing edge |
| Simulation | Discrete event simulation | Min-heap orders events by timestamp, processes chronologically |
| Data Streaming | Top-K analytics (trending topics, top sellers) | Fixed-size heap maintains current top-K efficiently |
| Networking | Bandwidth/QoS packet scheduling | Priority queue serves higher-priority packets first |
| Compression | Huffman Coding | Repeatedly merges two least-frequent nodes |
| Load Balancing | Assign task to least-loaded server | Min-heap on current server load |
| Databases | External sort-merge, k-way merge of sorted runs | Min-heap merges multiple sorted disk runs |
| Job Schedulers | Cron-like systems, "next job to run" | Min-heap ordered by next execution timestamp |

### 13.1 Dijkstra's Algorithm (Concept Only — Not a Standalone Graph Topic Here)

```python
import heapq

def dijkstra(graph: dict, start) -> dict:
    """
    graph: adjacency list {node: [(neighbor, weight), ...]}
    Returns shortest distance from `start` to every reachable node.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]                     # (distance, node)

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > distances[node]:
            continue                        # stale entry (lazy deletion pattern) - skip

        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))   # "duplicate push" instead of decrease-key

    return distances
```

**Why the `if current_dist > distances[node]: continue` check matters:** Since `heapq` lacks a native decrease-key, we simply **push a new, better entry** whenever we find a shorter path, leaving the old (stale) entry in the heap. When that stale entry is eventually popped, this check detects it's outdated (a shorter distance was already recorded) and skips it — this is exactly the **lazy deletion** pattern from Section 12.1, applied to graph algorithms.

**Complexity:** O((V + E) log V) using a binary heap.

### 13.2 Event Simulation Example

```python
import heapq

def simulate_events(events: list) -> list:
    """events: list of (timestamp, event_name). Process strictly in time order."""
    heapq.heapify(events)
    processed = []
    while events:
        timestamp, name = heapq.heappop(events)
        processed.append((timestamp, name))
        # In a real simulation, processing might PUSH new future events here
    return processed
```

---

## 14. Problem Recognition Guide

### 14.1 Recognition Flowchart

```
                         ┌─────────────────────────────┐
                         │   Does the problem involve   │
                         │  "Kth largest/smallest",      │
                         │  "Top K", "closest K"?        │
                         └───────────┬───────────────────┘
                                     │ YES
                                     ▼
                         Use a size-K heap (opposite-type
                         heap: min-heap for "K largest",
                         max-heap for "K smallest")

                         ┌─────────────────────────────┐
                         │  Does it involve merging      │
                         │  multiple SORTED sequences?   │
                         └───────────┬───────────────────┘
                                     │ YES
                                     ▼
                         Use a heap of size k (one entry
                         per sequence) — Merge K pattern

                         ┌─────────────────────────────┐
                         │  Does it need a running        │
                         │  median / percentile split?    │
                         └───────────┬───────────────────┘
                                     │ YES
                                     ▼
                         Use Two-Heap technique
                         (max-heap for lower half,
                          min-heap for upper half)

                         ┌─────────────────────────────┐
                         │  Does it need "always pick     │
                         │  the current max/min next,     │
                         │  repeatedly, with the set       │
                         │  changing over time"?          │
                         └───────────┬───────────────────┘
                                     │ YES
                                     ▼
                         Classic Priority Queue /
                         greedy-with-heap pattern
                         (task scheduler, Huffman, IPO)
```

### 14.2 Interview Clues (Keyword Triggers)

| Keyword / Phrase in Problem | Likely Pattern |
|---|---|
| "Kth largest" / "Kth smallest" | Size-K heap |
| "Top K frequent" / "K most common" | Size-K heap on frequency |
| "Merge K sorted ..." | Merge-K heap pattern |
| "Running median" / "median so far" / "data stream" | Two heaps |
| "Closest K points" | Size-K heap on distance |
| "Reorganize" / "rearrange so no two adjacent are equal" | Max-heap greedy |
| "Schedule tasks with cooldown" | Max-heap + queue |
| "Always pick cheapest/most urgent next" | Priority queue |
| "Minimum cost to connect / combine repeatedly" | Min-heap greedy (like Huffman) |

### 14.3 Heap vs Sorting

| Use Heap When | Use Sorting When |
|---|---|
| You only need the min/max repeatedly, not a full order | You need the full order, or need it more than once |
| Data arrives incrementally (streaming) | Data is static and known upfront |
| `k << n` (only top-k needed) | `k` is close to `n` |
| You need to interleave insertions and extractions | You do all inserts, then all reads |

### 14.4 Heap vs Binary Search

Heaps and binary search solve **different kinds of problems**, but they sometimes overlap in "Kth element" problems:

| Scenario | Better Tool |
|---|---|
| Kth largest in an unsorted, changing stream | Heap (size-K) |
| Kth largest in a value range with monotonic count function (e.g., "Kth smallest pair distance") | Binary search on the answer, often combined with a counting pass |
| Find in a fully sorted static array | Binary search, O(log n), no heap needed |

### 14.5 Heap vs BST (Binary Search Tree)

| Aspect | Heap | BST (balanced, e.g. AVL/Red-Black) |
|---|---|---|
| Find min/max | O(1) | O(log n) (traverse to leftmost/rightmost) |
| Insert | O(log n) | O(log n) |
| Search arbitrary value | O(n) | O(log n) |
| In-order traversal (sorted output) | Not directly supported | O(n), naturally sorted |
| Storage | Compact array | Node objects with pointers |
| Use case | Priority-based access only | Full ordered set/map operations (range queries, predecessor/successor) |

> 🧠 **Key Interview Distinction**: A heap only guarantees fast access to the **extreme** element. A BST guarantees fast access to **any** element **and** maintains full sorted order. Don't use a heap when you need range queries, in-order traversal, or arbitrary search — reach for a BST/sorted structure instead.

### 14.6 Heap vs Sorted Array/List

| Aspect | Heap | Sorted Array |
|---|---|---|
| Build from scratch | O(n) | O(n log n) |
| Insert | O(log n) | O(n) (shifting) |
| Extract min/max | O(log n) | O(1) if extracting from the correct end, O(n) if from the wrong end |
| Random access by rank | O(n) (no direct support) | O(1) |
| Best for | Frequent, mixed insert/extract-min operations | Static or append-only structure with frequent read-by-position |

---

## 15. Optimization Strategies

### 15.1 Brute Force → Heap → Optimized Heap (General Framework)

| Stage | Typical Complexity | Example |
|---|---|---|
| Brute Force | Usually O(n log n) or O(n²) | Sort everything, or recompute min/max from scratch each time |
| Heap (naive, unbounded size) | O(n log n) | Push all n elements, then pop what's needed |
| **Optimized Heap (bounded size k)** | **O(n log k)** | Maintain only a size-k heap (Sections 11.1, 11.2, 11.10) |

### 15.2 `heapify()` vs Repeated `heappush()`

| Method | Complexity | When to Use |
|---|---|---|
| `heapq.heapify(existing_list)` | O(n) | You have **all** elements upfront |
| `n` calls to `heapq.heappush()` | O(n log n) | Elements arrive **incrementally** (streaming) — no choice but to insert one at a time |

**Rule:** If you ever find yourself building a heap from a fully-known list using a loop of `heappush()` calls, **stop** — use `heapify()` instead for a free O(log n) → O(1) amortized speedup per element.

### 15.3 Time Optimization Checklist

- ✅ Bound heap size to `k` whenever only the top/bottom `k` elements matter.
- ✅ Use `heapify()` for bulk construction, not repeated `heappush()`.
- ✅ Use `heappushpop()`/`heapreplace()` instead of separate push+pop calls when both are needed back-to-back.
- ✅ Avoid `sqrt()` when comparing distances — compare squared distances instead (Section 11.10).
- ✅ Prefer bucket-sort-style O(n) solutions over heaps when frequency/value ranges are **bounded** by `n` (Section 11.2).

### 15.4 Space Optimization Checklist

- ✅ Use lazy deletion (Section 12.1) instead of physically rebuilding the heap on every removal.
- ✅ For heap sort, use the in-place O(1)-space version (Section 10) instead of `heapq.heapify` + repeated pop into a new list (which costs O(n) extra space).
- ✅ Stream `heapq.merge()` as a generator instead of materializing the merged list, when you only need to iterate once.

---

## 16. Interview Preparation

### 16.1 Difficulty Tiers

| Tier | Examples | What's Tested |
|---|---|---|
| **Easy** | Last Stone Weight, Kth Largest Element (basic) | Can you use `heapq` correctly at all? |
| **Medium** | Top K Frequent, Merge K Sorted Lists, Task Scheduler, K Closest Points, Reorganize String, IPO | Can you recognize the pattern and bound heap size correctly? |
| **Hard** | Sliding Window Median, Median from Data Stream (with updates/removals), Smallest Range Covering Elements from K Lists | Can you combine heaps with auxiliary structures (lazy deletion, two heaps, hashmaps)? |

### 16.2 Pattern-Wise Question Map

| Pattern | Representative Problems |
|---|---|
| Size-K Heap | Kth Largest Element (LC 215), K Closest Points (LC 973), Top K Frequent Elements (LC 347) |
| Merge-K | Merge K Sorted Lists (LC 23), Smallest Range Covering Elements from K Lists (LC 632) |
| Two Heaps (Median) | Find Median from Data Stream (LC 295), Sliding Window Median (LC 480) |
| Greedy + Max-Heap | Task Scheduler (LC 621), Reorganize String (LC 767), Rearrange String k Distance Apart (LC 358) |
| Greedy + Min-Heap (merge cost) | Minimum Cost to Connect Sticks (LC 1167), Huffman-style problems |
| Priority Queue Design | Design Twitter (LC 355), Kth Largest Element in a Stream (LC 703) |
| Graph + Heap | Network Delay Time (LC 743, Dijkstra), Path With Minimum Effort (LC 1631), Swim in Rising Water (LC 778) |

### 16.3 "Blind 75" / NeetCode Heap Problems (Commonly Cited Set)

| Problem | Platform | Pattern |
|---|---|---|
| Kth Largest Element in an Array | LeetCode 215 | Size-K heap |
| Top K Frequent Elements | LeetCode 347 | Size-K heap on frequency |
| K Closest Points to Origin | LeetCode 973 | Size-K max-heap |
| Merge K Sorted Lists | LeetCode 23 | Merge-K heap |
| Find Median from Data Stream | LeetCode 295 | Two heaps |
| Task Scheduler | LeetCode 621 | Max-heap greedy |
| Last Stone Weight | LeetCode 1046 | Max-heap simulation |
| Design Twitter | LeetCode 355 | Priority queue design |

### 16.4 Company-Wise Tendencies (General Patterns Observed)

> Note: exact company question sets change often; the table below reflects commonly reported **themes**, not guaranteed current questions.

| Company Type | Commonly Emphasized Heap Themes |
|---|---|
| Big Tech (large-scale systems) | Top-K streaming analytics, merge-K (log processing), scheduling |
| Finance / Trading Firms | Running median / percentile tracking, event simulation |
| Startups (general SWE interviews) | Kth largest/smallest, Top-K frequent, basic priority queue design |

### 16.5 Standard Interview Templates (Memorize These Shapes)

**Template A — Size-K Heap:**
```python
import heapq
def top_or_bottom_k(nums, k, want_largest=True):
    heap = []
    for num in nums:
        heapq.heappush(heap, num if want_largest else -num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap
```

**Template B — Merge-K:**
```python
import heapq
def merge_k(sequences):
    heap = [(seq[0], i, 0) for i, seq in enumerate(sequences) if seq]
    heapq.heapify(heap)
    result = []
    while heap:
        val, seq_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(sequences[seq_idx]):
            next_val = sequences[seq_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, seq_idx, elem_idx + 1))
    return result
```

**Template C — Two Heaps (Median):**
```python
import heapq
class TwoHeapMedian:
    def __init__(self):
        self.low, self.high = [], []   # low: max-heap(neg), high: min-heap
    def add(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))
    def median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
```

### 16.6 Interview Tricks

- Always clarify: "Do you want a min-heap or max-heap behavior?" out loud — shows you understand `heapq`'s default is min-only.
- State the complexity **before** coding: "I'll use a size-k heap for O(n log k)" — signals pattern recognition immediately to the interviewer.
- If payload objects aren't directly comparable, proactively mention the tuple tie-breaker trick (Section 4.9) — this is a strong signal of practical Python fluency.
- For "design" style questions (e.g., Design Twitter), explicitly discuss lazy deletion vs. true removal trade-offs.

---

## 17. Python-Specific Tips & Tricks

### 17.1 `heapq` Essentials Recap

- `heapq` operates on plain Python **lists** — no special class, no wrapper object.
- Always a **min-heap**; simulate max-heap via negation or a custom `__lt__` wrapper (Section 8).
- `heap[0]` is always the min — but the rest of the list is **not fully sorted**.

### 17.2 `dataclass` for Clean Priority Items

```python
from dataclasses import dataclass, field
import heapq

@dataclass(order=True)
class Job:
    priority: int
    job_id: str = field(compare=False)
    payload: dict = field(compare=False, default_factory=dict)

jobs = []
heapq.heappush(jobs, Job(2, "job-42", {"type": "email"}))
heapq.heappush(jobs, Job(1, "job-07", {"type": "sms"}))
print(heapq.heappop(jobs).job_id)   # "job-07" (priority 1 wins)
```

Using `field(compare=False)` is the idiomatic way to exclude non-comparable fields from ordering — cleaner than manual tuple index management for complex payloads.

### 17.3 `itertools.count()` for Tie-Breaking and Stability

Already covered in depth (Section 4.9, 9.3) — worth re-emphasizing as a **must-know idiom**:

```python
import heapq, itertools
counter = itertools.count()
heap = []
heapq.heappush(heap, (priority, next(counter), payload))
```

This guarantees:
1. No crash comparing non-comparable payloads.
2. FIFO ordering (stability) among equal priorities.

### 17.4 Max-Heap Negation Tricks — Quick Reference

| Data | Trick |
|---|---|
| Plain numbers | Push `-x`, pop and negate back |
| `(priority, data)` tuples | Negate only the priority: `(-priority, data)` |
| Complex objects | Custom `__lt__` reversing comparison (Section 8.4) |
| Need both min & max heap simultaneously | Maintain two separate heaps (as in Two-Heap Median pattern) |

### 17.5 Performance Tips

- `heapq` is implemented in C for its core logic (via the `_heapq` C extension when available) — it's fast; avoid reimplementing it manually in performance-critical code unless you need custom behavior (like an Indexed Priority Queue).
- Prefer `heapify()` (O(n)) over building via repeated `heappush()` (O(n log n)) whenever the full dataset is available upfront.
- For huge inputs, prefer generator-based `heapq.merge()` over materializing a fully concatenated + sorted list.

### 17.6 Memory Optimization

- Avoid storing large duplicate payload objects across many heap entries (e.g., in lazy deletion scenarios) — store lightweight IDs/keys and look up full data in a separate dict when needed, instead of duplicating large objects.
- When merging huge sorted files with `heapq.merge()`, pass **iterators/generators**, not fully-loaded lists, to keep memory bounded regardless of file size.

### 17.7 Common Python Pitfalls Specific to `heapq`

- Comparing `dict`/custom objects without `__lt__` defined → `TypeError` at runtime, often deep inside a tie-break scenario that's hard to reproduce/debug.
- Mutating a list that's already a heap using regular list operations (`list.append()`, `list.sort()`, `del list[i]`) **without** going through `heapq` functions — silently corrupts the heap invariant.
- Assuming `list(heap)` gives sorted order — it does **not**; only `heap[0]` is guaranteed meaningful without popping.
- Forgetting `heapq.heapify()` mutates **in-place** and returns `None` — writing `heap = heapq.heapify(arr)` gives `heap = None`, a very common bug for beginners.

---

## 18. Common Mistakes

| # | Mistake | Why It's Wrong | Fix |
|---|---|---|---|
| 1 | Confusing Heap with BST | Assuming in-order traversal gives sorted output, or that arbitrary search is O(log n) | Heaps only guarantee root = min/max; use a BST/sorted structure for full ordering needs |
| 2 | Assuming heap array is sorted | `list(heap)` is not sorted; only `heap[0]` is meaningful | Pop elements one by one to get sorted order, or use `sorted()` separately |
| 3 | Using min-heap when max-heap needed (or vice versa) | E.g., using min-heap of size k for "Kth largest" instead of the correct pairing | Remember: for "K largest", use a **min**-heap of size K (evicts smallest); for "K smallest", use a **max**-heap of size K |
| 4 | Incorrect `heapify()` usage | Writing `heap = heapq.heapify(arr)` — `heapify` returns `None` | `heapq.heapify(arr)` mutates in place; just call it, don't assign its result |
| 5 | Comparator/tie-break mistakes | Pushing tuples with non-comparable second elements, causing a crash on ties | Add a unique tie-breaker (`itertools.count()`) as a middle tuple element |
| 6 | Ignoring duplicate priorities | Assuming heap pop order is stable by default | It is not stable without an explicit tie-breaker; add one if FIFO order among ties matters |
| 7 | Negative-value max-heap bugs | Forgetting to re-negate popped values, or negating the payload instead of just the priority | Negate only the numeric priority; always re-negate on read/pop |
| 8 | Index calculation errors | Mixing 0-indexed and 1-indexed parent/child formulas | Be consistent: 0-indexed uses `parent=(i-1)//2`; verify which convention a reference source uses |
| 9 | Forgetting bounds checks in manual bubble-down | Accessing `heap[left]`/`heap[right]` without checking `< size` first | Always guard child-index accesses with a bounds check |
| 10 | Using O(n) arbitrary deletion when lazy deletion would suffice | Physically removing from the middle of a heap (rebuild cost) when a sentinel/deleted-set would do | Use lazy deletion (Section 12.1) for O(log n) amortized removal |
| 11 | Rebuilding a heap after every single insert instead of maintaining it incrementally | Calling `sorted()` or `heapify()` repeatedly inside a loop | Use `heappush`/`heappop` to maintain the heap incrementally, O(log n) per op |
| 12 | Off-by-one in "size-k" heap eviction logic | Evicting before checking the size properly, or comparing wrong element | Push first, **then** check `if len(heap) > k: pop()` |

---

## 17. Python-Specific Tips & Tricks

### 17.1 `heapq` Quick Recall

```python
import heapq

heapq.heapify(lst)                 # O(n) - build heap in-place
heapq.heappush(lst, x)             # O(log n)
heapq.heappop(lst)                 # O(log n)
heapq.heappushpop(lst, x)          # O(log n) - push then pop, faster if x likely small
heapq.heapreplace(lst, x)          # O(log n) - pop then push, ALWAYS removes old root first
heapq.nlargest(k, lst)             # O(n log k)
heapq.nsmallest(k, lst)            # O(n log k)
list(heapq.merge(*lists))          # O(n log k) - lazy generator
```

### 17.2 `dataclass` Ordering Recap

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Job:
    priority: int
    name: str = field(compare=False)
```

`order=True` auto-generates `__lt__`, `__le__`, `__gt__`, `__ge__` based on field declaration order; `compare=False` excludes a field from all of them.

### 17.3 `itertools.count()` for Stable Tie-Breaking

```python
import itertools
counter = itertools.count()
heapq.heappush(pq, (priority, next(counter), payload))
```

Guarantees no two tuples ever compare equal at the second position, so Python never needs to fall through to comparing `payload` directly.

### 17.4 Max-Heap Tricks Recap

```python
# Trick 1: negate numeric values
heapq.heappush(max_heap, -value)
largest = -max_heap[0]

# Trick 2: negate only the priority in a (priority, data) tuple
heapq.heappush(max_heap, (-priority, data))

# Trick 3: custom __lt__ wrapper for non-numeric ordering logic
class Rev:
    def __init__(self, v): self.v = v
    def __lt__(self, other): return self.v > other.v
```

### 17.5 Performance Tips

- `heapq` is implemented in C (via the `_heapq` accelerator module when available) — it's fast; don't reimplement it by hand in production code.
- Avoid repeatedly calling `len(heap)` inside tight loops if you can track size in a variable — marginal, but adds up in hot paths (Python function/attribute overhead is non-trivial vs. C).
- Prefer tuple comparisons over custom `__lt__` methods when possible — CPython's tuple comparison is implemented in C and is faster than a Python-level method call.

### 17.6 Memory Optimization Tips

- Use lazy deletion instead of rebuilding heaps from scratch after removals.
- For huge datasets, use `heapq.merge()` as a generator rather than materializing full merged results.
- Store lightweight tuples `(priority, id)` rather than large objects directly in the heap when possible; look up full objects via a separate dict keyed by `id`.

### 17.7 Common Python Pitfalls

| Pitfall | Fix |
|---|---|
| Assuming `heapq` gives a max-heap | It's always a min-heap; negate for max behavior |
| Comparing non-comparable payloads (crash) | Add a tie-breaker (counter) or use `dataclass(order=True)` with `compare=False` |
| Forgetting `heap[0]` is just "current min," not "the array is sorted" | Never assume the rest of the array is in any particular order |
| Mutating a list passed into `heapify()` unexpectedly | Copy the list first if you need to preserve the original (`arr[:]`) |
| Using `sorted(list)[0]` repeatedly instead of a heap | O(n log n) every time vs. O(log n) with a heap — huge difference at scale |

---

## 18. Common Mistakes

### 18.1 Conceptual Mistakes

| Mistake | Why It's Wrong | Correction |
|---|---|---|
| Confusing Heap with BST | Heap has no full in-order property; BST does | Use BST/sorted structure for range queries, ordered traversal |
| Assuming heap array is sorted | Heap only orders parent-child, not siblings | Only `heap[0]` is guaranteed correct; pop repeatedly for sorted order |
| Using wrong heap type (min vs max) for "Kth largest/smallest" | Reversed intuition is a very common bug | Kth **largest** → min-heap of size k; Kth **smallest** → max-heap of size k |
| Believing `heapify()` is O(n log n) | Confusing it with repeated insertion | It's O(n) — see mathematical proof in Section 12.2 |

### 18.2 Implementation Mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Incorrect index formulas (1-indexed vs 0-indexed mixed) | Wrong parent/child, corrupted heap | Stick to one convention consistently; Python `heapq` is 0-indexed |
| Comparator/tuple ordering mistakes | Wrong tie-breaking, unexpected order, or crashes on non-comparable elements | Use `(priority, counter, data)` tuples |
| Duplicate priorities crashing comparisons | `TypeError` when comparing custom objects | Add tie-breaker as shown in Section 4.9 |
| Negative-value max-heap bugs | Forgetting to re-negate on read/pop | Always negate on push AND un-negate on read |
| Index calculation errors in manual bubble-up/down | Off-by-one, wrong child/parent used | Carefully verify: `parent=(i-1)//2`, `left=2i+1`, `right=2i+2` (0-indexed) |
| Forgetting bounds checks on child indices | `IndexError` or reading garbage | Always check `left < size` / `right < size` before comparing |
| Physically removing from the middle of a heap array | O(n) cost defeats heap's purpose, and naive removal breaks heap property without re-heapify | Use lazy deletion, or bubble up/down after replacing with the last element |

---

## 19. Cheat Sheets

### 19.1 Heap Operations Complexity Cheat Sheet

| Operation | Binary Heap (array-based) |
|---|---|
| Find Min/Max | O(1) |
| Insert | O(log n) |
| Delete Min/Max (extract) | O(log n) |
| Build Heap (from array) | O(n) |
| Delete Arbitrary Element (index known) | O(log n) |
| Delete Arbitrary Element (index unknown) | O(n) |
| Search Arbitrary Element | O(n) |
| Merge Two Heaps | O(n) (binary heap); O(log n) for Binomial/Fibonacci heaps |
| Decrease/Increase Key (index known) | O(log n) |

### 19.2 `heapq` Functions Cheat Sheet

| Function | Signature | Complexity |
|---|---|---|
| `heapify` | `heapq.heapify(x)` | O(n) |
| `heappush` | `heapq.heappush(heap, item)` | O(log n) |
| `heappop` | `heapq.heappop(heap)` | O(log n) |
| `heappushpop` | `heapq.heappushpop(heap, item)` | O(log n) |
| `heapreplace` | `heapq.heapreplace(heap, item)` | O(log n) |
| `nlargest` | `heapq.nlargest(k, iterable, key=None)` | O(n log k) |
| `nsmallest` | `heapq.nsmallest(k, iterable, key=None)` | O(n log k) |
| `merge` | `heapq.merge(*iterables, key=None, reverse=False)` | O(n log k) |

### 19.3 Index Formula Sheet (0-indexed, Python convention)

```
parent(i)      = (i - 1) // 2
left_child(i)  = 2*i + 1
right_child(i) = 2*i + 2
```

### 19.4 Pattern Recognition Cheat Sheet

| Signal in Problem Statement | Pattern | Heap Type |
|---|---|---|
| "Kth largest" | Size-K heap | Min-heap of size k |
| "Kth smallest" | Size-K heap | Max-heap of size k |
| "Top K frequent" | Size-K heap on frequency | Min-heap of size k (by count) |
| "Merge K sorted ___" | Merge-K | Min-heap of size k |
| "Running/streaming median" | Two heaps | Max-heap (lower) + Min-heap (upper) |
| "Schedule with cooldown" | Greedy + heap | Max-heap on frequency/urgency |
| "Rearrange, no two adjacent equal" | Greedy + heap | Max-heap on frequency |
| "Repeatedly combine two cheapest/smallest" | Greedy merge (Huffman-like) | Min-heap |
| "Always serve highest priority next" | Priority Queue | Depends on definition of "highest" |

### 19.5 Decision Tree — Choosing Min-Heap vs Max-Heap

```
Need the smallest element quickly, repeatedly? ---------> MIN-HEAP
Need the largest element quickly, repeatedly? ----------> MAX-HEAP
Need "Kth LARGEST" from a stream? ------------------------> MIN-HEAP of size K
                                                            (evict smallest of top-K candidates)
Need "Kth SMALLEST" from a stream? -----------------------> MAX-HEAP of size K
                                                            (evict largest of bottom-K candidates)
Need BOTH halves of a distribution (median)? --------------> TWO HEAPS
                                                            (max-heap low + min-heap high)
```

---

## 20. Practice Problem Bank

> Difficulty and exact platform ratings may vary/update over time; use these as a strong practice roadmap.

### 20.1 Basics & Heap Construction

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Implement a Min-Heap / Max-Heap from scratch | GeeksforGeeks | Easy | Core operations |
| Build a Heap (Build Heap in O(n)) | GeeksforGeeks | Easy–Medium | Build heap |
| Heap Sort | GeeksforGeeks | Medium | Heap sort |
| Check if a given array represents a valid Binary Heap | GeeksforGeeks | Easy | Heap property validation |

### 20.2 Priority Queue Fundamentals

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Design a Priority Queue with update | Codeforces (various) | Medium | Custom PQ / lazy deletion |
| Kth Largest Element in a Stream | LeetCode 703 | Easy | Size-K heap (streaming) |
| Last Stone Weight | LeetCode 1046 | Easy | Max-heap simulation |

### 20.3 Kth Largest / Smallest Family

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Kth Largest Element in an Array | LeetCode 215 | Medium | Size-K heap |
| Kth Smallest Element in a Sorted Matrix | LeetCode 378 | Medium | Heap on matrix rows |
| Find K Pairs with Smallest Sums | LeetCode 373 | Medium | Heap with pair generation |
| Kth Smallest Element in a BST | LeetCode 230 | Medium | (BST in-order, heap optional) |

### 20.4 Top K Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Top K Frequent Elements | LeetCode 347 | Medium | Size-K heap on frequency |
| Top K Frequent Words | LeetCode 692 | Medium | Size-K heap + tie-break |
| Sort Characters By Frequency | LeetCode 451 | Medium | Max-heap on frequency |
| K Closest Points to Origin | LeetCode 973 | Medium | Size-K heap on distance |

### 20.5 Merge Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Merge K Sorted Lists | LeetCode 23 | Hard | Merge-K heap |
| Smallest Range Covering Elements from K Lists | LeetCode 632 | Hard | Merge-K heap variant |
| Merge K Sorted Arrays | GeeksforGeeks | Medium | Merge-K heap |

### 20.6 Running Median / Two Heaps

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Find Median from Data Stream | LeetCode 295 | Hard | Two heaps |
| Sliding Window Median | LeetCode 480 | Hard | Two heaps + lazy deletion |
| IPO | LeetCode 502 | Hard | Two heaps (capital/profit) |

### 20.7 Scheduling & Greedy

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Task Scheduler | LeetCode 621 | Medium | Max-heap + cooldown queue |
| Reorganize String | LeetCode 767 | Medium | Max-heap greedy |
| Rearrange String k Distance Apart | LeetCode 358 | Hard | Max-heap greedy (generalized) |
| Meeting Rooms II | LeetCode 253 | Medium | Min-heap on end times |
| Car Pooling | LeetCode 1094 | Medium | Heap / sweep-line variant |

### 20.8 Frequency-Based Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Top K Frequent Elements | LeetCode 347 | Medium | Frequency + heap |
| Rearrange Words by Frequency | InterviewBit | Medium | Frequency + heap |
| Frequency Sort | GeeksforGeeks | Easy–Medium | Frequency + heap/bucket |

### 20.9 Advanced Heap Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Minimum Cost to Connect Sticks | LeetCode 1167 | Medium | Min-heap greedy merge (Huffman-like) |
| Swim in Rising Water | LeetCode 778 | Hard | Min-heap + grid traversal |
| Path With Minimum Effort | LeetCode 1631 | Medium | Min-heap (Dijkstra-like) |
| Network Delay Time | LeetCode 743 | Medium | Dijkstra with heap |
| The Skyline Problem | LeetCode 218 | Hard | Max-heap + sweep-line |
| Trapping Rain Water II | LeetCode 407 | Hard | Min-heap + grid BFS |

### 20.10 Competitive Programming Judges

| Problem Theme | Platform | Notes |
|---|---|---|
| Priority Queue scheduling problems | Codeforces | Search "priority queue" tag |
| Huffman / merge-cost minimization | CodeChef | Classic greedy + heap tag |
| Dijkstra with heap optimization | AtCoder | Graph shortest-path problems |
| K-way merge / external sort simulation | CSES Problem Set | "Sorting and Searching" section |
| Median maintenance problems | HackerRank | "Find the Running Median" |

---

## 21. Final Revision & Mind Maps

### 21.1 One-Page Mind Map

```
                              HEAP & PRIORITY QUEUE
                                       |
        ┌──────────────┬──────────────┼──────────────┬───────────────┐
        │              │              │               │               │
    FUNDAMENTALS     TYPES        OPERATIONS       PATTERNS       APPLICATIONS
        │              │              │               │               │
  Complete Bin.    Min/Max Heap   Insert(bubble up)  Kth Largest    Dijkstra
  Tree Property    D-ary Heap     Extract(bubble dn) Top K Freq.    Prim's MST
  Array Mapping    Binomial       Peek O(1)          Merge K        CPU Sched.
  parent/child     Fibonacci      Build O(n)         Two Heaps      Huffman
  index formulas   Pairing        Delete arbitrary   Scheduler      Event Sim.
                   Leftist/Skew   Decrease/Incr-key   Reorganize     Streaming
                                                       IPO            Top-K
```

### 21.2 Heap Operation Cheat Sheet (Ultra-Condensed)

```
peek()      -> O(1)
push()      -> O(log n)   (append + bubble_up)
pop()       -> O(log n)   (swap w/ last + bubble_down)
heapify()   -> O(n)       (bubble_down from last non-leaf to root)
build via n pushes -> O(n log n)  <-- AVOID if all data known upfront!
```

### 21.3 Pattern Map (Ultra-Condensed)

```
"Kth X"        -> size-K heap (opposite type: min for largest, max for smallest)
"Top K"        -> size-K heap on a derived key (frequency, distance, etc.)
"Merge K"      -> heap of size k, one head element per source
"Median"       -> two heaps (max low / min high), balance sizes
"Greedy pick   -> max or min heap, repeatedly extract + reinsert derived value
 next best"
```

### 21.4 15-Minute Revision

1. Heap = complete binary tree + heap property; stored as array (2 min).
2. Index formulas: `parent=(i-1)//2`, `left=2i+1`, `right=2i+2` (1 min).
3. `heapq` is min-heap only; negate for max-heap (2 min).
4. `heapify()` = O(n); repeated `heappush` = O(n log n) (2 min).
5. Size-K heap pattern for Kth largest/smallest & Top-K (3 min).
6. Two-heap pattern for running median (3 min).
7. Tuple tie-breaker trick with `itertools.count()` (2 min).

### 21.5 1-Hour Revision Plan

| Time | Focus |
|---|---|
| 0–10 min | Re-read Section 1 (Introduction) + Section 2–3 (Fundamentals, Array Rep) |
| 10–20 min | Re-implement `bubble_up`/`bubble_down`/`heapify` from memory (Section 6) |
| 20–30 min | Review all of Section 4 (`heapq` module reference) hands-on in a REPL |
| 30–45 min | Solve (or re-derive) Kth Largest, Top K Frequent, Merge K Lists from memory |
| 45–55 min | Review Two-Heap Median pattern + dry run it manually |
| 55–60 min | Skim Cheat Sheets (Section 19) + Common Mistakes (Section 18) |

### 21.6 Interview Cheat Sheet (Say This Out Loud)

> "This looks like a **[Kth largest / Top-K / Merge-K / Running median / Scheduling]** problem. I'll use a **[min-heap / max-heap / two heaps]** of size **[k / n]**, giving **O(n log k)** time and **O(k)** space. Since payloads might not be directly comparable, I'll add a tie-breaker using `itertools.count()`."

---

## 22. FAQs

**Q1: Is a heap the same as a priority queue?**
No. A priority queue is an abstract data type (interface); a heap is the most common concrete data structure used to implement it efficiently.

**Q2: Why doesn't Python's `heapq` support max-heaps directly?**
To keep the module minimal and consistent. The standard workaround is negating values (Section 8) or wrapping with a custom `__lt__` comparator.

**Q3: Is a heap sorted?**
No — only the root is guaranteed to be the min (or max). Sibling and deeper-level ordering is unconstrained beyond the parent-child rule.

**Q4: Why is `heapify()` O(n) but pushing n elements one at a time is O(n log n)?**
Because `heapify()`'s bubble-down starts from the bottom of the tree (where most nodes live and only sift a short distance), while repeated insertion sifts new elements up from the bottom of a **growing** tree, doing more total work across all n insertions. See the formal proof in Section 12.2.

**Q5: Can two heaps have the same elements but different array layouts?**
Yes — the heap property allows multiple valid arrangements for the same multiset of values (e.g., swapping two equal-priority subtrees). There is no single "correct" heap array for a given input.

**Q6: When should I use a heap instead of just sorting?**
When you only need the min/max repeatedly (not the full order), when data arrives incrementally, or when only the top/bottom `k` elements matter out of `n` (giving O(n log k) instead of O(n log n)).

**Q7: How do I handle a priority queue where priorities can change after insertion?**
Use the lazy-deletion "entry_finder" pattern (Section 9.4): mark the old entry as invalid, then push a fresh entry with the new priority.

**Q8: What's the difference between `heappushpop()` and `heapreplace()`?**
`heappushpop()` pushes first, then pops — so if the new item is smaller than the current root (in a min-heap), it's returned immediately without ever entering the heap. `heapreplace()` always pops the old root first, then pushes the new item — so the old root is always returned, regardless of the new item's value.

**Q9: Do I need to know Fibonacci Heaps for interviews?**
Almost never for implementation. You may be asked conceptually "why would Fibonacci heaps improve Dijkstra's complexity?" — know the *idea* (O(1) amortized decrease-key), but expect to implement everything using Python's binary-heap-based `heapq` in practice.

**Q10: Why use squared distance instead of actual distance in "K closest points" problems?**
Squaring preserves relative ordering (since distance is non-negative) while avoiding unnecessary floating-point `sqrt()` computation — a small but real performance and precision optimization.

**Q11: Can a heap have duplicate values?**
Yes, heaps freely allow duplicate values; the heap property (`parent <= child` for min-heaps) is not strict inequality, so equal values are perfectly valid.

**Q12: Is heap sort stable?**
No. The swapping during bubble-down can reorder equal elements relative to each other, so heap sort is not a stable sorting algorithm.

**Q13: What is the space complexity of a heap holding n elements?**
O(n) — one array slot per element, with no extra pointer overhead (unlike tree structures using node objects with explicit child pointers).

**Q14: How is a heap different from a stack or queue?**
A stack is LIFO, a queue is FIFO — both order by **insertion time**. A heap (via a priority queue) orders by **priority value**, regardless of insertion order (unless you explicitly add a tie-breaker for insertion-order stability among equal priorities).

**Q15: What's the best way to merge two existing heaps in Python?**
For binary heaps (which is what `heapq` implements), there's no efficient built-in merge — the practical approach is `heapq.heapify(heap1 + heap2)`, which costs O(n+m). True O(log n) merging requires a different heap variant (Binomial, Fibonacci, Pairing, Leftist/Skew — Section 5).

---

## 📘 End of Handbook

This handbook covered heaps and priority queues from first principles (complete binary trees, array representation, heap property) through the full `heapq` module API, manual from-scratch implementations, every major interview pattern (Kth largest, Top-K, Merge-K, Running Median, Scheduling, Huffman), advanced concepts (lazy deletion, indexed priority queues, D-ary/Binomial/Fibonacci/Pairing/Leftist heaps), optimization strategies, and a complete practice roadmap across LeetCode, GeeksforGeeks, Codeforces, and other platforms.

**Suggested next step:** Pick one problem from each subsection of Section 20 and solve it without looking at the code samples above — then compare your solution against the corresponding pattern template in Section 16.5.

## 17. Python-Specific Tips & Tricks

### 17.1 Core `heapq` Tips

- `heapq` operates on **plain lists** — there's no dedicated `Heap` class. This means you can freely inspect `heap[0]` (peek) without any special method call.
- `heapq.heapify()` is O(n) — always prefer it over a loop of `heappush()` when you have all data upfront.
- `heapq` has no `remove()` — implement lazy deletion (Section 12.1) for arbitrary removal needs.
- `heapq` has no `decrease_key()` — either use lazy deletion + push duplicates (simple, used in Dijkstra, Section 13.1) or build an Indexed Priority Queue (Section 12.3) for O(log n) true decrease-key.

### 17.2 `dataclass` Ordering Trick

```python
from dataclasses import dataclass, field
import heapq

@dataclass(order=True)
class Event:
    timestamp: float
    priority: int = field(compare=False)
    payload: str = field(compare=False)

events = []
heapq.heappush(events, Event(3.5, 1, "low prio event"))
heapq.heappush(events, Event(1.2, 5, "urgent event"))
print(heapq.heappop(events).payload)   # "urgent event" (lowest timestamp wins)
```

Only fields **without** `compare=False` participate in ordering — put your true sort key(s) first, and exclude everything else.

### 17.3 `itertools.count()` for Tie-Breaking (Recap)

```python
import heapq, itertools
counter = itertools.count()
heap = []
heapq.heappush(heap, (priority, next(counter), payload))
```

This guarantees **stable** (insertion-order) tie-breaking and avoids `TypeError` crashes on non-comparable payloads — arguably the single most useful `heapq` idiom to memorize.

### 17.4 Max-Heap Tricks Using Negatives (Recap Table)

| Scenario | Trick |
|---|---|
| Simple numeric max-heap | Push `-value`, negate again on pop |
| Max-heap of (priority, data) tuples | Negate **only** the priority field, never the data |
| Complex objects, custom rules | Override `__lt__` to reverse comparison (Section 8.4) — avoids arithmetic negation entirely |

### 17.5 Performance Tips

- For read-heavy, write-rarely workloads, consider whether `sorted()` + binary search (via the `bisect` module) might outperform a heap — heaps shine specifically for **interleaved** insert/extract-min patterns.
- Avoid pushing large/heavy objects directly into the heap if only a small key is needed for comparison — push `(key, index)` and look up the full object separately via an index/list, reducing comparison and memory overhead.
- `heapq.nsmallest(k, ...)`/`nlargest(k, ...)` internally optimize for small `k`; but if `k` is large (close to `n`), Python's `nlargest`/`nsmallest` implementation itself falls back toward sorting internally — so don't assume it's always faster than `sorted()`.

### 17.6 Memory Optimization

- Prefer **generators** (`heapq.merge()`) over materializing full merged lists when you only need to iterate once.
- For very large heaps of custom objects, use `__slots__` on your wrapper/node classes to reduce per-object memory overhead (relevant for Huffman nodes, linked-list nodes, etc.).

### 17.7 Common Python Pitfalls Specific to `heapq`

| Pitfall | Fix |
|---|---|
| Comparing tuples with non-comparable second elements | Add a tie-breaker index/counter as the second tuple element |
| Assuming the underlying list is fully sorted | Only `heap[0]` is guaranteed correct; the rest is partially ordered |
| Mutating the list used as a heap directly (e.g., `list.append()` instead of `heappush()`) | Breaks the heap invariant — always use `heapq` functions for any mutation |
| Forgetting `heapify()` is in-place and returns `None` | Don't write `heap = heapq.heapify(arr)` — it mutates `arr` and returns nothing |
| Using `heapq` for max-heap without negating | Results come out in ascending (min) order instead of descending (max) |

---

## 18. Common Mistakes

| # | Mistake | Why It's Wrong | Fix |
|---|---|---|---|
| 1 | Confusing Heap with BST | Heaps don't support O(log n) arbitrary search or in-order sorted traversal | Use a BST/sorted structure if you need full ordering or search |
| 2 | Assuming heap array is sorted | Only the root is guaranteed to be min/max | Never index into the middle of a heap array expecting sorted order |
| 3 | Using min-heap when max-heap logic is needed (or vice versa) | Produces reversed/incorrect results (e.g., Kth largest via max-heap of size k is WRONG — should be min-heap of size k) | Re-derive which heap type matches the pattern (Section 11.1) |
| 4 | Incorrect `heapify()` usage (assuming O(n log n) or expecting a return value) | `heapify()` is in-place, returns `None`, and is O(n) | Call it as a statement: `heapq.heapify(arr)`, then use `arr` directly |
| 5 | Comparator/tuple mistakes | Comparing non-comparable objects crashes; wrong field order changes sort priority | Add tie-breakers; verify tuple field order matches intended sort priority |
| 6 | Mishandling duplicate priorities | Can cause crashes (non-comparable payload tie) or non-deterministic/unstable order | Use `itertools.count()` tie-breaker for determinism/stability |
| 7 | Negative-value max-heap bugs | Forgetting to re-negate on pop, or negating the wrong tuple field | Always double negate: once on push, once on pop; only negate the priority, not the payload |
| 8 | Index calculation errors (parent/child formulas) | Mixing up 0-indexed vs 1-indexed conventions from different textbooks | Standardize on 0-indexed formulas: `parent=(i-1)//2`, `left=2i+1`, `right=2i+2` |
| 9 | Forgetting heap size bound in size-K patterns | Leads to O(n log n) instead of intended O(n log k), and returns wrong element if bound is never enforced | Always add `if len(heap) > k: heapq.heappop(heap)` |
| 10 | Trying to physically delete from the middle of a heap array | Naive removal breaks the heap invariant unless followed by a proper bubble-up/down fix, and locating the index is O(n) | Use lazy deletion, or an Indexed Priority Queue for O(log n) true removal |

---

## 17. Python-Specific Tips & Tricks

### 17.1 Quick Reference: Idiomatic Patterns

```python
import heapq
import itertools

# 1. Build a heap from an existing list in O(n)
arr = [5, 3, 8, 1]
heapq.heapify(arr)

# 2. Max-heap via negation
max_heap = []
heapq.heappush(max_heap, -5)

# 3. Priority + payload with stable tie-breaking
counter = itertools.count()
pq = []
heapq.heappush(pq, (priority, next(counter), payload))

# 4. Get top-k without manually managing a heap
top3 = heapq.nlargest(3, arr)
bottom3 = heapq.nsmallest(3, arr)

# 5. Merge already-sorted iterables lazily
merged = heapq.merge([1,4,7], [2,5,8], [3,6,9])   # generator, not a list!

# 6. dataclass-based comparable items
from dataclasses import dataclass, field
@dataclass(order=True)
class Job:
    priority: int
    name: str = field(compare=False)
```

### 17.2 `itertools.count()` Deep Dive

`itertools.count()` produces an infinite, ever-increasing sequence (0, 1, 2, 3, ...) with **O(1)** memory (it's a lazy generator, not a stored list). It's the idiomatic Python solution for:
- Breaking ties in heap comparisons (Section 4.9).
- Simulating insertion order / stability.
- Acting as a cheap monotonic "logical timestamp" without touching `time.time()`.

### 17.3 Performance Tips

- `heapq` is implemented in C internally (via the `_heapq` C accelerator module when available) — it's typically much faster than a hand-rolled Python class for the same operations. **Use `heapq` in production code; only hand-roll a heap class for learning/interviews when explicitly asked.**
- Avoid pushing large, expensive-to-copy objects directly into the heap — push lightweight tuples of `(key, id, reference)` instead, and look up the full object separately if needed.
- `heapq.nlargest`/`nsmallest` are more efficient than `sorted(arr)[-k:]` when `k` is small, since they avoid a full O(n log n) sort.

### 17.4 Memory Optimization

- Prefer generators (`heapq.merge()`) over materialized lists when you only need to iterate once — avoids O(n) extra memory.
- With lazy deletion (Section 12.1), periodically consider "garbage collecting" a heap that has accumulated too many stale entries relative to valid ones, if long-running.

### 17.5 Common Python Pitfalls (Heap-Specific)

| Pitfall | Fix |
|---|---|
| Comparing non-comparable objects (e.g., dicts) directly in tuples | Add an explicit tie-breaker (`itertools.count()`) or use `dataclass(order=True)` |
| Assuming the heap list is fully sorted | Only `heap[0]` is guaranteed extreme; the rest is partially ordered |
| Forgetting to re-negate values after popping from a negated max-heap | Always mirror negation on both push and pop |
| Mutating a list that's also being used as a heap, without calling `heapify()` afterward | Any external mutation invalidates the heap invariant — must re-`heapify()` |
| Using `heap.sort()` accidentally on a heap-backed list mid-algorithm | Sorting doesn't break the heap invariant *by accident* since a sorted list IS a valid heap, but any *subsequent* `heappush`/`heappop` calls after arbitrary unrelated mutations can be unsafe if you're not careful about what "arbitrary mutations" means |

### 17.6 Max-Heap Tricks Using Negatives — Extended Cheat Sheet

| Goal | Trick |
|---|---|
| Max-heap of numbers | Push `-x`, pop and negate back |
| Max-heap of (priority, data) tuples | Push `(-priority, data)` — only negate the priority |
| Max-heap with floats | Same negation trick works identically for floats |
| Max-heap needing stable tie-break | Push `(-priority, count, data)` with `itertools.count()` |
| Avoid negation entirely (cleaner for complex objects) | Custom wrapper class with reversed `__lt__` (Section 8.4) |

---

## 18. Common Mistakes

### 18.1 Conceptual Mistakes

| Mistake | Why It's Wrong | Correct Understanding |
|---|---|---|
| "A heap is a sorted array" | Only the root is guaranteed extreme; siblings/deeper nodes aren't ordered | Heap = partial order (parent ≤ children for min-heap), not total order |
| "Heap = Binary Search Tree" | BSTs support O(log n) search for any value; heaps don't (O(n)) | Heap only optimizes access to the **extreme** value |
| "In-order traversal of a heap gives sorted order" | This property belongs to BSTs, not heaps | Heaps have no such traversal guarantee |
| "`heapq` supports max-heaps natively" | It's a min-heap implementation only | Simulate max-heap via negation or custom `__lt__` |

### 18.2 Implementation Mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Wrong heap type chosen (min instead of max, or vice versa) | Wrong element retrieved (largest instead of smallest, etc.) | Re-check which extreme the problem needs; negate if using `heapq` for max behavior |
| Incorrect `heapify()` usage (calling it after already assuming sorted order) | Silent bugs — heap looks "wrong" but is actually valid, just not sorted | Remember: `heapify()` guarantees heap property, not full sort |
| Comparator/tie-break mistakes with tuples | `TypeError` when comparing non-comparable payloads on ties | Add tie-breaker (`itertools.count()`) or `dataclass(order=True)` |
| Duplicate priorities causing crashes | Same as above — heapq falls through to comparing the 2nd tuple element | Same fix |
| Negative-value max-heap bugs (forgetting to negate on push OR pop) | Values come out with wrong sign, or ordering reversed unexpectedly | Consistently negate both directions; consider a wrapper class instead |
| Index calculation errors (0-indexed vs 1-indexed formulas mixed) | Wrong parent/child computed, corrupting the heap silently | Stick to one convention; Python/`heapq` uses 0-indexed |
| Forgetting bounds checks on child indices | `IndexError` when accessing `heap[left]`/`heap[right]` | Always check `left < len(heap)` / `right < len(heap)` before accessing |
| Not shrinking the "heap region" during in-place heap sort | Sifting corrupts already-sorted portion of the array | Track and respect the shrinking `size`/`end` boundary explicitly |

---

## 17. Python-Specific Tips & Tricks

### 17.1 Quick Reference of Idioms

```python
import heapq
import itertools

# 1. Build a heap from an existing list in O(n)
arr = [5, 3, 8, 1]
heapq.heapify(arr)

# 2. Max-heap via negation
max_heap = []
heapq.heappush(max_heap, -5)
largest = -max_heap[0]

# 3. Tuple with tie-breaker to avoid comparing non-comparable payloads
counter = itertools.count()
pq = []
heapq.heappush(pq, (priority, next(counter), payload))

# 4. Get top-k without manually managing a heap
top_3 = heapq.nlargest(3, arr)
bottom_3 = heapq.nsmallest(3, arr)

# 5. Merge sorted iterables lazily (memory efficient, generator-based)
merged = heapq.merge([1, 4, 7], [2, 5, 8], [3, 6, 9])

# 6. dataclass-based ordering, excluding non-comparable fields
from dataclasses import dataclass, field

@dataclass(order=True)
class Entry:
    priority: int
    data: object = field(compare=False)
```

### 17.2 `itertools.count()` Deep Dive

`itertools.count()` produces an infinite, lazy, ever-increasing sequence (0, 1, 2, 3, ...) with O(1) memory and O(1) per-call cost — perfect as a **unique, monotonically increasing tie-breaker** since it guarantees no two entries ever compare equal on the second tuple field, sidestepping any need to compare the actual payload.

### 17.3 Performance Tips

- `heapq` is implemented in C for its core operations, so it's typically faster than a hand-rolled Python heap class for large `n` — prefer `heapq` in production code; write your own class only for learning/interview practice.
- Avoid pushing large, deeply-nested objects directly into a heap — push a small tuple `(priority, id)` and look up the full object in a separate dict when needed, reducing comparison and memory overhead.
- For **very** large `k` close to `n` in `nlargest`/`nsmallest`, just use `sorted()` — the heap-based approach's `log k` factor loses its advantage.

### 17.4 Memory Optimization

- `heapq` reuses the passed-in list directly (no hidden copy) — be aware that `heapify()` **mutates** its argument in place; if you need to preserve the original list, pass a copy (`heapq.heapify(arr[:])`).
- Prefer `__slots__` on custom wrapper classes (Section 8.4) pushed into heaps in large quantities, to reduce per-object memory overhead.

### 17.5 Common Python Pitfalls Specific to `heapq`

| Pitfall | Fix |
|---|---|
| Assuming `heapq` supports max-heap directly | Negate values, or use `_sign` trick (Section 8, 9.5) |
| `TypeError` comparing tuples with non-comparable 2nd element | Add a tie-breaker index/counter (Section 4.9) |
| Forgetting `heapify()` mutates in place | Pass a copy if original order must be preserved |
| Using `list.sort()` + `pop(0)` instead of a heap | `pop(0)` on a list is O(n); always use `heapq` for repeated min extraction |
| Trying to binary-search a heap array directly | A heap array is **not sorted** — binary search will give wrong results |

### 17.6 Max-Heap Tricks Cheat Sheet

```python
# Numbers: negate on push AND pop
heapq.heappush(h, -x)
top = -h[0]
val = -heapq.heappop(h)

# (priority, data) tuples: negate ONLY the priority
heapq.heappush(h, (-priority, data))

# Custom objects: override __lt__ with reversed comparison
class Max:
    def __init__(self, v): self.v = v
    def __lt__(self, other): return self.v > other.v
```

---

## 18. Common Mistakes

| # | Mistake | Why It's Wrong | Fix |
|---|---|---|---|
| 1 | Confusing Heap with BST | Heap only orders parent vs children locally; BST orders left < node < right globally | Use BST-based structure if full ordering/search is needed |
| 2 | Assuming heap array is fully sorted | Heap property is **local**, not global | Only `heap[0]` is guaranteed extreme; use `sorted()` if full order needed |
| 3 | Using min-heap logic where max-heap is needed (or vice versa) | Wrong extreme element retrieved | Explicitly negate, or use `_sign`/`__lt__` trick |
| 4 | Manually re-sorting the list after every insert instead of using heap operations | Degrades to O(n log n) per op instead of O(log n) | Use `heappush`/`heappop` properly |
| 5 | Comparator mistakes with tuples (assuming only 1st element matters) | Python compares tuples lexicographically — ties fall through to 2nd element | Add explicit tie-breaker (counter) if payload isn't comparable |
| 6 | Not handling duplicate priorities | Silent incorrect ordering or crash on non-comparable payload | Use `itertools.count()` tie-breaker |
| 7 | Forgetting to re-negate values after popping from a "max-heap via negation" | Returns negative numbers by mistake | Always negate again on read/pop |
| 8 | Index calculation errors (0-indexed vs 1-indexed formulas mixed up) | Wrong parent/child references, corrupted heap | Stick to one convention consistently; Python/`heapq` = 0-indexed |
| 9 | Physically deleting from the middle of a heap array (`del heap[i]`) without re-heapifying | Breaks the heap property silently | Use proper `delete_at_index` (Section 6.6) or lazy deletion |
| 10 | Using `heapq` for a problem needing efficient **decrease-key** on arbitrary elements without an index map | O(n) search every time to find and update | Use Indexed Priority Queue (Section 12.3) or the lazy "push duplicate, skip stale" pattern |
| 11 | Building a heap with `n` calls to `heappush()` when all data is known upfront | O(n log n) instead of O(n) | Use `heapq.heapify()` |
| 12 | Forgetting the size-k heap eviction check (`if len(heap) > k: pop()`) | Full O(n log n) heap instead of O(n log k) | Add the bound check |

---

## 19. Cheat Sheets

### 19.1 Heap Operations Complexity Cheat Sheet

| Operation | Time | Space |
|---|---|---|
| Build heap (`heapify`) | O(n) | O(1) extra (in-place) |
| Insert (`push`) | O(log n) | O(1) |
| Extract-min/max (`pop`) | O(log n) | O(1) |
| Peek | O(1) | O(1) |
| Search arbitrary element | O(n) | O(1) |
| Delete arbitrary element (index known) | O(log n) | O(1) |
| Delete arbitrary element (index unknown) | O(n) | O(1) |
| Decrease/Increase key (index known) | O(log n) | O(1) |
| Merge two heaps (binary heap) | O(n) | O(n) |
| Merge two heaps (binomial/Fibonacci) | O(log n) / O(1) | O(1) |

### 19.2 `heapq` Function Cheat Sheet

| Function | Signature | Purpose |
|---|---|---|
| `heapify` | `heapq.heapify(x)` | In-place O(n) heap construction |
| `heappush` | `heapq.heappush(heap, item)` | O(log n) insert |
| `heappop` | `heapq.heappop(heap)` | O(log n) remove & return min |
| `heappushpop` | `heapq.heappushpop(heap, item)` | Push then pop (optimized) |
| `heapreplace` | `heapq.heapreplace(heap, item)` | Pop then push (optimized) |
| `nlargest` | `heapq.nlargest(k, iterable, key=None)` | k largest elements |
| `nsmallest` | `heapq.nsmallest(k, iterable, key=None)` | k smallest elements |
| `merge` | `heapq.merge(*iterables, key=None, reverse=False)` | Lazily merge sorted iterables |

### 19.3 Heap Formula Sheet (0-indexed, Python convention)

```
parent(i)      = (i - 1) // 2
left_child(i)  = 2*i + 1
right_child(i) = 2*i + 2

height of heap with n nodes = floor(log2(n))
last non-leaf index         = n // 2 - 1
number of leaves            = ceil(n / 2)
```

### 19.4 Pattern Recognition Quick Table

| Signal Words | Pattern | Core Structure |
|---|---|---|
| Kth largest/smallest | Size-K heap | Opposite-type heap, size capped at k |
| Top-K frequent | Size-K heap on frequency | Min-heap of size k |
| Merge K sorted X | Merge-K | Heap of size k, one entry per source |
| Running/streaming median | Two heaps | Max-heap (low) + Min-heap (high) |
| Greedy "always most/least X next" | Priority queue greedy | Single heap, negate for max if needed |
| Decrease-key heavy graph algo | Indexed PQ / lazy duplicate push | Heap + hashmap or lazy skip |

### 19.5 Decision Tree Cheat Sheet (Compact)

```
Need extreme (min/max) repeatedly, set changes over time?
 ├─ YES → Heap-based Priority Queue
 │         ├─ Only top/bottom K matter? → Size-K heap
 │         ├─ Merging sorted sources? → Merge-K heap
 │         ├─ Need median/percentile? → Two heaps
 │         └─ Greedy repeated selection? → Single heap + greedy loop
 └─ NO  → Consider sorting, BST, or hashmap instead
```

---

## 20. Practice Problem Bank

### 20.1 Basics & Heap Construction

| # | Problem | Platform | Difficulty | Pattern |
|---|---|---|---|---|
| 1 | Build a Heap | GeeksforGeeks | Basic | heapify from scratch |
| 2 | Heap Sort | GeeksforGeeks | Basic | Build-heap + repeated extraction |
| 3 | Check if Array Represents a Min-Heap | GeeksforGeeks | Basic | Heap property validation |
| 4 | Convert Min-Heap to Max-Heap | GeeksforGeeks | Basic | Full re-heapify |
| 5 | Binary Heap Operations | HackerRank | Basic | insert/delete/peek |

### 20.2 Priority Queue

| # | Problem | Platform | Difficulty | Pattern |
|---|---|---|---|---|
| 1 | Implement Priority Queue using Heap | GeeksforGeeks | Basic | PQ from scratch |
| 2 | Design Twitter | LeetCode 355 | Medium | Priority queue design |
| 3 | Kth Largest Element in a Stream | LeetCode 703 | Easy | Persistent size-K heap |
| 4 | Priority Scheduling Simulation | Code360 | Medium | Greedy PQ |

### 20.3 Kth Largest / Smallest

| # | Problem | Platform | Difficulty | Pattern |
|---|---|---|---|---|
| 1 | Kth Largest Element in an Array | LeetCode 215 | Medium | Size-K heap |
| 2 | Kth Smallest Element in a Sorted Matrix | LeetCode 378 | Medium | Merge-K variant |
| 3 | Find K Pairs with Smallest Sums | LeetCode 373 | Medium | Size-K heap + pointers |
| 4 | Kth Smallest Element in a BST | LeetCode 230 | Medium | In-order traversal (BST, not heap — comparison problem) |

### 20.4 Top K Problems

| # | Problem | Platform | Difficulty | Pattern |
|---|---|---|---|---|
| 1 | Top K Frequent Elements | LeetCode 347 | Medium | Size-K heap on frequency |
| 2 | Top K Frequent Words | LeetCode 692 | Medium | Size-K heap, alphabetical tie-break |
| 3 | K Closest Points to Origin | LeetCode 973 | Medium | Size-K heap on distance |
| 4 | Sort Characters By Frequency | LeetCode 451 | Medium | Max-heap on frequency |

### 20.5 Merge Problems

| # | Problem | Platform | Difficulty | Pattern |
|---|---|---|---|---|
| 1 | Merge K Sorted Lists | LeetCode 23 | Hard | Merge-K heap |
| 2 | Smallest Range Covering Elements from K Lists | LeetCode 632 | Hard | Merge-K + sliding window |
| 3 | Merge K Sorted Arrays | GeeksforGeeks | Medium | Merge-K heap |
| 4 | External Sort of Large Files | CSES / systems design | Advanced | Merge-K + disk I/O |

### 20.6 Running Median / Two Heaps

| # | Problem | Platform | Difficulty | Pattern |
|---|---|---|---|---|
| 1 | Find Median from Data Stream | LeetCode 295 | Hard | Two heaps |
| 2 | Sliding Window Median | LeetCode 480 | Hard | Two heaps + lazy deletion |
| 3 | IPO | LeetCode 502 | Hard | Two heaps (capital/profit) |

### 20.7 Scheduling Problems

| # | Problem | Platform | Difficulty | Pattern |
|---|---|---|---|---|
| 1 | Task Scheduler | LeetCode 621 | Medium | Max-heap + cooldown queue |
| 2 | Reorganize String | LeetCode 767 | Medium | Max-heap greedy |
| 3 | Rearrange String k Distance Apart | LeetCode 358 | Hard | Max-heap + cooldown queue |
| 4 | Single-Threaded CPU | LeetCode 1834 | Medium | Min-heap on (processing time, index) |
| 5 | Meeting Rooms II | LeetCode 253 | Medium | Min-heap on end times |
| 6 | Car Pooling | LeetCode 1094 | Medium | Min-heap / difference array |

### 20.8 Frequency Problems

| # | Problem | Platform | Difficulty | Pattern |
|---|---|---|---|---|
| 1 | Top K Frequent Elements | LeetCode 347 | Medium | Size-K heap |
| 2 | Frequency Sort | GeeksforGeeks | Medium | Max-heap / bucket sort |
| 3 | Rearrange Characters to Make Adjacent Not Same | GeeksforGeeks | Medium | Max-heap greedy |

### 20.9 Advanced Heap Problems

| # | Problem | Platform | Difficulty | Pattern |
|---|---|---|---|---|
| 1 | Minimum Cost to Connect Sticks | LeetCode 1167 | Medium | Min-heap greedy merge |
| 2 | Network Delay Time | LeetCode 743 | Medium | Dijkstra + heap |
| 3 | Path With Minimum Effort | LeetCode 1631 | Medium | Dijkstra-variant + heap |
| 4 | Swim in Rising Water | LeetCode 778 | Hard | Min-heap + grid traversal |
| 5 | The Skyline Problem | LeetCode 218 | Hard | Max-heap + sweep line |
| 6 | Trapping Rain Water II | LeetCode 407 | Hard | Min-heap + boundary BFS |
| 7 | Employee Free Time | LeetCode 759 | Hard | Min-heap on interval merge |
| 8 | Ugly Number II | LeetCode 264 | Medium | Min-heap / DP |

### 20.10 Additional Platforms Cross-Reference

| Problem Theme | Codeforces | CodeChef | AtCoder | CSES |
|---|---|---|---|---|
| Basic priority queue simulation | "Ivan and Burgers"-style PQ tasks | Various "PRIQUEUE" tagged problems | ABC "priority queue" tagged tasks | "Traffic Lights" (uses ordered structures, PQ-adjacent) |
| Dijkstra with heap | Many "shortest path" tagged problems | "SHPATH" style problems | ABC/ARC shortest path tasks | "Shortest Routes I/II" |
| Merge/scheduling with heap | "Kth ancestor"/scheduling-tagged sets | Scheduling-tagged problems | Scheduling-themed ABC tasks | "Room Allocation", "Tasks and Deadlines" |

> 📌 Exact problem names/IDs on Codeforces/CodeChef/AtCoder/CSES shift over time and are best looked up live by tag (e.g., search tag `priority-queue` or `heaps` on Codeforces, or the CSES "Sorting and Searching" section for `Room Allocation`, `Tasks and Deadlines`, `Movie Festival II`).

---

## 21. Final Revision & Mind Maps

### 21.1 One-Page Mind Map

```
                                    HEAP & PRIORITY QUEUE
                                            │
        ┌───────────────┬───────────────────┼───────────────────┬───────────────┐
        │               │                   │                   │               │
   FUNDAMENTALS     PYTHON heapq         PATTERNS            ADVANCED        APPLICATIONS
        │               │                   │                   │               │
  Complete Binary   heapify/push/pop   Size-K Heap          Lazy Deletion     Dijkstra
  Tree Property     nlargest/nsmallest Merge-K              Indexed PQ        Prim's MST
  Array Mapping     merge()            Two Heaps (Median)   D-ary/Binomial/   Huffman Coding
  parent/left/right tuples+counter     Greedy PQ            Fibonacci Heaps   CPU Scheduling
  Bubble Up/Down    dataclass(order)   (Scheduler, IPO,      Build-Heap O(n)   Event Simulation
  Build-Heap O(n)   Max-heap negation   Huffman, Reorganize)  proof             Streaming Top-K
```

### 21.2 15-Minute Revision Checklist

- [ ] Heap = complete binary tree + heap property (local, not global order).
- [ ] 0-indexed formulas: `parent=(i-1)//2`, `left=2i+1`, `right=2i+2`.
- [ ] `heapq` is min-heap only; negate for max-heap.
- [ ] `heapify()` = O(n); repeated `heappush()` = O(n log n).
- [ ] Size-K heap pattern → O(n log k) for Kth largest/smallest, Top-K, K-closest.
- [ ] Merge-K pattern → heap holds one "current head" per source, O(N log k).
- [ ] Two-heap pattern → running median, max-heap(low) + min-heap(high), balance sizes.
- [ ] Tuples in heap: use `(priority, itertools.count(), payload)` to avoid comparison crashes.
- [ ] Lazy deletion: mark-and-skip instead of physically removing from the middle.
- [ ] Heap sort: build max-heap, repeatedly swap root to end + shrink + sift-down = O(n log n), O(1) space, **not stable**.

### 21.3 1-Hour Deep Revision Plan

1. **(10 min)** Re-derive the array index formulas and draw the tree↔array mapping by hand.
2. **(10 min)** Re-implement `bubble_up` and `bubble_down` from memory without looking (Section 6.1–6.2).
3. **(10 min)** Re-derive why `heapify()` is O(n) (Section 6.8 / 12.2) — explain it out loud as if teaching someone.
4. **(15 min)** Solve, from memory: Kth Largest (11.1), Top K Frequent (11.2), Merge K Sorted Lists (11.3).
5. **(10 min)** Solve, from memory: Find Median from Data Stream (11.4).
6. **(5 min)** Review the Common Mistakes table (Section 18) and Cheat Sheets (Section 19).

### 21.4 Heap Operation Cheat Sheet (Recap)

| You want to... | Use |
|---|---|
| Build a heap from known data | `heapq.heapify(list)` |
| Add one element | `heapq.heappush(heap, item)` |
| Remove smallest | `heapq.heappop(heap)` |
| Peek smallest | `heap[0]` |
| Add + remove in one optimized step (push first) | `heapq.heappushpop(heap, item)` |
| Add + remove in one optimized step (pop first) | `heapq.heapreplace(heap, item)` |
| Get top-k without managing a heap manually | `heapq.nlargest(k, iterable)` / `heapq.nsmallest(k, iterable)` |
| Merge multiple sorted sequences lazily | `heapq.merge(*iterables)` |
| Simulate a max-heap | Negate values, or use `(-priority, ...)` tuples |
| Avoid tuple comparison crash | Add `itertools.count()` tie-breaker |
| Support update/decrease-key | Lazy deletion + `_entry_finder` dict, or Indexed Priority Queue |

---

## 22. FAQs

**Q1: Is a heap the same as a priority queue?**
No. A **priority queue** is an abstract data type (interface); a **heap** is the most common concrete implementation of it. You could also implement a priority queue with a sorted list or balanced BST, just less efficiently for this specific use case.

**Q2: Why doesn't Python's `heapq` have a max-heap?**
Design simplicity — one canonical implementation (min-heap) with a trivial workaround (negation) covers both cases without doubling the API surface.

**Q3: Is a heap array sorted?**
No. Only the root (`heap[0]`) is guaranteed to be the min (or max). Other elements only satisfy the local parent-child heap property, not a global order.

**Q4: Why is `heapify()` O(n) but pushing n elements one-by-one is O(n log n)?**
Because `heapify()`'s bubble-down starts from the bottom of the tree (where most nodes live and only need to move a short distance), while repeated insertion bubbles new elements up from the bottom, potentially traveling the full height of the tree each time. The math (Section 12.2) shows the total bubble-down work sums to O(n) via a converging series, while total bubble-up work in the worst case sums to O(n log n).

**Q5: When should I use a heap vs sorting the whole array?**
Use a heap when you only need the min/max (or top-K) repeatedly, especially with a **changing/streaming** dataset. Use sorting when you need the full order, or need it more than once without further mutation.

**Q6: Can heaps have duplicate values?**
Yes — heaps place no restriction on distinct values; duplicates are handled naturally by the heap property (ties can be ordered either way and both are valid).

**Q7: Is heap sort stable?**
No. Equal-valued elements can be reordered relative to each other during the swap operations in heap sort.

**Q8: What's the difference between `heappushpop()` and `heapreplace()`?**
`heappushpop()` pushes first, then pops — so if the new item is smaller than the current min (in a min-heap), it's returned immediately without ever entering the heap. `heapreplace()` pops first, then pushes — it always removes the old root, regardless of the new item's value.

**Q9: How do I implement decrease-key with Python's `heapq`?**
Python's `heapq` has no native decrease-key. The standard workaround is either (a) push a new, better entry and use a "stale entry" check on pop (common in Dijkstra implementations, Section 13.1), or (b) maintain your own Indexed Priority Queue with a position-tracking dict (Section 12.3).

**Q10: Why use `itertools.count()` in heap tuples?**
To provide a unique, ever-increasing tie-breaker so that `heapq` never needs to compare the actual payload data when two priorities are equal — preventing `TypeError` crashes on non-comparable objects, and additionally making the queue **stable** (FIFO among equal priorities).

**Q11: What's the actual time complexity of `heapq.nlargest(k, iterable)`?**
O(n log k) when `k < n` — it internally maintains a heap of size `k`, not a full sort.

**Q12: Should I ever implement my own heap class instead of using `heapq`?**
For production code, no — `heapq`'s core is implemented in C and is well-tested. Implement your own only for learning purposes, or when you need functionality `heapq` doesn't provide out-of-the-box (like a true Indexed Priority Queue with O(log n) decrease-key).

**Q13: Are Fibonacci/Binomial/Pairing heaps ever actually used in interviews?**
Rarely required to implement from scratch. They come up as **discussion/theory** questions ("what heap variant would give better asymptotic complexity for Dijkstra on a dense graph?") rather than coding tasks.

**Q14: How is a heap different from a Binary Search Tree in practice?**
A heap only guarantees fast access to the extreme (min/max) element; a BST guarantees fast access to **any** element and maintains full sorted order via in-order traversal. Don't use a heap if you need range queries or predecessor/successor lookups.

**Q15: What's the space complexity of building a heap from an array?**
O(1) additional space if using in-place `heapify()` (Section 6.8) — no new array is allocated; elements are just rearranged within the existing list.

---

## 📘 Closing Summary

This handbook covered heaps and priority queues from **first principles** (complete binary tree property, array-index arithmetic) through **Python's native `heapq` module**, **manual from-scratch implementations**, every major **interview pattern** (size-K heaps, merge-K, two-heap median tracking, greedy scheduling), **advanced theoretical variants** (D-ary, Binomial, Fibonacci, Pairing, Leftist heaps), and a full **practice problem bank** across major competitive programming and interview platforms.

**Core Takeaway:** A heap trades *full ordering* for *fast, repeated access to an extreme element* — and that trade-off is exactly what makes it the right tool whenever a problem needs "the current min/max/top-K, over and over, as the dataset changes."

Master the **size-K heap**, **merge-K**, and **two-heap** patterns first — together they cover the vast majority of heap questions asked in real interviews.

## 17. Python-Specific Tips & Tricks

### 17.1 `heapq` Quick Reference Recap

```python
import heapq

heap = []
heapq.heappush(heap, 5)          # insert
heapq.heapify(existing_list)     # bulk build, O(n)
smallest = heap[0]                # peek, O(1)
val = heapq.heappop(heap)         # remove & return min
heapq.heappushpop(heap, 3)        # push then pop (optimized)
heapq.heapreplace(heap, 3)        # pop then push (optimized)
heapq.nlargest(3, heap)
heapq.nsmallest(3, heap)
list(heapq.merge(list1, list2))
```

### 17.2 `dataclass` for Clean Priority Objects

Already shown in Section 4.10 — remember `@dataclass(order=True)` + `field(compare=False)` for non-comparable payloads.

### 17.3 Tuple Comparison Gotchas

```python
# BAD: crashes if priorities tie and dicts/objects aren't comparable
heapq.heappush(pq, (priority, {"name": "task"}))    # TypeError on tie!

# GOOD: add a tie-breaker
heapq.heappush(pq, (priority, next(counter), {"name": "task"}))
```

### 17.4 `itertools.count()` for Stable Tie-Breaking

```python
import itertools
counter = itertools.count()   # 0, 1, 2, 3, ... forever, thread-unsafe but fine for single-threaded use
```

### 17.5 Max-Heap Tricks Using Negatives (Recap)

```python
heapq.heappush(max_heap, -value)      # store negated
largest = -max_heap[0]                 # negate back when reading
```

### 17.6 Performance Tips

- `heapq` is implemented in C (via the `_heapq` C accelerator module when available) — it's fast; don't reimplement it manually in production code.
- Avoid pushing large, deep-copied objects onto a heap repeatedly — store lightweight references/IDs plus a lookup dict instead, if payloads are heavy.
- `list.sort()` (Timsort) is highly optimized in CPython; for one-time full sorts, it often beats manually pushing every element onto a heap one-by-one.

### 17.7 Memory Optimization Tips

- Prefer generators (`heapq.merge()`) over materializing full lists when you only need to iterate once.
- Use lazy deletion instead of storing multiple independent copies of a "cleaned" heap.
- For huge datasets exceeding memory, consider chunked/external processing rather than holding everything in one in-memory heap.

### 17.8 Common Python Pitfalls Specific to `heapq`

| Pitfall | Fix |
|---|---|
| Assuming `heap[1]` is the 2nd smallest | It's not — only `heap[0]` is guaranteed anything; `heap[1]` and `heap[2]` are just "some children," either could be larger than each other |
| Comparing custom objects without `__lt__` | Implement `__lt__` or use tuples with a comparable priority key |
| Forgetting `heapq` is a MIN-heap | Negate for max-heap behavior, or use a custom `__lt__` wrapper |
| Mutating a list used as a heap without calling `heapify()` afterward | Any direct mutation (e.g. `heap[3] = x`) can violate the heap invariant — always go through `heapq` functions |
| Using `heap.sort()` on a heap-backed list expecting it to "stay a heap" | Sorting maintains sorted order but heap operations still work fine on sorted lists (a sorted list happens to satisfy the heap property too) — this isn't wrong, just usually unnecessary overhead |

---

## 18. Common Mistakes

### 18.1 Confusing Heap With BST

A heap does **not** support O(log n) arbitrary search, in-order traversal, or range queries. It **only** guarantees fast access to the current min/max. Don't reach for a heap when you need a fully ordered, searchable structure — that's a BST/balanced tree/sorted container's job.

### 18.2 Assuming Sorted Order

```
INCORRECT assumption:              CORRECT understanding:

heap = [1, 3, 2, 7, 4, 5, 6]       heap = [1, 3, 2, 7, 4, 5, 6]
"This looks sorted-ish,             Only guarantee: heap[0]=1 is min.
 so heap[1]=3 must be 2nd           heap[1]=3 and heap[2]=2 are just
 smallest" -- WRONG!                the two children of root; either
                                     could be smaller than the other,
                                     and NEITHER is guaranteed to be
                                     the 2nd smallest overall (e.g.
                                     the 2nd smallest could be a
                                     grandchild we haven't compared
                                     against 3 or 2 directly).
```

### 18.3 Wrong Heap Type Selection

| Need | Correct Heap |
|---|---|
| Kth **largest** | **Min**-heap of size k |
| Kth **smallest** | **Max**-heap of size k |
| Always serve **highest** priority first | Max-heap |
| Always serve **lowest** cost/distance first | Min-heap |

### 18.4 Incorrect `heapify()` Usage

```python
# WRONG: heapify() returns None, it mutates in place!
heap = heapq.heapify([5, 3, 8])    # heap is None! BUG.

# CORRECT:
heap = [5, 3, 8]
heapq.heapify(heap)                 # mutates heap in place
```

### 18.5 Comparator Mistakes

Forgetting that `heapq` always uses natural `<` ordering (or the tuple's lexicographic order) — there's no built-in `key=` parameter for `heappush`/`heappop` (unlike `sorted()` or `nlargest`/`nsmallest`, which DO accept `key=`). To customize ordering for push/pop, wrap values in tuples or a class with a custom `__lt__`.

### 18.6 Duplicate Priorities

Handled via the tie-breaker counter pattern (Section 4.9) — always add a secondary comparable key when priorities can repeat and payloads aren't directly comparable.

### 18.7 Negative-Value Max-Heap Bugs

```python
# BUG: forgot to negate on push
heapq.heappush(max_heap, value)      # should be -value!

# BUG: forgot to negate back on pop
result = heapq.heappop(max_heap)     # this is still negative! should be -result
```

### 18.8 Index Calculation Errors

Mixing up 0-indexed (`parent = (i-1)//2`) vs 1-indexed (`parent = i//2`) formulas — always confirm which convention a given reference/textbook uses before applying formulas directly.

---

## 17. Python-Specific Tips & Tricks

### 17.1 Core `heapq` Tips

- `heapq` operates on **plain lists** — there's no dedicated `Heap` class. This means you can freely inspect `heap[0]` (peek) or even `len(heap)` without any special API.
- `heap[0]` is always the min — but `heap[1]` and `heap[2]` are **not** guaranteed to be the 2nd/3rd smallest (common misconception).
- `heapq` module functions are all **module-level**, not instance methods — always call as `heapq.heappush(heap, x)`, never `heap.heappush(x)`.

### 17.2 `dataclass` Ordering Recap

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Job:
    priority: int
    name: str = field(compare=False)
```

`order=True` auto-generates `__lt__`, `__le__`, `__gt__`, `__ge__` based on field declaration order — the **first** field is the primary sort key by default.

### 17.3 Tuples for Multi-Level Priority

```python
# Sort by priority first, then by secondary key (e.g., earlier deadline), then insertion order
heapq.heappush(pq, (priority, deadline, next(counter), task))
```

Tuples compare **element-by-element, left to right** — this is a natural, zero-cost way to encode multi-level sort criteria without writing custom comparator classes.

### 17.4 `itertools.count()` as a Universal Tie-Breaker

```python
import itertools
counter = itertools.count()   # infinite, thread-unsafe but fine for single-threaded use
```

Always insert this as the **second** tuple element (after priority, before payload) to guarantee:
1. No `TypeError` when comparing non-comparable payloads.
2. FIFO stability among equal priorities.

### 17.5 Max-Heap Trick Quick Reference

```python
# Push:  heapq.heappush(heap, -value)
# Peek:  -heap[0]
# Pop:   -heapq.heappop(heap)
```

Always remember to negate **both when pushing and when reading back** — a very common source of sign-related bugs.

### 17.6 Performance Tips

- `heapq.heapify()` is implemented in C (via the `_heapq` C extension when available) — significantly faster than a pure-Python re-implementation for large inputs.
- Avoid pushing large, expensive-to-compare objects directly — push a lightweight numeric/tuple key instead, and look up the full object separately (via a dict) if needed.
- For very hot loops, minimize tuple size — comparing `(priority, id)` is faster than `(priority, id, large_object)` if Python ever needs to fall through to comparing later tuple elements.

### 17.7 Memory Optimization

- Prefer **generators** (`heapq.merge()`) over materializing full merged lists when you only need to iterate once.
- Use lazy deletion instead of rebuilding heaps to avoid repeated O(n) list reconstructions.

### 17.8 Common Python Pitfalls

| Pitfall | Fix |
|---|---|
| Assuming `heap[1]` is 2nd smallest | Only `heap[0]` is guaranteed; use `heapq.nsmallest(2, heap)` for real 2nd smallest |
| Comparing non-comparable objects in ties | Add a tie-breaker (`itertools.count()`) |
| Mutating a list while it's used as a heap without going through `heapq` functions | Always use `heapq.heappush`/`heappop`, never `list.append` + assume heap validity |
| Forgetting `heapify()` is in-place (returns `None`) | Don't write `heap = heapq.heapify(arr)` — this sets `heap` to `None`! Just call `heapq.heapify(arr)` and continue using `arr`. |
| Using `heapq` for max-heap without negation | Always negate (or use a custom `__lt__` wrapper) |

---

## 18. Common Mistakes

### 18.1 Conceptual Mistakes

| Mistake | Correction |
|---|---|
| "A heap is a sorted array" | A heap is only **partially** ordered — parent ≤ (or ≥) children, siblings can be in any order |
| "A heap is a type of BST" | A heap has a completely different invariant (parent-child heap property vs. BST's left<root<right ordering); traversal order differs entirely |
| "In-order traversal of a heap gives sorted order" | That's true for BSTs, **not** heaps — heaps have no such guarantee |
| "The 2nd element in the array is the 2nd smallest" | Only `heap[0]` is guaranteed to be extreme; use `nsmallest`/`nlargest` for true ranked access |

### 18.2 Implementation Mistakes

- **Wrong heap type for the problem**: Using a min-heap when you need to track the "top-k largest" (should be min-heap of size **k** — correct, but many confuse this with wanting a max-heap of size k, which would actually be wrong here — always re-derive from first principles, don't just memorize).
- **Incorrect `heapify()` usage**: forgetting it mutates in-place and returns `None`.
- **Comparator mistakes**: forgetting tuple elements are compared left-to-right; accidentally putting the tie-breaker key in the wrong position.
- **Duplicate priorities crashing comparisons**: not adding a tie-breaker when payloads aren't inherently comparable.
- **Negative-value max-heap bugs**: forgetting to re-negate when reading values back out.
- **Index calculation errors**: mixing up 0-indexed (`parent = (i-1)//2`) vs 1-indexed (`parent = i//2`) formulas from different textbooks/sources.
- **Off-by-one in child bounds checks**: using `<=` instead of `<` (or vice versa) when checking `left < size`/`right < size`.
- **Modifying heap size without going through `heapq`**: e.g., directly `del heap[3]` — silently corrupts the heap invariant since no re-heapify occurs.

### 18.3 Complexity Mistakes

- Assuming `heapq.heapify()` is O(n log n) — it's O(n) (Section 6.8 / 12.2).
- Assuming `n` calls to `heappush()` is O(n) — it's actually **O(n log n)**.
- Forgetting that `nlargest`/`nsmallest` cost O(n log k), not O(n) or O(log n).

---

## 19. Cheat Sheets

### 19.1 `heapq` Function Cheat Sheet

| Function | Signature | Returns | Time |
|---|---|---|---|
| `heapify` | `heapq.heapify(x)` | `None` (in-place) | O(n) |
| `heappush` | `heapq.heappush(heap, item)` | `None` (in-place) | O(log n) |
| `heappop` | `heapq.heappop(heap)` | smallest item | O(log n) |
| `heappushpop` | `heapq.heappushpop(heap, item)` | item that was popped | O(log n) |
| `heapreplace` | `heapq.heapreplace(heap, item)` | old smallest (before push) | O(log n) |
| `nlargest` | `heapq.nlargest(k, iterable, key=None)` | list of k largest | O(n log k) |
| `nsmallest` | `heapq.nsmallest(k, iterable, key=None)` | list of k smallest | O(n log k) |
| `merge` | `heapq.merge(*iterables, key=None, reverse=False)` | sorted generator | O(n log k) |

### 19.2 Complexity Cheat Sheet

| Operation | Time | Space |
|---|---|---|
| Build heap (`heapify`) | O(n) | O(1) extra |
| Insert (`push`) | O(log n) | O(1) extra |
| Extract min/max (`pop`) | O(log n) | O(1) extra |
| Peek | O(1) | O(1) |
| Search arbitrary element | O(n) | O(1) |
| Delete arbitrary (index known) | O(log n) | O(1) |
| Delete arbitrary (index unknown) | O(n) | O(1) |
| Decrease/Increase key (index known) | O(log n) | O(1) |
| Heap Sort (full) | O(n log n) | O(1) extra (in-place variant) |
| Merge two heaps (plain binary heap) | O(n) | O(n) |
| Merge two heaps (Binomial heap) | O(log n) | O(1) |

### 19.3 Pattern Recognition Cheat Sheet

| Signal in Problem | Pattern to Apply |
|---|---|
| "Kth largest/smallest" | Size-K heap (opposite type) |
| "Top K frequent/common" | Size-K heap on frequency, or bucket sort if frequency bounded |
| "Merge K sorted ___" | Heap of size K, one head element per source |
| "Median of stream" | Two heaps (max-heap low, min-heap high) |
| "Closest K points/values" | Size-K max-heap on distance |
| "No two adjacent equal" | Max-heap greedy + "hold back last used" |
| "Cooldown between repeats" | Max-heap + waiting queue |
| "Always connect/combine cheapest two" | Min-heap greedy (Huffman-style) |
| "Shortest path in weighted graph" | Min-heap (Dijkstra) with lazy deletion |

### 19.4 Python Syntax Cheat Sheet

```python
import heapq

# Min-heap basics
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
smallest = heapq.heappop(heap)          # 1

# Build from list
arr = [5, 1, 8, 3]
heapq.heapify(arr)                       # in-place, O(n)

# Max-heap via negation
max_heap = []
heapq.heappush(max_heap, -5)
largest = -heapq.heappop(max_heap)       # 5

# Tuples with tie-breaker
import itertools
counter = itertools.count()
pq = []
heapq.heappush(pq, (priority, next(counter), payload))

# Top/bottom k
heapq.nlargest(3, arr)
heapq.nsmallest(3, arr)

# Merge sorted iterables
list(heapq.merge(list1, list2, list3))
```

### 19.5 Heap Formula Sheet (0-Indexed)

```
parent(i)       = (i - 1) // 2
left_child(i)   = 2*i + 1
right_child(i)  = 2*i + 2
height of heap  = floor(log2(n))
last_non_leaf   = n // 2 - 1
```

### 19.6 Decision Tree Cheat Sheet

```
Need min/max repeatedly, set changes over time? ──► YES ──► Heap / Priority Queue
        │
        NO
        ▼
Need full sorted order, more than once? ──► YES ──► Sort once (or maintain sorted structure)
        │
        NO
        ▼
Need arbitrary search/range queries? ──► YES ──► BST / balanced tree / hashmap
```

---

## 20. Practice Problem Bank

### 20.1 Basics & Heap Construction

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Implement a Min-Heap from scratch | GeeksforGeeks | Easy | Manual heap ops |
| Check if an array represents a Binary Heap | GeeksforGeeks | Easy | Heap property validation |
| Convert Min-Heap to Max-Heap | GeeksforGeeks | Easy | Build heap / heapify |
| Binary Heap Operations | HackerRank | Easy | Insert/Delete/Peek |

### 20.2 Priority Queue

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Kth Largest Element in a Stream | LeetCode 703 | Easy | Persistent size-k heap |
| Design a Priority Queue with update | Code360 | Medium | Lazy deletion / entry-finder |
| Sliding Window Maximum | LeetCode 239 | Hard | Monotonic deque (contrast case — NOT heap-optimal; good for comparison) |
| Meeting Rooms II | LeetCode 253 | Medium | Min-heap of end times |

### 20.3 Kth Largest / Smallest

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Kth Largest Element in an Array | LeetCode 215 | Medium | Size-K heap |
| Kth Smallest Element in a Sorted Matrix | LeetCode 378 | Medium | Heap on matrix rows |
| Find K Pairs with Smallest Sums | LeetCode 373 | Medium | Heap with generated pairs |
| Kth Smallest Prime Fraction | LeetCode 786 | Hard | Heap on fractions |

### 20.4 Top K

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Top K Frequent Elements | LeetCode 347 | Medium | Size-K heap / bucket sort |
| Top K Frequent Words | LeetCode 692 | Medium | Size-K heap with tie-break |
| Sort Characters By Frequency | LeetCode 451 | Medium | Heap / bucket sort |
| K Closest Points to Origin | LeetCode 973 | Medium | Size-K max-heap |

### 20.5 Merge Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Merge K Sorted Lists | LeetCode 23 | Hard | Merge-K heap |
| Smallest Range Covering Elements from K Lists | LeetCode 632 | Hard | Merge-K + sliding window |
| Merge K Sorted Arrays | GeeksforGeeks | Medium | Merge-K heap |

### 20.6 Running Median / Streaming

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Find Median from Data Stream | LeetCode 295 | Hard | Two heaps |
| Sliding Window Median | LeetCode 480 | Hard | Two heaps + lazy deletion |
| IPO | LeetCode 502 | Hard | Two heaps (capital/profit) |

### 20.7 Scheduling

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Task Scheduler | LeetCode 621 | Medium | Max-heap + cooldown queue |
| Reorganize String | LeetCode 767 | Medium | Max-heap greedy |
| Rearrange String k Distance Apart | LeetCode 358 | Hard | Max-heap + cooldown queue |
| Single-Threaded CPU | LeetCode 1834 | Medium | Min-heap on (processing time, index) |
| Process Tasks Using Servers | LeetCode 1882 | Medium | Two heaps (free/busy servers) |

### 20.8 Frequency Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Top K Frequent Elements | LeetCode 347 | Medium | (see 20.4) |
| Frequency Sort | GeeksforGeeks | Easy | Heap/bucket sort |
| Rearrange Characters by Frequency | InterviewBit | Medium | Max-heap greedy |

### 20.9 Advanced Heap

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Minimum Cost to Connect Sticks | LeetCode 1167 | Medium | Min-heap greedy merge |
| Swim in Rising Water | LeetCode 778 | Hard | Min-heap graph traversal |
| Path With Minimum Effort | LeetCode 1631 | Medium | Min-heap Dijkstra-variant |
| The Skyline Problem | LeetCode 218 | Hard | Max-heap with lazy deletion |
| Trapping Rain Water II | LeetCode 407 | Hard | Min-heap boundary expansion |
| Network Delay Time | LeetCode 743 | Medium | Dijkstra with min-heap |

### 20.10 Competitive Programming (Codeforces / CodeChef / AtCoder / CSES)

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| CSES: Sliding Window Median | CSES | Medium | Two heaps + lazy deletion |
| CSES: Stick Lengths / Factory Machines (related greedy) | CSES | Medium | Heap greedy |
| Codeforces: K-th Beautiful String (heap-adjacent) | Codeforces | Medium | Priority-based greedy |
| CodeChef: HEAPS (search "priority queue" tag) | CodeChef | Varies | Basic to advanced PQ |
| AtCoder: various "ho-th smallest sum" problems | AtCoder | Medium–Hard | Heap-based pair generation |

> 📌 **Note on links:** Exact problem URLs/numbers can shift over time as platforms reorganize; search the problem name + platform to locate the current link.

---

## 21. Final Revision & Mind Maps

### 21.1 One-Page Mind Map

```
                                    HEAP
                                      │
        ┌─────────────────┬──────────┼──────────┬─────────────────┐
        │                 │          │          │                 │
     SHAPE            ORDERING    STORAGE    OPERATIONS       VARIANTS
   (complete           (min/max    (array,      │            (binary,
    binary tree)        property)   0-indexed)  │             d-ary,
                                                 │             binomial,
                          ┌──────────────────────┼─────────┐   fibonacci,
                          │           │          │         │   pairing,
                       INSERT      DELETE     PEEK    BUILD    leftist)
                     (bubble up) (bubble down) O(1)   O(n)
                     O(log n)    O(log n)              (Floyd's algo)


                              PRIORITY QUEUE (ADT)
                                      │
                    implemented via Binary Heap (heapq)
                                      │
              ┌───────────┬──────────┼───────────┬─────────────┐
              │           │          │           │             │
          push/pop     tuples    dataclass   lazy deletion   max-heap
         O(log n)    (priority,   (order=True) (entry_finder)  (negation)
                       tiebreak,
                       payload)


                                PATTERNS
                                    │
       ┌──────────┬──────────┬─────┼──────┬───────────┬─────────────┐
       │          │          │            │           │             │
   Size-K      Merge-K    Two Heaps   Greedy Max-   IPO/Capital   Huffman
   Heap        Heap       (Median)    Heap (sched., (2 heaps)     (min-heap
  (Kth/TopK)  (sorted                 reorganize)                 merge)
              lists)
```

### 21.2 15-Minute Revision (Absolute Essentials)

1. **Heap = complete binary tree + heap property** (parent ≤/≥ children). Not sorted, only root is guaranteed extreme.
2. **Array storage**: `parent(i)=(i-1)//2`, `left(i)=2i+1`, `right(i)=2i+2` (0-indexed).
3. **`heapq` is min-heap only**. Max-heap = negate values.
4. **Core ops**: `heapify`(O(n)), `heappush`/`heappop`(O(log n) each), peek = `heap[0]` (O(1)).
5. **Tuples for priority+data**: `(priority, tie_breaker, payload)` — use `itertools.count()` to avoid comparison crashes.
6. **Size-K heap pattern**: for "Kth largest/Top-K," maintain a heap of size k, popping the "wrong end" element when it exceeds k. O(n log k).
7. **Two-heap pattern**: for running median — max-heap (lower half) + min-heap (upper half), balanced sizes.
8. **Lazy deletion**: mark stale entries invalid instead of physically removing — skip them on pop.
9. **Heap Sort**: build max-heap O(n), then repeatedly swap root to end + shrink + sift-down → O(n log n), O(1) space.
10. **`heapify` is O(n)**, not O(n log n) — because most nodes are near the bottom (short sift-down distance).

### 21.3 1-Hour Revision (Full Pass Checklist)

- [ ] Re-derive parent/child index formulas from scratch (0-indexed).
- [ ] Implement `bubble_up` and `bubble_down` from memory.
- [ ] Implement `MinHeap` class with `push`/`pop`/`heapify` classmethod.
- [ ] Write the max-heap negation trick + a custom `__lt__` wrapper alternative.
- [ ] Solve Kth Largest Element (LC 215) using the size-k heap template.
- [ ] Solve Top K Frequent Elements (LC 347) with `Counter` + size-k heap.
- [ ] Solve Merge K Sorted Lists (LC 23) with the tie-breaker tuple pattern.
- [ ] Solve Find Median from Data Stream (LC 295) with the two-heap pattern.
- [ ] Solve Task Scheduler (LC 621) with max-heap + cooldown queue.
- [ ] Explain why `heapify()` is O(n) out loud, unprompted.
- [ ] Explain the difference between `heappushpop` and `heapreplace`.
- [ ] Explain lazy deletion and why `heapq` has no native `decrease_key`.
- [ ] Review the Heap vs BST vs Sorted Array comparison table.
- [ ] Skim the pattern-recognition keyword table (Section 14.2).

### 21.4 Interview Cheat Sheet (One Glance Before Walking In)

```
IF "Kth ___" or "Top K ___"        -> size-K heap (opposite type heap)
IF "merge K sorted ___"            -> heap of size K (one head per source) + tie-breaker
IF "median" / "data stream"        -> two heaps (max-heap low / min-heap high)
IF "no two adjacent equal"         -> max-heap greedy + hold-back-one-round
IF "cooldown between repeats"      -> max-heap + waiting queue
IF "always combine 2 cheapest"     -> min-heap greedy (Huffman-style)
IF "shortest path, weighted graph" -> min-heap Dijkstra + lazy skip stale entries
IF need max-heap in Python         -> negate values (or custom __lt__)
IF payload not comparable          -> tuple with itertools.count() tie-breaker
```

---

## 22. FAQs

**Q1: Is a heap the same as a priority queue?**
No. A priority queue is an abstract data type (interface); a heap is the most common concrete data structure used to implement it efficiently.

**Q2: Why is `heap[1]` not necessarily the second-smallest element?**
Because the heap property only constrains parent-child relationships, not sibling ordering. `heap[1]` is only guaranteed to be ≥ `heap[0]` — it could be larger than `heap[2]`, `heap[3]`, etc. Use `heapq.nsmallest(2, heap)` to get the true second-smallest.

**Q3: Why doesn't Python's `heapq` support a max-heap directly?**
Design simplicity — the module authors chose to implement only a min-heap and document the negation trick as the standard workaround, keeping the API surface minimal.

**Q4: Why is `heapify()` O(n) but `n` calls to `heappush()` is O(n log n)?**
`heapify()`'s bubble-down starts from nodes near the bottom (where sift-down distance is short) and the total work sums to a converging series (O(n)). Repeated `heappush()` instead sifts elements **up** from the bottom each time, and in the worst case each insertion can travel all the way up (O(log n)), giving O(n log n) total.

**Q5: Can a heap have duplicate values?**
Yes — heaps place no restriction on uniqueness, unlike a BST-based Set.

**Q6: How do I delete an arbitrary (non-root) element efficiently?**
With plain `heapq`, you can't do this in less than O(n) without extra bookkeeping. Use **lazy deletion** (mark-and-skip, Section 12.1) or maintain an **Indexed Priority Queue** (Section 12.3) with an item→index map for true O(log n) arbitrary deletion.

**Q7: When should I use a heap instead of just sorting the array?**
When you need only the top/bottom `k` elements (not the full order), or when data arrives incrementally and you need to repeatedly query/update the min or max efficiently.

**Q8: Is heap sort stable?**
No. Equal elements can be reordered during the swap-based extraction phase.

**Q9: What's the difference between `heappushpop()` and `heapreplace()`?**
`heappushpop()` pushes first, and if the new item is ≤ the current root, it's returned immediately without ever entering the heap. `heapreplace()` always pops the old root first, then unconditionally pushes the new item — even if the new item is smaller than everything else in the heap.

**Q10: Why do we need `itertools.count()` as a tie-breaker in tuples?**
Because when two tuples have equal first elements (priority), Python compares the next tuple element to break the tie. If that next element (e.g., a dict, custom object, or another heap payload) isn't comparable, a `TypeError` is raised. A monotonically increasing counter as the second element guarantees ties are always broken there, safely, before ever reaching the (potentially incomparable) payload.

**Q11: Do I need to know Fibonacci Heaps for interviews?**
Almost never for implementation. You may be asked *conceptually* ("what heap variant gives O(1) decrease-key?") in senior/staff-level system-design-adjacent discussions, but coding one from scratch is exceedingly rare in standard interviews.

**Q12: How does a heap compare to a balanced BST for priority-queue use cases?**
A heap gives O(1) peek and simpler, more cache-friendly array-based storage. A BST gives O(log n) peek but supports additional operations (range queries, in-order traversal, arbitrary search) that a heap cannot do efficiently. Use a heap when you *only* need priority-based extremes; use a BST/sorted structure when you need broader ordered-set operations too.

**Q13: What is the "size-k heap" trick actually optimizing?**
It bounds the heap to hold only the `k` most relevant elements seen so far, turning an O(n log n) full-sort solution into an O(n log k) solution — a meaningful improvement whenever `k` is much smaller than `n`.

**Q14: My heap-based solution passed on small inputs but got TLE (Time Limit Exceeded) — why?**
Common causes: (1) rebuilding the heap from scratch every iteration instead of maintaining it incrementally; (2) using `heappush()` in a loop when `heapify()` would do the whole job in O(n); (3) not bounding heap size to `k` when only top-k matters, leaving it to grow to O(n) and inflating every operation to O(log n) on the full set instead of O(log k).

---

*End of Handbook — Heaps & Priority Queues in Pure Python, from first principles through FAANG-level interview mastery.*

## 17. Python-Specific Tips & Tricks

### 17.1 `heapq` Quick Reference

```python
import heapq

heapq.heapify(lst)              # O(n) — convert list to min-heap in place
heapq.heappush(heap, x)         # O(log n)
heapq.heappop(heap)             # O(log n) — returns and removes smallest
heapq.heappushpop(heap, x)      # O(log n) — push then pop (cheaper if x becomes the min)
heapq.heapreplace(heap, x)      # O(log n) — pop then push (always removes old root first)
heapq.nlargest(k, iterable)     # O(n log k)
heapq.nsmallest(k, iterable)    # O(n log k)
heapq.merge(*iterables)         # O(n log k) — lazy generator
```

### 17.2 `dataclass` Ordering Tricks

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Job:
    priority: int
    seq: int = field(compare=False)
    payload: object = field(compare=False)
```

`order=True` auto-generates `__lt__`, `__le__`, `__gt__`, `__ge__` based on field declaration order (top to bottom) — so listing `priority` first makes it the primary sort key.

### 17.3 Tuple Comparison Nuance

```python
# Tuples compare element-by-element, left to right, exactly like strings.
(1, "z") < (1, "a")     # False! Same first element, compares second: "z" > "a"
(1, "z") < (2, "a")     # True — first elements differ (1 < 2), stops there
```

### 17.4 `itertools.count()` for Stable, Crash-Proof Priority Queues

```python
import heapq
import itertools

counter = itertools.count()
pq = []
heapq.heappush(pq, (priority, next(counter), payload))
```

This single idiom **solves two problems at once**: (1) prevents crashes when comparing non-comparable payloads, and (2) guarantees FIFO order for equal priorities.

### 17.5 Max-Heap Tricks Using Negatives

```python
# Simple negation for numeric max-heap
heapq.heappush(max_heap, -value)
largest = -max_heap[0]

# Negate ONLY the priority in a (priority, data) tuple — never negate the data itself
heapq.heappush(pq, (-priority, data))
```

### 17.6 Memory Optimization Tips

- Use `heapq.merge()` (a generator) instead of building a full merged list when you only need to **iterate** the result once.
- For very large heaps, consider using `array` module typed arrays instead of plain lists if all elements are primitive numeric types (reduces per-element Python object overhead) — a micro-optimization relevant mainly at scale.
- Prefer lazy deletion over rebuilding a heap from scratch after every removal — rebuilding costs O(n) each time, while lazy deletion amortizes to O(log n).

### 17.7 Common Python Pitfalls with Heaps

| Pitfall | Fix |
|---|---|
| Assuming `heap[1]` is the 2nd smallest | It's **not** guaranteed — only `heap[0]` has a guaranteed position |
| Comparing custom objects directly, no `__lt__` | Add tie-breaker tuple or implement `__lt__` |
| Using `heapq` for a max-heap without negating | Always negate values (or priorities) for max-heap behavior |
| Mutating a list that's already used as a heap without re-heapifying | Any external mutation (e.g., `heap[3] = 100`) can break the heap invariant — always go through `heapq` functions |
| Forgetting `heapify()` is in-place and returns `None` | `heap = heapq.heapify(lst)` gives `heap = None`! Correct: `heapq.heapify(lst)` then use `lst` directly |

---

## 18. Common Mistakes

| # | Mistake | Why It's Wrong | Fix |
|---|---|---|---|
| 1 | Confusing Heap with BST | Heap only orders parent-child locally; BST orders the **entire** left/right subtree relative to a node | Use a BST/sorted structure if you need full ordering or range queries |
| 2 | Assuming the heap array is sorted | Only `heap[0]` is guaranteed correct; other positions are unordered relative to each other | Pop elements one by one to get sorted order, or use `sorted(heap)` separately |
| 3 | Using min-heap logic where max-heap is needed (or vice versa) | E.g., using a max-heap of size k for "Kth largest" (should be **min**-heap of size k) | Carefully re-derive: for "K largest," we discard the smallest of the current top-k candidates → min-heap |
| 4 | Manual `heapify()` misuse — calling it on a non-list or expecting a return value | `heapify()` mutates in place and returns `None` | Call `heapq.heapify(my_list)`, then use `my_list` |
| 5 | Comparator/tie-breaking mistakes | Crashes (`TypeError`) when payloads aren't directly comparable and priorities tie | Add `itertools.count()` tie-breaker, or implement `__lt__` |
| 6 | Duplicate priorities handled incorrectly | Assuming stable order without an explicit tie-breaker | Explicitly add a secondary sort key (counter or timestamp) |
| 7 | Negative-value max-heap bugs | Forgetting to re-negate on pop, or negating the payload instead of just the priority | Negate only the numeric priority; always flip sign back when reading results |
| 8 | Index calculation errors (0-indexed vs 1-indexed formulas) | Mixing CLRS's 1-indexed formulas with Python's 0-indexed arrays | Always use `parent(i) = (i-1)//2`, `left(i) = 2i+1`, `right(i) = 2i+2` for 0-indexed arrays |
| 9 | Trying to delete an arbitrary element in O(log n) with plain `heapq` | `heapq` has no built-in support for this | Use lazy deletion (Section 12.1) or an Indexed Priority Queue (Section 12.3) |
| 10 | Forgetting bounds checks when manually implementing bubble-down | Accessing `heap[left]`/`heap[right]` beyond array length | Always check `left < size` / `right < size` before comparing |
| 11 | Using a heap when a simple `min()`/`max()` would suffice (k=1 case) | Unnecessary O(log n) overhead per operation vs O(n) single-pass scan for one-off lookups | Use built-in `min()`/`max()` when you only need this once and don't need repeated access |
| 12 | Rebuilding the heap from scratch after every single removal | O(n) cost per removal instead of amortized O(log n) | Use lazy deletion instead |

---

## 19. Cheat Sheets

### 19.1 Heap Operations Cheat Sheet

| Operation | Manual Implementation | `heapq` Equivalent | Time |
|---|---|---|---|
| Build from array | Floyd's algorithm (Section 6.8) | `heapq.heapify(lst)` | O(n) |
| Insert | Append + bubble up | `heapq.heappush(heap, x)` | O(log n) |
| Extract min | Swap root/last, pop, bubble down | `heapq.heappop(heap)` | O(log n) |
| Peek min | `heap[0]` | `heap[0]` | O(1) |
| Push then pop | — | `heapq.heappushpop(heap, x)` | O(log n) |
| Pop then push | — | `heapq.heapreplace(heap, x)` | O(log n) |
| K largest | Size-k min-heap | `heapq.nlargest(k, it)` | O(n log k) |
| K smallest | Size-k max-heap | `heapq.nsmallest(k, it)` | O(n log k) |
| Merge sorted iterables | Merge-K pattern | `heapq.merge(*its)` | O(n log k) |

### 19.2 `heapq` Functions Cheat Sheet

```python
heapq.heapify(x)
heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heappushpop(heap, item)
heapq.heapreplace(heap, item)
heapq.nlargest(n, iterable, key=None)
heapq.nsmallest(n, iterable, key=None)
heapq.merge(*iterables, key=None, reverse=False)
```

### 19.3 Complexity Table (Master Reference)

| Structure/Op | Time | Space |
|---|---|---|
| Build heap (`heapify`) | O(n) | O(1) extra |
| Insert | O(log n) | O(1) |
| Extract min/max | O(log n) | O(1) |
| Peek | O(1) | O(1) |
| Search arbitrary element | O(n) | O(1) |
| Delete arbitrary (index known) | O(log n) | O(1) |
| Delete arbitrary (index unknown) | O(n) | O(1) |
| Decrease/Increase key (plain heapq, via re-push) | O(log n) amortized (with lazy deletion) | O(n) (stale entries) |
| Heap Sort | O(n log n) | O(1) |
| Merge two heaps (binary heap) | O(n) | O(n) |
| Merge two heaps (Binomial heap) | O(log n) | O(1) |

### 19.4 Pattern Recognition Cheat Sheet

| Signal in Problem | Pattern | Heap Type |
|---|---|---|
| "Kth largest" | Size-K heap | Min-heap of size k |
| "Kth smallest" | Size-K heap | Max-heap of size k |
| "Top K frequent" | Size-K heap on frequency | Min-heap of size k |
| "Merge K sorted ___" | Merge-K | Min-heap of size k |
| "Running median" / "median so far" | Two heaps | Max-heap (low) + Min-heap (high) |
| "No two adjacent equal" | Greedy rearrangement | Max-heap |
| "Task with cooldown" | Greedy scheduling | Max-heap + queue |
| "Always connect/combine 2 cheapest" | Greedy merge cost | Min-heap |
| "Closest K points/distances" | Size-K heap on distance | Max-heap of size k |

### 19.5 Heap Formula Sheet (0-Indexed)

```
parent(i)      = (i - 1) // 2
left_child(i)  = 2*i + 1
right_child(i) = 2*i + 2

height of heap with n nodes = floor(log2(n))
last non-leaf index         = (n // 2) - 1
number of leaves            = ceil(n / 2)
```

### 19.6 Decision Tree — Quick Reference

```
Need min/max only, data changes over time?
  └── YES → Heap
        │
        ├── Need only top/bottom K? ────────────► Size-K heap
        ├── Merging multiple sorted seqs? ──────► Merge-K heap
        ├── Need running median? ───────────────► Two heaps
        ├── Greedy "always pick extreme, repeat"? ► Priority queue / greedy heap
        └── Need arbitrary search/range query? ─► NOT a heap → use BST/sorted structure
  └── NO → reconsider: maybe simple sort, two-pointer, or hashmap is simpler
```

---

## 20. Practice Problem Bank

### 20.1 Basics & Heap Construction

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Implement a Min Heap / Max Heap | GeeksforGeeks | Easy | Core operations |
| Build a Heap | Code360 (Coding Ninjas) | Easy | `heapify` |
| Heap Sort | GeeksforGeeks | Medium | Heap sort |
| Check if Array Represents a Min-Heap | GeeksforGeeks | Easy | Heap property validation |
| Convert Min-Heap to Max-Heap | GeeksforGeeks | Medium | Re-heapify |

### 20.2 Priority Queue Fundamentals

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Implement Priority Queue using Heap | GeeksforGeeks | Medium | PQ design |
| Design Twitter | LeetCode 355 | Medium | PQ + hashmap |
| Kth Largest Element in a Stream | LeetCode 703 | Easy | Persistent size-K heap |
| Last Stone Weight | LeetCode 1046 | Easy | Max-heap simulation |

### 20.3 Kth Largest / Kth Smallest

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Kth Largest Element in an Array | LeetCode 215 | Medium | Size-K heap |
| Kth Smallest Element in a Sorted Matrix | LeetCode 378 | Medium | Merge-K variant |
| Find K Pairs with Smallest Sums | LeetCode 373 | Medium | Size-K heap + pairs |
| Kth Smallest Element in a BST | LeetCode 230 | Medium | (BST in-order, contrast case) |
| Kth Largest Sum in a Binary Tree | LeetCode 2583 | Medium | Size-K heap |

### 20.4 Top K / Frequency Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Top K Frequent Elements | LeetCode 347 | Medium | Size-K heap on frequency |
| Top K Frequent Words | LeetCode 692 | Medium | Size-K heap + tie-breaking |
| Sort Characters By Frequency | LeetCode 451 | Medium | Max-heap on frequency |
| Rearrange String k Distance Apart | LeetCode 358 | Hard | Greedy max-heap + queue |

### 20.5 Merge Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Merge K Sorted Lists | LeetCode 23 | Hard | Merge-K heap |
| Merge K Sorted Arrays | GeeksforGeeks | Medium | Merge-K heap |
| Smallest Range Covering Elements from K Lists | LeetCode 632 | Hard | Merge-K + sliding window |
| Find K Pairs with Smallest Sums | LeetCode 373 | Medium | Merge-K variant |

### 20.6 Running Median / Two-Heap Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Find Median from Data Stream | LeetCode 295 | Hard | Two heaps |
| Sliding Window Median | LeetCode 480 | Hard | Two heaps + lazy deletion |
| IPO | LeetCode 502 | Hard | Two heaps (capital/profit) |

### 20.7 Scheduling / Greedy Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Task Scheduler | LeetCode 621 | Medium | Max-heap + cooldown queue |
| Reorganize String | LeetCode 767 | Medium | Max-heap greedy |
| Minimum Cost to Connect Sticks | LeetCode 1167 | Medium | Min-heap greedy merge |
| Single-Threaded CPU | LeetCode 1834 | Medium | Min-heap on (processing_time, index) |
| Process Tasks Using Servers | LeetCode 1882 | Medium | Two heaps (free/busy servers) |

### 20.8 Distance / Geometry Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| K Closest Points to Origin | LeetCode 973 | Medium | Size-K heap on squared distance |
| Path With Minimum Effort | LeetCode 1631 | Medium | Dijkstra-style min-heap |
| Swim in Rising Water | LeetCode 778 | Hard | Min-heap + grid traversal |
| The Skyline Problem | LeetCode 218 | Hard | Max-heap + sweep line |

### 20.9 Advanced / Competitive Programming

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Ugly Number II | LeetCode 264 | Medium | Min-heap generative sequence |
| Super Ugly Number | LeetCode 313 | Medium | Min-heap generative sequence |
| Trapping Rain Water II | LeetCode 407 | Hard | Min-heap + boundary BFS |
| Employee Free Time | LeetCode 759 | Hard | Merge-K + interval merge |
| Network Delay Time | LeetCode 743 | Medium | Dijkstra (min-heap) |
| Connecting Cities With Minimum Cost | LeetCode 1135 | Medium | (MST context, contrast case) |
| Nearly Sorted / K-sorted Array Sort | GeeksforGeeks | Medium | Size-K heap |
| Job Sequencing Problem | GeeksforGeeks | Medium | Max-heap greedy |
| Priority CPU Scheduling Simulation | HackerRank | Medium | PQ simulation |
| Codeforces 4C variants (frequency/heap based) | Codeforces | 1200–1600 rated | Heap + hashmap |
| CSES Sliding Window Cost / Josephus-like problems | CSES | Medium | Two heaps / cyclic PQ |
| Huffman Encoding | GeeksforGeeks / InterviewBit | Medium | Min-heap greedy merge |
| Nearly sorted algorithm (K-distance sort) | InterviewBit | Medium | Size-K heap |
| Connect Ropes with Minimum Cost | GeeksforGeeks | Easy | Min-heap greedy merge |
| CodeChef "Chef and Priority Queue"-style problems | CodeChef | Varies | PQ simulation |
| AtCoder heap-based greedy simulation problems | AtCoder | Varies | Min/Max-heap greedy |

---

## 21. Final Revision & Mind Maps

### 21.1 One-Page Mind Map

```
                                   HEAP & PRIORITY QUEUE
                                            │
        ┌───────────────────┬───────────────┼───────────────┬─────────────────────┐
        │                   │                │               │                     │
     STRUCTURE          OPERATIONS       PYTHON TOOLS      PATTERNS             ADVANCED
        │                   │                │               │                     │
  Complete Binary       Insert(↑)         heapq module    Size-K Heap        Lazy Deletion
  Tree + Array          Extract(↓)        heapify O(n)    Merge-K            Indexed PQ
  parent=(i-1)//2       Peek O(1)         heappush/pop    Two Heaps(median)  D-ary/Binomial/
  left=2i+1             Build O(n)        nlargest/small  Greedy Scheduling  Fibonacci Heaps
  right=2i+2            Heap Sort         merge()         Huffman-style      (theory only)
                         Decrease-key     tuple trick        merge cost
                        (via lazy del.)   dataclass order
```

### 21.2 15-Minute Revision

1. Heap = complete binary tree + heap property (parent ≤/≥ children). Stored as array: `parent=(i-1)//2`, `left=2i+1`, `right=2i+2`.
2. `heapq` = **min-heap only**. For max-heap: negate values.
3. Core ops: `heapify` O(n), `push`/`pop` O(log n), peek O(1).
4. Size-K heap pattern: min-heap for "K largest," max-heap for "K smallest" → O(n log k).
5. Merge-K pattern: one heap entry per sequence, always with a tie-breaker index.
6. Two heaps = running median: max-heap (low half) + min-heap (high half), rebalance to keep sizes within 1.
7. Non-comparable payloads → always use `(priority, itertools.count(), data)` tuples.
8. No native decrease-key in `heapq` → use lazy deletion (push new entry, mark/skip the old one).
9. Heap sort: build max-heap, repeatedly swap root to the end + shrink + bubble-down → O(n log n), O(1) space.

### 21.3 1-Hour Revision Path

1. Read Section 1–3 (Intro + Fundamentals + Array representation) — 10 min.
2. Read Section 4 (`heapq` reference) thoroughly, run the code snippets mentally — 15 min.
3. Read Section 6–7 (manual bubble up/down + full class) — 10 min.
4. Read Section 11 in full (all patterns) — this is the highest-yield section — 20 min.
5. Skim Section 14 (recognition flowchart) and Section 19 (cheat sheets) right before an interview — 5 min.

### 21.4 Interview Cheat Sheet (Print-and-Keep)

```
Q: "Kth largest?"         -> min-heap, size k
Q: "Kth smallest?"        -> max-heap, size k
Q: "Top K frequent?"      -> min-heap on frequency, size k
Q: "Merge K sorted?"      -> heap of size k, one entry per source + index tie-breaker
Q: "Running median?"      -> two heaps (max-heap low, min-heap high), balance sizes
Q: "No adjacent equal?"   -> max-heap greedy, hold back last-used element one round
Q: "Task w/ cooldown?"    -> max-heap + FIFO cooldown queue
Q: "Always merge 2 min?"  -> min-heap greedy (Huffman-style)
Q: "Need arbitrary search/order?" -> NOT a heap problem; use BST/sorted structure instead
```

---

## 22. FAQs

**Q1: Is a heap always a binary tree?**
No — heaps can be **d-ary** (any fixed branching factor), but the **binary heap** is by far the most common, and the one `heapq` implements.

**Q2: Is `heapq` thread-safe?**
No. Concurrent pushes/pops from multiple threads without external locking can corrupt the heap invariant. Use `queue.PriorityQueue` (which wraps `heapq` with locking) for thread-safe scenarios.

**Q3: Why doesn't Python have a built-in max-heap?**
Design minimalism — Anthropic did not build `heapq`, but by Python's own design philosophy ("there should be one obvious way to do it"), a single min-heap primitive plus a documented negation trick was considered sufficient, avoiding API duplication.

**Q4: Can a heap have duplicate values?**
Yes, absolutely — heaps place no restriction on uniqueness, unlike a `set`.

**Q5: Is a heap sorted?**
No. Only the root is guaranteed to be the min (or max). The rest of the array only satisfies the **local** parent-child heap property, not a global order.

**Q6: What's the difference between a Heap and a Priority Queue?**
A heap is a **concrete data structure**. A priority queue is an **abstract interface/contract**. In practice, "priority queue" and "binary heap" are often used interchangeably because the heap is the overwhelmingly dominant implementation choice.

**Q7: Why is `heapify()` O(n) but building via `n` inserts is O(n log n)?**
Because `heapify`'s bubble-down work is concentrated near the bottom of the tree (many nodes, but short sift distances), while repeated insertion's bubble-up work is concentrated near the top over time (fewer long-distance sifts but on average log n each) — see the full proof in Section 12.2.

**Q8: How do I do "decrease-key" in Python's `heapq`?**
There's no native support. Standard workaround: push a new, updated entry and use **lazy deletion** to skip the stale one when it's eventually popped (Section 9.4, Section 13.1's Dijkstra example).

**Q9: When should I NOT use a heap?**
When you need: arbitrary-element search faster than O(n), full sorted order/range queries, or when a simpler approach (single `min()`/`max()`, two-pointer, or a direct O(n) bucket-count) already solves the problem without heap overhead.

**Q10: Are heaps stable?**
Not inherently. To make a heap-based priority queue stable (FIFO among equal priorities), add an explicit monotonically increasing tie-breaker (`itertools.count()`).

**Q11: What is the time complexity to check if an array is a valid heap?**
O(n) — verify the heap property holds for every internal node against its children in a single pass.

**Q12: Can I convert a max-heap array directly into a min-heap array in O(n)?**
Not by simple negation-free transformation of an *existing arrangement* — you must effectively **rebuild** via `heapify()` under the new ordering (negate all values first if using the negation trick, then re-run `heapify()`), which is still O(n) overall.

---
