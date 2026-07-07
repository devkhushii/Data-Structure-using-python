# The Complete Two Pointer Technique Handbook (Python Edition)


## 📚 Table of Contents

1. [Introduction to Two Pointer Technique](#1-introduction-to-two-pointer-technique)
2. [Python Foundations for Two Pointer](#2-python-foundations-for-two-pointer)
3. [Types of Two Pointer Techniques](#3-types-of-two-pointer-techniques)
4. [Core Pattern: Pair Sum / Two Sum (Sorted Array)](#4-core-pattern-pair-sum--two-sum-sorted-array)
5. [Three Sum](#5-three-sum)
6. [Four Sum](#6-four-sum)
7. [Remove Duplicates from Sorted Array](#7-remove-duplicates-from-sorted-array)
8. [Move Zeroes](#8-move-zeroes)
9. [Dutch National Flag (Sort Colors)](#9-dutch-national-flag-sort-colors)
10. [Container With Most Water](#10-container-with-most-water)
11. [Trapping Rain Water](#11-trapping-rain-water)
12. [Valid Palindrome](#12-valid-palindrome)
13. [Reverse String / Reverse Words](#13-reverse-string--reverse-words)
14. [Merge Two Sorted Arrays](#14-merge-two-sorted-arrays)
15. [Squares of a Sorted Array](#15-squares-of-a-sorted-array)
16. [K Closest Elements](#16-k-closest-elements)
17. [Intersection of Two Arrays](#17-intersection-of-two-arrays)
18. [Fast & Slow Pointer (Floyd's Technique)](#18-fast--slow-pointer-floyds-technique)
19. [Middle of Linked List](#19-middle-of-linked-list)
20. [Happy Number](#20-happy-number)
21. [Two Pointer vs Sliding Window](#21-two-pointer-vs-sliding-window)
22. [Problem Recognition Framework](#22-problem-recognition-framework)
23. [Optimization Journeys: Brute Force → Two Pointer](#23-optimization-journeys-brute-force--two-pointer)
24. [Interview Preparation Guide](#24-interview-preparation-guide)
25. [Python-Specific Tips & Idioms](#25-python-specific-tips--idioms)
26. [Common Mistakes Catalog](#26-common-mistakes-catalog)
27. [Cheat Sheets](#27-cheat-sheets)
28. [Practice Problem Bank](#28-practice-problem-bank)
29. [Final Revision Kit](#29-final-revision-kit)
30. [FAQs](#30-faqs)

---

## 1. Introduction to Two Pointer Technique

### 1.1 What is the Two Pointer Technique?

The **Two Pointer Technique** is an algorithmic pattern where **two index variables (pointers)** traverse a data structure — usually an array, string, or linked list — according to a specific set of rules, to solve a problem in **less time and/or space** than a brute-force nested-loop approach.

> **Formal definition:** A Two Pointer algorithm maintains two references (indices or node references) into a sequence, and advances one or both references based on a comparison or condition, until a termination condition is met, thereby avoiding redundant re-scanning of already-examined elements.

### 1.2 History and Origin

- The technique doesn't have a single "inventor" — it emerges naturally from **merge-sort's merge step** (John von Neumann, 1945), which is the earliest well-known "two pointer" procedure: merging two sorted lists using one pointer per list.
- It became a named, teachable pattern through **competitive programming folklore** (Topcoder, ACM-ICPC editorials) and later through **interview prep culture** (CTCI, LeetCode, NeetCode, Blind 75), where it was formalized as a distinct pattern separate from brute force.
- Floyd's Cycle Detection Algorithm (Robert W. Floyd, ~1967) formalized the **Fast & Slow pointer** subtype, originally used for detecting cycles in functional iteration sequences (e.g., pseudo-random number generators).

### 1.3 Why Two Pointer Exists

Most naive solutions to array/string problems use **nested loops** — O(n²) or worse — because they re-check pairs or windows redundantly.

Two Pointer exists to exploit **structure already present in the data** (sortedness, monotonicity, or a linked structure) so that:
- Each pointer moves **forward only** (never backtracks) in most variants.
- Each element is visited a **constant number of times** (typically once or twice).
- This collapses O(n²) brute force into **O(n)** or O(n log n).

### 1.4 Intuition

Think of two pointers as **two people scanning a line from different starting points**, communicating with each other about what they see, and stepping toward or away from each other based on that feedback — instead of one person re-scanning the entire line for every position (which is what nested loops do).

### 1.5 Real-World Analogy

> **The Library Shelf Analogy:** Imagine a **perfectly sorted shelf of books by price**, and you want two books whose combined price equals exactly $50. Instead of comparing every book with every other book (brute force), you stand at the **cheapest** book (left pointer) and someone else stands at the **most expensive** book (right pointer). If the sum is too high, the right person steps one book inward (cheaper). If too low, the left person steps one book inward (pricier). You converge on the answer in one pass — because the shelf is sorted, you never need to re-check books you've already ruled out.

Another analogy: **Two friends walking towards each other in a tunnel** to meet in the middle — much faster than one friend walking the entire tunnel alone and back.

### 1.6 Characteristics

| Characteristic | Description |
|---|---|
| Pointer count | Exactly two (sometimes generalized to k pointers) |
| Movement | Forward-only (opposite/same direction) or fast-slow (different speeds) |
| Precondition | Often requires sorted data or a linked/cyclic structure |
| Complexity gain | O(n²) → O(n) or O(n log n) typical |
| Space | Usually O(1) extra space (in-place) |
| Traversal | Single pass (occasionally two passes) |

### 1.7 Advantages

- **Time efficiency**: Converts many O(n²) brute-force problems to O(n).
- **Space efficiency**: Most implementations use O(1) extra space — no auxiliary hash maps or arrays needed.
- **Simplicity**: Once recognized, the code is usually short and readable.
- **In-place operations**: Ideal for array mutation problems (remove duplicates, move zeroes, partitioning).
- **Elegant termination**: Natural stopping conditions (`left < right`, `slow != fast`) prevent infinite loops when applied correctly.

### 1.8 Disadvantages / Limitations

- **Requires structure**: Doesn't work on unsorted, unstructured data unless you sort first (adding O(n log n)) or the problem has inherent order (like a linked list).
- **Not always applicable**: Some problems need hashing/DP even if they look similar (e.g., unsorted Two Sum with **arbitrary output order requirement** needs a hash map, not two pointers, unless you're okay losing original indices).
- **Pointer logic can be subtle**: Off-by-one errors, incorrect movement rules, and duplicate handling are common pitfalls.
- **Not a silver bullet**: Doesn't apply to problems needing **global reordering** without monotonic structure (e.g., arbitrary graph problems).

### 1.9 Applications (Overview)

- Searching for pairs/triplets/quadruplets with a target sum in sorted arrays.
- In-place array partitioning and deduplication.
- String palindrome checking and reversal.
- Merging sorted sequences.
- Cycle detection in linked lists / functional graphs.
- Finding the middle of a linked list in one pass.
- Container/water-trapping geometry problems.
- Comparing/matching two sequences (subsequence check, string comparison with backspaces).

### 1.10 Real-World Examples (Software Engineering)

- **Merge step of external sort / merge sort** — merging two sorted runs from disk.
- **TCP/IP sliding window fallback logic** conceptually related to pointer bounds (not identical to sliding window pattern, but pointer-bound reasoning is shared).
- **Diffing algorithms** (like `git diff`) use two-pointer-style scanning over two sequences of lines.
- **Database merge joins** — merging two sorted relations by walking two cursors forward.
- **Garbage collection** (Floyd's cycle detection is literally used to detect reference cycles in certain runtime systems).


---

## 2. Python Foundations for Two Pointer

Before diving into patterns, let's establish the Python-specific mechanics you'll use in every two-pointer implementation.

### 2.1 Pointer Variables in Python

Python has no native pointer/reference type for primitives like C++ — "pointers" here just means **integer indices** into a sequence (or, for linked lists, **references to node objects**).

```python
left = 0
right = len(arr) - 1
```

That's it. `left` and `right` are plain integers. All the "pointer" logic is really **index arithmetic**.

### 2.2 while vs for loops

Two pointer problems almost always use `while`, not `for`, because:
- The number of iterations is **data-dependent**, not fixed.
- Both pointers may move by different amounts on different iterations.
- Termination depends on a **relationship between two variables** (`left < right`), not a fixed range.

```python
# Correct: while loop, because loop bound depends on both pointers
while left < right:
    ...

# Awkward / usually wrong for two-pointer: for loop can't easily skip variable steps
for i in range(len(arr)):
    ...  # doesn't naturally support two independently-moving indices
```

> **Rule of thumb:** If both pointers move together at a fixed relationship (e.g., `right = left + k`), a `for` loop MAY work. If pointers move conditionally, always use `while`.

### 2.3 enumerate()

Useful when you need **value + index** together, e.g., for the same-direction "slow" pointer while scanning with `for`:

```python
slow = 0
for fast, value in enumerate(arr):
    if value != 0:
        arr[slow], arr[fast] = arr[fast], arr[slow]
        slow += 1
```

Here `fast` comes from `enumerate`, while `slow` is manually tracked — a common same-direction two-pointer idiom.

### 2.4 zip()

`zip()` is useful when comparing **two separate sequences** element-by-element (merge-style two pointer over two different lists, rather than one list with two indices):

```python
i, j = 0, 0
merged = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        merged.append(a[i]); i += 1
    else:
        merged.append(b[j]); j += 1
```

`zip()` itself is NOT a substitute for two-pointer merge logic (it stops at the shorter list and can't do conditional branching per element) — but it's handy for simpler **parallel, lock-step** dual traversal, e.g., comparing two strings of equal length.

### 2.5 reversed()

`reversed()` gives you an iterator from the end — sometimes a clean substitute for a manual right-to-left pointer when you don't need index values:

```python
for ch in reversed(s):
    ...
```

But when you need **both indices simultaneously** (typical opposite-direction two pointer), you cannot rely on `reversed()` alone — you need explicit `left`/`right` integers.

### 2.6 Swapping and Tuple Assignment

Python's tuple assignment makes in-place swaps trivial — critical for partitioning patterns:

```python
arr[i], arr[j] = arr[j], arr[i]
```

This is atomic-looking in code (though it evaluates the right-hand tuple first, then assigns), and is idiomatic Python — always prefer this over a manual temp variable.

### 2.7 Slicing — Use With Caution

```python
arr[left:right+1]
```

Slicing creates a **new list** (O(k) time and space) — great for readability in non-performance-critical code, but **defeats the O(1) space advantage** of two pointer if used inside a hot loop. Avoid slicing inside the pointer loop itself; only use it for final result construction if needed.

### 2.8 Best Practices

- Name pointers meaningfully: `left`/`right`, `slow`/`fast`, `i`/`j`, `read`/`write` — not `p1`/`p2`.
- Always define **clear loop invariants** before coding (e.g., "everything left of `slow` is non-zero").
- Prefer `while left < right` (strict) over `while left <= right` unless the problem explicitly needs pointers to meet at the same index.
- Keep the swap/update logic **inside** the loop body, not scattered.
- Add **assertions** during development (`assert left <= right`) to catch invariant violations early — remove before submission if performance-critical.

### 2.9 Performance Considerations

- Avoid `len(arr)` inside a tight loop condition repeatedly if it's expensive to compute (for lists it's O(1) in Python, so this is a non-issue for `list`, but matters for custom objects).
- Avoid unnecessary list slicing/copying inside loops (`O(n)` per slice → turns O(n) into O(n²)).
- Prefer in-place swaps over building new lists when the problem asks for in-place modification.
- Use `sys.stdin` fast input in competitive programming contexts where I/O dominates.


---

## 3. Types of Two Pointer Techniques

### 3.1 Overview Table

| Type | Pointer Start | Movement | Typical Use |
|---|---|---|---|
| Opposite Direction (Converging) | Both ends (`0`, `n-1`) | Move toward each other | Pair sum, palindrome, container with water |
| Same Direction (Fast-Slow, non-cyclic) | Both at `0` | Both move forward, different rates/conditions | Remove duplicates, move zeroes, partition |
| Fast & Slow (Cyclic) | Both at head | Fast moves 2x speed of slow | Cycle detection, middle node, happy number |
| Multiple Pointers (k>2) | Various | Nested two-pointer inside a loop | 3Sum, 4Sum |
| Bidirectional Scan | Both ends | Converge with skip logic | Trapping rain water, valid palindrome with skips |
| Diverging Pointers | Same start (middle) | Move outward | Expand-around-center (palindromic substrings) |

### 3.2 Opposite Direction Pointers

**Definition:** One pointer starts at index `0`, the other at index `n-1`. They move toward each other until they cross or meet.

**ASCII Visualization:**
```
Array:  [1, 3, 5, 7, 9, 11]
Index:   0  1  2  3  4   5

Step 0:
 L                      R
 [1, 3, 5, 7, 9, 11]
 ↓                   ↓
 1                  11     -> sum too big, move R left

Step 1:
 L                  R
 [1, 3, 5, 7, 9, 11]
 ↓               ↓
 1               9        -> sum too small, move L right

Step 2:
    L            R
 [1, 3, 5, 7, 9, 11]
    ↓          ↓
    3          9
```

**When to use:** Sorted array, need pair/triplet with a target relationship (sum, difference), or symmetric checks (palindrome).

### 3.3 Same Direction Pointers (Read/Write, Slow/Fast without cycles)

**Definition:** Both pointers start at index `0`. One (`fast`/`read`) scans ahead; the other (`slow`/`write`) marks the position for the next valid element.

**ASCII Visualization (Remove Duplicates):**
```
arr = [1, 1, 2, 2, 3]
        s
        f
slow=0, fast=0 -> arr[0]==arr[0], fast++

arr = [1, 1, 2, 2, 3]
        s  f
fast=1: arr[1]==arr[slow] -> duplicate, fast++ (slow stays)

arr = [1, 1, 2, 2, 3]
        s     f
fast=2: arr[2]!=arr[slow] -> slow++, copy, now slow=1
```

**When to use:** In-place deduplication, partitioning, moving/filtering elements, merging into a single array from the back.

### 3.4 Fast & Slow Pointer (Tortoise and Hare)

**Definition:** Slow pointer moves 1 step, fast pointer moves 2 steps, per iteration. Used for detecting cycles or finding midpoints without knowing the length in advance.

**ASCII Visualization:**
```
1 -> 2 -> 3 -> 4 -> 5
          ^         |
          |_________|

slow: 1 -> 2 -> 3 -> 4 -> 5 -> 3 -> 4 ...
fast: 1 -> 3 -> 5 -> 4 -> 3 -> ...

Eventually slow == fast  →  cycle detected
```

### 3.5 Multiple Pointers (k > 2)

Used when the base pattern (two pointer) is nested inside an outer loop — e.g., **3Sum** fixes one index and runs opposite-direction two pointer on the rest; **4Sum** fixes two indices and runs two pointer on the remainder.

### 3.6 Bidirectional Scan with Skip Logic

Similar to opposite direction, but pointers may **skip** over invalid characters/values before comparing (e.g., skip non-alphanumeric characters in palindrome check).

### 3.7 Diverging / Expand-Around-Center Pointers

**Definition:** Both pointers start at the **same index (or adjacent indices)** and move **outward** in opposite directions, rather than starting at the ends and moving inward.

```
s = "babad"
       ↑
     l=r=2 ('b')
  l←    →r
 "b[a b a]d"
```

Used in problems like **Longest Palindromic Substring** (expand around each center).


---

## 4. Core Pattern: Pair Sum / Two Sum (Sorted Array)

### 4.1 Problem Statement

> Given a **sorted** array `nums` and an integer `target`, return indices (or values) of two numbers such that they add up to `target`. Assume exactly one solution exists (or return `[-1, -1]` if none).

### 4.2 Why It Exists / Intuition

Brute force checks every pair → O(n²). But because the array is **sorted**, we know:
- If the current sum is **too small**, moving the left pointer right can only increase it (since array is sorted ascending).
- If the current sum is **too large**, moving the right pointer left can only decrease it.

This monotonicity lets us **eliminate one entire row or column of the conceptual n×n pair matrix** on every step — this is the core insight of opposite-direction two pointer.

### 4.3 Real-World Analogy

Like adjusting hot and cold taps to get a target water temperature — if it's too hot, reduce hot water (move right pointer down); if too cold, increase hot water (move left pointer up). You converge, never randomly re-trying.

### 4.4 ASCII Visualization

```
nums = [2, 7, 11, 15],  target = 9

L=0                R=3
[2, 7, 11, 15]
 2        15   sum=17 > 9  → R--

L=0        R=2
[2, 7, 11, 15]
 2    11        sum=13 > 9  → R--

L=0    R=1
[2, 7, 11, 15]
 2  7            sum=9 == 9  → FOUND! [0, 1]
```

### 4.5 Python Implementation

```python
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """Return 0-indexed pair (i, j) with i < j such that nums[i] + nums[j] == target.
    Assumes nums is sorted in non-decreasing order."""
    left, right = 0, len(nums) - 1          # pointers at both ends

    while left < right:                      # stop when they'd cross/meet
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]              # found exact match
        elif current_sum < target:
            left += 1                         # need a bigger sum -> move left up
        else:
            right -= 1                        # need a smaller sum -> move right down

    return [-1, -1]                           # no pair found
```

### 4.6 Line-by-Line Explanation

| Line | Explanation |
|---|---|
| `left, right = 0, len(nums) - 1` | Initialize pointers at the two extremes of the sorted array |
| `while left < right:` | Loop until pointers meet or cross — guarantees each index pair is checked once |
| `current_sum = nums[left] + nums[right]` | Compute the current candidate sum |
| `if current_sum == target:` | Exact match found — return immediately |
| `elif current_sum < target: left += 1` | Sum too small — the only way to increase it (given sorted array) is to increase the left value |
| `else: right -= 1` | Sum too large — the only way to decrease it is to decrease the right value |
| `return [-1, -1]` | No valid pair exists in the array |

### 4.7 Complete Dry Run

| Step | Left | Right | nums[L] | nums[R] | Sum | Decision | Action |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 3 | 2 | 15 | 17 | 17 > 9 | right-- |
| 2 | 0 | 2 | 2 | 11 | 13 | 13 > 9 | right-- |
| 3 | 0 | 1 | 2 | 7 | 9 | 9 == 9 | return [0,1] |

### 4.8 Time & Space Complexity

- **Time:** O(n) — each pointer moves at most n times total, combined.
- **Space:** O(1) — only two integer pointers used (excluding output).
- (If the array must first be sorted: O(n log n) total, O(n) if you need original-index mapping.)

### 4.9 Edge Cases

- Empty array or single element → no pair possible, return `[-1, -1]`.
- All elements identical (e.g., `[3,3,3,3]`, target=6) → still works, first valid pair found.
- Negative numbers — works fine since comparisons are still monotonic in a sorted array.
- No valid pair exists — loop exits naturally via `left < right` becoming false.
- Duplicates needing distinct indices — verify problem doesn't require `i != j` explicitly if array could have same-value elements at different indices (this pattern already ensures `left != right`).

### 4.10 Common Mistakes

- Using `left <= right` when the problem requires `i != j` (this would allow the same index to pair with itself in some formulations — verify based on exact problem definition).
- Forgetting the array must be **sorted** — this pattern silently gives wrong answers on unsorted input.
- Off-by-one when converting between 0-indexed and 1-indexed answers (some platforms, like LeetCode's "Two Sum II", expect 1-indexed output).
- Not handling the "no solution" case, causing an infinite loop or an unhandled `None` return.

### 4.11 Interview Tips

- Always ask: "Is the array sorted, or can I sort it? Do I need to preserve original indices?" — if original indices matter and sorting is required, you must **sort (value, index) pairs**, not just values.
- Mention explicitly why this beats brute force (O(n) vs O(n²)) — interviewers want to hear the **monotonicity argument**, not just "it's faster."
- If asked for **unsorted** Two Sum with original indices, the two-pointer technique on a value-sorted copy still works if you carry index metadata; alternatively, a hash map gives O(n) without sorting — know both and articulate the tradeoff (hash map uses O(n) extra space, two pointer uses O(1) extra space after O(n log n) sort).

### 4.12 Optimizations

- If you only need existence (not indices), you can early-exit as shown.
- If the array has many duplicates and you need **all unique pairs**, add duplicate-skipping logic (see Three Sum section — same principle applies).

### 4.13 Variations

- Two Sum with indices needed **on unsorted input** → use a hash map instead (not two pointer), or sort (value, original_index) tuples.
- Two Sum **closest to target** (not exact) → track `min(abs(diff))` while doing the same pointer walk.
- Two Sum **count all pairs** (with duplicates) → requires careful counting of equal-value runs rather than simple pointer increments.

### 4.14 Practice Problems

- LeetCode 167 — Two Sum II - Input Array Is Sorted (Easy)
- LeetCode 1 — Two Sum (Easy, unsorted variant — hash map preferred)
- GeeksforGeeks — Two Sum - Pair with Given Sum in Sorted Array

### 4.15 Summary / Revision Notes

- **Pattern:** Opposite direction pointer.
- **Precondition:** Sorted array.
- **Core idea:** Sum too small → move left up; sum too large → move right down.
- **Complexity:** O(n) time, O(1) space.
- **Keyword triggers:** "sorted array", "pair sum", "find two numbers".


---

## 5. Three Sum

### 5.1 Problem Statement

> Given an array `nums`, find all **unique triplets** `[a, b, c]` such that `a + b + c == 0` (or a given target).

### 5.2 Intuition

Three Sum = **fix one pointer**, then solve **Two Sum (sorted)** on the remaining subarray. This is the classic "reduce k-sum to (k-1)-sum" recursive/iterative idea.

### 5.3 ASCII Visualization

```
Sorted: [-4, -1, -1, 0, 1, 2]
          i    L          R
Fix i = -4, run two-pointer on [-1,-1,0,1,2] for target 4
```

### 5.4 Python Implementation

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()                                   # sorting enables two-pointer logic
    n = len(nums)
    result = []

    for i in range(n - 2):                        # fixed pointer
        if i > 0 and nums[i] == nums[i - 1]:       # skip duplicate fixed values
            continue
        if nums[i] > 0:                            # smallest value is positive -> no triplet sums to 0
            break

        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:   # skip dup left
                    left += 1
                while left < right and nums[right] == nums[right + 1]: # skip dup right
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result
```

### 5.5 Line-by-Line Explanation

- `nums.sort()`: required precondition for two-pointer to work.
- Outer `for i`: the "fixed" pointer, iterating up to `n-2` (need at least 2 elements after it).
- `if i > 0 and nums[i] == nums[i-1]: continue`: avoids duplicate triplets caused by repeating the same fixed value.
- `if nums[i] > 0: break`: early termination — since sorted, if the smallest remaining value is already positive, no triplet can sum to 0.
- Inner `while left < right`: standard opposite-direction two pointer for the remaining Two Sum subproblem.
- Duplicate-skipping `while` loops after a match: ensures unique triplets in the output.

### 5.6 Dry Run

`nums = [-1, 0, 1, 2, -1, -4]` → sorted: `[-4, -1, -1, 0, 1, 2]`

| i | nums[i] | L | R | Sum | Action |
|---|---|---|---|---|---|
| 0 | -4 | 1 | 5 | -1+2=1 | 1<4 → L++ |
| 0 | -4 | 2 | 5 | -1+2=1 | 1<4 → L++ |
| 0 | -4 | 3 | 5 | 0+2=2 | 2<4 → L++ |
| 0 | -4 | 4 | 5 | 1+2=3 | 3<4 → L++, L==R stop |
| 1 | -1 | 2 | 5 | -1+2=1 | 1==1 → found [-1,-1,2], move both, skip dups |
| 1 | -1 | 3 | 4 | 0+1=1 | 1==1 → found [-1,0,1] |

Result: `[[-1,-1,2], [-1,0,1]]`

### 5.7 Complexity

- **Time:** O(n²) — outer loop O(n) × inner two-pointer O(n).
- **Space:** O(1) extra (excluding output and sort's internal space, O(log n) for Timsort).

### 5.8 Edge Cases

- Array with fewer than 3 elements → return `[]`.
- All zeros → single triplet `[0,0,0]`, must dedupe.
- All positive or all negative → no valid triplet, early `break`/loop completes with empty result.

### 5.9 Common Mistakes

- Forgetting to sort first.
- Forgetting duplicate-skipping (produces repeated triplets).
- Skipping duplicates for `i` **before** checking `i > 0` (causes index error at `i=0`).
- Not skipping duplicates for L/R **after finding a match** (only, not before — skipping too early breaks valid triplet counting).

### 5.10 Interview Tips

Emphasize the **reduction pattern**: k-Sum → fix one → (k-1)-Sum → ... → base case Two Sum via two pointers. This generalizes directly to 4Sum, 5Sum, etc.

### 5.11 Variations

- 3Sum Closest (return triplet whose sum is closest to target, not necessarily equal).
- 3Sum Smaller (count triplets with sum less than target).

### 5.12 Practice Problems

- LeetCode 15 — 3Sum (Medium)
- LeetCode 16 — 3Sum Closest (Medium)
- LeetCode 259 — 3Sum Smaller (Medium, Premium)

---

## 6. Four Sum

### 6.1 Problem Statement

> Find all unique quadruplets `[a,b,c,d]` in `nums` such that `a+b+c+d == target`.

### 6.2 Intuition

Same reduction idea, one level deeper: **fix two pointers** (nested loops), then run two-pointer Two Sum on the rest.

### 6.3 Python Implementation

```python
def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result
```

### 6.4 Complexity

- **Time:** O(n³) — two nested fixed loops × inner two-pointer O(n).
- **Space:** O(1) extra excluding output.

### 6.5 Edge Cases

- Fewer than 4 elements → return `[]`.
- Integer overflow is not a concern in Python (arbitrary precision ints), unlike Java/C++ — worth mentioning in interviews as a Python-specific advantage.

### 6.6 Common Mistakes

- Forgetting the **second** duplicate-skip condition `j > i+1` (must compare relative to the fixed `i`, not just `j > 0`).
- Same left/right duplicate-skipping mistakes as 3Sum.

### 6.7 Generalization: k-Sum

The pattern generalizes: recursively fix pointers until 2 remain, then apply two-pointer. Time complexity for k-Sum is O(n^(k-1)).

### 6.8 Practice Problems

- LeetCode 18 — 4Sum (Medium)
- LeetCode 454 — 4Sum II (different technique — hash map, good to contrast)


---

## 7. Remove Duplicates from Sorted Array

### 7.1 Problem Statement

> Given a sorted array, remove duplicates **in-place** such that each unique element appears only once, and return the new length.

### 7.2 Intuition

Same-direction two pointer: `slow` marks the boundary of the "clean" (deduplicated) region; `fast` scans ahead looking for new unique values to bring into that region.

### 7.3 ASCII Visualization

```
arr = [0,0,1,1,1,2,2,3,3,4]
        s
        f
Advance fast; whenever arr[fast] != arr[slow], slow++ and copy arr[fast] into arr[slow].

Final clean region: [0,1,2,3,4, ...] with slow+1 = 5 valid elements
```

### 7.4 Python Implementation

```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    slow = 0                                  # index of last unique element placed
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1                           # length of deduplicated prefix
```

### 7.5 Line-by-Line Explanation

- `slow = 0`: the first element is trivially unique.
- `for fast in range(1, len(nums))`: scan starts from the second element.
- `if nums[fast] != nums[slow]`: found a new unique value.
- `slow += 1; nums[slow] = nums[fast]`: write the new unique value right after the last known unique one.
- Return `slow + 1` because `slow` is a 0-indexed position, so the count is `slow + 1`.

### 7.6 Dry Run

`nums = [0,0,1,1,1,2,2,3,3,4]`

| fast | nums[fast] | nums[slow] | Match? | slow after | Array state |
|---|---|---|---|---|---|
| 1 | 0 | 0 | same | 0 | unchanged |
| 2 | 1 | 0 | diff | 1 | [0,1,1,1,1,2,2,3,3,4] |
| 3 | 1 | 1 | same | 1 | unchanged |
| 4 | 1 | 1 | same | 1 | unchanged |
| 5 | 2 | 1 | diff | 2 | [0,1,2,1,1,2,2,3,3,4] |
| 6 | 2 | 2 | same | 2 | unchanged |
| 7 | 3 | 2 | diff | 3 | [0,1,2,3,1,2,2,3,3,4] |
| 8 | 3 | 3 | same | 3 | unchanged |
| 9 | 4 | 3 | diff | 4 | [0,1,2,3,4,2,2,3,3,4] |

Result: length `5`, prefix `[0,1,2,3,4]`.

### 7.7 Complexity

- **Time:** O(n) — single pass.
- **Space:** O(1) — in-place.

### 7.8 Edge Cases

- Empty array → return 0.
- All identical elements → result length 1.
- Already all-unique array → `slow` advances every step, no-op copies.

### 7.9 Common Mistakes

- Comparing `nums[fast]` to `nums[fast-1]` instead of `nums[slow]` (works for this specific problem since sorted, but breaks the general "read/write pointer" pattern used in variations like "remove duplicates keeping at most 2").
- Forgetting the `if not nums: return 0` guard, causing an index error on `nums[slow]` access before any assignment (not fatal here since slow starts at 0 safely, but good practice).
- Off-by-one in the final return value (`slow` vs `slow + 1`).

### 7.10 Interview Tips

Interviewers often extend this to "remove duplicates, keep at most **2** occurrences" — know the generalized template:

```python
def remove_duplicates_keep_k(nums: list[int], k: int) -> int:
    slow = 0
    for fast in range(len(nums)):
        if slow < k or nums[fast] != nums[slow - k]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

### 7.11 Variations

- Remove Duplicates II (keep at most 2 copies) — LeetCode 80.
- Remove Element (remove all instances of a given value) — LeetCode 27, same read/write pointer idea.

### 7.12 Practice Problems

- LeetCode 26 — Remove Duplicates from Sorted Array (Easy)
- LeetCode 80 — Remove Duplicates from Sorted Array II (Medium)
- LeetCode 27 — Remove Element (Easy)

---

## 8. Move Zeroes

### 8.1 Problem Statement

> Given an array `nums`, move all `0`s to the end while maintaining the relative order of non-zero elements, in-place.

### 8.2 Intuition

Same-direction two pointer (read/write): `slow` tracks where the next non-zero element should be written; `fast` scans the whole array.

### 8.3 ASCII Visualization

```
[0,1,0,3,12]
  s
  f
fast finds 1 (non-zero) -> swap(slow, fast), slow++

[1,0,0,3,12]
    s
      f
fast finds 3 -> swap(slow, fast), slow++

[1,3,0,0,12]
      s
         f
fast finds 12 -> swap(slow, fast), slow++

[1,3,12,0,0]
```

### 8.4 Python Implementation

```python
def move_zeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

### 8.5 Line-by-Line Explanation

- `slow` always points to the **first zero** (or the position for the next non-zero element).
- When `nums[fast]` is non-zero, we swap it into the `slow` position — this pushes a zero rightward automatically.
- If `fast == slow`, the swap is a no-op, which is fine and simplifies the code (no need for a separate branch).

### 8.6 Dry Run

`nums = [0,1,0,3,12]`

| fast | nums[fast] | Action | Array | slow |
|---|---|---|---|---|
| 0 | 0 | skip | [0,1,0,3,12] | 0 |
| 1 | 1 | swap(0,1) | [1,0,0,3,12] | 1 |
| 2 | 0 | skip | [1,0,0,3,12] | 1 |
| 3 | 3 | swap(1,3) | [1,3,0,0,12] | 2 |
| 4 | 12 | swap(2,4) | [1,3,12,0,0] | 3 |

### 8.7 Complexity

- **Time:** O(n), **Space:** O(1).

### 8.8 Edge Cases

- All zeros → array unchanged (slow never advances, no swaps happen since `nums[fast]` never non-zero).
- No zeros → every step swaps with itself (harmless).
- Single element → trivially correct.

### 8.9 Common Mistakes

- Using extra space (building a new list of non-zeros + appending zeros) when the problem explicitly requires in-place with O(1) extra space.
- Swapping unconditionally (including when `nums[fast] == 0`), which corrupts order.

### 8.10 Interview Tips

Mention this is functionally similar to the **partition step of Quicksort** (Lomuto partition scheme) — same read/write pointer idea, just partitioning by "is zero" instead of "is less than pivot."

### 8.11 Practice Problems

- LeetCode 283 — Move Zeroes (Easy)


---

## 9. Dutch National Flag (Sort Colors)

### 9.1 Problem Statement

> Given an array with only values `0`, `1`, `2`, sort it in-place in one pass, without using a counting sort auxiliary array.

### 9.2 Intuition

This is a **three-pointer** partitioning scheme (an extension of two pointer), invented by Edsger Dijkstra, named after the three colors/bands of the Dutch flag.

- `low`: boundary for region of 0s.
- `mid`: current element being examined.
- `high`: boundary for region of 2s.

### 9.3 ASCII Visualization

```
[2,0,2,1,1,0]
 low
 mid
 high=5

arr[mid]=2 -> swap(mid,high), high--  (don't advance mid, need to re-check swapped-in value)
[0,0,2,1,1,2]
 l  m         h=4
arr[mid]=0 -> swap(low,mid), low++, mid++
[0,0,2,1,1,2]
    lm       h=4
arr[mid]=0 -> same value, low++, mid++
[0,0,2,1,1,2]
       lm   h=4
arr[mid]=2 -> swap(mid,high), high--
[0,0,1,1,2,2]
       l m h=3
arr[mid]=1 -> mid++
...continues until mid > high
```

### 9.4 Python Implementation

```python
def sort_colors(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # NOTE: do NOT increment mid here — the swapped-in value must be re-checked
```

### 9.5 Line-by-Line Explanation

- `low`/`mid`/`high` partition the array into `[0..low-1]=0s`, `[low..mid-1]=1s`, `[mid..high]=unknown`, `[high+1..end]=2s`.
- On seeing `0`: swap to the `low` boundary (guaranteed to be a `1` or already processed), advance both `low` and `mid`.
- On seeing `1`: it's already in the correct conceptual region, just advance `mid`.
- On seeing `2`: swap with `high` boundary, decrement `high`, but **do not advance `mid`** — the newly swapped-in value at `mid` hasn't been examined yet.

### 9.6 Dry Run

Already shown in visualization above; final result: `[0,0,1,1,2,2]`.

### 9.7 Complexity

- **Time:** O(n) — single pass, each element touched a constant number of times.
- **Space:** O(1).

### 9.8 Edge Cases

- Array already sorted → works correctly, mostly `mid++` moves.
- All same value → single region, no swaps needed beyond none.
- Single element → trivially sorted.

### 9.9 Common Mistakes

- Incrementing `mid` after swapping with `high` (this is the **#1 classic bug** — the swapped-in element from the high end hasn't been classified yet).
- Confusing this with simple two-pointer partition (this needs **three** pointers, not two, because there are three categories, not two).

### 9.10 Interview Tips

This is a favorite **FAANG whiteboard question** because it tests whether you understand *why* `mid` shouldn't always advance — a subtle but important detail. Always explain the invariant regions explicitly.

### 9.11 Practice Problems

- LeetCode 75 — Sort Colors (Medium)
- GeeksforGeeks — Dutch National Flag Problem

---

## 10. Container With Most Water

### 10.1 Problem Statement

> Given `n` non-negative integers `height[i]` representing vertical lines, find two lines that, together with the x-axis, form a container holding the most water.

### 10.2 Intuition

Area = `min(height[left], height[right]) * (right - left)`. Start with the **widest possible container** (both ends), then greedily move the pointer at the **shorter** line inward — because:
- Moving the taller line's pointer can only keep the height the same or worse (bounded by the still-shorter line) while width shrinks — guaranteed no improvement.
- Moving the shorter line's pointer is the *only* move that could possibly find a taller line, compensating for the reduced width.

### 10.3 ASCII Visualization

```
height = [1,8,6,2,5,4,8,3,7]
index:    0 1 2 3 4 5 6 7 8

L=0                       R=8
height[0]=1, height[8]=7 -> area = min(1,7)*8 = 8
1 is shorter -> move L

L=1                       R=8
height[1]=8, height[8]=7 -> area = min(8,7)*7 = 49  <- best so far
7 is shorter -> move R

L=1                    R=7
height[1]=8, height[7]=3 -> area = min(8,3)*6 = 18
3 is shorter -> move R
... continues
```

### 10.4 Python Implementation

```python
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        best = max(best, width * current_height)

        if height[left] < height[right]:
            left += 1          # shorter line is on the left -> move it
        else:
            right -= 1         # shorter (or equal) line is on the right -> move it

    return best
```

### 10.5 Line-by-Line Explanation

- `width`: current container width.
- `current_height`: bounded by the shorter of the two lines (water spills over the shorter side).
- `best = max(best, ...)`: track maximum area seen.
- The `if`/`else`: move the pointer at the **shorter** line — the key greedy insight.

### 10.6 Dry Run

| L | R | height[L] | height[R] | Area | Move |
|---|---|---|---|---|---|
| 0 | 8 | 1 | 7 | 8 | L++ (1<7) |
| 1 | 8 | 8 | 7 | 49 | R-- (7<8) |
| 1 | 7 | 8 | 3 | 18 | R-- |
| 1 | 6 | 8 | 8 | 30 | R-- (equal→ move R) |
| 1 | 5 | 8 | 4 | 16 | R-- |
| 1 | 4 | 8 | 5 | 15 | R-- |
| 1 | 3 | 8 | 2 | 6 | R-- |
| 1 | 2 | 8 | 6 | 6 | R-- ; loop ends |

Max area = **49**.

### 10.7 Complexity

- **Time:** O(n), **Space:** O(1).

### 10.8 Edge Cases

- Fewer than 2 lines → area is 0 (no container possible).
- All same height → area determined purely by width, first and last elements give max.
- Increasing/decreasing monotonic heights → still handled correctly by the greedy rule.

### 10.9 Common Mistakes

- Trying to brute-force check all pairs (O(n²)) — valid but doesn't demonstrate the two-pointer insight expected in interviews.
- Moving **both** pointers simultaneously, which can skip over the true optimal configuration.
- Moving the **taller** line's pointer (inverted logic) — this is provably suboptimal, a classic mistake.

### 10.10 Interview Tips

Be ready to **prove** why moving the shorter pointer is safe — interviewers frequently ask "why does this greedy approach work?" The proof: fixing the shorter side's position and moving the taller side's pointer only decreases or maintains width while height stays capped by the (still) shorter side — so it can never yield a better area than already considered.

### 10.11 Practice Problems

- LeetCode 11 — Container With Most Water (Medium)


---

## 11. Trapping Rain Water

### 11.1 Problem Statement

> Given `n` non-negative integers representing an elevation map, compute how much water it can trap after raining.

### 11.2 Intuition

Water trapped at index `i` = `min(max_left[i], max_right[i]) - height[i]` (if positive). Instead of precomputing `max_left` and `max_right` arrays (O(n) space), use two pointers with **running maxima** from both ends — whichever side has the smaller running max determines how much water can be trapped at that side's pointer, because the smaller max is the actual limiting wall.

### 11.3 ASCII Visualization

```
height = [0,1,0,2,1,0,1,3,2,1,2,1]

L=0 (h=0,maxL=0)              R=11 (h=1,maxR=1)
maxL(0) <= maxR(1) -> process left
  water += maxL - height[L] = 0 - 0 = 0
  maxL = max(maxL, height[L]) = 0
  L++
```

### 11.4 Python Implementation

```python
def trap(height: list[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0
    water = 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= max_left:
                max_left = height[left]        # new wall, no water trapped here
            else:
                water += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                water += max_right - height[right]
            right -= 1

    return water
```

### 11.5 Line-by-Line Explanation

- We compare `height[left]` and `height[right]` to decide which side is currently the "limiting" (shorter) side — that side's water level is safely bounded by its own running max, **regardless of what's beyond the other pointer**, because the other side is guaranteed to have an equal-or-taller wall somewhere.
- `max_left`/`max_right`: running maximum height seen so far from each side.
- If the current height is a new max, no water is trapped there (it's a wall itself); otherwise, water trapped = `running_max - current_height`.

### 11.6 Dry Run

`height = [0,1,0,2,1,0,1,3,2,1,2,1]`

| L | R | h[L] | h[R] | maxL | maxR | Water added | Total |
|---|---|---|---|---|---|---|---|
| 0 | 11 | 0 | 1 | 0 | 0 | 0 (new maxL=0) | 0 |
| 1 | 11 | 1 | 1 | 0→1 | 0 | 0 (new maxL=1) | 0 |
| 2 | 11 | 0 | 1 | 1 | 0→1 | 1 | 1 |
| 3 | 11 | 2 | 1 | 1→2 | 1 | 0 | 1 |
| ... | ... | ... | ... | ... | ... | ... | ... |

(Full dry run continues similarly; final answer for this classic example is **6**.)

### 11.7 Complexity

- **Time:** O(n) single pass, **Space:** O(1) — improvement over the O(n) space DP/prefix-max approach.

### 11.8 Edge Cases

- Empty or single-bar elevation map → 0 water trapped.
- Strictly increasing or strictly decreasing heights → 0 water trapped (no basin).
- All equal heights → 0 water trapped (flat, no walls higher than the surface).

### 11.9 Common Mistakes

- Comparing `max_left` vs `max_right` instead of `height[left]` vs `height[right]` (this is a subtle but critical distinction — the movement decision is based on current heights, while water calculation uses the running max).
- Forgetting `>=` vs `>` when updating running max (using strict `>` still works correctly here, but be consistent and test edge cases like plateaus).

### 11.10 Interview Tips

Explain the **three approaches progression**: (1) brute-force O(n²) checking every index against full left/right scan, (2) O(n) time / O(n) space using precomputed `max_left`/`max_right` arrays, (3) O(n) time / O(1) space two-pointer — interviewers love seeing this optimization narrative.

### 11.11 Practice Problems

- LeetCode 42 — Trapping Rain Water (Hard)

---

## 12. Valid Palindrome

### 12.1 Problem Statement

> Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring case.

### 12.2 Intuition

Opposite-direction pointers with **skip logic**: advance past non-alphanumeric characters before comparing.

### 12.3 ASCII Visualization

```
s = "A man, a plan, a canal: Panama"

L→                              ←R
'A'                              'a'   -> lowercase both, equal, move in
 'man,'                        'canal:' -> skip commas/colons, compare letters only
```

### 12.4 Python Implementation

```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

### 12.5 Line-by-Line Explanation

- Two inner `while` loops skip non-alphanumeric characters from each side, guarded by `left < right` to prevent overshooting.
- Case-insensitive comparison via `.lower()`.
- If mismatch found, return `False` immediately; otherwise converge inward.

### 12.6 Dry Run

`s = "A man, a plan, a canal: Panama"` → after skip logic, effectively compares `"amanaplanacanalpanama"` against itself from both ends — all matches → returns `True`.

### 12.7 Complexity

- **Time:** O(n), **Space:** O(1) (no new string created).

### 12.8 Edge Cases

- Empty string → trivially a palindrome (`True`).
- String with only non-alphanumeric characters (e.g., `",,,"`) → trivially `True` (pointers cross without ever comparing).
- Single character → trivially `True`.
- Mixed case → handled via `.lower()`.

### 12.9 Common Mistakes

- Creating a cleaned/filtered copy of the string first (`O(n)` extra space) instead of skipping in-place — works, but loses the O(1) space benefit, and interviewers often explicitly ask for the O(1) version.
- Forgetting `left < right` guard inside the skip-loops, causing an index-out-of-range or infinite skip when the string is all non-alphanumeric.

### 12.10 Interview Tips

Mention the space-optimized version explicitly, since many candidates default to `s = ''.join(c.lower() for c in s if c.isalnum()); return s == s[::-1])` — that's correct but O(n) space; the two-pointer in-place version demonstrates deeper mastery.

### 12.11 Variations

- Valid Palindrome II (may delete **at most one** character) — requires trying both skip options on mismatch.

```python
def valid_palindrome_ii(s: str) -> bool:
    def is_pal(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1; j -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_pal(left + 1, right) or is_pal(left, right - 1)
        left += 1
        right -= 1
    return True
```

### 12.12 Practice Problems

- LeetCode 125 — Valid Palindrome (Easy)
- LeetCode 680 — Valid Palindrome II (Easy/Medium)


---

## 13. Reverse String / Reverse Words

### 13.1 Reverse String (In-Place)

**Problem:** Reverse a list of characters in-place.

```python
def reverse_string(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

**Dry Run:** `['h','e','l','l','o']` → swap(0,4)→`['o','e','l','l','h']` → swap(1,3)→`['o','l','l','e','h']` → `left(2) < right(2)` false, stop. Result: `['o','l','l','e','h']`.

**Complexity:** O(n) time, O(1) space (true in-place, unlike `s[::-1]` which creates a new string/list).

### 13.2 Reverse Words in a String

**Problem:** Given a string with words separated by spaces, reverse the **order of words** (not each word's characters), collapsing extra whitespace.

**Two-pointer relevant sub-step:** After splitting into words, reversing the word list itself can be done via opposite-direction two pointer swap (same as 13.1, applied to a list of words instead of characters). The full Pythonic solution:

```python
def reverse_words(s: str) -> str:
    words = s.split()          # split() with no args also collapses whitespace
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return " ".join(words)
```

### 13.3 Common Mistakes

- Using `s[::-1]` for character reversal when the problem explicitly requires **O(1) extra space, in-place** modification (slicing creates a new object).
- For reverse words: forgetting to strip/collapse multiple spaces (Python's `str.split()` with no arguments handles this automatically — a key Python-specific tip).

### 13.4 Practice Problems

- LeetCode 344 — Reverse String (Easy)
- LeetCode 151 — Reverse Words in a String (Medium)

---

## 14. Merge Two Sorted Arrays

### 14.1 Problem Statement

> Merge two sorted arrays into one sorted array. A common variant (LeetCode 88): merge `nums2` into `nums1` in-place, where `nums1` has extra trailing space.

### 14.2 Intuition

Classic **same-direction, different-sequence** two pointer — one pointer per array. The in-place variant is trickier: merging from the **front** would overwrite unprocessed values in `nums1`, so we merge **from the back**, using a third pointer for the write position.

### 14.3 ASCII Visualization (merging from the back)

```
nums1 = [1,2,3,0,0,0], m=3
nums2 = [2,5,6],       n=3

i=2 (nums1 last real) j=2 (nums2 last) write=5
nums1[i]=3 < nums2[j]=6 -> write nums2[j] at write, j--, write--

nums1 = [1,2,3,0,0,6]
i=2  j=1  write=4
nums1[i]=3 < nums2[j]=5 -> write 5, j--, write--

nums1 = [1,2,3,0,5,6]
i=2  j=0  write=3
nums1[i]=3 > nums2[j]=2 -> write 3, i--, write--

nums1 = [1,2,3,3,5,6]  (careful: this shows conceptual step; continues until done)
```

### 14.4 Python Implementation

```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j, write = m - 1, n - 1, m + n - 1        # last valid indices, and last write slot

    while j >= 0:                                 # only need to stop once nums2 is exhausted
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1
        write -= 1
```

### 14.5 Line-by-Line Explanation

- `i`, `j`: pointers to the last real elements of `nums1` and `nums2` respectively.
- `write`: pointer to the last index of the combined array — writing from the back avoids overwriting `nums1` values not yet processed.
- Loop condition `while j >= 0`: once `nums2` is exhausted, remaining `nums1` elements are already in their correct sorted position (no need to move them).
- Compares `nums1[i]` and `nums2[j]`; places the larger at `write`, decrementing the source pointer and `write`.

### 14.6 Complexity

- **Time:** O(m+n), **Space:** O(1) (true in-place, exploiting the extra trailing space in `nums1`).

### 14.7 Edge Cases

- `nums2` empty (`n=0`) → loop never executes, `nums1` remains correctly unchanged.
- `nums1`'s real elements empty (`m=0`) → loop copies all of `nums2` directly.
- All elements of `nums2` smaller than all of `nums1` → `j` gets exhausted only after i has been fully deferred; verify with dry run this still works (it does, since `nums1[i] > nums2[j]` will be true repeatedly until i also gets exhausted, but loop condition only checks `j`, which is correctly sufficient).

### 14.8 Common Mistakes

- Merging from the **front** in-place (overwrites `nums1` values before they're read — classic bug).
- Forgetting the loop only needs `j >= 0`, not `i >= 0 and j >= 0` (since remaining `nums1` prefix is already correctly placed if `nums2` runs out first).

### 14.9 Practice Problems

- LeetCode 88 — Merge Sorted Array (Easy)
- LeetCode 21 — Merge Two Sorted Lists (Easy — same two-pointer idea applied to linked lists)

---

## 15. Squares of a Sorted Array

### 15.1 Problem Statement

> Given a sorted array (possibly containing negatives), return a sorted array of the squares of each number.

### 15.2 Intuition

Because of negative numbers, the **largest squares** occur at the **extremes** of the sorted array (most negative or most positive value), not necessarily at one end. Use opposite-direction pointers, filling the **result array from the back** (largest first).

### 15.3 ASCII Visualization

```
nums = [-4,-1,0,3,10]
         L           R
squares:  16          100
100 > 16 -> place 100 at end of result, R--

result = [_,_,_,_,100]
```

### 15.4 Python Implementation

```python
def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    write = n - 1                              # fill from the back (largest values first)

    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        if left_sq > right_sq:
            result[write] = left_sq
            left += 1
        else:
            result[write] = right_sq
            right -= 1
        write -= 1

    return result
```

### 15.5 Dry Run

`nums = [-4,-1,0,3,10]`

| L | R | left_sq | right_sq | Placed | write |
|---|---|---|---|---|---|
| 0 | 4 | 16 | 100 | 100 | 4 |
| 0 | 3 | 16 | 9 | 16 | 3 |
| 1 | 3 | 1 | 9 | 9 | 2 |
| 1 | 2 | 1 | 0 | 1 | 1 |
| 2 | 2 | 0 | 0 | 0 | 0 |

Result: `[0, 1, 9, 16, 100]`

### 15.6 Complexity

- **Time:** O(n), **Space:** O(n) for the output (required, since order changes), O(1) extra beyond output.

### 15.7 Edge Cases

- All non-negative → equivalent to squaring in place, no reordering needed (still handled correctly, general case subsumes it).
- All negative → largest magnitude at index 0, decreasing to the right — pointer logic still applies symmetrically.
- Single element → trivial.

### 15.8 Common Mistakes

- Sorting after squaring with `sorted(x**2 for x in nums)` — correct but O(n log n), missing the O(n) two-pointer optimization interviewers are testing for.
- Writing results from the **front** instead of the **back** (breaks the fill order since we discover largest values first).

### 15.9 Practice Problems

- LeetCode 977 — Squares of a Sorted Array (Easy)


---

## 16. K Closest Elements

### 16.1 Problem Statement

> Given a sorted array `arr`, an integer `k`, and a target `x`, find the `k` closest elements to `x` in the array, sorted in ascending order.

### 16.2 Intuition

Use two pointers as a **shrinking window**: start with the full array as the window `[left, right]`, and repeatedly shrink from whichever side is **farther from `x`**, until the window size equals `k`.

### 16.3 ASCII Visualization

```
arr = [1,2,3,4,5], k=4, x=3
L=0            R=4
window size = 5, need 4 -> compare distances at ends
|arr[L]-x| = 2, |arr[R]-x| = 2  -> tie, remove from right (convention: prefer smaller/left elements on tie)
```

### 16.4 Python Implementation

```python
def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    left, right = 0, len(arr) - 1

    while right - left + 1 > k:                      # shrink window to size k
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        else:
            right -= 1                                # tie goes to keeping the smaller (left) element

    return arr[left:right + 1]
```

### 16.5 Line-by-Line Explanation

- Window `[left, right]` starts as the whole array.
- While window is bigger than `k`, discard the end that's **farther** from `x`.
- On a tie (`abs` equal), we discard the right side — this keeps the smaller value, matching the standard problem convention (favor smaller elements when equally close).

### 16.6 Dry Run

`arr = [1,2,3,4,5], k=4, x=3`

| L | R | size | \|arr[L]-x\| | \|arr[R]-x\| | Action |
|---|---|---|---|---|---|
| 0 | 4 | 5 | 2 | 2 | tie → R-- |
| 0 | 3 | 4 | == k, stop | | |

Result: `arr[0:4] = [1,2,3,4]`.

### 16.7 Complexity

- **Time:** O(n - k) ≈ O(n) shrink steps, **Space:** O(1) extra (O(k) for the output slice).
- (An alternative binary-search approach achieves O(log(n-k) + k) — worth mentioning as an optimization beyond basic two pointer.)

### 16.8 Edge Cases

- `k == len(arr)` → window is already the answer, loop doesn't execute.
- `x` smaller than all elements → pointer shrinks entirely from the right.
- `x` larger than all elements → pointer shrinks entirely from the left.
- Ties in distance → convention matters; clarify with interviewer which side to prefer.

### 16.9 Common Mistakes

- Comparing `x - arr[left]` vs `arr[right] - x` without absolute value (incorrect when `x` could be less than `arr[left]` or greater than `arr[right]`, though technically in this problem `x` may lie inside or outside the array range — always use `abs()` to be safe).
- Off-by-one on the window-size condition (`right - left + 1 > k`, not `right - left > k`).

### 16.10 Interview Tips

Mention the **binary search + two pointer hybrid**: binary search for the optimal starting `left` index directly, avoiding the O(n) linear shrink — a strong follow-up optimization to discuss if asked "can you do better?"

### 16.11 Practice Problems

- LeetCode 658 — Find K Closest Elements (Medium)

---

## 17. Intersection of Two Arrays

### 17.1 Problem Statement

> Given two arrays, return their intersection (each element only once, or with multiplicity depending on variant).

### 17.2 Intuition

If both arrays are **sorted**, use two pointers (one per array) — advance the pointer pointing to the smaller value; when values match, record it and advance both.

### 17.3 Python Implementation

```python
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if not result or result[-1] != nums1[i]:   # dedupe for "Intersection I" (unique output)
                result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return result
```

### 17.4 Dry Run

`nums1=[1,2,2,1], nums2=[2,2]` → sorted: `[1,1,2,2]`, `[2,2]`

| i | j | nums1[i] | nums2[j] | Action |
|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 1<2 → i++ |
| 1 | 0 | 1 | 2 | 1<2 → i++ |
| 2 | 0 | 2 | 2 | match → add 2, i++, j++ |
| 3 | 1 | 2 | 2 | match, but result[-1]==2 already → skip add, i++, j++ |

Result: `[2]`.

### 17.5 Complexity

- **Time:** O(n log n + m log m) due to sorting (or O(n+m) if already sorted), **Space:** O(1) extra (excluding output).
- Alternative: hash set gives O(n+m) without sorting, but O(n+m) extra space — good tradeoff discussion point.

### 17.6 Edge Cases

- No common elements → empty result.
- One array empty → empty result.
- Full duplicates variant ("Intersection II", keep multiplicity) → remove the dedupe check, always append on match.

### 17.7 Common Mistakes

- Forgetting to sort first if arrays aren't guaranteed sorted.
- Confusing "Intersection I" (unique values) with "Intersection II" (with multiplicity/counts) — check problem statement carefully.

### 17.8 Practice Problems

- LeetCode 349 — Intersection of Two Arrays (Easy)
- LeetCode 350 — Intersection of Two Arrays II (Easy)


---

## 18. Fast & Slow Pointer (Floyd's Technique)

### 18.1 Why It Exists

For **linked structures** (or any "functional graph" where each element points to exactly one next element), you cannot use index-based opposite-direction pointers because there's no O(1) random access, and you often don't know the length in advance. Floyd's Fast & Slow technique solves cycle detection and midpoint-finding in **O(1) space**, without needing a hash set of visited nodes.

### 18.2 Intuition / Real-World Analogy

**Race track analogy:** Two runners on a circular track, one running twice as fast as the other. If the track is a loop, the faster runner will eventually **lap** the slower one — they must meet again. If the track is a straight line (no loop), the faster runner simply reaches the end first — no meeting.

### 18.3 ASCII Visualization

```
Linked list with cycle:
1 -> 2 -> 3 -> 4 -> 5
          ^         |
          |_________|

slow moves 1 step, fast moves 2 steps per iteration:

Iter 0: slow=1, fast=1
Iter 1: slow=2, fast=3
Iter 2: slow=3, fast=5
Iter 3: slow=4, fast=4   <- fast wrapped: 5->3->4
Iter 4: slow=5, fast=... eventually slow==fast -> CYCLE DETECTED
```

### 18.4 Why It Works (Mathematical Proof Sketch)

Let the cycle have length `C`, and suppose slow enters the cycle at some point. Once both pointers are in the cycle, the **fast pointer gains 1 net step on the slow pointer every iteration** (since fast moves 2, slow moves 1). Because the cycle is finite, this "gap" (mod C) must eventually become 0 — meaning they meet. This is analogous to two runners on a circular track with different speeds always eventually meeting.

### 18.5 Python Implementation — Cycle Detection

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next            # 1 step
        fast = fast.next.next       # 2 steps

        if slow == fast:            # they met -> cycle exists
            return True

    return False                    # fast reached the end -> no cycle
```

### 18.6 Line-by-Line Explanation

- `slow, fast = head, head`: both start at the same node.
- `while fast and fast.next:`: guards against `None.next` errors — if `fast` or `fast.next` is `None`, there's no cycle (a real end-of-list was reached).
- `slow = slow.next`, `fast = fast.next.next`: the core speed differential.
- `if slow == fast:`: pointer (node identity) equality, not value equality — this is critical, since values could coincidentally match without being the same node.

### 18.7 Finding the Cycle Start (Detect Cycle II)

Once a meeting point is found, **reset one pointer to head** and move both at speed 1 — they will meet exactly at the cycle's starting node. This follows from the mathematical relationship between the distance to the cycle start and the meeting point.

```python
def detect_cycle_start(head: ListNode):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None                 # no cycle

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow                     # the node where the cycle begins
```

### 18.8 Complexity

- **Time:** O(n), **Space:** O(1) — this is the entire point versus a hash-set-based visited-node approach, which is O(n) space.

### 18.9 Edge Cases

- Empty list (`head is None`) → no cycle, loop doesn't execute.
- Single node pointing to itself → cycle of length 1, detected correctly.
- No cycle, list of any length → fast pointer reaches `None`, loop exits cleanly.

### 18.10 Common Mistakes

- Comparing `slow.val == fast.val` instead of `slow is fast` / `slow == fast` (node identity) — values can repeat without indicating a cycle.
- Forgetting the `fast.next` check in the while condition (causes `AttributeError: 'NoneType' object has no attribute 'next'`).
- Off-by-one in the cycle-start-finding phase (must reset `slow` to `head`, not `fast`).

### 18.11 Interview Tips

Always explicitly state the alternative (hash set of visited nodes, O(n) space) first, then present Floyd's as the **space-optimized** solution — this framing shows you understand the tradeoff, not just memorized the trick.

### 18.12 Practice Problems

- LeetCode 141 — Linked List Cycle (Easy)
- LeetCode 142 — Linked List Cycle II (Medium)

---

## 19. Middle of Linked List

### 19.1 Problem Statement

> Find the middle node of a singly linked list in one pass.

### 19.2 Intuition

By the time `fast` reaches the end (moving 2 steps per iteration), `slow` (moving 1 step) will be exactly at the midpoint — no need to first count the length and then traverse again.

### 19.3 Python Implementation

```python
def middle_node(head: ListNode) -> ListNode:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow                     # for even-length lists, this is the SECOND middle node
```

### 19.4 Dry Run

`1 -> 2 -> 3 -> 4 -> 5`

| Iter | slow | fast |
|---|---|---|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |

`fast.next` is `None` → stop. `slow = 3` (the true middle of 5 elements).

For an even-length list `1->2->3->4`: iter1: slow=2,fast=3; iter2: slow=3,fast=None(fast.next check fails after fast=3.next=4, fast.next=None) — result is node `3`, the **second** middle (0-indexed: [1,2,3,4] middle candidates are 2 and 3; this implementation returns the second one, per LeetCode's convention).

### 19.5 Complexity

- **Time:** O(n), **Space:** O(1) — versus the two-pass alternative (count length, then traverse to `n//2`), which is also O(n) time but requires two full traversals.

### 19.6 Edge Cases

- Single node → returns that node.
- Empty list → returns `None` (since `head` is `None`, loop doesn't execute, `slow` stays `None`).
- Even-length list → returns the second of the two middle nodes (verify against exact problem convention).

### 19.7 Common Mistakes

- Assuming this returns the **first** middle node for even-length lists without checking the exact problem specification.
- Forgetting the `fast and fast.next` guard, causing a crash on odd/even length edge cases.

### 19.8 Practice Problems

- LeetCode 876 — Middle of the Linked List (Easy)

---

## 20. Happy Number

### 20.1 Problem Statement

> A number is "happy" if repeatedly replacing it with the sum of the squares of its digits eventually reaches 1. Otherwise it loops endlessly in a cycle. Determine if a number is happy.

### 20.2 Intuition

This is **not a linked list**, but the sequence of "next number" transformations forms an implicit **functional graph** — exactly the structure Floyd's Fast & Slow technique was designed for. If the number is not happy, it will enter a cycle (provably, since the sum-of-squared-digits function has a bounded range for multi-digit numbers, guaranteeing eventual repetition).

### 20.3 Python Implementation

```python
def is_happy(n: int) -> bool:
    def next_number(x: int) -> int:
        total = 0
        while x > 0:
            digit = x % 10
            total += digit * digit
            x //= 10
        return total

    slow, fast = n, next_number(n)

    while fast != 1 and slow != fast:
        slow = next_number(slow)
        fast = next_number(next_number(fast))

    return fast == 1
```

### 20.4 Line-by-Line Explanation

- `next_number`: computes the sum of squares of digits — the "transition function" of our implicit graph.
- `slow` starts at `n`, `fast` starts one step ahead — mirrors the linked-list version's `slow=head, fast=head` followed by the loop's first double-step, just pre-computed here for clarity.
- Loop continues while `fast` hasn't reached `1` (happy) and `slow`/`fast` haven't collided (cycle, unhappy).
- Return `True` only if we exited because `fast == 1`.

### 20.5 Dry Run

`n = 19`: 1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1 → happy.
`n = 2`: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 (cycle repeats) → not happy, detected via slow==fast collision.

### 20.6 Complexity

- **Time:** O(log n) per `next_number` call (number of digits), and the cycle length for non-happy numbers is bounded by a small constant (empirically small for this specific function) — overall considered O(log n) amortized for practical purposes.
- **Space:** O(1) — versus a hash-set-based "seen" approach which is O(k) space for k values seen before a cycle/termination.

### 20.7 Edge Cases

- `n = 1` → immediately happy (loop doesn't even execute since `fast` starts at `next_number(1) = 1`).
- Single-digit numbers → still handled correctly by the general digit-sum logic.

### 20.8 Common Mistakes

- Using a hash set (`seen = set()`) is a valid and common solution too — but doesn't demonstrate O(1) space; mention Floyd's as the space-optimized alternative in interviews.
- Off-by-one in initializing `fast` (some implementations start `fast = n` too and do the double-step check inside the loop symmetrically — both are valid, just be consistent).

### 20.9 Interview Tips

This problem is a great test of **pattern transfer**: recognizing that "detect a cycle in a sequence generated by repeatedly applying a function" is the *same* abstract problem as "detect a cycle in a linked list," even though there's no explicit `Node` class here.

### 20.10 Practice Problems

- LeetCode 202 — Happy Number (Easy)


---

## 21. Two Pointer vs Sliding Window

### 21.1 The Core Confusion

Many learners conflate these two patterns because both use pointer indices moving through an array. Here's the precise distinction:

| Aspect | Two Pointer | Sliding Window |
|---|---|---|
| Core idea | Two independent indices with a relationship-based movement rule | A contiguous **range/subarray** `[left, right]` that expands/shrinks |
| Typical direction | Opposite (converging) OR same-direction, single pass each | Same direction only — `right` expands, `left` shrinks to maintain a constraint |
| State tracked | Usually just the two index values | Often a running aggregate over the window (sum, count, frequency map) |
| Precondition | Often needs sorted data or linked/cyclic structure | Works on unsorted data; needs a "monotonic feasibility" property (window constraint gets easier/harder monotonically as it grows/shrinks) |
| Typical problems | Pair sum, palindrome, container with water, cycle detection | Longest substring without repeats, max sum subarray of size k, minimum window substring |

### 21.2 Visualization: Two Pointer (Converging) vs Sliding Window (Expanding)

```
TWO POINTER (opposite direction):
[1, 3, 5, 7, 9, 11]
 L                R      -> both move INWARD, converging, array typically sorted

SLIDING WINDOW:
[a, b, c, d, e, f, g]
 L  R                    -> window starts small
 L     R                 -> right expands
    L  R                 -> left shrinks (window boundary moves, doesn't cross)
```

### 21.3 Key Conceptual Difference

- **Two Pointer** is about **two points relating to each other** (their combined value, their distance, their equality) — the region *between* them isn't necessarily tracked as a coherent "window" with an aggregate.
- **Sliding Window** is about a **contiguous range** whose *aggregate property* (sum, count of distinct chars, etc.) is maintained incrementally as the window's boundaries move — almost always **same-direction only** (never converging).

> **Important nuance:** Sliding Window is technically a **specialized subtype of "same-direction two pointer"** — every sliding window uses two pointers, but not every two-pointer problem is a sliding window. The distinguishing feature is whether you maintain a **windowed aggregate/invariant** (sliding window) versus a **direct pointer-value relationship** (general two pointer, e.g., pair sum).

### 21.4 Decision Tree: Which Pattern To Use?

```
Is the data sorted (or can be sorted without breaking the requirement)?
│
├── YES → Do you need a PAIR/TRIPLE with a target relationship (sum, product)?
│         ├── YES → Two Pointer (Opposite Direction)
│         └── NO  → Do you need in-place partition/dedup?
│                   ├── YES → Two Pointer (Same Direction, read/write)
│                   └── NO  → reconsider problem
│
└── NO (unsorted, but contiguous subarray/substring matters)
          │
          └── Does the problem ask for a CONTIGUOUS subarray/substring satisfying
              a constraint (sum ≤ k, at most k distinct chars, longest without repeat)?
              ├── YES → Sliding Window
              └── NO  → Consider Fast & Slow (if linked/cyclic structure) or other techniques
```

### 21.5 Recognition Keywords

| Keyword / Phrase | Likely Pattern |
|---|---|
| "sorted array", "pair sum", "triplet sum" | Two Pointer (opposite direction) |
| "in-place", "remove duplicates", "partition" | Two Pointer (same direction) |
| "cycle", "linked list", "repeated sequence" | Fast & Slow Pointer |
| "longest substring", "smallest window", "at most K distinct" | Sliding Window |
| "contiguous subarray with sum" | Sliding Window (if all positive) or prefix-sum+hashmap (if negatives allowed) |
| "palindrome" (checking) | Two Pointer (opposite, converging) |
| "palindrome" (finding substrings) | Two Pointer (diverging, expand-around-center) |

### 21.6 Similarities

- Both use O(1) extra pointer/index variables (not counting any aggregate state).
- Both typically achieve O(n) time from an O(n²) brute force.
- Both rely on **avoiding redundant re-examination** of already-processed elements.

### 21.7 Differences Summary

- Two Pointer often **requires sorted input**; Sliding Window usually does **not**.
- Two Pointer pointers can **converge** (move toward each other); Sliding Window pointers **only expand rightward and shrink leftward** — never cross or reverse roles.
- Two Pointer typically answers "does a pair/triple exist / partition the array"; Sliding Window typically answers "what is the best/longest/shortest contiguous range."


---

## 22. Problem Recognition Framework

### 22.1 The General Recognition Flowchart

```
START: Read the problem carefully.
│
├── Does it involve an ARRAY/STRING/LINKED LIST?
│   │
│   ├── LINKED LIST + "cycle" / "middle" / "nth from end" / "intersection of two lists"
│   │        → Fast & Slow Pointer (or opposite-ended pointers for "nth from end" on arrays)
│   │
│   ├── ARRAY/STRING is SORTED (or sortable without losing needed info)
│   │        │
│   │        ├── Need PAIR/TRIPLET/QUADRUPLET matching a target (sum/product/difference)?
│   │        │        → Opposite-Direction Two Pointer (nest for 3Sum/4Sum)
│   │        │
│   │        ├── Need to CHECK SYMMETRY (palindrome) or MAXIMIZE a geometric quantity
│   │        │   bounded by two ends (container, rainwater)?
│   │        │        → Opposite-Direction Two Pointer
│   │        │
│   │        └── Need IN-PLACE MODIFICATION (dedupe, partition, move elements)?
│   │                 → Same-Direction (Read/Write) Two Pointer
│   │
│   └── ARRAY/STRING is UNSORTED
│            │
│            ├── Need a CONTIGUOUS subarray/substring satisfying a running constraint?
│            │        → Sliding Window (same-direction two pointer with an aggregate)
│            │
│            ├── Need EXACT pair with target, output must reference ORIGINAL indices,
│            │   and sorting would destroy index mapping?
│            │        → Hash Map (NOT two pointer) — unless you carry (value, original_index)
│            │          tuples through the sort
│            │
│            └── Need to compare TWO SEPARATE sequences (merge, subsequence check)?
│                     → Two Pointer (one pointer per sequence, same or opposite direction
│                       depending on whether both are traversed forward)
│
└── Does it involve a MATHEMATICAL SEQUENCE generated by repeatedly applying a function
    (e.g., digit-sum transforms, pseudo-random generators)?
             → Fast & Slow Pointer (treat it as an implicit linked structure)
```

### 22.2 Interview Clues (What Interviewers Say That Hints at Two Pointer)

- "The array is sorted..." → strong signal for opposite-direction two pointer.
- "...in-place, O(1) extra space..." → strong signal for same-direction two pointer.
- "...without using extra space for cycle detection..." → Fast & Slow.
- "...find all pairs/triplets..." → opposite-direction, nested for k>2.
- "Can you do it in one pass?" → usually two pointer or sliding window (as opposed to a naive two-pass or O(n²) approach).

### 22.3 Pattern Identification Checklist

Ask yourself, in order:
1. Is the data linear (array/string/linked list)? — Two pointer needs linear structure.
2. Is there a **monotonic property** I can exploit (sorted order, or a window constraint that grows/shrinks predictably)?
3. Do I need **O(1) extra space**? If yes, and brute force uses nested loops, two pointer is a strong candidate.
4. Does the structure have a possible **cycle** or is generated by repeated function application? → Fast & Slow.
5. Am I comparing/merging **two distinct sequences**? → dual-pointer merge style.

### 22.4 Pointer Direction Selection Guide

| Signal in Problem | Direction to Choose |
|---|---|
| Sorted array, need target relationship between 2 elements | Opposite direction |
| Need to keep relative order while filtering/compacting | Same direction (read/write) |
| Symmetric check (palindrome) | Opposite direction |
| Expanding from a center point (palindromic substrings) | Diverging (from center outward) |
| Traversing a possibly-cyclic linked structure | Fast & Slow |
| Merging two already-sorted sequences | Same-direction, one pointer per sequence |


---

## 23. Optimization Journeys: Brute Force → Two Pointer

### 23.1 Two Sum (Sorted) — Optimization Path

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute Force (nested loops) | O(n²) | O(1) | Check every pair |
| Hash Map | O(n) | O(n) | Works even if unsorted, but uses extra space |
| Two Pointer (sorted) | O(n) | O(1) | Best if array is sorted or sortable without losing needed info |

### 23.2 Three Sum — Optimization Path

| Approach | Time | Space |
|---|---|---|
| Brute Force (3 nested loops) | O(n³) | O(1) |
| Hash Set per fixed pair | O(n²) | O(n) |
| Sort + Two Pointer (fix one, 2-pointer on rest) | O(n²) | O(1) extra |

### 23.3 Cycle Detection — Optimization Path

| Approach | Time | Space |
|---|---|---|
| Hash Set of visited nodes | O(n) | O(n) |
| Floyd's Fast & Slow | O(n) | O(1) |

### 23.4 General Space Optimization Principle

Whenever brute force or a hash-based approach already achieves optimal **time** complexity, the two-pointer refinement's main contribution is usually **space** — from O(n) auxiliary structures down to O(1). Always mention this explicitly in interviews: "this doesn't improve the time complexity over the hash-map version, but it removes the O(n) space requirement."

### 23.5 General Time Optimization Principle

Whenever brute force uses nested loops re-scanning ranges that a single monotonic pass could cover, two pointer collapses O(n²)/O(n³) into O(n)/O(n²) by **eliminating redundant re-comparisons** — every element is "visited" a small constant number of times total across both pointers, rather than being compared against every other element individually.

### 23.6 Reducing Nested Loops — General Recipe

1. Identify the brute-force nested loop structure (e.g., `for i: for j: ...`).
2. Ask: "Does fixing `i` and moving `j` monotonically (in one direction only) still cover all necessary comparisons, given some structural property (sortedness)?"
3. If yes, replace the inner loop with a pointer that **never resets** — it only ever moves forward (or converges), giving amortized O(n) across all outer iterations instead of O(n) *per* outer iteration.

### 23.7 Choosing the Correct Pointer Strategy — Quick Reference

- **Need a target sum/relationship between exactly 2 elements, sorted data** → Opposite direction.
- **Need to filter/compact/partition in place** → Same direction (read/write).
- **Need to detect a cycle or find a structural midpoint** → Fast & Slow.
- **Need to merge or compare two separate sorted sequences** → Dual-pointer merge (same direction, one pointer per sequence).


---

## 24. Interview Preparation Guide

### 24.1 Standard Templates to Memorize

**Template 1 — Opposite Direction (Pair Sum style)**
```python
def opposite_direction_template(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]      # or any relationship
        if current == target:
            # process match
            left += 1
            right -= 1
        elif current < target:
            left += 1
        else:
            right -= 1
```

**Template 2 — Same Direction (Read/Write)**
```python
def same_direction_template(arr, condition):
    slow = 0
    for fast in range(len(arr)):
        if condition(arr[fast]):
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    return slow
```

**Template 3 — Fast & Slow**
```python
def fast_slow_template(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True   # cycle / meeting condition
    return False
```

**Template 4 — Diverging (Expand Around Center)**
```python
def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]   # the palindrome found
```

**Template 5 — Merge (Dual Sequence)**
```python
def merge_template(a, b):
    i, j, merged = 0, 0, []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged
```

### 24.2 Difficulty Tiers

| Tier | Problems |
|---|---|
| Easy | Two Sum II, Valid Palindrome, Remove Duplicates, Move Zeroes, Reverse String, Middle of Linked List, Linked List Cycle, Happy Number, Squares of Sorted Array |
| Medium | 3Sum, 3Sum Closest, Container With Most Water, Sort Colors, Linked List Cycle II, Find K Closest Elements, Reverse Words in a String, 4Sum |
| Hard | Trapping Rain Water, Minimum Window Substring (sliding window, contrast case), Median of Two Sorted Arrays (related but binary-search-based) |

### 24.3 Pattern-Wise Question Groupings

- **Opposite Direction:** Two Sum II, 3Sum, 4Sum, Container With Most Water, Trapping Rain Water, Valid Palindrome, Squares of Sorted Array.
- **Same Direction (Read/Write):** Remove Duplicates I/II, Move Zeroes, Remove Element, Sort Colors (3-pointer variant).
- **Fast & Slow:** Linked List Cycle I/II, Middle of Linked List, Happy Number, Find the Duplicate Number (array-as-implicit-linked-list variant).
- **Merge/Dual Sequence:** Merge Sorted Array, Merge Two Sorted Lists, Intersection of Two Arrays.

### 24.4 Company-Wise Tendency (General Patterns Observed in Interview Prep Communities)

> Note: exact company question sets change over time and are not something to treat as guaranteed — always check current interview-prep aggregators for the latest reported questions. As **general tendencies** reported across prep communities:
- **Amazon/Meta/Google:** frequently ask 3Sum, Container With Most Water, Trapping Rain Water, Linked List Cycle variants.
- **Microsoft:** frequently ask Merge Sorted Array, Valid Palindrome, Remove Duplicates.
- **Bloomberg/Two Sigma (finance-adjacent):** frequently ask Two Sum variants and array partitioning problems.

### 24.5 Blind 75 / NeetCode 150 — Two Pointer Subset

Problems commonly categorized under "Two Pointers" in the Blind 75 / NeetCode 150 lists include: Two Sum II, 3Sum, Container With Most Water, Trapping Rain Water, Valid Palindrome. Under "Fast & Slow" / Linked List sections: Linked List Cycle, Middle of Linked List, Reorder List, Remove Nth Node From End of List.

### 24.6 Frequently Asked Interview Questions (Conceptual)

- "Why does the two-pointer approach require sorted data for pair-sum problems?"
- "Explain why moving the shorter line's pointer is always safe in Container With Most Water."
- "Why doesn't incrementing `mid` after a swap-with-`high` work in Dutch National Flag?"
- "Prove that Floyd's Fast & Slow pointer must eventually meet if there's a cycle."
- "What's the difference between Two Pointer and Sliding Window?"

### 24.7 Interview Tricks

- Always state the **brute-force approach first**, then explain the **structural property** (sortedness, cyclicity) that enables the two-pointer optimization — this shows structured thinking, not memorization.
- When stuck, ask: "Is there a way to avoid re-scanning elements I've already ruled out?" — this question alone often reveals the two-pointer insight.
- Practice **explaining pointer movement out loud** — interviewers weight communication heavily for this pattern since the logic can look "magic" without a clear invariant explanation.

### 24.8 Standard Interview Answer Structure

1. Clarify: sorted or not? In-place required? Space constraints?
2. State brute force + complexity.
3. Identify the exploitable structural property.
4. Propose two-pointer approach + complexity improvement.
5. Code it cleanly with meaningful variable names.
6. Dry-run on a small example out loud.
7. State edge cases handled.
8. Discuss variations/follow-ups proactively.


---

## 25. Python-Specific Tips & Idioms

### 25.1 enumerate() Recap
```python
for index, value in enumerate(arr):
    ...
```
Use when you need both index and value while one pointer is naturally the loop variable.

### 25.2 zip() Recap
```python
for a_val, b_val in zip(list_a, list_b):
    ...
```
Great for **lock-step, equal-length** parallel traversal (e.g., comparing two strings char by char) — but cannot express conditional differential movement (one pointer advancing without the other), so it's not suitable for merge-style dual-pointer logic where advancement is conditional.

### 25.3 reversed()
```python
for ch in reversed(s):
    ...
```
Useful for simple backward iteration without needing an explicit index; combine with `enumerate(reversed(s))` cautiously (indices will be from the reversed sequence, not the original — a common source of bugs).

### 25.4 Slicing
```python
arr[left:right+1]
```
Creates a **new list/string** — O(k) time/space where k is slice length. Fine for final result construction; avoid inside hot per-iteration loops.

### 25.5 Tuple Swap
```python
a, b = b, a
arr[i], arr[j] = arr[j], arr[i]
```
Idiomatic and safe — evaluates the right-hand side fully before assignment, so no temp variable needed.

### 25.6 Walrus Operator (Python 3.8+) in Pointer Loops
```python
while (current_sum := nums[left] + nums[right]) < target:
    left += 1
```
Can make code more compact, but use sparingly — clarity matters more than cleverness in interviews.

### 25.7 String Immutability Gotcha

Python strings are **immutable** — `s[left], s[right] = s[right], s[left]` does **NOT** work on a `str`. To reverse a string in-place two-pointer style, you must first convert to a `list`:
```python
s = list(s)
left, right = 0, len(s) - 1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
s = ''.join(s)
```

### 25.8 Performance Tips

- Avoid repeated `len()` calls inside loop conditions if the container isn't a plain `list`/`str` (for these, `len()` is O(1), so it's a non-issue in Python specifically, but a good habit for other languages/data types).
- Avoid list slicing inside the pointer loop body — do it once at the end if you need a sub-list result.
- For very large competitive-programming inputs, prefer `sys.stdin.readline` and avoid Python-level function call overhead in the hottest loops (consider inlining simple logic).

### 25.9 Memory Optimization

- Prefer in-place swaps (`arr[i], arr[j] = arr[j], arr[i]`) over creating new lists when the problem requires O(1) space.
- Use generators (`(x for x in ...)`) instead of list comprehensions when you don't need to keep the whole sequence in memory (e.g., summing without storing).

### 25.10 Common Python Pitfalls in Two-Pointer Code

- Forgetting strings are immutable (see 25.7).
- Off-by-one from Python's `range()` being exclusive of the stop value.
- Mutating a list while iterating over it directly with a `for x in list` loop (always iterate by index or use `enumerate` for two-pointer-style same-direction scans that mutate the list).
- Confusing `is` (identity) vs `==` (equality) when comparing linked list nodes — for cycle detection, comparing node objects with `==` typically works if `__eq__` isn't overridden (defaults to identity), but be explicit and prefer clarity.


---

## 26. Common Mistakes Catalog

### 26.1 Wrong Pointer Movement

```python
# WRONG: moving the wrong pointer when sum is too small
if current_sum < target:
    right -= 1     # BUG: this makes the sum even smaller!
```
**Fix:** When sum is too small, move `left` **up** (increase value); when too large, move `right` **down** (decrease value).

### 26.2 Infinite Loops

```python
# WRONG: forgetting to update a pointer in some branch
while left < right:
    if arr[left] == arr[right]:
        pass  # BUG: neither pointer moves -> infinite loop
```
**Fix:** Every branch of the loop body must guarantee **at least one pointer** advances.

### 26.3 Missing Duplicate Handling (3Sum/4Sum)

```python
# WRONG: no duplicate skip after finding a match
if current_sum == target:
    result.append([...])
    left += 1
    right -= 1
    # missing: while left < right and nums[left]==nums[left-1]: left += 1
```
**Fix:** Always skip past duplicate values after recording a match, on both sides.

### 26.4 Wrong Stopping Condition

```python
# WRONG: using <= when pointers should never meet (would double count same index)
while left <= right:   # BUG for pair-sum where i != j is required
```
**Fix:** Use `left < right` for problems needing two **distinct** indices; use `left <= right` only when the pointers meeting at the same index is a valid/expected terminal state (e.g., binary search).

### 26.5 Incorrect Boundary Checks

```python
# WRONG: accessing fast.next.next without checking fast.next first
while fast:
    fast = fast.next.next   # BUG: crashes if fast.next is None
```
**Fix:** Always guard with `while fast and fast.next:`.

### 26.6 Pointer Initialization Errors

```python
# WRONG: starting right at len(arr) instead of len(arr) - 1
left, right = 0, len(arr)   # BUG: off-by-one, will index out of range
```
**Fix:** `right = len(arr) - 1` for 0-indexed arrays.

### 26.7 Off-By-One Errors

```python
# WRONG: window size check
while right - left > k:      # BUG: should be right - left + 1 > k for inclusive window
```
**Fix:** Always double-check whether your window/range is inclusive or exclusive at each end, and adjust the arithmetic accordingly.

### 26.8 Mistake Frequency Table (For Quick Self-Review)

| Mistake | Symptom | Fix Strategy |
|---|---|---|
| Wrong direction moved | Wrong answer, sometimes still terminates | Re-derive the monotonicity argument before coding |
| No pointer advances in some branch | Infinite loop / timeout | Ensure every branch advances ≥1 pointer |
| Missing duplicate skip | Duplicate results in output | Add explicit skip-while after each match |
| Wrong `<=` vs `<` | Off-by-one, wrong answer, or infinite loop | Match condition to problem's index-distinctness requirement |
| Missing `fast.next` guard | Crash (`AttributeError`) | Always check both `fast` and `fast.next` |
| `right = len(arr)` instead of `len(arr)-1` | `IndexError` | Always `-1` for 0-indexed last valid index |
| Inclusive/exclusive window confusion | Off-by-one in window size checks | Write out window size formula explicitly: `right - left + 1` |


---

## 27. Cheat Sheets

### 27.1 Two Pointer Templates Cheat Sheet

| Pattern | Template Skeleton |
|---|---|
| Opposite Direction | `left, right = 0, n-1; while left < right: ... adjust left or right` |
| Same Direction (Read/Write) | `slow = 0; for fast in range(n): if cond: swap/copy; slow += 1` |
| Fast & Slow | `slow, fast = head, head; while fast and fast.next: slow=slow.next; fast=fast.next.next` |
| Diverging (Expand Center) | `while left >= 0 and right < n and match: left -= 1; right += 1` |
| Dual Sequence Merge | `i, j = 0, 0; while i < len(a) and j < len(b): compare and advance one or both` |

### 27.2 Pattern Recognition Cheat Sheet

| If you see... | Think... |
|---|---|
| "sorted array" + "pair/triplet sum" | Opposite Direction Two Pointer |
| "in-place" + "O(1) space" + "remove/partition" | Same Direction Two Pointer |
| "linked list" + "cycle"/"middle"/"nth from end" | Fast & Slow Pointer |
| "palindromic substring" (find, not check) | Diverging / Expand Around Center |
| "merge two sorted" | Dual Sequence Merge |
| "longest/shortest contiguous subarray/substring" | Sliding Window |

### 27.3 Complexity Table

| Problem | Brute Force | Two Pointer |
|---|---|---|
| Two Sum (sorted) | O(n²) | O(n) |
| 3Sum | O(n³) | O(n²) |
| 4Sum | O(n⁴) | O(n³) |
| Remove Duplicates | O(n²) (shifting) | O(n) |
| Container With Most Water | O(n²) | O(n) |
| Trapping Rain Water | O(n²) or O(n) w/ O(n) space | O(n) w/ O(1) space |
| Cycle Detection | O(n) w/ O(n) space (hash set) | O(n) w/ O(1) space |
| Merge Sorted Arrays | O((m+n)log(m+n)) (concat+sort) | O(m+n) |

### 27.4 Pointer Movement Rules Cheat Sheet

- Sum too small → move **left** pointer **right** (increase value).
- Sum too large → move **right** pointer **left** (decrease value).
- Match found (pair/triplet) → move **both** pointers inward, skip duplicates.
- Container/water problems → move the pointer at the **shorter/limiting** side.
- Fast & Slow → `slow` always +1 step, `fast` always +2 steps, per iteration.
- Same-direction read/write → `fast` scans unconditionally each iteration; `slow` only advances when the "keep" condition is met.

### 27.5 Python Syntax Cheat Sheet

```python
left, right = 0, len(arr) - 1          # opposite direction init
slow, fast = head, head                 # fast/slow init
arr[i], arr[j] = arr[j], arr[i]         # swap
s = list(s); ''.join(s)                 # string <-> list for in-place ops
while left < right: ...                 # standard converging loop
while fast and fast.next: ...           # standard fast/slow guard
```

### 27.6 Master Decision Tree (Condensed)

```
Sorted + pair/triplet target        -> Opposite Direction
Unsorted + in-place filter/compact  -> Same Direction (Read/Write)
Linked/cyclic structure             -> Fast & Slow
Merging two sorted sequences        -> Dual Sequence Merge
Contiguous range + running property -> Sliding Window (NOT plain two pointer)
Symmetric check                     -> Opposite Direction
Symmetric search (find substrings)  -> Diverging / Expand Around Center
```


---

## 28. Practice Problem Bank

### 28.1 Basics

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Two Sum II - Input Array Is Sorted | LeetCode | Easy | Opposite Direction | leetcode.com/problems/two-sum-ii-input-array-is-sorted |
| Reverse String | LeetCode | Easy | Opposite Direction | leetcode.com/problems/reverse-string |
| Squares of a Sorted Array | LeetCode | Easy | Opposite Direction | leetcode.com/problems/squares-of-a-sorted-array |
| Move Zeroes | LeetCode | Easy | Same Direction | leetcode.com/problems/move-zeroes |
| Remove Element | LeetCode | Easy | Same Direction | leetcode.com/problems/remove-element |

### 28.2 Opposite Direction

| Problem | Platform | Difficulty | Concept | Link |
|---|---|---|---|---|
| Valid Palindrome | LeetCode | Easy | Palindrome check | leetcode.com/problems/valid-palindrome |
| Container With Most Water | LeetCode | Medium | Max area | leetcode.com/problems/container-with-most-water |
| Sort Colors | LeetCode | Medium | 3-pointer partition | leetcode.com/problems/sort-colors |
| Two Sum - Pair with Given Sum | GeeksforGeeks | Easy | Pair sum | geeksforgeeks.org |

### 28.3 Same Direction

| Problem | Platform | Difficulty | Concept | Link |
|---|---|---|---|---|
| Remove Duplicates from Sorted Array | LeetCode | Easy | Dedup | leetcode.com/problems/remove-duplicates-from-sorted-array |
| Remove Duplicates from Sorted Array II | LeetCode | Medium | Dedup (keep k) | leetcode.com/problems/remove-duplicates-from-sorted-array-ii |
| Sort Array By Parity | LeetCode | Easy | Partition | leetcode.com/problems/sort-array-by-parity |

### 28.4 Fast & Slow Pointer

| Problem | Platform | Difficulty | Concept | Link |
|---|---|---|---|---|
| Linked List Cycle | LeetCode | Easy | Cycle detection | leetcode.com/problems/linked-list-cycle |
| Linked List Cycle II | LeetCode | Medium | Cycle start | leetcode.com/problems/linked-list-cycle-ii |
| Middle of the Linked List | LeetCode | Easy | Midpoint | leetcode.com/problems/middle-of-the-linked-list |
| Happy Number | LeetCode | Easy | Implicit cycle | leetcode.com/problems/happy-number |
| Find the Duplicate Number | LeetCode | Medium | Array-as-linked-list cycle | leetcode.com/problems/find-the-duplicate-number |
| Palindrome Linked List | LeetCode | Easy | Middle + reverse | leetcode.com/problems/palindrome-linked-list |

### 28.5 Pair Sum

| Problem | Platform | Difficulty | Link |
|---|---|---|---|
| Two Sum | LeetCode | Easy | leetcode.com/problems/two-sum |
| Two Sum II | LeetCode | Easy | leetcode.com/problems/two-sum-ii-input-array-is-sorted |
| Two Sum IV - Input is a BST | LeetCode | Easy | leetcode.com/problems/two-sum-iv-input-is-a-bst |

### 28.6 Three Sum

| Problem | Platform | Difficulty | Link |
|---|---|---|---|
| 3Sum | LeetCode | Medium | leetcode.com/problems/3sum |
| 3Sum Closest | LeetCode | Medium | leetcode.com/problems/3sum-closest |
| 3Sum Smaller | LeetCode | Medium | leetcode.com/problems/3sum-smaller |
| 3Sum With Multiplicity | LeetCode | Medium | leetcode.com/problems/3sum-with-multiplicity |

### 28.7 Four Sum

| Problem | Platform | Difficulty | Link |
|---|---|---|---|
| 4Sum | LeetCode | Medium | leetcode.com/problems/4sum |
| 4Sum II | LeetCode | Medium | leetcode.com/problems/4sum-ii |

### 28.8 Partitioning

| Problem | Platform | Difficulty | Link |
|---|---|---|---|
| Sort Colors | LeetCode | Medium | leetcode.com/problems/sort-colors |
| Partition Array According to Given Pivot | LeetCode | Medium | leetcode.com/problems/partition-array-according-to-given-pivot |
| Sort Array By Parity II | LeetCode | Easy | leetcode.com/problems/sort-array-by-parity-ii |

### 28.9 Merge Problems

| Problem | Platform | Difficulty | Link |
|---|---|---|---|
| Merge Sorted Array | LeetCode | Easy | leetcode.com/problems/merge-sorted-array |
| Merge Two Sorted Lists | LeetCode | Easy | leetcode.com/problems/merge-two-sorted-lists |
| Interval List Intersections | LeetCode | Medium | leetcode.com/problems/interval-list-intersections |

### 28.10 Palindrome

| Problem | Platform | Difficulty | Link |
|---|---|---|---|
| Valid Palindrome | LeetCode | Easy | leetcode.com/problems/valid-palindrome |
| Valid Palindrome II | LeetCode | Easy/Medium | leetcode.com/problems/valid-palindrome-ii |
| Longest Palindromic Substring | LeetCode | Medium | leetcode.com/problems/longest-palindromic-substring |
| Palindromic Substrings | LeetCode | Medium | leetcode.com/problems/palindromic-substrings |

### 28.11 Cycle Detection

| Problem | Platform | Difficulty | Link |
|---|---|---|---|
| Linked List Cycle | LeetCode | Easy | leetcode.com/problems/linked-list-cycle |
| Linked List Cycle II | LeetCode | Medium | leetcode.com/problems/linked-list-cycle-ii |
| Circular Array Loop | LeetCode | Medium | leetcode.com/problems/circular-array-loop |

### 28.12 Advanced Two Pointer

| Problem | Platform | Difficulty | Link |
|---|---|---|---|
| Trapping Rain Water | LeetCode | Hard | leetcode.com/problems/trapping-rain-water |
| Trapping Rain Water II | LeetCode | Hard | leetcode.com/problems/trapping-rain-water-ii |
| Minimum Window Substring | LeetCode | Hard | leetcode.com/problems/minimum-window-substring (sliding window, good contrast case) |
| Median of Two Sorted Arrays | LeetCode | Hard | leetcode.com/problems/median-of-two-sorted-arrays (binary search, related concept) |

### 28.13 Cross-Platform Practice

| Problem | Platform | Difficulty |
|---|---|---|
| Pair Sum in Sorted Array | GeeksforGeeks | Easy |
| Dutch National Flag Algorithm | GeeksforGeeks | Medium |
| Three Sum | InterviewBit | Medium |
| Merge Two Sorted Arrays | HackerRank | Easy |
| Watermelon / basic two-pointer warmups | Codeforces | Beginner (Div 2 A-level) |
| Two Pointer practice set | CSES Problem Set | Varies |
| AtCoder Beginner Contest two-pointer problems | AtCoder | Varies |
| Array partition problems | CodeChef | Beginner-Medium |

> **Note:** Always verify exact links and problem availability directly on each platform, as URLs and problem numbering can change over time.


---

## 29. Final Revision Kit

### 29.1 One-Page Notes

- **Two Pointer** = two indices traversing a linear structure with a movement rule exploiting monotonicity or cyclic structure.
- **5 core subtypes:** Opposite Direction, Same Direction (Read/Write), Fast & Slow, Diverging (Expand Around Center), Dual-Sequence Merge.
- **Precondition for most subtypes:** sorted data (opposite direction) or linked/cyclic structure (fast & slow).
- **Complexity payoff:** O(n²)→O(n) time typically; O(n)→O(1) space typically (vs hash-based alternatives).
- **vs Sliding Window:** Sliding window is same-direction two pointer maintaining a windowed aggregate over a contiguous range; general two pointer doesn't require a windowed aggregate and can converge from both ends.

### 29.2 Mind Map (Textual)

```
TWO POINTER
├── Opposite Direction (converging)
│   ├── Pair/Triplet/Quad Sum (2Sum, 3Sum, 4Sum)
│   ├── Container With Most Water
│   ├── Trapping Rain Water
│   ├── Valid Palindrome
│   └── Squares of Sorted Array
├── Same Direction (Read/Write)
│   ├── Remove Duplicates (I, II)
│   ├── Move Zeroes
│   ├── Remove Element
│   └── Dutch National Flag (3-pointer variant)
├── Fast & Slow
│   ├── Cycle Detection (I, II)
│   ├── Middle of Linked List
│   └── Happy Number / Find Duplicate Number
├── Diverging (Expand Around Center)
│   └── Longest Palindromic Substring
└── Dual-Sequence Merge
    ├── Merge Sorted Array
    ├── Merge Two Sorted Lists
    └── Intersection of Two Arrays
```

### 29.3 Pattern Map — Keyword to Pattern

| Keyword | Pattern |
|---|---|
| "sorted", "pair sum" | Opposite Direction |
| "in-place", "partition" | Same Direction |
| "cycle", "linked list midpoint" | Fast & Slow |
| "palindromic substring" (find) | Diverging |
| "merge two sorted" | Dual-Sequence Merge |
| "contiguous subarray/substring with constraint" | Sliding Window (related, not plain two pointer) |

### 29.4 Pointer Movement Guide (Quick Recall)

- Sum too small → `left += 1`
- Sum too large → `right -= 1`
- Match found → move both inward + skip duplicates
- Shorter wall (container/water) → move that pointer
- Fast & Slow → `slow` 1 step, `fast` 2 steps
- Read/write → `fast` always advances; `slow` advances only on "keep" condition

### 29.5 Recognition Flowchart (Quick Recall)

```
Sorted + need pair/triplet target?      -> Opposite Direction
Need in-place filter/compact?           -> Same Direction
Linked/cyclic structure?                -> Fast & Slow
Merging two sorted sequences?           -> Dual-Sequence Merge
Contiguous range + running property?    -> Sliding Window
```

### 29.6 Complexity Sheet (Quick Recall)

| Problem Class | Two Pointer Time | Two Pointer Space |
|---|---|---|
| Pair Sum | O(n) | O(1) |
| 3Sum | O(n²) | O(1) extra |
| 4Sum | O(n³) | O(1) extra |
| Dedup / Partition | O(n) | O(1) |
| Cycle Detection | O(n) | O(1) |
| Merge | O(m+n) | O(1) extra |

### 29.7 Interview Cheat Sheet (Quick Recall)

- Always state brute force first, then the structural insight, then the optimized approach.
- Explicitly name the pattern subtype you're using (interviewers value precise vocabulary).
- Prove correctness of greedy pointer movement when asked "why does this work?"
- Always dry-run on a small example, out loud.
- Mention space complexity improvement vs hash-based alternatives when relevant.

### 29.8 15-Minute Revision Plan

1. (3 min) Re-read the One-Page Notes (29.1) and Mind Map (29.2).
2. (4 min) Re-derive the 5 core templates from memory (Section 24.1) without looking.
3. (4 min) Solve Two Sum II and Remove Duplicates from memory, checking against Sections 4 and 7.
4. (4 min) Review the Common Mistakes Catalog (Section 26) to refresh what NOT to do.

### 29.9 1-Hour Revision Plan

1. (10 min) Read the full Introduction (Section 1) and Types of Two Pointer (Section 3).
2. (20 min) Re-implement from scratch, without looking: Two Sum II, 3Sum, Remove Duplicates, Move Zeroes, Container With Most Water.
3. (10 min) Re-implement Fast & Slow: Linked List Cycle, Middle of Linked List, Happy Number.
4. (10 min) Review Two Pointer vs Sliding Window (Section 21) and the Decision Tree (Section 22).
5. (10 min) Skim the Cheat Sheets (Section 27) and attempt 2-3 problems from the Practice Problem Bank (Section 28) cold.


---

## 30. FAQs

**Q1: Does the array always need to be sorted for Two Pointer?**
Not always — it depends on the subtype. Opposite-direction pair-sum problems need sorted data. Same-direction read/write problems (dedup, partition) often work on data that's sorted for a *different* reason (like removing duplicates from a sorted array) but the *technique itself* doesn't strictly require sortedness — e.g., Move Zeroes works on any array order. Fast & Slow doesn't need "sorted" data at all — it needs a linked/cyclic structure.

**Q2: When should I use a hash map instead of two pointer?**
When you need original indices from **unsorted** data and sorting would break that mapping, or when there's no monotonic/structural property to exploit (arbitrary unordered data with no linked structure). Hash maps trade O(n) space for avoiding the sort/structure requirement.

**Q3: Is Sliding Window a type of Two Pointer?**
Yes — it's a specialized same-direction two-pointer pattern that maintains a windowed aggregate (sum, count, frequency map) as the window expands and shrinks. The distinguishing feature from general two pointer is the **windowed invariant/aggregate being tracked incrementally**.

**Q4: Why does Floyd's Fast & Slow pointer use O(1) space instead of a hash set?**
Because it exploits the **mathematical guarantee** that a fast pointer moving twice as fast as a slow pointer must eventually "lap" it within a cycle — no need to remember every visited node, just track two positions.

**Q5: What's the biggest interview red flag when using Two Pointer?**
Not being able to explain **why** the pointer movement rule is correct (the monotonicity or greedy argument). Interviewers often probe this specifically because it's easy to memorize the code pattern without understanding the underlying proof.

**Q6: Can Two Pointer be generalized beyond two pointers?**
Yes — Three Sum/Four Sum use a **fixed outer pointer(s) + inner two-pointer**, generalizing to "k-Sum" with O(n^(k-1)) time. Dutch National Flag uses **three pointers** simultaneously for three-way partitioning.

**Q7: Does Two Pointer work on unsorted arrays at all?**
Yes, for problems that don't require a target-sum relationship exploiting sortedness — e.g., Move Zeroes, Remove Element, and Sliding Window-style contiguous-range problems all work on unsorted data, because their correctness relies on a different structural property (in-place partitioning order, or windowed monotonic feasibility) rather than numeric sortedness.

**Q8: How do I know whether to skip duplicates before or after finding a match in k-Sum problems?**
Skip duplicates for the **fixed/outer** pointer(s) at the **start** of each outer iteration (to avoid redundant outer passes), and skip duplicates for `left`/`right` **only after recording a match** (skipping before a match is found isn't meaningful, since no match has been recorded yet to be duplicated).

**Q9: Is Two Pointer always O(n)?**
Not necessarily — the "two pointer" idea can be nested (3Sum is O(n²), 4Sum is O(n³)), so the complexity depends on how many pointers are fixed vs how many actively move in a single monotonic pass. The **core two-pointer inner loop** itself is always O(n) for the portion of the array it scans.

**Q10: What's the single most important thing to internalize about this technique?**
That two pointer isn't really "a specific algorithm" — it's a **structural insight**: whenever moving one index provably lets you safely skip re-examining a range of already-ruled-out possibilities (because of sortedness, geometric bounds, or cyclic structure), you can replace a nested loop with two cooperating, forward-moving indices.

---

## Closing Notes

This handbook covers the Two Pointer Technique from first principles through advanced interview-level patterns, entirely in Python. Revisit the **Decision Tree** (Section 22) and **Cheat Sheets** (Section 27) as your fastest path to recognizing which subtype applies to a new, unseen problem — recognition is the real skill; the code templates themselves are short and mechanical once the right subtype is identified.

