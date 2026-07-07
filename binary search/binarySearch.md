# The Complete Binary Search Handbook (Python Edition)

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Python Binary Search Tooling](#2-python-binary-search-tooling)
3. [Binary Search Fundamentals](#3-binary-search-fundamentals)
4. [Binary Search Templates](#4-binary-search-templates)
5. [Binary Search Patterns](#5-binary-search-patterns)
6. [Binary Search on Answer](#6-binary-search-on-answer)
7. [Applications](#7-applications)
8. [Problem Recognition](#8-problem-recognition)
9. [Optimization: Brute Force → Binary Search](#9-optimization-brute-force--binary-search)
10. [Interview Preparation](#10-interview-preparation)
11. [Python Tips & Idioms](#11-python-tips--idioms)
12. [Common Mistakes](#12-common-mistakes)
13. [Cheat Sheets](#13-cheat-sheets)
14. [Practice Problems](#14-practice-problems)
15. [Final Revision](#15-final-revision)
16. [FAQs](#16-faqs)

> **How to use this handbook:** Read Sections 1–4 linearly if you're building fundamentals. If you already know the basics, jump straight to Section 5 (Patterns) and Section 6 (Binary Search on Answer) — these are where most interview difficulty lives. Section 13 is a fast-access cheat sheet.

---

## 1. Introduction

### 1.1 What is Binary Search?

**Binary Search** is a search algorithm that finds the position of a target value (or a boundary of a property) within a **sorted, monotonic search space** by repeatedly dividing that space in half.

Instead of checking every element one by one (linear search, `O(n)`), binary search eliminates **half of the remaining candidates** at every step, giving `O(log n)` time complexity.

> **Formal definition:** Given a sorted array `A` of size `n` and a target `t`, binary search finds an index `i` such that `A[i] == t` (or determines no such index exists) in `O(log n)` comparisons.

The deeper, more powerful definition (used constantly in interviews and competitive programming) is:

> Binary search finds the **boundary point** in a search space where a **monotonic boolean predicate** `P(x)` flips from `False` to `True` (or `True` to `False`).

This second definition is the one that unlocks "Binary Search on Answer" problems, which don't look like searching at all.

### 1.2 History

- The idea of repeatedly halving a search interval resembles the **bisection method** in numerical analysis (root-finding for continuous functions), used long before computers.
- The first published binary search algorithm for computers is attributed to John Mauchly (1946).
- Despite its simplicity, a **correct, bug-free binary search implementation eluded most programmers for decades** — Jon Bentley's *Programming Pearls* noted that most published implementations contained bugs (an overflow bug in `mid = (low + high) / 2` shipped in Java's `Arrays.binarySearch` for years).
- Lesson: binary search is **conceptually trivial but implementation-hostile**. That's why this handbook obsesses over templates and boundary conditions.

### 1.3 Why Binary Search Exists

Linear search costs `O(n)`. As `n` grows (millions/billions of records), `O(n)` becomes unusable. Binary search exists because:

- Many datasets are **sorted or sortable once, queried many times** — pay `O(n log n)` once to sort, then `O(log n)` per query.
- Many problems that don't look like "search" are actually **"find the boundary where an answer becomes feasible"** — and feasibility is usually monotonic.

### 1.4 Divide and Conquer Intuition

Binary Search is the simplest possible **Divide and Conquer** algorithm:

| Step | Divide and Conquer | Binary Search |
|---|---|---|
| Divide | Split problem into subproblems | Split search space into halves |
| Conquer | Solve subproblems recursively | Recurse into ONE half only |
| Combine | Merge results | No merge needed — answer is in the chosen half |

Because binary search only recurses into **one half** (not both, like merge sort):

```
T(n) = T(n/2) + O(1) = O(log n)
```

versus merge sort's `T(n) = 2T(n/2) + O(n) = O(n log n)`.

### 1.5 Search Space Reduction — ASCII Visualization

```
Search space of 16 elements, target = 7

Index:   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
Value:   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
                                     ^
                                  target

Step 1: low=0, high=15, mid=7  -> A[7]=8 > 7  -> search LEFT half
[ 1   2   3   4   5   6   7   8 ] 9  10  11  12  13  14  15  16
  L                   M       H

Step 2: low=0, high=6, mid=3   -> A[3]=4 < 7  -> search RIGHT half
  1   2   3 [ 4   5   6   7 ]  8
  L           M           H

Step 3: low=4, high=6, mid=5   -> A[5]=6 < 7  -> search RIGHT half
              4 [ 5   6   7 ]  8
                  L   M   H

Step 4: low=6, high=6, mid=6   -> A[6]=7 == 7 -> FOUND at index 6
                      6
                     L,M,H  -> return 6
```

Each step **halves** the candidate range: 16 → 8 → 4 → 2 → 1, i.e. `log2(16) = 4` steps — matching `O(log n)`.

### 1.6 Preconditions for Binary Search

1. **Sorted order** (for classic search) — non-decreasing or non-increasing.
2. **Random access** in `O(1)` — arrays qualify; plain linked lists do NOT (access cost destroys the complexity benefit).
3. **Monotonicity** (for predicate-based / "search on answer" problems) — the predicate `P(x)` must look like `False False False ... True True True` (or the reverse), with no interleaving.

> ⚠️ **Warning:** Binary search on an unsorted or non-monotonic space gives **silently wrong answers** — it terminates and returns *something*, but that something may be garbage. Always verify the precondition first.

### 1.7 Characteristics

| Property | Value |
|---|---|
| Time Complexity | `O(log n)` |
| Space Complexity (iterative) | `O(1)` |
| Space Complexity (recursive) | `O(log n)` (call stack) |
| Requires sorted input | Yes |
| In-place | Yes |
| Paradigm | Divide and Conquer |

### 1.8 Advantages

- Extremely fast: `O(log n)` vs `O(n)` for linear search.
- Simple to reason about once the template is internalized.
- Generalizes far beyond arrays — works on **any monotonic predicate over any ordered domain** (integers, floats, "days", "capacities", "speeds").
- Low memory footprint (iterative version is `O(1)`).

### 1.9 Disadvantages

- Requires sorted / monotonic data — sorting costs `O(n log n)` if not already sorted.
- Not suitable for structures without efficient random access (e.g., linked lists).
- Easy to get boundary conditions wrong — a huge fraction of real-world bugs.
- Doesn't handle duplicates "specially" without extra logic (need first/last occurrence variants).

### 1.10 Applications (Preview)

- Searching sorted arrays/lists; finding insertion points (`bisect.insort`).
- Database index lookups (B-Trees internally generalize binary search).
- Version control bisecting (`git bisect`).
- Optimization problems: "minimum capacity to ship packages in D days", "Koko eating bananas", "allocate books/pages".
- Numerical methods: root-finding via the bisection method.
- ML hyperparameter search along a monotonic axis (overview only).

### 1.11 Real-World Examples

- **Dictionary lookup**: flipping to roughly the middle, then narrowing left/right.
- **Guessing game**: "Guess a number 1–100" using "higher/lower" hints.
- **`git bisect`**: binary searches commit history to find the first "bad" commit, using build-and-test as the predicate.
- **Search engines**: sorted term dictionaries use binary search / B-Trees for prefix lookups.

---

## 2. Python Binary Search Tooling

Python ships a battle-tested binary search module: **`bisect`**. Understanding it deeply — and knowing when *not* to use it — is a core interview and real-world skill.

### 2.1 The `bisect` Module Overview

```python
import bisect

# Core functions
bisect.bisect_left(a, x, lo=0, hi=len(a))    # leftmost insertion point
bisect.bisect_right(a, x, lo=0, hi=len(a))   # rightmost insertion point (alias: bisect.bisect)
bisect.insort_left(a, x)                      # insert x keeping a sorted (leftmost)
bisect.insort_right(a, x)                     # insert x keeping a sorted (rightmost) (alias: bisect.insort)
```

All operate in `O(log n)` for the **search** portion; `insort` is `O(n)` overall because list insertion shifts elements.

### 2.2 `bisect_left` vs `bisect_right` — The Most Important Distinction in Python Binary Search

Given a sorted array `a` and value `x`:

- **`bisect_left(a, x)`** returns the **leftmost** index `i` such that `a[i-1] < x <= a[i]`. Inserting `x` at `i` keeps the array sorted, with `x` going **before** any existing equal elements.
- **`bisect_right(a, x)`** returns the leftmost index `i` such that `a[i-1] <= x < a[i]`. `x` goes **after** any existing equal elements.

```
a = [1, 3, 3, 3, 5, 7]
       0  1  2  3  4  5

bisect_left(a, 3)  -> 1   (before the first 3)
bisect_right(a, 3) -> 4   (after the last 3)
```

ASCII view:

```
Index:   0   1   2   3   4   5
Value:   1   3   3   3   5   7
             ^           ^
       bisect_left(3)  bisect_right(3)
             |___________|
             the "equal range" for 3 is [1, 4)
             so count of 3s = 4 - 1 = 3
```

> **Interview Tip:** `bisect_right(a, x) - bisect_left(a, x)` gives the **count of occurrences** of `x` in `a` in `O(log n)`. This one line replaces an entire "count occurrences" template.

### 2.3 `bisect_left`/`bisect_right` as Lower Bound / Upper Bound

| Python function | Classic CS name | Returns |
|---|---|---|
| `bisect_left(a, x)` | Lower Bound | first index where `a[i] >= x` |
| `bisect_right(a, x)` | Upper Bound | first index where `a[i] > x` |

### 2.4 Using `bisect` for Common Problems

**Find first occurrence of `x`:**
```python
import bisect

def first_occurrence(a, x):
    i = bisect.bisect_left(a, x)
    if i < len(a) and a[i] == x:
        return i
    return -1
```

**Find last occurrence of `x`:**
```python
def last_occurrence(a, x):
    i = bisect.bisect_right(a, x) - 1
    if i >= 0 and a[i] == x:
        return i
    return -1
```

**Search insert position (LeetCode 35):**
```python
def search_insert(a, x):
    return bisect.bisect_left(a, x)
```

**Floor (largest element <= x):**
```python
def floor_value(a, x):
    i = bisect.bisect_right(a, x) - 1
    return a[i] if i >= 0 else None
```

**Ceiling (smallest element >= x):**
```python
def ceiling_value(a, x):
    i = bisect.bisect_left(a, x)
    return a[i] if i < len(a) else None
```

### 2.5 `insort` — Maintaining a Sorted Structure

```python
import bisect

sorted_list = [1, 3, 5, 7]
bisect.insort_left(sorted_list, 4)
print(sorted_list)  # [1, 3, 4, 5, 7]
```

> ⚠️ **Warning:** `insort` is `O(n)` per call because Python lists are contiguous arrays — insertion requires shifting elements. For many insertions, consider `sortedcontainers.SortedList` (`O(log n)` insert) instead of repeated `insort` on a plain list.

### 2.6 Using the `key` Parameter (Python 3.10+)

Since Python 3.10, `bisect` functions accept a `key` argument, letting you binary search on a derived value without building a separate array:

```python
import bisect

people = [("Alice", 30), ("Bob", 25), ("Cara", 40)]
people.sort(key=lambda p: p[1])
# people = [("Bob", 25), ("Alice", 30), ("Cara", 40)]

i = bisect.bisect_left(people, 30, key=lambda p: p[1])
print(i)  # 1
```

> **Note:** On Python < 3.10, emulate this by pre-extracting the key array: `keys = [p[1] for p in people]` then `bisect.bisect_left(keys, 30)`.

### 2.7 Custom Binary Search (When `bisect` Isn't Enough)

`bisect` only compares elements with `<`. It cannot express arbitrary predicates like "can we ship all packages within D days with capacity x?". For those, write a **custom predicate-based binary search** (Section 6 covers this in depth).

### 2.8 Performance Comparison

| Approach | Time per search | Notes |
|---|---|---|
| Linear search (`x in list`) | `O(n)` | Simple, no sort needed |
| `list.sort()` once + `bisect` per query | `O(n log n)` once, `O(log n)`/query | Best when queries ≫ 1 |
| Custom iterative binary search | `O(log n)` | Full control over predicate/boundary |
| `sortedcontainers.SortedList` | `O(log n)` insert **and** search | Best for dynamic sorted data |

### 2.9 Best Practices

- Prefer `bisect` over hand-rolled binary search for **plain "find in sorted array"** tasks — it's tested, C-implemented, and removes an entire class of off-by-one bugs.
- Reach for a **custom template** only when you need a predicate more complex than a plain comparison.
- Never call `bisect` on an unsorted list — it won't raise an error; it silently returns a wrong index.
- For **repeated insertions into a large sorted collection**, avoid `list.insort` (`O(n)` per insert); use `sortedcontainers.SortedList`.

---

## 3. Binary Search Fundamentals

### 3.1 The Search Interval

Every binary search maintains a **search interval** `[low, high]` (or `[low, high)`) representing "the target, if it exists, is somewhere in here." The algorithm's entire job is to shrink this interval until it becomes empty or a single element, while never discarding the target.

Two conventions exist:

| Convention | Interval meaning | `high` initialized to |
|---|---|---|
| **Inclusive** | `[low, high]` — both ends are valid candidates | `len(a) - 1` |
| **Exclusive** | `[low, high)` — `high` is one-past-the-last valid candidate | `len(a)` |

> **Tip:** Pick ONE convention and internalize it. Mixing conventions mid-implementation is the #1 source of off-by-one bugs. This handbook uses the **inclusive `[low, high]`** convention for the "standard" template and the **exclusive `[low, high)`** convention for boundary (lower/upper bound) templates — matching Python's own `bisect` semantics.

### 3.2 Mid Calculation

```python
mid = (low + high) // 2          # fine in Python — no overflow (arbitrary precision ints)
mid = low + (high - low) // 2    # defensive style, habit carried from C/Java/C++
```

> **Note (language comparison):** In languages with fixed-width integers (Java, C++), `(low + high) / 2` can **overflow** if `low + high` exceeds the integer range, producing a negative or wrapped value. The defensive fix is `low + (high - low) / 2`. **Python integers have arbitrary precision, so overflow cannot happen** — `(low + high) // 2` is always safe in Python. Many candidates still use the defensive form out of habit or to signal awareness of the issue to interviewers.

### 3.3 Loop Invariants

A loop invariant is a condition that holds true **before and after every iteration**. For binary search, the invariant is usually:

> "If the target exists in the array, it exists within `a[low..high]` (inclusive) or `a[low..high)` (exclusive)."

Maintaining this invariant means:
- Never move `low` or `high` in a way that could exclude the target.
- Always make **provable progress** (the interval must strictly shrink) or the loop can spin forever.

### 3.4 Inclusive vs Exclusive Range — Side by Side

```
INCLUSIVE [low, high]                 EXCLUSIVE [low, high)

low, high = 0, n - 1                  low, high = 0, n
while low <= high:                    while low < high:
    mid = (low + high) // 2               mid = (low + high) // 2
    if a[mid] == target:                  if a[mid] == target:
        return mid                            return mid
    elif a[mid] < target:                 elif a[mid] < target:
        low = mid + 1                         low = mid + 1
    else:                                 else:
        high = mid - 1                        high = mid
return -1                             return -1  (adjust as needed)
```

> ⚠️ **Warning:** In the exclusive convention, if you write `high = mid` when you meant `high = mid - 1`-equivalent logic, you can create an **infinite loop** when `low == mid` (which happens when `high - low == 1`). This is why exclusive-range templates conventionally compute `mid = low + (high - low) // 2` and require the "shrink" branch touching `mid` itself (not `mid ± 1`) whenever the predicate keeps `mid` as a valid candidate. See Section 4 for the exact boundary templates.

### 3.5 Iterative Binary Search

**Problem:** Given a sorted array `a` and target `x`, return the index of `x`, or `-1` if absent.

```python
def binary_search_iterative(a: list[int], x: int) -> int:
    low, high = 0, len(a) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

**Line-by-line explanation:**
- `low, high = 0, len(a) - 1` — initialize inclusive search interval covering the whole array.
- `while low <= high:` — loop continues while the interval is non-empty (a single element `low == high` is still valid to check).
- `mid = low + (high - low) // 2` — defensive midpoint calculation.
- `if a[mid] == x: return mid` — target found.
- `elif a[mid] < x: low = mid + 1` — target must be to the right; `mid` is eliminated since it's `< x`.
- `else: high = mid - 1` — target must be to the left; `mid` is eliminated since it's `> x`.
- `return -1` — interval became empty (`low > high`) without finding `x`.

**Dry Run:** `a = [2, 4, 6, 8, 10, 12, 14]`, `x = 10`

| Step | low | mid | high | a[mid] | Decision | Explanation |
|---|---|---|---|---|---|---|
| 1 | 0 | 3 | 6 | 8 | 8 < 10 → go right | `low = mid+1 = 4` |
| 2 | 4 | 5 | 6 | 12 | 12 > 10 → go left | `high = mid-1 = 4` |
| 3 | 4 | 4 | 4 | 10 | 10 == 10 → **found** | return `4` |

**Complexity:** Time `O(log n)`, Space `O(1)`.

**Edge cases:**
- Empty array (`len(a) == 0`): loop never executes, returns `-1`. ✅ handled.
- Single-element array: `low == high == 0`, checked once. ✅ handled.
- Target smaller than all elements / larger than all elements: interval shrinks to empty, returns `-1`. ✅ handled.
- Array with duplicates: returns **some** index containing `x`, not necessarily first or last — use Section 4 templates for that.

**Common mistakes:**
- Using `high = len(a)` (exclusive) but writing `while low <= high` (inclusive-style loop) — inconsistent conventions cause out-of-bounds access.
- Writing `high = mid` instead of `high = mid - 1` in the inclusive template — can cause infinite loop.
- Forgetting `-1` return for "not found".

**Interview tips:**
- Always state which convention (inclusive/exclusive) you're using out loud — interviewers reward this explicitness.
- Trace through a tiny example (`n = 1` or `n = 2`) before declaring the code correct.

### 3.6 Recursive Binary Search

```python
def binary_search_recursive(a: list[int], x: int, low: int = 0, high: int | None = None) -> int:
    if high is None:
        high = len(a) - 1
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        return binary_search_recursive(a, x, mid + 1, high)
    else:
        return binary_search_recursive(a, x, low, mid - 1)
```

**Line-by-line explanation:**
- Default arguments `low=0, high=None` let the first call omit bounds; `high` is set to `len(a)-1` on first entry.
- `if low > high: return -1` — **base case**: empty interval means not found.
- Otherwise compute `mid` and recurse into exactly one half, mirroring the iterative version's branches.

**Dry run:** identical steps to the iterative dry run above, but each row is a recursive call frame instead of a loop iteration.

**Complexity:** Time `O(log n)`; Space `O(log n)` due to the call stack (vs `O(1)` for iterative).

**When to use recursive vs iterative:**
- **Iterative** is preferred in production code and interviews by default — no stack overflow risk, marginally faster (no call overhead).
- **Recursive** is clearer when binary search is one case inside a broader recursive algorithm (e.g., some divide-and-conquer geometry problems), or when explicitly asked to demonstrate recursion.

> ⚠️ **Warning:** Python's default recursion limit (~1000) is irrelevant here since `log2(n)` stays tiny even for huge `n` (`log2(10^18) ≈ 60`), but it's worth knowing recursive binary search *can* theoretically hit limits only on pathological non-halving recursions — not a real concern for correct binary search.

### 3.7 Correct Template Design Philosophy

The most reliable way to avoid bugs is to **fix one template per problem type** and never improvise mid-interview. This handbook recommends memorizing exactly **four** templates (Section 4):

1. Standard search (find exact index or -1)
2. Lower bound (first index where `predicate(i)` is True, predicate is "False...True")
3. Upper bound (first index where `predicate(i)` is True, for "given value's insertion point strictly after duplicates")
4. Generic predicate template for "Binary Search on Answer" (Section 6)

### 3.8 Boundary Management Rules of Thumb

| Rule | Why |
|---|---|
| If `a[mid]` can still be a valid answer, don't discard it: use `high = mid` (not `mid - 1`) or `low = mid` (not `mid + 1`) | Prevents skipping the true boundary |
| If using `low = mid` (not `mid+1`), compute mid with a **ceiling** bias: `mid = low + (high - low + 1) // 2` | Prevents infinite loop when `high == low + 1` |
| Always ensure the interval **strictly shrinks** every iteration | Guarantees termination |
| Loop condition must match interval convention (`low < high` for exclusive-style "shrink to one point", `low <= high` for inclusive "find or exhaust") | Prevents off-by-one / infinite loop |

---

## 4. Binary Search Templates

> These are the templates to **memorize cold**. Every pattern in Section 5 is a thin wrapper around one of these.

### 4.1 Template A — Standard Search (Exact Match)

```python
def template_standard(a: list[int], target: int) -> int:
    low, high = 0, len(a) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
**Use when:** array has (or you only need) unique elements and you want any matching index.

### 4.2 Template B — Lower Bound (First index where `a[i] >= x`)

```python
def lower_bound(a: list[int], x: int) -> int:
    low, high = 0, len(a)          # exclusive range
    while low < high:
        mid = low + (high - low) // 2
        if a[mid] < x:
            low = mid + 1
        else:
            high = mid            # a[mid] >= x could BE the answer; keep it
    return low                     # low == high == first index with a[i] >= x
```
Equivalent to `bisect.bisect_left(a, x)`.

**Dry Run:** `a = [1, 3, 3, 3, 5, 7]`, `x = 3`

| Step | low | mid | high | a[mid] | Decision | Explanation |
|---|---|---|---|---|---|---|
| 1 | 0 | 3 | 6 | 3 | `a[mid] >= x` → `high = mid` | keep mid as candidate |
| 2 | 0 | 1 | 3 | 3 | `a[mid] >= x` → `high = mid` | keep mid as candidate |
| 3 | 0 | 0 | 1 | 1 | `a[mid] < x` → `low = mid+1` | discard mid |
| — | 1 | — | 1 | — | loop ends (`low == high`) | return `1` |

### 4.3 Template C — Upper Bound (First index where `a[i] > x`)

```python
def upper_bound(a: list[int], x: int) -> int:
    low, high = 0, len(a)
    while low < high:
        mid = low + (high - low) // 2
        if a[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return low
```
Equivalent to `bisect.bisect_right(a, x)`.

### 4.4 Template D — First / Last Occurrence (built from B and C)

```python
def first_occurrence(a: list[int], x: int) -> int:
    i = lower_bound(a, x)
    return i if i < len(a) and a[i] == x else -1

def last_occurrence(a: list[int], x: int) -> int:
    i = upper_bound(a, x) - 1
    return i if i >= 0 and a[i] == x else -1

def count_occurrences(a: list[int], x: int) -> int:
    return upper_bound(a, x) - lower_bound(a, x)
```

### 4.5 Template E — Floor and Ceiling

```python
def floor_index(a: list[int], x: int) -> int:
    """Largest index i such that a[i] <= x, else -1."""
    i = upper_bound(a, x) - 1
    return i

def ceiling_index(a: list[int], x: int) -> int:
    """Smallest index i such that a[i] >= x, else len(a)."""
    return lower_bound(a, x)
```

### 4.6 Template F — Generic Predicate Template ("Binary Search on Answer")

This is the **most important template in this handbook** — see Section 6 for full treatment.

```python
def binary_search_on_answer(lo: int, hi: int, feasible) -> int:
    """
    Find the smallest x in [lo, hi] such that feasible(x) is True,
    given feasible(x) is monotonic: False False ... False True True ... True.
    Returns hi + 1 (or a sentinel) if no x in range is feasible.
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid           # mid works; try to find something smaller/equal
        else:
            lo = mid + 1        # mid doesn't work; must go higher
    return lo                   # lo == hi == smallest feasible x
```

> **Tip:** To find the **largest** `x` such that `feasible(x)` is True (predicate is `True True ... True False False`), flip the template:
> ```python
> def binary_search_largest_true(lo, hi, feasible):
>     while lo < hi:
>         mid = lo + (hi - lo + 1) // 2   # CEILING mid — critical!
>         if feasible(mid):
>             lo = mid                     # mid works; try to go higher
>         else:
>             hi = mid - 1
>     return lo
> ```
> Note the **ceiling mid** (`+1` before `// 2`). Without it, `lo = mid` combined with a floor-biased mid can infinite-loop when `hi == lo + 1`.

### 4.7 Template Comparison Table

| Template | Loop condition | Shrink rule (match) | Shrink rule (no match) | Returns |
|---|---|---|---|---|
| A. Standard | `low <= high` | — (`return mid`) | `low=mid+1` / `high=mid-1` | index or -1 |
| B. Lower bound | `low < high` | `high = mid` | `low = mid+1` | first `a[i] >= x` |
| C. Upper bound | `low < high` | `low = mid+1` | `high = mid` | first `a[i] > x` |
| F. Smallest true | `low < high` | `hi = mid` | `lo = mid+1` | smallest feasible x |
| F′. Largest true | `low < high` | `lo = mid` (ceil mid) | `hi = mid-1` | largest feasible x |

### 4.8 Predicate-Based Template — Generalization

Every template above can be reframed as: *"find the boundary of a monotonic predicate."*

```
Standard search:     predicate(i) = (a[i] >= x)      -> lower_bound
First occurrence:    predicate(i) = (a[i] >= x), then check equality
Binary search on ans:predicate(x) = "is x feasible?" -> smallest/largest true
```

This unification is **the single biggest unlock** for solving unfamiliar binary search problems: always ask **"what is my predicate, and is it monotonic?"**

---

## 5. Binary Search Patterns

### 5.1 Pattern: Exact Match on Sorted Array

Covered fully in Section 4.1 (Template A). Use `bisect` in practice; hand-roll only in interviews to demonstrate understanding.

### 5.2 Pattern: Boundary Search (Lower/Upper Bound, First/Last Occurrence)

Covered fully in Section 4.2–4.5.

### 5.3 Pattern: Search on Rotated Sorted Array

**Problem:** Array was sorted, then rotated at an unknown pivot (e.g., `[4,5,6,7,0,1,2]`). Find target `x` in `O(log n)`.

**ASCII visualization:**
```
Original sorted: [0, 1, 2, 4, 5, 6, 7]
Rotated at pivot 4: [4, 5, 6, 7, 0, 1, 2]

Index:  0  1  2  3  4  5  6
Value:  4  5  6  7  0  1  2
        |________|  |______|
        sorted half   sorted half
       (left of mid)  (right of mid)

Key insight: at least ONE half (split by mid) is always fully sorted.
```

**Approach:** At each step, determine which half (`[low, mid]` or `[mid, high]`) is sorted by comparing `a[low]` and `a[mid]`. Then check if `target` lies within that sorted half's range — if yes, recurse there; if no, recurse into the other half.

```python
def search_rotated(a: list[int], target: int) -> int:
    low, high = 0, len(a) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if a[mid] == target:
            return mid
        if a[low] <= a[mid]:               # left half [low..mid] is sorted
            if a[low] <= target < a[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:                                # right half [mid..high] is sorted
            if a[mid] < target <= a[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
```

**Line-by-line explanation:**
- `a[low] <= a[mid]` tests whether the left segment is sorted (rotation point is NOT in `[low, mid]`).
- If left is sorted, check whether `target` falls in `[a[low], a[mid])` — if so, search left; otherwise the rotation/target must be on the right.
- Symmetric logic for when the right half is sorted.

**Dry run:** `a = [4,5,6,7,0,1,2]`, `target = 0`

| Step | low | mid | high | a[mid] | Sorted half | Decision |
|---|---|---|---|---|---|---|
| 1 | 0 | 3 | 6 | 7 | left `[4,5,6,7]` sorted | target=0 not in `[4,7)` → `low=mid+1=4` |
| 2 | 4 | 5 | 6 | 1 | left `[0,1]` sorted | target=0 in `[0,1)` → `high=mid-1=4` |
| 3 | 4 | 4 | 4 | 0 | — | `a[mid]==target` → return `4` |

**Complexity:** `O(log n)` time, `O(1)` space.

**Edge cases:** No rotation (fully sorted); rotation at index 0 (no effective rotation); duplicates present (see 5.4); array of size 1.

**Common mistakes:** Using `a[low] < a[mid]` instead of `<=` (breaks when `low == mid`); forgetting the half-open range check `a[low] <= target < a[mid]` needs the correct inequality direction.

**When NOT to use:** If duplicates make `a[low] == a[mid] == a[high]` ambiguous (can't tell which half is sorted) — see 5.4 for the fix.

### 5.4 Pattern: Search on Rotated Array with Duplicates

When `a[low] == a[mid]`, you cannot tell which half is sorted. Fix: shrink the ambiguous ends.

```python
def search_rotated_with_dupes(a: list[int], target: int) -> bool:
    low, high = 0, len(a) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if a[mid] == target:
            return True
        if a[low] == a[mid] == a[high]:
            low += 1
            high -= 1
        elif a[low] <= a[mid]:
            if a[low] <= target < a[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if a[mid] < target <= a[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False
```

> ⚠️ **Warning:** This degrades to `O(n)` worst case (e.g., all elements equal except one) because of the `low += 1; high -= 1` linear shrink. This is a fundamental limitation, not a bug — it's provably impossible to guarantee `O(log n)` here (interviewers expect you to state this).

### 5.5 Pattern: Find Minimum in Rotated Sorted Array

```python
def find_min_rotated(a: list[int]) -> int:
    low, high = 0, len(a) - 1
    while low < high:
        mid = low + (high - low) // 2
        if a[mid] > a[high]:
            low = mid + 1     # minimum is to the right of mid
        else:
            high = mid          # a[mid] could BE the minimum; keep it
    return a[low]
```

**Predicate framing:** `predicate(i) = (a[i] <= a[-1])` is monotonic `False...False True...True` for a rotated array (with a caveat for no rotation) — this is exactly Template B (lower bound) in disguise.

### 5.6 Pattern: Peak Element (Local Maximum)

**Problem:** Find any index `i` such that `a[i-1] < a[i] > a[i+1]` (treating out-of-bounds neighbors as `-infinity`).

**ASCII visualization:**
```
Value:  1   2   3   1   5   6   4
Index:  0   1   2   3   4   5   6
                ^               peak (local max) at index 2
                        ^       peak (local max) at index 5
Both are valid answers -- "a peak", not "the global maximum".
```

```python
def find_peak_element(a: list[int]) -> int:
    low, high = 0, len(a) - 1
    while low < high:
        mid = low + (high - low) // 2
        if a[mid] > a[mid + 1]:
            high = mid          # descending here; a peak is at mid or to the left
        else:
            low = mid + 1        # ascending; peak is strictly to the right
    return low
```

**Why this works:** Comparing `a[mid]` to `a[mid+1]` tells you which direction is "uphill." Because the array has `-infinity` boundaries, walking uphill always eventually reaches a peak — this makes the "is there a peak to my right" predicate monotonic.

**Complexity:** `O(log n)`.

**Edge cases:** Single element (trivially a peak); strictly increasing array (peak is the last element); strictly decreasing array (peak is the first element); plateau values (problem usually guarantees `a[i] != a[i+1]` — check constraints).

### 5.7 Pattern: Bitonic / Mountain Array

**Problem:** Array increases then decreases (a "mountain"). Find the peak, or search for a target across both slopes.

```python
def peak_index_mountain(a: list[int]) -> int:
    low, high = 0, len(a) - 1
    while low < high:
        mid = low + (high - low) // 2
        if a[mid] < a[mid + 1]:
            low = mid + 1        # still climbing
        else:
            high = mid            # descending or at peak
    return low

def search_mountain(a: list[int], target: int) -> int:
    peak = peak_index_mountain(a)

    # search ascending part [0, peak]
    lo, hi = 0, peak
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    # search descending part [peak+1, end]
    lo, hi = peak + 1, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == target:
            return mid
        elif a[mid] > target:   # descending, so ">" means go right
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
```

**Complexity:** `O(log n)` — three binary searches in sequence, still `O(log n)` total.

### 5.8 Pattern: Search in Infinite / Unbounded Sorted Array

**Problem:** Array has no known length (only an interface `get(i)` that returns a sentinel like `float('inf')` beyond the end).

**Approach:** Exponentially probe to find a valid `high` bound, then binary search normally.

```python
def search_infinite_array(reader, target: int) -> int:
    low, high = 0, 1
    while reader.get(high) < target:
        low = high
        high *= 2

    while low <= high:
        mid = low + (high - low) // 2
        val = reader.get(mid)
        if val == target:
            return mid
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

**Why exponential probing:** Doubling `high` finds an upper bound in `O(log p)` steps, where `p` is the target's true position — this keeps overall complexity `O(log p)`, not `O(p)`.

**ASCII visualization:**
```
Probe: high=1 -> 2 -> 4 -> 8 -> 16 ...
Value at these indices grows until it exceeds target,
then normal binary search runs inside [low, high].
```

### 5.9 Pattern: Matrix Binary Search (2D)

**Variant A — Fully sorted matrix (row-major, like a flattened sorted array):**

```python
def search_matrix_flat(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    while low <= high:
        mid = low + (high - low) // 2
        r, c = divmod(mid, cols)
        val = matrix[r][c]
        if val == target:
            return True
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
```
**Precondition:** each row's last element `<` next row's first element (true "flattened sorted" matrix). `O(log(rows*cols))`.

**Variant B — Row-wise and column-wise sorted (not flattenable), e.g. LeetCode 240:**

```python
def search_matrix_staircase(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    row, col = 0, len(matrix[0]) - 1   # start top-right corner
    while row < len(matrix) and col >= 0:
        val = matrix[row][col]
        if val == target:
            return True
        elif val > target:
            col -= 1        # eliminate this column
        else:
            row += 1        # eliminate this row
    return False
```

> **Note:** Variant B is technically a "staircase search," not classic binary search (it's `O(rows + cols)`, not `O(log(rows*cols))`) — but it's grouped here because it's the standard answer to "binary search a 2D matrix" when rows/columns are independently sorted but not globally sorted. Always clarify with the interviewer which matrix-sortedness guarantee is given.

### 5.10 Pattern: Nearly Sorted Array (element off by one position)

**Problem:** Each element may be swapped with an adjacent one from a fully sorted order. Modify standard search to check `mid-1`, `mid`, `mid+1`.

```python
def search_nearly_sorted(a: list[int], target: int) -> int:
    low, high = 0, len(a) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if a[mid] == target:
            return mid
        if mid - 1 >= low and a[mid - 1] == target:
            return mid - 1
        if mid + 1 <= high and a[mid + 1] == target:
            return mid + 1
        if a[mid] < target:
            low = mid + 2
        else:
            high = mid - 2
    return -1
```

### 5.11 Pattern Summary Table

| Pattern | Key Trick | Complexity |
|---|---|---|
| Exact match | Template A | `O(log n)` |
| Lower/Upper bound | Template B/C | `O(log n)` |
| Rotated array search | Identify sorted half | `O(log n)` |
| Rotated w/ duplicates | Shrink on tie | `O(log n)` avg, `O(n)` worst |
| Find min in rotated | Compare `a[mid]` vs `a[high]` | `O(log n)` |
| Peak element | Compare `a[mid]` vs `a[mid+1]` | `O(log n)` |
| Mountain array | Find peak, then 2 searches | `O(log n)` |
| Infinite array | Exponential probing + search | `O(log p)` |
| Matrix (flattened) | Map 1D index to 2D | `O(log(rc))` |
| Matrix (staircase) | Start top-right, eliminate row/col | `O(r + c)` |
| Nearly sorted | Check `mid-1, mid, mid+1` | `O(log n)` |

---

## 6. Binary Search on Answer

> This is the single highest-leverage section in this handbook. Once mastered, it turns a huge class of "optimization" problems (that look nothing like searching) into routine binary search applications.

### 6.1 The Core Idea

Instead of searching for a value **in an array**, we search for a value **in the space of possible answers** (e.g., "minimum capacity," "minimum days," "maximum speed"). The key requirement is that we can write a **feasibility predicate**:

```
feasible(x) -> True or False
```

that is **monotonic** over the answer space:

```
feasible: False False False ... False True True True ... True
                                   ^
                          the boundary IS the answer
```

### 6.2 Recognizing Monotonic Functions

Ask: *"If capacity `x` works, does every capacity `> x` also work?"* If yes → monotonic → binary searchable.

```
Example: "Can I ship all packages in D days with ship capacity x?"
x = 1   -> infeasible (too slow)
x = 5   -> infeasible
x = 10  -> feasible  <- boundary
x = 20  -> feasible  (bigger capacity only helps)
x = 100 -> feasible
```

Monotonicity here is intuitive: **more capacity never hurts**.

### 6.3 Search Space Identification

Before coding, explicitly state:
- **Lower bound (`lo`)**: the smallest answer that could conceivably work (often `1` or `max(array)`).
- **Upper bound (`hi`)**: the largest answer that could conceivably be needed (often `sum(array)` or a problem-given max).
- **Feasibility check**: usually a greedy `O(n)` simulation.

### 6.4 Predicate Functions — General Shape

```python
def feasible(x: int) -> bool:
    # simulate / greedily check whether "x" satisfies the problem's requirement
    ...
    return True_or_False
```

### 6.5 Worked Example 1 — Koko Eating Bananas (LeetCode 875)

**Problem:** Koko eats bananas from `n` piles at speed `k` bananas/hour (one pile at a time; if a pile has fewer than `k`, she finishes it and rests that hour). Find the **minimum integer `k`** so she finishes all piles within `h` hours.

**Search space:** `lo = 1`, `hi = max(piles)` (eating faster than the biggest pile never helps further).

**Predicate:** `feasible(k)` = "can Koko finish all piles within `h` hours if she eats at speed `k`?"

```python
import math

def min_eating_speed(piles: list[int], h: int) -> int:
    def hours_needed(k: int) -> int:
        return sum(math.ceil(p / k) for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if hours_needed(mid) <= h:
            hi = mid            # mid works; try slower (smaller) speed
        else:
            lo = mid + 1          # mid too slow; need faster speed
    return lo
```

**Line-by-line explanation:**
- `hours_needed(k)` computes total hours via `ceil(pile / k)` summed across piles — this IS the feasibility predicate, reframed as a numeric check against `h`.
- Binary search over speed `k` in `[1, max(piles)]` using the **smallest true** template (Section 4.6).
- `hours_needed(mid) <= h` means speed `mid` is fast enough → it's feasible → shrink `hi` to `mid` since a slower speed might also work.
- Otherwise `mid` is too slow → shrink from below.

**Dry run:** `piles = [3,6,7,11]`, `h = 8`

| Step | lo | mid | hi | hours_needed(mid) | Feasible? | Decision |
|---|---|---|---|---|---|---|
| 1 | 1 | 5 | 11 | ceil(3/5)+ceil(6/5)+ceil(7/5)+ceil(11/5)=1+2+2+3=8 | `8<=8` True | `hi=5` |
| 2 | 1 | 3 | 5 | 1+2+3+4=10 | `10<=8` False | `lo=4` |
| 3 | 4 | 4 | 5 | 1+2+2+3=8 | True | `hi=4` |
| — | 4 | — | 4 | — | loop ends | return `4` |

**Complexity:** `O(n log(max(piles)))`.

**Edge cases:** `h == len(piles)` (must eat each pile in exactly one hour → `k = max(piles)`); huge piles causing large `hi`.

**Common mistakes:** Using `hi = mid - 1` (should be `hi = mid`, since `mid` itself might be the answer); using floor division instead of `math.ceil` for hours.

### 6.6 Worked Example 2 — Capacity to Ship Packages Within D Days (LeetCode 1011)

**Search space:** `lo = max(weights)` (ship must at least hold the heaviest package), `hi = sum(weights)` (one day, ship everything).

```python
def ship_within_days(weights: list[int], days: int) -> int:
    def days_needed(capacity: int) -> int:
        day_count, current_load = 1, 0
        for w in weights:
            if current_load + w > capacity:
                day_count += 1
                current_load = 0
            current_load += w
        return day_count

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if days_needed(mid) <= days:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**Why monotonic:** More ship capacity → same or fewer days needed. Textbook "smallest feasible x" binary search on answer.

**Complexity:** `O(n log(sum(weights)))`.

### 6.7 Worked Example 3 — Allocate Minimum Number of Pages (Book Allocation)

**Problem:** Allocate `n` books (each with page counts) to `m` students, contiguous allocation, minimizing the **maximum pages assigned to any one student**.

**Search space:** `lo = max(pages)`, `hi = sum(pages)`.

```python
def allocate_books(pages: list[int], students: int) -> int:
    def students_needed(max_pages: int) -> int:
        count, current = 1, 0
        for p in pages:
            if current + p > max_pages:
                count += 1
                current = 0
            current += p
        return count

    lo, hi = max(pages), sum(pages)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if students_needed(mid) <= students:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**Recognizing the pattern:** "Minimize the maximum" problems (book allocation, ship capacity, split array largest sum) are all the **identical template** with a different `feasible`/count function.

### 6.8 Worked Example 4 — Aggressive Cows (Maximize the Minimum Distance)

**Problem:** Place `c` cows in `n` stalls (given positions) to **maximize the minimum distance** between any two cows.

This flips the direction: predicate is `True True ... True False False` (larger distance eventually becomes infeasible), so we want the **largest feasible x** (Template F′ from Section 4.6).

```python
def aggressive_cows(stalls: list[int], cows: int) -> int:
    stalls.sort()

    def can_place(min_dist: int) -> bool:
        count, last_pos = 1, stalls[0]
        for pos in stalls[1:]:
            if pos - last_pos >= min_dist:
                count += 1
                last_pos = pos
        return count >= cows

    lo, hi = 1, stalls[-1] - stalls[0]
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2   # ceiling mid — required for "largest true"
        if can_place(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo
```

> ⚠️ **Warning:** This is the template most people get wrong under pressure because it requires the **ceiling mid** (`+1` before `//2`). Forgetting it causes an infinite loop when `hi == lo + 1` and `can_place(lo)` is True (since `mid` would compute to `lo`, `lo = mid` doesn't change `lo`, and the loop never progresses).

### 6.9 Worked Example 5 — Median of Two Sorted Arrays (Binary Search on Partition) (LeetCode 4)

**Problem:** Find the median of two sorted arrays in `O(log(min(m, n)))`.

**Search space:** binary search over the **partition index** in the smaller array.

```python
def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    lo, hi = 0, m
    half = (m + n + 1) // 2

    while lo <= hi:
        i = lo + (hi - lo) // 2      # partition in nums1
        j = half - i                   # partition in nums2

        left1 = nums1[i - 1] if i > 0 else float('-inf')
        right1 = nums1[i] if i < m else float('inf')
        left2 = nums2[j - 1] if j > 0 else float('-inf')
        right2 = nums2[j] if j < n else float('inf')

        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 1:
                return max(left1, left2)
            return (max(left1, left2) + min(right1, right2)) / 2
        elif left1 > right2:
            hi = i - 1
        else:
            lo = i + 1

    raise ValueError("Input arrays are not sorted or invalid")
```

**Why this is "binary search on answer":** The predicate `feasible(i)` = "is partition `i` in `nums1` (with the mirrored partition `j` in `nums2`) a valid median split?" is monotonic in `i` — this is one of the hardest, most celebrated applications of binary search in interviews.

**Complexity:** `O(log(min(m, n)))`.

### 6.10 Floating-Point Binary Search on Answer

When the answer space is continuous (e.g., "minimum speed as a real number", square roots, or the bisection method for root-finding), use a **fixed iteration count** instead of an equality check (floats never exactly converge):

```python
def sqrt_binary_search(x: float, precision: int = 1e-9) -> float:
    lo, hi = 0.0, max(1.0, x)
    for _ in range(100):          # ~100 iterations is overkill-safe for double precision
        mid = (lo + hi) / 2
        if mid * mid < x:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2
```

> **Note:** Fixed iteration counts (e.g., 100–200) are standard for floating point binary search because `hi - lo` shrinks geometrically; after ~100 iterations the interval is far smaller than any representable double precision, making further iteration pointless. Alternatively loop `while hi - lo > precision`.

### 6.11 Decision Problems vs Optimization Problems

| Type | Question | Technique |
|---|---|---|
| Decision problem | "Can we achieve X with resource `r`?" | Direct predicate → `O(feasible check)` |
| Optimization problem | "What's the min/max `r` such that X is achievable?" | Binary search over `r`, using the decision problem as predicate |

**Key insight:** Binary Search on Answer converts an **optimization** problem into repeated **decision** problems — a very general and powerful transformation.

### 6.12 Interview Examples Checklist

| Problem | Predicate | Direction |
|---|---|---|
| Koko Eating Bananas | hours needed `<= h` | smallest true |
| Ship Packages in D Days | days needed `<= D` | smallest true |
| Book Allocation / Split Array Largest Sum | students/parts needed `<= m` | smallest true |
| Aggressive Cows | can place `>= c` cows | largest true |
| Magnetic Force Between Balls | can place `>= m` balls | largest true |
| Smallest Divisor Given a Threshold | sum of ceil divisions `<= threshold` | smallest true |
| Median of Two Sorted Arrays | valid partition | equality-style binary search on partition |
| Sqrt(x) / Nth root | `mid^k <= x` | largest true |

---

## 7. Applications

### 7.1 Searching

The most direct application: locating elements in sorted arrays, sorted linked structures (with random access), and sorted files. Any time data is sorted once and queried repeatedly, binary search (or `bisect`) is the default tool.

### 7.2 Scheduling Problems

"Minimum time to complete all jobs given `k` workers" style problems are Binary Search on Answer: binary search over the time `T`, with predicate "can all jobs finish within `T` using `k` workers?" (usually checked greedily or via a helper simulation).

### 7.3 Allocation Problems

Book allocation, painter's partition problem, split array largest sum — all "minimize the maximum chunk" problems, solved with Template F (Section 4.6 / 6.7).

### 7.4 Optimization Problems

Any problem phrased as "find the minimum/maximum X such that condition holds" is a candidate for Binary Search on Answer, **provided** the condition is monotonic in X. This is the majority of "hard" binary search interview problems.

### 7.5 Databases

- **B-Trees / B+ Trees** (used by most relational databases for indexes) are a generalization of binary search to multi-way branching — each node holds sorted keys and a binary-search (or linear scan for small nodes) locates the correct child pointer.
- **Range queries** on sorted indexes use lower_bound/upper_bound-style logic to find the start and end of a range in `O(log n)`.

### 7.6 Search Engines

Inverted indexes store sorted posting lists; merging/intersecting them and finding specific document IDs often uses binary-search-style galloping/exponential search for efficiency when list sizes differ significantly.

### 7.7 Machine Learning Hyperparameter Search (Overview)

For a single hyperparameter with a **unimodal** or monotonic relationship to validation loss (rare but occurs, e.g., regularization strength search along one clear direction), a bisection-style search can be faster than grid search. In practice, most ML hyperparameter search uses random search, Bayesian optimization, or grid search because the loss landscape usually isn't monotonic across multiple hyperparameters — binary search here is a narrow, special-case tool, not a general solution.

### 7.8 Competitive Programming

- **Binary search on answer** is one of the most common "medium-hard" tags on Codeforces/AtCoder.
- Combined with **prefix sums**, **two pointers**, or **greedy checks** as the predicate function.
- **Parametric search** (a formalization of binary search on answer) is a named technique in competitive programming literature.

---

## 8. Problem Recognition

### 8.1 Recognition Flowchart

```
                     ┌─────────────────────────────┐
                     │  Is the data/array sorted,   │
                     │  or CAN it be sorted without │
                     │  breaking the problem?       │
                     └──────────────┬───────────────┘
                                    │ yes
                                    v
                     ┌─────────────────────────────┐
                     │ Are you searching for a      │
                     │ specific value / boundary?   │
                     └──────────────┬───────────────┘
                          yes       │        no
              ┌────────────────────┘        └───────────────────┐
              v                                                  v
   Use Template A/B/C/D                          ┌─────────────────────────────┐
   (exact match, first/last,                     │ Does the problem ask         │
    lower/upper bound)                           │ "min/max X such that ..."?   │
                                                  └──────────────┬───────────────┘
                                                       yes       │        no
                                       ┌────────────────────────┘        └──> Probably NOT binary search;
                                       v                                       reconsider (DP, greedy, etc.)
                          ┌─────────────────────────────┐
                          │ Is the condition monotonic   │
                          │ in X? ("bigger X never hurts │
                          │  feasibility" or vice versa) │
                          └──────────────┬───────────────┘
                               yes       │        no
                    Binary Search on Answer          Binary search does NOT apply;
                    (Template F / F′)                 look for another technique
```

### 8.2 Interview Clue Keywords

| Keyword / Phrase | Likely Pattern |
|---|---|
| "sorted array" | Standard search / boundary search |
| "first occurrence" / "last occurrence" | Lower/Upper bound |
| "insert position" | `bisect_left` |
| "rotated array" | Rotated search pattern |
| "peak element" / "local maximum" | Peak element pattern |
| "minimum days/time/capacity/speed to..." | Binary search on answer (smallest true) |
| "maximum minimum distance" / "as large as possible while..." | Binary search on answer (largest true) |
| "matrix sorted rows and columns" | Matrix search |
| "infinite array" / "unknown size" | Exponential search + binary search |
| "median of two arrays" | Partition-based binary search |
| "count of elements less/greater than x" | `bisect_left`/`bisect_right` difference |

### 8.3 Monotonicity Detection Checklist

Ask these three questions:
1. Can I define a Boolean predicate `P(x)` over the answer space?
2. If `P(x)` is True, is `P(x+1)` (or `P(x-1)`, depending on direction) guaranteed to also be True?
3. Can I evaluate `P(x)` efficiently (ideally `O(n)` or `O(n log n)`) for a fixed `x`?

If all three are "yes," binary search on answer applies.

### 8.4 Search Space Construction Guide

1. Identify the variable being optimized (call it `x`).
2. Find the **loosest possible lower bound** for `x` (often `0`, `1`, or `min(array)`).
3. Find the **loosest possible upper bound** for `x` (often `max(array)`, `sum(array)`, or a stated constraint).
4. Write `feasible(x)` as a standalone function — test it manually on 2–3 values before wiring up the binary search loop.

---

## 9. Optimization: Brute Force → Binary Search

### 9.1 General Progression

| Stage | Approach | Complexity | When |
|---|---|---|---|
| 1 | Brute force: try every possible answer, check feasibility for each | `O(range * check_cost)` | Always correct, usually too slow |
| 2 | Binary search on answer | `O(log(range) * check_cost)` | When predicate is monotonic |
| 3 | Optimized predicate | `O(log(range) * optimized_check_cost)` | When the `O(n)` check itself can be sped up (e.g., prefix sums) |

### 9.2 Example Progression — "Smallest Divisor Given a Threshold" (LeetCode 1283)

**Brute force:** try divisor `d = 1, 2, 3, ...` until `sum(ceil(x/d) for x in nums) <= threshold`. Worst case `O(max(nums) * n)`.

**Binary search on answer:**
```python
import math

def smallest_divisor(nums: list[int], threshold: int) -> int:
    def total(d: int) -> int:
        return sum(math.ceil(x / d) for x in nums)

    lo, hi = 1, max(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if total(mid) <= threshold:
            hi = mid
        else:
            lo = mid + 1
    return lo
```
`O(n log(max(nums)))` — an exponential-to-logarithmic improvement in the search dimension.

### 9.3 Predicate Optimization

If `feasible(x)` itself is `O(n)`, sometimes precomputation (prefix sums, sorting, monotonic stacks/queues) can reduce it to `O(log n)` or `O(1)`, further improving total complexity from `O(n log(range))` to `O(log n * log(range))`.

### 9.4 Time-Space Trade-offs

- Precomputing prefix sums to speed up `feasible(x)` costs `O(n)` extra space for faster per-call evaluation — usually a good trade since binary search calls `feasible` `O(log(range))` times.
- Recursive binary search trades `O(1)` space for `O(log n)` stack space in exchange for arguably clearer code in some contexts — rarely worth it in production Python.

### 9.5 Boundary Optimization

Tightening `lo`/`hi` before starting the binary search (rather than using overly loose bounds like `0` to `10**18`) reduces the number of iterations, which matters when `feasible(x)` is expensive. E.g., in Koko Eating Bananas, using `hi = max(piles)` instead of an arbitrary large constant tightens the search meaningfully.

---

## 10. Interview Preparation

### 10.1 Difficulty-Tiered Problem List

**Easy:**
- Binary Search (LeetCode 704)
- Search Insert Position (LeetCode 35)
- First Bad Version (LeetCode 278)
- Sqrt(x) (LeetCode 69)
- Peak Index in a Mountain Array (LeetCode 852)

**Medium:**
- Find First and Last Position of Element in Sorted Array (LeetCode 34)
- Search in Rotated Sorted Array (LeetCode 33)
- Find Minimum in Rotated Sorted Array (LeetCode 153)
- Koko Eating Bananas (LeetCode 875)
- Capacity to Ship Packages Within D Days (LeetCode 1011)
- Find Peak Element (LeetCode 162)
- Search a 2D Matrix (LeetCode 74)
- Search a 2D Matrix II (LeetCode 240)
- Divide Chocolate / Book Allocation (variants across platforms)
- Aggressive Cows (Codeforces/GfG/Spoj style)
- Smallest Divisor Given a Threshold (LeetCode 1283)

**Hard:**
- Median of Two Sorted Arrays (LeetCode 4)
- Split Array Largest Sum (LeetCode 410)
- Find in Mountain Array (LeetCode 1095)
- Minimize Max Distance to Gas Station (LeetCode 774)
- Kth Smallest Element in a Sorted Matrix (LeetCode 378) — binary search on value
- Search in Rotated Sorted Array II, with duplicates (LeetCode 81)

### 10.2 Pattern-Wise Grouping

| Pattern | Representative Problems |
|---|---|
| Boundary search | LC 34, LC 35, LC 278 |
| Rotated array | LC 33, LC 81, LC 153 |
| Peak / mountain | LC 162, LC 852, LC 1095 |
| Matrix search | LC 74, LC 240, LC 378 |
| Binary search on answer (min feasible) | LC 875, LC 1011, LC 410, LC 1283 |
| Binary search on answer (max feasible) | Aggressive Cows, LC 774 |
| Partition-based | LC 4 |

### 10.3 Company-Wise Tendencies (General Patterns, Not Guarantees)

> **Note:** Company-specific question banks change constantly and vary by team/region. Treat the below as *pattern emphasis*, not a leak of real questions.

| Company (general trend) | Typical emphasis |
|---|---|
| Google | Binary search on answer, matrix search, elegant edge-case handling |
| Amazon | Rotated arrays, allocation/optimization problems tied to "operational" framing |
| Microsoft | Boundary search, first/last occurrence, peak element |
| Meta | Median of two sorted arrays, partition-based search, K-th element problems |
| Bloomberg/Finance | Binary search on answer with financial framing (allocation, capacity) |

### 10.4 Blind 75 / NeetCode Binary Search List

- Binary Search
- Search a 2D Matrix
- Koko Eating Bananas
- Find Minimum in Rotated Sorted Array
- Search in Rotated Sorted Array
- Time Based Key-Value Store (binary search on timestamps in a sorted list per key)
- Median of Two Sorted Arrays

### 10.5 Interview Tricks

- **State your template convention out loud** ("I'll use an exclusive `[lo, hi)` range") before coding — interviewers reward explicit reasoning.
- **Always dry-run on `n=0`, `n=1`, `n=2`** before declaring code done.
- For Binary Search on Answer problems, **write the `feasible()` function first and test it standalone** with 2–3 manual values before wiring the search loop.
- If duplicates are mentioned, immediately ask: "should I return any occurrence, or specifically first/last?"
- If asked to "optimize," always mention **both** the brute-force complexity and the binary-search complexity — showing the delta is often what's being evaluated.

### 10.6 Templates to Memorize (Quick Reference)

```python
# 1. Standard
low, high = 0, n - 1
while low <= high:
    mid = low + (high - low) // 2
    ...

# 2. Lower/Upper bound
low, high = 0, n
while low < high:
    mid = low + (high - low) // 2
    ...

# 3. Binary search on answer (smallest true)
lo, hi = LOW, HIGH
while lo < hi:
    mid = lo + (hi - lo) // 2
    if feasible(mid): hi = mid
    else: lo = mid + 1

# 4. Binary search on answer (largest true)
lo, hi = LOW, HIGH
while lo < hi:
    mid = lo + (hi - lo + 1) // 2   # ceiling mid
    if feasible(mid): lo = mid
    else: hi = mid - 1
```

---

## 11. Python Tips & Idioms

### 11.1 `bisect` Recap

Always default to `bisect.bisect_left` / `bisect.bisect_right` for plain sorted-array lookups instead of hand-writing loops — fewer bugs, faster (C-implemented).

### 11.2 Custom Binary Search Idioms

```python
# Clean, idiomatic iterative template
def bsearch(lo: int, hi: int, feasible) -> int:
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

### 11.3 `lambda` with `bisect` (`key=` parameter)

```python
import bisect

intervals = [(1, 'a'), (5, 'b'), (9, 'c')]
starts = [iv[0] for iv in intervals]
idx = bisect.bisect_left(starts, 6)   # pre-3.10 style
```
On Python 3.10+: `bisect.bisect_left(intervals, 6, key=lambda iv: iv[0])`.

### 11.4 Performance Tips

- Avoid re-slicing arrays inside the binary search loop (`a[low:high]` creates a new list each call — `O(n)` per slice!). Always index directly (`a[mid]`), never slice.
- Prefer `bisect`'s C implementation over Python-level loops when applicable — it's meaningfully faster for large `n`.
- Cache expensive-to-compute values used inside `feasible()` outside the binary search loop wherever possible (e.g., precompute `max(nums)` once, not per call).

### 11.5 Memory Optimization

- Iterative binary search uses `O(1)` extra space — prefer it over recursive in performance-sensitive code.
- Avoid building auxiliary arrays (e.g., a full prefix-sum array) when a running variable suffices, if memory is constrained.

### 11.6 Common Python Pitfalls

- **Integer division:** `/` produces a `float` in Python 3; always use `//` for index math (`mid = (low + high) // 2`, never `/`).
- **Mutable default arguments:** avoid `def f(a, high=[])` style bugs — irrelevant to binary search directly, but common in wrapping recursive helpers.
- **`sort()` returns `None`:** `a = a.sort()` silently sets `a` to `None` — use `a.sort()` (in place) or `sorted(a)` (returns new list), never assign `sort()`'s return value.
- **Off-by-one with `len(a)` vs `len(a) - 1`:** always double check whether your convention is inclusive or exclusive at initialization.

---

## 12. Common Mistakes

### 12.1 Infinite Loops

**Cause:** Using `low = mid` (not `mid + 1`) with a floor-biased `mid` in a "largest true" search.

```python
# BUGGY — infinite loop when hi == lo + 1 and feasible(lo) is True
mid = lo + (hi - lo) // 2   # floor mid
if feasible(mid):
    lo = mid                 # if mid == lo, lo never changes!
```

**Fix:** use ceiling mid (`mid = lo + (hi - lo + 1) // 2`) whenever the "keep" branch sets `lo = mid`.

### 12.2 Wrong Mid Calculation

```python
mid = (low + high) / 2     # WRONG in Python for indices — produces a float!
mid = (low + high) // 2    # correct
```

### 12.3 Wrong Boundary Update

```python
# WRONG: discards mid even though a[mid] might be the answer
if a[mid] >= x:
    high = mid - 1     # should be high = mid in an exclusive-range lower_bound template
```

### 12.4 Incorrect Loop Condition

Mixing `while low <= high` with an exclusive `[low, high)` interval initialization (`high = len(a)`) causes out-of-bounds access on `a[high]`.

### 12.5 Missing Equality Case

Forgetting to check `a[mid] == target` before the `<`/`>` branches in Template A causes the standard search to always return `-1`, even for present elements — a totally silent bug.

### 12.6 Lower vs Upper Bound Confusion

| Symptom | Cause |
|---|---|
| Off-by-one when counting duplicates | Swapped `bisect_left`/`bisect_right` |
| First occurrence returns last occurrence's index | Used `upper_bound` logic instead of `lower_bound` |

### 12.7 Predicate Mistakes

- Predicate not actually monotonic (e.g., mistakenly including a term that decreases feasibility as `x` grows) — always sanity check monotonicity with 3+ manual test points before trusting binary search.
- Off-by-one inside `feasible()` itself (e.g., `<=` vs `<` in a greedy simulation) — test `feasible()` independently first.

### 12.8 Search Space Mistakes

Setting `hi` too small (excludes the true answer) or too large (wastes iterations, and can risk overflow in other languages — not Python, but still wasteful). Always double check that the extreme values `feasible(lo)` and `feasible(hi)` bracket the true answer correctly (`feasible(hi)` should be `True`, `feasible(lo - 1)` should be `False`, if `lo` is meant to be reachable).

### 12.9 Floating-Point Precision Issues

Comparing floats with `==` inside a binary search predicate never converges reliably — always use a fixed iteration count or an epsilon-based tolerance (`abs(hi - lo) > 1e-9`).

---

## 13. Cheat Sheets

### 13.1 Binary Search Templates Cheat Sheet

```python
# STANDARD SEARCH
low, high = 0, n - 1
while low <= high:
    mid = low + (high - low) // 2
    if a[mid] == target: return mid
    elif a[mid] < target: low = mid + 1
    else: high = mid - 1
return -1

# LOWER BOUND (first index a[i] >= x)   == bisect_left
low, high = 0, n
while low < high:
    mid = low + (high - low) // 2
    if a[mid] < x: low = mid + 1
    else: high = mid
return low

# UPPER BOUND (first index a[i] > x)    == bisect_right
low, high = 0, n
while low < high:
    mid = low + (high - low) // 2
    if a[mid] <= x: low = mid + 1
    else: high = mid
return low

# SMALLEST TRUE (binary search on answer)
lo, hi = LOW, HIGH
while lo < hi:
    mid = lo + (hi - lo) // 2
    if feasible(mid): hi = mid
    else: lo = mid + 1
return lo

# LARGEST TRUE (binary search on answer)
lo, hi = LOW, HIGH
while lo < hi:
    mid = lo + (hi - lo + 1) // 2   # ceiling mid!
    if feasible(mid): lo = mid
    else: hi = mid - 1
return lo
```

### 13.2 Complexity Table

| Operation | Time | Space |
|---|---|---|
| Standard binary search | `O(log n)` | `O(1)` iter / `O(log n)` recursive |
| `bisect_left` / `bisect_right` | `O(log n)` | `O(1)` |
| `insort` | `O(n)` | `O(1)` extra (in-place shift) |
| Binary search on answer | `O(log(range) * check_cost)` | depends on `check_cost` |
| Rotated array search | `O(log n)` | `O(1)` |
| Rotated array w/ duplicates | `O(n)` worst, `O(log n)` avg | `O(1)` |
| Matrix search (flattened) | `O(log(rows*cols))` | `O(1)` |
| Matrix search (staircase) | `O(rows + cols)` | `O(1)` |
| Median of two sorted arrays | `O(log(min(m,n)))` | `O(1)` |

### 13.3 Boundary Update Rules Cheat Sheet

| Situation | Rule |
|---|---|
| `a[mid]` cannot be the answer, answer is right | `low = mid + 1` |
| `a[mid]` cannot be the answer, answer is left | `high = mid - 1` |
| `a[mid]` COULD be the answer, keep searching right-inclusive | `low = mid` (needs ceiling mid) |
| `a[mid]` COULD be the answer, keep searching left-inclusive | `high = mid` |

### 13.4 Recognition Guide (One-Liner Cheat Sheet)

> "Sorted + looking for a value/boundary" → Templates A–D.
> "Min/Max X such that condition(X)" + monotonic condition → Binary Search on Answer.
> "Rotated" → check which half is sorted.
> "Peak/Mountain" → compare `a[mid]` to neighbor.
> "Matrix" → flatten (if fully sorted) or staircase (if only row/col sorted).

### 13.5 Python Syntax Cheat Sheet

```python
import bisect
bisect.bisect_left(a, x)        # lower bound
bisect.bisect_right(a, x)       # upper bound (alias bisect.bisect)
bisect.insort_left(a, x)        # insert, keep sorted, leftmost
bisect.insort_right(a, x)       # insert, keep sorted, rightmost (alias insort)
bisect.bisect_left(a, x, key=lambda e: e.value)   # Python 3.10+
```

### 13.6 Predicate Template Cheat Sheet

```python
def feasible(x: int) -> bool:
    # greedy / simulation check
    ...
    return condition_holds
```

---

## 14. Practice Problems

> Difficulty and exact constraints may shift slightly across platforms/time — always re-check the live problem statement.

### 14.1 Basics

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Binary Search | LeetCode (704) | Easy | Standard search |
| Implement Binary Search | GeeksforGeeks | Easy | Standard search |
| Binary Search | HackerRank | Easy | Standard search |

### 14.2 Lower Bound / Upper Bound

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Search Insert Position | LeetCode (35) | Easy | Lower bound |
| Floor in a Sorted Array | GeeksforGeeks | Easy | Floor/lower bound |
| Ceiling in a Sorted Array | GeeksforGeeks | Easy | Ceiling/upper bound |

### 14.3 First / Last Occurrence

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Find First and Last Position of Element in Sorted Array | LeetCode (34) | Medium | First/last occurrence |
| Number of Occurrences | GeeksforGeeks | Easy | `bisect_right - bisect_left` |

### 14.4 Rotated Array

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Search in Rotated Sorted Array | LeetCode (33) | Medium | Rotated search |
| Search in Rotated Sorted Array II | LeetCode (81) | Medium | Rotated w/ duplicates |
| Find Minimum in Rotated Sorted Array | LeetCode (153) | Medium | Find min in rotated |
| Find Minimum in Rotated Sorted Array II | LeetCode (154) | Hard | Find min w/ duplicates |

### 14.5 Peak Element

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Find Peak Element | LeetCode (162) | Medium | Peak element |
| Peak Index in a Mountain Array | LeetCode (852) | Easy | Mountain array |
| Find in Mountain Array | LeetCode (1095) | Hard | Mountain array + search |

### 14.6 Matrix Search

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Search a 2D Matrix | LeetCode (74) | Medium | Flattened matrix |
| Search a 2D Matrix II | LeetCode (240) | Medium | Staircase search |
| Kth Smallest Element in a Sorted Matrix | LeetCode (378) | Medium | Binary search on value |

### 14.7 Infinite Array

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Search in a Sorted Array of Unknown Size | LeetCode (702) | Medium | Exponential + binary search |

### 14.8 Binary Search on Answer

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Koko Eating Bananas | LeetCode (875) | Medium | Smallest true |
| Capacity to Ship Packages Within D Days | LeetCode (1011) | Medium | Smallest true |
| Split Array Largest Sum | LeetCode (410) | Hard | Smallest true |
| Smallest Divisor Given a Threshold | LeetCode (1283) | Medium | Smallest true |
| Minimize Max Distance to Gas Station | LeetCode (774) | Hard | Floating point / largest true |
| Aggressive Cows | Spoj / GeeksforGeeks | Medium | Largest true |
| Allocate Minimum Number of Pages | GeeksforGeeks / Code360 | Medium | Smallest true |
| Painter's Partition Problem | GeeksforGeeks / Code360 | Medium | Smallest true |

### 14.9 Allocation / Optimization

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Magnetic Force Between Two Balls | LeetCode (1552) | Medium | Largest true |
| Divide Chocolate | LeetCode (1231) | Hard | Largest true |
| Minimum Number of Days to Make m Bouquets | LeetCode (1482) | Medium | Smallest true |

### 14.10 Advanced Binary Search

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Median of Two Sorted Arrays | LeetCode (4) | Hard | Partition-based |
| Kth Element of Two Sorted Arrays | GeeksforGeeks / InterviewBit | Hard | Partition-based |
| K-th Smallest Prime Fraction | LeetCode (786) | Hard | Binary search on value + heap |

### 14.11 Competitive Programming Sources

| Source | Typical style |
|---|---|
| Codeforces | "Binary search on answer" tagged problems, often combined with greedy or two pointers |
| CSES Problem Set | "Factory Machines," "Array Division" — classic binary search on answer |
| AtCoder | Binary search combined with number theory or DP feasibility checks |
| CodeChef | Optimization-flavored binary search on answer problems |

---

## 15. Final Revision

### 15.1 One-Page Notes

- Binary search halves the search space each step → `O(log n)`.
- Requires sorted data or a monotonic predicate.
- Four templates to know cold: Standard, Lower Bound, Upper Bound, Binary-Search-on-Answer (both directions).
- `bisect_left` = lower bound; `bisect_right` = upper bound; their difference = count of an element.
- Binary Search on Answer = binary search over the **answer**, not the array, using a monotonic `feasible(x)` predicate.
- Ceiling mid (`(lo + hi + 1) // 2`) is required whenever the "keep" branch does `lo = mid`.
- Rotated array search: figure out which half is sorted by comparing `a[low]` and `a[mid]`.
- Peak element: compare `a[mid]` to `a[mid+1]` to determine uphill direction.

### 15.2 Mind Map (Text Form)

```
Binary Search
├── On Arrays
│   ├── Exact Match (Template A)
│   ├── Boundary Search (Lower/Upper Bound)
│   ├── Rotated Array
│   │   ├── No duplicates -> O(log n)
│   │   └── With duplicates -> O(n) worst case
│   ├── Peak / Mountain Array
│   ├── Matrix (Flattened / Staircase)
│   └── Infinite / Unknown-size Array (exponential probe)
└── On Answer (Predicate-Based)
    ├── Smallest feasible X (False...True)
    ├── Largest feasible X (True...False, needs ceiling mid)
    └── Partition-based (Median of Two Sorted Arrays)
```

### 15.3 Pattern Map (Quick Lookup)

| If the problem says... | Use... |
|---|---|
| "find index of X" | Template A |
| "first/last occurrence" | Templates B/C |
| "rotated" | Rotated pattern |
| "peak/mountain" | Peak pattern |
| "matrix" | Matrix pattern |
| "min/max such that..." | Binary Search on Answer |

### 15.4 Recognition Guide (Repeat for Retention)

Sorted + value lookup → boundary templates.
Optimization + monotonic condition → binary search on answer.
Rotated → sorted-half detection.
Matrix → flatten or staircase depending on sortedness guarantee.

### 15.5 Complexity Sheet (Repeat for Retention)

All core operations: `O(log n)` time, `O(1)` space (iterative). Binary Search on Answer: `O(log(range) * check_cost)`.

### 15.6 Boundary Rules (Repeat for Retention)

`low = mid + 1` / `high = mid - 1` when `mid` is provably wrong.
`low = mid` (ceiling mid) / `high = mid` (floor mid) when `mid` could still be the answer.

### 15.7 Interview Cheat Sheet (Condensed)

1. Confirm sorted/monotonic precondition.
2. State inclusive vs exclusive convention out loud.
3. Write `feasible()` (if binary search on answer) and test it standalone.
4. Choose the correct template (Section 13.1).
5. Dry run on `n = 0, 1, 2`.
6. State final complexity.


### 15.9 1-Hour Revision

Re-read Sections 3, 4, 5, 6 in full; re-implement Koko Eating Bananas and Search in Rotated Sorted Array from scratch without referencing this handbook, then check against the templates here.

---

## 16. FAQs

**Q: Why does Python not need the `low + (high - low) / 2` overflow-safe formula?**
A: Python integers have arbitrary precision — they grow as large as needed and never overflow. The overflow-safe formula is a carryover habit from languages like Java/C++ with fixed-width integers, and remains fine (if unnecessary) to use in Python.

**Q: When should I use `bisect` vs writing my own binary search?**
A: Use `bisect` for plain "find in sorted array" tasks. Write your own only when you need a custom predicate that `bisect`'s simple `<` comparison can't express (e.g., "binary search on answer" problems).

**Q: How do I know whether to use `lo = mid` or `lo = mid + 1`?**
A: If `a[mid]` (or `feasible(mid)`) could still be a valid answer, don't discard it — use `hi = mid` or `lo = mid` (with ceiling mid). If `mid` is provably not the answer, safely move past it with `lo = mid + 1` or `hi = mid - 1`.

**Q: Is recursive or iterative binary search better for interviews?**
A: Iterative is generally preferred — no stack overflow risk and marginally faster. Use recursive only if explicitly asked or if it fits naturally into a larger recursive algorithm.

**Q: What's the difference between "binary search" and "binary search on answer"?**
A: Classic binary search finds a value **within an existing sorted array**. Binary search on answer treats an **answer variable** (e.g., speed, capacity, distance) as the search space and uses a monotonic feasibility check as the comparison function — no array indexing involved.

**Q: My binary search works on small inputs but infinite-loops on larger ones. Why?**
A: Almost always a boundary update bug: either you're using a floor-biased mid with `lo = mid` (needs ceiling mid instead), or your loop condition doesn't match your interval convention (inclusive vs exclusive). Re-check Section 12.1 and 12.4.

**Q: Can binary search be used on unsorted data?**
A: Only if you can define a monotonic predicate over some transformation of that data (e.g., rotated sorted arrays are technically "unsorted" globally but retain enough structure). On truly unstructured, non-monotonic data, binary search gives silently wrong answers.

**Q: How many iterations does binary search take?**
A: `ceil(log2(n))` for an array of size `n`; for binary search on answer, `ceil(log2(hi - lo))`.

**Q: Does binary search work on linked lists?**
A: Not efficiently — indexing into the middle of a linked list is `O(n)`, so binary search on a plain singly/doubly linked list degrades to `O(n log n)` total, worse than a simple linear scan. Skip lists (an augmented linked structure) solve this by adding shortcut pointers.

**Q: What's the difference between `bisect_left` and `bisect_right` again, in one sentence?**
A: `bisect_left` finds the insertion point **before** any equal elements; `bisect_right` finds the insertion point **after** any equal elements.

---
