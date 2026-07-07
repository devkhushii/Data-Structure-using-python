# 🔍 The Complete Python Searching Algorithms Handbook

---

## 📖 Table of Contents

1. [Introduction to Searching](#1-introduction-to-searching)
2. [Searching in Python (Built-in Tools)](#2-searching-in-python-built-in-tools)
3. [Linear Search Family](#3-linear-search-family)
4. [Binary Search — The Core Idea](#4-binary-search--the-core-idea)
5. [Binary Search Templates (Universal)](#5-binary-search-templates-universal)
6. [Binary Search Patterns](#6-binary-search-patterns)
   - [6.1 First & Last Occurrence](#61-first--last-occurrence)
   - [6.2 Lower Bound & Upper Bound](#62-lower-bound--upper-bound)
   - [6.3 Floor & Ceiling](#63-floor--ceiling)
   - [6.4 Count Occurrences](#64-count-occurrences)
   - [6.5 Search Insert Position](#65-search-insert-position)
   - [6.6 Peak Element](#66-peak-element)
   - [6.7 Search in Rotated Sorted Array](#67-search-in-rotated-sorted-array)
   - [6.8 Search in Nearly Sorted Array](#68-search-in-nearly-sorted-array)
   - [6.9 Search in a 2D Matrix](#69-search-in-a-2d-matrix)
   - [6.10 Binary Search on Answer](#610-binary-search-on-answer)
   - [6.11 Binary Search on Infinite / Unbounded Array](#611-binary-search-on-infinite--unbounded-array)
7. [Other Classical Search Algorithms](#7-other-classical-search-algorithms)
   - [7.1 Jump Search](#71-jump-search)
   - [7.2 Interpolation Search](#72-interpolation-search)
   - [7.3 Exponential Search](#73-exponential-search)
   - [7.4 Fibonacci Search](#74-fibonacci-search)
   - [7.5 Ternary Search](#75-ternary-search)
8. [Searching Patterns & Problem-Solving Frameworks](#8-searching-patterns--problem-solving-frameworks)
9. [Applications of Searching](#9-applications-of-searching)
10. [Problem Recognition Guide](#10-problem-recognition-guide)
11. [Optimization: Brute Force → Better → Optimal](#11-optimization-brute-force--better--optimal)
12. [Common Mistakes & Pitfalls](#12-common-mistakes--pitfalls)
13. [Interview Preparation Guide](#13-interview-preparation-guide)
14. [Cheat Sheets](#14-cheat-sheets)
15. [Practice Problem Bank](#15-practice-problem-bank)
16. [Final Revision & Mind Maps](#16-final-revision--mind-maps)
17. [FAQs](#17-faqs)

---

## 1. Introduction to Searching

### 1.1 What is Searching?

**Searching** is the process of locating a specific element (the *target* or *key*) within a collection of data (the *search space*), and reporting either:
- its **position/index**, or
- a **boolean** (found / not found), or
- some **derived value** (count, nearest value, boundary, etc.)

> **Definition (formal):** Given a search space `S` and a predicate `P(x)` (usually "does x equal the target" or "does x satisfy a condition"), searching finds an `x ∈ S` such that `P(x)` is true, using the fewest possible comparisons/operations.

### 1.2 Why Searching Exists

Every non-trivial program needs to answer questions like:
- "Does this value exist?"
- "Where is this value?"
- "What is the smallest/largest value satisfying X?"

Without efficient searching, every lookup would require scanning the entire dataset — infeasible for databases with billions of rows, search engines with trillions of documents, or real-time systems.

### 1.3 A Short History

| Era | Development |
|---|---|
| Pre-1940s | Manual/linear lookups in ledgers, libraries (Dewey Decimal) |
| 1946 | John Mauchly discusses binary search-like merging techniques |
| 1962 | First **bug-free published binary search** by Hermann Bottenbruch (many earlier versions had bugs — even Jon Bentley noted most implementations had bugs for decades!) |
| 1970s–80s | B-Trees, hashing, and interpolation search formalized for databases |
| 1990s–2000s | Search engines (Google, 1998) popularize inverted indexes at massive scale |
| 2000s–present | Approximate/vector search (ANN, HNSW) for ML embeddings, LSM trees for modern databases |

> **Fun fact / Interview trivia:** Jon Bentley's famous study found that the majority of professional programmers, when asked to implement binary search, wrote a version with a bug — often related to `mid` calculation or boundary conditions. Even the standard Java library had an integer-overflow bug in `Arrays.binarySearch` for **9 years** before it was fixed in 2006.

### 1.4 Characteristics of a Search Problem

- Has a well-defined **search space** (array, matrix, range of numbers, tree, graph, or an abstract answer-space).
- Has a **target/predicate** to satisfy.
- May or may not require the search space to be **sorted/monotonic** (sorting is what unlocks Binary Search's O(log n)).
- Produces a **deterministic** result (found/not found/position).

### 1.5 Advantages of (Efficient) Searching

- Reduces time complexity drastically (O(n) → O(log n) or better).
- Enables real-time systems (autocomplete, routing, fraud detection).
- Powers indexing structures used everywhere in software engineering.

### 1.6 Disadvantages / Trade-offs

- Efficient searching (like Binary Search) often requires **pre-processing** (sorting, indexing) which costs time/space upfront.
- More complex to implement correctly than a plain scan — off-by-one bugs are notorious.
- Some efficient searches only work under specific conditions (sorted data, monotonic predicate).

### 1.7 Applications & Real-World Examples

| Domain | Example |
|---|---|
| Databases | B-Tree/B+Tree index lookups, binary search within sorted pages |
| Search Engines | Inverted index lookup, ranking, autocomplete |
| Operating Systems | Process scheduling, page table lookups |
| Version Control | `git bisect` — binary search over commits to find a bug |
| Networking | Routing table lookups (longest prefix match) |
| Computational Geometry | Binary search on answer for optimization problems |
| Everyday life | Looking up a word in a dictionary, finding a name in a phone book, guessing a number in "20 questions" |

### 1.8 Search Space — The Central Idea

```
SEARCH SPACE (before searching)
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 2 │ 5 │ 8 │12 │16 │23 │38 │56 │72 │   target = 23
└───┴───┴───┴───┴───┴───┴───┴───┴───┘
  0   1   2   3   4   5   6   7   8    <- indices

Linear Search  : scans left→right, one element at a time.
Binary Search  : repeatedly halves the search space (requires sorted/monotonic space).
```

The **search space** is not always an array of numbers — it can be:
- A **range of possible answers** (e.g., "minimum time to ship packages") → *Binary Search on Answer*
- A **2D grid** → *Matrix Search*
- An **infinite stream** → *Exponential Search*
- A **rotated sorted array** → modified Binary Search

### 1.9 Search Strategy Taxonomy

```
                         SEARCHING
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                      │
 UNINFORMED               INFORMED               HASH-BASED
 (no structure          (uses sorted/            (O(1) avg via
  assumption)             monotonic property)      hash function)
       │                     │                      │
 Linear Search         Binary Search           dict / set lookup
 Sentinel Search        Jump Search             Hash Tables
                        Interpolation Search
                        Exponential Search
                        Fibonacci Search
                        Ternary Search (unimodal)
```

> 💡 **Note:** This handbook focuses on *comparison-based* and *arithmetic-based* searching (Linear/Binary family). Hash-based O(1) lookup is mentioned only for contrast — it is a Hashing topic, not a Searching-algorithm topic.

---
## 2. Searching in Python (Built-in Tools)

Python gives you several ways to search **before** you ever write your own algorithm. Knowing when to use each is an interview signal of maturity.

### 2.1 The `in` operator

```python
arr = [4, 2, 9, 7, 5]
print(9 in arr)      # True  -> O(n) linear scan for list
print(9 in set(arr)) # True  -> O(1) average, uses hashing
```

- **Definition:** `in` invokes `__contains__`. For `list`/`tuple`, it's a **linear scan** — O(n). For `set`/`dict`, it's **hash-based** — O(1) average.
- **Why it exists:** Pythonic, readable membership testing.
- **Common mistake:** Assuming `in` on a `list` is O(1) just because it "feels instant" for small inputs — it is **not**. For repeated membership checks, convert to a `set` first.

### 2.2 `list.index(x)`

```python
arr = [10, 20, 30, 40]
pos = arr.index(30)      # 2
# arr.index(99)          # raises ValueError!
```

- Returns the **first** index of `x`; raises `ValueError` if not found.
- O(n) — internally a linear search written in C (fast constant factor, but still linear).
- **Edge case:** always guard with `if x in arr` or `try/except ValueError`.

### 2.3 `str.find()` vs `str.index()`

```python
s = "searching algorithms"
print(s.find("algo"))     # 11 (index) — returns -1 if not found
print(s.find("xyz"))      # -1
print(s.index("algo"))    # 11 — raises ValueError if not found
```

| Method | Not Found Behaviour | Use When |
|---|---|---|
| `.find()` | returns `-1` | You want to check existence without exceptions |
| `.index()` | raises `ValueError` | You are certain the substring exists |

Internally, CPython's string search uses a hybrid of **Boyer–Moore–Horspool / Crochemore-Perrin ("Two-Way")** algorithm for substrings — sub-linear in practice, not naive O(n·m).

### 2.4 The `bisect` module — Python's Built-in Binary Search

The `bisect` module operates ONLY on data that is **already sorted**. It doesn't search for a value's index and tell you "found/not found" directly — instead, it gives you an **insertion point**, which is far more powerful.

```python
import bisect

arr = [1, 3, 3, 3, 5, 7, 9]

bisect.bisect_left(arr, 3)    # 1  -> leftmost position to insert 3 (before existing 3s)
bisect.bisect_right(arr, 3)   # 4  -> rightmost position to insert 3 (after existing 3s)
bisect.bisect(arr, 3)         # 4  -> alias for bisect_right

bisect.insort_left(arr, 4)    # inserts 4 in sorted position (mutates list)
```

**ASCII visualization of bisect_left vs bisect_right on value 3:**

```
index:   0   1   2   3   4   5   6
array:  [1,  3,  3,  3,  5,  7,  9]
                ↑
     bisect_left(arr,3) = 1   (before the block of 3s)
                            ↑
     bisect_right(arr,3) = 4  (after the block of 3s)
```

#### Using `bisect` to implement Lower/Upper Bound and Exact Search

```python
import bisect

def binary_search_bisect(arr, target):
    """Exact search using bisect_left. O(log n)."""
    i = bisect.bisect_left(arr, target)
    if i < len(arr) and arr[i] == target:
        return i
    return -1

def lower_bound(arr, target):
    """First index where arr[i] >= target."""
    return bisect.bisect_left(arr, target)

def upper_bound(arr, target):
    """First index where arr[i] > target."""
    return bisect.bisect_right(arr, target)

def count_occurrences(arr, target):
    return bisect.bisect_right(arr, target) - bisect.bisect_left(arr, target)
```

**Dry run** — `binary_search_bisect([1,3,3,3,5,7,9], 5)`:

| Step | Action | Result |
|---|---|---|
| 1 | `bisect_left(arr, 5)` internally binary searches | returns `i = 4` |
| 2 | Check `arr[4] == 5` | `True` |
| 3 | Return | `4` |

#### Performance Comparison

| Method | Time Complexity | Requires Sorted? | Returns |
|---|---|---|---|
| `x in list` | O(n) | No | bool |
| `list.index(x)` | O(n) | No | first index or error |
| `x in set` | O(1) avg | No | bool |
| `bisect_left/right` | O(log n) | **Yes** | insertion index |
| Custom binary search | O(log n) | **Yes** | index / -1 |

### 2.5 Best Practices

- ✅ If data is **sorted and static**, prefer `bisect` over writing your own binary search — it's C-optimized and battle-tested.
- ✅ If you need **existence checks repeatedly**, use a `set`/`dict`, not `in` on a list.
- ✅ If you need **custom comparison logic** (predicate-based, "search on answer"), you must write your own binary search — `bisect` only compares raw values.
- ⚠️ `bisect` assumes the list is sorted; it will **not** warn you if it isn't — you'll silently get wrong answers.
- ⚠️ `bisect.bisect_left`/`right` work on ascending order only, by default (no `key`/`reverse` before Python 3.10; Python 3.10+ added a `key` parameter).

```python
# Python 3.10+ key parameter example
import bisect
data = [{"score": 10}, {"score": 20}, {"score": 30}]
i = bisect.bisect_left(data, 20, key=lambda d: d["score"])   # 1
```

---
## 3. Linear Search Family

### 3.1 Linear Search

**Definition:** Scan every element one by one until the target is found or the space is exhausted.

**Why it exists:** It is the *only* option when data is unsorted, unindexed, or the search space has no exploitable structure (e.g., a linked list, a stream).

**Real-world analogy:** Looking for your friend's name by flipping through every page of an unsorted stack of business cards.

**ASCII Visualization:**

```
target = 23

[ 5 ][12 ][ 9 ][23 ][ 7 ]
  ↑
 check 5≠23, move →
       ↑
      check 12≠23, move →
             ↑
            check 9≠23, move →
                   ↑
                  check 23==23 ✔ FOUND at index 3
```

**Python Implementation:**

```python
def linear_search(arr, target):
    """
    Returns the index of the first occurrence of target, or -1.
    Works on ANY iterable structure — sorted or not.
    """
    for i in range(len(arr)):        # visit every index once
        if arr[i] == target:          # compare current element to target
            return i                  # found -> return immediately
    return -1                         # loop finished without match
```

**Line-by-line explanation:**
1. `for i in range(len(arr))` — iterate index 0 to n-1.
2. `if arr[i] == target` — the core comparison.
3. `return i` — early exit as soon as a match is found (this is what makes best case O(1)).
4. `return -1` — sentinel value indicating failure, by convention.

**Dry Run** — `linear_search([5,12,9,23,7], 23)`:

| Step | i | arr[i] | Match? | Action |
|---|---|---|---|---|
| 1 | 0 | 5 | No | continue |
| 2 | 1 | 12 | No | continue |
| 3 | 2 | 9 | No | continue |
| 4 | 3 | 23 | **Yes** | return 3 |

**Complexity:**

| Case | Time | Space |
|---|---|---|
| Best | O(1) | O(1) |
| Average | O(n) | O(1) |
| Worst | O(n) | O(1) |

**Edge Cases:**
- Empty array → returns -1 immediately.
- Target at last index → worst case, full scan.
- Multiple occurrences → returns the *first* one only.
- Duplicate-heavy arrays → linear search doesn't care, still O(n).

**Common Mistakes:**
- Forgetting the `-1` sentinel and returning `None` inconsistently.
- Using linear search on large **sorted** datasets when Binary Search would be far faster — a classic interview red flag.

**Interview Tip:** If interviewer explicitly says data is **unsorted** and asks for search, Linear Search is often the *expected correct* answer — don't over-engineer.

**Optimizations:**
- **Move-to-front:** if searches are repeated and skewed (some elements queried more), move found elements toward the front (like an LRU-ish heuristic) to speed up future searches.
- **Sentinel Linear Search** (below): removes the bounds-check per iteration.

---

### 3.2 Sentinel Linear Search

**Definition:** A micro-optimization that removes the `i < len(arr)` boundary check from every loop iteration by placing the target itself at the end of the array as a "sentinel," guaranteeing the loop always terminates via the value-match condition.

**Why it exists:** In lower-level languages (C/C++), removing a comparison per iteration measurably speeds up tight loops. In Python this benefit is mostly pedagogical since the interpreter overhead dominates — but it's a favorite CS-fundamentals interview question.

**ASCII Visualization:**

```
Original: [5, 12, 9, 7]        target = 9
Append sentinel: [5, 12, 9, 7, 9]
                              ↑ sentinel guarantees termination

i=0: 5≠9 -> i++
i=1: 12≠9 -> i++
i=2: 9==9 -> STOP (this could be real match or the sentinel)
Check: i < original_length (2 < 4) -> real match!
```

**Python Implementation:**

```python
def sentinel_linear_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    last = arr[n - 1]        # save the real last element
    arr[n - 1] = target      # overwrite last slot with target (sentinel)

    i = 0
    while arr[i] != target:  # no need to check i < n here!
        i += 1

    arr[n - 1] = last        # restore original array

    if i < n - 1 or arr[n - 1] == target:
        return i
    return -1
```

**Line-by-line explanation:**
1. Save `last` so we can restore the array (avoid mutating caller's data permanently).
2. Overwrite the last element with `target` — this is the sentinel guaranteeing the while loop terminates.
3. `while arr[i] != target: i += 1` — single condition, no bounds check.
4. Restore the array.
5. Distinguish "found for real" vs "only found because of the sentinel we planted."

**Dry Run** — `sentinel_linear_search([5,12,9,7], 9)`:

| Step | i | arr[i] | Note |
|---|---|---|---|
| setup | — | arr becomes [5,12,9,9] | sentinel placed at index 3 |
| 1 | 0 | 5 | ≠9, continue |
| 2 | 1 | 12 | ≠9, continue |
| 3 | 2 | 9 | ==9, stop |
| check | i=2 < n-1=3 | True | genuine match, restore & return 2 |

**Complexity:** Same asymptotic O(n) time, O(1) space — the win is a smaller constant factor (fewer comparisons per loop), essentially irrelevant in Python due to interpreter overhead, but tests conceptual understanding.

**Edge Cases:** Empty array, target equal to last real element (must disambiguate correctly — shown in the `if` check above), target not present at all.

**Common Mistakes:**
- Forgetting to restore the array (mutates caller's data — a **major bug** in production code).
- Not disambiguating between "found because of the real element" vs "found only because of the sentinel."

**Interview Tip:** Rarely coded in interviews directly, but frequently asked as a **conceptual** question: "How can you remove the bounds check from linear search?"

---
## 4. Binary Search — The Core Idea

### 4.1 Definition

**Binary Search** finds a target in a **sorted** (or more generally, **monotonic**) search space by repeatedly halving it: compare the target to the middle element, and discard the half that cannot contain the answer.

### 4.2 Why It Exists

Linear Search is O(n). If the data is sorted, we can exploit **order** to eliminate half the remaining candidates with every comparison — giving O(log n), which is exponentially faster for large n (e.g., searching 1 billion sorted elements takes ~30 comparisons instead of up to 1 billion).

### 4.3 Intuition & Real-World Analogy

**The "Guess the Number" game:** I'm thinking of a number between 1 and 100. You guess 50. I say "higher." You guess 75. I say "lower." You guess 62... In at most 7 guesses (⌈log₂100⌉), you always find it. This is Binary Search.

**Dictionary analogy:** You don't read a dictionary front-to-back to find "mango" — you open to the middle, see you're in "P," flip left, open to the middle of the remaining half, and so on.

### 4.4 Precondition: Monotonicity, not just "sorted"

The array doesn't need to be numerically sorted — it needs a **monotonic predicate**: a boolean function `P(x)` such that as `x` increases, `P(x)` goes from `False...False, True...True` (or vice-versa) with **no mixing**. This generalization is the basis of "Binary Search on Answer" (Section 6.10).

```
Sorted array:      [2, 5, 8, 12, 16, 23, 38]     -> P(x) = "x >= target"
                    F  F  F  F   F   T   T

Monotonic predicate example: "can ship all packages within D days?"
D:                  1    2    3    4    5
can_ship(D):        F    F    F    T    T
                              ^ boundary is what we binary search for
```

### 4.5 Internal Working — Step by Step

```
STEP 0:  low = 0, high = n-1
STEP 1:  mid = low + (high - low) // 2
STEP 2:  if arr[mid] == target: FOUND
STEP 3:  elif arr[mid] < target: low = mid + 1   (discard left half incl. mid)
STEP 4:  else: high = mid - 1                     (discard right half incl. mid)
STEP 5:  repeat while low <= high
STEP 6:  if loop ends without match: NOT FOUND
```

**ASCII Visualization — full trace of interval shrinking:**

```
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72]     target = 23
       0  1  2   3   4   5   6   7   8

Round 1: low=0 high=8 mid=4 -> arr[4]=16 < 23 -> low=5
[2,5,8,12,16,|23,38,56,72]
             low=5      high=8

Round 2: low=5 high=8 mid=6 -> arr[6]=38 > 23 -> high=5
[23,38,|56,72]  (within remaining window)
 low=5  high=5

Round 3: low=5 high=5 mid=5 -> arr[5]=23 == 23 -> FOUND at index 5
```

### 4.6 Memory Representation

Binary Search on an **array** requires **O(1) random access** — this is why it works beautifully on Python `list` (array-backed) but is **inefficient on a linked list** (O(n) just to reach the middle), which is why linked lists use different search strategies (or aren't binary-searched at all).

```
Python list (array, contiguous memory):
 index:  0    1    2    3    4
memory: [2]  [5]  [8]  [12] [16]   <- O(1) access to arr[mid]

Linked list (nodes scattered in memory):
[2] -> [5] -> [8] -> [12] -> [16]   <- O(n) just to reach the "middle" node
```

### 4.7 Iterative Binary Search — Python Implementation

```python
def binary_search_iterative(arr, target):
    """
    Classic iterative binary search on a sorted (ascending) array.
    Returns index of target, or -1 if absent.
    """
    low, high = 0, len(arr) - 1

    while low <= high:                        # search space non-empty
        mid = low + (high - low) // 2          # avoids overflow (habit from C/Java)
        if arr[mid] == target:
            return mid                          # found
        elif arr[mid] < target:
            low = mid + 1                       # discard left half
        else:
            high = mid - 1                      # discard right half

    return -1                                   # search space exhausted
```

**Line-by-line explanation:**
1. `low, high = 0, len(arr)-1` — inclusive bounds of the current search window.
2. `while low <= high` — loop continues **while there is at least one element** to check. Using `<` instead of `<=` is a classic off-by-one bug that misses single-element windows.
3. `mid = low + (high - low) // 2` — computed this way (not `(low+high)//2`) to avoid integer overflow in languages with fixed-width integers. Python ints don't overflow, but **this is an important interview talking point**.
4. Three-way comparison against `arr[mid]`.
5. `low = mid + 1` / `high = mid - 1` — **must** exclude `mid` itself since it's already been checked, otherwise → **infinite loop**.

**Dry Run** — `binary_search_iterative([2,5,8,12,16,23,38,56,72], 12)`:

| Step | low | mid | high | arr[mid] | Decision |
|---|---|---|---|---|---|
| 1 | 0 | 4 | 8 | 16 | 16>12 → high=3 |
| 2 | 0 | 1 | 3 | 5  | 5<12 → low=2 |
| 3 | 2 | 2 | 3 | 8  | 8<12 → low=3 |
| 4 | 3 | 3 | 3 | 12 | match! return 3 |

**Complexity:** Time O(log n) all cases (best case O(1) if mid hits immediately); Space O(1).

### 4.8 Recursive Binary Search — Python Implementation

```python
def binary_search_recursive(arr, target, low=0, high=None):
    """
    Recursive binary search. Returns index of target, or -1.
    """
    if high is None:
        high = len(arr) - 1

    if low > high:                 # base case: search space empty
        return -1

    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
```

**Line-by-line explanation:**
- Default `high=None` trick lets callers call `binary_search_recursive(arr, target)` without knowing the length.
- Base case `low > high` mirrors the iterative loop's exit condition.
- Two recursive branches mirror the iterative `low=mid+1` / `high=mid-1` updates.

**Dry Run** — same array, target=12: identical decisions as the iterative table above, but each row is now a **stack frame** instead of a loop iteration.

**Complexity:** Time O(log n); **Space O(log n)** due to the recursion call stack (this is the key difference vs iterative, which is O(1) space) — **a very common interview follow-up question**: *"Can you do it without recursion to save space?"*

### 4.9 Iterative vs Recursive — Comparison Table

| Aspect | Iterative | Recursive |
|---|---|---|
| Space | O(1) | O(log n) (call stack) |
| Readability | Slightly less elegant | Cleaner, mirrors the math |
| Python-specific risk | None | Python's default recursion limit (1000) — irrelevant here since log n is tiny, but matters for **deep** recursions elsewhere |
| Tail-call optimized? | N/A | **No** — Python does NOT optimize tail calls, so recursion always costs real stack frames |
| Interview default | ✅ Usually preferred | Good for showing you understand the structure |

---

## 5. Binary Search Templates (Universal)

Interviewers love templates because most Binary Search bugs come from **inconsistent boundary conventions**. Below are the three templates most competitive programmers standardize on.

### 5.1 Template 1 — Exact Match ("closed interval," both ends inclusive)

```python
def template1(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```
- **When to use:** simple "does X exist" search.
- **Invariant:** answer, if it exists, is in `[lo, hi]` at all times.

### 5.2 Template 2 — Lower Bound / "Leftmost True" ("half-open interval")

```python
def template2(arr, predicate):
    """
    Finds the leftmost index where predicate(arr[index]) is True,
    assuming predicate is monotonic: False False ... False True True ... True
    """
    lo, hi = 0, len(arr)          # hi is EXCLUSIVE / one-past-end
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if predicate(arr[mid]):
            hi = mid               # mid COULD be the answer, keep it in range
        else:
            lo = mid + 1            # mid is definitely not the answer
    return lo                       # lo == hi == first True index (or len(arr) if none)
```
- **When to use:** lower_bound, first occurrence, "search on answer" (minimize feasible value).
- **Invariant:** everything in `[0, lo)` is `False`; everything in `[hi, n)` is `True`; loop ends when `lo == hi`.
- ⚠️ **This is the single most important template to memorize** — first occurrence, lower bound, peak element, rotated search, and search-on-answer can ALL be expressed with this template by changing the `predicate`.

### 5.3 Template 3 — Upper Bound / "Rightmost True"

```python
def template3(arr, predicate):
    """
    Finds the rightmost index where predicate(arr[index]) is True,
    assuming predicate is monotonic: True True ... True False False ... False
    """
    lo, hi = 0, len(arr) - 1
    ans = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if predicate(arr[mid]):
            ans = mid               # record candidate, look further right
            lo = mid + 1
        else:
            hi = mid - 1
    return ans
```
- **When to use:** upper_bound, last occurrence, "search on answer" (maximize feasible value).

### 5.4 Choosing a Template — Decision Flow

```
Is the question "does this exact value exist"?
        │
        Yes ──────────────► Template 1
        │
        No
        │
Is it "find the FIRST/leftmost position satisfying a condition"?
        │
        Yes ──────────────► Template 2
        │
        No
        │
Is it "find the LAST/rightmost position satisfying a condition"?
        │
        Yes ──────────────► Template 3
```

> 🧠 **Interview Tip:** State out loud which template you're using and *why the predicate is monotonic* before coding — this alone signals strong fundamentals to an interviewer.

---
## 6. Binary Search Patterns

### 6.1 First & Last Occurrence

**Problem Statement:** Given a sorted array with duplicates, find the first and last index of `target`.

**Approach:** Run Binary Search, but instead of returning immediately on a match, keep narrowing in the direction of the boundary you want.

```python
def find_first_occurrence(arr, target):
    lo, hi, ans = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            ans = mid           # record, but keep searching LEFT for an earlier one
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

def find_last_occurrence(arr, target):
    lo, hi, ans = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            ans = mid           # record, but keep searching RIGHT for a later one
            lo = mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans
```

**ASCII Visualization:**

```
arr = [2, 4, 4, 4, 4, 7, 9]      target = 4
       0  1  2  3  4  5  6

find_first: shrinks toward index 1 (leftmost 4)
find_last : shrinks toward index 4 (rightmost 4)
```

**Dry Run — find_first_occurrence:**

| Step | lo | mid | hi | arr[mid] | Action |
|---|---|---|---|---|---|
| 1 | 0 | 3 | 6 | 4 | match, ans=3, hi=2 |
| 2 | 0 | 1 | 2 | 4 | match, ans=1, hi=0 |
| 3 | 0 | 0 | 0 | 2 | 2<4, lo=1 |
| loop ends (lo>hi) | | | | | return ans=1 |

**Complexity:** O(log n) time, O(1) space.

**Edge Cases:** target absent → returns -1; all elements equal target → first=0, last=n-1; single-element array.

**Common Mistakes:** Returning immediately on match (loses the "keep searching" behavior); confusing which direction (`lo=mid+1` vs `hi=mid-1`) to continue in.

**Variations:** Combine both to get **count of occurrences** = `last - first + 1` (if found).

---

### 6.2 Lower Bound & Upper Bound

**Definition:**
- **Lower Bound**: first index `i` such that `arr[i] >= target`.
- **Upper Bound**: first index `i` such that `arr[i] > target`.

```python
def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo

def upper_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

These are literally **Template 2** with predicates `arr[mid] >= target` and `arr[mid] > target` respectively — matching Python's own `bisect.bisect_left` / `bisect.bisect_right`.

**ASCII Visualization:**

```
arr = [1, 3, 3, 3, 5, 7]    target = 3
       0  1  2  3  4  5

lower_bound(3) = 1   (first index with value >= 3)
upper_bound(3) = 4   (first index with value >  3)
```

**Dry run of lower_bound([1,3,3,3,5,7], 3):**

| Step | lo | hi | mid | arr[mid] | Action |
|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 3 | >=3, hi=3 |
| 2 | 0 | 3 | 1 | 3 | >=3, hi=1 |
| 3 | 0 | 1 | 0 | 1 | <3, lo=1 |
| loop ends (lo==hi=1) | | | | | return 1 |

**Applications:** Insert position, counting elements ≤/≥/</> a value, finding closest values.

---

### 6.3 Floor & Ceiling

**Definition:**
- **Floor of x** = largest element `<= x`.
- **Ceiling of x** = smallest element `>= x`.

```python
def find_floor(arr, x):
    lo, hi, ans = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] <= x:
            ans = arr[mid]
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

def find_ceiling(arr, x):
    lo, hi, ans = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] >= x:
            ans = arr[mid]
            hi = mid - 1
        else:
            lo = mid + 1
    return ans
```

**Real-world analogy:** Rounding a price down to the nearest available denomination (floor) or up to the next available size (ceiling) — e.g., "next available appointment slot after 2:30 PM" = ceiling search over time slots.

**Edge Cases:** x smaller than all elements → floor = -1 (none); x larger than all → ceiling = -1 (none).

---

### 6.4 Count Occurrences

```python
def count_occurrences(arr, target):
    first = find_first_occurrence(arr, target)
    if first == -1:
        return 0
    last = find_last_occurrence(arr, target)
    return last - first + 1
```

**Complexity:** O(log n) — two binary searches, still logarithmic, dramatically better than the O(n) brute-force count.

---

### 6.5 Search Insert Position

**Problem Statement (LeetCode 35):** Given a sorted array and a target, return the index if found; otherwise return the index where it would be inserted to keep the array sorted.

```python
def search_insert(arr, target):
    return lower_bound(arr, target)   # identical to lower_bound!
```

**Insight:** This problem is *literally* `bisect.bisect_left`. Recognizing this equivalence instantly is a strong interview signal.

---

### 6.6 Peak Element

**Problem Statement (LeetCode 162):** Find an index `i` such that `arr[i] > arr[i-1]` and `arr[i] > arr[i+1]` (treat out-of-bounds neighbors as `-∞`). Array is NOT necessarily sorted, but has no two adjacent equal elements.

**Why Binary Search still applies:** The "slope" of the array is a usable monotonic-like signal — if `arr[mid] < arr[mid+1]`, a peak is guaranteed to exist to the right (the sequence must eventually turn downward or hit the boundary).

```python
def find_peak_element(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1        # peak is to the right (climbing uphill)
        else:
            hi = mid            # peak is at mid or to the left (going downhill)
    return lo
```

**ASCII Visualization:**

```
arr = [1, 2, 3, 1]         index: 0 1 2 3
            ↑ peak at index 2 (3 > 2 and 3 > 1)

        3
       / \
      2   1
     /
    1

At mid, if arr[mid] < arr[mid+1] -> uphill -> peak lies to the right.
If arr[mid] > arr[mid+1] -> downhill -> peak lies at mid or to the left.
```

**Dry Run** — `find_peak_element([1,2,3,1])`:

| Step | lo | hi | mid | arr[mid] vs arr[mid+1] | Action |
|---|---|---|---|---|---|
| 1 | 0 | 3 | 1 | 2 < 3 | lo=2 |
| 2 | 2 | 3 | 2 | 3 > 1 | hi=2 |
| loop ends (lo==hi=2) | | | | | return 2 |

**Complexity:** O(log n). **Common Mistake:** Trying to binary search on the *values* instead of the *slope* — the array isn't sorted, so this only works because we search on the **direction of change**, not the raw values.

---

### 6.7 Search in Rotated Sorted Array

**Problem Statement (LeetCode 33):** A sorted array has been rotated at an unknown pivot (e.g., `[4,5,6,7,0,1,2]`). Find target in O(log n).

**Approach:** At every step, **at least one half of `[lo, mid]` or `[mid, hi]` is guaranteed to be normally sorted.** Determine which half is sorted, then check if the target lies within that half's range — if yes, recurse there; if no, go to the other half.

```python
def search_rotated(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid

        if arr[lo] <= arr[mid]:                      # left half [lo..mid] is sorted
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                          # right half [mid..hi] is sorted
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

**ASCII Visualization:**

```
arr = [4, 5, 6, 7, 0, 1, 2]      target = 0
       0  1  2  3  4  5  6

mid = 3 -> arr[3] = 7
arr[lo]=4 <= arr[mid]=7  -> LEFT half [4,5,6,7] is sorted
is target(0) in [4,7)? No -> search RIGHT half -> lo = mid+1 = 4

Now lo=4 hi=6, mid=5 -> arr[5]=1
arr[lo]=0 <= arr[mid]=1 -> LEFT half [0,1] sorted
is target(0) in [0,1)? Yes -> hi = mid-1 = 4
Now lo=4 hi=4 mid=4 -> arr[4]=0 == target -> FOUND at index 4
```

**Complexity:** O(log n). **Edge Cases:** No rotation (fully sorted); target at pivot; array with all identical elements (see 6.7.1 below); single element.

**Common Mistakes:**
- Using `<=` vs `<` incorrectly when checking `arr[lo] <= target < arr[mid]` — must match inclusive/exclusive correctly with sorted-half boundaries.
- Forgetting duplicates can break the "which half is sorted" determination (see next).

#### 6.7.1 Variation: Rotated Array WITH Duplicates (LeetCode 81)

When `arr[lo] == arr[mid]`, you cannot tell which half is sorted. Fix: shrink the ambiguous boundary by one.

```python
def search_rotated_with_duplicates(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return True
        if arr[lo] == arr[mid] == arr[hi]:
            lo += 1
            hi -= 1
        elif arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return False
```

**Complexity:** Worst-case degrades to O(n) when there are many duplicates (e.g., `[2,2,2,2,2,2,1,2]`), because `lo+=1, hi-=1` may only shrink by one element per step.

#### 6.7.2 Find Minimum in Rotated Sorted Array (the pivot)

```python
def find_min_rotated(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > arr[hi]:
            lo = mid + 1          # minimum is to the right
        else:
            hi = mid               # minimum is at mid or to the left
    return arr[lo]
```

---

### 6.8 Search in Nearly Sorted Array

**Problem Statement:** In an array where each element may be swapped with at most one adjacent neighbor (e.g., `[10, 3, 40, 20, 50]` → 3 and 10 swapped, 20 and 40 swapped), find target in O(log n).

```python
def search_nearly_sorted(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        if mid - 1 >= lo and arr[mid - 1] == target:
            return mid - 1
        if mid + 1 <= hi and arr[mid + 1] == target:
            return mid + 1
        if arr[mid] < target:
            lo = mid + 2      # skip mid+1 since we already checked it
        else:
            hi = mid - 2      # skip mid-1 since we already checked it
    return -1
```

**Insight:** Check `mid-1` and `mid+1` in addition to `mid` at every step, then jump by 2 instead of 1.

---

### 6.9 Search in a 2D Matrix

#### 6.9.1 Fully Sorted Matrix (each row sorted, first element of each row > last element of previous row)

Treat the matrix as a **flattened sorted array** using index math — this avoids ever materializing the flattened array.

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        r, c = divmod(mid, cols)          # convert 1D index -> 2D coordinates
        val = matrix[r][c]
        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
```

**ASCII Visualization:**

```
matrix = [[ 1,  3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]

Flattened view (conceptually):
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
 0  1  2  3   4   5   6   7   8   9  10  11

divmod(mid, cols) converts a flat index back to (row, col)
e.g. mid=6 -> divmod(6,4) = (1, 2) -> matrix[1][2] = 16
```

#### 6.9.2 Row-wise and Column-wise Sorted Matrix (LeetCode 240) — Staircase Search

Here rows AND columns are sorted independently, but rows aren't globally ordered relative to each other — the flattening trick doesn't apply. Use the **"staircase"** approach: start top-right, move left if too big, move down if too small.

```python
def search_matrix_staircase(matrix, target):
    if not matrix or not matrix[0]:
        return False
    row, col = 0, len(matrix[0]) - 1     # start at top-right corner
    while row < len(matrix) and col >= 0:
        val = matrix[row][col]
        if val == target:
            return True
        elif val > target:
            col -= 1                      # too big -> eliminate this column
        else:
            row += 1                      # too small -> eliminate this row
    return False
```

**ASCII Visualization:**

```
matrix = [[ 1,  4,  7, 11],
          [ 2,  5,  8, 12],
          [ 3,  6,  9, 16]]
target = 5

start at top-right: (0,3)=11 > 5 -> move left
(0,2)=7 > 5 -> move left
(0,1)=4 < 5 -> move down
(1,1)=5 == 5 -> FOUND
```

**Complexity:** O(rows + cols) — not O(log(rows*cols)) since rows aren't globally sorted relative to each other; still far better than O(rows*cols).

**When to use which:** fully-sorted-as-flattened-array → binary search O(log(r*c)); row/col independently sorted → staircase O(r+c).

---

### 6.10 Binary Search on Answer

**Definition:** Instead of searching over array indices, binary search over the **range of possible answers**, using a `feasible(x)` predicate that is monotonic.

**Why it exists:** Many optimization problems ("minimize the maximum," "maximize the minimum," "smallest X such that condition holds") have a hidden monotonic structure even though there's no explicit sorted array.

**General Template:**

```python
def binary_search_on_answer(lo, hi, feasible):
    """
    Finds the SMALLEST x in [lo, hi] for which feasible(x) is True,
    assuming feasibility is monotonic: False...False True...True
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**Worked Example — "Koko Eating Bananas" (LeetCode 875):**

> Koko has piles of bananas. She eats at speed `k` bananas/hour. Given `h` hours, find the minimum `k` such that she can eat all bananas within `h` hours.

```python
import math

def min_eating_speed(piles, h):
    def feasible(k):
        hours_needed = sum(math.ceil(pile / k) for pile in piles)
        return hours_needed <= h

    lo, hi = 1, max(piles)     # speed range: 1 banana/hr to max pile size
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid            # mid works, try slower
        else:
            lo = mid + 1        # mid too slow, need faster
    return lo
```

**Why `feasible(k)` is monotonic:** if speed `k` works, any speed `> k` also works (finishes even faster) → `False,False,...,False,True,True,...,True` shape → binary search applies even though we never sorted anything.

**Other classic "search on answer" problems:**
| Problem | feasible(x) meaning |
|---|---|
| Aggressive Cows (max-min distance) | "can we place all cows with min distance ≥ x?" |
| Book Allocation / Split Array Largest Sum | "can we split into k parts each ≤ x?" |
| Capacity To Ship Packages Within D Days | "can ship all packages in ≤ D days with capacity x?" |
| Median of Two Sorted Arrays (advanced) | binary search on the partition index |
| Square Root of a number | "is x*x <= n?" |

**Interview Tip:** Whenever a problem says "minimize the maximum" or "maximize the minimum," think **Binary Search on Answer** immediately — it's one of the highest-leverage pattern recognitions in FAANG interviews.

**Common Mistakes:** Picking wrong `lo`/`hi` bounds (must guarantee `feasible(hi)` is True and cover all valid answers); off-by-one in whether to use Template 2 (leftmost True) vs Template 3 (rightmost True) depending on whether you're minimizing or maximizing.

---

### 6.11 Binary Search on Infinite / Unbounded Array

**Problem:** Array size unknown (or "infinite," e.g., a stream/API that only supports indexed access and returns a sentinel past the end). Find target.

**Approach:** First find a valid upper bound by **doubling** (this is literally Exponential Search — see Section 7.3), then run ordinary binary search within `[prev_bound, current_bound]`.

```python
def search_infinite_array(reader, target):
    """
    reader(i) simulates an API that returns arr[i], or float('inf') if i is out of bounds.
    """
    lo, hi = 0, 1
    while reader(hi) < target:
        lo = hi
        hi *= 2                     # doubling to find a valid upper bound

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        val = reader(mid)
        if val == target:
            return mid
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Complexity:** O(log p) where `p` is the position of the target — we never need to know the true array size.

---
## 7. Other Classical Search Algorithms

### 7.1 Jump Search

**Definition:** Divide the sorted array into blocks of size `√n`. Jump block-by-block until you find a block that could contain the target, then linear-search within that block.

**Why it exists:** A middle ground between Linear Search O(n) and Binary Search O(log n) — useful when "jumping back" (random access one step at a time) is cheaper than a full binary search's back-and-forth jumps, e.g., on certain external storage/tape systems where sequential access is cheaper than random access.

**Real-world analogy:** Skimming a book by jumping every 20 pages until you overshoot your target topic, then flipping back and reading normally.

**ASCII Visualization:**

```
arr = [1,3,5,7,9,11,13,15,17,19]  n=10, block size = √10 ≈ 3
       0 1 2 3 4 5  6  7  8  9

target = 13

Blocks:  [1,3,5] [7,9,11] [13,15,17] [19]
index:    0 1 2   3  4  5   6  7  8   9

Jump: check index 2 (5) -> 5<13, jump to index 5 (11) -> 11<13, jump to index 8 (17) -> 17>=13, STOP jumping
Linear search backwards within block [6,7,8]: index 6 -> 13 == target -> FOUND
```

**Python Implementation:**

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))          # optimal block size
    prev = 0

    # Phase 1: jump ahead in blocks
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Phase 2: linear search within the identified block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1
```

**Line-by-line explanation:**
1. `step = √n` — the theoretically optimal block size that balances jump-count vs linear-scan-count.
2. Phase 1 loop advances `prev`/`step` by `√n` each time, checking the last element of each block.
3. Phase 2 does an ordinary linear scan over the identified block only.

**Dry Run:** shown in the visualization above.

**Complexity:**

| Case | Time | Space |
|---|---|---|
| Best | O(1) | O(1) |
| Average/Worst | O(√n) | O(1) |

**Why √n is optimal:** Total cost = (n/step) jumps + (step) linear comparisons. Minimizing `n/step + step` via calculus gives `step = √n`.

**Edge Cases:** target smaller than first element; target larger than last element; empty array; block size ≥ n (degenerates to linear search).

**Common Mistakes:** Off-by-one in block boundaries (`min(step, n) - 1`); forgetting `prev >= n` early exit causing index errors.

**When to use:** Sorted data where **jumping backward is costly** (e.g., magnetic tape, some external-memory structures) — rare in typical interviews but a strong CS-fundamentals topic.

**When NOT to use:** In-memory arrays with O(1) random access — Binary Search always dominates (O(log n) < O(√n)).

---

### 7.2 Interpolation Search

**Definition:** An improvement over Binary Search for **uniformly distributed sorted data** — instead of always checking the middle, it estimates the probable position of the target using linear interpolation (like guessing where "M" is in a dictionary based on proportional position, not always opening to the exact middle).

**Formula:**

```
pos = lo + ((target - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo])
```

**Real-world analogy:** Looking up "Smith" in a phone book — you flip to roughly 80% through, not the exact middle, because you know "S" is near the end of the alphabet.

**ASCII Visualization:**

```
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]   target = 70
        0   1   2   3   4   5   6   7   8    9

Binary search would check mid = index 4 (value 50) first.
Interpolation search estimates:
pos = 0 + ((70-10)*(9-0)) // (100-10) = (60*9)//90 = 540//90 = 6
Directly checks index 6 -> value 70 -> FOUND in ONE probe!
```

**Python Implementation:**

```python
def interpolation_search(arr, target):
    lo, hi = 0, len(arr) - 1

    while lo <= hi and arr[lo] <= target <= arr[hi]:
        if arr[lo] == arr[hi]:               # avoid division by zero
            return lo if arr[lo] == target else -1

        pos = lo + ((target - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1

    return -1
```

**Line-by-line explanation:**
1. Loop condition also checks `arr[lo] <= target <= arr[hi]` — if the target is outside the current range, it cannot exist (a nice early-exit that plain Binary Search doesn't explicitly need, but is implicit there).
2. Guard against `arr[lo] == arr[hi]` to avoid a `ZeroDivisionError`.
3. `pos` formula — proportional estimate of where target *should* be if data is uniformly distributed.
4. Same three-way branching as Binary Search, but narrowing to `pos` instead of `mid`.

**Dry Run:** shown above — found in 1 probe vs binary search's typical ~4 probes for this dataset.

**Complexity:**

| Case | Time | Condition |
|---|---|---|
| Best/Average (uniform distribution) | O(log log n) | data is roughly evenly spaced |
| Worst (skewed distribution, e.g. exponential) | O(n) | e.g. `[1,2,3,4,...,100, 10000000]` |
| Space | O(1) | |

**Edge Cases:** all elements identical (guarded above); target outside `[arr[lo], arr[hi]]`; non-uniform distributions degrading to O(n) — **must mention this trade-off in interviews**.

**Common Mistakes:** Forgetting the divide-by-zero guard; assuming O(log log n) unconditionally (it depends entirely on data distribution — a frequently-tested nuance).

**Interview Tip:** Bring this up when asked "how would you improve binary search for a specific dataset" (e.g., uniformly distributed numeric IDs, timestamps).

---

### 7.3 Exponential Search

**Definition:** Find a range `[i/2, i]` where the target could exist by repeatedly doubling `i` (1, 2, 4, 8, 16, ...), then run ordinary Binary Search within that range.

**Why it exists:** Ideal for **unbounded/infinite arrays** or when the target is expected to be near the **beginning** of a very large array (avoids the O(log n) "wasted" comparisons of binary search starting from a huge range).

**Real-world analogy:** `git bisect` when you don't know how many commits back a bug was introduced — you'd check HEAD~1, HEAD~2, HEAD~4, HEAD~8... doubling until you overshoot, then binary search within that window.

**ASCII Visualization:**

```
arr = [1,2,3,5,8,13,21,34,55,89,144]  target = 34
index: 0 1 2 3 4  5  6  7  8  9  10

Phase 1 (doubling): check index 1(2) -> <34, index 2(3) -> <34,
                     index 4(8) -> <34, index 8(55) -> >=34 STOP

Range found: [4, 8]  (previous power, current power)

Phase 2: ordinary binary search within arr[4..8] = [8,13,21,34,55]
         -> finds 34 at global index 7
```

**Python Implementation:**

```python
def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0

    i = 1
    while i < n and arr[i] <= target:
        i *= 2                          # double the bound

    lo, hi = i // 2, min(i, n - 1)      # narrow range for binary search

    # standard binary search within [lo, hi]
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Line-by-line explanation:**
1. Handle empty array and immediate match at index 0 as special cases.
2. Doubling loop: `i` grows 1, 2, 4, 8, ... until `arr[i] > target` or out of bounds.
3. `lo, hi = i//2, min(i, n-1)` — the range is bounded by the last "too small" checkpoint and the first "too big" (or end-of-array) checkpoint.
4. Standard binary search on that narrowed range.

**Complexity:**

| Phase | Time |
|---|---|
| Doubling (finding range) | O(log p) where p = position of target |
| Binary search within range | O(log p) |
| **Total** | **O(log p)** |

This beats plain Binary Search's O(log n) when `p << n` (target near the front). For target near the end, it's roughly the same as Binary Search.

**Edge Cases:** target at index 0; target at last index; empty array; target absent (larger than all elements — doubling runs until `i >= n`).

**When to use:** Unbounded/streaming arrays, or when you have a strong prior that the target is near the start.

**When NOT to use:** Small arrays or no reason to believe the target is near the start — plain Binary Search is simpler and equally efficient.

---

### 7.4 Fibonacci Search

**Definition:** A Binary-Search variant that uses **Fibonacci numbers** to divide the array instead of the midpoint, using only **addition/subtraction** instead of division — historically significant for hardware **without a fast division unit**.

**Why it exists:** On old hardware, division was much slower than addition/subtraction. Fibonacci Search achieves O(log n) search using only `+`/`-`, avoiding `/` and `%` entirely for computing the split point. Today this is mostly of **historical/academic interest**, but it's a classic CS-course and interview-trivia topic.

**ASCII Visualization:**

```
Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, ...

arr with n=10 elements. Smallest Fibonacci number >= 10 is 13 (F(7)=13, F(6)=8, F(5)=5)

Split point uses F(5)=5 (two Fibonacci numbers back) to decide the probe index,
instead of computing n/2 via division.
```

**Python Implementation:**

```python
def fibonacci_search(arr, target):
    n = len(arr)

    fib2, fib1 = 0, 1              # (n-2)'th and (n-1)'th Fibonacci numbers
    fib = fib2 + fib1               # n'th Fibonacci number
    while fib < n:
        fib2, fib1 = fib1, fib
        fib = fib2 + fib1

    offset = -1                     # marks eliminated range from the front

    while fib > 1:
        i = min(offset + fib2, n - 1)   # candidate index using Fibonacci, no division!

        if arr[i] < target:
            fib, fib1, fib2 = fib1, fib2, fib1 - fib2
            offset = i
        elif arr[i] > target:
            fib, fib1 = fib2, fib1 - fib2
        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1
```

**Line-by-line explanation:**
1. Find the smallest Fibonacci number `fib >= n` — this determines the initial "frame" size.
2. `offset` tracks how much of the array (from the front) has been eliminated.
3. `i = offset + fib2` — the probe index, computed with pure addition.
4. If `arr[i] < target`: shift down two Fibonacci indices (eliminate the front portion up to `i`).
5. If `arr[i] > target`: shift down one Fibonacci index (eliminate the back portion after `i`).
6. Final check handles a leftover single-element edge case.

**Complexity:** O(log n) time (Fibonacci numbers grow exponentially, same base logic as Binary Search), O(1) space.

**Comparison with Binary Search:**

| Aspect | Binary Search | Fibonacci Search |
|---|---|---|
| Split computation | Division (`//2`) | Addition/subtraction only |
| Access pattern | Always exact middle | Slightly uneven splits (golden-ratio-like) |
| Relevance today | Universal | Mostly historical / embedded systems trivia |
| Cache behavior | N/A | Can be marginally better for certain block storage due to smaller probe steps near the edges |

**Interview Tip:** Rarely implemented live, but knowing it exists ("Binary Search variant that avoids division using Fibonacci numbers, useful on hardware without cheap division") is a great differentiator if asked "what other search algorithms do you know?"

---

### 7.5 Ternary Search

**Definition:** Instead of splitting into 2 parts (Binary Search), split the range into **3 parts** using two midpoints `m1`, `m2`. Primarily used for finding the maximum/minimum of a **unimodal function** (a function that strictly increases then strictly decreases, or vice versa) — NOT a general replacement for binary search on sorted arrays.

**Why it exists:** For finding an **extremum** (peak/valley) of a unimodal function over a continuous or discrete domain, where there's no explicit "target value" to compare against — just a shape to exploit.

**ASCII Visualization:**

```
Unimodal function (single peak):

        f(x)
         ^
         |        ___
         |      /     \
         |    /         \
         |  /             \
         |/                 \
         +---------------------> x
           m1        m2

If f(m1) < f(m2): the peak lies in [m1, hi]  (discard [lo, m1))
If f(m1) > f(m2): the peak lies in [lo, m2]  (discard (m2, hi])
```

**Python Implementation (finding maximum of a unimodal function):**

```python
def ternary_search_max(f, lo, hi, epsilon=1e-9):
    """
    Finds x that maximizes unimodal function f over [lo, hi].
    Works on continuous domains (floats).
    """
    while hi - lo > epsilon:
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) < f(m2):
            lo = m1                  # peak is to the right of m1
        else:
            hi = m2                  # peak is to the left of m2
    return (lo + hi) / 2

# Discrete version (array index search for the peak)
def ternary_search_discrete(arr, lo, hi):
    while hi - lo > 2:
        m1 = lo + (hi - lo) // 3
        m2 = hi - (hi - lo) // 3
        if arr[m1] < arr[m2]:
            lo = m1 + 1
        else:
            hi = m2 - 1
    return max(range(lo, hi + 1), key=lambda i: arr[i])
```

**Dry Run (conceptual)** — `f(x) = -(x-5)**2 + 10` (peak at x=5) over `[0, 10]`:

| Step | lo | hi | m1 | m2 | f(m1) vs f(m2) | Action |
|---|---|---|---|---|---|---|
| 1 | 0 | 10 | 3.33 | 6.67 | f(3.33)=7.2, f(6.67)=7.2 (~equal) | narrows symmetrically toward 5 |
| ... | ... | ... | ... | ... | ... | converges near x=5 |

**Complexity:** O(log₃(n)) ≈ O(log n) — asymptotically same order as Binary Search, but with a **larger constant** (2 function evaluations per iteration instead of 1), so in practice **Binary Search on the derivative's sign (if available) is often preferred** for discrete unimodal problems.

**Edge Cases:** flat regions (multiple x with the same max value) — ternary search's strict inequality assumptions can behave unpredictably; must confirm strict unimodality.

**Common Mistakes:**
- Using Ternary Search on a plain **sorted array to find a target value** — this is a classic misconception. Ternary Search is for **unimodal optimization**, not for target-lookup in sorted data (Binary Search is strictly better there — fewer comparisons, same complexity class).
- Not handling floating-point precision (`epsilon`) termination correctly, causing infinite loops.

**When to use:** Maximizing/minimizing a unimodal function (competitive programming "search the peak" problems, geometry optimization).

**When NOT to use:** General sorted-array searching — use Binary Search instead (it's strictly better: same complexity, half the comparisons per step).

---
## 8. Searching Patterns & Problem-Solving Frameworks

### 8.1 Search Space Reduction — The Unifying Idea

Every efficient searching algorithm in this handbook follows the same meta-pattern:

```
1. Define a search space (array indices, a value range, a 2D grid, an answer range).
2. Define a way to evaluate a candidate ("compare," "predicate," "feasible(x)").
3. Use the evaluation result to DISCARD a portion of the space that cannot contain the answer.
4. Repeat until the space is empty or a single candidate remains.
```

This is why Binary Search, Binary Search on Answer, Rotated Array Search, Peak Finding, and even Ternary Search all "feel similar" — they are the *same algorithdmic skeleton* applied to different predicates/spaces.

### 8.2 Divide and Conquer — Searching Perspective

Binary Search is technically a **degenerate case of Divide and Conquer** where only ONE of the two halves needs to be recursed into (unlike, say, Merge Sort, which recurses into BOTH halves). This is precisely why Binary Search is O(log n) instead of O(n log n).

```
Merge Sort:      T(n) = 2·T(n/2) + O(n)     -> O(n log n)   (both halves processed)
Binary Search:   T(n) = 1·T(n/2) + O(1)     -> O(log n)     (only ONE half processed)
```

### 8.3 Two-Pointer vs Binary Search — When Each Applies

| Aspect | Two Pointer | Binary Search |
|---|---|---|
| Typical use | Pair-sum, subarray window problems on sorted data | Single-target/boundary lookup, "search on answer" |
| Movement | Pointers move inward from both ends, O(n) total | Jumps to a computed midpoint, O(log n) |
| Requires sorted data? | Often yes | Often yes (or monotonic predicate) |
| Example | "Two Sum II" (sorted array) | "Find first bad version" |

> Both exploit **sortedness/monotonicity**, but Two Pointer explores the space **linearly** (still O(n), just with a better constant than brute force), while Binary Search explores it **logarithmically**.

### 8.4 Range Search

**Definition:** Find ALL elements/indices within `[low_target, high_target]`.

```python
def range_search(arr, low_target, high_target):
    start = lower_bound(arr, low_target)
    end = upper_bound(arr, high_target)
    return arr[start:end], (start, end - 1)
```

Uses two binary searches — O(log n) to find boundaries, regardless of how many elements are actually in the range.

### 8.5 Monotonic Search

**Definition:** A generalization: any function/predicate `f` over an ordered domain is *monotonic* if `f` never "goes back" once it changes value. Whenever you can prove a problem's predicate is monotonic, Binary Search (via Template 2/3) applies — even without a literal sorted array.

**Recognizing monotonicity is often THE hardest and most valuable interview skill** in this entire handbook.

### 8.6 Decision-Based Search

Frame the problem as a **yes/no decision function** over a range, then binary search the boundary:

```
"Can we achieve X with budget/capacity/time = v?"  → feasible(v): bool
Find the SMALLEST/LARGEST v for which feasible(v) is True.
```

This is exactly Section 6.10 (Binary Search on Answer) — repeated here because it deserves to be recognized as a **pattern**, not just a "trick for a few problems."

---

## 9. Applications of Searching

### 9.1 Databases

- **B-Trees / B+Trees:** Index structures where each node itself is searched with (a variant of) Binary Search before descending to a child — this is why database index lookups are O(log n) even over billions of rows.
- **Binary search within sorted pages:** many storage engines binary-search within a sorted page of rows before falling back to sequential scan.

### 9.2 Search Engines

- **Inverted Index:** maps each term → sorted list of document IDs; querying multiple terms requires efficiently **intersecting sorted lists** (a searching/merging problem).
- **Autocomplete:** typically backed by a Trie or sorted list + binary search for prefix range queries (`lower_bound("appl")` to `upper_bound("appl" + chr(0x10FFFF))`-style range queries).

### 9.3 Dictionaries & Sets (Hashing, for contrast)

Python `dict`/`set` use **hashing**, not comparison-based search — O(1) average case. Mentioned here only to clarify **when NOT to reach for Binary Search**: if you don't need order, ranking, or range queries, a hash-based structure is usually faster.

### 9.4 File Systems

- Directory lookups in many filesystems use B-Tree-like structures (e.g., ext4's HTree, NTFS's B+Tree) — binary/tree search for filenames.

### 9.5 Information Retrieval

- Ranking, TF-IDF top-k retrieval often combine hashing (fast lookup) with sorted-structure search (range/threshold queries) — e.g., "give me all documents with a score above X" = a **lower_bound/upper_bound**-style operation on a sorted score list.

### 9.6 Indexing

- Any database index (B-Tree, LSM-Tree in modern databases like RocksDB/Cassandra) fundamentally relies on searching sorted structures to achieve sub-linear lookup.

### 9.7 Scheduling & Optimization

- "Binary Search on Answer" directly powers real scheduling problems: load balancing (minimize the maximum load), job sequencing with deadlines, and resource allocation (e.g., Kubernetes-style bin packing heuristics).

### 9.8 Version Control — `git bisect`

`git bisect` is literally Binary Search applied to a **commit history search space**, where the "predicate" is "is this commit good or bad?" — a perfect real-world illustration of monotonic-predicate search (assuming the bug, once introduced, stays introduced).

---
## 10. Problem Recognition Guide

### 10.1 Recognition Flowchart

```
START: Read the problem statement.
   │
   ├─ Is the data explicitly sorted OR can it be sorted without breaking the problem?
   │      │
   │     Yes
   │      │
   │      ├─ Does it ask for exact existence? ──────────────► Binary Search (Template 1)
   │      ├─ Does it ask for first/last position? ──────────► Template 2 / Template 3
   │      ├─ Is the array rotated? ──────────────────────────► Modified Binary Search (6.7)
   │      ├─ Is it a 2D grid, sorted rows/cols? ──────────────► Matrix Search (6.9)
   │      └─ Otherwise → plain Binary Search variants
   │
   ├─ Is there NO explicit array, but a RANGE of possible numeric answers
   │  with a "can we achieve X?" yes/no decision that gets easier/harder
   │  monotonically as X increases? ─────────────────────────► Binary Search on Answer (6.10)
   │
   ├─ Is it about finding a peak/valley of an unimodal sequence
   │  (not a target VALUE, but an EXTREMUM)? ─────────────────► Peak Element (6.6) / Ternary Search (7.5)
   │
   ├─ Is data unsorted and has NO exploitable structure? ─────► Linear Search (3.1)
   │
   └─ Is a hash-based O(1) lookup sufficient (no ordering/range needs)? ─► use dict/set, not a search algorithm
```

### 10.2 Interview Clues — Keyword Table

| Keyword / Phrase in Problem | Likely Pattern |
|---|---|
| "sorted array" | Binary Search family |
| "first occurrence" / "last occurrence" | Templates 2/3 |
| "insert position" | lower_bound |
| "rotated" | Rotated Array Search |
| "minimum X such that condition holds" | Binary Search on Answer (minimize) |
| "maximum X such that condition holds" | Binary Search on Answer (maximize) |
| "minimize the maximum" / "maximize the minimum" | Binary Search on Answer |
| "peak" / "valley" | Peak Element / Ternary Search |
| "matrix sorted row-wise and column-wise" | Staircase Search |
| "matrix fully sorted" | Flattened Binary Search |
| "infinite array" / "stream" | Exponential Search |
| "count of elements ≤/≥ X" | lower_bound / upper_bound |
| "closest element to X" | Floor/Ceiling comparison |
| "unimodal function" | Ternary Search |
| "no random access / expensive random access" | Jump Search (rare, conceptual) |
| "uniformly distributed data" | Interpolation Search |

### 10.3 Monotonic Property Recognition — Self-Check Questions

Ask yourself:
1. If I fix a candidate answer `x`, can I answer "is `x` good enough?" in a **deterministic** way?
2. If `x` is good enough, is every value **on one side** of `x` (either all larger or all smaller) ALSO good enough?
3. Is there NO case where "good" and "bad" answers interleave unpredictably?

If all three are "yes," the problem has a monotonic predicate → Binary Search applies, even without an explicit sorted array.

---

## 11. Optimization: Brute Force → Better → Optimal

### 11.1 General Progression Table

| Problem | Brute Force | Better | Optimal |
|---|---|---|---|
| Find target in sorted array | Linear scan O(n) | — | Binary Search O(log n) |
| Count occurrences | Linear scan + counter O(n) | — | Two binary searches (first/last) O(log n) |
| Find element in rotated array | Linear scan O(n) | Find pivot then binary search (2 passes) O(log n) | Single-pass modified binary search O(log n) |
| Search 2D matrix (fully sorted) | Scan every cell O(r·c) | Binary search each row O(r log c) | Treat as flattened 1D array O(log(r·c)) |
| Search 2D matrix (row & col sorted) | Scan every cell O(r·c) | Binary search each row O(r log c) | Staircase search O(r + c) |
| Minimize max load (Koko-style) | Try every speed 1..max O(max·n) | — | Binary search on answer O(n log max) |
| Find peak element | Scan and compare neighbors O(n) | — | Binary search on slope O(log n) |
| kth smallest in two sorted arrays | Merge both, then index O(m+n) | — | Binary search on partition O(log(min(m,n))) |

### 11.2 Choosing the Right Search Algorithm — Cheat Table

| Situation | Best Algorithm |
|---|---|
| Data unsorted, one-off search | Linear Search |
| Data unsorted, MANY repeated searches | Sort once + Binary Search, OR use a hash set |
| Data sorted, in-memory array | Binary Search |
| Data sorted, uniformly distributed numeric | Interpolation Search |
| Data sorted, unknown/infinite size | Exponential Search |
| No division hardware (embedded/legacy systems) | Fibonacci Search |
| Sequential access far cheaper than random access | Jump Search |
| No explicit array, but monotonic feasibility | Binary Search on Answer |
| Need to find an extremum of a unimodal function | Ternary Search |

### 11.3 Time-Space Trade-offs

| Approach | Time | Space | Notes |
|---|---|---|---|
| Recursive Binary Search | O(log n) | O(log n) | Call stack overhead |
| Iterative Binary Search | O(log n) | O(1) | Preferred in production/interviews unless recursion improves clarity |
| Pre-sorting then Binary Search (one-time cost) | O(n log n) once, O(log n) per query | O(1) extra (in-place sort) or O(n) (stable sort/merge sort) | Worth it if ≥ O(log n) queries follow |
| Hash Set for existence checks | O(n) build, O(1) per query | O(n) | No ordering/range query support |

---

## 12. Common Mistakes & Pitfalls

### 12.1 Off-by-One Errors

```python
# ❌ WRONG: misses the last element
while lo < hi:               # should be <= for a closed interval search!
    ...

# ✅ CORRECT (Template 1, closed interval):
while lo <= hi:
    ...
```

### 12.2 Infinite Loops

```python
# ❌ WRONG: mid never changes because 'hi = mid' with lo==mid can loop forever
# when using a closed-interval style with a half-open template mismatch:
def buggy(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid            # BUG: should be mid + 1 — may not advance!
        else:
            hi = mid
    return lo
```

**Rule of thumb:** In Template 2 (half-open `[lo, hi)`), if you move `lo`, it MUST become `mid + 1` (never plain `mid`), or the loop can stall when `lo == mid`.

### 12.3 Incorrect Mid Calculation

```python
# ⚠️ Can overflow in fixed-width-integer languages (C/C++/Java) for huge arrays:
mid = (lo + hi) // 2

# ✅ Overflow-safe (habit worth keeping even in Python, for interview credibility):
mid = lo + (hi - lo) // 2
```

> **Note on Python specifically:** Python's `int` has arbitrary precision, so `(lo+hi)//2` will NOT overflow in Python. However, **always write the overflow-safe form in interviews** — it demonstrates language-agnostic rigor and is expected knowledge, especially since this is a famous historical bug (see Section 1.3).

### 12.4 Overflow Discussion (Language Comparison)

| Language | Integer overflow risk in `(lo+hi)//2`? |
|---|---|
| Python | No (arbitrary precision integers) |
| C / C++ | **Yes**, if `lo + hi` exceeds `INT_MAX` |
| Java | **Yes** — famously caused a real bug in `java.util.Arrays.binarySearch` for 9 years |
| JavaScript | Practically no for array-length-scale numbers (uses doubles, safe up to 2^53) |

### 12.5 Wrong Boundary Updates

```python
# ❌ WRONG: forgetting +1/-1, causing infinite loop when arr[mid] doesn't match
if arr[mid] < target:
    lo = mid       # BUG — must be mid + 1
else:
    hi = mid       # BUG — must be mid - 1 (in Template 1)
```

### 12.6 Incorrect Loop Conditions

| Template | Correct condition | Common bug |
|---|---|---|
| Template 1 (closed interval) | `while lo <= hi` | Using `while lo < hi` (misses single-element checks) |
| Template 2 (half-open) | `while lo < hi` | Using `while lo <= hi` (can go out of bounds since `hi` is exclusive) |

### 12.7 Binary Search Template Mistakes — Summary Table

| Mistake | Symptom | Fix |
|---|---|---|
| Mixing closed/half-open conventions | Infinite loop or wrong answer | Pick ONE template and be consistent about whether `hi` is inclusive |
| Not excluding `mid` after checking it | Infinite loop | Always `lo = mid + 1` or `hi = mid - 1` in Template 1 |
| Wrong predicate direction | Wrong boundary found (first vs last) | Double check which side you continue searching after a match |
| Forgetting duplicates in rotated search | Wrong "which half is sorted" decision | Add the `arr[lo]==arr[mid]==arr[hi]` shrink-by-one fallback |
| Assuming interpolation search is always O(log log n) | TLE on adversarial/skewed data | Mention & handle the O(n) worst case explicitly |

### 12.8 Missing Edge Cases Checklist

- [ ] Empty array / empty search range
- [ ] Single-element array
- [ ] Target smaller than all elements
- [ ] Target larger than all elements
- [ ] Target equal to first/last element
- [ ] All elements identical
- [ ] Duplicates present when the algorithm assumes uniqueness
- [ ] Negative numbers (if using unsigned-assumption tricks)
- [ ] Already-sorted "rotated" array (rotation count = 0 or = n)

---
## 13. Interview Preparation Guide

### 13.1 Difficulty-Tiered Roadmap

**Easy:**
- Binary Search (exact match)
- Search Insert Position
- Sqrt(x)
- First Bad Version
- Find Smallest Letter Greater Than Target

**Medium:**
- First and Last Occurrence of an Element
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Search a 2D Matrix (I and II)
- Find Peak Element
- Koko Eating Bananas
- Capacity To Ship Packages Within D Days
- Find K Closest Elements

**Hard:**
- Median of Two Sorted Arrays
- Split Array Largest Sum
- Search in Rotated Sorted Array II (with duplicates)
- Aggressive Cows / Allocate Minimum Number of Pages (GfG-style)
- Kth Element of Two Sorted Arrays

### 13.2 Pattern-wise Question Map

| Pattern | Representative Problems |
|---|---|
| Exact Binary Search | Binary Search (LC 704), Sqrt(x) (LC 69) |
| First/Last Occurrence | First and Last Position of Element in Sorted Array (LC 34) |
| Lower/Upper Bound | Search Insert Position (LC 35) |
| Rotated Array | Search in Rotated Sorted Array (LC 33, 81), Find Minimum in Rotated Sorted Array (LC 153, 154) |
| Peak Element | Find Peak Element (LC 162) |
| Matrix Search | Search a 2D Matrix (LC 74), Search a 2D Matrix II (LC 240) |
| Binary Search on Answer | Koko Eating Bananas (LC 875), Capacity To Ship Packages (LC 1011), Split Array Largest Sum (LC 410), Allocate Books (GfG) |
| Advanced Partition-Based | Median of Two Sorted Arrays (LC 4) |
| Ternary Search / Peak of Unimodal | Peak Index in a Mountain Array (LC 852) |

### 13.3 Company-Wise Tendencies (General Trends, not guarantees)

| Company | Tendency |
|---|---|
| Google | Loves Binary Search on Answer and generalization to monotonic predicates |
| Amazon | Rotated array search, search insert position — practical variants |
| Meta | First/last occurrence, matrix search |
| Microsoft | Classic binary search + edge case rigor |
| Bloomberg/Fintech | Floor/Ceiling, closest element (financial tick/price lookups) |

> ⚠️ These are general trends observed across community-reported interview experiences, not guarantees — always prepare the full pattern space.

### 13.4 Blind 75 / NeetCode Searching-Relevant List

- Binary Search
- Search a 2D Matrix
- Koko Eating Bananas
- Find Minimum in Rotated Sorted Array
- Search in Rotated Sorted Array
- Time Based Key-Value Store (uses binary search on timestamps)
- Median of Two Sorted Arrays

### 13.5 Frequently Asked Interview Questions (Conceptual)

1. **"Walk me through how Binary Search works and prove its time complexity."**
   → Explain halving, recurrence `T(n) = T(n/2) + O(1)`, solve via Master Theorem or direct substitution to get O(log n).
2. **"Why does `mid = lo + (hi-lo)//2` matter over `(lo+hi)//2`?"**
   → Overflow safety in fixed-width-integer languages (Section 12.3/12.4).
3. **"How would you search in a rotated sorted array?"**
   → Explain the "one half is always sorted" invariant (Section 6.7).
4. **"How is Binary Search on Answer different from normal Binary Search?"**
   → No literal array; search over a value range using a monotonic feasibility predicate (Section 6.10).
5. **"What's the difference between `bisect_left` and `bisect_right`?"**
   → Insertion point before vs after existing duplicates (Section 2.4).
6. **"Can Binary Search be applied to a Linked List?"**
   → Technically no in O(log n), because you lack O(1) random access; reaching the "middle" node costs O(n) itself (Section 4.6).
7. **"When would you NOT use Binary Search even on sorted data?"**
   → When you need O(1) amortized lookups with insertions/deletions — a balanced BST or hash-based structure may be more appropriate depending on requirements.

### 13.6 Interview Tricks & Communication Tips

- **State the invariant out loud** before coding: "At every step, the answer — if it exists — lies within `[lo, hi]`."
- **Pick and name your template** (Template 1/2/3) so the interviewer can follow your boundary logic.
- **Always ask about duplicates** in rotated-array problems — it changes both the approach and worst-case complexity.
- **Trace through a tiny example (n=1, n=2)** before submitting — this catches 90% of off-by-one bugs live.
- **Mention time/space complexity proactively**, don't wait to be asked.

---

## 14. Cheat Sheets

### 14.1 Searching Algorithms — Master Complexity Table

| Algorithm | Best | Average | Worst | Space | Requires Sorted? |
|---|---|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) | O(1) | No |
| Sentinel Linear Search | O(1) | O(n) | O(n) | O(1) | No |
| Binary Search (iterative) | O(1) | O(log n) | O(log n) | O(1) | Yes |
| Binary Search (recursive) | O(1) | O(log n) | O(log n) | O(log n) | Yes |
| Jump Search | O(1) | O(√n) | O(√n) | O(1) | Yes |
| Interpolation Search | O(1) | O(log log n)* | O(n) | O(1) | Yes (+uniform dist. for best case) |
| Exponential Search | O(1) | O(log p) | O(log n) | O(1) | Yes |
| Fibonacci Search | O(1) | O(log n) | O(log n) | O(1) | Yes |
| Ternary Search (unimodal) | O(1) | O(log₃ n) | O(log₃ n) | O(1) | Unimodal, not "sorted" |

*\*Average case only under uniformly distributed data.*

### 14.2 Binary Search Templates — Quick Reference

```python
# TEMPLATE 1 — Exact match, closed interval [lo, hi]
lo, hi = 0, n - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: lo = mid + 1
    else: hi = mid - 1
return -1

# TEMPLATE 2 — Leftmost True, half-open [lo, hi)
lo, hi = 0, n
while lo < hi:
    mid = lo + (hi - lo) // 2
    if predicate(mid): hi = mid
    else: lo = mid + 1
return lo

# TEMPLATE 3 — Rightmost True, closed interval [lo, hi]
lo, hi, ans = 0, n - 1, -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if predicate(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
return ans
```

### 14.3 Recognition Cheat Sheet

```
"exists?"              -> Template 1
"first / leftmost"      -> Template 2
"last / rightmost"      -> Template 3
"minimize feasible X"   -> Template 2 on answer-range
"maximize feasible X"   -> Template 3 on answer-range
"rotated array"         -> modified Template 1 (check sorted half)
"peak / valley"         -> slope-based Template 2/3
"unimodal extremum"     -> Ternary Search
```

### 14.4 Python Syntax Cheat Sheet

```python
import bisect

bisect.bisect_left(arr, x)     # insertion point before existing duplicates
bisect.bisect_right(arr, x)    # insertion point after existing duplicates (== bisect(arr, x))
bisect.insort_left(arr, x)     # insert x maintaining sorted order (before duplicates)
bisect.insort_right(arr, x)    # insert x maintaining sorted order (after duplicates)

x in arr                       # O(n) for list, O(1) avg for set
arr.index(x)                   # first index, O(n), raises ValueError if absent
s.find(sub)                    # returns -1 if absent
s.index(sub)                   # raises ValueError if absent

# Python 3.10+ bisect key parameter:
bisect.bisect_left(data, value, key=lambda d: d.field)
```

### 14.5 Decision Tree (Text Form, printable)

```
                         ┌─────────────────────┐
                         │ Is data sorted /     │
                         │ can be sorted?        │
                         └─────┬────────────┬───┘
                             Yes            No
                               │              │
                     ┌─────────┴───────┐    ┌──┴──────────────┐
                     │ Rotated? Matrix? │    │ Monotonic       │
                     │ Duplicates?      │    │ feasibility     │
                     └─────────┬───────┘    │ over a RANGE?    │
                               │              └──┬───────────┬─┘
                    ┌──────────┴─────────┐      Yes          No
                    │ Use the matching    │      │            │
                    │ Binary Search        │  Binary Search   Linear Search
                    │ variant (6.1–6.9)     │  on Answer       (or hash set
                    └──────────────────────┘  (6.10)            if no order needed)
```

---
## 15. Practice Problem Bank

> Links point to the platform's problem search/name where a stable direct link isn't guaranteed to persist — search the exact title on the platform if a link has moved.

### 15.1 Linear Search

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Find the Index of the First Occurrence in a String | LeetCode (28) | Easy | Linear/Two-Way string search | Substring search |
| Linear Search | GeeksforGeeks | Easy | Linear Search | Basics |
| Find Second Largest Element | GeeksforGeeks | Easy | Linear scan | Single-pass tracking |

### 15.2 Binary Search — Core

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Binary Search | LeetCode (704) | Easy | Template 1 | Exact match |
| Sqrt(x) | LeetCode (69) | Easy | Binary Search on Answer | Integer sqrt |
| Search Insert Position | LeetCode (35) | Easy | Template 2 | Lower bound |
| Guess Number Higher or Lower | LeetCode (374) | Easy | Template 1 | Interactive binary search |
| First Bad Version | LeetCode (278) | Easy | Template 2 | Monotonic predicate |

### 15.3 Lower/Upper Bound

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Find First and Last Position of Element in Sorted Array | LeetCode (34) | Medium | Templates 2 & 3 | First/last occurrence |
| Find Smallest Letter Greater Than Target | LeetCode (744) | Easy | Upper bound | Circular upper bound |
| Number of Elements Smaller Than Current Element (sorted variant) | GeeksforGeeks | Easy | lower/upper bound | Counting |
| Count Occurrences in Sorted Array | GeeksforGeeks | Easy | Template 2/3 | First/last difference |

### 15.4 Rotated Array

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Search in Rotated Sorted Array | LeetCode (33) | Medium | Modified Binary Search | Sorted-half detection |
| Search in Rotated Sorted Array II | LeetCode (81) | Medium | Modified BS + duplicates | Shrink-by-one fallback |
| Find Minimum in Rotated Sorted Array | LeetCode (153) | Medium | Modified BS | Pivot finding |
| Find Minimum in Rotated Sorted Array II | LeetCode (154) | Hard | Modified BS + duplicates | Pivot with duplicates |
| Find the Rotation Count | GeeksforGeeks | Medium | Modified BS | Pivot index |

### 15.5 Peak Element

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Find Peak Element | LeetCode (162) | Medium | Slope-based BS | Local maximum |
| Peak Index in a Mountain Array | LeetCode (852) | Medium | Slope-based BS | Mountain array |
| Find in Mountain Array | LeetCode (1095) | Hard | 3-phase BS | Interactive mountain search |

### 15.6 Search on Answer

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Koko Eating Bananas | LeetCode (875) | Medium | BS on Answer | Minimize max speed |
| Capacity To Ship Packages Within D Days | LeetCode (1011) | Medium | BS on Answer | Minimize max capacity |
| Split Array Largest Sum | LeetCode (410) | Hard | BS on Answer | Minimize max subarray sum |
| Allocate Minimum Number of Pages | GeeksforGeeks / Code360 | Hard | BS on Answer | Book allocation |
| Aggressive Cows | Code360 / SPOJ | Hard | BS on Answer (maximize min) | Maximize minimum distance |
| Magnetic Force Between Two Balls | LeetCode (1552) | Medium | BS on Answer | Maximize minimum distance |

### 15.7 Matrix Search

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Search a 2D Matrix | LeetCode (74) | Medium | Flattened BS | Fully sorted matrix |
| Search a 2D Matrix II | LeetCode (240) | Medium | Staircase Search | Row/col sorted matrix |
| Kth Smallest Element in a Sorted Matrix | LeetCode (378) | Medium | BS on Answer + matrix | Count-based feasibility |

### 15.8 Advanced Binary Search

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Median of Two Sorted Arrays | LeetCode (4) | Hard | Partition-based BS | O(log(min(m,n))) median |
| Kth Element of Two Sorted Arrays | GeeksforGeeks / Code360 | Hard | Partition-based BS | Generalized median |
| Find K Closest Elements | LeetCode (658) | Medium | BS + window | Closest-k via boundary search |
| Time Based Key-Value Store | LeetCode (981) | Medium | BS on timestamps | Design + search |
| Russian Doll Envelopes | LeetCode (354) | Hard | BS + LIS | Sort + patience sorting |

### 15.9 Competitive Programming (Codeforces / CodeChef / AtCoder / CSES)

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Factory Machines | CSES | Medium | BS on Answer | Minimize time |
| Array Division | CSES | Medium | BS on Answer | Minimize max partition sum |
| Distributing Candies | Codeforces | Medium | BS on Answer | Feasibility check |
| Codeforces "Buy Low Sell High" adjacent BS problems | Codeforces | Varies | BS variants | Practice searching for boundaries |
| ATC "Snuke's Coloring" style range problems | AtCoder | Hard | BS + prefix sums | Combined pattern |

### 15.10 HackerRank / InterviewBit

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Ice Cream Parlor | HackerRank | Easy | BS / two-pointer | Pair sum on sorted data |
| Binary Search | InterviewBit | Easy | Template 1 | Basics |
| Rotated Sorted Array Search | InterviewBit | Medium | Modified BS | Rotated variant |
| Search for a Range | InterviewBit | Medium | Templates 2/3 | First/last occurrence |
| Sorted Insert Position | InterviewBit | Easy | Template 2 | Lower bound |

---

## 16. Final Revision & Mind Maps

### 16.1 One-Page Notes

```
SEARCHING = repeatedly shrinking a search space using a comparison or predicate.

Unsorted data           -> Linear Search                  O(n)
Sorted, in-memory        -> Binary Search                  O(log n)
Sorted, uniform values   -> Interpolation Search            O(log log n)*
Sorted, unknown size     -> Exponential Search              O(log p)
No division hardware     -> Fibonacci Search                O(log n)
Sequential-cheap storage -> Jump Search                     O(√n)
Rotated sorted array     -> Modified Binary Search           O(log n)
Matrix (fully sorted)    -> Flattened Binary Search           O(log(r·c))
Matrix (row/col sorted)  -> Staircase Search                  O(r+c)
No array, feasibility    -> Binary Search on Answer            O(log(range) · check_cost)
Unimodal extremum        -> Ternary Search / slope-based BS     O(log n)
```

### 16.2 Mind Map (Text Form)

```
                         SEARCHING
                            │
    ┌───────────────┬───────┴────────┬────────────────┐
    │                │                │                │
LINEAR FAMILY   BINARY SEARCH     SPECIALIZED       ON ANSWER
    │             FAMILY           VARIANTS             │
Linear Search       │               │              Binary Search
Sentinel Search   Template 1    Jump Search         on Answer
                  Template 2    Interpolation      (Koko, Ship
                  Template 3    Exponential         Packages,
                     │          Fibonacci           Split Array,
              ┌──────┴─────┐   Ternary             Aggressive Cows)
         First/Last    Rotated
         Occurrence    Array Search
         Lower/Upper   Peak Element
         Bound         Matrix Search
         Floor/Ceiling
```

### 16.3 Binary Search Templates — Final Memorization Block

```python
# EXISTENCE           # LEFTMOST TRUE         # RIGHTMOST TRUE
lo,hi=0,n-1            lo,hi=0,n                lo,hi,ans=0,n-1,-1
while lo<=hi:          while lo<hi:             while lo<=hi:
  mid=lo+(hi-lo)//2      mid=lo+(hi-lo)//2         mid=lo+(hi-lo)//2
  if arr[mid]==t:          if pred(mid):             if pred(mid):
    return mid                hi=mid                    ans=mid; lo=mid+1
  elif arr[mid]<t:         else: lo=mid+1            else: hi=mid-1
    lo=mid+1              return lo                 return ans
  else: hi=mid-1
return -1
```

### 16.4 Complexity Sheet (Compact)

```
Linear:            O(n)
Binary:             O(log n)
Jump:               O(√n)
Interpolation:      O(log log n) avg / O(n) worst
Exponential:        O(log p)
Fibonacci:          O(log n)
Ternary:            O(log₃ n) ≈ O(log n)
```

### 16.5 Recognition Guide (Compact)

```
exists?          -> Template 1
first?           -> Template 2
last?            -> Template 3
minimize X?      -> Template 2 on answer range
maximize X?      -> Template 3 on answer range
rotated?         -> check sorted half at each step
peak/valley?     -> compare slope, not value
```

### 16.6 15-Minute Revision Plan

1. (3 min) Re-read Section 4 & 5 — Binary Search core + 3 templates.
2. (4 min) Skim Section 6.1–6.5 — first/last, lower/upper bound, floor/ceiling.
3. (4 min) Skim Section 6.7 & 6.10 — Rotated Array + Binary Search on Answer (highest interview ROI).
4. (2 min) Scan Section 12 — Common Mistakes checklist.
5. (2 min) Recite the 3 templates from memory (Section 16.3) without looking.

### 16.7 1-Hour Deep Revision Plan

1. (10 min) Re-derive Binary Search from scratch, including recursive + iterative, and explain time complexity via recurrence.
2. (10 min) Re-implement (from memory) find_first_occurrence, find_last_occurrence, lower_bound, upper_bound.
3. (10 min) Re-implement search_rotated (with and without duplicates) and explain the "sorted half" invariant out loud.
4. (10 min) Solve one Binary-Search-on-Answer problem end-to-end (e.g., Koko Eating Bananas) without looking at the solution, then compare.
5. (10 min) Solve Search a 2D Matrix I and II back-to-back, explicitly contrasting the two approaches (flattened vs staircase).
6. (10 min) Review Section 7 (Jump/Interpolation/Exponential/Fibonacci/Ternary) at a conceptual level — you're unlikely to implement these live, but you must be able to describe when/why to use each.

---

## 17. FAQs

**Q1. Is Binary Search always O(log n)?**
A. Only when each step provably discards a constant fraction (typically half) of the remaining search space AND accessing the midpoint is O(1). If access is not O(1) (e.g., linked list) or the discard fraction isn't guaranteed, the complexity changes.

**Q2. Why do we write `mid = lo + (hi - lo) // 2` instead of `(lo + hi) // 2`?**
A. To avoid integer overflow in languages with fixed-width integers (C/C++/Java). Python doesn't have this issue, but writing it the safe way is expected interview practice (Section 12.3).

**Q3. Can Binary Search work on unsorted data?**
A. No — Binary Search fundamentally relies on being able to discard a half based on a comparison, which is only valid if there's a monotonic ordering (sorted values or a monotonic predicate).

**Q4. What's the real difference between `bisect_left` and `bisect_right`?**
A. `bisect_left` returns the position **before** any existing equal elements; `bisect_right` returns the position **after** them. Both are O(log n) via binary search under the hood (Section 2.4).

**Q5. When should I prefer `bisect` over writing my own binary search?**
A. Whenever you're doing a standard boundary search (lower/upper bound) on a plain sorted sequence of comparable values. Write your own only when you need a custom predicate the `bisect` module can't express directly (pre-3.10) or complex multi-field logic.

**Q6. Is Ternary Search ever better than Binary Search for searching a sorted array?**
A. No. For target-lookup in a sorted array, Binary Search is strictly better (fewer comparisons per step, same O(log n) class). Ternary Search's true purpose is optimizing (finding the extremum of) a unimodal function — a different problem class entirely.

**Q7. Why does Interpolation Search sometimes perform worse than Binary Search?**
A. If the data isn't roughly uniformly distributed (e.g., highly skewed/exponential values), the interpolation formula's position estimate can be very wrong, degrading to O(n) in the worst case (Section 7.2).

**Q8. How do I know if a "Binary Search on Answer" applies?**
A. Ask: "If I fix a candidate value X, can I check feasibility in a way that's monotonic (works for all X above/below a threshold)?" If yes, binary search the threshold (Section 6.10, Section 10.3).

**Q9. What's the hardest part of Rotated Array Search?**
A. Correctly identifying **which half is sorted** at each step, and handling duplicates that break that identification (Section 6.7, 6.7.1).

**Q10. Do I need to memorize all 3 Binary Search templates, or just one?**
A. Memorize Template 2 (leftmost-True, half-open) deeply — it can express Template 1 and Template 3's use cases too with the right predicate. But knowing all three fluently makes code cleaner and communicates strong fundamentals.

**Q11. Is recursion or iteration preferred for Binary Search in interviews?**
A. Iterative is generally preferred (O(1) space, no stack-overflow risk), but recursive is perfectly acceptable if you can justify the trade-off when asked.

**Q12. What is the single highest-leverage topic to master in this handbook for FAANG interviews?**
A. **Binary Search on Answer** (Section 6.10) and the **Leftmost/Rightmost True template** (Section 5.2/5.3) — together they solve a disproportionate share of "hard" Binary-Search-tagged interview problems.

---

