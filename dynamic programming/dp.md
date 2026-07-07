# The Complete Dynamic Programming Handbook (Python Edition)


## Table of Contents

1. [Introduction to Dynamic Programming](#1-introduction-to-dynamic-programming)
2. [Python DP Templates](#2-python-dp-templates)
3. [DP Fundamentals](#3-dp-fundamentals)
4. [Core DP Patterns Overview](#4-core-dp-patterns-overview)
5. [Classic DP Problems](#5-classic-dp-problems)
   - [5.1 Basics](#51-basics)
   - [5.2 Knapsack Pattern](#52-knapsack-pattern)
   - [5.3 Sequence DP](#53-sequence-dp)
   - [5.4 Grid DP](#54-grid-dp)
   - [5.5 Interval DP](#55-interval-dp)
   - [5.6 Partition DP](#56-partition-dp)
   - [5.7 State Machine DP](#57-state-machine-dp)
   - [5.8 Advanced DP (Bitmask / Digit)](#58-advanced-dp-bitmask--digit)
6. [Advanced DP Concepts & Optimizations](#6-advanced-dp-concepts--optimizations)
7. [Applications of DP](#7-applications-of-dp)
8. [Problem Recognition Guide](#8-problem-recognition-guide)
9. [The Optimization Ladder](#9-the-optimization-ladder)
10. [Interview Preparation](#10-interview-preparation)
11. [Python Tips for DP](#11-python-tips-for-dp)
12. [Common Mistakes](#12-common-mistakes)
13. [Cheat Sheets](#13-cheat-sheets)
14. [Practice Problem Bank](#14-practice-problem-bank)
15. [Final Revision](#15-final-revision)

---

## 1. Introduction to Dynamic Programming

### 1.1 What Is Dynamic Programming?

Dynamic Programming (DP) is a method for solving complex problems by breaking them into simpler **overlapping subproblems**, solving each subproblem **once**, and storing (caching) the result so it never needs to be recomputed. It sits between brute-force recursion (which recomputes everything) and greedy algorithms (which never look back).

> **Definition:** DP is an algorithmic technique for solving an optimization or counting problem by combining the solutions of overlapping subproblems, where each subproblem is solved only once and its result is reused.

### 1.2 History

- Coined by **Richard Bellman** in the 1950s while working at the RAND Corporation.
- Bellman needed a name that sounded impressive to funders — "dynamic" and "programming" (meaning *planning/tabulation*, not coding) were chosen deliberately because they could not be used pejoratively by government officials.
- Formalized in his 1957 book *Dynamic Programming*, which introduced the **Bellman Equation** and the **Principle of Optimality**.

### 1.3 Bellman's Principle of Optimality

> *"An optimal policy has the property that whatever the initial state and initial decision are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision."*

In plain English: **if the overall solution is optimal, then every sub-solution embedded inside it must also be optimal.** This is exactly what allows us to build a global optimum from local optimal answers to subproblems — it is the theoretical justification for DP.

### 1.4 Why DP Exists

Without DP, many problems that look "recursive" explode exponentially because the same subproblem gets solved again and again.

```
Fibonacci(5) naive recursion tree:

                    fib(5)
                 /          \
             fib(4)          fib(3)
            /      \         /      \
        fib(3)    fib(2)  fib(2)   fib(1)
        /    \     /   \   /   \
    fib(2) fib(1) fib(1)fib(0) fib(1)fib(0)
    /   \
 fib(1) fib(0)
```

Notice `fib(3)` is computed twice, `fib(2)` three times, `fib(1)` five times. As `n` grows, this redundancy grows exponentially (`O(2^n)`). DP eliminates this redundancy by remembering answers.

### 1.5 Characteristics of a DP Problem

A problem is solvable with DP if and only if it exhibits **both** of the following properties:

#### 1.5.1 Overlapping Subproblems

The same subproblem is encountered multiple times during a naive recursive solution.

```
ASCII: Overlapping Subproblems Detection
----------------------------------------
fib(5)
 ├── fib(4)
 │    ├── fib(3)   <-- also needed below
 │    └── fib(2)
 └── fib(3)        <-- SAME as above (overlap!)
      ├── fib(2)
      └── fib(1)
```

If subproblems are all *distinct* (no overlap), you likely need **Divide & Conquer**, not DP (e.g., Merge Sort).

#### 1.5.2 Optimal Substructure

An optimal solution to the problem can be constructed from optimal solutions of its subproblems.

```
Shortest Path Example (Optimal Substructure):

  A --2--> B --3--> D
   \              /
    5---> C --1--/

ShortestPath(A, D) = min(
    ShortestPath(A, B) + cost(B, D),
    ShortestPath(A, C) + cost(C, D)
)
```

| Property | Question to Ask | If YES |
|---|---|---|
| Overlapping Subproblems | "Do I solve the same smaller problem more than once?" | Cache it (memoize) |
| Optimal Substructure | "Can I build the best answer from the best answers of smaller pieces?" | DP applies |

### 1.6 State Representation & State Transition (Preview)

- **State**: the minimal set of parameters that uniquely describes a subproblem (e.g., `dp[i]`, `dp[i][j]`, `dp[i][j][k]`).
- **Transition**: the recurrence relation connecting a state to smaller states (e.g., `dp[i] = dp[i-1] + dp[i-2]`).

These are covered in full depth in [Section 3](#3-dp-fundamentals).

### 1.7 Advantages of DP

- Converts exponential-time brute force into polynomial time.
- Systematic — once state & transition are found, implementation is mechanical.
- Works for both **optimization** (min/max) and **counting** (number of ways) problems.
- Generalizes to multi-dimensional state spaces (grids, strings, bitmasks).

### 1.8 Disadvantages of DP

- Requires extra memory for the cache/table (can be O(n), O(n²), or worse).
- Correct **state definition** can be non-obvious and is the single hardest skill to learn.
- Not applicable if subproblems don't overlap, or if greedy choice property already holds (greedy is simpler and faster when valid).
- Recursion-based memoization can hit Python's recursion limit for large inputs.

### 1.9 Applications & Real-World Examples

| Domain | Example |
|---|---|
| Bioinformatics | DNA sequence alignment (Edit Distance / LCS) |
| NLP | Spell correction, speech recognition (Edit Distance, HMM Viterbi) |
| Finance | Optimal portfolio rebalancing, stock buy/sell timing |
| Route Planning | Shortest path with constraints, Bellman-Ford |
| Compilers | Optimal register allocation, instruction scheduling |
| Game Theory | Minimax with memoization, Nim-like games (Stone Game) |
| Operating Systems | Resource allocation, scheduling (Knapsack-like) |
| Robotics | Path planning under obstacles (Grid DP) |
| Everyday Life | Coin change while making exact change at a cash register |

> **Real-World Analogy:** Think of DP like keeping a diary of answers to questions you've already figured out. Next time someone asks the same question, instead of re-deriving the answer from scratch, you just flip to the page in your diary and read it off. That diary is your memoization cache.

---

## 2. Python DP Templates

Python offers several idiomatic ways to implement DP. Knowing all of them — and when to use each — is a core interview skill.

### 2.1 Top-Down Memoization (Manual Dictionary Cache)

```python
def fib_memo(n, cache=None):
    """Top-down Fibonacci using an explicit dictionary cache."""
    if cache is None:
        cache = {}
    if n in cache:                 # 1. Have we solved this exact state before?
        return cache[n]
    if n <= 1:                     # 2. Base case
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)  # 3. Transition
    return cache[n]
```

**Line-by-line explanation**
1. `cache` defaults to a fresh dict per top-level call (avoids the classic Python mutable-default-argument bug).
2. `if n in cache` — an O(1) lookup avoids recomputation; this is the entire point of memoization.
3. Base case `n <= 1` returns `0` or `1` directly (`fib(0)=0`, `fib(1)=1`).
4. The recursive transition mirrors the mathematical recurrence exactly, and the result is stored before returning.

### 2.2 `functools.lru_cache` (Idiomatic Python Memoization)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_lru(n):
    if n <= 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)
```

**Notes**
- `maxsize=None` means unbounded cache (never evicts) — use this for DP unless memory is a genuine constraint.
- Since Python 3.9, `@cache` (from `functools`) is a shorthand for `@lru_cache(maxsize=None)`.
- `lru_cache` requires all arguments to be **hashable** (ints, strings, tuples — not lists or dicts).

```python
from functools import cache

@cache
def fib_cache(n):
    if n <= 1:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)
```

> **Tip:** In interviews, `@lru_cache(maxsize=None)` is the fastest way to convert brute-force recursion into a memoized solution — always mention it as your "Option 1" before writing bottom-up code.

> **Warning:** `lru_cache` persists across function calls at module scope. If you call the same `@cache`-decorated function again with a different meaning of the parameters, clear it explicitly with `fib_cache.cache_clear()`.

### 2.3 Bottom-Up Tabulation

```python
def fib_tab(n):
    """Bottom-up Fibonacci — builds the table from the base case upward."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)     # 1. Allocate table for every state 0..n
    dp[0], dp[1] = 0, 1    # 2. Base cases
    for i in range(2, n + 1):      # 3. Fill table in dependency order
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]            # 4. Answer state
```

**Line-by-line explanation**
1. Table sized `n+1` so index `n` is directly accessible (no off-by-one).
2. Seed the smallest states first.
3. Iterate strictly left-to-right since `dp[i]` depends only on smaller indices — this iteration order IS the topological order of the dependency graph.
4. Return the designated "answer state" — not necessarily the last cell in general DP (e.g. counting DP may need `max(dp)`).

### 2.4 Space-Optimized DP (Rolling Variables)

```python
def fib_optimized(n):
    """O(1) space — only the last two states are ever needed."""
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1
```

This works because `dp[i]` only depends on `dp[i-1]` and `dp[i-2]` — we don't need the entire history, just a **rolling window**.

### 2.5 Rolling Array for 2D DP

When `dp[i][j]` depends only on row `i-1` (not further back), you can collapse an `O(n*m)` table into two `O(m)` rows:

```python
def unique_paths_rolling(m, n):
    prev = [1] * n
    for _ in range(1, m):
        curr = [1] * n
        for j in range(1, n):
            curr[j] = curr[j - 1] + prev[j]
        prev = curr
    return prev[-1]
```

### 2.6 Dictionary-Based DP (Sparse States)

Useful when the state space is huge but only a few states are actually visited (e.g., DP over large sums, bitmask combinations that prune heavily):

```python
def coin_change_sparse(coins, amount):
    memo = {0: 0}
    def dp(remaining):
        if remaining < 0:
            return float('inf')
        if remaining in memo:
            return memo[remaining]
        best = min(dp(remaining - c) for c in coins) + 1
        memo[remaining] = best
        return best
    result = dp(amount)
    return result if result != float('inf') else -1
```

### 2.7 Best Practices & Performance Considerations

| Practice | Reason |
|---|---|
| Prefer `@lru_cache` for prototyping | Fast to write, easy to reason about |
| Convert to tabulation for production | Avoids recursion-depth limits, usually faster (no function-call overhead) |
| Use arrays/lists over dicts when state space is dense | O(1) array access beats hashing |
| Space-optimize only after correctness | Premature optimization risks introducing bugs in transitions |
| Increase recursion limit cautiously | `sys.setrecursionlimit(10000)` — only if truly needed, can crash the interpreter (stack overflow) |
| Use `tuple` state keys for multi-dimensional memoization | Tuples are hashable, lists are not |

```python
import sys
sys.setrecursionlimit(10_000)  # use with caution — real stack can still overflow
```

---

## 3. DP Fundamentals

### 3.1 State

The **state** is the smallest set of variables that fully describes a subproblem — enough information to compute an answer, and no more.

```
Good state design asks:
  "If I know these values, can I compute the answer
   WITHOUT knowing how I got here?"
```

**Example — House Robber:** `dp[i]` = max money robbable from houses `0..i`. We do NOT need to know *which* houses were robbed, only the index reached — that's what makes it a valid, minimal state.

### 3.2 Transition (Recurrence Relation)

The transition connects a state to the smaller states it depends on.

```
General template:
   dp[state] = best_of( dp[smaller_state_1] OP contribution_1,
                         dp[smaller_state_2] OP contribution_2,
                         ... )
```

Example (House Robber): `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.

### 3.3 Base Case

The smallest, directly-known state(s) that terminate the recursion / seed the table. Missing or wrong base cases are the #1 cause of DP bugs.

### 3.4 Answer State

The specific `dp[...]` cell (or reduction like `max(dp)`) that represents the final answer. Not always the "last" cell in the table!

### 3.5 Recursion → DP Conversion Pipeline

```
Step 1: Write brute-force recursion.
Step 2: Identify repeated calls (overlapping subproblems) -> add memo dict/array.
Step 3: (Optional) Convert top-down memo into bottom-up table.
Step 4: (Optional) Reduce table dimensions via space optimization.
```

```python
# STEP 1 — Brute force
def solve(i):
    if base_case(i):
        return base_value
    return combine(solve(i - 1), solve(i - 2))

# STEP 2 — Memoized
from functools import lru_cache
@lru_cache(maxsize=None)
def solve_memo(i):
    if base_case(i):
        return base_value
    return combine(solve_memo(i - 1), solve_memo(i - 2))

# STEP 3 — Tabulated
def solve_tab(n):
    dp = [0] * (n + 1)
    dp[0] = base_value
    for i in range(1, n + 1):
        dp[i] = combine(dp[i - 1], dp[i - 2])
    return dp[n]

# STEP 4 — Space optimized
def solve_opt(n):
    a, b = base_value, base_value
    for i in range(1, n + 1):
        a, b = b, combine(b, a)
    return b
```

### 3.6 Top-Down vs Bottom-Up Thinking

| Aspect | Top-Down (Memoization) | Bottom-Up (Tabulation) |
|---|---|---|
| Direction | Starts from the big problem, recurses down | Starts from base cases, builds up |
| Code style | Recursive function + cache | Iterative loop + table |
| Ease of writing | Usually easier — mirrors brute force | Requires figuring out fill order upfront |
| Stack usage | Uses call stack (risk of recursion limit) | No recursion — no stack risk |
| Computes only needed states | Yes — naturally lazy | No — computes all states unless pruned |
| Speed in practice | Slightly slower (function call overhead) | Slightly faster (tight loops) |
| Easier to space-optimize | No | Yes |

```
ASCII: Direction of Computation
--------------------------------
Top-Down:                     Bottom-Up:
   solve(n)                     dp[0] -> dp[1] -> dp[2] -> ... -> dp[n]
   /       \                        (fill table left to right,
solve(n-1) solve(n-2)                 in dependency order)
   ...  (unwinds back up)
```

### 3.7 State Compression

Reducing the *number of dimensions* or *size* of the state, e.g.:
- Replacing `dp[i][j]` with `dp[j]` when row `i` only needs row `i-1` (rolling array).
- Replacing a subset `dp[mask]` with a bitmask integer instead of a set/list.

### 3.8 Space Optimization

Reducing memory once correctness is verified. Common patterns:
- **1D → O(1):** keep only the last `k` values in variables.
- **2D → 1D:** keep only the previous row.
- **Iterate in the correct direction** (forward vs backward) to avoid overwriting values still needed (critical for 0/1 Knapsack — must iterate the capacity dimension **backward**).

### 3.9 Correctness Intuition — Why DP Works

DP's correctness rests entirely on **Bellman's Principle of Optimality** (Section 1.3): if we can prove that an optimal solution to state `i` must be built from optimal solutions to smaller states, then filling states in dependency order (smallest → largest) guarantees the final answer is globally optimal — we never need to "look back and revise" a completed state.

> **Interview Tip:** Whenever you propose a DP solution, briefly state the optimal substructure argument out loud — interviewers reward this because it proves you're not just pattern-matching a memorized template.

---

## 4. Core DP Patterns Overview

This section is a map of every major DP "shape." Each pattern is explored fully with worked problems in Section 5 — here we build **recognition intuition**.

### 4.1 Pattern Summary Table

| Pattern | Typical State | Typical Dimensions | Example Problem |
|---|---|---|---|
| 1D Linear DP | `dp[i]` = best answer using first `i` elements | O(n) | Climbing Stairs |
| Fibonacci-style | `dp[i] = f(dp[i-1], dp[i-2])` | O(n) → O(1) | Fibonacci, Tribonacci |
| 0/1 Knapsack | `dp[i][w]` = best value with first `i` items, capacity `w` | O(n·W) | 0/1 Knapsack, Subset Sum |
| Unbounded Knapsack | `dp[w]` = best value with capacity `w`, unlimited items | O(n·W) | Coin Change, Rod Cutting |
| Subsequence DP | `dp[i][j]` over two sequences | O(n·m) | LCS, Edit Distance |
| Substring / Palindrome DP | `dp[i][j]` = property of substring `s[i..j]` | O(n²) | Longest Palindromic Substring |
| Interval DP | `dp[i][j]` = best answer for merging/splitting range `[i,j]` | O(n³) | Matrix Chain Mult., Burst Balloons |
| Grid DP | `dp[r][c]` = best answer reaching cell `(r,c)` | O(rows·cols) | Unique Paths, Min Path Sum |
| Partition DP | `dp[i][k]` = best answer partitioning first `i` elements into `k` parts | O(n²·k) | Stone Game, Partition Array |
| State Machine DP | `dp[i][state]` = best answer at step `i` while in `state` | O(n·states) | Stock Buy/Sell, Decode Ways |
| Bitmask DP | `dp[mask]` or `dp[i][mask]` | O(2^n · n) | TSP, Assignment Problem |
| Digit DP | `dp[pos][tight][sum]` | O(digits · states) | Count numbers with digit property |
| Tree DP | `dp[node][state]` computed via DFS | O(n) | Max path sum in tree, House Robber III |
| Probability/Expectation DP | `dp[state]` = probability/expected value | Varies | Dice/Markov chain problems |

### 4.2 Visual Pattern Map

```
                         DYNAMIC PROGRAMMING
                                |
        -----------------------------------------------------
        |            |            |            |            |
     1D LINEAR    KNAPSACK    SEQUENCE DP   GRID DP     STATE MACHINE
   (Fibonacci,   (0/1, Un-   (LCS, LIS,   (Unique     (Stock buy/sell,
    Stairs,       bounded,    Edit Dist)   Paths,       Decode Ways)
    House Robber) Subset Sum)              Min Path)
        |
   -------------------------
   |                        |
INTERVAL DP             PARTITION DP           ADVANCED
(MCM, Burst              (Stone Game,        (Bitmask, Digit,
 Balloons)                Partition Array)     Tree DP, SOS DP)
```

### 4.3 How to Choose Dimensions

```
Ask yourself:
1. How many "moving parts" change as the problem shrinks?
   -> that's your number of dimensions.
2. What is the RANGE of each moving part?
   -> that determines array sizes / time complexity.
3. Is there a constraint dimension (capacity, count, budget)?
   -> that's usually the second or third dimension.
```

---

## 5. Classic DP Problems

### 5.1 Basics

#### 5.1.1 Fibonacci Number

**Problem:** Compute the `n`-th Fibonacci number, `F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)`.

**Why it's DP:** `F(n-2)` is recomputed many times in naive recursion (overlapping subproblems); optimal answer for `n` is built directly from optimal answers for `n-1` and `n-2` (optimal substructure).

**State:** `dp[i]` = the `i`-th Fibonacci number.
**Transition:** `dp[i] = dp[i-1] + dp[i-2]`.
**Base case:** `dp[0]=0, dp[1]=1`.

```python
def fib(n: int) -> int:
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1
```

**Dry Run** (`n = 5`):

| Step | i | prev2 | prev1 | Explanation |
|---|---|---|---|---|
| start | - | 0 | 1 | base cases |
| 1 | 2 | 1 | 1 | dp[2] = 0+1 = 1 |
| 2 | 3 | 1 | 2 | dp[3] = 1+1 = 2 |
| 3 | 4 | 2 | 3 | dp[4] = 1+2 = 3 |
| 4 | 5 | 3 | 5 | dp[5] = 2+3 = 5 |

Result: `fib(5) = 5`. ✅

**Complexity:** Time `O(n)`, Space `O(1)` (space-optimized) or `O(n)` (full table).
**Edge cases:** `n=0`, `n=1`, negative `n` (invalid input — validate!).
**Common mistakes:** Off-by-one on array size; forgetting both base cases; using naive recursion in an interview without mentioning complexity.
**Variations:** Tribonacci (`dp[i]=dp[i-1]+dp[i-2]+dp[i-3]`), Fibonacci mod `p`, matrix-exponentiation Fibonacci for `O(log n)`.

#### 5.1.2 Climbing Stairs

**Problem:** You can climb 1 or 2 steps at a time. How many distinct ways to reach step `n`?

**Identification clue:** "Number of ways" + "each step depends on a fixed number of previous steps" → classic Fibonacci-shaped counting DP.

**State:** `dp[i]` = number of ways to reach step `i`.
**Transition:** `dp[i] = dp[i-1] + dp[i-2]` (arrive from one step below, or two steps below).
**Base case:** `dp[0]=1` (one way: do nothing), `dp[1]=1`.

```python
def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1
```

This is *literally* Fibonacci shifted by one index — recognizing structural equivalence between problems is a key interview skill.

**Complexity:** `O(n)` time, `O(1)` space.
**Memoization version:**

```python
from functools import lru_cache

def climb_stairs_memo(n: int) -> int:
    @lru_cache(maxsize=None)
    def dp(i):
        if i <= 1:
            return 1
        return dp(i - 1) + dp(i - 2)
    return dp(n)
```

#### 5.1.3 Min Cost Climbing Stairs

**Problem:** `cost[i]` = cost to step on stair `i`. Starting at step 0 or 1, reach beyond the last stair with minimum total cost.

**State:** `dp[i]` = minimum cost to reach step `i`.
**Transition:** `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`.
**Base case:** `dp[0] = cost[0]`, `dp[1] = cost[1]`.
**Answer:** `min(dp[n-1], dp[n-2])` (can step off from either of the last two stairs).

```python
def min_cost_climbing_stairs(cost: list[int]) -> int:
    n = len(cost)
    prev2, prev1 = cost[0], cost[1]
    for i in range(2, n):
        prev2, prev1 = prev1, cost[i] + min(prev1, prev2)
    return min(prev1, prev2)
```

**Dry run** (`cost = [10,15,20]`):

| i | value | reasoning |
|---|---|---|
| 0 | 10 | base |
| 1 | 15 | base |
| 2 | 20 + min(15,10) = 30 | dp[2] |

Answer: `min(dp[1], dp[2]) = min(15, 30) = 15`.

**Common mistake:** Forgetting you can *start* at index 0 OR 1 — both are "free" entry points, not just index 0.

#### 5.1.4 House Robber I

**Problem:** Rob houses in a line, `nums[i]` = money in house `i`. Can't rob two adjacent houses. Maximize total money.

**Why DP:** At each house you face a binary decision (rob / skip) whose optimal outcome depends only on the best solutions to the prefix — classic optimal substructure.

**State:** `dp[i]` = max money robbable from houses `0..i`.
**Transition:** `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` — either skip house `i` (`dp[i-1]`), or rob it (`dp[i-2] + nums[i]`).
**Base case:** `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])`.

```python
def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
    return prev1
```

**Dry run** (`nums = [2,7,9,3,1]`):

| i | nums[i] | dp[i] | decision |
|---|---|---|---|
| 0 | 2 | 2 | rob house 0 |
| 1 | 7 | 7 | rob house 1 (better than 2) |
| 2 | 9 | max(7, 2+9)=11 | rob house 2 |
| 3 | 3 | max(11, 7+3)=11 | skip house 3 |
| 4 | 1 | max(11, 11+1)=12 | rob house 4 |

Answer: `12`. ✅ (Rob houses 0, 2, 4 → 2+9+1 = 12.)

**Complexity:** `O(n)` time, `O(1)` space.
**Common mistakes:** Forgetting the `len(nums)==1` edge case; conflating "adjacent in array" with "adjacent in value."

#### 5.1.5 House Robber II (Circular Street)

**Problem:** Same as above, but houses form a circle — house 0 and house `n-1` are adjacent.

**Key Insight:** Since house 0 and house `n-1` can't both be robbed, the answer is:
`max(rob(nums[0 : n-1]), rob(nums[1 : n]))` — i.e., solve House Robber I twice, once excluding the last house, once excluding the first.

```python
def rob_circular(nums: list[int]) -> int:
    def rob_linear(houses: list[int]) -> int:
        prev2, prev1 = 0, 0
        for money in houses:
            prev2, prev1 = prev1, max(prev1, prev2 + money)
        return prev1

    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

**Interview Tip:** This "reduce a circular problem to two linear subproblems" trick recurs constantly (Stone Game variants, circular subarray problems) — remember it as a named technique: **"break the circle at each fixed point."**

#### 5.1.6 Tribonacci

**Problem:** `T(0)=0, T(1)=1, T(2)=1, T(n)=T(n-1)+T(n-2)+T(n-3)`.

```python
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c
```

**Generalization:** For a "k-bonacci" sequence, keep a rolling window of the last `k` values — this generalizes to **any fixed-lookback linear recurrence**.

---

### 5.2 Knapsack Pattern

The Knapsack pattern covers any problem where you choose a subset of items under a **capacity constraint** to optimize value.

```
ASCII: Knapsack Decision Tree (item i, capacity w)
---------------------------------------------------
                dp(i, w)
               /         \
     skip item i       take item i (if weight[i] <= w)
     dp(i-1, w)         value[i] + dp(i-1, w - weight[i])
```

#### 5.2.1 0/1 Knapsack

**Problem:** `n` items, each with `weight[i]` and `value[i]`. Choose a subset (each item used **at most once**) to maximize value without exceeding capacity `W`.

**State:** `dp[i][w]` = max value using first `i` items with capacity `w`.
**Transition:** `dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])` if `weight[i] <= w`, else `dp[i-1][w]`.
**Base case:** `dp[0][w] = 0` for all `w` (no items → no value).

```python
def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w_i, v_i = weights[i - 1], values[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]                     # option 1: skip item i
            if w_i <= w:                                 # option 2: take item i
                dp[i][w] = max(dp[i][w], dp[i - 1][w - w_i] + v_i)
    return dp[n][capacity]
```

**Dry run** (`weights=[1,3,4,5]`, `values=[1,4,5,7]`, `capacity=7`):

```
DP Table (rows = items considered, cols = capacity 0..7)

        w:  0  1  2  3  4  5  6  7
i=0        0  0  0  0  0  0  0  0
i=1 (w=1,v=1) 0  1  1  1  1  1  1  1
i=2 (w=3,v=4) 0  1  1  4  5  5  5  5
i=3 (w=4,v=5) 0  1  1  4  5  6  6  9
i=4 (w=5,v=7) 0  1  1  4  5  7  8  9
```

Answer: `dp[4][7] = 9` (items with weight 3 and 4 → value 4+5=9).

**Space-Optimized Version (1D, iterate capacity BACKWARD):**

```python
def knapsack_01_optimized(weights: list[int], values: list[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    for w_i, v_i in zip(weights, values):
        for w in range(capacity, w_i - 1, -1):   # MUST go backward!
            dp[w] = max(dp[w], dp[w - w_i] + v_i)
    return dp[capacity]
```

> **Warning:** Iterating the capacity loop **forward** in the 1D version would let you use the same item multiple times (accidentally turning 0/1 Knapsack into Unbounded Knapsack). This is the single most common 0/1 Knapsack bug.

**Complexity:** Time `O(n·W)`, Space `O(n·W)` → `O(W)` optimized.
**Edge cases:** capacity `0`; item weight `0`; all items too heavy.
**When NOT to use DP:** if `W` is astronomically large (e.g., `10^9`) — then Knapsack DP is infeasible and you need meet-in-the-middle or approximation algorithms instead.

#### 5.2.2 Unbounded Knapsack

**Problem:** Same as above but each item can be used **unlimited** times.

**Transition:** `dp[w] = max(dp[w], dp[w - weight[i]] + value[i])`, iterating capacity **forward** (since reuse is allowed).

```python
def knapsack_unbounded(weights: list[int], values: list[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    for w in range(1, capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]
```

**Key contrast with 0/1 Knapsack:** direction of the capacity loop is the *only* structural difference — internalize this table:

| Knapsack Type | Loop Order | Reuse Items? |
|---|---|---|
| 0/1 Knapsack (1D) | capacity **backward** | No |
| Unbounded Knapsack | capacity **forward** | Yes |

#### 5.2.3 Subset Sum

**Problem:** Given a set of positive integers, is there a subset that sums exactly to `target`?

**State:** `dp[i][s]` = True if a subset of the first `i` numbers sums to `s`.
**Transition:** `dp[i][s] = dp[i-1][s] or (s >= nums[i-1] and dp[i-1][s-nums[i-1]])`.

```python
def subset_sum(nums: list[int], target: int) -> bool:
    dp = [False] * (target + 1)
    dp[0] = True                          # sum 0 is always achievable (empty subset)
    for num in nums:
        for s in range(target, num - 1, -1):   # 0/1 Knapsack shape -> backward
            dp[s] = dp[s] or dp[s - num]
    return dp[target]
```

This is 0/1 Knapsack with `value[i] = weight[i]` and a **boolean** objective instead of a maximization objective — recognizing this equivalence saves derivation time in interviews.

#### 5.2.4 Equal Partition (Partition Equal Subset Sum)

**Problem:** Can the array be partitioned into two subsets with equal sum?

**Reduction:** Equivalent to Subset Sum with `target = total_sum / 2` (if `total_sum` is odd, answer is immediately `False`).

```python
def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    return subset_sum(nums, total // 2)
```

#### 5.2.5 Target Sum

**Problem:** Assign `+` or `-` to each number so the expression evaluates to `target`. Count the number of ways.

**Key transformation:** Let `P` = sum of positively-signed numbers, `N` = sum of negatively-signed numbers.
`P - N = target` and `P + N = total_sum` → `P = (target + total_sum) / 2`.
This reduces the problem to: **"count subsets that sum to P"** — a counting variant of Subset Sum.

```python
def find_target_sum_ways(nums: list[int], target: int) -> int:
    total = sum(nums)
    if abs(target) > total or (total + target) % 2 != 0:
        return 0
    P = (total + target) // 2
    dp = [0] * (P + 1)
    dp[0] = 1
    for num in nums:
        for s in range(P, num - 1, -1):
            dp[s] += dp[s - num]
    return dp[P]
```

**Common mistake:** Forgetting the parity check `(total + target) % 2 != 0` — if it fails, no integer solution for `P` exists.

#### 5.2.6 Coin Change I (Minimum Coins)

**Problem:** Minimum number of coins to make `amount` (unlimited supply of each denomination). Return `-1` if impossible.

**State:** `dp[a]` = min coins to make amount `a`.
**Transition:** `dp[a] = min(dp[a - c] + 1 for c in coins if c <= a)`.
**Base case:** `dp[0] = 0`.

```python
def coin_change_min(coins: list[int], amount: int) -> int:
    INF = float('inf')
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != INF else -1
```

**Dry run** (`coins=[1,2,5]`, `amount=11`):

| a | dp[a] | best coin used |
|---|---|---|
| 0 | 0 | - |
| 5 | 1 | one 5 |
| 10 | 2 | two 5s |
| 11 | 3 | 5+5+1 |

#### 5.2.7 Coin Change II (Number of Combinations)

**Problem:** Count the number of *combinations* (order doesn't matter) that make `amount`.

**Crucial difference from Coin Change I:** Loop order! Coins on the **outer** loop, amount on the **inner** loop — this enforces combinations (not permutations).

```python
def coin_change_ways(coins: list[int], amount: int) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:                    # outer: coin
        for a in range(c, amount + 1):  # inner: amount
            dp[a] += dp[a - c]
    return dp[amount]
```

> **Interview Tip:** If a problem asks for *combinations* (unordered), put the item loop outside. If it asks for *permutations* (ordered, e.g., "Combination Sum IV" on LeetCode — a misleading name!), put the amount/target loop outside instead. This single loop-order swap is a frequently-tested subtlety.

#### 5.2.8 Rod Cutting

**Problem:** Rod of length `n`, `price[i]` = price of a piece of length `i+1`. Maximize revenue from cutting the rod into pieces.

**State:** `dp[L]` = max revenue for rod length `L`.
**Transition:** `dp[L] = max(price[i] + dp[L - (i+1)] for i in range(L))`.

```python
def rod_cutting(price: list[int], n: int) -> int:
    dp = [0] * (n + 1)
    for L in range(1, n + 1):
        best = float('-inf')
        for i in range(L):
            piece_len = i + 1
            if piece_len <= L:
                best = max(best, price[i] + dp[L - piece_len])
        dp[L] = best
    return dp[n]
```

This is structurally **Unbounded Knapsack** — "cut length" = "item weight," "price" = "item value," rod length = "capacity."

---

### 5.3 Sequence DP

Sequence DP problems compare or analyze one or two sequences (arrays/strings), typically using a 1D or 2D table indexed by position(s) in the sequence(s).

#### 5.3.1 Longest Increasing Subsequence (LIS)

**Problem:** Find the length of the longest strictly increasing subsequence in an array.

**State:** `dp[i]` = length of the LIS **ending exactly at index `i`**.
**Transition:** `dp[i] = max(dp[j] + 1 for j < i if nums[j] < nums[i])`, else `dp[i] = 1`.

```
ASCII: LIS Transition Visualization for nums = [10, 9, 2, 5, 3, 7, 101, 18]

index:   0   1   2   3   4   5    6    7
nums:   10   9   2   5   3   7  101   18
dp:      1   1   1   2   2   3    4    4
                       ^
             dp[3] = dp[2]+1 (5 > 2)
                       ^
             dp[5] = max(dp[2],dp[3],dp[4])+1 = dp[4]+1 = 3 (7>2,5,3)
```

```python
def length_of_lis(nums: list[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

**Complexity:** `O(n²)` time, `O(n)` space.

**Optimized O(n log n) — Patience Sorting with Binary Search:**

```python
import bisect

def length_of_lis_fast(nums: list[int]) -> int:
    tails = []  # tails[k] = smallest possible tail value of an increasing subseq of length k+1
    for x in nums:
        pos = bisect.bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)
```

**Why this works:** `tails` is always sorted. Replacing an existing tail with a smaller value doesn't shrink the *length* of any subsequence, but it keeps future extensions easier — this is a **greedy + binary search** optimization layered on top of DP intuition (not DP itself, but critical to mention as an interview follow-up).

**Common mistake:** Confusing "subsequence" (elements need not be contiguous) with "subarray" (must be contiguous) — always clarify with the interviewer.

#### 5.3.2 Number of Longest Increasing Subsequences

**Problem:** Count how many LIS's of maximum length exist.

**State:** `dp[i]` = LIS length ending at `i`; `cnt[i]` = number of LIS's of that length ending at `i`.

```python
def find_number_of_lis(nums: list[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n
    cnt = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]
                elif dp[j] + 1 == dp[i]:
                    cnt[i] += cnt[j]
    longest = max(dp)
    return sum(c for d, c in zip(dp, cnt) if d == longest)
```

#### 5.3.3 Longest Common Subsequence (LCS)

**Problem:** Given strings `s1`, `s2`, find the length of their longest common subsequence.

**State:** `dp[i][j]` = LCS length of `s1[0:i]` and `s2[0:j]`.
**Transition:**
- If `s1[i-1] == s2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`
- Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

```
ASCII: LCS DP Table for s1="ABCBDAB", s2="BDCABA"

        ""  B  D  C  A  B  A
    ""   0  0  0  0  0  0  0
    A    0  0  0  0  1  1  1
    B    0  1  1  1  1  2  2
    C    0  1  1  2  2  2  2
    B    0  1  1  2  2  3  3
    D    0  1  2  2  2  3  3
    A    0  1  2  2  3  3  4
    B    0  1  2  2  3  4  4
```

```python
def longest_common_subsequence(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

**Space-optimized (2 rows):**

```python
def lcs_optimized(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            curr[j] = prev[j - 1] + 1 if s1[i - 1] == s2[j - 1] else max(prev[j], curr[j - 1])
        prev = curr
    return prev[n]
```

**Complexity:** `O(m·n)` time, `O(m·n)` → `O(min(m,n))` optimized.
**Reconstructing the actual subsequence** requires keeping the full table (or backtracking pointers) — space optimization sacrifices the ability to reconstruct the path.

#### 5.3.4 Longest Common Substring

**Problem:** Like LCS but the match must be **contiguous**.

**Transition change:** on mismatch, reset to `0` instead of taking a max.

```python
def longest_common_substring(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    best = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                best = max(best, dp[i][j])
            # else dp[i][j] stays 0 (contiguity broken)
    return best
```

#### 5.3.5 Edit Distance (Levenshtein Distance)

**Problem:** Minimum number of insertions, deletions, substitutions to convert `s1` into `s2`.

**State:** `dp[i][j]` = edit distance between `s1[0:i]` and `s2[0:j]`.
**Transition:**
- If `s1[i-1] == s2[j-1]`: `dp[i][j] = dp[i-1][j-1]` (no operation needed)
- Else: `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])` (delete, insert, replace)

```python
def edit_distance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i          # delete all of s1[:i]
    for j in range(n + 1):
        dp[0][j] = j          # insert all of s2[:j]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete from s1
                    dp[i][j - 1],      # insert into s1
                    dp[i - 1][j - 1],  # replace
                )
    return dp[m][n]
```

**Dry run** (`s1="horse"`, `s2="ros"`) → answer `3` (horse→rorse→rose→ros).

**Complexity:** `O(m·n)` time and space; space-optimizable to `O(min(m,n))`.

#### 5.3.6 Delete Operation for Two Strings

**Problem:** Minimum deletions (only deletions, no insert/replace) to make two strings equal.

**Key insight:** Equivalent to `len(s1) + len(s2) - 2 * LCS(s1, s2)`.

```python
def min_distance_delete_only(s1: str, s2: str) -> int:
    lcs = longest_common_subsequence(s1, s2)
    return len(s1) + len(s2) - 2 * lcs
```

#### 5.3.7 Shortest Common Supersequence Length

**Problem:** Shortest string that has both `s1` and `s2` as subsequences.

**Key insight:** `len(SCS) = len(s1) + len(s2) - LCS(s1, s2)`.

```python
def shortest_common_supersequence_length(s1: str, s2: str) -> int:
    return len(s1) + len(s2) - longest_common_subsequence(s1, s2)
```

#### 5.3.8 Distinct Subsequences

**Problem:** Count how many distinct subsequences of `s` equal `t`.

**State:** `dp[i][j]` = number of ways `s[0:i]` forms `t[0:j]`.
**Transition:** if `s[i-1]==t[j-1]`: `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]` (use this char, or skip it), else `dp[i][j] = dp[i-1][j]`.
**Base case:** `dp[i][0] = 1` for all `i` (empty target always matched once, by deleting everything).

```python
def num_distinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[m][n]
```

#### 5.3.9 Interleaving String

**Problem:** Check if `s3` is formed by interleaving `s1` and `s2` (preserving relative order within each).

**State:** `dp[i][j]` = True if `s3[0:i+j]` can be formed from `s1[0:i]` and `s2[0:j]`.
**Transition:** `dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])`.

```python
def is_interleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                       (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
    return dp[m][n]
```

---

### 5.4 Grid DP

Grid DP problems traverse a 2D grid where movement is typically restricted (e.g., only right/down), and each cell's optimal value depends on cells above/left of it.

#### 5.4.1 Unique Paths

**Problem:** Count paths from top-left to bottom-right of an `m x n` grid, moving only right or down.

**State:** `dp[r][c]` = number of paths to reach cell `(r,c)`.
**Transition:** `dp[r][c] = dp[r-1][c] + dp[r][c-1]`.
**Base case:** `dp[0][c] = 1` and `dp[r][0] = 1` (only one way along an edge).

```
ASCII: Unique Paths DP Table (m=3, n=3)

  1  1  1
  1  2  3
  1  3  6
```

```python
def unique_paths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[m - 1][n - 1]
```

**Space-optimized (1 row):**

```python
def unique_paths_optimized(m: int, n: int) -> int:
    row = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            row[c] += row[c - 1]
    return row[-1]
```

**Closed-form alternative:** `C(m+n-2, m-1)` via combinatorics — worth mentioning as an `O(1)`-ish alternative (ignoring big-int multiplication cost), showing DP isn't always the *only* tool.

#### 5.4.2 Unique Paths II (With Obstacles)

**Transition:** Same as above, but `dp[r][c] = 0` if `grid[r][c] == 1` (obstacle).

```python
def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 if grid[0][0] == 0 else 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                dp[r][c] = 0
                continue
            if r > 0:
                dp[r][c] += dp[r - 1][c]
            if c > 0:
                dp[r][c] += dp[r][c - 1]
            if r == 0 and c == 0:
                dp[r][c] = 1
    return dp[m - 1][n - 1]
```

**Common mistake:** Forgetting that an obstacle at the very start (`grid[0][0]==1`) means the answer is immediately `0`.

#### 5.4.3 Minimum Path Sum

**Problem:** Path from top-left to bottom-right minimizing sum of cell values.

**Transition:** `dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])`.

```python
def min_path_sum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for c in range(1, n):
        dp[0][c] = dp[0][c - 1] + grid[0][c]
    for r in range(1, m):
        dp[r][0] = dp[r - 1][0] + grid[r][0]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
    return dp[m - 1][n - 1]
```

#### 5.4.4 Triangle (Minimum Path Sum, Triangle Shape)

**Problem:** Given a triangle array, find the minimum path sum from top to bottom (each step moves to an adjacent number on the row below).

**Best approach:** Work **bottom-up** — this avoids needing to track "which cells are reachable" from the top.

```python
def minimum_total(triangle: list[list[int]]) -> int:
    n = len(triangle)
    dp = triangle[-1][:]                     # start with the last row
    for r in range(n - 2, -1, -1):
        for c in range(len(triangle[r])):
            dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
    return dp[0]
```

**Why bottom-up is superior here:** Top-down would require checking boundary conditions (`c-1` might not exist on the left edge); bottom-up naturally has exactly two valid children (`c` and `c+1`) for every interior cell.

#### 5.4.5 Cherry Pickup (Overview)

**Problem (advanced):** Two agents traverse a grid from `(0,0)` to `(n-1,n-1)` simultaneously, collecting cherries, maximizing the total collected (cells are zeroed after being visited by either agent).

**Key idea:** Since both agents take the same number of steps at any given time, track both positions with a *single* time-synchronized state: `dp[r1][r2][t]` where `c1 = t - r1`, `c2 = t - r2` are derived (not stored) — reducing what looks like 4D state down to effectively 3D. This is a **Tree/Grid DP + simultaneous-agent** pattern common in "two people traverse together" problems; full derivation is beyond a first pass but the state-reduction insight (derive a coordinate instead of storing it) generalizes broadly.

---

### 5.5 Interval DP

Interval DP solves problems over a **range `[i, j]`**, typically by choosing a "split point" `k` inside the range and combining the two halves. The defining feature: **iterate by increasing interval length**, not by index.

```
ASCII: Interval DP Fill Order (by increasing length)
------------------------------------------------------
len=1:  dp[0][0] dp[1][1] dp[2][2] dp[3][3]
len=2:  dp[0][1] dp[1][2] dp[2][3]
len=3:  dp[0][2] dp[1][3]
len=4:  dp[0][3]
   (each relies only on SHORTER intervals already computed)
```

#### 5.5.1 Matrix Chain Multiplication

**Problem:** Given dimensions of matrices to multiply in sequence, find the minimum number of scalar multiplications by choosing optimal parenthesization.

**State:** `dp[i][j]` = min cost to multiply matrices `i..j`.
**Transition:** `dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j] for k in range(i, j))`.
**Base case:** `dp[i][i] = 0` (single matrix, no multiplication needed).

```python
def matrix_chain_order(p: list[int]) -> int:
    n = len(p) - 1                      # number of matrices
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):       # length = number of matrices in this chain
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]
```

**Complexity:** `O(n³)` time (`n²` states × `O(n)` split choices), `O(n²)` space.

#### 5.5.2 Burst Balloons

**Problem:** Bursting balloon `i` gives `nums[i-1]*nums[i]*nums[i+1]` coins. Maximize total coins from bursting all balloons.

**Key reframing (the hard insight):** Instead of thinking "which balloon do I burst first," think "which balloon do I burst **last** within a range `(i, j)`" — this makes the two sub-ranges independent, which is required for valid DP decomposition.

**State:** `dp[i][j]` = max coins from bursting all balloons strictly between `i` and `j` (exclusive boundaries, padded with virtual `1`s).
**Transition:** `dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j] for k in range(i+1, j))`.

```python
def max_coins(nums: list[int]) -> int:
    balloons = [1] + nums + [1]
    n = len(balloons)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for i in range(0, n - length):
            j = i + length
            for k in range(i + 1, j):
                coins = balloons[i] * balloons[k] * balloons[j]
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + coins)
    return dp[0][n - 1]
```

**Interview Tip:** This "last action instead of first action" reframing trick is one of the most important advanced DP insights — it appears whenever the naive first-choice split makes subproblems *dependent* on each other.

#### 5.5.3 Palindrome Partitioning II (Minimum Cuts)

**Problem:** Minimum cuts needed to partition a string into palindromic substrings.

**Step 1 — Precompute palindrome table:** `is_pal[i][j]` = True if `s[i:j+1]` is a palindrome.
**Step 2 — DP over cut positions:** `dp[i]` = min cuts for `s[0:i+1]`.

```python
def min_cut(s: str) -> int:
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                is_pal[i][j] = (length == 2) or is_pal[i + 1][j - 1]

    dp = [0] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
            continue
        dp[i] = float('inf')
        for k in range(i):
            if is_pal[k + 1][i]:
                dp[i] = min(dp[i], dp[k] + 1)
    return dp[n - 1]
```

**Complexity:** `O(n²)` for the palindrome table + `O(n²)` for the cut DP = `O(n²)` overall.

#### 5.5.4 Strange Printer

**Problem:** A printer can print a contiguous same-character sequence in one turn, and can overwrite existing characters. Minimum turns to print string `s`.

**State:** `dp[i][j]` = min turns to print `s[i:j+1]`.
**Key transition insight:** If `s[i] == s[k]` for some `k` in `(i, j]`, we can "merge" the first print with the print at `k`, saving a turn.

```python
def strange_printer(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            dp[i][j] = dp[i][j - 1] + 1          # naive: one extra turn for s[j]
            for k in range(i, j):
                if s[k] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i][k] + (dp[k + 1][j - 1] if k + 1 <= j - 1 else 0))
    return dp[0][n - 1]
```

---

### 5.6 Partition DP

Partition DP splits a sequence into `k` contiguous groups, optimizing some function over the groups.

#### 5.6.1 Partition Array for Maximum Sum

**Problem:** Partition array into contiguous subarrays of length at most `k`; each subarray's values become its max value; maximize total sum.

**State:** `dp[i]` = max sum for the first `i` elements.
**Transition:** try every partition size `L` (1..k) for the *last* group ending at `i`.

```python
def max_sum_after_partitioning(arr: list[int], k: int) -> int:
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        curr_max = 0
        for L in range(1, min(k, i) + 1):
            curr_max = max(curr_max, arr[i - L])
            dp[i] = max(dp[i], dp[i - L] + curr_max * L)
    return dp[n]
```

**Complexity:** `O(n·k)` time, `O(n)` space.

#### 5.6.2 Stone Game (Series Overview)

**Problem (Stone Game I):** Two players alternately take stones from either end of a row; each maximizes their own total; determine if the first player wins.

**State:** `dp[i][j]` = the **maximum score difference** (current player's score minus opponent's) achievable from the subarray `[i, j]`.
**Transition:** `dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])` — the current player picks the option that maximizes their net advantage, since after their pick, the opponent becomes the "current player" of the remaining subgame (hence the subtraction).

```python
def stone_game(piles: list[int]) -> bool:
    n = len(piles)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = piles[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
    return dp[0][n - 1] > 0
```

**Interview Tip:** This "score difference instead of absolute score" trick is the standard way to model **two-player zero-sum alternating games** with DP — it collapses what looks like a minimax problem into a single-array optimization.

**Variations:** Stone Game II/III/IV add move-count constraints or special moves (squares, variable pile counts) — same score-difference core idea, extended state (e.g., `dp[i][M]` tracking a move-limit parameter `M`).

---

### 5.7 State Machine DP

State Machine DP models problems where an entity moves between a small, fixed set of **states** over time, and the transition depends on both the previous state and the current input.

```
ASCII: Generic State Machine DP
---------------------------------
   State A ---transition_AB---> State B
      ^                              |
      |__________transition_BA______|

dp[i][state] = best value at step i while in `state`
```

#### 5.7.1 Best Time to Buy and Sell Stock I (One Transaction)

**Problem:** One buy + one sell. Maximize profit.

**State:** `min_price_so_far`, `max_profit_so_far` (this is a rolling/greedy-flavored DP — a 2-state machine: "not holding" vs "holding").

```python
def max_profit_one_transaction(prices: list[int]) -> int:
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit
```

#### 5.7.2 Best Time to Buy and Sell Stock II (Unlimited Transactions)

**State:** `dp[i][0]` = max profit at day `i` **not holding** stock; `dp[i][1]` = max profit at day `i` **holding** stock.
**Transition:**
- `dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])` (rest, or sell today)
- `dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])` (rest, or buy today)

```python
def max_profit_unlimited(prices: list[int]) -> int:
    hold, cash = float('-inf'), 0
    for price in prices:
        cash, hold = max(cash, hold + price), max(hold, cash - price)
    return cash
```

**Dry run** (`prices=[7,1,5,3,6,4]`):

| day | price | cash (not holding) | hold (holding) |
|---|---|---|---|
| 0 | 7 | 0 | -7 |
| 1 | 1 | 0 | max(-7, 0-1)=-1 |
| 2 | 5 | max(0,-1+5)=4 | max(-1, 0-5)=-1 |
| 3 | 3 | max(4,-1+3)=4 | max(-1, 4-3)=1 |
| 4 | 6 | max(4, 1+6)=7 | max(1, 4-6)=1 |
| 5 | 4 | max(7, 1+4)=7 | max(1, 7-4)=3 |

Answer: `7`.

#### 5.7.3 Best Time to Buy and Sell Stock III (At Most 2 Transactions)

**State:** `dp[i][k][0/1]` — day `i`, transaction number `k` (1 or 2), holding or not. Space-optimized to 4 scalar variables.

```python
def max_profit_two_transactions(prices: list[int]) -> int:
    buy1 = buy2 = float('-inf')
    sell1 = sell2 = 0
    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)
    return sell2
```

#### 5.7.4 Best Time to Buy and Sell Stock IV (At Most K Transactions)

**Generalized state:** `dp[i][k][0/1]`, size `O(n·k)`.

```python
def max_profit_k_transactions(k: int, prices: list[int]) -> int:
    n = len(prices)
    if n == 0 or k == 0:
        return 0
    if k >= n // 2:                                # unlimited transactions case
        return max_profit_unlimited(prices)
    buy = [float('-inf')] * (k + 1)
    sell = [0] * (k + 1)
    for price in prices:
        for t in range(1, k + 1):
            buy[t] = max(buy[t], sell[t - 1] - price)
            sell[t] = max(sell[t], buy[t] + price)
    return sell[k]
```

**Optimization note:** When `k >= n//2`, transactions are effectively unlimited (you can never make more than `n//2` profitable transactions), so we short-circuit to the O(n) unlimited-transaction solution to avoid an unnecessary `O(n·k)` blow-up.

#### 5.7.5 Best Time to Buy and Sell Stock with Cooldown

**State:** three states — `held`, `sold` (just sold, cooldown starts), `rest` (free to buy).
**Transition:**
- `held[i] = max(held[i-1], rest[i-1] - price)`
- `sold[i] = held[i-1] + price`
- `rest[i] = max(rest[i-1], sold[i-1])`

```python
def max_profit_cooldown(prices: list[int]) -> int:
    if not prices:
        return 0
    held, sold, rest = float('-inf'), 0, 0
    for price in prices:
        prev_sold = sold
        sold = held + price
        held = max(held, rest - price)
        rest = max(rest, prev_sold)
    return max(sold, rest)
```

#### 5.7.6 Best Time to Buy and Sell Stock with Transaction Fee

**Transition:** subtract `fee` at the point of sale.

```python
def max_profit_with_fee(prices: list[int], fee: int) -> int:
    cash, hold = 0, float('-inf')
    for price in prices:
        cash, hold = max(cash, hold + price - fee), max(hold, cash - price)
    return cash
```

#### 5.7.7 Decode Ways

**Problem:** Count ways to decode a digit string into letters (`'1'->'A'`...`'26'->'Z'`).

**State:** `dp[i]` = number of ways to decode `s[0:i]`.
**Transition:** `dp[i] += dp[i-1]` if `s[i-1] != '0'` (single digit valid); `dp[i] += dp[i-2]` if `s[i-2:i]` forms a valid two-digit code (`10`-`26`).

```python
def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        one_digit = int(s[i - 1])
        two_digit = int(s[i - 2:i])
        if one_digit != 0:
            dp[i] += dp[i - 1]
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    return dp[n]
```

**Edge cases:** leading `'0'` (invalid), `"06"` (invalid two-digit — leading zero), consecutive zeros (`"100"` → only decodable as `1,0,0`? No — `0` alone is invalid, must check carefully: `"100"` → `dp` sees `'0'` at position 2 which is invalid alone, must combine as `"10"` then `"0"` fails, so answer is 0 — a classic tricky edge case worth tracing by hand).

#### 5.7.8 Paint House

**Problem:** `n` houses in a row, 3 paint colors, cost matrix `cost[i][color]`. No two adjacent houses share a color. Minimize total cost.

**State:** `dp[i][c]` = min cost to paint houses `0..i` with house `i` painted color `c`.
**Transition:** `dp[i][c] = cost[i][c] + min(dp[i-1][c'] for c' != c)`.

```python
def min_cost_paint_house(costs: list[list[int]]) -> int:
    if not costs:
        return 0
    r, g, b = costs[0]
    for i in range(1, len(costs)):
        r, g, b = (
            costs[i][0] + min(g, b),
            costs[i][1] + min(r, b),
            costs[i][2] + min(r, g),
        )
    return min(r, g, b)
```

---

### 5.8 Advanced DP (Bitmask & Digit)

#### 5.8.1 Bitmask DP — Traveling Salesman Problem (TSP)

**Why bitmask:** When the state needs to track "which subset of items/cities have been visited," and `n` is small (typically `n <= 20`), represent the subset as an integer bitmask — each bit = one element's inclusion.

```
ASCII: Bitmask Representation for n=4 cities
------------------------------------------------
mask = 0b1011  ->  cities {0, 1, 3} visited, city 2 not visited
        bit3 bit2 bit1 bit0
          1    0    1    1
```

**State:** `dp[mask][i]` = min cost to visit exactly the cities in `mask`, ending at city `i`.
**Transition:** `dp[mask | (1<<j)][j] = min(dp[mask][i] + dist[i][j])` for every unvisited `j`.
**Base case:** `dp[1][0] = 0` (start at city 0, only city 0 visited).

```python
def tsp(dist: list[list[int]]) -> int:
    n = len(dist)
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0                                   # start at city 0
    for mask in range(1 << n):
        for i in range(n):
            if dp[mask][i] == INF or not (mask & (1 << i)):
                continue
            for j in range(n):
                if mask & (1 << j):
                    continue                        # already visited
                new_mask = mask | (1 << j)
                new_cost = dp[mask][i] + dist[i][j]
                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost
    full_mask = (1 << n) - 1
    return min(dp[full_mask][i] + dist[i][0] for i in range(n))
```

**Complexity:** Time `O(2^n · n²)`, Space `O(2^n · n)` — exponential, but far better than `O(n!)` brute force permutation search.

**Common mistake:** Forgetting to add the return trip to the starting city in the final answer computation.

#### 5.8.2 Digit DP — Count Numbers with a Digit Property

**Why Digit DP:** When you need to count/sum numbers in a range `[1, N]` satisfying some digit-based property (e.g., "no repeated digits," "digit sum divisible by k") — Digit DP builds the number digit-by-digit while tracking a **"tight"** flag (are we still bounded by `N`'s prefix, or free to place any digit?).

**State:** `dp[pos][tight][extra_state]` — position in the digit string, whether we're still constrained by `N`, plus any problem-specific accumulator (digit sum, last digit, count of digits used, etc).

```python
def count_numbers_with_digit_sum(N: int, target_sum: int) -> int:
    """Count integers in [0, N] whose digit sum equals target_sum."""
    digits = list(map(int, str(N)))
    n = len(digits)
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(pos: int, remaining_sum: int, tight: bool, started: bool) -> int:
        if remaining_sum < 0:
            return 0
        if pos == n:
            return 1 if (remaining_sum == 0 and started) else 0
        limit = digits[pos] if tight else 9
        total = 0
        for d in range(0, limit + 1):
            new_tight = tight and (d == limit)
            new_started = started or d > 0
            new_remaining = remaining_sum - d if new_started else remaining_sum
            total += dp(pos + 1, new_remaining, new_tight, new_started)
        return total

    return dp(0, target_sum, True, False)
```

**Line-by-line explanation**
- `tight`: True means every digit placed so far exactly matches `N`'s prefix, so the *next* digit is capped at `digits[pos]`; False means we've already placed a strictly smaller digit somewhere, so we're free to use `0..9`.
- `started`: tracks whether we've placed a non-zero digit yet (handles numbers with fewer digits than `N`, avoiding leading-zero miscounts).
- The `lru_cache` here only works correctly because `tight` is almost always `False` after the first divergence — this keeps the effectively-visited state space small despite the `bool` "always changing" tight flag.

**Common mistake:** Forgetting the `started` flag and double-counting leading zeros as significant digits.

#### 5.8.3 Tree DP (Conceptual Overview)

**Why it's DP:** A tree has no cycles, so a post-order DFS naturally computes each subtree's DP value from its children's DP values first — optimal substructure via recursion on the tree structure itself.

```
ASCII: Tree DP order of computation (post-order)
--------------------------------------------------
        root
       /    \
     A        B
    / \      /
  C    D    E

Computation order: C, D, A, E, B, root
(children always resolved before their parent)
```

**Example — House Robber III (Tree version):** `dp(node)` returns a pair `(rob_this, skip_this)`.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def rob_tree(root: TreeNode | None) -> int:
    def dfs(node):
        if not node:
            return (0, 0)                       # (rob this node, don't rob this node)
        left_rob, left_skip = dfs(node.left)
        right_rob, right_skip = dfs(node.right)
        rob_this = node.val + left_skip + right_skip
        skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
        return (rob_this, skip_this)
    return max(dfs(root))
```

#### 5.8.4 SOS DP — Sum over Subsets (Overview)

**Problem shape:** For every bitmask `m`, compute `f(m) = sum of a[s] for all subsets s of m`.

**Naive:** `O(3^n)` (iterate all subset-of-subset pairs). **SOS DP:** `O(n · 2^n)` by processing one bit at a time.

```python
def sum_over_subsets(a: list[int], n_bits: int) -> list[int]:
    dp = a[:]  # dp[mask] eventually = sum over all subsets of mask
    for bit in range(n_bits):
        for mask in range(1 << n_bits):
            if mask & (1 << bit):
                dp[mask] += dp[mask ^ (1 << bit)]
    return dp
```

This pattern underlies many bitmask-counting competitive-programming problems (e.g., "count pairs with AND/OR properties").

---

## 6. Advanced DP Concepts & Optimizations

### 6.1 State Compression (Recap & Extension)

Beyond bitmasks, state compression includes:
- Encoding `(row, col)` pairs as a single integer `row * width + col` to use 1D arrays.
- Encoding small multi-valued states (e.g., 3 colors) as base-3 digits packed into one integer.

### 6.2 Space Optimization Patterns

| Original | Optimized | Condition |
|---|---|---|
| `dp[i]` depends on `dp[i-1], dp[i-2]` | 2 scalars | Fixed constant lookback |
| `dp[i][j]` depends only on row `i-1` | 2 rows (`prev`, `curr`) | No dependency beyond one row back |
| `dp[i][w]` (Knapsack) | 1D array, iterate `w` backward | Each item used once |

### 6.3 Divide & Conquer Optimization (Overview)

Applies when the optimal split point `opt[i][j]` in interval DP is **monotonic** — i.e., `opt[i][j-1] <= opt[i][j] <= opt[i+1][j]`. This lets you binary-search (or restrict the range of) the split point `k` instead of trying all `k`, reducing `O(n³)` interval DP to `O(n² log n)`.

```
Monotonicity intuition:
  As the interval expands, the "best place to cut" doesn't
  jump around arbitrarily — it slides monotonically.
```

### 6.4 Knuth's Optimization (Overview)

A special case of D&C optimization applicable when the cost function satisfies the **quadrangle inequality**. Common in Matrix Chain Multiplication–style problems; reduces `O(n³)` to `O(n²)`.

### 6.5 Convex Hull Trick (Overview)

Used when transitions have the form `dp[i] = min_j(dp[j] + b[j] * a[i])` — a linear function per `j`. Maintaining a **lower convex hull** of these lines allows each query to be answered in `O(log n)` (or amortized `O(1)` if slopes are monotonic), turning an `O(n²)` DP into `O(n log n)`.

### 6.6 Monotonic Queue / Deque Optimization (Overview)

Used when transitions look like `dp[i] = min(dp[j])` for `j` in a **sliding window** `[i-k, i-1]`. A monotonic deque maintains window minimums/maximums in amortized `O(1)` per step, turning `O(n·k)` into `O(n)`.

```python
from collections import deque

def sliding_window_min_dp_example(nums: list[int], k: int) -> list[int]:
    """dp[i] uses min(dp[i-k..i-1]) — deque keeps candidate indices in increasing dp-value order."""
    dp = [0] * len(nums)
    dq = deque()  # stores indices, dp-values increasing front-to-back
    for i, x in enumerate(nums):
        while dq and dq[0] < i - k:
            dq.popleft()
        best_prev = dp[dq[0]] if dq else 0
        dp[i] = best_prev + x
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
        dq.append(i)
    return dp
```

### 6.7 Profile DP (Overview)

Used for grid-tiling problems (e.g., counting ways to tile a board with dominoes) where the state is the "profile" (bitmask) of the boundary between filled and unfilled cells, processed column-by-column or cell-by-cell (**broken profile** technique).

### 6.8 Probability / Expectation DP

**Key idea:** Replace "best value" with "expected value," and transitions become weighted sums instead of min/max.

```python
def knight_probability(n: int, k: int, row: int, col: int) -> float:
    moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
    dp = [[0.0] * n for _ in range(n)]
    dp[row][col] = 1.0
    for _ in range(k):
        new_dp = [[0.0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if dp[r][c] == 0:
                    continue
                prob = dp[r][c] / 8.0
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        new_dp[nr][nc] += prob
        dp = new_dp
    return sum(sum(row) for row in dp)
```

---

## 7. Applications of DP

| Application Area | How DP Is Used |
|---|---|
| **Scheduling** | Weighted Job Scheduling (interval DP + binary search for compatible jobs) |
| **Bioinformatics** | Sequence alignment (Edit Distance / LCS variants) for DNA/protein comparison |
| **NLP** | Viterbi algorithm (DP over Hidden Markov Model states) for POS tagging, speech recognition |
| **Game Theory** | Minimax with memoization for perfect-information games (Stone Game, Nim variants) |
| **AI / Reinforcement Learning** | Value Iteration / Policy Iteration are literally Bellman-equation DP over states |
| **Robotics** | Path planning under cost/obstacle grids (Grid DP) |
| **Finance** | Optimal stopping problems, portfolio optimization, options pricing (binomial trees are a DP table) |
| **Route Planning** | Bellman-Ford shortest path (an explicit DP relaxation over edges) |
| **Compiler Optimization** | Optimal instruction scheduling, register allocation, expression tree evaluation order (like Matrix Chain Mult.) |

---

## 8. Problem Recognition Guide

### 8.1 The Master Recognition Flowchart

```
                     Does the problem ask for:
                "optimal value" / "count of ways" / "yes-no feasibility"?
                                    |
                          ---------- ----------
                         | YES                  | NO
                         v                       v
        Can you define a recursive       Probably NOT dp — consider
        relation using smaller               brute force / other
        subproblems of the same                algorithms
        problem shape?
                |
        --------+--------
       | YES             | NO
       v                  v
  Do subproblems      Consider Divide &
  REPEAT/OVERLAP?      Conquer instead
       |
  -----+-----
 | YES        | NO
 v             v
  DP        Optimal substructure alone
 applies    isn't enough for DP speedup
```

### 8.2 Verbal Clues That Scream "DP"

| Clue Phrase | Likely Pattern |
|---|---|
| "minimum/maximum number of ways to..." | Counting or Knapsack DP |
| "can you make exactly X using..." | Subset Sum / Coin Change |
| "longest / shortest subsequence / substring" | Sequence DP |
| "minimum cost to merge/combine ranges" | Interval DP |
| "partition into k groups minimizing/maximizing..." | Partition DP |
| "on day i, buy/sell/hold..." | State Machine DP |
| "visit all cities/nodes at minimum cost" (small n) | Bitmask DP |
| "count numbers between L and R with property..." | Digit DP |
| "maximum sum path in a tree" | Tree DP |
| "two players take turns, optimal play" | Game-theory DP (score-difference) |

### 8.3 DP vs Greedy

| Question | If Answer Is Yes |
|---|---|
| Does the locally-best choice always lead to a globally-best solution, **provably**? | Greedy suffices (faster, simpler) |
| Could an early "greedy" choice block a better later option? | You need DP to consider all choices |

> **Rule of Thumb:** If you can't *prove* the greedy-choice property (e.g., via an exchange argument), default to DP — it's always correct if optimal substructure holds, whereas an unproven greedy heuristic risks silently wrong answers.

### 8.4 DP vs Backtracking

| Aspect | Backtracking | DP |
|---|---|---|
| Goal | Enumerate all valid solutions | Compute an optimal value / count efficiently |
| Subproblem reuse | No (explores fresh each time) | Yes (memoized) |
| Typical complexity | Exponential | Polynomial (if applicable) |
| Use when | You need actual solutions/paths, or constraints make DP state explode | You need a single optimal number, or a *manageable* set of distinct solutions |

### 8.5 State & Transition Identification Checklist

```
1. What CHANGES as the problem gets smaller? -> these become your indices.
2. What's the RANGE of each changing quantity? -> defines dp array size.
3. What's the SMALLEST valid subproblem? -> base case.
4. How does an optimal answer for a bigger problem relate to smaller ones?
   -> that relationship is your transition equation.
5. Where does the FINAL answer live in the table?
   -> not always dp[n]! Sometimes max(dp), dp[n][target], etc.
```

---

## 9. The Optimization Ladder

Every DP problem should be solved by climbing this ladder — and in interviews, you should *narrate* climbing it.

```
Rung 4: SPACE-OPTIMIZED DP    <- O(1) or O(n) space, rolling variables
             ^
Rung 3: TABULATION (Bottom-Up) <- O(n) or O(n^2) space, iterative
             ^
Rung 2: MEMOIZATION (Top-Down) <- brute force + cache
             ^
Rung 1: BRUTE-FORCE RECURSION  <- exponential, no cache
```

### 9.1 Worked Example of the Full Ladder — Coin Change (Min Coins)

```python
# Rung 1: Brute force
def coin_change_brute(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    return 1 + min((coin_change_brute(coins, amount - c) for c in coins), default=float('inf'))

# Rung 2: Memoization
from functools import lru_cache
def coin_change_memo(coins, amount):
    @lru_cache(maxsize=None)
    def dp(a):
        if a == 0:
            return 0
        if a < 0:
            return float('inf')
        return 1 + min((dp(a - c) for c in coins), default=float('inf'))
    result = dp(amount)
    return result if result != float('inf') else -1

# Rung 3: Tabulation
def coin_change_tab(coins, amount):
    INF = float('inf')
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != INF else -1

# Rung 4: Space is already O(amount) minimal here (1D) — Coin Change doesn't reduce further
# because every dp[a] potentially depends on ANY smaller a, not just a fixed lookback window.
```

**Lesson:** Not every DP can be squeezed to O(1) space — space optimization is only valid when dependencies are bounded/local. Always verify the dependency pattern before attempting to compress.

### 9.2 Transition Optimization Summary

| Technique | Speeds Up | When Applicable |
|---|---|---|
| Binary Search (patience sorting) | LIS: O(n²) → O(n log n) | Transition is monotonic and searchable |
| Monotonic Deque | Sliding-window min/max DP: O(n·k) → O(n) | Fixed-size window transitions |
| Divide & Conquer Opt. | Interval DP: O(n³) → O(n² log n) | Optimal split point is monotonic |
| Convex Hull Trick | Linear-transition DP: O(n²) → O(n log n) | Transition is `dp[j] + line(j)(x)` |
| Matrix Exponentiation | Linear recurrence: O(n) → O(log n) | Fixed-size linear recurrence (e.g. Fibonacci) |

---

## 10. Interview Preparation

### 10.1 Difficulty-Tiered Problem List

| Difficulty | Problems |
|---|---|
| **Easy** | Fibonacci, Climbing Stairs, Min Cost Climbing Stairs, House Robber I |
| **Medium** | House Robber II/III, Coin Change I/II, LIS, LCS, Unique Paths, Edit Distance, Decode Ways, Word Break, Partition Equal Subset Sum, Target Sum, Stock problems (II, with cooldown/fee) |
| **Hard** | Edit Distance variants with weighted ops, Burst Balloons, Matrix Chain Multiplication, Palindrome Partitioning II, Stock IV (k transactions), Distinct Subsequences, Cherry Pickup, Regular Expression Matching, Wildcard Matching |

### 10.2 Pattern-Wise Interview Question Map

| Pattern | Representative Questions |
|---|---|
| Knapsack | 0/1 Knapsack, Partition Equal Subset Sum, Target Sum, Coin Change I/II |
| Sequence DP | LCS, LIS, Edit Distance, Distinct Subsequences |
| Grid DP | Unique Paths I/II, Minimum Path Sum, Triangle |
| Interval DP | Matrix Chain Multiplication, Burst Balloons, Palindrome Partitioning II |
| State Machine | All Stock Buy/Sell variants, Decode Ways, Paint House |
| Bitmask | Traveling Salesman, Partition to K Equal Sum Subsets |

### 10.3 Company-Wise Tendencies (General Patterns Observed)

| Company Tendency | Common DP Focus |
|---|---|
| Big Tech (general) | LCS/LIS/Edit Distance family, Knapsack family, Stock problems |
| Quant/Finance-oriented firms | Stock trading DP variants, probability/expectation DP |
| Systems-oriented companies | Grid DP, scheduling-style interval DP |
| Competitive-programming-heavy interviews | Bitmask DP, Digit DP, optimization tricks (CHT, monotonic deque) |

> **Note:** Company tendencies shift over time and vary by team — always check current interview experience aggregators (e.g., LeetCode's company tag pages) close to your interview date rather than relying solely on generalized lists.

### 10.4 "Blind 75" / "NeetCode 150" Style DP Coverage

Both well-known curated lists include a DP section that closely tracks: Climbing Stairs, House Robber I/II, LIS, LCS, Word Break, Combination Sum IV, Decode Ways, Unique Paths, Jump Game, Coin Change, Maximum Product Subarray, Partition Equal Subset Sum, Palindromic Substrings — all of which are covered in Section 5 of this handbook.

### 10.5 Interview Thinking Process (Step-by-Step Script)

```
1. Restate the problem in your own words; confirm constraints (n size, value ranges).
2. Ask: "Can I brute-force this with recursion?" Write the recursive relation ALOUD.
3. Identify overlapping subproblems -> propose memoization.
4. State the time/space complexity of the memoized solution.
5. Convert to tabulation if asked for iterative / production-quality code.
6. Discuss space optimization possibility.
7. Walk through a dry run on a small example.
8. State edge cases explicitly (empty input, single element, all same values).
```

### 10.6 Standard DP Templates (Quick-Reference)

```python
# 1D DP Template
dp = [base_case] * (n + 1)
for i in range(1, n + 1):
    dp[i] = transition(dp[i - 1], ...)

# 2D DP Template
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = transition(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

# Interval DP Template
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = best_of([dp[i][k] + dp[k + 1][j] for k in range(i, j)])

# Bitmask DP Template
for mask in range(1 << n):
    for i in range(n):
        if mask & (1 << i):
            for j in range(n):
                if not (mask & (1 << j)):
                    dp[mask | (1 << j)][j] = transition(dp[mask][i])
```

---

## 11. Python Tips for DP

### 11.1 `functools.lru_cache` / `cache`

```python
from functools import lru_cache, cache

@lru_cache(maxsize=None)   # explicit unbounded cache
def f(n): ...

@cache                     # Python 3.9+ shorthand, equivalent to lru_cache(maxsize=None)
def g(n): ...
```

### 11.2 List Comprehensions for Table Initialization

```python
# CORRECT — creates independent inner lists
dp = [[0] * m for _ in range(n)]

# WRONG — all rows are the SAME list object (aliasing bug!)
dp = [[0] * m] * n
```

> **Warning:** `[[0]*m]*n` is one of the most common Python DP bugs — mutating `dp[0][0]` will silently mutate `dp[1][0], dp[2][0], ...` too, because all rows reference the same underlying list.

### 11.3 `collections.defaultdict` for Sparse DP

```python
from collections import defaultdict
dp = defaultdict(lambda: float('-inf'))
```

Useful when the state space is huge but sparsely visited (e.g., DP keyed by `(sum, count)` pairs that rarely occur).

### 11.4 `itertools` for Enumerating Transitions

```python
from itertools import product
for mask, i in product(range(1 << n), range(n)):
    ...
```

### 11.5 `bisect` for O(log n) Transition Search

Used heavily in LIS-style optimizations (Section 5.3.1) to replace an O(n) inner search loop with O(log n).

### 11.6 `math.inf` vs `float('inf')`

Both work identically for DP sentinel values representing "unreachable" / "infinitely bad." `math.inf` is marginally more explicit/readable in modern code.

```python
import math
dp = [math.inf] * (n + 1)
dp[0] = 0
```

### 11.7 Performance Tips

- Prefer **arrays/lists** over dictionaries when the state space is dense — array indexing avoids hashing overhead.
- Avoid redundant `len()` calls inside hot loops — cache them in a variable first.
- Use **tuple unpacking** for rolling-variable swaps (`a, b = b, a + b`) — it's both idiomatic and avoids a temp variable.
- For very large DP tables, consider `array` module or `numpy` arrays for lower memory overhead than Python lists of ints.
- Increase recursion limit only as a last resort for top-down solutions on deep recursions; prefer converting to iterative tabulation instead, since Python's actual C-stack can crash even after raising `sys.setrecursionlimit`.

### 11.8 Memory Optimization Tips

- Release big tables you no longer need: reassign to smaller structures (e.g., after computing final row, discard 2D table) so the garbage collector can reclaim memory.
- Use `__slots__` in custom node classes for Tree DP to avoid per-instance dict overhead on huge trees.

### 11.9 Common Python Pitfalls Specific to DP

| Pitfall | Fix |
|---|---|
| Mutable default arguments (`def f(n, cache={})`) | Use `cache=None` and initialize inside the function |
| Aliased nested lists (`[[0]*m]*n`) | Use list comprehension `[[0]*m for _ in range(n)]` |
| Off-by-one in table sizing | Always size tables `n+1` when `dp[i]` should mean "first i elements" |
| Recursion limit errors on large `n` | Convert to iterative tabulation |
| Unhashable memoization keys (lists, dicts as args) | Convert to tuples before calling a `lru_cache`'d function |

---

## 12. Common Mistakes

| Mistake | Why It Happens | How to Avoid |
|---|---|---|
| **Wrong state definition** | Choosing a state that doesn't capture enough info to make the transition, or captures too much (blowing up complexity) | Ask: "Given this state, can I compute the transition without any other outside info?" |
| **Missing base case** | Forgetting the smallest subproblem(s) that terminate recursion | Explicitly enumerate ALL base cases before coding the transition |
| **Incorrect transitions** | Mis-deriving the recurrence, or handling one case (e.g. "take") but not the other ("skip") | Draw the decision tree for one state by hand before coding |
| **Wrong iteration order** | Filling `dp[i]` before its dependencies `dp[i-1]`, `dp[j<i]` are ready | Always iterate in the topological order of the dependency graph (usually smallest state first) |
| **Space optimization bugs** | Iterating a 0/1 Knapsack capacity loop forward instead of backward, overwriting values still needed | Always ask: "does the current update depend on a value from the SAME pass?" — if yes, iterate in the direction that avoids reading an already-updated cell |
| **Index errors** | Off-by-one between 0-indexed arrays and 1-indexed `dp` tables sized `n+1` | Consistently pick one convention; comment which one you're using |
| **Duplicate computations** | Missing a memo check, or re-deriving results already in the table | Always check the cache/table FIRST thing inside the function |
| **Recursion limit issues** | Deep top-down recursion on large `n` (e.g. n > 10,000) | Convert to bottom-up tabulation for large inputs |

---

## 13. Cheat Sheets

### 13.1 DP Template Cheat Sheet

```python
# ---- Top-down memo skeleton ----
from functools import lru_cache
@lru_cache(maxsize=None)
def dp(state):
    if base_case(state):
        return base_value
    return combine(dp(smaller_state_1), dp(smaller_state_2))

# ---- Bottom-up tabulation skeleton ----
table = [init] * (n + 1)
table[0] = base_value
for i in range(1, n + 1):
    table[i] = combine(table[i - 1], ...)

# ---- Space-optimized skeleton ----
a, b = base_value, base_value
for i in range(1, n + 1):
    a, b = b, combine(a, b)
```

### 13.2 Pattern Recognition Cheat Sheet

| If the problem mentions... | Think... |
|---|---|
| Capacity / weight limit | Knapsack |
| Two strings/arrays compared | LCS / Edit Distance family |
| Single array, subsequence property | LIS family |
| Merging/splitting a range optimally | Interval DP |
| Buy/sell/hold over time | State Machine DP |
| Small `n`, visit-all-subsets | Bitmask DP |
| Count in numeric range `[L,R]` | Digit DP |
| Tree structure, subtree property | Tree DP |
| Alternating two-player optimal game | Score-difference DP |

### 13.3 State Definition Cheat Sheet

| Pattern | Typical State |
|---|---|
| Linear/Knapsack | `dp[i]` or `dp[i][w]` |
| Two sequences | `dp[i][j]` = first `i` of seq1, first `j` of seq2 |
| Interval | `dp[i][j]` = answer over range `[i, j]` |
| State machine | `dp[i][state]` |
| Bitmask | `dp[mask]` or `dp[mask][i]` |
| Digit DP | `dp[pos][tight][extra]` |

### 13.4 Transition Formula Cheat Sheet

| Problem | Transition |
|---|---|
| Fibonacci | `dp[i] = dp[i-1] + dp[i-2]` |
| House Robber | `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` |
| 0/1 Knapsack | `dp[w] = max(dp[w], dp[w-wt]+val)` (backward loop) |
| Unbounded Knapsack | `dp[w] = max(dp[w], dp[w-wt]+val)` (forward loop) |
| LCS | `dp[i][j] = dp[i-1][j-1]+1` if match else `max(dp[i-1][j], dp[i][j-1])` |
| Edit Distance | `dp[i][j] = dp[i-1][j-1]` if match else `1+min(del, insert, replace)` |
| LIS | `dp[i] = max(dp[j]+1 for j<i if nums[j]<nums[i])` |
| Interval DP | `dp[i][j] = min/max(dp[i][k]+dp[k+1][j]+cost)` |

### 13.5 Complexity Cheat Sheet

| Pattern | Time | Space (naive) | Space (optimized) |
|---|---|---|---|
| 1D Linear DP | O(n) | O(n) | O(1) |
| 0/1 Knapsack | O(n·W) | O(n·W) | O(W) |
| LCS / Edit Distance | O(m·n) | O(m·n) | O(min(m,n)) |
| LIS (naive) | O(n²) | O(n) | O(n) |
| LIS (optimized) | O(n log n) | O(n) | O(n) |
| Interval DP | O(n³) | O(n²) | O(n²) |
| Bitmask DP (TSP) | O(2^n · n²) | O(2^n · n) | O(2^n · n) |
| Digit DP | O(digits · states) | O(digits · states) | same (memoized) |

### 13.6 Python Syntax Cheat Sheet

```python
from functools import lru_cache, cache
import bisect, math
from collections import defaultdict, deque

@cache
def f(n): ...

INF = math.inf
dp = [[0]*m for _ in range(n)]        # correct 2D init
pos = bisect.bisect_left(sorted_list, x)
```

### 13.7 Interview Guide Cheat Sheet

```
1. Clarify constraints (n size -> tells you which complexity is acceptable).
2. Brute force recursion first, out loud.
3. Identify state + transition + base case explicitly.
4. Memoize -> mention Big-O.
5. Convert to tabulation if asked, or for production code.
6. Discuss space optimization.
7. Dry run a small example.
8. Mention edge cases.
```

---

## 14. Practice Problem Bank

### 14.1 Basics / 1D DP

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Fibonacci Number | LeetCode | Easy | 1D DP |
| Climbing Stairs | LeetCode | Easy | 1D DP |
| Min Cost Climbing Stairs | LeetCode | Easy | 1D DP |
| House Robber | LeetCode | Medium | 1D DP |
| House Robber II | LeetCode | Medium | 1D DP + circular reduction |
| N-th Tribonacci Number | LeetCode | Easy | 1D DP |
| Maximum Subarray | LeetCode | Medium | 1D DP (Kadane's) |
| Delete and Earn | LeetCode | Medium | 1D DP (House Robber reduction) |

### 14.2 Knapsack Pattern

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| 0/1 Knapsack | GeeksforGeeks | Medium | 0/1 Knapsack |
| Partition Equal Subset Sum | LeetCode | Medium | Subset Sum |
| Target Sum | LeetCode | Medium | Subset Sum (signed) |
| Coin Change | LeetCode | Medium | Unbounded Knapsack |
| Coin Change II | LeetCode | Medium | Unbounded Knapsack (combinations) |
| Rod Cutting | GeeksforGeeks | Medium | Unbounded Knapsack |
| Ones and Zeroes | LeetCode | Medium | 2D Knapsack |
| Last Stone Weight II | LeetCode | Medium | Subset Sum reduction |

### 14.3 Sequence DP (LIS / LCS / Edit Distance family)

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Longest Increasing Subsequence | LeetCode | Medium | LIS |
| Number of Longest Increasing Subsequence | LeetCode | Medium | LIS + counting |
| Russian Doll Envelopes | LeetCode | Hard | LIS (2D sort + LIS) |
| Longest Common Subsequence | LeetCode | Medium | LCS |
| Edit Distance | LeetCode | Hard | Edit Distance |
| Delete Operation for Two Strings | LeetCode | Medium | LCS reduction |
| Shortest Common Supersequence | LeetCode | Hard | LCS reduction |
| Distinct Subsequences | LeetCode | Hard | Subsequence counting |
| Interleaving String | LeetCode | Medium | 2D sequence DP |
| Longest Palindromic Subsequence | LeetCode | Medium | LCS with reversed string |

### 14.4 Grid DP

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Unique Paths | LeetCode | Medium | Grid DP |
| Unique Paths II | LeetCode | Medium | Grid DP w/ obstacles |
| Minimum Path Sum | LeetCode | Medium | Grid DP |
| Triangle | LeetCode | Medium | Grid DP (bottom-up) |
| Dungeon Game | LeetCode | Hard | Grid DP (reverse direction) |
| Cherry Pickup | LeetCode | Hard | Grid DP + simultaneous agents |

### 14.5 Interval DP

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Matrix Chain Multiplication | GeeksforGeeks | Hard | Interval DP |
| Burst Balloons | LeetCode | Hard | Interval DP |
| Palindrome Partitioning II | LeetCode | Hard | Interval DP + palindrome table |
| Strange Printer | LeetCode | Hard | Interval DP |
| Minimum Cost to Merge Stones | LeetCode | Hard | Interval DP (grouped) |

### 14.6 Partition DP

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Partition Array for Maximum Sum | LeetCode | Medium | Partition DP |
| Stone Game | LeetCode | Medium | Partition/Game DP |
| Stone Game II | LeetCode | Medium | Game DP w/ move limit |
| Predict the Winner | LeetCode | Medium | Game DP (score difference) |

### 14.7 State Machine DP

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Best Time to Buy and Sell Stock | LeetCode | Easy | State Machine |
| Best Time to Buy and Sell Stock II | LeetCode | Medium | State Machine |
| Best Time to Buy and Sell Stock III | LeetCode | Hard | State Machine |
| Best Time to Buy and Sell Stock IV | LeetCode | Hard | State Machine |
| Best Time to Buy and Sell Stock with Cooldown | LeetCode | Medium | State Machine |
| Best Time to Buy and Sell Stock with Transaction Fee | LeetCode | Medium | State Machine |
| Decode Ways | LeetCode | Medium | State Machine |
| Paint House | LeetCode | Medium | State Machine |
| Paint House II | LeetCode | Hard | State Machine (k colors) |

### 14.8 Digit DP

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Numbers With Repeated Digits | LeetCode | Hard | Digit DP |
| Count of Numbers with Given Digit Sum | GeeksforGeeks | Hard | Digit DP |
| Non-negative Integers without Consecutive Ones | LeetCode | Hard | Digit DP (bitwise variant) |

### 14.9 Bitmask DP

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Traveling Salesman Problem | GeeksforGeeks | Hard | Bitmask DP |
| Partition to K Equal Sum Subsets | LeetCode | Medium | Bitmask DP |
| Shortest Path Visiting All Nodes | LeetCode | Hard | Bitmask DP (BFS + mask) |
| Minimum Cost to Connect Sticks / Assignment Problem | Codeforces | Hard | Bitmask DP |

### 14.10 Advanced / Competitive Programming

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Longest Path in Matrix | Code360 | Medium | Grid + memoized DFS DP |
| Word Break | LeetCode | Medium | 1D DP + Trie/Set lookup |
| Word Break II | LeetCode | Hard | DP + backtracking |
| Regular Expression Matching | LeetCode | Hard | 2D Sequence DP |
| Wildcard Matching | LeetCode | Hard | 2D Sequence DP |
| Frog Jump | Codeforces | Medium | 1D/2D DP |
| Divisor Game | LeetCode | Easy | Game DP |
| Knight Probability in Chessboard | LeetCode | Medium | Probability DP |
| Super Egg Drop | LeetCode | Hard | DP + binary search optimization |
| Count Different Palindromic Subsequences | LeetCode | Hard | Interval/Sequence DP |
| Codeforces DP Problem Set (various) | Codeforces | Varies | Mixed |
| CSES Dynamic Programming Section (full section) | CSES | Varies | Mixed (canonical DP training set) |
| AtCoder Educational DP Contest ("DP is Fun" A–Z) | AtCoder | Varies | Comprehensive DP pattern coverage |

> **Study Tip:** The **AtCoder Educational DP Contest** ("EDPC," problems A through Z) is widely regarded as the single best structured problem set for mastering every DP pattern from scratch, in increasing difficulty — an ideal companion to this handbook. The **CSES Dynamic Programming section** is a similarly excellent, tightly curated set for competitive-programming-style DP practice.

---

## 15. Final Revision

### 15.1 One-Page Mind Map

```
                              DYNAMIC PROGRAMMING
                                       |
        ---------------------------------------------------------------
        |                |                |                |          |
   OVERLAPPING      OPTIMAL         STATE DESIGN      TEMPLATES   OPTIMIZATIONS
   SUBPROBLEMS      SUBSTRUCTURE   (state, transition, (memo,      (space, CHT,
   (cache repeats)  (build big      base, answer)      tab, space   monotonic
                     from small)                        opt)        deque, D&C)
                                       |
        ---------------------------------------------------------------
        |          |          |          |          |          |     |
       1D       KNAPSACK   SEQUENCE     GRID     INTERVAL   PARTITION STATE
     (Fib,      (0/1, Un-  (LCS,LIS,   (Unique   (MCM,       (Stone   MACHINE
     Stairs,     bounded,   EditDist)   Paths,    Burst      Game)    (Stock,
     Robber)     Subset)                MinPath)  Balloons)           Decode)
                                       |
                            -----------------------
                            |                     |
                        BITMASK                DIGIT DP
                        (TSP, subset             (count by
                         partition)               digit prop)
```

### 15.2 Recognition Flowchart (Condensed)

```
"Optimal / count / feasible?" -> "Recursive relation exists?" -> "Subproblems repeat?"
      YES                              YES                            YES -> DP!
```

### 15.3 State Identification Guide (Condensed)

```
Changing quantities  -> dimensions of dp[]
Range of quantities  -> size of dp[] array
Smallest subproblem  -> base case
Relationship between -> transition equation
 big & small problems
Where the final      -> answer state (not always dp[n]!)
 answer sits
```

### 15.4 Transition Cheat Sheet (Condensed)

```
Fibonacci-style:     dp[i] = dp[i-1] + dp[i-2]
Knapsack (0/1):      dp[w] = max(dp[w], dp[w-wt]+val)   [backward loop]
Knapsack (unbounded):dp[w] = max(dp[w], dp[w-wt]+val)   [forward loop]
LCS:                 dp[i][j] = dp[i-1][j-1]+1 (match) else max(left, up)
Edit Distance:       dp[i][j] = dp[i-1][j-1] (match) else 1+min(3 options)
Interval DP:         dp[i][j] = best(dp[i][k] + dp[k+1][j] + cost)
Bitmask DP:          dp[mask|bit][j] = best(dp[mask][i] + cost(i,j))
```

### 15.5 Complexity Sheet (Condensed)

```
1D DP:        O(n)          Knapsack:     O(n*W)
LCS/EditDist: O(m*n)        LIS(fast):    O(n log n)
Interval DP:  O(n^3)        Bitmask DP:   O(2^n * n^2)
```

### 15.6 Interview Cheat Sheet (Condensed)

```
1. Brute force recursion, state it aloud.
2. Overlapping subproblems? -> memoize.
3. State + transition + base case, explicit.
4. Complexity of memoized solution.
5. Convert to tabulation.
6. Space-optimize if dependency is bounded.
7. Dry run + edge cases.
```



### 15.8 1-Hour Deep Revision Plan

```
0:00-0:10  Section 1 (Introduction) + Section 3 (Fundamentals) — theory refresh.
0:10-0:20  Section 2 (Python Templates) — rewrite each template from memory.
0:20-0:35  Section 5.1-5.3 — re-derive Fibonacci, House Robber, Knapsack, LCS, LIS from scratch.
0:35-0:45  Section 5.5-5.8 — re-derive one Interval DP, one State Machine DP, one Bitmask DP problem.
0:45-0:55  Section 8 (Recognition Guide) + Section 9 (Optimization Ladder) — practice classifying 5 random problems mentally.
0:55-1:00  Section 15 cheat sheets — final glance before an interview or exam.
```

---

## FAQs

**Q: Is Dynamic Programming the same as memoization?**
A: No. Memoization is one *implementation technique* for DP (top-down with caching). DP is the broader *algorithmic paradigm*; tabulation (bottom-up) is an equally valid DP implementation that doesn't use memoization at all.

**Q: Why does my top-down solution get a `RecursionError`?**
A: Python's default recursion limit (~1000) is exceeded by deep recursion. Convert to bottom-up tabulation for large inputs rather than relying on `sys.setrecursionlimit`, since raising the limit can still crash the actual C stack.

**Q: How do I know how many dimensions my `dp` table needs?**
A: Count the number of independent quantities that change as the problem shrinks (Section 8.5, Section 15.3). Each independent changing quantity is one dimension.

**Q: When should I use `lru_cache` vs writing my own dictionary cache?**
A: Use `lru_cache`/`cache` for quick, idiomatic solutions in interviews and prototypes. Write manual dictionary/array caches when you need explicit control (e.g., cache invalidation, non-hashable arguments converted to tuples, or converting to tabulation later).

**Q: Why does my 0/1 Knapsack give wrong (too-large) answers after space optimization?**
A: You likely iterated the capacity loop forward instead of backward, allowing the same item to be counted multiple times (Section 5.2.1 warning).

**Q: Is DP always faster than brute force?**
A: Only when overlapping subproblems actually exist. If all subproblems are distinct (no overlap), DP's memoization provides no benefit and adds needless overhead — Divide & Conquer without memoization is more appropriate there.

**Q: What's the difference between "subsequence" and "substring/subarray" in DP problems?**
A: A subsequence preserves relative order but need not be contiguous; a substring/subarray must be contiguous. This distinction changes the transition (e.g., LCS vs Longest Common Substring, Section 5.3.3 vs 5.3.4) — always clarify with the interviewer which is meant.

**Q: How do I practice DP effectively?**
A: Follow the Optimization Ladder (Section 9) for every problem: brute force → memoize → tabulate → space-optimize. Use the AtCoder Educational DP Contest (Section 14.10) for structured, pattern-by-pattern practice, and revisit the Problem Recognition Guide (Section 8) before attempting new problems cold.

---
