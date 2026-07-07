# 🚀 The Complete Advanced Data Structures Handbook 



## 📖 Table of Contents

1. [Introduction to Advanced Data Structures](#1-introduction-to-advanced-data-structures)
2. [Segment Trees](#2-segment-trees)
3. [Fenwick Tree (Binary Indexed Tree)](#3-fenwick-tree-binary-indexed-tree)
4. [Sparse Table](#4-sparse-table)
5. [Skip List](#5-skip-list)
6. [Disjoint Set Union (Union-Find)](#6-disjoint-set-union-union-find)
7. [Self-Balancing Trees](#7-self-balancing-trees)
8. [B-Tree Family](#8-b-tree-family)
9. [Interval Structures](#9-interval-structures)
10. [Range Query Structures — Unified Comparison](#10-range-query-structures--unified-comparison)
11. [Spatial Data Structures](#11-spatial-data-structures)
12. [String-Oriented Advanced Structures](#12-string-oriented-advanced-structures)
13. [Cache & Memory Structures](#13-cache--memory-structures)
14. [Randomized Structures](#14-randomized-structures)
15. [Advanced Graph-Oriented Structures](#15-advanced-graph-oriented-structures)
16. [Competitive Programming Structures](#16-competitive-programming-structures)
17. [Advanced Concepts](#17-advanced-concepts)
18. [Real-World Applications](#18-real-world-applications)
19. [Problem Recognition Guide](#19-problem-recognition-guide)
20. [Complexity Comparison — Master Tables](#20-complexity-comparison--master-tables)
21. [Python Tips for Advanced DS](#21-python-tips-for-advanced-ds)
22. [Common Mistakes Compendium](#22-common-mistakes-compendium)
23. [Cheat Sheets](#23-cheat-sheets)
24. [Practice Problems](#24-practice-problems)
25. [Final Revision Kit](#25-final-revision-kit)

---

## 1. Introduction to Advanced Data Structures

### 1.1 What Are Advanced Data Structures?

Basic data structures (arrays, lists, stacks, queues, basic trees) answer the question: *"How do I store data?"*
Advanced data structures answer a harder question: *"How do I store data so that a whole **class** of expensive operations becomes cheap — even as the data changes?"*

They typically trade a bit of memory or preprocessing time for **asymptotically better** query/update performance on patterns like:

- Range queries (sum, min, max, gcd) over a mutable array
- Dynamic connectivity between elements
- Ordered operations (rank, k-th smallest) in logarithmic time
- Nearest-neighbor / spatial search
- Prefix/pattern matching over strings
- Efficient caching with eviction policies

### 1.2 Why They Exist

| Naive Approach | Problem | Advanced Structure That Fixes It |
|---|---|---|
| Recompute sum over a range every query — O(n) | Too slow for many queries | Segment Tree / Fenwick Tree — O(log n) |
| Linear search for min in range | O(n) per query | Sparse Table — O(1) per query (static) |
| Re-run BFS/DFS to check connectivity after each edge | O(n) per check | DSU — nearly O(1) amortized |
| Linked list search | O(n) | Skip List — O(log n) expected |
| Unbalanced BST degrades to O(n) | Adversarial insert order | AVL / Red-Black / Treap — O(log n) guaranteed |
| Disk-based B-tree-less index | Too many disk seeks | B-Tree/B+ Tree — minimizes disk I/O |

### 1.3 Evolution Timeline

```
1962 ── AVL Tree (Adelson-Velsky & Landis) — first self-balancing BST
1970 ── B-Tree (Bayer & McCreight) — disk-friendly balanced tree
1972 ── Red-Black Tree — relaxed balancing, used in libraries/OS
1975 ── Segment Tree ideas emerge in computational geometry
1978 ── Fenwick-like prefix structures precursors
1989 ── Fenwick Tree (Peter Fenwick) — compact BIT
1989 ── Skip List (William Pugh) — probabilistic alternative to balanced trees
1996 ── Treap popularized (randomized BST + heap)
2000s ─ Persistent & functional data structures gain traction (Clojure, Haskell)
2010s ─ Succinct & cache-oblivious structures rise with big data era
```

### 1.4 Choosing the Right Data Structure — Trade-off Philosophy

Every advanced data structure sits somewhere on these axes:

```
        Query Speed
             ▲
             │   Sparse Table (O(1), static only)
             │
             │   Segment Tree / Fenwick (O(log n), dynamic)
             │
             │   Sqrt Decomposition (O(√n), simple, dynamic)
             │
             └──────────────────────────────► Update Flexibility
         (static data)                 (fully dynamic data)
```

**Golden Rule:** *Ask three questions before picking a structure:*
1. Is the data static or dynamic (updates allowed)?
2. What operation dominates: point query, range query, or both?
3. Do I need persistence (access old versions) or just the latest state?

> 💡 **Tip:** In interviews, saying *"this is a range-update, range-query problem, so I'll use a Segment Tree with lazy propagation"* before writing code demonstrates structured thinking — a huge signal to interviewers.

### 1.5 Real-World Examples Preview

| Structure | Real-World Use |
|---|---|
| B+ Tree | MySQL/PostgreSQL indexes |
| Segment Tree | Competitive programming range queries, GIS |
| Skip List | Redis sorted sets |
| Bloom Filter | Chrome Safe Browsing, Cassandra, Bitcoin |
| LRU Cache | OS page replacement, CPU caches |
| Treap | CP balanced BST alternative |
| KD-Tree | Nearest neighbor search, ML libraries |
| Suffix Array | Bioinformatics (genome search), text editors |
| Rope | Text editors (VS Code, Word) for huge documents |

---
## 2. Segment Trees

### 2.1 Definition

A **Segment Tree** is a binary tree where each node represents an aggregate (sum, min, max, gcd, etc.) over a **contiguous range** (segment) of an underlying array. The root represents the whole array; each leaf represents a single element.

### 2.2 Why It Exists / Problem It Solves

Given an array `A[0..n-1]`, support:
- `query(l, r)` — aggregate over `A[l..r]`
- `update(i, val)` — change a single element (or a range)

A naive array gives O(1) update but O(n) query. A prefix-sum array gives O(1) query but O(n) update. **Segment Tree gives O(log n) for both.**

### 2.3 Intuition & Real-World Analogy

Think of a company's org chart used for computing total headcount:
- CEO node = total company headcount
- VP nodes = headcount of their division
- Manager nodes = headcount of their team
- Employee (leaf) = 1

To get headcount of "Engineering", you don't count every employee — you read the pre-aggregated VP-Engineering number. If one employee joins, only the chain from that employee up to the CEO needs updating — **O(log n)** nodes, not all `n`.

### 2.4 ASCII Visualization (Sum Segment Tree over `[1,3,5,7,9,11]`)

```
Array index:      0   1   2   3   4   5
Array value:      1   3   5   7   9  11

                         [0..5]=36
                        /          \
                 [0..2]=9          [3..5]=27
                /       \          /        \
          [0..1]=4   [2..2]=5  [3..4]=16   [5..5]=11
          /    \                /    \
     [0..0]=1 [1..1]=3     [3..3]=7 [4..4]=9
```

Each internal node stores the sum of its two children's ranges, built bottom-up in O(n).

### 2.5 Internal Working & Memory Representation

Two common implementations:
1. **Array-based (1-indexed, size `4*n`)** — simplest, cache-friendly, used in most CP code.
2. **Node/pointer-based** — flexible (dynamic/persistent trees) but more memory overhead due to Python object headers.

```
Array-based memory layout (1-indexed):
tree[1]         -> root, range [0, n-1]
tree[2*i]       -> left child of node i
tree[2*i+1]     -> right child of node i
```

### 2.6 Python Implementation — Recursive Segment Tree (Range Sum, Point Update)

```python
class SegmentTree:
    """
    Recursive Segment Tree supporting:
    - Point update: O(log n)
    - Range sum query: O(log n)
    1-indexed internal tree array of size 4*n (safe upper bound).
    """
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.arr = arr
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        mid = (start + end) // 2
        left, right = 2 * node, 2 * node + 1
        self._build(left, start, mid)
        self._build(right, mid + 1, end)
        self.tree[node] = self.tree[left] + self.tree[right]

    def update(self, idx, value):
        self._update(1, 0, self.n - 1, idx, value)

    def _update(self, node, start, end, idx, value):
        if start == end:
            self.arr[idx] = value
            self.tree[node] = value
            return
        mid = (start + end) // 2
        left, right = 2 * node, 2 * node + 1
        if idx <= mid:
            self._update(left, start, mid, idx, value)
        else:
            self._update(right, mid + 1, end, idx, value)
        self.tree[node] = self.tree[left] + self.tree[right]

    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0                      # out of range
        if l <= start and end <= r:
            return self.tree[node]        # fully inside range
        mid = (start + end) // 2
        left, right = 2 * node, 2 * node + 1
        return (self._query(left, start, mid, l, r) +
                self._query(right, mid + 1, end, l, r))
```

### 2.7 Line-by-Line Explanation

- `self.tree = [0]*(4*n)` — 4n is a safe upper bound for a recursive segment tree array size.
- `_build` recursively splits `[start,end]` into halves until `start==end` (a leaf), then combines children on the way back up.
- `_update` walks down to the leaf that needs to change, then recomputes every ancestor's aggregate on the way back up.
- `_query` has 3 cases: no overlap (return identity, `0` for sum), total overlap (return the precomputed node value directly), partial overlap (recurse both sides and combine).

### 2.8 Complete Dry Run

Array: `[1, 3, 5, 7, 9, 11]`, build tree, then `update(1, 10)`, then `query(1, 4)`.

| Step | Structure State | Operation | Result | Explanation |
|---|---|---|---|---|
| 1 | leaves = [1,3,5,7,9,11] | build | tree[1]=36 | Root sums entire array |
| 2 | tree[2]=9 ([0..2]), tree[3]=27 ([3..5]) | build internal | — | Post-order combine |
| 3 | idx=1 old=3 new=10 | update(1,10) | descend to leaf idx=1 | path: node1 to node2 to node4(leaf 1) |
| 4 | tree[4]=10 (was 3) | leaf updated | — | direct assignment |
| 5 | tree[2] = tree[4]+tree[5] = 10+5 = 15 | ascend | tree[2]=15 | recombine parent |
| 6 | tree[1] = tree[2]+tree[3] = 15+27 = 42 | ascend | tree[1]=42 | recombine root |
| 7 | query(1,4) over updated array [1,10,5,7,9,11] | query(1,0,5,1,4) | partial overlap, recurse | mid=2 |
| 8 | left=query(node2,0,2,1,4) | partial overlap | recurse node4([1,1]) fully + node5([2,2]) fully | 10+5=15 |
| 9 | right=query(node3,3,5,1,4) | partial overlap | recurse node6([3,4]) fully=7+9=16, node7([5,5]) no overlap=0 | 16 |
| 10 | total = 15 + 16 | combine | 31 | matches 10+5+7+9=31 correct |

### 2.9 Time & Space Complexity

| Operation | Time | Space |
|---|---|---|
| Build | O(n) | O(n) (up to 4n) |
| Point Update | O(log n) | O(log n) recursion stack |
| Range Query | O(log n) | O(log n) recursion stack |

### 2.10 Edge Cases
- Empty array (n=0) - guard before building.
- Single element array - tree has just one leaf, root = leaf.
- Query range fully outside array bounds - should return identity element.
- l > r in query (invalid range) - validate before calling.

### 2.11 Common Mistakes
- Using 4n incorrectly for non-recursive/iterative trees (iterative only needs 2n).
- Forgetting the identity element differs per operation: 0 for sum, +inf for min, -inf for max, 1 for product.
- Off-by-one errors mixing inclusive/exclusive range conventions.
- Not updating self.arr[idx] alongside tree[node] when other code depends on the raw array.

### 2.12 Interview Tips
- Always clarify: "Is this range-sum, range-min, or a custom associative operation?"
- Mention iterative (bottom-up) segment trees as an optimization for competitive programming.
- If asked for range update, immediately mention lazy propagation.

---

### 2.13 Range Update with Lazy Propagation

**Problem it solves:** naive range update (looping to update every index in [l,r]) is O(n) per update. Lazy propagation defers updates to child nodes until they're actually needed, achieving O(log n) range updates.

#### Intuition
Don't do work you don't have to do yet, but leave a "sticky note" (lazy[node]) so you remember to do it when someone actually visits that node.

#### ASCII Visualization — Lazy Propagation

```
Before range update add(+5) to range [2,4]:

           [0..5]
          /       \
     [0..2]        [3..5]
     /    \         /    \
 [0..1] [2..2]  [3..4]  [5..5]

During update(2,4,+5): node [2..2] fully inside -> add 5 (leaf, no children)
                       node [3..4] fully inside -> add to sum, set lazy[node]=+5 (defer to children)
                       node [5..5] outside -> skip

After: [3..4]'s sum reflects +5*2, but children [3..3] and [4..4] are NOT yet updated.
They will be updated (pushed down) only when a future query/update visits them.
```

#### Python Implementation — Range Sum with Range Update (Lazy Propagation)

```python
class LazySegmentTree:
    """
    Supports:
    - Range update: add `val` to every element in [l, r] -> O(log n)
    - Range sum query over [l, r] -> O(log n)
    """
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.arr = arr
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _push_down(self, node, start, end):
        """Propagate pending lazy value to children before descending further."""
        if self.lazy[node] != 0:
            mid = (start + end) // 2
            left, right = 2 * node, 2 * node + 1
            self.tree[left] += self.lazy[node] * (mid - start + 1)
            self.tree[right] += self.lazy[node] * (end - mid)
            self.lazy[left] += self.lazy[node]
            self.lazy[right] += self.lazy[node]
            self.lazy[node] = 0

    def update_range(self, l, r, val):
        self._update_range(1, 0, self.n - 1, l, r, val)

    def _update_range(self, node, start, end, l, r, val):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.tree[node] += val * (end - start + 1)
            self.lazy[node] += val
            return
        self._push_down(node, start, end)
        mid = (start + end) // 2
        self._update_range(2 * node, start, mid, l, r, val)
        self._update_range(2 * node + 1, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        self._push_down(node, start, end)
        mid = (start + end) // 2
        return (self._query(2 * node, start, mid, l, r) +
                self._query(2 * node + 1, mid + 1, end, l, r))
```

#### Line-by-Line Explanation
- lazy[node] stores a pending "add" that applies to the entire subtree rooted at node, but hasn't been pushed to children yet.
- _push_down is called before recursing into children — it applies the pending update to both children, then clears the current node's lazy.
- _update_range and _query both call _push_down because both need accurate child values before descending.

#### Dry Run

| Step | Operation | Node Visited | Effect | Explanation |
|---|---|---|---|---|
| 1 | update_range(2,4,+5) on [1,3,5,7,9,11] | node1 [0..5] | partial | recurse |
| 2 | | node2 [0..2] | partial overlap w/ [2,4] | recurse into children |
| 3 | | node5 [2..2] | fully inside [2,4] | tree[5]=5+5=10 (leaf) |
| 4 | | node3 [3..5] | partial overlap | push_down node3, then recurse |
| 5 | | node6 [3..4] | fully inside [2,4] | tree[6]+=5*2 -> 26, lazy[6]=5 (deferred) |
| 6 | | node7 [5..5] | outside [2,4] | untouched |
| 7 | query(3,3) | node6 [3..4] | must push down first | tree[12]+=5, tree[13]+=5, lazy[6]=0 |
| 8 | | node12 [3..3] | 7+5=12 | returns 12 (matches expected) |

#### Complexity
| Operation | Time | Space |
|---|---|---|
| Range Update | O(log n) | O(log n) |
| Range Query | O(log n) | O(4n) total |

#### Common Mistakes
- Forgetting to multiply lazy value by segment length for sum aggregates (min/max just add value directly).
- Not clearing lazy[node] to 0 after pushing down - causes double-application bugs.
- Calling query/update without pushing down first - leads to stale/incorrect subtree sums.

---

### 2.14 Iterative (Bottom-Up) Segment Tree

**Why:** Avoids recursion overhead - faster constant factor, popular in CP for point-update/range-query without lazy propagation.

```python
class IterativeSegmentTree:
    """Iterative segment tree - point update, range sum query. Size = 2*n."""
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, idx, value):
        idx += self.n
        self.tree[idx] = value
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def query(self, l, r):
        """Sum over [l, r] inclusive."""
        res = 0
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res
```

> Note: Leaves live at indices [n, 2n-1]. Parent of i is i//2. This layout is cache-friendly because it's a flat array with no pointers.

### 2.15 Dynamic Segment Tree (Overview)

Used when the index range is huge (e.g., 1e9) but the number of updates/queries is small. Nodes are created on demand using object pointers instead of pre-allocating 4n.

```python
class DynamicSegTreeNode:
    __slots__ = ('left', 'right', 'val')
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0

class DynamicSegmentTree:
    """Handles ranges up to 1e9 by lazily creating nodes only where touched."""
    def __init__(self, lo, hi):
        self.lo, self.hi = lo, hi
        self.root = DynamicSegTreeNode()

    def update(self, idx, val):
        self._update(self.root, self.lo, self.hi, idx, val)

    def _update(self, node, lo, hi, idx, val):
        if lo == hi:
            node.val += val
            return
        mid = (lo + hi) // 2
        if idx <= mid:
            if not node.left:
                node.left = DynamicSegTreeNode()
            self._update(node.left, lo, mid, idx, val)
        else:
            if not node.right:
                node.right = DynamicSegTreeNode()
            self._update(node.right, mid + 1, hi, idx, val)
        node.val = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)

    def query(self, node, lo, hi, l, r):
        if node is None or r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return node.val
        mid = (lo + hi) // 2
        return (self.query(node.left, lo, mid, l, r) +
                self.query(node.right, mid + 1, hi, l, r))
```

**Applications:** counting inversions with huge value ranges, coordinate-compressed alternatives when compression isn't feasible online.

### 2.16 Persistent Segment Tree (Overview)

**Definition:** Keeps a version history - every update creates O(log n) new nodes (the path from root to the changed leaf) while reusing all unchanged subtrees from the previous version.

```python
class PersistentNode:
    __slots__ = ('left', 'right', 'val')
    def __init__(self, left=None, right=None, val=0):
        self.left, self.right, self.val = left, right, val

class PersistentSegmentTree:
    """Each update returns a NEW root; old roots remain queryable."""
    def __init__(self, arr):
        self.n = len(arr)
        self.versions = [self._build(0, self.n - 1, arr)]

    def _build(self, lo, hi, arr):
        if lo == hi:
            return PersistentNode(val=arr[lo])
        mid = (lo + hi) // 2
        left = self._build(lo, mid, arr)
        right = self._build(mid + 1, hi, arr)
        return PersistentNode(left, right, left.val + right.val)

    def update(self, version, idx, val):
        new_root = self._update(self.versions[version], 0, self.n - 1, idx, val)
        self.versions.append(new_root)
        return len(self.versions) - 1

    def _update(self, node, lo, hi, idx, val):
        if lo == hi:
            return PersistentNode(val=val)
        mid = (lo + hi) // 2
        if idx <= mid:
            new_left = self._update(node.left, lo, mid, idx, val)
            return PersistentNode(new_left, node.right, new_left.val + node.right.val)
        else:
            new_right = self._update(node.right, mid + 1, hi, idx, val)
            return PersistentNode(node.left, new_right, node.left.val + new_right.val)

    def query(self, version, lo, hi, l, r, node=None):
        node = node or self.versions[version]
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return node.val
        mid = (lo + hi) // 2
        return (self.query(version, lo, mid, l, r, node.left) +
                self.query(version, mid + 1, hi, l, r, node.right))
```

**Applications:** K-th smallest in range, version-controlled arrays, offline queries on historical states.

### 2.17 2D Segment Tree (Overview)

A segment tree of segment trees - outer tree indexed by row, each node holding an inner segment tree indexed by column. Supports 2D range sum/min queries in O(log n * log m). Rare in interviews; common in CP problems tagged "2D range query".

### 2.18 Merge Sort Tree (Overview)

Each segment tree node stores a sorted copy of the elements in its range. Enables "count elements <= X in range [l,r]" via binary search at each visited node - O(log^2 n) per query.

```python
import heapq
import bisect

class MergeSortTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [[] for _ in range(4 * self.n)]
        self._build(1, 0, self.n - 1, arr)

    def _build(self, node, start, end, arr):
        if start == end:
            self.tree[node] = [arr[start]]
            return
        mid = (start + end) // 2
        self._build(2*node, start, mid, arr)
        self._build(2*node+1, mid+1, end, arr)
        self.tree[node] = list(heapq.merge(self.tree[2*node], self.tree[2*node+1]))

    def count_leq(self, l, r, x):
        return self._query(1, 0, self.n - 1, l, r, x)

    def _query(self, node, start, end, l, r, x):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return bisect.bisect_right(self.tree[node], x)
        mid = (start + end) // 2
        return (self._query(2*node, start, mid, l, r, x) +
                self._query(2*node+1, mid+1, end, l, r, x))
```
**Applications:** "count numbers <= K in range [l,r]", offline order-statistics queries.

### 2.19 Segment Tree Beats (Overview)

An advanced variant supporting operations like "range chmin" in amortized O(log^2 n) using extra bookkeeping (max, second-max, count-of-max per node). Rarely needed outside Div-1 Codeforces problems - research-level overview only.

### 2.20 Segment Tree — Variations Summary Table

| Variant | Extra Capability | Extra Cost |
|---|---|---|
| Basic recursive | Point update, range query | O(4n) space |
| Iterative | Same, faster constant factor | O(2n) space |
| Lazy propagation | Range update, range query | +O(n) lazy array |
| Dynamic | Huge index ranges | Node allocation overhead |
| Persistent | Version history queries | O(log n) new nodes/update |
| 2D | 2D range queries | O(n*m) space |
| Merge Sort Tree | Order-statistics in range | O(n log n) space |
| Segment Tree Beats | Range chmin/chmax | Amortized log-squared complexity |

### 2.21 Applications
- Range sum/min/max/gcd queries (CP staple)
- Range update + range query (lazy propagation)
- Counting inversions
- K-th order statistic in a range (merge sort tree / persistent tree)
- 2D range queries (image processing, GIS grids)

### 2.22 Practice Problems (Segment Tree)
| Problem | Platform | Difficulty |
|---|---|---|
| Range Minimum Query | CSES | Easy |
| Range Update Queries | CSES | Medium |
| Range Sum Query - Mutable | LeetCode 307 | Medium |
| Falling Squares | LeetCode 699 | Hard |
| Count of Smaller Numbers After Self | LeetCode 315 | Hard |
| Chef and Segments | CodeChef | Medium |

### 2.23 Summary & Revision Notes
- Segment Tree = precomputed tree of aggregates over ranges.
- O(log n) point update & range query; O(log n) range update with lazy propagation.
- Identity element depends on the operation (0 for sum, infinity/-infinity for min/max).
- Use iterative version for CP speed; recursive for readability/lazy propagation.
- Persistent version = version-controlled segment tree (each update is a new "commit").

---
## 3. Fenwick Tree (Binary Indexed Tree)

### 3.1 Definition
A **Fenwick Tree (BIT)** is a compact array-based structure that maintains prefix aggregates (usually sums) allowing both point updates and prefix queries in O(log n), using only O(n) space with a much smaller constant factor than a segment tree.

### 3.2 Why It Exists
Segment trees solve the same problem but use 4n space and are conceptually heavier. BIT exploits the **binary representation of indices** to store partial sums in a way that both update and query touch only O(log n) array cells — with a compact single array and no recursion needed for the common sum case.

### 3.3 Intuition & Real-World Analogy
Think of denominations of currency: to make any amount you combine powers-of-2-sized "bins." Each BIT index `i` is responsible for a range whose length equals the lowest set bit of `i` (`i & -i`). Moving to the parent/next responsible index means adding or subtracting that lowest set bit.

### 3.4 ASCII Visualization

```
Array (1-indexed): A[1..8] = [3, 2, -1, 6, 5, 4, -3, 3]

BIT responsibility ranges (lowest set bit determines range length):
tree[1] -> A[1]            (i&-i = 1)
tree[2] -> A[1..2]         (i&-i = 2)
tree[3] -> A[3]            (i&-i = 1)
tree[4] -> A[1..4]         (i&-i = 4)
tree[5] -> A[5]            (i&-i = 1)
tree[6] -> A[5..6]         (i&-i = 2)
tree[7] -> A[7]            (i&-i = 1)
tree[8] -> A[1..8]         (i&-i = 8)

Update path for index 3: 3 -> 4 -> 8         (i += i & -i)
Query (prefix sum) path for index 6: 6 -> 4 -> 0  (i -= i & -i)
```

### 3.5 Internal Working & Memory Representation
BIT is a single flat array of size `n+1` (1-indexed; index 0 unused). No pointers, no child/parent object references — just index arithmetic using `i & -i` (two's complement trick to isolate the lowest set bit).

### 3.6 Python Implementation

```python
class FenwickTree:
    """
    1-indexed Binary Indexed Tree.
    Supports:
      - update(i, delta): add delta to A[i]      -> O(log n)
      - prefix_sum(i): sum of A[1..i]            -> O(log n)
      - range_sum(l, r): sum of A[l..r]          -> O(log n)
    """
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)          # move to next responsible index

    def prefix_sum(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)          # move to parent responsible index
        return result

    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

    @classmethod
    def build(cls, arr):
        """Build in O(n) from a 0-indexed array."""
        bit = cls(len(arr))
        for i, val in enumerate(arr, start=1):
            bit.update(i, val)
        return bit
```

### 3.7 Line-by-Line Explanation
- `i & (-i)` isolates the lowest set bit of `i` using two's complement (e.g., `6 = 0b110`, `-6` in two's complement flips+adds 1, `6 & -6 = 0b010 = 2`).
- `update`: adds `delta` to `tree[i]`, then jumps to the next index that also "covers" position `i` by adding the lowest set bit — climbing up the implicit tree.
- `prefix_sum`: accumulates `tree[i]` then subtracts the lowest set bit to jump to the previous non-overlapping range — walking down the implicit tree.
- `range_sum(l, r) = prefix_sum(r) - prefix_sum(l-1)` — classic prefix-sum subtraction trick.

### 3.8 Complete Dry Run

Array (1-indexed): `A = [_, 3, 2, -1, 6, 5, 4, -3, 3]` (index 0 unused). Build BIT, then `update(3, +2)`, then `range_sum(2, 6)`.

| Step | Operation | Index Path | tree[] State | Explanation |
|---|---|---|---|---|
| 1 | build: update(1,3) | i=1→2→4→8 | tree[1]+=3, tree[2]+=3, tree[4]+=3, tree[8]+=3 | 1&-1=1, 2&-2=2, 4&-4=4 |
| 2 | build: update(2,2) | i=2→4→8 | tree[2]+=2, tree[4]+=2, tree[8]+=2 | |
| 3 | ... (continues for all 8 elements) | | | |
| 4 | update(3, +2) | i=3→4→8 | tree[3]+=2, tree[4]+=2, tree[8]+=2 | A[3] changes -1 → 1 |
| 5 | range_sum(2,6) = prefix_sum(6) - prefix_sum(1) | prefix(6): i=6→4→0 | tree[6]+tree[4] | 6&-6=2, 4&-4=4 |
| 6 | prefix_sum(1): i=1→0 | tree[1] | | |
| 7 | Final result | | sum of A[2..6] = 2+1+6+5+4 = 18 | matches direct computation ✅ |

### 3.9 Time & Space Complexity

| Operation | Time | Space |
|---|---|---|
| Build (via n updates) | O(n log n) — or O(n) with linear build trick | O(n) |
| Point Update | O(log n) | O(1) |
| Prefix Sum Query | O(log n) | O(1) |
| Range Sum Query | O(log n) | O(1) |

> 💡 **Optimization:** A true O(n) build exists: `tree[i] += tree[i - (i & -i)]` isn't quite it — the real linear build initializes `tree[i] = arr[i]` then propagates: `for i in range(1, n+1): parent = i + (i & -i); if parent <= n: tree[parent] += tree[i]`.

### 3.10 Edge Cases
- 1-indexing is mandatory — index 0 breaks the `i & -i` logic (infinite loop since `0 & -0 = 0`).
- Negative deltas work fine (subtraction is just update with `-delta`).
- Range sum with `l=1` requires `prefix_sum(0)` which correctly returns 0 (loop doesn't execute).

### 3.11 Common Mistakes
- ❌ Using 0-indexing directly without converting to 1-indexed internally.
- ❌ Forgetting `i & -i` requires Python's arbitrary-precision two's complement semantics (works fine in Python, but differs from fixed-width C++ behavior — worth understanding for cross-language correctness).
- ❌ Confusing BIT (prefix-sum only, no arbitrary range without subtraction) with Segment Tree (any associative range op directly).

### 3.12 Range Update + Range Query BIT (Two BITs Trick)

**Problem it solves:** Standard BIT only supports point update + range query. To support **range update + range query**, maintain two BITs using the identity:

```
prefix_sum(i) = i * BIT1.prefix_sum(i) - BIT2.prefix_sum(i)
```

```python
class RangeUpdateRangeQueryBIT:
    """Supports range update (add val to [l,r]) and range sum query [l,r]."""
    def __init__(self, n):
        self.n = n
        self.bit1 = FenwickTree(n)   # tracks the "delta" applied
        self.bit2 = FenwickTree(n)   # tracks delta * (index - 1) correction

    def _update(self, bit, i, delta):
        bit.update(i, delta)

    def range_update(self, l, r, val):
        self.bit1.update(l, val)
        self.bit1.update(r + 1, -val)
        self.bit2.update(l, val * (l - 1))
        self.bit2.update(r + 1, -val * r)

    def _prefix_sum(self, i):
        return i * self.bit1.prefix_sum(i) - self.bit2.prefix_sum(i)

    def range_sum(self, l, r):
        return self._prefix_sum(r) - self._prefix_sum(l - 1)
```

**Dry Run (concept):** `range_update(2,4,+5)` on array of size 8 sets `bit1` deltas at 2 (+5) and 5 (-5), representing "add 5 starting at index 2, cancel it starting at index 5." The correction term in `bit2` fixes the linear term so `prefix_sum` gives the correct cumulative total, not just a flat +5 for every index beyond 4.

### 3.13 Coordinate Compression (Companion Technique)

**Why:** BIT/Segment Tree indices must be small and dense (`0..n`). When values are huge or sparse (e.g., up to `10^9`), compress them to ranks `0..k-1`.

```python
def coordinate_compress(values):
    """Map each value to its rank among sorted unique values. O(n log n)."""
    sorted_unique = sorted(set(values))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}  # 1-indexed for BIT
    return [rank[v] for v in values], sorted_unique
```

**Applications:** counting inversions with values up to 1e9, offline range queries over huge coordinate spaces.

### 3.14 2D BIT (Binary Indexed Tree)

**Why:** Extends prefix sums to 2D grids — point update, 2D prefix/range sum query, both in `O(log n · log m)`.

```python
class BIT2D:
    """2D Fenwick Tree for point update + 2D range sum query."""
    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]

    def update(self, r, c, delta):
        i = r
        while i <= self.rows:
            j = c
            while j <= self.cols:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def prefix_sum(self, r, c):
        result = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                result += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return result

    def range_sum(self, r1, c1, r2, c2):
        """Sum of the rectangle [r1..r2] x [c1..c2] using inclusion-exclusion."""
        return (self.prefix_sum(r2, c2) - self.prefix_sum(r1 - 1, c2)
                - self.prefix_sum(r2, c1 - 1) + self.prefix_sum(r1 - 1, c1 - 1))
```

**Applications:** 2D range sum in image processing, spreadsheet range sums, matrix update problems.

### 3.15 Fenwick Tree vs Segment Tree — Head-to-Head

| Aspect | Fenwick Tree (BIT) | Segment Tree |
|---|---|---|
| Space | O(n) | O(4n) |
| Code complexity | Very simple (~15 lines) | More complex |
| Supported operations | Prefix sum natively; any invertible group op (sum, XOR) | Any associative op incl. non-invertible (min, max, gcd) |
| Range update + range query | Needs "two BITs" trick | Native via lazy propagation |
| Constant factor | Very fast | Slightly slower (more overhead) |
| Persistence / 2D extension | Harder | More natural to extend |

> ⚠️ **Warning:** BIT cannot directly support **min/max range queries with updates** because those operations aren't invertible (you can't "subtract" a min). Use Segment Tree or Sparse Table (static) instead.

### 3.16 Applications
- Counting inversions in an array
- Frequency tables / rank queries (order statistics)
- Range sum with point updates in competitive programming
- 2D range sums (image integral images, grid problems)

### 3.17 Practice Problems (Fenwick Tree)
| Problem | Platform | Difficulty |
|---|---|---|
| Range Sum Query - Mutable | LeetCode 307 | Medium |
| Count of Smaller Numbers After Self | LeetCode 315 | Hard |
| Range Update Queries | CSES | Medium |
| Static Range Sum Queries | CSES | Easy |
| Reverse Pairs | LeetCode 493 | Hard |

### 3.18 Summary & Revision Notes
- BIT = compact prefix-sum structure exploiting `i & -i` bit tricks.
- O(log n) point update, O(log n) prefix/range sum query, O(n) space.
- Only works for **invertible** operations (sum, XOR) natively — not min/max.
- Range update + range query needs the "two BIT" trick.
- Simpler and faster in practice than segment trees for pure sum problems.

---
## 4. Sparse Table

### 4.1 Definition
A **Sparse Table** is a static (immutable) data structure that answers **idempotent** range queries (min, max, gcd, AND, OR) in **O(1)** after O(n log n) preprocessing. It cannot handle updates efficiently — rebuilding is O(n log n).

### 4.2 Why It Exists
For static arrays, Segment Trees give O(log n) queries — great, but Sparse Table gives **O(1)**, which matters when you have millions of queries (e.g., LCA via RMQ, competitive programming with `10^6` queries).

### 4.3 Intuition & Real-World Analogy
Precompute the answer for **every range whose length is a power of two**, starting at every position. Any query range `[l, r]` can be covered by **two overlapping power-of-two ranges** — and because the operation is idempotent (applying it to overlapping data doesn't change the result, e.g. `min(min(A), min(A)) = min(A)`), overlap doesn't cause incorrect double-counting.

### 4.4 ASCII Visualization

```
Array: [4, 2, 6, 1, 9, 3, 5, 8]   (n = 8)

sparse[0][i] = A[i]                         (length 1)
sparse[1][i] = min(A[i], A[i+1])            (length 2)
sparse[2][i] = min(A[i..i+3])               (length 4)
sparse[3][i] = min(A[i..i+7])               (length 8)

Query min(2, 6) [length 5]:
    Largest power of 2 <= 5 is 4 (k=2)
    Cover with sparse[2][2] (covers [2,5]) and sparse[2][3] (covers [3,6])
    Overlap at [3,5] is fine because min is idempotent.
    answer = min(sparse[2][2], sparse[2][3])
```

### 4.5 Python Implementation

```python
import math

class SparseTable:
    """
    Static RMQ (min) sparse table.
    Preprocessing: O(n log n)
    Query: O(1)
    Works for any idempotent, associative operation (min, max, gcd, and, or).
    """
    def __init__(self, arr, op=min):
        self.n = len(arr)
        self.op = op
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        k = self.log[self.n] + 1
        self.table = [[0] * self.n for _ in range(k)]
        self.table[0] = list(arr)
        for j in range(1, k):
            length = 1 << j
            half = 1 << (j - 1)
            for i in range(self.n - length + 1):
                self.table[j][i] = op(self.table[j - 1][i], self.table[j - 1][i + half])

    def query(self, l, r):
        """Query over inclusive range [l, r], 0-indexed."""
        j = self.log[r - l + 1]
        return self.op(self.table[j][l], self.table[j][r - (1 << j) + 1])
```

### 4.6 Line-by-Line Explanation
- `self.log[i]` precomputes `floor(log2(i))` for O(1) lookup during queries instead of calling `math.log2` (avoids floating-point errors).
- `table[j][i]` stores the result of the operation over the range `[i, i + 2^j - 1]`.
- Build: `table[j][i] = op(table[j-1][i], table[j-1][i + 2^(j-1)])` — combine two half-length ranges.
- Query: pick `j = floor(log2(length))`, then combine `table[j][l]` (covers `[l, l+2^j-1]`) and `table[j][r-2^j+1]` (covers `[r-2^j+1, r]`) — these two ranges together fully cover `[l,r]`, possibly overlapping, which is fine since `op` is idempotent.

### 4.7 Complete Dry Run

Array: `[4, 2, 6, 1, 9, 3, 5, 8]`, query `min(1, 5)` (0-indexed, inclusive).

| Step | j (level) | table[j] content (partial) | Explanation |
|---|---|---|---|
| 1 | j=0 | [4,2,6,1,9,3,5,8] | raw array |
| 2 | j=1 | table[1][1]=min(2,6)=2 | length-2 ranges |
| 3 | j=2 | table[2][1]=min(table[1][1],table[1][3])=min(2,min(1,9))=1 | length-4 ranges |
| 4 | Query(1,5): length=5 | j=log[5]=2 | 2^2=4 |
| 5 | table[2][1] covers [1,4] = min(2,6,1,9)=1 | table[2][5-4+1]=table[2][2] covers [2,5]=min(6,1,9,3)=1 | overlap [2,4] harmless |
| 6 | result = min(1,1) = 1 | | matches actual min(A[1..5])=min(2,6,1,9,3)=1 ✅ |

### 4.8 Time & Space Complexity

| Operation | Time | Space |
|---|---|---|
| Build | O(n log n) | O(n log n) |
| Query | O(1) | O(1) |
| Update | Not supported efficiently (O(n log n) rebuild) | — |

### 4.9 Edge Cases
- Single-element array — `k=1`, table has just the base row.
- Query with `l == r` — length 1, `j=0`, trivially returns `table[0][l]`.
- Non-idempotent operations (sum) **cannot** use the overlapping-range trick — use prefix sums or BIT instead for sum queries.

### 4.10 Common Mistakes
- ❌ Using Sparse Table for **sum** queries — sum is not idempotent, overlapping ranges double-count.
- ❌ Trying to support updates — defeats the purpose; use Segment Tree instead for dynamic data.
- ❌ Recomputing `log2` with floating point inside the query loop — precompute `self.log[]` instead to avoid precision bugs.

### 4.11 Interview Tips
- Mention explicitly: *"Since the array is static and min/gcd is idempotent, I can use a Sparse Table for O(1) queries instead of O(log n) with a Segment Tree."*
- Classic application: **O(1) LCA via Euler tour + RMQ Sparse Table**.

### 4.12 Applications
- Static Range Minimum/Maximum Query (RMQ)
- LCA (Lowest Common Ancestor) via Euler tour reduction to RMQ
- Range GCD / Range AND / Range OR queries
- Competitive programming problems with huge query counts on static arrays

### 4.13 Sparse Table vs Segment Tree

| Aspect | Sparse Table | Segment Tree |
|---|---|---|
| Data mutability | Static only | Dynamic (updates supported) |
| Query time | O(1) | O(log n) |
| Build time | O(n log n) | O(n) |
| Space | O(n log n) | O(n) |
| Supported ops | Idempotent only (min, max, gcd, and, or) | Any associative op (incl. sum) |

### 4.14 Practice Problems (Sparse Table)
| Problem | Platform | Difficulty |
|---|---|---|
| Static Range Minimum Queries | CSES | Easy |
| Range Minimum Query (RMQ) | SPOJ | Easy |
| LCA in a Tree | Codeforces | Medium |

### 4.15 Summary & Revision Notes
- Sparse Table = O(1) query for static idempotent range queries after O(n log n) preprocessing.
- Works because overlapping power-of-two ranges don't break idempotent operations.
- No updates supported — use Segment Tree if the array changes.

---

## 5. Skip List

### 5.1 Definition
A **Skip List** is a probabilistic data structure built from multiple layers of sorted linked lists, where higher layers "skip" over many elements, enabling O(log n) expected search/insert/delete — a simpler probabilistic alternative to balanced BSTs.

### 5.2 Why It Exists
Balanced BSTs (AVL, Red-Black) give O(log n) guarantees but require complex rotation logic. Skip Lists achieve the **same expected complexity** using randomization instead of strict invariants — much simpler to implement correctly, and naturally supports concurrent access patterns (used in Redis, LevelDB).

### 5.3 Intuition & Real-World Analogy
Think of an express train system: local trains stop at every station (level 0), express trains skip several stations (level 1), and super-express trains skip even more (level 2+). To go from station A to station Z, you hop on the highest-level train that doesn't overshoot, then drop down a level when you need finer control — dramatically reducing the number of stops.

### 5.4 ASCII Visualization

```
Level 3:  HEAD -----------------------------> 50 -----------------------------> NIL
Level 2:  HEAD ---------> 20 ----------------> 50 --------------> 80 --------> NIL
Level 1:  HEAD ---> 10 -> 20 --------> 40 ----> 50 --------> 70 -> 80 -------> NIL
Level 0:  HEAD -> 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80 -> 90 -> NIL

Search(70): start at level 3, HEAD->50 (50<70, move right), 50 is last at level3 -> drop to level2
  level2: 50->80 (80>70, don't move) -> drop to level1
  level1: 50->70 (70==70) FOUND at level1, confirmed at level0
```

### 5.5 Internal Working & Memory Representation

Each node stores a value and an array of "forward" pointers, one per level it participates in. Level assignment is randomized (typically via coin flips: level increases with probability `p=0.5` each time).

```
Node memory layout:
+-------+----------------------------------+
| value | forward[0] forward[1] ... forward[k] |
+-------+----------------------------------+
```

### 5.6 Python Implementation

```python
import random

class SkipListNode:
    __slots__ = ('value', 'forward')
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    """
    Probabilistic ordered set supporting:
      - search(value): O(log n) expected
      - insert(value): O(log n) expected
      - delete(value): O(log n) expected
    """
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipListNode(-math.inf if False else float('-inf'), max_level)
        self.level = 0  # current highest level in use

    def _random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, value):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.value == value

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current is None or current.value != value:
            new_level = self._random_level()
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level
            new_node = SkipListNode(value, new_level)
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def delete(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1
```

*(Note: `import math` should be at the top of the module; the inline `False` guard above is just illustrative — use `float('-inf')` directly.)*

### 5.7 Line-by-Line Explanation
- `header` is a sentinel node with value `-infinity` and pointers at every possible level, so searches always start from a consistent point.
- `_random_level()` flips a biased coin repeatedly — each success climbs one level. This gives geometric distribution of levels, ensuring only `O(log n)` nodes exist at high levels on average.
- `search`: start at the highest active level, move right while the next value is smaller, drop a level when you can't move right anymore — this is the "express train" descent.
- `insert`: same traversal as search, but records the rightmost node at **each level** that needs its forward pointer rewired (`update[]` array) — classic linked-list insertion generalized to multiple levels.
- `delete`: same traversal, then splice the node out at every level it appears in, and shrink `self.level` if the topmost levels become empty.

### 5.8 Complete Dry Run

Insert `30`, `10`, `50`, `20` into an empty skip list (assume coin flips give levels 0,1,0,2 respectively for simplicity).

| Step | Operation | Level Assigned | Resulting List (level 0) | Explanation |
|---|---|---|---|---|
| 1 | insert(30) | level 0 | HEAD→30 | first node |
| 2 | insert(10) | level 1 | HEAD→10→30 (level0), HEAD→10 (level1) | 10 gets a level-1 pointer too |
| 3 | insert(50) | level 0 | HEAD→10→30→50 (level0) | |
| 4 | insert(20) | level 2 | HEAD→10→20→30→50 (level0); level1: HEAD→10→20; level2: HEAD→20 | 20 becomes the new tallest tower, self.level bumped to 2 |
| 5 | search(30) | — | start level2: HEAD→20 (20<30, move); 20 is last at level2, drop to level1: 20→30? no forward pointer at level1 from 20 to 30 unless recorded; drop to level0: 20→30 FOUND | demonstrates multi-level descent |

### 5.9 Time & Space Complexity

| Operation | Expected Time | Worst Case | Space |
|---|---|---|---|
| Search | O(log n) | O(n) (extremely unlikely) | O(n log n) expected total pointers |
| Insert | O(log n) | O(n) | |
| Delete | O(log n) | O(n) | |

### 5.10 Edge Cases
- Duplicate insert — should be a no-op if value already exists (check in `insert` before creating a new node).
- Deleting from an empty list — `current.forward[0]` will be `None`, delete safely no-ops.
- All coin flips landing on max level repeatedly (pathological) — bounded by `max_level` cap.

### 5.11 Common Mistakes
- ❌ Forgetting the sentinel `header` needs pointers at **all** `max_level` levels from the start.
- ❌ Not shrinking `self.level` after deletions empty out the top levels — wastes time on future searches.
- ❌ Using `random.random() < p` without a level cap — could (rarely) create excessively tall towers.

### 5.12 Interview Tips
- Mention Skip List as an alternative to balanced BSTs when asked to implement an ordered set/map from scratch — it's much easier to get right under interview time pressure.
- Redis's sorted set (`ZSET`) uses a skip list internally combined with a hash table for O(1) value lookups.

### 5.13 Skip List vs Balanced BST

| Aspect | Skip List | Balanced BST (AVL/RB) |
|---|---|---|
| Implementation complexity | Simple (no rotations) | Complex (rotation logic) |
| Complexity guarantee | Expected O(log n) (probabilistic) | Worst-case O(log n) (deterministic) |
| Concurrency friendliness | Good (lock-free variants exist) | Harder (rotations touch multiple nodes) |
| Memory overhead | Extra forward-pointer arrays | Extra balance factor / color bit |
| Real-world use | Redis ZSET, LevelDB | C++ std::map, Java TreeMap |

### 5.14 Applications
- Redis sorted sets
- LevelDB / RocksDB internal memtables
- Concurrent ordered sets in lock-free programming

### 5.15 Practice Problems (Skip List)
| Problem | Platform | Difficulty |
|---|---|---|
| Design Skiplist | LeetCode 1206 | Hard |

### 5.16 Summary & Revision Notes
- Skip List = layered sorted linked lists with randomized "express lanes."
- O(log n) expected time for search/insert/delete — simpler than balanced BST rotations.
- Used in Redis, LevelDB for ordered, concurrent-friendly structures.

---

## 6. Disjoint Set Union (Union-Find)

### 6.1 Definition
**DSU (Union-Find)** maintains a collection of disjoint sets and supports two operations: `find(x)` — which set does `x` belong to, and `union(x, y)` — merge the sets containing `x` and `y`. With path compression + union by rank/size, both operations run in **amortized nearly O(1)** — technically O(α(n)), the inverse Ackermann function.

### 6.2 Why It Exists
Determining connectivity in a dynamically-growing graph (edges added one at a time) via repeated BFS/DFS is O(n) per query. DSU answers "are x and y connected?" and "connect x and y" in near-constant time, making it indispensable for Kruskal's MST, cycle detection, and dynamic connectivity problems.

### 6.3 Intuition & Real-World Analogy
Think of merging friend groups at a party: each person points to a "representative" of their group. To check if two people are in the same group, follow pointers to the representative. When two groups merge, make one representative point to the other. **Path compression** = "next time, everyone in the group points directly to the representative" (flattening the tree so future lookups are instant).

### 6.4 ASCII Visualization

```
Initial (make_set for 0..5): each node is its own parent
0   1   2   3   4   5
|   |   |   |   |   |
0   1   2   3   4   5

union(0,1), union(2,3), union(1,2):

Before path compression (chain from union by rank might create depth):
      0            2
      |           / \
      1          1   3
                 |
                (merged into 2's tree via union(1,2))

find(3) traversal: 3 -> 2  (root found, depth 2)

After path compression on find(3):
3's parent set DIRECTLY to root 2 (no intermediate hops needed next time)
```

### 6.5 Python Implementation

```python
class DSU:
    """
    Disjoint Set Union with path compression + union by rank.
    Amortized O(alpha(n)) per operation (effectively O(1)).
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # number of disjoint sets

    def find(self, x):
        # Path compression: flatten the tree during find
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # already in the same set
        # Union by rank: attach smaller-rank tree under larger-rank tree
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        self.count -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### 6.6 Line-by-Line Explanation
- `parent[i] = i` initially — every element is its own representative (singleton set).
- `find(x)` recursively follows parent pointers to the root, then **rewrites every visited node's parent directly to the root** (`self.parent[x] = self.find(self.parent[x])`) — this is path compression.
- `union(x, y)` finds both roots; if different, attaches the shorter tree (by rank) under the taller one to keep the overall tree shallow — this is union by rank.
- `rank` is an upper bound on tree height (not exact after path compression, but still a valid heuristic for balancing).

### 6.7 Complete Dry Run

`n=6`, operations: `union(0,1)`, `union(2,3)`, `union(1,2)`, `find(3)`.

| Step | Operation | parent[] Before | parent[] After | Explanation |
|---|---|---|---|---|
| 1 | union(0,1) | [0,1,2,3,4,5] | [0,0,2,3,4,5] | root(0)=0,root(1)=1, ranks equal, attach 1 under 0, rank[0]=1 |
| 2 | union(2,3) | [0,0,2,3,4,5] | [0,0,2,2,4,5] | root(2)=2,root(3)=3, attach 3 under 2, rank[2]=1 |
| 3 | union(1,2) | [0,0,2,2,4,5] | [2,0,2,2,4,5] | root(1)=find(1)=0, root(2)=2; rank[0]=1=rank[2]=1, tie -> attach root(0)=0 under root(2)=2, rank[2] becomes 2 |
| 4 | find(3) | parent[3]=2 | parent[3]=2 (already root's direct child) | 3->2, 2 is root, return 2; path compression trivial here (already depth 1) |
| 5 | find(1) | parent[1]=0, parent[0]=2 | parent[1]=2 (compressed directly!) | recursive find(1)->find(0)->2(root); on the way back, parent[0]=2 (already correct) and parent[1] rewritten to 2 |

### 6.8 Time & Space Complexity

| Operation | Time (amortized) | Space |
|---|---|---|
| make_set | O(1) | O(n) total |
| find | O(α(n)) ≈ O(1) | O(1) extra (O(log n) recursion depth worst case pre-compression) |
| union | O(α(n)) ≈ O(1) | O(1) |

> 📝 **Note:** α(n) (inverse Ackermann) grows so slowly it's < 5 for any practical `n` (even `n = 2^65536`). This is why DSU is called "nearly constant time."

### 6.9 Edge Cases
- `union(x, x)` — same element, `find` returns same root, correctly returns `False` (no-op).
- Calling `find` on an out-of-range index — must validate bounds before calling.
- Large recursion depth in `find` for adversarial input **without** path compression — can hit Python's recursion limit; iterative path compression avoids this.

### 6.10 Common Mistakes
- ❌ Implementing `find` without path compression — degrades to O(n) worst case (a long chain).
- ❌ Implementing union without rank/size — trees can become skewed, degrading performance.
- ❌ Recursive `find` on very large inputs can hit Python's default recursion limit (~1000) — use an **iterative** version for safety in production/CP with large n.

### 6.11 Iterative Path Compression (Production-Safe Version)

```python
class DSUIterative:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        # second pass: path compression (iterative, no recursion)
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]  # union by size
        return True
```

### 6.12 Interview Tips
- Always mention **both** optimizations together: path compression alone gives O(log n) amortized; union by rank/size alone gives O(log n); **together** they give O(α(n)) — nearly O(1).
- Common interview framing: "detect cycle in an undirected graph," "count connected components," "accounts merge" (LeetCode) — all scream DSU.

### 6.13 Applications
- Kruskal's Minimum Spanning Tree algorithm
- Cycle detection in undirected graphs
- Dynamic connectivity queries ("are these two nodes connected right now?")
- Image processing (connected component labeling)
- "Number of Islands II" style dynamic grid connectivity
- Percolation problems

### 6.14 Practice Problems (DSU)
| Problem | Platform | Difficulty |
|---|---|---|
| Number of Provinces | LeetCode 547 | Medium |
| Accounts Merge | LeetCode 721 | Medium |
| Redundant Connection | LeetCode 684 | Medium |
| Road Construction | CSES | Medium |
| Union Find | Codeforces EDU | Easy-Medium |

### 6.15 Summary & Revision Notes
- DSU = forest of trees where each tree is a disjoint set, root = representative.
- Path compression + union by rank/size = O(α(n)) amortized ≈ O(1).
- Use iterative find in production to avoid recursion-depth issues.
- Signal phrases: "dynamic connectivity," "merge groups," "cycle detection in undirected graph."

---
## 7. Self-Balancing Trees

### 7.1 Why They Exist
A plain BST degrades to O(n) per operation on sorted/adversarial input (becomes a linked list). Self-balancing trees enforce an invariant after every insert/delete that guarantees O(log n) height, hence O(log n) search/insert/delete **always**, not just on average.

```
Unbalanced BST from sorted insert [1,2,3,4,5]:      Balanced equivalent:
1                                                          3
 \                                                        / \
  2                                                      2   4
   \                                                    /     \
    3          <- O(n) height, degrades to linked list 1       5
     \
      4
       \
        5
```

### 7.2 AVL Tree

#### Definition
An **AVL Tree** (Adelson-Velsky & Landis, 1962) is a BST where for every node, the height difference between left and right subtrees (the **balance factor**) is at most 1. Rebalancing is done via **rotations** after insert/delete.

#### ASCII Visualization — Rotations

```
Left-Left case (needs Right Rotation):
      z                       y
     /                       / \
    y          ---->        x   z
   /
  x

Right-Right case (needs Left Rotation):
  z                            y
   \                          / \
    y          ---->         z   x
     \
      x

Left-Right case (needs Left Rotation on child, then Right Rotation):
    z                  z                    y
   /                  /                    / \
  y        ---->     x         ---->      y   z
   \                 /
    x               y

Right-Left case (mirror of above): Right rotation on child, then Left rotation.
```

#### Python Implementation

```python
class AVLNode:
    __slots__ = ('key', 'left', 'right', 'height')
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """Self-balancing BST maintaining |balance factor| <= 1 at every node."""

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, z):
        y = z.left
        z.left = y.right
        y.right = z
        self._update_height(z)
        self._update_height(y)
        return y  # new subtree root

    def _rotate_left(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        self._update_height(z)
        self._update_height(y)
        return y

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # no duplicates

        self._update_height(root)
        balance = self._balance_factor(root)

        # Left Left
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)
        # Right Right
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)
        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            successor = self._min_value_node(root.right)
            root.key = successor.key
            root.right = self.delete(root.right, successor.key)

        self._update_height(root)
        balance = self._balance_factor(root)

        if balance > 1 and self._balance_factor(root.left) >= 0:
            return self._rotate_right(root)
        if balance > 1 and self._balance_factor(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        if balance < -1 and self._balance_factor(root.right) <= 0:
            return self._rotate_left(root)
        if balance < -1 and self._balance_factor(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root
```

#### Line-by-Line Explanation
- `height` stored per node avoids recomputing subtree heights from scratch (O(1) lookup vs O(n) recount).
- `balance_factor = height(left) - height(right)`; valid range is `{-1, 0, 1}` — anything outside triggers rotation.
- Insert follows standard BST insert recursively, then **on the way back up**, checks balance and rotates as needed — this bottom-up check is what makes AVL self-balancing.
- The four rotation cases (LL, RR, LR, RL) are determined by comparing the balance factor sign and which side the inserted key landed on.

#### Dry Run — Insert causing rotation

Insert `10, 20, 30` into an empty AVL tree (classic Right-Right case).

| Step | Operation | Tree State | Balance Factor | Action |
|---|---|---|---|---|
| 1 | insert(10) | 10 | 0 | no rotation |
| 2 | insert(20) | 10→right(20) | root(10) balance = 0 - 1 = -1 | still OK |
| 3 | insert(30) | 10→right(20)→right(30) | root(10) balance = 0 - 2 = -2 | **imbalanced!** RR case (30 > 20) |
| 4 | rotate_left(10) | new root = 20, left=10, right=30 | balanced (0) | tree height reduced from 3 to 2 |

#### Complexity
| Operation | Time | Space |
|---|---|---|
| Search | O(log n) | O(log n) recursion |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |

#### Common Mistakes
- ❌ Forgetting to update height **before** computing balance factor after a rotation.
- ❌ Not handling all 4 rotation cases (especially LR/RL which need a double rotation).
- ❌ Off-by-one in balance factor threshold (`> 1` not `>= 1`).

#### Applications
- Databases and file systems needing guaranteed O(log n) worst case (unlike Red-Black which optimizes for fewer rotations but slightly taller trees)
- Any application requiring strict height balance (e.g., real-time systems needing predictable worst-case latency)

---

### 7.3 Red-Black Tree

#### Definition
A **Red-Black Tree** is a self-balancing BST where each node is colored red or black, and 5 invariants ensure the longest root-to-leaf path is at most 2× the shortest — giving O(log n) guaranteed height with **fewer rotations** than AVL (better for write-heavy workloads).

#### The 5 Red-Black Invariants
1. Every node is red or black.
2. The root is always black.
3. Every leaf (NIL) is black.
4. A red node cannot have a red child (**no two reds in a row**).
5. Every path from a node to its descendant NIL leaves has the **same number of black nodes** (black-height).

#### ASCII Visualization

```
Valid Red-Black Tree (B=black, R=red):

              10(B)
             /      \
          5(R)       15(R)
         /   \        /   \
      3(B)  7(B)   12(B)  20(B)

Every path root->NIL has exactly 2 black nodes (10 and one of {5/15's children}) -> valid black-height.
```

#### Python Implementation (Insert with Recoloring + Rotations)

```python
RED, BLACK = 'RED', 'BLACK'

class RBNode:
    __slots__ = ('key', 'color', 'left', 'right', 'parent')
    def __init__(self, key, color=RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    """Simplified Red-Black Tree with insert + fixup."""
    def __init__(self):
        self.NIL = RBNode(None, color=BLACK)
        self.root = self.NIL

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = RBNode(key)
        node.left = self.NIL
        node.right = self.NIL
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        node.color = RED
        self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent and node.parent.color == RED:
            grandparent = node.parent.parent
            if node.parent == grandparent.left:
                uncle = grandparent.right
                if uncle.color == RED:
                    # Case 1: recolor and move up
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    grandparent.color = RED
                    node = grandparent
                else:
                    if node == node.parent.right:
                        # Case 2: rotate to convert to Case 3
                        node = node.parent
                        self._rotate_left(node)
                    # Case 3: rotate grandparent
                    node.parent.color = BLACK
                    grandparent.color = RED
                    self._rotate_right(grandparent)
            else:
                uncle = grandparent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    grandparent.color = RED
                    node = grandparent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = BLACK
                    grandparent.color = RED
                    self._rotate_left(grandparent)
            if node == self.root:
                break
        self.root.color = BLACK
```

#### Line-by-Line Explanation
- `NIL` sentinel simplifies edge cases — every "null" pointer instead points to a shared black sentinel node, avoiding constant `None` checks.
- New nodes are always inserted **red** — this only risks violating invariant 4 (no two reds in a row), never invariant 5 (black-height), simplifying the fixup logic.
- `_fix_insert` handles 3 cases per side: **uncle is red** → recolor and move up; **uncle is black, node is "inner" (zig-zag)** → rotate to make it "outer"; **uncle is black, node is "outer"** → rotate grandparent and recolor.

#### Dry Run (conceptual)
Inserting `10, 20, 30` in sequence: `10` becomes root (recolored black). `20` inserted red as `10`'s right child (parent black — no violation). `30` inserted red as `20`'s right child — parent `20` is red → violation. Uncle (`10`'s left, which is `NIL`, black) → Case 3 (outer case): rotate grandparent `10` left, recolor `20` black and `10` red. Final tree: `20(B)` root with `10(R)` and `30(R)` children — balanced.

#### Complexity
| Operation | Time | Space |
|---|---|---|
| Search | O(log n) | O(1) |
| Insert | O(log n), ≤ 2 rotations | O(1) |
| Delete | O(log n), ≤ 3 rotations | O(1) |

#### AVL vs Red-Black — Head-to-Head

| Aspect | AVL Tree | Red-Black Tree |
|---|---|---|
| Balance strictness | Stricter (height diff ≤ 1) | Looser (up to 2x height difference) |
| Search speed | Faster (shorter trees) | Slightly slower |
| Insert/Delete speed | Slower (more rotations) | Faster (fewer rotations) |
| Use case | Read-heavy workloads | Write-heavy workloads |
| Real-world use | Database indexes needing fast lookups | C++ std::map, Java TreeMap, Linux CFS scheduler |

#### Applications
- Linux kernel's Completely Fair Scheduler (CFS) uses a Red-Black Tree
- C++ STL `std::map` / `std::set` (typically Red-Black Tree internally)
- Java's `TreeMap` / `TreeSet`

---

### 7.4 Splay Tree

#### Definition
A **Splay Tree** is a self-adjusting BST where every accessed node is moved to the root via a sequence of rotations called "splaying." Frequently accessed elements end up near the root, giving excellent **amortized** O(log n) performance with great practical performance on skewed access patterns (temporal locality).

#### Intuition
Like a "most recently used" cache built into a tree — recently accessed items are cheap to access again because they're near the top.

#### ASCII Visualization — Zig-Zig Splay

```
Splaying node x when x, parent(x), grandparent(x) form a straight line (zig-zig):

      g                     x
     /                     / \
    p          ---->      ?   p
   /                          / \
  x                          ?   g

Two rotations in the SAME direction, applied bottom-up.
```

#### Python Implementation (simplified — splay via rotations)

```python
class SplayNode:
    __slots__ = ('key', 'left', 'right')
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            if root.left is None:
                return root
            if key < root.left.key:                 # Zig-Zig (left-left)
                root.left.left = self._splay(root.left.left, key)
                root = self._rotate_right(root)
            elif key > root.left.key:                # Zig-Zag (left-right)
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._rotate_left(root.left)
            return self._rotate_right(root) if root.left else root
        else:
            if root.right is None:
                return root
            if key > root.right.key:                 # Zig-Zig (right-right)
                root.right.right = self._splay(root.right.right, key)
                root = self._rotate_left(root)
            elif key < root.right.key:                # Zig-Zag (right-left)
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._rotate_right(root.right)
            return self._rotate_left(root) if root.right else root

    def insert(self, key):
        if self.root is None:
            self.root = SplayNode(key)
            return
        self.root = self._splay(self.root, key)
        if self.root.key == key:
            return  # already exists
        new_node = SplayNode(key)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root is not None and self.root.key == key
```

#### Complexity
| Operation | Amortized Time | Worst Case (single op) |
|---|---|---|
| Search/Insert/Delete | O(log n) | O(n) |

#### Applications
- Caching systems with temporal locality
- Network routers (LRU-like packet buffer management)
- Garbage collectors (some implementations)

#### Common Mistakes
- ❌ Assuming per-operation O(log n) guarantee — splay trees only guarantee **amortized** O(log n) over a sequence of operations.
- ❌ Forgetting to splay on **search** too, not just insert/delete — the self-adjusting property requires splaying on every access.

---

### 7.5 Treap

*(Covered in depth in Section 14 — Randomized Structures, since Treap = Tree + Heap combining BST ordering with heap-based randomized priorities.)*

### 7.6 AA Tree & Scapegoat Tree (Overview)

**AA Tree:** A simplified variant of Red-Black Trees using only one extra "level" field instead of color, restricting to fewer rebalancing cases (only right-links can be red-equivalent) — easier to implement correctly than full Red-Black, though less commonly used in production.

**Scapegoat Tree:** A self-balancing BST with **zero extra per-node memory** (no color/height/balance field) — instead, it rebuilds an entire unbalanced subtree ("finds a scapegoat") whenever a node's depth exceeds `log_(3/2)(n)`, giving amortized O(log n) insert and O(log n) search using pure size-counting instead of stored balance metadata.

### 7.7 Self-Balancing Trees — Master Comparison

| Structure | Balance Mechanism | Worst-Case Height | Rotations/Op | Extra Memory/Node | Best For |
|---|---|---|---|---|---|
| AVL | Strict height balance | 1.44 log n | Up to O(log n) | height (int) | Read-heavy |
| Red-Black | Color invariants | 2 log n | ≤ 3 | 1 bit (color) | Write-heavy, general purpose |
| Splay | Move-to-root on access | O(n) worst single op | Varies | none | Temporal locality / caching |
| Treap | Randomized heap priority | O(log n) expected | O(log n) expected | priority (int) | Simple to implement, CP |
| AA Tree | Level field | 2 log n | Fewer cases than RB | level (int) | Simpler RB alternative |
| Scapegoat | Weight-based rebuild | log_(3/2) n | Amortized rebuild | none | Memory-constrained systems |

### 7.8 Practice Problems (Self-Balancing Trees)
| Problem | Platform | Difficulty |
|---|---|---|
| Balanced BST from array | GeeksforGeeks | Easy |
| Design a Skiplist / balanced structure | LeetCode | Hard |
| Kth Smallest Element in a BST | LeetCode 230 | Medium |
| CF 1288E (Splay/segment tree hybrid) | Codeforces | Hard |

### 7.9 Summary & Revision Notes
- AVL = strict balance (height diff ≤ 1), best for read-heavy, more rotations on write.
- Red-Black = looser balance via color invariants, fewer rotations, industry standard (std::map, TreeMap, Linux scheduler).
- Splay = move-to-root, amortized O(log n), great for temporal locality/caching.
- Treap = randomized BST + heap priorities, simplest to implement correctly under time pressure.
- All guarantee O(log n) height except Splay (amortized only).

---
## 8. B-Tree Family

### 8.1 Why B-Trees Exist
In-memory trees (AVL, Red-Black) assume pointer traversal is cheap. On **disk**, every node access is a costly seek (~milliseconds). B-Trees minimize the **number of disk reads** by making each node hold many keys (not just 1), keeping the tree extremely shallow (height 3-4 even for millions of records) — matching the disk block size so one node read = one disk I/O.

### 8.2 B-Tree Definition
A **B-Tree of order m** is a self-balancing search tree where:
- Every node has at most `m` children and at least `⌈m/2⌉` children (except root).
- A node with `k` children holds `k-1` keys.
- All leaves are at the same depth (perfectly balanced).
- Keys within a node are sorted; search descends via the appropriate range.

### 8.3 ASCII Visualization (B-Tree of order 4, max 3 keys/node)

```
                     [ 20 | 40 ]
                    /      |      \
           [5|10|15]   [25|30|35]  [50|60|70]

Search(30): 30 is between 20 and 40 -> go to middle child [25|30|35] -> found directly in node.
Only 2 node visits (2 disk reads) even though there are 9 total keys.
```

### 8.4 Python Implementation (Simplified B-Tree, order = degree `t`, insert + search)

```python
class BTreeNode:
    def __init__(self, t, leaf=True):
        self.t = t              # minimum degree
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    """
    Simplified B-Tree supporting insert and search.
    Each node holds between t-1 and 2t-1 keys (except root: 1 to 2t-1).
    """
    def __init__(self, t=3):
        self.t = t
        self.root = BTreeNode(t, leaf=True)

    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == key:
            return True
        if node.leaf:
            return False
        return self.search(node.children[i], key)

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _split_child(self, parent, i):
        t = self.t
        full_child = parent.children[i]
        new_child = BTreeNode(t, leaf=full_child.leaf)
        mid_key = full_child.keys[t - 1]

        new_child.keys = full_child.keys[t:]
        full_child.keys = full_child.keys[:t - 1]

        if not full_child.leaf:
            new_child.children = full_child.children[t:]
            full_child.children = full_child.children[:t]

        parent.children.insert(i + 1, new_child)
        parent.keys.insert(i, mid_key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)
```

### 8.5 Line-by-Line Explanation
- `t` (minimum degree) controls node capacity: each node holds `t-1` to `2t-1` keys, and has `t` to `2t` children (except root).
- `insert`: if the root is full (`2t-1` keys), it must be split **first** — this is the only way a B-Tree grows in height (always from the root, keeping it balanced).
- `_split_child`: splits a full child into two nodes around its median key, which gets promoted to the parent.
- `_insert_non_full`: recursively descends to the correct leaf, splitting any full child **before** descending into it (this "split ahead of time" strategy means insertion is always a single top-down pass, never needs to backtrack).

### 8.6 Complete Dry Run

Insert `10, 20, 5, 6, 12, 30, 7, 17` into a B-Tree with `t=2` (max 3 keys/node).

| Step | Key Inserted | Root State | Action |
|---|---|---|---|
| 1-3 | 10, 20, 5 | [5, 10, 20] | fits in root leaf (max 3 keys for t=2) |
| 4 | 6 | root full (3 keys) → split | median 10 promoted; new root=[10], children=[5,6] and [20] |
| 5 | 12 | descend right of 10 → [20] gets 12 → [12, 20] | |
| 6 | 30 | [12,20] + 30 → [12,20,30] fits | |
| 7 | 7 | descend left of 10 → [5,6] + 7 → [5,6,7] fits | |
| 8 | 17 | right child [12,20,30] is full (3 keys) → split before descending; median 20 promoted to root → root=[10,20]; children=[5,6,7], [12,17], [30] | tree grows in height only via root split |

Final tree:
```
              [10 | 20]
             /    |     \
        [5,6,7] [12,17] [30]
```

### 8.7 Time & Space Complexity

| Operation | Time | Space |
|---|---|---|
| Search | O(log_t n) | O(1) extra |
| Insert | O(log_t n) | O(1) extra |
| Delete | O(log_t n) (complex merging/borrowing logic) | O(1) extra |

### 8.8 B+ Tree

#### Definition
A **B+ Tree** is a variant where **all data is stored in leaf nodes only**; internal nodes store just keys for routing. Leaf nodes are additionally **linked together** in a doubly-linked list, enabling fast sequential range scans.

#### ASCII Visualization

```
Internal nodes (routing only, no data):
                    [ 20 | 40 ]
                   /      |      \
            [10|15]    [25|30]   [50|60]     <- internal
              |            |          |
        (leaf nodes, linked list, hold actual records)
    [10,15] <-> [20,25,30] <-> [40,50,60] <-> NIL
```

#### Why B+ Tree Over B-Tree for Databases
- **Range queries** (`SELECT * WHERE age BETWEEN 20 AND 40`) are O(log n + k) — traverse to the start leaf, then walk the linked list for `k` results — no need to revisit internal nodes.
- Internal nodes only store keys (no data payload), so **more keys fit per node**, meaning shallower trees and fewer disk reads for the same total data.
- All data at the same leaf depth simplifies consistent scan performance.

#### B-Tree vs B+ Tree

| Aspect | B-Tree | B+ Tree |
|---|---|---|
| Data location | Any node (internal or leaf) | Leaf nodes only |
| Leaf linking | No | Yes (linked list) |
| Range query efficiency | O(log n) per lookup, no fast scan | O(log n + k) — fast sequential scan |
| Space efficiency | Less (data mixed with routing) | More (routing nodes hold only keys) |
| Used in | Some filesystems (older designs) | MySQL InnoDB, PostgreSQL, most modern RDBMS |

#### B* Tree (Overview)
A **B* Tree** further improves space utilization by requiring nodes to be at least **2/3 full** (vs 1/2 for B-Tree/B+ Tree) and using a more complex splitting strategy — splits two nodes into three when both are full instead of splitting one into two, reducing tree height further at the cost of implementation complexity.

### 8.9 Edge Cases
- Deletion causing a node to fall below minimum keys — requires **borrowing** from a sibling or **merging** with a sibling (analogous to B-Tree deletion algorithms, more complex than insertion).
- Choosing `t` (degree) too small — tree behaves like a binary tree (more disk reads); too large — wastes space per node if underfilled.

### 8.10 Common Mistakes
- ❌ Forgetting to promote the median key during a split.
- ❌ Not maintaining minimum key count invariants during deletion (leads to invalid trees).
- ❌ Confusing B-Tree (data anywhere) with B+ Tree (data in leaves only) when discussing database indexing in interviews.

### 8.11 Applications
- **MySQL InnoDB**, **PostgreSQL**, **Oracle** — B+ Tree indexes
- **File systems**: NTFS, HFS+, ext4 (via variants) use B-Tree-like structures for directory indexing
- **NoSQL databases**: some use LSM-trees (different family) but B-Trees remain dominant for traditional RDBMS

### 8.12 Practice Problems (B-Tree Family)
| Problem | Platform | Difficulty |
|---|---|---|
| Implement a B-Tree | GeeksforGeeks | Hard |
| Design an in-memory database index | System Design (conceptual) | Hard |

### 8.13 Summary & Revision Notes
- B-Tree/B+ Tree exist to minimize disk I/O by maximizing keys-per-node (matching disk block size).
- B+ Tree stores data only in leaves, links leaves for fast range scans — the industry standard for RDBMS indexes.
- B* Tree trades implementation complexity for better space utilization (2/3 full minimum vs 1/2).

---

## 9. Interval Structures

### 9.1 Interval Tree

#### Definition
An **Interval Tree** is a BST where each node stores an interval `[low, high]`, ordered by `low`, and additionally tracks the **maximum high value** in its subtree — enabling efficient "find all intervals overlapping with query interval `[l, r]`" queries.

#### Why It Exists
Naively checking overlap against every interval is O(n) per query. Interval trees prune entire subtrees when the subtree's max-high is less than the query's low, achieving O(log n + k) where k = number of matching intervals.

#### ASCII Visualization

```
Intervals: [15,20], [10,30], [17,19], [5,20], [12,15], [30,40]

BST ordered by low, augmented with subtree max-high:

                [17,19] max=40
               /              \
         [5,20] max=30      [30,40] max=40
        /       \
   [12,15]    [15,20]
    max=15     max=20

Query overlap([14,16]):
  root [17,19]: overlap? 14<=19 and 17<=16? NO (17>16) -> no overlap at root, but check left subtree since low(17) could still have overlaps on the left (14 < 17)
  left child [5,20]: overlap? 5<=16 and 14<=20 YES -> report [5,20], recurse both children
  [12,15]: overlap? 12<=16,14<=15 YES -> report
  [15,20]: overlap? YES -> report
```

#### Python Implementation

```python
class IntervalNode:
    __slots__ = ('low', 'high', 'max_high', 'left', 'right')
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.max_high = high
        self.left = None
        self.right = None

class IntervalTree:
    """BST ordered by interval.low, augmented with subtree max_high for pruning."""
    def __init__(self):
        self.root = None

    def insert(self, low, high):
        self.root = self._insert(self.root, low, high)

    def _insert(self, node, low, high):
        if node is None:
            return IntervalNode(low, high)
        if low < node.low:
            node.left = self._insert(node.left, low, high)
        else:
            node.right = self._insert(node.right, low, high)
        node.max_high = max(node.max_high, high)
        return node

    def search_overlap(self, low, high):
        result = []
        self._search(self.root, low, high, result)
        return result

    def _search(self, node, low, high, result):
        if node is None:
            return
        if node.low <= high and low <= node.high:   # this node's interval overlaps
            result.append((node.low, node.high))
        # if left subtree's max_high >= low, an overlap might exist there
        if node.left and node.left.max_high >= low:
            self._search(node.left, low, high, result)
        # always need to check right subtree UNLESS node.low > high (query ends before this node even starts)
        if node.right and node.low <= high:
            self._search(node.right, low, high, result)
```

#### Line-by-Line Explanation
- `max_high` per node = the maximum `high` value across the entire subtree — this augmentation is what enables pruning.
- `_search` checks the current node for overlap directly (`node.low <= high and low <= node.high` — the classic interval overlap condition), then decides whether to recurse left/right based on whether pruning conditions allow a possible match.
- Left subtree is skipped if `node.left.max_high < low` (no interval in the left subtree can possibly reach far enough right to overlap).

#### Dry Run
Using the example diagram above with `search_overlap(14, 16)`:

| Step | Node | Overlap Check | Recurse Left? | Recurse Right? |
|---|---|---|---|---|
| 1 | [17,19] | 17<=16? NO → no overlap here | left.max_high=30 >= 14 → YES | node.low=17 <= 16? NO → skip right |
| 2 | [5,20] | 5<=16 and 14<=20 → YES, report [5,20] | left.max_high=15>=14 → YES | node.low=5<=16 → YES |
| 3 | [12,15] | 12<=16,14<=15 → YES, report | no children | no children |
| 4 | [15,20] | 15<=16,14<=20 → YES, report | no children | no children |
| 5 | Final result | [(5,20), (12,15), (15,20)] | | matches expected overlaps |

#### Complexity
| Operation | Time | Space |
|---|---|---|
| Insert | O(log n) (if balanced) | O(log n) |
| Search overlap | O(log n + k) where k = matches | O(log n + k) |

#### Common Mistakes
- ❌ Forgetting to update `max_high` on the way back up after insertion.
- ❌ Incorrect pruning condition (must check `left.max_high >= low`, not `left.max_high >= high`).
- ❌ Not balancing the underlying BST — a plain BST can degrade to O(n); production interval trees pair this augmentation with a Red-Black or AVL tree.

#### Applications
- Calendar/meeting scheduling conflict detection
- Genomic interval overlap queries (bioinformatics)
- Computational geometry (finding overlapping rectangles' x/y projections)

### 9.2 Interval Tree vs Segment Tree

| Aspect | Interval Tree | Segment Tree |
|---|---|---|
| Query type | "Which intervals overlap point/range X?" | "Aggregate over range X" |
| Data model | Stores actual intervals | Stores array elements |
| Structure | Augmented BST | Complete binary tree over array indices |
| Typical use | Overlap detection, scheduling | Range sum/min/max queries |

### 9.3 Interval Skip List (Overview)
A probabilistic alternative to the augmented BST interval tree — uses skip list layers instead of BST rotations, storing interval endpoints with "search fingers" for fast overlap queries. Useful in concurrent/lock-free settings where BST rotations are expensive to synchronize.

### 9.4 Practice Problems (Interval Structures)
| Problem | Platform | Difficulty |
|---|---|---|
| Merge Intervals | LeetCode 56 | Medium |
| Non-overlapping Intervals | LeetCode 435 | Medium |
| My Calendar I/II/III | LeetCode 729/731/732 | Medium-Hard |
| Data Stream as Disjoint Intervals | LeetCode 352 | Hard |

### 9.5 Summary & Revision Notes
- Interval Tree = BST ordered by low, augmented with subtree max-high for O(log n + k) overlap queries.
- Different from Segment Tree — interval trees answer "which stored intervals overlap X," segment trees answer "aggregate over array range X."

---

## 10. Range Query Structures — Unified Comparison

### 10.1 Sqrt Decomposition

#### Definition
Split the array into `√n`-sized blocks, precompute an aggregate per block. Query = combine full blocks in O(√n) + partial blocks in O(√n) = O(√n) total. Update = O(1) (update element + its block's aggregate).

```python
import math

class SqrtDecomposition:
    """Range sum query + point update in O(sqrt(n))."""
    def __init__(self, arr):
        self.n = len(arr)
        self.block_size = int(math.sqrt(self.n)) + 1
        self.arr = list(arr)
        self.block = [0] * ((self.n // self.block_size) + 1)
        for i in range(self.n):
            self.block[i // self.block_size] += arr[i]

    def update(self, idx, val):
        b = idx // self.block_size
        self.block[b] += val - self.arr[idx]
        self.arr[idx] = val

    def query(self, l, r):
        b_l, b_r = l // self.block_size, r // self.block_size
        if b_l == b_r:
            return sum(self.arr[l:r + 1])
        total = sum(self.arr[l: (b_l + 1) * self.block_size])
        for b in range(b_l + 1, b_r):
            total += self.block[b]
        total += sum(self.arr[b_r * self.block_size: r + 1])
        return total
```

**When to use:** simpler to implement than segment trees, decent for O(√n) operations when O(log n) isn't strictly required, and forms the backbone of **Mo's Algorithm** (Section 16).

### 10.2 Wavelet Tree (Overview)
A structure for answering **"k-th smallest in range"** and **"count of values ≤ x in range"** queries by recursively partitioning the value range (not the index range) — each level splits values into "low half" and "high half," maintaining a bitmap of which side each position went to. Query time O(log(max_value)). Common in succinct data structure literature and specialized CP problems; considered research/advanced-CP level.

### 10.3 Master Comparison Table — All Range Query Structures

| Structure | Build | Point Update | Range Update | Range Query | Space | Static/Dynamic |
|---|---|---|---|---|---|---|
| Prefix Sum Array | O(n) | O(n) (rebuild suffix) | — | O(1) | O(n) | Static |
| Sqrt Decomposition | O(n) | O(1) | O(√n) | O(√n) | O(n) | Dynamic |
| Fenwick Tree (BIT) | O(n log n) | O(log n) | O(log n) (2-BIT trick) | O(log n) | O(n) | Dynamic |
| Segment Tree | O(n) | O(log n) | O(log n) (lazy prop) | O(log n) | O(4n) | Dynamic |
| Sparse Table | O(n log n) | Not supported | Not supported | O(1) | O(n log n) | Static |
| Wavelet Tree | O(n log(max_val)) | Not typical | Not typical | O(log(max_val)) | O(n log(max_val)) | Static (mostly) |

### 10.4 Decision Flowchart — Which Range Query Structure?

```
                    Is the array STATIC (no updates)?
                       /                          \
                     YES                           NO
                      |                             |
        Is the operation idempotent?      Do you need RANGE updates too
        (min/max/gcd/and/or)                (not just point updates)?
             /        \                        /              \
           YES         NO                    YES               NO
            |           |                     |                 |
      Sparse Table  Prefix Sum        Segment Tree        Fenwick Tree
      (O(1) query)  (O(1) query,      w/ Lazy Prop        (simpler, O(log n))
                      static only)     (O(log n))
```

### 10.5 Interview Tips
- If asked to optimize a brute-force range-sum-with-updates solution, the expected answer path is: *"Prefix sum array fails because updates are O(n). Fenwick Tree or Segment Tree gives O(log n) for both."*
- If min/max is needed instead of sum, explicitly rule out BIT (not invertible) and reach for Segment Tree.
- If the array **never changes**, always mention Sparse Table for O(1) queries as the optimal choice.

---
## 11. Spatial Data Structures

### 11.1 KD-Tree

#### Definition
A **KD-Tree (k-dimensional tree)** is a binary tree that recursively partitions k-dimensional space by alternating the splitting dimension at each depth — level 0 splits by x, level 1 by y, level 2 back to x, etc. (for 2D). Enables efficient nearest-neighbor and range queries in multi-dimensional space.

#### Why It Exists
Linear scan for "nearest point to (x,y)" is O(n). KD-Trees reduce this to O(log n) average case by pruning entire regions of space that can't contain a closer point.

#### ASCII Visualization (2D KD-Tree)

```
Points: (3,6), (17,15), (13,15), (6,12), (9,1), (2,7), (10,19)

Level 0 (split by x): root = (7,2) [median x]... (simplified example)

Spatial partition view:
   y
   |    *(13,15)      *(17,15)
   |         |
   |    *(6,12)
   |    |         *(10,19)
   |    *(2,7)
   |         *(9,1)  <- root splits here (vertical line at x=7)
   +------------------------- x
        (splits alternate: vertical, then horizontal, then vertical...)
```

#### Python Implementation

```python
class KDNode:
    __slots__ = ('point', 'left', 'right')
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

class KDTree:
    """2D KD-Tree supporting nearest-neighbor search. Generalizes to k dimensions."""
    def __init__(self, points, k=2):
        self.k = k
        self.root = self._build(points, depth=0)

    def _build(self, points, depth):
        if not points:
            return None
        axis = depth % self.k
        points.sort(key=lambda p: p[axis])
        mid = len(points) // 2
        return KDNode(
            point=points[mid],
            left=self._build(points[:mid], depth + 1),
            right=self._build(points[mid + 1:], depth + 1)
        )

    def nearest_neighbor(self, target):
        best = [None, float('inf')]  # [best_point, best_dist_sq]

        def dist_sq(a, b):
            return sum((a[i] - b[i]) ** 2 for i in range(self.k))

        def search(node, depth):
            if node is None:
                return
            d = dist_sq(node.point, target)
            if d < best[1]:
                best[0], best[1] = node.point, d

            axis = depth % self.k
            diff = target[axis] - node.point[axis]
            near, far = (node.left, node.right) if diff < 0 else (node.right, node.left)

            search(near, depth + 1)
            # only explore the far side if the splitting plane is closer than current best
            if diff ** 2 < best[1]:
                search(far, depth + 1)

        search(self.root, 0)
        return best[0]
```

#### Line-by-Line Explanation
- `_build` sorts points by the current axis (alternating each depth level) and picks the median as the splitting node — this keeps the tree balanced.
- `nearest_neighbor` recursively descends toward the side matching the target's position, then **only** backtracks into the "far" side if the splitting hyperplane's distance is less than the current best distance found — this pruning is what gives KD-Trees their speed.

#### Dry Run
Points: `[(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]`, query nearest to `(9,2)`.

| Step | Node Visited | Axis | Action | Best So Far |
|---|---|---|---|---|
| 1 | root=(7,2) (median by x) | x | dist=(9-7)^2+(2-2)^2=4 | best=(7,2), dist=4 |
| 2 | descend right (9 > 7) → (9,6) | y | dist=(9-9)^2+(2-6)^2=16 | still best=(7,2) |
| 3 | check far side (left of (7,2)): (7-9)^2=4 < best(4)? NO(equal, boundary) → mild prune | | |
| 4 | Final answer | | | (7,2) is nearest (dist=4) |

#### Complexity
| Operation | Average Time | Worst Case |
|---|---|---|
| Build | O(n log n) | O(n log n) |
| Nearest Neighbor | O(log n) | O(n) (unbalanced/high dimensions) |
| Range Search | O(√n + k) in 2D | O(n) |

> ⚠️ **Warning:** KD-Trees suffer from the **"curse of dimensionality"** — performance degrades toward O(n) as the number of dimensions grows large (roughly beyond 20 dimensions), because pruning becomes ineffective when most points are "equally far" in high-dimensional space.

#### Applications
- Nearest neighbor search in ML (k-NN classifiers)
- Computer graphics (ray tracing acceleration structures — though Octrees/BVH more common there)
- GIS "find nearest restaurant" queries

### 11.2 Quad Tree

#### Definition
A **Quad Tree** recursively divides 2D space into **4 equal quadrants**, subdividing further only where point density requires it — unlike KD-Tree's median-based splits, Quad Tree splits are based on fixed spatial midpoints.

#### ASCII Visualization

```
+-------------------+
|  NW      |   NE   |
|    *     |     *  |
|----------+--------|
|  SW      |   SE   |
|          |  * *   |  <- SE quadrant subdivides further since it has 2 points
+-------------------+
```

#### Python Implementation (simplified point Quad Tree)

```python
class QuadTreeNode:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary   # (x, y, width, height)
        self.capacity = capacity
        self.points = []
        self.divided = False
        self.nw = self.ne = self.sw = self.se = None

    def _in_boundary(self, point):
        x, y, w, h = self.boundary
        px, py = point
        return x <= px < x + w and y <= py < y + h

    def _subdivide(self):
        x, y, w, h = self.boundary
        hw, hh = w / 2, h / 2
        self.nw = QuadTreeNode((x, y, hw, hh), self.capacity)
        self.ne = QuadTreeNode((x + hw, y, hw, hh), self.capacity)
        self.sw = QuadTreeNode((x, y + hh, hw, hh), self.capacity)
        self.se = QuadTreeNode((x + hw, y + hh, hw, hh), self.capacity)
        self.divided = True

    def insert(self, point):
        if not self._in_boundary(point):
            return False
        if len(self.points) < self.capacity and not self.divided:
            self.points.append(point)
            return True
        if not self.divided:
            self._subdivide()
        return (self.nw.insert(point) or self.ne.insert(point) or
                self.sw.insert(point) or self.se.insert(point))
```

#### Complexity
| Operation | Average Time |
|---|---|
| Insert | O(log n) |
| Range Query | O(√n + k) |

#### Applications
- Image compression (quadtree encoding)
- Collision detection in 2D games
- Spatial indexing for maps (clustering nearby markers)

### 11.3 Octree (Overview)
The 3D generalization of Quad Tree — subdivides space into **8 octants**. Used extensively in 3D graphics (mesh simplification, collision detection in physics engines), 3D point cloud processing (LiDAR data), and volumetric rendering (Minecraft-style voxel engines).

### 11.4 R-Tree (Overview)
Unlike KD-Tree/Quad-Tree (which partition space), an **R-Tree** groups nearby objects using **minimum bounding rectangles (MBRs)**, which may overlap. Optimized for indexing **rectangles/regions** (not just points), making it the standard choice for spatial databases (PostGIS, Oracle Spatial) indexing geographic shapes like countries, roads, and buildings.

### 11.5 Spatial Structures — Comparison Table

| Structure | Splits By | Best For | Used In |
|---|---|---|---|
| KD-Tree | Median of points, alternating axis | Nearest-neighbor, low dimensions | ML libraries (scikit-learn), computational geometry |
| Quad Tree | Fixed spatial midpoint (2D) | Uniform 2D region queries | Games, GIS map clustering |
| Octree | Fixed spatial midpoint (3D) | 3D spatial queries | 3D graphics, voxel engines, LiDAR |
| R-Tree | Bounding rectangles (can overlap) | Indexing shapes/regions | PostGIS, spatial databases |

### 11.6 Practice Problems (Spatial Structures)
| Problem | Platform | Difficulty |
|---|---|---|
| K Closest Points to Origin | LeetCode 973 | Medium |
| The Skyline Problem | LeetCode 218 | Hard |
| My Calendar III | LeetCode 732 | Hard |

### 11.7 Summary & Revision Notes
- KD-Tree: median-based space partition, great for nearest-neighbor in low dimensions.
- Quad Tree/Octree: fixed midpoint subdivision for 2D/3D uniform region queries.
- R-Tree: bounding-rectangle based, standard for spatial databases indexing shapes.

---

## 12. String-Oriented Advanced Structures

*(Tries are NOT covered here — see the Trees handbook.)*

### 12.1 Suffix Array

#### Definition
A **Suffix Array** is a sorted array of all suffixes of a string, represented by their starting indices — enabling O(log n) substring search and forming the backbone of many string algorithms (LCP array, Burrows-Wheeler Transform).

#### Why It Exists
A **Suffix Tree** gives the same power but with heavy memory overhead (pointers, edge labels). Suffix Arrays achieve similar power with **much less memory** (just an array of integers), at the cost of needing an auxiliary LCP (Longest Common Prefix) array for some operations.

#### ASCII Visualization

```
String: "banana$"  (indices 0-6)

All suffixes:
0: banana$
1: anana$
2: nana$
3: ana$
4: na$
5: a$
6: $

Sorted suffixes (lexicographic):
6: $
5: a$
3: ana$
1: anana$
0: banana$
4: na$
2: nana$

Suffix Array = [6, 5, 3, 1, 0, 4, 2]
```

#### Python Implementation (O(n log^2 n) construction — simple, interview-friendly)

```python
def build_suffix_array(s):
    """
    O(n log^2 n) suffix array construction using Python's sort
    with prefix-doubling rank comparison.
    """
    s += '$'  # sentinel smaller than all characters
    n = len(s)
    suffixes = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0] * n
    k = 1
    while k < n:
        def compare_key(i):
            first = rank[i]
            second = rank[i + k] if i + k < n else -1
            return (first, second)

        suffixes.sort(key=compare_key)
        tmp[suffixes[0]] = 0
        for i in range(1, n):
            tmp[suffixes[i]] = tmp[suffixes[i - 1]]
            if compare_key(suffixes[i]) != compare_key(suffixes[i - 1]):
                tmp[suffixes[i]] += 1
        rank = tmp[:]
        if rank[suffixes[-1]] == n - 1:
            break
        k *= 2
    return suffixes

def build_lcp_array(s, suffix_array):
    """Kasai's algorithm: O(n) LCP array construction given the suffix array."""
    s += '$'
    n = len(s)
    rank = [0] * n
    for i, suf in enumerate(suffix_array):
        rank[suf] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
        else:
            h = 0
    return lcp
```

#### Line-by-Line Explanation
- **Prefix doubling:** each round doubles the comparison length `k` (compare 1 char, then 2, then 4, ...) using a `(rank[i], rank[i+k])` pair as a sort key — this correctly ranks suffixes by their first `2k` characters using only previously computed ranks, giving `O(log n)` rounds of `O(n log n)` sorting = `O(n log^2 n)` total.
- **Kasai's algorithm** computes the LCP array in O(n) by exploiting the fact that if `LCP(i, i-1) = h`, then `LCP(i+1, rank_of_previous_suffix) >= h - 1` — avoiding recomputation from scratch for each pair.

#### Dry Run (abbreviated)
For `"banana"`: suffix array = `[6, 5, 3, 1, 0, 4, 2]` (indices into `"banana$"`), LCP array (between consecutive sorted suffixes) = `[0, 0, 1, 3, 0, 0, 2]` — e.g., `LCP` between `"ana$"` (idx 3) and `"anana$"` (idx 1) = 3 (`"ana"` shared).

#### Complexity
| Operation | Time | Space |
|---|---|---|
| Build (prefix doubling) | O(n log² n) | O(n) |
| Build (DC3/SA-IS, advanced) | O(n) | O(n) |
| LCP array (Kasai) | O(n) | O(n) |
| Substring search using SA + binary search | O(m log n) | O(1) extra |

#### Applications
- Longest common substring / longest repeated substring
- Full-text search indexes (search engines)
- Bioinformatics (genome assembly, read alignment)
- Burrows-Wheeler Transform (used in bzip2 compression)

### 12.2 Suffix Automaton (Overview)
A **Suffix Automaton** is the smallest DFA (deterministic finite automaton) that accepts exactly all suffixes of a string, built in O(n) time using an ingenious incremental construction (each character addition creates O(1) amortized new states). It's more memory-compact than a suffix tree for many pattern-matching tasks and supports counting distinct substrings, longest common substring between two strings (by feeding both into the automaton), and substring existence checks in O(m) per query.

### 12.3 Suffix Tree (Overview)
A compressed trie of all suffixes of a string, built in O(n) via Ukkonen's algorithm. Each edge is labeled with a substring (not a single character) for compression. Supports O(m) substring search, but has significant memory overhead in practice (~10-20x the string size due to pointers) — Suffix Arrays are usually preferred in production code for this reason.

### 12.4 Rope

#### Definition
A **Rope** is a binary tree where leaves hold small string chunks and internal nodes store the total length of their left subtree — enabling O(log n) concatenation, insertion, and deletion for **very large strings** (megabytes+), unlike a plain Python string which requires O(n) for any modification (strings are immutable).

#### ASCII Visualization

```
Rope for "Hello_World" (split into chunks):

              [len=6]
             /        \
        "Hello_"    "World"
        (leaf)       (leaf)

Concatenating with another rope "!!!" is O(1) (just create a new root pointing to both):

                  [len=11]
                 /          \
           [len=6]          "!!!"
          /        \
     "Hello_"    "World"
```

#### Python Implementation (simplified)

```python
class RopeNode:
    __slots__ = ('left', 'right', 'weight', 'value')
    def __init__(self, value=None, left=None, right=None):
        self.value = value          # only set for leaf nodes
        self.left = left
        self.right = right
        self.weight = len(value) if value else (left.total_len() if left else 0)

    def total_len(self):
        if self.value is not None:
            return len(self.value)
        return (self.left.total_len() if self.left else 0) + (self.right.total_len() if self.right else 0)

def concat(rope_a, rope_b):
    """O(1) concatenation — just create a new parent node."""
    return RopeNode(left=rope_a, right=rope_b)

def rope_index(node, i):
    """Get character at index i. O(log n)."""
    if node.value is not None:
        return node.value[i]
    if i < node.weight:
        return rope_index(node.left, i)
    else:
        return rope_index(node.right, i - node.weight)
```

#### Complexity
| Operation | Rope | Plain Python String |
|---|---|---|
| Concatenation | O(1) (or O(log n) if rebalanced) | O(n) (full copy) |
| Insert at index | O(log n) | O(n) |
| Index access | O(log n) | O(1) |
| Substring | O(log n + k) | O(k) |

#### Applications
- Text editors handling huge files (VS Code, Word use rope-like structures internally)
- Version control diff/patch systems

### 12.5 Piece Table (Overview)
An alternative to Rope used by text editors (e.g., older versions of Microsoft Word, VS Code's early implementations): keeps the **original file buffer immutable**, and all edits are stored in a separate **"add buffer,"** with a table of "pieces" (references into either buffer) describing the current document as a sequence of spans. Insertions/deletions just modify the piece table (O(1) amortized for append-only add buffer), never touching the original data — naturally supporting undo/redo by keeping old piece-table versions.

### 12.6 Gap Buffer (Overview)
A simpler alternative to Rope/Piece Table used in structures like Emacs's buffer implementation: maintains a single array with a "gap" (unused space) positioned at the current cursor location. Insertions at the cursor are O(1) (just fill the gap); moving the cursor requires shifting the gap, O(distance moved). Simple to implement but degrades for editors with many cursors or very large random-access edits (each cursor jump costs O(n) gap-shifting in the worst case).

### 12.7 String Structures — Comparison Table

| Structure | Best For | Build Time | Search | Memory |
|---|---|---|---|---|
| Suffix Array | Substring search, LCP-based problems | O(n log² n) or O(n) advanced | O(m log n) | Low (just int array) |
| Suffix Automaton | Distinct substrings, LCS between 2 strings | O(n) | O(m) | Moderate |
| Suffix Tree | Substring search, repeated substrings | O(n) (Ukkonen's) | O(m) | High (pointer overhead) |
| Rope | Huge mutable strings (editors) | O(n) initial | O(log n) index | Moderate |
| Piece Table | Text editors w/ undo/redo | O(1) per edit | O(pieces) | Low-Moderate |
| Gap Buffer | Simple single-cursor editors | O(n) initial | O(1) at cursor | Low |

### 12.8 Practice Problems (String Structures)
| Problem | Platform | Difficulty |
|---|---|---|
| Longest Duplicate Substring | LeetCode 1044 | Hard |
| Longest Common Substring | GeeksforGeeks | Medium |
| Distinct Substrings | SPOJ | Hard |
| Text Editor | LeetCode 2296 | Medium |

### 12.9 Summary & Revision Notes
- Suffix Array = sorted list of suffix start-indices; pair with Kasai's LCP array for many string algorithms.
- Suffix Automaton = smallest DFA of all suffixes, O(n) build, great for distinct-substring counting.
- Rope/Piece Table/Gap Buffer solve the "editing huge strings efficiently" problem — used inside real text editors.

---

## 13. Cache & Memory Structures

### 13.1 LRU Cache (Least Recently Used)

#### Definition
An **LRU Cache** evicts the **least recently used** item when capacity is exceeded. Implemented via a combination of a **hash map** (O(1) lookup) and a **doubly linked list** (O(1) reordering to mark "most recently used").

#### ASCII Visualization

```
Capacity = 3

Access order: A, B, C, A, D  (D causes eviction since capacity=3)

Doubly Linked List (MRU on left, LRU on right):
After A: [A]
After B: [B, A]
After C: [C, B, A]
After A (access again, move to front): [A, C, B]
After D (insert, evict LRU=B): [D, A, C]   <- B evicted
```

#### Python Implementation

```python
class LRUNode:
    __slots__ = ('key', 'value', 'prev', 'next')
    def __init__(self, key=0, value=0):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    """O(1) get and put using hashmap + doubly linked list."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> LRUNode
        self.head = LRUNode()  # dummy head (MRU side)
        self.tail = LRUNode()  # dummy tail (LRU side)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = LRUNode(key, value)
        self.cache[key] = node
        self._add_front(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

#### Line-by-Line Explanation
- Dummy `head`/`tail` sentinels eliminate special-casing for empty-list operations.
- `get`: on cache hit, the node is unlinked and re-inserted at the front (marking it as most-recently-used) — O(1) via direct pointer manipulation.
- `put`: inserts/updates, then evicts `tail.prev` (the actual least-recently-used node) if over capacity.

#### Complexity
| Operation | Time | Space |
|---|---|---|
| get | O(1) | O(capacity) |
| put | O(1) | O(capacity) |

#### Applications
- OS page replacement, CPU cache eviction policies
- Browser cache, CDN cache eviction
- Database buffer pool management

### 13.2 LFU Cache (Least Frequently Used)

#### Definition
Evicts the item with the **lowest access frequency**; ties broken by least-recently-used among equal-frequency items. Requires O(1) get/put using a combination of hash maps and **frequency buckets** (each bucket is a doubly linked list of keys with that frequency).

#### Python Implementation

```python
from collections import defaultdict, OrderedDict

class LFUCache:
    """O(1) get/put using freq buckets of OrderedDicts (insertion order = recency)."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> {key: None} (ordered)

    def _touch(self, key):
        freq = self.key_to_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None

    def get(self, key):
        if key not in self.key_to_val:
            return -1
        self._touch(key)
        return self.key_to_val[key]

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._touch(key)
            return
        if len(self.key_to_val) >= self.capacity:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[evict_key]
            del self.key_to_freq[evict_key]
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
```

#### Complexity
| Operation | Time | Space |
|---|---|---|
| get | O(1) | O(capacity) |
| put | O(1) | O(capacity) |

#### LRU vs LFU

| Aspect | LRU | LFU |
|---|---|---|
| Eviction criterion | Least recently accessed | Least frequently accessed |
| Adapts to bursty one-time access | Yes (recency matters) | No (a one-time burst inflates frequency, causing "cache pollution") |
| Adapts to steady popular items | Can evict popular-but-not-recent items | Better retains consistently popular items |
| Implementation complexity | Simpler (1 hashmap + 1 linked list) | More complex (freq buckets) |
| Real-world use | CPU caches, most general-purpose caches | CDN caching for stable popularity distributions |

### 13.3 Bloom Filter

#### Definition
A **Bloom Filter** is a space-efficient **probabilistic** set membership structure: `False` means "definitely not in the set," `True` means "possibly in the set" (false positives possible, false negatives impossible). Uses a bit array + multiple independent hash functions.

#### ASCII Visualization

```
Bit array (size 16), 3 hash functions

insert("apple"): h1=2, h2=5, h3=11 -> set bits 2,5,11 to 1
insert("banana"): h1=1, h2=5, h3=9  -> set bits 1,5,9 to 1

Bit array: [0,1,1,0,0,1,0,0,0,1,0,1,0,0,0,0]
                ^ ^     ^     ^   ^
                1 2     5     9   11

query("apple"): check bits 2,5,11 -> all 1 -> "possibly in set" (correct, TRUE positive)
query("grape"): h1=1,h2=9,h3=11 -> all happen to be 1 -> "possibly in set" (FALSE POSITIVE!)
query("kiwi"):  h1=0,h2=3,h3=... -> bit 0 or 3 is 0 -> "definitely NOT in set" (correct)
```

#### Python Implementation

```python
import hashlib

class BloomFilter:
    """Probabilistic set membership. False positives possible, false negatives impossible."""
    def __init__(self, size=1000, num_hashes=5):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hashes(self, item):
        result = []
        for i in range(self.num_hashes):
            h = hashlib.md5(f"{item}_{i}".encode()).hexdigest()
            result.append(int(h, 16) % self.size)
        return result

    def add(self, item):
        for idx in self._hashes(item):
            self.bit_array[idx] = 1

    def might_contain(self, item):
        return all(self.bit_array[idx] == 1 for idx in self._hashes(item))
```

#### Line-by-Line Explanation
- Each item is hashed with `k` independent hash functions (simulated here via salting MD5 with an index), setting `k` bit positions to 1.
- `might_contain` checks if **all** `k` corresponding bits are 1 — if even one is 0, the item was definitely never added. If all are 1, it's *probably* present, but could be a false positive from other items' hash collisions.

#### Optimal Parameters
Given desired false-positive rate `p` and expected number of items `n`:
```
optimal bit array size:  m = -(n * ln(p)) / (ln(2))^2
optimal number of hashes: k = (m/n) * ln(2)
```

#### Complexity
| Operation | Time | Space |
|---|---|---|
| add | O(k) | O(m) bits total |
| might_contain | O(k) | O(1) extra |

> ⚠️ **Warning:** Bloom Filters **cannot delete items** in their basic form (unsetting a bit could break membership for other items sharing that bit). Use a **Counting Bloom Filter** if deletion is needed.

#### Counting Bloom Filter
Replaces each bit with a small counter (e.g., 4 bits). Insertion increments counters; deletion decrements them; membership checks if all relevant counters are > 0. Costs more memory (multiple bits per slot) but supports deletion.

```python
class CountingBloomFilter:
    def __init__(self, size=1000, num_hashes=5):
        self.size = size
        self.num_hashes = num_hashes
        self.counters = [0] * size

    def _hashes(self, item):
        result = []
        for i in range(self.num_hashes):
            h = hashlib.md5(f"{item}_{i}".encode()).hexdigest()
            result.append(int(h, 16) % self.size)
        return result

    def add(self, item):
        for idx in self._hashes(item):
            self.counters[idx] += 1

    def remove(self, item):
        if self.might_contain(item):
            for idx in self._hashes(item):
                self.counters[idx] = max(0, self.counters[idx] - 1)

    def might_contain(self, item):
        return all(self.counters[idx] > 0 for idx in self._hashes(item))
```

#### Cuckoo Filter (Overview)
An alternative to Bloom Filters that supports **deletion natively** (unlike basic Bloom Filters) and often achieves better space efficiency at low false-positive rates. Stores a compact **fingerprint** of each item in one of two candidate buckets (determined by two hash functions), using "cuckoo hashing" — if both candidate buckets are full, it evicts an existing fingerprint to its alternate bucket (like a cuckoo bird pushing eggs out of a nest), cascading until a free slot is found.

#### Applications
- **Bloom Filter**: Chrome's Safe Browsing (checking if URL is malicious without storing the entire blacklist), Cassandra/HBase (avoiding unnecessary disk reads for non-existent keys), Bitcoin SPV clients
- **Counting Bloom Filter**: network routers tracking active flows with deletion support
- **Cuckoo Filter**: modern replacements for Bloom Filters in systems needing deletion (e.g., some CDN cache-existence checks)

### 13.4 Cache Structures — Comparison Table

| Structure | Purpose | False Positives? | Deletion Support |
|---|---|---|---|
| LRU Cache | Evict least recently used | N/A (exact cache) | Yes |
| LFU Cache | Evict least frequently used | N/A (exact cache) | Yes |
| Bloom Filter | Probabilistic set membership | Yes | No |
| Counting Bloom Filter | Probabilistic set membership | Yes | Yes |
| Cuckoo Filter | Probabilistic set membership | Yes (lower rate) | Yes (native) |

### 13.5 Practice Problems (Cache Structures)
| Problem | Platform | Difficulty |
|---|---|---|
| LRU Cache | LeetCode 146 | Medium |
| LFU Cache | LeetCode 460 | Hard |
| Design a Bloom Filter | System Design (conceptual) | Medium |

### 13.6 Summary & Revision Notes
- LRU = hashmap + doubly linked list, O(1) get/put, evicts oldest-accessed.
- LFU = hashmap + frequency buckets, O(1) get/put, evicts least-frequently-accessed.
- Bloom Filter = probabilistic membership, no false negatives, possible false positives, no deletion (use Counting Bloom Filter for that).

---

## 14. Randomized Structures

### 14.1 Treap (Tree + Heap)

#### Definition
A **Treap** is a BST where each node also has a randomly assigned **priority**, and the tree maintains **heap order** on priorities (parent priority ≥ children's, for a max-heap convention) while maintaining **BST order** on keys. The randomization of priorities makes the expected tree height O(log n), avoiding the need for explicit rotation-balancing logic like AVL/Red-Black.

#### Why It Exists
Treaps give the simplicity of a plain BST insert (no complex rotation case analysis) while still guaranteeing **expected** O(log n) height via randomization — it's essentially "AVL/RB tree balancing via probability instead of invariant-checking."

#### ASCII Visualization

```
Insert order with random priorities: (5, pri=90), (3, pri=40), (8, pri=70), (1, pri=95)

BST order by key, heap order by priority (max-heap on priority):

              1(95)
                \
                5(90)
               /    \
             3(40)   8(70)

Verify: BST property (left<node<right by key): 1 < 5, and within 5's subtree 3 < 5 < 8. ✓
Heap property (parent priority >= child priority): 95>=90, 90>=40, 90>=70. ✓
```

#### Python Implementation

```python
import random

class TreapNode:
    __slots__ = ('key', 'priority', 'left', 'right')
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None

class Treap:
    """Randomized BST: BST order by key, max-heap order by random priority."""
    def __init__(self):
        self.root = None

    def _rotate_right(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        return left

    def _rotate_left(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        return right

    def insert(self, root, key):
        if root is None:
            return TreapNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
            if root.left.priority > root.priority:      # heap violation, fix via rotation
                root = self._rotate_right(root)
        else:
            root.right = self.insert(root.right, key)
            if root.right.priority > root.priority:
                root = self._rotate_left(root)
        return root

    def delete(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # rotate down the higher-priority child, then delete from that side
            if root.left.priority > root.right.priority:
                root = self._rotate_right(root)
                root.right = self.delete(root.right, key)
            else:
                root = self._rotate_left(root)
                root.left = self.delete(root.left, key)
        return root
```

#### Line-by-Line Explanation
- Each node gets a random priority at creation (`random.random()`), independent of key.
- `insert` performs a normal BST insert recursively, then **on the way back up**, if the child's priority exceeds the parent's, a rotation fixes the heap-order violation — bubbling high-priority nodes toward the root.
- `delete` rotates the node-to-delete downward (always rotating in the direction of the higher-priority child) until it becomes a leaf, then removes it directly — avoiding the need for a "successor replacement" strategy like standard BST delete.

#### Complete Dry Run
Insert keys `5, 3, 8, 1` with priorities `90, 40, 70, 95` respectively (as in the diagram above):

| Step | Insert | BST Path | Priority Check | Rotation? |
|---|---|---|---|---|
| 1 | 5 (pri=90) | root = 5 | — | none (first node) |
| 2 | 3 (pri=40) | 5.left = 3 | 40 < 90 | no rotation needed |
| 3 | 8 (pri=70) | 5.right = 8 | 70 < 90 | no rotation needed |
| 4 | 1 (pri=95) | descend: 1 < 5 → 5.left=3; 1 < 3 → 3.left = 1 | 1's priority(95) > 3's priority(40) → rotate_right(3) → 3 becomes 1's right child, 1 takes 3's place as 5.left | rotate at node 3 |
| 5 | back up to root=5 | 1's priority(95) > 5's priority(90) → rotate_right(5) | 1 becomes new root, 5 becomes 1's right child | final structure matches diagram |

#### Complexity
| Operation | Expected Time | Space |
|---|---|---|
| Search | O(log n) | O(1) |
| Insert | O(log n) | O(1) |
| Delete | O(log n) | O(1) |

#### Common Mistakes
- ❌ Using a non-random priority (e.g., insertion order) — defeats the entire purpose; height guarantees only hold with **uniform random** priorities.
- ❌ Forgetting priority comparisons must be **strict** and use a proper max-heap convention consistently (mixing max-heap and min-heap conventions across insert/delete causes corruption).

#### Applications
- Competitive programming's go-to "implement an ordered set/map quickly under time pressure" structure
- Randomized balanced BST alternative to AVL/RB when implementation simplicity matters more than worst-case guarantees

### 14.2 Randomized BST (General Concept)
Any BST that uses randomization (either in construction order or via Treap-style priorities) to achieve expected O(log n) height without explicit balance invariants. Treap is the most common concrete example; another is **randomized insertion order BST** (randomly shuffling keys before inserting into a plain BST also yields expected O(log n) height, by a classic probabilistic argument related to quicksort's average case).

### 14.3 Randomized Heap (Overview)
A **Randomized Meldable Heap** (e.g., "Randomized Binary Heap" or "Skew Heap") supports O(log n) expected time for the classic heap operations **plus O(log n) meld** (merging two heaps) — something a standard array-based binary heap cannot do efficiently (array heaps need O(n) to merge). Randomization (flipping a coin to decide which subtree to recurse into during merge) replaces the need for explicit balance bookkeeping, similar in spirit to Treaps.

### 14.4 Skip List (Cross-Reference)
Skip Lists (Section 5) are also a **randomized structure** — the level assignment via coin flips is what gives expected O(log n) height, making it a randomized alternative to balanced BSTs, conceptually a "sibling" to Treaps in the randomized-structures family.

### 14.5 Randomized Structures — Why Randomization Works (Intuition)
The key theoretical insight: **if you can't guarantee your input avoids worst-case patterns, use randomness to guarantee the worst case is astronomically unlikely, rather than trying to detect and fix imbalance explicitly.** This trades deterministic worst-case guarantees for extremely high-probability guarantees, in exchange for much simpler code (no rotation-case enumeration, no color-invariant bookkeeping).

### 14.6 Practice Problems (Randomized Structures)
| Problem | Platform | Difficulty |
|---|---|---|
| Implement a Treap-based ordered set | Competitive Programming (various) | Medium-Hard |
| Merge k sorted heaps | Conceptual / CP | Medium |

### 14.7 Summary & Revision Notes
- Treap = BST (by key) + max-heap (by random priority) → expected O(log n) height without rotation-case logic.
- Randomization is a general technique: trade deterministic guarantees for high-probability guarantees, simplifying implementation.
- Skip List, Treap, and Randomized BST are conceptually related "randomized balance" siblings.

---
## 15. Advanced Graph-Oriented Structures

*(Only the data structures themselves — not general graph algorithms like BFS/DFS/Dijkstra, which belong to the Graphs handbook.)*

### 15.1 DSU (Cross-Reference)
Already covered in full depth in Section 6 — the foundational structure for dynamic connectivity, used inside Kruskal's MST and cycle detection.

### 15.2 Heavy-Light Decomposition (HLD)

#### Definition
**Heavy-Light Decomposition** breaks a tree into a set of vertical chains such that any root-to-node path crosses **O(log n) chains**, enabling path queries/updates (sum, max on a tree path) to be answered in O(log² n) by combining a segment tree with the decomposition.

#### Why It Exists
Segment Trees work on arrays, not trees. HLD "flattens" a tree into an array (via chain-based DFS ordering) so that any path query can be decomposed into O(log n) **contiguous array ranges**, each answerable via a segment tree in O(log n) — giving O(log² n) total.

#### Intuition
At each node, classify one child as "heavy" (the child with the largest subtree) and all others as "light." Heavy edges chain together into long contiguous segments; light edges are "chain transitions." Any root-to-leaf path takes at most O(log n) light edges (because each light edge at least halves the subtree size), hence at most O(log n) chains are involved.

#### ASCII Visualization

```
Tree (numbers = subtree sizes):
          1(7)
         /    \
      2(4)    3(2)
     /   \       \
   4(1)  5(2)    6(1)
         /
       7(1)

Heavy child of 1 = 2 (size 4 > size 2)
Heavy child of 2 = 5 (size 2 > size 1)
Heavy child of 5 = 7

Heavy chain: 1 -> 2 -> 5 -> 7   (drawn as one contiguous array segment)
Light edges: 1->3, 2->4, 5-> (nothing else), 3->6

Flattened array (chain-based DFS order): [1, 2, 5, 7, 4, 3, 6]
                                           <--chain1--> <c2> <c3><c4>
```

#### Python Implementation (HLD + Segment Tree for path sum queries)

```python
import sys

class HeavyLightDecomposition:
    """
    Supports path queries (e.g., sum) on a tree in O(log^2 n),
    and subtree queries in O(log n) via the flattened array + segment tree.
    """
    def __init__(self, n, adj, values, root=0):
        self.n = n
        self.adj = adj              # adjacency list
        self.values = values        # value at each node
        self.root = root
        self.parent = [-1] * n
        self.depth = [0] * n
        self.heavy = [-1] * n
        self.subtree_size = [1] * n
        self.head = [0] * n         # chain head for each node
        self.pos = [0] * n          # position in flattened array
        self._dfs_sizes(root, -1)
        self.cur_pos = 0
        self._decompose(root, root)
        # segment tree built over self.pos-ordered values (uses SegmentTree from Section 2)

    def _dfs_sizes(self, u, par):
        self.parent[u] = par
        max_size = 0
        for v in self.adj[u]:
            if v != par:
                self.depth[v] = self.depth[u] + 1
                self._dfs_sizes(v, u)
                self.subtree_size[u] += self.subtree_size[v]
                if self.subtree_size[v] > max_size:
                    max_size = self.subtree_size[v]
                    self.heavy[u] = v

    def _decompose(self, u, h):
        self.head[u] = h
        self.pos[u] = self.cur_pos
        self.cur_pos += 1
        if self.heavy[u] != -1:
            self._decompose(self.heavy[u], h)   # continue the SAME chain for heavy child
        for v in self.adj[u]:
            if v != self.parent[u] and v != self.heavy[u]:
                self._decompose(v, v)            # light child starts a NEW chain

    def query_path(self, seg_tree, u, v):
        """Combine O(log n) chain segments to answer a path query via segment tree."""
        result = 0
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            result += seg_tree.query(self.pos[self.head[u]], self.pos[u])
            u = self.parent[self.head[u]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        result += seg_tree.query(self.pos[u], self.pos[v])
        return result
```

#### Line-by-Line Explanation
- `_dfs_sizes`: computes subtree sizes and marks each node's "heavy child" (largest subtree) in one DFS.
- `_decompose`: assigns each node a position in the flattened array, continuing the parent's chain for the heavy child (`h` stays the same) but starting a **new chain** (`h = v`) for light children.
- `query_path`: repeatedly jumps from the **deeper chain head** up to its parent, querying the segment tree over that chain's contiguous array range, until both `u` and `v` are on the same chain — then does one final query within that chain.

#### Complete Dry Run
Using the tree from the visualization, query the path sum between nodes `4` and `6`:

| Step | u | v | head[u] | head[v] | Action |
|---|---|---|---|---|---|
| 1 | 4 | 6 | 2 (chain: 1-2-5-7's head is 1; but 4 is light child of 2, so head[4]=4) | head[6]=6 (light child of 3) | heads differ, compare depth |
| 2 | depth[head[4]]=depth[4]=2, depth[head[6]]=depth[6]=2 (equal) | | since equal, either can be treated as "u" | pick u=6 arbitrarily | query pos[head[6]]..pos[6] = single node 6, then u=parent[6]=3 |
| 3 | Now u=3, v=4. head[3]=3(light child of 1), head[4]=4 | still different heads | depth[3]=1 < depth[4]=2 -> swap: u=4,v=3 | query pos[head[4]]..pos[4]=single node 4, then u=parent[4]=2 |
| 4 | Now u=2, v=3. head[2]=1 (heavy chain), head[3]=3 | different heads, depth[1]=0<depth[3]=1 -> swap u=3,v=2 | query node 3 alone, u=parent[3]=1 | |
| 5 | Now u=1, v=2. head[1]=1=head[2]=1 | SAME chain! | final query: pos[1]..pos[2] (both on heavy chain, contiguous) | combine all partial sums: node6 + node4 + node3 + (node1,node2 range) = full path sum ✅ |

#### Complexity
| Operation | Time | Space |
|---|---|---|
| Preprocessing (DFS + decompose) | O(n) | O(n) |
| Path query/update | O(log² n) | O(1) extra (uses segment tree's O(log n) internally) |
| Subtree query/update | O(log n) | O(1) extra |

#### Common Mistakes
- ❌ Forgetting to always jump from the **deeper** chain head — jumping from the shallower one breaks correctness.
- ❌ Off-by-one when the final same-chain segment needs `min(pos[u], pos[v])` to `max(pos[u], pos[v])`.
- ❌ Not handling the case where `u == v` (path query on a single node).

#### Applications
- Tree path queries (sum/max/min on path between two nodes) in competitive programming
- LCA computation (as a side effect of HLD's chain jumping)
- Dynamic tree problems needing efficient path updates

### 15.3 Link-Cut Tree (Overview)

A **Link-Cut Tree** maintains a forest of trees supporting `link(u,v)`, `cut(u,v)`, and path queries in **amortized O(log n)**, even as the tree structure itself changes dynamically (unlike HLD, which assumes a static tree). Built using **splay trees** to represent "preferred paths," with an `access()` operation that re-roots the splay-tree representation on demand. Considered one of the most complex data structures in competitive programming — typically only appears in Div-1 Codeforces problems tagged "data structures" at the hardest tier.

### 15.4 Euler Tour Tree (Overview)

Represents a forest using an **Euler tour** (each edge traversed twice: once entering, once leaving a subtree) stored in a balanced BST (often a Splay Tree or Treap), enabling `link`, `cut`, and subtree aggregate queries in **O(log n)** amortized — an alternative to Link-Cut Trees, generally simpler for subtree queries but less flexible for arbitrary path queries.

### 15.5 Dynamic Trees (General Concept, Overview)

An umbrella term for structures (Link-Cut Trees, Euler Tour Trees, Top Trees) that support **online updates to the tree's edge structure itself** (not just node values) — `link`, `cut`, and re-rooting — while still answering aggregate queries efficiently. Essential for problems where the underlying graph/tree changes over time (e.g., dynamic connectivity with edge insertions/deletions in a forest).

### 15.6 Graph-Oriented Structures — Comparison

| Structure | Handles | Update Type | Query Time | Complexity to Implement |
|---|---|---|---|---|
| DSU | Static forest, connectivity | Union only (no cut) | ~O(1) amortized | Low |
| HLD | Static tree, path/subtree queries | Node value updates | O(log² n) path, O(log n) subtree | Medium |
| Link-Cut Tree | Dynamic forest | Link + Cut + path queries | O(log n) amortized | Very High |
| Euler Tour Tree | Dynamic forest | Link + Cut + subtree queries | O(log n) amortized | High |

### 15.7 Practice Problems (Graph-Oriented Structures)
| Problem | Platform | Difficulty |
|---|---|---|
| Path Queries | CSES | Hard |
| Company Queries II (LCA) | CSES | Medium |
| Query on a tree (HLD) | SPOJ QTREE | Hard |
| Dynamic Connectivity | Codeforces | Very Hard |

### 15.8 Summary & Revision Notes
- HLD flattens a tree into O(log n) chains, enabling O(log² n) path queries via segment tree.
- Link-Cut Trees / Euler Tour Trees handle **dynamic** tree structure changes (edges added/removed), unlike HLD which assumes a static tree shape.
- DSU remains the go-to for pure connectivity without needing path aggregate queries.

---

## 16. Competitive Programming Structures

### 16.1 Mo's Algorithm (Data Structure Perspective)

#### Definition
**Mo's Algorithm** is an **offline** query-processing technique: given `Q` range queries `[l, r]` on a static array, sort queries by block (using √n block decomposition) and process them in an order that minimizes the total pointer movement, achieving `O((n + Q) √n)` total time instead of `O(Q · n)` naive.

#### Why It Exists
If you have many range queries (e.g., "count distinct elements in range [l,r]") that can't be answered with a simple prefix-sum trick, but they're all known **in advance** (offline), Mo's Algorithm lets you reuse work between similar queries by processing them in a clever sorted order.

#### Intuition
Sort queries by `(l // block_size, r)`. Maintain a "current window" `[cur_l, cur_r]` with two pointers; for each query, slide the pointers to match the new `[l, r]`, adding/removing elements one at a time and updating a running answer — because queries are sorted, the total pointer movement across all queries is bounded by `O((n+Q)√n)`.

#### ASCII Visualization

```
Array: [1,2,1,3,2,1,4]   Queries: (0,3), (2,5), (1,6), (0,2)

Block size = sqrt(7) ~ 3

Sort queries by (l/block, r):
  (0,2): block 0, r=2
  (0,3): block 0, r=3
  (2,5): block 0, r=5   <- wait, l=2 is also block 0 (2//3=0)
  (1,6): block 0, r=6

Processing in this order, cur_l/cur_r move minimally between consecutive queries
instead of jumping randomly -> total movement bounded by O(n*sqrt(n))
```

#### Python Implementation

```python
import math
from collections import defaultdict

def mos_algorithm(arr, queries):
    """
    queries: list of (l, r, original_index) - answer count of distinct elements in [l, r]
    Returns answers in original query order.
    """
    n = len(arr)
    block_size = max(1, int(math.sqrt(n)))

    def mo_cmp(query):
        l, r, _ = query
        block = l // block_size
        # alternate sort direction of r per block to reduce pointer thrashing (optimization)
        return (block, r if block % 2 == 0 else -r)

    queries_sorted = sorted(queries, key=mo_cmp)

    freq = defaultdict(int)
    distinct_count = 0
    cur_l, cur_r = 0, -1
    answers = [0] * len(queries)

    def add(idx):
        nonlocal distinct_count
        freq[arr[idx]] += 1
        if freq[arr[idx]] == 1:
            distinct_count += 1

    def remove(idx):
        nonlocal distinct_count
        freq[arr[idx]] -= 1
        if freq[arr[idx]] == 0:
            distinct_count -= 1

    for l, r, orig_idx in queries_sorted:
        while cur_r < r:
            cur_r += 1
            add(cur_r)
        while cur_l > l:
            cur_l -= 1
            add(cur_l)
        while cur_r > r:
            remove(cur_r)
            cur_r -= 1
        while cur_l < l:
            remove(cur_l)
            cur_l += 1
        answers[orig_idx] = distinct_count

    return answers
```

#### Line-by-Line Explanation
- Queries are sorted by `(block of l, r)` — this ensures `cur_l` only moves within a block (`O(√n)` per block transition) while `r` moves monotonically within each block, bounding total movement.
- The **alternating sort direction** for `r` (odd vs even blocks) is a common optimization that avoids `cur_r` snapping back to the start of a new block, roughly halving practical runtime.
- Four `while` loops adjust `cur_l`/`cur_r` step-by-step toward the target `[l, r]`, calling `add`/`remove` for each single-element pointer move.

#### Complexity
| Metric | Value |
|---|---|
| Total pointer movements | O((n + Q) √n) |
| Time per add/remove | O(1) (for distinct-count; varies by problem) |
| Overall time | O((n + Q) √n) |
| Requirement | Must be **offline** (all queries known upfront) |

#### Common Mistakes
- ❌ Applying Mo's Algorithm to problems requiring **online** queries (each query must be answered immediately, in order) — Mo's fundamentally requires reordering queries.
- ❌ Forgetting the alternating sort-direction optimization — still correct without it, but noticeably slower in practice.
- ❌ Using Mo's Algorithm when a simpler prefix-sum/BIT solution exists — Mo's is a **fallback** for queries that don't decompose nicely (e.g., "count distinct," "mode of range").

#### Applications
- "Count distinct elements in range [l,r]" across many queries
- "Range mode query" (most frequent element in a range)
- Any range query that's hard to maintain incrementally but easy to update with single-element add/remove

### 16.2 Ordered Set / Ordered Map (Python Alternatives)

Python's standard library has no built-in balanced BST like C++'s `std::set` / Java's `TreeSet`. Common alternatives:

```python
# Option 1: sortedcontainers library (most popular, C-optimized, O(sqrt(n)) worst-case
# but very fast in practice due to internal array-of-arrays with block rebalancing)
from sortedcontainers import SortedList, SortedDict, SortedSet

sl = SortedList([5, 1, 4, 2])
sl.add(3)
print(sl)                      # SortedList([1, 2, 3, 4, 5])
print(sl.bisect_left(3))       # index where 3 would be inserted (returns 2)
print(sl[0], sl[-1])           # min and max in O(1)
sl.remove(3)                   # O(sqrt(n))

# Option 2: bisect module + list (manual, O(n) insert due to shifting, O(log n) search)
import bisect
arr = [1, 2, 4, 5]
bisect.insort(arr, 3)          # inserts 3 in sorted position -> O(n) due to list shift
idx = bisect.bisect_left(arr, 4)  # O(log n) binary search
```

> 📝 **Note:** `sortedcontainers.SortedList` is implemented as a "list of sorted lists" (load-balanced), giving O(√n) worst-case insert/delete but excellent real-world constants — often the pragmatic choice in Python competitive programming instead of implementing a Treap/AVL from scratch.

### 16.3 Policy-Based Data Structures (Concept Only)

In C++, GNU's Policy-Based Data Structures (`__gnu_pbds`) provide an "ordered set" supporting `order_of_key` (rank of an element) and `find_by_order` (k-th smallest) in O(log n) — features `std::set` lacks. **Python has no direct equivalent**, but the same functionality can be approximated with:
- A **Fenwick Tree over compressed coordinates** (rank queries via prefix sum, O(log n))
- `sortedcontainers.SortedList` (`.bisect_left()` for rank, indexing `sl[k]` for k-th smallest) — both O(log n) amortized in practice.

### 16.4 Persistent Structures (Cross-Reference)
See Section 2.16 (Persistent Segment Tree) and Section 17.1 (Persistent Data Structures general concept).

### 16.5 Coordinate Compression (Cross-Reference)
Already covered in Section 3.13 — essential companion technique whenever BIT/Segment Tree indices must be dense but input values are sparse/huge.

### 16.6 Practice Problems (CP Structures)
| Problem | Platform | Difficulty |
|---|---|---|
| Range Distinct Queries | CSES | Hard |
| D-Query (distinct in range) | SPOJ | Hard |
| Powerful Array | Codeforces 86D | Hard (classic Mo's) |

### 16.7 Summary & Revision Notes
- Mo's Algorithm = offline query reordering for O((n+Q)√n) range queries that don't decompose nicely.
- `sortedcontainers.SortedList` is Python's pragmatic stand-in for C++'s ordered set/Policy-Based Data Structures.
- Coordinate compression is a mandatory companion whenever indices need to be dense.

---

## 17. Advanced Concepts

### 17.1 Persistent Data Structures

**Definition:** Structures where every "modification" produces a **new version** while all previous versions remain accessible and unmodified — achieved by sharing unchanged substructure between versions (structural sharing) rather than copying everything.

```
Full copy (naive persistence):        Structural sharing (true persistence):
v0: [1,2,3,4,5]                       v0 root -----> shares most nodes with v1
v1: [1,2,3,4,5] (copy) with idx2=99   v1 root -----> only new nodes on the changed path
Space: O(n) per version (wasteful)     Space: O(log n) new nodes per version (efficient)
```

Already demonstrated concretely via the Persistent Segment Tree (Section 2.16).

### 17.2 Functional / Immutable Data Structures

**Definition:** Data structures where objects are **never mutated** after creation — every "update" operation returns a new structure. Common in functional languages (Haskell, Clojure, Scala) and increasingly in Python for thread-safety and predictable state (e.g., using `tuple` instead of `list`, `frozenset` instead of `set`, or libraries like `pyrsistent`).

```python
# Immutable linked list (functional style) in Python
class ImmutableNode:
    __slots__ = ('value', 'next')
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def cons(value, lst):
    """O(1) - prepend without modifying the original list."""
    return ImmutableNode(value, lst)

# Usage:
lst1 = cons(3, cons(2, cons(1, None)))   # 3 -> 2 -> 1
lst2 = cons(4, lst1)                      # 4 -> 3 -> 2 -> 1 (lst1 untouched, structure shared!)
```

**Why it matters:** immutability eliminates entire classes of concurrency bugs (no locks needed for read access), enables trivial undo/redo, and simplifies reasoning about program state — at the cost of extra allocation and potentially worse cache locality than in-place mutation.

### 17.3 Cache-Friendly / Cache-Oblivious Structures

**Definition:** Structures designed to perform well regardless of the specific CPU cache size/line size ("cache-oblivious") by using recursive, self-similar layouts (e.g., **van Emde Boas layout** for trees) that guarantee good locality at every level of the memory hierarchy simultaneously, without needing to know cache parameters at compile time.

**Practical Python note:** Python's object overhead (each object has significant header bytes) makes true cache-oblivious design less impactful than in C/C++, but the **general principle still matters**: array-based structures (segment trees, BIT) consistently outperform pointer-based ones (linked BSTs) in practice due to memory locality — this is part of why the iterative segment tree (Section 2.14) beats the recursive/pointer version despite identical asymptotic complexity.

### 17.4 Succinct Data Structures (Overview)

**Definition:** Structures that represent data using space **close to the information-theoretic minimum** (e.g., representing a bit array of `n` bits using `n + o(n)` bits, not `O(n)` bits with a large constant), while still supporting fast queries. Key primitives: **rank** (count of 1-bits up to position `i`) and **select** (position of the k-th 1-bit), both achievable in O(1) with `o(n)`-bit auxiliary structures.

**Applications:** succinct trees (representing a tree with `2n + o(n)` bits instead of pointer-heavy `O(n log n)` bits), compressed suffix arrays, search engines needing to fit huge indexes in RAM (e.g., FM-index for genome search).

### 17.5 External Memory / Disk-Based Structures (Overview)

**Definition:** Structures explicitly designed for data **larger than RAM**, optimized to minimize disk I/O operations rather than raw CPU operations. B-Trees/B+ Trees (Section 8) are the classic example. Other notable structures:
- **LSM-Tree (Log-Structured Merge Tree):** used by Cassandra, RocksDB, LevelDB — batches writes in memory (memtable), periodically flushing sorted runs to disk (SSTables), merging them in the background — optimized for **write-heavy** workloads, unlike B-Trees which are more balanced for read/write.
- **External Memory Sorting:** merge-sort variants that read/write in disk-block-sized chunks to minimize seeks.

### 17.6 Advanced Concepts — Comparison Table

| Concept | Core Idea | Real-World Example |
|---|---|---|
| Persistent | Every update creates a new queryable version via structural sharing | Git (loosely analogous), persistent segment tree |
| Functional/Immutable | No mutation, every "change" returns a new object | Clojure's data structures, Python tuples |
| Cache-Oblivious | Recursive self-similar layout, good locality at all cache levels | Van Emde Boas tree layout |
| Succinct | Near information-theoretic-minimum space, still fast queries | FM-index (genome search), compressed suffix arrays |
| External Memory | Minimize disk I/O, not just CPU ops | B+ Tree (databases), LSM-Tree (Cassandra/RocksDB) |

### 17.7 Practice Problems (Advanced Concepts)
| Problem | Platform | Difficulty |
|---|---|---|
| Persistent Array Queries | Codeforces (various) | Hard |
| Design an immutable linked list | Conceptual | Medium |

### 17.8 Summary & Revision Notes
- Persistent = keep every version queryable via structural sharing (not full copies).
- Functional/Immutable = no mutation, safe for concurrency, common in Haskell/Clojure and increasingly Python.
- Succinct = near-minimum space with rank/select primitives for O(1) queries.
- External memory structures (B-Trees, LSM-Trees) optimize for disk I/O, not CPU cycles.

---

## 18. Real-World Applications

### 18.1 Applications by Domain

| Domain | Data Structures Used | Why |
|---|---|---|
| **Databases** | B+ Tree, LSM-Tree, Bloom Filter | Fast indexed lookups, range scans, avoiding unnecessary disk reads |
| **Search Engines** | Suffix Array/Automaton, Bloom Filter, Inverted Index (Trie-based, separate handbook) | Fast substring/keyword search over huge corpora |
| **Operating Systems** | Red-Black Tree (Linux CFS scheduler), LRU Cache (page replacement), Buddy allocator (not covered here) | Predictable O(log n) scheduling, cache eviction |
| **Compilers** | Interval Trees (register allocation liveness ranges), DSU (variable aliasing/union-find in type inference) | Efficient range/set operations during compilation passes |
| **GIS (Geographic Info Systems)** | R-Tree, Quad Tree, KD-Tree | Spatial indexing of geographic shapes and points |
| **Networking** | Bloom Filter (routing table lookups), Skip List (some router data structures) | Space-efficient probabilistic membership checks |
| **Distributed Systems** | Bloom Filter (Cassandra), LSM-Tree (RocksDB/Cassandra storage engine), Merkle Trees (not covered — see Trees handbook) | Efficient replication, conflict detection, write-heavy storage |
| **Competitive Programming** | Segment Tree, Fenwick Tree, DSU, Sparse Table, Treap | The bread-and-butter toolkit for range queries and connectivity problems |
| **AI / Machine Learning** | KD-Tree (k-NN), Bloom Filter (deduplication in large datasets) | Fast nearest-neighbor search, efficient data pipeline dedup |
| **Game Development** | Quad Tree/Octree (collision detection), Spatial Hashing | Efficient broad-phase collision detection in 2D/3D worlds |

### 18.2 Interview Signal Phrases → Data Structure Mapping

| Interviewer Says... | You Should Think... |
|---|---|
| "...many range sum queries with updates..." | Fenwick Tree or Segment Tree |
| "...range min/max with updates..." | Segment Tree (BIT can't do non-invertible ops) |
| "...static array, many range queries, no updates..." | Sparse Table (O(1) query) |
| "...are these two elements connected/in the same group..." | DSU |
| "...design an LRU cache..." | HashMap + Doubly Linked List |
| "...design a search autocomplete / prefix matching..." | Trie (see Trees handbook) or Suffix Array |
| "...nearest neighbor in 2D/3D space..." | KD-Tree |
| "...detect if URL/username might already exist, huge dataset..." | Bloom Filter |
| "...need an ordered set with rank/k-th-smallest..." | Fenwick Tree over compressed coords, or `sortedcontainers.SortedList` |
| "...path queries on a tree..." | Heavy-Light Decomposition |
| "...database index design..." | B+ Tree |

---
## 19. Problem Recognition Guide

### 19.1 Master Decision Tree

```
START: What does the problem primarily ask for?
│
├── "Range aggregate query (sum/min/max) over an array, WITH updates"
│    │
│    ├── Is the array STATIC (never updates)? ──YES──> Sparse Table (O(1) query) [if idempotent op]
│    │                                          │
│    │                                          NO (below)
│    │
│    ├── Need only SUM (invertible op)? ──YES──> Fenwick Tree (simpler, less code)
│    │
│    ├── Need MIN/MAX/GCD (non-invertible)? ──YES──> Segment Tree
│    │
│    └── Need RANGE UPDATES too (not just point)? ──YES──> Segment Tree + Lazy Propagation
│                                                    (or Fenwick "two-BIT" trick for sum-only)
│
├── "Are two elements/nodes connected? Merge groups dynamically."
│    └──> DSU (Union-Find) with path compression + union by rank/size
│
├── "Ordered set/map operations: search, insert, delete, k-th smallest, rank"
│    ├── Need it FAST under time pressure, simplicity matters? ──> Treap or sortedcontainers.SortedList
│    ├── Need STRICT worst-case guarantees? ──> AVL Tree
│    └── General purpose, moderate rotations? ──> Red-Black Tree
│
├── "Path queries/updates on a TREE (sum/max between two nodes)"
│    ├── Tree structure is STATIC? ──> Heavy-Light Decomposition + Segment Tree
│    └── Tree structure CHANGES dynamically (links/cuts)? ──> Link-Cut Tree
│
├── "Find all intervals overlapping with a query interval"
│    └──> Interval Tree (augmented BST with subtree max-high)
│
├── "Nearest neighbor / spatial range query in 2D/3D"
│    ├── Points, low dimensions? ──> KD-Tree
│    ├── Uniform 2D/3D regions, games/GIS? ──> Quad Tree / Octree
│    └── Rectangles/shapes, spatial database? ──> R-Tree
│
├── "Substring search / longest common substring / repeated substrings"
│    └──> Suffix Array (+ LCP array via Kasai's) or Suffix Automaton
│
├── "Check if item MIGHT be in a huge set, memory is tight, false positives OK"
│    └──> Bloom Filter (or Counting Bloom Filter if deletion needed)
│
├── "Design a cache with eviction policy"
│    ├── Evict least RECENTLY used? ──> LRU Cache (HashMap + Doubly Linked List)
│    └── Evict least FREQUENTLY used? ──> LFU Cache (HashMap + frequency buckets)
│
├── "Many OFFLINE range queries, answer doesn't decompose nicely (e.g., distinct count)"
│    └──> Mo's Algorithm (√n block decomposition + sorted query order)
│
├── "Need to query PAST versions of a data structure after updates"
│    └──> Persistent Segment Tree / Persistent structure with structural sharing
│
└── "Database / huge dataset, need disk-efficient indexing"
     └──> B+ Tree (data in leaves, linked for range scans)
```

### 19.2 Recognition Clues Table

| Keyword / Clue in Problem | Likely Structure |
|---|---|
| "prefix sum", "range sum", "cumulative frequency" | Fenwick Tree |
| "range minimum/maximum query" | Segment Tree or Sparse Table (if static) |
| "lazy propagation", "range update" | Segment Tree with lazy propagation |
| "union", "merge groups", "connected components" | DSU |
| "k-th smallest/largest in range" | Merge Sort Tree, Persistent Segment Tree, or Wavelet Tree |
| "balanced BST", "ordered set from scratch" | AVL / Red-Black / Treap |
| "path between two nodes in a tree" | Heavy-Light Decomposition |
| "overlapping intervals", "meeting rooms", "calendar" | Interval Tree |
| "nearest point", "k-NN" | KD-Tree |
| "membership test", "duplicate detection at scale" | Bloom Filter |
| "LRU", "LFU", "cache eviction" | LRU/LFU Cache |
| "longest common substring", "repeated substring" | Suffix Array / Suffix Automaton |
| "many static queries", "offline queries" | Sparse Table or Mo's Algorithm |
| "version history", "undo", "time travel query" | Persistent Data Structure |
| "database index", "range scan" | B+ Tree |

### 19.3 Complexity-Based Selection Guide

| If you need... | ...then pick |
|---|---|
| O(1) query, static data | Sparse Table (idempotent ops), Prefix Sum (any op) |
| O(log n) query + O(log n) update | Segment Tree, Fenwick Tree, AVL/RB Tree |
| O(√n) query + O(1) update | Sqrt Decomposition |
| O(α(n)) ≈ O(1) amortized | DSU |
| O(log² n) tree path query | Heavy-Light Decomposition |
| O(1) amortized set membership (probabilistic) | Bloom Filter |

---

## 20. Complexity Comparison — Master Tables

### 20.1 The Grand Unified Complexity Table

| Structure | Build | Search | Insert | Delete | Range Query | Range Update | Space |
|---|---|---|---|---|---|---|---|
| Segment Tree | O(n) | — | O(log n) point | O(log n) point | O(log n) | O(log n) w/ lazy | O(n) |
| Fenwick Tree | O(n log n) | — | O(log n) point | O(log n) point | O(log n) | O(log n) (2-BIT) | O(n) |
| Sparse Table | O(n log n) | — | Not supported | Not supported | O(1) | Not supported | O(n log n) |
| Sqrt Decomposition | O(n) | — | O(1) point | O(1) point | O(√n) | O(√n) | O(n) |
| Skip List | O(n log n) | O(log n) exp. | O(log n) exp. | O(log n) exp. | O(n) (no native range agg) | — | O(n log n) exp. |
| DSU | O(n) | O(α(n)) find | O(α(n)) union | Not supported (no split) | — | — | O(n) |
| AVL Tree | O(n log n) | O(log n) | O(log n) | O(log n) | O(log n) w/ augmentation | — | O(n) |
| Red-Black Tree | O(n log n) | O(log n) | O(log n) | O(log n) | O(log n) w/ augmentation | — | O(n) |
| Splay Tree | O(n log n) amort. | O(log n) amort. | O(log n) amort. | O(log n) amort. | — | — | O(n) |
| Treap | O(n log n) exp. | O(log n) exp. | O(log n) exp. | O(log n) exp. | O(log n) w/ augmentation | O(log n) w/ lazy | O(n) |
| B-Tree/B+ Tree | O(n log_t n) | O(log_t n) | O(log_t n) | O(log_t n) | O(log_t n + k) (B+ only) | — | O(n) |
| Interval Tree | O(n log n) | O(log n) | O(log n) | O(log n) | O(log n + k) overlap | — | O(n) |
| KD-Tree | O(n log n) | O(log n) avg NN | O(log n) avg | O(log n) avg | O(√n + k) range | — | O(n) |
| Bloom Filter | O(n·k) | — | O(k) | Not supported (basic) | — | — | O(m) bits |
| LRU/LFU Cache | O(1) init | O(1) get | O(1) put | O(1) evict | — | — | O(capacity) |
| Suffix Array | O(n log² n) | O(m log n) | — | — | — | — | O(n) |
| HLD | O(n) | — | — | — | O(log² n) path | O(log² n) path | O(n) |
| Link-Cut Tree | O(n) | — | O(log n) amort. link/cut | O(log n) amort. | O(log n) amort. path | O(log n) amort. | O(n) |

*(n = number of elements, k = matches returned or dimensions where applicable, t = B-Tree degree, m = query string length)*

### 20.2 Head-to-Head Comparisons (Explicitly Requested)

#### Segment Tree vs Fenwick Tree
| Aspect | Segment Tree | Fenwick Tree |
|---|---|---|
| Space | O(4n) | O(n) |
| Supported operations | Any associative op | Invertible ops only (sum, XOR) |
| Range update + range query | Native (lazy propagation) | Needs "two BIT" trick |
| Code complexity | Higher | Very low (~15 lines) |
| Best for | Min/max/gcd range queries | Pure sum/frequency queries |

#### AVL vs Red-Black Tree
| Aspect | AVL | Red-Black |
|---|---|---|
| Balance strictness | Height diff ≤ 1 (strict) | Up to 2x height diff (loose) |
| Search speed | Faster | Slightly slower |
| Insert/Delete speed | Slower (more rotations) | Faster (fewer rotations) |
| Best for | Read-heavy | Write-heavy |

#### Skip List vs Balanced BST
| Aspect | Skip List | Balanced BST |
|---|---|---|
| Guarantee type | Expected (probabilistic) | Worst-case (deterministic) |
| Implementation complexity | Simple | Complex (rotation logic) |
| Concurrency friendliness | Good | Harder |

#### Sparse Table vs Segment Tree
| Aspect | Sparse Table | Segment Tree |
|---|---|---|
| Mutability | Static only | Dynamic |
| Query time | O(1) | O(log n) |
| Supported ops | Idempotent only | Any associative |

#### B-Tree vs B+ Tree
| Aspect | B-Tree | B+ Tree |
|---|---|---|
| Data location | Any node | Leaves only |
| Range scan | Slower (no leaf linking) | Fast (linked leaves) |
| Used in | Legacy filesystems | Modern RDBMS (MySQL, PostgreSQL) |

#### LRU vs LFU
| Aspect | LRU | LFU |
|---|---|---|
| Eviction basis | Recency | Frequency |
| Handles bursty one-time access | Better | Worse (cache pollution) |
| Handles steady popularity | Can evict popular-but-stale items | Better retention |

#### Persistent vs Normal Structures
| Aspect | Persistent | Normal (Ephemeral) |
|---|---|---|
| Version access | All versions queryable | Only latest version exists |
| Space per update | O(log n) new nodes | O(1) (in-place mutation) |
| Use case | Version control, offline k-th-smallest-in-range-of-history | Standard single-version workloads |

---

## 21. Python Tips for Advanced DS

### 21.1 `bisect` Module — Binary Search on Sorted Sequences

```python
import bisect

arr = [1, 3, 4, 4, 6, 8]
bisect.bisect_left(arr, 4)    # 2  -> leftmost insertion point for 4
bisect.bisect_right(arr, 4)   # 4  -> rightmost insertion point for 4
bisect.insort(arr, 5)         # inserts 5 in sorted position, O(n) due to list shifting

# Use case: coordinate compression rank lookup
sorted_unique = sorted(set(arr))
rank_of_x = bisect.bisect_left(sorted_unique, x)
```

### 21.2 `heapq` Module — Binary Heap Primitives

```python
import heapq

h = [5, 2, 8, 1]
heapq.heapify(h)               # O(n) in-place min-heap conversion
heapq.heappush(h, 3)           # O(log n)
smallest = heapq.heappop(h)    # O(log n)
heapq.heapreplace(h, 10)       # pop then push, O(log n), more efficient than separate calls
top_3 = heapq.nsmallest(3, h)  # O(n log k)

# For max-heap: negate values on push/pop
max_heap = []
heapq.heappush(max_heap, -5)
largest = -heapq.heappop(max_heap)
```

### 21.3 `collections` Module Essentials

```python
from collections import defaultdict, OrderedDict, deque, Counter

# defaultdict avoids KeyError boilerplate, useful for adjacency lists, frequency maps
graph = defaultdict(list)
graph[1].append(2)

# OrderedDict maintains insertion order + supports move_to_end() -> useful for LRU
od = OrderedDict()
od['a'] = 1
od.move_to_end('a')            # O(1), moves 'a' to the end (most-recently-used position)
od.popitem(last=False)         # O(1), pops the FIRST item (least-recently-used)

# deque for O(1) append/pop from BOTH ends (unlike list's O(n) pop(0))
dq = deque([1, 2, 3])
dq.appendleft(0)               # O(1)
dq.popleft()                   # O(1)
```

> 💡 **Tip:** A minimal LRU Cache can actually be implemented in ~10 lines using `OrderedDict` instead of a custom doubly linked list — great for interviews when time is short, though understanding the manual linked-list version (Section 13.1) demonstrates deeper understanding.

### 21.4 `array` Module — Memory-Efficient Homogeneous Arrays

```python
from array import array

# Regular Python list of ints has significant per-element overhead (~28 bytes/int object + pointer)
# array module stores raw C-type values contiguously -> much more memory-efficient
int_array = array('i', [1, 2, 3, 4])   # 'i' = signed int, 4 bytes each
int_array.append(5)
```

**When to use:** large numeric arrays (millions of elements) where memory matters — e.g., segment tree leaves, BIT arrays for huge n.

### 21.5 Recursion Limits & Iterative Alternatives

```python
import sys
sys.setrecursionlimit(10**6)   # default is ~1000, often too low for deep recursive trees/DFS

# BUT: increasing recursion limit doesn't increase the ACTUAL C stack size in CPython
# -> can still segfault on very deep recursion (e.g., >100k depth) despite the limit being raised.
# Prefer iterative implementations for:
#   - DSU find() on adversarial/skewed input
#   - Deep tree traversals (unbalanced BST edge case)
#   - Any recursive segment tree build on n > 10^6
```

### 21.6 `__slots__` — Memory Optimization for Node-Based Structures

```python
class TreeNodeSlow:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    # Each instance has a __dict__ -> ~120+ bytes overhead per object

class TreeNodeFast:
    __slots__ = ('val', 'left', 'right')
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    # No __dict__ -> significantly less memory per node, faster attribute access
```

> ⚠️ **Warning:** `__slots__` prevents adding new attributes dynamically and doesn't play well with multiple inheritance unless carefully managed — but for millions of tree nodes (segment tree, BST, Treap), the memory savings are substantial and usually worth it.

### 21.7 `dataclass` — Cleaner Node Definitions

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    key: int
    priority: float = 0.0
    left: Optional['Node'] = None
    right: Optional['Node'] = None

# Combine with slots for best of both worlds (Python 3.10+):
@dataclass(slots=True)
class FastNode:
    key: int
    left: Optional['FastNode'] = None
    right: Optional['FastNode'] = None
```

### 21.8 Object Optimization Checklist

| Technique | Benefit | When to Use |
|---|---|---|
| `__slots__` | Reduces per-object memory, faster attribute access | Any node-based structure with millions of instances |
| Iterative over recursive | Avoids stack overflow, often faster (no call overhead) | Deep trees, large n |
| Array-based over pointer-based | Better cache locality | Segment tree, BIT, heaps |
| `sys.setrecursionlimit` | Allows deeper recursion when truly needed | Only as a last resort, prefer iterative |
| `array` module / NumPy | Compact homogeneous storage | Large numeric arrays |
| Memoization via `functools.lru_cache` | Avoids recomputation in recursive DP-like structures | Recursive builds with overlapping subproblems |

---

## 22. Common Mistakes Compendium

| Structure | Common Mistake | Fix |
|---|---|---|
| Segment Tree | Wrong identity element for the operation | Use 0 for sum, +inf/-inf for min/max, 1 for product |
| Segment Tree (Lazy) | Forgetting to push down before recursing | Always call `_push_down` before descending in both update and query |
| Fenwick Tree | Using 0-indexing directly | Convert to 1-indexed internally; index 0 breaks `i & -i` |
| Fenwick Tree | Using it for min/max range queries | BIT only supports invertible ops (sum, XOR) — use Segment Tree instead |
| Sparse Table | Using it for sum queries | Sum isn't idempotent — overlapping ranges double count; use BIT/Segment Tree |
| Sparse Table | Supporting updates | Defeats the purpose — rebuild is O(n log n); use Segment Tree if dynamic |
| Skip List | Not capping `max_level` | Can (rarely) create pathologically tall towers |
| DSU | No path compression | Degrades to O(n) worst case on skewed input |
| DSU | Recursive find() on huge n | Can hit Python recursion limit — use iterative find |
| AVL Tree | Forgetting to update height before computing balance factor | Always update height first, then check balance |
| Red-Black Tree | Missing one of the 3 fixup cases (uncle red/black, inner/outer) | Carefully enumerate all cases per side (mirror symmetric cases) |
| Splay Tree | Assuming worst-case (not just amortized) O(log n) | Splay trees only guarantee amortized bounds |
| B-Tree | Forgetting to promote median key on split | Median must move up to the parent during a split |
| Interval Tree | Wrong pruning condition (`max_high >= high` instead of `>= low`) | Prune left subtree only if `left.max_high < low` |
| KD-Tree | Not pruning the "far" subtree check correctly | Only recurse into far side if splitting-plane distance < current best |
| Bloom Filter | Expecting deletion support | Use Counting Bloom Filter or Cuckoo Filter for deletion |
| Bloom Filter | Too few/many hash functions for desired false-positive rate | Use the optimal `k = (m/n)*ln(2)` formula |
| LRU Cache | Forgetting dummy head/tail sentinels | Simplifies edge cases (empty list, single node) significantly |
| LFU Cache | Not updating `min_freq` after eviction/touch | Must track and update min_freq to know which bucket to evict from |
| Treap | Non-random priorities | Height guarantee only holds with true randomization |
| HLD | Jumping from the shallower chain head instead of deeper | Always jump from `head[u]` where `depth[head[u]]` is greater |
| Mo's Algorithm | Using it for online queries | Requires all queries known upfront (offline only) |
| Suffix Array | Floating-point `log2` precision bugs | Precompute integer log table instead |
| General (all structures) | Off-by-one in inclusive/exclusive range conventions | Be explicit and consistent about `[l, r]` inclusive vs `[l, r)` exclusive throughout |

---
## 23. Cheat Sheets

### 23.1 Segment Tree Template (Copy-Paste Ready)

```python
class SegTree:
    def __init__(self, arr, op=lambda a, b: a + b, identity=0):
        self.n = len(arr)
        self.op = op
        self.identity = identity
        self.tree = [identity] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):  # [l, r) half-open
        res = self.identity
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = self.op(res, self.tree[l]); l += 1
            if r & 1:
                r -= 1; res = self.op(res, self.tree[r])
            l //= 2; r //= 2
        return res

# Usage: SegTree(arr, op=min, identity=float('inf'))  for range-min
#        SegTree(arr, op=max, identity=float('-inf')) for range-max
#        SegTree(arr, op=math.gcd, identity=0)         for range-gcd
```

### 23.2 Fenwick Tree Template

```python
class BIT:
    def __init__(self, n):
        self.n = n; self.t = [0] * (n + 1)
    def update(self, i, delta):
        while i <= self.n: self.t[i] += delta; i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0: s += self.t[i]; i -= i & (-i)
        return s
    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)
```

### 23.3 DSU Template

```python
class DSU:
    def __init__(self, n):
        self.p = list(range(n)); self.sz = [1] * n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.sz[ra] < self.sz[rb]: ra, rb = rb, ra
        self.p[rb] = ra; self.sz[ra] += self.sz[rb]
        return True
```

### 23.4 Rotation Cheat Sheet (AVL / Treap / Red-Black — shared mechanics)

```
RIGHT ROTATION (fixes Left-Left imbalance):
      z                y
     /                / \
    y      ==>       x   z
   /
  x

def rotate_right(z):
    y = z.left
    z.left = y.right
    y.right = z
    return y   # y is the new subtree root

LEFT ROTATION (fixes Right-Right imbalance):
  z                    y
   \                  / \
    y      ==>       z   x
     \
      x

def rotate_left(z):
    y = z.right
    z.right = y.left
    y.left = z
    return y   # y is the new subtree root

Left-Right case: rotate_left(z.left) first, THEN rotate_right(z)
Right-Left case: rotate_right(z.right) first, THEN rotate_left(z)
```

### 23.5 Range Query Selection Cheat Sheet

```
Static data + idempotent op (min/max/gcd/and/or)  -> Sparse Table       (O(1) query)
Static data + any op                              -> Prefix Sum Array  (O(1) query, sum only) or Sparse Table
Dynamic data + sum only                           -> Fenwick Tree       (O(log n))
Dynamic data + min/max/gcd (point update)         -> Segment Tree       (O(log n))
Dynamic data + range update + range query         -> Segment Tree + Lazy Propagation
Dynamic data + simplicity over speed              -> Sqrt Decomposition (O(sqrt n))
```

### 23.6 Python Syntax Cheat Sheet

```python
# Fast I/O for competitive programming
import sys
input = sys.stdin.readline

# Fast output
sys.stdout.write(str(result) + "\n")

# Common idioms
i & (-i)                      # isolate lowest set bit
1 << k                        # 2^k
bin(x).count('1')             # popcount
math.gcd(a, b)                # GCD
from functools import reduce
reduce(math.gcd, arr)         # GCD of entire array
```

### 23.7 Interview Cheat Sheet — 30-Second Pitch Per Structure

| Structure | 30-Second Pitch |
|---|---|
| Segment Tree | "Precomputed tree of range aggregates; O(log n) point update, O(log n) range query; supports any associative op; lazy propagation for range updates." |
| Fenwick Tree | "Compact prefix-sum structure using bit tricks (`i & -i`); O(log n) point update and prefix/range sum; simpler than segment tree but sum/XOR only." |
| Sparse Table | "O(1) query after O(n log n) preprocessing; only for static data and idempotent ops like min/max/gcd." |
| DSU | "Tracks connected components; O(α(n)) ≈ O(1) amortized with path compression + union by rank/size." |
| AVL/Red-Black | "Self-balancing BST guaranteeing O(log n) height; AVL is stricter (faster reads), Red-Black is looser (faster writes)." |
| Treap | "BST + heap hybrid using random priorities; expected O(log n) height without explicit rotation-case logic." |
| B+ Tree | "Disk-optimized balanced tree; data only in linked leaves, enabling fast range scans; the backbone of RDBMS indexes." |
| Skip List | "Layered linked lists with randomized 'express lanes'; expected O(log n), simpler than balanced BST rotations." |
| Bloom Filter | "Probabilistic set membership; O(k) add/check; no false negatives, possible false positives; no deletion (use Counting variant)." |
| LRU Cache | "HashMap + doubly linked list; O(1) get/put; evicts least-recently-used on overflow." |
| KD-Tree | "Recursively splits k-dim space by alternating axis at each level; O(log n) average nearest-neighbor search." |
| HLD | "Decomposes a tree into O(log n) chains; enables O(log² n) path queries via segment tree over the flattened array." |

---

## 24. Practice Problems

### 24.1 Segment Tree
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Static Range Sum Queries | CSES | Easy | Basic range sum |
| Range Sum Query - Mutable | LeetCode 307 | Medium | Point update, range query |
| Range Minimum Query | CSES | Easy | Range min |
| Range Update Queries | CSES | Medium | Lazy propagation |
| Hotel Queries | CSES | Hard | Segment tree binary search |
| Falling Squares | LeetCode 699 | Hard | Coordinate compression + segment tree |
| Count of Smaller Numbers After Self | LeetCode 315 | Hard | Merge sort tree / BIT |

### 24.2 Lazy Propagation
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Range Update Range Sum | CSES | Medium | Classic lazy prop |
| Forest Queries II | CSES | Hard | 2D segment tree |
| Codeforces 1114F | Codeforces | Hard | Segment tree beats |

### 24.3 Fenwick Tree
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Dynamic Range Sum Queries | CSES | Easy | Basic BIT |
| Reverse Pairs | LeetCode 493 | Hard | BIT + coordinate compression |
| Count of Range Sum | LeetCode 327 | Hard | BIT / merge sort |

### 24.4 Sparse Table
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Static Range Minimum Queries | CSES | Easy | Basic sparse table |
| Range LCP | Codeforces | Medium | Sparse table + suffix array |

### 24.5 DSU
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Number of Provinces | LeetCode 547 | Medium | Basic union-find |
| Accounts Merge | LeetCode 721 | Medium | DSU + hashing |
| Redundant Connection | LeetCode 684 | Medium | Cycle detection |
| Road Construction | CSES | Medium | DSU with component counting |
| Satisfiability of Equality Equations | LeetCode 990 | Medium | DSU |

### 24.6 AVL / Red-Black / Balanced Trees
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Balance a BST | LeetCode 1382 | Medium | Tree rebalancing |
| Convert Sorted Array to BST | LeetCode 108 | Easy | Balanced construction |
| Design a leaderboard/ordered structure | GeeksforGeeks | Hard | Balanced BST / Treap |

### 24.7 Treap
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Implicit Treap for array with reversals | Codeforces | Hard | Treap with implicit keys |
| Ordered Set operations | InterviewBit / CP | Medium | Treap basics |

### 24.8 Skip List
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Design Skiplist | LeetCode 1206 | Hard | Direct implementation |

### 24.9 KD Tree
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| K Closest Points to Origin | LeetCode 973 | Medium | Can use KD-Tree or heap |
| Closest Pair of Points | GeeksforGeeks | Hard | Divide & conquer / KD-Tree |

### 24.10 B-Tree
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Implement a B-Tree | GeeksforGeeks | Hard | Direct implementation |

### 24.11 Heavy-Light Decomposition
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Path Queries | CSES | Hard | HLD + segment tree |
| Query on a tree (QTREE) | SPOJ | Hard | Classic HLD problem |
| Company Queries II | CSES | Medium | LCA (HLD side effect) |

### 24.12 Persistent Structures
| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| K-th smallest in range (persistent segment tree) | Codeforces / CSES | Hard | Persistent segment tree |
| Photo of a house (persistent DSU) | Codeforces | Hard | Persistent DSU |

### 24.13 Additional Cross-Platform Problems

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Range Frequency Queries | LeetCode 2080 | Medium | BIT / merge sort tree |
| My Calendar III | LeetCode 732 | Hard | Segment tree / interval tree |
| The Skyline Problem | LeetCode 218 | Hard | Segment tree / sweep line |
| Design Search Autocomplete System | LeetCode 642 | Hard | Trie + heap (cross-reference) |
| LFU Cache | LeetCode 460 | Hard | LFU cache design |
| LRU Cache | LeetCode 146 | Medium | LRU cache design |
| Text Editor | LeetCode 2296 | Medium | Rope / gap buffer concept |
| Longest Duplicate Substring | LeetCode 1044 | Hard | Suffix array |
| Powerful Array | Codeforces 86D | Hard | Mo's Algorithm |
| D-Query | SPOJ | Hard | Mo's Algorithm |
| Range Sum Query 2D - Mutable | LeetCode 308 | Hard | 2D BIT |

---

## 25. Final Revision Kit

### 25.1 One-Page Revision

```
SEGMENT TREE        -> O(log n) range query/update, any associative op, O(4n) space
FENWICK TREE (BIT)   -> O(log n) prefix sum, invertible ops only, O(n) space, i&-i trick
SPARSE TABLE         -> O(1) query, static + idempotent ops only, O(n log n) preprocessing
SKIP LIST            -> O(log n) expected, randomized layered linked lists
DSU                  -> O(alpha(n)) amortized, path compression + union by rank/size
AVL TREE             -> O(log n) guaranteed, strict balance (diff <= 1), more rotations
RED-BLACK TREE       -> O(log n) guaranteed, looser balance, fewer rotations, industry std
SPLAY TREE           -> O(log n) amortized, move-to-root, great for temporal locality
TREAP                -> O(log n) expected, BST + random heap priority, simple to code
B-TREE / B+ TREE     -> O(log_t n), disk-optimized, B+ has data only in linked leaves
INTERVAL TREE        -> O(log n + k) overlap queries, augmented BST with max_high
KD-TREE              -> O(log n) avg nearest-neighbor, alternating-axis space partition
QUAD/OCTREE          -> fixed-midpoint 2D/3D space partition, games/GIS/3D graphics
R-TREE               -> bounding-rectangle based, spatial databases
SUFFIX ARRAY         -> O(n log^2 n) build, O(m log n) search, pair with Kasai's LCP
ROPE / PIECE TABLE    -> O(log n) edit ops on huge mutable strings, text editors
LRU CACHE            -> O(1) get/put, HashMap + doubly linked list, evict oldest-accessed
LFU CACHE            -> O(1) get/put, HashMap + freq buckets, evict least-frequent
BLOOM FILTER         -> O(k) add/check, probabilistic, no false negatives, no deletion
HLD                  -> O(log^2 n) tree path query, flattens tree into O(log n) chains
LINK-CUT TREE        -> O(log n) amortized dynamic tree link/cut/path query
MO'S ALGORITHM       -> O((n+Q)sqrt(n)) offline range queries that don't decompose nicely
PERSISTENT STRUCTURES -> O(log n) new nodes/update, all versions queryable
```



### 25.3 1-Hour Revision (Deeper Pass)

- Re-derive the Segment Tree lazy propagation push-down logic from scratch on paper.
- Re-derive Fenwick Tree's `i & -i` update/query loops and explain WHY they work (binary representation argument).
- Draw all 4 AVL rotation cases (LL, RR, LR, RL) from memory.
- Explain the 5 Red-Black invariants and why new nodes are inserted red.
- Implement DSU with path compression + union by rank from memory, in under 5 minutes.
- Walk through Heavy-Light Decomposition's chain-jumping query logic on a hand-drawn tree.
- Explain when Sparse Table fails (non-idempotent ops) and why.
- Explain Bloom Filter's false-positive-only guarantee and the optimal `m`/`k` formulas.
- Compare Mo's Algorithm applicability vs a direct BIT/Segment Tree solution for a sample "count distinct in range" problem.

### 25.4 Interview Notes — Final Checklist

- [ ] Can explain WHY each structure exists (what naive approach it improves upon) before diving into HOW.
- [ ] Can state time/space complexity for every operation without hesitation.
- [ ] Can identify the correct structure from problem phrasing alone (see Section 19 recognition guide).
- [ ] Can write the Segment Tree and Fenwick Tree templates from memory (Section 23).
- [ ] Can draw ASCII/whiteboard diagrams of rotations (AVL) and lazy propagation push-down.
- [ ] Knows the key trade-off comparisons (Segment Tree vs Fenwick, AVL vs Red-Black, Sparse Table vs Segment Tree).
- [ ] Comfortable discussing real-world applications (databases, OS schedulers, caches, search engines).

### 25.5 Formula Sheet

```
Sparse Table levels needed:        k = floor(log2(n)) + 1
Fenwick lowest set bit:            i & (-i)
Bloom Filter optimal bit size:     m = -(n * ln(p)) / (ln(2))^2
Bloom Filter optimal hash count:   k = (m/n) * ln(2)
AVL max height bound:              h <= 1.44 * log2(n + 2) - 0.328
Red-Black max height bound:        h <= 2 * log2(n + 1)
DSU amortized complexity:          O(alpha(n))  [alpha = inverse Ackermann, effectively O(1)]
Mo's Algorithm block size:         block_size = floor(sqrt(n))
Mo's Algorithm total complexity:   O((n + Q) * sqrt(n))
Sqrt Decomposition block size:     block_size = floor(sqrt(n)) + 1
B-Tree height bound:               h = O(log_t(n)), t = minimum degree
```

### 25.6 Rotation Cheat Sheet (Quick Reference)

```
LL imbalance -> single RIGHT rotation on the unbalanced node
RR imbalance -> single LEFT rotation on the unbalanced node
LR imbalance -> LEFT rotate the left child, THEN RIGHT rotate the node
RL imbalance -> RIGHT rotate the right child, THEN LEFT rotate the node
```

### 25.7 Mind Map (Text Form)

```
ADVANCED DATA STRUCTURES
│
├── RANGE QUERY FAMILY
│   ├── Segment Tree (dynamic, any op)
│   ├── Fenwick Tree (dynamic, sum/XOR)
│   ├── Sparse Table (static, idempotent)
│   └── Sqrt Decomposition (dynamic, simple)
│
├── CONNECTIVITY FAMILY
│   └── DSU (Union-Find)
│
├── SELF-BALANCING TREE FAMILY
│   ├── AVL (strict balance)
│   ├── Red-Black (loose balance)
│   ├── Splay (move-to-root)
│   └── Treap (randomized)
│
├── DISK / DATABASE FAMILY
│   ├── B-Tree
│   └── B+ Tree
│
├── SPATIAL FAMILY
│   ├── KD-Tree
│   ├── Quad Tree / Octree
│   └── R-Tree
│
├── STRING FAMILY
│   ├── Suffix Array / Automaton / Tree
│   └── Rope / Piece Table / Gap Buffer
│
├── CACHE / PROBABILISTIC FAMILY
│   ├── LRU / LFU Cache
│   └── Bloom Filter / Counting Bloom Filter / Cuckoo Filter
│
├── TREE-ON-TREE FAMILY (advanced)
│   ├── Heavy-Light Decomposition
│   ├── Link-Cut Tree
│   └── Euler Tour Tree
│
└── PARADIGM-LEVEL CONCEPTS
    ├── Persistent Data Structures
    ├── Functional / Immutable Structures
    ├── Cache-Oblivious Structures
    ├── Succinct Data Structures
    └── External Memory Structures (LSM-Tree, B+ Tree)
```

---

## 📌 Closing Notes

This handbook is designed to be your **single reference** for Advanced Data Structures — from first-principles intuition to production-grade Python implementations to FAANG interview pattern recognition. Revisit Section 19 (Problem Recognition Guide) whenever you're stuck deciding which structure to reach for, and Section 23 (Cheat Sheets) for quick, copy-paste-ready templates during contests or interviews.

**Suggested study path:**
1. Master Segment Tree + Fenwick Tree first (highest ROI for interviews and CP).
2. Learn DSU (extremely common, high ROI, easy to master).
3. Understand AVL vs Red-Black conceptually (rarely implemented from scratch in interviews, but frequently discussed).
4. Add Sparse Table, Treap, and Interval Tree once comfortable with the above.
5. Tackle HLD, Link-Cut Trees, and Persistent Structures only once targeting Div-1/hard FAANG onsite-level problems.

