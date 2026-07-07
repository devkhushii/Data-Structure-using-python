# 🧮 THE COMPLETE PREFIX SUM HANDBOOK (Python Edition)



## 📑 Table of Contents

1. [Introduction to Prefix Sum](#1-introduction-to-prefix-sum)
2. [Python Implementation Foundations](#2-python-implementation-foundations)
3. [Prefix Sum Fundamentals](#3-prefix-sum-fundamentals)
4. [Types of Prefix Sum](#4-types-of-prefix-sum)
5. [Prefix Sum Patterns](#5-prefix-sum-patterns)
6. [Difference Array](#6-difference-array)
7. [2D Prefix Sum](#7-2d-prefix-sum)
8. [Real-World Applications](#8-real-world-applications)
9. [Problem Recognition](#9-problem-recognition)
10. [Optimization Strategies](#10-optimization-strategies)
11. [Interview Preparation](#11-interview-preparation)
12. [Python Tips & Idioms](#12-python-tips--idioms)
13. [Common Mistakes](#13-common-mistakes)
14. [Cheat Sheets](#14-cheat-sheets)
15. [Practice Problem Bank](#15-practice-problem-bank)
16. [Final Revision Kit](#16-final-revision-kit)
17. [FAQs](#17-faqs)

---

## 1. Introduction to Prefix Sum

### 1.1 What Is Prefix Sum?

**Definition:** A **Prefix Sum** (also called a *cumulative sum* or *running sum*) is a derived array where each element at index `i` stores the sum of all elements of the original array from index `0` to `i`.

Formally, given an array `arr[0..n-1]`, the prefix sum array `prefix[0..n-1]` is defined as:

```
prefix[i] = arr[0] + arr[1] + ... + arr[i]  =  Σ arr[j] for j = 0 to i
```

### 1.2 Why Does Prefix Sum Exist?

**The core problem it solves:** Answering repeated *range sum queries* efficiently.

| Approach | Preprocessing | Per Query | Total for Q queries |
|---|---|---|---|
| Brute Force (loop every query) | O(1) | O(n) | O(n·Q) |
| Prefix Sum | O(n) | O(1) | O(n + Q) |

When `Q` is large (thousands of queries on the same array), recomputing sums from scratch every time is wasteful. Prefix Sum trades a **one-time O(n) preprocessing cost** for **O(1) query answering** — one of the most fundamental time-space tradeoffs in computer science.

> **💡 Intuition (Real-World Analogy):**
> Think of a **bank account ledger**. Instead of re-adding every single transaction from account-opening day every time you want to know your balance on a given date, the bank keeps a **running balance** after every transaction. To know your balance change between two dates, you just subtract two running-balance entries — you never re-sum the entire history.
>
> Another analogy: **odometer readings** in a car. If you note the odometer reading at the start of a trip and at the end, the distance traveled is just `end - start` — you don't need to track every meter driven in between.

### 1.3 History & Origin

The concept of cumulative sums predates computer science — it appears in numerical analysis, statistics (Cumulative Distribution Functions), and integral calculus (a discrete analogue of `∫f(x)dx`, where prefix sum is the discrete integral and the array itself is the discrete derivative). In competitive programming, it became a canonical "first optimization trick" taught right after arrays, because it demonstrates the *preprocess-once, query-fast* paradigm that recurs in Segment Trees, Fenwick Trees, Sparse Tables, and DP.

### 1.4 Running Sum vs Cumulative Sum vs Prefix Sum

These three terms are **used interchangeably** in most contexts:

| Term | Common Usage Context |
|---|---|
| Running Sum | Streaming/online contexts (LeetCode "Running Sum of 1d Array") |
| Cumulative Sum | Statistics, NumPy (`cumsum`), Data Science |
| Prefix Sum | Competitive Programming, DSA interviews |

All three refer to the exact same mathematical construction.

### 1.5 Characteristics of Prefix Sum

- **Monotonic Growth Pattern:** If all elements are non-negative, `prefix[]` is non-decreasing.
- **Deterministic:** Given the same array, the prefix array is always identical.
- **Linear Space:** Requires O(n) extra space (can sometimes be done in-place).
- **Composable:** Prefix sum arrays can be combined with hashing, binary search, and difference arrays to solve a huge family of problems.

### 1.6 Advantages

✅ Reduces range-sum queries from O(n) to O(1)
✅ Simple to implement — a handful of lines
✅ Extends naturally to 2D, XOR, product, and other operations
✅ Forms the basis for more advanced structures (Fenwick Tree is essentially a "dynamic prefix sum")

### 1.7 Disadvantages

⚠️ Requires O(n) extra memory
⚠️ **Static by default** — if the underlying array changes (a point update), the entire prefix array from that point onward must be rebuilt (O(n) per update) unless you use a Fenwick/Segment Tree instead
⚠️ Not suitable when updates and queries are interleaved frequently (use Fenwick Tree / Segment Tree instead)
⚠️ Susceptible to integer overflow in fixed-width-integer languages (not a concern in Python, discussed later for contrast)

### 1.8 Applications At a Glance

- Range sum / range average queries
- Subarray sum problems (`Subarray Sum Equals K`, etc.)
- Difference arrays for range updates
- 2D matrix region sum queries (image processing, heatmaps)
- Histogram and frequency analysis
- Financial time-series analysis (moving cumulative balance)
- Probability: Cumulative Distribution Functions
- Competitive programming staple in Codeforces/CSES/LeetCode

### 1.9 ASCII Visualization — The Core Idea

```
Original Array (arr):
Index :   0    1    2    3    4
Value :  [2] [4] [1] [5] [3]

Prefix Sum Array (prefix), inclusive:
Index :   0    1    2    3    4
Value :  [2] [6] [7] [12] [15]
           |    |    |    |     |
           2   2+4  6+1  7+5  12+3
```

Querying the sum of `arr[1..3]` (indices 1 to 3 inclusive = 4+1+5=10):

```
prefix[3] - prefix[0] = 12 - 2 = 10   ✅
```

> **📝 Note:** This works because `prefix[3]` = sum(0..3) and `prefix[0]` = sum(0..0). Subtracting removes the unwanted `arr[0]` portion, leaving exactly `arr[1]+arr[2]+arr[3]`.

---

## 2. Python Implementation Foundations

### 2.1 Inclusive vs Exclusive Prefix Sum

There are **two conventions**. Confusing them is the #1 source of off-by-one bugs.

```
Original:        arr    = [2, 4, 1, 5, 3]

Inclusive prefix: prefix[i] = sum(arr[0..i])
                   prefix = [2, 6, 7, 12, 15]     (len == n)

Exclusive prefix: prefix[i] = sum(arr[0..i-1])
                   prefix = [0, 2, 6, 7, 12, 15]  (len == n+1)
```

```
INCLUSIVE                          EXCLUSIVE
┌───┬───┬───┬────┬────┐            ┌───┬───┬───┬───┬────┬────┐
│ 2 │ 6 │ 7 │ 12 │ 15 │            │ 0 │ 2 │ 6 │ 7 │ 12 │ 15 │
└───┴───┴───┴────┴────┘            └───┴───┴───┴───┴────┴────┘
  0   1   2   3    4                 0   1   2   3   4    5
prefix[i] = sum(0..i)               prefix[i] = sum(0..i-1)
```

> **⚠️ Warning:** Most production-quality solutions use the **exclusive/padded** convention (`prefix` has length `n+1`, `prefix[0] = 0`) because it makes the range-sum formula uniform for **all** ranges, including ranges starting at index 0, without special-casing.

### 2.2 The Universal Range Query Formula

Using the **exclusive/padded** convention (`prefix[0] = 0`, length `n+1`):

```
sum(arr[l..r]) = prefix[r+1] - prefix[l]        (0-indexed, inclusive l and r)
```

Using the **inclusive** convention (length `n`):

```
sum(arr[l..r]) = prefix[r] - prefix[l-1]   if l > 0
sum(arr[l..r]) = prefix[r]                 if l == 0
```

> **💡 Tip:** The padded/exclusive convention is preferred in interviews because it eliminates the `if l == 0` special case entirely. This is considered the "clean" industry-standard template.

### 2.3 Manual Prefix Construction (Exclusive/Padded — Recommended Template)

**Problem Statement:** Given an array of `n` integers, build a prefix sum structure and answer `sum(arr[l..r])` for multiple `(l, r)` queries in O(1) each.

**Approach:** Build a padded prefix array of size `n+1` where `prefix[0] = 0`, then `prefix[i] = prefix[i-1] + arr[i-1]`.

```python
def build_prefix_sum(arr: list[int]) -> list[int]:
    """
    Builds an exclusive/padded prefix sum array.
    prefix[i] represents sum(arr[0..i-1])
    len(prefix) == len(arr) + 1
    """
    n = len(arr)
    prefix = [0] * (n + 1)          # prefix[0] is always 0 (sum of empty prefix)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
    return prefix


def range_sum(prefix: list[int], l: int, r: int) -> int:
    """Returns sum(arr[l..r]) inclusive, 0-indexed, using padded prefix array."""
    return prefix[r + 1] - prefix[l]
```

**Line-by-Line Explanation:**

| Line | Explanation |
|---|---|
| `n = len(arr)` | Store array length for reuse |
| `prefix = [0] * (n + 1)` | Allocate padded array; `prefix[0]=0` represents "sum of nothing" |
| `for i in range(1, n + 1)` | Iterate 1-indexed over the padded array |
| `prefix[i] = prefix[i-1] + arr[i-1]` | Add the *previous* running total to the *current* original element (note the `-1` shift because `prefix` is 1 longer than `arr`) |
| `return prefix[r+1] - prefix[l]` | Apply the universal formula — subtract the sum "before `l`" from the sum "up to and including `r`" |

**Complete Dry Run:**

`arr = [2, 4, 1, 5, 3]`, query `range_sum(prefix, 1, 3)`

| Step | i | arr[i-1] | prefix[i-1] | prefix[i] (computed) |
|---|---|---|---|---|
| Init | - | - | - | prefix[0] = 0 |
| 1 | 1 | arr[0]=2 | 0 | prefix[1] = 0+2 = 2 |
| 2 | 2 | arr[1]=4 | 2 | prefix[2] = 2+4 = 6 |
| 3 | 3 | arr[2]=1 | 6 | prefix[3] = 6+1 = 7 |
| 4 | 4 | arr[3]=5 | 7 | prefix[4] = 7+5 = 12 |
| 5 | 5 | arr[4]=3 | 12 | prefix[5] = 12+3 = 15 |

Final `prefix = [0, 2, 6, 7, 12, 15]`

Query `range_sum(prefix, l=1, r=3)`:
```
prefix[r+1] - prefix[l]  =  prefix[4] - prefix[1]  =  12 - 2  =  10
```
Verify manually: `arr[1]+arr[2]+arr[3] = 4+1+5 = 10` ✅

**Time & Space Complexity:**

| Operation | Time | Space |
|---|---|---|
| Build | O(n) | O(n) |
| Query | O(1) | O(1) |
| Q queries | O(n + Q) | O(n) |

**Edge Cases:**
- Empty array (`n=0`) → `prefix = [0]`, no valid queries possible
- Single element array → `prefix = [0, arr[0]]`
- `l == r` (single-element range) → still works correctly
- `l == 0` → `prefix[l] = prefix[0] = 0`, formula degenerates correctly to `prefix[r+1]`
- Negative numbers in `arr` → works fine, prefix sum is not required to be monotonic
- Query with `l > r` → invalid input, should be validated/guarded against

**Common Mistakes:**
- ❌ Forgetting the `+1` padding, causing an off-by-one on every query
- ❌ Using `prefix[r] - prefix[l-1]` formula with a *padded* array (mixing conventions)
- ❌ Not initializing `prefix[0] = 0` explicitly (though Python's `[0]*(n+1)` handles this)

**Interview Tip:** Always state out loud *which convention* you're using (inclusive vs exclusive) before writing code — interviewers explicitly watch for this because it signals structured thinking rather than pattern memorization.

### 2.4 `itertools.accumulate` — The Pythonic Way

Python's standard library provides `itertools.accumulate`, which builds an **inclusive** prefix sum in a single, highly optimized C-level call.

```python
from itertools import accumulate

arr = [2, 4, 1, 5, 3]
prefix_inclusive = list(accumulate(arr))
print(prefix_inclusive)   # [2, 6, 7, 12, 15]

# To get the padded/exclusive form used in the universal formula:
prefix_padded = [0] + prefix_inclusive
print(prefix_padded)      # [0, 2, 6, 7, 12, 15]
```

`accumulate` also accepts a custom binary function — this is the gateway to Prefix XOR, Prefix Product, Prefix Max/Min (covered in Section 4):

```python
import operator
from itertools import accumulate

arr = [2, 4, 1, 5, 3]

prefix_sum_    = list(accumulate(arr, operator.add))       # default op is add
prefix_xor     = list(accumulate(arr, operator.xor))
prefix_product = list(accumulate(arr, operator.mul))
prefix_max     = list(accumulate(arr, max))
prefix_min     = list(accumulate(arr, min))

print(prefix_sum_)      # [2, 6, 7, 12, 15]
print(prefix_xor)       # [2, 6, 7, 2, 1]
print(prefix_product)   # [2, 8, 8, 40, 120]
print(prefix_max)       # [2, 4, 4, 5, 5]
print(prefix_min)       # [2, 2, 1, 1, 1]
```

`accumulate` also supports an `initial` keyword (Python 3.8+) which directly produces the **padded** form without manual concatenation:

```python
prefix_padded = list(accumulate(arr, initial=0))
print(prefix_padded)    # [0, 2, 6, 7, 12, 15]
```

> **💡 Tip:** `accumulate(arr, initial=0)` is the single most idiomatic, interview-safe, production-safe way to build a padded prefix sum array in Python. Mention it — it shows fluency beyond textbook loops.

### 2.5 Manual Loop vs List Comprehension vs `accumulate` — Performance Comparison

```python
import timeit
from itertools import accumulate

arr = list(range(1_000_000))

def manual_loop(a):
    n = len(a)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]
    return prefix

def using_accumulate(a):
    return list(accumulate(a, initial=0))

# Representative timing (values vary by machine):
# manual_loop        ~ 120 ms   (pure Python bytecode loop)
# using_accumulate   ~ 25 ms    (C-implemented, ~5x faster)
```

| Method | Speed | Readability | Recommended Use |
|---|---|---|---|
| Manual `for` loop | Slowest | Good for teaching | Interviews (to show understanding) |
| List comprehension* | N/A (can't easily express recurrence) | — | Not naturally applicable — prefix sum is inherently *stateful* |
| `itertools.accumulate` | Fastest (C-level) | Excellent | Production Python code |

> **📝 Note:** A plain list comprehension *cannot* elegantly express prefix sum because each element depends on the previous computed result — this is a classic case where comprehensions are the wrong tool, and beginners often try (and fail) to force one. `accumulate` exists precisely to fill this pythonic gap.

### 2.6 Memory Considerations

- A prefix array occupies **O(n) additional space** — for very large arrays (10^8+), this can matter.
- **In-place variant:** If the original array can be mutated and doesn't need to be preserved, you can build the prefix sum *in-place*, saving O(n) space:

```python
def build_prefix_inplace(arr: list[int]) -> None:
    """Mutates arr into its own inclusive prefix sum. O(1) extra space."""
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

arr = [2, 4, 1, 5, 3]
build_prefix_inplace(arr)
print(arr)   # [2, 6, 7, 12, 15]
```

⚠️ **Trade-off:** This destroys the original array — only use when the original values are no longer needed.

### 2.7 Best Practices Checklist

- ✅ Prefer `itertools.accumulate(arr, initial=0)` for the padded form in production
- ✅ Always document which convention (inclusive/exclusive) your function uses
- ✅ Validate `0 <= l <= r < n` before querying
- ✅ For frequent *updates* interleaved with queries, do NOT use static prefix sum — use a Fenwick Tree/Segment Tree instead
- ✅ For 64-bit-overflow-prone languages this matters; in Python, integers are arbitrary precision, so **overflow is a non-issue** (see Section 13.6)

---

## 3. Prefix Sum Fundamentals

### 3.1 The Recurrence Relation

Every prefix sum, regardless of convention, follows one universal recurrence:

```
prefix[i] = prefix[i-1] + arr[i]        (inclusive convention)
prefix[i] = prefix[i-1] + arr[i-1]      (exclusive/padded convention)
```

This is a **first-order linear recurrence** — each term depends only on the immediately preceding term plus one new input. This is why it can be computed in a single O(n) left-to-right pass, and why `functools.reduce` / `itertools.accumulate` are natural fits (they are designed exactly for such recurrences).

### 3.2 Zero-Based vs One-Based Prefix Arrays

```
Zero-based inclusive (len n):        Zero-based padded/exclusive (len n+1):
prefix[0] = arr[0]                   prefix[0] = 0
prefix[i] = prefix[i-1] + arr[i]     prefix[i] = prefix[i-1] + arr[i-1]
```

Competitive programmers coming from 1-indexed languages sometimes use a **1-based array** (`arr[1..n]`, `arr[0]` unused) — Python rarely needs this since Python lists are always 0-indexed, but you may see it in translated C++ solutions. **Recommendation: stick to the padded (exclusive) 0-based convention in Python — it's the cleanest.**

### 3.3 Prefix Initialization Rules

| Convention | `prefix[0]` value | Array length |
|---|---|---|
| Inclusive | `arr[0]` | `n` |
| Exclusive / Padded | `0` | `n + 1` |

> **⚠️ Warning:** The single most common bug in prefix sum code is initializing `prefix[0]` incorrectly for the chosen convention. If using padded/exclusive, `prefix[0]` **must** be `0`, representing "sum of an empty range," **not** `arr[0]`.

### 3.4 Building Intuition With a Physical Model

```
arr:        [ 2 ][ 4 ][ 1 ][ 5 ][ 3 ]
             ▼    ▼    ▼    ▼    ▼
Cumulative
water level  ██   ██   █    ██   ██
tank:        ██   ████ ████ ██████ ████████
             2    6    7    12    15
```

Think of pouring each `arr[i]` value into a tank one after another — the water level after pouring the i-th cup is exactly `prefix[i]`. This "water level" mental model helps beginners internalize *why* prefix sum is monotonically increasing when all values are non-negative.

### 3.5 Prefix Sum as Discrete Integration

For readers with a calculus background: if `arr` is viewed as a discrete function `f(i)`, then:

- `arr` (the original array) is analogous to the **derivative** `f'(x)`
- `prefix` (the prefix sum array) is analogous to the **integral** `F(x) = ∫f(x)dx`
- The **difference array** (Section 6) is the discrete second derivative

This is why `sum(arr[l..r]) = prefix[r] - prefix[l-1]` mirrors the Fundamental Theorem of Calculus: `∫[a,b] f(x)dx = F(b) - F(a)`.

---

## 4. Types of Prefix Sum

### 4.1 Overview Table

| Type | Operation | Combine Function | Inverse Operation for Query |
|---|---|---|---|
| Prefix Sum | `+` | `add` | Subtraction |
| Prefix XOR | `^` | `xor` | XOR (self-inverse) |
| Prefix Product | `×` | `mul` | Division (careful with 0) |
| Prefix Min/Max | `min`/`max` | — | **Not invertible** (no query formula) |
| Prefix Count | count matches | `add` on boolean/indicator | Subtraction |
| Prefix Frequency | per-value running counts | `add` per key | Subtraction |
| Prefix Modulo | `(prefix[i-1]+arr[i]) % m` | `add` then `mod` | Modular subtraction |
| Prefix Parity | running `count % 2` | `xor` with 1 | XOR |

> **💡 Key Insight:** A range query using the "subtract two prefixes" trick is only valid when the underlying operation has a **well-defined inverse** relative to how ranges combine. Sum and XOR both qualify — Min and Max do **not** (this is precisely why Sparse Tables / Segment Trees exist for range-min/max queries, not simple prefix arrays).

### 4.2 1D Prefix Sum — Recap

Already covered fully in Section 2.3. This is the base case for everything else.

### 4.3 Prefix XOR

**Definition:** `prefixXor[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]`

**Why it exists:** XOR has the special property that `x ^ x = 0`. This means `prefixXor[r] ^ prefixXor[l-1] = arr[l] ^ ... ^ arr[r]` — an O(1) range-XOR query, exactly mirroring the sum formula but with XOR instead of subtraction.

```python
from itertools import accumulate
import operator

def build_prefix_xor(arr: list[int]) -> list[int]:
    """Padded prefix XOR array. prefix[i] = XOR of arr[0..i-1]."""
    return list(accumulate(arr, operator.xor, initial=0))

def range_xor(prefix_xor: list[int], l: int, r: int) -> int:
    """XOR of arr[l..r] inclusive, 0-indexed."""
    return prefix_xor[r + 1] ^ prefix_xor[l]
```

**ASCII Visualization:**

```
arr           :  [5]  [3]  [7]  [2]  [6]
binary        : 101  011  111  010  110

prefixXor     :  0    5    6    1    3    5
index         :  0    1    2    3    4    5
                       ↑ cumulative XOR (not sum!)
```

**Dry Run:** `arr = [5,3,7,2,6]`, query `range_xor(prefixXor, 1, 3)` → should equal `3^7^2 = 6`

| i | arr[i-1] | prefixXor[i-1] | prefixXor[i] |
|---|---|---|---|
| 1 | 5 | 0 | 0^5 = 5 |
| 2 | 3 | 5 | 5^3 = 6 |
| 3 | 7 | 6 | 6^7 = 1 |
| 4 | 2 | 1 | 1^2 = 3 |
| 5 | 6 | 3 | 3^6 = 5 |

`prefixXor = [0,5,6,1,3,5]`. Query: `prefixXor[4] ^ prefixXor[1] = 3 ^ 5 = 6` ✅ (matches `3^7^2=6`)

**Real-World / Interview Use:** "Find XOR of subarray," "Single Number" variants, bitmask DP with subarrays, and cryptographic checksum-style problems.

**Common Mistakes:** Using subtraction instead of XOR for the query (XOR is its own inverse, not additive inverse); forgetting that `x ^ x = 0` is the entire reason this trick works.

### 4.4 Prefix Product

**Definition:** `prefixProduct[i] = arr[0] × arr[1] × ... × arr[i]`

```python
from itertools import accumulate
import operator

def build_prefix_product(arr: list[int]) -> list[int]:
    return list(accumulate(arr, operator.mul, initial=1))   # identity for product is 1

def range_product(prefix_product: list[int], l: int, r: int) -> float:
    """Product of arr[l..r]. WARNING: breaks if any arr[i] == 0."""
    return prefix_product[r + 1] / prefix_product[l]
```

> **⚠️ Warning:** Division-based range product queries **fail catastrophically** if any element in `arr[0..l-1]` is `0` (division by zero) or if any element in the query range is `0` combined with floating point precision. **LeetCode 152 "Maximum Product Subarray"** is deliberately designed so plain prefix product doesn't work cleanly — it requires tracking running max/min because of sign flips and zeros. This is a classic **trap** interviewers use to test if candidates blindly apply prefix sum patterns without considering operation properties.

**When NOT to use prefix product:** whenever zeros or negative numbers make the "divide to undo" trick unreliable — segment-restart approaches or DP are safer.

### 4.5 Prefix Count

**Definition:** A running count of elements satisfying some condition (e.g., prefix count of even numbers, prefix count of a target character).

```python
def build_prefix_count(arr: list[int], condition) -> list[int]:
    """
    prefix[i] = number of elements in arr[0..i-1] satisfying condition(x)
    """
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + (1 if condition(arr[i - 1]) else 0)
    return prefix

# Example: prefix count of even numbers
arr = [2, 3, 4, 5, 6]
prefix_even = build_prefix_count(arr, lambda x: x % 2 == 0)
print(prefix_even)  # [0, 1, 1, 2, 2, 3]
```

**Use case:** "Count how many even numbers exist between index l and r" → `range_sum(prefix_even, l, r)` using the exact same universal formula from Section 2.2. This demonstrates that **Prefix Sum is really a general-purpose technique for any additive, invertible aggregate**, not just literal sums.

### 4.6 Prefix Minimum / Maximum

```python
from itertools import accumulate

arr = [5, 2, 8, 1, 9]
prefix_min = list(accumulate(arr, min))   # [5, 2, 2, 1, 1]
prefix_max = list(accumulate(arr, max))   # [5, 5, 8, 8, 9]
```

> **⚠️ Critical Limitation:** Unlike sum/XOR, **you cannot query an arbitrary range min/max using only two prefix values.** `prefix_min` only tells you the minimum from index `0` to `i` — it says *nothing* about the minimum of an arbitrary sub-range `[l, r]` where `l > 0`. For arbitrary range min/max queries, you need a **Sparse Table** (O(1) query, immutable) or **Segment Tree** (O(log n) query, mutable) — both outside the scope of this handbook, mentioned here only to draw the boundary of what prefix sum *cannot* do.

### 4.7 Prefix Frequency (Multi-Key)

Used when tracking running counts of **multiple distinct values** simultaneously — typically via `Counter` or `defaultdict`.

```python
from collections import defaultdict

def build_prefix_frequency(arr: list[int]) -> list[dict]:
    """
    prefix_freq[i] = dict mapping value -> count of occurrences in arr[0..i-1]
    NOTE: For real problems, avoid materializing all n dicts (O(n*k) space) —
    this is shown for teaching purposes only. See 4.7.1 for the practical pattern.
    """
    n = len(arr)
    prefix_freq = [defaultdict(int)]
    for i in range(1, n + 1):
        new_freq = defaultdict(int, prefix_freq[i - 1])
        new_freq[arr[i - 1]] += 1
        prefix_freq.append(new_freq)
    return prefix_freq
```

#### 4.7.1 The Practical Pattern: Single Running Dict (Not an Array of Dicts)

In real interview problems, you almost never store `n` separate dictionaries (too much memory). Instead, you maintain **one running dictionary** and query it at the moment you need it — this is the seed of the **Prefix Sum + Hash Map pattern** (fully covered in Section 5.4).

```python
from collections import defaultdict

def count_of_value_in_range(arr, l, r, target):
    """Simple O(r-l) version for contrast — the hash map pattern in Sec 5.4 makes this O(1)."""
    return sum(1 for x in arr[l:r+1] if x == target)
```

### 4.8 Prefix Modulo

**Definition:** `prefix[i] = (prefix[i-1] + arr[i-1]) % m`

Used in problems where sums can be astronomically large (irrelevant in Python due to bignums) but the problem **explicitly asks for an answer mod m** (common in Codeforces/CSES for combinatorics-heavy problems), or where you need `prefix[i] % k == prefix[j] % k` type groupings (see **Subarray Sums Divisible by K**, Section 5.7).

```python
def build_prefix_mod(arr: list[int], m: int) -> list[int]:
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = (prefix[i - 1] + arr[i - 1]) % m
    return prefix
```

> **⚠️ Warning:** When subtracting two modded prefix values for a range query, you must re-mod and handle negative results: `((prefix[r+1] - prefix[l]) % m + m) % m` — Python's `%` operator actually already returns non-negative results for positive `m` (unlike C++/Java), but it's good practice to write it explicitly for portability and clarity.

### 4.9 Prefix Parity

A specialized case of prefix count/modulo: tracking whether the running count of some event is odd or even, often implemented as `running_xor_with_1` or `count % 2`.

```python
def build_prefix_parity(arr: list[int], condition) -> list[int]:
    """Tracks whether count of condition-matches so far is even (0) or odd (1)."""
    n = len(arr)
    parity = [0] * (n + 1)
    for i in range(1, n + 1):
        flip = 1 if condition(arr[i - 1]) else 0
        parity[i] = parity[i - 1] ^ flip
    return parity
```

**Use case example:** "Equal 0s and 1s" style problems (Section 5.6) and toggling-state problems.

### 4.10 Comparison Cheat Table

| Type | Query Formula | Invertible? | Common Problems |
|---|---|---|---|
| Sum | `prefix[r+1]-prefix[l]` | ✅ | Range Sum Query, Subarray Sum = K |
| XOR | `prefix[r+1]^prefix[l]` | ✅ | XOR Queries of a Subarray |
| Product | `prefix[r+1]/prefix[l]` | ⚠️ risky | Product of Array Except Self (variant) |
| Min/Max | ❌ no O(1) formula | ❌ | Needs Sparse Table / Segment Tree |
| Count | `prefix[r+1]-prefix[l]` | ✅ | Count elements/chars in range |
| Modulo | needs re-mod | ✅ (careful) | Subarray Sums Divisible by K |
| Parity | `prefix[r+1]^prefix[l]` | ✅ | Equal 0s/1s, toggle-state problems |

---

## 5. Prefix Sum Patterns

### 5.1 Range Sum Query (Immutable Array)

**Problem Statement (LeetCode 303):** Given an integer array `nums`, handle multiple queries of the type: calculate the sum of elements between indices `left` and `right` inclusive.

**Approach:** Precompute a padded prefix sum once; answer each query in O(1).

```python
class NumArray:
    def __init__(self, nums: list[int]):
        from itertools import accumulate
        self.prefix = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Dry run
na = NumArray([-2, 0, 3, -5, 2, -1])
print(na.sumRange(0, 2))   # -2+0+3 = 1
print(na.sumRange(2, 5))   # 3-5+2-1 = -1
print(na.sumRange(0, 5))   # sum of all = -3
```

**Complexity:** Build O(n), Query O(1), Space O(n).

**Alternative Approaches:**
- Brute force recompute per query: O(n) per query — too slow for many queries.
- Segment Tree: O(log n) per query, O(n) build — overkill here since the array is **immutable** (no updates); use only if updates are also required (→ see LeetCode 307, "Range Sum Query - Mutable," which explicitly requires a Fenwick Tree/Segment Tree instead).

**When to use:** Static array + many range-sum queries.
**When NOT to use:** Array with frequent point updates interleaved with queries (use Fenwick Tree).

### 5.2 Range Average Query

Trivial extension: `average(l, r) = sum(l, r) / (r - l + 1)`. Same prefix array, just divide by range length at query time. No separate structure needed — included here only because it appears verbatim in interview question banks.

### 5.3 Subarray Sum Equals K (Prefix Sum + Hash Map) — THE Canonical Pattern

**Problem Statement (LeetCode 560):** Given an array of integers `nums` and an integer `k`, return the **total number of subarrays** whose sum equals `k`.

**Why Brute Force Fails at Scale:** Checking every `(l, r)` pair and summing is O(n²) (or O(n³) if you resum each range naively). For `n` up to 2×10⁴+, this can time out.

**The Key Insight:** `sum(arr[l..r]) = prefix[r] - prefix[l-1] = k`  ⟺  `prefix[l-1] = prefix[r] - k`

So for every index `r`, we need to know: **how many earlier prefix values equal `prefix[r] - k`?** This is exactly what a hash map (dict) can answer in O(1) — turning an O(n²) brute force into an **O(n)** single pass.

```
For each r, count += frequency_map.get(prefix[r] - k, 0)
Then register prefix[r] itself into frequency_map for future r's.
```

**Python Implementation:**

```python
from collections import defaultdict

def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    count = 0
    running_sum = 0
    freq = defaultdict(int)
    freq[0] = 1          # CRITICAL: empty prefix (sum=0) occurs once, before any elements
    for num in nums:
        running_sum += num
        count += freq[running_sum - k]      # how many previous prefixes make this a valid subarray?
        freq[running_sum] += 1              # register current prefix for future lookups
    return count
```

**Line-by-Line Explanation:**

| Line | Explanation |
|---|---|
| `freq[0] = 1` | Represents the "prefix before index 0" = 0. Without this, subarrays starting at index 0 that sum exactly to `k` would be missed. |
| `running_sum += num` | Incrementally builds the prefix sum without storing a full array — O(1) space per step instead of O(n) |
| `count += freq[running_sum - k]` | If some earlier prefix equals `running_sum - k`, then the subarray between that point and now sums to exactly `k` |
| `freq[running_sum] += 1` | Register the current prefix value so **future** indices can find it |

**Complete Dry Run:** `nums = [1, 1, 1]`, `k = 2`

| Step | num | running_sum | freq[running_sum-k] added to count | count | freq (after update) |
|---|---|---|---|---|---|
| init | - | 0 | - | 0 | {0:1} |
| 1 | 1 | 1 | freq[1-2]=freq[-1]=0 | 0 | {0:1, 1:1} |
| 2 | 1 | 2 | freq[2-2]=freq[0]=1 | 1 | {0:1, 1:1, 2:1} |
| 3 | 1 | 3 | freq[3-2]=freq[1]=1 | 2 | {0:1, 1:1, 2:1, 3:1} |

**Result: 2** — corresponding to subarrays `[1,1]` (index 0-1) and `[1,1]` (index 1-2) ✅

**ASCII Visualization:**

```
nums    :   1     1     1
index   :   0     1     2

running :   1     2     3
sum

freq map after each step:
step0: {0:1}
step1: {0:1, 1:1}
step2: {0:1, 1:1, 2:1}    <- found freq[0]=1 → +1 to count
step3: {0:1, 1:1, 2:1, 3:1}  <- found freq[1]=1 → +1 to count
```

**Time & Space Complexity:** O(n) time, O(n) space (hash map can hold up to n distinct prefix values).

**Edge Cases:**
- `k = 0` with array containing zeros → must correctly count multiple zero-sum subarrays
- Negative numbers in `nums` → works correctly; prefix sums need not be monotonic
- All elements equal to `k` → every single-element subarray counts
- Empty array → returns 0 by definition (loop doesn't execute)

**Common Mistakes:**
- ❌ Forgetting `freq[0] = 1` initialization — silently undercounts subarrays that start at index 0
- ❌ Using `freq[running_sum + k]` instead of `freq[running_sum - k]` (sign error)
- ❌ Updating `freq[running_sum]` **before** checking `count`, which would incorrectly let a subarray count itself as length-0

**Interview Tip:** This pattern (**Prefix Sum + Hash Map**) is arguably the single most frequently recurring "aha" pattern across FAANG interviews. Master this dry run cold — it generalizes to XOR-K, Divisible-by-K, and Equal-0s-and-1s variants below.

### 5.4 Generalized "Prefix Sum + Hash Map" Template

```python
from collections import defaultdict

def count_subarrays_matching(nums, target, combine=lambda a, b: a + b,
                              inverse_needed=lambda cur, target: cur - target,
                              identity=0):
    """
    Generalized template:
    - combine: how prefix accumulates (add for sum, xor for XOR problems)
    - inverse_needed: what earlier-prefix-value we are looking for
    - identity: the neutral starting prefix value
    """
    count = 0
    running = identity
    freq = defaultdict(int)
    freq[identity] = 1
    for num in nums:
        running = combine(running, num)
        count += freq[inverse_needed(running, target)]
        freq[running] += 1
    return count

# Sum version (identical to 5.3):
count_subarrays_matching([1,1,1], 2)

# XOR version (Section 5.9):
import operator
count_subarrays_matching([4,2,2,6,4], 6, combine=operator.xor,
                          inverse_needed=lambda cur, t: cur ^ t, identity=0)
```

> **📝 Note:** Recognizing that Sections 5.3, 5.6, 5.7, and 5.9 are all **the same template with a different combine function** is a hallmark of advanced pattern recognition — interviewers are impressed when candidates explicitly name this generalization.

### 5.5 Count Subarrays with Sum Exactly K (Non-Negative Array Variant — Sliding Window Comparison)

If **all elements are guaranteed non-negative**, a **sliding window** can also solve "count subarrays with sum ≤ K" type problems in O(n) *without* a hash map — but **cannot** directly count "sum exactly K" as elegantly, because shrinking/growing windows do not naturally enumerate every exact-sum subarray without extra bookkeeping.

| Scenario | Best Tool |
|---|---|
| Sum exactly K, negatives allowed | Prefix Sum + Hash Map |
| Sum exactly K, all non-negative | Prefix Sum + Hash Map still works; Sliding Window needs adaptation |
| Sum at most / at least K, non-negative | Sliding Window (simpler, O(1) space) |
| Longest subarray with sum ≤ K, non-negative | Sliding Window |
| Longest subarray with sum = K, negatives allowed | Prefix Sum + Hash Map (store *first occurrence* index) |

### 5.6 Equal Count of 0s and 1s (Binary Array Longest Subarray)

**Problem Statement (LeetCode 525, "Contiguous Array"):** Given a binary array `nums`, find the maximum length of a contiguous subarray with an **equal number of 0s and 1s**.

**Key Trick:** Convert every `0` to `-1`. Now "equal 0s and 1s" becomes "subarray sum = 0" — directly reducible to the prefix-sum-hash-map pattern, but this time we want the **longest** such subarray, so we store the **first occurrence index** of each prefix value instead of a frequency count.

```python
def find_max_length(nums: list[int]) -> int:
    prefix_to_first_index = {0: -1}   # sum=0 achieved "before" index 0
    running_sum = 0
    max_len = 0
    for i, num in enumerate(nums):
        running_sum += 1 if num == 1 else -1
        if running_sum in prefix_to_first_index:
            max_len = max(max_len, i - prefix_to_first_index[running_sum])
        else:
            prefix_to_first_index[running_sum] = i
    return max_len
```

**Dry Run:** `nums = [0, 1, 0]`

| i | num | running_sum | seen before? | max_len | map update |
|---|---|---|---|---|---|
| - | - | 0 | - | 0 | {0: -1} |
| 0 | 0 | -1 | No | 0 | {0:-1, -1:0} |
| 1 | 1 | 0 | Yes (at -1) | max(0, 1-(-1))=2 | (no update — first occurrence kept) |
| 2 | 0 | -1 | Yes (at 0) | max(2, 2-0)=2 | (no update) |

**Result: 2** (subarray `[0,1]` or `[1,0]`, both length 2) ✅

**Why "first occurrence" not frequency?** Because for **longest subarray**, we want the *earliest* possible starting boundary to maximize the length; overwriting with later indices would shrink potential answers.

### 5.7 Subarray Sums Divisible by K

**Problem Statement (LeetCode 974):** Given an array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.

**Key Insight:** `sum(arr[l..r]) % k == 0` ⟺ `prefix[r] % k == prefix[l-1] % k`. So instead of exact prefix values, we bucket prefixes **by their remainder mod k**, and count pairs of equal remainders (combination count, like counting pairs within each frequency bucket).

```python
from collections import defaultdict

def subarrays_div_by_k(nums: list[int], k: int) -> int:
    freq = defaultdict(int)
    freq[0] = 1                 # empty-prefix remainder
    running_sum = 0
    count = 0
    for num in nums:
        running_sum += num
        remainder = running_sum % k         # Python's % always returns non-negative for positive k
        count += freq[remainder]
        freq[remainder] += 1
    return count
```

**Dry Run:** `nums = [4, 5, 0, -2, -3, 1]`, `k = 5`

| num | running_sum | remainder (%5) | count += freq[rem] | freq after |
|---|---|---|---|---|
| 4 | 4 | 4 | +0 → 0 | {0:1, 4:1} |
| 5 | 9 | 4 | +1 (freq[4]=1) → 1 | {0:1, 4:2} |
| 0 | 9 | 4 | +2 (freq[4]=2) → 3 | {0:1, 4:3} |
| -2 | 7 | 2 | +0 → 3 | {0:1, 4:3, 2:1} |
| -3 | 4 | 4 | +3 (freq[4]=3) → 6 | {0:1, 4:4, 2:1} |
| 1 | 5 | 0 | +1 (freq[0]=1) → 7 | {0:2, 4:4, 2:1} |

**Result: 7** ✅ (matches known answer for this classic example)

**Common Mistake:** Forgetting that in some languages `%` can return negative remainders for negative dividends, requiring `((x % k) + k) % k`. **In Python this is unnecessary** since `%` with a positive divisor always returns a non-negative result — but state this explicitly in interviews to show cross-language awareness.

### 5.8 Continuous Subarray Sum (Multiple of K, Length ≥ 2)

**Problem Statement (LeetCode 523):** Check if the array has a continuous subarray of size **at least 2** whose sum is a multiple of `k`.

Nearly identical to 5.7, but here we only care about **existence**, and we must track the **first index** each remainder was seen at (to enforce the length-≥-2 constraint), rather than frequency counts.

```python
def check_subarray_sum(nums: list[int], k: int) -> bool:
    remainder_first_index = {0: -1}
    running_sum = 0
    for i, num in enumerate(nums):
        running_sum += num
        remainder = running_sum % k if k != 0 else running_sum
        if remainder in remainder_first_index:
            if i - remainder_first_index[remainder] >= 2:
                return True
        else:
            remainder_first_index[remainder] = i
    return False
```

**Edge Case:** `k == 0` must be special-cased (division/modulo by zero) — in that case, we're really asking whether a subarray of length ≥ 2 sums to exactly 0.

### 5.9 Prefix XOR Problems (Subarray XOR Queries / XOR Equals K)

**Problem Statement (analogous to LeetCode 1310 / "XOR Queries of a Subarray" & "Subarray XOR = K"):** Similar to Section 5.3 but with XOR instead of sum.

```python
from collections import defaultdict

def count_subarrays_xor_k(nums: list[int], k: int) -> int:
    freq = defaultdict(int)
    freq[0] = 1
    running_xor = 0
    count = 0
    for num in nums:
        running_xor ^= num
        count += freq[running_xor ^ k]   # because a^b=k <=> a = b^k (XOR self-inverse)
        freq[running_xor] += 1
    return count
```

This is a **direct instantiation** of the generalized template in Section 5.4, swapping `+`/`-` for `^`.

### 5.10 Prefix Sum with Sliding Window — Comparison

| Criterion | Prefix Sum (+ Hash Map) | Sliding Window |
|---|---|---|
| Handles negative numbers | ✅ Yes | ❌ Usually requires non-negative |
| Space | O(n) (hash map) | O(1) |
| Query type | Exact sum = K, arbitrary range sums | Sum constraints with monotonic window growth (≤K, ≥K) |
| Typical complexity | O(n) time, O(n) space | O(n) time, O(1) space |
| When window can shrink/grow monotonically | Not needed | Ideal |

### 5.11 Prefix Sum with Binary Search — Comparison

If the array has **only non-negative numbers**, the prefix sum array is **monotonically non-decreasing**, which unlocks **binary search** on the prefix array — e.g., "find the smallest subarray length with sum ≥ target" (LeetCode 209, though sliding window is simpler there) or "find index where cumulative sum first exceeds X" (common in weighted-random-selection algorithms).

```python
import bisect

def first_index_prefix_at_least(prefix: list[int], target: int) -> int:
    """Requires prefix to be non-decreasing (i.e., all arr[i] >= 0)."""
    return bisect.bisect_left(prefix, target)
```

> **⚠️ Warning:** Binary search on a prefix array is **only valid if the array is monotonic**, which requires all original elements to be non-negative. Applying binary search on a prefix array with negative numbers present produces silently wrong results — a subtle and dangerous interview trap.

---

## 6. Difference Array

### 6.1 What Is a Difference Array?

**Definition:** The **Difference Array** is the *inverse construction* of a prefix sum — where prefix sum turns "individual values" into "running totals," the difference array turns "running totals" back into "individual increments." It is defined as:

```
diff[0] = arr[0]
diff[i] = arr[i] - arr[i-1]     for i >= 1
```

Applying **prefix sum to a difference array reconstructs the original array**:
```
prefix_sum(diff) == arr
```

### 6.2 Why Does It Exist? (The Real Motivation: Range Updates)

**The problem it solves:** Efficiently applying **many range-update operations** ("add value `v` to every element from index `l` to `r`") followed by reading the final array.

| Approach | Per Update | Per Final Readout |
|---|---|---|
| Brute force (loop and add to every index in range) | O(r-l+1), worst case O(n) | O(1) per index already updated |
| Difference Array | O(1) | O(n) once, at the end, via prefix sum |

> **💡 Intuition (Real-World Analogy):** Think of **painting a fence**. Instead of walking along the fence and painting every single plank in the range `[l, r]` one at a time (slow if you do this hundreds of times for overlapping ranges), you instead place a "start painting here" marker at `l` and a "stop painting here" marker at `r+1`. At the very end, you walk the fence once and accumulate all the markers — this single walk (prefix sum) tells you the final paint level (value) at every plank.

### 6.3 Construction & Range Update Mechanics

To add value `v` to `arr[l..r]` (inclusive) using a difference array:

```python
def range_update(diff: list[int], l: int, r: int, v: int) -> None:
    """
    diff must have length n+1 (padded) to safely handle r == n-1.
    Adds v to every element of the *conceptual* array from index l to r inclusive.
    """
    diff[l] += v
    diff[r + 1] -= v
```

**Why this works:** Adding `v` at position `l` means "from here onward, everyone is `v` higher" once we prefix-sum the diff array. Subtracting `v` at `r+1` cancels that boost exactly one step after the intended range ends.

**Full Workflow:**

```python
def build_difference_array(arr: list[int]) -> list[int]:
    n = len(arr)
    diff = [0] * (n + 1)
    diff[0] = arr[0] if n > 0 else 0
    for i in range(1, n):
        diff[i] = arr[i] - arr[i - 1]
    return diff

def apply_updates_and_reconstruct(n: int, updates: list[tuple]) -> list[int]:
    """
    updates: list of (l, r, v) meaning 'add v to arr[l..r]'
    Returns the final array after all updates, starting from an all-zero array.
    """
    diff = [0] * (n + 1)
    for l, r, v in updates:
        diff[l] += v
        diff[r + 1] -= v
    # Reconstruct via prefix sum (this is the "difference-to-prefix" conversion)
    from itertools import accumulate
    result = list(accumulate(diff[:n]))
    return result
```

**Complete Dry Run:** `n = 5`, updates = `[(1, 3, 2), (0, 4, 1), (2, 2, 5)]` (starting array is all zeros)

```
Initial diff (size n+1=6): [0, 0, 0, 0, 0, 0]

Apply (1, 3, +2):  diff[1] += 2   diff[4] -= 2
diff = [0, 2, 0, 0, -2, 0]

Apply (0, 4, +1):  diff[0] += 1   diff[5] -= 1
diff = [1, 2, 0, 0, -2, -1]

Apply (2, 2, +5):  diff[2] += 5   diff[3] -= 5
diff = [1, 2, 5, -5, -2, -1]

Prefix-sum diff[0..4] to reconstruct arr:
result[0] = 1
result[1] = 1+2 = 3
result[2] = 3+5 = 8
result[3] = 8-5 = 3
result[4] = 3-2 = 1
```

**Final reconstructed array: `[1, 3, 8, 3, 1]`**

**Verification (manual):**
- Index 0: only update (0,4,+1) applies → 1 ✅
- Index 1: updates (1,3,+2) and (0,4,+1) apply → 2+1=3 ✅
- Index 2: all three updates apply → 2+1+5=8 ✅
- Index 3: (1,3,+2) and (0,4,+1) apply → 2+1=3 ✅
- Index 4: only (0,4,+1) applies → 1 ✅

**ASCII Visualization of Range Update:**

```
Range update: add +2 to indices [1, 3]

Index      :  0    1    2    3    4
Conceptual :  +0   +2   +2   +2   +0
effect

Difference array encodes only the "boundary changes":
diff        :  0   [+2]  0    0  [-2]
                     ▲              ▲
                start of         one past
                the bump         end of bump

Prefix-summing diff reconstructs the "conceptual effect" row above.
```

**Time & Space Complexity:**

| Operation | Time | Space |
|---|---|---|
| Single range update | O(1) | O(1) |
| Q range updates | O(Q) | O(n) |
| Final reconstruction (prefix sum) | O(n) | O(n) |
| **Total for Q updates + 1 readout** | **O(n + Q)** | O(n) |

Compare to brute force range updates: **O(n·Q)** — the difference array is dramatically faster when `Q` is large.

**Edge Cases:**
- Update range touching the last index (`r == n-1`) → requires the diff array to be padded to size `n+1` so `diff[r+1] = diff[n]` doesn't go out of bounds
- Overlapping updates → handled correctly automatically; contributions simply add up during the final prefix sum
- Single-element range update (`l == r`) → still works: `diff[l] += v; diff[l+1] -= v`
- Update with `v = 0` → harmless no-op

**Common Mistakes:**
- ❌ Not padding the diff array to `n+1`, causing an `IndexError` when `r == n-1`
- ❌ Forgetting to reconstruct via prefix sum at the end — the diff array alone is **not** the final answer; it must be prefix-summed
- ❌ Confusing "difference array" (this section, for **range updates**) with "prefix sum" (Section 2, for **range queries**) — they are inverse operations solving *opposite* problems, but this exact terminology confusion is extremely common among learners

### 6.4 Relationship Between Prefix Sum and Difference Array

```
                  build difference
      arr  ───────────────────────────►  diff
       ▲                                   │
       │                                   │
       └───────────────────────────────────┘
              prefix sum (reconstruct)

prefix_sum(difference_array(arr)) == arr     (they are exact inverses)
difference_array(prefix_sum(arr)) == arr     (also true, in the other direction)
```

This is the discrete analogue of the calculus relationship: differentiation and integration are inverse operations.

### 6.5 Applications of Difference Arrays

- **Range Update, Point Query** problems (the mirror image of "Range Query, Point Update," which needs a Fenwick Tree instead)
- Calendar/booking systems: "add 1 booking to every day from `start` to `end`" repeated many times, then read final daily counts
- **Car Pooling** (LeetCode 1094): passenger count changes at pickup/drop-off — a textbook difference array problem
- **Corporate Flight Bookings** (LeetCode 1109): seat reservations across flight ranges
- Terrain/height-map generation: applying repeated "raise this segment of terrain by X" operations efficiently

### 6.6 Difference Array — Worked Interview Problem: Car Pooling

**Problem Statement (LeetCode 1094):** Given trips `[numPassengers, from, to)` and a car capacity, determine if the car can complete all trips without exceeding capacity at any point.

```python
def car_pooling(trips: list[list[int]], capacity: int) -> bool:
    max_time = max(trip[2] for trip in trips) + 1
    diff = [0] * (max_time + 1)
    for num_passengers, start, end in trips:
        diff[start] += num_passengers
        diff[end] -= num_passengers        # 'to' is already exclusive per problem statement
    current_passengers = 0
    for change in diff:
        current_passengers += change
        if current_passengers > capacity:
            return False
    return True
```

**When to Use Difference Array:** Many range-update operations, single final readout, updates dominate over queries.
**When NOT to Use:** Queries and updates are interleaved and both need to be fast — use a **Fenwick Tree with range-update/point-query dual trick** or a **Segment Tree with lazy propagation** instead (outside this handbook's scope, mentioned only for contrast).

---

## 7. 2D Prefix Sum

### 7.1 What Is a 2D Prefix Sum?

**Definition:** An extension of 1D prefix sum to matrices. `prefix[i][j]` stores the sum of **all elements in the rectangle** from `(0,0)` to `(i-1,j-1)` (using a padded convention with an extra row and column of zeros, exactly mirroring the 1D padded approach).

**Why it exists:** To answer **rectangle sum queries** (sum of all values within any axis-aligned sub-rectangle of a matrix) in O(1) after O(rows×cols) preprocessing — critical in image processing (integral images), heatmap analytics, and 2D range-query interview problems.

### 7.2 The Inclusion-Exclusion Principle

The 2D prefix sum formula is a direct application of the **Inclusion-Exclusion Principle** from combinatorics:

```
prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + matrix[i-1][j-1]
```

**Why the subtraction?** Adding `prefix[i-1][j]` (everything above) and `prefix[i][j-1]` (everything to the left) **double-counts** the overlapping top-left rectangle `prefix[i-1][j-1]` — so we subtract it back out exactly once.

```
ASCII Visualization of Inclusion-Exclusion:

┌─────────────┬───┐
│             │   │
│  A (top-left,   │
│  counted        │
│  in BOTH B&C)│   │
├─────────────┼───┤
│      B      │ C │  <- new cell (i-1, j-1) contributes matrix[i-1][j-1]
└─────────────┴───┘

prefix[i][j] = (region up to row i-1, all cols)   -->  prefix[i-1][j]
             + (region up to col j-1, all rows)   -->  prefix[i][j-1]
             - (double-counted top-left overlap)  -->  prefix[i-1][j-1]
             + (the new single cell)               -->  matrix[i-1][j-1]
```

### 7.3 Construction (Python Implementation)

**Problem Statement:** Given a 2D matrix, preprocess it to answer sum-of-any-sub-rectangle queries in O(1).

```python
def build_2d_prefix_sum(matrix: list[list[int]]) -> list[list[int]]:
    """
    Builds a padded 2D prefix sum with an extra row and column of zeros.
    prefix[i][j] = sum of matrix[0..i-1][0..j-1]
    Shape: (rows+1) x (cols+1)
    """
    if not matrix or not matrix[0]:
        return [[0]]
    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = (
                prefix[i - 1][j]
                + prefix[i][j - 1]
                - prefix[i - 1][j - 1]
                + matrix[i - 1][j - 1]
            )
    return prefix


def region_sum(prefix: list[list[int]], row1: int, col1: int, row2: int, col2: int) -> int:
    """Sum of matrix[row1..row2][col1..col2] inclusive, 0-indexed."""
    return (
        prefix[row2 + 1][col2 + 1]
        - prefix[row1][col2 + 1]
        - prefix[row2 + 1][col1]
        + prefix[row1][col1]
    )
```

**Line-by-Line Explanation:**

| Line | Explanation |
|---|---|
| `prefix = [[0]*(cols+1) for _ in range(rows+1)]` | Padded grid, one extra row/col of zeros (mirrors 1D padding) |
| `prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]` | Inclusion-exclusion for everything strictly above/left of the new cell |
| `+ matrix[i-1][j-1]` | Add the actual new cell's value (shifted by -1 due to padding) |
| `region_sum` 4-term formula | Full 2D inclusion-exclusion: total rect minus above-strip minus left-strip plus double-subtracted corner |

**Complete Dry Run:**

```
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
```

Building `prefix` (4x4 padded):

| i\j | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 3 | 6 |
| 2 | 0 | 5 | 12 | 21 |
| 3 | 0 | 12 | 27 | 45 |

Step-by-step for `prefix[2][2]` (row=2,col=2, corresponds to matrix cell (1,1)=5):
```
prefix[2][2] = prefix[1][2] + prefix[2][1] - prefix[1][1] + matrix[1][1]
             = 3 + 5 - 1 + 5
             = 12  ✅ (sum of top-left 2x2 block: 1+2+4+5=12)
```

Query `region_sum(prefix, row1=1, col1=1, row2=2, col2=2)` — sum of the bottom-right 2x2 block `[[5,6],[8,9]]` = 28:
```
= prefix[3][3] - prefix[1][3] - prefix[3][1] + prefix[1][1]
= 45 - 6 - 12 + 1
= 28  ✅
```

**Time & Space Complexity:**

| Operation | Time | Space |
|---|---|---|
| Build | O(rows × cols) | O(rows × cols) |
| Query | O(1) | O(1) |
| Q queries | O(rows·cols + Q) | O(rows·cols) |

**ASCII Diagram — Rectangle Query Visualization:**

```
Full grid up to (row2,col2)     Subtract top strip        Subtract left strip      Add back double-
                                 (above row1)               (left of col1)          subtracted corner
┌─────────────────┐            ┌─────────────────┐        ┌─────────────────┐      ┌───┐
│#################│            │#################│        │#################│      │###│
│#################│    -       │       (empty)   │   -    │#      ##########│  +   │###│
│#####┌─────┐#####│            │                 │        │#      ##########│      └───┘
│#####│ Q U │#####│            │                 │        │#      ##########│
│#####│ E R │#####│            │                 │        │#      ##########│
│#####└─────┘#####│            │                 │        │#      ##########│
└─────────────────┘            └─────────────────┘        └─────────────────┘
   prefix[r2+1][c2+1]              prefix[r1][c2+1]           prefix[r2+1][c1]     prefix[r1][c1]
```

**Edge Cases:**
- Empty matrix / empty row → guard clause returns early
- Single row or single column matrix → degenerates gracefully to 1D prefix sum logic
- Query for a single cell (`row1==row2, col1==col2`) → still correct via the 4-term formula
- Non-rectangular/jagged input → invalid input for this technique; matrix must be rectangular

**Common Mistakes:**
- ❌ **2D Prefix Indexing Errors:** forgetting the `+1` padding offset when indexing into `prefix` from `matrix` coordinates (the single most common 2D-specific bug)
- ❌ Omitting the `- prefix[i-1][j-1]` term during construction (double-counts overlap)
- ❌ Omitting the final `+ prefix[row1][col1]` term during query (under-subtracts, since it was subtracted twice by the two strip-removal terms)
- ❌ Mixing up `(row, col)` argument order when calling `region_sum`

**Interview Tip:** Draw the 4-rectangle inclusion-exclusion diagram (as above) on the whiteboard **before** writing code — this is the single highest-leverage visual for both understanding and communicating your reasoning for this exact problem class (**LeetCode 304 "Range Sum Query 2D - Immutable"**).

### 7.4 Optimization Notes

- If matrix is extremely large and queries are sparse, a **row-wise 1D prefix sum** (prefix sum per row only) can reduce preprocessing to O(rows×cols) but push query time to O(rows) — a valid alternative when rectangle queries always span the same column range but different row ranges.
- For **mutable matrices** with interleaved point updates, use a **2D Fenwick Tree (Binary Indexed Tree)** — outside this handbook's core scope, mentioned for completeness (LeetCode 308).

### 7.5 Applications

- **Image Processing — "Integral Images":** Used in real-time face detection algorithms (Viola-Jones) to compute the sum of pixel intensities within any rectangular region in O(1), critical for scanning thousands of candidate windows per frame.
- **Heat Maps / Spatial Analytics:** Aggregating event counts (e.g., sensor readings, sales-by-region) within arbitrary geographic bounding boxes.
- **Game Development:** Fast area-damage or area-effect calculations on grid-based maps.

---

## 8. Real-World Applications

### 8.1 Range Queries in Databases & Analytics Dashboards

Analytics dashboards showing "total sales between date A and date B" over a fixed historical dataset frequently precompute daily cumulative totals so any date-range query is an O(1) subtraction rather than a full table scan.

### 8.2 Image Processing — Integral Images

As introduced in 7.5, the **integral image** is literally a 2D prefix sum of pixel intensities. It allows constant-time computation of the average intensity, sum, or variance-related quantities within any rectangular window, which is foundational to classic object-detection pipelines (Haar-cascade face detection) and box-blur filters.

```python
# Conceptual box-blur using 2D prefix sum
def average_pixel_intensity(prefix, r1, c1, r2, c2):
    total = region_sum(prefix, r1, c1, r2, c2)  # from Section 7.3
    area = (r2 - r1 + 1) * (c2 - c1 + 1)
    return total / area
```

### 8.3 Heat Maps

Spatial or temporal heat maps (e.g., "clicks per pixel region on a webpage," "crime incidents per city block") are typically built by binning raw events into a grid and then optionally prefix-summing that grid to answer "how many events occurred within this bounding box" queries instantly.

### 8.4 Data Analytics & Histograms

Cumulative histograms (used to compute percentiles, medians, and CDFs) are direct applications of prefix sum over frequency-binned data:

```python
def percentile_bucket(freq_hist: list[int], percentile: float) -> int:
    """freq_hist[v] = count of items with value v. Returns bucket at given percentile."""
    from itertools import accumulate
    cum = list(accumulate(freq_hist))
    total = cum[-1]
    target = total * percentile
    for i, c in enumerate(cum):
        if c >= target:
            return i
    return len(freq_hist) - 1
```

### 8.5 Financial Analysis — Running Balance / Cumulative P&L

Cumulative profit-and-loss tracking, running account balances, and moving-cumulative-return calculations in trading systems are all textbook prefix sums over a time series of transactions or daily returns.

### 8.6 Time Series Analysis

Cumulative sums are used to detect **trend shifts** (CUSUM control charts in statistical process control) — a classic application of prefix sum in quality engineering and anomaly detection, where a sustained deviation shows up as a consistently sloped segment in the cumulative-sum plot.

### 8.7 Competitive Programming

Prefix Sum (and its 2D/XOR/difference-array variants) appears constantly across Codeforces Div 2/3, AtCoder Beginner Contests, and CSES Problem Set as either the core technique or a preprocessing step inside a larger DP/greedy solution.

---

## 9. Problem Recognition

### 9.1 Keywords That Signal "Prefix Sum"

| Keyword / Phrase in Problem Statement | Likely Technique |
|---|---|
| "range sum query", "sum between indices" | 1D Prefix Sum |
| "multiple queries", "answer Q queries efficiently" | Prefix Sum (precompute once) |
| "subarray sum equals K" | Prefix Sum + Hash Map |
| "number of subarrays with sum/XOR ..." | Prefix Sum + Hash Map |
| "rectangle sum", "submatrix sum" | 2D Prefix Sum |
| "add value to a range", "range update" | Difference Array |
| "divisible by k", "remainder" (with subarray sum) | Prefix Sum + Modulo bucketing |
| "equal number of 0s and 1s" | Prefix Sum with -1/+1 transform |
| "cumulative", "running total", "balance over time" | Prefix Sum |
| "XOR of subarray" | Prefix XOR |

### 9.2 Decision Tree — Choosing the Right Technique

```
                     ┌─────────────────────────┐
                     │  Problem involves a      │
                     │  contiguous subarray/    │
                     │  submatrix aggregate?    │
                     └───────────┬─────────────┘
                                 │ Yes
                 ┌───────────────┴────────────────┐
                 │ Are there MANY repeated         │
                 │ read-only range queries?        │
                 └───────────────┬────────────────┘
              Yes ┌──────────────┴──────────────┐ No (single pass / count subarrays)
                  │                              │
     ┌────────────┴───────────┐      ┌───────────┴────────────────┐
     │ 1D or 2D array?         │      │ Need exact match to target  │
     └────────────┬────────────┘      │ (sum/xor/mod == K)?          │
   1D┌────────────┴──┐2D               └───────────┬─────────────────┘
     │                │                       Yes   │      No
┌────┴────┐    ┌──────┴──────┐          ┌──────────┴───┐  ┌─────────────────┐
│1D Prefix│    │2D Prefix Sum│          │Prefix Sum +   │  │Sliding Window   │
│Sum      │    │(Inclusion-  │          │Hash Map       │  │(if non-negative,│
│         │    │Exclusion)   │          │(generalized   │  │monotonic window)│
└─────────┘    └─────────────┘          │template §5.4) │  └─────────────────┘
                                          └───────────────┘

                     ┌─────────────────────────┐
                     │  Problem instead has     │
                     │  MANY range-UPDATE ops   │
                     │  and a final readout?    │
                     └───────────┬─────────────┘
                                 │ Yes
                          ┌──────┴───────┐
                          │ Difference   │
                          │ Array        │
                          └──────────────┘

                     ┌─────────────────────────┐
                     │ Updates AND queries      │
                     │ interleaved & both       │
                     │ need to be fast?         │
                     └───────────┬─────────────┘
                                 │ Yes
                          ┌──────┴────────────────┐
                          │ Fenwick Tree /         │
                          │ Segment Tree           │
                          │ (OUTSIDE this          │
                          │ handbook's scope)      │
                          └────────────────────────┘
```

### 9.3 Prefix Sum vs Sliding Window vs Hashing — Full Comparison

| Criterion | Prefix Sum | Sliding Window | Pure Hashing (no prefix) |
|---|---|---|---|
| Handles negative numbers | ✅ | ❌ (usually) | Depends on problem |
| Handles "exact sum = K" | ✅ (best fit) | ⚠️ Harder | ⚠️ Possible but usually combined w/ prefix |
| Handles "at most / at least K" (non-negative) | ⚠️ Works but overkill | ✅ (best fit) | ❌ |
| Extra space | O(n) typically | O(1) | O(n) |
| Supports arbitrary range queries after preprocessing | ✅ | ❌ | ❌ |
| Supports range updates efficiently | ❌ (needs Difference Array variant) | ❌ | ❌ |

### 9.4 Interview Clues Checklist

Ask yourself these questions when you see a subarray/submatrix aggregate problem:
1. **Is the array static or does it change?** Static → prefix sum. Frequent updates + queries → Fenwick/Segment Tree.
2. **Am I counting subarrays or just answering one aggregate query?** Counting with an exact target → hash map + prefix. Single/few queries → plain prefix array.
3. **Are all numbers non-negative?** If yes, sliding window and binary-search-on-prefix become viable alternatives.
4. **Is it 1D or 2D?** 2D → inclusion-exclusion 2D prefix sum.
5. **Am I updating ranges, not querying them?** → Difference array.
6. **Does the operation have an inverse (sum, xor) or not (min, max)?** No inverse → prefix sum doesn't directly give O(1) range queries; consider Sparse Table/Segment Tree.

---

## 10. Optimization Strategies

### 10.1 Brute Force → Prefix Sum: The Core Upgrade Path

```
Brute Force Range Sum:          Prefix Sum Range Sum:
for each query (l, r):          precompute prefix[] once: O(n)
    total = 0                   for each query (l, r):
    for i in range(l, r+1):         total = prefix[r+1] - prefix[l]   # O(1)
        total += arr[i]
    # O(r-l+1) per query, O(n*Q) total     # O(n + Q) total
```

### 10.2 Prefix Sum + Hash Map (Space-for-Time Trade)

Storing every prefix value seen so far in a hash map turns an O(n²) nested-loop subarray-counting problem into O(n) — trading O(n) extra space for an asymptotic time win. This is the single highest-value optimization pattern in this handbook (fully detailed in Section 5.3–5.4, 5.7, 5.9).

### 10.3 Prefix + Frequency Array (When Values Are Bounded)

When array values are bounded to a small range (e.g., `0 <= arr[i] <= 100`), a **frequency array** (plain Python list indexed by value) often outperforms a hash map (dict) due to lower constant-factor overhead and cache-friendlier access patterns:

```python
def build_prefix_frequency_bounded(arr: list[int], max_val: int) -> list[list[int]]:
    """For small max_val, e.g. counting problems with value range 0..100."""
    n = len(arr)
    prefix = [[0] * (max_val + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1][:]     # copy previous row
        prefix[i][arr[i - 1]] += 1
    return prefix
```

> **⚠️ Warning:** This approach costs O(n × max_val) space — only appropriate when `max_val` is genuinely small; otherwise the earlier hash-map-based running-total pattern (Section 4.7.1) is preferred.

### 10.4 Prefix + Modulo (Reducing Distinct Bucket Count)

When you only care about divisibility (Section 5.7), bucket prefixes by `remainder % k` instead of by exact value — this bounds the number of distinct buckets to `k` (often far smaller than `n`), which can matter for memory-constrained environments.

### 10.5 Space Optimization

- **Rolling variable instead of full array:** If you only ever need the *current* running prefix value (not historical values), don't materialize the whole prefix array — track a single scalar (as done throughout Section 5's hash-map patterns).
- **In-place prefix construction** (Section 2.6) — saves O(n) when the original array is disposable.
- **2D prefix sum row-only variant** (Section 7.4) when queries share a fixed column range.

### 10.6 Time Optimization

- Use `itertools.accumulate` (C-implemented) instead of manual Python loops wherever the full array is genuinely needed (Section 2.4–2.5) — up to 5x faster in practice.
- Avoid rebuilding the entire prefix array on every update in a mutable-array scenario — if updates are truly frequent and interleaved with queries, switch data structures entirely (Fenwick Tree) rather than trying to "optimize" repeated O(n) rebuilds.

---

## 11. Interview Preparation

### 11.1 Standard Templates to Memorize

**Template A — 1D Range Sum Query:**
```python
from itertools import accumulate
prefix = list(accumulate(arr, initial=0))
def query(l, r): return prefix[r + 1] - prefix[l]
```

**Template B — Count Subarrays With Exact Sum K:**
```python
from collections import defaultdict
def subarray_sum_equals_k(nums, k):
    freq = defaultdict(int); freq[0] = 1
    running = count = 0
    for num in nums:
        running += num
        count += freq[running - k]
        freq[running] += 1
    return count
```

**Template C — Difference Array Range Update:**
```python
def apply_range_update(diff, l, r, v):
    diff[l] += v
    diff[r + 1] -= v
```

**Template D — 2D Prefix Sum:**
```python
def build_2d_prefix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0]*(cols+1) for _ in range(rows+1)]
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + matrix[i-1][j-1]
    return prefix
```

### 11.2 Problems by Difficulty

**Easy:**
- Running Sum of 1d Array (LeetCode 1480)
- Find Pivot Index (LeetCode 724)
- Range Sum Query - Immutable (LeetCode 303)
- Richest Customer Wealth (LeetCode 1672, trivial row-sum)

**Medium:**
- Subarray Sum Equals K (LeetCode 560)
- Contiguous Array (LeetCode 525)
- Product of Array Except Self (LeetCode 238 — prefix/suffix product variant)
- Range Sum Query 2D - Immutable (LeetCode 304)
- Continuous Subarray Sum (LeetCode 523)
- Subarray Sums Divisible by K (LeetCode 974)
- Corporate Flight Bookings (LeetCode 1109 — Difference Array)
- Car Pooling (LeetCode 1094 — Difference Array)
- Maximum Size Subarray Sum Equals k (LeetCode 325)

**Hard:**
- Count of Range Sum (LeetCode 327 — prefix sum + merge sort / BIT)
- Range Sum Query 2D - Mutable (LeetCode 308 — needs 2D Fenwick, mentioned for contrast)
- Maximum Sum of 3 Non-Overlapping Subarrays (LeetCode 689 — prefix sum + DP)
- Number of Submatrices That Sum to Target (LeetCode 1074 — 2D prefix sum + hash map combo)

### 11.3 Pattern-Wise Question Map

| Pattern | Representative Problems |
|---|---|
| Basic Range Sum | LeetCode 303, 1480, 724 |
| Prefix Sum + Hash Map (sum=K) | LeetCode 560, 1074 |
| Prefix XOR | "Subarray XOR = K" style problems, 1310 (queries variant) |
| Difference Array | LeetCode 1094, 1109 |
| 2D Prefix Sum | LeetCode 304, 1074, 1314 (Matrix Block Sum) |
| Modulo Bucketing | LeetCode 974, 523 |
| -1/+1 Transform | LeetCode 525 |

### 11.4 Company-Wise Tendencies (General Patterns Observed)

> **📝 Note:** Company-specific question sets change frequently and are best verified on aggregator sites (e.g., LeetCode's company tag feature, which requires premium access) rather than memorized from static lists. As a general pattern:
- **Amazon, Google, Meta, Microsoft:** Frequently ask Subarray Sum Equals K and its variants (XOR/mod) as a 25-35 minute medium-difficulty screening question.
- **Bloomberg, Two Sigma, Trading Firms:** Favor 2D prefix sum and difference array problems due to their relevance to time-series/financial data.
- **Google:** Known for pushing into the generalized template (Section 5.4) and asking candidates to derive multiple variants live.

### 11.5 Blind 75 / NeetCode Relevant Entries

- **Product of Array Except Self** (prefix/suffix product pattern)
- **Contiguous Array** (prefix sum with -1/+1 transform)
- **Subarray Sum Equals K** (commonly included in extended NeetCode 150 lists)

### 11.6 Frequently Asked Interview Questions (Conceptual)

1. *"What's the time complexity improvement prefix sum gives you, and why?"* → O(n) per query → O(1) per query after O(n) preprocessing.
2. *"How would you extend this to 2D?"* → Inclusion-exclusion, Section 7.
3. *"What if the array is updated frequently?"* → Prefix sum degrades to O(n) per update; recommend Fenwick/Segment Tree instead.
4. *"Walk me through why `freq[0] = 1` is needed in the hash map pattern."* → Represents the empty prefix so subarrays starting at index 0 are counted correctly.
5. *"Can you do this with O(1) extra space?"* → Only if you don't need the full prefix array — accumulate a running scalar instead of storing history (viable for single-query or streaming scenarios, not for the hash map pattern which inherently needs history).

### 11.7 Interview Tricks & Delivery Tips

- **State your convention out loud** (inclusive/exclusive) before coding — Section 2.1.
- **Draw the ASCII/whiteboard diagram** for 2D inclusion-exclusion before coding — Section 7.3.
- **Name the generalized template explicitly** when solving XOR/mod variants — shows pattern mastery, not memorization (Section 5.4).
- **Always ask about negative numbers** — determines if sliding window is even viable (Section 9.3).
- **Mention the Fenwick Tree/Segment Tree alternative** when asked about updates — shows you know prefix sum's boundary of applicability (Section 6.6, 10.6).

---

## 12. Python Tips & Idioms

### 12.1 `itertools.accumulate` — Recap and Advanced Usage

```python
from itertools import accumulate
import operator

# Basic padded prefix sum
prefix = list(accumulate(arr, initial=0))

# Custom operator (works for sum, xor, mul, max, min — Section 4.1 table)
prefix_xor = list(accumulate(arr, operator.xor, initial=0))

# accumulate is a GENERATOR — avoid materializing the full list if you only
# need to iterate once (saves memory for very large arrays):
for running_total in accumulate(arr):
    pass  # process on the fly, no O(n) list allocation
```

### 12.2 List Comprehensions — What They Can and Cannot Do Here

```python
# ❌ Cannot cleanly express prefix sum in one comprehension (needs external state):
# prefix = [sum(arr[:i+1]) for i in range(len(arr))]   # WORKS but is O(n^2)! Common trap.

# ✅ Comprehensions ARE great for transforming arrays before prefix-summing:
adjusted = [x if x > 0 else 0 for x in arr]   # e.g., clip negatives before prefix sum
prefix = list(accumulate(adjusted, initial=0))
```

> **⚠️ Warning:** `[sum(arr[:i+1]) for i in range(len(arr))]` is a classic beginner trap — it *looks* elegant but re-sums from scratch every iteration, making it **O(n²)**, completely defeating the purpose of prefix sum. Always use `accumulate` or a manual O(n) loop.

### 12.3 `defaultdict` for Hash-Map-Based Patterns

```python
from collections import defaultdict
freq = defaultdict(int)     # auto-initializes missing keys to 0 — avoids KeyError
freq[0] = 1                 # seed the empty-prefix case (Section 5.3)
```

### 12.4 `Counter` for One-Shot Frequency Analysis

```python
from collections import Counter
c = Counter(arr)            # useful for one-time frequency snapshots,
                             # but NOT for running/incremental prefix frequency —
                             # for that, build incrementally with defaultdict (Section 4.7.1)
```

### 12.5 Dictionary vs List for Prefix Lookups

| Use `dict` / `defaultdict` when | Use plain `list` (frequency array) when |
|---|---|
| Values can be arbitrarily large/negative (prefix sums, XORs) | Values are bounded to a small known range |
| Sparse value space | Dense value space |
| You need `O(1)` average lookup with hashing overhead | You want raw array-indexing speed, no hashing |

### 12.6 Performance Tips

- Prefer `accumulate` over manual loops for bulk construction (Section 2.5 benchmark).
- Avoid repeated list slicing (`arr[l:r+1]`) inside loops — it creates new lists and costs O(r-l), silently reintroducing the brute-force complexity you were trying to eliminate.
- For read-heavy 2D prefix sums, precompute once and reuse — never rebuild inside a query loop.

### 12.7 Memory Optimization

- Use generators (`accumulate` without wrapping in `list(...)`) when you only need to stream through values once.
- Use `array` module or NumPy arrays (`numpy.cumsum`) instead of Python lists for very large numeric datasets to reduce per-element memory overhead — NumPy's `cumsum` is vectorized and often faster still than `itertools.accumulate` for large numeric workloads:

```python
import numpy as np
arr_np = np.array([2, 4, 1, 5, 3])
prefix_np = np.cumsum(arr_np)          # array([ 2,  6,  7, 12, 15])
prefix_padded_np = np.concatenate(([0], prefix_np))
```

> **📝 Note:** `numpy.cumsum` is the go-to choice in data-science/production numerical contexts; `itertools.accumulate` is the go-to choice in pure-Python interview/DSA contexts (no external dependency, works on any iterable, supports arbitrary binary operators).

### 12.8 Common Python Pitfalls Specific to Prefix Sum Code

- ❌ Mutating a list you meant to keep immutable via in-place prefix construction (Section 2.6) when the caller still needs original values elsewhere.
- ❌ Copying a `dict` incorrectly inside a loop (`new_freq = prefix_freq[i-1]` instead of `dict(prefix_freq[i-1])`) — this aliases the same object instead of copying it, corrupting "historical" prefix frequency snapshots.
- ❌ Assuming `%` behaves like C++/Java for negative numbers — Python's `%` differs (Section 4.8, 5.7).

---

## 13. Common Mistakes

### 13.1 Wrong Initialization

Using `prefix[0] = arr[0]` when your query formula assumes the padded/exclusive convention (`prefix[0]` should be `0`), or vice versa. **Fix:** Pick one convention and be consistent — the padded convention is recommended throughout this handbook.

### 13.2 Off-by-One Errors

The most common single class of bug in this entire topic. Always occurs at the boundary between "prefix index" and "array index." **Fix:** Always dry-run a 3-4 element example by hand (as done in every section above) before trusting your formula.

### 13.3 Incorrect Query Formula

Mixing inclusive-convention subtraction (`prefix[r] - prefix[l-1]`) with a padded/exclusive prefix array, or vice versa. **Fix:** Match the formula to the convention — see the universal formula table in Section 2.2.

### 13.4 Missing `prefix[0]` / `freq[0]=1` Initialization

In the hash-map pattern (Section 5.3), forgetting `freq[0] = 1` silently undercounts subarrays starting at index 0. In the plain prefix array, forgetting to pad with a leading `0` breaks the universal query formula.

### 13.5 Inclusive vs Exclusive Confusion

Switching conventions mid-solution (e.g., building an inclusive array but writing a query formula that assumes padding). **Fix:** Document your convention as a comment directly above the array construction line.

### 13.6 Integer Overflow Discussion (Language Comparison — Not a Python Issue)

> **📝 Note (Cross-Language Context):** In C++ and Java, prefix sums of large arrays with large values can silently overflow a 32-bit `int` (max ~2.1 billion), requiring a switch to `long`/`long long`. **Python integers are arbitrary-precision** — they grow automatically and **never silently overflow**. This is a genuine practical advantage of Python for this topic, but it's worth understanding the *concept* of overflow since interviewers evaluating language-agnostic understanding may ask about it, and you may need to translate solutions to other languages.

### 13.7 Difference Array Mistakes

- ❌ Forgetting to pad the difference array to size `n+1`, causing an `IndexError` on `diff[r+1]` when `r == n-1`.
- ❌ Forgetting the final reconstruction prefix-sum step — the difference array by itself is **not** the answer.
- ❌ Applying updates to the *original array* directly instead of to the difference array, defeating the O(1)-per-update benefit entirely.

### 13.8 2D Prefix Indexing Errors

- ❌ Forgetting the `+1` offset between `matrix` coordinates and `prefix` coordinates.
- ❌ Omitting the inclusion-exclusion correction term (`- prefix[i-1][j-1]` during build, `+ prefix[row1][col1]` during query).
- ❌ Swapping row/column argument order.

---

## 14. Cheat Sheets

### 14.1 Prefix Sum Templates Cheat Sheet

```python
# ── 1D PADDED PREFIX SUM ──────────────────────────────
from itertools import accumulate
prefix = list(accumulate(arr, initial=0))
query = lambda l, r: prefix[r + 1] - prefix[l]

# ── PREFIX XOR ─────────────────────────────────────────
import operator
prefix_xor = list(accumulate(arr, operator.xor, initial=0))
query_xor = lambda l, r: prefix_xor[r + 1] ^ prefix_xor[l]

# ── COUNT SUBARRAYS SUM == K (Hash Map) ────────────────
from collections import defaultdict
def count_sum_k(nums, k):
    freq = defaultdict(int); freq[0] = 1
    running = count = 0
    for x in nums:
        running += x
        count += freq[running - k]
        freq[running] += 1
    return count

# ── COUNT SUBARRAYS DIVISIBLE BY K (Modulo bucketing) ──
def count_div_k(nums, k):
    freq = defaultdict(int); freq[0] = 1
    running = count = 0
    for x in nums:
        running += x
        r = running % k
        count += freq[r]
        freq[r] += 1
    return count

# ── LONGEST SUBARRAY EQUAL 0s/1s (-1/+1 transform) ─────
def longest_equal(nums):
    first_seen = {0: -1}
    running = best = 0
    for i, x in enumerate(nums):
        running += 1 if x == 1 else -1
        if running in first_seen:
            best = max(best, i - first_seen[running])
        else:
            first_seen[running] = i
    return best
```

### 14.2 Difference Array Template Cheat Sheet

```python
def range_update(diff, l, r, v):
    diff[l] += v
    diff[r + 1] -= v

def reconstruct(diff, n):
    from itertools import accumulate
    return list(accumulate(diff[:n]))
```

### 14.3 2D Prefix Template Cheat Sheet

```python
def build_2d(matrix):
    rows, cols = len(matrix), len(matrix[0])
    P = [[0]*(cols+1) for _ in range(rows+1)]
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + matrix[i-1][j-1]
    return P

def region_sum(P, r1, c1, r2, c2):
    return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
```

### 14.4 Complexity Table (Master Summary)

| Structure / Technique | Build | Point Query | Range Query | Point Update | Range Update |
|---|---|---|---|---|---|
| Plain Array | — | O(1) | O(n) | O(1) | O(n) |
| 1D Prefix Sum | O(n) | O(1) | O(1) | O(n) rebuild | O(n) rebuild |
| Difference Array | O(n) | O(n) reconstruct | O(n) reconstruct | O(1)* | O(1) |
| 2D Prefix Sum | O(rows·cols) | O(1) | O(1) | O(rows·cols) rebuild | O(rows·cols) rebuild |
| Fenwick Tree (mention only) | O(n log n) | O(log n) | O(log n) | O(log n) | O(log n) w/ variant |
| Segment Tree (mention only) | O(n) | O(log n) | O(log n) | O(log n) | O(log n) w/ lazy prop |

*Point update on a difference array changes the *shape* of the reconstructed array from that point on — treat with care; it's not equivalent to a point update on the original array without also adjusting `diff[i+1]`.

### 14.5 Pattern Recognition Cheat Sheet (Condensed)

```
"sum between l and r, many queries"        → 1D Prefix Sum
"sum of submatrix, many queries"           → 2D Prefix Sum
"count subarrays with sum/xor/mod == K"    → Prefix + Hash Map
"add v to range, many updates, 1 readout"  → Difference Array
"longest subarray with property X"         → Prefix + first-seen-index Hash Map
"all non-negative + range constraint"      → Consider Sliding Window instead
"updates AND queries both frequent"        → Fenwick Tree / Segment Tree (beyond this handbook)
```

### 14.6 Python Syntax Quick Reference

| Task | Idiom |
|---|---|
| Padded prefix sum | `accumulate(arr, initial=0)` |
| Prefix XOR | `accumulate(arr, operator.xor, initial=0)` |
| Safe dict default | `defaultdict(int)` |
| One-shot frequency count | `Counter(arr)` |
| Binary search on sorted/monotonic prefix | `bisect.bisect_left(prefix, target)` |
| Vectorized cumulative sum | `numpy.cumsum(arr)` |

---

## 15. Practice Problem Bank

| # | Problem Name | Platform | Difficulty | Pattern | Concept | Link |
|---|---|---|---|---|---|---|
| 1 | Running Sum of 1d Array | LeetCode | Easy | Basic Prefix Sum | 1D Prefix | leetcode.com/problems/running-sum-of-1d-array |
| 2 | Find Pivot Index | LeetCode | Easy | Prefix + Suffix comparison | 1D Prefix | leetcode.com/problems/find-pivot-index |
| 3 | Range Sum Query - Immutable | LeetCode | Easy | Basic Prefix Sum | 1D Prefix | leetcode.com/problems/range-sum-query-immutable |
| 4 | Subarray Sum Equals K | LeetCode | Medium | Prefix + Hash Map | Count Subarrays | leetcode.com/problems/subarray-sum-equals-k |
| 5 | Contiguous Array | LeetCode | Medium | Prefix + -1/+1 transform | Longest Subarray | leetcode.com/problems/contiguous-array |
| 6 | Continuous Subarray Sum | LeetCode | Medium | Prefix + Modulo | Divisibility | leetcode.com/problems/continuous-subarray-sum |
| 7 | Subarray Sums Divisible by K | LeetCode | Medium | Prefix + Modulo bucketing | Divisibility | leetcode.com/problems/subarray-sums-divisible-by-k |
| 8 | Range Sum Query 2D - Immutable | LeetCode | Medium | 2D Prefix Sum | Inclusion-Exclusion | leetcode.com/problems/range-sum-query-2d-immutable |
| 9 | Corporate Flight Bookings | LeetCode | Medium | Difference Array | Range Update | leetcode.com/problems/corporate-flight-bookings |
| 10 | Car Pooling | LeetCode | Medium | Difference Array | Range Update | leetcode.com/problems/car-pooling |
| 11 | Product of Array Except Self | LeetCode | Medium | Prefix/Suffix Product | Prefix Product | leetcode.com/problems/product-of-array-except-self |
| 12 | Maximum Size Subarray Sum Equals k | LeetCode | Medium | Prefix + Hash Map (first index) | Longest Subarray | leetcode.com/problems/maximum-size-subarray-sum-equals-k |
| 13 | Count of Range Sum | LeetCode | Hard | Prefix Sum + Merge Sort/BIT | Advanced Counting | leetcode.com/problems/count-of-range-sum |
| 14 | Range Sum Query 2D - Mutable | LeetCode | Hard | 2D Fenwick Tree (contrast) | Mutable 2D | leetcode.com/problems/range-sum-query-2d-mutable |
| 15 | Number of Submatrices That Sum to Target | LeetCode | Hard | 2D Prefix + Hash Map | Advanced 2D | leetcode.com/problems/number-of-submatrices-that-sum-to-target |
| 16 | Matrix Block Sum | LeetCode | Medium | 2D Prefix Sum | Sliding Rectangle | leetcode.com/problems/matrix-block-sum |
| 17 | Maximum Sum of 3 Non-Overlapping Subarrays | LeetCode | Hard | Prefix Sum + DP | Multi-window | leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays |
| 18 | Prefix Sum Array | GeeksforGeeks | Basic | 1D Prefix Sum | Foundational | geeksforgeeks.org (search: "prefix sum array") |
| 19 | Range Sum Query | Code360 (Coding Ninjas) | Easy | 1D Prefix Sum | Foundational | naukri.com/code360 (search: "range sum query") |
| 20 | Difference Array \| Range Update Query | GeeksforGeeks | Medium | Difference Array | Range Update | geeksforgeeks.org (search: "difference array range update") |
| 21 | 2D Range Sum Query | Code360 | Medium | 2D Prefix Sum | Inclusion-Exclusion | naukri.com/code360 |
| 22 | Static Range Sum Queries (CSES) | CSES | Easy | 1D Prefix Sum | Foundational | cses.fi/problemset/task/1646 |
| 23 | Forest Queries (CSES) | CSES | Easy | 2D Prefix Sum | Inclusion-Exclusion | cses.fi/problemset/task/1652 |
| 24 | Range XOR Queries (CSES) | CSES | Medium | Prefix XOR | XOR Range | cses.fi/problemset/task/1650 |
| 25 | Range Update Queries (CSES) | CSES | Medium | Difference Array + Prefix | Range Update | cses.fi/problemset/task/1651 |
| 26 | Prefix Sums (Educational) | Codeforces | Div 2 A/B level | 1D Prefix Sum | Foundational | codeforces.com (search by tag: prefix-sums) |
| 27 | XOR-Subarray Counting | Codeforces | Div 2 C level | Prefix XOR + Hash Map | Counting | codeforces.com (tag: bitmasks, prefix-sums) |
| 28 | Prefix Sum Practice | HackerRank | Easy-Medium | 1D Prefix Sum | Foundational | hackerrank.com (search: "prefix sum") |
| 29 | Cumulative Sum Array | InterviewBit | Easy | 1D Prefix Sum | Foundational | interviewbit.com (search: "prefix sum") |
| 30 | ABC Range Sum (various contests) | AtCoder | Beginner | 1D/2D Prefix Sum | Foundational + Inclusion-Exclusion | atcoder.jp (search: "cumulative sum") |

> **📝 Note:** Some listed links are search-pointers rather than direct permalinks because platform URL structures/problem numbering change over time (especially GfG, Code360, HackerRank, InterviewBit, and AtCoder contest-specific problems). Search using the exact problem name shown for the most current, correct link.

### 15.1 Problems Categorized by Concept (Quick Index)

- **Running Sum:** #1
- **Range Sum Query:** #3, #18, #19, #22, #26
- **Prefix XOR:** #24, #27
- **Prefix Hash Map:** #4, #12, #15, #27
- **Difference Array:** #9, #10, #20, #25
- **2D Prefix Sum:** #8, #16, #21, #23, #30
- **Prefix Modulo:** #6, #7
- **Count Subarrays:** #4, #7, #13
- **Longest Subarray:** #5, #12
- **Advanced Prefix Sum:** #13, #15, #17

---

## 16. Final Revision Kit

### 16.1 One-Page Notes

```
PREFIX SUM = precompute cumulative aggregate ONCE (O(n)) → answer range queries O(1)

FORMULA (padded, 0-indexed):   sum(l..r) = prefix[r+1] - prefix[l]
BUILD:                          prefix = accumulate(arr, initial=0)

HASH MAP VARIANT (count exact-match subarrays):
    freq[0] = 1
    for x in arr: running += x; count += freq[running-k]; freq[running]+=1

DIFFERENCE ARRAY (inverse of prefix sum, for RANGE UPDATES):
    diff[l] += v ; diff[r+1] -= v      → then prefix-sum diff to get final array

2D PREFIX SUM (inclusion-exclusion):
    P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + M[i-1][j-1]
    region  = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
```

### 16.2 Mind Map

```
                              PREFIX SUM
                                  │
        ┌─────────────┬──────────┼──────────┬─────────────┐
        │             │          │          │             │
     1D BASIC     TYPES         PATTERNS   DIFFERENCE   2D PREFIX
     Range Query  (XOR,Product, (Hash Map  ARRAY        (Inclusion-
                  Min/Max,      variants)  (Range       Exclusion)
                  Count,Mod)               Updates)
        │             │          │          │             │
   O(1) query    each has own  count K,   diff[l]+=v    O(1) rect
   after O(n)    combine fn    divisible  diff[r+1]-=v  query after
   build                       by K,      then prefix   O(rows*cols)
                               longest    sum            build
                               subarray
```

### 16.3 Pattern Map (Condensed Decision Guide)

See full decision tree in Section 9.2. Quick version:

```
Static + many queries         → Prefix Sum
Count subarrays == target     → Prefix + Hash Map
Many range updates            → Difference Array
2D region queries             → 2D Prefix Sum (Inclusion-Exclusion)
Non-negative + window bound   → Sliding Window (not Prefix Sum)
Frequent updates + queries    → Fenwick/Segment Tree (beyond scope)
```

### 16.4 Recognition Flowchart

(Full version in Section 9.2 — condensed callout below)

```
Keyword scan → "range sum/query" → Prefix Sum
             → "count subarrays ==K/XOR/div" → Prefix + Hash Map
             → "range update" → Difference Array
             → "submatrix/rectangle" → 2D Prefix Sum
             → "equal 0s/1s" → -1/+1 transform + Hash Map
```

### 16.5 Complexity Sheet

See full table in Section 14.4.

### 16.6 Interview Cheat Sheet

- State convention (inclusive/exclusive) out loud.
- Draw inclusion-exclusion diagram for 2D.
- Name the generalized hash-map template for XOR/mod variants.
- Mention Fenwick/Segment Tree when asked about frequent updates.
- Dry-run a small 3-5 element example before trusting any formula.

### 16.7 15-Minute Revision

1. Recall the universal formula: `sum(l,r) = prefix[r+1]-prefix[l]` (2 min)
2. Recall the hash-map template + `freq[0]=1` (3 min)
3. Recall difference array: `diff[l]+=v; diff[r+1]-=v` (2 min)
4. Recall 2D inclusion-exclusion formula (3 min)
5. Skim Common Mistakes list, Section 13 (5 min)

### 16.8 1-Hour Revision

1. Re-derive Section 2.3 build + query from scratch, no peeking (10 min)
2. Solve Subarray Sum Equals K from memory (Section 5.3) (10 min)
3. Solve one Difference Array problem (Section 6.6, Car Pooling) (10 min)
4. Solve 2D Prefix Sum dry run (Section 7.3) by hand on paper (10 min)
5. Review Decision Tree (Section 9.2) and explain each branch out loud (10 min)
6. Review all Common Mistakes (Section 13) and Cheat Sheets (Section 14) (10 min)

---

## 17. FAQs

**Q: Is Prefix Sum the same as Cumulative Sum?**
A: Yes — same construction, different naming conventions depending on field (Section 1.4).

**Q: Why does Python not need to worry about integer overflow in prefix sums?**
A: Python integers are arbitrary-precision and grow automatically; this differs from fixed-width `int`/`long` types in C++/Java (Section 13.6).

**Q: When should I use Prefix Sum vs a Fenwick Tree (Binary Indexed Tree)?**
A: Use Prefix Sum when the array is static (no updates) or updates are rare. Use a Fenwick Tree when point updates and range queries are both frequent and interleaved (Section 6.6, 10.6, 14.4).

**Q: Can Prefix Sum answer range minimum/maximum queries?**
A: No — min/max have no inverse operation, so the "subtract two prefixes" trick doesn't work. Use a Sparse Table (static) or Segment Tree (dynamic) instead (Section 4.6).

**Q: What's the single most important line to remember in the hash-map pattern?**
A: `freq[0] = 1` — without it, subarrays starting at index 0 are silently undercounted (Section 5.3, 13.4).

**Q: Is `itertools.accumulate` always faster than a manual loop?**
A: Generally yes, because it's implemented in C; the difference becomes significant for large arrays (Section 2.5).

**Q: How is a Difference Array different from a Prefix Sum array?**
A: They are exact inverses. Prefix Sum turns individual values into running totals (used for fast **queries**). Difference Array turns running totals back into increments (used for fast **range updates**) (Section 6.4).

**Q: Why does 2D Prefix Sum need to subtract the top-left corner?**
A: Because adding the "above" region and "left" region both include the top-left overlapping rectangle — subtracting it once removes the double-count (Inclusion-Exclusion Principle, Section 7.2).

**Q: Can Prefix Product be used the same way as Prefix Sum?**
A: With extreme caution — division-based range product queries break with zeros in the array and can suffer floating-point issues. Many "product" problems (e.g., Maximum Product Subarray) deliberately avoid straightforward prefix-product due to this (Section 4.4).

**Q: What is the most common bug when implementing Prefix Sum?**
A: Off-by-one errors from mixing inclusive and exclusive conventions (Sections 13.2–13.3).

**Q: Does Prefix Sum help with Sliding Window problems?**
A: They solve overlapping but distinct problem shapes — Prefix Sum excels at exact-target subarray counting and works with negative numbers; Sliding Window excels at monotonic window growth/shrink problems with non-negative constraints (Section 5.10, 9.3).

---

## 📌 Closing Summary

Prefix Sum is fundamentally about **one idea**: precompute a cumulative aggregate once, so that any range query becomes a single O(1) subtraction (or XOR, or lookup) instead of a fresh O(n) scan. Every variant in this handbook — XOR, Product, 2D, Difference Array, Modulo bucketing, Hash Map counting — is a reapplication of that same idea to a different operation or a different problem shape (query vs. update). Master the **universal formula**, the **hash-map generalization**, and the **2D inclusion-exclusion identity**, and you have covered the vast majority of Prefix-Sum-based interview and competitive-programming questions you will ever encounter.

