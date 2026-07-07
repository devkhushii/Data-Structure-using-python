# The Complete Competitive Programming Techniques Handbook 


## Table of Contents

1. [Introduction to Competitive Programming](#1-introduction-to-competitive-programming)
2. [Python for Competitive Programming](#2-python-for-competitive-programming)
3. [The Problem-Solving Framework](#3-the-problem-solving-framework)
4. [Complexity Optimization](#4-complexity-optimization)
5. [Pattern Recognition](#5-pattern-recognition)
6. [Competitive Programming Techniques](#6-competitive-programming-techniques)
7. [Contest Strategies](#7-contest-strategies)
8. [Debugging Techniques](#8-debugging-techniques)
9. [Optimization Techniques](#9-optimization-techniques)
10. [Common Contest Mistakes](#10-common-contest-mistakes)
11. [Competitive Programming Templates](#11-competitive-programming-templates)
12. [Contest Platforms](#12-contest-platforms)
13. [Interview vs. CP](#13-interview-vs-cp)
14. [Problem Recognition Decision Trees](#14-problem-recognition-decision-trees)
15. [Python Tips & Tricks](#15-python-tips--tricks)
16. [Cheat Sheets](#16-cheat-sheets)
17. [Practice Problems by Pattern](#17-practice-problems-by-pattern)
18. [Final Revision](#18-final-revision)

---

## 1. Introduction to Competitive Programming

### 1.1 What Is Competitive Programming?

Competitive programming (CP) is a mind sport where participants solve well-defined algorithmic problems, under time pressure, and submit code that is judged automatically for **correctness** and **efficiency** against hidden test cases.

**Why it matters:**
- Builds rapid pattern recognition for algorithmic structure.
- Trains you to reason precisely about time/space complexity *before* writing code.
- Is the closest peacetime analog to the "whiteboard coding" interview format used by FAANG/MAANG companies.
- Rewards clarity of thought over cleverness of syntax.

**Real-world analogy:** CP is like timed chess puzzles — you're not inventing chess, you're recognizing "oh, this is a smothered-mate pattern" quickly and executing it flawlessly. The techniques in this handbook are your tactical motifs.

### 1.2 History (Brief)

| Era | Milestone |
|---|---|
| 1970s–80s | ACM ICPC founded; academic algorithm contests begin. |
| 1989 | IOI (International Olympiad in Informatics) launched for pre-college students. |
| 1997 | TopCoder founded — first major online judge with real-time rating. |
| 2009 | Codeforces launched — becomes the dominant training ground. |
| 2010s | AtCoder, CodeChef, HackerRank, LeetCode rise; LeetCode becomes the interview-prep standard. |
| 2011–2023 | Google Code Jam and Facebook/Meta Hacker Cup run as flagship industry contests (Code Jam retired in 2023). |

### 1.3 Contest Formats

| Format | Description | Example |
|---|---|---|
| ICPC-style | Team of 3, 1 computer, 5 hours, first-to-solve tiebreak, frozen scoreboard | ICPC Regionals/World Finals |
| IOI-style | Individual, partial scoring (subtasks), no penalty for wrong submission | IOI, USACO |
| Codeforces Div-based | Individual, ratings-based divisions (Div 1/2/3/4), time-penalty scoring | CF Rounds |
| Rated Long Contests | Days-long, partial credit, editorial released after | CodeChef Long Challenge |
| Marathon/Optimization | No single "correct" answer — score is a continuous metric | AtCoder Heuristic Contest, Kaggle-style |
| Interview-style | Single problem, 30–45 min, communication matters as much as code | FAANG interviews, LeetCode |

### 1.4 Rating Systems

Most platforms use an **Elo-derived** rating system (Codeforces uses a custom Elo variant; TopCoder pioneered the modern CP Elo formula). Key idea: your rating changes based on **performance relative to expectation**, not raw score.

```
New Rating ≈ Old Rating + K * (Actual Performance − Expected Performance)
```

**Contest tip:** Ratings are noisy early on (first ~10 contests) — don't overreact to a single bad round.

### 1.5 Difficulty Levels (Rough Mapping)

| Level | Codeforces Rating | LeetCode | Typical Topics |
|---|---|---|---|
| Beginner | < 1200 | Easy | Simulation, basic loops, brute force |
| Intermediate | 1200–1600 | Medium | Two pointers, prefix sums, binary search, basic greedy/DP |
| Advanced | 1600–2100 | Medium-Hard | Graphs, DP on trees, number theory, segment trees |
| Expert | 2100–2600 | Hard | Advanced DP, flows, heavy-light, offline techniques |
| Master+ | 2600+ | Hard+ | FFT, suffix structures, advanced combinatorics, research-level constructive problems |

### 1.6 Problem Categories (High-Level)

Implementation, Math, Greedy, Dynamic Programming, Graphs, Data Structures, Strings, Geometry, Number Theory, Combinatorics, Game Theory, Constructive, Interactive, Bitmask, Flows.

### 1.7 Choosing the Right Platform

```
┌─────────────────────────────────────────────────────────┐
│              PLATFORM SELECTION GUIDE                    │
├─────────────────────────────────────────────────────────┤
│  Goal: Build strong fundamentals   → CSES Problem Set    │
│  Goal: Frequent rated practice     → Codeforces          │
│  Goal: Clean, well-tested problems → AtCoder             │
│  Goal: FAANG interview prep        → LeetCode            │
│  Goal: Team/ICPC training          → Codeforces Gyms,     │
│                                       ICPC archives        │
│  Goal: Long-form / research-y      → CodeChef Long,       │
│                                       Meta Hacker Cup       │
└─────────────────────────────────────────────────────────┘
```

**Contest Tip:** Beginners should live on CSES + Codeforces Div 3/4 for the first 3 months before branching out.

---
## 2. Python for Competitive Programming

Python is not the fastest language in raw constant factor, but with the right idioms it is fast *enough* for the vast majority of CP problems (Codeforces/AtCoder typically give Python 2–3x the time limit of C++). The goal of this section is to make Python's overhead disappear.

### 2.1 Fast Input

**Why it matters:** `input()` in a loop is slow because it flushes/re-reads line-by-line with Python-level overhead. For problems with 10^5–10^6 input tokens, this alone can TLE you.

```python
import sys
input = sys.stdin.readline          # override input with a faster line reader
data = sys.stdin.read().split()     # fastest: read EVERYTHING once, split into tokens
```

**Template — full fast I/O boilerplate:**

```python
import sys

def main():
    data = sys.stdin.buffer.read().split()   # buffer.read() avoids text-decoding overhead
    idx = 0
    def nxt():
        nonlocal idx
        val = data[idx]
        idx += 1
        return val

    n = int(nxt())
    arr = [int(nxt()) for _ in range(n)]
    # ... solve ...

if __name__ == "__main__":
    main()
```

**Line-by-line explanation:**
- `sys.stdin.buffer.read()` reads the raw bytes of stdin in one syscall — this is the single biggest speedup available in Python I/O.
- `.split()` on bytes splits on whitespace, giving a list of `bytes` tokens.
- `nxt()` is a closure-based pointer/cursor so we avoid repeatedly slicing the list (slicing is O(k) each time; indexing is O(1)).
- `int(nxt())` converts a bytes token directly to int — no need to `.decode()` first, since `int()` accepts bytes.

**Dry run:**

| Step | Input Remaining | idx | Action | Result |
|---|---|---|---|---|
| 1 | `b"3 1 2 3"` tokens `[3,1,2,3]` | 0 | `nxt()` → "3" | n = 3 |
| 2 | same | 1 | `nxt()` → "1" | arr[0]=1 |
| 3 | same | 2 | `nxt()` → "2" | arr[1]=2 |
| 4 | same | 3 | `nxt()` → "3" | arr[2]=3 |

**Complexity:** O(total input size) for reading; O(1) amortized per token fetch.

**Common mistakes:**
- Forgetting `input = sys.stdin.readline` leaves a trailing `\n` — always `.strip()` when reading strings (not needed for `int()`/`split()`).
- Mixing `input()` and `sys.stdin` reads in the same program — pick one and commit.

### 2.2 Fast Output

**Why it matters:** `print()` calls flush per call by default in some environments and carry formatting overhead. For 10^5+ lines of output, batch it.

```python
import sys

out = []
for i in range(n):
    out.append(str(results[i]))
sys.stdout.write("\n".join(out) + "\n")
```

**Contest tip:** Never call `print()` inside a hot loop with 10^5+ iterations. Always accumulate into a list and join once.

### 2.3 Recursion Limit & Recursion-Heavy Problems

Python's default recursion limit is ~1000. DFS on a graph/tree with 10^5 nodes will crash with `RecursionError` unless raised.

```python
import sys
sys.setrecursionlimit(1 << 25)          # raise the ceiling
threading.stack_size(1 << 27)           # (if using a thread) raise the OS-level stack size too
```

**Warning:** Raising `sys.setrecursionlimit` alone is not always enough — the *OS thread stack* can still overflow and crash the interpreter (a silent, non-Python-catchable crash). The robust pattern is to run your recursive solution inside a new thread with a larger stack:

```python
import sys, threading

def solve():
    # your recursive DFS here
    pass

def main():
    sys.setrecursionlimit(1 << 25)
    threading.stack_size(1 << 27)
    t = threading.Thread(target=solve)
    t.start()
    t.join()

main()
```

**Contest tip:** When in doubt, convert deep recursion to **iterative DFS with an explicit stack** — it sidesteps recursion-limit issues entirely and is often faster in Python.

### 2.4 The Essential Library Toolkit

| Module | Key Tools | CP Use Case |
|---|---|---|
| `sys` | `stdin`, `stdout`, `setrecursionlimit` | Fast I/O, deep recursion |
| `math` | `gcd`, `isqrt`, `comb`, `factorial`, `log2`, `inf` | Number theory, combinatorics |
| `collections` | `deque`, `Counter`, `defaultdict`, `OrderedDict` | Queues, frequency maps, adjacency lists |
| `heapq` | `heappush`, `heappop`, `heapify`, `nlargest/nsmallest` | Priority queues, Dijkstra, greedy scheduling |
| `bisect` | `bisect_left`, `bisect_right`, `insort` | Binary search on sorted arrays, coordinate compression |
| `itertools` | `permutations`, `combinations`, `product`, `accumulate`, `groupby`, `pairwise` | Brute force enumeration, prefix sums |
| `functools` | `lru_cache`, `cache`, `reduce`, `cmp_to_key` | Memoized recursion, custom sort comparators |
| `functools.cache` | unbounded memo cache (3.9+) | Simpler syntax than `lru_cache(None)` |
| `array` | typed arrays | Lower memory footprint vs list |
| `statistics` | `median`, `mean` | Rarely, but occasionally needed directly |
| `random` | `randint`, `shuffle` | Anti-hash-test defense, randomized algorithms |
| `operator` | `add`, `mul`, `itemgetter` | Custom sort keys, `reduce` operations |
| `string` | `ascii_lowercase`, etc. | String/char-set problems |

### 2.5 Key Idioms with Examples

**`collections.Counter` — frequency counting in O(n):**
```python
from collections import Counter
freq = Counter(arr)          # {value: count}
most_common_3 = freq.most_common(3)
```

**`collections.defaultdict` — adjacency lists without KeyError:**
```python
from collections import defaultdict
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
```

**`heapq` — min-heap (Python only has min-heap; negate for max-heap):**
```python
import heapq
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
smallest = heapq.heappop(h)          # 1

max_heap = []
heapq.heappush(max_heap, -5)         # negate to simulate max-heap
largest = -heapq.heappop(max_heap)
```

**`bisect` — O(log n) search on sorted data:**
```python
import bisect
arr = [1, 3, 3, 5, 8]
i = bisect.bisect_left(arr, 3)   # 1  (leftmost insertion point)
j = bisect.bisect_right(arr, 3)  # 3  (rightmost insertion point)
bisect.insort(arr, 4)            # keeps arr sorted, O(n) due to shifting
```

**`itertools.accumulate` — prefix sums in one line:**
```python
from itertools import accumulate
prefix = list(accumulate(arr))                       # running sum
prefix_max = list(accumulate(arr, func=max))          # running max
prefix_with_zero = list(accumulate(arr, initial=0))   # prefix[0] = 0 convention
```

**`functools.lru_cache` / `cache` — memoized recursive DP:**
```python
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```
**Warning:** `lru_cache` requires hashable arguments — lists/dicts won't work; convert to tuples.

**`itertools.pairwise` (3.10+) — adjacent pairs without manual indexing:**
```python
from itertools import pairwise
for a, b in pairwise([1, 2, 4, 7]):
    print(b - a)     # differences: 1, 2, 3
```

### 2.6 Python Performance Tricks

| Trick | Why it helps |
|---|---|
| Use local variables inside hot loops (`x = obj.attr` before loop) | Attribute/global lookups are slower than local variable access |
| Prefer list comprehensions over manual `for` + `append` | Comprehensions are compiled to faster bytecode |
| Use `sys.stdin`/`sys.stdout` over `input()`/`print()` | Avoids per-call overhead |
| Avoid deep recursion; convert to iteration where hot | Python function calls have high overhead |
| Use `map(int, line.split())` for row parsing | Faster than list comprehension for pure type conversion |
| Use `array` or `numpy` for huge numeric arrays | Lower memory, vectorized ops |
| Avoid repeated `len()` calls inside loops if trivially cacheable | Micro-optimization, matters at 10^7+ iterations |
| Use `%`-free modular code where possible (precompute) | Modulo is relatively expensive at high iteration counts |
| String building: use `"".join(list)` not `+=` in a loop | `+=` on strings is O(n) per op → O(n²) total; join is O(n) |

### 2.7 Memory Optimization

- Prefer `array('i', ...)` over `list` for large homogeneous integer arrays (4–8x less memory).
- Use generators (`(x for x in ...)`) instead of list comprehensions when you only need to iterate once.
- Delete large intermediate structures (`del big_list`) before recursing/allocating more, if memory limit is tight.
- Careful with recursion depth × frame size — each Python stack frame is expensive in memory too.

---
## 3. The Problem-Solving Framework

Every strong competitive programmer follows some version of this loop, whether consciously or not. Making it explicit turns "talent" into "process."

```
┌───────────────────────────────────────────────────────────────┐
│                 THE CP PROBLEM-SOLVING LOOP                    │
│                                                                 │
│   READ ──▶ EXTRACT CONSTRAINTS ──▶ BRUTE FORCE (mentally)       │
│    ▲                                        │                  │
│    │                                        ▼                  │
│  RE-READ                            OBSERVE PATTERNS            │
│  (if stuck)                                 │                  │
│    │                                        ▼                  │
│    │                              MAP TO KNOWN TECHNIQUE        │
│    │                                        │                  │
│    │                                        ▼                  │
│    │                              PROVE / CONVINCE YOURSELF     │
│    │                                        │                  │
│    │                                        ▼                  │
│    └────────────────────────────  DRY RUN ON PAPER              │
│                                             │                  │
│                                             ▼                  │
│                                        CODE IT                 │
│                                             │                  │
│                                             ▼                  │
│                                    TEST: SAMPLE + EDGE CASES     │
│                                             │                  │
│                                             ▼                  │
│                                          SUBMIT                │
└───────────────────────────────────────────────────────────────┘
```

### 3.1 Reading the Problem (Properly)

- Read the **whole** statement once without solving — many people jump to coding after skimming and miss a constraint that changes everything.
- Identify: input format, output format, special conditions ("if no solution exists, print -1"), and whether it's interactive.
- Re-read the **sample explanation** — it often reveals the intended approach implicitly.

**Contest tip:** If a problem "feels" like standard DP/greedy but the numbers don't add up, re-read — you likely missed a constraint (e.g., "sum of N over all test cases ≤ 2·10^5" changes complexity budgets entirely).

### 3.2 Identifying Constraints (The Most Important Skill in CP)

Constraints are a *direct hint* at intended complexity. This is arguably the highest-leverage skill in this entire handbook.

| N (input size) | Expected complexity | Typical technique family |
|---|---|---|
| ≤ 10–12 | O(2^N), O(N!) | Brute force, bitmask DP, permutations |
| ≤ 20–24 | O(2^N · N) | Bitmask DP, meet in the middle |
| ≤ 500 | O(N³) | Floyd-Warshall, simple DP over pairs |
| ≤ 5,000 | O(N²) | Nested loops, O(N²) DP |
| ≤ 10^5 | O(N log N) | Sorting, binary search, segment tree, heap |
| ≤ 10^6 | O(N) or O(N log N) | Two pointers, sieve, prefix sums, linear DP |
| ≤ 10^7–10^8 | O(N) with tiny constant | Sieve-like loops, simple array scans |
| ≥ 10^9 (value, not count) | O(log N) or O(√N) | Binary search, math formulas, number theory |

**Contest tip:** Always check the constraints *before* thinking about approach — it prunes 80% of the wrong-direction thinking immediately.

### 3.3 Observation Building

Most CP problems (especially Div 2 C–E, or "constructive" problems) are solved not by knowing an algorithm, but by **building small true observations** until they compose into a solution.

**Process:**
1. Try tiny cases by hand (N=1, 2, 3).
2. Look for monotonicity ("as X increases, does the answer only increase/decrease?").
3. Look for invariants (something that stays constant no matter what).
4. Ask: "What's the greedy choice at each step, and can I prove it doesn't lose generality?"

### 3.4 Brute Force First — Always

Writing the O(N²) or O(2^N) brute force first:
- Confirms you understand the problem.
- Gives you a **reference implementation** to stress-test your optimized solution against.
- Sometimes brute force IS the intended solution (check constraints!).

```python
def brute_force(arr):
    n = len(arr)
    best = 0
    for i in range(n):
        for j in range(i, n):
            # evaluate subarray arr[i..j] naively
            best = max(best, sum(arr[i:j+1]))
    return best
```

### 3.5 The Optimization Process

Once brute force works, ask in order:
1. Can I **precompute** something (prefix sums, sorted order) to avoid recomputation?
2. Can I use **two pointers / sliding window** because of monotonicity?
3. Can I **binary search** the answer instead of computing it directly?
4. Can I trade a nested loop for a **hash map / set** lookup?
5. Can I use a **different data structure** (heap, BIT, segment tree) to maintain the needed aggregate in log time?
6. Can I **reduce state space** (DP dimension reduction, bitmask compression)?

### 3.6 Proof of Correctness (Contest-Level, Not Formal)

You don't need a formal proof in a contest — you need **enough conviction** that a greedy/observation-based solution won't fail. Techniques:
- **Exchange argument**: show that swapping any two adjacent choices doesn't improve the answer.
- **Small counterexample hunting**: try to break your own idea with N=2,3,4 before trusting it.
- **Look at extremes**: does it still work at the boundary values in the constraints?

### 3.7 Edge Case Analysis Checklist

- N = 0 or N = 1
- All elements equal
- Already sorted / reverse sorted
- Negative numbers (if allowed)
- Empty string / empty array
- Overflow-prone sums (less of an issue in Python, but relevant for the *conceptual* modulo/overflow logic you'd need in C++, and Python big-int slowness)
- Multiple test cases with cumulative N constraint ("sum of N ≤ 2×10^5")
- Ties in comparisons / sorting
- Self-loops / duplicate edges in graphs
- Disconnected graph components

### 3.8 Dry Run Before Coding

Always trace your algorithm on the **provided sample** by hand before typing code. This catches conceptual bugs before they become syntax bugs, and it's far faster to fix a wrong idea on paper than in a debugger.

---
## 4. Complexity Optimization

### 4.1 The Core Skill: Recognizing the Complexity Ceiling

Given a time limit (usually 1–2 seconds) and Python's rough throughput of **~10^7–10^8 simple operations/second**, you can back-calculate the required complexity from N.

```
┌───────────────────────────────────────────────────────────┐
│           COMPLEXITY BUDGET ESTIMATOR (Python, ~1-2s TL)   │
├───────────────────────────────────────────────────────────┤
│ N ≈ 10        → up to O(N!) / O(2^N · N) fine               │
│ N ≈ 20        → O(2^N) fine, O(N!) too slow                 │
│ N ≈ 500       → O(N^3) fine (~1.25×10^8)                    │
│ N ≈ 5,000     → O(N^2) fine (~2.5×10^7)                     │
│ N ≈ 10^5      → O(N log N) needed                           │
│ N ≈ 10^6      → O(N) or O(N log N) with small constant       │
│ N ≈ 10^7-10^8 → O(N) with very tight constant (numpy/PyPy)   │
└───────────────────────────────────────────────────────────┘
```

**Contest tip:** Because of Python's overhead, when C++ solutions target O(N log N) at N=10^6, you often need to shave a further constant factor in Python — via `sys.stdin`, avoiding per-element function-call overhead, or vectorizing with `numpy`.

### 4.2 O(N²) → O(N log N): Classic Transformations

| Original O(N²) pattern | O(N log N) fix |
|---|---|
| For each element, scan all others for a pair sum | Sort + two pointers |
| For each pair (i,j), check if a range condition holds | Sort by one dimension, then use BIT/sorted structure for the other |
| For each query, scan whole array | Precompute prefix sums / sparse table for O(1)–O(log N) queries |
| For each element, find nearest greater/smaller by brute force | Monotonic stack (O(N) total) |
| Count inversions via nested loop | Merge sort counting / BIT-based counting |

**Example — count pairs with sum == target:**
```python
def count_pairs_bruteforce(arr, target):        # O(N^2)
    n, count = len(arr), 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count

def count_pairs_fast(arr, target):               # O(N) using hashmap
    from collections import defaultdict
    seen = defaultdict(int)
    count = 0
    for x in arr:
        count += seen[target - x]
        seen[x] += 1
    return count
```

**Dry run (fast version), arr = [1,5,3,3,2], target = 6:**

| x | target-x | seen[target-x] before update | count so far | seen after update |
|---|---|---|---|---|
| 1 | 5 | 0 | 0 | {1:1} |
| 5 | 1 | 1 | 1 | {1:1, 5:1} |
| 3 | 3 | 0 | 1 | {1:1,5:1,3:1} |
| 3 | 3 | 1 | 2 | {1:1,5:1,3:2} |
| 2 | 4 | 0 | 2 | {1:1,5:1,3:2,2:1} |

Final count = 2 → pairs (1,5) and (3,3).

### 4.3 O(2^N) → Polynomial: Meet in the Middle & DP

When N ≤ 40 but too large for full 2^N (e.g., N=35), **split the set in half** and combine — reduces 2^N to 2·2^(N/2), which is enormous savings. (Full technique detailed in §6.2.)

When the exponential blowup comes from *overlapping subproblems* (not truly independent choices), **memoize** — this converts O(2^N) recursion into O(states × transition) DP.

### 4.4 Time vs. Space Trade-offs

| Situation | Trade space for time | Trade time for space |
|---|---|---|
| Repeated range-sum queries | Precompute prefix sum array (O(N) space, O(1) query) | Recompute each time (O(1) space, O(N) query) |
| DP over (i, j) states | Full 2D table | Rolling array if only previous row needed |
| Repeated "is X visited" checks | Boolean array / set (O(N) space, O(1) check) | Linear scan (O(1) space, O(N) check) |
| Combinatorics with repeated nCr | Precompute factorials + inverse factorials mod p | Compute nCr from scratch each call (slow) |

### 4.5 Amortized Thinking

Some operations look expensive per-call but are cheap **on average across the whole algorithm**. Recognizing amortized O(1)/O(N) behavior prevents you from wrongly rejecting an approach as "too slow."

- **Two pointers**: each pointer moves forward at most N times total across the whole loop → O(N) overall, even though it "looks like" nested loops.
- **Monotonic stack**: each element is pushed and popped at most once → O(N) total despite the inner `while` loop.
- **Union-Find with path compression + union by rank**: O(α(N)) per operation, practically O(1).
- **Dynamic array (Python list) `.append()`**: amortized O(1) due to geometric over-allocation, even though occasional resizes are O(N).

### 4.6 Constraint Analysis Practice Table

| Constraint given | What it's telling you |
|---|---|
| "1 ≤ N ≤ 18" | Bitmask DP over subsets (2^18 ≈ 262144) |
| "sum of N over all test cases ≤ 2×10^5" | Per-test-case complexity can be O(N) or O(N log N), NOT O(N) per test case naively multiplied by T |
| "1 ≤ A_i ≤ 10^9" | Values need hashing/coordinate compression before array-indexing by value |
| "Q ≤ 10^5 queries, N ≤ 10^5" | Need O(log N) per query → segment tree / BIT / binary search |
| "N ≤ 10^3, Q ≤ 10^3" | O(N·Q) or O(N²) per query might be fine |
| Special note: "It is guaranteed a solution exists" | You can skip -1/no-solution handling logic |

---
## 5. Pattern Recognition

This section teaches **recognition only** — spotting which family a problem belongs to from its shape and constraints. (Deep teaching of these DS/algorithms belongs in a separate handbook.)

### 5.1 The Master Pattern-Recognition Map

```
┌────────────────────────────────────────────────────────────────────┐
│                    PATTERN RECOGNITION MAP                          │
├────────────────────────────────────────────────────────────────────┤
│ "Subarray/substring with condition"                                  │
│    ├─ contiguous + monotonic condition ──────▶ Sliding Window        │
│    ├─ contiguous + sum/count queries ────────▶ Prefix Sum            │
│    └─ two ends moving inward, sorted ────────▶ Two Pointers          │
│                                                                       │
│ "Find pair/triple satisfying condition" ─────▶ Two Pointers / Hashing│
│                                                                       │
│ "Find k-th smallest / search over answer" ───▶ Binary Search          │
│                                                                       │
│ "Optimal local choice leads to optimal global"─▶ Greedy               │
│                                                                       │
│ "Overlapping subproblems, optimal substructure"▶ DP                   │
│                                                                       │
│ "Connectivity, shortest path, components" ────▶ Graph (BFS/DFS/       │
│                                                   Dijkstra/Union-Find) │
│                                                                       │
│ "Hierarchical / parent-child relationships" ──▶ Tree algorithms        │
│                                                                       │
│ "Prefix matching over many strings" ──────────▶ Trie                  │
│                                                                       │
│ "Repeatedly need current min/max" ────────────▶ Heap                  │
│                                                                       │
│ "Next greater/smaller element" ───────────────▶ Monotonic Stack        │
│                                                                       │
│ "Sliding min/max in a window" ────────────────▶ Monotonic Deque        │
│                                                                       │
│ "Small N (≤20), subset-based decisions" ──────▶ Bitmask DP             │
│                                                                       │
│ "Split problem into independent halves" ──────▶ Divide & Conquer       │
│                                                                       │
│ "Number theory flavored (gcd, primes, mod)" ──▶ Math                   │
│                                                                       │
│ "Just simulate what's described" ─────────────▶ Simulation             │
│                                                                       │
│ "Build/construct something satisfying rules" ─▶ Constructive           │
│                                                                       │
│ "You query the judge, judge responds" ────────▶ Interactive            │
└────────────────────────────────────────────────────────────────────┘
```

### 5.2 Quick Recognition Signals

| Signal in problem statement | Likely technique |
|---|---|
| "maximum/minimum length subarray such that..." | Sliding Window |
| "number of subarrays with sum/property X" | Prefix Sum + Hashmap |
| "sorted array, find pair/triplet" | Two Pointers |
| "smallest value such that condition holds" | Binary Search on Answer |
| "minimum coins / minimum jumps / ways to reach" | DP |
| "connect / group / cluster elements" | Union-Find or Graph traversal |
| "next greater element" / "largest rectangle" | Monotonic Stack |
| "N ≤ 20" alongside "subset" | Bitmask DP |
| "range update, range query" | Segment Tree / BIT / Difference Array |
| "queries can be answered offline" | Sort queries + sweep, or Mo's Algorithm |
| "you don't know the full input; must respond after each query" | Interactive |
| "construct any valid answer" | Constructive Algorithms |
| "counts modulo 10^9+7" | Combinatorics / DP with modular arithmetic |
| "game, two players play optimally" | Game Theory (Grundy numbers, parity argument) |

### 5.3 Pattern Recognition Practice: Walk-Throughs

**Example 1:** *"Given an array, find the length of the longest subarray with at most K distinct elements."*
- Keywords: "subarray", "at most K" (monotonic constraint that shrinks/grows a window) → **Sliding Window**.

**Example 2:** *"Given N points, answer Q queries: how many points lie within rectangle (x1,y1)-(x2,y2), where all queries are known in advance."*
- Keywords: "queries known in advance" → **Offline processing**; "2D range count" → sort + **Fenwick Tree** (BIT) sweep, i.e., **Sweep Line + BIT**.

**Example 3:** *"N ≤ 18, each city has a cost to visit and depends on which cities were visited before it."*
- Keywords: N ≤ 18 + subset dependency → **Bitmask DP** (Traveling-Salesman-style).

**Example 4:** *"You may ask up to 20 queries of the form '?  x' and must guess a hidden number."*
- Keywords: "may ask queries", hidden judge state → **Interactive problem**, likely **Binary Search** under the hood.

---
## 6. Competitive Programming Techniques

This is the core toolbox chapter. Each technique includes definition, intuition, template, dry run, complexity, and pitfalls.

### 6.1 Coordinate Compression

**Definition:** Replace large/sparse values with their rank in sorted order, so you can index arrays by "position" instead of raw value.

**Why it matters:** Values can be up to 10^9, but you only ever care about their *relative order*. Compressing lets you use arrays/BITs/segment trees indexed 0..N-1 instead of needing a hashmap or huge array.

**Intuition / analogy:** Like converting "houses numbered 1, 45, 1002, 5,000,000 on a street" into "1st, 2nd, 3rd, 4th house" — you only need relative position to reason about order.

```
Original:  [50, 10, 40, 10, 30]
Sorted+Unique: [10, 30, 40, 50]
Compressed:    [3,   0,  2,  0,  1]   (rank of each element)
```

**Template:**
```python
def compress(arr):
    sorted_unique = sorted(set(arr))
    rank = {v: i for i, v in enumerate(sorted_unique)}
    return [rank[x] for x in arr], sorted_unique

arr = [50, 10, 40, 10, 30]
compressed, mapping = compress(arr)
# compressed = [3, 0, 2, 0, 1]
# mapping[i] gives back original value for rank i
```

**Line-by-line:** `sorted(set(arr))` dedups and sorts in O(N log N). `rank` dict maps value→index in O(N). Final list comprehension re-maps in O(N).

**Dry run:** table above — arr[0]=50 is the 4th smallest distinct value → rank 3 (0-indexed).

**Complexity:** O(N log N) time (dominated by sort), O(N) space.

**Edge cases:** Duplicate values (handled via `set`), negative numbers (works fine, order-based), need to map *back* to original values for output (`mapping[i]`).

**Common mistakes:** Forgetting to deduplicate before ranking (causes off-by-one gaps); using compressed ranks in final output instead of mapping back.

**Contest tip:** Coordinate compression is almost always a *preprocessing step*, not the whole solution — pair it with BIT/segment tree/DP over ranks.

**Applications:** 2D range queries, counting inversions, DP over compressed coordinates (e.g., "longest increasing subsequence of compressed values"), sweep line algorithms.

---

### 6.2 Meet in the Middle

**Definition:** Split a problem of size N into two halves of size N/2, brute-force each half independently, then combine results — turning O(2^N) into O(2^(N/2)).

**Why it matters:** When N is too large for full brute force (N=30–40) but too "combinatorial" for polynomial DP, this is often the only way.

**Intuition:** Instead of enumerating all 2^40 subsets, enumerate 2^20 subsets of each half (≈10^6 each) and combine smartly (sort + binary search, or hashmap).

```
┌───────────────────────────────────────────────┐
│      MEET IN THE MIDDLE — SPLIT & COMBINE       │
│                                                 │
│   Full set (N=40)                              │
│   ┌───────────────┬───────────────┐             │
│   │ Left half(20) │ Right half(20)│             │
│   └───────┬───────┴───────┬───────┘             │
│           │                │                    │
│    enumerate 2^20     enumerate 2^20             │
│    subset sums        subset sums                │
│           │                │                    │
│           └──── combine ───┘                     │
│           (sort one, binary search other)         │
└───────────────────────────────────────────────┘
```

**Template — subset-sum closest to target:**
```python
from itertools import combinations
import bisect

def all_subset_sums(arr):
    n = len(arr)
    sums = []
    for r in range(n + 1):
        for combo in combinations(arr, r):
            sums.append(sum(combo))
    return sums

def meet_in_middle_best_sum(arr, target):
    n = len(arr)
    left, right = arr[:n // 2], arr[n // 2:]
    left_sums = sorted(all_subset_sums(left))
    right_sums = sorted(all_subset_sums(right))

    best = float('-inf')
    for ls in left_sums:
        remaining = target - ls
        # find right_sum closest to `remaining` without exceeding target
        pos = bisect.bisect_right(right_sums, remaining) - 1
        if pos >= 0:
            best = max(best, ls + right_sums[pos])
    return best
```

**Line-by-line:** We split `arr` into two halves; `all_subset_sums` enumerates every subset sum of a half in O(2^(N/2)); we sort the right half's sums so each left-half sum can binary-search for the best complement in O(log(2^(N/2))).

**Dry run:** `arr=[3,4,5,6], target=10`. Left=[3,4] → sums {0,3,4,7}. Right=[5,6] → sums {0,5,6,11} sorted [0,5,6,11].
For ls=7: remaining=3 → bisect_right finds pos before value 5 → pos=0 → right_sums[0]=0 → candidate=7.
For ls=4: remaining=6 → pos where right_sums≤6 → index of 6 → candidate=4+6=10. ✅ Best=10.

**Complexity:** O(2^(N/2) log(2^(N/2))) time, O(2^(N/2)) space — feasible for N up to ~40.

**Common mistakes:** Forgetting to sort before binary search; not handling the "no valid combination" case (pos = -1).

**Contest tip:** Look for "N ≤ 40" as the classic meet-in-the-middle signal (too big for 2^N, too small/awkward for polynomial DP).

**Applications:** Subset sum near a target, counting subsets with XOR/sum conditions, 4-SUM problems, some knapsack variants with huge weight ranges but small N.

---

### 6.3 Sweep Line

**Definition:** Process geometric or interval-based events in sorted order (usually by x-coordinate or time), maintaining a running data structure that reflects "what's currently active."

**Why it matters:** Converts 2D or interval problems into a 1D problem processed left-to-right, often turning O(N²) into O(N log N).

**Intuition / analogy:** Imagine a vertical line sweeping left to right across a set of intervals on a timeline — at each event (interval start/end), you update your "currently active" set.

```
Intervals:  [1----4]      [3--------7]
                  [2----5]
Sweep:  1  2  3  4  5  6  7
Active: 1  2  3  3  2  1  0   <- count of overlapping intervals at each point
              ^--- max overlap = 3 at x=3..4
```

**Template — maximum overlapping intervals:**
```python
def max_overlap(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))     # +1 when an interval starts
        events.append((end, -1))      # -1 when an interval ends
    events.sort(key=lambda e: (e[0], e[1]))  # process ends before starts on ties if needed

    current = best = 0
    for _, delta in events:
        current += delta
        best = max(best, current)
    return best
```

**Line-by-line:** Every interval contributes two "events" — a `+1` at its start and `-1` at its end. Sorting by position (with tie-break rules depending on whether touching endpoints count as overlapping) lets us sweep through in order, maintaining a running counter of active intervals.

**Dry run:** intervals=[(1,4),(3,7),(2,5)] → events sorted: (1,+1),(2,+1),(3,+1),(4,-1),(5,-1),(7,-1). Running current: 1,2,3,2,1,0 → best=3.

**Complexity:** O(N log N) (dominated by sort).

**Edge cases:** Touching intervals (e.g., [1,3] and [3,5]) — decide via tie-break whether they "overlap" at the shared point; empty interval list; single interval.

**Common mistakes:** Wrong tie-break order between `-1` and `+1` events at the same coordinate (causes off-by-one overlap counts).

**Contest tip:** Sweep line pairs extremely well with **Fenwick Tree / segment tree** when you need more than a simple counter (e.g., "count points inside range at each sweep step").

**Variations:** Sweep by angle (rotational sweep in computational geometry), sweep by time for "meeting room" scheduling problems, 2D sweep with a segment tree over the y-axis (classic rectangle-union-area problem).

**Applications:** Interval scheduling, skyline problem, rectangle union area, closest pair of points (with a sliding strip).

---
### 6.4 Difference Array

**Definition:** A technique to apply O(1) range updates (add value V to range [l, r]) and recover the final array in O(N) with a single prefix-sum pass, instead of O(N) per update.

**Why it matters:** Naive range update is O(N) per update → O(N·Q) total. Difference array makes each update O(1), total O(N + Q).

**Intuition:** Instead of updating every element in a range, just record "a change of +V starts here" and "a change of -V starts right after the range ends." Taking a prefix sum later reconstructs the effect.

```
Array (0-indexed), N=6.  Update: add 5 to range [1,3]

diff:      [0, +5,  0,  0, -5,  0]
                 ^ start          ^ cancel after index 3

prefix sum of diff → actual added values:
           [0,  5,  5,  5,  0,  0]
```

**Template:**
```python
def range_update_diff_array(n, updates):
    diff = [0] * (n + 1)
    for l, r, v in updates:              # add v to arr[l..r] inclusive
        diff[l] += v
        diff[r + 1] -= v
    # reconstruct final array via prefix sum
    result = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]
        result[i] = running
    return result
```

**Line-by-line:** `diff` has one extra slot to safely apply the "cancel" at `r+1` even when `r == n-1`. Each update touches only 2 indices. The final loop accumulates `running` to materialize actual values — this is exactly a prefix sum.

**Dry run:** n=6, updates=[(1,3,5)]. diff=[0,5,0,0,-5,0,0]. Prefix pass: running after each i: i=0→0, i=1→5, i=2→5, i=3→5, i=4→0, i=5→0. result=[0,5,5,5,0,0]. ✅ matches diagram.

**Complexity:** O(N + Q) total instead of O(N·Q).

**Edge cases:** `r == n-1` (must still write to `diff[n]`, hence array of size n+1); overlapping updates (they simply add, which is correct since diff arrays are linear).

**Common mistakes:** Forgetting the `+1` sized array (index-out-of-range or losing the cancellation); applying diff logic to *range assignment* instead of *range addition* (assignment needs a different technique, e.g., segment tree with lazy propagation).

**Contest tip:** Difference array is the "poor man's segment tree" for **range-add, single final query** (not for range-add-with-intermediate-queries — use a Fenwick tree with two BITs or segment tree with lazy propagation for that).

**Variations:** 2D difference array (for range-add on a submatrix, reconstruct via 2D prefix sum); difference array combined with binary search on answer for "can we achieve X with these operations" problems.

**Applications:** Bulk range-add operations (e.g., "N people board/leave a bus between stations, find max passengers at once"), CSES "Room Allocation"-style problems.

---

### 6.5 Prefix Sum Tricks (Contest-Level, Beyond Basics)

Beyond plain prefix sums, contest problems frequently need:

- **Prefix XOR** — for subarray-XOR-equals-K problems, using the identity `XOR(l,r) = prefix[r] ^ prefix[l-1]`.
- **Prefix count of a property** (e.g., prefix count of odd numbers) to answer "count of subarrays with even sum" via hashmap of prefix-parities.
- **2D prefix sums** for submatrix sum queries in O(1) after O(N·M) preprocessing.

```python
# Subarrays with XOR == K
from collections import defaultdict
def count_subarrays_xor_k(arr, k):
    freq = defaultdict(int)
    freq[0] = 1
    prefix_xor = 0
    count = 0
    for x in arr:
        prefix_xor ^= x
        count += freq[prefix_xor ^ k]
        freq[prefix_xor] += 1
    return count
```

**Contest tip:** Whenever you see "subarray sum/xor equals K", think "prefix + hashmap," not nested loops.

---

### 6.6 Monotonic Stack / Monotonic Queue Usage

**Definition:** A stack (or deque) that is kept strictly increasing or decreasing, used to efficiently answer "next greater/smaller element" style queries in O(N) total.

**Why it matters:** Naively finding, for every element, the next greater element to its right is O(N²). A monotonic stack does it in O(N) because each element is pushed/popped at most once.

**Intuition:** As you scan left to right, pop off any stack elements that are "dominated" (smaller than current, if looking for next-greater) — they can never be the answer for anything after this point, so discard them permanently.

```
arr = [2, 1, 5, 3, 4]
Find "next greater element" for each:

i=0 (2): stack=[]        push 2         stack=[2]
i=1 (1): 1<2, push       stack=[2,1]
i=2 (5): 5>1 pop(1)→ans[1]=5
         5>2 pop(2)→ans[0]=5
         push 5          stack=[5]
i=3 (3): 3<5, push       stack=[5,3]
i=4 (4): 4>3 pop(3)→ans[3]=4
         4<5, push       stack=[5,4]
remaining stack elements → no next greater → -1
ans = [5, 5, -1, 4, -1]
```

**Template:**
```python
def next_greater_element(arr):
    n = len(arr)
    ans = [-1] * n
    stack = []                      # holds indices, values decreasing bottom→top
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            j = stack.pop()
            ans[j] = arr[i]
        stack.append(i)
    return ans
```

**Complexity:** O(N) total — each index is pushed once and popped at most once, so total stack operations ≤ 2N.

**Common mistakes:** Using `<=` instead of `<` (changes behavior for duplicate values — decide based on whether you want "strictly greater" or "greater or equal"); storing values instead of indices when you need positions for later computation (e.g., "distance to next greater").

**Contest tip:** Monotonic stack is the standard tool for: largest rectangle in histogram, trapping rain water, stock span problem, next greater/smaller in circular array (traverse array twice).

**Monotonic Deque (sliding window min/max):**
```python
from collections import deque

def sliding_window_max(arr, k):
    dq = deque()      # stores indices, values decreasing front→back
    result = []
    for i, x in enumerate(arr):
        while dq and arr[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:          # index out of window
            dq.popleft()
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result
```

**Contest tip:** Sliding window max/min via monotonic deque is O(N) vs. O(N·K) for a naive heap-per-window approach, and avoids the "lazy deletion" complexity of using a heap directly.

---
### 6.7 State Compression (Bitmask Techniques)

**Definition:** Encode a set of booleans (e.g., "which items are chosen") as bits of an integer, enabling fast set operations (union, intersection, membership) via bitwise operators, and enabling DP over subsets.

**Why it matters:** When N ≤ ~20, "which subset of items has been used" is a natural DP dimension — represented compactly as an integer 0 to 2^N-1.

**Intuition / analogy:** A row of N light switches, each on/off, can be represented as one N-bit number instead of an array of N booleans — checking/toggling any switch becomes an O(1) bit operation.

```
N=4 items. Subset {item0, item2} → bits: 0101 → decimal 5

Bit tricks:
  check if item i is in mask:      mask & (1 << i)
  add item i to mask:              mask | (1 << i)
  remove item i from mask:         mask & ~(1 << i)
  iterate all subsets of mask:     sub = mask; while sub: ...; sub = (sub-1) & mask
```

**Template — Traveling Salesman via Bitmask DP:**
```python
def tsp(dist):
    n = len(dist)
    FULL = 1 << n
    INF = float('inf')
    # dp[mask][i] = min cost to have visited exactly `mask`, currently at city i
    dp = [[INF] * n for _ in range(FULL)]
    dp[1][0] = 0                      # start at city 0, only city 0 visited

    for mask in range(FULL):
        for u in range(n):
            if dp[mask][u] == INF or not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue          # already visited
                new_mask = mask | (1 << v)
                new_cost = dp[mask][u] + dist[u][v]
                if new_cost < dp[new_mask][v]:
                    dp[new_mask][v] = new_cost

    return min(dp[FULL - 1][i] + dist[i][0] for i in range(n))
```

**Line-by-line:** `dp[mask][u]` means "cheapest way to have visited exactly the cities in `mask`, ending at city `u`." We transition by trying to extend to any unvisited city `v`. Final answer closes the tour back to city 0.

**Dry run (n=3, tiny distances):** With `dist=[[0,1,2],[1,0,3],[2,3,0]]`, dp builds up mask=001 (just city0)→cost 0, then extends to mask=011 (cities0,1) at city1 cost=1, mask=101 (cities0,2) at city2 cost=2, then mask=111 combining both paths, finally closing the loop back to city 0. Final answer = 6 (path 0→1→2→0 or similar, whichever is cheapest).

**Complexity:** O(2^N · N²) time, O(2^N · N) space — practical for N ≤ ~18.

**Common mistakes:** Off-by-one in mask indexing (mask=1 means "only city 0 visited," not "no cities visited"); forgetting to check `mask & (1<<u)` before using `dp[mask][u]`.

**Contest tip:** N ≤ 20 combined with "order/subset dependency" is the classic bitmask-DP signal. Also used for "assignment problems" (assign N workers to N tasks) and "can we partition into K equal-sum subsets."

**Variations:** Submask enumeration (`for sub in submasks(mask)`) for O(3^N) subset-of-subset DP; profile DP (bitmask represents a "profile" of a DP frontier, common in grid tiling problems).

---

### 6.8 Binary Lifting (Recognition)

**Definition:** Precompute "2^k-th ancestor" jump tables in a tree so that any ancestor query (LCA, k-th ancestor, jumping up by an arbitrary distance) can be answered in O(log N) instead of O(N).

**When to recognize it:** "Find the k-th ancestor of a node," "find LCA (lowest common ancestor) of two nodes," repeated tree-ancestor queries with N and Q both up to 10^5.

```python
LOG = 20
def build_binary_lifting(n, parent):
    up = [[0] * n for _ in range(LOG)]
    up[0] = parent[:]                          # up[0][v] = direct parent of v
    for k in range(1, LOG):
        for v in range(n):
            up[k][v] = up[k-1][up[k-1][v]]      # jump 2^(k-1) then 2^(k-1) again
    return up

def kth_ancestor(up, v, k):
    for i in range(LOG):
        if k & (1 << i):
            v = up[i][v]
    return v
```

**Why it works:** Any integer k can be written as a sum of powers of 2 (its binary representation), so jumping by k = jumping by each set bit's power of 2 in sequence.

**Complexity:** O(N log N) preprocessing, O(log N) per query.

**Contest tip:** This is a *recognition-level* technique here — full LCA/tree-algorithm teaching belongs in the Trees/Graphs handbook. In CP, treat binary lifting as your "go-to" whenever you see repeated ancestor/jump queries on a static tree.

---

### 6.9 Euler Tour Technique

**Definition:** Flatten a tree into an array via a DFS traversal (recording entry/exit times), so that **subtree queries** become **contiguous range queries** on the flattened array — solvable with a segment tree/BIT.

**Why it matters:** "Update a value at node X, query the sum of all values in the subtree of node Y" is hard directly on a tree, but trivial once the tree is linearized.

```
Tree:            1
                / \
               2   3
              / \
             4   5

Euler tour (entry times): 1:[0], 2:[1], 4:[2], 5:[3], 3:[4]
Subtree(2) = nodes {2,4,5} = contiguous range [in[2], out[2]] in the tour array
```

**Template:**
```python
def euler_tour(n, graph, root=0):
    tin = [0] * n
    tout = [0] * n
    timer = 0
    stack = [(root, -1, False)]
    while stack:
        node, parent, processed = stack.pop()
        if processed:
            tout[node] = timer - 1
            continue
        tin[node] = timer
        timer += 1
        stack.append((node, parent, True))
        for nxt in graph[node]:
            if nxt != parent:
                stack.append((nxt, node, False))
    return tin, tout
```

**Complexity:** O(N) to build the tour; subsequent subtree-range queries are O(log N) with a BIT/segment tree on top.

**Contest tip:** Combine Euler Tour + BIT for "subtree sum update/query" problems; combine Euler Tour + sparse table (RMQ) for O(1) LCA queries.

---

### 6.10 Mo's Algorithm

**Definition:** An offline technique for answering many range queries `[l, r]` efficiently by sorting queries in a special order (block decomposition on `l`, then by `r`) so that the "current window" moves a total of O((N+Q)·√N) steps instead of O(N·Q).

**Why it matters:** For problems like "count distinct elements in range [l,r]" across many queries, where no simple prefix-sum trick applies (because the aggregate isn't easily invertible), Mo's Algorithm gives O((N+Q)√N) instead of O(N·Q).

**Intuition:** Sort queries so that "nearby" queries are processed consecutively — like solving a jigsaw puzzle by moving to touching pieces, minimizing how far the "current window" [l,r] has to shift.

```
┌───────────────────────────────────────────────────────┐
│                 MO'S ALGORITHM: BLOCK SORT              │
│                                                          │
│  Divide array of size N into blocks of size √N           │
│  Sort queries by (block of l, r) [with alternating       │
│  direction per block for the tie-break optimization]      │
│  Move current [L,R] window incrementally per query         │
│  add(x): extend window, remove(x): shrink window            │
└───────────────────────────────────────────────────────┘
```

**Template — count distinct elements in range queries:**
```python
def mos_algorithm(arr, queries):
    n = len(arr)
    block = max(1, int(n ** 0.5))

    def query_key(q):
        l, r, _ = q
        block_id = l // block
        return (block_id, r if block_id % 2 == 0 else -r)   # alternating sort trick

    indexed_queries = [(l, r, i) for i, (l, r) in enumerate(queries)]
    indexed_queries.sort(key=query_key)

    freq = {}
    distinct_count = 0
    answers = [0] * len(queries)
    cur_l, cur_r = 0, -1

    def add(x):
        nonlocal distinct_count
        freq[x] = freq.get(x, 0) + 1
        if freq[x] == 1:
            distinct_count += 1

    def remove(x):
        nonlocal distinct_count
        freq[x] -= 1
        if freq[x] == 0:
            distinct_count -= 1

    for l, r, idx in indexed_queries:
        while cur_r < r:
            cur_r += 1; add(arr[cur_r])
        while cur_l > l:
            cur_l -= 1; add(arr[cur_l])
        while cur_r > r:
            remove(arr[cur_r]); cur_r -= 1
        while cur_l < l:
            remove(arr[cur_l]); cur_l += 1
        answers[idx] = distinct_count

    return answers
```

**Line-by-line:** Queries are bucketed by block of `l`, sorted by `r` (alternating direction per block to avoid worst-case pointer thrashing). We maintain `[cur_l, cur_r]` and incrementally `add`/`remove` elements as we slide toward each query's `[l, r]`, tracking `distinct_count` via a frequency map.

**Complexity:** O((N + Q)·√N) time — a huge win over O(N·Q) naive re-scanning per query.

**Common mistakes:** Forgetting the alternating sort-direction trick (still correct, but ~2x slower in practice); off-by-one errors in the four `while` loops (very easy to get wrong — write them exactly symmetric as shown).

**Contest tip:** Mo's Algorithm is *offline only* — it cannot handle queries requiring immediate (online) answers, nor updates between queries (a variant, "Mo's with updates," exists but adds another √N factor).

**Applications:** Distinct-elements-in-range, range mode queries, range XOR-frequency problems, CSES "Distinct Values Queries."

---

### 6.11 Heavy-Light Decomposition & Small-to-Large Merging (Recognition)

**Heavy-Light Decomposition (HLD):** Decomposes a tree into chains such that any path query (path sum, path max, etc.) between two nodes touches only O(log N) chains, each answerable via a segment tree in O(log N) — total O(log²N) per path query.

**When to recognize it:** "Update/query along the path between two nodes in a tree," with N, Q up to 10^5. This is a heavier technique — in a contest, recognize the *need* for it, then apply a memorized or library template; the internals are usually not rederived live.

**Small-to-Large Merging (DSU on Tree):** When merging data structures (sets, maps, counts) associated with children into a parent, always merge the *smaller* structure into the *larger* one. This guarantees each element is "re-homed" O(log N) times total, giving O(N log N) overall instead of O(N²).

```python
# Conceptual skeleton for small-to-large merging
def dfs_merge(node, parent, graph, data):
    for child in graph[node]:
        if child == parent:
            continue
        dfs_merge(child, node, graph, data)
        if len(data[node]) < len(data[child]):
            data[node], data[child] = data[child], data[node]   # keep the bigger one
        data[node] |= data[child]        # merge smaller into bigger (set union)
    return data[node]
```

**Contest tip:** Both HLD and small-to-large are "recognition-level" here — know *when* a problem needs them ("path queries on a tree" → HLD; "aggregate subtree info efficiently across all nodes" → small-to-large / DSU on tree), and reach for a pre-written library template rather than deriving from scratch mid-contest.

---
### 6.12 Randomization in Competitive Programming

**Definition:** Deliberately introducing randomness — random pivots, random hashing bases, random shuffling — to defeat adversarial test cases or to build simple probabilistic algorithms.

**Why it matters:** Codeforces (and similar judges) often contain **anti-hash tests** specifically designed to break naive deterministic hashmaps/hash-based string algorithms. Randomization is your defense.

**Key use cases:**

1. **Defeating anti-hash tests on `dict`/`set` with integer keys:** Some problems are crafted so that Python's (or C++'s) default hash produces many collisions for adversarial input, causing an O(N) hashmap to degrade toward O(N²). Randomizing your hash function's "salt" (e.g., XOR every key with a random 64-bit constant before inserting) neutralizes this.
```python
import random
RANDOM_XOR = random.getrandbits(30)
def safe_key(x):
    return x ^ RANDOM_XOR
```
2. **Randomized pivot in quickselect/quicksort** to avoid worst-case O(N²) on adversarial/sorted input:
```python
import random
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))
```
3. **Randomized string hashing** (polynomial rolling hash with a random base/modulus) to avoid deliberately-crafted hash collisions in string-matching problems.
4. **Monte Carlo verification** — e.g., verifying polynomial identities or matrix equality by evaluating at random points instead of full computation.

**Contest tip:** If your hashmap-based solution mysteriously TLEs only on the last test case of a Codeforces problem, suspect an anti-hash test — add a random salt.

**Common mistakes:** Using `random.seed()` with a fixed seed (defeats the purpose — the adversary can then predict your "random" values if the seed is guessable, though in practice CP judges just need *some* randomness per-run).

---

### 6.13 Greedy Observations

**Definition:** Solving a problem by always making the locally-optimal choice at each step, relying on a proof (often an exchange argument) that local optimality implies global optimality.

**Why it matters:** Greedy is usually the *fastest possible* solution when it works (often O(N log N) for sorting + one pass), but it's also the technique most prone to **being wrong without a proof**.

**How to build a greedy observation:**
1. Sort by some key (very often the first step).
2. Process elements in that order, maintaining minimal state.
3. Try to justify: "if I ever deviate from this rule, I can show a swap that doesn't make things worse" (exchange argument).

**Classic example — Activity Selection (max non-overlapping intervals):**
```python
def max_activities(intervals):
    intervals.sort(key=lambda x: x[1])     # greedy key: sort by END time
    count = 0
    last_end = float('-inf')
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    return count
```
**Why sorting by end time works (exchange argument):** If an optimal solution picks an activity ending later when one ending earlier was available and compatible, swapping to the earlier-ending one never removes future options and can only free up more room — so "always take the earliest-ending compatible activity" is safe.

**Contest tip:** When you have a greedy idea, **stress test it against brute force on small random inputs** before trusting it in a contest — this is faster than trying to hand-prove it under time pressure.

**Common mistakes:** Choosing the wrong sort key (e.g., sorting by start time instead of end time in interval scheduling — a very common bug); assuming greedy works without any justification at all.

---

### 6.14 Case Analysis

**Definition:** Breaking a problem into an exhaustive set of mutually-exclusive cases (often based on parity, sign, or a small number of configurations), solving each case with a tailored (often O(1) or simple) rule.

**Why it matters:** Many "constructive" or "ad-hoc" problems (common in Div 2 B/C) are solved not by an algorithm, but by carefully enumerating: "what if N is even vs odd?", "what if all elements are equal?", "what if K=0?"

**Contest tip:** When stuck, explicitly write out: "Case 1: ___. Case 2: ___." on paper — this externalizes your reasoning and often reveals the missing case that was causing Wrong Answer.

**Common mistakes:** Missing a case (especially N=1, K=0, or "all same value"); cases that aren't actually mutually exclusive (double-counting).

---

### 6.15 Mathematical Observations

**Definition:** Recognizing a closed-form formula, invariant, parity argument, or number-theoretic property that replaces simulation/brute force entirely.

**Common recurring mathematical patterns in CP:**

| Pattern | Formula / Idea |
|---|---|
| Sum 1..N | N(N+1)/2 |
| Sum of squares 1..N | N(N+1)(2N+1)/6 |
| GCD/LCM relationship | `gcd(a,b) * lcm(a,b) == a*b` |
| Modular inverse (prime mod) | `pow(a, mod-2, mod)` via Fermat's little theorem |
| nCr mod p (large n) | Precompute factorials + modular inverse factorials |
| Parity invariant | Many "can we reach state X" problems reduce to a parity/XOR invariant that never changes |
| Pigeonhole argument | "N+1 items in N boxes → some box has ≥2" — used to bound answer existence |
| Sum of divisors / Euler's totient | Sieve-based precomputation for range queries |

**Template — modular combinatorics:**
```python
MOD = 10**9 + 7
MAXN = 2 * 10**5 + 10

fact = [1] * MAXN
for i in range(1, MAXN):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * MAXN
inv_fact[MAXN-1] = pow(fact[MAXN-1], MOD-2, MOD)
for i in range(MAXN-2, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD
```

**Contest tip:** Whenever you see "answer modulo 10^9+7" combined with counting, expect factorial/inverse-factorial precomputation — never compute factorials from scratch per query (too slow, and division under modulo isn't valid without modular inverse).

---

### 6.16 Simulation

**Definition:** Directly implementing the process described in the problem, step by step, without any algorithmic cleverness — when the problem *is* the algorithm.

**Why it matters:** Some problems (especially easy/medium ones) are pure "implementation stamina" tests — the skill is in careful, bug-free translation of the spec into code, not in finding a clever trick.

**Contest tip:** For simulation-heavy problems, write small helper functions for each described "rule," dry-run each helper individually on the sample before wiring them together — bugs compound quickly in simulation code.

**Common mistakes:** Off-by-one in the "number of steps" or grid boundaries; misreading a subtle rule (e.g., "moves happen simultaneously" vs "one at a time"); assuming an efficient formula exists when the constraints (small N) indicate simulation is intended and safe.

---

### 6.17 Constructive Algorithms

**Definition:** Problems that ask you to *build* any valid object satisfying given constraints, rather than compute a numeric answer — success is judged by a checker that verifies your construction, not by matching an exact expected output.

**Why it matters:** These problems reward creative, systematic construction strategies over classic algorithms; they're extremely common on Codeforces (especially Div 2 C-E).

**General strategies:**
1. **Work backward from a simple/symmetric construction** (e.g., alternate two values, use a known extremal pattern) and check it satisfies constraints.
2. **Reduce to a smaller/known sub-case**, then extend by induction ("if I can build it for N, can I extend to N+1 or N+2?").
3. **Use parity/binary representation** as a building block (many constructive problems boil down to binary encoding).
4. **Try extremal/boundary constructions first** (all same value, strictly increasing, alternating) — these often turn out to be the answer or a close starting point.

**Contest tip:** For constructive problems, don't look for "the one clean idea" too early — sketch 2–3 small examples by hand (N=3,4,5) and look for a repeating pattern before generalizing.

**Common mistakes:** Constructing something that satisfies most, but not all, constraints (double-check every stated condition against your construction); off-by-one when translating a hand-drawn pattern into code indices.

---
## 7. Contest Strategies

### 7.1 Contest Timeline

```
┌──────────────────────────────────────────────────────────────────┐
│                     TYPICAL CONTEST TIMELINE                       │
├──────────────────────────────────────────────────────────────────┤
│  T-30min   Warm up: solve 1 easy problem from another judge         │
│            Check environment (editor, templates, internet)          │
│                                                                     │
│  T+0       Contest starts. Read ALL problems' titles/constraints     │
│            first (2-3 min) to build a mental difficulty map          │
│                                                                     │
│  T+5min    Start with the problem you're most confident about        │
│            (often, but not always, problem A/1)                      │
│                                                                     │
│  T+mid     If stuck >15-20 min on current problem, SWITCH to          │
│            another unsolved problem — don't tunnel-vision             │
│                                                                     │
│  T-30min   Stop attempting new hard problems; focus on making sure    │
│            already-written solutions are debugged and submitted       │
│                                                                     │
│  T-5min    Final submission check; make sure nothing is sitting        │
│            uncommitted/unsubmitted                                    │
│                                                                     │
│  T+end     Post-contest: read editorial for problems you couldn't      │
│            solve; UPSOLVE within 24-48 hours while memory is fresh      │
└──────────────────────────────────────────────────────────────────┘
```

### 7.2 Before Contest

- Warm up with 1 quick, easy problem to get into "reading mode."
- Have your template file ready (fast I/O, common imports) — don't write boilerplate from scratch every contest.
- Know your judge's quirks (e.g., Codeforces vs AtCoder input format conventions).

### 7.3 During Contest

- **Read all problems first** (skim titles + constraints) to build a priority queue of what to attempt.
- **Time-box each problem.** If you're stuck past a self-imposed limit (e.g., 20 minutes with zero progress), move on and come back later.
- **Submit early, submit often** (on judges without heavy per-wrong-submission penalty) — but always test against samples locally first.
- Track partial progress mentally: "I have the O(N²) working, now optimizing" — don't lose a working brute force chasing an optimization that might not land in time.

### 7.4 Problem Selection Strategy

```
┌───────────────────────────────────────────────────┐
│         PROBLEM SELECTION DECISION TREE             │
│                                                      │
│   Is this problem's difficulty near your comfort    │
│   zone (based on rating/letter position)?            │
│        │                                            │
│    ┌───┴────┐                                       │
│   YES       NO                                      │
│    │         │                                      │
│  Attempt   Is it MUCH easier (low risk, quick pts)?  │
│  directly       │                                    │
│              ┌──┴───┐                                │
│             YES     NO (much harder)                  │
│              │       │                                │
│           Do it    Skip for now; revisit after         │
│           quickly  clearing easier problems first        │
└───────────────────────────────────────────────────┘
```

### 7.5 Penalty Minimization

- Understand your judge's penalty system (Codeforces: time penalty per wrong submission on solved problems; ICPC: +20 min per wrong submission on eventually-solved problems).
- **Test locally against the sample AND self-made edge cases** before submitting, especially on judges with harsh penalties.
- Don't "spam submit" hoping to get lucky — each wrong submission has a real cost.

### 7.6 When to Skip vs. When to Push Through

- Skip if: you have no observations after ~15-20 minutes AND other unsolved problems remain.
- Push through if: you have a partial idea that's converging, or it's late in the contest and this is your best remaining shot at points.

### 7.7 When to Upsolve

**Always upsolve** problems you didn't finish, ideally within 24-48 hours:
1. Try again without the editorial first (fresh mind sometimes cracks it).
2. If stuck, read just enough of the editorial to get unstuck, then implement the rest yourself.
3. Only fully read the editorial as a last resort — and then re-implement from scratch without copying, to cement the technique.

### 7.8 Stress Management

- A blank mind after 10 minutes of reading is normal — re-read the statement slowly, tracing the sample input by hand.
- Ranking anxiety mid-contest is a distraction — focus only on "can I get the next problem," not the live scoreboard.
- If completely stuck on every problem, switch to writing a **brute force** for the hardest remaining problem — partial credit (IOI-style) or at least practice value.

---
## 8. Debugging Techniques

### 8.1 Debugging Workflow

```
┌────────────────────────────────────────────────────────────────┐
│                     DEBUGGING WORKFLOW                           │
│                                                                    │
│   Wrong Answer / TLE / RE / MLE on submit                          │
│              │                                                    │
│              ▼                                                    │
│   Re-run against the SAMPLE inputs manually — do they pass?        │
│              │                                                    │
│        ┌─────┴─────┐                                              │
│       NO          YES                                             │
│        │            │                                             │
│  Fix logic     Write a BRUTE FORCE checker                          │
│  bug via         │                                                 │
│  manual dry-run  Generate RANDOM small test cases                   │
│                    │                                                │
│                  Compare brute force vs optimized on many randoms     │
│                    │                                                │
│              ┌─────┴─────┐                                          │
│            MATCH        MISMATCH                                     │
│              │              │                                        │
│         Check for      Found a failing case! Shrink it manually        │
│         TLE/MLE        (remove elements until minimal) then debug        │
│         (perf issue)                                                    │
└────────────────────────────────────────────────────────────────┘
```

### 8.2 Manual Dry Run

Always the first line of defense — trace your algorithm's variables step-by-step on the given sample, comparing against expected output at each stage. Catches ~50% of bugs before any code is even run.

### 8.3 Debug Printing (Contest-Safe Pattern)

```python
import sys
DEBUG = True   # flip to False before final submission (or gate behind an env var)

def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr)   # stderr doesn't interfere with judged stdout

debug("state at step", i, "=", dp)
```

**Contest tip:** Printing to `sys.stderr` instead of `sys.stdout` means debug output never corrupts your actual judged output, even if you forget to remove a debug line (most judges don't grade stderr).

### 8.4 Assertions

```python
assert len(arr) == n, f"length mismatch: {len(arr)} vs {n}"
assert all(x >= 0 for x in arr), "unexpected negative value"
```
**Contest tip:** Assertions are excellent for catching "impossible state reached" bugs early, but remember Python's `-O` flag strips them — don't rely on assertions for actual control flow, only for catching bugs during development/testing.

### 8.5 Brute Force Checker + Stress Testing

The single most powerful CP debugging technique: write an obviously-correct-but-slow brute force, then auto-generate small random tests and diff the two solutions' outputs.

```python
import random
import subprocess

def generate_random_test(max_n=8, max_val=10):
    n = random.randint(1, max_n)
    arr = [random.randint(1, max_val) for _ in range(n)]
    return n, arr

def stress_test(brute_force_fn, optimized_fn, trials=1000):
    for trial in range(trials):
        n, arr = generate_random_test()
        expected = brute_force_fn(arr)
        actual = optimized_fn(arr)
        if expected != actual:
            print(f"MISMATCH on trial {trial}")
            print(f"Input: {arr}")
            print(f"Expected (brute): {expected}")
            print(f"Got (optimized): {actual}")
            return False
    print(f"All {trials} trials passed!")
    return True
```

**Contest tip:** Keep max_n and max_val SMALL (≤10) when stress testing — small failing cases are far easier to debug by hand than large ones. Once you find a mismatch, try to shrink it further manually (remove/simplify elements while it still fails).

### 8.6 Boundary / Corner Case Testing

Explicitly test: N=1, N=0 (if allowed), all-equal arrays, strictly sorted/reverse-sorted arrays, minimum and maximum constraint values.

### 8.7 Verdict-Specific Debugging

| Verdict | Likely cause | Debug approach |
|---|---|---|
| **WA** (Wrong Answer) | Logic bug, missed edge case, wrong greedy/formula | Stress test vs brute force |
| **TLE** (Time Limit Exceeded) | Wrong complexity, or right complexity but bad constant factor | Re-derive complexity from constraints; profile with `time.perf_counter()`; check for accidental O(N) operations inside a loop (e.g., `list.pop(0)`, `x in list`) |
| **MLE** (Memory Limit Exceeded) | Storing more than needed (e.g., full O(N²) table when O(N) rolling array suffices) | Check DP dimensionality; use `array` instead of `list`; free unused structures |
| **RE** (Runtime Error) | Index out of range, division by zero, recursion limit, empty-sequence access (`max([])`) | Add print-based tracing right before the crash point; check all array accesses against bounds |

### 8.8 TLE-Specific Debugging in Python

```python
import time
start = time.perf_counter()
# ... code section ...
print(f"Elapsed: {time.perf_counter() - start:.3f}s", file=sys.stderr)
```
Time individual sections to find the actual bottleneck rather than guessing.

**Common Python-specific TLE traps:**
- `x in some_list` inside a loop → O(N) each time; use a `set` instead → O(1).
- `list.pop(0)` or `list.insert(0, x)` → O(N) each time; use `collections.deque` instead.
- String concatenation with `+=` in a loop → O(N²) total; use `"".join(list)`.
- Recomputing something inside a loop that could be hoisted outside.

---
## 9. Optimization Techniques

### 9.1 Precomputation

**Idea:** Compute reusable information once, up front, rather than recomputing it for every query.

```python
# Precompute all divisors up to N using a sieve-like approach — O(N log N) total
def precompute_divisors(n):
    divisors = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for multiple in range(i, n + 1, i):
            divisors[multiple].append(i)
    return divisors
```
**Contest tip:** If a quantity (factorials, divisor counts, smallest prime factor, prefix sums) is queried more than once, precompute it — this is one of the highest-value, lowest-risk optimizations in CP.

### 9.2 Prefix Computation

Already covered in depth (§6.5) — the general principle: **any repeated range aggregate query should trigger "can I prefix-sum this?" as your first thought.**

### 9.3 Caching / Memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(state):
    # expensive recursive computation
    ...
```
**Contest tip:** `lru_cache` is convenient but has overhead (hashing arguments, dict lookups); for maximum performance in tight-TLE problems, convert to an explicit array/dict-based DP with iterative (bottom-up) computation.

### 9.4 Space Optimization (DP Rolling Arrays)

When `dp[i]` only depends on `dp[i-1]` (or `dp[i-1], dp[i-2]`), don't store the full O(N) or O(N²) table — keep only the needed previous row(s).

```python
# 0/1 Knapsack — space-optimized to O(capacity) instead of O(n * capacity)
def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for cap in range(capacity, w - 1, -1):    # iterate BACKWARD to avoid reuse in same item
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return dp[capacity]
```
**Why backward iteration matters:** Iterating forward would let the same item be "reused" within one pass (turning 0/1 knapsack into unbounded knapsack) — backward iteration ensures each `dp[cap]` update only sees pre-item-`w` values for smaller `cap`.

### 9.5 Time Optimization Checklist

- Move loop-invariant computations outside the loop.
- Replace repeated `list` membership checks with `set`.
- Replace repeated string concatenation with list + `join`.
- Replace `.pop(0)`/`.insert(0, x)` with `deque`.
- Use built-in functions (`sum()`, `max()`, `sorted()`) — they're implemented in C and much faster than manual Python loops.
- Avoid unnecessary object creation inside hot loops (e.g., creating new lists/dicts every iteration).

### 9.6 Input/Output Optimization

Already covered in depth (§2.1–2.2): always use `sys.stdin`/buffered read for input, and batch output via `"\n".join(...)` + one `sys.stdout.write` call.

---

## 10. Common Contest Mistakes

| Mistake | Why it happens | Fix |
|---|---|---|
| **Wrong complexity assumption** | Misjudging what N implies (see §3.2/§4.1 tables) | Always re-derive the complexity budget from constraints before coding |
| **Overflow (conceptual)** | Python has arbitrary-precision ints, so true overflow isn't an issue, but *slow big-int arithmetic* can silently cause TLE if numbers grow unexpectedly large (e.g., unbounded Fibonacci without modulo) | Apply modulo where the problem specifies it, even in Python |
| **Infinite loop** | Missing/incorrect loop-exit condition, or a `while` loop whose state doesn't monotonically progress | Add explicit progress invariants; assert loop iteration counts during testing |
| **Recursion limit exceeded** | Default Python recursion limit (~1000) hit on deep trees/graphs | `sys.setrecursionlimit`, or convert to iterative DFS (see §2.3) |
| **Off-by-one errors** | Confusing inclusive/exclusive ranges, 0-indexed vs 1-indexed | Always explicitly decide and comment your indexing convention; dry-run on N=1,2 |
| **Input parsing errors** | Multiple numbers per line, trailing whitespace, multi-test-case format misunderstood | Use `sys.stdin.read().split()` tokenization (§2.1) to sidestep line-based parsing entirely |
| **Floating point errors** | Comparing floats with `==`, accumulating floating-point error over many operations | Use integer arithmetic where possible; use `math.isclose()`; avoid floats in exact-count problems |
| **Modulo errors** | Forgetting to apply modulo at each step (not just the end), or using `/` instead of modular inverse | Apply `% MOD` after every addition/multiplication; use `pow(a, MOD-2, MOD)` for modular division |
| **Wrong data structure choice** | Using `list` where `set`/`dict`/`deque` is needed → hidden O(N) costs | Know the Big-O of each container's operations (see §2.4 and Cheat Sheet §16) |
| **Ignoring constraints** | Not checking "sum of N over test cases," or the true range of values | Re-read constraints section fully before choosing an approach (§3.2) |

---
## 11. Competitive Programming Templates

Reusable, contest-ready Python templates. Keep these in a personal snippets file you can paste from during contests.

### 11.1 Fast I/O + Multiple Test Cases Template

```python
import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    def nxt():
        nonlocal idx
        val = data[idx]; idx += 1
        return val
    def nxt_int():
        return int(nxt())

    t = nxt_int()
    out = []
    for _ in range(t):
        n = nxt_int()
        arr = [nxt_int() for _ in range(n)]
        # ---- solve(arr) here ----
        ans = sum(arr)
        out.append(str(ans))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
```

### 11.2 Debug Utility Template

```python
import sys
DEBUG = True

def dbg(*args, **kwargs):
    if DEBUG:
        print(*args, file=sys.stderr, **kwargs)
```

### 11.3 Timing Utility Template

```python
import time

class Timer:
    def __init__(self, label="block"):
        self.label = label
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, *exc):
        import sys
        print(f"[{self.label}] {time.perf_counter() - self.start:.4f}s", file=sys.stderr)

# usage:
# with Timer("sorting step"):
#     arr.sort()
```

### 11.4 Prefix Sum Template

```python
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i + 1] = prefix[i] + x
    return prefix

def range_sum(prefix, l, r):     # inclusive [l, r], 0-indexed
    return prefix[r + 1] - prefix[l]
```

### 11.5 Difference Array Template

(See §6.4 for full explanation.)
```python
def diff_array_range_add(n, updates):
    diff = [0] * (n + 1)
    for l, r, v in updates:
        diff[l] += v
        diff[r + 1] -= v
    res, running = [0] * n, 0
    for i in range(n):
        running += diff[i]
        res[i] = running
    return res
```

### 11.6 Coordinate Compression Template

(See §6.1.)
```python
def compress(values):
    su = sorted(set(values))
    rank = {v: i for i, v in enumerate(su)}
    return [rank[v] for v in values], su
```

### 11.7 Binary Search Skeleton (Search over Answer)

```python
def binary_search_answer(lo, hi, feasible):
    """
    Finds the smallest value x in [lo, hi] for which feasible(x) is True,
    assuming feasible(x) is monotonic: False,False,...,False,True,True,...,True
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

# Example: smallest x such that x*x >= n
n = 50
ans = binary_search_answer(0, n, lambda x: x * x >= n)
```
**Common mistake:** Using `mid = (lo + hi) // 2` when you need the *largest* feasible x — then you must use `mid = (lo + hi + 1) // 2` and `lo = mid` / `hi = mid - 1` instead, to avoid infinite loops.

### 11.8 DFS / BFS Skeleton

```python
from collections import deque

def bfs(graph, start):
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def dfs_iterative(graph, start):
    visited = {start}
    stack = [start]
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return order
```

### 11.9 Union-Find (Disjoint Set Union) Skeleton

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path compression (halving)
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True
```
**Complexity:** O(α(N)) amortized per operation (effectively constant).

### 11.10 Segment Tree Skeleton (Range Sum, Point Update)

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, l, r):          # sum over [l, r), 0-indexed, half-open
        l += self.n; r += self.n
        res = 0
        while l < r:
            if l & 1:
                res += self.tree[l]; l += 1
            if r & 1:
                r -= 1; res += self.tree[r]
            l //= 2; r //= 2
        return res
```
**Complexity:** O(N) build, O(log N) update/query. Note the half-open `[l, r)` convention — a very common source of off-by-one bugs; be consistent.

### 11.11 Fenwick Tree (Binary Indexed Tree) Skeleton

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):      # 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):               # prefix sum [1..i]
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def range_query(self, l, r):      # sum [l..r], 1-indexed inclusive
        return self.query(r) - self.query(l - 1)
```
**Complexity:** O(log N) update/query, O(N) space — simpler and faster in practice than a segment tree for pure prefix-sum use cases.

### 11.12 Dijkstra's Algorithm Skeleton

```python
import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue          # stale entry, skip (lazy deletion)
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```
**Complexity:** O((V + E) log V) with a binary heap. **Common mistake:** forgetting the `if d > dist[u]: continue` stale-entry check, which is necessary because Python's `heapq` has no `decrease-key` — we push duplicates instead and skip outdated ones.

### 11.13 Topological Sort Skeleton (Kahn's Algorithm)

```python
from collections import deque

def topo_sort(graph, n):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    q = deque([i for i in range(n) if indegree[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return order if len(order) == n else None   # None => cycle detected
```
**Complexity:** O(V + E). Returning `None` when a cycle exists is a common and important edge-case check.

### 11.14 Modular Arithmetic Template

```python
MOD = 10**9 + 7

def mod_add(a, b): return (a + b) % MOD
def mod_sub(a, b): return (a - b) % MOD
def mod_mul(a, b): return (a * b) % MOD
def mod_inv(a):    return pow(a, MOD - 2, MOD)     # requires MOD to be prime (Fermat's little theorem)
def mod_div(a, b): return mod_mul(a, mod_inv(b))
```

### 11.15 Binary Exponentiation Template

```python
def power(base, exp, mod=None):
    result = 1
    base = base % mod if mod else base
    while exp > 0:
        if exp & 1:
            result = result * base % mod if mod else result * base
        base = base * base % mod if mod else base * base
        exp >>= 1
    return result

# Python's built-in pow(base, exp, mod) already does this in optimized C —
# prefer pow(base, exp, mod) directly in contests unless you need a custom
# monoid (e.g., matrix exponentiation).
```

**Matrix exponentiation (for linear recurrences like Fibonacci in O(log N)):**
```python
def mat_mult(A, B, mod):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if A[i][k]:
                for j in range(p):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def mat_power(M, power_exp, mod):
    n = len(M)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # identity
    while power_exp > 0:
        if power_exp & 1:
            result = mat_mult(result, M, mod)
        M = mat_mult(M, M, mod)
        power_exp >>= 1
    return result
```

---
## 12. Contest Platforms

| Platform | Style | Best for | Notes |
|---|---|---|---|
| **Codeforces** | Div 1/2/3/4 rated rounds, ~2 hours, ICPC-style penalty | Most frequent rated practice, huge problem archive | Editorials are excellent; Div 3/4 are beginner-friendly |
| **AtCoder** | Beginner/Regular/Grand contests | Very clean problem statements, strong math/DP focus | Great for building rigor; ABC is beginner-friendly |
| **CodeChef** | Short + Long Challenge + Starters | Long-format practice (days to think), Indian CP community hub | Long Challenge rewards optimization over speed |
| **LeetCode** | Weekly/Biweekly contests + huge practice bank | FAANG interview prep specifically | Problem style closely mirrors real interview questions |
| **CSES Problem Set** | Not a contest — a curated practice set | Learning one technique at a time, systematically | The best "textbook" of problems for building fundamentals |
| **SPOJ** | Old-school archive | Classical problems, some very hard/classic DS problems | Dated UI, but problems are timeless classics |
| **HackerRank** | Practice tracks + some contests | Interview prep, structured skill tracks | Popular for company-specific interview prep tracks |
| **HackerEarth** | Practice + hiring contests | Company hiring challenges | Similar niche to HackerRank |
| **ICPC** | Team contest, in-person regionals/finals | The pinnacle of team-based collegiate CP | Requires strong collaboration/communication skills |
| **IOI** | Individual, pre-college, partial scoring | High-school-level olympiad training | Subtask-based partial credit rewards partial solutions |
| **Meta Hacker Cup** | Individual, industry-run, online | Large-scale industry contest, good problems, prizes | Runs annually; multiple rounds |
| **Google Code Jam** *(historical, retired 2023)* | Individual, industry-run | Was a major industry contest; now archived | Still an excellent problem archive for practice |

### Platform Selection Flowchart

```
┌─────────────────────────────────────────────────────┐
│  New to CP?           → Start with CSES + AtCoder ABC │
│  Want frequent rated   → Codeforces (Div 3/4 first)    │
│  practice?                                             │
│  Prepping for FAANG    → LeetCode (+ occasional CF)     │
│  interviews?                                            │
│  On an ICPC team?      → Codeforces Gyms + ICPC archives │
│  Want long-form,        → CodeChef Long Challenge          │
│  less time pressure?                                       │
└─────────────────────────────────────────────────────┘
```

---

## 13. Interview vs. CP

| Dimension | Competitive Programming | FAANG Interview |
|---|---|---|
| **Time pressure** | 1–5 hours for 5–8 problems | 30–45 minutes for 1 problem |
| **Communication** | Not required (solo, or silent team collaboration) | Critical — you must narrate your thought process out loud |
| **Correctness bar** | Must pass ALL hidden tests exactly | Must handle the interviewer's follow-up edge cases; some flexibility if you catch bugs yourself |
| **Optimization expectation** | Must hit the exact intended complexity | Often acceptable to start with brute force, then optimize when asked |
| **Problem difficulty** | Wide range, including research-level | Consistently "medium" difficulty, rarely extremely hard |
| **Coding style** | Terse, minimal abstraction, fast to write | Clean, readable, well-named variables — style is graded |
| **Tools allowed** | Full IDE, sometimes internet (varies by contest) | Usually a shared doc/whiteboard, limited or no autocomplete |
| **Mindset needed** | Pattern-match fast, sacrifice readability for speed | Explain trade-offs, ask clarifying questions, prioritize clarity |

### 13.1 Mindset Shift for Interviews

- **Ask clarifying questions first** — CP problems are unambiguous by design; interview problems often deliberately are not.
- **Talk while you think** — silence in an interview reads as "stuck," even if you're actually reasoning productively.
- **State the brute force explicitly**, then narrate your optimization path ("this is O(N²); I think we can get to O(N log N) by sorting first...") — this mirrors §3.5's optimization process, but said out loud.
- **Write production-quality code**: meaningful variable names, maybe a helper function or two, rather than single-letter variables and one giant function (which is fine in CP).
- **Test your code out loud** at the end by tracing through an example, exactly like a dry run (§3.8) — interviewers explicitly look for this habit.

### 13.2 Skills That Transfer Directly

- Pattern recognition (§5) — recognizing "this is a sliding window problem" is equally valuable in both settings.
- Complexity analysis (§4) — interviewers always ask "what's the time/space complexity?"
- Edge case checklists (§3.7) — interviewers explicitly probe these.
- Dry-running code (§3.8) — expected behavior in both settings.

### 13.3 Skills That Need Adjusting

- Terse one-letter variable names (fine in CP) → should become descriptive names in interviews.
- Skipping input validation (fine in CP, since input format is guaranteed) → interviewers may want you to at least mention validation.
- Silent, heads-down coding (normal in CP) → must be replaced with narrated, collaborative problem-solving in interviews.

---

## 14. Problem Recognition Decision Trees

### 14.1 Master Technique-Selection Decision Tree

```
START: Read constraints first.
│
├─ N ≤ 20?  ──────────────────────────▶ Consider Bitmask DP / Brute Force / Meet-in-Middle
│
├─ N ≤ 500-5000? ─────────────────────▶ O(N^2) / O(N^3) DP or nested loops likely fine
│
├─ N ≤ 10^5-10^6?
│     │
│     ├─ Involves subarray/substring + condition? ──▶ Sliding Window / Two Pointers
│     ├─ Involves range sum/count queries? ─────────▶ Prefix Sum / BIT / Segment Tree
│     ├─ Involves "next greater/smaller"? ──────────▶ Monotonic Stack
│     ├─ Involves connectivity/shortest path? ──────▶ Graph traversal / Dijkstra / DSU
│     ├─ Involves sorting + greedy choice? ──────────▶ Greedy (verify via exchange argument)
│     ├─ Involves optimal substructure? ─────────────▶ DP
│     ├─ Involves searching for a threshold value? ──▶ Binary Search on Answer
│     └─ Involves many range queries offline? ───────▶ Mo's Algorithm / Sweep Line + BIT
│
├─ N very large (≥10^9) but as a VALUE not a count? ▶ Math / Number Theory / O(log N) or O(√N)
│
└─ Statement says "construct any valid..."? ────────▶ Constructive Algorithms (§6.17)
```

### 14.2 Observation Checklist (Use When Stuck)

1. Have I re-read the constraints and matched them to a complexity budget (§3.2)?
2. Have I tried N=1, 2, 3 by hand?
3. Is there a monotonic property I can exploit (two pointers / binary search)?
4. Is there an invariant that never changes (parity, sum, XOR)?
5. Can I sort by some key to enable a greedy pass?
6. Does the state space collapse (bitmask, small N) enough for DP?
7. Am I missing an edge case that changes the whole approach?

---
## 15. Python Tips & Tricks

### 15.1 Built-in Functions Worth Knowing

```python
sum(iterable, start=0)
max(iterable, key=..., default=...)
min(iterable, key=..., default=...)
sorted(iterable, key=..., reverse=True)
all(iterable)          # True if every element is truthy
any(iterable)           # True if at least one element is truthy
zip(a, b)                # pairwise iteration
enumerate(a, start=0)     # index + value
reversed(a)                # reverse iterator
divmod(a, b)                 # (a // b, a % b) in one call
```

### 15.2 itertools Deep Cuts

```python
from itertools import (permutations, combinations, combinations_with_replacement,
                        product, accumulate, groupby, pairwise, chain, islice)

list(permutations([1,2,3]))               # all orderings
list(combinations([1,2,3], 2))             # all size-2 subsets
list(product([0,1], repeat=3))              # all binary strings of length 3
list(accumulate([1,2,3,4]))                   # [1,3,6,10]
[(k, list(g)) for k, g in groupby("aaabbc")]   # group consecutive equal elements
```
**Contest tip:** `groupby` only groups *consecutive* equal elements — sort first if you need global grouping.

### 15.3 functools Deep Cuts

```python
from functools import reduce, cmp_to_key

reduce(lambda a, b: a * b, [1,2,3,4])       # 24 (product)

def compare(a, b):
    if a + b < b + a: return -1
    elif a + b > b + a: return 1
    return 0
sorted(["9","5","34"], key=cmp_to_key(compare))   # custom comparator sort (e.g., "largest number" problem)
```

### 15.4 collections Deep Cuts

```python
from collections import Counter, defaultdict, deque, OrderedDict, namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)      # p.x, p.y — readable tuple access

od = OrderedDict()    # rarely needed since Python 3.7+ dicts preserve insertion order,
                       # but explicit when you need move_to_end() for LRU-cache-like behavior
```

### 15.5 heapq Deep Cuts

```python
import heapq
heapq.heapify(arr)                    # O(N) in-place heapify (faster than N pushes)
heapq.nlargest(3, arr)                  # top 3 without full sort
heapq.nsmallest(3, arr, key=lambda x: x[1])   # with a custom key

# Custom objects: use tuples (priority, item) so heapq compares priority first
heapq.heappush(h, (priority, item))
```

### 15.6 bisect Deep Cuts

```python
import bisect
# bisect_left vs bisect_right on duplicates:
arr = [1, 3, 3, 3, 5]
bisect.bisect_left(arr, 3)     # 1 (before the first 3)
bisect.bisect_right(arr, 3)    # 4 (after the last 3)
# Use bisect_right - bisect_left to count occurrences of a value in O(log N)
```

### 15.7 decimal & fractions (Rare but Occasionally Essential)

```python
from decimal import Decimal, getcontext
getcontext().prec = 50
Decimal("0.1") + Decimal("0.2")     # exact decimal arithmetic, avoids float error

from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)     # exact rational arithmetic: Fraction(1, 2)
```
**Contest tip:** Use `Fraction` when a problem requires *exact* rational comparisons (common in geometry/probability problems) rather than risking floating-point precision errors.

### 15.8 Common Python Pitfalls

| Pitfall | Explanation |
|---|---|
| Mutable default arguments | `def f(x, arr=[]):` — the same list is reused across calls! Use `arr=None` and set inside. |
| Shallow copy of nested lists | `b = a[:]` only copies the outer list; use `copy.deepcopy(a)` for nested structures, or rebuild explicitly |
| Integer division | `//` floors toward negative infinity in Python (not toward zero like C++) — matters for negative numbers |
| `is` vs `==` | `is` checks identity, not value equality — never use `is` to compare numbers/strings for equality |
| Global recursion limit shared across test cases | If you raise it once, it stays raised — fine, but don't assume it resets |
| Late binding in closures/lambdas in loops | `[lambda: i for i in range(3)]` — all three lambdas see the FINAL value of `i` unless you capture it via default arg `lambda i=i: i` |

---

## 16. Cheat Sheets

### 16.1 Complexity Cheat Sheet

| Notation | Name | Rough N limit (1-2s TL) |
|---|---|---|
| O(1) | Constant | Any N |
| O(log N) | Logarithmic | Any N |
| O(√N) | Square root | Any N |
| O(N) | Linear | ~10^7-10^8 |
| O(N log N) | Linearithmic | ~10^5-10^6 |
| O(N√N) | | ~10^5 |
| O(N^2) | Quadratic | ~5,000-10,000 |
| O(N^3) | Cubic | ~300-500 |
| O(2^N) | Exponential | ~20-24 |
| O(2^(N/2)) | Meet in middle | ~40 |
| O(N!) | Factorial | ~10-11 |

### 16.2 Data Structure Operation Cheat Sheet

| Structure | Access | Search | Insert | Delete | Notes |
|---|---|---|---|---|---|
| `list` | O(1) | O(N) | O(1) amortized (end) / O(N) (front/middle) | O(N) | Use `deque` for front ops |
| `deque` | O(1) ends | O(N) | O(1) both ends | O(1) both ends | Best for queue/stack-like use |
| `dict` / `set` | O(1) avg | O(1) avg | O(1) avg | O(1) avg | Worst-case O(N) with hash collisions (anti-hash tests!) |
| `heapq` (list-backed) | O(1) min | O(N) | O(log N) | O(log N) | Only min-accessible directly |
| `sorted list` (via `bisect`) | O(1) | O(log N) | O(N) | O(N) | Insertion/deletion is O(N) due to shifting |
| Segment Tree | — | O(log N) | O(log N) update | — | Range query + point/range update |
| Fenwick Tree (BIT) | — | O(log N) | O(log N) | — | Simpler, faster constant than segment tree, prefix-sum-shaped |
| Union-Find (DSU) | — | O(α(N)) find | O(α(N)) union | — | Effectively O(1) amortized |

### 16.3 Pattern Recognition Quick-Reference

(See full map in §5.1 — condensed here for revision.)

| Keyword | Technique |
|---|---|
| "subarray", "at most/exactly K distinct" | Sliding Window |
| "sorted array", "pair/triplet sum" | Two Pointers |
| "range sum query" | Prefix Sum / BIT / Segment Tree |
| "next greater/smaller" | Monotonic Stack |
| "sliding window min/max" | Monotonic Deque |
| "smallest X such that condition" | Binary Search on Answer |
| "N ≤ 20, subsets" | Bitmask DP |
| "many offline range queries" | Mo's Algorithm / Sweep + BIT |
| "path between two tree nodes" | HLD / Binary Lifting (LCA) |
| "subtree aggregate" | Euler Tour + BIT |
| "construct any valid X" | Constructive |
| "two players play optimally" | Game Theory |

### 16.4 Contest Checklist (Pin This)

- [ ] Read full statement + constraints before coding
- [ ] Derive complexity budget from N (§3.2/§4.1)
- [ ] Write brute force first if unsure
- [ ] Dry run on the sample by hand
- [ ] Check edge cases (N=0,1, duplicates, negatives)
- [ ] Use fast I/O for large inputs
- [ ] Apply modulo consistently if required
- [ ] Test locally before submitting
- [ ] If WA: stress test vs. brute force
- [ ] If TLE: re-derive complexity, check for hidden O(N) ops
- [ ] Upsolve unsolved problems within 48 hours

### 16.5 Debugging Checklist

- [ ] Does it pass the given samples exactly?
- [ ] Have I stress-tested against a brute force on random small inputs?
- [ ] Have I checked N=0/1 and all-equal-elements cases?
- [ ] Have I checked for off-by-one in ranges (inclusive vs exclusive)?
- [ ] Have I checked recursion depth for large N?
- [ ] Have I applied modulo after every multiplication/addition where required?

### 16.6 Optimization Guide (One-Glance)

```
Slow due to...           →  Fix
─────────────────────────────────────────────
Repeated recomputation   →  Precompute / prefix sums / memoize
Nested O(N) search        →  Hashmap / set / sorted + binary search
Repeated range updates     →  Difference array / segment tree / BIT
Front-of-list operations    →  collections.deque
String concatenation in loop→ list + "".join()
Deep recursion               →  Increase recursion limit / iterative + explicit stack
Large DP table                →  Rolling array (space optimization)
```

### 16.7 Python Syntax Cheat Sheet (CP-Relevant)

```python
# Multi-assignment / swap
a, b = b, a

# List comprehension with condition
evens = [x for x in arr if x % 2 == 0]

# Nested comprehension (2D grid)
grid = [[0] * cols for _ in range(rows)]     # NEVER [[0]*cols]*rows — that aliases rows!

# f-strings for debug output
print(f"{x=}, {y=}")     # Python 3.8+: prints "x=5, y=10"

# Ternary
result = "even" if x % 2 == 0 else "odd"

# Unpacking with *
first, *rest = [1, 2, 3, 4]

# Chained comparison
if 0 <= i < n:
    ...
```
**Critical warning:** `[[0] * cols] * rows` creates `rows` references to the *same* inner list — mutating one row mutates all rows. Always use a list comprehension `[[0]*cols for _ in range(rows)]` for 2D grids.

### 16.8 Interview Cheat Sheet

- State the brute force out loud first.
- Narrate your complexity reasoning (§3.2/§4.1) at each step.
- Ask about constraints if not given (they're often not stated explicitly in interviews, unlike CP).
- Write clean, named variables — not CP-style single letters.
- Test with a walk-through example at the end, out loud.

---
## 17. Practice Problems by Pattern

> Note: ratings/difficulty are approximate and may shift over time as platforms re-calibrate. Search the problem name on the given platform to find it — direct links are omitted here since they can change/break, but names below are real, well-known problems.

### 17.1 Observation / Ad-hoc

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Watermelon | Codeforces | 800 | Parity observation |
| Theatre Square | Codeforces | 1000 | Math + ceiling division observation |
| Chef and Reversing | CodeChef | Easy | Case analysis |
| Two Sum | LeetCode | Easy | Hashing observation |

### 17.2 Greedy

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Applepie vs. cows-style scheduling (Room Allocation) | CSES | Medium | Interval greedy + heap |
| Tolik and His Uncle | Codeforces | 1100 | Greedy construction |
| Jump Game | LeetCode | Medium | Greedy reachability |
| Gas Station | LeetCode | Medium | Greedy + prefix reasoning |

### 17.3 Math

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Exponentiation | CSES | Easy | Binary exponentiation + modulo |
| Common Divisors | CSES | Easy | GCD/number theory |
| Counting Divisors | CSES | Medium | Sieve-based divisor counting |
| GCD Array-style problems | Codeforces | 1200-1500 | Number theory + sieve |

### 17.4 Simulation

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Robot Return | Codeforces | 800 | Direct simulation |
| Simulate the Robot | LeetCode | Medium | Grid simulation |
| Chess Tournament-style problems | Codeforces | 1200-1400 | Rule-following simulation |

### 17.5 Constructive

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Construct the String | Codeforces | 1200-1500 | Constructive + parity |
| Building Teams | CSES | Medium | Bipartite construction (BFS coloring) |
| Beautiful Matrix-style construction | Codeforces | 1300-1600 | Pattern-based construction |

### 17.6 Binary Search on Answer

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Factory Machines | CSES | Medium | Binary search on answer |
| Array Division | CSES | Medium | Binary search + greedy feasibility check |
| Koko Eating Bananas | LeetCode | Medium | Binary search on answer |
| Capacity To Ship Packages Within D Days | LeetCode | Medium | Binary search + greedy feasibility |

### 17.7 Prefix Sum / Sliding Window / Two Pointers

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Subarray Sums I & II | CSES | Easy-Medium | Prefix sum + hashmap |
| Maximum Subarray Sum | CSES | Easy | Kadane's / prefix reasoning |
| Longest Substring Without Repeating Characters | LeetCode | Medium | Sliding window |
| Playing With Numbers-style range problems | Codeforces | 1100-1400 | Two pointers |

### 17.8 Offline Queries / Sweep Line / Mo's Algorithm

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Distinct Values Queries | CSES | Hard | Mo's Algorithm or offline BIT |
| Range Update Queries | CSES | Medium | Difference array / BIT |
| Meeting rooms-style interval overlap counting | LeetCode | Medium | Sweep line |
| Salary Queries | CSES | Hard | Offline coordinate compression + BIT |

### 17.9 Coordinate Compression

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Coordinate Compression-flavored inversion counting | Codeforces | 1300-1600 | Compression + BIT |
| Nested Segments-style problems | Codeforces | 1400-1700 | Compression + sweep |

### 17.10 Meet in the Middle

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Meet in the middle subset-sum-flavored problems | Codeforces | 1700-2000 | Meet in the middle |
| Partition into two subsets close to equal sum | Various | Medium-Hard | Meet in the middle / bitmask hybrid |

### 17.11 Mixed / Advanced Techniques

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Company Queries I & II | CSES | Medium-Hard | Binary lifting (LCA / k-th ancestor) |
| Subtree Queries | CSES | Hard | Euler tour + BIT |
| Path Queries | CSES | Hard | Euler tour + BIT (subtree-path hybrid) |
| Distinct Colors | CSES | Hard | Small-to-large merging (DSU on tree) |

### 17.12 Building a Practice Plan

```
┌────────────────────────────────────────────────────────────┐
│                 12-WEEK PRACTICE ROADMAP                     │
├────────────────────────────────────────────────────────────┤
│ Weeks 1-2:   Implementation, Math, Ad-hoc (CSES Intro set)    │
│ Weeks 3-4:   Sorting, Greedy, Binary Search                    │
│ Weeks 5-6:   Prefix Sums, Two Pointers, Sliding Window          │
│ Weeks 7-8:   Graphs (BFS/DFS/DSU), basic DP                     │
│ Weeks 9-10:  Advanced DP, Bitmask DP, Trees                       │
│ Weeks 11-12: Segment Trees/BIT, Offline techniques, Mixed sets     │
│                                                                   │
│ Throughout:  1-2 rated contests/week (Codeforces Div 2/3/4),        │
│              ALWAYS upsolve within 48 hours                          │
└────────────────────────────────────────────────────────────┘
```

---

## 18. Final Revision

### 18.1 One-Page Revision

```
┌──────────────────────────────────────────────────────────────┐
│                  CP TECHNIQUES — ONE PAGER                     │
├──────────────────────────────────────────────────────────────┤
│ 1. Read constraints → derive complexity budget (§3.2, §4.1)     │
│ 2. Brute force first, always (§3.4)                              │
│ 3. Pattern-match via keywords (§5, §16.3)                          │
│ 4. Common toolbox: prefix sum, two pointers, binary search,          │
│    monotonic stack, difference array, coordinate compression,         │
│    bitmask DP, sweep line, Mo's algorithm, meet in the middle           │
│ 5. Prove greedy via exchange argument, or stress test it (§6.13)        │
│ 6. Dry run before coding (§3.8)                                            │
│ 7. Fast I/O always: sys.stdin.buffer.read().split() (§2.1)                  │
│ 8. WA → stress test vs brute force (§8.5)                                     │
│ 9. TLE → re-derive complexity, check hidden O(N) ops (§8.8)                     │
│ 10. Upsolve everything within 48 hours (§7.7)                                     │
└──────────────────────────────────────────────────────────────┘
```

### 18.2 Mind Map — Techniques by Trigger

```
                        ┌─────────────────┐
                        │  READ PROBLEM     │
                        └────────┬─────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                   ▼
      "range query?"      "subset/subarray?"    "construct something?"
              │                  │                   │
   ┌──────────┼─────────┐   ┌────┼─────┐      ┌──────┴───────┐
   ▼          ▼          ▼  ▼         ▼        ▼              ▼
Prefix Sum  Segment   BIT  Sliding  Two      Try small     Look for
            Tree           Window  Pointers  cases, find    parity/
                                              pattern        pattern
```

### 18.3 Contest Strategy Guide (Recap)

Read all → time-box each problem → switch if stuck → test before submit → upsolve after. (Full detail: §7.)

### 18.4 Optimization Flowchart (Recap)

Precompute → prefix/diff arrays → right data structure → memoize → space-optimize (rolling array) → tighten I/O. (Full detail: §9, §16.6.)

### 18.5 Debugging Checklist (Recap)

Samples pass → stress test vs brute force → check edge cases → check off-by-ones → check recursion depth → check modulo application. (Full detail: §8, §16.5.)

### 18.6 Complexity Sheet (Recap)

See §16.1 for the full N-to-complexity mapping table.

### 18.7 Standard Templates (Recap)

Fast I/O, DSU, Segment Tree, Fenwick Tree, Dijkstra, Topo Sort, Modular Arithmetic, Binary Exponentiation — all in §11.

### 18.8 Interview Notes (Recap)

Narrate thinking, ask clarifying questions, brute force → optimize out loud, clean naming, verbal dry run at the end. (Full detail: §13.)

### 18.9 15-Minute Revision

1. Skim §16.1 (complexity table) and §16.3 (pattern keywords) — 3 min
2. Skim §16.4 (contest checklist) — 2 min
3. Re-read your personal "common mistakes I make" log (keep one!) — 5 min
4. Re-skim your template file (§11) to make sure it's all still correct/pasteable — 5 min

### 18.10 1-Hour Revision

1. Re-read §3 (Problem-Solving Framework) in full — 10 min
2. Re-read §6 (CP Techniques) skimming templates and dry runs — 20 min
3. Solve 1 easy problem from each of 3 different pattern categories (§17) as a warm-up — 25 min
4. Review §8 (Debugging) and §10 (Common Mistakes) — 5 min

### 18.11 FAQ

**Q: Is Python too slow for competitive programming?**
A: For the vast majority of Div 2/3/4 Codeforces, AtCoder ABC/ARC, and CSES problems, Python (with fast I/O and the idioms in §2 and §9) is fast enough, especially since most judges give Python 2-3x the C++ time limit. For the top ~5% hardest, tightest-constant problems, a compiled language has an edge — but that's a small fraction of practice value for most competitors.

**Q: Should I memorize all these templates?**
A: No — keep a personal template file (many editors/judges allow file upload or a "custom test" pre-fill) and understand *when* to reach for each one (that's what §5, §14, and §16.3 are for). Recognition matters far more than memorization.

**Q: How do I know if my greedy solution is correct?**
A: Prefer an exchange-argument proof (§6.13) when time allows; when it doesn't, stress test against a brute force on small random inputs (§8.5) — this catches the vast majority of incorrect greedy ideas.

**Q: I understand the theory but still can't solve problems — what's wrong?**
A: This is normal and universal. The gap is closed only by volume of practice + upsolving with editorials (§7.7) — theory gives you the vocabulary, but pattern recognition (§5) is built through repetition.

**Q: What's the single highest-leverage habit in this whole handbook?**
A: Constraint analysis (§3.2, §4.1) — correctly reading N and deriving the target complexity before writing any code prevents the majority of wasted contest time.

---
