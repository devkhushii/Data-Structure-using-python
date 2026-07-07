# 🧠 THE COMPLETE BACKTRACKING HANDBOOK 


## 📚 Table of Contents

1. [Introduction to Backtracking](#1-introduction-to-backtracking)
2. [Backtracking in Python](#2-backtracking-in-python)
3. [Core Concepts](#3-core-concepts)
4. [Backtracking Patterns](#4-backtracking-patterns)
5. [Classical Problems](#5-classical-problems)
   - [5.1 Subsets](#51-subsets)
   - [5.2 Subsequences](#52-subsequences)
   - [5.3 Combinations](#53-combinations)
   - [5.4 Combination Sum](#54-combination-sum)
   - [5.5 Permutations](#55-permutations)
   - [5.6 Unique Permutations](#56-unique-permutations)
   - [5.7 Letter Combinations of a Phone Number](#57-letter-combinations-of-a-phone-number)
   - [5.8 Generate Parentheses](#58-generate-parentheses)
   - [5.9 N-Queens](#59-n-queens)
   - [5.10 Sudoku Solver](#510-sudoku-solver)
   - [5.11 Rat in a Maze](#511-rat-in-a-maze)
   - [5.12 Word Search](#512-word-search)
   - [5.13 Palindrome Partitioning](#513-palindrome-partitioning)
   - [5.14 Restore IP Addresses](#514-restore-ip-addresses)
   - [5.15 Expression Add Operators](#515-expression-add-operators)
   - [5.16 Partition into K Equal Sum Subsets](#516-partition-into-k-equal-sum-subsets)
   - [5.17 Crossword Puzzle (Overview)](#517-crossword-puzzle-overview)
6. [Pruning Techniques](#6-pruning-techniques)
7. [Applications of Backtracking](#7-applications-of-backtracking)
8. [Problem Recognition Guide](#8-problem-recognition-guide)
9. [Optimization Strategies](#9-optimization-strategies)
10. [Interview Preparation](#10-interview-preparation)
11. [Python-Specific Tips](#11-python-specific-tips)
12. [Common Mistakes](#12-common-mistakes)
13. [Cheat Sheets](#13-cheat-sheets)
14. [Practice Problem Bank](#14-practice-problem-bank)
15. [Final Revision Kit](#15-final-revision-kit)
16. [FAQs](#16-faqs)

---

# 1. Introduction to Backtracking

## 1.1 What Is Backtracking?

**Backtracking** is a general algorithmic technique for solving problems incrementally by trying out partial solutions and then abandoning ("backtracking on") a partial solution as soon as it is determined that it cannot possibly lead to a valid complete solution.

Formally: Backtracking is a **depth-first, systematic search** over a **state space** of candidate solutions, where at every step we make a **choice**, recursively explore the consequences of that choice, and then **undo** the choice to try the next one.

> **Definition (Formal):** Given a state space `S`, a set of choices `C(s)` available at each state `s`, and a constraint function `valid(s)`, backtracking explores `S` via DFS, pruning any branch where `valid(s) == False`, and recording `s` whenever `s` is a goal state.

## 1.2 Why Does Backtracking Exist?

Many problems cannot be solved by a greedy choice or a simple formula because:

- The problem requires exploring **all possible configurations** (or all valid ones).
- Decisions made early can invalidate later possibilities, so we need the ability to **undo**.
- Brute force generates and checks everything **without reuse of partial work**, while pure recursion without pruning wastes time exploring dead branches.

Backtracking exists to give us **brute force with intelligence** — it still explores the full theoretical search space in the worst case, but it **prunes** invalid branches early, often turning an exponential-but-hopeless search into something tractable in practice.

## 1.3 Recursive Search, Trial and Error, Decision Making

Backtracking is best understood as three ideas fused together:

| Idea | Meaning |
|---|---|
| **Recursive Search** | Each recursive call represents "explore this partial solution further." |
| **Trial and Error** | We *try* a choice, and if it fails downstream, we *error out* and try another. |
| **Decision Making** | At every node of the recursion tree, we are making a decision: include/exclude, pick this/pick that. |

## 1.4 State Space Search

Every backtracking problem can be modeled as a **State Space Tree**:

- **Root** = empty/initial state.
- **Each edge** = one choice/decision.
- **Each node** = a partial solution (state).
- **Leaf / terminal node** = either a complete valid solution, or a dead end.

```
                      ROOT (empty state)
                     /      |       \
               choice1   choice2   choice3
                 /           |          \
              state1       state2      state3
              /   \         /  \        /   \
           ...    ...     ...  ...   ...    ...
```

## 1.5 Characteristics of Backtracking

- **Incremental construction** of solutions (one choice at a time).
- **Depth-First** traversal of the state space.
- **Constraint checking** at every node (pruning).
- **Undo mechanism** — the defining feature that separates backtracking from plain recursive brute force.
- Naturally expressed with recursion + a shared mutable "path"/"state" structure.

## 1.6 Advantages

- Conceptually simple: "choose → explore → un-choose."
- Guarantees correctness — explores all valid possibilities (or finds *a* solution) if given enough time.
- Naturally supports pruning, which can turn exponential problems into fast, practical solutions.
- Memory-efficient compared to storing the entire search space (only the current path is kept, unlike BFS-based enumeration).

## 1.7 Disadvantages

- Worst-case time complexity is often exponential or factorial: `O(2^n)`, `O(n!)`, `O(k^n)`.
- Recursive depth can hit Python's recursion limit for large `n`.
- Naïve implementations (excessive copying, poor pruning) can be extremely slow.
- Not suitable when a polynomial-time DP or greedy solution exists and applies.

## 1.8 Applications (Preview)

| Domain | Example |
|---|---|
| Combinatorics | Subsets, permutations, combinations |
| Puzzles | N-Queens, Sudoku, crosswords |
| Pathfinding | Rat in a Maze, word search |
| AI / CSP | Constraint Satisfaction Problems, scheduling |
| Compilers | Parsing ambiguous grammars |
| Games | Tic-tac-toe, chess move exploration |
| Bioinformatics | Sequence alignment, motif search |

## 1.9 Real-World Analogy

> **Analogy — Solving a Maze with a Piece of Chalk:**
> Imagine walking through a maze, marking your path on the floor with chalk. At every junction, you pick a direction. If you hit a dead end, you erase your chalk marks back to the last junction (backtrack) and try the next unexplored direction. You never revisit a path you know is wrong twice, and you always know exactly how to "undo" your last move.

> **Analogy — Trying Outfits:**
> You're getting dressed and trying to match a shirt, pants, and shoes. You try a shirt, then a pair of pants — but if the shoes clash irreparably, you don't restart from scratch; you just swap the shoes (undo just that one choice) and try again.

## 1.10 Backtracking vs. Related Techniques

| Technique | Explores full space? | Undoes choices? | Typical Complexity | Use Case |
|---|---|---|---|---|
| Brute Force | Yes (often generates then checks) | No (regenerates) | Exponential | Small `n`, no pruning insight |
| Backtracking | Yes, but prunes | Yes | Exponential (pruned) | Combinatorial search with constraints |
| Greedy | No (one path only) | No | Polynomial | Locally optimal choice is globally optimal |
| Dynamic Programming | No (reuses subproblems) | N/A (memoized) | Polynomial/Pseudo-poly | Overlapping subproblems + optimal substructure |
| BFS/DFS (graphs) | Yes (all reachable nodes) | No (visited marking) | O(V+E) | Reachability/shortest path, not full enumeration of combinatorial choices |

> 💡 **Tip:** Backtracking is DFS *with pruning and undo* over a **decision tree**, not over a graph of vertices/edges. This is the key mental model shift.

---
# 2. Backtracking in Python

## 2.1 The Universal Template

Almost every backtracking solution in Python follows this skeleton:

```python
def backtrack(path, choices, result):
    # 1. Base case / Goal check
    if is_goal(path):
        result.append(path[:])   # store a COPY, not a reference
        return

    # 2. Try every available choice
    for choice in get_choices(choices, path):
        if not is_valid(choice, path):   # constraint check / pruning
            continue

        # 3. CHOOSE
        path.append(choice)

        # 4. EXPLORE
        backtrack(path, choices, result)

        # 5. UN-CHOOSE (undo / backtrack)
        path.pop()
```

This **Choose → Explore → Unchoose** cycle is the heart of every problem in this handbook.

## 2.2 State Management

"State" is whatever information is needed to know (a) what has been decided so far, and (b) what remains possible. In Python this is typically:

- A **list** (`path`) representing the partial solution being built.
- A **boolean/visited array** or **set** tracking used elements.
- Extra scalars (e.g., `remaining_sum`, `open_brackets`) representing derived state that would otherwise be recomputed.

## 2.3 Mutable vs. Immutable State — Why It Matters

Python beginners frequently make **the single most common backtracking bug**: appending a *reference* to a mutable list instead of a *copy*.

```python
result = []
path = []

def backtrack():
    if len(path) == 3:
        result.append(path)      # ❌ BUG: stores a reference!
        return
    for i in range(3):
        path.append(i)
        backtrack()
        path.pop()
```

Because `path` is mutated in place, every entry in `result` ends up pointing to the *same* list object — by the time backtracking finishes, all entries reflect the final (usually empty) state.

**Fix:**

```python
result.append(path[:])       # shallow copy via slicing
# or
result.append(list(path))    # equivalent
# or
result.append(path.copy())   # equivalent
```

> ⚠️ **Warning:** `path[:]`, `list(path)`, and `.copy()` all perform a **shallow** copy. If `path` contains nested mutable objects (e.g., list of lists), you need `copy.deepcopy(path)` instead.

## 2.4 Path Management Strategies

| Strategy | When to Use | Trade-off |
|---|---|---|
| Append/Pop on a shared list | Most problems (subsets, permutations, combinations) | O(1) undo, but must remember to copy on save |
| String concatenation (`path + char`) | Small strings (parentheses, IP addresses) | Strings are immutable → no explicit undo needed, but O(n) per concatenation |
| Index-based recursion (no explicit removal) | Array-based problems (subset sum with include/exclude) | Avoids append/pop entirely; state passed via parameters |
| Swap-based (in-place permutations) | Space-optimized permutations | Avoids extra path list, but trickier to reason about |

## 2.5 Visited Arrays, Boolean Arrays, and Sets

To avoid reusing an element (in permutations, N-Queens, Sudoku, etc.) we need fast **"is this used?"** checks:

```python
# Boolean array — O(1) lookup, O(n) space, fastest for fixed-size index-based domains
visited = [False] * n

# Set — O(1) average lookup, flexible for arbitrary hashable values
used = set()

# Dictionary — O(1) lookup + extra metadata (e.g., count of remaining uses)
counter = {"A": 2, "B": 1}
```

| Structure | Best For | Lookup | Insert/Remove |
|---|---|---|---|
| `list` of `bool` | Fixed-size index domains (array positions) | O(1) | O(1) |
| `set()` | Arbitrary hashable values, diagonals in N-Queens | O(1) avg | O(1) avg |
| `dict` / `Counter` | Values with multiplicities (duplicate handling) | O(1) avg | O(1) avg |

## 2.6 Memory Behavior in Python Recursion

- Every recursive call pushes a new **stack frame** holding local variables — this is real memory, bounded by Python's default recursion limit (~1000, configurable via `sys.setrecursionlimit`).
- Lists passed by reference are **not copied** on each call (Python passes references), which is *why* append/pop mutation works efficiently — but also why forgetting to copy before saving is such an easy bug.
- Default arguments (e.g., `def f(path=[])`) are evaluated **once** at function definition time — never use mutable default arguments for backtracking state.

```python
# ❌ DANGEROUS — path is shared across ALL calls to solve(), forever
def solve(path=[]):
    ...

# ✅ SAFE
def solve(path=None):
    if path is None:
        path = []
    ...
```

## 2.7 Best Practices Checklist

- ✅ Always copy (`path[:]`) before saving to results.
- ✅ Always undo (`pop()`, unset visited, restore board cell) after the recursive call returns.
- ✅ Prune *before* recursing, not after — check `is_valid` before appending to path.
- ✅ Sort input first when duplicate handling or bounding is needed.
- ✅ Use early-return base cases to reduce nesting.
- ✅ Prefer `set`/`Counter` over repeated `in path` checks (`O(n)` → `O(1)`).
- ✅ Avoid deep copying full boards/grids each call — mutate in place, then undo.

---
# 3. Core Concepts

Every backtracking algorithm is built from the same vocabulary. Master these terms and every problem in this handbook becomes a variation on a theme.

## 3.1 Glossary Table

| Term | Meaning | Example (N-Queens) |
|---|---|---|
| **State** | The partial solution built so far | Queen placements in rows 0..r-1 |
| **Choice** | An option available at the current state | Column `c` for the next queen |
| **Constraint** | A rule a choice must satisfy | No shared column/diagonal |
| **Goal** | The condition defining a complete, valid solution | All `n` queens placed safely |
| **Decision Tree** | The tree of all choice sequences | Every column choice per row |
| **State Space Tree** | Decision tree annotated with actual states | Board configurations at each node |
| **Branch** | An edge from a state to a child state | Placing a queen in a specific column |
| **Leaf** | A node with no further choices (goal or dead end) | Row `n` reached (goal) or no valid column (dead end) |
| **Dead End** | A state where no choice satisfies constraints | Every column attacked |
| **Feasible / Candidate Solution** | A partial state that hasn't violated constraints yet | Queens placed validly so far, but not all `n` rows filled |
| **Complete Solution** | A feasible state that also satisfies the goal | All `n` queens placed, no conflicts |
| **Pruning** | Skipping branches that cannot lead to a solution | Skipping attacked columns |
| **Undo Operation** | Reverting a choice to restore prior state | Removing the placed queen before trying the next column |

## 3.2 State Space Tree — Deep Dive

Consider generating all subsets of `{1, 2}` using an include/exclude pattern:

```
                         {}                      <- state at index 0
                 /               \
         include 1              exclude 1
             /                        \
           {1}                        {}          <- state at index 1
          /    \                    /    \
   include 2  exclude 2      include 2  exclude 2
       /            \             /          \
    {1,2}          {1}          {2}          {}    <- leaves (index 2 = done)
```

- **4 leaves** = `2^2` subsets, matching the branching factor of 2 (include/exclude) at depth 2.
- Every root-to-leaf path is one complete candidate solution.

## 3.3 Call Stack Representation

Backtracking's recursion tree **is** the Python call stack. Tracing `backtrack([], [1,2])`:

```
call backtrack(path=[])                         # depth 0
│
├── path.append(1) → backtrack(path=[1])        # depth 1
│   │
│   ├── path.append(2) → backtrack(path=[1,2])  # depth 2 → GOAL, save [1,2]
│   │   └── path.pop() → path=[1]
│   │
│   └── (no more choices at depth 1 besides 2)
│   path.pop() → path=[]
│
├── path.append(2) → backtrack(path=[2])        # depth 1
│   │
│   └── (no more choices, since 1 < 2 was already used)
│   path.pop() → path=[]
│
└── done
```

Each **indentation level = one stack frame**. The `pop()` calls correspond exactly to stack frames returning — this is why append/pop must be perfectly paired.

## 3.4 Branch, Leaf, Dead End — Visualized

```
                (root)
              /   |    \
          A      B      C          <- branches
         /|\    /|\    /|\
        ......................
       /                     \
   [valid leaf]          [DEAD END]
   (goal reached)     (constraint violated,
                        pruned before
                        recursing further)
```

> 📝 **Note:** A "dead end" in backtracking is detected **before** wasting time recursing deeper — that's the entire point of the constraint check (`is_valid`). Detecting it *after* fully exploring is just brute force with extra steps.

## 3.5 Feasible vs. Candidate vs. Complete Solutions

| Concept | Definition | Backtracking Action |
|---|---|---|
| Feasible/Partial | Satisfies constraints so far, but incomplete | Continue recursing |
| Infeasible | Violates a constraint | Prune (don't recurse) |
| Complete & Valid | Feasible AND meets the goal condition | Record as a solution, then backtrack anyway to find others |
| Complete & Invalid | Reached full length but broke a constraint | Should have been pruned earlier — if not, filter here (worse performance) |

---
# 4. Backtracking Patterns

Almost all backtracking interview problems reduce to a small number of reusable **patterns**. Recognizing which pattern applies is 80% of solving the problem.

## 4.1 Pattern Overview Table

| Pattern | Core Idea | Canonical Problems |
|---|---|---|
| Pick / Not-Pick (Include/Exclude) | At each element, branch into "take it" and "skip it" | Subsets, Subset Sum |
| Choose → Explore → Unchoose | Generic template; try each choice from a pool, recurse, undo | Almost everything |
| Generate All | Explore entire state space, collect every valid leaf | Subsets, Permutations |
| Find One (Existence) | Stop at first valid solution — return `True`/path immediately | Sudoku, Word Search (single path), N-Queens (find one) |
| Constraint Satisfaction (CSP) | Variables + domains + constraints, assign one variable at a time | Sudoku, N-Queens, Map Coloring |
| DFS Backtracking on Grid | Explore neighboring cells, mark visited, undo after | Word Search, Rat in a Maze |
| Path Building | Build a path/sequence incrementally, validate as you go | Word Search, Maze |
| Subset Generation | Choose any subset of a fixed pool (order doesn't matter, no reuse) | Subsets |
| Permutation Generation | Choose an ordering of all elements (order matters, no reuse) | Permutations |
| Combination Generation | Choose `k` of `n` elements, order doesn't matter | Combinations |
| Partition Pattern | Split a sequence into valid contiguous parts | Palindrome Partitioning, Restore IP Addresses |
| Grid Backtracking | 2D state space, choices = 4-directional moves | Rat in a Maze, Word Search |
| String Backtracking | Choices = characters/positions within a string | Letter Combinations, Expression Add Operators |

## 4.2 Pick / Not-Pick Pattern

```python
def subsets_pick_notpick(nums):
    result = []
    path = []

    def solve(i):
        if i == len(nums):
            result.append(path[:])
            return
        # Pick nums[i]
        path.append(nums[i])
        solve(i + 1)
        path.pop()               # undo
        # Not pick nums[i]
        solve(i + 1)

    solve(0)
    return result
```

**Decision Tree for `[1, 2]`:**

```
                         solve(0)
                    /               \
                 PICK 1            SKIP 1
                  /                    \
             solve(1)                solve(1)
             /      \                /      \
          PICK 2   SKIP 2        PICK 2    SKIP 2
            |         |             |         |
        solve(2)  solve(2)      solve(2)  solve(2)
         [1,2]      [1]           [2]        []
```

## 4.3 Choose → Explore → Unchoose (Generic Template)

This is the master pattern all others specialize:

```python
def generic_backtrack(state, choices):
    if goal_reached(state):
        record(state)
        return
    for choice in choices(state):
        if not valid(choice, state):
            continue
        apply(choice, state)      # CHOOSE
        generic_backtrack(state, choices)   # EXPLORE
        undo(choice, state)       # UNCHOOSE
```

## 4.4 Generate-All vs. Find-One

| Aspect | Generate All | Find One |
|---|---|---|
| Return type | `List[Solution]` | `bool` or single `Solution`/`None` |
| Recursion continues after a hit? | Yes (keep searching siblings) | No (`return True` propagates up immediately) |
| Typical problems | Subsets, Permutations, Combination Sum | Sudoku Solver, N-Queens "does a solution exist", Word Search |

```python
# Find-One skeleton — note the early-exit propagation
def solve(state):
    if goal(state):
        return True
    for choice in choices(state):
        if valid(choice, state):
            apply(choice, state)
            if solve(state):        # if a deeper call found a solution...
                return True          # ...propagate success immediately, skip undo of the final board if you want to keep it!
            undo(choice, state)
    return False
```

> 💡 **Interview Tip:** In "Find One" problems (Sudoku, N-Queens count-only), returning `True` immediately without exploring siblings is the single biggest performance difference vs. "Generate All" — always clarify with the interviewer whether they want *one* solution, *all* solutions, or a *count*.

## 4.5 Grid / String / Partition Patterns at a Glance

```
GRID BACKTRACKING                 STRING BACKTRACKING              PARTITION PATTERN
(4-directional DFS)               (character-by-character)         (split into valid chunks)

  (r,c)                              "cat"                          "aab"
   │  choices: up/down/left/right     │ choices: append char          │ choices: cut point
   ▼                                  ▼                               ▼
 mark visited                     path += char                    substring [0:i]
   │                                  │                               │
 recurse to neighbor              recurse(index+1)                 recurse(i, end)
   │                                  │                               │
 unmark visited                  path = path[:-1]                 (strings immutable,
 (backtrack)                     (or pop if using list)             no explicit undo needed)
```

---
# 5. Classical Backtracking Problems

## 5.1 Subsets

**Problem:** Given an array of unique integers `nums`, return all possible subsets (the power set).

**Approach:** At index `start`, the current `path` is *always* a valid subset — record it immediately, then try extending it with every element from `start` onward (never looking backward, which avoids duplicates/reorderings).

```python
def subsets(nums):
    result = []
    path = []

    def backtrack(start):
        result.append(path[:])              # every state is a valid subset
        for i in range(start, len(nums)):
            path.append(nums[i])            # CHOOSE
            backtrack(i + 1)                # EXPLORE (never reuse earlier indices)
            path.pop()                      # UNCHOOSE

    backtrack(0)
    return result

print(subsets([1, 2, 3]))
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

**Line-by-Line Explanation:**
1. `result`, `path` — accumulator and current partial subset.
2. `backtrack(start)` — `start` prevents picking earlier elements again (order doesn't matter for subsets).
3. `result.append(path[:])` — **every** call represents a valid subset, so we save immediately (no "goal check" needed beyond reaching the end of choices).
4. The `for` loop tries each remaining candidate; `path.append`/`backtrack`/`path.pop()` is the choose-explore-unchoose triad.

**State Space Tree** (for `[1,2,3]`):

```
                              backtrack(0), path=[]  -> save []
              /                      |                       \
      choose 1                  choose 2                  choose 3
    backtrack(1)                backtrack(2)               backtrack(3)
    path=[1] -> save            path=[2] -> save            path=[3] -> save
    /        \                     |
choose2      choose3            choose3
backtrack(2) backtrack(3)       backtrack(3)
path=[1,2]   path=[1,3]         path=[2,3]
  -> save      -> save            -> save
   |
choose3
backtrack(3)
path=[1,2,3]
  -> save
```

**Dry Run:**

| Step | Current State (`path`) | Choice | Action | Backtrack | Explanation |
|---|---|---|---|---|---|
| 1 | `[]` | – | save `[]` | – | Empty subset always valid |
| 2 | `[]` | 1 | append 1 → `[1]` | – | Choose index 0 |
| 3 | `[1]` | – | save `[1]` | – | |
| 4 | `[1]` | 2 | append 2 → `[1,2]` | – | Choose index 1 |
| 5 | `[1,2]` | – | save `[1,2]` | – | |
| 6 | `[1,2]` | 3 | append 3 → `[1,2,3]` | – | Choose index 2 |
| 7 | `[1,2,3]` | – | save `[1,2,3]` | – | End of array reached |
| 8 | `[1,2,3]` | – | – | pop → `[1,2]` | No more choices at index 3 |
| 9 | `[1,2]` | – | – | pop → `[1]` | No more choices after 2 |
| 10 | `[1]` | 3 | append 3 → `[1,3]` | – | Try next candidate (index 2) |
| ... | ... | ... | ... | ... | (pattern continues for all branches) |

**Complexity:** Time `O(n · 2^n)` (2^n subsets, O(n) to copy each), Space `O(n)` recursion depth + `O(n·2^n)` output.

**Branching Factor:** At depth `d`, there are `n - d` choices (decreasing), but total leaves/nodes = `2^n` since each element is independently in/out.

**Edge Cases:** empty array → `[[]]`; single element → `[[], [x]]`.

**Common Mistakes:** forgetting `path[:]` (reference bug, see §2.3); using `start` incorrectly (using `i` instead of `i+1` causes reuse of the same element).

**Interview Tip:** This is the cleanest introduction to backtracking recursion trees — master it before permutations/combinations.

**Variations:** Subsets with duplicates (sort + skip `nums[i]==nums[i-1]` at same recursion depth), subset sum (add a running-sum parameter and constraint check).

---

## 5.2 Subsequences

A **subsequence** preserves relative order but need not be contiguous — for arrays, "subset" and "subsequence" backtracking code are identical (§5.1). The distinction matters mainly for **strings**, where a subsequence is any character selection preserving order (not to be confused with a *substring*, which must be contiguous).

```python
def subsequences(s):
    result = []
    path = []

    def backtrack(i):
        if i == len(s):
            if path:                       # skip empty subsequence if not wanted
                result.append("".join(path))
            return
        # include s[i]
        path.append(s[i])
        backtrack(i + 1)
        path.pop()
        # exclude s[i]
        backtrack(i + 1)

    backtrack(0)
    return result

print(subsequences("ab"))   # ['ab', 'a', 'b']
```

This uses the **Pick/Not-Pick** pattern (§4.2) rather than the "start index" pattern — both are valid; pick/not-pick makes the include/exclude decision explicit at *every* index rather than skipping directly to the next unvisited index.

**Complexity:** `O(n · 2^n)` — `2^n` subsequences of a length-`n` string.

**Interview Tip:** If asked for subsequences *of a specific target sum/pattern* (e.g., "does a subsequence equal X"), this is often better solved by DP; backtracking is for **enumeration**, not just existence checks on large `n`.

---

## 5.3 Combinations

**Problem:** Given `n` and `k`, return all possible combinations of `k` numbers chosen from `1..n`.

```python
def combine(n, k):
    result = []
    path = []

    def backtrack(start):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            # PRUNE: if remaining numbers (n - i + 1) can't fill the needed slots, stop
            if (k - len(path)) > (n - i + 1):
                continue
            path.append(i)
            backtrack(i + 1)
            path.pop()

    backtrack(1)
    return result

print(combine(4, 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

**State Space Tree (`n=4, k=2`):**

```
                         backtrack(1), path=[]
        /            |             |           \
     take1         take2         take3        take4  (pruned: not enough left for k=2)
   path=[1]       path=[2]      path=[3]
   /   |   \       /   \          |
  2    3    4     3     4         4
[1,2][1,3][1,4] [2,3] [2,4]     [3,4]
```

**Dry Run:**

| Step | State | Choice | Action | Backtrack | Explanation |
|---|---|---|---|---|---|
| 1 | `[]` | 1 | append → `[1]` | – | |
| 2 | `[1]` | 2 | append → `[1,2]` | – | len==k, save |
| 3 | `[1,2]` | – | – | pop → `[1]` | |
| 4 | `[1]` | 3 | append → `[1,3]` | – | save |
| 5 | `[1,3]` | – | – | pop → `[1]` | |
| 6 | `[1]` | 4 | append → `[1,4]` | – | save |
| 7 | `[1,4]` | – | – | pop → `[]` | |
| 8 | `[]` | 2 | append → `[2]` | – | |
| ... | ... | ... | ... | ... | continues symmetrically |

**Complexity:** Time `O(k · C(n,k))`, Space `O(k)` recursion depth.

**Pruning Insight:** The check `(k - len(path)) > (n - i + 1)` is a **bounding** technique — it skips branches where even taking *every remaining* number wouldn't reach length `k`. Without it, the algorithm still works but explores useless branches.

**Common Mistakes:** Off-by-one in the pruning bound; using `i` instead of `i + 1` in the recursive call (causes repeated elements within one combination).

**Variations:** Combination Sum (allow reuse — recurse with `i` not `i+1`, §5.4); Combination Sum II (no reuse + duplicate skipping).

---

## 5.4 Combination Sum

**Problem:** Given `candidates` (distinct positive integers) and a `target`, find all unique combinations where the chosen numbers sum to `target`. **The same number may be reused unlimited times.**

```python
def combinationSum(candidates, target):
    result = []
    path = []
    candidates.sort()                       # enables early break-pruning

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:   # sorted -> everything after is bigger too
                break
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])   # note: i, NOT i+1 -> allows reuse
            path.pop()

    backtrack(0, target)
    return result

print(combinationSum([2, 3, 6, 7], 7))
# [[2, 2, 3], [7]]
```

**Why sort first?** Sorting lets us `break` (not just `continue`) the moment `candidates[i] > remaining`, since every subsequent candidate is also too large — a direct **bounding** optimization.

**State Space Tree (partial, `[2,3,6,7]`, target 7):**

```
                    backtrack(0, 7)
        /              |            |         \
     take2          take3        take6       take7
  backtrack(0,5)  backtrack(1,4) backtrack(2,1) backtrack(3,0)
   /      \           |             (7-6=1, no                -> remaining==0
 take2   take3      take3           candidate <=1)              -> SAVE [7]
backtrack backtrack backtrack(1,1)
 (0,3)     (1,2)    (7-3-3-... )
  ...       ...        BREAK (nothing <=1 after 3)
   |
 take2 -> backtrack(0,1) -> BREAK (2>1)
 take3 -> backtrack(1,0) -> remaining==0 -> SAVE [2,2,3]
```

**Complexity:** Time is problem/input-dependent, roughly `O(2^target)` worst case (exponential in target/depth), bounded by pruning. Space `O(target/min(candidates))` recursion depth.

**Edge Cases:** No valid combination → `[]`; `target` smaller than every candidate → `[]` immediately.

**Common Mistakes:** Passing `i + 1` instead of `i` (accidentally disallows reuse — that's actually Combination Sum II's rule); forgetting to sort (loses the `break` optimization, must use `continue` instead, which is correct but slower).

**Variations:**
- **Combination Sum II:** no reuse, candidates *may* contain duplicates → sort + skip `i > start and candidates[i]==candidates[i-1]`.
- **Combination Sum III:** exactly `k` numbers from `1..9`, no reuse.

---

## 5.5 Permutations

**Problem:** Given a list of distinct integers, return all possible permutations (orderings).

```python
def permute(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result

print(permute([1, 2, 3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Key Difference from Subsets/Combinations:** Permutations loop over **all** indices every call (not `range(start, n)`), because order matters and every element must eventually appear in every position — so we need a `used[]` array to avoid picking the same index twice within one path.

**State Space Tree (`[1,2,3]`, partial):**

```
                       backtrack(), path=[]
        /                    |                     \
     use idx0             use idx1               use idx2
   path=[1]              path=[2]                path=[3]
   /       \              /      \                /      \
 idx1      idx2         idx0    idx2            idx0     idx1
path=[1,2] path=[1,3]  path=[2,1] path=[2,3]  path=[3,1] path=[3,2]
   |          |            |         |            |         |
 idx2       idx1         idx2      idx0          idx1      idx0
[1,2,3]    [1,3,2]      [2,1,3]   [2,3,1]       [3,1,2]   [3,2,1]
```

**Call Stack Trace (first branch only):**

```
backtrack()                          path=[]
 used=[F,F,F]
 → choose idx0 (val 1), used=[T,F,F]
   backtrack()                       path=[1]
    → choose idx1 (val 2), used=[T,T,F]
      backtrack()                    path=[1,2]
       → choose idx2 (val 3), used=[T,T,T]
         backtrack()                 path=[1,2,3] → SAVE
         undo idx2 → used=[T,T,F], path=[1,2]
      undo idx1 → used=[T,F,F], path=[1]
    → choose idx2 (val 3), used=[T,F,T]
      ...
```

**Complexity:** Time `O(n · n!)` (n! permutations, O(n) to build/copy each), Space `O(n)` for `used` + recursion depth.

**Branching Factor:** `n` at depth 0, `n-1` at depth 1, ..., `1` at depth `n-1` → total leaves = `n!`.

**Common Mistakes:** Forgetting `used[i] = False` on undo (permanently blocks that index); using a `set` of *values* instead of *indices* when duplicates are present (breaks with repeated values — see §5.6).

**Alternative Approach — Swap-Based (in-place, no `used` array):**

```python
def permute_swap(nums):
    result = []
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]   # swap into position
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]   # swap back (undo)
    backtrack(0)
    return result
```
This avoids the extra `used` array and `path` list at the cost of being harder to read and **not stable** for tracking "used" semantics when duplicates exist.

**When to use which:** `used[]` + `path` version — clearer, easier to extend with pruning/duplicate-skipping. Swap version — marginally less memory, common in competitive programming for raw speed.

---

## 5.6 Unique Permutations

**Problem:** Given a list that **may contain duplicates**, return all *unique* permutations.

```python
def permuteUnique(nums):
    result = []
    path = []
    nums.sort()                       # duplicates become adjacent
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            # Skip duplicate values UNLESS the previous identical value
            # is still "active" in the current path (used[i-1] == True
            # would mean we're extending the same branch, which is fine;
            # used[i-1] == False means the previous identical value was
            # already fully processed and backtracked — using it again
            # here would just regenerate the same permutation).
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result

print(permuteUnique([1, 1, 2]))
# [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

**Why Sorting + `not used[i-1]` Works:**

```
sorted nums = [1, 1, 2]   (indices: 0, 1, 2)

At the top level, trying index 0 (value 1) is allowed (used[-1] doesn't apply).
After fully exploring index 0's subtree and backtracking (used[0]=False again),
trying index 1 (value 1) at the SAME level is now checked:
   nums[1] == nums[0]  AND  used[0] == False  → SKIP
   (this would produce an identical permutation set to index 0's branch)

But if index 0 IS currently used (used[0] == True) and we're deeper in that
same branch trying index 1, nums[1]==nums[0] and used[0]==True → NOT skipped,
because we're using the "second 1" as a genuinely different element in the
same active path, which is required and safe.
```

**Complexity:** Time `O(n · n!)` worst case (fewer than `n!` when duplicates exist, still exponential), Space `O(n)`.

**Common Mistakes:** Forgetting to sort first (duplicate-adjacency check fails without sorting); using `used[i-1]` condition backwards (using `used[i-1] == True` to skip instead of `False` — produces wrong/missing results).

**Interview Tip:** The "sort + skip if previous duplicate not used" trick generalizes to **every** duplicate-handling backtracking problem (Subsets II, Combination Sum II, Permutations II) — memorize this one pattern.

---

## 5.7 Letter Combinations of a Phone Number

**Problem:** Given a string of digits `2-9`, return all letter combinations the number could represent (as on a phone keypad).

```python
def letterCombinations(digits):
    if not digits:
        return []

    mapping = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    result = []
    path = []

    def backtrack(i):
        if i == len(digits):
            result.append("".join(path))
            return
        for ch in mapping[digits[i]]:
            path.append(ch)
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result

print(letterCombinations("23"))
# ['ad','ae','af','bd','be','bf','cd','ce','cf']
```

**Decision Tree (`"23"`):**

```
                        backtrack(0)
            /        |        \
          'a'       'b'       'c'          <- letters for digit '2'
         /  |  \   /  |  \   /  |  \
       'd' 'e' 'f' 'd' 'e' 'f' 'd' 'e' 'f'  <- letters for digit '3'
       ad   ae  af  bd  be  bf  cd  ce  cf
```

**Complexity:** Time `O(4^n · n)` where `n = len(digits)` (max 4 letters per digit, e.g. "7"/"9"), Space `O(n)` recursion depth.

**Edge Cases:** Empty input → `[]` (not `[""]`); digit `"1"` or `"0"` typically not mapped (validate input assumptions with interviewer).

**Common Mistakes:** Off-by-one in base case (`i == len(digits)` not `i == len(digits) - 1`); returning `[""]` for empty input instead of `[]` (check problem statement).

---

## 5.8 Generate Parentheses

**Problem:** Given `n` pairs of parentheses, generate all combinations of well-formed parentheses.

```python
def generateParenthesis(n):
    result = []
    path = []

    def backtrack(open_count, close_count):
        if len(path) == 2 * n:
            result.append("".join(path))
            return
        if open_count < n:                      # can always add '(' if we haven't used all n
            path.append("(")
            backtrack(open_count + 1, close_count)
            path.pop()
        if close_count < open_count:             # only add ')' if it won't create an invalid prefix
            path.append(")")
            backtrack(open_count, close_count + 1)
            path.pop()

    backtrack(0, 0)
    return result

print(generateParenthesis(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
```

**Constraint Checking Visualized:**

```
State: open_count=1, close_count=1, path="()"
  Choice ')' → close_count(1) < open_count(1)? NO -> PRUNED (would make "())" invalid)
  Choice '(' → open_count(1) < n(3)? YES -> ALLOWED -> path="()("
```

This is a textbook example of **constraint-based pruning replacing an explicit validity check** — instead of generating all `2^(2n)` strings of `(`/`)` and checking balance afterward (brute force), we only ever generate strings that are valid *prefixes* of a balanced sequence.

**State Space Tree (`n=2`, partial):**

```
                         (0,0) ""
                        /
                    (1,0) "("
                   /        \
              (2,0)"(("   (1,1)"()"
                 |             |          \
             (2,1)"(()"    (2,1)"()("   [close<open? 1<1 NO, pruned]
                 |               |
             (2,2)"(())"    (2,2)"()()"
```

**Complexity:** Time & Space `O(4^n / √n)` — bounded by the **Catalan number** `C_n = (1/(n+1)) · C(2n, n)`, the exact count of valid sequences.

**Branching Factor Analysis:** Maximum 2 choices per node, but the *effective* branching factor is throttled hard by the `close_count < open_count` constraint — this is why pruning turns a `2^(2n)` brute force into a `Catalan(n)` search.

**Common Mistakes:** Using `if/elif` instead of two independent `if`s (both branches can be valid at once — must try both, not just one); forgetting the `close_count < open_count` guard (produces invalid strings like `")("`).

**Interview Tip:** This problem is the cleanest illustration of "prune the search space via a mathematical invariant" rather than post-hoc filtering — call this out explicitly when explaining your solution.

---

## 5.9 N-Queens

**Problem:** Place `n` queens on an `n×n` chessboard so that no two queens attack each other (same row, column, or diagonal). Return all distinct board configurations.

**Approach:** Place one queen per row (rows never conflict since we place exactly one queen per row by construction). For each row, try every column; use sets to track occupied columns and the two diagonal directions in O(1).

```python
def solveNQueens(n):
    result = []
    cols = set()
    diag1 = set()   # identified by (row - col), constant along a "/" diagonal
    diag2 = set()   # identified by (row + col), constant along a "\" diagonal
    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue                              # PRUNE: attacked
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            board[row][col] = "Q"

            backtrack(row + 1)

            board[row][col] = "."                     # UNDO
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

    backtrack(0)
    return result

solutions = solveNQueens(4)
print(len(solutions))     # 2
for r in solutions[0]:
    print(r)
# .Q..
# ...Q
# Q...
# ..Q.
```

**Why `row - col` and `row + col`?** Every cell on the same "↗" diagonal shares a constant `row - col`; every cell on the same "↘" diagonal shares a constant `row + col`. This gives **O(1) diagonal-conflict checks** instead of O(n) scanning.

**State Space Tree (`n=4`, partial — showing pruning):**

```
                       row 0: try col 0,1,2,3
                     Q at (0,0)
                    /
              row 1: col0 X(same col) col1 X(diag) col2 OK col3 OK
                 Q at (1,2)                Q at (1,3)
                /                              \
      row2: col0 OK? check...           row2: all attacked -> DEAD END, backtrack
     ...eventually all paths from (0,0) fail for n=4 with THIS branch order
     (full search finds solutions starting Q at (0,1) and (0,2))
```

**Call Stack / Undo Trace:**

```
backtrack(0): cols={}, diag1={}, diag2={}
  col=0 valid → cols={0}, diag1={0}, diag2={0}, board[0][0]='Q'
    backtrack(1): 
      col=0 → in cols? NO wait 0 in cols=True → skip
      col=1 → diag1: 1-1=0 in diag1={0}? YES → skip
      col=2 → cols:2∉{0} diag1:1-2=-1∉{0} diag2:1+2=3∉{0} → VALID
        cols={0,2}, diag1={0,-1}, diag2={0,3}, board[1][2]='Q'
        backtrack(2): ... (continues or dead-ends)
        UNDO: board[1][2]='.', cols={0}, diag1={0}, diag2={0}
      col=3 → similarly tried
    UNDO row 0: board[0][0]='.', cols={}, diag1={}, diag2={}
  col=1 valid → try next branch...
```

**Complexity:** Time `O(n!)` worst case (roughly — much better in practice due to pruning; true bound relates to the permutation search tree with diagonal pruning), Space `O(n)` for sets + `O(n²)` for board.

**Edge Cases:** `n=1` → one trivial solution `["Q"]`; `n=2` or `n=3` → no solution exists (`[]`).

**Common Mistakes:** Using O(n) row/column scanning instead of O(1) sets (still correct, just slower); forgetting to remove entries from `diag1`/`diag2` sets on undo (corrupts future pruning).

**Interview Tip:** Mention the O(1) diagonal-identification trick proactively — it signals strong pattern recognition and is a common "optimize this" follow-up.

**Variations:** N-Queens II (return only the *count*, skip storing boards — an optimization); "does at least one solution exist" (Find-One pattern, §4.4).

---

## 5.10 Sudoku Solver

**Problem:** Fill a 9×9 Sudoku grid so every row, column, and 3×3 box contains digits `1-9` exactly once, given some cells pre-filled.

```python
def solveSudoku(board):
    def valid(r, c, val):
        for i in range(9):
            if board[r][i] == val or board[i][c] == val:
                return False
        box_r, box_c = 3 * (r // 3), 3 * (c // 3)
        for i in range(box_r, box_r + 3):
            for j in range(box_c, box_c + 3):
                if board[i][j] == val:
                    return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for val in "123456789":
                        if valid(r, c, val):
                            board[r][c] = val
                            if backtrack():          # Find-One pattern
                                return True
                            board[r][c] = "."        # UNDO
                    return False                     # no digit worked here -> dead end
        return True                                  # no empty cells left -> solved

    backtrack()
    return board
```

**This is a Constraint Satisfaction Problem (CSP):**

| CSP Element | Sudoku Mapping |
|---|---|
| Variables | The 81 cells |
| Domains | `{1,...,9}` per empty cell |
| Constraints | Row, column, and box "all different" |
| Assignment | Filling in a digit (a "choice") |
| Consistency Check | `valid(r, c, val)` |

**State Space Tree (conceptual, first empty cell only):**

```
              cell(0,0) empty, try 1..9
       /        |        |               \
     try 1    try 2    try 3     ...    try 9
   valid?    valid?   valid?           valid?
     |          X         |                |
  recurse    (skip)    recurse          recurse
  to next                to next        to next
  empty cell             empty cell      empty cell
     |                                       |
  ...continues until either SOLVED       or DEAD END -> backtrack,
  (all 81 filled) or a dead end forces      undo this cell's value,
  backtracking to try the next digit         try next digit at PARENT
  at some ancestor cell                       cell
```

**Complexity:** Time worst-case `O(9^m)` where `m` = number of empty cells (heavily pruned in practice by the `valid()` constraint check — real Sudoku puzzles solve near-instantly). Space `O(m)` recursion depth ≤ 81.

**Common Mistakes:** Checking validity *after* placing all 81 (way too slow — must check incrementally per cell); not returning `True`/`False` correctly through the recursion (breaks the Find-One early-exit propagation, see §4.4); recomputing full board validity instead of localized row/col/box checks.

**Optimizations:**
- **Constraint Propagation:** maintain per-row/column/box "available digits" bitmasks, updated incrementally instead of rescanning 9+9+9 cells every check — turns `valid()` from O(27) into O(1).
- **Most-Constrained-Variable Heuristic:** always pick the empty cell with the *fewest* valid candidates first (fail fast), rather than scanning row-major order.

**Interview Tip:** Sudoku is the go-to example for explaining CSPs in interviews — explicitly naming "variables/domains/constraints" demonstrates AI/CS fundamentals, not just coding.

---

## 5.11 Rat in a Maze

**Problem:** A rat starts at `(0,0)` in an `n×n` grid (1 = open, 0 = blocked) and must reach `(n-1,n-1)`, moving in directions `D`(own), `L`, `R`, `U`. Return all paths as strings, in sorted order.

```python
def ratInMaze(maze):
    n = len(maze)
    result = []
    path = []
    visited = [[False] * n for _ in range(n)]

    directions = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]

    def backtrack(r, c):
        if r == n - 1 and c == n - 1:
            result.append("".join(path))
            return
        for d, dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True                 # mark visited (CHOOSE)
                path.append(d)
                backtrack(nr, nc)                       # EXPLORE
                path.pop()                              # UNCHOOSE
                visited[nr][nc] = False                 # unmark (UNDO)

    if maze[0][0] == 1:
        visited[0][0] = True
        backtrack(0, 0)

    return sorted(result)

maze = [[1,0,0,0],
        [1,1,0,1],
        [1,1,0,0],
        [0,1,1,1]]
print(ratInMaze(maze))
# ['DDRDRR', 'DRDDRR']
```

**Grid DFS Visualization:**

```
Maze (1=open, 0=blocked):        Path 1: DDRDRR             Path 2: DRDDRR
  1 0 0 0                         S . . .                    S . . .
  1 1 0 1                         ↓ . . .                     ↓ . . .
  1 1 0 0                         ↓→↓. .                     ↓ . . .
  0 1 1 1                         . ↓→→E                       ↓→↓→E    (etc.)
```

**Complexity:** Time `O(4^(n²))` worst case (4 choices per cell, up to n² cells) — pruned heavily by `visited` + blocked-cell checks; Space `O(n²)` for visited + recursion depth.

**Common Mistakes:** Forgetting to unmark `visited` on backtrack (rat can never revisit a cell in *any* other path, which is wrong — visited should be **path-local**, not global); not checking boundaries before indexing (`IndexError`).

**Variations:** Return only *one* path (Find-One); return the *shortest* path (better solved with BFS, not backtracking, since BFS naturally finds shortest paths in unweighted grids — a good "when NOT to use backtracking" example).

---

## 5.12 Word Search

**Problem:** Given a 2D board of letters and a word, determine if the word can be constructed from letters of sequentially adjacent cells (horizontally/vertically), using each cell at most once.

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False

        temp = board[r][c]
        board[r][c] = "#"                 # mark visited in-place (no extra memory!)

        found = (backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or
                 backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1))

        board[r][c] = temp                # UNDO — restore original letter

        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
print(exist(board, "ABCCED"))  # True
print(exist(board, "SEE"))     # True
print(exist(board, "ABCB"))    # False
```

**In-Place Marking Trick:** Instead of a separate `visited` grid, we temporarily overwrite `board[r][c] = "#"` (a character guaranteed not to match any letter), then restore it — this is a classic **space optimization**: O(1) extra space for "visited" instead of O(rows·cols).

**DFS Traversal Visualization (`"ABCCED"`):**

```
Board:            Search path for "ABCCED":
A B C E           A(0,0)→B(0,1)→C(0,2)→C(1,2)→E(2,2)... wait, must recheck adjacency
S F C S              [start]  [right] [right] [down]  [down]  [left]
A D E E             A    →    B   →   C    →   C    →   E   →   D
                    (0,0)   (0,1)   (0,2)    (1,2)    (2,2)   (2,1)
```

**Complexity:** Time `O(rows · cols · 4^L)` where `L = len(word)` (4 directions per character, from every starting cell), Space `O(L)` recursion depth (board is mutated in place, not copied).

**Common Mistakes:** Copying the board instead of in-place marking (wastes O(rows·cols) memory per call — very slow); forgetting to restore `board[r][c] = temp` (corrupts board for other starting positions); not handling the case where the same cell is reused within one path (in-place marking with `"#"` inherently prevents this).

**Interview Tip:** Explicitly mention the in-place-marking space trick — interviewers often ask "can you do this without extra memory?" as a follow-up, and volunteering it first is a strong signal.

**Variations:** Word Search II (multiple words — build a **Trie** first, then backtrack once over the board, pruning branches that aren't a Trie prefix — a major optimization over calling `exist()` once per word).

---

## 5.13 Palindrome Partitioning

**Problem:** Partition a string `s` such that every substring of the partition is a palindrome. Return all such partitionings.

```python
def partition(s):
    result = []
    path = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end)
                path.pop()

    backtrack(0)
    return result

print(partition("aab"))
# [['a', 'a', 'b'], ['aa', 'b']]
```

**This is the Partition Pattern (§4.5):** the "choice" at each step is *where to cut next*, not which element to pick.

**State Space Tree (`"aab"`):**

```
                        backtrack(0), s="aab"
              /                    |                     \
        cut "a"(0:1)         cut "aa"(0:2)          cut "aab"(0:3)
        palindrome? YES       palindrome? YES        palindrome? NO -> pruned
             |                       |
      backtrack(1)              backtrack(2)
      /          \                   |
  cut"a"(1:2)  cut"ab"(1:3)      cut"b"(2:3)
  palin? YES    palin? NO        palin? YES
      |          (pruned)             |
  backtrack(2)                   backtrack(3) == len(s) -> SAVE ["aa","b"]
      |
  cut"b"(2:3)
  palin? YES
      |
  backtrack(3) == len(s) -> SAVE ["a","a","b"]
```

**Complexity:** Time `O(n · 2^n)` worst case (2^n possible partitions of an n-length string, O(n) palindrome check each — can be reduced to O(1) amortized with a precomputed DP table). Space `O(n)` recursion depth.

**Optimization — Precompute Palindrome Table:**

```python
def partition_optimized(s):
    n = len(s)
    # dp[i][j] = True if s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length <= 2 or dp[i + 1][j - 1]):
                dp[i][j] = True

    result, path = [], []
    def backtrack(start):
        if start == n:
            result.append(path[:])
            return
        for end in range(start, n):
            if dp[start][end]:
                path.append(s[start:end + 1])
                backtrack(end + 1)
                path.pop()
    backtrack(0)
    return result
```
This turns each `is_palindrome` check from `O(n)` into `O(1)`, at the cost of `O(n²)` preprocessing time/space — a classic **backtracking + DP hybrid**.

**Common Mistakes:** Re-checking palindromes naively for large strings (slow); off-by-one errors in substring slicing (`s[start:end]` is exclusive of `end`).

**Variations:** Palindrome Partitioning II (return the *minimum number of cuts* — pure DP is more efficient here than backtracking, another "when NOT to use backtracking" case).

---

## 5.14 Restore IP Addresses

**Problem:** Given a string of digits, return all possible valid IP address combinations (4 segments, each `0-255`, no leading zeros unless the segment is exactly `"0"`).

```python
def restoreIpAddresses(s):
    result = []
    path = []

    def backtrack(start):
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return
        for length in range(1, 4):                 # each segment is 1-3 digits
            if start + length > len(s):
                break
            segment = s[start:start + length]
            if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                continue                            # PRUNE invalid segment
            path.append(segment)
            backtrack(start + length)
            path.pop()

    backtrack(0)
    return result

print(restoreIpAddresses("25525511135"))
# ['255.255.11.135', '255.255.111.35']
```

**Constraint Checking Table:**

| Segment | Rule | Example (Valid) | Example (Invalid) |
|---|---|---|---|
| Length | 1-3 digits | `"5"`, `"25"`, `"255"` | `"1234"` (too long) |
| Leading zero | Only `"0"` itself allowed | `"0"` | `"05"`, `"00"` |
| Range | `0 ≤ value ≤ 255` | `"255"` | `"256"`, `"999"` |

**State Space Tree (partial, `"2552..."`):**

```
                    backtrack(0), path=[]
        /                |                  \
   seg="2"           seg="25"             seg="255"
  (len(path)=1)      (len(path)=1)        (len(path)=1)
        |                |                     |
   ... 3 more levels, each trying length 1,2,3 and pruning
   invalid segments (leading zero / >255 / string exhausted
   before 4 segments / string not exhausted after 4 segments)
```

**Complexity:** Time `O(1)` effectively — at most `3^4 = 81` combinations are ever tried regardless of input length (4 segments × 3 possible lengths each), so this is technically **constant time bounded by problem constraints**. Space `O(1)` (max recursion depth 4).

**Common Mistakes:** Forgetting the "no leading zero" rule (`"010"` is invalid even though numerically `≤255`); not checking `start == len(s)` at the end (allows leftover unused digits to silently pass); allowing segment length > 3 (e.g., `"2555"` numerically could be sliced wrong).

**Interview Tip:** Point out early that this problem's search space is *bounded by a small constant* (81), not by input length — this reframes the complexity analysis correctly and shows precise Big-O reasoning.

---

## 5.15 Expression Add Operators

**Problem:** Given a string of digits `num` and a target integer, return all ways to add the binary operators `+`, `-`, or `*` between digits so the resulting expression evaluates to `target`. (No leading zeros in any operand.)

```python
def addOperators(num, target):
    result = []
    n = len(num)

    def backtrack(index, expr, value, prev_operand):
        if index == n:
            if value == target:
                result.append(expr)
            return
        for i in range(index, n):
            segment = num[index:i + 1]
            if len(segment) > 1 and segment[0] == "0":     # no leading zeros
                break
            curr = int(segment)
            if index == 0:
                # first operand — no operator before it
                backtrack(i + 1, segment, curr, curr)
            else:
                backtrack(i + 1, expr + "+" + segment, value + curr, curr)
                backtrack(i + 1, expr + "-" + segment, value - curr, -curr)
                # for '*': undo the previous operand's addition/subtraction,
                # then apply it multiplied by curr (operator precedence trick)
                backtrack(i + 1, expr + "*" + segment, value - prev_operand + prev_operand * curr, prev_operand * curr)
    backtrack(0, "", 0, 0)
    return result

print(addOperators("123", 6))
# ['1+2+3', '1*2*3']
```

**The Multiplication Precedence Trick:** Since `*` binds tighter than `+`/`-`, when we add a `*`, we must "undo" the previous operand's contribution to `value` and re-apply it multiplied by the new number:

```
Example: "1+2*3" should evaluate to 1 + (2*3) = 7, not (1+2)*3 = 9

State before adding '*3': value = 1+2 = 3, prev_operand = +2
New value = value - prev_operand + prev_operand*curr
          = 3 - 2 + 2*3 = 1 + 6 = 7   ✅ correct precedence
```

**Complexity:** Time `O(4^n)` (3 operators + 1 "extend the operand" choice per position, roughly), Space `O(n)` recursion depth + string building.

**Common Mistakes:** Missing the leading-zero check (`"05"` as an operand is invalid); forgetting the multiplication-precedence undo trick (produces wrong values silently, not a crash — hard to debug); mismanaging `index==0` (there is no operator before the first operand).

**Interview Tip:** This is one of the hardest backtracking problems on major interview lists specifically *because* of the precedence trick — explaining it clearly is a strong signal of deep understanding, not just memorized code.

---

## 5.16 Partition into K Equal Sum Subsets

**Problem:** Given an array `nums` and integer `k`, determine if it's possible to partition `nums` into `k` non-empty subsets with equal sums.

```python
def canPartitionKSubsets(nums, k):
    total = sum(nums)
    if total % k != 0:
        return False
    target = total // k
    nums.sort(reverse=True)             # PRUNE: place large numbers first (fail fast)
    if nums[0] > target:
        return False

    n = len(nums)
    used = [False] * n

    def backtrack(start, k_remaining, current_sum):
        if k_remaining == 0:
            return True                                  # all k subsets successfully formed
        if current_sum == target:
            return backtrack(0, k_remaining - 1, 0)       # start filling the next subset
        for i in range(start, n):
            if used[i] or current_sum + nums[i] > target:
                continue
            used[i] = True
            if backtrack(i + 1, k_remaining, current_sum + nums[i]):
                return True
            used[i] = False
            if current_sum == 0:
                break                    # PRUNE: if this element fails as a fresh subset's
                                         # first pick, no reordering of remaining will help
        return False

    return backtrack(0, k, 0)

print(canPartitionKSubsets([4,3,2,3,5,2,1], 4))   # True
```

**Key Pruning Techniques Used:**

1. **Sort descending** — large numbers are the most constrained; placing them first fails fast instead of discovering infeasibility deep in the recursion.
2. **`current_sum + nums[i] > target` skip** — a direct bounding/feasibility check.
3. **`if current_sum == 0: break`** — if the *first* element tried for a new subset fails, trying a *different* first element in the same position is symmetric and pointless (any valid combination containing `nums[i]` could equally start with a different element — this specific break prunes a huge redundant branch class).

**State Space Tree (conceptual):**

```
                     backtrack(start=0, k_remaining=4, sum=0)
                                    |
                     try nums[i] as part of subset #1
                     /              |                \
                nums[0]         nums[1]            nums[2] ...
              sum updated    sum updated          sum updated
                    |
        ... continue until current_sum == target for subset #1,
        then reset sum=0, k_remaining -=1, start=0, try to fill subset #2
        ... repeat until k_remaining == 0 (success) or all branches exhausted (fail)
```

**Complexity:** Time `O(k^n)` worst case (each element can conceptually go into any of `k` buckets), heavily pruned in practice. Space `O(n)` for `used` + recursion depth.

**Common Mistakes:** Not sorting descending (huge performance loss — order-of-magnitude slower on large inputs); forgetting the `current_sum == 0: break` pruning (correct but far slower); not handling `total % k != 0` as an immediate `False`.

**Variations:** Matchsticks to Square (special case where `k=4`); Fair Distribution of Cookies (similar bucket-filling backtracking with different constraints).

---

## 5.17 Crossword Puzzle (Overview)

**Problem (Conceptual):** Given a crossword grid with blank/filled cells and a list of words, place every word into the grid such that intersecting letters match.

Crossword solving is a **large-scale CSP**, combining ideas from every problem above:

- **Variables:** each word to be placed.
- **Domains:** every (position, orientation) pair where the word *could* fit given the grid's blank-cell shape.
- **Constraints:** intersecting cells must share the same letter; word must fit entirely within blank cells.

```python
def solveCrossword(board, words):
    rows, cols = len(board), len(board[0])

    def can_place(word, r, c, horizontal):
        for k in range(len(word)):
            rr, cc = (r, c + k) if horizontal else (r + k, c)
            if rr >= rows or cc >= cols:
                return False
            if board[rr][cc] not in ("-", word[k]):
                return False
        return True

    def place(word, r, c, horizontal, letter):
        for k in range(len(word)):
            rr, cc = (r, c + k) if horizontal else (r + k, c)
            board[rr][cc] = letter[k] if letter else "-"

    def backtrack(word_index):
        if word_index == len(words):
            return True
        word = words[word_index]
        for r in range(rows):
            for c in range(cols):
                for horizontal in (True, False):
                    if can_place(word, r, c, horizontal):
                        original = [board[r][c + k] if horizontal else board[r + k][c] for k in range(len(word))]
                        place(word, r, c, horizontal, word)
                        if backtrack(word_index + 1):
                            return True
                        # undo: restore original letters
                        for k in range(len(word)):
                            rr, cc = (r, c + k) if horizontal else (r + k, c)
                            board[rr][cc] = original[k]
        return False

    backtrack(0)
    return board
```

> 📝 **Note:** Full crossword solving (with arbitrary word intersections, like LeetCode's "Crossword Puzzle" variants) is **notoriously slow** with naive backtracking on large grids — real solvers use **constraint propagation** (arc-consistency, à la the AC-3 algorithm) to shrink domains before/during search, which is the natural next topic after mastering plain backtracking CSPs.

**Interview Tip:** Crossword-style problems are rare as *full* interview questions but common as **"design a CSP solver"** system-design-adjacent discussions — knowing the variables/domains/constraints framing (§5.10) transfers directly.

---
# 6. Pruning Techniques

Pruning is what separates **backtracking** from **brute force**. Both explore a state space, but backtracking cuts off branches the instant they're known to fail.

## 6.1 Techniques Overview

| Technique | Idea | Example |
|---|---|---|
| **Constraint Checking** | Verify a choice doesn't violate a rule before recursing | N-Queens column/diagonal check |
| **Bounding** | Skip if even the best-case remaining choices can't reach the goal | Combinations: `(k - len(path)) > (n - i + 1)` |
| **Early Termination** | Stop searching entirely once *one* answer is found (Find-One) | Sudoku, N-Queens existence |
| **Duplicate Avoidance** | Skip choices that would generate an already-seen result | Subsets II, Permutations II |
| **Visited Array/Set** | Prevent reusing an element/cell within one path | Permutations, Word Search |
| **Sorting Before Search** | Enables `break` instead of `continue`, and duplicate-adjacency checks | Combination Sum, Combination Sum II |
| **Branch Pruning (General)** | Any domain-specific early `continue`/`break`/`return` | All of the above |
| **Search Space Reduction** | Precompute reusable data to make constraint checks O(1) | Sudoku bitmasks, Palindrome DP table |

## 6.2 Constraint Checking — Visualized

```
BEFORE choosing:  check is_valid(choice, state)?
                        |
              ┌─────────┴─────────┐
             YES                  NO
              │                    │
        proceed to CHOOSE      SKIP this choice
        → EXPLORE → UNCHOOSE   (continue loop, no
                                 recursive call made
                                 at all — this IS
                                 the "pruned" branch)
```

> 💡 **Tip:** The performance value of pruning comes from checking constraints **before** recursing, not after. A check placed only in the base case still explores every branch fully — no better than brute force.

## 6.3 Bounding — Visualized

```
Combinations(n=5, k=3), path=[1], considering candidates 2..5

  remaining slots needed = k - len(path) = 3 - 1 = 2
  remaining slots left starting at i:
     i=2: n - i + 1 = 5 - 2 + 1 = 4  → 2 <= 4  OK, try it
     i=4: n - i + 1 = 5 - 4 + 1 = 2  → 2 <= 2  OK, try it (exactly enough)
     i=5: n - i + 1 = 5 - 5 + 1 = 1  → 2 >  1  PRUNE (not enough remain)
```

## 6.4 Duplicate Avoidance Patterns

| Scenario | Technique |
|---|---|
| Duplicate *values* at the same recursion depth (Subsets II, Combination Sum II) | Sort, then `if i > start and nums[i] == nums[i-1]: continue` |
| Duplicate *permutations* from duplicate values (Permutations II) | Sort, then `if i > 0 and nums[i]==nums[i-1] and not used[i-1]: continue` (§5.6) |
| Duplicate *board states* (rare, e.g. some puzzle variants) | Memoize visited states with a `set` of canonical representations |

## 6.5 Search Space Reduction via Precomputation

| Problem | Naive Check | Reduced Check |
|---|---|---|
| Palindrome Partitioning | `O(n)` string reversal per substring | `O(1)` via precomputed `dp[i][j]` table |
| Sudoku | `O(27)` row+col+box scan per placement | `O(1)` via maintained bitmasks per row/col/box |
| N-Queens | `O(n)` diagonal scan | `O(1)` via `diag1`/`diag2` sets |

---

# 7. Applications of Backtracking

| Domain | Application | Notes |
|---|---|---|
| **Puzzle Solving** | Sudoku, crosswords, KenKen, logic grid puzzles | Modeled as CSPs |
| **Constraint Satisfaction** | Map/graph coloring, scheduling, exam timetabling | Variables + domains + constraints |
| **Scheduling** | Assigning tasks to time slots/resources under constraints | Backtracking as a fallback when greedy/DP don't apply |
| **AI Search** | Game tree exploration (with pruning like alpha-beta) | Minimax + backtracking share DFS structure |
| **Pathfinding** | Maze solving, robot motion planning (small state spaces) | BFS/Dijkstra preferred for *shortest* path; backtracking for *all* paths |
| **Game Solving** | Tic-tac-toe, small chess endgames, word games (Boggle) | Exhaustive move exploration |
| **Combinatorial Optimization** | Knapsack variants (via branch-and-bound, backtracking's optimization-aware cousin) | Adds bounding functions on objective value |
| **Compilers/Parsing** | Backtracking parsers for ambiguous grammars | Modern parsers prefer non-backtracking approaches (LL/LR) for performance |
| **Bioinformatics** | Motif finding, sequence alignment variants | Exhaustive search over small alphabets |

---

# 8. Problem Recognition Guide

## 8.1 Recognition Flowchart

```
                     ┌───────────────────────────────┐
                     │ Does the problem ask for ALL   │
                     │ solutions / combinations /     │
                     │ arrangements / configurations? │
                     └───────────────┬─────────────────┘
                                     │ YES
                                     ▼
                     ┌───────────────────────────────┐
                     │ Are choices made incrementally,│
                     │ with later choices depending   │
                     │ on earlier ones (constraints)? │
                     └───────────────┬─────────────────┘
                                     │ YES
                                     ▼
                     ┌───────────────────────────────┐
                     │ Can a partial solution be      │
                     │ detected as "doomed" before    │
                     │ it's fully built (pruning)?    │
                     └───────────────┬─────────────────┘
                              YES    │    NO (all must be built fully)
                                     ▼                 ▼
                          BACKTRACKING WITH        BACKTRACKING
                          PRUNING (efficient)      (still valid, brute-force-like)
```

## 8.2 Interview Clue Keywords

| Keyword in Problem Statement | Likely Pattern |
|---|---|
| "all possible subsets/combinations" | Subset/Combination generation |
| "all permutations/arrangements/orderings" | Permutation generation |
| "partition the string/array such that..." | Partition pattern |
| "place N non-attacking..." | CSP grid placement (N-Queens style) |
| "fill the grid such that..." | CSP (Sudoku style) |
| "does there exist a path..." | Grid DFS backtracking (Find-One) |
| "return the number of ways" | Could be backtracking (small n) OR DP (large n) — check constraints! |
| Small `n` (`n ≤ 12-20`) in constraints | Strong signal for backtracking/bitmask DP over brute force |
| "generate all valid..." | Constraint-driven generation (Generate Parentheses style) |

## 8.3 State-Space Thinking Checklist

1. What does one **state** look like? (a partial path, a partial board, a partial string?)
2. What are the **choices** available from a given state?
3. What **constraint(s)** must a choice satisfy?
4. What is the **goal condition** (when is a state "complete")?
5. Can I detect an invalid state **early** (pruning opportunity)?
6. Do I need **Generate All** or **Find One**?
7. Are there **duplicates** in the input that need special handling?

> ⚠️ **Warning:** If `n` in the constraints is large (e.g., `n ≥ 10^5`), the problem is almost certainly **not** meant to be solved with raw backtracking — look for DP, greedy, or a mathematical formula instead.

---

# 9. Optimization Strategies

## 9.1 Brute Force → Backtracking → Optimized Backtracking

```
BRUTE FORCE                  BACKTRACKING                 OPTIMIZED BACKTRACKING
Generate ALL possible        Build incrementally,         Same as backtracking, PLUS:
candidates, THEN filter      pruning invalid branches      - O(1) constraint checks
valid ones.                  as soon as detected.          - bounding functions
                                                            - precomputed lookup tables
O(total space) always        O(pruned space) — often       - smart choice ordering
                              much smaller in practice      (most-constrained-first)
```

## 9.2 Concrete Optimization Techniques

| Technique | Effect |
|---|---|
| **Constraint Propagation** | Reduce future domains immediately after each assignment (e.g., Sudoku candidate elimination) |
| **Efficient State Representation** | Use bitmasks/sets instead of O(n) scans (N-Queens diagonals, Sudoku rows) |
| **Branch Pruning** | Add domain-specific early exits (bounding, bad-prefix detection) |
| **Search Space Reduction** | Precompute reusable data (palindrome tables, prefix sums) |
| **Ordering Choices** | Try most-constrained or most-likely-to-fail choices first (fail fast) |
| **Duplicate Elimination** | Sort + skip to avoid regenerating identical results |
| **Iterative Deepening** (advanced) | Bound recursion depth progressively when solution length is unknown |
| **Memoization** (when subproblems repeat, unlike most enumeration tasks) | Cache results for identical sub-states (rare in "generate all" tasks, common in Find-One/count tasks with overlapping states) |

## 9.3 Ordering Choices — Example (Partition into K Subsets)

Sorting `nums` descending before backtracking (§5.16) is a direct application of "most-constrained-first" — large numbers have the fewest valid placements, so trying them first fails fast instead of deep in the recursion.

---

# 10. Interview Preparation

## 10.1 Difficulty Progression

| Level | Problems |
|---|---|
| **Easy** | Subsets, Letter Combinations, Binary Watch |
| **Medium** | Permutations, Combinations, Combination Sum, Generate Parentheses, Palindrome Partitioning, Word Search, Restore IP Addresses |
| **Hard** | N-Queens, Sudoku Solver, Expression Add Operators, Partition to K Equal Sum Subsets, Word Search II |

## 10.2 Pattern-Wise Question Map

| Pattern | Representative Problems |
|---|---|
| Pick/Not-Pick | Subsets, Subsets II, Subset Sum |
| Combinations | Combinations, Combination Sum, Combination Sum II/III |
| Permutations | Permutations, Permutations II, Next Permutation (iterative, not backtracking) |
| Partition | Palindrome Partitioning, Restore IP Addresses |
| Grid DFS | Word Search, Rat in a Maze, Number of Islands (DFS, not full backtracking) |
| CSP | N-Queens, Sudoku Solver |

## 10.3 Company-Wise Tendencies (General Trends)

| Company Type | Common Emphasis |
|---|---|
| Big Tech (FAANG-style) | N-Queens, Word Search, Combination Sum, Permutations — clean code + complexity analysis |
| Quant/Finance | Combinatorics-heavy variants, expression building, probability-adjacent backtracking |
| Startups | Practical variants — scheduling, grid puzzles, real constraint-satisfaction scenarios |



## 10.4 "Blind 75" / "NeetCode" Style Backtracking Set

A commonly cited core set of backtracking problems appearing across popular curated interview lists:

- Subsets
- Combination Sum
- Permutations
- Word Search
- Palindrome Partitioning
- Letter Combinations of a Phone Number
- N-Queens

## 10.5 Frequently Asked Interview Tricks

- "Can you avoid the extra `used` array?" → swap-based permutations .
- "Can you do this in-place / O(1) extra space?" → Word Search in-place marking.
- "What if there are duplicates?" → sort + skip pattern .
- "Can you return just the count, not all solutions?" → skip storing full paths, just increment a counter (N-Queens II style).
- "Can you find just one solution faster?" → Find-One pattern with early-exit propagation .

---

# 11. Python-Specific Tips

## 11.1 List Operations Cheat Sheet

| Operation | Code | Complexity |
|---|---|---|
| Append | `path.append(x)` | O(1) amortized |
| Remove last (undo) | `path.pop()` | O(1) |
| Shallow copy | `path[:]` / `list(path)` / `path.copy()` | O(n) |
| Deep copy (nested structures) | `copy.deepcopy(path)` | O(n) but slower (avoid unless truly needed) |
| Membership check | `x in path` | O(n) — prefer a `set` for repeated checks |

## 11.2 Deep Copy vs. Shallow Copy

```python
import copy

path = [[1, 2], [3, 4]]
shallow = path[:]              # new outer list, SAME inner lists
deep = copy.deepcopy(path)     # new outer list AND new inner lists

path[0].append(99)
print(shallow)  # [[1, 2, 99], [3, 4]]  <- affected! shares inner list references
print(deep)     # [[1, 2], [3, 4]]      <- unaffected
```

> ⚠️ **Warning:** For flat lists of immutable elements (ints, strings), shallow copy (`path[:]`) is sufficient and much faster. Only reach for `deepcopy` when `path` contains nested mutable structures.

## 11.3 Recursion Depth

```python
import sys
print(sys.getrecursionlimit())     # default: 1000
sys.setrecursionlimit(10000)       # raise if needed for deep recursion (e.g., large permutation depth)
```

> ⚠️ **Warning:** Raising the recursion limit doesn't raise the *actual* C-stack limit — extremely deep recursion can still crash the interpreter (`Segmentation fault`) rather than raising a clean `RecursionError`. For very deep search spaces, consider converting to an **iterative** backtracking implementation using an explicit stack.

## 11.4 Performance Tips

- Prefer **local variable lookups** over repeated attribute access in hot recursive loops.
- Use `sys.setrecursionlimit` cautiously; prefer restructuring to reduce depth when possible.
- Avoid unnecessary `path[:]` copies — only copy when **saving** a result, never on every recursive call.
- Use `"".join(path)` instead of repeated string concatenation (`path + ch`) inside loops — strings are immutable, so `+=` in a loop is O(n) per operation, `O(n²)` total.
- Prefer `set`/`frozenset` for O(1) membership tests over list scans.

## 11.5 Common Python Pitfalls

| Pitfall | Fix |
|---|---|
| Mutable default argument (`def f(path=[])`) | Use `path=None`, initialize inside function |
| Forgetting `path[:]` when saving results | Always copy on save |
| Off-by-one in slicing (`s[i:j]` excludes `j`) | Double-check slice boundaries with a dry run |
| Modifying a list while iterating over it | Iterate over a copy, or use indices carefully |
| Global recursion depth exceeded silently truncating results | Catch `RecursionError` explicitly during development/testing |

---

# 12. Common Mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| **Forgetting to Undo** | Path/board state leaks into sibling branches, wrong/missing results | Always pair every "choose" with an "unchoose" |
| **Wrong Base Case** | Infinite recursion, `RecursionError`, or missing/incomplete results | Carefully define exactly when a state is "complete" |
| **Duplicate Results** | Same combination/permutation appears multiple times | Sort input + skip duplicate at same depth |
| **Mutable List Bugs** | All saved results look identical (usually all empty) | Save `path[:]`, not `path` |
| **Incorrect Visited Handling** | Cells/elements reused illegally, or falsely blocked forever | Mark on choose, unmark on undo — never leave marked permanently |
| **Infinite Recursion** | Program hangs / crashes with `RecursionError` | Ensure every recursive call moves strictly closer to a base case |
| **Missing Constraints** | Invalid solutions included in output | Validate every choice *before* recursing, not just at the end |
| **Excessive Copying** | Extremely slow runtime on large inputs | Copy only at save-points; mutate in place otherwise |
| **Poor Pruning** | Correct but far too slow (TLE in competitive judges) | Add bounding/early-exit checks  |

---

# 13. Cheat Sheets

## 13.1 The One Template to Rule Them All

```python
def backtrack(state):
    if is_goal(state):
        record_solution(state)
        return  # (or `return True` for Find-One pattern)

    for choice in get_choices(state):
        if not is_valid(choice, state):
            continue
        apply_choice(choice, state)      # CHOOSE
        backtrack(state)                 # EXPLORE
        undo_choice(choice, state)       # UNCHOOSE
```

## 13.2 Complexity Cheat Sheet

| Problem | Time Complexity | Space Complexity |
|---|---|---|
| Subsets | O(n · 2^n) | O(n) |
| Combinations | O(k · C(n,k)) | O(k) |
| Combination Sum | O(2^target) (bounded) | O(target/min) |
| Permutations | O(n · n!) | O(n) |
| Letter Combinations | O(4^n · n) | O(n) |
| Generate Parentheses | O(4^n / √n) (Catalan) | O(n) |
| N-Queens | O(n!) (heavily pruned) | O(n) |
| Sudoku Solver | O(9^m), m = empty cells | O(m) |
| Rat in a Maze | O(4^(n²)) | O(n²) |
| Word Search | O(rows·cols·4^L) | O(L) |
| Palindrome Partitioning | O(n · 2^n) | O(n) (or O(n²) with DP table) |
| Restore IP Addresses | O(1) (bounded by 3^4) | O(1) |
| Partition K Subsets | O(k^n) (heavily pruned) | O(n) |

## 13.3 Pattern Recognition Cheat Sheet

| Signal | Pattern |
|---|---|
| "no reuse, order doesn't matter" | Combinations/Subsets |
| "reuse allowed, order doesn't matter" | Combination Sum |
| "no reuse, order matters" | Permutations |
| "reuse allowed, order matters" | Rare — usually a different technique (DP) |
| "grid + path" | Grid DFS Backtracking |
| "split string/array into valid parts" | Partition Pattern |
| "place items under mutual constraints" | CSP (N-Queens, Sudoku) |

## 13.4 Python Syntax Quick Reference

```python
path[:]                 # shallow copy
path.copy()             # shallow copy (equivalent)
list(path)              # shallow copy (equivalent)
"".join(path)           # build string from list of chars
sorted(nums)            # returns new sorted list
nums.sort()             # sorts in place
nums.sort(reverse=True) # sort descending
set(), frozenset()      # O(1) membership
from collections import Counter  # for multiplicity tracking
```

## 13.5 State-Space Summary Diagram

```
                         ┌────────────┐
                         │   ROOT     │  (empty/initial state)
                         └─────┬──────┘
                    choice1 ┌──┼──┐ choice2  ...
                            ▼     ▼
                       ┌────────┐ ┌────────┐
                       │ state1 │ │ state2 │   <- feasible (continue)
                       └───┬────┘ └───┬────┘
                     valid?│      invalid? -> PRUNE (dead end)
                           ▼
                       ┌────────┐
                       │ state1a│  ... continues until GOAL (leaf, save)
                       └────────┘      or DEAD END (leaf, discard)
```

---
# 14. Practice Problem Bank


## 14.1 Basics

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Subsets | LeetCode | Easy/Medium | Pick/Not-Pick |
| Binary Watch | LeetCode | Easy | Combination-style |
| Letter Case Permutation | LeetCode | Medium | Pick/Not-Pick |
| Power Set | GeeksforGeeks | Basic | Subset Generation |

## 14.2 Subsets

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Subsets | LeetCode | Medium | Distinct elements |
| Subsets II | LeetCode | Medium | Duplicate handling |
| Power Set | InterviewBit | Medium | Bitmask alternative comparison |

## 14.3 Subsequences

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Generate all subsequences of a string | GeeksforGeeks | Basic | Pick/Not-Pick on strings |
| Distinct Subsequences II | LeetCode | Hard | Combined with DP |

## 14.4 Combinations

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Combinations | LeetCode | Medium | Fixed-size selection |
| Combination Sum | LeetCode | Medium | Reuse allowed |
| Combination Sum II | LeetCode | Medium | No reuse + duplicates |
| Combination Sum III | LeetCode | Medium | Fixed count + fixed digit pool |
| Combination Sum IV | LeetCode | Medium | Actually a DP problem (order matters, counts only) — good "which technique?" test |

## 14.5 Permutations

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Permutations | LeetCode | Medium | Basic permutation |
| Permutations II | LeetCode | Medium | Duplicate handling |
| Next Permutation | LeetCode | Medium | NOT backtracking (iterative algorithm) — good contrast problem |
| Permutation Sequence | LeetCode | Hard | Mathematical (factorial number system), backtracking too slow at scale |

## 14.6 Partitioning

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Palindrome Partitioning | LeetCode | Medium | Partition pattern |
| Palindrome Partitioning II | LeetCode | Hard | DP preferred (min cuts) |
| Restore IP Addresses | LeetCode | Medium | Bounded partition |
| Partition to K Equal Sum Subsets | LeetCode | Medium/Hard | Bucket-filling backtracking |
| Matchsticks to Square | LeetCode | Medium | Special case of K-subsets (k=4) |

## 14.7 Grid Problems

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Word Search | LeetCode | Medium | Grid DFS backtracking |
| Word Search II | LeetCode | Hard | Trie + backtracking |
| Rat in a Maze | GeeksforGeeks / Code360 | Medium | All-paths grid backtracking |
| Unique Paths III | LeetCode | Hard | Must visit every empty cell exactly once |
| N-Queens | LeetCode | Hard | CSP grid placement |
| N-Queens II | LeetCode | Hard | Count-only variant |

## 14.8 String Problems

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Letter Combinations of a Phone Number | LeetCode | Medium | Mapping-based backtracking |
| Generate Parentheses | LeetCode | Medium | Constraint-pruned generation |
| Expression Add Operators | LeetCode | Hard | Operator precedence backtracking |
| Word Break II | LeetCode | Hard | Partition + dictionary constraint |

## 14.9 Constraint Satisfaction

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Sudoku Solver | LeetCode | Hard | Full CSP |
| Valid Sudoku | LeetCode | Medium | Constraint checking only (no solving) |
| Crossword Puzzle | GeeksforGeeks | Hard | Large-scale CSP |
| Graph Coloring | GeeksforGeeks | Medium | Classic CSP |

## 14.10 Advanced Backtracking

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Word Search II | LeetCode | Hard | Trie-optimized backtracking |
| The Knight's Tour | GeeksforGeeks | Hard | Hamiltonian path on a grid graph |
| Hamiltonian Path/Cycle | GeeksforGeeks | Hard | Graph backtracking (conceptual link only) |
| M-Coloring Problem | GeeksforGeeks | Medium | CSP variant of graph coloring |
| Rat in a Maze with multiple movements | Code360 | Medium | Extended grid backtracking |

## 14.11 Competitive Programming Judges

| Platform | Typical Backtracking Focus |
|---|---|
| Codeforces | Constructive/backtracking hybrid problems, often with heavy pruning requirements under tight time limits |
| CodeChef | Combinatorial search problems, sometimes combined with meet-in-the-middle |
| AtCoder | Clean, well-bounded backtracking/DFS problems, often bitmask-based |
| CSES (Introductory Problems / Search section) | "Chessboard and Queens," "Grid Paths," "Creating Strings" — canonical backtracking practice set |

---
# 15. Final Revision Kit

## 15.1 One-Page Notes

- Backtracking = DFS over a decision tree + **choose → explore → unchoose**.
- Every problem needs: **state, choices, constraints, goal**.
- **Prune before recursing**, not after.
- **Copy before saving** (`path[:]`), never save a live reference.
- **Undo every choice** exactly once, symmetric to how it was applied.
- Sort input whenever duplicates or bounding are involved.
- Distinguish **Generate All** (keep exploring after a hit) vs **Find One** (return immediately).

## 15.2 Mind Map (Textual)

```
BACKTRACKING
├── Core Idea: Choose → Explore → Unchoose
├── Patterns
│   ├── Pick/Not-Pick        → Subsets
│   ├── Start-Index Loop     → Combinations, Combination Sum
│   ├── Used[]/Swap          → Permutations
│   ├── Partition (cut point)→ Palindrome Partitioning, Restore IP
│   ├── Grid DFS             → Word Search, Rat in a Maze
│   └── CSP (Var/Domain/Constraint) → N-Queens, Sudoku
├── Pruning
│   ├── Constraint Check (before recursing)
│   ├── Bounding (feasibility check)
│   ├── Duplicate Skip (sort + adjacent-skip)
│   └── Early Termination (Find-One)
├── Python Gotchas
│   ├── path[:] on save
│   ├── mutable default args
│   └── recursion limit
└── Complexity
    ├── Subsets/Subsequences → 2^n
    ├── Permutations         → n!
    └── Combinations         → C(n,k)
```

## 15.3 Pattern Map (Quick Lookup)

| If the problem says... | Use this template base |
|---|---|
| "all subsets" | Pick/Not-Pick or start-index loop |
| "all permutations" | `used[]` array or swap-based |
| "k elements from n, order doesn't matter" | Start-index + bounding |
| "reach a sum, reuse allowed" | Start-index loop, recurse with same index |
| "split into valid pieces" | Cut-point loop (partition pattern) |
| "path through a grid" | 4-directional DFS + visited marking |
| "assign values under mutual constraints" | CSP: iterate empty variables, try domain values, check constraints |

## 15.4 State Space Template (Copy-Paste Starting Point)

```python
def solve(nums):
    result = []
    path = []

    def backtrack(start):
        # 1. GOAL CHECK
        if goal_condition(path):
            result.append(path[:])
            return

        # 2. TRY EVERY CHOICE
        for i in range(start, len(nums)):
            # 3. CONSTRAINT CHECK (pruning)
            if not is_valid(nums[i], path):
                continue

            # 4. CHOOSE
            path.append(nums[i])

            # 5. EXPLORE
            backtrack(i + 1)   # or `i` if reuse allowed, or `0`/other index scheme

            # 6. UNCHOOSE
            path.pop()

    backtrack(0)
    return result
```

## 15.5 Complexity Sheet (Condensed)

```
2^n   →  Subsets, Subsequences, Subset Sum
n!    →  Permutations, N-Queens (loose upper bound)
C(n,k)→  Combinations
k^n   →  Bucket/partition-style assignment (K subsets)
9^m   →  Sudoku (m = blank cells)
4^L   →  Grid word search (L = word length)
Catalan(n) → Generate Parentheses
```



## 15.7 1-Hour Revision

1. Re-derive and re-code (without looking): Subsets, Combinations, Permutations, Combination Sum, Generate Parentheses.
2. Solve N-Queens using sets for O(1) diagonal checks.
3. Solve Word Search with in-place board marking.
4. Solve Palindrome Partitioning, then optimize with a precomputed DP table.
5. Review the Common Mistakes table (§12) and confirm you haven't made any of them in your fresh code.
6. Time yourself solving one Medium and one Hard problem from the Practice Problem Bank (§14) under interview conditions (~25-40 minutes each).

---
# 16. FAQs

**Q1. What's the difference between backtracking and plain recursion?**
A: All backtracking is recursive, but not all recursion is backtracking. Backtracking specifically involves making a choice, recursing, and then **undoing** that choice to try alternatives — the "undo" step is the defining characteristic. Plain recursion (e.g., computing Fibonacci) doesn't need to undo anything.

**Q2. What's the difference between backtracking and DFS on a graph?**
A: DFS on a graph explores *reachability* between vertices/edges, typically visiting each node once. Backtracking explores a *decision tree* of choices, where the same "state" concept doesn't correspond to a fixed graph — it's built dynamically from the sequence of choices made, and undoing is essential to correctly explore siblings.

**Q3. When should I use backtracking instead of dynamic programming?**
A: Use backtracking when the problem asks you to **enumerate/generate all solutions** (or find one, or check existence) rather than just compute an optimal value or count. If the problem only wants a count, minimum/maximum value, or yes/no answer *and* has overlapping subproblems, DP is usually far more efficient (polynomial vs. exponential).

**Q4. Why does my backtracking solution return a list of empty lists / all-identical results?**
A: This is almost always the mutable-reference bug (§2.3) — you appended `path` instead of `path[:]` to your results list.

**Q5. How do I know if I need a `for` loop over `range(start, n)` vs. `range(n)` with a `used[]` array?**
A: Use `range(start, n)` when **order doesn't matter** (subsets, combinations) — this naturally avoids duplicates/reorderings. Use `range(n)` + `used[]` when **order matters** (permutations), since every element needs to appear in every position.

**Q6. How do I handle duplicates in the input array?**
A: Sort the array first, then skip a choice if it equals the previous choice **and** the previous choice is not "active" in the current path (see §5.6 and §6.4 for the precise conditions, which differ slightly between combination-style and permutation-style duplicate skipping).

**Q7. My backtracking solution times out (TLE) on larger inputs — what should I check first?**
A: In order: (1) Are you pruning **before** recursing, not just filtering results at the end? (2) Are you copying the board/path unnecessarily instead of mutating in place? (3) Have you sorted the input to enable bounding/`break` optimizations? (4) Is there a Find-One early-exit you're missing? (5) Could a DP/greedy/mathematical approach replace backtracking entirely for this specific ask?

**Q8. Is backtracking the same as brute force?**
A: Backtracking generalizes brute force — brute force *without* pruning is a valid (if inefficient) backtracking implementation. What makes backtracking valuable is pruning: cutting off invalid branches as early as possible.

**Q9. How deep can Python recursion go, and what happens if I exceed it?**
A: Python's default recursion limit is ~1000 frames (`sys.getrecursionlimit()`). Exceeding it raises `RecursionError`. You can raise the limit with `sys.setrecursionlimit()`, but this doesn't protect against the underlying C-stack limit — for very deep search spaces (e.g., very large `n`), consider an iterative backtracking implementation using an explicit stack instead.

**Q10. What's the difference between "Generate All" and "Find One," and why does it matter for code structure?**
A: "Generate All" keeps exploring every branch after recording a solution (no early return). "Find One" returns `True`/the solution immediately once found, and that `True` must **propagate up through every recursive call** via `if solve(...): return True` — forgetting this propagation is a common bug that silently turns a Find-One solver into one that explores far more of the tree than necessary (or one that fails to actually stop).

**Q11. Do I always need a `visited` array/set?**
A: Only when an element/cell could otherwise be reused illegally within a single candidate solution (permutations, grid paths, Sudoku placement checks via row/col/box sets). Problems like subsets/combinations use a `start` index instead, which achieves the same "don't reuse" effect without extra memory.

**Q12. How do I choose between recursion with a shared mutable `path` list vs. passing new lists each call?**
A: Shared mutable `path` + append/pop is the standard, efficient approach (O(1) choose/unchoose). Passing new lists each call (`backtrack(path + [x])`) avoids needing an explicit "undo" step but costs O(n) per call to build the new list — acceptable for small inputs, wasteful for large ones.

**Q13. Can backtracking be parallelized?**
A: Yes, in principle — independent branches of the state space tree can be explored concurrently (e.g., dispatching each top-level choice to a separate worker/process). This is uncommon in interview settings but relevant in real-world large-scale CSP solvers and competitive-programming contexts with multi-threading allowances.

**Q14. Why do some backtracking problems use `break` and others use `continue` when a choice is invalid?**
A: Use `break` when the input is **sorted** and you know every subsequent choice is *also* invalid for the same reason (e.g., Combination Sum: once `candidates[i] > remaining`, all later candidates are too, since sorted ascending). Use `continue` when an individual choice failing doesn't imply anything about the *next* choice (e.g., N-Queens: one column being attacked says nothing about the next column).

---
