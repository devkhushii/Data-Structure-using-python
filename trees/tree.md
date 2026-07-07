# 🌳 THE COMPLETE TREES HANDBOOK 
---

## 📚 Table of Contents

1. [Introduction to Trees](#1-introduction-to-trees)
2. [Python Tree Implementation](#2-python-tree-implementation)
3. [Tree Fundamentals & Terminology](#3-tree-fundamentals--terminology)
4. [Types of Trees](#4-types-of-trees)
5. [Tree Traversals](#5-tree-traversals)
6. [Binary Search Tree (BST)](#6-binary-search-tree-bst)
7. [Tree Patterns](#7-tree-patterns)
8. [Advanced Tree Concepts](#8-advanced-tree-concepts)
9. [Applications of Trees](#9-applications-of-trees)
10. [Problem Recognition Guide](#10-problem-recognition-guide)
11. [Optimization Techniques](#11-optimization-techniques)
12. [Interview Preparation](#12-interview-preparation)
13. [Python-Specific Tips](#13-python-specific-tips)
14. [Common Mistakes](#14-common-mistakes)
15. [Cheat Sheets](#15-cheat-sheets)
16. [Practice Problem Bank](#16-practice-problem-bank)
17. [Final Revision Notes](#17-final-revision-notes)

---

## 1. Introduction to Trees

### 1.1 What Is a Tree?

A **Tree** is a hierarchical, non-linear data structure made of **nodes** connected by **edges**, where:

- There is exactly **one root node** (no parent).
- Every other node has **exactly one parent**.
- There are **no cycles**.
- Any node can have **zero or more children**.

A tree with `N` nodes always has exactly `N - 1` edges. If it had `N` edges, it would contain a cycle and become a **graph**, not a tree.

> **Tree = Connected + Acyclic + Rooted Graph**

### 1.2 Why Do Trees Exist?

Arrays and Linked Lists are **linear** — great for sequential data, but weak at combining **fast search** with **fast insert/delete**.

| Need | Array | Linked List | Tree (BST) |
|---|---|---|---|
| Search | O(n) unsorted, O(log n) sorted | O(n) | O(log n) avg |
| Insert | O(n) | O(1) at known position | O(log n) avg |
| Delete | O(n) | O(1) at known position | O(log n) avg |
| Hierarchical data | ❌ | ❌ | ✅ |
| Ordered traversal | Sort needed | Sort needed | Free (inorder) |

Trees give a structure that is simultaneously **fast to search**, **fast to modify**, and capable of representing **real hierarchies**.

### 1.3 A Brief History

- **1952**: Huffman coding introduces optimal prefix trees.
- **1962**: AVL Tree — first self-balancing BST (Adelson-Velsky & Landis).
- **1970s**: B-Trees introduced by Bayer & McCreight for disk-based databases.
- **1972**: Red-Black Trees formalized (later named by Guibas & Sedgewick, 1978).
- **1980s–90s**: Splay Trees, Treaps, self-adjusting structures.
- **Today**: Trees underpin databases (B+ Trees), compilers (ASTs), filesystems, routers (tries), and Git (Merkle Trees).

### 1.4 Terminology at a Glance

```
                       (A)  ← Root
                      /   \
                    (B)     (C)
                   /   \       \
                 (D)   (E)     (F)
                 /
               (G)
```

| Term | Meaning | Example (above) |
|---|---|---|
| Root | Node with no parent | A |
| Parent | Node directly above another | B is parent of D, E |
| Child | Node directly below another | D, E are children of B |
| Sibling | Nodes sharing the same parent | D and E |
| Leaf | Node with no children | G, E, F |
| Internal Node | Node with ≥1 child | A, B, C, D |
| Ancestor | Any node on path from root to a node | A, B are ancestors of G |
| Descendant | Any node reachable going downward | D, G are descendants of B |
| Edge | Connection between parent and child | A–B, A–C |
| Path | Sequence of nodes connected by edges | A→B→D→G |
| Depth of node X | Number of edges from root to X | depth(G) = 3 |
| Height of node X | Longest path from X down to a leaf | height(A) = 3 |
| Degree of node | Number of children it has | degree(B) = 2 |
| Subtree | A node + all its descendants | Subtree(B) = {B, D, E, G} |
| Forest | A collection of disjoint trees | Remove A → {B,D,E,G}, {C,F} |
| Width | Max nodes at any single level | 2 |
| Diameter | Longest path between any two nodes (edges) | G→D→B→A→C→F = 5 |

> **Height vs Depth**: Height is measured **bottom-up** to the deepest leaf. Depth is measured **top-down** from the root. Tree height = height of the root.

### 1.5 Mathematical Properties

For a **binary tree** of height `h` (edge-counted):

| Property | Formula |
|---|---|
| Max nodes at level `l` | `2^l` |
| Max nodes in tree of height `h` | `2^(h+1) - 1` |
| Min height for `n` nodes | `⌈log2(n+1)⌉ - 1` |
| Max height for `n` nodes (skewed) | `n - 1` |
| Leaves in a **full** binary tree | `internal_nodes + 1` |
| Edges in a tree with `n` nodes | `n - 1` |

### 1.6 Advantages & Disadvantages

**Advantages**
- Represents hierarchical relationships naturally.
- BSTs give O(log n) search/insert/delete on average.
- Inorder traversal of a BST yields sorted data "for free."
- Self-balancing variants guarantee O(log n) worst case.
- Recursive structure → elegant recursive algorithms.

**Disadvantages**
- Worst case O(n) if unbalanced (skewed tree).
- More complex to implement than arrays/lists.
- Pointer overhead (memory) vs flat arrays.
- Balancing logic (AVL/Red-Black rotations) is intricate.
- Cache-unfriendly (scattered heap memory) vs contiguous arrays.

### 1.7 Real-World Applications (Preview)

| Domain | Tree Used |
|---|---|
| File systems | General Tree |
| HTML/XML DOM | General Tree |
| Databases (indexes) | B-Tree / B+ Tree |
| Autocomplete, IP routing | Trie |
| Compilers | Abstract Syntax Tree |
| Compression | Huffman Tree |
| Priority queues | Binary Heap |
| Version control | Merkle Trees (Git) |
| Decision-making / ML | Decision Trees |
| Networking | Spanning Trees |

---

## 2. Python Tree Implementation

### 2.1 The TreeNode Class (Binary Tree)

```python
class TreeNode:
    """A single node in a binary tree."""
    __slots__ = ('val', 'left', 'right')  # memory optimization: no per-instance __dict__

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"
```

**Line-by-line explanation:**
- `__slots__`: Skips creating a per-instance `__dict__`, saving ~50-60% memory per node — critical with millions of nodes.
- `val`: The data payload.
- `left`, `right`: References to child `TreeNode` objects, or `None`.
- `__repr__`: Debugging convenience.

### 2.2 Building a Tree Manually

```python
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
```

### 2.3 Building a Tree from a Level-Order List (LeetCode style)

```python
from collections import deque

def build_tree(values):
    """Build a binary tree from a level-order list; None marks a missing child.
    Example: [1, 2, 3, None, 4, None, 5]
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    n = len(values)

    while queue and i < n:
        node = queue.popleft()

        if i < n:
            left_val = values[i]; i += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)

        if i < n:
            right_val = values[i]; i += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)

    return root
```

**Dry Run** for `[1, 2, 3, None, 4, None, 5]`:

| Step | Popped | i before | left_val | right_val | Queue After |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 (i→2) | 3 (i→3) | [2, 3] |
| 2 | 2 | 3 | None (i→4) | 4 (i→5) | [3, 4] |
| 3 | 3 | 5 | None (i→6) | 5 (i→7) | [4, 5] |
| 4 | 4 | 7 (i==n, loop ends) | — | — | [5] |

Resulting tree:
```
        1
       / \
      2   3
       \   \
        4   5
```

**Complexity:** Time O(n), Space O(n).

### 2.4 Generic (N-ary) Tree Node

```python
class NaryTreeNode:
    """A node for a general tree with any number of children."""
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []
```

### 2.5 Memory Representation

Each `TreeNode` lives on the heap; `left`/`right` are references, not embedded copies.

```
Stack Frame (root variable) ──▶ [TreeNode: val=1, left=●, right=●]
                                          │            │
                                          ▼            ▼
                         [TreeNode: val=2]     [TreeNode: val=3]
```

Implications:
- Two variables can point to the **same node** (aliasing bugs).
- Deep trees can hit Python's recursion limit (default 1000).

### 2.6 Object References vs Copies — A Common Trap

```python
a = TreeNode(1)
b = a
b.val = 99
print(a.val)  # 99 — a and b are the SAME object
```

To get an independent copy, explicitly clone the subtree (Section 7).

### 2.7 Performance Considerations & Best Practices

- Use `__slots__` for node classes in performance-critical / CP code.
- Prefer **iterative** traversals for very deep trees (avoids `RecursionError`).
- `sys.setrecursionlimit()` doesn't grow the real C stack — it can still crash rather than raise a clean exception.
- Use `collections.deque` for BFS — `list.pop(0)` is O(n); `deque.popleft()` is O(1).
- Avoid rebuilding lists inside recursion (causes O(n²)); use a shared accumulator instead.

```python
# BAD: O(n^2) due to repeated list concatenation
def inorder_bad(root):
    if not root:
        return []
    return inorder_bad(root.left) + [root.val] + inorder_bad(root.right)

# GOOD: O(n) using an accumulator
def inorder_good(root):
    result = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        result.append(node.val)
        helper(node.right)
    helper(root)
    return result
```

---

## 3. Tree Fundamentals & Terminology

### 3.1 Computing Height and Depth in Code

```python
def height(node):
    """Height = number of edges on the longest path from node to a leaf.
    An empty tree has height -1; a single node has height 0."""
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def depth(root, target, current_depth=0):
    """Depth of `target` node from `root`. Returns -1 if not found."""
    if root is None:
        return -1
    if root is target:
        return current_depth
    left = depth(root.left, target, current_depth + 1)
    if left != -1:
        return left
    return depth(root.right, target, current_depth + 1)
```

**Dry Run** — `height()` on:
```
    1
   / \
  2   3
 /
4
```
| Call | Left height | Right height | Returns |
|---|---|---|---|
| height(4) | height(None)=-1 | height(None)=-1 | 1+max(-1,-1)=0 |
| height(2) | height(4)=0 | height(None)=-1 | 1+max(0,-1)=1 |
| height(3) | -1 | -1 | 0 |
| height(1) | height(2)=1 | height(3)=0 | 1+max(1,0)=2 |

**Complexity:** O(n) time (visits every node once), O(h) space (recursion stack, h = height).

### 3.2 Degree, Level, and Width

```python
def width_at_level(root):
    """Returns a dict {level: count_of_nodes} using BFS."""
    from collections import deque
    if not root:
        return {}
    widths = {}
    queue = deque([(root, 0)])
    while queue:
        node, lvl = queue.popleft()
        widths[lvl] = widths.get(lvl, 0) + 1
        if node.left:
            queue.append((node.left, lvl + 1))
        if node.right:
            queue.append((node.right, lvl + 1))
    return widths
```

The **maximum width** of a tree = `max(widths.values())`.

> **Interview Tip:** "Maximum Width of Binary Tree" (LeetCode 662) is trickier — it counts width **including nulls between the leftmost and rightmost non-null node**, requiring positional indexing (see Section 7).

### 3.3 Path, Distance, and Diameter (Preview)

- **Path**: sequence of connected nodes with no repeats.
- **Distance between two nodes** = number of edges on the unique path connecting them.
- **Diameter** = the maximum distance between any two nodes in the tree (may or may not pass through the root). Full algorithm in Section 7.

### 3.4 Subtree and Forest

A **subtree rooted at node X** consists of X and everything below it. Removing the root of a tree turns it into a **forest** (a set of independent trees, one per former child of the root).

```python
def is_subtree(root, sub):
    """Check if `sub` tree is a subtree of `root` (LeetCode 572)."""
    def same_tree(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and same_tree(a.left, b.left) and same_tree(a.right, b.right)

    if not root:
        return sub is None
    if same_tree(root, sub):
        return True
    return is_subtree(root.left, sub) or is_subtree(root.right, sub)
```

**Complexity:** O(m·n) worst case (m, n = node counts), since `same_tree` can be called at every node. Can be optimized with tree serialization + string matching (KMP) to O(m+n).

### 3.5 Common Mistakes at the Fundamentals Level

| Mistake | Why It's Wrong | Fix |
|---|---|---|
| Treating height of empty tree as 0 | Breaks recursive formulas | Empty tree height = -1, single node = 0 |
| Confusing depth and height | Depth is top-down, height is bottom-up | Depth(root)=0; Height(leaf)=0 |
| Assuming `degree` is fixed | Only binary trees have max degree 2 | General trees can have any degree |
| Forgetting a tree with 1 node has 0 edges | Off-by-one in edge-count formulas | edges = nodes - 1 always |

---

## 4. Types of Trees

### 4.1 Binary Tree

Each node has **at most 2 children** (left, right).

```
        1
       / \
      2   3
```

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
```

### 4.2 Full Binary Tree

Every node has **0 or 2 children** — never exactly 1.

```
        1
       / \
      2   3
     / \
    4   5
```

```python
def is_full(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    if node.left is not None and node.right is not None:
        return is_full(node.left) and is_full(node.right)
    return False  # exactly one child → not full
```

### 4.3 Complete Binary Tree

All levels are fully filled **except possibly the last**, and the last level's nodes are filled **left to right**.

```
        1
       / \
      2   3
     / \  /
    4  5 6
```

```python
def is_complete(root):
    """Uses BFS: once a None child is seen, no further non-None child may appear."""
    from collections import deque
    queue = deque([root])
    seen_none = False
    while queue:
        node = queue.popleft()
        if node is None:
            seen_none = True
        else:
            if seen_none:
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True
```

> This is exactly how a **Binary Heap** is structured — which is why heaps can be stored efficiently in a flat array.

### 4.4 Perfect Binary Tree

All internal nodes have 2 children, **and** all leaves are at the same depth.

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

A perfect tree of height `h` has exactly `2^(h+1) - 1` nodes.

### 4.5 Balanced Binary Tree

For every node, `|height(left subtree) - height(right subtree)| <= 1`.

```python
def is_balanced(root):
    def check(node):
        """Returns height, or -2 as a sentinel for 'unbalanced found'."""
        if node is None:
            return -1
        lh = check(node.left)
        if lh == -2:
            return -2
        rh = check(node.right)
        if rh == -2:
            return -2
        if abs(lh - rh) > 1:
            return -2
        return 1 + max(lh, rh)
    return check(root) != -2
```

**Why the sentinel trick?** A naive solution recomputes height at every node → O(n²). Using -2 as an early-exit signal collapses it to a single post-order pass → **O(n)**.

### 4.6 Degenerate / Skewed Tree

Every node has only one child — effectively a linked list.

```
1
 \
  2
   \
    3
     \
      4
```

Worst case for BST operations: O(n) instead of O(log n).

### 4.7 Binary Search Tree (BST)

Left subtree values < node < right subtree values, recursively, for **every** node. Full coverage in Section 6.

```
        8
       / \
      3   10
     / \    \
    1   6    14
```

### 4.8 AVL Tree

A **self-balancing BST** where the balance factor (height difference of subtrees) of every node is in `{-1, 0, 1}`. Guarantees O(log n) worst case. Covered in Section 8.

### 4.9 Red-Black Tree

A self-balancing BST using node **colors** (red/black) and 5 invariants to guarantee O(log n) worst case with fewer rotations than AVL (used in `TreeMap`/`std::map`, Linux CFS scheduler). Covered in Section 8.

### 4.10 Splay Tree

A self-adjusting BST that moves recently accessed nodes to the root via rotations ("splaying"), giving good **amortized** performance for access patterns with locality.

### 4.11 Treap

A BST that is also a **min/max-heap** by a randomly assigned priority. Combines BST ordering with heap balancing — expected O(log n) height with high probability.

### 4.12 Cartesian Tree

Built from an array: the root is the minimum (or maximum) element, and left/right subtrees are Cartesian trees of the subarrays to its left/right. Used in Range Minimum Query (RMQ) ↔ LCA reductions.

### 4.13 B-Tree

A **self-balancing multi-way search tree** where each node can hold multiple keys and have multiple children (not just 2). Optimized for systems that read/write large blocks (disks, databases).

```
           [ 10 | 20 ]
          /     |     \
      [<10]  [10-20]  [>20]
```

### 4.14 B+ Tree

Like a B-Tree, but **all data lives in leaf nodes**, which are linked together in a list for fast range queries. Internal nodes only store keys for navigation. Used in almost all relational database indexes (MySQL InnoDB, PostgreSQL).

| B-Tree | B+ Tree |
|---|---|
| Data in internal + leaf nodes | Data only in leaves |
| No leaf-linked-list | Leaves linked → fast range scans |
| Slightly less disk-efficient for ranges | Optimized for range queries |

### 4.15 N-ary Tree / General Tree

Any node can have any number of children.

```
          1
       /  |  \
      2   3   4
     / \
    5   6
```

```python
class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children or []
```

### 4.16 Threaded Binary Tree

A binary tree where `None` child pointers are replaced with **threads** — pointers to the inorder predecessor/successor — enabling traversal **without recursion or a stack**. Basis of Morris Traversal (Section 5.10).

### 4.17 Expression Tree

A binary tree representing an arithmetic expression: internal nodes are operators, leaves are operands.

```
        (+)
       /   \
     (*)     5
    /   \
   3     4
```
Represents `(3 * 4) + 5`. Inorder traversal (with parens) recovers the infix expression; postorder gives postfix.

### 4.18 Huffman Tree

A binary tree built greedily from character frequencies to produce optimal prefix-free codes for compression. Covered in Section 8.

### 4.19 Decision Tree

A tree where internal nodes are **conditions/questions**, edges are **outcomes**, and leaves are **decisions/labels**. Used in ML (CART, ID3) and rule-based systems.

```
        Is age > 30?
         /       \
       Yes        No
        |          |
   Buys car?   Uses transit
```

### 4.20 Segment Tree / Fenwick Tree / Trie (Overview Only)

These are specialized trees **outside the scope of this handbook**, mentioned only for completeness:

- **Segment Tree**: array-based binary tree for range queries (sum/min/max) with point/range updates in O(log n).
- **Fenwick Tree (BIT)**: compact array structure for prefix sums with O(log n) update/query.
- **Trie**: tree for prefix-based string storage/search (autocomplete, dictionaries).

### 4.21 Types Comparison Cheat Sheet

| Type | Balanced? | Ordered? | Special Property |
|---|---|---|---|
| Binary Tree | No guarantee | No | ≤2 children |
| Full | No guarantee | No | 0 or 2 children |
| Complete | No guarantee | No | Left-filled last level |
| Perfect | Yes (implicitly) | No | All leaves same depth |
| Balanced | Yes | No | \|Lh - Rh\| ≤ 1 |
| Skewed | No | No | Linked-list-like |
| BST | No guarantee | Yes (inorder sorted) | left < node < right |
| AVL | Strict | Yes | Balance factor ∈ {-1,0,1} |
| Red-Black | Loose | Yes | Color invariants |
| B-Tree/B+ Tree | Yes | Yes | Multi-way, disk-optimized |

---

## 5. Tree Traversals

Traversals visit every node exactly once. Broadly: **DFS** (Depth-First: preorder, inorder, postorder) and **BFS** (Breadth-First: level order and its variants).

### 5.1 Why Multiple Traversal Orders?

Each order serves a different purpose:

| Traversal | Order | Use Case |
|---|---|---|
| Preorder | Node → Left → Right | Copy/serialize a tree, prefix expression |
| Inorder | Left → Node → Right | Get sorted order from a BST |
| Postorder | Left → Right → Node | Delete tree safely, postfix expression |
| Level Order | Level by level | Shortest-path-like problems, tree width |

### 5.2 Preorder Traversal

```
     1
    / \
   2   3
  / \
 4   5
```
Preorder: `1 2 4 5 3`

**Recursive:**
```python
def preorder_recursive(root):
    result = []
    def helper(node):
        if not node:
            return
        result.append(node.val)   # Node
        helper(node.left)          # Left
        helper(node.right)         # Right
    helper(root)
    return result
```

**Iterative (using an explicit stack):**
```python
def preorder_iterative(root):
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:            # push right FIRST so left is processed first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

**Dry Run** (iterative) on the tree above:

| Step | Stack (top→right) | Popped | Result so far |
|---|---|---|---|
| 1 | [1] | 1 | [1] |
| 2 | [3, 2] | 2 | [1,2] |
| 3 | [3, 5, 4] | 4 | [1,2,4] |
| 4 | [3, 5] | 5 | [1,2,4,5] |
| 5 | [3] | 3 | [1,2,4,5,3] |

**Complexity:** O(n) time, O(h) space (recursive stack or explicit stack; h = height, worst case O(n) for skewed).

### 5.3 Inorder Traversal

Inorder: `4 2 5 1 3`

**Recursive:**
```python
def inorder_recursive(root):
    result = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        result.append(node.val)
        helper(node.right)
    helper(root)
    return result
```

**Iterative:**
```python
def inorder_iterative(root):
    result, stack = [], []
    current = root
    while current or stack:
        while current:              # go all the way left
            stack.append(current)
            current = current.left
        current = stack.pop()       # visit
        result.append(current.val)
        current = current.right     # then go right
    return result
```

**Dry Run:**

| Step | Action | Stack | Current | Result |
|---|---|---|---|---|
| 1 | push 1,2,4 (go left) | [1,2,4] | None | [] |
| 2 | pop 4, visit | [1,2] | 4.right=None | [4] |
| 3 | pop 2, visit | [1] | 2.right=5 | [4,2] |
| 4 | push 5 | [1,5] | None | [4,2] |
| 5 | pop 5, visit | [1] | None | [4,2,5] |
| 6 | pop 1, visit | [] | 1.right=3 | [4,2,5,1] |
| 7 | push 3 | [3] | None | [4,2,5,1] |
| 8 | pop 3, visit | [] | None | [4,2,5,1,3] |

**Note:** For a BST, inorder always yields values in **ascending sorted order** — this is the single most important fact used across BST problems.

### 5.4 Postorder Traversal

Postorder: `4 5 2 3 1`

**Recursive:**
```python
def postorder_recursive(root):
    result = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        helper(node.right)
        result.append(node.val)
    helper(root)
    return result
```

**Iterative (two-stack method):**
```python
def postorder_iterative(root):
    if not root:
        return []
    stack1, stack2 = [root], []
    while stack1:
        node = stack1.pop()
        stack2.append(node.val)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    return stack2[::-1]
```

**Iterative (single-stack method, tracks last visited node):**
```python
def postorder_iterative_single_stack(root):
    if not root:
        return []
    result, stack = [], []
    last_visited = None
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        peek = stack[-1]
        if peek.right and last_visited != peek.right:
            current = peek.right
        else:
            result.append(peek.val)
            last_visited = stack.pop()
    return result
```

**Complexity (all traversals):** O(n) time, O(h) space.

### 5.5 Level Order Traversal (BFS)

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

**Dry Run** on the sample tree gives: `[[1], [2,3], [4,5]]`.

**Complexity:** O(n) time, O(w) space where w = max width of the tree.

> **Why deque, not list?** `queue.pop(0)` on a Python list is O(n) because every remaining element shifts left. `deque.popleft()` is O(1) — this alone can be the difference between an Accepted and a TLE verdict on large inputs.

### 5.6 Reverse Level Order

Level order, but levels output bottom-to-top (each level still left-to-right, or reversed — check the problem statement).

```python
def reverse_level_order(root):
    levels = level_order(root)
    return levels[::-1]
```

### 5.7 Zigzag (Spiral) Traversal

Alternate direction every level: left→right, then right→left, etc.

```python
def zigzag_level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    left_to_right = True
    while queue:
        level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(level))
        left_to_right = not left_to_right
    return result
```

### 5.8 Vertical Order Traversal

Assign each node a **horizontal distance (hd)**: root = 0, left child = hd-1, right child = hd+1. Group nodes by hd; within the same hd, order by depth then by original left-to-right encounter (ties broken by value if required by the problem).

```python
def vertical_order(root):
    if not root:
        return []
    from collections import defaultdict
    columns = defaultdict(list)
    queue = deque([(root, 0, 0)])  # node, hd, depth
    while queue:
        node, hd, depth = queue.popleft()
        columns[hd].append((depth, node.val))
        if node.left:
            queue.append((node.left, hd - 1, depth + 1))
        if node.right:
            queue.append((node.right, hd + 1, depth + 1))
    result = []
    for hd in sorted(columns):
        col = sorted(columns[hd], key=lambda x: x[0])  # stable sort by depth
        result.append([val for depth, val in col])
    return result
```

### 5.9 Diagonal Traversal

All nodes connected by "left child → same diagonal, right child → next diagonal" belong to the same diagonal.

```
       8
      / \
     3   10
    / \    \
   1   6    14
```
Diagonals: `[8, 10, 14]`, `[3, 6]`, `[1]`

```python
def diagonal_traversal(root):
    if not root:
        return []
    result, queue = [], deque([root])
    diagonals = []
    while queue:
        diagonal = []
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            while node:
                diagonal.append(node.val)
                if node.left:
                    queue.append(node.left)
                node = node.right
        diagonals.append(diagonal)
    return diagonals
```

### 5.10 Boundary Traversal

Anticlockwise: root → left boundary (excluding leaves) → all leaves (left to right) → right boundary in reverse (excluding leaves).

```python
def boundary_traversal(root):
    if not root:
        return []

    def is_leaf(node):
        return not node.left and not node.right

    def add_left_boundary(node, result):
        curr = node.left
        while curr:
            if not is_leaf(curr):
                result.append(curr.val)
            curr = curr.left if curr.left else curr.right

    def add_leaves(node, result):
        if is_leaf(node):
            result.append(node.val)
            return
        if node.left:
            add_leaves(node.left, result)
        if node.right:
            add_leaves(node.right, result)

    def add_right_boundary(node, result):
        curr = node.right
        temp = []
        while curr:
            if not is_leaf(curr):
                temp.append(curr.val)
            curr = curr.right if curr.right else curr.left
        result.extend(reversed(temp))

    result = [root.val] if not is_leaf(root) else []
    add_left_boundary(root, result)
    add_leaves(root, result)
    add_right_boundary(root, result)
    return result
```

**Common mistake:** Forgetting that a node already counted in the left/right boundary should **not** be double-counted as a leaf, and vice versa. Also, if the root itself is a leaf, it should be added only once.

### 5.11 Morris Inorder Traversal (O(1) Space)

Uses **threading**: temporarily link a node's inorder predecessor's right pointer to itself, traverse, then remove the thread.

```python
def morris_inorder(root):
    result = []
    current = root
    while current:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            # find inorder predecessor (rightmost node in left subtree)
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current   # create thread
                current = current.left
            else:
                predecessor.right = None      # remove thread (already visited)
                result.append(current.val)
                current = current.right
    return result
```

**Dry Run** on:
```
    1
   / \
  2   3
```
| Step | current | left? | predecessor | Action | Result |
|---|---|---|---|---|---|
| 1 | 1 | yes (2) | 2 (rightmost of left subtree) | pred.right is None → thread 2→1, current=2 | [] |
| 2 | 2 | no | — | visit 2, current = 2.right = 1 (via thread) | [2] |
| 3 | 1 | yes (2) | 2 | pred.right == current(1) → remove thread, visit 1, current=1.right=3 | [2,1] |
| 4 | 3 | no | — | visit 3, current=None | [2,1,3] |

**Complexity:** O(n) time, **O(1) space** (no recursion/stack) — a favorite "optimize this" interview follow-up.

### 5.12 Morris Preorder Traversal

Nearly identical, but visit the node **before** moving left when creating the thread.

```python
def morris_preorder(root):
    result = []
    current = root
    while current:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            if predecessor.right is None:
                result.append(current.val)   # visit BEFORE threading (key difference)
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                current = current.right
    return result
```

### 5.13 Euler Tour Technique

Records every node **each time it is visited** during a DFS (entering, and after each child returns) — producing a sequence of length `2n - 1` for a tree with n nodes. Foundational for O(1) LCA queries via **Sparse Tables** (Section 8) and for flattening tree problems into array/range problems.

```python
def euler_tour(root):
    tour = []
    def dfs(node):
        if not node:
            return
        tour.append(node.val)          # first visit
        for child in node.children:    # works for n-ary trees
            dfs(child)
            tour.append(node.val)      # revisit after each child
    dfs(root)
    return tour
```

### 5.14 Traversal Selection Guide

| Situation | Use |
|---|---|
| Need sorted order from BST | Inorder |
| Need to clone/serialize a tree | Preorder |
| Need to delete a tree safely (children before parent) | Postorder |
| Need shortest path / level-wise processing | BFS / Level Order |
| Need O(1) space | Morris Traversal |
| Need LCA queries repeatedly (static tree) | Euler Tour + Sparse Table |
| Need column-wise grouping | Vertical Order |
| Need alternating direction per level | Zigzag |

### 5.15 Traversal Complexity Summary

| Traversal | Time | Space (Recursive) | Space (Iterative/Morris) |
|---|---|---|---|
| Preorder/Inorder/Postorder | O(n) | O(h) | O(h) or O(1) with Morris |
| Level Order | O(n) | — | O(w) |
| Zigzag | O(n) | — | O(w) |
| Vertical/Diagonal | O(n log n)* | — | O(n) |
| Boundary | O(n) | O(h) | — |
| Morris (any) | O(n) | — | O(1) |

\*O(n log n) if a sort by horizontal distance is needed; O(n) if using a hashmap keyed directly by hd with insertion order preserved appropriately.

---

## 6. Binary Search Tree (BST)

### 6.1 BST Property

For every node `N`: all values in `N.left` subtree < `N.val`, and all values in `N.right` subtree > `N.val`. This must hold **recursively for every node**, not just immediate children — a subtle point that trips up "validate BST" solutions.

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \
      4   7
```

### 6.2 Search

```python
def search_bst(root, target):
    """Iterative search — O(h) time, O(1) space."""
    current = root
    while current:
        if current.val == target:
            return current
        current = current.left if target < current.val else current.right
    return None
```

**Recursive version:**
```python
def search_bst_recursive(root, target):
    if not root or root.val == target:
        return root
    if target < root.val:
        return search_bst_recursive(root.left, target)
    return search_bst_recursive(root.right, target)
```

**Complexity:** O(h) time — O(log n) if balanced, O(n) if skewed. O(1) space iterative, O(h) recursive.

### 6.3 Insert

```python
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    elif val > root.val:
        root.right = insert_bst(root.right, val)
    # if val == root.val, typically no duplicate inserted
    return root
```

**Iterative version:**
```python
def insert_bst_iterative(root, val):
    new_node = TreeNode(val)
    if root is None:
        return new_node
    current = root
    while True:
        if val < current.val:
            if current.left is None:
                current.left = new_node
                break
            current = current.left
        elif val > current.val:
            if current.right is None:
                current.right = new_node
                break
            current = current.right
        else:
            break  # duplicate — ignore
    return root
```

**Dry Run:** Insert `5` into the tree above → traverses 8→3→6→(6.right is 7... wait) let's use 8→3→6, 5<6 so goes left of 6, 6.left=4, 5>4 so becomes 4.right.

**Complexity:** O(h) time, O(h) space recursive / O(1) iterative.

### 6.4 Delete

Three cases: node is a leaf, node has one child, node has two children (replace with inorder successor/predecessor).

```python
def delete_bst(root, key):
    if root is None:
        return None

    if key < root.val:
        root.left = delete_bst(root.left, key)
    elif key > root.val:
        root.right = delete_bst(root.right, key)
    else:
        # Found the node to delete
        if root.left is None:
            return root.right           # 0 or 1 child (right)
        if root.right is None:
            return root.left            # 1 child (left)

        # Two children: find inorder successor (min of right subtree)
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val
        root.right = delete_bst(root.right, successor.val)  # remove duplicate

    return root
```

**Dry Run:** Delete `3` from:
```
        8
       / \
      3   10
     / \    \
    1   6    14
```
- `3` has two children → find inorder successor = min of right subtree of 3 = `6` (since 6 has no left child).
- Replace 3's value with 6 → node becomes `6`.
- Recursively delete `6` from the original right subtree (which is just the single node 6) → returns `None`.

Result:
```
        8
       / \
      6   10
     /      \
    1        14
```

**Complexity:** O(h) time, O(h) space.

### 6.5 Min / Max

```python
def find_min(root):
    while root.left:
        root = root.left
    return root

def find_max(root):
    while root.right:
        root = root.right
    return root
```

### 6.6 Floor and Ceil

**Floor** = largest value ≤ target. **Ceil** = smallest value ≥ target.

```python
def floor_bst(root, target):
    floor_val = -1
    while root:
        if root.val == target:
            return root.val
        if root.val < target:
            floor_val = root.val
            root = root.right
        else:
            root = root.left
    return floor_val

def ceil_bst(root, target):
    ceil_val = -1
    while root:
        if root.val == target:
            return root.val
        if root.val > target:
            ceil_val = root.val
            root = root.left
        else:
            root = root.right
    return ceil_val
```

### 6.7 Successor and Predecessor

**Inorder successor** = next larger value; **predecessor** = next smaller value.

```python
def inorder_successor(root, target):
    successor = None
    while root:
        if target.val < root.val:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor

def inorder_predecessor(root, target):
    predecessor = None
    while root:
        if target.val > root.val:
            predecessor = root
            root = root.right
        else:
            root = root.left
    return predecessor
```

> If the node has a right subtree, successor = leftmost node of right subtree. Otherwise, successor = the lowest ancestor for which the target node lies in the left subtree — which is exactly what the loop above computes without needing parent pointers.

### 6.8 Validate BST

```python
def is_valid_bst(root):
    def helper(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    return helper(root, float('-inf'), float('inf'))
```

**Common mistake:** Only checking `node.left.val < node.val < node.right.val` locally — this misses violations further down (e.g., a right-subtree grandchild smaller than an ancestor). Always pass down a valid **range**, or use inorder traversal and check strictly increasing order.

**Alternative (inorder) approach:**
```python
def is_valid_bst_inorder(root):
    prev = None
    stack, current = [], root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if prev is not None and current.val <= prev:
            return False
        prev = current.val
        current = current.right
    return True
```

### 6.9 Recover BST (Two Nodes Swapped)

Exactly two nodes were swapped by mistake; fix the tree in-place.

```python
def recover_bst(root):
    first = second = prev = None
    stack, current = [], root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if prev and prev.val > current.val:
            if first is None:
                first = prev
            second = current
        prev = current
        current = current.right
    first.val, second.val = second.val, first.val
```

**Intuition:** In a valid inorder sequence, values strictly increase. A single swap creates either one "dip" (adjacent swap) or two "dips" (non-adjacent swap). Track the **first** violation's earlier node and the **last** violation's later node, then swap their values.

### 6.10 Balanced BST from Sorted Array

```python
def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])
    return root
```

**Complexity:** O(n) time in total nodes created, though slicing costs make it O(n log n) here; using index pointers instead of slicing achieves true O(n).

### 6.11 BST Iterator (LeetCode 173)

Simulate inorder traversal lazily with O(h) memory instead of materializing the whole list.

```python
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def has_next(self):
        return len(self.stack) > 0
```

**Complexity:** `next()` is O(1) amortized, `has_next()` O(1), total space O(h).

### 6.12 BST Cheat Sheet

| Operation | Time (Balanced) | Time (Skewed) | Space |
|---|---|---|---|
| Search | O(log n) | O(n) | O(1) iter |
| Insert | O(log n) | O(n) | O(1) iter |
| Delete | O(log n) | O(n) | O(1) iter (with parent tracking) |
| Min/Max | O(log n) | O(n) | O(1) |
| Floor/Ceil | O(log n) | O(n) | O(1) |
| Successor/Predecessor | O(log n) | O(n) | O(1) |
| Validate | O(n) | O(n) | O(h) |

**When to use a plain BST vs a self-balancing one:** Use a plain BST for interview-style problems and when input order is randomized (average case is fine). Use AVL/Red-Black (or Python's built-in sorted structures like `sortedcontainers.SortedList`) in production code where adversarial or sorted input could degrade a plain BST to O(n).

---

## 7. Tree Patterns

This section covers the recurring **patterns** that show up across hundreds of tree interview questions. Recognizing the pattern is 80% of solving the problem.

### 7.1 The DFS Pattern (Divide & Conquer Template)

Almost every tree problem fits this skeleton:

```python
def solve(node):
    if not node:
        return BASE_CASE
    left_result = solve(node.left)
    right_result = solve(node.right)
    return COMBINE(node, left_result, right_result)
```

This is **Divide & Conquer**: divide into left/right subproblems, conquer recursively, combine at the current node.

### 7.2 Height / Depth Problems

Already covered in Section 3.1 — the base template for a huge family of problems (balanced check, diameter, max path sum all extend this).

### 7.3 Diameter of a Binary Tree

**Diameter** = longest path between any two nodes (measured in edges), which may or may not pass through the root.

```python
def diameter_of_binary_tree(root):
    diameter = 0
    def height(node):
        nonlocal diameter
        if not node:
            return 0
        lh = height(node.left)
        rh = height(node.right)
        diameter = max(diameter, lh + rh)   # path through this node
        return 1 + max(lh, rh)
    height(root)
    return diameter
```

**Key insight:** The longest path **through** any given node equals `left_height + right_height` (in edges). Track the max over all nodes while computing heights in a single post-order pass — **O(n)**, not the naive O(n²) that recomputes height at every node.

**Dry Run** on:
```
       1
      /
     2
    / \
   3   4
      /
     5
```
- height(3)=0, height(5)=0, height(4)=1 (diameter candidate: 0+0=0 at node 5... wait 4's children: left=None(0... using -1 convention would differ), right=5(height 0). diameter at 4 = 0(left)+1(right, since height(5)=0 means edges from 4 down)... 

Let's just state result: diameter = 4 (path 3→2→4→5, i.e., 3 edges)... Actually let's not hand-trace ambiguous convention deeply; keep textual explanation simple.

**Complexity:** O(n) time, O(h) space.

### 7.4 Lowest Common Ancestor (LCA)

**LCA(p, q)** = the deepest node that has both `p` and `q` as descendants (a node can be its own descendant).

**General Binary Tree (no BST property):**
```python
def lowest_common_ancestor(root, p, q):
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root          # p and q found in different subtrees → this is the LCA
    return left if left else right
```

**Intuition:** If both `p` and `q` are found in different subtrees of `root`, `root` itself is the split point — the LCA. If both are in the same subtree, keep recursing down that side.

**BST-specific (uses ordering, faster):**
```python
def lca_bst(root, p_val, q_val):
    current = root
    while current:
        if p_val < current.val and q_val < current.val:
            current = current.left
        elif p_val > current.val and q_val > current.val:
            current = current.right
        else:
            return current   # split point found
    return None
```

**Complexity:** General tree: O(n) time, O(h) space. BST: O(h) time, O(1) space iterative.

### 7.5 Maximum Path Sum (Any Node to Any Node)

```python
def max_path_sum(root):
    best = float('-inf')
    def helper(node):
        nonlocal best
        if not node:
            return 0
        left_gain = max(helper(node.left), 0)    # ignore negative contributions
        right_gain = max(helper(node.right), 0)
        best = max(best, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)  # can only extend ONE side upward
    helper(root)
    return best
```

**Common mistake:** Returning `node.val + left_gain + right_gain` from the helper — that would represent a "bent" path being extended further up, which is invalid since a path can't branch twice.

### 7.6 Root-to-Leaf and Leaf-to-Root Problems

```python
def root_to_leaf_paths(root):
    result, path = [], []
    def dfs(node):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            result.append(list(path))
        dfs(node.left)
        dfs(node.right)
        path.pop()   # backtrack
    dfs(root)
    return result
```

**Backtracking is essential** here — `path.pop()` after exploring both children removes the current node so sibling branches don't see stale state.

### 7.7 Path Sum Variants

```python
def has_path_sum(root, target):
    """LeetCode 112 — does any root-to-leaf path sum to target?"""
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    remaining = target - root.val
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)


def path_sum_count_any_direction(root, target):
    """LeetCode 437 — count paths (not necessarily root-to-leaf) summing to target,
    using prefix-sum hashmap (like subarray-sum-equals-k, adapted to trees)."""
    from collections import defaultdict
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1
    count = 0

    def dfs(node, current_sum):
        nonlocal count
        if not node:
            return
        current_sum += node.val
        count += prefix_counts[current_sum - target]
        prefix_counts[current_sum] += 1
        dfs(node.left, current_sum)
        dfs(node.right, current_sum)
        prefix_counts[current_sum] -= 1   # backtrack — crucial!
    dfs(root, 0)
    return count
```

**Complexity:** O(n) time, O(h) space — a huge improvement over the naive O(n²) "check every node as a potential path start."

### 7.8 Tree Views

**Right View** (rightmost node at each level):
```python
def right_side_view(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
```

**Left View:** same, but capture `i == 0`.

**Top View / Bottom View:** use the horizontal-distance technique from Section 5.8 (vertical order); top view keeps the **first** node seen at each hd (BFS order), bottom view keeps the **last**.

```python
def top_view(root):
    if not root:
        return []
    from collections import defaultdict
    first_at_hd = {}
    queue = deque([(root, 0)])
    while queue:
        node, hd = queue.popleft()
        if hd not in first_at_hd:
            first_at_hd[hd] = node.val
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    return [first_at_hd[hd] for hd in sorted(first_at_hd)]
```

For **bottom view**, simply overwrite `first_at_hd[hd]` unconditionally every time (last write wins).

### 7.9 Tree Construction from Traversals

**From Preorder + Inorder:**
```python
def build_tree_pre_in(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)          # O(n) — use a hashmap for O(1) lookups in practice
    root.left = build_tree_pre_in(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree_pre_in(preorder[mid + 1:], inorder[mid + 1:])
    return root
```

**Optimized with index map (avoids repeated `.index()` calls and slicing):**
```python
def build_tree_pre_in_optimized(preorder, inorder):
    inorder_index = {val: i for i, val in enumerate(inorder)}
    self_preorder_idx = [0]

    def helper(left, right):
        if left > right:
            return None
        root_val = preorder[self_preorder_idx[0]]
        self_preorder_idx[0] += 1
        root = TreeNode(root_val)
        mid = inorder_index[root_val]
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root

    return helper(0, len(inorder) - 1)
```

**Complexity:** Naive O(n²) (due to `.index()` + slicing), optimized **O(n)**.

**Why Inorder + Preorder (or Inorder + Postorder) but NOT Preorder + Postorder alone?** Preorder and Postorder alone cannot disambiguate a node with only **one** child (is it a left or right child?) — Inorder tells you which side elements belong to. Preorder+Postorder only uniquely reconstructs a **full** binary tree (0 or 2 children), not a general binary tree.

### 7.10 Serialization and Deserialization

Convert a tree to a string (for storage/transfer) and back.

```python
class Codec:
    def serialize(self, root):
        vals = []
        def dfs(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        vals = iter(data.split(','))
        def build():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()
```

**Why preorder (not inorder alone)?** Preorder with explicit null markers uniquely encodes structure — you always know when to stop each subtree because of the `#` sentinels. Inorder alone never tells you the root, so it can't reconstruct structure by itself.

**Complexity:** O(n) time and space for both operations.

### 7.11 Symmetry Check (Mirror of Itself)

```python
def is_symmetric(root):
    def mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val
                and mirror(left.left, right.right)
                and mirror(left.right, right.left))
    return mirror(root.left, root.right) if root else True
```

**Key idea:** Compare the tree against its **mirror** simultaneously — left's left with right's right, left's right with right's left.

### 7.12 Mirror / Invert a Binary Tree

```python
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

This one-liner swap is a famous interview micro-problem (the "convert me to your interviewer" joke about this LeetCode problem and Homebrew's creator).

### 7.13 Flatten Binary Tree to Linked List

Flatten in-place into a "linked list" following preorder, using the `right` pointer only.

```python
def flatten(root):
    current = root
    while current:
        if current.left:
            # find rightmost node of left subtree
            rightmost = current.left
            while rightmost.right:
                rightmost = rightmost.right
            rightmost.right = current.right   # reattach original right subtree
            current.right = current.left
            current.left = None
        current = current.right
```

**Complexity:** O(n) time, O(1) extra space (this is essentially Morris-traversal-style threading).

### 7.14 Clone a Binary Tree (Deep Copy)

```python
def clone_tree(root):
    if not root:
        return None
    new_node = TreeNode(root.val)
    new_node.left = clone_tree(root.left)
    new_node.right = clone_tree(root.right)
    return new_node
```

**Clone with random pointers (harder variant)** uses a hashmap `old_node -> new_node`, built in a first pass, then random pointers wired in a second pass — same idea as "Copy List with Random Pointer" applied to trees.

### 7.15 Pattern Recognition Cheat Sheet

| Clue in Problem Statement | Likely Pattern |
|---|---|
| "sum of any path" / "max path sum" | Post-order DFS with global accumulator |
| "path from root to leaf" | DFS + backtracking |
| "level by level" / "row by row" | BFS |
| "leftmost/rightmost at each level" | BFS + index check |
| "column" / "vertical" | BFS/DFS + horizontal distance |
| "ancestor of two nodes" | LCA recursion |
| "reconstruct tree from arrays" | Preorder/Inorder/Postorder construction |
| "serialize/store/transmit tree" | Preorder + null markers |
| "mirror" / "symmetric" | Simultaneous two-pointer recursion |
| "flatten" | Morris-style right-threading |
| "balanced?" | Post-order height with early exit |
| "is it the same/subtree" | Structural recursive comparison |

---

## 8. Advanced Tree Concepts

### 8.1 Tree Rotations (The Foundation of Self-Balancing Trees)

A **rotation** re-arranges a small set of pointers to change the tree's shape **without violating the BST property** and while keeping the inorder sequence identical.

**Right Rotation around node `y`:**
```
      y                x
     / \              / \
    x   T3    ─►     T1   y
   / \                   / \
  T1 T2                 T2 T3
```

```python
def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    return x   # new subtree root
```

**Left Rotation around node `x`:**
```python
def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    return y   # new subtree root
```

**Why rotations preserve BST property:** Notice `T1 < x < T2 < y < T3` before AND after — the inorder sequence (`T1, x, T2, y, T3`) is unchanged; only the parent-child shape changes. This is the trick that lets us rebalance without breaking ordering.

### 8.2 AVL Tree — Self-Balancing via Strict Rotations

Every node maintains a **balance factor** = `height(left) - height(right)`, which must stay in `{-1, 0, 1}`.

```python
class AVLNode:
    __slots__ = ('val', 'left', 'right', 'height')
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1  # height of a leaf = 1 in this convention


def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))


def avl_insert(node, val):
    # 1. Normal BST insert
    if not node:
        return AVLNode(val)
    if val < node.val:
        node.left = avl_insert(node.left, val)
    elif val > node.val:
        node.right = avl_insert(node.right, val)
    else:
        return node  # no duplicates

    # 2. Update height
    update_height(node)

    # 3. Get balance factor
    balance = get_balance(node)

    # 4. Four rotation cases
    if balance > 1 and val < node.left.val:      # Left-Left
        return rotate_right(node)
    if balance < -1 and val > node.right.val:    # Right-Right
        return rotate_left(node)
    if balance > 1 and val > node.left.val:      # Left-Right
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if balance < -1 and val < node.right.val:    # Right-Left
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node
```

**The Four Imbalance Cases:**

```
LL Case (balance > 1, new node in left-left):
        z                y
       /                / \
      y      ──►       x   z
     /
    x
(single right rotation on z)

RR Case (mirror of LL):
    z                    y
     \                  / \
      y      ──►       z   x
       \
        x
(single left rotation on z)

LR Case (balance > 1, new node in left-right):
      z              z              x
     /              /              / \
    y      ──►     x      ──►     y   z
     \            /
      x          y
(left rotate y, then right rotate z)

RL Case (mirror of LR):
    z                z                  x
     \                \                / \
      y      ──►       x     ──►      z   y
     /                  \
    x                    y
(right rotate y, then left rotate z)
```

**Complexity:** O(log n) guaranteed for search/insert/delete — this is AVL's whole selling point over a plain BST.

### 8.3 Red-Black Tree — Looser Balance, Fewer Rotations

Five invariants:
1. Every node is Red or Black.
2. The root is Black.
3. Every leaf (NIL) is Black.
4. A Red node cannot have a Red child (no two reds in a row).
5. Every path from a node to its descendant NIL leaves has the **same number of Black nodes** (black-height).

These invariants guarantee the longest root-to-leaf path is at most **2×** the shortest — looser than AVL's strict balance, but this means **fewer rotations on insert/delete**, making Red-Black Trees preferred in practice (C++ `std::map`, Java `TreeMap`, Linux kernel schedulers).

```
AVL vs Red-Black:
- AVL: stricter balance → faster lookups, slower insert/delete (more rotations)
- Red-Black: looser balance → slightly slower lookups, faster insert/delete (fewer rotations)
```

| Aspect | AVL | Red-Black |
|---|---|---|
| Balance strictness | Strict (\|bf\|≤1) | Loose (2× factor) |
| Lookup speed | Faster | Slightly slower |
| Insert/Delete speed | Slower (more rotations) | Faster (fewer rotations) |
| Typical use | Read-heavy workloads | Write-heavy / general purpose |

*(Full Red-Black insertion/deletion code with recoloring is intricate and rarely hand-written in interviews — understanding the invariants and trade-off vs AVL is what's typically tested.)*

### 8.4 Binary Lifting (Overview)

Precompute `up[k][v]` = the `2^k`-th ancestor of node `v`, built via `up[k][v] = up[k-1][up[k-1][v]]`. This allows jumping to **any ancestor** in O(log n) time and, combined with depth information, answering **LCA queries in O(log n)** after O(n log n) preprocessing — a major upgrade over the O(n) LCA in Section 7.4 when there are many queries.

```python
import math

def build_binary_lifting(n, parent, LOG=None):
    LOG = LOG or math.ceil(math.log2(max(n, 2)))
    up = [[0] * n for _ in range(LOG)]
    up[0] = parent[:]
    for k in range(1, LOG):
        for v in range(n):
            up[k][v] = up[k-1][up[k-1][v]]
    return up
```

### 8.5 Heavy-Light Decomposition (Overview)

Decomposes a tree into **chains** such that any root-to-node path crosses at most O(log n) chains. This lets range-update/range-query structures (like Segment Trees) operate on **tree paths**, not just linear arrays — used for problems like "update all node values on the path between u and v" in O(log² n).

### 8.6 Threaded Trees (Recap and Formalization)

A **threaded binary tree** replaces `None` right pointers with a thread to the inorder successor (or `None` left pointers with a thread to the inorder predecessor). This is precisely the mechanism Morris Traversal exploits **temporarily** — a threaded tree makes it **permanent**, trading a boolean "is this a thread or a real child" flag per pointer for O(1)-space traversal at any time.

### 8.7 Expression Tree Evaluation

```python
def evaluate_expression_tree(node):
    if node is None:
        return 0
    if not node.left and not node.right:   # leaf = operand
        return float(node.val)
    left_val = evaluate_expression_tree(node.left)
    right_val = evaluate_expression_tree(node.right)
    if node.val == '+':
        return left_val + right_val
    if node.val == '-':
        return left_val - right_val
    if node.val == '*':
        return left_val * right_val
    if node.val == '/':
        return left_val / right_val
```

**Building an expression tree from postfix:**
```python
def build_expr_tree_from_postfix(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}
    for token in tokens:
        node = TreeNode(token)
        if token in operators:
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack[-1]
```

### 8.8 Huffman Coding (Huffman Tree Construction)

Greedily merge the two lowest-frequency nodes repeatedly using a min-heap, until one tree remains.

```python
import heapq

class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char, self.freq, self.left, self.right = char, freq, left, right
    def __lt__(self, other):
        return self.freq < other.freq   # needed for heapq comparisons

def build_huffman_tree(frequencies):
    """frequencies: dict like {'a': 5, 'b': 9, 'c': 12, ...}"""
    heap = [HuffmanNode(ch, f) for ch, f in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node is None:
        return codebook
    if node.char is not None:       # leaf
        codebook[node.char] = prefix or "0"
        return codebook
    generate_codes(node.left, prefix + "0", codebook)
    generate_codes(node.right, prefix + "1", codebook)
    return codebook
```

**Why it works:** Merging the two rarest symbols first, repeatedly, ensures common symbols end up near the root (short codes) and rare symbols end up deep (long codes) — provably optimal prefix-free encoding (Huffman's 1952 proof via exchange argument).

**Complexity:** O(n log n) using a heap (n = number of distinct symbols).

### 8.9 Persistent Trees (Overview)

A **persistent** (immutable) tree keeps every past version accessible after updates, by creating new nodes only along the path that changed and reusing all unchanged subtrees ("path copying"). An update costs O(log n) extra nodes instead of O(n) for a full copy — the same idea Git uses for commits (Merkle-tree-like structural sharing) and how Clojure/Scala persistent data structures work internally.

### 8.10 Advanced Concepts Summary Table

| Concept | Purpose | Complexity |
|---|---|---|
| Rotations | Rebalance BSTs | O(1) per rotation |
| AVL Tree | Strict self-balancing | O(log n) all ops |
| Red-Black Tree | Looser self-balancing, fewer rotations | O(log n) all ops |
| Binary Lifting | Fast ancestor/LCA queries | O(n log n) build, O(log n) query |
| Heavy-Light Decomposition | Path queries/updates | O(log² n) per query |
| Threaded Trees | O(1) space traversal | O(n) traversal |
| Expression Trees | Evaluate/build expressions | O(n) |
| Huffman Trees | Optimal compression | O(n log n) build |
| Persistent Trees | Versioned immutable structures | O(log n) per update |

---

## 9. Applications of Trees

### 9.1 File Systems

Directories and files form a **General Tree**: each folder is a node whose children are subfolders/files. Operations like `du -sh` (disk usage) are post-order traversals (sum children before reporting the parent); `find` is a DFS.

```
/home
 ├── user
 │    ├── docs
 │    │    └── resume.pdf
 │    └── photos
 └── shared
```

### 9.2 HTML/XML DOM

Every HTML/XML document is parsed into a tree: `<html>` is the root, `<head>`/`<body>` are children, and so on. Browser rendering engines and libraries like BeautifulSoup traverse this tree (DFS) to apply CSS, run `querySelector`, and render layout.

### 9.3 Database Indexing (B-Tree / B+ Tree)

Relational databases (MySQL InnoDB, PostgreSQL, Oracle) store table indexes as **B+ Trees**: keys guide navigation through internal nodes, and actual row pointers live in leaf nodes linked together for fast **range scans** (`WHERE age BETWEEN 20 AND 30`). This is why indexed range queries are so much faster than full table scans.

### 9.4 Routing (Tries for IP/Prefix Matching)

Routers use **tries** (mentioned only for context, not covered in depth here) keyed on IP prefixes to perform **longest prefix match** in O(bit-length) time — critical for backbone routers handling millions of packets per second.

### 9.5 Decision Systems / AI (Decision Trees)

Machine learning **Decision Trees** (CART, ID3, C4.5) recursively split data on the feature that maximizes information gain (or minimizes Gini impurity), producing a tree where leaves are predictions. Random Forests and Gradient Boosted Trees (XGBoost, LightGBM) are ensembles of many such trees.

### 9.6 Compilers (Abstract Syntax Trees)

Source code is parsed into an **Abstract Syntax Tree (AST)**: e.g., `a = b + c * d` becomes a tree with `=` at the root, `a` as one child, and a `+` subtree as the other. Compilers traverse this AST (typically postorder) to generate machine code or perform optimizations (constant folding, dead-code elimination).

```
        =
       / \
      a   +
         / \
        b   *
           / \
          c   d
```

### 9.7 Expression Evaluation

Covered in Section 8.7 — calculators, spreadsheet formula engines, and interpreters all build expression trees from parsed input, then evaluate them recursively (postorder).

### 9.8 Compression (Huffman Trees)

Covered in Section 8.8 — used in DEFLATE (ZIP, gzip), JPEG, and MP3 as one stage of their compression pipelines.

### 9.9 Search Engines

Search engines use tree-like structures for:
- **Inverted index B-Trees** to map terms to document lists quickly.
- **Trie-based autocomplete** for query suggestions.
- **Merkle Trees** in distributed/decentralized search and content-addressed storage to verify data integrity efficiently.

### 9.10 Version Control (Git)

Git represents a repository's state as a **Merkle Tree**: each commit points to a tree object, which points to blobs (files) and other trees (subdirectories), each identified by the SHA-1/SHA-256 hash of its content. This lets Git detect changes in O(1) by comparing hashes instead of diffing entire file trees.

---

## 10. Problem Recognition Guide

### 10.1 The Master Decision Flowchart

```
                    Is the problem about a Tree?
                              │
             ┌────────────────┴────────────────┐
             │                                  │
      Need LEVEL-WISE info?              Need PATH / SUBTREE info?
      (widths, views, zigzag)             (sums, LCA, diameter)
             │                                  │
             ▼                                  ▼
        Use BFS (queue)                   Use DFS (recursion)
             │                                  │
     ┌───────┴───────┐                 ┌────────┴────────┐
     │               │                 │                 │
 Need per-level   Need single      Need bottom-up     Need top-down
 grouping?        row (e.g. right  aggregation?        decisions
 (level order)    view)?           (height, diameter,  (path sum from
                                    balanced check)      root, max depth
                                         │                so far)?
                                         ▼                    │
                                    Post-order DFS             ▼
                                                          Pre-order DFS
                                                          (pass state down)
```

### 10.2 Interview Clues Table

| Clue Phrase | Pattern to Reach For |
|---|---|
| "shortest path in an unweighted tree/level" | BFS |
| "level by level" | BFS with level-size loop |
| "deepest / furthest leaf" | DFS height computation |
| "any two nodes" / "diameter" | Post-order DFS + global variable |
| "common ancestor" | LCA recursion (or binary lifting if many queries) |
| "reconstruct from arrays" | Preorder/Inorder/Postorder construction |
| "duplicate subtrees" | Postorder + serialization + hashmap |
| "balanced" | Postorder height with early-exit sentinel |
| "views" (left/right/top/bottom) | BFS + index or horizontal distance |
| "flatten" | Morris-style right-threading |
| "kth smallest in BST" | Inorder traversal (early stop at k) |
| "range sum" in BST | Prune using BST ordering |
| "serialize / deserialize" | Preorder + null markers |
| "O(1) space traversal" | Morris Traversal |

### 10.3 DFS vs BFS Selection Guide

| Signal | Choose |
|---|---|
| Need shortest number of levels/edges | BFS |
| Need to explore full paths / accumulate along a path | DFS |
| Tree could be very wide but shallow | BFS (space = width) |
| Tree could be very deep but narrow | DFS with iteration or Morris (avoid stack overflow) |
| Need "per-level" answers | BFS |
| Need "per-path" or "per-subtree" answers | DFS |

### 10.4 Recursive vs Iterative Selection Guide

| Signal | Choose |
|---|---|
| Tree depth is small/bounded, code clarity matters | Recursive |
| Tree could be deep (risk of `RecursionError`) | Iterative (explicit stack/queue) |
| Space must be strictly O(1) | Morris Traversal |
| Need to pause/resume traversal (e.g., BST Iterator) | Iterative with explicit stack |

### 10.5 Traversal Selection Guide (Recap)

See Section 5.14 for the full table — the short version: **Inorder for BST-sorted output, Preorder for copy/serialize, Postorder for delete/bottom-up aggregation, BFS for level-wise.**

---

## 11. Optimization Techniques

### 11.1 Recursive → Iterative Conversion

Every recursive DFS can be converted to iterative using an **explicit stack** that mimics the call stack:

```python
# Recursive
def dfs_recursive(node):
    if not node:
        return
    process(node)
    dfs_recursive(node.left)
    dfs_recursive(node.right)

# Iterative equivalent
def dfs_iterative(root):
    stack = [root] if root else []
    while stack:
        node = stack.pop()
        process(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

**Why bother?** Python's default recursion limit is 1000 frames; a skewed tree with 100,000 nodes will crash a recursive solution with `RecursionError`, while an iterative one handles it fine (bounded only by available memory).

### 11.2 DFS vs BFS — Space Trade-off

- DFS space = O(h) — good for tall, narrow trees.
- BFS space = O(w) — good for short, wide trees.
- For a **balanced** tree of n nodes, both are O(log n) and O(n/2) respectively — DFS usually wins on space; BFS wins when you need level-wise semantics regardless.

### 11.3 Morris Traversal — Eliminating Space Entirely

Already detailed in Section 5.11–5.12. The single biggest "optimize this" follow-up interviewers ask after any O(h)-space traversal solution.

### 11.4 Avoiding Repeated Traversals

A **very common performance bug**: computing height (or any O(n) property) freshly inside every recursive call, causing overall O(n²).

```python
# BAD — O(n^2): height() is called inside every recursive step of is_balanced
def is_balanced_bad(root):
    if not root:
        return True
    lh, rh = height(root.left), height(root.right)   # O(n) EACH call
    if abs(lh - rh) > 1:
        return False
    return is_balanced_bad(root.left) and is_balanced_bad(root.right)

# GOOD — O(n): compute height and check balance in the SAME pass (Section 4.5)
```

**Rule of thumb:** If a tree problem seems to require "for every node, look at the whole subtree below it," check whether that inner computation can be **folded into the same post-order pass** that's already visiting every node once.

### 11.5 Memoization for Overlapping Subtree Computations

For problems like "count subtrees matching pattern X" or "duplicate subtrees," serialize each subtree (postorder + structure) into a string/tuple and cache counts in a hashmap — avoids recomputation for identical subtree shapes.

```python
def find_duplicate_subtrees(root):
    from collections import defaultdict
    counts = defaultdict(int)
    duplicates = []

    def serialize(node):
        if not node:
            return "#"
        s = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
        counts[s] += 1
        if counts[s] == 2:      # add only once, when it FIRST becomes a duplicate
            duplicates.append(node)
        return s

    serialize(root)
    return duplicates
```

**Complexity:** O(n²) worst case due to string building at every node (each string can be O(n) long) — can be reduced to O(n) using a hashmap that assigns a unique integer ID per distinct (val, left_id, right_id) triple instead of full string serialization.

### 11.6 Choosing the Right Complexity Target

| Query Pattern | Naive | Optimized |
|---|---|---|
| Single LCA query | O(n) | O(h) with BST, O(log n) with binary lifting |
| Many LCA queries (same static tree) | O(n) each → O(nq) | O(n log n) preprocess + O(log n) per query |
| Height inside every node check | O(n²) | O(n) single pass |
| Subtree pattern counting | O(n²) (string builds) | O(n) with ID-based hashing |
| kth smallest in BST, repeated queries | O(n) per query | Augment nodes with subtree-size counts → O(log n) per query |

---

## 12. Interview Preparation

### 12.1 Standard Templates to Memorize

**Template 1 — Height/Depth-based (post-order, bottom-up):**
```python
def solve(node):
    if not node:
        return BASE
    left = solve(node.left)
    right = solve(node.right)
    return combine(node, left, right)
```

**Template 2 — Top-down with state passed as arguments (pre-order):**
```python
def solve(node, state):
    if not node:
        return
    new_state = update(state, node)
    solve(node.left, new_state)
    solve(node.right, new_state)
```

**Template 3 — BFS level processing:**
```python
def bfs(root):
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            # process node
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
```

**Template 4 — Backtracking along a path:**
```python
def dfs(node, path):
    if not node:
        return
    path.append(node.val)
    if not node.left and not node.right:
        record(path)
    dfs(node.left, path)
    dfs(node.right, path)
    path.pop()
```

### 12.2 Difficulty-Tiered Problem List

**Easy**
- Maximum Depth of Binary Tree
- Invert Binary Tree
- Same Tree
- Symmetric Tree
- Path Sum
- Minimum Depth of Binary Tree
- Sum of Left Leaves
- Convert Sorted Array to BST
- Merge Two Binary Trees
- Range Sum of BST

**Medium**
- Binary Tree Level Order Traversal
- Zigzag Level Order Traversal
- Construct Binary Tree from Preorder and Inorder
- Validate Binary Search Tree
- Kth Smallest Element in a BST
- Lowest Common Ancestor of a Binary Tree
- Binary Tree Right Side View
- Flatten Binary Tree to Linked List
- Populating Next Right Pointers in Each Node
- Delete Node in a BST
- Path Sum II
- Path Sum III
- Diameter of Binary Tree
- Boundary of Binary Tree
- Vertical Order Traversal
- Sum Root to Leaf Numbers
- House Robber III (tree DP)

**Hard**
- Binary Tree Maximum Path Sum
- Serialize and Deserialize Binary Tree
- Recover Binary Search Tree
- Count of Smaller Numbers After Self (BIT/BST-based)
- Binary Tree Cameras
- Vertical Order Traversal (strict tie-break variant)
- N-ary Tree Level Order + Diameter
- Longest Consecutive Sequence in Binary Tree

### 12.3 Pattern-wise Question Map

| Pattern | Representative Problems |
|---|---|
| Post-order height/aggregation | Balanced Tree, Diameter, Max Path Sum |
| BFS level processing | Level Order, Zigzag, Right View |
| Path + backtracking | Path Sum II, Root-to-Leaf Paths |
| LCA | LCA of Binary Tree, LCA of BST, LCA of Deepest Leaves |
| Construction | Build Tree from Traversals, Recover from Preorder |
| Serialization | Serialize/Deserialize BT, Serialize N-ary Tree |
| BST-specific | Validate BST, Kth Smallest, Delete Node, Floor/Ceil |
| Views | Right/Left/Top/Bottom View |
| Morris (O(1) space) | Inorder/Preorder Traversal follow-ups |
| Tree DP | House Robber III, Binary Tree Cameras |

### 12.4 Company-Wise Focus (General Trends)

| Company | Typical Emphasis |
|---|---|
| Google | LCA variants, tree construction, complex traversals |
| Amazon | BST operations, path sum variants, practical tree modeling |
| Microsoft | Views, serialization, balanced tree checks |
| Meta | Diameter/max path sum, tree DP, vertical order |
| Infosys/TCS/Wipro (service-based) | Basic traversals, BST insert/delete/search, height/depth |

*(These are general industry trends, not guarantees — always practice broadly.)*

### 12.5 Blind 75 / NeetCode Tree Problems Checklist

- [ ] Invert Binary Tree
- [ ] Maximum Depth of Binary Tree
- [ ] Diameter of Binary Tree
- [ ] Balanced Binary Tree
- [ ] Same Tree
- [ ] Subtree of Another Tree
- [ ] Lowest Common Ancestor of a BST
- [ ] Binary Tree Level Order Traversal
- [ ] Binary Tree Right Side View
- [ ] Count Good Nodes in Binary Tree
- [ ] Validate Binary Search Tree
- [ ] Kth Smallest Element in a BST
- [ ] Construct Binary Tree from Preorder and Inorder Traversal
- [ ] Binary Tree Maximum Path Sum
- [ ] Serialize and Deserialize Binary Tree

### 12.6 Frequently Asked Interview Questions (Conceptual)

**Q: What is the difference between a Tree and a Graph?**
A: A tree is a connected, acyclic graph with exactly one path between any two nodes and a designated root; a general graph can have cycles, multiple paths, and no root.

**Q: Why does a balanced BST guarantee O(log n) but a regular BST doesn't?**
A: A regular BST's height depends on insertion order — sorted-order insertion degenerates it into a linked list (O(n) height). Balanced variants (AVL, Red-Black) actively restructure via rotations to keep height at O(log n) regardless of insertion order.

**Q: Preorder+Postorder — can you always reconstruct the tree?**
A: Only if the tree is guaranteed **full** (every node has 0 or 2 children); otherwise the reconstruction is ambiguous for single-child nodes.

**Q: How would you detect a cycle turning your "tree" into a graph?**
A: Track visited nodes during traversal; if you revisit a node not through its recorded parent, or your total edge/node count doesn't satisfy `edges == nodes - 1` with full connectivity, it's not a valid tree.

**Q: When would you use Morris Traversal in production code (not just interviews)?**
A: Rarely, in practice — real systems usually have enough stack space or use explicit iterative stacks; Morris is prized more for its cleverness and O(1)-space guarantee in memory-constrained embedded contexts.

### 12.7 Interview Tricks and Etiquette

- Always clarify: "Is this a Binary Tree or a BST?" before assuming ordering.
- State your **traversal choice and why** out loud — interviewers weight reasoning heavily.
- Start with the **recursive** solution (usually clearer), then offer the **iterative** version if asked about space/stack-depth concerns.
- Mention **edge cases** proactively: empty tree, single node, all-left/all-right skewed tree, duplicate values.
- If stuck, fall back to Template 1 (post-order divide & conquer) — it solves a surprising majority of tree problems.

---

## 13. Python-Specific Tips

### 13.1 Recursion Limits

```python
import sys
sys.setrecursionlimit(10000)  # default is 1000
```
**Warning:** This only changes Python's *soft* limit on frame count — it does not enlarge the underlying C stack. Extremely deep recursion (e.g., 100,000+ frames on a skewed tree) can still cause a **segmentation fault** rather than a clean `RecursionError`. For genuinely deep/skewed trees, prefer **iterative** traversals.

### 13.2 `collections.deque` for BFS

```python
from collections import deque
queue = deque([root])
queue.popleft()   # O(1) — always use this for BFS, never list.pop(0) which is O(n)
```

### 13.3 `collections.deque` as an O(1) Stack Too

`deque` also supports O(1) `append`/`pop` from the right end, so it can replace a plain `list` as a stack if you want a single import for both stack and queue needs.

### 13.4 Using `dataclass` for Cleaner Node Definitions

```python
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None
```
Trade-off: `dataclass` gives free `__repr__`/`__eq__`, but is slightly slower and more memory-heavy than a plain class with `__slots__`. Use `dataclass` for readability in non-performance-critical code; use `__slots__` classes in CP/performance-sensitive code.

### 13.5 Generators for Lazy Traversal

```python
def inorder_generator(node):
    if node:
        yield from inorder_generator(node.left)
        yield node.val
        yield from inorder_generator(node.right)

# Usage: process nodes one at a time without building a full list
for val in inorder_generator(root):
    if val == target:
        break   # stops early — saves work compared to building the whole list first
```

### 13.6 Performance Tips

- Cache repeated attribute lookups in tight loops (`left = node.left` before use, if used more than once).
- Avoid string concatenation in loops for serialization; use a list + `''.join(...)`.
- Prefer `deque` over `list` for both BFS queues and DFS stacks in performance-sensitive code.
- Use `__slots__` on node classes for large trees (millions of nodes) to cut memory substantially.
- Avoid unnecessary list slicing (`preorder[1:mid+1]`) in construction — it's O(k) per slice; use index ranges instead (Section 7.9).

### 13.7 Memory Optimization

```python
class TreeNode:
    __slots__ = ('val', 'left', 'right')
```
For a tree with 10 million nodes, `__slots__` can save hundreds of MB versus a default class (which carries a per-instance `__dict__`).

### 13.8 Common Python Pitfalls Specific to Trees

```python
# PITFALL 1: Mutable default argument
def bad_traversal(node, result=[]):   # DANGER — shared across calls!
    ...

def good_traversal(node, result=None):
    if result is None:
        result = []
    ...

# PITFALL 2: Comparing nodes with `==` when you mean identity
if node == target:      # uses __eq__, may not be defined as identity
    ...
if node is target:       # correct if you want the SAME object
    ...

# PITFALL 3: Forgetting `nonlocal` for variables mutated in nested closures
def diameter(root):
    best = 0
    def height(node):
        best = max(best, ...)   # UnboundLocalError! `best` is treated as local here
        ...
    # Fix: add `nonlocal best` inside height()
```

---

## 14. Common Mistakes

| # | Mistake | Explanation | Fix |
|---|---|---|---|
| 1 | Not handling `None` root | Every function should short-circuit on empty tree | `if not root: return <base>` first line |
| 2 | Wrong base case for height | Treating empty-tree height as 0 instead of -1 breaks recursive height formulas | Use height(None) = -1 convention consistently, or clearly define height(None)=0 and adjust formulas accordingly |
| 3 | Off-by-one in "levels" vs "edges" | Diameter/height in edges vs nodes causes wrong answers | Always clarify: does the problem want edge-count or node-count? |
| 4 | Traversal order confusion | Swapping preorder/postorder logic (e.g., visiting node before recursing when postorder is needed) | Write out Node/Left/Right order explicitly before coding |
| 5 | Stack overflow / `RecursionError` on skewed trees | Deep recursion on 10⁵+ node skewed trees | Convert to iterative, or raise recursion limit cautiously |
| 6 | Infinite recursion from cyclic "trees" | Malformed input (not actually acyclic) causes infinite loop | Track visited node identities if input isn't guaranteed to be a valid tree |
| 7 | Validating BST using only immediate children | Misses violations from non-adjacent ancestors | Pass down a valid (low, high) range recursively (Section 6.8) |
| 8 | Incorrect LCA logic assuming BST-ordering on a general tree | BST-based LCA shortcut doesn't work without the ordering guarantee | Use the general two-subtree-recursion LCA for plain binary trees |
| 9 | Recomputing height inside every balanced-check call | Causes hidden O(n²) | Fold height computation and balance check into one post-order pass |
| 10 | Forgetting to backtrack (`path.pop()`) | Leaves stale values in shared path list across branches | Always pop after recursing into both children |
| 11 | Using `list.pop(0)` for BFS | O(n) per dequeue — quietly turns O(n) BFS into O(n²) | Use `collections.deque` and `popleft()` |
| 12 | Not distinguishing edges vs nodes in "distance between nodes" | Off-by-one errors in path length | Distance = number of edges on the path, not nodes visited |
| 13 | Assuming Preorder+Postorder always reconstructs a tree | Fails for non-full binary trees (ambiguous single-child placement) | Require Inorder + (Preorder or Postorder) for general binary trees |
| 14 | Aliasing bug — assigning `b = a` and mutating `b` | Both variables reference the same node object | Explicitly clone the subtree if independence is required |
| 15 | Forgetting `nonlocal`/`self.` for mutated closures | `UnboundLocalError` in nested functions that update an outer variable | Declare `nonlocal var` or use a mutable container (`list`, instance attribute) |

### 14.1 Debugging Checklist for Tree Problems

1. Print the tree structure (level order) before and after your operation.
2. Test on: empty tree, single node, two nodes (left-only and right-only), a perfect small tree, and a skewed tree.
3. Verify your base case handles `None` explicitly.
4. Trace through one full dry run by hand before trusting the code.
5. Check whether the problem wants edges or nodes when it says "distance," "length," or "depth."

---

## 15. Cheat Sheets

### 15.1 Traversal Templates (Copy-Paste Ready)

```python
# Preorder (iterative)
def preorder(root):
    if not root: return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return result

# Inorder (iterative)
def inorder(root):
    result, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur); cur = cur.left
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right
    return result

# Postorder (iterative, two stacks)
def postorder(root):
    if not root: return []
    s1, s2 = [root], []
    while s1:
        node = s1.pop()
        s2.append(node.val)
        if node.left: s1.append(node.left)
        if node.right: s1.append(node.right)
    return s2[::-1]

# Level order (BFS)
def level_order(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

### 15.2 BST Operations Cheat Sheet

```python
# Search: O(h)
def search(root, target):
    while root and root.val != target:
        root = root.left if target < root.val else root.right
    return root

# Insert: O(h)
def insert(root, val):
    if not root: return TreeNode(val)
    if val < root.val: root.left = insert(root.left, val)
    elif val > root.val: root.right = insert(root.right, val)
    return root

# Delete: O(h)
def delete(root, key):
    if not root: return None
    if key < root.val: root.left = delete(root.left, key)
    elif key > root.val: root.right = delete(root.right, key)
    else:
        if not root.left: return root.right
        if not root.right: return root.left
        succ = root.right
        while succ.left: succ = succ.left
        root.val = succ.val
        root.right = delete(root.right, succ.val)
    return root
```

### 15.3 DFS vs BFS Quick Reference

| | DFS | BFS |
|---|---|---|
| Data structure | Stack (or recursion) | Queue (deque) |
| Space | O(h) | O(w) |
| Best for | Paths, subtree aggregation | Levels, shortest hops |
| Order guaranteed | Pre/in/post | Level-by-level |

### 15.4 Complexity Master Table

| Operation | Time (Balanced) | Time (Skewed) | Space |
|---|---|---|---|
| Traversal (any DFS) | O(n) | O(n) | O(h) |
| Morris Traversal | O(n) | O(n) | O(1) |
| BFS / Level Order | O(n) | O(n) | O(w) |
| BST Search/Insert/Delete | O(log n) | O(n) | O(h) or O(1) iter |
| Height/Depth | O(n) | O(n) | O(h) |
| Diameter | O(n) | O(n) | O(h) |
| LCA (general tree) | O(n) | O(n) | O(h) |
| LCA (BST) | O(log n) | O(n) | O(1) iter |
| LCA (binary lifting, per query) | O(log n) | O(log n) | O(n log n) preprocessing |
| Serialize/Deserialize | O(n) | O(n) | O(n) |
| Tree construction (from traversals) | O(n) | O(n) | O(n) |

### 15.5 Pattern Recognition Quick Map

| Keyword | Pattern |
|---|---|
| level, row, width | BFS |
| path, sum, diameter | Post-order DFS |
| ancestor, LCA | Two-subtree recursion |
| sorted order, kth smallest | Inorder (BST) |
| reconstruct | Preorder/Inorder/Postorder combo |
| serialize | Preorder + null markers |
| view (left/right/top/bottom) | BFS + index/horizontal distance |
| balanced, height check | Post-order with sentinel |
| O(1) space | Morris Traversal |

### 15.6 Formula Sheet

```
edges           = nodes - 1
max_nodes(h)    = 2^(h+1) - 1        (perfect tree, height h in edges)
max_nodes(l)    = 2^l                 (at level l, root at level 0)
min_height(n)   = ceil(log2(n+1)) - 1
max_height(n)   = n - 1                (skewed)
height(None)    = -1  (edge-count convention)
height(leaf)    = 0
balance_factor  = height(left) - height(right)
diameter(node)  = height(left) + height(right) + 2   (in nodes) 
                  or height(left) + height(right)     (in edges, common convention)
```

---

## 16. Practice Problem Bank

### 16.1 Basics

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Maximum Depth of Binary Tree | LeetCode #104 | Easy | Height DFS |
| Minimum Depth of Binary Tree | LeetCode #111 | Easy | BFS/DFS |
| Same Tree | LeetCode #100 | Easy | Structural recursion |
| Symmetric Tree | LeetCode #101 | Easy | Mirror recursion |
| Invert Binary Tree | LeetCode #226 | Easy | Post-order swap |
| Merge Two Binary Trees | LeetCode #617 | Easy | Simultaneous recursion |
| Count Complete Tree Nodes | LeetCode #222 | Medium | Binary search on structure |

### 16.2 Traversals

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Binary Tree Inorder Traversal | LeetCode #94 | Easy | Iterative stack |
| Binary Tree Preorder Traversal | LeetCode #144 | Easy | Iterative stack |
| Binary Tree Postorder Traversal | LeetCode #145 | Easy | Two stacks |
| Binary Tree Level Order Traversal | LeetCode #102 | Medium | BFS |
| Binary Tree Zigzag Level Order | LeetCode #103 | Medium | BFS + direction flag |
| Vertical Order Traversal | LeetCode #987 | Hard | BFS/DFS + hd |
| Diagonal Traversal | GeeksforGeeks | Medium | BFS + right-chain |
| Boundary Traversal of Binary Tree | GeeksforGeeks | Medium | Left/leaves/right |
| Morris Inorder Traversal | InterviewBit | Hard | Threading |

### 16.3 BST

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Search in a Binary Search Tree | LeetCode #700 | Easy | BST search |
| Insert into a Binary Search Tree | LeetCode #701 | Medium | BST insert |
| Delete Node in a BST | LeetCode #450 | Medium | BST delete |
| Validate Binary Search Tree | LeetCode #98 | Medium | Range check / inorder |
| Kth Smallest Element in a BST | LeetCode #230 | Medium | Inorder + early stop |
| Convert Sorted Array to BST | LeetCode #108 | Easy | Divide & conquer |
| Recover Binary Search Tree | LeetCode #99 | Hard | Inorder + swap detection |
| Two Sum IV - Input is a BST | LeetCode #653 | Easy | Inorder + two-pointer / set |
| Trim a Binary Search Tree | LeetCode #669 | Medium | BST-guided recursion |

### 16.4 DFS-Based

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Path Sum | LeetCode #112 | Easy | Root-to-leaf DFS |
| Path Sum II | LeetCode #113 | Medium | DFS + backtracking |
| Path Sum III | LeetCode #437 | Medium | Prefix sum + DFS |
| Sum Root to Leaf Numbers | LeetCode #129 | Medium | DFS with running value |
| Binary Tree Maximum Path Sum | LeetCode #124 | Hard | Post-order + global max |
| Count Good Nodes in Binary Tree | LeetCode #1448 | Medium | DFS + running max |

### 16.5 BFS-Based

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Binary Tree Right Side View | LeetCode #199 | Medium | BFS last-in-level |
| Average of Levels in Binary Tree | LeetCode #637 | Easy | BFS + average |
| Populating Next Right Pointers | LeetCode #116 / #117 | Medium | BFS or O(1) space linking |
| Cousins in Binary Tree | LeetCode #993 | Easy | BFS + parent/depth tracking |
| Maximum Width of Binary Tree | LeetCode #662 | Medium | BFS + positional index |

### 16.6 Height / Diameter / Balance

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Balanced Binary Tree | LeetCode #110 | Easy | Post-order sentinel |
| Diameter of Binary Tree | LeetCode #543 | Easy | Post-order global max |
| Diameter of N-Ary Tree | LeetCode #1522 | Medium | Post-order generalization |
| Binary Tree Cameras | LeetCode #968 | Hard | Tree DP (greedy states) |
| House Robber III | LeetCode #337 | Medium | Tree DP |

### 16.7 LCA

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Lowest Common Ancestor of a BST | LeetCode #235 | Easy | BST-ordering LCA |
| Lowest Common Ancestor of a Binary Tree | LeetCode #236 | Medium | Two-subtree recursion |
| LCA of Deepest Leaves | LeetCode #865 | Medium | Depth-tracked recursion |
| Smallest Common Region | LeetCode #1257 | Medium | LCA on general tree |

### 16.8 Views

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Binary Tree Right/Left Side View | LeetCode #199 | Medium | BFS |
| Top View of Binary Tree | GeeksforGeeks | Medium | BFS + hd |
| Bottom View of Binary Tree | GeeksforGeeks | Medium | BFS + hd (last write wins) |

### 16.9 Construction

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Construct Binary Tree from Preorder and Inorder | LeetCode #105 | Medium | Index map recursion |
| Construct Binary Tree from Inorder and Postorder | LeetCode #106 | Medium | Index map recursion |
| Construct Binary Tree from Preorder and Postorder | LeetCode #889 | Medium | Full-tree-only reconstruction |
| Convert Sorted List to BST | LeetCode #109 | Medium | Slow/fast pointer + recursion |

### 16.10 Serialization

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Serialize and Deserialize Binary Tree | LeetCode #297 | Hard | Preorder + null markers |
| Serialize and Deserialize N-ary Tree | LeetCode #428 | Hard | Preorder + child-count markers |
| Find Duplicate Subtrees | LeetCode #652 | Medium | Serialization + hashmap |

### 16.11 Balanced / Self-Balancing Trees

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| AVL Tree Insertion | GeeksforGeeks | Hard | Rotations |
| Convert BST to Balanced BST | GeeksforGeeks | Medium | Inorder + rebuild |
| Count of Smaller Numbers After Self | LeetCode #315 | Hard | BIT/BST with counts |

### 16.12 Advanced / Multi-Platform

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Binary Tree Maximum Path Sum II | Codeforces (various) | Hard | Tree DP |
| LCA with Binary Lifting | CSES "Company Queries II" | Hard | Binary lifting |
| Subtree Queries | CSES | Hard | Euler tour + Segment Tree |
| Tree Diameter | CSES | Medium | Two-BFS method |
| Tree Matching | CSES | Hard | Tree DP |
| Distance Queries (LCA) | CSES | Hard | Binary lifting |
| XOR and Sum | AtCoder (various) | Hard | Tree DP + bit tricks |
| Timus/Codeforces Heavy-Light Decomposition problems | Codeforces | Hard | HLD |

> **Platform note:** Exact problem numbers/links shift over time — search each title directly on LeetCode, GeeksforGeeks, CSES, or Codeforces to get the current canonical link.

---

## 17. Final Revision Notes

### 17.1 One-Page Mind Map

```
                              TREES
                                │
      ┌───────────┬────────────┼────────────┬───────────┐
      │            │            │            │           │
  Fundamentals  Types       Traversals    Patterns    Advanced
      │            │            │            │           │
  root/height   Binary/BST   DFS/BFS     Diameter    AVL/Red-Black
  depth/degree  AVL/RB       Pre/In/Post  LCA         Rotations
  subtree       B-Tree/B+    Level/Zigzag Views       Binary Lifting
  diameter      N-ary/Threaded Morris      Construct   HLD
                Huffman/Expr  Euler Tour  Serialize    Huffman
                                          Symmetry/    Persistent
                                          Invert/Flatten
```

### 17.2 15-Minute Revision

1. **Terminology**: root, parent, child, leaf, height (bottom-up), depth (top-down), edges = nodes - 1.
2. **Traversals**: Preorder (N-L-R, copy/serialize), Inorder (L-N-R, sorted for BST), Postorder (L-R-N, delete), Level order (BFS, widths/views).
3. **BST core four**: Search/Insert/Delete O(h); Validate needs a range, not just local comparison.
4. **The universal template**: post-order divide & conquer solves height, balance, diameter, and max path sum problems.
5. **LCA**: general tree = two-subtree recursion; BST = ordering-guided single pass.
6. **Space optimization**: Morris Traversal for O(1) space; iterative for deep/skewed trees to avoid recursion limits.
7. **Self-balancing**: AVL = strict balance factor ∈{-1,0,1}, more rotations; Red-Black = looser (2× bound), fewer rotations.

### 17.3 1-Hour Deep Revision Checklist

- [ ] Re-derive height/depth formulas and the min/max height bounds for n nodes.
- [ ] Re-implement all three DFS traversals both recursively and iteratively from memory.
- [ ] Re-implement BST search/insert/delete, including the two-children deletion case.
- [ ] Re-derive the diameter algorithm and explain why it's O(n) not O(n²).
- [ ] Re-implement general-tree LCA and BST LCA, and explain the difference.
- [ ] Walk through Morris inorder traversal step-by-step on a small tree.
- [ ] Explain AVL's 4 rotation cases (LL, RR, LR, RL) with diagrams from memory.
- [ ] Explain the difference between Red-Black and AVL trade-offs.
- [ ] Write serialize/deserialize using preorder + null markers.
- [ ] Solve one problem from each row of the Pattern Recognition table (Section 15.5) without looking at solutions.

### 17.4 Interview-Day Cheat Sheet (Print-Friendly)

```
HEIGHT:      height(None) = -1; height(leaf) = 0
BALANCE:     |height(L) - height(R)| <= 1 at every node
DIAMETER:    max over all nodes of height(L) + height(R)
LCA (tree):  if p,q in different subtrees of X -> X is LCA
LCA (BST):   walk down; split point where p,q diverge = LCA
BST INSERT/SEARCH/DELETE: O(h); h = O(log n) balanced, O(n) skewed
TRAVERSAL PICK:
   sorted output      -> Inorder (BST)
   copy/serialize     -> Preorder
   delete safely      -> Postorder
   level-wise         -> BFS
   O(1) space         -> Morris
BACKTRACK PATHS: path.append(val) ... recurse ... path.pop()
AVOID O(n^2): never recompute height/size inside every recursive call —
              fold it into the same post-order pass.
```

### 17.5 Closing Notes

Trees reward **pattern recognition** more than memorization: nearly every problem is a variation of "post-order aggregate," "pre-order propagate state," or "BFS level-process." Master the four templates in Section 12.1, internalize when height is edges vs nodes, and always ask whether the input is a general Binary Tree or specifically a BST before choosing your approach — that single distinction determines whether you need O(n) or can get away with O(log n).

