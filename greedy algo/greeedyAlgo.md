# The Complete Greedy Algorithms Handbook


---

## Table of Contents

1. [Introduction to Greedy Algorithms](#1-introduction-to-greedy-algorithms)
2. [Greedy Fundamentals](#2-greedy-fundamentals)
3. [Python Greedy Templates](#3-python-greedy-templates)
4. [Core Greedy Patterns](#4-core-greedy-patterns)
5. [Classic Greedy Problems](#5-classic-greedy-problems)
   - [5.1 Activity Selection Problem](#51-activity-selection-problem)
   - [5.2 Fractional Knapsack](#52-fractional-knapsack)
   - [5.3 Job Sequencing with Deadlines](#53-job-sequencing-with-deadlines)
   - [5.4 Huffman Coding](#54-huffman-coding)
   - [5.5 Minimum Platforms](#55-minimum-platforms)
   - [5.6 Merge Intervals](#56-merge-intervals)
   - [5.7 Insert Interval](#57-insert-interval)
   - [5.8 Non-overlapping Intervals](#58-non-overlapping-intervals)
   - [5.9 Meeting Rooms I & II](#59-meeting-rooms-i--ii)
   - [5.10 Gas Station](#510-gas-station)
   - [5.11 Jump Game](#511-jump-game)
   - [5.12 Jump Game II](#512-jump-game-ii)
   - [5.13 Candy Distribution](#513-candy-distribution)
   - [5.14 Lemonade Change](#514-lemonade-change)
   - [5.15 Assign Cookies](#515-assign-cookies)
   - [5.16 Boat to Save People](#516-boat-to-save-people)
   - [5.17 Maximum Units on a Truck](#517-maximum-units-on-a-truck)
   - [5.18 Partition Labels](#518-partition-labels)
   - [5.19 Valid Parenthesis String](#519-valid-parenthesis-string)
   - [5.20 Queue Reconstruction by Height](#520-queue-reconstruction-by-height)
   - [5.21 Minimum Arrows to Burst Balloons](#521-minimum-arrows-to-burst-balloons)
   - [5.22 Remove Duplicate Letters](#522-remove-duplicate-letters)
   - [5.23 Reorganize String](#523-reorganize-string)
   - [5.24 IPO Problem](#524-ipo-problem)
   - [5.25 Task Scheduler](#525-task-scheduler)
6. [Advanced Greedy Concepts](#6-advanced-greedy-concepts)
7. [Applications of Greedy Algorithms](#7-applications-of-greedy-algorithms)
8. [Problem Recognition Guide](#8-problem-recognition-guide)
9. [Optimization Strategies](#9-optimization-strategies)
10. [Interview Preparation](#10-interview-preparation)
11. [Python Tips for Greedy Coding](#11-python-tips-for-greedy-coding)
12. [Common Mistakes](#12-common-mistakes)
13. [Cheat Sheets](#13-cheat-sheets)
14. [Practice Problem Bank](#14-practice-problem-bank)
15. [Final Revision Kit](#15-final-revision-kit)
16. [FAQs](#16-faqs)

---

## 1. Introduction to Greedy Algorithms

### 1.1 What is a Greedy Algorithm?

A **Greedy Algorithm** builds a solution piece by piece, always choosing the option that looks best **right now** — the *locally optimal* choice — without reconsidering earlier choices, in the hope that this sequence of local choices produces a *globally optimal* solution.

> **Formal idea:** At each step, pick the choice that maximizes (or minimizes) an immediate criterion, commit to it permanently, and shrink the problem. Never backtrack.

### 1.2 History

Greedy strategies are as old as algorithmic thinking itself. Formal treatment emerged with:

- **Kruskal (1956)** and **Prim (1957)** — greedy Minimum Spanning Tree algorithms.
- **Huffman (1952)** — greedy optimal prefix-free coding.
- **Edmonds (1971)** — matroid theory, which formalized *why* greedy works for certain structures.
- Modern competitive programming and interviews popularized greedy as a distinct "pattern" separate from Dynamic Programming (DP) and Brute Force.

### 1.3 Why Greedy Exists

Many optimization problems have exponentially many candidate solutions. Brute force explores all of them; DP explores overlapping subproblems with memoization. Greedy exists because **some problems have enough mathematical structure that a single, non-backtracking pass is provably optimal** — giving huge speed and simplicity gains over DP or brute force.

```
Brute Force  →  Explore ALL possibilities            (Slow, always correct)
Dynamic Prog →  Explore overlapping subproblems       (Medium, always correct if modeled right)
Greedy       →  Explore ONE path, never look back     (Fast, correct ONLY if proven)
```

### 1.4 Characteristics of Greedy Algorithms

| Characteristic | Meaning |
|---|---|
| Irrevocable choices | Once made, a decision is never undone |
| Local view | Decision based only on current state, not future consequences |
| Fast | Usually O(n log n) or O(n) after sorting |
| Requires proof | Must be proven correct — it is *not* correct by default |
| Often paired with sorting/heap | To always expose the "best current" candidate |

### 1.5 Greedy Choice Property

> **Definition:** A globally optimal solution can be reached by making a locally optimal (greedy) choice at each step.

This is the *load-bearing assumption* of every greedy algorithm. If it doesn't hold, greedy fails.

### 1.6 Optimal Substructure

> **Definition:** An optimal solution to the problem contains within it optimal solutions to subproblems.

This property is **shared with Dynamic Programming**. The difference:

- **DP:** many subproblems overlap and must be explored/combined (choice depends on comparing multiple subproblem solutions).
- **Greedy:** the subproblem to solve next is uniquely determined by the greedy choice — no comparison of alternatives needed.

### 1.7 Local vs Global Optimum

```
                     GLOBAL OPTIMUM (best overall answer)
                             ▲
                             │  Does greedy path reach here?
                             │
   Local Optimum A ●         │         ● Local Optimum B
        (greedy picks this)  │
                             │
        ┌────────────────────┴────────────────────┐
        │        SEARCH SPACE OF ALL SOLUTIONS      │
        └────────────────────────────────────────────┘
```

Greedy always walks toward the *nearest* uphill step. If the "hill" of the search space is shaped so every local peak is also part of the global peak (i.e., the problem is "greedy-friendly"), greedy wins. Otherwise, greedy can get trapped at a local optimum that is far from the best global answer.

### 1.8 Advantages of Greedy

- Simple to design and implement.
- Very fast — typically O(n log n).
- Low memory footprint — O(1) or O(n) extra space.
- Easy to reason about once correctness is established.

### 1.9 Disadvantages of Greedy

- Does **not** work for most optimization problems.
- Requires a rigorous proof (exchange argument / matroid / induction) — "it looks right" is not enough.
- Debugging incorrect greedy strategies is hard, because the algorithm always *runs* and *terminates*, it just may give a wrong answer silently.
- No general recipe — every problem needs its own correctness argument.

### 1.10 Real-World Applications

| Domain | Example |
|---|---|
| Operating Systems | CPU/Disk scheduling (SJF, priority) |
| Networking | Routing table construction, Dijkstra's greedy relaxation |
| Compression | Huffman encoding used in ZIP, JPEG, MP3 |
| Finance | Coin/currency change-making, greedy portfolio heuristics |
| Logistics | Vehicle loading (fractional knapsack style), delivery batching |
| Compilers | Register allocation (graph coloring, greedy heuristics) |
| AI/Heuristics | A* search greedy component, greedy NLP decoding (greedy token selection) |

### 1.11 Real-World Analogy

> **Analogy — Making Change with Coins:** A cashier giving change greedily picks the largest denomination coin that doesn't exceed the remaining amount, repeatedly. For "nice" currency systems (like INR or USD) this always uses the minimum number of coins. But for an arbitrary/adversarial coin system (e.g., coins {1, 3, 4} for amount 6), greedy gives 4+1+1 = 3 coins, while the optimal is 3+3 = 2 coins. This single example is the seed of *every* greedy counterexample in this handbook.

```
Amount = 6, Coins = {1, 3, 4}

GREEDY PATH:            OPTIMAL PATH:
  6                        6
  -4 → 2                   -3 → 3
  -1 → 1                   -3 → 0
  -1 → 0
  Coins used: 4,1,1 = 3    Coins used: 3,3 = 2   ✅ better
```


---

## 2. Greedy Fundamentals

### 2.1 The Exchange Argument (The Core Proof Technique)

The **exchange argument** is the standard way to *prove* a greedy strategy optimal. The structure:

1. Assume an optimal solution `OPT` exists that **differs** from the greedy solution `G` at some point.
2. Show that you can **swap/exchange** a piece of `OPT` with the greedy choice **without making the solution worse** (i.e., the new solution is still feasible and at least as good).
3. Repeat this exchange until `OPT` is transformed into `G`, proving `G` is *also* optimal.

```
OPT:      [ x1 , x2 , x3 , x4 ]
                    |
                    | swap x2 with greedy's pick g2
                    v
OPT':     [ x1 , g2 , x3 , x4 ]     (still feasible, cost unchanged or improved)
                    |
                    | repeat exchange steps...
                    v
G:        [ g1 , g2 , g3 , g4 ]     (now identical to greedy -- G is optimal too)
```

**Interview Tip:** When asked "prove this greedy works," structure your answer as an exchange argument -- interviewers specifically look for this reasoning pattern.

### 2.2 Proof of Correctness -- General Recipe

| Step | Action |
|---|---|
| 1 | State the greedy rule precisely (e.g., "sort by finish time, pick earliest") |
| 2 | Assume some other choice is part of an optimal solution |
| 3 | Show replacing that choice with the greedy choice doesn't hurt optimality |
| 4 | Conclude by induction that the greedy solution overall is optimal |

### 2.3 Counterexamples -- Why Greedy Fails

Greedy is a hypothesis, not a law. Classic **failure cases**:

- **0/1 Knapsack:** Picking the item with the best value/weight ratio first fails because items are indivisible -- you might waste capacity. (Fractional Knapsack works with greedy; 0/1 Knapsack needs DP.)
- **Coin Change with arbitrary denominations:** As shown in Section 1, greedy fails for non-canonical coin systems.
- **Longest Path in a Graph:** Greedily extending the "locally longest" edge does not yield the longest overall path.
- **Traveling Salesman Problem (TSP):** Nearest-neighbor greedy heuristic can be arbitrarily worse than optimal.

```
GREEDY FAILURE PATTERN:

   Step 1 choice looks best  ->  but it BLOCKS a much better Step 2 choice
   +--------+                     +--------+
   | Choice |  locally best       | Choice |  now no good options left
   |   A    |                     |   B    |
   +--------+                     +--------+
        Result: locally great, globally poor
```

### 2.4 Greedy vs Dynamic Programming

| Aspect | Greedy | Dynamic Programming |
|---|---|---|
| Decision making | One irrevocable choice per step | Explore/compare multiple subproblem outcomes |
| Optimal Substructure | Required | Required |
| Greedy Choice Property | Required | Not required |
| Time Complexity | Usually O(n log n) | Usually O(n^2) or higher |
| Space | O(1)-O(n) | O(n)-O(n^2) (memo tables) |
| Backtracking | Never | Implicit, via recurrence |
| Example | Activity Selection | 0/1 Knapsack |

### 2.5 Greedy vs Backtracking

| Aspect | Greedy | Backtracking |
|---|---|---|
| Explores alternatives | No | Yes, exhaustively (with pruning) |
| Guarantees correctness | Only if proven | Always (explores full space) |
| Speed | Fast | Slow (exponential worst case) |
| Use case | Provably greedy-correct problems | Constraint satisfaction, combinatorial search |

### 2.6 Greedy vs Brute Force

| Aspect | Greedy | Brute Force |
|---|---|---|
| Search space explored | Single path | Entire space |
| Correctness | Conditional | Always correct |
| Complexity | Low | Exponential/Factorial typically |
| When to use | Structure is provably greedy-friendly | No structure known, small n |

### 2.7 Decision Flow: Is This Problem Greedy?

```
                     +---------------------------+
                     |  Can you sort/prioritize   |
                     |  choices by some metric?   |
                     +-------------+---------------+
                                   | yes
                                   v
                     +---------------------------+
                     | Does picking best-by-metric |
                     | now NEVER hurt future steps  |
                     | (no useful backtracking)?    |
                     +-------------+---------------+
                         yes <-----+-----> no
                          |                 |
                          v                 v
                 +--------------+   +--------------------+
                 | Try GREEDY   |   | Consider DP /       |
                 | + prove via  |   | Backtracking /      |
                 | exchange arg |   | Brute Force instead |
                 +--------------+   +--------------------+
```

### 2.8 Matroid Theory (Intuition Only)

A **matroid** is an abstract structure `(S, I)` where `S` is a set of elements and `I` is a collection of "independent" subsets of `S` satisfying:

1. **Hereditary property:** if a set is independent, every subset of it is independent too.
2. **Exchange property:** if `A` and `B` are independent and `|A| < |B|`, there's an element in `B \ A` that can be added to `A` and keep it independent.

> **Why it matters:** Whenever your problem's feasible choices form a matroid, greedy is *guaranteed* to be optimal for maximizing a weight function over independent sets. This is the deep mathematical reason algorithms like Kruskal's MST work. You rarely need to prove matroid structure in an interview, but recognizing "this smells like a matroid" builds strong intuition for why sorting + greedy selection works.

---

## 3. Python Greedy Templates

These are reusable skeletons. Recognize the pattern, drop in your comparator/metric, done.

### 3.1 Sorting-based Greedy Template

```python
def sorting_greedy_template(items, key_func, reverse=False):
    """
    Generic template: sort by a metric, then walk through
    making a locally optimal choice at each step.
    """
    items.sort(key=key_func, reverse=reverse)
    result = []
    state = None  # whatever running state your problem needs (e.g., last_end_time)

    for item in items:
        if is_feasible(item, state):     # define per-problem
            result.append(item)
            state = update_state(item, state)

    return result
```

### 3.2 Heap-based Greedy Template (usage only)

```python
import heapq

def heap_greedy_template(items):
    """
    Generic template: always process the current best/worst
    item efficiently using a heap instead of re-sorting.
    """
    heap = []
    for item in items:
        heapq.heappush(heap, item)   # push (priority, item)

    result = []
    while heap:
        best = heapq.heappop(heap)
        result.append(best)
        # optionally push new derived items back, e.g. Huffman merge

    return result
```

### 3.3 Interval-based Greedy Template

```python
def interval_greedy_template(intervals):
    """
    Generic template for interval scheduling / merging problems.
    Sort by start OR end depending on the problem.
    """
    intervals.sort(key=lambda x: x[1])  # sort by end time (classic activity selection)
    selected = []
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end:      # no overlap -> greedy accepts
            selected.append((start, end))
            last_end = end

    return selected
```

### 3.4 Priority-based Selection Template

```python
def priority_selection_template(candidates, priority_func):
    """
    Pick items one at a time by priority until a constraint is exhausted.
    """
    candidates.sort(key=priority_func, reverse=True)
    budget = 0  # e.g., remaining capacity/time/money
    chosen = []

    for c in candidates:
        if fits(c, budget):
            chosen.append(c)
            budget = consume(c, budget)

    return chosen
```

### 3.5 Two-pointer Greedy Template

```python
def two_pointer_greedy_template(arr):
    """
    Common for problems like 'Assign Cookies' or 'Boat to Save People'
    where sorted arrays are consumed from both ends.
    """
    arr.sort()
    left, right = 0, len(arr) - 1
    count = 0

    while left <= right:
        if condition_met(arr[left], arr[right]):
            left += 1
        right -= 1
        count += 1

    return count
```

### 3.6 Frequency-based Greedy Template

```python
from collections import Counter
import heapq

def frequency_greedy_template(s):
    """
    Common for string-rearrangement problems (Reorganize String,
    Task Scheduler) -- always place the most frequent remaining
    character/task first.
    """
    freq = Counter(s)
    max_heap = [(-count, ch) for ch, count in freq.items()]
    heapq.heapify(max_heap)

    result = []
    while max_heap:
        count, ch = heapq.heappop(max_heap)
        result.append(ch)
        # push back with decremented count if needed by the problem

    return result
```

### 3.7 Best Practices

- Always **decide and justify the sort key first** -- 90% of greedy bugs are wrong sort criteria.
- Keep a single **running state variable** (`last_end`, `remaining_capacity`, `current_fuel`) -- avoid recomputing from scratch.
- Prefer `heapq` over repeated re-sorting when the "best" element changes dynamically.
- Use `key=` and `lambda` instead of custom comparator classes -- more Pythonic and faster.
- Write the **brute-force version first** mentally (or on paper) to confirm your greedy metric before coding.

### 3.8 Performance Considerations

| Operation | Complexity | Notes |
|---|---|---|
| `list.sort(key=...)` | O(n log n) | Timsort, stable |
| `heapq.heappush/pop` | O(log n) | Use for dynamic "current best" |
| `heapq.heapify` | O(n) | Bulk-build once, cheaper than n pushes |
| `bisect.insort` | O(n) | Use only if you need sorted insertion, not just heap semantics |
| `collections.Counter` | O(n) | Frequency table for frequency-greedy |

---

## 4. Core Greedy Patterns

Almost every greedy interview question is one of these patterns wearing a costume.

### 4.1 Pattern Map

```
                         GREEDY PATTERNS
                               |
     +---------------+--------+--------+----------------+
     |               |                 |                |
 SORT + PICK     INTERVAL          FREQUENCY        TWO-POINTER
 (Knapsack,      SCHEDULING /      GREEDY           GREEDY
  Job Seq,        MERGING          (Reorganize      (Assign Cookies,
  IPO)           (Meeting Rooms,    String, Task     Boat to Save
                  Merge Intervals,  Scheduler)        People)
                  Non-overlap)
```

### 4.2 Sorting + Greedy

**Idea:** Sort candidates by a single decisive metric (deadline, ratio, finish time, profit), then scan once, greedily accepting/rejecting.

**Used in:** Activity Selection, Fractional Knapsack, Job Sequencing, IPO.

### 4.3 Earliest Finish Time

**Idea:** Among overlapping options, the one that frees up resources soonest leaves the most room for future choices. This is *the* canonical exchange-argument proof (see Activity Selection, Section 5.1).

### 4.4 Earliest Start Time

**Idea:** Useful for merging or "sweep" problems (Merge Intervals, Minimum Platforms) where you process events in the order they occur.

### 4.5 Highest Profit / Minimum Cost

**Idea:** Sort by value density (profit per unit resource) — used in Fractional Knapsack, truck loading, and resource allocation problems.

### 4.6 Interval Scheduling & Merging

**Idea:** Sort intervals (by start or end), then use a single pass with a "current boundary" variable to merge or select non-overlapping intervals.

```
Timeline sweep:
  |----A----|
        |----B----|
                    |--C--|

Sorted by start, merge while overlapping:
  A,B overlap -> merge into [A_start, max(A_end,B_end)]
  Result overlaps with C? -> merge or keep separate
```

### 4.7 Resource Allocation

**Idea:** Assign the "cheapest sufficient" resource to each demand, sorted appropriately (Assign Cookies, Boat to Save People).

### 4.8 Frequency Greedy

**Idea:** Always handle the most frequent/urgent item first to avoid it causing a conflict later (Reorganize String, Task Scheduler, Huffman Coding).

### 4.9 Prefix Greedy

**Idea:** Make a decision based on prefix aggregates (running sum, running min/max) — e.g., Gas Station, Candy Distribution (left-to-right + right-to-left prefix passes).

### 4.10 Monotonic Decision / Local Optimization

**Idea:** Maintain a monotonic invariant (non-decreasing heights, non-increasing arrival deadlines) that guarantees each local choice is safe — e.g., Jump Game (max-reach monotonic expansion), Queue Reconstruction by Height.


---

## 5. Classic Greedy Problems

> Every problem below follows the same rigorous template: Definition -> Intuition -> Analogy -> Visualization -> Python Code -> Line-by-Line -> Dry Run -> Correctness -> Complexity -> Edge Cases -> Mistakes -> Interview Tips -> Variations -> Summary.

### 5.1 Activity Selection Problem

**Problem Statement:** Given `n` activities with start and end times, select the maximum number of activities that a single person/resource can perform, assuming no two selected activities overlap.

**Why it exists:** Models any single-resource scheduling problem -- one meeting room, one machine, one server thread.

**Intuition:** To fit in as many activities as possible, always keep the *earliest possible* free time. The activity that finishes soonest leaves the most room for everything after it.

**Real-world analogy:** Booking a single conference room -- prefer the meeting that ends earliest so the room frees up fastest for the next booking.

**ASCII Visualization:**

```
Activities (start, end):
A: |----|          (1,4)
B:    |-------|    (3,7)
C:        |--|     (5,7)... wait let's align properly below

Sorted by finish time:
A(1,3)  ############
B(2,5)      #####################
C(4,6)              ###############
D(6,8)                        ###############

Greedy walk:
 pick A (1,3) -> last_end=3
 B starts at 2 < 3 -> REJECT (overlaps)
 C starts at 4 >= 3 -> ACCEPT -> last_end=6
 D starts at 6 >= 6 -> ACCEPT -> last_end=8

Selected: A, C, D
```

**Python Implementation:**

```python
def activity_selection(activities):
    """
    activities: List[Tuple[start, end]]
    Returns the maximum set of non-overlapping activities.
    """
    # Step 1: sort by finish time (the greedy key)
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]
    last_end = activities[0][1]

    # Step 2: single greedy pass
    for start, end in activities[1:]:
        if start >= last_end:      # no overlap with last selected activity
            selected.append((start, end))
            last_end = end

    return selected
```

**Line-by-Line Explanation:**

- `activities.sort(key=lambda x: x[1])`: sorts activities by their finish time -- the core greedy decision.
- `selected = [activities[0]]`: always take the first (earliest-finishing) activity -- it can never hurt to take it.
- `last_end = activities[0][1]`: tracks the end time of the most recently accepted activity.
- The loop scans every remaining activity once; `start >= last_end` is the O(1) feasibility check.
- Accepting an activity updates `last_end`, shrinking the remaining problem.

**Dry Run:**

| Step | Current Activity | last_end before | start >= last_end? | Selected | last_end after |
|---|---|---|---|---|---|
| 1 | A (1,3) | -inf | -- (first, auto-select) | [A] | 3 |
| 2 | B (2,5) | 3 | 2 >= 3? No | [A] | 3 |
| 3 | C (4,6) | 3 | 4 >= 3? Yes | [A, C] | 6 |
| 4 | D (6,8) | 6 | 6 >= 6? Yes | [A, C, D] | 8 |

**Correctness Intuition (Exchange Argument):** Suppose an optimal solution `OPT` doesn't pick the earliest-finishing activity `A`. `OPT` must pick some other first activity `X` with `end(X) >= end(A)`. Replacing `X` with `A` in `OPT` cannot reduce the number of subsequent compatible activities, since `A` frees the resource at least as early. By induction, the greedy choice at every step is safe.

**Time Complexity:** O(n log n) for sorting + O(n) for the scan = **O(n log n)**.
**Space Complexity:** O(1) extra (O(n) if you must materialize the sorted copy).

**Edge Cases:**
- Empty activity list -> return `[]`.
- Activities with identical end times -> any tie-break works; result count is unaffected.
- Single activity -> trivially selected.

**Common Mistakes:**
- Sorting by **start time** instead of **finish time** (does not guarantee optimality).
- Using strict `>` instead of `>=` when activities may touch exactly at boundaries (clarify with interviewer whether touching counts as overlap).

**Interview Tips:** This is the "hello world" of greedy interval problems. Master its exchange-argument proof -- it's reused almost verbatim for Meeting Rooms, Non-overlapping Intervals, and Minimum Arrows to Burst Balloons.

**Optimizations:** None needed beyond the sort; this is already asymptotically optimal.

**Variations:** Weighted Activity Selection (requires DP, not greedy, because maximizing *weight* instead of *count* breaks the greedy choice property).

**Practice Problems:** GeeksforGeeks "Activity Selection Problem"; LeetCode 435 (Non-overlapping Intervals, inverse framing).

**Summary:** Sort by end time, greedily accept if the start is not earlier than the last accepted end. O(n log n). Foundational proof pattern for the entire interval-greedy family.

---

### 5.2 Fractional Knapsack

**Problem Statement:** Given `n` items each with a `weight` and `value`, and a knapsack of capacity `W`, maximize total value. Unlike 0/1 Knapsack, items **can be broken into fractions**.

**Why it exists:** Models resource allocation where partial consumption is allowed -- pouring liquids, cutting cloth, allocating divisible budgets.

**Intuition:** Always take as much as possible of the item with the highest **value-per-unit-weight** first. Because fractions are allowed, there's never a "wasted" leftover capacity dilemma -- you can always top off with a slice of the next best item.

**Real-world analogy:** Filling a truck with sand of different densities/values -- pour in the most valuable sand per kg first, and top off the last bit of space with a partial scoop.

**ASCII Visualization:**

```
Items sorted by value/weight ratio (descending):

Item   Value  Weight  Ratio
C       120     10     12.0   #################### take ALL
A       60      10      6.0   ########## take ALL
B       100     20      5.0   ####### take PART (fill remaining capacity)

Knapsack capacity = 25
Fill: C (10) -> remaining 15
      A (10) -> remaining 5
      B (5 of 20, i.e. 1/4) -> remaining 0
Total value = 120 + 60 + 25 = 205
```

**Python Implementation:**

```python
def fractional_knapsack(items, capacity):
    """
    items: List[Tuple[value, weight]]
    capacity: int/float total capacity of the knapsack
    Returns the maximum achievable value (float).
    """
    # Step 1: sort by value-per-weight ratio, descending (the greedy key)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    remaining = capacity

    for value, weight in items:
        if remaining <= 0:
            break
        take = min(weight, remaining)      # take whole item or just a fraction
        fraction = take / weight
        total_value += value * fraction
        remaining -= take

    return total_value
```

**Line-by-Line Explanation:**

- Sorting by `value/weight` ratio identifies the "densest" value first -- the greedy metric.
- `take = min(weight, remaining)`: take the whole item if it fits, otherwise only the remaining capacity's worth.
- `fraction = take / weight`: proportion of the item actually taken.
- `total_value += value * fraction`: add the proportional value.
- Loop breaks early once capacity is exhausted -- a simple optimization.

**Dry Run:**

| Step | Item (value, weight) | Ratio | remaining before | take | fraction | value added | remaining after |
|---|---|---|---|---|---|---|---|
| 1 | C (120, 10) | 12.0 | 25 | 10 | 1.0 | 120 | 15 |
| 2 | A (60, 10) | 6.0 | 15 | 10 | 1.0 | 60 | 5 |
| 3 | B (100, 20) | 5.0 | 5 | 5 | 0.25 | 25 | 0 |

Total value = 120 + 60 + 25 = **205**

**Correctness Intuition (Exchange Argument):** Suppose `OPT` takes less of the highest-ratio item than greedy and correspondingly more of a lower-ratio item. Swapping one unit of weight from the lower-ratio item to the higher-ratio item strictly increases (or keeps equal) total value, since value-per-unit is higher. Repeating this swap converts `OPT` into the greedy solution without ever decreasing value -- hence greedy is optimal.

**Time Complexity:** O(n log n) for sorting; O(n) for the greedy fill. **Total: O(n log n)**.
**Space Complexity:** O(1) extra.

**Edge Cases:**
- `capacity == 0` -> total value 0.
- All items have identical ratio -> any order works, result is the same.
- Capacity larger than total weight of all items -> take everything.

**Common Mistakes:**
- Sorting by `value` or `weight` alone instead of the **ratio** -- classic bug.
- Forgetting that this greedy approach is **invalid for 0/1 Knapsack** (items indivisible) -- interviewers love this trap.
- Integer division bugs in other languages; Python 3's `/` is safe (true division).

**Interview Tips:** Always explicitly state *why* this doesn't generalize to 0/1 Knapsack -- it demonstrates you understand the boundary of greedy's applicability, which is often the actual point of the question.

**Optimizations:** Use a max-heap instead of full sort if items stream in dynamically.

**Variations:** 0/1 Knapsack (DP only), Bounded Knapsack, Multiple Knapsacks.

**Practice Problems:** GeeksforGeeks "Fractional Knapsack Problem"; HackerRank "Greedy Florist" (related greedy resource allocation).

**Summary:** Sort by value/weight ratio descending; fill greedily, allowing fractional take of the last item. O(n log n). The direct counterexample to why 0/1 Knapsack needs DP.

---

### 5.3 Job Sequencing with Deadlines

**Problem Statement:** Given `n` jobs, each with a `deadline` and `profit`, and each job takes 1 unit of time, schedule jobs into time slots (one job per slot) to maximize total profit, where a job only counts if completed by its deadline.

**Why it exists:** Models single-machine scheduling with deadlines and rewards -- appears in ad scheduling, batch job execution, task prioritization.

**Intuition:** Process jobs in order of **decreasing profit**. For each job, greedily place it in the **latest available slot** at or before its deadline -- this preserves earlier slots for jobs with tighter deadlines that might come later in the profit-sorted order.

**Real-world analogy:** A freelancer picks the highest-paying gigs first and schedules each as late as possible before its deadline, keeping earlier open days free for other urgent, high-paying gigs.

**ASCII Visualization:**

```
Jobs sorted by profit desc: J1(profit=100,deadline=2), J2(90,1), J3(80,2), J4(70,1)

Slots:  [ 1 ][ 2 ]

Place J1 (deadline 2) -> latest free slot <=2 is slot 2 -> [ _ ][J1]
Place J2 (deadline 1) -> latest free slot <=1 is slot 1 -> [J2 ][J1]
Place J3 (deadline 2) -> slot 2 taken, slot 1 taken -> REJECT
Place J4 (deadline 1) -> slot 1 taken -> REJECT

Result: J2, J1 scheduled. Total profit = 90 + 100 = 190
```

**Python Implementation:**

```python
def job_sequencing(jobs):
    """
    jobs: List[Tuple[job_id, deadline, profit]]
    Returns (scheduled_job_ids, total_profit)
    """
    # Step 1: sort by profit descending (the greedy key)
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * (max_deadline + 1)   # slots[1..max_deadline] used
    total_profit = 0
    scheduled = []

    for job_id, deadline, profit in jobs:
        # Step 2: find latest free slot <= deadline
        for slot in range(min(deadline, max_deadline), 0, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                scheduled.append(job_id)
                break

    return scheduled, total_profit
```

**Line-by-Line Explanation:**

- Sort by profit descending: always consider the most valuable job first.
- `slots` array represents time units 1..max_deadline; `None` means free.
- Inner loop searches backward from `min(deadline, max_deadline)` down to 1 for a free slot -- placing as late as possible.
- If a free slot is found, mark it, add profit, record the job; otherwise the job is dropped (missed deadline / no room).

**Dry Run:** (see visualization above; tabulated)

| Step | Job (deadline, profit) | Search order | Slot found | Profit added | Slots state |
|---|---|---|---|---|---|
| 1 | J1 (2, 100) | 2 -> 1 | 2 | 100 | [_, _, J1] |
| 2 | J2 (1, 90) | 1 | 1 | 90 | [_, J2, J1] |
| 3 | J3 (2, 80) | 2 -> 1 | none free | 0 | unchanged |
| 4 | J4 (1, 70) | 1 | none free | 0 | unchanged |

Total profit = **190**

**Correctness Intuition:** Among jobs with equal or lower profit, delaying a job to the latest possible slot never blocks a higher-profit job (already scheduled greedily first) and maximizes the chance that other jobs can still fit earlier slots. This is proven via an exchange argument on slot assignments: any schedule can be rearranged to place each job as late as possible without reducing total profit.

**Time Complexity:** Naive: O(n log n) sort + O(n * d) slot search (d = max deadline) = **O(n log n + n*d)**. Optimized with **Disjoint Set Union (DSU)** "find latest free slot": **O(n log n + n * alpha(n))** ~ near O(n log n).

**Space Complexity:** O(d) for the slots array (or O(n) with DSU).

**Edge Cases:**
- All jobs share the same deadline -> only 1 job (highest profit) can be scheduled.
- Deadline of 0 -> job can never be scheduled (no valid slot).
- More jobs than slots -> lower-profit excess jobs are dropped.

**Common Mistakes:**
- Placing jobs in the **earliest** free slot instead of the **latest** -- this wastes early slots that tighter-deadline jobs might need.
- Off-by-one errors in slot indexing (slots are 1-indexed by deadline, not 0-indexed).
- Forgetting to bound the slot search by `max_deadline` when a job's deadline exceeds the number of available slots.

**Interview Tips:** Mention the **DSU (Union-Find) optimization** for `find-latest-free-slot` -- it shows depth beyond the O(n*d) brute approach and is a favorite follow-up question.

**Optimizations:**

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        self.parent[x] = y

def job_sequencing_optimized(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    dsu = DSU(max_deadline)
    total_profit, scheduled = 0, []

    for job_id, deadline, profit in jobs:
        avail_slot = dsu.find(min(deadline, max_deadline))
        if avail_slot > 0:
            dsu.union(avail_slot, avail_slot - 1)   # mark slot used, point to previous
            total_profit += profit
            scheduled.append(job_id)

    return scheduled, total_profit
```

**Variations:** Weighted Job Scheduling with variable durations (requires DP, not pure greedy, once jobs have different lengths and can overlap in complex ways -- see "Job Scheduling Problem" with intervals, which is DP-based when maximizing weighted non-overlapping intervals).

**Practice Problems:** GeeksforGeeks "Job Sequencing Problem"; LeetCode-style variants on scheduling with deadlines.

**Summary:** Sort jobs by profit descending; assign each job to the latest available slot before its deadline (accelerated via DSU). O(n log n) with the optimization.

---

### 5.4 Huffman Coding

**Problem Statement:** Given character frequencies, build an optimal **prefix-free binary code** that minimizes the total encoded length (sum of `frequency * code_length` for all characters).

**Why it exists:** Foundational lossless compression algorithm -- used in ZIP, JPEG, MP3, and as a component of DEFLATE/gzip.

**Intuition:** Repeatedly merge the two **least frequent** nodes into a new node (whose frequency is their sum), building a binary tree bottom-up. Frequent characters end up near the root (short codes); rare characters end up deep (long codes).

**Real-world analogy:** Morse code assigns the shortest sequences (`.`  for E, `-` for T) to the most common English letters and longer sequences to rare letters (`--..` for Z) -- Huffman coding automates and optimizes this idea for arbitrary frequency distributions.

**ASCII Visualization (Huffman Tree construction):**

```
Frequencies: a:5, b:9, c:12, d:13, e:16, f:45

Step 1: merge a(5)+b(9)=14        Step 2: merge 14+c(12)=26
     (14)                              (26)
    /    \                            /    \
  a(5)   b(9)                      (14)    c(12)
                                   /   \
                                 a(5)  b(9)

... continue merging smallest pairs until one tree remains ...

Final Huffman Tree (conceptual):
                        (100)
                      /        \
                  (55)          f(45)
                 /    \
              (26)     e(16)... [merged further with d(13) etc.]
             /    \
           (14)   c(12)
          /   \
        a(5)  b(9)

Shorter codes near the root (f is very frequent -> short code),
longer codes deep in the tree (a is rare -> long code).
```

**Python Implementation:**

```python
import heapq
from collections import Counter

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):          # needed so heapq can compare Nodes
        return self.freq < other.freq

def huffman_coding(text):
    """
    Returns a dict mapping character -> binary code string.
    """
    freq = Counter(text)
    heap = [Node(f, ch) for ch, f in freq.items()]
    heapq.heapify(heap)                       # Step 1: build min-heap of frequencies

    if len(heap) == 1:                        # edge case: single unique character
        only = heap[0]
        return {only.char: "0"}

    while len(heap) > 1:                      # Step 2: repeatedly merge two smallest
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}

    def assign_codes(node, path=""):          # Step 3: traverse tree to build codes
        if node is None:
            return
        if node.char is not None:             # leaf node
            codes[node.char] = path or "0"
            return
        assign_codes(node.left, path + "0")
        assign_codes(node.right, path + "1")

    assign_codes(root)
    return codes
```

**Line-by-Line Explanation:**

- `Counter(text)`: computes character frequencies in O(n).
- `Node.__lt__`: enables `heapq` to order nodes purely by frequency.
- `heapq.heapify(heap)`: builds the min-heap in O(n).
- Main loop: pop the two smallest-frequency nodes, merge them into a parent node with combined frequency, push back -- repeated until one tree remains (O(n log n) total).
- `assign_codes`: DFS from root, appending `"0"` for left branches and `"1"` for right branches; leaf nodes record their accumulated path as the final code.

**Dry Run:** (frequencies a:5, b:9, c:12, d:13, e:16, f:45)

| Step | Heap (sorted freqs) | Merge | New node freq |
|---|---|---|---|
| 1 | [5,9,12,13,16,45] | a(5)+b(9) | 14 |
| 2 | [12,13,14,16,45] | c(12)+d(13) | 25 |
| 3 | [14,16,25,45] | 14+16=30 | 30 |
| 4 | [25,30,45] | 25+30=55 | 55 |
| 5 | [45,55] | 45+55=100 | 100 (root) |

Resulting codes (typical): `f: 0`, `c: 100`, `d: 101`, `a: 1100`, `b: 1101`, `e: 111` (exact bit assignment depends on left/right convention, but lengths are optimal).

**Correctness Intuition (Exchange Argument):** In any optimal prefix code, the two least frequent characters must be at the deepest level and be siblings (otherwise swapping them with whoever *is* at the deepest level only decreases or maintains total cost, since deeper codes cost more and should be assigned to the least-frequent symbols). Repeatedly merging the two smallest frequencies mirrors exactly this optimal structural property, proven by induction on the number of characters.

**Time Complexity:** O(n log n) -- each of the n-1 merges does O(log n) heap operations.
**Space Complexity:** O(n) for the heap and tree nodes.

**Edge Cases:**
- Single unique character -> must still assign a 1-bit code (`"0"`) even though technically 0 bits would "suffice" -- decoding requires at least 1 bit per symbol here.
- All characters equally frequent -> Huffman tree becomes balanced, codes approach fixed-length encoding.
- Empty text -> return empty code map.

**Common Mistakes:**
- Forgetting `__lt__` on the `Node` class, causing `heapq` comparison errors when frequencies tie (Python tries to compare the next tuple/object field).
- Not handling the single-character edge case (produces a 0-length code, breaking decodability).
- Confusing Huffman coding (variable-length, no fixed structure) with fixed-length binary encoding.

**Interview Tips:** Be ready to explain **why prefix-free codes are decodable unambiguously** (no code is a prefix of another, so a decoder can greedily consume bits without lookahead) -- this is often the follow-up conceptual question.

**Optimizations:** Use `heapq` with tuples `(freq, unique_id, node)` instead of a custom `__lt__` to avoid comparison overhead when frequencies tie, if `unique_id` is cheap to generate (e.g., an incrementing counter).

**Variations:** Adaptive Huffman Coding (tree updates as data streams in), Canonical Huffman Codes (used for compact code-table storage in real compression formats).

**Practice Problems:** GeeksforGeeks "Huffman Coding | Greedy Algo-3"; LeetCode discussions on Huffman-style problems.

**Summary:** Repeatedly merge two least-frequent nodes using a min-heap; resulting tree yields globally optimal prefix-free codes. O(n log n) time, O(n) space.

---

### 5.5 Minimum Platforms

**Problem Statement:** Given arrival and departure times of trains at a station, find the **minimum number of platforms** needed so that no train has to wait.

**Why it exists:** Classic resource-count problem -- "how many concurrent resources are needed at peak overlap," seen in staffing, server pool sizing, and room-booking systems.

**Intuition:** Sort arrivals and departures separately. Sweep through time: every arrival increases the platform need by 1, every departure (that happens before or at the same time as processing) decreases it by 1. Track the running maximum -- that's the answer.

**Real-world analogy:** Counting the maximum number of guests simultaneously present at a party given everyone's arrival and departure times.

**ASCII Visualization:**

```
Arrivals:    9:00  9:40  9:50  11:00 15:00 18:00
Departures: 9:10  12:00 11:20 11:30 19:00 20:00

Sorted arr: [9:00, 9:40, 9:50, 11:00, 15:00, 18:00]
Sorted dep: [9:10, 11:20, 11:30, 12:00, 19:00, 20:00]

Sweep:
 time 9:00 arr -> platforms=1 (max=1)
 time 9:10 dep -> platforms=0
 time 9:40 arr -> platforms=1 (max=1)
 time 9:50 arr -> platforms=2 (max=2)
 time 11:00 arr -> platforms=3 (max=3)
 time 11:20 dep -> platforms=2
 time 11:30 dep -> platforms=1
 time 12:00 dep -> platforms=0
 ... etc

Answer: 3 platforms needed at peak (around 11:00)
```

**Python Implementation:**

```python
def min_platforms(arrivals, departures):
    """
    arrivals, departures: List[int] (times represented as sortable numbers, e.g. minutes)
    Returns the minimum number of platforms required.
    """
    arrivals = sorted(arrivals)
    departures = sorted(departures)

    n = len(arrivals)
    i = j = 0
    platforms_needed = 0
    max_platforms = 0

    while i < n and j < n:
        if arrivals[i] <= departures[j]:      # a train arrives before/at a departure
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:                                  # a train departs, freeing a platform
            platforms_needed -= 1
            j += 1

    return max_platforms
```

**Line-by-Line Explanation:**

- Sorting arrivals and departures independently lets us merge-sweep them like two sorted streams (classic two-pointer technique).
- `arrivals[i] <= departures[j]`: if the next event chronologically is an arrival, a new platform is needed.
- Otherwise a departure happens first, freeing one platform.
- `max_platforms` records the peak simultaneous platform usage -- the final answer.

**Dry Run:** (see visualization table above; formalized)

| i | j | arrivals[i] | departures[j] | Action | platforms_needed | max_platforms |
|---|---|---|---|---|---|---|
| 0 | 0 | 9:00 | 9:10 | arrival | 1 | 1 |
| 1 | 0 | 9:40 | 9:10 | departure | 0 | 1 |
| 1 | 1 | 9:40 | 11:20 | arrival | 1 | 1 |
| 2 | 1 | 9:50 | 11:20 | arrival | 2 | 2 |
| 3 | 1 | 11:00 | 11:20 | arrival | 3 | 3 |
| 3 | 2 | 15:00 | 11:30 | departure | 2 | 3 |

...continues similarly; final answer **3**.

**Correctness Intuition:** At any instant, the number of platforms needed equals the number of trains whose arrival has occurred but departure hasn't yet. Sweeping sorted events in chronological order and tracking a running counter exactly computes this maximum overlap -- it's a direct simulation, not even requiring an exchange argument, but it *is* greedy in spirit (process events in time order, make the immediate correct local update).

**Time Complexity:** O(n log n) for sorting both arrays; O(n) for the sweep. **Total: O(n log n)**.
**Space Complexity:** O(n) for sorted copies (O(1) extra if sorting in place).

**Edge Cases:**
- A train's arrival equals another's departure -- convention matters (the code above treats simultaneous arrival/departure as needing a new platform; clarify with interviewer if departure should free the platform for a same-time arrival).
- All trains fully disjoint in time -> answer is 1.
- All trains overlap completely -> answer is n.

**Common Mistakes:**
- Sorting the `(arrival, departure)` pairs together instead of sorting arrivals and departures **independently** -- this is the single most common bug.
- Mishandling the tie-break between simultaneous arrival and departure events.

**Interview Tips:** This is essentially "meeting rooms II" wearing a train-themed costume -- recognize the equivalence immediately when either version appears.

**Optimizations:** None further needed; O(n log n) is optimal (sorting lower bound).

**Variations:** Meeting Rooms II (Section 5.9) is the identical problem in different clothing; can also be solved via a min-heap of end times.

**Practice Problems:** GeeksforGeeks "Minimum Platforms"; LeetCode 253 (Meeting Rooms II).

**Summary:** Sort arrivals and departures separately; two-pointer sweep tracking a running counter of active trains; the maximum value of that counter is the answer. O(n log n).


---

### 5.6 Merge Intervals

**Problem Statement:** Given a collection of intervals, merge all overlapping intervals into their minimal covering set.

**Why it exists:** Fundamental preprocessing step for calendar apps, resource booking systems, and range-based data compaction.

**Intuition:** Sort by start time. Walk through, and if the current interval overlaps the last merged interval, extend the last one's end; otherwise start a new merged interval.

**Real-world analogy:** Combining overlapping calendar blocks into single "busy" blocks for a free/busy view.

**ASCII Visualization:**

```
Input:   [1,3] [2,6] [8,10] [15,18]

Sorted by start (already sorted here):
  |--1,3--|
      |----2,6----|
                        |--8,10--|
                                       |--15,18--|

Overlap 1,3 & 2,6 -> merge to [1,6]
[8,10] doesn't overlap [1,6] -> new group
[15,18] doesn't overlap [8,10] -> new group

Output: [1,6] [8,10] [15,18]
```

**Python Implementation:**

```python
def merge_intervals(intervals):
    """
    intervals: List[List[int]] each [start, end]
    Returns merged non-overlapping intervals, sorted by start.
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])   # sort by start time
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:            # overlap (or touching) -> merge
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged
```

**Line-by-Line Explanation:**

- Sort by start time so overlapping intervals become adjacent in the scan.
- `merged` accumulates the result; initialize with the first interval.
- For each subsequent interval, compare its start against the last merged interval's end.
- If overlapping (`start <= last_end`), extend the last merged interval's end to the max of both ends.
- Otherwise, append as a brand-new interval group.

**Dry Run:**

| Step | Interval | last merged | Overlap? | Action | merged list |
|---|---|---|---|---|---|
| 1 | [1,3] | -- | -- | init | [[1,3]] |
| 2 | [2,6] | [1,3] | 2<=3 yes | extend end to 6 | [[1,6]] |
| 3 | [8,10] | [1,6] | 8<=6 no | new group | [[1,6],[8,10]] |
| 4 | [15,18] | [8,10] | 15<=10 no | new group | [[1,6],[8,10],[15,18]] |

**Correctness Intuition:** After sorting by start, any interval that overlaps the current merged block must appear before we move past it (since starts are non-decreasing). Extending the end to the maximum ensures we don't miss overlaps with subsequent intervals that fall within the extended range. A single left-to-right pass suffices because no interval later in sorted order can overlap an *earlier* start than what's already been considered.

**Time Complexity:** O(n log n) for sorting + O(n) scan = **O(n log n)**.
**Space Complexity:** O(n) for the output (O(log n) to O(n) for sort's internal stack, depending on implementation).

**Edge Cases:**
- Empty input -> return `[]`.
- Fully nested intervals (e.g., `[1,10]` and `[2,3]`) -> correctly merge to `[1,10]`.
- Touching intervals (`[1,3]` and `[3,5]`) -> merge (per typical problem convention) since they share boundary point 3.

**Common Mistakes:**
- Sorting by end time instead of start time (breaks the single-pass merge invariant).
- Using `<` instead of `<=` for the overlap check, mishandling touching intervals.
- Mutating the input list unexpectedly when the interviewer expects a fresh list.

**Interview Tips:** This exact pattern (sort by start, extend-or-append) reappears in Insert Interval and various sweep-line problems -- master it once, reuse everywhere.

**Optimizations:** None beyond the O(n log n) sort; this is optimal.

**Variations:** Insert Interval (Section 5.7) is Merge Intervals with one new interval inserted before merging.

**Practice Problems:** LeetCode 56 (Merge Intervals); GeeksforGeeks "Merging Intervals".

**Summary:** Sort by start; extend the last merged interval's end whenever overlap is detected, otherwise start a new group. O(n log n).

---

### 5.7 Insert Interval

**Problem Statement:** Given a set of **non-overlapping** intervals sorted by start time, insert a new interval and merge if necessary, keeping the result sorted and non-overlapping.

**Why it exists:** Common in calendar systems when adding a single new event to an already-merged schedule -- avoids re-sorting/re-merging everything from scratch.

**Intuition:** Since the input is already sorted and non-overlapping, walk through in three phases: (1) intervals ending strictly before the new interval starts -- keep as-is, (2) intervals overlapping the new interval -- merge them all into one, (3) intervals starting strictly after the new interval ends -- keep as-is.

**Real-world analogy:** Adding one new busy block to an already-consolidated calendar and only touching the neighbors that actually clash with it.

**ASCII Visualization:**

```
Existing: [1,3] [6,9]
New:      [2,5]

Phase 1 (ends before new starts): none ([1,3] overlaps 2, so skip phase 1 for it)
Phase 2 (merge overlapping): [1,3] overlaps [2,5] -> merge to [1,5]
                              [6,9] does not overlap [1,5] (6 > 5) -> stop merging
Phase 3 (remaining): [6,9] unchanged

Output: [1,5] [6,9]
```

**Python Implementation:**

```python
def insert_interval(intervals, new_interval):
    """
    intervals: List[List[int]] sorted, non-overlapping
    new_interval: List[int] [start, end]
    Returns the updated sorted, non-overlapping interval list.
    """
    result = []
    i, n = 0, len(intervals)
    start, end = new_interval

    # Phase 1: intervals ending before new_interval starts
    while i < n and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    # Phase 2: merge all overlapping intervals into one
    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    result.append([start, end])

    # Phase 3: remaining intervals after new_interval
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
```

**Line-by-Line Explanation:**

- Phase 1 loop copies intervals entirely to the left of the new interval unchanged.
- Phase 2 loop absorbs every interval that overlaps the (growing) new interval, expanding `start`/`end` as needed -- this is the greedy merge step.
- After phase 2, exactly one merged interval `[start, end]` is appended.
- Phase 3 copies the remaining untouched intervals.

**Dry Run:**

| Phase | i | intervals[i] | Condition | Action |
|---|---|---|---|---|
| 1 | 0 | [1,3] | 3 < 2? No | stop phase 1 (nothing copied) |
| 2 | 0 | [1,3] | 1 <= 5? Yes | merge: start=min(2,1)=1, end=max(5,3)=5, i=1 |
| 2 | 1 | [6,9] | 6 <= 5? No | stop phase 2 |
| -- | -- | -- | append [1,5] | result=[[1,5]] |
| 3 | 1 | [6,9] | -- | copy | result=[[1,5],[6,9]] |

**Correctness Intuition:** Because the original intervals are sorted and non-overlapping, once an interval's start exceeds the merged interval's current end, no later interval can overlap it either (since starts only increase). This guarantees the three-phase greedy sweep never needs to revisit earlier decisions.

**Time Complexity:** O(n) -- single pass, no sorting required since input is pre-sorted.
**Space Complexity:** O(n) for the output list.

**Edge Cases:**
- New interval overlaps nothing -> insert at correct sorted position via phases 1/3 with phase 2 doing one trivial "merge" of just itself.
- New interval swallows all existing intervals -> phase 2 consumes everything.
- Empty existing interval list -> return `[new_interval]`.

**Common Mistakes:**
- Forgetting this problem assumes **pre-sorted, non-overlapping** input; naively sorting everything and calling `merge_intervals` works but discards the O(n) optimization opportunity.
- Off-by-one in overlap conditions (`<` vs `<=`).

**Interview Tips:** Explicitly mention the O(n) vs O(n log n) trade-off compared to just appending and re-running Merge Intervals -- shows you noticed the "already sorted" precondition.

**Optimizations:** Already optimal at O(n).

**Variations:** Batch-inserting multiple new intervals (equivalent to Merge Intervals from scratch).

**Practice Problems:** LeetCode 57 (Insert Interval).

**Summary:** Three-phase single pass: copy-before, merge-overlap, copy-after. O(n), leveraging the pre-sorted, non-overlapping precondition.

---

### 5.8 Non-overlapping Intervals

**Problem Statement:** Given a set of intervals, find the **minimum number of intervals to remove** so that the rest are non-overlapping.

**Why it exists:** The complement framing of Activity Selection -- instead of maximizing what you keep, you minimize what you discard; both are solved by the identical greedy rule.

**Intuition:** Maximize the number of non-overlapping intervals you can keep (exactly Activity Selection, sorted by end time), then the answer is `total - kept`.

**Real-world analogy:** Given a set of clashing meeting requests, cancel the fewest possible so the rest fit without conflict.

**ASCII Visualization:**

```
Intervals: [1,2] [2,3] [3,4] [1,3]

Sorted by end: [1,2] [2,3] [1,3] [3,4]

Greedy keep (Activity Selection logic):
 keep [1,2] -> last_end=2
 [2,3]: start 2 >= 2 -> keep -> last_end=3
 [1,3]: start 1 >= 3? No -> remove
 [3,4]: start 3 >= 3 -> keep -> last_end=4

Kept = 3, Total = 4 -> Removed = 1
```

**Python Implementation:**

```python
def erase_overlap_intervals(intervals):
    """
    intervals: List[List[int]]
    Returns the minimum number of intervals to remove.
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])   # sort by end time (identical to Activity Selection)
    kept = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= last_end:            # no overlap -> keep it
            kept += 1
            last_end = end
        # else: overlaps -> implicitly "removed" (skip)

    return len(intervals) - kept
```

**Line-by-Line Explanation:**

- Identical core loop to Activity Selection -- sort by end time, greedily keep non-overlapping intervals.
- `kept` counts how many intervals survive the greedy filter.
- The answer is simply the total count minus the survivors -- everything not kept must have been removed.

**Dry Run:**

| Step | Interval | last_end before | start>=last_end? | kept | last_end after |
|---|---|---|---|---|---|
| 1 | [1,2] | -- | init | 1 | 2 |
| 2 | [2,3] | 2 | yes | 2 | 3 |
| 3 | [1,3] | 3 | 1>=3 no | 2 | 3 |
| 4 | [3,4] | 3 | yes | 3 | 4 |

Removed = 4 - 3 = **1**

**Correctness Intuition:** Maximizing the kept non-overlapping set is exactly Activity Selection, already proven optimal via the exchange argument (Section 5.1). Minimizing removals is a linear transformation (`total - kept`) of that same optimum, so it inherits the proof directly.

**Time Complexity:** O(n log n).
**Space Complexity:** O(1) extra.

**Edge Cases:**
- No intervals -> 0 removals.
- All intervals identical -> keep 1, remove the rest.
- Already non-overlapping -> 0 removals.

**Common Mistakes:**
- Sorting by start time instead of end time -- breaks the proof.
- Trying to directly decide "which to remove" instead of the easier complementary "which to keep" framing.

**Interview Tips:** Recognizing that this is literally Activity Selection in disguise is the entire point of the question -- say so explicitly.

**Optimizations:** None needed.

**Variations:** Minimum Arrows to Burst Balloons (Section 5.21) uses the same core loop with a subtly different overlap condition.

**Practice Problems:** LeetCode 435 (Non-overlapping Intervals).

**Summary:** Sort by end time, greedily count keepable non-overlapping intervals (Activity Selection), then subtract from total. O(n log n).

---

### 5.9 Meeting Rooms I & II

**Problem Statement:**
- **Meeting Rooms I:** Given meeting intervals, determine if a person can attend **all** meetings (i.e., no two overlap).
- **Meeting Rooms II:** Given meeting intervals, find the **minimum number of conference rooms** required to hold all meetings.

**Why it exists:** Direct real-world resource-count problem, identical in structure to Minimum Platforms (Section 5.5).

**Intuition:**
- **Room I:** Sort by start time; if any meeting starts before the previous one ends, attendance is impossible.
- **Room II:** Use a min-heap of end times ("room availability"); for each meeting, if the earliest-freeing room is free before this meeting starts, reuse it; otherwise allocate a new room.

**Real-world analogy:** Exactly Minimum Platforms, but for meeting rooms instead of railway platforms.

**ASCII Visualization (Room II via heap):**

```
Meetings sorted by start: [0,30] [5,10] [15,20]

Heap (end times of rooms in use) starts empty.

[0,30]: heap empty -> new room -> heap=[30]
[5,10]: heap top=30 > 5 (room busy) -> new room -> heap=[10,30]
[15,20]: heap top=10 <= 15 (room free!) -> reuse -> pop 10, push 20 -> heap=[20,30]

Rooms used (heap size) = 2
```

**Python Implementation (Room I):**

```python
def can_attend_all_meetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:   # overlap detected
            return False
    return True
```

**Python Implementation (Room II):**

```python
import heapq

def min_meeting_rooms(intervals):
    """
    intervals: List[List[int]] [start, end]
    Returns the minimum number of rooms needed.
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])   # process meetings in start-time order
    heap = []                             # min-heap of end times ("room free at")

    for start, end in intervals:
        if heap and heap[0] <= start:     # earliest-freeing room is already free
            heapq.heappop(heap)           # reuse that room
        heapq.heappush(heap, end)         # occupy a room (new or reused) until 'end'

    return len(heap)                      # heap size = rooms simultaneously in use
```

**Line-by-Line Explanation:**

- Sort meetings by start time so we process them in chronological order.
- The heap holds end times of currently occupied rooms, smallest (earliest-freeing) on top.
- If the earliest-freeing room's end time is `<=` the current meeting's start, that room can be reused -- pop it.
- Push the current meeting's end time -- either reusing a freed slot or genuinely adding a new room.
- Final heap size equals the number of rooms simultaneously in use at the peak.

**Dry Run:** See visualization above; final answer **2** rooms.

**Correctness Intuition:** The heap always represents the set of "rooms currently busy" with their earliest checkout time exposed at the top. Reusing a room the moment it's free (rather than always allocating new) is optimal because delaying reuse can never reduce future room needs -- it can only cause unnecessary new allocations. This is a direct greedy/exchange argument identical in spirit to Minimum Platforms.

**Time Complexity:** O(n log n) -- sorting + n heap operations each O(log n).
**Space Complexity:** O(n) for the heap in the worst case (all meetings overlap).

**Edge Cases:**
- No meetings -> 0 rooms.
- All meetings overlap -> rooms needed = n.
- Meetings that touch exactly (`end == next start`) -> typically allowed to share a room (check problem convention).

**Common Mistakes:**
- Using `<` instead of `<=` when checking if a room is free -- changes whether back-to-back meetings can share a room.
- Solving Room II with the Room I algorithm (doesn't generalize -- Room I is a special case answering "is max concurrency <= 1?").

**Interview Tips:** Present both the **heap solution** and the **two-pointer arrival/departure sweep** (identical to Minimum Platforms) -- interviewers often ask for both to test versatility.

**Optimizations:** The two-pointer sweep (Section 5.5 style) achieves the same O(n log n) with slightly lower constant factors (array sort vs. heap operations); mention both.

**Variations:** Minimum Platforms (Section 5.5) is the exact same problem in a different setting.

**Practice Problems:** LeetCode 252 (Meeting Rooms), LeetCode 253 (Meeting Rooms II).

**Summary:** Room I: sort + adjacent overlap check. Room II: min-heap of end times, reuse rooms when freed, heap size = answer. O(n log n).

---

### 5.10 Gas Station

**Problem Statement:** There are `n` gas stations in a circle, each with `gas[i]` fuel and a cost `cost[i]` to travel to the next station. Determine the starting station index from which a car can complete the full circuit, or return -1 if impossible.

**Why it exists:** Classic prefix-sum + greedy problem testing the insight that a **global feasibility check** can be reduced to a single linear scan.

**Intuition:** If the total gas is less than total cost, no solution exists. Otherwise, exactly one valid starting point exists. Track a running "tank" balance; whenever it goes negative, none of the stations from the last reset point up to the current one could have been a valid start -- reset the candidate start to the *next* station.

**Real-world analogy:** Planning a round trip and figuring out the only gas station from which you'll never run dry, using a single pass instead of testing every possible starting point.

**ASCII Visualization:**

```
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
diff = [-2,-2,-2, 3, 3]

Running tank, starting candidate = 0:
 i=0: tank=-2 -> negative! reset candidate=1, tank=0
 i=1: tank=-2 -> negative! reset candidate=2, tank=0
 i=2: tank=-2 -> negative! reset candidate=3, tank=0
 i=3: tank=3
 i=4: tank=6

Total diff sum = -2-2-2+3+3 = 0 >= 0 -> feasible
Answer: start at index 3
```

**Python Implementation:**

```python
def can_complete_circuit(gas, cost):
    """
    gas, cost: List[int] of equal length n
    Returns the starting index, or -1 if no valid start exists.
    """
    total_tank = 0
    curr_tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_tank += diff
        curr_tank += diff

        if curr_tank < 0:            # can't reach i+1 from current 'start'
            start = i + 1            # every station from old start..i is disqualified
            curr_tank = 0            # reset running balance for new candidate

    return start if total_tank >= 0 else -1
```

**Line-by-Line Explanation:**

- `total_tank` accumulates the overall gas-cost balance across the whole circuit -- determines feasibility.
- `curr_tank` accumulates the balance since the current `start` candidate.
- Whenever `curr_tank` dips negative, **no station between the old start and `i` (inclusive)** could be a valid start either (proven below), so jump the candidate to `i + 1` and reset.
- At the end, if `total_tank >= 0`, the last surviving `start` candidate is guaranteed valid; otherwise no solution exists.

**Dry Run:** (see visualization; tabulated)

| i | gas[i] | cost[i] | diff | curr_tank (before check) | curr_tank<0? | start after |
|---|---|---|---|---|---|---|
| 0 | 1 | 3 | -2 | -2 | yes | 1 |
| 1 | 2 | 4 | -2 | -2 | yes | 2 |
| 2 | 3 | 5 | -2 | -2 | yes | 3 |
| 3 | 4 | 1 | 3 | 3 | no | 3 |
| 4 | 5 | 2 | 3 | 6 | no | 3 |

`total_tank = 0 >= 0` -> answer = **3**

**Correctness Intuition:** If the tank goes negative arriving at station `i` starting from `start`, then for **any** station `j` with `start <= j < i`, starting from `j` instead can only accumulate a `curr_tank` that is `>=` what starting from `start` would give at that point (since all intermediate partial sums from `start` to `j` were non-negative, otherwise we'd have reset earlier) -- so if `start` fails by position `i`, every `j` in between fails too, justifying the jump to `i+1`. Combined with the fact that a solution exists iff total gas >= total cost, exactly one valid rotation exists, and this single pass finds it.

**Time Complexity:** O(n) -- one pass.
**Space Complexity:** O(1).

**Edge Cases:**
- `sum(gas) < sum(cost)` -> return -1 immediately (handled naturally since `total_tank` ends negative).
- Single station -> trivially valid if `gas[0] >= cost[0]`.
- All diffs are exactly zero -> any starting point works; algorithm returns index 0.

**Common Mistakes:**
- Trying an O(n^2) brute-force simulation from every start (works but misses the greedy insight interviewers want).
- Forgetting to check `total_tank >= 0` at the end -- the loop alone doesn't verify global feasibility, only tracks the *candidate*.

**Interview Tips:** Clearly separate the two invariants being tracked (`total_tank` for feasibility, `curr_tank` for candidate validity) -- interviewers often ask "why do you need both?"

**Optimizations:** Already optimal at O(n) time, O(1) space.

**Variations:** Similar "single pass with reset on failure" pattern appears in Kadane's algorithm (max subarray) and Jump Game.

**Practice Problems:** LeetCode 134 (Gas Station).

**Summary:** Single pass tracking both a total feasibility sum and a running candidate-start balance; reset the candidate whenever the running balance goes negative. O(n) time, O(1) space.


---

### 5.11 Jump Game

**Problem Statement:** Given an array `nums` where `nums[i]` is the maximum jump length from index `i`, determine if you can reach the last index starting from index 0.

**Why it exists:** Tests the "monotonic reachability" greedy pattern -- tracking the farthest reachable point in a single pass rather than exploring every possible jump sequence (which would be exponential).

**Intuition:** Maintain `max_reach`, the farthest index reachable so far. Scan left to right; if the current index ever exceeds `max_reach`, it's unreachable and the whole array is unreachable. Otherwise keep extending `max_reach = max(max_reach, i + nums[i])`.

**Real-world analogy:** Hopping across stepping stones where each stone tells you the maximum number of stones you can leap; you only care about the farthest stone you could ever reach at each point, not the specific path.

**ASCII Visualization:**

```
nums = [2, 3, 1, 1, 4]
idx:    0  1  2  3  4

i=0: max_reach = max(0, 0+2) = 2
i=1: 1 <= 2 (reachable) -> max_reach = max(2, 1+3) = 4
i=2: 2 <= 4 -> max_reach = max(4, 2+1) = 4
i=3: 3 <= 4 -> max_reach = max(4, 3+1) = 4
i=4: 4 <= 4 -> reached last index (4)!  ✅ True

Reach frontier grows:  [0]---2   -------->4
                            (jumps keep extending frontier past the end)
```

**Python Implementation:**

```python
def can_jump(nums):
    """
    nums: List[int]
    Returns True if the last index is reachable from index 0.
    """
    max_reach = 0
    n = len(nums)

    for i in range(n):
        if i > max_reach:          # current index is unreachable
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:     # early exit optimization
            return True

    return True
```

**Line-by-Line Explanation:**

- `max_reach` starts at 0 -- we always start able to "reach" index 0.
- The check `i > max_reach` catches the exact failure moment: we've walked past every index we could ever have jumped to.
- `max_reach = max(max_reach, i + nums[i])`: greedily always keep the best (farthest) frontier seen so far -- never shrink it.
- Early exit the moment the frontier reaches or passes the last index.

**Dry Run:** (see visualization; tabulated)

| i | i > max_reach? | i + nums[i] | max_reach after |
|---|---|---|---|
| 0 | 0>0 no | 2 | 2 |
| 1 | 1>2 no | 4 | 4 |
| 2 | 2>4 no | 3 | 4 |
| 3 | 3>4 no | 4 | 4 |
| 4 | 4>4 no | 8 | 8 (>= n-1=4) -> return True |

**Correctness Intuition:** `max_reach` is a monotonically non-decreasing upper bound on every index reachable using *any* combination of jumps seen so far -- it doesn't matter *which* specific path achieves it, only that some path does. If the scan ever reaches an index beyond this bound, no sequence of prior jumps -- greedy or otherwise -- could have gotten there, so failure is certain and correctly detected.

**Time Complexity:** O(n) -- single pass.
**Space Complexity:** O(1).

**Edge Cases:**
- Single-element array -> trivially reachable (already at the last index).
- `nums[0] == 0` and array length > 1 -> immediately stuck, return False.
- A zero in the middle that's already "jumped over" by an earlier large jump -> still fine, since `max_reach` already accounts for it.

**Common Mistakes:**
- Simulating actual jump paths recursively/exponentially instead of tracking a simple frontier -- leads to TLE (Time Limit Exceeded).
- Checking `nums[i] == 0` as an automatic failure -- incorrect, since an earlier jump might have already carried the frontier past this zero.

**Interview Tips:** Explicitly state the invariant ("max_reach is the union of all reachable indices so far") -- this one sentence usually convinces interviewers you understand *why* greedy works here.

**Optimizations:** Already O(n) optimal; early-exit condition is a minor constant-factor speedup.

**Variations:** Jump Game II (Section 5.12) asks for the *minimum number of jumps* instead of feasibility -- a related but distinct greedy (level-order/BFS-style frontier expansion).

**Practice Problems:** LeetCode 55 (Jump Game).

**Summary:** Track the farthest reachable index using a single running maximum; fail the instant the scan pointer outpaces it. O(n) time, O(1) space.

---

### 5.12 Jump Game II

**Problem Statement:** Given the same setup as Jump Game, return the **minimum number of jumps** needed to reach the last index (guaranteed reachable).

**Why it exists:** Extends the reachability insight into a "greedy BFS-by-levels" pattern -- widely reused in shortest-path-on-implicit-graph problems.

**Intuition:** Think of it as BFS by levels, where each "level" is one jump. Track the current jump's reachable boundary (`current_end`) and the farthest boundary achievable with one more jump (`farthest`). When you exhaust the current level (`i == current_end`), you're forced to take another jump -- increment the counter and advance the boundary.

**Real-world analogy:** Counting the minimum number of "hops" a frog needs across lily pads, where at each pad the frog knows the max hop distance, similar to finding shortest path length in an unweighted level graph.

**ASCII Visualization:**

```
nums = [2, 3, 1, 1, 4]
idx:    0  1  2  3  4

Jump 0 (from idx 0): current_end=0, farthest=0
 i=0: farthest = max(0, 0+2) = 2
 i==current_end(0) -> jump! jumps=1, current_end=2

Jump 1 (exploring within [1,2]):
 i=1: farthest = max(2, 1+3) = 4
 i=2: farthest = max(4, 2+1) = 4
 i==current_end(2) -> jump! jumps=2, current_end=4

current_end(4) >= n-1(4) -> stop. Minimum jumps = 2

Level view:
 Level0: {0}
 Level1: {1,2}      (reachable in 1 jump)
 Level2: {2,3,4}    (reachable in 2 jumps, includes index 4 -> done)
```

**Python Implementation:**

```python
def jump_game_ii(nums):
    """
    nums: List[int], last index guaranteed reachable
    Returns the minimum number of jumps to reach the last index.
    """
    n = len(nums)
    jumps = 0
    current_end = 0     # farthest index reachable using 'jumps' jumps so far
    farthest = 0         # farthest index reachable using 'jumps + 1' jumps

    for i in range(n - 1):         # no need to jump FROM the last index
        farthest = max(farthest, i + nums[i])

        if i == current_end:        # exhausted the current jump's range -> must jump again
            jumps += 1
            current_end = farthest

    return jumps
```

**Line-by-Line Explanation:**

- `current_end` represents the boundary of everything reachable with the jumps taken so far ("current BFS level").
- `farthest` continuously tracks the best possible next-level boundary while scanning within the current level.
- The loop runs to `n - 2` inclusive (`range(n-1)`), since jumping *from* the last index is never needed.
- When `i` catches up to `current_end`, the current level is fully explored -- commit to another jump and adopt `farthest` as the new boundary.

**Dry Run:** (see visualization; tabulated)

| i | farthest after update | i==current_end? | jumps after | current_end after |
|---|---|---|---|---|
| 0 | 2 | 0==0 yes | 1 | 2 |
| 1 | 4 | 1==2 no | 1 | 2 |
| 2 | 4 | 2==2 yes | 2 | 4 |
| 3 | 4 | 3==4 no | 2 | 4 |

Minimum jumps = **2**

**Correctness Intuition:** This is BFS on an implicit graph where edges go from index `i` to every index in `[i+1, i+nums[i]]`, except we avoid building the graph explicitly by tracking only level boundaries. Since BFS finds the shortest path in an unweighted graph, and this greedy frontier-expansion exactly simulates BFS levels, the jump count returned is provably minimal.

**Time Complexity:** O(n) -- single pass.
**Space Complexity:** O(1).

**Edge Cases:**
- Array of length 1 -> 0 jumps needed (already at the destination).
- Large single jump covering the whole array from index 0 -> answer is 1.
- Problem guarantees reachability; if not guaranteed, combine with the Jump Game feasibility check first.

**Common Mistakes:**
- Iterating through the full range `range(n)` instead of `range(n - 1)`, causing unnecessary/incorrect final jump counting.
- Confusing this with Jump Game I and returning a boolean instead of a count.
- Updating `current_end` inside the same iteration as `farthest` before finishing the check -- must check `i == current_end` using the **old** boundary first.

**Interview Tips:** Draw the "BFS levels" analogy explicitly on the whiteboard -- it's the cleanest way to justify why a greedy frontier expansion yields the *minimum* jump count, not just *a* valid count.

**Optimizations:** Already optimal at O(n) / O(1).

**Variations:** Weighted variants (cost per jump) typically require Dijkstra's algorithm or DP instead of this pure greedy approach.

**Practice Problems:** LeetCode 45 (Jump Game II).

**Summary:** Treat jumps as BFS levels; track current level's boundary and the farthest next-level boundary; increment jump count each time the scan exhausts the current level. O(n) time, O(1) space.

---

### 5.13 Candy Distribution

**Problem Statement:** `n` children stand in a line, each with a rating. Each child must get at least 1 candy, and any child with a higher rating than an immediate neighbor must get more candies than that neighbor. Find the minimum total candies needed.

**Why it exists:** Classic **two-pass prefix/suffix greedy** problem -- demonstrates that some greedy problems need two directional sweeps because a single left-to-right pass can't satisfy constraints from both neighbors simultaneously.

**Intuition:** Do one left-to-right pass ensuring the "greater than left neighbor" rule, then one right-to-left pass ensuring the "greater than right neighbor" rule, taking the max of both passes for each child.

**Real-world analogy:** Distributing bonuses in a row of employees by performance ranking, where anyone ranked higher than an immediate neighbor (on either side) must get a strictly bigger bonus than that neighbor.

**ASCII Visualization:**

```
ratings = [1, 0, 2]

Left-to-right pass (compare to LEFT neighbor):
 idx0: base 1                -> [1, _, _]
 idx1: 0 < 1 (not increasing) -> stays 1 -> [1, 1, _]
 idx2: 2 > 0 -> left[2]=left[1]+1=2 -> [1, 1, 2]

Right-to-left pass (compare to RIGHT neighbor), track separately:
 idx2: base 1                -> [_, _, 1]
 idx1: 0 < 2 -> not increasing rightwards -> stays 1 -> [_, 1, 1]
 idx0: 1 > 0 -> right[0]=right[1]+1=2 -> [2, 1, 1]

Final candies = elementwise max(left, right) = [max(1,2), max(1,1), max(2,1)]
             = [2, 1, 2]
Total = 5
```

**Python Implementation:**

```python
def candy(ratings):
    """
    ratings: List[int]
    Returns the minimum total candies satisfying all constraints.
    """
    n = len(ratings)
    if n == 0:
        return 0

    candies = [1] * n     # everyone starts with at least 1 candy

    # Left-to-right pass: satisfy "higher rating than LEFT neighbor" rule
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right-to-left pass: satisfy "higher rating than RIGHT neighbor" rule
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)
```

**Line-by-Line Explanation:**

- `candies = [1] * n`: baseline -- every child gets at least one candy.
- The left-to-right loop enforces: if `ratings[i] > ratings[i-1]`, this child needs strictly more candy than the left neighbor.
- The right-to-left loop enforces the mirrored constraint against the right neighbor, using `max()` to avoid **undoing** progress already made by the first pass.
- Summing the final array gives the minimum total satisfying both directional constraints simultaneously.

**Dry Run:** (see visualization; tabulated)

| Pass | i | Comparison | candies[i] |
|---|---|---|---|
| L->R | 1 | 0<1, no increase | 1 |
| L->R | 2 | 2>0, increase | 2 |
| R->L | 1 | 0<2, no increase | 1 |
| R->L | 0 | 1>0, increase | max(1, 1+1)=2 |

Final: `[2, 1, 2]`, total = **5**

**Correctness Intuition:** Each child's final candy count must simultaneously satisfy both the left-neighbor and right-neighbor constraints. Since these are independent monotonic conditions, computing the minimum needed for each direction separately and taking the elementwise maximum guarantees both are satisfied with the smallest possible numbers -- any smaller value at any index would violate at least one directional constraint.

**Time Complexity:** O(n) -- two linear passes.
**Space Complexity:** O(n) for the candies array (can be optimized to O(1) with a more complex single-pass slope-tracking technique).

**Edge Cases:**
- All ratings equal -> everyone gets exactly 1 candy (no strict inequalities triggered).
- Strictly increasing ratings -> candies form `1, 2, 3, ..., n`.
- Strictly decreasing ratings -> candies form `n, n-1, ..., 1`.
- Single child -> 1 candy.

**Common Mistakes:**
- Only doing a single left-to-right pass -- fails to satisfy right-neighbor constraints (classic bug).
- Overwriting instead of taking `max()` in the second pass, which can undo correct values from the first pass.
- Off-by-one errors in the reverse loop range.

**Interview Tips:** Explaining *why one pass is insufficient* (a peak in the middle needs to satisfy both sides independently) is the key insight interviewers probe for.

**Optimizations:** An O(1)-space single-pass solution exists using slope-counting (tracking ascending/descending run lengths), but the two-pass version is clearer and sufficient for most interviews.

**Variations:** "Trapping Rain Water" shares the same two-pass (or two-pointer) prefix/suffix maximum pattern conceptually.

**Practice Problems:** LeetCode 135 (Candy).

**Summary:** Two directional passes (left-to-right then right-to-left), taking the elementwise maximum, correctly satisfies both neighbor constraints with minimum total candy. O(n) time, O(n) space.

---

### 5.14 Lemonade Change

**Problem Statement:** Each customer pays with a $5, $10, or $20 bill for a $5 lemonade. Starting with no change, determine if every customer can be given correct change in order.

**Why it exists:** A simple, canonical example showing that greedy "always break the largest usable bill" is provably optimal because $20 bills are useless for giving change -- there's no reason to ever "save" a $10 over a $5 when both could work.

**Intuition:** Track counts of $5 and $10 bills only ($20s are never given as change here). For a $10 payment, give one $5. For a $20 payment, **prefer giving a $10 + $5** over three $5s whenever possible -- this conserves $5 bills, which are more versatile (usable for both future $10 and $20 change).

**Real-world analogy:** A cashier should always break the least flexible denomination first to preserve maximum flexibility (small bills) for future transactions.

**ASCII Visualization:**

```
bills = [5, 5, 5, 10, 20]

bill=5:  five+=1  -> five=1, ten=0
bill=5:  five+=1  -> five=2, ten=0
bill=5:  five+=1  -> five=3, ten=0
bill=10: need one 5 -> five=2, ten=1
bill=20: prefer (10+5) -> five=1, ten=0   (else three 5s: five=... not needed here)

All customers served -> True
```

**Python Implementation:**

```python
def lemonade_change(bills):
    """
    bills: List[int] payments in order
    Returns True if every customer can receive correct change.
    """
    five = ten = 0

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:  # bill == 20
            if ten > 0 and five > 0:        # prefer 10 + 5 (greedy: conserve $5 bills)
                ten -= 1
                five -= 1
            elif five >= 3:                  # fallback: three $5 bills
                five -= 3
            else:
                return False

    return True
```

**Line-by-Line Explanation:**

- `five`/`ten` track available bills of each denomination ($20s are collected but never used as change).
- For a $10 bill, exactly one $5 is required as change -- fail immediately if none available.
- For a $20 bill, **greedily prefer** breaking a $10 + $5 combo over three $5 bills, because $5 bills are strictly more useful for satisfying future $10 payments.
- If neither change combination is possible, the sequence fails.

**Dry Run:** (see visualization; tabulated)

| bill | Action | five after | ten after |
|---|---|---|---|
| 5 | five+=1 | 1 | 0 |
| 5 | five+=1 | 2 | 0 |
| 5 | five+=1 | 3 | 0 |
| 10 | five-=1, ten+=1 | 2 | 1 |
| 20 | prefer 10+5 | 1 | 0 |

Result: **True**

**Correctness Intuition (Exchange Argument):** Suppose an alternative strategy breaks three $5s for a $20 payment when a $10+$5 combo was also available. Since $5 bills can satisfy *any* future change requirement ($10 or $20) while $10 bills can only help with $20 payments, ending up with fewer $5s and more $10s (relatively) is never better than the reverse. Preferring to spend the less flexible $10 bill first is always at least as good, proving the greedy rule optimal.

**Time Complexity:** O(n) -- single pass.
**Space Complexity:** O(1) -- only two counters needed.

**Edge Cases:**
- First customer pays with $10 or $20 -> immediately impossible (no $5s yet), returns False.
- All customers pay with $5 -> trivially always True.
- Exactly enough $5s for a run of $20s requiring the three-$5 fallback -> must be handled correctly.

**Common Mistakes:**
- Giving three $5 bills for a $20 payment even when a $10+$5 combo is available -- technically valid change, but wastes flexible $5 bills and can cause **later** failures; must prefer $10+$5.
- Forgetting that $20 bills collected are never useful as change (no bill larger than $20 is ever needed here).

**Interview Tips:** This problem is a great "explain why greedy is safe" warm-up question -- the exchange argument is short and intuitive, good for demonstrating proof technique under time pressure.

**Optimizations:** Already optimal at O(n) / O(1).

**Variations:** General currency change-making with more denominations often requires DP (see Section 2.3's coin-change counterexample) unless the denomination system is "canonical."

**Practice Problems:** LeetCode 860 (Lemonade Change).

**Summary:** Track only $5 and $10 counts; for $20 payments, prefer breaking a $10+$5 combo over three $5s to conserve flexible currency. O(n) time, O(1) space.


---

### 5.15 Assign Cookies

**Problem Statement:** Each child `i` has a greed factor `g[i]` (minimum cookie size that satisfies them), and each cookie `j` has a size `s[j]`. Maximize the number of content children, where each cookie can satisfy at most one child.

**Why it exists:** The canonical **two-pointer greedy matching** problem -- pairs the smallest sufficient resource with the smallest demand.

**Intuition:** Sort both greed factors and cookie sizes. Use the smallest available cookie to try to satisfy the least-greedy unsatisfied child; if it's big enough, that's a match -- move both pointers; otherwise the cookie is too small for *anyone* remaining (since it's the smallest cookie and this is the least-greedy child), discard the cookie and try the next one.

**Real-world analogy:** Matching the smallest available shirt sizes to the smallest-fitting customers first, maximizing total satisfied customers with limited stock.

**ASCII Visualization:**

```
g = [1, 2, 3]   (sorted)
s = [1, 1]      (sorted)

i=0 (child g=1), j=0 (cookie s=1): 1>=1 -> match! i=1, j=1
i=1 (child g=2), j=1 (cookie s=1): 1>=2? No -> cookie too small, discard, j=2
j=2 -> no more cookies -> stop

Content children = 1
```

**Python Implementation:**

```python
def find_content_children(g, s):
    """
    g: List[int] greed factors
    s: List[int] cookie sizes
    Returns the maximum number of content children.
    """
    g.sort()
    s.sort()

    i = j = 0    # i -> children pointer, j -> cookies pointer
    content = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:      # cookie is big enough for this child
            content += 1
            i += 1            # this child is satisfied, move to next child
        j += 1                # this cookie is used up either way (matched or too small)

    return content
```

**Line-by-Line Explanation:**

- Sorting both arrays enables a linear two-pointer sweep instead of pairwise comparison (O(n*m)).
- `i` tracks the least-greedy unsatisfied child; `j` tracks the smallest unused cookie.
- If the current cookie satisfies the current child, count it and advance `i`.
- `j` always advances -- whether matched or discarded as "too small for anyone remaining," since children are sorted by increasing greed.

**Dry Run:** (see visualization; tabulated)

| i | j | g[i] | s[j] | s[j]>=g[i]? | content | Next |
|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | yes | 1 | i=1, j=1 |
| 1 | 1 | 2 | 1 | no | 1 | j=2 |
| 1 | 2 | -- | -- | out of cookies | 1 | stop |

Result: **1**

**Correctness Intuition (Exchange Argument):** If the smallest cookie can satisfy the least-greedy child, using it there is always safe -- any larger, more-greedy child that *could* also be satisfied by this cookie could equally well be satisfied by a larger cookie later (or not at all), so "wasting" a small cookie on a more-greedy child never helps and might hurt. If the smallest cookie *cannot* satisfy even the least-greedy child, it cannot satisfy anyone (all other children are equally or more greedy), so discarding it is forced and safe.

**Time Complexity:** O(n log n + m log m) for sorting both arrays; O(n + m) for the sweep. **Total: O(n log n + m log m)**.
**Space Complexity:** O(1) extra.

**Edge Cases:**
- No cookies -> 0 content children.
- No children -> 0 (trivially).
- Cookie sizes all smaller than every child's greed -> 0 matches.
- More cookies than children -> extra cookies simply go unused.

**Common Mistakes:**
- Sorting only one of the two arrays.
- Trying to match the *largest* cookie to the *most* greedy child first -- also technically works for counting maximum matches (a symmetric greedy), but combining it incorrectly with the smallest-first logic causes bugs; pick one consistent direction.
- Off-by-one pointer advancement (forgetting to advance `j` on a mismatch).

**Interview Tips:** This is often used as a warm-up/easy problem -- interviewers check if you jump straight to sorting + two-pointer instead of overcomplicating with nested loops.

**Optimizations:** Already optimal.

**Variations:** Boat to Save People (Section 5.16) uses a very similar two-pointer greedy but pairs from *opposite* ends of a single sorted array.

**Practice Problems:** LeetCode 455 (Assign Cookies).

**Summary:** Sort both arrays; two-pointer sweep matching the smallest sufficient cookie to the least-greedy unsatisfied child. O(n log n).

---

### 5.16 Boat to Save People

**Problem Statement:** Given people's weights and a boat weight `limit` that carries at most 2 people per trip, find the minimum number of boat trips to carry everyone across.

**Why it exists:** Demonstrates two-pointer greedy pairing from **opposite ends of a single sorted array** -- pairing the heaviest remaining person with the lightest remaining person whenever possible.

**Intuition:** Sort weights. Always try to pair the heaviest unassigned person with the lightest unassigned person. If they fit together, both go in one trip; if not, the heaviest person must go alone (since even the lightest available partner doesn't fit, nobody else would either).

**Real-world analogy:** A ferry operator pairing the heaviest and lightest waiting passengers together whenever weight limits allow, to minimize total ferry trips.

**ASCII Visualization:**

```
people = [1, 2, 3, 5], limit = 5   (sorted)

left=0 (1), right=3 (5): 1+5=6 > 5 -> heaviest goes alone -> trips=1, right=2
left=0 (1), right=2 (3): 1+3=4 <= 5 -> pair! trips=2, left=1, right=1
left=1 (2), right=1 (2): same index -> single person left -> trips=3

Total trips = 3
```

**Python Implementation:**

```python
def num_rescue_boats(people, limit):
    """
    people: List[int] weights
    limit: int max weight per boat (max 2 people)
    Returns the minimum number of boat trips.
    """
    people.sort()
    left, right = 0, len(people) - 1
    trips = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1              # lightest person successfully paired
        right -= 1                  # heaviest person always leaves (paired or alone)
        trips += 1

    return trips
```

**Line-by-Line Explanation:**

- Sorting enables pairing extremes efficiently.
- `left` points to the lightest unassigned person, `right` to the heaviest.
- If they fit together, advance `left` (that lighter person is now assigned) as well as decrementing `right`.
- If they don't fit, only `right` (the heaviest) is assigned -- alone in this trip.
- Every iteration represents exactly one trip, regardless of whether it carries 1 or 2 people.

**Dry Run:** (see visualization; tabulated)

| left | right | people[left] | people[right] | Sum | <=limit? | Action | trips |
|---|---|---|---|---|---|---|---|
| 0 | 3 | 1 | 5 | 6 | No | heaviest alone | 1 |
| 0 | 2 | 1 | 3 | 4 | Yes | pair | 2 |
| 1 | 1 | 2 | 2 | -- | left==right, single | alone | 3 |

Result: **3**

**Correctness Intuition (Exchange Argument):** The heaviest person must go in *some* trip, either alone or paired with exactly one other person. Since they take up the most capacity, pairing them with the **lightest** available person gives the best chance of fitting -- if even the lightest person doesn't fit with them, no one else will either, forcing a solo trip. This greedy pairing never wastes capacity that a smarter pairing could have used better, which is provable via a standard exchange argument on any two swapped pairings.

**Time Complexity:** O(n log n) for sorting; O(n) for the two-pointer sweep. **Total: O(n log n)**.
**Space Complexity:** O(1) extra.

**Edge Cases:**
- Single person -> 1 trip.
- Every pair fits -> trips = ceil(n/2).
- No pair fits (everyone near the weight limit alone) -> trips = n.

**Common Mistakes:**
- Pairing lightest-with-lightest or heaviest-with-heaviest instead of lightest-with-heaviest -- suboptimal.
- Forgetting to decrement `right` even when a solo trip occurs -- causes infinite loops or wrong counts.

**Interview Tips:** Draw the two-pointer convergence explicitly -- interviewers want to see you recognize "extremes-pairing" as a distinct sub-pattern from "consecutive-pairing" (used in Assign Cookies).

**Optimizations:** Already optimal.

**Variations:** Generalizations with boat capacity > 2 people typically require different techniques (often not pure two-pointer greedy).

**Practice Problems:** LeetCode 881 (Boats to Save People).

**Summary:** Sort weights; two-pointer greedy pairing lightest with heaviest whenever they fit, otherwise the heaviest goes alone. O(n log n).

---

### 5.17 Maximum Units on a Truck

**Problem Statement:** Given boxes described as `[numberOfBoxes, unitsPerBox]` and a truck with a maximum box capacity, maximize the total number of units that can be loaded.

**Why it exists:** A discrete (box-level, not fractional) variant of the value-density greedy idea from Fractional Knapsack -- but since whole boxes are atomic and interchangeable within a type, greedy remains valid (unlike 0/1 Knapsack).

**Intuition:** Sort box types by `unitsPerBox` descending. Load as many boxes as possible from the highest-density type first, then the next, until the truck's box capacity is exhausted.

**Real-world analogy:** A logistics manager loading a truck with limited box slots, prioritizing box types that pack the most value (units) per box.

**ASCII Visualization:**

```
boxTypes = [[5,10],[2,5],[4,7]], truckSize = 10

Sort by unitsPerBox desc: [5,10] [4,7] [2,5]

Load [5,10]: take min(5,10)=5 boxes -> units += 5*10=50, truckSize=5
Load [4,7]:  take min(4,5)=4 boxes  -> units += 4*7=28,  truckSize=1
Load [2,5]:  take min(2,1)=1 box    -> units += 1*5=5,   truckSize=0

Total units = 50+28+5 = 83
```

**Python Implementation:**

```python
def maximum_units(box_types, truck_size):
    """
    box_types: List[List[int]] each [numberOfBoxes, unitsPerBox]
    truck_size: int max number of boxes the truck can carry
    Returns the maximum total units loadable.
    """
    box_types.sort(key=lambda x: x[1], reverse=True)   # sort by unitsPerBox desc

    total_units = 0
    remaining = truck_size

    for count, units_per_box in box_types:
        if remaining <= 0:
            break
        take = min(count, remaining)
        total_units += take * units_per_box
        remaining -= take

    return total_units
```

**Line-by-Line Explanation:**

- Sorting by `unitsPerBox` descending ensures we always consider the most "valuable" box type first -- the greedy metric.
- `take = min(count, remaining)`: load as many boxes of this type as available, capped by remaining truck capacity.
- Accumulate units and decrement remaining capacity; stop early once the truck is full.

**Dry Run:** (see visualization; tabulated)

| Box type | units/box | remaining before | take | units added | remaining after |
|---|---|---|---|---|---|
| [5,10] | 10 | 10 | 5 | 50 | 5 |
| [4,7] | 7 | 5 | 4 | 28 | 1 |
| [2,5] | 5 | 1 | 1 | 5 | 0 |

Total = **83**

**Correctness Intuition (Exchange Argument):** Since box slots are interchangeable and each box of a given type contributes identical units, swapping a lower-density box for a higher-density one (whenever available) strictly increases or maintains total units. This is structurally identical to Fractional Knapsack's proof, except here "fractions" are whole boxes -- and since whole boxes of the same type are perfectly substitutable, no indivisibility problem arises (unlike 0/1 Knapsack across *different* item types).

**Time Complexity:** O(n log n) for sorting `n` box types; O(n) for the greedy fill. **Total: O(n log n)**.
**Space Complexity:** O(1) extra.

**Edge Cases:**
- `truck_size` larger than total available boxes -> load everything.
- All box types have identical `unitsPerBox` -> order doesn't matter, same total.
- `truck_size == 0` -> 0 units.

**Common Mistakes:**
- Sorting by `numberOfBoxes` instead of `unitsPerBox` -- wrong metric entirely.
- Forgetting the `min(count, remaining)` cap, over-counting boxes.

**Interview Tips:** Contrast explicitly with 0/1 Knapsack in your answer -- explain *why* this discrete problem is still greedy-safe (homogeneous, substitutable units within a type) while 0/1 Knapsack (heterogeneous, non-substitutable individual items) is not.

**Optimizations:** Already optimal.

**Variations:** Multi-constraint loading (weight AND volume limits simultaneously) generally breaks pure greedy and needs DP or LP relaxation.

**Practice Problems:** LeetCode 1710 (Maximum Units on a Truck).

**Summary:** Sort box types by units-per-box descending; greedily fill truck capacity from the top. O(n log n), a discrete cousin of Fractional Knapsack.

---

### 5.18 Partition Labels

**Problem Statement:** Given a string, partition it into as many parts as possible such that each letter appears in at most one part, and return the sizes of these parts.

**Why it exists:** Demonstrates a **"last occurrence" prefix-greedy** pattern -- track the farthest boundary a partition must extend to based on where its characters last appear.

**Intuition:** Precompute the last occurrence index of every character. Scan left to right, extending the current partition's `end` boundary to the last occurrence of every character seen so far. When the scan pointer catches up to `end`, the partition is complete and cannot be shrunk further without splitting a repeated character across two parts.

**Real-world analogy:** Splitting a rope into the maximum number of segments such that no colored bead's two ends fall into different segments -- extend each candidate cut point only as far as the rightmost occurrence of every bead color seen so far.

**ASCII Visualization:**

```
s = "ababcbacadefegdehijhklij"

last occurrence: a->8, b->5, c->7, d->14, e->15, f->11, g->13, h->19, i->22, j->23, k->20, l->21

i=0 'a': end=max(0,8)=8
i=1 'b': end=max(8,5)=8
i=2 'a': end=max(8,8)=8
...
i=8 (== end) -> partition closes! size=9 ("ababcbaca")

Continue scanning from i=9 with a fresh end...
Eventually partitions: [9, 7, 8]  (sizes)
```

**Python Implementation:**

```python
def partition_labels(s):
    """
    s: str
    Returns List[int] sizes of each partition.
    """
    last = {ch: i for i, ch in enumerate(s)}   # last occurrence index of each char

    sizes = []
    start = end = 0

    for i, ch in enumerate(s):
        end = max(end, last[ch])    # extend partition boundary as needed

        if i == end:                 # scan pointer caught up -> partition closes here
            sizes.append(end - start + 1)
            start = i + 1

    return sizes
```

**Line-by-Line Explanation:**

- `last` dict maps each character to the rightmost index it appears at (overwritten each time, so the final value is the true last occurrence) -- built in one O(n) pass.
- `end` tracks the current partition's required right boundary, extended greedily as new characters are encountered.
- When the scan index `i` equals `end`, every character seen in `[start, i]` has its last occurrence within this range -- the partition is safe to close.
- Record the size and reset `start` for the next partition.

**Dry Run (shortened for `s = "abac"`, last: a->2, b->1, c->3):**

| i | ch | last[ch] | end after | i==end? | Action |
|---|---|---|---|---|---|
| 0 | a | 2 | 2 | no | -- |
| 1 | b | 1 | 2 | no | -- |
| 2 | a | 2 | 2 | yes | close partition size=3 ("aba") |
| 3 | c | 3 | 3 | yes | close partition size=1 ("c") |

Result: `[3, 1]`

**Correctness Intuition:** A partition boundary can only be placed at index `i` if no character within `[start, i]` reoccurs later beyond `i` -- which is exactly what `end = max(end, last[ch])` tracks. The moment `i == end`, we have found the **earliest possible** valid cut, which is also the greedy choice that maximizes the number of partitions (cutting as early/often as validly possible).

**Time Complexity:** O(n) -- one pass to build `last`, one pass to partition.
**Space Complexity:** O(k) where `k` is the alphabet size (O(1) for fixed lowercase English letters).

**Edge Cases:**
- Single character string -> one partition of size 1.
- All characters distinct -> `n` partitions, each of size 1.
- All characters identical -> one partition of size `n`.

**Common Mistakes:**
- Forgetting to reset `start` after closing a partition.
- Using the *first* occurrence instead of the *last* occurrence -- inverts the logic entirely.

**Interview Tips:** This pattern ("extend boundary to last occurrence, cut when scan catches up") is reusable for many "minimize/maximize splits under a constraint" problems -- name it explicitly if you've seen it before.

**Optimizations:** Already optimal at O(n).

**Variations:** Merge Intervals uses a structurally similar "extend boundary, cut when no overlap" idea but on explicit interval inputs rather than derived last-occurrence indices.

**Practice Problems:** LeetCode 763 (Partition Labels).

**Summary:** Track each character's last occurrence; greedily extend the current partition's boundary; close the partition exactly when the scan catches up. O(n) time.

---

### 5.19 Valid Parenthesis String

**Problem Statement:** Given a string containing `'('`, `')'`, and `'*'` (which can represent `'('`, `')'`, or an empty string), determine if the string can be interpreted as a valid parenthesis sequence.

**Why it exists:** Demonstrates a **range-tracking greedy** pattern -- instead of tracking one balance counter, track a *range* of possible balances simultaneously to handle the wildcard's ambiguity without exponential branching.

**Intuition:** Track `low` (minimum possible open-paren balance, treating every `*` as `)` or empty when it helps minimize) and `high` (maximum possible balance, treating every `*` as `(` when it helps maximize). If `high` ever goes negative, the string is unsalvageable. At the end, the string is valid if `low` can reach exactly 0 (clamping `low` at 0 throughout, since balance can never be treated as negative).

**Real-world analogy:** Tracking the best-case and worst-case number of open commitments (like unclosed loan guarantees) when some transactions are ambiguous (`*`) and could go either way -- valid only if some consistent interpretation nets to exactly zero open commitments at the end.

**ASCII Visualization:**

```
s = "(*))"

char '(' : low=1,  high=1
char '*' : low=0 (treat as ')'), high=2 (treat as '(')
char ')' : low=-1->clamp 0, high=1
char ')' : low=-1->clamp 0, high=0

End: low==0 -> VALID  ✅

Range view:
 '('  low=1  high=1     [1,1]
 '*'  low=0  high=2     [0,2]
 ')'  low=0  high=1     [0,1]
 ')'  low=0  high=0     [0,0]  <- 0 is within final range -> valid
```

**Python Implementation:**

```python
def check_valid_string(s):
    """
    s: str containing '(', ')', '*'
    Returns True if s can be a valid parenthesis string.
    """
    low = high = 0   # low = min possible balance, high = max possible balance

    for ch in s:
        if ch == '(':
            low += 1
            high += 1
        elif ch == ')':
            low -= 1
            high -= 1
        else:  # '*'
            low -= 1      # treat as ')'
            high += 1     # treat as '('

        if high < 0:       # even the BEST interpretation is unbalanced -> fail fast
            return False

        low = max(low, 0)  # balance can never validly be negative; clamp

    return low == 0
```

**Line-by-Line Explanation:**

- `low`/`high` represent the achievable range of open-parenthesis counts considering all valid interpretations of `*` seen so far.
- `'('` increases both bounds (forced open); `')'` decreases both (forced close); `'*'` widens the range (could be either, or empty when decreasing `low`).
- `high < 0` means every interpretation so far is already invalid -- fail immediately (pruning).
- `low = max(low, 0)`: balance is never allowed to be negative in *any* valid interpretation, so clamp the lower bound.
- Final check `low == 0`: some valid interpretation achieves exact balance zero if and only if 0 lies within the final `[low, high]` range and is reachable -- clamping ensures `low` correctly reflects this.

**Dry Run:** (see visualization; tabulated)

| ch | low before | high before | low after (pre-clamp) | high after | high<0? | low after clamp |
|---|---|---|---|---|---|---|
| ( | 0 | 0 | 1 | 1 | no | 1 |
| * | 1 | 1 | 0 | 2 | no | 0 |
| ) | 0 | 2 | -1 | 1 | no | 0 |
| ) | 0 | 1 | -1 | 0 | no | 0 |

Final `low == 0` -> **True**

**Correctness Intuition:** `[low, high]` always represents a *contiguous* achievable range of balances (provable by induction, since each operation shifts or widens the range contiguously). Clamping `low` at 0 removes interpretations that are already invalid (negative balance at some point) without losing any valid ones. If `high` ever dips below 0, no interpretation remains valid. At the end, the string is valid exactly when 0 is achievable, i.e., `low == 0` (since `low` is clamped and the range is contiguous, `low == 0` implies 0 is in range).

**Time Complexity:** O(n) -- single pass.
**Space Complexity:** O(1) -- two counters.

**Edge Cases:**
- Empty string -> valid (trivially balanced).
- All `*` -> always valid (can always interpret as empty).
- String starting with `)` and no preceding `(` or `*` -> `high` goes negative immediately -> invalid.

**Common Mistakes:**
- Trying to track a single balance counter and branching exponentially on `*` -- correct but exponential; the range-tracking trick avoids this entirely.
- Forgetting to clamp `low` at 0 -- allows nonsensical "negative balance" interpretations to pollute the final check.

**Interview Tips:** This is a great problem to demonstrate that greedy doesn't always mean "track one number" -- sometimes it means "track a provably contiguous range of possibilities" cheaply, avoiding exponential blowup.

**Optimizations:** Already optimal at O(n) / O(1); alternative O(n) stack-based solutions (two stacks for unmatched `(` and `*` indices) also exist but use more space.

**Variations:** Standard "Valid Parentheses" (no wildcard) is solved trivially with a single counter or stack.

**Practice Problems:** LeetCode 678 (Valid Parenthesis String).

**Summary:** Track a `[low, high]` range of achievable open-paren balances; clamp `low` at 0; fail fast if `high` goes negative; valid iff `low == 0` at the end. O(n) time, O(1) space.


---

### 5.20 Queue Reconstruction by Height

**Problem Statement:** Given a list of people `[height, k]` where `k` is the number of people **in front of this person who have a height greater than or equal to** their own, reconstruct the queue order.

**Why it exists:** A classic "insertion greedy" pattern -- decide a processing order where each insertion decision is *locally final* because of a clever sort choice that neutralizes future interference.

**Intuition:** Sort people by height descending (ties broken by `k` ascending). Insert each person into the result list at index `k`. Because taller people are placed first, inserting a shorter person later at position `k` never disturbs the relative `k` counts of already-placed taller people (shorter people don't count toward *their* "taller-or-equal in front" requirement).

**Real-world analogy:** Lining up people for a photo where each person specifies how many equally-tall-or-taller people must stand in front of them -- placing tallest-first and inserting each by their required count naturally satisfies everyone.

**ASCII Visualization:**

```
people = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

Sort by height desc, k asc:
 [7,0] [7,1] [6,1] [5,0] [5,2] [4,4]

Insert at index k into growing result list:
 insert [7,0] at 0        -> [7,0]
 insert [7,1] at 1        -> [7,0],[7,1]
 insert [6,1] at 1        -> [7,0],[6,1],[7,1]
 insert [5,0] at 0        -> [5,0],[7,0],[6,1],[7,1]
 insert [5,2] at 2        -> [5,0],[7,0],[5,2],[6,1],[7,1]
 insert [4,4] at 4        -> [5,0],[7,0],[5,2],[6,1],[4,4],[7,1]

Final queue: [5,0][7,0][5,2][6,1][4,4][7,1]
```

**Python Implementation:**

```python
def reconstruct_queue(people):
    """
    people: List[List[int]] each [height, k]
    Returns the reconstructed queue order.
    """
    # Sort by height descending; for ties, by k ascending
    people.sort(key=lambda p: (-p[0], p[1]))

    result = []
    for height, k in people:
        result.insert(k, [height, k])   # insert at the required position

    return result
```

**Line-by-Line Explanation:**

- Sorting by height descending processes the tallest people first -- they are the ones whose "taller-or-equal in front" count matters for everyone shorter.
- Tie-break by `k` ascending ensures equal-height people are placed in a consistent, valid relative order.
- `result.insert(k, ...)`: placing this person exactly at index `k` guarantees exactly `k` people (all taller-or-equal, since shorter people inserted later don't affect this count) end up in front of them.

**Dry Run:** (see visualization above; tabulated)

| Person [h,k] | Insert index | Result after |
|---|---|---|
| [7,0] | 0 | [[7,0]] |
| [7,1] | 1 | [[7,0],[7,1]] |
| [6,1] | 1 | [[7,0],[6,1],[7,1]] |
| [5,0] | 0 | [[5,0],[7,0],[6,1],[7,1]] |
| [5,2] | 2 | [[5,0],[7,0],[5,2],[6,1],[7,1]] |
| [4,4] | 4 | [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] |

**Correctness Intuition:** Because we insert strictly from tallest to shortest, every already-placed person is taller-or-equal to the person being inserted now. Inserting at index `k` therefore places exactly `k` taller-or-equal people before them (all previously placed people qualify), satisfying their constraint permanently -- future insertions of shorter people can only ever appear *after* their position or shift their index without affecting the *count* of taller-or-equal people in front (since shorter people never count toward this person's requirement).

**Time Complexity:** O(n log n) for sorting + O(n^2) worst case for `n` list insertions (each insertion is O(n)) = **O(n^2)** overall. Can be improved to O(n log n) using a Binary Indexed Tree / order-statistics structure.
**Space Complexity:** O(n).

**Edge Cases:**
- All people have `k = 0` -> any height order works as long as sorted appropriately; algorithm still produces a valid arrangement.
- Duplicate heights -> tie-break by `k` ascending is essential for correctness.
- Single person -> trivially `[[height, 0]]`.

**Common Mistakes:**
- Sorting by height ascending instead of descending -- completely breaks the insertion logic.
- Forgetting the secondary sort key (`k` ascending) for equal heights.
- Using `append` instead of `insert(k, ...)`.

**Interview Tips:** Explain *why* processing tallest-first "freezes" the taller people's constraints permanently -- this insight is the crux of the correctness proof and is what interviewers want to hear.

**Optimizations:** Replace list insertion with a Fenwick Tree (Binary Indexed Tree) over available "slots" to find the k-th empty slot in O(log n), reducing total complexity to O(n log n).

**Variations:** Similar "insert by rank" greedy patterns appear in some scheduling and ranking reconstruction problems.

**Practice Problems:** LeetCode 406 (Queue Reconstruction by Height).

**Summary:** Sort tallest-first (ties by k ascending); insert each person at index k in the growing result list. O(n^2) simple version, O(n log n) with a Fenwick Tree.

---

### 5.21 Minimum Arrows to Burst Balloons

**Problem Statement:** Balloons are represented as horizontal diameter intervals `[x_start, x_end]`. An arrow shot at position `x` bursts every balloon whose interval contains `x`. Find the minimum number of arrows to burst all balloons.

**Why it exists:** A close cousin of Activity Selection / Non-overlapping Intervals, but the "overlap" condition is inclusive (touching endpoints count as overlapping) since a single vertical arrow can hit balloons that merely touch.

**Intuition:** Sort balloons by end coordinate. Shoot an arrow at the end of the first balloon; this arrow also bursts every other balloon whose interval overlaps this point. Move to the next balloon not yet burst and repeat.

**Real-world analogy:** Popping balloons at a carnival stall using vertical darts -- one throw at the right x-coordinate can pop several overlapping balloons at once; the goal is minimum throws.

**ASCII Visualization:**

```
Balloons: [10,16] [2,8] [1,6] [7,12]

Sorted by end: [1,6] [2,8] [7,12] [10,16]

Shoot arrow at x=6 (end of [1,6]):
  [1,6] bursts (6 in [1,6])
  [2,8] bursts (6 in [2,8])
  [7,12]? 6 not in [7,12] -> survives
  arrows=1

Next unburst balloon: [7,12]. Shoot arrow at x=12:
  [7,12] bursts
  [10,16]? 12 in [10,16] -> bursts too!
  arrows=2

Total arrows = 2
```

**Python Implementation:**

```python
def find_min_arrow_shots(points):
    """
    points: List[List[int]] each [x_start, x_end]
    Returns the minimum number of arrows needed.
    """
    if not points:
        return 0

    points.sort(key=lambda p: p[1])   # sort by end coordinate
    arrows = 1
    arrow_pos = points[0][1]           # shoot the first arrow at the first balloon's end

    for start, end in points[1:]:
        if start > arrow_pos:          # this balloon is NOT hit by the current arrow
            arrows += 1
            arrow_pos = end             # shoot a new arrow at this balloon's end
        # else: balloon is hit by the existing arrow, no new arrow needed

    return arrows
```

**Line-by-Line Explanation:**

- Sorting by end coordinate lets us always consider the balloon that forces the earliest possible arrow placement.
- `arrow_pos` tracks where the most recent arrow was shot.
- If a balloon's `start` is beyond the current arrow's position, it cannot be hit by that arrow -- a new arrow is required, placed at this balloon's `end` (the greedy choice, to potentially hit the most future balloons too).
- If `start <= arrow_pos`, the current arrow already bursts this balloon (since it's sorted by end, and this balloon's start being `<= arrow_pos <= this balloon's end` means the arrow point lies within `[start, end]`).

**Dry Run:** (see visualization; tabulated)

| Balloon | start | arrow_pos before | start>arrow_pos? | Action | arrows | arrow_pos after |
|---|---|---|---|---|---|---|
| [1,6] | 1 | -- | init | first arrow at 6 | 1 | 6 |
| [2,8] | 2 | 6 | 2>6 no | hit by existing arrow | 1 | 6 |
| [7,12] | 7 | 6 | 7>6 yes | new arrow at 12 | 2 | 12 |
| [10,16] | 10 | 12 | 10>12 no | hit by existing arrow | 2 | 12 |

Result: **2**

**Correctness Intuition (Exchange Argument):** Placing the arrow at the earliest possible "end" coordinate among unburst balloons maximizes the chance of also bursting subsequent overlapping balloons (since any later arrow position could only cover a subset of what the earliest-end position covers, among balloons sorted by end). Any optimal solution can be transformed to match this greedy arrow placement without increasing the arrow count, by shifting arrows to the earliest valid "end" position they could occupy.

**Time Complexity:** O(n log n) for sorting; O(n) for the scan. **Total: O(n log n)**.
**Space Complexity:** O(1) extra.

**Edge Cases:**
- No balloons -> 0 arrows.
- All balloons overlap at a common point -> 1 arrow.
- No balloons overlap at all -> arrows = number of balloons.
- Touching balloons (`[1,2]` and `[2,3]`) -- **do** count as burstable by a single arrow at x=2, since `2` belongs to both intervals (inclusive endpoints).

**Common Mistakes:**
- Sorting by start instead of end.
- Using `>=` instead of `>` in the overlap check (or vice versa) -- easy to invert the inclusive/exclusive boundary logic; this differs subtly from Non-overlapping Intervals (Section 5.8), which uses strict "no shared point" semantics, whereas this problem treats touching points as overlapping.

**Interview Tips:** Explicitly contrast this with Non-overlapping Intervals -- the code looks almost identical, but the boundary condition (`>` vs `>=`) flips because "touching" balloons *can* be popped together, unlike touching activities which may or may not be considered overlapping depending on convention.

**Optimizations:** Already optimal.

**Variations:** Minimum Platforms / Meeting Rooms II solve a structurally related "count simultaneous overlaps" problem, though the objective (minimum resources vs. minimum arrows) differs.

**Practice Problems:** LeetCode 452 (Minimum Number of Arrows to Burst Balloons).

**Summary:** Sort balloons by end coordinate; greedily shoot each new arrow at the end of the first unburst balloon, which bursts every balloon overlapping that point. O(n log n).

---

### 5.22 Remove Duplicate Letters

**Problem Statement:** Given a string, remove duplicate letters so each letter appears exactly once, keeping the result's **smallest lexicographical order** among all valid results (result must still be a subsequence using each distinct letter exactly once, preserving relative order availability).

**Why it exists:** Demonstrates a **monotonic stack greedy** pattern combined with "last occurrence" lookahead -- widely reused in "smallest subsequence" style problems.

**Intuition:** Use a stack. For each character, while the stack's top is greater than the current character, **and** that top character still occurs later in the string (so removing it now doesn't lose it forever), pop it. Push the current character if it's not already in the stack.

**Real-world analogy:** Building the smallest possible password using each required character exactly once, where you can "undo" a recent larger character choice only if that same character will reappear later, giving you another chance to use it.

**ASCII Visualization:**

```
s = "cbacdcbc"

last occurrence: c->7, b->6, a->2, d->4

Process 'c': stack=[] -> push -> stack=['c']
Process 'b': top 'c' > 'b' and c occurs later (idx7>1)? yes -> pop 'c'
             stack=[] -> push 'b' -> stack=['b']
Process 'a': top 'b' > 'a' and b occurs later (idx6>2)? yes -> pop 'b'
             stack=[] -> push 'a' -> stack=['a']
Process 'c': 'c' not in stack -> push -> stack=['a','c']
Process 'd': top 'c' < 'd' -> no pop -> push -> stack=['a','c','d']
Process 'c': already in stack -> skip
Process 'b': top 'd' > 'b', but d occurs later? last[d]=4, current idx=6, 4<6 -> NO, don't pop
             push 'b' -> stack=['a','c','d','b']
Process 'c': already in stack -> skip

Result: "acdb"
```

**Python Implementation:**

```python
def remove_duplicate_letters(s):
    """
    s: str
    Returns the lexicographically smallest subsequence containing
    each distinct letter of s exactly once.
    """
    last_occurrence = {ch: i for i, ch in enumerate(s)}
    stack = []
    in_stack = set()

    for i, ch in enumerate(s):
        if ch in in_stack:
            continue    # this letter is already placed; skip duplicates

        # Pop while: top is lexicographically larger AND will reappear later
        while stack and stack[-1] > ch and last_occurrence[stack[-1]] > i:
            removed = stack.pop()
            in_stack.remove(removed)

        stack.append(ch)
        in_stack.add(ch)

    return "".join(stack)
```

**Line-by-Line Explanation:**

- `last_occurrence` precomputes where each character last appears -- tells us whether it's "safe" to remove a character now (it'll come back later).
- `in_stack` set gives O(1) duplicate-skip checks.
- The `while` loop is the greedy core: pop a larger character off the stack **only if** doing so doesn't lose it forever (it reoccurs after the current index).
- After popping as much as validly possible, push the current character (if not already present).

**Dry Run:** (see visualization above; tabulated)

| i | ch | Stack before | Pop condition checks | Stack after |
|---|---|---|---|---|
| 0 | c | [] | -- | [c] |
| 1 | b | [c] | c>b and last[c]=7>1 -> pop | [b] |
| 2 | a | [b] | b>a and last[b]=6>2 -> pop | [a] |
| 3 | c | [a] | a<c, no pop; c not in stack | [a,c] |
| 4 | d | [a,c] | c<d, no pop | [a,c,d] |
| 5 | c | [a,c,d] | c already in stack -> skip | [a,c,d] |
| 6 | b | [a,c,d] | d>b but last[d]=4<=6 -> no pop | [a,c,d,b] |
| 7 | c | [a,c,d,b] | c already in stack -> skip | [a,c,d,b] |

Result: **"acdb"**

**Correctness Intuition (Exchange Argument):** Placing a smaller character earlier always yields a lexicographically smaller (or equal) result, **provided** we don't permanently lose access to a character we pop. The `last_occurrence` check exactly guards this: we only pop a character if it's guaranteed to reappear later, meaning we can still include it afterward without violating the "each letter exactly once" constraint. This greedy pop-and-replace strategy is proven optimal by induction on string position, since at each step it makes the lexicographically best decision that remains globally feasible.

**Time Complexity:** O(n) -- each character is pushed and popped at most once (amortized), plus O(1) dict/set lookups.
**Space Complexity:** O(k) for the stack/set, where `k` is the number of distinct characters (O(26) for lowercase English letters).

**Edge Cases:**
- All characters identical -> result is a single character.
- Already in sorted order with no repeats -> result equals the input.
- Single character string -> trivially itself.

**Common Mistakes:**
- Forgetting the `last_occurrence[stack[-1]] > i` guard -- pops characters that never reappear, losing them permanently and producing an invalid (incomplete) result.
- Not skipping already-placed characters, causing duplicates in the output.

**Interview Tips:** This is a strong "monotonic stack + greedy" showcase problem -- explicitly name the pattern ("monotonic stack with a reversibility check via last-occurrence") to signal pattern recognition depth.

**Optimizations:** Already optimal at O(n).

**Variations:** "Smallest Subsequence of Distinct Characters" is the exact same problem under a different name; "Remove K Digits" (make smallest number by removing k digits) uses an almost identical monotonic stack greedy without the reversibility/reappearance constraint.

**Practice Problems:** LeetCode 316 (Remove Duplicate Letters), LeetCode 1081 (same as 316).

**Summary:** Monotonic stack; pop a larger top character only if it reoccurs later in the string; skip already-placed duplicates. O(n) time, O(1)-ish space (bounded alphabet).

---

### 5.23 Reorganize String

**Problem Statement:** Given a string, rearrange its characters so that no two adjacent characters are the same. Return any valid rearrangement, or an empty string if impossible.

**Why it exists:** Canonical **frequency-greedy with a max-heap** pattern -- always place the currently most frequent remaining character, as long as it's not immediately repeating the previous placement.

**Intuition:** Count character frequencies. Repeatedly take the most frequent remaining character and place it, unless it's the same as the character just placed -- in which case place the *second* most frequent instead, and hold the first one back for the next slot. A max-heap efficiently gives "current most frequent" in O(log k) per step.

**Real-world analogy:** Scheduling the most-in-demand ad slots across a broadcast day such that the same advertiser never airs twice in a row -- always slot in the most in-demand advertiser who *isn't* the one who just aired.

**ASCII Visualization:**

```
s = "aab"

freq: a=2, b=1
max-heap by freq: [(-2,'a'), (-1,'b')]

Step 1: pop (-2,'a') -> place 'a'. prev=('a', now count=1)
        push prev back into heap since count>0 -> heap=[(-1,'a'),(-1,'b')]
Step 2: pop (-1,'a')? Wait -- can't place 'a' right after 'a' if it's the SAME
        as prev; use held-back logic: pop (-1,'b') (since 'a' is prev) -> place 'b'
        push back prev('a',count=1) -> heap=[(-1,'a')]
Step 3: pop (-1,'a') -> place 'a' (prev was 'b', different, OK)

Result: "aba"
```

**Python Implementation:**

```python
import heapq
from collections import Counter

def reorganize_string(s):
    """
    s: str
    Returns a rearrangement with no two adjacent identical characters,
    or "" if impossible.
    """
    freq = Counter(s)
    max_heap = [(-count, ch) for ch, count in freq.items()]
    heapq.heapify(max_heap)

    result = []
    prev_count, prev_char = 0, ''   # "held back" character from the previous step

    while max_heap:
        count, ch = heapq.heappop(max_heap)
        result.append(ch)

        # Re-insert the previously held-back character now that one slot has passed
        if prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_char))

        # Hold back the current character (decrement its remaining count) for next round
        prev_count, prev_char = count + 1, ch   # count is negative, so +1 increases it toward 0

    if len(result) != len(s):
        return ""    # impossible to rearrange without adjacent duplicates

    return "".join(result)
```

**Line-by-Line Explanation:**

- `max_heap` stores `(-count, char)` so Python's min-heap behaves like a max-heap on frequency.
- Each iteration pops the currently most frequent character and places it immediately.
- The *previous* iteration's character is deliberately **not** reinserted into the heap until **after** the current placement -- this is what prevents two identical characters from ever being placed consecutively.
- `prev_count, prev_char` hold the just-placed character's updated (decremented) count for reinsertion next round.
- If the final result's length doesn't match the input length, some character's frequency was too high to avoid adjacency -- impossible case.

**Dry Run:** (see visualization; tabulated)

| Step | Popped | Placed | prev reinserted? | Heap after |
|---|---|---|---|---|
| 1 | (-2,'a') | 'a' | none yet (prev_count=0) | [] |
| 2 | (-1,'b') | 'b' | yes, push (-1,'a') | [(-1,'a')] |
| 3 | (-1,'a') | 'a' | yes, push (0,'b') -- but 0 means exhausted, still pushed (harmless, popped last if needed) | [] |

Result: **"aba"**

**Correctness Intuition:** The classic *necessary and sufficient* feasibility condition is: the most frequent character's count must not exceed `ceil(n / 2)`. The heap-based greedy naturally respects this because it always interleaves the most frequent remaining character with the next-most-frequent, spreading out any single character's occurrences as evenly as possible -- which is provably the arrangement least likely to force adjacency, by a counting/pigeonhole argument.

**Time Complexity:** O(n log k) where `k` is the number of distinct characters (heap operations per character in the string).
**Space Complexity:** O(k) for the heap and frequency map.

**Edge Cases:**
- A single character repeated more than `ceil(n/2)` times -> impossible, return `""`.
- All characters distinct -> any order is valid.
- String of length 1 -> trivially itself.

**Common Mistakes:**
- Reinserting the just-used character into the heap *immediately* (same iteration) instead of delaying by one step -- causes adjacent duplicates.
- Forgetting the final length check to detect infeasibility.

**Interview Tips:** State the feasibility condition (`max_freq <= ceil(n/2)`) upfront -- it demonstrates you understand *why* the greedy heap approach works and gives you an O(1) early-exit check before even running the algorithm.

**Optimizations:** A simpler O(n log k) or even O(n) approach exists: sort characters by frequency, then fill even indices first, then odd indices (a "wiggle fill" strategy) -- avoids heap overhead entirely.

**Variations:** Task Scheduler (Section 5.25) uses nearly identical frequency-greedy logic but with an explicit cooldown period instead of a strict "no adjacent" rule.

**Practice Problems:** LeetCode 767 (Reorganize String).

**Summary:** Max-heap by frequency; place the most frequent remaining character each step, delaying reinsertion of the just-placed character by one step to avoid adjacency. O(n log k).

---

### 5.24 IPO Problem

**Problem Statement:** Given `n` projects each with a `capital` requirement and a `profit`, and starting capital `W`, select at most `k` projects (only those affordable at the time) to maximize final capital, where completed projects' profit is added to your capital for future selections.

**Why it exists:** Demonstrates combining a **min-heap (filter by affordability)** with a **max-heap (pick best profit among affordable)** -- a two-heap greedy pattern common in "budget-constrained sequential selection" problems.

**Intuition:** At each of the `k` rounds, among all projects whose `capital` requirement is `<=` current capital, greedily pick the one with the **highest profit** (since profit compounds into future affordability). Efficiently maintain "affordable projects" using a min-heap sorted by capital requirement (pop everything affordable into a max-heap sorted by profit), then pop the max-profit one.

**Real-world analogy:** A startup investor with a limited budget, choosing which affordable venture to fund first each round to maximize compounding returns for future rounds.

**ASCII Visualization:**

```
capital = [0,1,2], profit = [1,2,3], W=0, k=2

min-heap by capital: [(0,proj0),(1,proj1),(2,proj2)]

Round 1: pop all with capital<=W(0) -> proj0 (capital 0) -> max-heap=[(-1,proj0)]
         pick max profit -> proj0 (profit 1) -> W = 0+1 = 1

Round 2: pop all with capital<=W(1) -> proj1 (capital 1) -> max-heap=[(-2,proj1)]
         pick max profit -> proj1 (profit 2) -> W = 1+2 = 3

Final capital = 3
```

**Python Implementation:**

```python
import heapq

def find_maximized_capital(k, w, profits, capital):
    """
    k: int max number of projects to select
    w: int initial capital
    profits, capital: List[int] parallel arrays
    Returns the maximum final capital achievable.
    """
    n = len(profits)
    # Min-heap of (capital_required, profit), sorted by capital
    projects = sorted(zip(capital, profits))
    min_heap_idx = 0
    max_heap = []   # max-heap of profits (negated) for currently affordable projects

    for _ in range(k):
        # Move all newly affordable projects into the max-heap
        while min_heap_idx < n and projects[min_heap_idx][0] <= w:
            cap_req, prof = projects[min_heap_idx]
            heapq.heappush(max_heap, -prof)
            min_heap_idx += 1

        if not max_heap:
            break   # no affordable project remains -> stop early

        w += -heapq.heappop(max_heap)   # take the most profitable affordable project

    return w
```

**Line-by-Line Explanation:**

- `projects` is sorted by capital requirement ascending -- acts as our "pool of not-yet-affordable" projects, walked with `min_heap_idx`.
- Each round, we pull every project that just became affordable (capital requirement `<= w`) into `max_heap` (profit-sorted, negated for max-heap-via-min-heap trick).
- We then greedily take the single most profitable currently affordable project, adding its profit to `w`.
- Loop runs at most `k` times, breaking early if no affordable projects remain.

**Dry Run:** (see visualization; tabulated)

| Round | w before | Newly affordable | max_heap | Picked | w after |
|---|---|---|---|---|---|
| 1 | 0 | proj(cap0,profit1) | [-1] | profit1 | 1 |
| 2 | 1 | proj(cap1,profit2) | [-2] | profit2 | 3 |

Final capital = **3**

**Correctness Intuition (Exchange Argument):** At any round, choosing a lower-profit affordable project over the highest-profit affordable one can never help -- the highest-profit project, once completed, strictly increases (or ties) future capital, which can only expand (never shrink) the set of affordable projects available in later rounds. Thus greedily maximizing profit at every step dominates any alternative choice, provable by exchanging any suboptimal pick with the greedy pick without loss.

**Time Complexity:** O(n log n) for the initial sort + O(n log n) for heap pushes across all rounds (each project pushed at most once) = **O(n log n)**.
**Space Complexity:** O(n) for the heaps.

**Edge Cases:**
- No project is ever affordable -> return initial `w` unchanged.
- `k` larger than the number of affordable projects across all rounds -> loop breaks early, still correct.
- All projects have zero profit -> capital never grows, but algorithm still terminates correctly.

**Common Mistakes:**
- Re-scanning the *entire* project list every round for affordability (O(n*k)) instead of using the sorted-pointer + min-heap-drain technique (O(n log n) total).
- Picking the cheapest affordable project instead of the most profitable one -- wrong greedy metric.

**Interview Tips:** Name this the "two-heap greedy" pattern explicitly -- it's a strong signal of pattern recognition and reused in various "unlock more options as you progress" problems.

**Optimizations:** Already near-optimal; the sorted-array + max-heap combo avoids needing a full second heap for the capital dimension.

**Variations:** Similar two-heap/one-sorted-array + one-heap patterns appear in "Course Schedule III" and other prerequisite-unlocking greedy problems.

**Practice Problems:** LeetCode 502 (IPO).

**Summary:** Sort projects by capital requirement; each round, drain newly affordable projects into a max-heap by profit, then greedily take the most profitable affordable project. O(n log n).

---

### 5.25 Task Scheduler

**Problem Statement:** Given a list of tasks (represented by characters) and a cooldown period `n` between two same-type tasks, find the minimum total time (including idle slots) needed to complete all tasks.

**Why it exists:** The definitive **frequency-greedy with cooldown** problem -- generalizes Reorganize String's "no adjacent duplicates" into "no duplicates within a cooldown window."

**Intuition:** The most frequent task dictates a lower bound on total time: it needs `(max_freq - 1)` cooldown gaps of length `n+1` each, plus 1 for its last occurrence, i.e., `(max_freq - 1) * (n + 1) + count_of_tasks_tied_with_max_freq`. If there are enough *other* distinct tasks to fill every gap, this formula is tight; otherwise, the total is simply `len(tasks)` (no idle time needed at all).

**Real-world analogy:** Scheduling CPU jobs where the same job type needs to "cool down" for `n` cycles before running again -- similar to memory bank conflict avoidance or ad-slot cooldown rules (same brand can't air twice within a cooldown window).

**ASCII Visualization:**

```
tasks = ['A','A','A','B','B','B'], n=2

Most frequent: A and B both at 3.

Frame structure:  A B _ A B _ A B
                   |-3 blocks of size (n+1)=3, last one only needs actual tasks, no trailing idle|

(max_freq - 1) * (n+1) + max_count_tied
 = (3-1)*(2+1) + 2   [2 tasks -- A and B -- tied at max_freq]
 = 2*3 + 2 = 8

len(tasks) = 6 <= 8 -> idle slots ARE needed -> answer = 8
```

**Python Implementation:**

```python
from collections import Counter

def least_interval(tasks, n):
    """
    tasks: List[str] task identifiers
    n: int cooldown period between same-type tasks
    Returns the minimum total time (including idle) to finish all tasks.
    """
    freq = Counter(tasks)
    max_freq = max(freq.values())

    # Number of distinct tasks that share the maximum frequency
    max_freq_count = sum(1 for count in freq.values() if count == max_freq)

    # Lower bound imposed by the most frequent task's cooldown structure
    intervals_needed = (max_freq - 1) * (n + 1) + max_freq_count

    # If there are enough tasks to fill every cooldown gap, no idle time is needed
    return max(len(tasks), intervals_needed)
```

**Line-by-Line Explanation:**

- `freq`: frequency count of each task type.
- `max_freq`: the highest single-task frequency -- this task dictates the minimum "skeleton" structure of the schedule.
- `max_freq_count`: how many distinct task types are tied at this maximum frequency -- each of them must occupy one slot per "round," extending the last round's length too.
- `intervals_needed`: the theoretical minimum length if we must respect the most frequent task's cooldown, assuming worst-case idle-filling.
- The final answer is the **max** of this theoretical minimum and the raw task count -- if there are enough other tasks to fill every gap with real work, idle time disappears entirely and the answer is simply `len(tasks)`.

**Dry Run:** (see visualization; tabulated)

| Quantity | Value |
|---|---|
| freq | {A:3, B:3} |
| max_freq | 3 |
| max_freq_count | 2 (A and B tied) |
| intervals_needed | (3-1)*(2+1) + 2 = 8 |
| len(tasks) | 6 |
| answer | max(6, 8) = **8** |

**Correctness Intuition:** Picture the most frequent task creating `max_freq - 1` "cooldown blocks" of size `n+1`, plus one final slot for its last occurrence (and for every other task tied at that frequency, since they also need a final slot in the last block). This is a hard lower bound on schedule length. If enough other distinct tasks exist to fill every idle slot in these blocks with real work, the schedule compresses down to exactly `len(tasks)` with zero idle time; otherwise idle slots are unavoidable and the formula is exact. This is proven via a direct constructive argument: always fill each cooldown slot with the next most frequent *other* available task (a mini frequency-greedy within each round), which is always possible whenever `len(tasks) < intervals_needed`.

**Time Complexity:** O(n) where n = number of tasks (for building frequency counts); the formula computation is O(1) given the counts (O(26) for the max scans, constant for fixed alphabet).
**Space Complexity:** O(1) (bounded alphabet frequency table).

**Edge Cases:**
- `n == 0` -> no cooldown needed, answer is simply `len(tasks)`.
- All tasks identical -> answer is `(count-1)*(n+1) + 1`.
- Enough task diversity to always fill gaps -> answer equals `len(tasks)`.

**Common Mistakes:**
- Forgetting to account for `max_freq_count` (multiple tasks tied at the max frequency) -- undercounts the required final-block slots.
- Actually simulating the full schedule with a heap (works, but O(n log k) with more complexity) when the closed-form formula suffices and is O(n).
- Forgetting the final `max(len(tasks), intervals_needed)` -- without it, the formula can *undercount* when there's plenty of task diversity to avoid idling.

**Interview Tips:** Present **both** the closed-form formula (fast, elegant) **and** a heap/queue-based simulation (Section 5.23-style, more general and easier to explain step-by-step) -- interviewers often want to see the simulation as a stepping stone to the formula.

**Optimizations:** The formula approach is already O(n), optimal.

**Variations:** Reorganize String (Section 5.23) is the special case `n = 1` of this exact problem (cooldown of 1 = "no two identical adjacent").

**Practice Problems:** LeetCode 621 (Task Scheduler).

**Summary:** Compute `(max_freq - 1) * (n + 1) + count_of_tasks_at_max_freq`, then take the max with `len(tasks)` to account for cases where task diversity fills all gaps. O(n) time, O(1) space.


---

## 6. Advanced Greedy Concepts

### 6.1 Huffman Coding Revisited — Deeper Theory

Huffman coding is provably optimal among all prefix-free codes (Section 5.4). A few deeper points:

- **Kraft's Inequality:** For any prefix-free code with lengths `l_1...l_n`, `sum(2^-l_i) <= 1`. Huffman's construction always satisfies this with equality when the tree is full (every internal node has exactly 2 children).
- **Entropy bound:** The average Huffman code length is always within 1 bit of the Shannon entropy of the source distribution — Huffman is near-optimal even against the theoretical information-theoretic minimum.
- **Canonical Huffman codes:** Real compression formats (like DEFLATE) store only code *lengths*, not the full tree, and reconstruct a canonical assignment — saving significant header space.

### 6.2 Greedy Scheduling Theory

Beyond single-resource scheduling (Sections 5.1, 5.3, 5.9), scheduling theory studies:

- **SJF (Shortest Job First):** Minimizes average waiting time on a single processor — a greedy rule provable optimal via exchange argument (swap any inversion of a longer job before a shorter one to reduce total wait).
- **EDF (Earliest Deadline First):** Optimal for single-processor scheduling to meet deadlines, provided total processor utilization does not exceed 100%.
- **Multiprocessor scheduling** generally loses greedy-optimality — becomes NP-hard in the general case, requiring approximation algorithms.

### 6.3 Interval Graph Coloring

**Problem:** Given overlapping intervals, assign each interval a "color" (resource) such that overlapping intervals get different colors, using the minimum number of colors.

**Greedy Insight:** The minimum number of colors needed equals the **maximum number of intervals overlapping at any single point** (the same quantity computed in Minimum Platforms / Meeting Rooms II). A greedy coloring — process intervals sorted by start time, assign the lowest-numbered color not currently in use — always achieves this minimum for interval graphs specifically (though *general* graph coloring is NP-hard; interval graphs are a special "perfect graph" case where greedy succeeds).

```
Intervals:  A[1,4]  B[2,6]  C[5,8]

Overlap check: A&B overlap, B&C overlap, A&C don't overlap
Max simultaneous overlap = 2 (A,B together)

Greedy coloring: A->color1, B->color2 (conflicts with A), C->color1 (reuse, no conflict with A)
Colors used = 2  (matches the maximum overlap)
```

### 6.4 Load Balancing (Overview)

**Problem:** Distribute `n` jobs across `m` machines to minimize the maximum load (makespan) on any single machine.

- **Greedy heuristic (List Scheduling):** Assign each job, in some order, to the currently least-loaded machine. This achieves a **2-approximation** (guaranteed within 2x of optimal) — not exact, but a strong, simple bound.
- **Longest Processing Time (LPT) first:** Sorting jobs by decreasing duration before list-scheduling improves the guarantee to a **4/3-approximation**.
- This is a rare and important case where greedy does **not** give an exact answer but gives a *provable approximation ratio* — a key concept bridging into approximation algorithms (Section 6.6).

### 6.5 Matroid Theory in Practice

Beyond the intuition in Section 2.8, matroids formally explain why:

- **Kruskal's MST algorithm** is greedy-optimal: the "independent sets" are forests (no cycles), which form a **graphic matroid**.
- **Fractional Knapsack**-style problems (uniform matroid: any subset of size <= capacity is independent) are always greedy-solvable.
- Whenever you can phrase "pick elements maximizing total weight subject to an independence constraint," and that independence constraint is a matroid, greedy (sort by weight descending, add if it keeps the set independent) is *guaranteed* optimal — this single theorem "explains" a surprising fraction of all correct greedy algorithms in this handbook.

### 6.6 Approximation Algorithms (Overview)

For NP-hard optimization problems where exact greedy fails, greedy heuristics are often used to get **provable approximation ratios**:

| Problem | Greedy Heuristic | Approximation Ratio |
|---|---|---|
| Set Cover | Repeatedly pick the set covering the most uncovered elements | O(log n) |
| Vertex Cover | Repeatedly pick the highest-degree vertex | 2-approximation (specific variants) |
| TSP (metric) | Nearest neighbor | 2x worst case (no constant-factor guarantee in general; Christofides gives 1.5x for metric TSP, not purely greedy) |
| Load Balancing | List scheduling / LPT | 2x / 4/3x |

> **Key Insight:** Even when greedy isn't *exactly* optimal, it is often "good enough" with a formally provable worst-case bound — this is a major reason greedy heuristics remain popular in real-world systems despite theoretical imperfection.

---

## 7. Applications of Greedy Algorithms

| Domain | Application | Greedy Technique Used |
|---|---|---|
| **CPU Scheduling** | Shortest Job First, Priority Scheduling | Sort by burst time / priority |
| **Network Routing** | Dijkstra's shortest path (greedy relaxation) | Always finalize the closest unvisited node |
| **Compression** | Huffman coding (ZIP, JPEG, MP3) | Merge two least-frequent symbols |
| **Resource Allocation** | Job sequencing, IPO-style capital allocation | Sort by profit/deadline/ratio |
| **Load Distribution** | List scheduling for multiprocessor systems | Assign to least-loaded resource |
| **Event Scheduling** | Meeting rooms, activity selection | Sort by end time |
| **Memory Allocation** | First-fit / best-fit heuristics | Sort by block size |
| **Logistics** | Truck loading (Maximum Units), vehicle routing heuristics | Sort by density/value ratio |
| **Finance** | Currency change-making (canonical systems), simple greedy portfolio heuristics | Sort by denomination / return ratio |
| **AI Heuristics** | Greedy best-first search, greedy decoding in NLP (always pick highest-probability next token) | Sort/select by immediate score |

---

## 8. Problem Recognition Guide

### 8.1 Interview Clues That Suggest Greedy

- The problem mentions **"maximum number of..."** or **"minimum number of..."** combined with a simple constraint (non-overlap, budget, capacity).
- Sorting the input by *some* natural metric (deadline, ratio, finish time, frequency) seems to simplify the structure.
- The problem allows only **one pass** of irrevocable decisions if you think about it long enough.
- A brute-force/backtracking solution would be exponential, but a single well-chosen sort dramatically simplifies things.
- The problem is about **intervals, scheduling, or resource allocation**.

### 8.2 Recognition Flowchart

```
                       +-----------------------------+
                       | Does the problem ask to      |
                       | MAXIMIZE or MINIMIZE COUNT    |
                       | under simple constraints?     |
                       +---------------+---------------+
                                       | yes
                                       v
                       +-----------------------------+
                       | Can you define ONE sort key   |
                       | that seems to always help?    |
                       +---------------+---------------+
                          yes  <-------+-------> no
                           |                     |
                           v                     v
                +--------------------+   +---------------------+
                | Try greedy; verify  |   | Look for DP:        |
                | with exchange arg   |   | Do choices interact  |
                | or small examples   |   | / need memo lookup?  |
                +--------------------+   +---------------------+
                           |
                           v
                +--------------------+
                | Find a counterexample|
                | by hand (small n)?   |
                +---------+-----------+
                   no  <--+--> yes
                    |            |
                    v            v
             +-----------+ +----------------+
             | Greedy OK  | | Fall back to DP |
             | -- proceed | | / Backtracking  |
             +-----------+ +----------------+
```

### 8.3 Exchange Argument Intuition (Quick Recall)

1. Assume a hypothetical optimal solution disagrees with greedy at the earliest point.
2. Show swapping in the greedy choice keeps feasibility and doesn't reduce quality.
3. Repeat until the hypothetical optimal *is* the greedy solution.
4. Conclude: greedy is (at least) as good as any optimal solution → greedy is optimal.

### 8.4 When Greedy Works

| Signal | Example |
|---|---|
| Matroid-like independence structure | MST, Fractional Knapsack |
| Interval / earliest-deadline structure | Activity Selection, Job Sequencing |
| Monotonic frontier expansion | Jump Game |
| Exchange argument holds cleanly | Huffman Coding, Gas Station |

### 8.5 When DP Is Required Instead

| Signal | Example |
|---|---|
| Items indivisible with competing constraints | 0/1 Knapsack |
| Choices need to be compared/combined, not just accepted/rejected | Longest Common Subsequence |
| Counterexample found by hand | Coin change with arbitrary denominations |
| "Maximize weighted..." version of a greedy-count problem | Weighted Activity Selection |

---

## 9. Optimization Strategies

### 9.1 Brute Force → Greedy

Identify the metric that brute force would eventually converge to trying "first" in its best branch, and check whether committing to that metric immediately (without backtracking) still reaches the optimum.

### 9.2 DP → Greedy (Where Valid)

If a DP recurrence's transition always picks the same "type" of choice regardless of other state (i.e., the recurrence doesn't actually need to compare alternatives), the DP can likely be collapsed into a simpler greedy — a strong sign is when the DP's transition doesn't depend on future look-ahead at all.

### 9.3 Sorting Optimization

- Use Python's built-in `sort()`/`sorted()` (Timsort) — O(n log n), highly optimized in C.
- Prefer `key=` functions over custom `__lt__`/comparator classes for speed and readability.
- Avoid re-sorting inside a loop — sort once outside.

### 9.4 Heap Optimization

- Use `heapq.heapify()` (O(n)) to bulk-build instead of n individual `heappush()` calls (O(n log n)).
- For "top-k" style greedy problems, a bounded heap of size `k` avoids storing all n elements.

### 9.5 Space Optimization

- Many two-pass greedy problems (Candy Distribution) can be compressed to O(1) extra space with careful single-pass slope tracking, at the cost of code clarity.
- Prefer in-place sorting (`list.sort()`) over `sorted()` when the original order isn't needed, to avoid an extra O(n) copy.

### 9.6 Time Optimization

- Early-exit conditions (Jump Game's `max_reach >= n-1` check) can meaningfully cut average-case runtime even when worst-case complexity is unchanged.
- Precompute lookups (like `last_occurrence` in Partition Labels / Remove Duplicate Letters) to avoid O(n) rescans inside a loop.

---

## 10. Interview Preparation

### 10.1 Problems by Difficulty

| Difficulty | Problems |
|---|---|
| Easy | Assign Cookies, Lemonade Change, Maximum Units on a Truck |
| Medium | Activity Selection, Fractional Knapsack, Merge Intervals, Insert Interval, Non-overlapping Intervals, Meeting Rooms I/II, Gas Station, Jump Game, Jump Game II, Candy, Boat to Save People, Partition Labels, Minimum Arrows to Burst Balloons, IPO, Task Scheduler |
| Hard | Job Sequencing (with DSU optimization), Huffman Coding, Queue Reconstruction by Height, Valid Parenthesis String, Remove Duplicate Letters, Reorganize String |

### 10.2 Pattern-wise Question Map

| Pattern | Representative Problems |
|---|---|
| Interval Greedy | Activity Selection, Merge/Insert Interval, Non-overlapping Intervals, Meeting Rooms, Minimum Arrows |
| Two-pointer Greedy | Assign Cookies, Boat to Save People |
| Frequency/Heap Greedy | Huffman Coding, Reorganize String, Task Scheduler, IPO |
| Prefix/Suffix Greedy | Candy Distribution, Gas Station, Partition Labels |
| Monotonic Frontier | Jump Game, Jump Game II |
| Monotonic Stack | Remove Duplicate Letters |
| Sort + Fill | Fractional Knapsack, Maximum Units on a Truck, Job Sequencing |

### 10.3 Company-wise Tendencies (General Trends, Not Guarantees)

| Company | Commonly Cited Greedy Topics |
|---|---|
| Amazon | Meeting Rooms, Gas Station, Task Scheduler |
| Google | Jump Game family, Huffman-style reasoning, IPO |
| Meta | Merge/Insert Intervals, Partition Labels |
| Microsoft | Activity Selection variants, Candy Distribution |
| Bloomberg/Finance firms | Job Sequencing, IPO, Fractional Knapsack |

*(These are general community-reported trends, not official or guaranteed patterns — always prepare broadly.)*

### 10.4 Blind 75 / NeetCode Greedy Subset

Commonly included greedy problems in popular curated lists: Jump Game, Jump Game II, Gas Station, Merge Intervals, Insert Interval, Non-overlapping Intervals, Partition Labels.

### 10.5 Standard Interview Templates to Memorize

1. **Sort + single-pass accept/reject** (Activity Selection style).
2. **Sort + fractional/greedy fill** (Fractional Knapsack style).
3. **Two-pointer from sorted array(s)** (Assign Cookies / Boat to Save People style).
4. **Heap-based "always process current best"** (Huffman / Reorganize String / IPO style).
5. **Prefix/suffix double-pass** (Candy Distribution style).
6. **Monotonic frontier expansion** (Jump Game style).

### 10.6 Interview Tricks

- Always state your greedy rule out loud **before** coding — interviewers grade reasoning, not just working code.
- If unsure whether greedy applies, **test on a small handcrafted counterexample** before committing — this single habit prevents most greedy interview failures.
- When asked "why does this work," default to the **exchange argument** structure (Section 2.1).


---

## 11. Python Tips for Greedy Coding

### 11.1 Sorting

```python
# Sort by a single key
items.sort(key=lambda x: x[1])

# Sort by multiple keys (primary, secondary)
items.sort(key=lambda x: (x[0], -x[1]))   # x[0] ascending, x[1] descending

# Sort descending
items.sort(key=lambda x: x[0], reverse=True)
```

### 11.2 Custom Sort Keys & Lambdas

- Use tuples in the `key=` function to encode multi-level sort priority: `key=lambda p: (-p[0], p[1])` sorts by first field descending, second field ascending — exactly what Queue Reconstruction by Height needs.
- `functools.cmp_to_key` exists for legacy comparator-style sorting but is rarely needed — prefer `key=`.

### 11.3 heapq Essentials

```python
import heapq

heap = []
heapq.heappush(heap, 5)
smallest = heapq.heappop(heap)
heapq.heapify(existing_list)          # O(n) bulk conversion to heap

# Max-heap trick: negate values
max_heap = []
heapq.heappush(max_heap, -value)
largest = -heapq.heappop(max_heap)

# k largest / k smallest without building a full heap manually
heapq.nlargest(k, iterable)
heapq.nsmallest(k, iterable)
```

### 11.4 collections Essentials

```python
from collections import Counter, defaultdict, deque

freq = Counter(some_iterable)          # frequency table
freq.most_common(k)                     # top-k frequent items, sorted

d = defaultdict(int)                    # avoids KeyError, auto-initializes to 0
dq = deque()                            # O(1) append/pop from both ends
```

### 11.5 itertools Essentials

```python
from itertools import accumulate, groupby, chain

prefix_sums = list(accumulate(nums))          # running prefix sums, O(n)
for key, group in groupby(sorted_items, key=lambda x: x[0]):
    ...                                          # group consecutive equal keys
```

### 11.6 bisect Essentials

```python
import bisect

bisect.insort(sorted_list, value)     # O(n) insert maintaining sorted order
idx = bisect.bisect_left(sorted_list, value)   # O(log n) find insertion point
```

Useful for greedy problems needing "find the smallest/largest element satisfying a condition" without a full heap (e.g., patience-sorting style problems).

### 11.7 Performance Tips

- Prefer `sort()` (in-place, no extra list) over `sorted()` when you don't need to preserve the original order.
- Avoid repeated `list.pop(0)` (O(n) each call) — use `collections.deque.popleft()` (O(1)) instead.
- Precompute expensive lookups (like `last_occurrence` dicts) once outside loops.
- Avoid needless tuple/object creation inside hot loops — reuse variables where possible.

### 11.8 Memory Optimization

- Use generators (`(x for x in ...)`) instead of list comprehensions when you only need to iterate once.
- For huge inputs, process with `sys.stdin` line-by-line rather than loading everything into memory (relevant in competitive programming).

### 11.9 Common Python Pitfalls

- **Mutable default arguments:** never use `def f(x, acc=[])` — the list persists across calls unexpectedly.
- **Integer division:** Python 3's `/` is true division (float); use `//` for floor division — matters in problems mixing ratios and integer slot counts.
- **Heap tie-breaking:** when heap elements are tuples with equal first elements, Python compares the next tuple element — ensure that's sortable/comparable (e.g., don't push raw unorderable objects; push `(priority, tie_breaker, obj)`).
- **Sorting stability:** Python's sort is stable — exploit this deliberately when secondary order matters and you sort in two stages.

---

## 12. Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---|---|---|
| Assuming greedy always works | Greedy Choice Property doesn't hold for most problems | Always verify with a proof or counterexample before trusting greedy |
| Wrong sorting criterion | e.g. sorting Fractional Knapsack by `value` instead of `value/weight` | Derive the sort key from the actual greedy proof, not intuition alone |
| Missing proof of correctness | "It looks right" isn't a proof | Use the exchange argument explicitly |
| Ignoring edge cases | Empty input, single element, all-equal elements | Explicitly test these cases |
| Incorrect interval comparisons | `<` vs `<=` mismatches for touching intervals | Clarify inclusive/exclusive boundary semantics per problem statement |
| Tie-breaking errors | e.g. Queue Reconstruction without secondary sort key | Always define a deterministic total order for ties |
| Local optimum mistakes | Confusing "best right now" with "best overall" | Explicitly test the greedy choice against a brute-force baseline on small inputs |

---

## 13. Cheat Sheets

### 13.1 Greedy Templates Cheat Sheet

| Template | Core Idea | Example Problem |
|---|---|---|
| Sort + accept/reject | Sort by key, scan once, accept if feasible | Activity Selection |
| Sort + fractional fill | Sort by ratio, fill until capacity exhausted | Fractional Knapsack |
| Two-pointer (same array) | Sort, converge pointers from both ends | Boat to Save People |
| Two-pointer (two arrays) | Sort both, match smallest-to-smallest | Assign Cookies |
| Heap "current best" | Maintain heap, always process top | Huffman Coding, IPO |
| Prefix/suffix double pass | Compute left-to-right then right-to-left constraints | Candy Distribution |
| Monotonic frontier | Track a running max reachable boundary | Jump Game |
| Monotonic stack | Pop while condition + reversibility check | Remove Duplicate Letters |

### 13.2 Pattern Recognition Cheat Sheet

```
"maximize count of non-overlapping X"      -> sort by end, Activity Selection pattern
"minimum resources for concurrent X"        -> sort + sweep OR heap, Meeting Rooms pattern
"maximize value with capacity constraint"   -> sort by ratio, Knapsack-style (check divisibility!)
"minimum removals to fix overlaps"          -> Activity Selection complement
"rearrange with adjacency constraint"       -> frequency + heap, Reorganize String pattern
"reachability / minimum jumps"              -> monotonic frontier, Jump Game pattern
"smallest lexicographic result"             -> monotonic stack, Remove Duplicate Letters pattern
```

### 13.3 Complexity Cheat Sheet

| Problem | Time | Space |
|---|---|---|
| Activity Selection | O(n log n) | O(1) |
| Fractional Knapsack | O(n log n) | O(1) |
| Job Sequencing (DSU) | O(n log n) | O(n) |
| Huffman Coding | O(n log n) | O(n) |
| Minimum Platforms | O(n log n) | O(1) |
| Merge/Insert Intervals | O(n log n) / O(n) | O(n) |
| Meeting Rooms II | O(n log n) | O(n) |
| Gas Station | O(n) | O(1) |
| Jump Game / II | O(n) | O(1) |
| Candy Distribution | O(n) | O(n) |
| Assign Cookies | O(n log n) | O(1) |
| Boat to Save People | O(n log n) | O(1) |
| Partition Labels | O(n) | O(1) (bounded alphabet) |
| Remove Duplicate Letters | O(n) | O(1) (bounded alphabet) |
| Reorganize String | O(n log k) | O(k) |
| IPO | O(n log n) | O(n) |
| Task Scheduler | O(n) | O(1) |

### 13.4 Sorting Strategies Cheat Sheet

| Sort By | Used For |
|---|---|
| End time ascending | Activity Selection, Non-overlapping Intervals, Minimum Arrows |
| Start time ascending | Merge Intervals, Meeting Rooms |
| Value/weight ratio descending | Fractional Knapsack, Maximum Units on a Truck |
| Profit descending | Job Sequencing |
| Height descending, k ascending | Queue Reconstruction by Height |
| Frequency descending (heap) | Huffman Coding, Reorganize String, Task Scheduler |

### 13.5 Python Syntax Cheat Sheet

```python
items.sort(key=lambda x: x[1])                     # sort by 2nd element
items.sort(key=lambda x: (-x[0], x[1]))             # multi-key sort
heapq.heapify(lst); heapq.heappush(h, v); heapq.heappop(h)
Counter(iterable).most_common(k)
bisect.insort(sorted_list, value)
```

### 13.6 Interview Guide Cheat Sheet

1. Restate the problem; ask about tie-break/boundary conventions.
2. Propose the greedy rule and sort key explicitly.
3. Justify with a short exchange-argument sketch.
4. Code the O(n log n) (or better) solution.
5. Dry-run a small example on the whiteboard.
6. State time/space complexity.
7. Mention edge cases and how they're handled.

---

## 14. Practice Problem Bank

> Links are omitted for platforms that frequently change URLs; search the exact problem name on the given platform.

### 14.1 Basics

| Problem | Platform | Difficulty |
|---|---|---|
| Assign Cookies | LeetCode | Easy |
| Lemonade Change | LeetCode | Easy |
| Maximum Units on a Truck | LeetCode | Easy |
| Minimum Number of Coins (canonical systems) | GeeksforGeeks | Easy |

### 14.2 Sorting + Greedy

| Problem | Platform | Difficulty |
|---|---|---|
| Fractional Knapsack | GeeksforGeeks | Medium |
| Job Sequencing with Deadlines | GeeksforGeeks | Medium |
| IPO | LeetCode | Hard |
| N Meetings in One Room | GeeksforGeeks | Medium |

### 14.3 Interval Problems

| Problem | Platform | Difficulty |
|---|---|---|
| Merge Intervals | LeetCode | Medium |
| Insert Interval | LeetCode | Medium |
| Non-overlapping Intervals | LeetCode | Medium |
| Minimum Number of Arrows to Burst Balloons | LeetCode | Medium |
| Meeting Rooms | LeetCode | Easy |
| Meeting Rooms II | LeetCode | Medium |

### 14.4 Scheduling

| Problem | Platform | Difficulty |
|---|---|---|
| Minimum Platforms | GeeksforGeeks | Medium |
| Task Scheduler | LeetCode | Medium |
| CPU Scheduling (SJF simulation) | InterviewBit | Medium |

### 14.5 Knapsack-adjacent

| Problem | Platform | Difficulty |
|---|---|---|
| Fractional Knapsack | GeeksforGeeks | Medium |
| Maximum Units on a Truck | LeetCode | Easy |
| Candy (as a resource-distribution variant) | LeetCode | Hard |

### 14.6 Jump Game Family

| Problem | Platform | Difficulty |
|---|---|---|
| Jump Game | LeetCode | Medium |
| Jump Game II | LeetCode | Medium |
| Jump Game III / VII (BFS/greedy hybrids) | LeetCode | Medium |

### 14.7 Resource Allocation

| Problem | Platform | Difficulty |
|---|---|---|
| Boats to Save People | LeetCode | Medium |
| Gas Station | LeetCode | Medium |
| IPO | LeetCode | Hard |

### 14.8 Huffman Coding

| Problem | Platform | Difficulty |
|---|---|---|
| Huffman Coding | GeeksforGeeks | Hard |
| Huffman Decoding | GeeksforGeeks | Medium |

### 14.9 String Greedy

| Problem | Platform | Difficulty |
|---|---|---|
| Remove Duplicate Letters | LeetCode | Medium |
| Reorganize String | LeetCode | Medium |
| Valid Parenthesis String | LeetCode | Medium |
| Partition Labels | LeetCode | Medium |

### 14.10 Advanced Greedy

| Problem | Platform | Difficulty |
|---|---|---|
| Queue Reconstruction by Height | LeetCode | Medium |
| Candy | LeetCode | Hard |
| Course Schedule III | LeetCode | Hard |
| Minimum Cost to Hire K Workers | LeetCode | Hard |

### 14.11 Competitive Programming Extras

| Problem | Platform |
|---|---|
| Greedy problem set (search "greedy") | Codeforces |
| Greedy problem set | CodeChef |
| Greedy category problems | AtCoder |
| Greedy tagged problems | CSES Problem Set |
| Greedy Algorithms track | HackerRank |

---

## 15. Final Revision Kit

### 15.1 One-Page Notes

```
GREEDY = locally optimal choice, never revisited, hoping for global optimum.
Requires: Greedy Choice Property + Optimal Substructure.
Prove with: Exchange Argument.
Disprove with: One good counterexample.

Core templates:
  1. Sort + accept/reject      (Activity Selection)
  2. Sort + fractional fill    (Fractional Knapsack)
  3. Two-pointer               (Assign Cookies, Boat to Save People)
  4. Heap "current best"       (Huffman, IPO, Reorganize String)
  5. Prefix/suffix double pass (Candy)
  6. Monotonic frontier        (Jump Game)
  7. Monotonic stack           (Remove Duplicate Letters)
```

### 15.2 Mind Map

```
                              GREEDY ALGORITHMS
                                     |
       +---------------+-------------+-------------+----------------+
       |               |             |             |                |
   INTERVALS      KNAPSACK-ISH   SCHEDULING     STRINGS         FRONTIER/GRAPH
       |               |             |             |                |
  Activity Sel.   Fractional     Job Sequencing  Reorganize      Jump Game I/II
  Merge/Insert    Knapsack       Task Scheduler  Remove Dup      Gas Station
  Non-overlap     Max Units      Huffman Coding  Valid Paren
  Meeting Rooms   IPO                            Partition Labels
  Min Arrows
  Min Platforms
```

### 15.3 Pattern Map (Quick Lookup)

```
Sort by END time         -> interval acceptance problems
Sort by RATIO desc       -> value-density fill problems
Sort by PROFIT desc      -> deadline/slot assignment problems
Sort by FREQUENCY (heap) -> rearrangement / merging problems
Two pointers on 1 array  -> pairing extremes (Boat to Save People)
Two pointers on 2 arrays -> matching sorted demands to sorted supply
```

### 15.4 Recognition Flowchart (Repeated for Quick Access)

```
Maximize/minimize count under simple constraint?
   -> yes -> single sort key seems to help?
        -> yes -> try greedy + exchange argument
        -> no  -> consider DP/backtracking
   -> no -> probably not a pure greedy problem
```

### 15.5 Greedy Decision Tree (Repeated for Quick Access)

```
                 Do choices interact with each other's future value?
                          |
              +-----------+-----------+
              | no                    | yes
              v                       v
        Greedy candidate        Likely needs DP
              |
              v
     Can you prove it via
     exchange argument?
        |         |
       yes        no
        |         |
        v         v
    Use Greedy   Search for counterexample;
                  fallback to DP/Backtracking
```

### 15.6 Complexity Sheet (Repeated for Quick Access)

See Section 13.3.

### 15.7 Interview Cheat Sheet (Repeated for Quick Access)

See Section 13.6.

### 15.8 15-Minute Revision

1. Recall the definition and Greedy Choice Property (2 min).
2. Recall the exchange argument structure (2 min).
3. Skim the 7 templates in Section 3 (3 min).
4. Skim the pattern map in Section 13.2 (3 min).
5. Mentally solve Activity Selection and Fractional Knapsack from memory (5 min).

### 15.9 1-Hour Revision

1. Read Sections 1–2 fully (Introduction + Fundamentals) — 10 min.
2. Re-derive the exchange argument for 3 different problems from Section 5 — 15 min.
3. Code Activity Selection, Fractional Knapsack, and Jump Game from scratch without looking — 20 min.
4. Review Common Mistakes (Section 12) and Cheat Sheets (Section 13) — 10 min.
5. Skim the Pattern Recognition Flowchart (Section 8.2) once more — 5 min.

---

## 16. FAQs

**Q1: Is greedy always faster than DP?**
A: Usually yes when applicable (often O(n log n) vs O(n^2) or worse), but greedy is only usable when provably correct — DP is the safe fallback when correctness can't be established.

**Q2: How do I know if my greedy solution is wrong?**
A: Test it against a small brute-force solution on many random small inputs. If they ever disagree, your greedy rule is wrong or incomplete.

**Q3: Can a problem have multiple valid greedy strategies?**
A: Yes — for example, Job Sequencing could alternatively be approached by sorting differently and using different tie-breaks, as long as the core exchange argument still holds.

**Q4: Why does Fractional Knapsack work with greedy but not 0/1 Knapsack?**
A: Divisibility. Greedy's ratio-based proof relies on being able to take *exactly* the needed fraction of the best item; 0/1 Knapsack's indivisibility breaks this, introducing combinatorial trade-offs that require DP.

**Q5: Is sorting always required for greedy?**
A: No — Gas Station and Jump Game are greedy without any sorting, relying instead on prefix-sum/frontier tracking. Sorting is common but not universal.

**Q6: What's the fastest way to prove a greedy algorithm wrong in an interview?**
A: Construct the smallest possible counterexample by hand (often 2-4 elements) — this is faster and more convincing than trying to reason abstractly under time pressure.

**Q7: Do I need to know matroid theory for interviews?**
A: No — it's a nice-to-have for deep understanding (and occasionally impresses in senior-level interviews) but is rarely required for standard interview problem-solving.

**Q8: How is Greedy related to Approximation Algorithms?**
A: When exact greedy optimality can't be proven for an NP-hard problem, greedy heuristics are often analyzed instead for a provable *approximation ratio* (Section 6.6) — a middle ground between "exactly optimal" and "no guarantee at all."

**Q9: What's the single most common greedy interview mistake?**
A: Choosing the wrong sort key — e.g., sorting by raw value instead of value/weight ratio, or by start time instead of end time — without first deriving the key from an exchange-argument proof.

**Q10: Should I always mention Big-O complexity even for simple greedy problems?**
A: Yes — always state both time and space complexity explicitly, even when trivial (O(n) / O(1)); it signals rigor and completeness to the interviewer.

---
