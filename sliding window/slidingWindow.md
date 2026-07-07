# THE COMPLETE SLIDING WINDOW HANDBOOK 
---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Python Implementation Foundations](#2-python-implementation-foundations)
3. [Types of Sliding Window](#3-types-of-sliding-window)
4. [Core Sliding Window Concepts](#4-core-sliding-window-concepts)
5. [Sliding Window vs Two Pointer](#5-sliding-window-vs-two-pointer)
6. [Problem Recognition](#6-problem-recognition)
7. [Fixed-Size Window Patterns](#7-fixed-size-window-patterns)
8. [Variable-Size Window Patterns](#8-variable-size-window-patterns)
9. [Frequency & Distinct-Element Windows](#9-frequency--distinct-element-windows)
10. [Applications](#10-applications)
11. [Optimization: Brute Force → Sliding Window](#11-optimization-brute-force--sliding-window)
12. [Interview Preparation](#12-interview-preparation)
13. [Python Tips & Idioms](#13-python-tips--idioms)
14. [Common Mistakes](#14-common-mistakes)
15. [Cheat Sheets & Templates](#15-cheat-sheets--templates)
16. [Practice Problem Bank](#16-practice-problem-bank)
17. [Final Revision](#17-final-revision)

---

# 1. Introduction

## 1.1 What is Sliding Window?

The **Sliding Window** technique is an algorithmic pattern that transforms a nested-loop, brute-force scan over a contiguous range of an array or string into a **single pass**, by maintaining a "window" — a contiguous subrange defined by two pointers, `left` and `right` — that expands and contracts as it slides over the data.

Instead of recomputing a result from scratch for every possible subarray/substring, the window **reuses previous computation** and only adjusts for the elements that enter or leave it.

> **Formal definition:** Given a sequence `A[0..n-1]`, a sliding window is a pair of indices `(left, right)` with `0 <= left <= right <= n-1` (or `right == n` meaning empty) such that all algorithmic work is confined to updating the aggregate state of `A[left..right]` as `left` and/or `right` move forward.

## 1.2 History & Origin

The idea traces back to classical **two-pointer** techniques used in merge-sort merging and partitioning, and to **amortized analysis** techniques in the study of streaming algorithms in the 1970s-80s (e.g., Munro–Paterson streaming median work). It was popularized in the coding-interview world through LeetCode-style problems from roughly 2015 onward, and today it is one of the "Big 5" interview patterns alongside Two Pointers, Fast & Slow Pointers, Binary Search, and BFS/DFS.

It is also a real production technique: **network congestion control (TCP sliding window protocol)**, **rate limiters**, **moving averages in time-series analytics**, and **log/stream processing** all use literal sliding windows.

## 1.3 Why Sliding Window Exists

Many problems ask: *"find the best/valid contiguous subarray or substring satisfying some property."*

A brute-force solution checks **every** subarray:

```python
n = len(arr)
best = None
for i in range(n):
    for j in range(i, n):
        window = arr[i:j+1]        # O(n) to build/scan
        # evaluate window            -> O(n)
        pass
# Total: O(n^3) or O(n^2) if evaluation is O(1)
```

This is `O(n^2)` or `O(n^3)`. Sliding Window exploits **monotonicity**: as `left` increases, information can only be removed; as `right` increases, information can only be added. Because each index enters and leaves the window **at most once**, the total work across the entire scan is `O(n)` — this is the key **amortized analysis** insight.

## 1.4 Intuition

Think of it as a **caterpillar** inching across a number line: its tail (`left`) and head (`right`) crawl forward, never backward. At every instant, the segment of ground between tail and head is "the window" and the caterpillar keeps a running summary (sum, count, frequency map) of what's inside it — updating that summary incrementally instead of re-measuring the whole segment each time.

## 1.5 Real-World Analogy

**Analogy — Train window scenery:** Imagine watching scenery from a moving train window of fixed width. As the train moves forward (right edge advances), new scenery enters on one side while old scenery exits on the other (left edge advances too, in lockstep) — you never have to "recompute" the entire view, you just track what changed.

**Analogy — Bank statement over trailing 30 days:** A "trailing 30-day spend" figure updates daily: add today's spend, subtract the spend from 31 days ago. You never re-sum the entire month from scratch.

## 1.6 Characteristics

| Characteristic | Description |
|---|---|
| Contiguity | Operates only on **contiguous** subarrays/substrings |
| Monotonic pointers | `left` and `right` only move forward, never backward |
| Amortized O(n) | Each element added/removed from window at most once (in most variants) |
| Incremental state | Aggregate (sum, count, map) updated in O(1) per step, not recomputed |
| Two flavors | Fixed-size window, Variable-size window |

## 1.7 Advantages

- Reduces `O(n^2)`/`O(n^3)` brute force to `O(n)`/`O(n log n)`.
- Low memory overhead — typically `O(1)` to `O(k)` extra space.
- Naturally suited to streaming data (you don't need the whole array in memory).
- Simple, reusable templates once mastered.

## 1.8 Disadvantages

- Only applies when the property being optimized is **monotonic/composable** over contiguous ranges (adding elements should predictably help or hurt validity — "shrinkability").
- Not directly applicable to **non-contiguous** subsequences.
- Can be tricky to get invariants right (off-by-one errors, wrong shrink conditions).
- Doesn't help when the window's aggregate can't be updated incrementally in O(1) (e.g., median of window without extra structures like heaps).

## 1.9 Applications (Preview)

- Substring/subarray search problems (interviews)
- Network protocols (TCP sliding window)
- Rate limiting / API throttling
- Time-series moving averages, stock analysis
- DNA sequence analysis (fixed-length k-mers)
- Log anomaly detection over trailing time windows
- Real-time analytics dashboards

## 1.10 Real-World Examples

| Domain | Example |
|---|---|
| Networking | TCP sliding window flow control |
| Finance | Moving average / rolling volatility of stock prices |
| DevOps | Rate limiter: "max 100 requests per 60-second window" |
| Bioinformatics | Scanning DNA for k-length motifs |
| NLP | N-gram generation over token streams |
| Video streaming | Buffering fixed-size chunks ahead of playback |

---

# 2. Python Implementation Foundations

## 2.1 Left & Right Pointers

Every sliding window uses two indices into the same sequence:

```python
left = 0
for right in range(len(arr)):
    # 1. include arr[right] into window state
    # 2. while window invalid: shrink by moving left forward
    # 3. (optionally) record result using current window [left, right]
    pass
```

**Key rule:** `right` is driven by a `for`/`enumerate` loop (always moves forward by exactly 1 per iteration). `left` is driven by a `while` loop **inside** the `for` loop (may move forward 0, 1, or many steps per iteration of `right`).

## 2.2 Window Maintenance

"Window state" is whatever aggregate you need to answer validity/optimality in O(1):

- A running `sum` (for sum-based windows)
- A `collections.Counter` / `dict` (for frequency-based windows: distinct chars, anagrams)
- A count of "bad" elements (for "at most K violations" windows)
- A `deque` of indices (for max/min-in-window problems — monotonic deque)

```python
from collections import Counter

window_sum = 0
window_freq = Counter()
```

## 2.3 `while` vs `for` Loop

| Loop | Role in Sliding Window |
|---|---|
| `for right in range(n)` | Drives window **expansion** — always exactly one step |
| `while <window invalid>` | Drives window **shrinking** — zero or more steps, nested inside the `for` |

```python
def template(arr, k):
    left = 0
    window_sum = 0
    best = 0
    for right in range(len(arr)):
        window_sum += arr[right]          # expand
        while window_sum > k:             # shrink while invalid
            window_sum -= arr[left]
            left += 1
        best = max(best, right - left + 1)
    return best
```

> **Warning:** Never use a `while` loop to drive `right` as well — that reintroduces `O(n^2)` behavior if not written carefully. `right` should be governed by the outer `for`.

## 2.4 `enumerate()`

Useful when you need both index and value of the right pointer, especially for character-position tracking:

```python
for right, ch in enumerate(s):
    # right is the index, ch is s[right]
    ...
```

## 2.5 `collections.Counter`

`Counter` is a `dict` subclass ideal for frequency-window problems (anagrams, permutations, minimum window substring):

```python
from collections import Counter
need = Counter("abc")     # Counter({'a':1,'b':1,'c':1})
window = Counter()
window[ch] += 1
if window[ch] > need[ch]:
    ...
```

**Tip:** `Counter` supports `==` comparison between two Counters directly (`window == need`), which is convenient but be aware it's `O(alphabet size)` per comparison — fine for fixed alphabets (26 lowercase letters), but track a separate `matched` counter for tighter O(1) checks in performance-critical code (see §9).

## 2.6 `defaultdict`

Useful when you don't want `KeyError`s and don't need Counter-specific arithmetic:

```python
from collections import defaultdict
freq = defaultdict(int)
freq[ch] += 1
```

## 2.7 `deque` (When Applicable)

For **monotonic deque** problems — e.g., "maximum of every window of size k" — a `deque` of indices keeps candidates in decreasing (or increasing) order of value:

```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()   # stores indices; nums[dq] is decreasing
    result = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

This is the standard **Sliding Window Maximum** (LeetCode 239) solution — `O(n)` because each index is pushed and popped from the deque at most once.

## 2.8 Best Practices

- Prefer `Counter`/`defaultdict` over manual `dict.get(key, 0)` bookkeeping — cleaner and less error-prone.
- Keep a **single source of truth** for "is window valid" — usually one integer counter (e.g., `distinct_count`, `mismatch_count`) rather than recomputing validity from the full frequency map each iteration.
- Always ask: *"What is the O(1) update when `right` enters?"* and *"What is the O(1) update when `left` leaves?"* — if you can't answer both, sliding window may not directly apply.
- Track the **answer** (best length, count, indices) inside the `for` loop, at the point where the window is known to be valid — don't defer it to after the loop.

## 2.9 Performance Considerations

- Avoid slicing (`arr[left:right+1]`) inside the loop — it creates a new list/string in `O(window size)`, destroying the `O(n)` guarantee. Track aggregates instead.
- String concatenation inside a loop (`result += ch`) is `O(n)` per op in the worst case due to immutability — use lists and `''.join()` if you must build strings.
- `len(dict)` and `Counter` membership checks are `O(1)` average case — safe to use freely.
- For very large inputs, prefer arrays (`list`) over generators when you need random access via indices.


# 3. Types of Sliding Window

## 3.1 Fixed Size Window

The window size `k` is **constant** throughout the scan. Once the window reaches size `k`, every subsequent step slides it by exactly one: one element enters on the right, exactly one leaves on the left.

```
Array: [2, 1, 5, 1, 3, 2],  k = 3

Step 1: [2 1 5] 1  3  2      sum = 8
Step 2:  2 [1 5 1] 3  2      sum = 7   (drop 2, add 1)
Step 3:  2  1 [5 1 3] 2      sum = 9   (drop 1, add 3)
Step 4:  2  1  5 [1 3 2]     sum = 6   (drop 5, add 2)
```

**Template:**

```python
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    best = window_sum
    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[right - k]
        best = max(best, window_sum)
    return best
```

## 3.2 Variable Size Window

The window **grows and shrinks** based on a condition (e.g., "longest substring with at most K distinct characters"). `right` always advances; `left` advances only when the window becomes invalid (or, in "at most" problems, to keep it valid).

```
Find longest subarray with sum <= 8:  [2, 1, 5, 1, 3, 2]

right=0: [2]            sum=2  ok        len=1
right=1: [2,1]          sum=3  ok        len=2
right=2: [2,1,5]        sum=8  ok        len=3
right=3: [2,1,5,1]      sum=9  shrink -> [1,5,1] sum=7  len=3
right=4: [1,5,1,3]      sum=10 shrink -> [5,1,3] sum=9 shrink -> [1,3] sum=4  len=2
right=5: [1,3,2]        sum=6  ok        len=3
```

## 3.3 Dynamic Window

A generalization of variable window where the **size itself is the answer being optimized** (either minimized, as in Minimum Window Substring, or maximized, as in Longest Substring Without Repeating Characters). The window has no target size in advance — it's driven purely by a validity predicate.

## 3.4 Frequency Window

Window state is a **frequency map** (character counts, element counts) rather than a scalar (sum). Used for anagram/permutation detection, "at most/exactly K distinct" problems.

## 3.5 Character Window

A specialization of Frequency Window applied to strings — tracks counts of characters (often over a fixed alphabet, e.g. 26 lowercase letters) to answer questions about substrings.

## 3.6 Numeric Window

Window state is numeric aggregates over arrays of numbers — sums, products, counts of elements satisfying a numeric predicate (e.g., "count of subarrays with product < k").

## 3.7 Multi-Condition Window

The validity of the window depends on **more than one constraint simultaneously** — e.g., "longest substring with at most 2 distinct characters AND no character appears more than 3 times." These require combining multiple counters/maps but the two-pointer skeleton remains unchanged.

## 3.8 Circular Window (Overview)

When the array is **circular** (e.g., "maximum sum of a circular subarray"), sliding window is typically combined with prefix sums or applied twice (once on the array doubled, `arr + arr`, restricted to length `< n`) or solved via the complementary "total sum − minimum subarray sum" trick. True sliding window logic itself doesn't change; only the array being scanned does.

```
Circular array: [5, -3, 5]
Doubled:        [5, -3, 5, 5, -3, 5]
Search windows of length < 3 in the doubled array for max sum,
or use Kadane's + total-sum-minus-min-subarray trick.
```

---

# 4. Core Sliding Window Concepts

## 4.1 Window Expansion

Expansion happens exactly once per outer-loop iteration: `right` moves forward, and the new element `arr[right]` is folded into the window's aggregate state.

```python
window_sum += arr[right]
window_freq[arr[right]] += 1
```

## 4.2 Window Shrinking

Shrinking happens **zero or more times** per outer-loop iteration, driven by a `while` loop that checks a validity condition. `arr[left]` is removed from the aggregate state before `left` advances.

```python
while <window invalid>:
    window_sum -= arr[left]
    window_freq[arr[left]] -= 1
    left += 1
```

## 4.3 Window Validation

A **validity check** decides whether the current window satisfies the problem's constraint. This can be:
- A direct comparison (`window_sum <= k`)
- A counter comparison (`distinct_count <= k`)
- A full map comparison (`window_freq == target_freq`) — expensive, prefer counters (§9.2)

## 4.4 Maintaining Invariants

An **invariant** is a property you guarantee is true at a specific point in the loop — e.g., "at the end of every iteration of `right`, the window `[left, right]` is valid." Sliding window correctness proofs almost always hinge on clearly stating the invariant and showing shrink/expand steps preserve it.

## 4.5 Frequency Counting

Central to character/frequency windows. Two common counter idioms:

```python
# Idiom A: Counter equality (simple, O(26) per check for lowercase alphabet)
if window_counter == target_counter: ...

# Idiom B: single integer "matches" counter (O(1) per check) -- preferred for perf
matches = 0
required = len(target_counter)
...
if window_counter[ch] == target_counter[ch]:
    matches += 1
if matches == required: ...
```

## 4.6 Window State

The minimum information needed to determine (a) validity and (b) the answer, without re-scanning the window. Examples: `window_sum`, `distinct_count`, `Counter`, `max_freq_char_count`.

## 4.7 Valid vs Invalid Window

| | Valid Window | Invalid Window |
|---|---|---|
| Meaning | Satisfies problem constraint | Violates problem constraint |
| Typical action | Record/update answer, then try to shrink further (for minimization) or extend (for maximization) | Must shrink (`left++`) until valid again |

## 4.8 Incremental Computation

The defining efficiency trick: computing `f(window after moving pointer)` from `f(window before moving pointer)` in `O(1)`, instead of recomputing from scratch in `O(window size)`. This is what makes the overall algorithm `O(n)` instead of `O(n^2)`.

```
Naive:      window_sum = sum(arr[left:right+1])       # O(window size) every step
Incremental: window_sum += arr[right]                  # O(1) on expand
             window_sum -= arr[left]                    # O(1) on shrink
```


# 5. Sliding Window vs Two Pointer

## 5.1 Similarities

- Both use two indices moving over a sequence.
- Both typically achieve `O(n)` time.
- Both avoid nested-loop brute force.
- Both rely on **monotonic pointer movement** (no backtracking).

## 5.2 Differences

| Aspect | Sliding Window | Two Pointer (general) |
|---|---|---|
| Contiguity | Always operates on a **contiguous** range `[left, right]` | Pointers can be anywhere — e.g., one at start, one at end (not necessarily contiguous span is "the answer") |
| Pointer origin | Both pointers typically start at index 0 and move in the **same direction** | Pointers often start at **opposite ends** and move toward each other, or at different starting points |
| State tracked | An aggregate over the *whole current range* (sum, freq map) | Often just the two pointed-to values themselves (e.g., `arr[i] + arr[j]`) |
| Typical problems | Longest/shortest substring, subarray sum/count problems | Two Sum (sorted array), container with most water, trapping rain water, palindrome check |
| Window concept | Explicit — window *is* the answer's shape | Implicit or absent — the pointers just narrow a search space |

## 5.3 Decision Tree

```
Is the problem about a CONTIGUOUS subarray/substring?
│
├── NO → Not sliding window. Consider: two pointers (opposite ends),
│         hashing, sorting, or other techniques.
│
└── YES → Does window size increase monotonically as you relax
          a constraint (i.e., "adding elements never help; only removing does" or vice versa)?
          │
          ├── YES → Sliding Window applies.
          │         │
          │         ├── Is window size FIXED (given as k)? → Fixed Window Template
          │         └── Is window size VARIABLE (longest/shortest/count)? → Variable Window Template
          │
          └── NO (non-monotonic constraint) → Sliding window does NOT
              directly apply; consider prefix sums + hashmap,
              DP, or divide & conquer instead.
```

## 5.4 Recognition Rules

Use Sliding Window when **all** of the following hold:
1. The problem talks about a **subarray** or **substring** (contiguous).
2. There's a **numeric or count-based property** to optimize or check (sum, length, distinct count, frequency).
3. Extending the window (adding an element) and shrinking it (removing an element) can each be evaluated in `O(1)` given the previous state.
4. The property is **monotonic**: if a window of length L is invalid, so is every superset window sliding the same start forward (or a similar monotonic argument holds) — this justifies never moving `left` backward.

## 5.5 Interview Clues

| Keyword / Phrase in Problem | Likely Technique |
|---|---|
| "contiguous subarray", "substring" | Sliding Window |
| "of size k" | Fixed Window |
| "longest", "shortest", "minimum length" + contiguous | Variable Window |
| "at most K distinct", "exactly K", "no more than" | Frequency Window |
| "two sorted arrays", "pair sum", "palindrome check" | Two Pointer (non-window) |
| "container", "trapping rain water" | Two Pointer (opposite ends) |
| "maximum in every window of size k" | Monotonic Deque |
| "median of window" | Two Heaps / Sorted structure + window |

## 5.6 When to Use Each

- **Use Sliding Window** when you need an aggregate (sum/count/frequency) over every contiguous range and ranges overlap/slide predictably.
- **Use (opposite-end) Two Pointer** when the array is sorted (or can be) and you're searching for a pair/triplet satisfying a condition, or narrowing from both ends based on comparing `arr[i]` and `arr[j]` directly (not an aggregate over a range).

## 5.7 Common Confusion

> **Confusion:** "Sliding Window" and "Two Pointer" are often used interchangeably in casual interview prep — technically, Sliding Window *is* a specific application of the two-pointer idea (same-direction pointers over a contiguous range with aggregate state), while "Two Pointer" more broadly includes opposite-direction techniques with no windowed aggregate at all. When in doubt, ask: *"Is there a contiguous range whose aggregate I'm tracking?"* If yes → sliding window. If it's just comparing two specific elements → plain two pointer.

---

# 6. Problem Recognition

## 6.1 Recognition Flowchart

```
                    ┌─────────────────────────────┐
                    │ Read the problem statement   │
                    └──────────────┬───────────────┘
                                   ▼
                 ┌───────────────────────────────────┐
                 │ Does it mention "subarray" /       │
                 │ "substring" / "contiguous"?        │
                 └───────────────┬────────────────────┘
                         NO      │      YES
                  ┌──────────────┘      └───────────────┐
                  ▼                                      ▼
       Consider other techniques              ┌─────────────────────────┐
       (DP, graphs, sorting, etc.)             │ Is a window SIZE given  │
                                                │ explicitly (k)?         │
                                                └───────────┬─────────────┘
                                                  YES        │      NO
                                          ┌───────────────────┘      └───────────────┐
                                          ▼                                          ▼
                              ┌───────────────────────┐               ┌───────────────────────────┐
                              │ FIXED-SIZE WINDOW     │               │ Is it "longest / shortest /│
                              │ Template               │               │ count of" a valid window?  │
                              └───────────────────────┘               └────────────┬───────────────┘
                                                                             YES     │
                                                                    ┌────────────────┘
                                                                    ▼
                                                       ┌─────────────────────────┐
                                                       │ VARIABLE-SIZE WINDOW    │
                                                       │ Template (grow + shrink)│
                                                       └─────────────────────────┘
```

## 6.2 Keywords Table

| Keyword | Interpretation |
|---|---|
| "subarray of size k" | Fixed window |
| "longest substring such that..." | Variable window, maximize length |
| "minimum window containing..." | Variable window, minimize length |
| "at most k distinct" | Variable window, `distinct <= k` invariant |
| "exactly k distinct" | `atMost(k) - atMost(k-1)` trick (see §9) |
| "number of subarrays with..." | Count-based variable window, often same `atMost` trick |
| "permutation of s1 in s2" | Fixed window (size `len(s1)`) + frequency match |
| "anagram" | Fixed window + frequency match |
| "replace at most k characters" | Variable window with a "max frequency character" tracker |

## 6.3 Window Size Selection

- If the problem gives you `k` directly → **fixed window** of size `k`.
- If the problem asks you to **find** the size (longest/shortest) → **variable window**.
- If the problem's constraint is about **counts of violations allowed** (e.g., "at most k zeros can be flipped") → variable window where shrink condition is `violations > k`.

## 6.4 Fixed vs Variable Decision Process

```python
# Ask yourself these three questions in order:

# Q1: Is a window length explicitly given?
#     e.g. "subarray of length k" -> FIXED
if explicit_length_given:
    use_fixed_window()

# Q2: Are you asked to MAXIMIZE or MINIMIZE the window length
#     subject to a constraint?
#     e.g. "longest substring with at most k distinct chars" -> VARIABLE
elif asked_to_optimize_length:
    use_variable_window()

# Q3: Are you asked to COUNT the number of valid contiguous
#     ranges satisfying a constraint?
#     e.g. "number of subarrays with sum == k" or "with at most k distinct"
else:
    use_variable_window_with_counting()  # often atMost(k) - atMost(k-1)
```


# 7. Fixed-Size Window Patterns

## 7.1 Maximum Sum Subarray of Size K

### Problem Statement
Given an array `arr` and an integer `k`, find the maximum sum of any contiguous subarray of size `k`.

### Approach
Brute force checks every window of size `k` and sums it: `O(n*k)`. Sliding window keeps a running sum and updates it in `O(1)` as the window slides by one: `O(n)`.

### Python Code

```python
def max_sum_subarray_k(arr, k):
    n = len(arr)
    if n < k:
        return None                       # not enough elements

    window_sum = sum(arr[:k])             # sum of first window
    best = window_sum

    for right in range(k, n):
        left = right - k
        window_sum += arr[right] - arr[left]   # slide: add new, remove old
        best = max(best, window_sum)

    return best
```

### Line-by-Line Explanation
- `n = len(arr)`: cache length to avoid recomputation.
- `if n < k: return None`: guard against impossible input.
- `window_sum = sum(arr[:k])`: build the very first window's sum in `O(k)` (one-time cost).
- `best = window_sum`: initialize best-so-far.
- `for right in range(k, n)`: `right` represents the new element entering; loop starts right after the first window.
- `left = right - k`: the index of the element about to leave (`k` positions behind `right`).
- `window_sum += arr[right] - arr[left]`: **the core trick** — add the incoming element, subtract the outgoing element, in `O(1)`.
- `best = max(best, window_sum)`: update running maximum.

### Dry Run

`arr = [2, 1, 5, 1, 3, 2]`, `k = 3`

| Step | Left | Right | Window | Action | window_sum | best |
|---|---|---|---|---|---|---|
| init | 0 | 2 | [2,1,5] | initial sum | 8 | 8 |
| 1 | 1 | 3 | [1,5,1] | +arr[3]=1, -arr[0]=2 | 8+1-2=7 | 8 |
| 2 | 2 | 4 | [5,1,3] | +arr[4]=3, -arr[1]=1 | 7+3-1=9 | 9 |
| 3 | 3 | 5 | [1,3,2] | +arr[5]=2, -arr[2]=5 | 9+2-5=6 | 9 |

**Answer: 9** (window `[5, 1, 3]`)

### Complexity Analysis
- Time: `O(n)` — one pass, `O(1)` work per step (plus one-time `O(k)` initial sum).
- Space: `O(1)` extra.

### Alternative Approaches
- **Brute force** `O(n*k)`: recompute sum for each window from scratch.
- **Prefix sum array** `O(n)` time, `O(n)` space: `prefix[i] = sum(arr[:i])`, then `window_sum = prefix[right+1] - prefix[left]`. Same time complexity as sliding window but uses `O(n)` extra space — sliding window is strictly better here.

### When to Use
Whenever window size `k` is **fixed** and you need an aggregate (sum, count, product) over every window.

### When NOT to Use
If `k` varies per query and you need many different `k` values against the same array, a **prefix sum array** (built once, `O(1)` query per `k`) is more efficient than re-running sliding window per query.

### Common Mistakes
- Off-by-one in `left = right - k` (should NOT be `right - k + 1` — verify against dry run).
- Forgetting the `n < k` edge case.
- Recomputing `sum(arr[left:right+1])` inside the loop (defeats the purpose — `O(n*k)`).

### Edge Cases
- `k > len(arr)` → no valid window exists.
- `k == len(arr)` → only one window, equal to `sum(arr)`.
- All negative numbers → still works; "maximum" sum may be the least negative.
- `k == 1` → equivalent to `max(arr)`.

---

## 7.2 Minimum Sum Window (Fixed Size)

### Problem Statement
Given an array and integer `k`, find the **minimum** sum among all contiguous subarrays of size `k`. (Mirror image of §7.1.)

### Python Code

```python
def min_sum_subarray_k(arr, k):
    n = len(arr)
    if n < k:
        return None

    window_sum = sum(arr[:k])
    best = window_sum

    for right in range(k, n):
        left = right - k
        window_sum += arr[right] - arr[left]
        best = min(best, window_sum)

    return best
```

### Dry Run

`arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]`, `k = 3`

| Step | Window | window_sum | best |
|---|---|---|---|
| init | [4,2,1] | 7 | 7 |
| 1 | [2,1,7] | 10 | 7 |
| 2 | [1,7,8] | 16 | 7 |
| 3 | [7,8,1] | 16 | 7 |
| 4 | [8,1,2] | 11 | 7 |
| 5 | [1,2,8] | 11 | 7 |
| 6 | [2,8,1] | 11 | 7 |
| 7 | [8,1,0] | 9 | 7 |

**Answer: 7**

### Complexity
`O(n)` time, `O(1)` space — identical structure to Maximum Sum Subarray, only `max`→`min` changes.

### Common Mistakes
Same class of mistakes as §7.1 — the logic is a mirror image, so bugs are symmetric (off-by-one, forgetting edge cases).

---

## 7.3 Maximum Average Subarray

### Problem Statement (LeetCode 643)
Given array `nums` and integer `k`, find the contiguous subarray of length `k` with the **maximum average**, and return that average.

### Approach
Since `k` is fixed, average = sum / k, and `k` is constant across all windows — so maximizing the average is equivalent to maximizing the sum. Reuse §7.1's exact logic, divide by `k` only once at the end.

### Python Code

```python
def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    best_sum = window_sum

    for right in range(k, len(nums)):
        left = right - k
        window_sum += nums[right] - nums[left]
        best_sum = max(best_sum, window_sum)

    return best_sum / k
```

### Dry Run

`nums = [1, 12, -5, -6, 50, 3]`, `k = 4`

| Step | Window | window_sum | best_sum |
|---|---|---|---|
| init | [1,12,-5,-6] | 2 | 2 |
| 1 | [12,-5,-6,50] | 2+50-1=51 | 51 |
| 2 | [-5,-6,50,3] | 51+3-12=42 | 51 |

**Answer: 51 / 4 = 12.75**

### Complexity
`O(n)` time, `O(1)` space.

### Common Mistakes
- Dividing by `k` inside the loop repeatedly (wasteful; do it once at the end).
- Using integer division (`//`) instead of true division (`/`) in Python 3 — always verify the expected return type (float vs int).

---

## 7.4 Fixed-Length String Problems — Permutation in String

### Problem Statement (LeetCode 567)
Given strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1` (i.e., one of `s1`'s anagrams is a **contiguous substring** of `s2`).

### Approach
Because a permutation of `s1` has the exact same length and character frequency as `s1`, this is a **fixed-size window** (size `len(s1)`) sliding over `s2`, checking if the window's character-frequency matches `s1`'s frequency.

### Python Code

```python
from collections import Counter

def check_inclusion(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return False

    need = Counter(s1)
    window = Counter(s2[:n1])

    if window == need:
        return True

    for right in range(n1, n2):
        left_char = s2[right - n1]
        right_char = s2[right]

        window[right_char] += 1              # expand
        window[left_char] -= 1               # shrink (implicit, fixed window)
        if window[left_char] == 0:
            del window[left_char]             # keep Counter clean for equality checks

        if window == need:
            return True

    return False
```

### Line-by-Line Explanation
- `need = Counter(s1)`: target frequency map.
- `window = Counter(s2[:n1])`: frequency map of the first window.
- The `for` loop slides the window one character at a time: increment the incoming char, decrement the outgoing char.
- `del window[left_char]` when count hits 0 keeps the Counter's key-set clean, so `window == need` compares correctly (a `Counter` with `{'a': 0}` is NOT `==` to one missing key `'a'` unless zero-count keys are removed... actually Python `Counter` equality *does* treat zero and missing as equal in Python 3.10+, but removing keeps behavior consistent and avoids `Counter.__eq__` edge-case surprises across versions).

### Dry Run

`s1 = "ab"`, `s2 = "eidbaooo"`

`need = {'a':1, 'b':1}`

| right | window before | left_char removed | right_char added | window after | match? |
|---|---|---|---|---|---|
| init(window=s2[:2]="ei") | {'e':1,'i':1} | - | - | {'e':1,'i':1} | No |
| 2 | {'e':1,'i':1} | 'e' (s2[0]) | 'd' (s2[2]) | {'i':1,'d':1} | No |
| 3 | {'i':1,'d':1} | 'i' (s2[1]) | 'b' (s2[3]) | {'d':1,'b':1} | No |
| 4 | {'d':1,'b':1} | 'd' (s2[2]) | 'a' (s2[4]) | {'b':1,'a':1} | **Yes** |

**Answer: True** (window "ba" at index 3-4 is a permutation of "ab")

### Complexity Analysis
- Time: `O(n2)` where `n2 = len(s2)` — each step does `O(1)` Counter updates; the `==` check is `O(alphabet size)` = `O(26)` = `O(1)` for lowercase English letters.
- Space: `O(alphabet size)` = `O(26)` = `O(1)`.

### Alternative Approaches
- Sort each window and compare to sorted `s1` — `O(n2 * k log k)`, much worse.
- Use a single `matches` integer counter (§9.2) to make the equality check strictly `O(1)` instead of `O(26)` — a further micro-optimization used in Minimum Window Substring style solutions.

### When to Use
Any "does an anagram/permutation of X appear in Y" problem.

### When NOT to Use
If characters come from a very large alphabet (e.g., unicode), the `O(alphabet)` comparisons become expensive — prefer the `matches` counter trick.

### Common Mistakes
- Forgetting to delete zero-count keys, causing subtle equality bugs in some Python versions/behaviors.
- Off-by-one on which index is "leaving" the window (`s2[right - n1]`, not `s2[right - n1 + 1]`).
- Not handling `len(s1) > len(s2)` upfront (guaranteed `False`).

### Edge Cases
- `s1` longer than `s2` → immediately `False`.
- `s1` and `s2` identical → `True` trivially (the whole string is the window).
- Repeated characters in `s1` (e.g., `"aab"`) — Counter handles multiplicities correctly.

---

## 7.5 Find All Anagrams in a String

### Problem Statement (LeetCode 438)
Given strings `s` and `p`, return the **starting indices** of all anagrams of `p` in `s`.

### Approach
Identical fixed-window-with-frequency-match logic as §7.4, except we **collect every matching start index** instead of stopping at the first.

### Python Code

```python
from collections import Counter

def find_anagrams(s, p):
    ns, npp = len(s), len(p)
    result = []
    if npp > ns:
        return result

    need = Counter(p)
    window = Counter(s[:npp])

    if window == need:
        result.append(0)

    for right in range(npp, ns):
        left_char = s[right - npp]
        right_char = s[right]

        window[right_char] += 1
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]

        if window == need:
            result.append(right - npp + 1)      # start index of current window

    return result
```

### Dry Run

`s = "cbaebabacd"`, `p = "abc"` → `need = {'a':1,'b':1,'c':1}`

| window start | window | match? |
|---|---|---|
| 0: "cba" | {'c':1,'b':1,'a':1} | Yes → append 0 |
| 1: "bae" | {'b':1,'a':1,'e':1} | No |
| 2: "aeb" | {'a':1,'e':1,'b':1} | No |
| 3: "eba" | {'e':1,'b':1,'a':1} | No |
| 4: "bab" | {'b':2,'a':1} | No |
| 5: "aba" | {'a':2,'b':1} | No |
| 6: "bac" | {'b':1,'a':1,'c':1} | Yes → append 6 |
| 7: "acd" | {'a':1,'c':1,'d':1} | No |

**Answer: [0, 6]**

### Complexity
Time `O(n)` (n = len(s)), Space `O(26)` = `O(1)`.

### Common Mistakes
- Recording the wrong start index (`right - npp + 1`, not `right - npp`).
- Not appending the very first window (index 0) before entering the loop.

### Edge Cases
- `p` longer than `s` → return `[]`.
- No anagram exists → return `[]`.
- Every window matches (e.g., `s = "aaaa"`, `p = "aa"`) → multiple overlapping matches.


# 8. Variable-Size Window Patterns

## 8.1 Longest Substring Without Repeating Characters

### Problem Statement (LeetCode 3)
Given a string `s`, find the length of the longest substring without repeating characters.

### Approach
**Brute force:** check every substring, verify uniqueness — `O(n^3)` (or `O(n^2)` with a set built incrementally).
**Sliding window:** expand `right`; whenever `s[right]` is already in the window, shrink `left` until the duplicate is removed. Track `best = max(best, right - left + 1)` at every step.

### Python Code

```python
def length_of_longest_substring(s):
    last_seen = {}          # char -> most recent index
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1        # jump left past the duplicate
        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best
```

### Line-by-Line Explanation
- `last_seen`: maps each character to the last index where it appeared.
- `if ch in last_seen and last_seen[ch] >= left`: only jump `left` if the earlier occurrence is **still inside** the current window (guards against stale/outdated indices from before `left`).
- `left = last_seen[ch] + 1`: jump left to just past the duplicate — an `O(1)` jump, avoiding a `while`-loop character-by-character shrink (a nice optimization over the "shrink one at a time with a set" version).
- `best = max(best, right - left + 1)`: window length is always `right - left + 1`.

### Dry Run

`s = "abcabcbb"`

| right | ch | last_seen[ch] before | left after | window | best |
|---|---|---|---|---|---|
| 0 | a | none | 0 | "a" | 1 |
| 1 | b | none | 0 | "ab" | 2 |
| 2 | c | none | 0 | "abc" | 3 |
| 3 | a | 0 (>=left=0) | 1 | "bca" | 3 |
| 4 | b | 1 (>=left=1) | 2 | "cab" | 3 |
| 5 | c | 2 (>=left=2) | 3 | "abc" | 3 |
| 6 | b | 4 (>=left=3) | 5 | "cb" | 3 |
| 7 | b | 6 (>=left=5) | 7 | "b" | 3 |

**Answer: 3** ("abc")

### Complexity Analysis
- Time: `O(n)` — each index visited once by `right`; `left` jumps directly (amortized `O(1)` overall, never revisits characters).
- Space: `O(min(n, alphabet size))` for the `last_seen` dict.

### Alternative Approaches
- **Set-based shrink**: maintain a `set` of characters in window; on duplicate, `while s[right] in window_set: window_set.remove(s[left]); left += 1`. Also `O(n)` amortized but does more per-character work than the direct-jump version above.
- **Brute force**: `O(n^2)` or `O(n^3)`.

### When to Use
Any "longest substring/subarray with all-unique elements" problem.

### When NOT to Use
If duplicates are allowed up to some count `k` (not zero) — that's a different pattern (§9, "at most K distinct" style, or "longest substring with at most 2 repeating chars").

### Common Mistakes
- Forgetting the `last_seen[ch] >= left` guard — without it, `left` can jump **backward**, corrupting the window (classic bug).
- Off-by-one: window length is `right - left + 1`, not `right - left`.
- Using a fixed-size array assuming ASCII when the input may contain full Unicode.

### Edge Cases
- Empty string → `0`.
- All unique characters → answer is `len(s)`.
- All identical characters (e.g., `"aaaa"`) → answer is `1`.

### Visualization

```
s = a  b  c  a  b  c  b  b
    ^0 ^1 ^2 ^3 ...

right=3 (s[3]='a'): duplicate of s[0].
Before jump:  L=0                R=3
              [a  b  c  a] <- invalid, 'a' repeats
After jump:       L=1        R=3
                  [b  c  a] <- valid again, length 3
```

---

## 8.2 Longest Repeating Character Replacement

### Problem Statement (LeetCode 424)
Given a string `s` and integer `k`, you may replace **at most `k` characters** in any substring so that the substring becomes all the same character. Return the length of the longest such substring achievable.

### Approach
A window `[left, right]` is valid if `(window length) - (count of most frequent character in window) <= k` — i.e., the number of characters you'd need to replace to make the whole window uniform is at most `k`. Track the max frequency character count (`max_freq`) as you expand; you don't need to *decrease* `max_freq` on shrink for correctness of the final answer (a subtle but important optimization — see notes).

### Python Code

```python
from collections import defaultdict

def character_replacement(s, k):
    freq = defaultdict(int)
    left = 0
    max_freq = 0          # highest frequency of any single char seen in current window
    best = 0

    for right, ch in enumerate(s):
        freq[ch] += 1
        max_freq = max(max_freq, freq[ch])

        window_len = right - left + 1
        if window_len - max_freq > k:
            freq[s[left]] -= 1
            left += 1
            # NOTE: max_freq is intentionally NOT recomputed here (see explanation)

        best = max(best, right - left + 1)

    return best
```

### Line-by-Line Explanation
- `freq[ch] += 1`: track character counts inside the window.
- `max_freq = max(max_freq, freq[ch])`: track the best (highest) single-character frequency ever seen *while expanding*.
- `window_len - max_freq > k`: this is the validity check — replacements needed exceed budget `k`.
- When invalid, shrink by one from the left (**not** a `while` loop — just one `if`!). This is a well-known micro-optimization: since we only care about the *maximum* window length ever achieved, it's safe to let `max_freq` be "stale" (an overestimate from an earlier, larger window) — the window can never shrink to something smaller than the best found so far, so an outdated `max_freq` cannot cause a false-positive increase in `best`.

### Dry Run

`s = "AABABBA"`, `k = 1`

| right | ch | freq | max_freq | window_len | valid? | left after | best |
|---|---|---|---|---|---|---|---|
| 0 | A | {A:1} | 1 | 1 | 1-1=0<=1 | 0 | 1 |
| 1 | A | {A:2} | 2 | 2 | 2-2=0<=1 | 0 | 2 |
| 2 | B | {A:2,B:1} | 2 | 3 | 3-2=1<=1 | 0 | 3 |
| 3 | A | {A:3,B:1} | 3 | 4 | 4-3=1<=1 | 0 | 4 |
| 4 | B | {A:3,B:2} | 3 | 5 | 5-3=2>1 | shrink: remove s[0]='A' -> {A:2,B:2}, left=1 | 4 |
| 5 | B | {A:2,B:3} | 3 | 5 (right=5,left=1) | 5-3=2>1 | shrink: remove s[1]='A' -> {A:1,B:3}, left=2 | 4 |
| 6 | A | {A:2,B:3} | 3 | 5 (right=6,left=2) | 5-3=2>1 | shrink: remove s[2]='B' -> {A:2,B:2}, left=3 | 4 |

**Answer: 4** (e.g., "AABA" → replace one B → "AAAA")

### Complexity Analysis
- Time: `O(n)` — `right` and `left` each advance at most `n` times total.
- Space: `O(alphabet size)` = `O(26)` = `O(1)` for uppercase English letters.

### Alternative Approaches
- Recompute `max_freq = max(freq.values())` on every shrink — correct but `O(alphabet)` per shrink, so `O(26n)` total; still technically `O(n)` for fixed alphabets but slower in practice and unnecessary.

### When to Use
"At most k replacements/removals to make a substring uniform/valid" problems.

### When NOT to Use
When the "budget" `k` interacts with **multiple different constraints simultaneously** in a way that a single `max_freq` scalar can't capture — then you may need to track more state.

### Common Mistakes
- Believing `max_freq` must be decremented on shrink — it must NOT be, for the optimization above to remain correct for the *maximum length* answer (though it would still be "conceptually accurate" per-window if recomputed, it's unnecessary work).
- Off-by-one in `window_len - max_freq > k` vs `>= k` (must be strictly greater to trigger shrink).

### Edge Cases
- `k >= len(s)` → answer is `len(s)` (can replace everything).
- `k == 0` → answer is the longest run of a single repeated character already present.
- Single character string → answer is `1`.

---

## 8.3 Minimum Window Substring

### Problem Statement (LeetCode 76)
Given strings `s` and `t`, return the minimum window substring of `s` that contains **every character of `t`** (including duplicates). Return `""` if no such window exists.

### Approach
This is the canonical **variable window, minimize length, frequency-based** problem. Expand `right` until the window contains all of `t`'s characters (with correct multiplicities); then greedily shrink `left` as much as possible while the window remains valid, recording the best (smallest) valid window found. Use a `matches` counter to check validity in `O(1)` instead of comparing full frequency maps.

### Python Code

```python
from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    need = Counter(t)
    required = len(need)          # number of DISTINCT chars that must be fully satisfied

    window_freq = {}
    formed = 0                    # number of distinct chars currently satisfying need's count

    left = 0
    best_len = float('inf')
    best_left = 0

    for right, ch in enumerate(s):
        window_freq[ch] = window_freq.get(ch, 0) + 1

        if ch in need and window_freq[ch] == need[ch]:
            formed += 1

        # Try to shrink as much as possible while window is fully valid
        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_left = left

            left_char = s[left]
            window_freq[left_char] -= 1
            if left_char in need and window_freq[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return "" if best_len == float('inf') else s[best_left:best_left + best_len]
```

### Line-by-Line Explanation
- `need = Counter(t)`: required character counts.
- `required = len(need)`: number of *distinct* characters that must be satisfied (not total count).
- `formed`: how many distinct characters currently have their required count fully met inside the window.
- `window_freq[ch] == need[ch]` (checked **exactly**, at the moment it's reached) increments `formed` — this avoids double-counting if a character's count keeps growing past what's needed.
- The `while formed == required` inner loop is where **all the shrinking happens** — this is a maximize-then-minimize pattern: expand until valid, then shrink as far as possible while still valid, recording the best window at every fully-valid state.
- `window_freq[left_char] < need[left_char]` after decrementing signals we've broken validity for that character, decrementing `formed`.

### Dry Run

`s = "ADOBECODEBANC"`, `t = "ABC"` → `need = {A:1, B:1, C:1}`, `required = 3`

| right | ch | window_freq (relevant) | formed | shrink? | best window so far |
|---|---|---|---|---|---|
| 0-3 | A,D,O,B | A:1,B:1 | 2 | no | - |
| 4 | E | - | 2 | no | - |
| 5 | C | A:1,B:1,C:1 | 3 | **yes** → shrink from left=0 | window "ADOBEC" len 6, best_len=6 |
| | | shrink removes A(idx0) → formed drops to 2, left=1 | | | |
| 6 | O | | 2 | no | best_len=6 |
| 7 | D | | 2 | no | best_len=6 |
| 8 | E | | 2 | no | best_len=6 |
| 9 | B | B:2 (was already >=1, formed unaffected for B) | 2 | no | best_len=6 |
| 10 | A | A:1 again | 3 | **yes** → shrink | window s[1..10]="DOBECODEBA" too big, shrink continues |
| | | shrink removes chars from left until formed<3 | | eventually finds "BANC" as tighter valid window later | |
| 11 | N | | | | |
| 12 | C | | 3 (again) | shrink finds window "BANC" (indices 9-12), len 4 | best_len=4 |

**Answer: "BANC"** (length 4) — this is the well-known expected output for this classic example.

### Complexity Analysis
- Time: `O(|s| + |t|)` — building `need` is `O(|t|)`; the main loop's `right` and `left` each move at most `|s|` times total (amortized `O(n)` despite the nested `while`).
- Space: `O(|s| + |t|)` in the worst case for the frequency maps (bounded by alphabet size in practice).

### Alternative Approaches
- Filter `s` to only characters present in `t` first (an optimization when `t`'s alphabet is much smaller than `s`) — reduces constant factor, not asymptotic complexity.

### When to Use
"Minimum window/substring/subarray containing all of X" problems — the signature "minimize length, must satisfy exact frequency requirement" problem.

### When NOT to Use
If you need **maximum** length instead of minimum — that's a different shrink strategy (shrink only when *invalid*, not "while valid").

### Common Mistakes
- Using `window_freq == need` (full dict comparison) inside the hot loop instead of the `formed`/`required` integer trick — correctness is fine but performance suffers on large alphabets.
- Incrementing/decrementing `formed` based on `>=` instead of `==`/`<` transitions — leads to incorrect counts when a character's frequency overshoots `need[ch]` multiple times.
- Forgetting `t` can have duplicate characters (`"AABC"` requires **two** A's) — must use `Counter`, not a `set`.

### Edge Cases
- `t` longer than `s` → impossible, return `""`.
- `t` has characters not present anywhere in `s` → return `""`.
- `s == t` → the whole string is the answer.

---

## 8.4 Fruit Into Baskets

### Problem Statement (LeetCode 904)
Given an array of tree types (`fruits`), you have exactly 2 baskets, each can hold only **one type** of fruit (unlimited quantity of that type). Find the length of the longest contiguous subarray containing at most 2 distinct fruit types.

### Approach
This is exactly the **"longest subarray with at most K distinct elements"** pattern with `K = 2`. Maintain a frequency map; when distinct count exceeds 2, shrink from the left until it's back to 2.

### Python Code

```python
from collections import defaultdict

def total_fruit(fruits):
    count = defaultdict(int)
    left = 0
    best = 0

    for right, fruit in enumerate(fruits):
        count[fruit] += 1

        while len(count) > 2:
            left_fruit = fruits[left]
            count[left_fruit] -= 1
            if count[left_fruit] == 0:
                del count[left_fruit]
            left += 1

        best = max(best, right - left + 1)

    return best
```

### Dry Run

`fruits = [1, 2, 1, 2, 3, 3, 1]`

| right | fruit | count | distinct | shrink? | window | best |
|---|---|---|---|---|---|---|
| 0 | 1 | {1:1} | 1 | no | [1] | 1 |
| 1 | 2 | {1:1,2:1} | 2 | no | [1,2] | 2 |
| 2 | 1 | {1:2,2:1} | 2 | no | [1,2,1] | 3 |
| 3 | 2 | {1:2,2:2} | 2 | no | [1,2,1,2] | 4 |
| 4 | 3 | {1:2,2:2,3:1} | 3 | yes→ remove fruits[0]=1: {1:1,2:2,3:1}, left=1 | [2,1,2,3] | 4 |
| 5 | 3 | {1:1,2:2,3:2} | 3 | yes→ remove fruits[1]=2: {1:1,2:1,3:2}, left=2 | [1,2,3,3] | 4 |
| 6 | 1 | {1:2,2:1,3:2} | 3 | yes→ remove fruits[2]=1: {2:1,3:2}, left=3 → still 2 distinct? {2:1,3:2} has 2 keys, stop | [2,3,3,1] | 4 |

**Answer: 4**

### Complexity
`O(n)` time, `O(1)` space (at most 3 distinct fruit types tracked at any instant before shrinking).

### When to Use
"At most K distinct elements in a subarray" — direct template, just swap `2` for any `K`.

### Common Mistakes
- Forgetting to `del` zero-count entries — causes `len(count)` to overcount distinct types.
- Off-by-one: the answer uses `right - left + 1`, computed **after** the shrink loop finishes.

### Edge Cases
- All same fruit type → answer is `len(fruits)`.
- Only 2 distinct types total → answer is `len(fruits)`.
- Array has fewer than 2 elements → trivial answers (0 or 1).

---

## 8.5 Max Consecutive Ones III (Longest Ones After Replacement)

### Problem Statement (LeetCode 1004)
Given a binary array `nums` and integer `k`, return the maximum number of consecutive 1's if you can flip at most `k` 0's to 1's.

### Approach
Track `zero_count` in the window. Window is valid while `zero_count <= k`. Shrink when it exceeds `k`.

### Python Code

```python
def longest_ones(nums, k):
    left = 0
    zero_count = 0
    best = 0

    for right, val in enumerate(nums):
        if val == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

### Dry Run

`nums = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`

| right | val | zero_count | valid? | left after | window len | best |
|---|---|---|---|---|---|---|
| 0-2 | 1,1,1 | 0 | yes | 0 | 1,2,3 | 3 |
| 3 | 0 | 1 | yes(<=2) | 0 | 4 | 4 |
| 4 | 0 | 2 | yes(<=2) | 0 | 5 | 5 |
| 5 | 0 | 3 | no→shrink until zero_count<=2: remove nums[0]=1(no change),left=1; remove nums[1]=1(no change),left=2; remove nums[2]=1(no change),left=3; remove nums[3]=0→zero_count=2,left=4 | 2 | 4 | 5 (right=5,left=4 → len=2) | 5 |
| 6-9 | 1,1,1,1 | 2 | yes | 4 | up to len=6 (right=9,left=4) | 6 |
| 10 | 0 | 3 | no→shrink: remove nums[4]=0→zero_count=2,left=5 | 2 | 6 (right=10,left=5) | 6 |

**Answer: 6**

### Complexity
`O(n)` time, `O(1)` space.

### Common Mistakes
- Using `if` instead of `while` for shrinking (must fully restore validity, and in rare adversarial inputs more than one shrink step may be needed after certain jumps — always prefer `while` for safety unless you've proven a single step suffices).
- Forgetting this is the **same template** as "longest substring with at most k distinct" — many learners re-derive it from scratch instead of recognizing the pattern.

### Edge Cases
- `k >= count of zeros in array` → answer is `len(nums)`.
- No zeros at all → answer is `len(nums)` regardless of `k`.
- `k == 0` → equivalent to "longest run of consecutive 1's" (classic Max Consecutive Ones I).

---

## 8.6 Binary Subarrays With Sum (overview)

### Problem Statement (LeetCode 930)
Given a binary array `nums` and integer `goal`, return the number of non-empty subarrays with sum exactly `goal`.

### Approach
Counting problems over "at most" constraints are solved via the **`atMost(k) - atMost(k-1)`** trick (detailed fully in §9.4): `exactly(goal) = atMost(goal) - atMost(goal - 1)`, where `atMost(k)` counts subarrays with sum `<= k`.

```python
def num_subarrays_with_sum(nums, goal):
    def at_most(k):
        if k < 0:
            return 0
        left = 0
        total = 0
        window_sum = 0
        for right, v in enumerate(nums):
            window_sum += v
            while window_sum > k:
                window_sum -= nums[left]
                left += 1
            total += right - left + 1     # count of subarrays ending at `right`
        return total

    return at_most(goal) - at_most(goal - 1)
```

**Why `right - left + 1` counts subarrays:** every subarray `[i, right]` for `left <= i <= right` has sum `<= k` (since removing elements from the front of a valid window can only keep it valid, for non-negative arrays) — so there are exactly `right - left + 1` valid subarrays ending at `right`.

### Complexity
`O(n)` time (two passes of `at_most`), `O(1)` space.

### Edge Cases
- `goal == 0` → careful, `at_most(-1)` must return `0` explicitly (guarded in code above).
- All zeros → many subarrays possible if `goal == 0`.

---

## 8.7 Nice Subarrays (overview)

### Problem Statement (LeetCode 1248)
A subarray is "nice" if it has exactly `k` **odd** numbers. Count the number of nice subarrays.

### Approach
Transform: replace every odd number with `1` and every even number with `0`; the problem becomes identical to §8.6 ("Binary Subarrays With Sum", with `goal = k`).

```python
def number_of_subarrays(nums, k):
    binary = [1 if x % 2 == 1 else 0 for x in nums]
    return num_subarrays_with_sum(binary, k)   # reuse §8.6 exactly
```

### Key Insight
Recognizing that a problem **reduces** to a previously-solved pattern via a simple transform is a high-value interview skill — always ask "can I simplify this input to match a template I already know?"


# 9. Frequency & Distinct-Element Windows

## 9.1 At Most K Distinct

### Problem Statement (LeetCode 340)
Find the length of the longest substring with **at most** `k` distinct characters.

### Python Code

```python
from collections import defaultdict

def length_of_longest_substring_k_distinct(s, k):
    if k == 0:
        return 0

    count = defaultdict(int)
    left = 0
    best = 0

    for right, ch in enumerate(s):
        count[ch] += 1

        while len(count) > k:
            left_ch = s[left]
            count[left_ch] -= 1
            if count[left_ch] == 0:
                del count[left_ch]
            left += 1

        best = max(best, right - left + 1)

    return best
```

This is structurally **identical** to Fruit Into Baskets (§8.4) with `k` generalized instead of hard-coded to `2` — confirming that recognizing this as one reusable template pays off across many problems.

### Dry Run

`s = "eceba"`, `k = 2`

| right | ch | count | distinct | shrink? | window | best |
|---|---|---|---|---|---|---|
| 0 | e | {e:1} | 1 | no | "e" | 1 |
| 1 | c | {e:1,c:1} | 2 | no | "ec" | 2 |
| 2 | e | {e:2,c:1} | 2 | no | "ece" | 3 |
| 3 | b | {e:2,c:1,b:1} | 3 | yes→remove s[0]='e':{e:1,c:1,b:1},left=1→still 3 distinct→remove s[1]='c':{e:1,b:1},left=2→2 distinct,stop | "eb" | 3 |
| 4 | a | {e:1,b:1,a:1} | 3 | yes→remove s[2]='e':{b:1,a:1},left=3 | "ba" | 3 |

**Answer: 3** ("ece")

### Complexity
`O(n)` time, `O(k)` space.

### Common Mistakes
- Not special-casing `k == 0` (would otherwise loop forever trying to shrink below 0 distinct, or misbehave).
- Using `while len(count) > k` is correct; using `if` instead of `while` is a bug because a single shrink step might not be enough after previously jumping right sometimes it is (in this exact problem it usually is one at a time since `right` moves one step at a time, but always default to `while` for safety — see §14).

### Edge Cases
- `k >= number of distinct characters in s` → answer is `len(s)`.
- `k == 0` → answer is `0` (no substring can have 0 distinct chars and non-zero length).

---

## 9.2 Exactly K Distinct

### Problem Statement (LeetCode 992 style)
Count the number of subarrays with **exactly** `k` distinct integers.

### Approach — The `atMost(k) - atMost(k-1)` Trick

Directly enforcing "exactly K" with a sliding window is awkward because "exactly" is **not monotonic** in the same simple way "at most" is (adding an element can take you from exactly-K to more-than-K, or from less-than-K to exactly-K — shrinking doesn't have one clean direction). The elegant fix:

```
exactly(K) = atMost(K) - atMost(K - 1)
```

Because: the count of subarrays with **at most K** distinct minus the count with **at most K-1** distinct leaves exactly the subarrays with **precisely K** distinct (every subarray with `<= K-1` distinct is "double counted" and cancels out).

### Python Code

```python
from collections import defaultdict

def subarrays_with_k_distinct(nums, k):
    def at_most(k):
        if k < 0:
            return 0
        count = defaultdict(int)
        left = 0
        total = 0
        for right, v in enumerate(nums):
            count[v] += 1
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            total += right - left + 1     # number of subarrays ending at `right` with <=k distinct
        return total

    return at_most(k) - at_most(k - 1)
```

### Why `total += right - left + 1` Works
For a fixed `right`, every subarray `[i, right]` where `left <= i <= right` automatically has `<= k` distinct elements too (since it's a sub-range of an already-valid range, and removing elements from the front can't increase distinct count). So there are exactly `right - left + 1` such subarrays ending at this `right`.

### Dry Run (for `at_most`)

`nums = [1,2,1,2,3]`, computing `at_most(2)`:

| right | v | count | distinct | shrink? | left | total += (right-left+1) | total |
|---|---|---|---|---|---|---|---|
| 0 | 1 | {1:1} | 1 | no | 0 | +1 | 1 |
| 1 | 2 | {1:1,2:1} | 2 | no | 0 | +2 | 3 |
| 2 | 1 | {1:2,2:1} | 2 | no | 0 | +3 | 6 |
| 3 | 2 | {1:2,2:2} | 2 | no | 0 | +4 | 10 |
| 4 | 3 | {1:2,2:2,3:1} | 3 | yes→remove nums[0]=1:{1:1,2:2,3:1},left=1→3 distinct still→remove nums[1]=2:{1:1,2:1,3:1},left=2→3 distinct still→remove nums[2]=1:{2:1,3:1},left=3→2 distinct,stop | 3 | +2 | 12 |

`at_most(2) = 12`. Similarly compute `at_most(1)`, then `exactly(2) = at_most(2) - at_most(1)`.

### Complexity
`O(n)` per `at_most` call, so `O(n)` overall (two calls, constants don't matter for Big-O).

### When to Use
Any "exactly K" counting problem over subarrays/substrings involving distinct-element or frequency constraints where "at most" is easy but "exactly" isn't directly expressible with a single monotonic window.

### Common Mistakes
- Forgetting the `k - 1 < 0` guard (must return `0`, not error or negative behavior).
- Trying to write "exactly K" sliding window logic directly without the subtraction trick — usually leads to bugs because "exactly K" is not itself monotonic.

---

## 9.3 At Least K

### Problem Statement Pattern
Count subarrays/substrings with **at least** `k` distinct elements (or at least `k` of some property).

### Approach
`atLeast(k) = total_subarrays - atMost(k - 1)`

Total number of subarrays of an array of length `n` is `n*(n+1)/2`. Subtracting those with fewer than `k` (`atMost(k-1)`) leaves those with at least `k`.

```python
def at_least_k_distinct(nums, k):
    n = len(nums)
    total_subarrays = n * (n + 1) // 2
    return total_subarrays - at_most(k - 1)   # at_most from §9.2
```

### Common Mistakes
- Forgetting total subarray count formula `n*(n+1)/2` (off-by-one is common here — verify with small example, e.g. `n=3` → `3*4/2=6` subarrays: `[0],[1],[2],[0,1],[1,2],[0,1,2]` = 6, correct).

---

## 9.4 Window with Hash Map vs Window with Set

| Structure | Use When | Distinct Count Check | Example Problems |
|---|---|---|---|
| `Counter` / `dict` (hash map) | Need **frequency** (how many times each element appears) | `len(map)` | Minimum Window Substring, At Most K Distinct, Anagrams |
| `set` | Only need **presence** (yes/no), not counts | `len(set)` | Longest Substring Without Repeating Characters (alternate impl) |

### Set-Based Longest Unique Substring (Alternative to §8.1)

```python
def length_of_longest_substring_set(s):
    seen = set()
    left = 0
    best = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        best = max(best, right - left + 1)
    return best
```

This is `O(n)` amortized (each character added/removed from the set at most once) but slightly less efficient in constant factor than the direct-jump `last_seen` dict version in §8.1, since it may shrink one-at-a-time instead of jumping `left` directly. Both are valid `O(n)` — prefer whichever is clearer to you in an interview.

## 9.5 Window with Queue/Deque (Concept Only)

For problems needing the **max or min of every window** (not frequency, but order statistics), a **monotonic deque** (§2.7) is the standard tool — it maintains candidates in sorted order so the front of the deque is always the current window's max (or min) in `O(1)` per query, with amortized `O(1)` updates.

```
Monotonic decreasing deque holds INDICES; front = index of window's max value.

nums = [1,3,-1,-3,5,3,6,7], k = 3

i=0: deque=[0]                          (value 1)
i=1: 3>=1, pop 0; deque=[1]             (value 3)
i=2: deque=[1,2]                        (values 3,-1) window[0..2] max=3
i=3: deque=[1,2,3]                      (values 3,-1,-3) window[1..3] max=3
i=4: 5>=-3 pop3; 5>=-1 pop2; 5>=3 pop1; deque=[4]   window[2..4] max=5
...
```


# 10. Applications

## 10.1 Streaming Data

Sliding window is a natural fit for **streaming** contexts where you cannot store the whole dataset — only a bounded recent window matters (e.g., "average of last 100 sensor readings"). Because the window's aggregate is updated incrementally, memory stays bounded at `O(k)` or `O(1)` regardless of total stream length.

```python
from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.window = deque()
        self.window_sum = 0

    def next(self, val):
        self.window.append(val)
        self.window_sum += val
        if len(self.window) > self.size:
            self.window_sum -= self.window.popleft()
        return self.window_sum / len(self.window)
```

## 10.2 Text Processing

Substring search, plagiarism detection (k-gram hashing / Rabin-Karp uses a **rolling hash**, itself a sliding-window sum-like computation), spell-checkers scanning fixed-length windows.

## 10.3 String Algorithms

Sliding window underlies fixed-length hashing in **Rabin-Karp** pattern matching: the rolling hash of a window of length `m` is updated in `O(1)` as the window slides, exactly analogous to the running-sum trick in §7.1.

```python
def rabin_karp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []

    base, mod = 256, 10**9 + 7
    high_order = pow(base, m - 1, mod)

    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod

    result = []
    for i in range(n - m + 1):
        if window_hash == pattern_hash and text[i:i+m] == pattern:
            result.append(i)
        if i < n - m:
            window_hash = (
                (window_hash - ord(text[i]) * high_order) * base + ord(text[i + m])
            ) % mod

    return result
```

## 10.4 Array Processing

Subarray sum/product/count problems (this handbook's core focus, §7-9).

## 10.5 Analytics

Rolling metrics in dashboards: trailing 7-day active users, trailing 30-day revenue — computed via the exact same "add new day, remove day that fell out of window" incremental update.

## 10.6 Signal Processing

Moving-average filters (smoothing noisy signals) and windowed FFT analysis (spectrograms) use literal sliding windows over sample arrays, often with overlap.

## 10.7 Time Series

Anomaly detection: flag a data point if it deviates significantly from the trailing window's mean/std-dev — requires an efficiently-updated running mean and variance (Welford's algorithm combined with sliding window eviction).

## 10.8 Network Monitoring

Rate limiting ("sliding window counter" and "sliding window log" algorithms) enforce limits like "max 100 requests per rolling 60-second window" — a direct real-world analogue of the interview pattern:

```python
import time
from collections import deque

class SlidingWindowRateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = deque()

    def allow_request(self):
        now = time.time()
        while self.requests and self.requests[0] <= now - self.window_seconds:
            self.requests.popleft()
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False
```

---

# 11. Optimization: Brute Force → Sliding Window

## 11.1 The General Transformation

```python
# STAGE 1: Brute Force -- O(n^2) or O(n^3)
def brute_force(arr, k):
    n = len(arr)
    best = 0
    for i in range(n):
        window_sum = 0
        for j in range(i, min(i + k, n)):
            window_sum += arr[j]     # O(k) recompute per starting index i
        best = max(best, window_sum)
    return best

# STAGE 2: Remove Nested Loop -- reuse previous window's sum
def sliding_window(arr, k):
    n = len(arr)
    window_sum = sum(arr[:k])
    best = window_sum
    for right in range(k, n):
        window_sum += arr[right] - arr[right - k]   # O(1) incremental update
        best = max(best, window_sum)
    return best
```

## 11.2 Removing Nested Loops

The single biggest optimization sliding window offers is turning an **inner recomputation loop** into an **O(1) incremental update**. Always ask: *"What changed between this window and the previous one?"* Usually the answer is "one element left, one element entered" — that's your `O(1)` update rule.

## 11.3 Incremental Updates — Checklist

| Aggregate | Incremental Update Rule |
|---|---|
| Sum | `window_sum += arr[right] - arr[left_removed]` |
| Count of elements matching predicate | `+1 if pred(arr[right]) else 0`, `-1 if pred(arr[left_removed]) else 0` |
| Frequency map | `freq[arr[right]] += 1`, `freq[arr[left_removed]] -= 1` (delete zero entries) |
| Product | `window_product *= arr[right]`, `window_product //= arr[left_removed]` (careful with zeros!) |
| Max/Min in window | Requires a monotonic deque (§2.7, §9.5) — cannot be updated with plain O(1) arithmetic |

## 11.4 Space Optimization

Most sliding window solutions need only `O(1)` or `O(k)`/`O(alphabet size)` extra space — dramatically better than a `O(n)` prefix-sum-array or `O(n^2)` memoized table used by naive DP-style solutions to the same problems.

## 11.5 Time Optimization Summary

| Approach | Typical Time Complexity |
|---|---|
| Brute force (rebuild window each time) | `O(n^2)` to `O(n^3)` |
| Prefix sums (precompute, O(1) query) | `O(n)` time, `O(n)` space |
| Sliding Window | `O(n)` time, `O(1)` to `O(k)` space |
| Sliding Window + Monotonic Deque | `O(n)` time (amortized), `O(k)` space |


# 12. Interview Preparation

## 12.1 Difficulty Progression

| Level | Problems | Focus |
|---|---|---|
| Easy | Max Consecutive Ones I, Maximum Average Subarray, Contains Duplicate II | Fixed windows, basic frequency |
| Medium | Longest Substring Without Repeating Characters, Longest Repeating Char Replacement, Permutation in String, Find All Anagrams, Fruit Into Baskets, Max Consecutive Ones III, Subarray Product Less Than K | Variable windows, frequency maps |
| Hard | Minimum Window Substring, Sliding Window Maximum, Subarrays with K Different Integers, Minimum Number of K Consecutive Bit Flips | Combined counters, monotonic deque, multi-constraint windows |

## 12.2 Pattern-Wise Question Map

| Pattern | Representative Problems |
|---|---|
| Fixed window, sum/average | Max Sum Subarray Size K, Maximum Average Subarray I |
| Fixed window, frequency match | Permutation in String, Find All Anagrams in a String |
| Variable window, no-repeat | Longest Substring Without Repeating Characters |
| Variable window, budgeted replacement | Longest Repeating Character Replacement, Max Consecutive Ones III |
| Variable window, minimize length | Minimum Window Substring, Minimum Size Subarray Sum |
| Variable window, at most K distinct | Longest Substring with At Most K Distinct Characters, Fruit Into Baskets |
| Counting via atMost trick | Subarrays with K Different Integers, Binary Subarrays With Sum, Count Nice Subarrays |
| Monotonic deque | Sliding Window Maximum |

## 12.3 Company-Wise Tendencies (General Patterns Observed)

> Note: exact questions asked rotate frequently and vary by team; the table below reflects commonly reported **pattern emphasis**, not guaranteed questions.

| Company | Commonly Emphasized Patterns |
|---|---|
| Amazon | Fixed/variable window sums, minimum window substring style |
| Google | Longest substring variants, combined constraint windows |
| Microsoft | Anagram/permutation window problems |
| Meta | Minimum window substring, subarray counting with atMost trick |
| FAANG generally | Sliding Window Maximum (monotonic deque) as a "hard" bar-raiser question |

## 12.4 Blind 75 / NeetCode Sliding Window Problems

- Best Time to Buy and Sell Stock (a degenerate/implicit "window" via single-pass min-tracking)
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Minimum Window Substring
- Sliding Window Maximum

## 12.5 Frequently Asked Interview Questions (FAQ Style)

**Q: How do you prove a sliding window solution is O(n) despite the nested while loop?**
A: Amortized analysis — argue that `left` can advance at most `n` times in total across the *entire* run of the algorithm (it never resets backward), so even though a single iteration of the outer loop might trigger multiple inner-loop shrink steps, the **sum of all shrink steps across the whole run** is bounded by `n`. Total work is `O(n) + O(n) = O(n)`.

**Q: When should I use `while` vs `if` for shrinking?**
A: Default to `while` unless you can prove a single shrink step always restores validity (true in some fixed-window problems where at most one element enters/leaves per step). `while` is always safe; `if` is a micro-optimization only valid in specific cases.

**Q: How do I decide the initial window state before the loop starts?**
A: For fixed windows, pre-populate the first `k` elements outside the loop, then slide starting at index `k`. For variable windows, start with an empty window (`left = 0`, aggregates at their identity value: `0` for sums, empty `Counter()` for frequency) and let the `for` loop naturally build it up from scratch.

**Q: What's the standard way to return indices, not just length?**
A: Track `best_left` (or `best_start`) alongside `best_len`, updated at the same point you update `best_len`, then slice `arr[best_left:best_left+best_len]` at the end (see Minimum Window Substring, §8.3).

## 12.6 Interview Tricks

- Say the **brute force** out loud first, then say "I can optimize this because as the window slides, only one element enters and one leaves" — interviewers want to see you *derive* the optimization, not just recite a memorized template.
- Explicitly state your **invariant** ("at the end of every outer-loop iteration, `[left, right]` is a valid/maximal window") before coding — this catches bugs before you write a single line.

## 12.7 Standard Templates (Quick Reference)

**Fixed Window Template:**
```python
def fixed_window_template(arr, k):
    window_val = init_aggregate(arr[:k])
    best = window_val
    for right in range(k, len(arr)):
        left = right - k
        window_val = update_add(window_val, arr[right])
        window_val = update_remove(window_val, arr[left])
        best = combine(best, window_val)
    return best
```

**Variable Window Template (Maximize length, shrink only when invalid):**
```python
def variable_window_max_template(arr):
    left = 0
    state = init_state()
    best = 0
    for right in range(len(arr)):
        state = add(state, arr[right])
        while not is_valid(state):
            state = remove(state, arr[left])
            left += 1
        best = max(best, right - left + 1)
    return best
```

**Variable Window Template (Minimize length, shrink while valid):**
```python
def variable_window_min_template(arr):
    left = 0
    state = init_state()
    best = float('inf')
    for right in range(len(arr)):
        state = add(state, arr[right])
        while is_valid(state):
            best = min(best, right - left + 1)
            state = remove(state, arr[left])
            left += 1
    return best if best != float('inf') else 0
```

---

# 13. Python Tips & Idioms

## 13.1 `Counter` Recap
```python
from collections import Counter
c = Counter("mississippi")   # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
c.most_common(2)              # [('i', 4), ('s', 4)]
c.subtract(Counter("is"))     # in-place subtraction
+c                            # drops zero and negative counts (neat idiom!)
```

## 13.2 `defaultdict` Recap
```python
from collections import defaultdict
d = defaultdict(int)     # missing keys default to 0
d = defaultdict(list)    # missing keys default to []
```

## 13.3 `deque` Recap
```python
from collections import deque
dq = deque()
dq.append(x)       # O(1) add right
dq.appendleft(x)    # O(1) add left
dq.pop()            # O(1) remove right
dq.popleft()        # O(1) remove left  <-- this is why deque beats list for windows (list.pop(0) is O(n)!)
```

## 13.4 `set` Recap
```python
s = set()
s.add(x)       # O(1) average
s.discard(x)   # O(1) average, no error if missing (unlike s.remove(x))
```

## 13.5 `enumerate()` Recap
```python
for i, val in enumerate(arr):        # default start=0
for i, val in enumerate(arr, start=1):
```

## 13.6 Performance Tips

- **Never** use `list.pop(0)` inside a hot loop — it's `O(n)`. Use `collections.deque` for O(1) pops from either end.
- **Never** slice (`arr[left:right+1]`) inside the loop just to inspect the window — maintain aggregates instead.
- Prefer `dict`/`Counter` membership tests (`in`) — average `O(1)` — over scanning lists.
- Use `sys.stdin` fast input methods for competitive programming with large inputs (`import sys; input = sys.stdin.readline`).
- Cache `len(arr)` in a variable if used repeatedly in a hot loop (minor CPython overhead saved).

## 13.7 Memory Optimization

- For character-only problems restricted to lowercase English letters, a **fixed-size list of 26 ints** (`[0]*26`) is often faster than a `dict`/`Counter` due to lower overhead:

```python
freq = [0] * 26
freq[ord(ch) - ord('a')] += 1
```

- Avoid building intermediate lists/strings (e.g., `list(s)`) when you can iterate directly.

## 13.8 Common Python Pitfalls

- `Counter() == {}` behaves inconsistently across mental models — always test edge cases explicitly (empty dict vs empty Counter comparisons are fine, but be careful comparing Counters with **zero-value keys** left in them across Python versions).
- Mutable default arguments (`def f(cache={})`) — never use for windowed algorithms holding state across calls; state should be local to the function invocation.
- Integer overflow is **not a concern in Python** (arbitrary precision ints), unlike C++/Java — but be aware this can hide bugs that would otherwise surface as overflow in other languages during competitive programming portability.

---

# 14. Common Mistakes

## 14.1 Forgetting to Shrink

The single most common bug: expanding the window (`right` moves) but never checking/enforcing the shrink condition, silently allowing an **invalid** window to be treated as valid. Always pair every `add()` with a corresponding validity check.

## 14.2 Shrinking Too Early or Too Aggressively

Shrinking before the window is actually invalid throws away valid, potentially-optimal windows. Always place the shrink `while`/`if` condition to trigger **only** when the true invariant is broken — verify with a dry run on a small example.

## 14.3 Wrong Window Size

Off-by-one errors are extremely common:
```python
window_len = right - left + 1     # CORRECT
window_len = right - left         # WRONG (off by one)
```

## 14.4 Incorrect Frequency Updates

Forgetting to delete zero-count keys from a `Counter`/`dict` when doing distinct-count checks (`len(count)`) leads to overcounting distinct elements — a very common silent bug.

## 14.5 Missing Edge Cases

- Empty input array/string.
- `k` larger than array length.
- `k == 0`.
- All elements identical.
- Target pattern longer than the source (`len(t) > len(s)`).

## 14.6 Infinite Loops

Usually caused by:
- Forgetting to increment `left` inside a `while` shrink loop.
- A shrink condition that can never become false given a bug in the update logic (e.g., updating the wrong variable).

## 14.7 Wrong Pointer Movement

- Moving `left` backward (never should happen in classic sliding window — always monotonic forward).
- Advancing `right` inside the shrink `while` loop by mistake (mixing up which pointer belongs to which loop).

## 14.8 Incorrect Validity Checks

- Using `>` when you meant `>=` (or vice versa) in the shrink condition — always trace through a boundary-case dry run (e.g., window exactly at the limit `k`) to confirm.
- Comparing `Counter`s for equality when a cheaper integer `matches`/`formed` counter would be both faster and less error-prone (§8.3, §9.2).


# 15. Cheat Sheets & Templates

## 15.1 Fixed Window Template (Cheat Sheet)

```python
def fixed_window(arr, k):
    window = sum(arr[:k])          # or Counter(arr[:k]) for frequency problems
    best = window
    for right in range(k, len(arr)):
        left = right - k
        window += arr[right] - arr[left]     # O(1) slide
        best = max(best, window)             # or min(), or comparison logic
    return best
```

## 15.2 Variable Window Template (Cheat Sheet)

```python
def variable_window(arr):
    left = 0
    state = {}                      # or 0, or Counter(), depending on problem
    best = 0                        # or float('inf') for minimization
    for right in range(len(arr)):
        # 1. Expand: fold arr[right] into state
        while <window invalid>:      # or `if`, when appropriate
            # 2. Shrink: remove arr[left] from state
            left += 1
        # 3. Update answer using current [left, right]
    return best
```

## 15.3 Complexity Table

| Pattern | Time | Space |
|---|---|---|
| Fixed window sum/avg | O(n) | O(1) |
| Fixed window frequency match | O(n) | O(alphabet) |
| Variable window (no-repeat) | O(n) | O(alphabet) |
| Variable window (budgeted replace) | O(n) | O(alphabet) |
| Minimum window substring | O(n + m) | O(alphabet) |
| At most / exactly / at least K distinct | O(n) | O(k) or O(alphabet) |
| Monotonic deque (max/min in window) | O(n) amortized | O(k) |
| Rolling hash (Rabin-Karp) | O(n + m) average | O(1) |

## 15.4 Pattern Recognition Guide (Quick Table)

| Signal in Problem | Template to Reach For |
|---|---|
| "size k" given | Fixed Window |
| "longest ... at most/no more than k [violations/distinct]" | Variable Window, maximize |
| "minimum window ... contains all of" | Variable Window, minimize (formed/required counters) |
| "number of subarrays/substrings with exactly k ..." | atMost(k) − atMost(k−1) |
| "number of subarrays with at least k ..." | total − atMost(k−1) |
| "maximum/minimum of every window of size k" | Monotonic Deque |
| "permutation/anagram of X in Y" | Fixed window + frequency match |

## 15.5 Window Decision Tree (Text Form)

```
contiguous? --NO--> not sliding window
    |YES
size given (k)? --YES--> FIXED WINDOW
    |NO
optimize length (longest/shortest)? --YES--> VARIABLE WINDOW (max or min template)
    |NO
count subarrays matching exact condition? --YES--> atMost(k) - atMost(k-1) trick
    |NO
need max/min value inside every window? --YES--> MONOTONIC DEQUE
```

## 15.6 Python Syntax Cheat Sheet

```python
from collections import Counter, defaultdict, deque

Counter(iterable)          # build frequency map
Counter.most_common(n)     # top n frequent elements
defaultdict(int)           # auto-zero missing keys
deque()                    # O(1) append/pop both ends
enumerate(iterable, start=0)
sum(iterable[:k])          # initial window sum
```

## 15.7 Common Conditions Reference

| Condition | Meaning |
|---|---|
| `window_sum <= target` | Sum-based validity |
| `len(count) <= k` | At most k distinct |
| `len(count) == k` | Exactly k distinct (careful — non-monotonic, use atMost trick for counting) |
| `window_len - max_freq <= k` | Budgeted replacement validity |
| `formed == required` | Frequency-match validity (Minimum Window Substring style) |
| `zero_count <= k` | Budgeted flips validity |

---

# 16. Practice Problem Bank

## 16.1 Fixed Window

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Maximum Sum Subarray of Size K | GeeksforGeeks | Easy | Fixed sum window | geeksforgeeks.org |
| Maximum Average Subarray I | LeetCode 643 | Easy | Fixed sum/average window | leetcode.com/problems/maximum-average-subarray-i |
| Permutation in String | LeetCode 567 | Medium | Fixed frequency window | leetcode.com/problems/permutation-in-string |
| Find All Anagrams in a String | LeetCode 438 | Medium | Fixed frequency window | leetcode.com/problems/find-all-anagrams-in-a-string |
| Repeated DNA Sequences | LeetCode 187 | Medium | Fixed window + hashing | leetcode.com/problems/repeated-dna-sequences |

## 16.2 Variable Window — Longest

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Longest Substring Without Repeating Characters | LeetCode 3 | Medium | No-repeat variable window | leetcode.com/problems/longest-substring-without-repeating-characters |
| Longest Repeating Character Replacement | LeetCode 424 | Medium | Budgeted replacement | leetcode.com/problems/longest-repeating-character-replacement |
| Fruit Into Baskets | LeetCode 904 | Medium | At most 2 distinct | leetcode.com/problems/fruit-into-baskets |
| Longest Substring with At Most K Distinct Characters | LeetCode 340 | Medium | At most k distinct | leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters |
| Max Consecutive Ones III | LeetCode 1004 | Medium | Budgeted flips | leetcode.com/problems/max-consecutive-ones-iii |
| Longest Subarray of 1's After Deleting One Element | LeetCode 1493 | Medium | Budgeted flips (k=1) | leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element |

## 16.3 Variable Window — Shortest / Minimum

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Minimum Window Substring | LeetCode 76 | Hard | Minimize length, frequency match | leetcode.com/problems/minimum-window-substring |
| Minimum Size Subarray Sum | LeetCode 209 | Medium | Minimize length, sum >= target | leetcode.com/problems/minimum-size-subarray-sum |
| Smallest Subarray with Sum Greater than X | InterviewBit | Medium | Minimize length, sum window | interviewbit.com |

## 16.4 Frequency / Distinct Element Windows

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Subarrays with K Different Integers | LeetCode 992 | Hard | atMost(k) − atMost(k−1) | leetcode.com/problems/subarrays-with-k-different-integers |
| Binary Subarrays With Sum | LeetCode 930 | Medium | atMost trick | leetcode.com/problems/binary-subarrays-with-sum |
| Count Number of Nice Subarrays | LeetCode 1248 | Medium | Reduction + atMost trick | leetcode.com/problems/count-number-of-nice-subarrays |
| Subarray Product Less Than K | LeetCode 713 | Medium | Product-based variable window | leetcode.com/problems/subarray-product-less-than-k |

## 16.5 Monotonic Deque

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Sliding Window Maximum | LeetCode 239 | Hard | Monotonic deque | leetcode.com/problems/sliding-window-maximum |
| Shortest Subarray with Sum at Least K | LeetCode 862 | Hard | Monotonic deque + prefix sum | leetcode.com/problems/shortest-subarray-with-sum-at-least-k |

## 16.6 String Algorithms Adjacent

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Rabin-Karp Substring Search | GeeksforGeeks | Medium | Rolling hash window | geeksforgeeks.org |
| Anagram Substring Search | HackerRank | Medium | Fixed frequency window | hackerrank.com |

## 16.7 Competitive Programming

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Two Pointers/Sliding Window practice set | CSES Problem Set | Varies | Multiple | cses.fi/problemset |
| Sliding Window problems | Codeforces (tag: two pointers) | Varies | Multiple | codeforces.com |
| String matching / windows | AtCoder | Varies | Multiple | atcoder.jp |
| Array/window based problems | CodeChef | Varies | Multiple | codechef.com |

## 16.8 Extra Practice (Code360 / GfG)

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Longest K unique characters substring | Code360 | Medium | At most k distinct |
| Distinct elements in every window | GeeksforGeeks | Medium | Sliding window + hashmap |
| First negative number in every window of size k | GeeksforGeeks | Medium | Fixed window + deque |


# 17. Final Revision

## 17.1 One-Page Notes

- Sliding Window solves **contiguous** subarray/substring problems in `O(n)` by maintaining an incrementally-updated aggregate.
- Two flavors: **Fixed size** (slide by exactly 1, add + remove 1 element per step) and **Variable size** (expand with `right`, shrink with `left` under a `while`/`if` validity check).
- The key skill is defining, for your specific problem: (1) what state to track, (2) the O(1) add rule, (3) the O(1)/O(shrink-steps) remove rule, (4) the validity condition, (5) where in the loop to record the answer.
- "Exactly K" counting problems: use `atMost(K) - atMost(K-1)`.
- "At least K" counting problems: use `total_subarrays - atMost(K-1)`.
- Max/min **inside** every window (not just aggregate) → Monotonic Deque, not a plain sliding window.

## 17.2 Mind Map (Text Form)

```
SLIDING WINDOW
├── Fixed Size
│   ├── Sum/Average (Max Sum Subarray, Max Average Subarray)
│   └── Frequency Match (Permutation in String, Find All Anagrams)
├── Variable Size — Maximize
│   ├── No violations allowed (Longest Substring Without Repeating Chars)
│   ├── Budgeted violations (Longest Repeating Char Replacement, Max Consecutive Ones III)
│   └── At most K distinct (Fruit Into Baskets, Longest Substring K Distinct)
├── Variable Size — Minimize
│   └── Frequency-match shrink-while-valid (Minimum Window Substring, Min Size Subarray Sum)
├── Counting
│   ├── atMost(k) - atMost(k-1)  -> exactly K
│   └── total - atMost(k-1)      -> at least K
└── Order Statistics in Window
    └── Monotonic Deque (Sliding Window Maximum)
```

## 17.3 Pattern Map (Quick Association Table)

| If you see... | Think... |
|---|---|
| "size k" | Fixed Window |
| "longest" | Variable Window, maximize |
| "minimum window / shortest" | Variable Window, minimize |
| "exactly k" | atMost trick |
| "at least k" | total − atMost(k−1) |
| "maximum of every window" | Monotonic Deque |
| "permutation/anagram" | Fixed window + frequency |

## 17.4 Window Templates (Consolidated)

```python
# FIXED
def fixed(arr, k):
    agg = init(arr[:k]); best = agg
    for right in range(k, len(arr)):
        agg = update(agg, add=arr[right], remove=arr[right-k])
        best = combine(best, agg)
    return best

# VARIABLE - MAXIMIZE
def variable_max(arr):
    left = 0; state = init_state(); best = 0
    for right in range(len(arr)):
        state = add(state, arr[right])
        while not valid(state):
            state = remove(state, arr[left]); left += 1
        best = max(best, right - left + 1)
    return best

# VARIABLE - MINIMIZE
def variable_min(arr):
    left = 0; state = init_state(); best = float('inf')
    for right in range(len(arr)):
        state = add(state, arr[right])
        while valid(state):
            best = min(best, right - left + 1)
            state = remove(state, arr[left]); left += 1
    return best
```

## 17.5 Recognition Flowchart (Compact)

```
contiguous? -> size given? -> FIXED
            -> optimize length? -> VARIABLE (max/min)
            -> count exact/at-least? -> atMost trick
            -> need max/min IN window? -> MONOTONIC DEQUE
            -> else -> not sliding window
```

## 17.6 Complexity Sheet (Compact)

| Pattern | Time | Space |
|---|---|---|
| Fixed window | O(n) | O(1)/O(alphabet) |
| Variable window | O(n) | O(1)/O(k) |
| Min window substring | O(n+m) | O(alphabet) |
| atMost/exactly/atLeast counting | O(n) | O(k) |
| Monotonic deque | O(n) amortized | O(k) |

## 17.7 Interview Cheat Sheet (Say This Out Loud)

1. "This is a contiguous subarray/substring problem, so I'll consider Sliding Window."
2. "Is the window size fixed or do I need to find it? [state answer]"
3. "My window state will be: [sum / Counter / distinct count / max_freq]."
4. "My validity condition is: [state it explicitly]."
5. "I'll expand with `right` every iteration, and shrink with `left` in a `while` loop whenever the window becomes invalid."
6. "This is O(n) because both pointers move forward at most n times total across the whole run — amortized analysis."

## 17.8 15-Minute Revision

- Reread §17.1 One-Page Notes.
- Recite the 3 core templates (§17.4) from memory.
- Mentally dry-run Longest Substring Without Repeating Characters (§8.1) and Minimum Window Substring (§8.3) — these two problems alone cover 80% of the interview surface area for this topic.
- Recall the atMost(k) − atMost(k−1) trick and why it's needed (non-monotonicity of "exactly").

## 17.9 1-Hour Revision Plan

| Time | Activity |
|---|---|
| 0–10 min | Reread §1 Introduction and §4 Core Concepts (why sliding window works — amortized O(n) argument) |
| 10–25 min | Re-derive and code §7.1 (Max Sum Subarray K) and §7.4 (Permutation in String) from scratch, no peeking |
| 25–45 min | Re-derive and code §8.1 (Longest Substring Without Repeating), §8.2 (Longest Repeating Char Replacement), §8.3 (Minimum Window Substring) |
| 45–55 min | Re-derive §9.2 (Exactly K Distinct via atMost trick) and §9.5 (Monotonic Deque concept) |
| 55–60 min | Skim §15 Cheat Sheets and §14 Common Mistakes once more before an interview |

## 17.10 FAQ Recap

**Q: Is Sliding Window the same as Two Pointer?**
A: Sliding Window is a specific, same-direction application of the two-pointer idea over a *contiguous* range with an aggregate state; general Two Pointer also includes opposite-direction techniques with no windowed aggregate (§5).

**Q: How do I know if my window state update is truly O(1)?**
A: Ask: "does updating my state when one element enters/leaves require looking at anything other than that single element and my current aggregate?" If yes to needing more, it's not O(1) and sliding window may need modification (e.g., a monotonic deque for max/min).

**Q: What's the most common bug?**
A: Forgetting to remove a zero-count entry from a frequency map, which corrupts `len(map)`-based distinct-count checks (§14.4).

---

