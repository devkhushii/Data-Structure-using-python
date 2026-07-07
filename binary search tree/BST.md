# 🌳 The Complete Binary Search Tree (BST) Handbook

---

## 📖 Table of Contents

1. [Introduction to BST](#1-introduction-to-bst)
2. [BST Fundamentals & Terminology](#2-bst-fundamentals--terminology)
3. [Python Implementation Foundations](#3-python-implementation-foundations)
4. [Core Operation: Search](#4-core-operation-search)
5. [Core Operation: Insert](#5-core-operation-insert)
6. [Core Operation: Delete](#6-core-operation-delete)
7. [BST Traversals](#7-bst-traversals)
8. [Morris Traversal (O(1) Space)](#8-morris-traversal-o1-space)
9. [Minimum & Maximum](#9-minimum--maximum)
10. [Successor & Predecessor](#10-successor--predecessor)
11. [Floor & Ceil](#11-floor--ceil)
12. [BST Validation](#12-bst-validation)
13. [Recover Swapped BST](#13-recover-swapped-bst)
14. [Kth Smallest / Kth Largest](#14-kth-smallest--kth-largest)
15. [BST Iterator](#15-bst-iterator)
16. [Lowest Common Ancestor (LCA)](#16-lowest-common-ancestor-lca)
17. [Range Search & Range Sum](#17-range-search--range-sum)
18. [Trim a BST](#18-trim-a-bst)
19. [Convert BST to Greater Tree](#19-convert-bst-to-greater-tree)
20. [Construct BST (Sorted Array / Preorder)](#20-construct-bst-sorted-array--preorder)
21. [Serialize & Deserialize BST](#21-serialize--deserialize-bst)
22. [Advanced BST Concepts](#22-advanced-bst-concepts)
23. [Real-World Applications](#23-real-world-applications)
24. [Problem Recognition Playbook](#24-problem-recognition-playbook)
25. [Optimization Playbook](#25-optimization-playbook)
26. [Python-Specific Tips](#26-python-specific-tips)
27. [Common Mistakes Catalogue](#27-common-mistakes-catalogue)
28. [Master Cheat Sheets](#28-master-cheat-sheets)
29. [Practice Problem Bank](#29-practice-problem-bank)
30. [Final Revision & FAQs](#30-final-revision--faqs)

---

## 1. Introduction to BST

### 1.1 What Is a BST?

A **Binary Search Tree (BST)** is a node-based binary tree data structure in which every node has at most two children (`left` and `right`), and which satisfies the **BST invariant**:

> For every node `N`, all values in `N.left` subtree are **strictly less than** `N.val`, and all values in `N.right` subtree are **strictly greater than** `N.val` (assuming no duplicates).

This single rule is what makes a BST different from a plain **Binary Tree** — a binary tree only cares about "at most two children"; a BST additionally cares about **ordering**.

### 1.2 Why Does BST Exist?

Before BSTs, the two common ways to store ordered data were:

| Structure | Search | Insert | Delete | Problem |
|---|---|---|---|---|
| Unsorted Array | O(n) | O(1) | O(n) | Search is slow |
| Sorted Array | O(log n) | O(n) | O(n) | Insert/Delete require shifting |
| Linked List | O(n) | O(1) | O(1) | No fast search |

BSTs were invented to give **O(log n)** search, insert, and delete **simultaneously** (on average/balanced case) — something none of the above structures could do together. This is the entire motivation for the data structure's existence.

### 1.3 Intuition & Real-World Analogy

Think of a BST like a **phone book organized as a decision game**: "Is the name before or after M?" Each comparison eliminates roughly half the remaining search space — exactly like **binary search on a sorted array**, except the tree lets you *insert and delete* efficiently too, which a static sorted array cannot do without heavy shifting.

Another analogy: a **filing cabinet with labeled dividers** where every divider tells you "smaller files to the left drawer, larger files to the right drawer," recursively, drawer within drawer.

### 1.4 BST Property — Visualized

```
                    Valid BST                         Invalid BST
                 ┌───────────┐                      ┌───────────┐
                 │     8     │                      │     8     │
                 └─────┬─────┘                      └─────┬─────┘
              ┌────────┴────────┐                ┌────────┴────────┐
          ┌───┴───┐          ┌───┴───┐        ┌───┴───┐          ┌───┴───┐
          │   3   │          │  10   │        │   3   │          │  10   │
          └───┬───┘          └───┬───┘        └───┬───┘          └───┬───┘
        ┌─────┴─────┐            └───┐       ┌─────┴─────┐            └───┐
    ┌───┴───┐   ┌───┴───┐        ┌───┴───┐  ┌───┴───┐   ┌───┴───┐     ┌───┴───┐
    │   1   │   │   6   │        │  14   │  │   1   │   │   9   │     │  14   │
    └───────┘   └───────┘        └───────┘  └───────┘   └───────┘     └───────┘
     all < 8     all < 8         all > 8      all < 8     9 > 8 but is
     ✅ correct   ✅ correct      ✅ correct    ✅ correct   in LEFT subtree
                                                            of 8 ❌ WRONG!
```

**Key insight for the invalid tree:** `9` is greater than `8`, but it sits in the **left subtree of 8**. Even though `9 > 3` and `9 > 1` (locally looks fine against its direct parent `3`), the BST rule is **global**, not just "compare to parent" — this is the #1 source of bugs when validating BSTs (see [Section 12](#12-bst-validation)).

### 1.5 Mathematical & Structural Properties

| Property | Description |
|---|---|
| Inorder traversal | Always produces values in **strictly increasing (sorted)** order |
| Height (balanced) | `O(log n)` |
| Height (skewed/degenerate) | `O(n)` — behaves like a linked list |
| Number of distinct BSTs on `n` nodes | Catalan number `C(n) = (2n)! / ((n+1)! * n!)` |
| Space | `O(n)` nodes, each with 2 pointers + value |
| Minimum element | Leftmost node |
| Maximum element | Rightmost node |

### 1.6 Advantages

- Fast **O(log n)** search/insert/delete when balanced.
- Maintains **sorted order** implicitly (inorder traversal).
- Supports **order-statistics** queries (kth smallest, rank, floor, ceil) naturally.
- Dynamic — unlike sorted arrays, grows/shrinks efficiently.
- Basis for advanced structures: AVL, Red-Black Trees, B-Trees, Order-Statistic Trees.

### 1.7 Disadvantages

- **Not guaranteed balanced** — adversarial/sorted input degenerates it to O(n) (a linked list in disguise).
- No O(1) random access (unlike arrays).
- More memory overhead per element (two pointers) than a flat array.
- Cache-unfriendly compared to arrays (pointer chasing).

### 1.8 Applications Preview

Databases (indexes), symbol tables/compilers, `TreeMap`/`TreeSet`-like ordered containers, filesystem directory structures, priority-based scheduling, range queries — detailed in [Section 23](#23-real-world-applications).

> **📝 Note:** Python's built-in `dict` and `set` are **hash tables**, not BSTs — Python has **no built-in BST** in its standard library. This is why understanding BSTs conceptually (and implementing them yourself) matters so much for interviews — you can't just `import BST`.

> **💡 Interview Tip:** If you see phrases like *"sorted," "kth smallest," "range between two values," "closest value,"* or *"maintain order while allowing insert/delete,"* — think BST immediately.


---

## 2. BST Fundamentals & Terminology

| Term | Definition |
|---|---|
| **Root** | The topmost node; has no parent |
| **Parent** | A node that has one or more child nodes |
| **Child** | A node directly connected below another node |
| **Leaf** | A node with no children |
| **Ancestor** | Any node on the path from root to a given node (exclusive of the node itself) |
| **Descendant** | Any node reachable downward from a given node |
| **Sibling** | Nodes sharing the same parent |
| **Height of a node** | Number of edges on the longest downward path from that node to a leaf |
| **Depth of a node** | Number of edges from the root to that node |
| **Level** | `depth + 1` (root is Level 1) |
| **Degree of a node** | Number of children it has (0, 1, or 2) |
| **Path** | A sequence of nodes connected by edges |
| **Balanced BST** | `\|height(left) - height(right)\| ≤ 1` for every node (recursively) |
| **Skewed / Degenerate BST** | Every node has at most 1 child — tree behaves like a linked list |

### 2.1 Balanced vs Skewed — Visualized

```
   Balanced BST (height ≈ log n)         Skewed BST (height = n) — WORST CASE
            4                                  1
          /   \                                 \
         2     6                                  2
        / \   / \                                  \
       1   3 5   7                                   3
                                                        \
   Height = 2, n = 7                                     4
   Search = O(log n)                                      \
                                                             5
                                                     Height = 4, n = 5
                                                     Search = O(n)
```

This happens when you insert **already-sorted data** (`1,2,3,4,5...`) into a plain BST — every new node becomes the rightmost (or leftmost) child. This is *the* classic BST pitfall and the reason self-balancing trees (AVL, Red-Black) exist.

> **⚠️ Warning:** A plain BST gives **no guarantee** on height. Worst-case complexity for search/insert/delete is **O(n)**, not O(log n). Average-case (random insertion order) is O(log n). Interviewers expect you to know and state this distinction.

---

## 3. Python Implementation Foundations

### 3.1 The `TreeNode` Class

```python
class TreeNode:
    """A single node in a Binary Search Tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # the value stored in this node
        self.left = left    # reference to left child (TreeNode or None)
        self.right = right  # reference to right child (TreeNode or None)

    def __repr__(self):
        return f"TreeNode({self.val})"
```

**Line-by-line explanation:**
- `val=0, left=None, right=None`: default arguments let you build a node with just a value (`TreeNode(5)`), or fully specify children for testing.
- `self.left` / `self.right`: these are **object references** (pointers). In Python, everything is a reference; `self.left = some_node` just makes `self.left` point to the same object in memory as `some_node` — no copying occurs.
- `__repr__`: purely for debugging convenience (so `print(node)` is readable).

### 3.2 Memory Representation

```
TreeNode object in memory:
┌─────────────────────────┐
│ id: 0x7f3a...            │
│ val:   8                 │
│ left:  ──────► points to TreeNode(3) object at 0x7f3b...
│ right: ──────► points to TreeNode(10) object at 0x7f3c...
└─────────────────────────┘
```

Each `TreeNode` is a separate heap-allocated Python object. `left`/`right` are **references** (like pointers in C), not embedded sub-objects. This is why setting `node.left = None` **detaches** the subtree from the tree (Python's garbage collector reclaims it if nothing else references it) without deleting the child nodes' own internal structure.

### 3.3 The `BST` Wrapper Class

```python
class BST:
    """Wrapper class holding a reference to the root TreeNode."""
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None
```

**Why wrap it?** Keeping a `BST` class (rather than passing bare `TreeNode`s around) lets you:
- Track `self.root` cleanly (root can change during delete/insert-into-empty-tree).
- Attach helper methods (`insert`, `search`, `delete`, `inorder`) as methods on one object — closer to how real libraries (`sortedcontainers`, Java's `TreeMap`) are structured.

> **📝 Note:** Throughout this handbook, standalone functions like `insert(root, val)` (returning the new subtree root) are shown first because that's the **most common interview format** (LeetCode gives you a `root: TreeNode` argument, not a class). The `BST` class wrapper is shown as the "real-world" production-style alternative.

### 3.4 Best Practices for Python BST Code

- Always **return the (possibly new) subtree root** from recursive `insert`/`delete` functions — this is the cleanest way to handle root re-assignment without global variables.
- Prefer **iterative** implementations in production code paths that must avoid Python's recursion limit (`sys.setrecursionlimit`, default ~1000) for very large/skewed trees.
- Use `None` (never `-1`, `float('inf')`, sentinel nodes) to represent "no child" unless you have a specific reason (e.g., a sentinel `NIL` node, common in Red-Black tree implementations, is a valid advanced technique).
- Type hints (`Optional[TreeNode]`) make BST code far more readable in real codebases:

```python
from typing import Optional

def search(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    ...
```


---

## 4. Core Operation: Search

### 4.1 Problem Statement
Given the root of a BST and a `target` value, determine whether the value exists, and/or return the node containing it.

### 4.2 Why BST Search Beats Linear Search
At every node, the BST property lets you **discard an entire subtree** without visiting it — exactly like binary search on a sorted array, except you're walking a tree instead of indexing an array.

### 4.3 Visualization — Search Path

```
Search for 6 in:
                 8
               /   \
              3     10
             / \       \
            1   6       14
               /
              4

Path taken:
  8 → 6 < 8 → go LEFT
  3 → 6 > 3 → go RIGHT
  6 → 6 == 6 → FOUND ✅

Visited: 8 → 3 → 6   (3 comparisons, not 7 nodes)
```

### 4.4 Recursive Implementation

```python
def search_recursive(root, target):
    if root is None or root.val == target:
        return root                      # found, or hit a dead end (None)
    if target < root.val:
        return search_recursive(root.left, target)
    return search_recursive(root.right, target)
```

**Line-by-line:**
1. `if root is None or root.val == target: return root` — base case: either we've fallen off the tree (`None`) or found the value; both cases return `root` directly (which is `None` in the "not found" case).
2. `if target < root.val:` — BST property tells us the target, if present, **must** be in the left subtree.
3. `return search_recursive(root.left, target)` — recurse left.
4. `return search_recursive(root.right, target)` — implicit else: recurse right.

### 4.5 Iterative Implementation

```python
def search_iterative(root, target):
    current = root
    while current is not None:
        if target == current.val:
            return current
        current = current.left if target < current.val else current.right
    return None
```

**Line-by-line:**
- `current = root` — start pointer at the root.
- `while current is not None:` — loop until we fall off the tree.
- `current = current.left if target < current.val else current.right` — move one level down, left or right, using the BST property.
- `return None` — loop exhausted without a match ⇒ not found.

### 4.6 Complete Dry Run

Searching for `target = 6` in the tree above:

| Step | Current Node | Comparison | Decision | Next |
|---|---|---|---|---|
| 1 | 8 | 6 < 8 | Go left | 3 |
| 2 | 3 | 6 > 3 | Go right | 6 |
| 3 | 6 | 6 == 6 | **Found**, return node | — |

Searching for `target = 5` (not present):

| Step | Current Node | Comparison | Decision | Next |
|---|---|---|---|---|
| 1 | 8 | 5 < 8 | Go left | 3 |
| 2 | 3 | 5 > 3 | Go right | 6 |
| 3 | 6 | 5 < 6 | Go left | 4 |
| 4 | 4 | 5 > 4 | Go right | `None` |
| 5 | `None` | — | **Not found**, return `None` | — |

### 4.7 Complexity Analysis

| Case | Time | Space (Recursive) | Space (Iterative) |
|---|---|---|---|
| Balanced BST | O(log n) | O(log n) — call stack | O(1) |
| Skewed BST | O(n) | O(n) — call stack | O(1) |

### 4.8 Recursive vs Iterative — When to Use

| Aspect | Recursive | Iterative |
|---|---|---|
| Readability | Cleaner, mirrors the BST definition | Slightly more verbose |
| Stack usage | Uses call stack (risk of `RecursionError` on skewed trees with `n > ~1000`) | O(1) auxiliary space |
| Interview default | Fine for most problems | Preferred when asked for "O(1) space" or "no recursion" |
| Production code | Avoid for very large/unbalanced trees | Preferred for robustness |

> **⚠️ Warning:** On a **skewed** BST with thousands of nodes, `search_recursive` can raise `RecursionError: maximum recursion depth exceeded`. Always mention this trade-off in interviews — it shows depth of understanding.

### 4.9 Edge Cases
- Empty tree (`root is None`) → return `None` immediately.
- Target equals root's value → return immediately (don't recurse further).
- Target smaller than every node / larger than every node → traverse to a leaf, then fall off (`None`).
- Duplicate values (if allowed by a custom implementation) → decide *and document* a convention (e.g., duplicates go right) — ambiguity here is a common interview trap.

### 4.10 Common Mistakes
- Forgetting the `is None` check and calling `.val` on `None` → `AttributeError`.
- Using `<=`/`>=` inconsistently between insert and search (must match the tree's duplicate convention).
- Re-searching from `root` on every step instead of updating `current` (turns O(log n) into O(n log n) accidentally).

### 4.11 Interview Tips
- Always clarify: *"Are duplicates allowed? What's the convention?"* before coding.
- Mention both recursive and iterative solutions proactively — strong signal of depth.
- State complexity **in terms of height `h`**, then clarify `h = log n` (balanced) vs `h = n` (skewed).

### 4.12 Practice Problems
- LeetCode 700 — Search in a Binary Search Tree (Easy)
- GeeksforGeeks — Search in BST


---

## 5. Core Operation: Insert

### 5.1 Problem Statement
Insert a new value into a BST while preserving the BST property, and return the (possibly new) root.

### 5.2 Intuition
Insertion is "search for where the value *would* be, then attach it there." A new value always becomes a **new leaf** (in the simple/unbalanced BST — no rotations).

### 5.3 Visualization

```
Insert 5 into:
        8                       8
      /   \                   /   \
     3     10       ──►      3     10
    / \       \             / \       \
   1   6       14          1   6       14
                               /
                              5

Path: 8 → go left (5<8) → 3 → go right (5>3) → 6 → go left (5<6) → None → attach 5 here
```

### 5.4 Recursive Implementation

```python
def insert_recursive(root, val):
    if root is None:
        return TreeNode(val)             # base case: found the empty spot
    if val < root.val:
        root.left = insert_recursive(root.left, val)
    elif val > root.val:
        root.right = insert_recursive(root.right, val)
    # if val == root.val: duplicate — typically ignored (no-op)
    return root                          # always return root so parent can re-link
```

**Line-by-line:**
1. `if root is None: return TreeNode(val)` — we've found the exact empty slot; create and return a new node — this becomes the new child of the caller.
2. `root.left = insert_recursive(root.left, val)` — recurse left, and **re-assign** `root.left` to the (possibly unchanged) result. This re-assignment is what actually attaches the new node.
3. Same logic mirrored for `root.right`.
4. `return root` — every call must return `root` so that the parent's re-assignment (`root.left = ...`) doesn't accidentally overwrite an existing subtree with `None`.

> **💡 Why `return root` at the end matters:** This is the single most important line beginners get wrong. If you forget it (or forget to use the return value at the call site), the newly built subtree is silently discarded because Python passes references by value — reassigning `root` inside the function does **not** affect the caller's variable unless you explicitly propagate it back via `return`.

### 5.5 Iterative Implementation

```python
def insert_iterative(root, val):
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
            break                         # duplicate — ignore
    return root
```

**Line-by-line:**
- `new_node = TreeNode(val)` — pre-create the node we'll attach.
- `if root is None: return new_node` — empty tree special case; the new node becomes the root.
- `current = root` — pointer for traversal, root itself stays fixed so we can return it at the end.
- The `while True` loop walks down; when it finds a `None` child slot in the correct direction, it attaches `new_node` and `break`s.

### 5.6 Complete Dry Run

Insert `5` into the tree from §5.3 (values: 8,3,10,1,6,14):

| Step | Current Node | Comparison | Action |
|---|---|---|---|
| 1 | 8 | 5 < 8 | Go left → 3 |
| 2 | 3 | 5 > 3 | Go right → 6 |
| 3 | 6 | 5 < 6 | `current.left is None` → attach `TreeNode(5)` as left child of 6 |

Recursive call-stack trace for the same insert:

```
insert(8, 5)
 └─ 5<8 → root.left = insert(3, 5)
             └─ 5>3 → root.left.right = insert(6, 5)
                          └─ 5<6 → root.left.right.left = insert(None, 5)
                                       └─ returns TreeNode(5)
                          └─ 6.left = TreeNode(5); return 6
             └─ 3.right = 6 (unchanged); return 3
 └─ 8.left = 3 (unchanged); return 8
```

### 5.7 Complexity Analysis

| Case | Time | Space |
|---|---|---|
| Balanced | O(log n) | O(log n) recursive / O(1) iterative |
| Skewed | O(n) | O(n) recursive / O(1) iterative |

### 5.8 Edge Cases
- Inserting into an empty tree → new node becomes root.
- Inserting a duplicate → convention-dependent (commonly: no-op, or push to right subtree — **must be stated explicitly**).
- Inserting values in strictly sorted order repeatedly → produces a **skewed tree** (see §2.1) — a classic interview follow-up: *"what happens if I insert 1,2,3,4,5 in order?"*

### 5.9 Common Mistakes
- Forgetting to `return root` (or the recursive call's result) — new node silently lost.
- Using `current = current.left` inside the iterative version but never updating `current.left`/`current.right` of the **previous** node — always track the parent, or restructure as shown above (check-before-move pattern) to avoid needing a separate parent pointer.
- Not handling duplicates consistently between `insert` and `search`/`delete`.

### 5.10 Interview Tips
- Always ask: *"Can I assume no duplicates? If duplicates exist, what should happen?"*
- Mention that **insertion order determines final shape** — this segues nicely into "that's why self-balancing trees exist" (AVL/Red-Black), showing broader knowledge.

### 5.11 Practice Problems
- LeetCode 701 — Insert into a Binary Search Tree (Medium)
- GeeksforGeeks — Insertion in BST


---

## 6. Core Operation: Delete

Deletion is the **hardest** of the three core BST operations because there are **three distinct structural cases**.

### 6.1 Problem Statement
Delete a node with a given value from a BST, preserving the BST property, and return the (possibly new) root.

### 6.2 The Three Cases — Visualized

```
CASE 1: Node to delete has NO children (leaf)
──────────────────────────────────────────────
Delete 1:
        8                    8
      /   \                /   \
     3     10   ──►       3     10
    / \       \             \      \
   1   6       14            6      14
Simply remove the leaf (set parent's pointer to None).


CASE 2: Node to delete has EXACTLY ONE child
──────────────────────────────────────────────
Delete 3 (has only left child... wait — has two here; use a 1-child example):
        8                       8
      /   \                   /   \
     3     10      ──►       1     10
    /         \                       \
   1           14                      14
Replace the node with its single child (splice it out).


CASE 3: Node to delete has TWO children
──────────────────────────────────────────────
Delete 8:
        8                       10
      /   \                    /  \
     3     10      ──►        3    14
    / \       \              / \
   1   6       14           1   6
Strategy: replace 8's value with its INORDER SUCCESSOR
(smallest value in right subtree = 10), then delete 10
from the right subtree (which is now a simpler case-1/case-2 delete).
```

> **📝 Note:** You could equally use the **inorder predecessor** (largest value in left subtree) instead of the successor — both are valid and commonly accepted. Successor is more common in textbooks/interviews.

### 6.3 Recursive Implementation (Full)

```python
def delete_node(root, key):
    if root is None:
        return None                                # key not found; nothing to delete

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # ---- FOUND THE NODE TO DELETE ----
        if root.left is None and root.right is None:      # Case 1: leaf
            return None
        if root.left is None:                              # Case 2: only right child
            return root.right
        if root.right is None:                              # Case 2: only left child
            return root.left
        # Case 3: two children
        successor = find_min(root.right)                    # smallest in right subtree
        root.val = successor.val                            # copy successor's value up
        root.right = delete_node(root.right, successor.val) # delete the duplicate successor
    return root


def find_min(node):
    while node.left is not None:
        node = node.left
    return node
```

**Line-by-line explanation:**
1. `if root is None: return None` — base case: key doesn't exist in this subtree; nothing to do.
2. `if key < root.val: root.left = delete_node(root.left, key)` — recurse left, re-attach result (mirrors insert's re-linking pattern).
3. `elif key > root.val: ...` — recurse right, mirrored.
4. `else:` — we are standing at the node to delete.
5. **Case 1** (`both children None`): simply return `None` — the caller's re-assignment (`root.left = ...` or `root.right = ...`) detaches this node.
6. **Case 2a** (`left is None`): return `root.right` — this single child "replaces" the deleted node in the parent's eyes.
7. **Case 2b** (`right is None`): symmetric, return `root.left`.
8. **Case 3** (both children exist):
   - `successor = find_min(root.right)` — find the smallest value in the right subtree (guaranteed to have **no left child** itself, by definition of "smallest").
   - `root.val = successor.val` — overwrite the current node's value with the successor's value. **We do not physically move nodes** — we copy the value, which is simpler and avoids re-wiring pointers.
   - `root.right = delete_node(root.right, successor.val)` — now delete the *original* successor node from the right subtree; since the successor has no left child, this recursive call will hit **Case 1 or Case 2**, never Case 3 again.
9. `return root` — propagate the (possibly value-mutated, possibly unchanged) root back up.

### 6.4 Iterative Implementation

```python
def delete_node_iterative(root, key):
    parent = None
    current = root

    # Step 1: locate the node to delete and its parent
    while current is not None and current.val != key:
        parent = current
        current = current.left if key < current.val else current.right

    if current is None:
        return root                       # key not found

    # Step 2: handle case of two children by swapping with inorder successor
    if current.left is not None and current.right is not None:
        succ_parent = current
        succ = current.right
        while succ.left is not None:
            succ_parent = succ
            succ = succ.left
        current.val = succ.val             # copy successor value
        # Now delete the successor node instead (it has at most 1 right child)
        parent, current = succ_parent, succ

    # Step 3: current now has at most one child — splice it out
    child = current.left if current.left is not None else current.right
    if parent is None:
        root = child                       # deleting the root itself
    elif parent.left is current:
        parent.left = child
    else:
        parent.right = child

    return root
```

**Line-by-line:**
- **Step 1** walks down tracking `parent`, exactly like iterative search, but also remembers who the parent was (needed since we must re-link the parent's pointer, and there's no call stack doing that automatically).
- **Step 2** only triggers for the two-children case: finds the inorder successor (leftmost node of right subtree) and its parent, copies the successor's value into `current`, then **re-targets** `current`/`parent` to point at the successor node itself (which we still need to physically remove).
- **Step 3** performs the actual splice: after step 2 (or immediately, if we never had two children), `current` has 0 or 1 child. `child` is that one child (or `None`). We attach `child` in place of `current` on whichever side of `parent` it was.

### 6.5 Complete Dry Run (Case 3 — Two Children)

Tree:
```
        8
      /   \
     3     10
    / \       \
   1   6       14
```
Delete `key = 8`:

| Step | Current | Action | Notes |
|---|---|---|---|
| 1 | 8 | `key == root.val` → both children exist → **Case 3** | |
| 2 | — | `find_min(root.right)` → walk `10 → (10.left is None)` → successor = `10` | |
| 3 | — | `root.val = 10` → node formerly "8" now holds value `10` | |
| 4 | — | `root.right = delete_node(10, 10)` → recurse into right subtree to remove the original 10 | |
| 5 | 10 (right subtree) | `key == root.val`, `left is None` → **Case 2** → return `root.right` (which is `14`) | |
| Result | — | Right subtree becomes just `14`; top node's value is now `10` | |

Final tree:
```
        10
      /   \
     3     14
    / \
   1   6
```

### 6.6 Complexity Analysis

| Case | Time | Space (Recursive) | Space (Iterative) |
|---|---|---|---|
| Balanced BST | O(log n) | O(log n) | O(1) |
| Skewed BST | O(n) | O(n) | O(1) |

### 6.7 Edge Cases
- Deleting from an empty tree → no-op, return `None`.
- Deleting a value not present → traverse to `None`, return unchanged tree.
- Deleting the **root** itself (all 3 cases apply to root exactly the same way — no special-casing needed in the recursive version, since the function returns the new subtree root and the caller reassigns `self.root = delete_node(self.root, key)`).
- Deleting a node whose **successor is its direct right child** (i.e., `root.right` has no left child) — `delete_node(root.right, successor.val)` should still work correctly; trace through it to convince yourself (it collapses to Case 2 immediately).
- Tree with only one node, deleting it → returns `None` — becomes an empty tree.

### 6.8 Common Mistakes
- Forgetting one of the 3 cases (most commonly: handling two-children but forgetting to also handle the *single-child* cases separately — a two-children check like `if root.left and root.right` must come **after** the two "only-one-child" checks, or you'll crash on `find_min(None)`).
- Physically **swapping nodes** (rewiring pointers) instead of **copying the successor's value** — this is *possible* but extremely error-prone; copying the value is the standard, safe approach.
- Using **predecessor** logic but accidentally searching the wrong subtree (predecessor = largest in **left** subtree, not right).
- Not returning the updated `root`/child reference, silently losing the reattached subtree (same bug class as in insert).

### 6.9 Interview Tips
- Explicitly narrate the 3 cases out loud before coding — interviewers reward structured thinking.
- Mention that using predecessor instead of successor is an equally valid alternative (shows flexibility).
- If asked for O(1) space, provide the iterative version and explain why recursion depth matches tree height.

### 6.10 Practice Problems
- LeetCode 450 — Delete Node in a BST (Medium)
- GeeksforGeeks — Deletion in BST
- InterviewBit — Delete Value in BST


---

## 7. BST Traversals

### 7.1 Why Traversals Matter for BSTs Specifically
In a plain binary tree, traversal order is just "a way to visit nodes." In a **BST**, **inorder traversal has a special, extremely important property**:

> **Inorder traversal of a BST always visits nodes in strictly increasing sorted order.**

This is *the* reason BSTs are so useful for order-statistics problems (kth smallest, range queries, closest value, floor/ceil) — sorted order comes "for free" from the tree's shape, with no explicit sort step needed.

### 7.2 Why Inorder Produces Sorted Order (Proof by Structure)

By the BST property, for any node `N`: everything in `N.left` < `N.val` < everything in `N.right`. Inorder traversal visits `left subtree`, then `N`, then `right subtree` — which, applied recursively, guarantees: (everything smaller) → (N) → (everything bigger), at every level. This recursive "smaller, self, bigger" pattern *is* sorted order by definition.

### 7.3 Visualization — All Traversals on One Tree

```
                 8
               /   \
              3     10
             / \       \
            1   6       14
               / \
              4   7

Inorder   (L, Node, R):  1, 3, 4, 6, 7, 8, 10, 14   ← SORTED
Preorder  (Node, L, R):  8, 3, 1, 6, 4, 7, 10, 14
Postorder (L, R, Node):  1, 4, 7, 6, 3, 14, 10, 8
Level Order (BFS):       8, 3, 10, 1, 6, 14, 4, 7
Reverse Inorder (R,N,L): 14, 10, 8, 7, 6, 4, 3, 1  ← REVERSE SORTED
```

### 7.4 Recursive Implementations

```python
def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)
    return result


def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.val)
        preorder(root.left, result)
        preorder(root.right, result)
    return result


def postorder(root, result=None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.val)
    return result
```

> **⚠️ Warning:** Never use a **mutable default argument** like `def inorder(root, result=[])`. Python default arguments are evaluated **once**, at function-definition time — every call without an explicit `result` would share and keep appending to the **same list** across calls. Always use `result=None` and initialize inside the function, as shown.

### 7.5 Iterative Implementations (Using an Explicit Stack)

```python
def inorder_iterative(root):
    result, stack = [], []
    current = root
    while current is not None or stack:
        while current is not None:      # push all left children
            stack.append(current)
            current = current.left
        current = stack.pop()           # visit
        result.append(current.val)
        current = current.right         # move to right subtree
    return result


def preorder_iterative(root):
    if root is None:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:                  # push right FIRST so left is popped first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def postorder_iterative(root):
    if root is None:
        return []
    result, stack = [], [root]
    output = []
    while stack:
        node = stack.pop()
        output.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return output[::-1]                 # reverse of (Node, Right, Left) = (Left, Right, Node)


def level_order(root):
    from collections import deque
    if root is None:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

**Key line-by-line notes:**
- `inorder_iterative`: simulates recursion's call-stack behavior manually — dive all the way left (pushing each node), then pop-visit-go-right, repeat.
- `preorder_iterative`: pushes **right before left** so that popping (LIFO) processes left first — a common "trick" worth memorizing.
- `postorder_iterative`: computes a **reversed postorder** using the same trick as preorder (push left before right, giving Node→Right→Left order), then reverses the final list — simpler than the "true" two-stack postorder algorithm.
- `level_order`: uses `collections.deque` for O(1) `popleft()` (a plain `list.pop(0)` is O(n) — a very common Python performance mistake).

### 7.6 Recursive Call Stack Visualization (Inorder)

```
inorder(8)
 ├─ inorder(3)
 │   ├─ inorder(1)
 │   │   ├─ inorder(None) → returns
 │   │   ├─ visit 1
 │   │   └─ inorder(None) → returns
 │   ├─ visit 3
 │   └─ inorder(6)
 │       ├─ inorder(4) → visit 4
 │       ├─ visit 6
 │       └─ inorder(7) → visit 7
 ├─ visit 8
 └─ inorder(10)
     ├─ inorder(None) → returns
     ├─ visit 10
     └─ inorder(14) → visit 14

Call stack depth at deepest point: 8→3→1 = depth 3 (matches tree height)
Output order: 1, 3, 4, 6, 7, 8, 10, 14
```

### 7.7 Dry Run Table — Iterative Inorder

| Step | Action | Stack (top→bottom) | Current | Output so far |
|---|---|---|---|---|
| 1 | push 8, go left | [8] | 3 | [] |
| 2 | push 3, go left | [8,3] | 1 | [] |
| 3 | push 1, go left | [8,3,1] | None | [] |
| 4 | pop 1, visit, go right | [8,3] | None | [1] |
| 5 | pop 3, visit, go right | [8] | 6 | [1,3] |
| 6 | push 6, go left | [8,6] | 4 | [1,3] |
| 7 | push 4, go left | [8,6,4] | None | [1,3] |
| 8 | pop 4, visit, go right | [8,6] | None | [1,3,4] |
| 9 | pop 6, visit, go right | [8] | 7 | [1,3,4,6] |
| 10 | push 7, go left | [8,7] | None | [1,3,4,6] |
| 11 | pop 7, visit, go right | [8] | None | [1,3,4,6,7] |
| 12 | pop 8, visit, go right | [] | 10 | [1,3,4,6,7,8] |
| 13 | push 10, go left | [10] | None | [1,3,4,6,7,8] |
| 14 | pop 10, visit, go right | [] | 14 | [1,3,4,6,7,8,10] |
| 15 | push 14, go left | [14] | None | [1,3,4,6,7,8,10] |
| 16 | pop 14, visit, go right | [] | None | [1,3,4,6,7,8,10,14] |

### 7.8 Complexity Analysis

| Traversal | Time | Space (Recursive) | Space (Iterative) |
|---|---|---|---|
| Inorder/Preorder/Postorder | O(n) | O(h) call stack | O(h) explicit stack |
| Level Order | O(n) | — | O(w) — max width of tree |

`h` = height (O(log n) balanced, O(n) skewed). `w` = max width (can be up to `n/2` for the last level).

### 7.9 Edge Cases
- Empty tree → all traversals return `[]`.
- Single-node tree → all traversals return `[val]`.
- Skewed tree → level order has O(1) width but O(n) depth; inorder/preorder/postorder still work but stack depth = n.

### 7.10 Common Mistakes
- Using `list.pop(0)` for a queue (O(n) each call) instead of `collections.deque.popleft()` (O(1)).
- Mutable default argument bug (`result=[]`), covered in §7.4.
- Confusing preorder/postorder push order (pushing left before right in preorder gives the **wrong** output order).

### 7.11 Interview Tips
- Always state clearly: *"Inorder gives sorted order because of the BST property"* — this single sentence signals real understanding, not memorized code.
- If asked "print BST elements in range [L,R]," mention you can **prune** traversal branches using the BST property (see [Section 17](#17-range-search--range-sum)) rather than doing a full O(n) traversal + filter.

### 7.12 Practice Problems
- LeetCode 94 — Binary Tree Inorder Traversal
- LeetCode 144 / 145 — Preorder / Postorder Traversal
- LeetCode 102 — Binary Tree Level Order Traversal
- GeeksforGeeks — Tree Traversals


---

## 8. Morris Traversal (O(1) Space)

### 8.1 Why Morris Traversal Exists
All traversals above use **O(h) auxiliary space** (call stack or explicit stack). **Morris Traversal** achieves **O(1) extra space** by temporarily turning the tree into a **threaded structure** using the tree's own unused `right` pointers — no stack, no recursion.

### 8.2 Core Idea
For each node, before going left, create a **temporary thread**: link the **rightmost node of the left subtree** (the inorder predecessor) back to the current node. This lets you "return" to the current node after finishing the left subtree — mimicking what a stack would normally remember — without using extra memory. The thread is removed once used, restoring the original tree.

### 8.3 Visualization

```
Before (normal tree):              During Morris (temporary thread added):
        8                                   8
      /   \                               /   \
     3     10                            3     10
    / \       \                         / \       \
   1   6       14                      1   6       14
                                             \
                                              (6's rightmost desc. in its OWN left subtree,
                                               here trivial; thread points back to 8's
                                               subtree root as needed during traversal)

Concept: predecessor.right = current  (temporary thread)
         ... traverse left subtree fully via the thread ...
         predecessor.right = None     (thread removed, tree restored)
```

### 8.4 Morris Inorder Traversal — Implementation

```python
def morris_inorder(root):
    result = []
    current = root

    while current is not None:
        if current.left is None:
            result.append(current.val)          # no left subtree: visit now
            current = current.right
        else:
            # find the inorder predecessor (rightmost node in left subtree)
            predecessor = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current       # create the thread
                current = current.left
            else:
                predecessor.right = None          # thread already exists: remove it
                result.append(current.val)        # visit current NOW (after left subtree done)
                current = current.right
    return result
```

**Line-by-line explanation:**
1. `if current.left is None:` — no left subtree means there's nothing more to defer; visit `current` immediately and move right.
2. `predecessor = current.left; while predecessor.right ...` — walk to the rightmost node of the left subtree (this is `current`'s inorder predecessor).
3. `if predecessor.right is None: predecessor.right = current; current = current.left` — **first visit**: no thread exists yet, so create one (`predecessor.right = current`) and dive into the left subtree.
4. `else: predecessor.right = None; result.append(current.val); current = current.right` — **second visit** (we've returned via the thread after finishing the left subtree): remove the thread (restore original structure), visit `current`, then move right.

### 8.5 Complete Dry Run

Tree:
```
        8
      /   \
     3     10
    / \       \
   1   6       14
```

| Step | current | Action | Thread created/removed | Output |
|---|---|---|---|---|
| 1 | 8 | has left; predecessor = rightmost(3's subtree) = 6 | 6.right = 8 (thread) | [] |
| 2 | 3 | has left; predecessor = 1 | 1.right = 3 (thread) | [] |
| 3 | 1 | no left → visit, go right (via thread) | — | [1] |
| 4 | 3 (via thread) | predecessor(1).right == current(3) → remove thread, visit 3, go right | 1.right = None | [1,3] |
| 5 | 6 | has left? No (6 has no left in this example... wait it does in §7 example) | — | — |
| ... | ... | (continues similarly) | ... | [1,3,4,6,7,8,10,14] |

*(Full mechanical trace omitted for brevity beyond the pattern above — the key mechanic to remember is: **first arrival creates the thread and goes left; second arrival [detected via the thread] removes the thread, visits, and goes right**.)*

### 8.6 Complexity Analysis

| Metric | Value |
|---|---|
| Time | O(n) — each edge is traversed at most twice (once to create thread, once to remove it) |
| Space | **O(1)** — no stack, no recursion; only pointer variables |

### 8.7 Recursive/Iterative-Stack vs Morris — Comparison

| Aspect | Stack-based Iterative | Morris |
|---|---|---|
| Space | O(h) | **O(1)** |
| Time | O(n) | O(n) |
| Mutates tree temporarily | No | **Yes** (threads added & removed) |
| Thread-safety (concurrent reads) | Safe | **Unsafe** — tree is briefly modified |
| Complexity to implement | Low | Higher — easy to get predecessor-finding wrong |

> **⚠️ Warning:** Morris Traversal temporarily mutates the tree. If another thread/process reads the tree concurrently during traversal, it will see a corrupted structure. Never use Morris Traversal on trees that must remain read-consistent under concurrency.

### 8.8 Edge Cases
- Empty tree → returns `[]` immediately (loop never executes).
- Every node has no left child (right-skewed) → behaves exactly like simple `while current: visit; current = current.right` — no threading ever needed.
- Left-skewed tree → predecessor search is O(1) each time (immediate left child has no right child), so total time stays O(n).

### 8.9 Common Mistakes
- Forgetting to check `predecessor.right is not current` in the while loop — without it, you'd walk **through** an existing thread indefinitely (infinite loop) instead of detecting it.
- Forgetting to remove the thread (`predecessor.right = None`) — leaves the tree permanently corrupted.
- Visiting the node at the wrong time (before vs after removing the thread) — swaps inorder output order.

### 8.10 Interview Tips
- Morris Traversal is a **strong differentiator** in FAANG interviews — mention it proactively when asked for O(1) space traversal, but only implement it if you have practiced it (it's easy to introduce subtle bugs under pressure).
- Morris **Preorder** is a small variant: visit `current` on **first** arrival (right when the thread is created) instead of on second arrival.

### 8.11 Morris Preorder (Variant)

```python
def morris_preorder(root):
    result = []
    current = root
    while current is not None:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right
            if predecessor.right is None:
                result.append(current.val)      # visit BEFORE going left (preorder!)
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                current = current.right
    return result
```

### 8.12 Practice Problems
- LeetCode 94 — Binary Tree Inorder Traversal (follow-up: O(1) space)
- LeetCode 99 — Recover Binary Search Tree (uses Morris traversal idea) — see [Section 13](#13-recover-swapped-bst)


---

## 9. Minimum & Maximum

### 9.1 Intuition
By the BST property, the **minimum** value is always found by going **left as far as possible**; the **maximum** by going **right as far as possible**.

### 9.2 Visualization

```
        8
      /   \
     3     10
    / \       \
   1   6       14

Minimum: 8→3→1 (1 has no left child) → MIN = 1
Maximum: 8→10→14 (14 has no right child) → MAX = 14
```

### 9.3 Implementation (Iterative — Preferred)

```python
def find_min(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root

def find_max(root):
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root
```

### 9.4 Recursive Alternative

```python
def find_min_recursive(root):
    if root is None or root.left is None:
        return root
    return find_min_recursive(root.left)
```

### 9.5 Complexity

| Case | Time | Space |
|---|---|---|
| Balanced | O(log n) | O(1) iterative / O(log n) recursive |
| Skewed | O(n) | O(1) iterative / O(n) recursive |

### 9.6 Common Mistakes
- Forgetting the `root is None` guard on an empty tree → crash.
- Confusing min/max direction (left=min, right=max) — easy to mix up under interview pressure.

### 9.7 Practice Problems
- GeeksforGeeks — Minimum/Maximum in BST
- Used as a **subroutine** in [Delete](#6-core-operation-delete) (Case 3) and [Successor/Predecessor](#10-successor--predecessor).

---

## 10. Successor & Predecessor

### 10.1 Definitions
- **Inorder Successor** of a node `N`: the node with the **smallest value greater than** `N.val` (i.e., the "next" node in sorted/inorder order).
- **Inorder Predecessor** of a node `N`: the node with the **largest value smaller than** `N.val` (the "previous" node in sorted order).

### 10.2 Two Cases for Successor

```
CASE A: N has a right subtree
────────────────────────────────
Successor = leftmost (minimum) node of N's right subtree.

        8                    Successor of 8:
      /   \                  → go right to 10
     3     10                → go left as far as possible: 10 has no left child
    / \       \              → Successor = 10
   1   6       14


CASE B: N has NO right subtree
────────────────────────────────
Successor = the lowest ancestor of N for which N lies in the LEFT subtree.

        8
      /   \
     3     10
    / \       \
   1   6       14
      / \
     4   7

Successor of 7: 7 has no right child.
Walk UP from 7: parent is 6 — 7 is in 6's RIGHT subtree, so 6 is NOT the answer, keep going up.
Parent of 6 is 3 — 6 is in 3's RIGHT subtree, so 3 is NOT the answer either, keep going up.
Parent of 3 is 8 — 3 is in 8's LEFT subtree! → Successor of 7 = 8
```

### 10.3 Implementation — Successor (With Root, No Parent Pointers)

This is the most common interview version: given only the `root` and a `target` value (no parent pointers), find the inorder successor **in O(h) time using the BST property directly** (no need to physically locate the node first).

```python
def inorder_successor(root, target_val):
    successor = None
    current = root
    while current is not None:
        if target_val < current.val:
            successor = current           # current is a CANDIDATE successor
            current = current.left        # look for a smaller valid candidate
        else:
            current = current.right       # target_val >= current.val, go right
    return successor
```

**Line-by-line explanation:**
- `if target_val < current.val:` — `current` is **larger** than target, so it's a **possible** answer; but there might be an even smaller valid one further left, so remember it (`successor = current`) and continue left.
- `else:` — `current` is `<=` target, so it and its entire left subtree are too small to be the successor; go right to look for something bigger.
- This single pass naturally finds the answer for **both Case A and Case B** above, without ever needing parent pointers — it's a beautiful property of using value comparisons directly on the BST structure.

### 10.4 Implementation — Predecessor (Mirror Logic)

```python
def inorder_predecessor(root, target_val):
    predecessor = None
    current = root
    while current is not None:
        if target_val > current.val:
            predecessor = current
            current = current.right
        else:
            current = current.left
    return predecessor
```

### 10.5 Complete Dry Run — Successor of 7

Tree:
```
        8
      /   \
     3     10
    / \       \
   1   6       14
      / \
     4   7
```

| Step | current | Comparison | successor updated? | Next |
|---|---|---|---|---|
| 1 | 8 | 7 < 8 | successor = 8 | go left → 3 |
| 2 | 3 | 7 > 3 | no change | go right → 6 |
| 3 | 6 | 7 > 6 | no change | go right → 7 |
| 4 | 7 | 7 == 7 (not `<`) | no change | go right → `None` |
| 5 | `None` | loop ends | — | return `successor = 8` ✅ |

### 10.6 Complexity Analysis

| Case | Time | Space |
|---|---|---|
| Balanced | O(log n) | O(1) |
| Skewed | O(n) | O(1) |

### 10.7 Edge Cases
- Target is the **maximum** value in the tree → no successor exists → return `None`.
- Target is the **minimum** value → no predecessor exists → return `None`.
- Target value not present in the tree at all → the algorithm still works (it finds where the value **would** fit and returns the appropriate neighbor) — useful for "closest greater/smaller value" style problems.

### 10.8 Common Mistakes
- Using `<=` instead of `<` (or vice versa) — flips whether the target itself, if present, is treated as its own successor (bug).
- Assuming parent pointers are available when they're not (many implementations don't have them — the value-comparison approach in §10.3 avoids this dependency entirely).
- Confusing successor logic with predecessor logic (mirror images — easy to swap by mistake).

### 10.9 Interview Tips
- Emphasize that this approach works in **O(h)**, single pass, **no need to physically find the node first** — many candidates over-complicate by first searching for the node, then walking up (requires parent pointers) — the direct-comparison method shown is more elegant and is the expected optimal answer.

### 10.10 Practice Problems
- LeetCode 285 — Inorder Successor in a BST (Medium)
- LeetCode 510 — Inorder Successor in a BST II (with parent pointers)
- GeeksforGeeks — Predecessor and Successor in BST


---

## 11. Floor & Ceil

### 11.1 Definitions
- **Floor(k)**: the **largest** value in the BST that is **≤ k**.
- **Ceil(k)**: the **smallest** value in the BST that is **≥ k**.

(Contrast with successor/predecessor, which are strictly `<` / `>` a target **node's value**; floor/ceil work for **any query value `k`**, whether or not `k` itself is present in the tree, and are inclusive of equality.)

### 11.2 Visualization

```
        8
      /   \
     3     10
    / \       \
   1   6       14

Floor(7)  = 6   (largest value ≤ 7)
Ceil(7)   = 8   (smallest value ≥ 7)
Floor(8)  = 8   (exact match allowed)
Ceil(15)  = None (nothing ≥ 15 exists)
Floor(0)  = None (nothing ≤ 0 exists)
```

### 11.3 Implementation

```python
def floor_bst(root, key):
    result = None
    current = root
    while current is not None:
        if current.val == key:
            return current.val                # exact match is its own floor
        if current.val < key:
            result = current.val               # candidate; look for a bigger one ≤ key
            current = current.right
        else:
            current = current.left
    return result


def ceil_bst(root, key):
    result = None
    current = root
    while current is not None:
        if current.val == key:
            return current.val
        if current.val > key:
            result = current.val               # candidate; look for a smaller one ≥ key
            current = current.left
        else:
            current = current.right
    return result
```

**Line-by-line (floor):**
- `if current.val == key: return current.val` — exact match is trivially its own floor.
- `if current.val < key:` — this node is a **valid candidate** (it's `≤ key`); but a larger, still-valid candidate might exist further right, so remember it and continue right.
- `else:` (i.e., `current.val > key`) — this node is too big to be the floor; discard it and go left, looking for something smaller.

Ceil mirrors this exactly with left/right and comparisons swapped.

### 11.4 Complete Dry Run — Floor(7)

| Step | current | Comparison | result updated? | Next |
|---|---|---|---|---|
| 1 | 8 | 8 > 7 | no | go left → 3 |
| 2 | 3 | 3 < 7 | result = 3 | go right → 6 |
| 3 | 6 | 6 < 7 | result = 6 | go right → `None` |
| 4 | `None` | loop ends | — | return `6` ✅ |

### 11.5 Complexity Analysis

| Case | Time | Space |
|---|---|---|
| Balanced | O(log n) | O(1) |
| Skewed | O(n) | O(1) |

### 11.6 Edge Cases
- `key` smaller than every element → Floor = `None`.
- `key` larger than every element → Ceil = `None`.
- `key` exactly equal to a node's value → both Floor and Ceil equal `key`.

### 11.7 Common Mistakes
- Swapping the "go left/go right" direction between floor and ceil (very common under pressure — always double check: floor wants **≤**, so it favors going right to find something bigger-but-still-valid; ceil wants **≥**, so it favors going left).
- Forgetting the exact-match short-circuit (still technically works without it, since `==` would just fall into one branch, but explicit handling is clearer).

### 11.8 Interview Tips
- Floor/Ceil questions often appear disguised as **"closest value to target"** (LeetCode 270) — recognize that "closest" = compare `floor` and `ceil` candidates and pick whichever has smaller absolute difference.

### 11.9 Practice Problems
- LeetCode 270 — Closest Binary Search Tree Value
- GeeksforGeeks — Floor and Ceil in BST

---

## 12. BST Validation

### 12.1 Problem Statement
Given a binary tree, determine whether it satisfies the BST property.

### 12.2 The #1 Trap — Local vs Global Validity

```
        5
      /   \
     3     8
    / \
   1   6      ← INVALID! 6 > 5, but 6 is checked only against
                its direct parent 3 (6 > 3 ✅ passes locally)
                A naive "compare to parent only" check WRONGLY
                says this tree is valid.
```

> **⚠️ Warning:** The single most common BST validation bug is checking each node **only against its immediate parent**. The BST property is **global**: every node in a left subtree must be less than **all its ancestors on the path**, not just its direct parent. You must pass down a valid `(min, max)` **range** that tightens as you descend.

### 12.3 Approach 1 — Min/Max Range (Recursive, Optimal)

```python
def is_valid_bst(root):
    def validate(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root, float('-inf'), float('inf'))
```

**Line-by-line:**
- `validate(node, low, high)` — `node.val` must lie strictly within `(low, high)`, a range that **narrows** as we descend.
- `if node is None: return True` — an empty subtree is trivially valid.
- `if not (low < node.val < high): return False` — the critical global check.
- Recurse left with an **updated upper bound** (`high = node.val`) — everything in the left subtree must be less than `node.val`.
- Recurse right with an **updated lower bound** (`low = node.val`) — everything in the right subtree must be greater than `node.val`.

### 12.4 Approach 2 — Inorder Traversal Must Be Strictly Increasing

```python
def is_valid_bst_inorder(root):
    prev = None
    def inorder(node):
        nonlocal prev
        if node is None:
            return True
        if not inorder(node.left):
            return False
        if prev is not None and node.val <= prev:
            return False
        prev = node.val
        return inorder(node.right)
    return inorder(root)
```

**Why this works:** A tree is a valid BST **if and only if** its inorder traversal is strictly increasing (this is the same property from [Section 7](#7-bst-traversals), used here as a **validation test** rather than just an observation).

### 12.5 Iterative Version (Stack-Based Inorder)

```python
def is_valid_bst_iterative(root):
    stack, prev = [], None
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if prev is not None and current.val <= prev:
            return False
        prev = current.val
        current = current.right
    return True
```

### 12.6 Complete Dry Run — Invalid Tree Detection

Tree (invalid, as shown in §12.2):
```
        5
      /   \
     3     8
    / \
   1   6
```

Using Range approach:

| Call | node | low | high | Check | Result |
|---|---|---|---|---|---|
| validate(5) | 5 | -inf | +inf | -inf<5<inf ✅ | recurse |
| validate(3) | 3 | -inf | 5 | -inf<3<5 ✅ | recurse |
| validate(1) | 1 | -inf | 3 | -inf<1<3 ✅ | recurse (leaf, True) |
| validate(6) | 6 | **3** | **5** | 3<6<5 → **False** (6 is not < 5) | ❌ **INVALID DETECTED** |

Notice: `6` is checked against `high = 5` (inherited from ancestor `5`, not just parent `3`) — this is exactly the global check that catches the bug a naive parent-only comparison would miss.

### 12.7 Complexity Analysis

| Approach | Time | Space |
|---|---|---|
| Min/Max Range | O(n) | O(h) recursive stack |
| Inorder (recursive) | O(n) | O(h) |
| Inorder (iterative) | O(n) | O(h) |
| Morris-based (O(1) space) | O(n) | **O(1)** |

### 12.8 Edge Cases
- Empty tree → valid (`True`) by convention.
- Single node → always valid.
- Duplicate values (`node.val == neighbor.val`) → typically **invalid** for a strict BST (`low < val < high`, strict inequality) — clarify with interviewer whether duplicates are allowed and adjust to `low <= val < high` or similar if so.
- Tree using `sys.maxsize`/`-sys.maxsize` instead of `float('inf')` — works too, but `float('inf')` is cleaner and avoids overflow-style edge cases entirely in Python (Python ints are arbitrary precision, so this is less of a concern than in C++/Java, but it's still a common thing interviewers probe about).

### 12.9 Common Mistakes
- **The classic bug**: comparing only to immediate parent instead of propagating a range (see §12.2).
- Using non-strict inequalities (`<=`) when duplicates should be invalid, or strict (`<`) when duplicates should be allowed — mismatch causes wrong answers on duplicate-containing test cases.
- Initializing bounds with finite sentinel values (e.g., `-999999`) instead of `float('-inf')`/`float('inf')` — breaks on trees containing values at or beyond that sentinel.

### 12.10 Interview Tips
- State the **naive wrong approach** (parent-only comparison) explicitly, then explain *why* it fails with an example — this proactive move demonstrates strong understanding and often earns extra credit.
- Offer both the range-based and inorder-based solutions — interviewers sometimes ask "can you do it another way?"

### 12.11 Practice Problems
- LeetCode 98 — Validate Binary Search Tree (Medium, extremely popular in FAANG interviews)
- GeeksforGeeks — Check if a given tree is BST


---

## 13. Recover Swapped BST

### 13.1 Problem Statement
Exactly **two nodes** of a BST have had their **values** mistakenly swapped. Recover the tree without changing its structure (i.e., swap the values back).

### 13.2 Intuition
Since a valid BST's inorder traversal is strictly increasing, a swap of two values creates one or two "inversions" (places where a value is followed by a smaller value) in the inorder sequence. Finding those inversions tells you exactly which two nodes were swapped.

### 13.3 Two Sub-Cases

```
CASE A: Swapped nodes are ADJACENT in inorder sequence
Correct inorder: 1, 2, 3, 4, 5
Swapped:         1, 2, 5, 4, 3  ← wait, let's use a cleaner example:
Swapped:         1, 4, 3, 2, 5   (swap values at positions holding "2" and "4")
                     ↑  ↑
                 one inversion: 4 > 3 (violates increasing order)
Only ONE inversion (first.val > next.val) is found.
The two swapped nodes are: first = node with value 4, second = node with value 3(the one right after).

CASE B: Swapped nodes are NOT adjacent
Correct inorder: 1, 2, 3, 4, 5
Swapped:         1, 4, 3, 2, 5   ← two inversions appear:
                    ↑1st inv: 4>3        ↑2nd inv: 3>2
first  = the node from the FIRST inversion's LARGER value (4)
second = the node from the SECOND inversion's SMALLER value (2)
```

### 13.4 Implementation (Inorder Traversal + Track Violations)

```python
def recover_tree(root):
    first = second = prev = None

    def inorder(node):
        nonlocal first, second, prev
        if node is None:
            return
        inorder(node.left)

        if prev is not None and prev.val > node.val:
            if first is None:
                first = prev              # first violation's larger element
            second = node                 # always update; final update = second violation's smaller element

        prev = node
        inorder(node.right)

    inorder(root)
    first.val, second.val = second.val, first.val   # swap VALUES, not nodes
```

**Line-by-line explanation:**
- Standard inorder traversal, but tracking `prev` (previous node visited) to detect `prev.val > node.val` — an **inversion**.
- `if first is None: first = prev` — only set `first` on the **first** inversion encountered (its larger element is one of the swapped values).
- `second = node` — updated on **every** inversion found (if there's a second inversion, this correctly ends up as that inversion's smaller element, matching Case B; if there's only one inversion, `second` simply ends up as that single inversion's smaller element, matching Case A).
- Finally, swap `first.val` and `second.val` — fixing the tree by exchanging **values only**, not restructuring pointers.

### 13.5 Complete Dry Run — Case B (Non-Adjacent Swap)

Correct BST inorder would be: `1, 2, 3, 4, 5`. Suppose nodes holding `2` and `4` were swapped, giving actual inorder: `1, 4, 3, 2, 5`.

| Step | node.val | prev.val | Inversion? | first | second |
|---|---|---|---|---|---|
| 1 | 1 | None | no | None | None |
| 2 | 4 | 1 | no (1<4) | None | None |
| 3 | 3 | 4 | **yes (4>3)** | first=4-node | second=3-node |
| 4 | 2 | 3 | **yes (3>2)** | (unchanged) | second=2-node |
| 5 | 5 | 2 | no (2<5) | (unchanged) | (unchanged) |

Final: `first` = node holding `4`, `second` = node holding `2`. Swap their values → tree restored to correct BST with inorder `1,2,3,4,5`. ✅

### 13.6 O(1) Space Version (Morris Inorder)

```python
def recover_tree_morris(root):
    first = second = prev = None
    current = root

    while current is not None:
        if current.left is None:
            if prev is not None and prev.val > current.val:
                if first is None:
                    first = prev
                second = current
            prev = current
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                if prev is not None and prev.val > current.val:
                    if first is None:
                        first = prev
                    second = current
                prev = current
                current = current.right

    first.val, second.val = second.val, first.val
```

This combines [Morris Traversal](#8-morris-traversal-o1-space) with the violation-tracking logic from §13.4, achieving the same result in **O(1) auxiliary space** instead of O(h).

### 13.7 Complexity Analysis

| Approach | Time | Space |
|---|---|---|
| Recursive inorder + tracking | O(n) | O(h) |
| Morris inorder + tracking | O(n) | **O(1)** |

### 13.8 Edge Cases
- Only two nodes total, swapped → single inversion, `first`/`second` are the only two nodes; works correctly.
- Swapped nodes are the **root and a deep descendant** → still detected correctly since the algorithm relies purely on inorder sequence order, not tree shape/depth.

### 13.9 Common Mistakes
- Swapping **node objects** (relinking `left`/`right` pointers) instead of swapping **values** — massively overcomplicated and error-prone; always swap values only.
- Forgetting to update `second` on **every** inversion (only updating it on the first one) — breaks Case B (non-adjacent swaps).
- Not resetting/removing Morris threads properly in the O(1) space version — corrupts the tree permanently.

### 13.10 Interview Tips
- Explicitly distinguish Case A (adjacent) vs Case B (non-adjacent) swaps in your explanation — this is the crux of the problem and shows you understand *why* the algorithm works, not just memorized code.

### 13.11 Practice Problems
- LeetCode 99 — Recover Binary Search Tree (Hard)
- GeeksforGeeks — Fix Two Swapped Nodes of a BST


---

## 14. Kth Smallest / Kth Largest

### 14.1 Problem Statement
Given a BST and integer `k`, find the `k`-th smallest (or largest) value.

### 14.2 Key Insight
Since inorder traversal visits nodes in sorted order, the **k-th element visited during inorder traversal is exactly the k-th smallest value**. For k-th largest, use **reverse inorder** (Right, Node, Left) — the k-th element visited is the k-th largest.

### 14.3 Visualization

```
        8
      /   \
     3     10
    / \       \
   1   6       14

Inorder: 1, 3, 6, 8, 10, 14
k=1 smallest → 1
k=3 smallest → 6
k=1 largest  → 14  (reverse inorder: 14,10,8,6,3,1 → 1st element)
k=3 largest  → 8   (reverse inorder 3rd element)
```

### 14.4 Approach 1 — Full Inorder Then Index (Simple, Not Optimal)

```python
def kth_smallest_naive(root, k):
    result = []
    def inorder(node):
        if node and len(result) < k:
            inorder(node.left)
            if len(result) < k:
                result.append(node.val)
                inorder(node.right)
    inorder(root)
    return result[-1]
```
This works but does unnecessary extra bookkeeping; better to **early-exit** as soon as we've counted `k` elements (Approach 2).

### 14.5 Approach 2 — Early-Exit Recursive Inorder (Optimal for One-Off Queries)

```python
def kth_smallest(root, k):
    count = 0
    result = None

    def inorder(node):
        nonlocal count, result
        if node is None or result is not None:
            return
        inorder(node.left)
        if result is not None:
            return
        count += 1
        if count == k:
            result = node.val
            return
        inorder(node.right)

    inorder(root)
    return result
```

### 14.6 Approach 3 — Iterative (Stack-Based, Stops Early Naturally)

```python
def kth_smallest_iterative(root, k):
    stack = []
    current = root
    count = 0
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.right
    return None                      # k larger than number of nodes
```

**Why the iterative version is often preferred:** it naturally **stops as soon as k is reached** (via `return`), without needing extra `if result is not None: return` guards scattered through recursive calls — cleaner early termination.

### 14.7 Kth Largest — Reverse Inorder

```python
def kth_largest(root, k):
    stack = []
    current = root
    count = 0
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.right    # go RIGHT first (reverse inorder)
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.left
    return None
```

### 14.8 Complete Dry Run — Kth Smallest, k=3

Tree: `8,3,10,1,6,14` (as above). Target: 3rd smallest.

| Step | Action | Stack | current | count | Return? |
|---|---|---|---|---|---|
| 1 | push 8, go left | [8] | 3 | 0 | |
| 2 | push 3, go left | [8,3] | 1 | 0 | |
| 3 | push 1, go left | [8,3,1] | None | 0 | |
| 4 | pop 1, count=1 | [8,3] | — | 1 | 1≠3 |
| 5 | go right (None), pop 3, count=2 | [8] | — | 2 | 2≠3 |
| 6 | go right → 6, push 6, go left (None) | [8,6] | None | 2 | |
| 7 | pop 6, count=3 | [8] | — | **3** | **return 6** ✅ |

### 14.9 Complexity Analysis

| Approach | Time | Space |
|---|---|---|
| Full inorder + index | O(n) always | O(n) |
| Early-exit recursive | O(h + k) | O(h) |
| Iterative stack, early exit | O(h + k) | O(h) |
| **Augmented BST (order-statistic tree)** | **O(log n)** per query | O(n) extra (size field per node) |

### 14.10 Optimization — Augmented "Order Statistic" BST

If **many** kth-smallest/rank queries are expected (not just one), augment each node with a `size` field (count of nodes in its subtree, including itself). Then kth-smallest can be found in **O(log n)** by comparing `k` against `left subtree size` at each step, without a full traversal:

```python
class AugmentedNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.size = 1                     # size of subtree rooted here

def kth_smallest_augmented(root, k):
    node = root
    while node is not None:
        left_size = node.left.size if node.left else 0
        if k == left_size + 1:
            return node.val
        elif k <= left_size:
            node = node.left
        else:
            k -= (left_size + 1)
            node = node.right
    return None                            # k out of range
```

> **📝 Note:** This is exactly the core idea behind an **Order Statistic Tree** — see [Section 22](#22-advanced-bst-concepts). It requires maintaining `size` correctly on every insert/delete (increment/decrement along the path), which adds bookkeeping but pays off hugely for repeated rank/kth queries.

### 14.11 Edge Cases
- `k` larger than the number of nodes → no valid answer; return `None` or raise an error depending on problem spec.
- `k = 1` → equivalent to `find_min` (smallest) or `find_max` (largest).
- `k = n` → equivalent to `find_max` (smallest) or `find_min` (largest).

### 14.12 Common Mistakes
- Off-by-one in the `count == k` check (starting count at 0 vs 1 inconsistently).
- Doing a **full** inorder traversal (visiting all n nodes) when an early-exit approach would save time for small `k` on a large tree.
- Forgetting reverse-inorder direction for kth **largest** (must go right-before-left, the mirror of standard inorder).

### 14.13 Interview Tips
- If interviewer says *"what if there are many `insert`/`delete` calls interleaved with many kth-smallest queries?"* — **immediately** bring up the augmented order-statistic tree (§14.10) — this is a strong signal of advanced knowledge.

### 14.14 Practice Problems
- LeetCode 230 — Kth Smallest Element in a BST (Medium)
- LeetCode 1038 / 538 — Binary Search Tree to Greater Sum Tree (uses reverse inorder) — see [Section 19](#19-convert-bst-to-greater-tree)
- GeeksforGeeks — Kth largest element in BST


---

## 15. BST Iterator

### 15.1 Problem Statement
Design an iterator over a BST that supports `next()` (returns the next smallest number in the BST, in sorted order) and `hasNext()`, both in **average O(1) time** and using **O(h) memory**.

### 15.2 Why This Is Tricky
A naive approach would run a full inorder traversal upfront and store all `n` values in a list, then just index through it — but that uses **O(n)** memory, not O(h) as typically required by the "controlled/lazy iterator" version of this problem. The optimal solution simulates the **call stack of an iterative inorder traversal**, materializing only O(h) nodes at a time.

### 15.3 Visualization — Stack State Over Time

```
        7
      /   \
     3     15
          /  \
         9    20

Initial stack (push all left children from root): [7, 3]
next() → pop 3 → push 3's right subtree's left spine (none) → return 3
         stack: [7]
next() → pop 7 → push 7's right subtree's left spine: push 15, then 9 → return 7
         stack: [15, 9]
next() → pop 9 → (9 has no children) → return 9
         stack: [15]
next() → pop 15 → push 15's right subtree's left spine: push 20 → return 15
         stack: [20]
next() → pop 20 → return 20
         stack: []
hasNext() → False
```

Output sequence: `3, 7, 9, 15, 20` — sorted order, exactly matching inorder traversal, produced **incrementally**.

### 15.4 Implementation

```python
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left_spine(root)

    def _push_left_spine(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right is not None:
            self._push_left_spine(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
```

**Line-by-line explanation:**
- `_push_left_spine(node)`: pushes `node` and every left-descendant onto the stack — this is the "dive all the way left" step from iterative inorder traversal ([Section 7](#7-bst-traversals)), extracted into a reusable helper.
- `__init__`: primes the stack with the left spine starting from `root` — the top of the stack is always the **next smallest unvisited value**.
- `next()`: pops the top (smallest remaining) node; if it has a right child, pushes that child's entire left spine (so the *next* smallest values are queued up); returns the popped value.
- `hasNext()`: simply checks whether the stack is non-empty.

### 15.5 Complexity Analysis

| Operation | Time | Space |
|---|---|---|
| `__init__` | O(h) — pushes left spine | O(h) |
| `next()` | **Amortized O(1)** (worst-case single call can be O(h), but total work across all `n` calls is O(n), so average is O(1)) | O(h) auxiliary |
| `hasNext()` | O(1) | O(1) |
| **Total for full traversal** | O(n) | **O(h)** |

> **📝 Note:** The "amortized O(1)" claim for `next()` is a classic **amortized analysis** result: across a full traversal of `n` nodes, every node is pushed exactly once and popped exactly once, so total work is O(n) over `n` calls → average O(1) per call, even though any single call could in theory do up to O(h) work (pushing a long left spine).

### 15.6 Edge Cases
- Empty tree (`root = None`) → `hasNext()` should immediately return `False`.
- Single node → one `next()` call returns it; `hasNext()` becomes `False` after.
- Fully right-skewed tree → `_push_left_spine` pushes only one node at a time (no left children exist), degrading each `next()` call's amortized behavior but total work across the whole traversal remains O(n).

### 15.7 Common Mistakes
- Materializing the entire inorder list upfront (`O(n)` space) — defeats the purpose of the problem, which specifically wants `O(h)`.
- Forgetting to push the **right child's entire left spine** (only pushing the right child itself) — breaks correctness for deeper subtrees.
- Not handling `root = None` gracefully in the constructor.

### 15.8 Interview Tips
- Explicitly state the O(h) space requirement and why the naive O(n) full-traversal approach doesn't meet it — shows you understood the actual constraint, not just "print sorted order."
- Mention the amortized O(1) argument for `next()` — commonly asked as a follow-up ("is `next()` really O(1)?").

### 15.9 Practice Problems
- LeetCode 173 — Binary Search Tree Iterator (Medium)
- LeetCode 285 — (uses similar underlying spine logic) — Inorder Successor in BST

---

## 16. Lowest Common Ancestor (LCA)

### 16.1 Problem Statement
Given a BST and two node values `p` and `q`, find their **lowest common ancestor** — the deepest node that has both `p` and `q` as descendants (a node can be its own descendant, per the standard LCA definition).

### 16.2 Key BST-Specific Insight
Unlike a plain binary tree (which needs O(n) traversal + path comparison, or the classic recursive "search both subtrees" trick), a **BST's ordering lets you find LCA in O(h) time** directly:

> If both `p` and `q` are **less than** the current node, the LCA must be in the **left** subtree. If both are **greater**, it must be in the **right** subtree. Otherwise (one is ≤ current ≤ other, or current equals one of them), **the current node IS the LCA**.

### 16.3 Visualization

```
        6
      /   \
     2     8
    / \   / \
   0   4 7   9
      / \
     3   5

LCA(2, 8): 2<6 and 8>6 → split → current node 6 IS the LCA.
LCA(2, 4): both < 6 → go left to 2. At 2: 2==2(p) → 2 IS the LCA (p is ancestor of q here).
LCA(3, 5): both <6→2; both >2→4; at 4: 3<4 and 5>4 → split → 4 IS the LCA.
```

### 16.4 Recursive Implementation

```python
def lowest_common_ancestor(root, p, q):
    if p < root.val and q < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if p > root.val and q > root.val:
        return lowest_common_ancestor(root.right, p, q)
    return root                     # split point (or root.val equals p or q) → answer
```

### 16.5 Iterative Implementation (Preferred — O(1) Space)

```python
def lowest_common_ancestor_iterative(root, p, q):
    current = root
    while current is not None:
        if p < current.val and q < current.val:
            current = current.left
        elif p > current.val and q > current.val:
            current = current.right
        else:
            return current
    return None
```

### 16.6 Complete Dry Run — LCA(3, 5)

Tree from §16.3.

| Step | current | p=3 vs current | q=5 vs current | Decision |
|---|---|---|---|---|
| 1 | 6 | 3<6 | 5<6 | both smaller → go left → 2 |
| 2 | 2 | 3>2 | 5>2 | both larger → go right → 4 |
| 3 | 4 | 3<4 | 5>4 | **split** → return `4` ✅ |

### 16.7 Complexity Analysis

| Case | Time | Space (Iterative) | Space (Recursive) |
|---|---|---|---|
| Balanced | O(log n) | O(1) | O(log n) |
| Skewed | O(n) | O(1) | O(n) |

### 16.8 Edge Cases
- `p` or `q` equals the root → root is immediately the LCA.
- `p` is an ancestor of `q` (or vice versa) → the algorithm still works correctly, since the loop stops as soon as it can't confidently say "both smaller" or "both larger."
- `p == q` → LCA is simply the node itself.

### 16.9 Common Mistakes
- Using the **generic binary tree LCA algorithm** (recursive search-both-subtrees, O(n)) when the BST property allows an O(h) solution — a common missed optimization that interviewers specifically probe for.
- Off-by-one logic errors: using `<=`/`>=` instead of strict `<`/`>` can cause incorrect early termination when `p` or `q` equals `current.val`.

### 16.10 Interview Tips
- Always mention explicitly: *"Because this is a BST (not a generic binary tree), I can use the ordering property to do this in O(h) instead of the generic O(n) two-subtree-search algorithm."* This is one of the most reliable "shows BST understanding" statements you can make.

### 16.11 Practice Problems
- LeetCode 235 — Lowest Common Ancestor of a Binary Search Tree (Easy)
- LeetCode 236 — LCA of a Binary Tree (contrast: generic version, O(n))


---

## 17. Range Search & Range Sum

### 17.1 Problem Statement
Given a BST and a range `[low, high]`, either (a) list all values within the range, or (b) compute the sum of all values within the range — **without visiting nodes outside the range whenever the BST property allows you to prune**.

### 17.2 Key Optimization — Pruning
Unlike a full O(n) traversal + filter, a BST lets you **skip entire subtrees** that are provably outside `[low, high]`:
- If `node.val < low`, the **entire left subtree** is also `< low` → skip it, only recurse right.
- If `node.val > high`, the **entire right subtree** is also `> high` → skip it, only recurse left.
- Otherwise, `node.val` is in range → include it, and recurse **both** sides (either side might still contain valid values).

### 17.3 Visualization

```
        10
       /   \
      5     15
     / \    /  \
    3   7  12  18

Range [6, 13]:
- 10: in range → include, recurse both
   - 5: 5<6 → PRUNE left subtree (3), only recurse right (7)
       - 7: in range → include
   - 15: 15>13 → PRUNE right subtree (18), only recurse left (12)
       - 12: in range → include

Result: [7, 10, 12]   (nodes 3, 5, 15, 18 were never fully explored where pruned)
```

### 17.4 Implementation — Range Sum

```python
def range_sum_bst(root, low, high):
    if root is None:
        return 0
    if root.val < low:
        return range_sum_bst(root.right, low, high)          # prune left entirely
    if root.val > high:
        return range_sum_bst(root.left, low, high)            # prune right entirely
    return (root.val +
            range_sum_bst(root.left, low, high) +
            range_sum_bst(root.right, low, high))
```

### 17.5 Implementation — Range Search (Collect Values)

```python
def range_search(root, low, high, result=None):
    if result is None:
        result = []
    if root is None:
        return result
    if root.val > low:
        range_search(root.left, low, high, result)
    if low <= root.val <= high:
        result.append(root.val)
    if root.val < high:
        range_search(root.right, low, high, result)
    return result
```

**Note:** this version keeps the recursion structured as inorder (so the result comes out **sorted**), while still pruning: it only recurses left if `root.val > low` (otherwise everything in the left subtree would be `< low` anyway) and only recurses right if `root.val < high`.

### 17.6 Iterative Implementation (Stack-Based, With Pruning)

```python
def range_sum_bst_iterative(root, low, high):
    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if low <= node.val <= high:
            total += node.val
        if node.val > low:               # left subtree might still be relevant
            stack.append(node.left)
        if node.val < high:              # right subtree might still be relevant
            stack.append(node.right)
    return total
```

### 17.7 Complete Dry Run — Range Sum [6, 13]

Tree from §17.3.

| Step | node | In range? | Prune decision | Running sum |
|---|---|---|---|---|
| 1 | 10 | yes | recurse both | 10 |
| 2 | 5 | no (5<6) | prune left (3), recurse right only | 10 |
| 3 | 7 | yes | (leaf) | 17 |
| 4 | 15 | no (15>13) | prune right (18), recurse left only | 17 |
| 5 | 12 | yes | (leaf) | **29** |

Final range sum = `10 + 7 + 12 = 29`. ✅ (matches result list `[7,10,12]` from §17.3)

### 17.8 Complexity Analysis

| Metric | Value |
|---|---|
| Time (worst case, e.g., full tree in range) | O(n) |
| Time (best case, narrow range, balanced tree) | O(log n + m) where `m` = number of nodes actually in range |
| Space | O(h) recursion stack |

> **📝 Note:** The pruning optimization doesn't change the **worst-case** complexity (if the entire tree happens to be within range, you must visit every node) — but it dramatically improves the **typical/average case** versus a naive full traversal + filter, especially for narrow ranges on large trees.

### 17.9 Edge Cases
- `low > high` → no valid range; should return 0 / empty list immediately (validate input if this is a possibility).
- Range fully outside the tree's min/max → correctly prunes everything, returns 0 / empty list.
- `low == high` → equivalent to searching for a single exact value.

### 17.10 Common Mistakes
- Forgetting to prune (just doing full traversal + `if low <= val <= high` filter) — technically correct but misses the key BST-specific optimization interviewers look for.
- Off-by-one on inclusive/exclusive range boundaries (`low <= val <= high` vs `low < val < high`) — clarify with the problem statement.

### 17.11 Interview Tips
- Explicitly call out the pruning optimization and explain *why* it's valid (BST property guarantees the entire skipped subtree is out of range) — don't just present the code silently.

### 17.12 Practice Problems
- LeetCode 938 — Range Sum of BST (Easy)
- GeeksforGeeks — Print BST elements in a given range

---

## 18. Trim a BST

### 18.1 Problem Statement
Given a BST and a range `[low, high]`, **trim** the tree so it contains only nodes with values in that range, preserving the BST structure, and return the new root.

### 18.2 Key Insight
If a node's value is **out of range on one side**, that entire side (including the node itself) can be discarded — but you must **recurse into the surviving subtree first**, because a descendant on the "wrong" side numerically might still fall back into range (e.g., a node with value `4` when `low=5` might have a right child with value `6`, which is in range).

### 18.3 Visualization

```
Trim to [1, 3]:
        3                    3
      /   \                 /
     0     4      ──►      1
      \                       (0 is <1, dropped; but 0's right
       1                       child 1 is IN range → reattached
                                as new left child chain-collapsed
                                up through the trim recursion)
```

### 18.4 Implementation

```python
def trim_bst(root, low, high):
    if root is None:
        return None
    if root.val < low:
        return trim_bst(root.right, low, high)     # discard root & its ENTIRE left subtree,
                                                      # but root's right subtree might still be valid
    if root.val > high:
        return trim_bst(root.left, low, high)       # mirror case
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)
    return root
```

**Line-by-line:**
- `if root.val < low:` — `root` itself is out of range, and (by BST property) its **entire left subtree** is even smaller, so also out of range — discard both, but `root.right` might contain values `≥ low`, so recurse there and **return that result directly** (splicing it up to replace `root`).
- `if root.val > high:` — mirror case, discard root and its entire right subtree, recurse left.
- Otherwise, `root.val` is within range — keep it, but still need to trim **both** children (they might individually have out-of-range descendants), then return `root`.

### 18.5 Complete Dry Run

Tree:
```
        3
      /   \
     0     4
      \
       1
        \
         2
```
Trim to `[1, 3]`:

| Call | node | Decision |
|---|---|---|
| trim(3) | 3 | in range [1,3] → trim both children, return 3 |
| trim(0) | 0 | 0<1 → discard 0 and its left (none); recurse right → trim(1) |
| trim(1) | 1 | in range → trim both children (none left, recurse right) |
| trim(2) | 2 | in range → return 2 |
| — | — | 1.right = 2; return 1 (this becomes 3.left) |
| trim(4) | 4 | 4>3 → discard 4 and its right (none); recurse left (none) → return None |
| — | — | 3.right = None |

Final tree:
```
      3
     /
    1
     \
      2
```

### 18.6 Complexity Analysis

| Metric | Value |
|---|---|
| Time | O(n) worst case (must visit every node once) |
| Space | O(h) recursion stack |

### 18.7 Edge Cases
- Entire tree out of range → returns `None`.
- Entire tree already within range → returns the tree unchanged (every node passes the "in range" branch).
- `low == high` → only nodes with exactly that value survive (if the tree even contains it).

### 18.8 Common Mistakes
- Discarding a node's **entire** subtree (both sides) when only the "wrong direction" side is guaranteed invalid — must still recurse into the potentially-valid side.
- Forgetting to reassign `root.left`/`root.right` from the recursive calls (silently losing the trimmed structure) — same class of bug as in insert/delete.

### 18.9 Interview Tips
- Emphasize the subtlety that a node can be discarded while **part of its subtree survives** — this is the crux of the problem and worth stating explicitly.

### 18.10 Practice Problems
- LeetCode 669 — Trim a Binary Search Tree (Medium)


---

## 19. Convert BST to Greater Tree

### 19.1 Problem Statement
Transform a BST such that every node's value becomes the **original value plus the sum of all values greater than it** in the original tree (a "Greater Sum Tree").

### 19.2 Key Insight — Reverse Inorder
Since reverse inorder (Right, Node, Left) visits nodes in **descending** order, tracking a running sum as you go lets each node accumulate the sum of everything larger than it, visited so far.

### 19.3 Visualization

```
Original BST:            Greater Sum Tree:
     4                        30    (4 + 5+13+8 = wait let's use exact tree)
   /   \
  1     6
       / \
      5   8

Reverse inorder visit order: 8, 6, 5, 4, 1
running_sum starts at 0.

visit 8: running_sum = 0+8 = 8   → node.val becomes 8
visit 6: running_sum = 8+6 = 14  → node.val becomes 14
visit 5: running_sum = 14+5 = 19 → node.val becomes 19
visit 4: running_sum = 19+4 = 23 → node.val becomes 23
visit 1: running_sum = 23+1 = 24 → node.val becomes 24

Result tree:
    23
   /   \
  24    14
       /  \
      19   8
```

### 19.4 Implementation (Recursive)

```python
def convert_bst_to_greater_tree(root):
    running_sum = 0

    def reverse_inorder(node):
        nonlocal running_sum
        if node is None:
            return
        reverse_inorder(node.right)      # visit larger values first
        running_sum += node.val
        node.val = running_sum
        reverse_inorder(node.left)       # then smaller values

    reverse_inorder(root)
    return root
```

### 19.5 Iterative Implementation

```python
def convert_bst_to_greater_tree_iterative(root):
    running_sum = 0
    stack = []
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.right       # dive right first (reverse inorder)
        current = stack.pop()
        running_sum += current.val
        current.val = running_sum
        current = current.left
    return root
```

### 19.6 Complexity Analysis

| Metric | Value |
|---|---|
| Time | O(n) |
| Space | O(h) (recursive stack / explicit stack) |

### 19.7 Edge Cases
- Single node → its new value equals its old value (nothing greater exists).
- All values identical (if duplicates allowed) → running sum still accumulates correctly per visit, though semantics of "greater than" become ambiguous — clarify duplicate handling with interviewer.

### 19.8 Common Mistakes
- Using **normal** inorder (ascending) instead of **reverse** inorder (descending) — produces a "smaller sum tree" instead of the intended "greater sum tree."
- Forgetting `nonlocal running_sum` in the recursive closure version — causes an `UnboundLocalError` in Python.

### 19.9 Interview Tips
- Explicitly state: *"I'll use reverse inorder because it visits nodes in descending order, which lets me maintain a running sum of everything larger seen so far."*

### 19.10 Practice Problems
- LeetCode 1038 / 538 — Binary Search Tree to Greater Sum Tree (Medium)

---

## 20. Construct BST (Sorted Array / Preorder)

### 20.1 Sub-Problem A: Sorted Array → Height-Balanced BST

**Problem:** Given a sorted array, build a BST with **minimum possible height** (balanced).

**Key Insight:** Always pick the **middle element** as the root — this guarantees the left and right halves are as equal in size as possible, recursively producing a balanced tree.

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

> **⚠️ Warning:** Slicing (`nums[:mid]`, `nums[mid+1:]`) creates **new list copies** each call, leading to O(n log n) **extra space/time** overhead just from copying. For large inputs, prefer passing `(nums, left, right)` index bounds instead of slicing:

```python
def sorted_array_to_bst_optimized(nums):
    def build(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root
    return build(0, len(nums) - 1)
```

**Visualization:**
```
nums = [1, 2, 3, 4, 5, 6, 7]
mid index = 3 → value 4 → root

           4
         /   \
        2     6
       / \   / \
      1   3 5   7

Height = 2 = ⌈log2(7+1)⌉ - 1 → minimum possible height achieved.
```

**Complexity:** Time O(n) (each element processed once), Space O(log n) recursion stack (balanced) + O(n) for output tree.

### 20.2 Sub-Problem B: Sorted (Singly) Linked List → Balanced BST

Same idea as §20.1, but without O(1) random access to the middle element. Two common strategies:
1. Convert linked list to an array first (O(n) extra space), then apply §20.1 — simplest.
2. **Fast/slow pointer** technique to find the middle node in O(n) time without extra array, recursively splitting the list — more advanced, avoids the O(n) array but recursion still costs O(n log n) total due to repeated middle-finding.

```python
def sorted_list_to_bst(head):
    # Strategy 1: convert to array (simplest, most commonly accepted in interviews)
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next
    return sorted_array_to_bst_optimized(values)
```

### 20.3 Sub-Problem C: Construct BST from Preorder Traversal

**Problem:** Given a preorder traversal of a BST (unique values), reconstruct the original tree.

**Key Insight:** The **first element is always the root**. Using the BST property, you can determine where the left subtree's preorder values end (the first value greater than root marks the start of the right subtree) — or, more efficiently, pass down a valid `(low, high)` bound (mirroring [Section 12](#12-bst-validation)'s validation technique) and greedily consume elements that fit.

```python
def bst_from_preorder(preorder):
    index = 0
    def build(bound):
        nonlocal index
        if index == len(preorder) or preorder[index] > bound:
            return None
        root = TreeNode(preorder[index])
        index += 1
        root.left = build(root.val)          # left subtree: everything < root.val
        root.right = build(bound)             # right subtree: everything < original bound
        return root
    return build(float('inf'))
```

**Line-by-line:**
- `build(bound)`: constructs a subtree using only preorder values that are `≤ bound` (the value inherited from an ancestor that constrains this subtree — mirrors the range-based BST validation approach).
- Each call consumes exactly one element from `preorder` (via the `nonlocal index` pointer) if it fits the bound; the **order of consumption naturally matches preorder (root, then left subtree, then right subtree)**.
- `root.left = build(root.val)` — left subtree must be entirely less than `root.val` (the new bound).
- `root.right = build(bound)` — right subtree keeps the **original inherited bound** (everything in the right subtree is still less than whatever constrained the current call, just greater than `root.val`, which is guaranteed implicitly since we already consumed all valid left-subtree elements first).

**Visualization:**
```
preorder = [8, 5, 1, 7, 10, 12]

build(inf): index0=8 fits(≤inf) → root=8, index=1
  build(8) [left, bound=8]:
     index1=5 fits(≤8) → root=5, index=2
       build(5): index2=1 fits(≤5) → root=1, index=3
         build(1): index3=7, 7>1 → None
         build(5): index3=7, 7≤5? NO(7>5) → None
       → 5.left=1
       build(8) [right of 5, bound=8]: index3=7 fits(≤8) → root=7,index=4
         build(7): index4=10,10>7→None
         build(8): index4=10,10≤8? NO→None
       → 5.right=7
  → 8.left = 5 (with children 1, 7)
  build(inf) [right of 8, bound=inf]: index4=10 fits → root=10, index=5
     build(10): index5=12,12>10→None
     build(inf): index5=12 fits→root=12,index=6 (end of array)
  → 8.right=10 (with right child 12)

Final tree:
        8
      /   \
     5     10
    / \       \
   1   7       12
```

**Complexity:** Time **O(n)** (each element consumed exactly once — a subtlety many candidates miss, assuming it's O(n log n) or O(n²) due to the nested recursion; it is not, because the `index` pointer never backtracks). Space O(h) recursion stack.

### 20.4 Common Mistakes (Construction)
- Using array slicing repeatedly (§20.1) without realizing the hidden O(n log n) copy overhead.
- In preorder-construction, using a naive "find split point by scanning for first value > root" approach, which degrades to **O(n²)** in the worst case (skewed tree) — the bound-passing technique in §20.3 avoids this and is the optimal O(n) solution.

### 20.5 Practice Problems
- LeetCode 108 — Convert Sorted Array to Binary Search Tree (Easy)
- LeetCode 109 — Convert Sorted List to Binary Search Tree (Medium)
- LeetCode 1008 — Construct Binary Search Tree from Preorder Traversal (Medium)


---

## 21. Serialize & Deserialize BST

### 21.1 Problem Statement
Convert a BST into a string (serialize) such that it can later be reconstructed (deserialize) into the exact same tree structure.

### 21.2 Key BST-Specific Optimization
For a **generic binary tree**, you typically need to serialize with explicit `None` markers (e.g., preorder with nulls) since structure can't otherwise be inferred. For a **BST specifically**, you can serialize with **just preorder values (no null markers needed)**, because the BST property lets you reconstruct structure uniquely from value order alone — exactly the technique from [Section 20.3](#20-construct-bst-sorted-array--preorder).

### 21.3 Implementation

```python
class Codec:
    def serialize(self, root):
        values = []
        def preorder(node):
            if node:
                values.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ','.join(values)

    def deserialize(self, data):
        if not data:
            return None
        preorder = list(map(int, data.split(',')))
        index = 0

        def build(bound):
            nonlocal index
            if index == len(preorder) or preorder[index] > bound:
                return None
            root = TreeNode(preorder[index])
            index += 1
            root.left = build(root.val)
            root.right = build(bound)
            return root

        return build(float('inf'))
```

**Why no null markers are needed:** unlike a generic tree, a BST's preorder sequence, combined with value comparisons, **uniquely determines structure** — this is exactly the bound-passing reconstruction from §20.3, reused here directly.

### 21.4 Visualization

```
Tree:
        8
      /   \
     5     10
    / \       \
   1   7       12

serialize() → "8,5,1,7,10,12"    (just preorder values, NO nulls needed!)

deserialize("8,5,1,7,10,12") → rebuilds the exact same tree using
                                 the bound-passing technique (§20.3)
```

### 21.5 Complexity Analysis

| Operation | Time | Space |
|---|---|---|
| Serialize | O(n) | O(n) output string + O(h) recursion |
| Deserialize | O(n) | O(n) output tree + O(h) recursion |

### 21.6 Comparison — Generic Binary Tree vs BST Serialization

| Aspect | Generic Binary Tree | BST |
|---|---|---|
| Needs null markers? | Yes | **No** — structure inferred from value order |
| Serialized size | Larger (nulls included) | Smaller (values only) |
| Reconstruction technique | Direct preorder-with-nulls parse | Bound-passing reconstruction |

### 21.7 Edge Cases
- Empty tree → serialize to empty string `""`; deserialize `""` → `None`.
- Single node → serializes to just that one value.
- All values on one side (skewed) → still works correctly, just produces O(n) recursion depth on both serialize and deserialize.

### 21.8 Common Mistakes
- Including null markers unnecessarily (wastes space; not wrong, just suboptimal for a BST specifically — though it does still work and is a valid fallback if you're unsure about the bound-passing technique under interview pressure).
- Forgetting to handle the empty-string edge case in `deserialize`.

### 21.9 Interview Tips
- Proactively mention: *"Since this is a BST, not a generic binary tree, I don't need to serialize null markers — the BST property lets me reconstruct structure purely from preorder value order."* This is a strong signal of specific BST expertise versus generic tree knowledge.

### 21.10 Practice Problems
- LeetCode 449 — Serialize and Deserialize BST (Medium)
- LeetCode 297 — Serialize and Deserialize Binary Tree (contrast: generic version, needs null markers)


---

## 22. Advanced BST Concepts

### 22.1 Why Plain BSTs Aren't Enough
As shown repeatedly, a plain BST offers **no height guarantee** — adversarial or sorted-order insertions degrade it to O(n) per operation ([Section 2.1](#2-bst-fundamentals--terminology)). **Self-balancing BSTs** solve this by enforcing a balance invariant after every insert/delete, guaranteeing O(log n) height always.

### 22.2 AVL Trees (Overview)

- **Invariant:** for every node, `|height(left) - height(right)| ≤ 1`.
- Maintained via **rotations** (single left/right, or double left-right/right-left) after insert/delete, whenever the balance factor is violated.
- Guarantees **strict** O(log n) height, making it slightly more rigidly balanced than Red-Black Trees.
- **Trade-off:** more rotations on average during insert/delete compared to Red-Black Trees, making AVL better for **read-heavy** workloads (search-dominant), Red-Black better for **write-heavy** workloads.

```
Unbalanced (before rotation):        After single right rotation:
        3                                    2
       /                                    / \
      2                        ──►         1   3
     /
    1
  (left-left case, balance factor = 2)   (balanced again)
```

### 22.3 Red-Black Trees (Overview)

- Each node is colored **red** or **black**, with invariants:
  1. Root is always black.
  2. No two consecutive red nodes (red node's children must be black).
  3. Every root-to-`None`-leaf path has the same number of black nodes ("black-height").
- These invariants guarantee height is **at most `2*log(n+1)`** — a looser bound than AVL's, but achieved with **fewer rotations** on average.
- Used internally by: C++ `std::map`/`std::set`, Java `TreeMap`/`TreeSet`, Linux kernel scheduler (`CFS`).

### 22.4 AVL vs Red-Black — Comparison Table

| Aspect | AVL Tree | Red-Black Tree |
|---|---|---|
| Balance strictness | Stricter (`\|bf\| ≤ 1`) | Looser |
| Height bound | ~1.44 log n | ~2 log n |
| Rotations per insert/delete | More | Fewer |
| Best for | Search-heavy workloads | Insert/delete-heavy workloads |
| Real-world usage | Databases needing fast lookups | `std::map`, Java `TreeMap`, Linux CFS scheduler |

### 22.5 Tree Rotations (Overview)

Rotations are **local, O(1)** restructuring operations used to restore balance without violating the BST property.

```
Right Rotation around y:              Left Rotation around x:
      y                x                    x                  y
     / \              / \                  / \                / \
    x   C    ──►      A   y                A   y     ──►      x   C
   / \                   / \                  / \            / \
  A   B                 B   C                B   C          A   B

(Both preserve inorder sequence: A, x, B, y, C — BST property intact)
```

```python
def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x                 # x is the new subtree root

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y                 # y is the new subtree root
```

> **📝 Note:** Rotations are O(1) — only a constant number of pointers change — which is exactly why self-balancing trees can maintain O(log n) height with only O(log n) total rotation work per insert/delete (at most O(log n) rotations needed to travel back up and fix violations, each one O(1)).

### 22.6 Order-Statistic Tree (Augmented BST) — Overview

Covered practically in [Section 14.10](#14-kth-smallest--kth-largest). Core idea: augment each node with a `size` (subtree node count) field, enabling:
- `select(k)` — find kth smallest in O(log n) (on a balanced augmented tree).
- `rank(val)` — find how many elements are smaller than `val`, in O(log n).

This is the foundation of **Fenwick Trees / Segment Trees for order statistics**, and Python's `sortedcontainers.SortedList` uses a related (though not tree-based) internal structure to achieve similar guarantees.

### 22.7 Threaded BST (Overview)

A **threaded binary tree** replaces `None` child pointers with **threads** pointing to the inorder predecessor/successor, enabling traversal **without recursion or a stack** — conceptually the "permanent" version of what [Morris Traversal](#8-morris-traversal-o1-space) does **temporarily**.

```
Normal BST:                     Threaded BST (dotted = thread, not a real child):
     2                                2
    / \                              / \
   1   3                            1   3
  (1.right=None,                  (1.right ┄┄► 2 [thread to successor]
   3.left=None)                    3.left  ┄┄► 2 [thread to predecessor])
```

- **Advantage:** O(1) space traversal permanently, no temporary tree mutation (unlike Morris).
- **Disadvantage:** every node needs an extra boolean flag (or sentinel convention) to distinguish "real child" from "thread," adding implementation complexity and per-node memory overhead.

### 22.8 Persistent BST (Overview)

A **persistent** (or "immutable"/"functional") BST preserves **every previous version** of the tree after each modification, by creating new nodes only along the path that changed (path copying) and sharing all unchanged subtrees with the previous version.

```
Original tree:              After inserting into left subtree
                             (persistent — old version still intact):
      5                             5'                5   (both roots exist!)
     / \                           /  \               / \
    3   8         insert(4)      3'    8 (shared)    3   8 (shared with new version)
                                 / \
                                3   4  (new nodes, only along the changed path)
```

- Only **O(log n)** new nodes created per modification (the path from root to the change), everything else is shared by reference — hugely space-efficient versus copying the whole tree.
- Used in: functional programming language standard libraries (Clojure, Scala immutable maps/sets), version-controlled databases, "undo" systems.

### 22.9 Advanced Concepts — Quick Comparison Table

| Structure | Guarantees Balance? | Extra Space/Node | Primary Use Case |
|---|---|---|---|
| Plain BST | No | None | Simple ordered storage, teaching |
| AVL Tree | Yes (strict) | Balance factor / height | Search-heavy systems |
| Red-Black Tree | Yes (looser) | 1 color bit | General-purpose ordered maps/sets |
| Order-Statistic BST | Depends on base tree | `size` field | Rank/kth-element queries |
| Threaded BST | No (orthogonal concern) | Thread flag(s) | O(1) space traversal, no recursion/stack |
| Persistent BST | Depends on base tree | O(log n) new nodes per update | Version history, undo, functional programming |

> **💡 Interview Tip:** You are **rarely** asked to implement AVL/Red-Black rotations from scratch in a standard interview — but you are **very often** asked *"what happens if the BST becomes unbalanced?"* and *"how would you fix that?"* — knowing the names, invariants, and trade-offs above (without necessarily coding full rotation logic) is usually sufficient and expected.


---

## 23. Real-World Applications

| Application | How BST Concepts Are Used |
|---|---|
| **Database Indexing** | B-Trees/B+ Trees (multi-way generalizations of BSTs) power indexes in MySQL, PostgreSQL, etc., enabling O(log n) range queries and lookups on disk-backed data. |
| **Symbol Tables (Compilers)** | Variable/function name lookups during compilation often use balanced BSTs or hash-augmented BSTs for scoped symbol resolution. |
| **Ordered Dictionaries/Sets** | C++ `std::map`/`std::set` (Red-Black Tree-backed), Java `TreeMap`/`TreeSet` — provide sorted iteration, floor/ceiling, range queries — all BST-derived operations covered in this handbook. |
| **Search Engines** | Certain indexing/ranking structures use balanced trees for maintaining sorted term frequencies or document scores that need frequent insert/delete with order preserved. |
| **Autocomplete (Comparison)** | Tries are generally preferred for prefix-based autocomplete (O(length of prefix) lookups), but BSTs can support "closest match" / lexicographic range queries via floor/ceil-style logic when a full trie isn't justified. |
| **Range Queries** | Financial systems, analytics dashboards, and scheduling systems use BST-like structures (or augmented BSTs / interval trees, a BST variant) to efficiently answer "how many/which records fall between X and Y." |
| **Scheduling** | The Linux kernel's Completely Fair Scheduler (CFS) uses a **Red-Black Tree** keyed by virtual runtime to always pick the "leftmost" (least-run) process in O(log n). |
| **Version Control / Undo Systems** | Persistent BSTs ([Section 22.8](#22-advanced-bst-concepts)) underlie some functional data structures used for maintaining history/undo stacks efficiently. |

> **📝 Note:** In practice, **raw unbalanced BSTs are rarely used directly in production systems** — almost everything above actually uses a **self-balancing variant** (Red-Black Tree, B-Tree, AVL) under the hood. Understanding plain BSTs is the essential **conceptual foundation** that makes all of these advanced structures learnable.

---

## 24. Problem Recognition Playbook

### 24.1 Master Decision Flowchart

```
                    ┌─────────────────────────────┐
                    │  Does the problem involve a  │
                    │  tree where each node has    │
                    │  an ORDER relationship        │
                    │  (values comparable, sorted)? │
                    └───────────────┬───────────────┘
                                    │ yes
                                    ▼
          ┌─────────────────────────────────────────────┐
          │ Keywords: "sorted," "kth smallest/largest,"  │
          │ "closest value," "range between X and Y,"    │
          │ "floor/ceil," "successor/predecessor,"       │
          │ "valid BST," "balanced/skewed"                │
          └───────────────────┬───────────────────────────┘
                               │ yes → THINK BST
                               ▼
        ┌──────────────────────────────────────────────────┐
        │ Which specific BST pattern does the problem need? │
        └──────────────────────────────────────────────────┘
                │little           │                │
                ▼                ▼                ▼
        "find/insert/delete   "kth smallest/     "range between
         a value"              largest,          two values"
                │               closest value"       │
                ▼                ▼                    ▼
        Search/Insert/     Inorder + early    Range Search /
        Delete patterns    exit, or           Range Sum (prune
        (Sections 4-6)     augmented tree     using BST property)
                            (Section 14)       (Section 17)

                │                │                │
                ▼                ▼                ▼
        "is this a valid   "two nodes swapped, "convert structure
         BST?"              fix the tree"       (array→BST, BST→
                │                │               greater tree, etc.)"
                ▼                ▼                ▼
        Min/Max range      Recover Swapped     Construction /
        validation          BST (Section 13)   Conversion patterns
        (Section 12)                            (Sections 18-21)
```

### 24.2 Keyword-to-Pattern Lookup Table

| Keyword / Phrase in Problem | Likely Pattern | Section |
|---|---|---|
| "search for a value" | Search | §4 |
| "insert a value" | Insert | §5 |
| "delete a node" | Delete (3 cases) | §6 |
| "print in sorted order" | Inorder Traversal | §7 |
| "O(1) space traversal" | Morris Traversal | §8 |
| "next greater / next smaller element" | Successor / Predecessor | §10 |
| "largest value ≤ k" / "smallest value ≥ k" | Floor / Ceil | §11 |
| "is this a valid BST" | Validation (min/max range) | §12 |
| "two nodes swapped" | Recover Swapped BST | §13 |
| "kth smallest/largest" | Kth Smallest/Largest | §14 |
| "design an iterator, O(h) space" | BST Iterator | §15 |
| "lowest common ancestor" | LCA (BST-optimized) | §16 |
| "sum/list of values in [L,R]" | Range Search/Sum | §17 |
| "keep only values in [L,R]" | Trim BST | §18 |
| "add sum of greater values" | Convert to Greater Tree | §19 |
| "build BST from sorted array/list" | Construction | §20 |
| "build BST from preorder" | Construction from Preorder | §20.3 |
| "serialize / deserialize a BST" | Serialize/Deserialize | §21 |
| "closest value to target" | Floor + Ceil, pick nearer | §11 |

### 24.3 Recursive vs Iterative — Decision Guide

```
Does the interviewer explicitly ask for O(1) auxiliary space,
or mention concern about recursion depth / stack overflow
on large/skewed trees?
        │
        ├── YES → Use ITERATIVE approach
        │          (search, insert, delete, traversal all have
        │           iterative forms shown in this handbook)
        │
        └── NO  → RECURSIVE is usually acceptable and often
                   cleaner/faster to write correctly under
                   interview time pressure — but ALWAYS mention
                   the recursion-depth trade-off proactively.
```


---

## 25. Optimization Playbook

### 25.1 Brute Force → BST
- **Before:** Linear scan of an unsorted list for search/range/kth-queries — O(n) per query.
- **After:** Store data in a BST — O(log n) average for search/insert/delete/kth-queries (balanced case).
- **When it's worth it:** Many repeated queries on data that also needs frequent insert/delete (if data is static and query-only, a sorted array + binary search is simpler and cache-friendlier).

### 25.2 Recursive → Iterative
- **Motivation:** avoid `RecursionError` on deep/skewed trees; achieve true O(1) auxiliary space for search/insert/delete/LCA (see Sections 4-6, 16).
- **Technique:** replace the implicit call stack with an explicit `while` loop tracking `current` (and `parent`, if needed for deletion/rewiring).
- **Trade-off:** slightly more verbose code; some operations (like the two-children delete case) still need auxiliary logic (finding successor) that isn't fully "free" iteratively, but avoids recursion depth entirely.

### 25.3 Stack-Based Traversal → Morris Traversal
- **Motivation:** eliminate O(h) auxiliary space entirely, achieving true O(1) space traversal.
- **Trade-off:** temporarily mutates the tree (thread creation/removal); not safe under concurrent reads; more complex to implement correctly.
- **When to use:** explicitly asked for O(1) space traversal, or memory-constrained environments processing very large/deep trees.

### 25.4 Plain BST → Augmented BST (Order Statistics)
- **Motivation:** repeated kth-smallest/rank queries interleaved with insert/delete — a plain BST needs O(h + k) per kth-query; an augmented BST with `size` fields achieves O(log n) (on a balanced base tree) per query.
- **Trade-off:** extra `size` field per node, and every insert/delete must correctly increment/decrement `size` along the affected path.

### 25.5 Plain BST → Self-Balancing BST (AVL / Red-Black)
- **Motivation:** guarantee O(log n) height regardless of insertion order (protect against adversarial/sorted input degenerating to O(n)).
- **Trade-off:** implementation complexity (rotations, color/balance-factor bookkeeping); slightly more work per insert/delete (though still O(log n) total, just with a larger constant factor).
- **When to bring this up:** whenever an interviewer asks "what if the input is already sorted?" or "what's the worst case?" — this is your cue to mention self-balancing trees as the production-grade solution.

### 25.6 Full Traversal + Filter → Pruned Range Query
- **Motivation:** for narrow ranges on large trees, avoid visiting every node (Section 17's pruning technique).
- **Trade-off:** none significant — this optimization is essentially "free" once you recognize the BST property allows it; always apply it for range-based problems.

### 25.7 Optimization Summary Table

| From | To | Gain | Cost |
|---|---|---|---|
| Linear scan | BST search | O(n) → O(log n) avg | Requires maintaining sorted structure |
| Recursive | Iterative | Avoids stack overflow, O(1) space | Slightly more code |
| Stack traversal | Morris traversal | O(h) → O(1) space | Temporary mutation, complexity |
| Plain BST | Augmented (order-stat) | O(h+k) → O(log n) per kth query | Extra `size` bookkeeping |
| Plain BST | Self-balancing (AVL/RB) | Worst-case O(n) → guaranteed O(log n) | Rotation complexity |
| Full traversal + filter | Pruned range query | Fewer nodes visited (avg case) | None significant |

---

## 26. Python-Specific Tips

### 26.1 Recursion Limit
Python's default recursion limit is **~1000** (`sys.getrecursionlimit()`). A skewed BST with more than ~1000 nodes will raise `RecursionError` on recursive search/insert/delete/traversal.

```python
import sys
print(sys.getrecursionlimit())      # typically 1000
sys.setrecursionlimit(10000)        # can raise it, but risks a genuine C-stack overflow/crash
                                     # for very deep recursion — prefer iterative solutions
                                     # for production code handling potentially skewed trees.
```

### 26.2 `collections.deque` for Level-Order Traversal
Always use `deque` (O(1) `popleft()`) instead of a plain `list` (O(n) `pop(0)`) for BFS/level-order traversal — covered in [Section 7.5](#7-bst-traversals).

```python
from collections import deque
queue = deque([root])
```

### 26.3 Mutable Default Argument Pitfall
Never write `def f(x, result=[])`. Covered in [Section 7.4](#7-bst-traversals) — default arguments are evaluated once at function-definition time, causing state to leak across calls.

### 26.4 `nonlocal` for Closures That Mutate Outer Variables
When a nested recursive helper function needs to mutate a variable from its enclosing scope (e.g., `count`, `prev`, `result` in Kth-Smallest or Recover-Swapped-BST), use `nonlocal`:

```python
def outer():
    count = 0
    def helper():
        nonlocal count      # without this, 'count += 1' inside helper() raises UnboundLocalError
        count += 1
    helper()
    return count
```

### 26.5 `dataclass` for Cleaner Node Definitions

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class TreeNode:
    val: int = 0
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None
```

`dataclass` auto-generates `__init__`, `__repr__`, and `__eq__`, reducing boilerplate versus a hand-written class — useful in production code, though many interview platforms still expect the plain hand-written `__init__` style shown throughout this handbook (check the platform's provided template first).

### 26.6 Generators for Lazy Traversal (Memory-Efficient)

```python
def inorder_generator(node):
    if node:
        yield from inorder_generator(node.left)
        yield node.val
        yield from inorder_generator(node.right)

# Usage: process values one at a time without materializing a full list
for val in inorder_generator(root):
    print(val)
```
This is especially useful when you only need to **process values one at a time** (e.g., early-exit search for a condition) without paying the O(n) memory cost of building a full list upfront — conceptually related to the [BST Iterator](#15-bst-iterator) pattern, but simpler when you don't need the full `next()`/`hasNext()` API.

### 26.7 Performance Tip — Avoid Repeated Attribute Lookups in Hot Loops
In performance-critical traversal code (e.g., competitive programming with large trees), local variable caching can help:

```python
def inorder_iterative_fast(root):
    result = []
    append = result.append          # cache method lookup
    stack = []
    push, pop = stack.append, stack.pop
    current = root
    while current is not None or stack:
        while current is not None:
            push(current)
            current = current.left
        current = pop()
        append(current.val)
        current = current.right
    return result
```
This micro-optimization matters mainly in **competitive programming** contexts with tight time limits; not necessary for typical interview answers, but worth knowing it exists.

### 26.8 Memory Optimization — `__slots__`
For very large trees (millions of nodes), `__slots__` prevents Python from creating a per-instance `__dict__`, saving significant memory:

```python
class TreeNode:
    __slots__ = ('val', 'left', 'right')
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```


---

## 27. Common Mistakes Catalogue

A consolidated list of the most frequent BST bugs, gathered from every section above:

| # | Mistake | Where It Bites | Fix |
|---|---|---|---|
| 1 | Validating BST by comparing only to immediate parent | Validation | Pass down a `(low, high)` range (§12) |
| 2 | Forgetting `return root` in recursive insert/delete | Insert, Delete | Always propagate the (possibly new) subtree root back up |
| 3 | Mutable default argument (`result=[]`) | Traversals | Use `result=None`, initialize inside function |
| 4 | Using `list.pop(0)` instead of `deque.popleft()` | Level-order traversal | Always use `collections.deque` for BFS queues |
| 5 | Confusing floor/ceil direction (which way to move) | Floor & Ceil | Floor favors going right on candidates; Ceil favors going left |
| 6 | Physically swapping nodes instead of values | Recover Swapped BST | Always swap `.val`, never rewire pointers |
| 7 | Forgetting `second` update on every inversion | Recover Swapped BST | Update `second` unconditionally on each violation found |
| 8 | Not removing Morris traversal threads | Morris Traversal | Always `predecessor.right = None` on second visit |
| 9 | Using generic O(n) LCA algorithm on a BST | LCA | Use BST-property-based O(h) algorithm (§16) |
| 10 | Pruning both subtrees incorrectly in Trim BST | Trim BST | Only discard the subtree that's provably invalid; recurse into the other |
| 11 | Array slicing in sorted-array-to-BST (hidden O(n log n)) | Construction | Use index bounds `(left, right)` instead of slicing |
| 12 | O(n²) preorder-to-BST reconstruction via naive split-point search | Construction | Use bound-passing technique for O(n) |
| 13 | Including unnecessary null markers in BST serialization | Serialize/Deserialize | BST needs no nulls — structure is inferable from value order |
| 14 | Assuming a plain BST guarantees O(log n) | General | Always state worst-case O(n) for skewed trees explicitly |
| 15 | Ignoring duplicate value handling convention | Insert, Search, Validation | Always clarify duplicate policy with interviewer upfront |
| 16 | `RecursionError` on deep/skewed trees | Any recursive operation | Prefer iterative for production; mention trade-off in interviews |
| 17 | `UnboundLocalError` from missing `nonlocal` | Closures with recursive helpers | Always declare `nonlocal` for outer-scope mutation |
| 18 | Re-searching from `root` every step instead of updating `current` | Search | Use a single traversal pointer, don't restart |
| 19 | Off-by-one in kth-smallest count check | Kth Smallest/Largest | Be explicit about whether count starts at 0 or 1 |
| 20 | Confusing successor logic (`<`) with predecessor logic (`>`) | Successor/Predecessor | Keep the two mirrored implementations clearly separated mentally |

---

## 28. Master Cheat Sheets

### 28.1 BST Operations Complexity Cheat Sheet

| Operation | Balanced (Avg) | Skewed (Worst) | Space |
|---|---|---|---|
| Search | O(log n) | O(n) | O(1) iterative / O(h) recursive |
| Insert | O(log n) | O(n) | O(1) iterative / O(h) recursive |
| Delete | O(log n) | O(n) | O(1) iterative / O(h) recursive |
| Min / Max | O(log n) | O(n) | O(1) |
| Successor / Predecessor | O(log n) | O(n) | O(1) |
| Floor / Ceil | O(log n) | O(n) | O(1) |
| Validate BST | O(n) | O(n) | O(h) or O(1) with Morris |
| Kth Smallest/Largest (one-off) | O(h + k) | O(n) | O(h) |
| Kth Smallest (augmented tree) | O(log n) | O(n) if base tree unbalanced | O(n) extra for size fields |
| LCA | O(log n) | O(n) | O(1) iterative |
| Range Sum/Search | O(log n + m) | O(n) | O(h) |
| Traversal (any) | O(n) | O(n) | O(h) stack / O(1) Morris |
| Construction (sorted array) | O(n) | — (always balanced) | O(log n) |
| Serialize/Deserialize | O(n) | O(n) | O(n) + O(h) |

`h` = tree height, `n` = number of nodes, `m` = number of nodes in a query range, `k` = kth index.

### 28.2 Traversal Template Cheat Sheet

```python
# INORDER   (sorted order)         : Left → Node → Right
# PREORDER  (copy tree/serialize)  : Node → Left → Right
# POSTORDER (delete tree safely)   : Left → Right → Node
# LEVEL ORDER (BFS, uses deque)    : level by level
# REVERSE INORDER (descending)     : Right → Node → Left
```

### 28.3 BST Property Quick Reference

```
For every node N:
    all(N.left subtree)  <  N.val  <  all(N.right subtree)

Validation must use a GLOBAL range (low, high), not just parent comparison.
```

### 28.4 Delete — 3-Case Quick Reference

```
1. Leaf (no children)        → return None
2. One child                 → return that child (splice out)
3. Two children               → copy inorder successor's value up,
                                 then delete the successor from right subtree
```

### 28.5 Decision Tree — Which Pattern to Use

```
Need to find something?
 ├─ Exact value           → Search (§4)
 ├─ Next bigger/smaller    → Successor/Predecessor (§10)
 ├─ ≤k or ≥k (any k)       → Floor/Ceil (§11)
 ├─ kth in sorted order    → Kth Smallest/Largest (§14)
 └─ Common ancestor        → LCA (§16)

Need to modify structure?
 ├─ Add a value            → Insert (§5)
 ├─ Remove a value         → Delete (§6)
 ├─ Keep only a range       → Trim (§18)
 └─ Add sum of greater vals → Convert to Greater Tree (§19)

Need to check/fix correctness?
 ├─ Is it valid?            → Validation (§12)
 └─ Two nodes swapped?      → Recover Swapped BST (§13)

Need to build/transform representation?
 ├─ From sorted array/list  → Construction (§20)
 ├─ From preorder            → Construction from Preorder (§20.3)
 └─ To/from string            → Serialize/Deserialize (§21)
```

### 28.6 Python Syntax Quick Reference

```python
# Node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

# Recursive template
def recurse(node):
    if node is None:
        return <base_case>
    left_result = recurse(node.left)
    right_result = recurse(node.right)
    return <combine>

# Iterative traversal template (inorder)
stack, current = [], root
while current or stack:
    while current:
        stack.append(current); current = current.left
    current = stack.pop()
    # process current.val
    current = current.right
```

### 28.7 Formula Sheet

| Formula | Meaning |
|---|---|
| `height = log2(n+1) - 1` | Minimum possible height for n nodes (perfectly balanced) |
| `C(n) = (2n)! / ((n+1)! n!)` | Number of structurally distinct BSTs on n nodes (Catalan number) |
| `2^h ≤ n ≤ 2^(h+1) - 1` | Node count bounds for a tree of height h |


---

## 29. Practice Problem Bank

### 29.1 Basics / Search / Insert

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Search in a Binary Search Tree | LeetCode 700 | Easy | Search |
| Insert into a Binary Search Tree | LeetCode 701 | Medium | Insert |
| Search a node in BST | GeeksforGeeks | Easy | Search |
| Insertion in BST | GeeksforGeeks | Easy | Insert |
| BST Insert | Code360 | Easy | Insert |

### 29.2 Delete

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Delete Node in a BST | LeetCode 450 | Medium | Delete (all 3 cases) |
| Delete a Node from BST | GeeksforGeeks | Medium | Delete |
| Delete Value in BST | InterviewBit | Medium | Delete |

### 29.3 Validation

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Validate Binary Search Tree | LeetCode 98 | Medium | Min/Max range validation |
| Check if a Binary Tree is BST | GeeksforGeeks | Medium | Validation |
| Recover Binary Search Tree | LeetCode 99 | Hard | Recover Swapped BST |

### 29.4 Traversals

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Binary Tree Inorder Traversal | LeetCode 94 | Easy | Inorder (recursive/iterative/Morris) |
| Binary Tree Preorder Traversal | LeetCode 144 | Easy | Preorder |
| Binary Tree Postorder Traversal | LeetCode 145 | Easy | Postorder |
| Binary Tree Level Order Traversal | LeetCode 102 | Medium | BFS |
| Tree Traversals | GeeksforGeeks | Easy | All traversal types |

### 29.5 Successor / Predecessor / Floor / Ceil

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Inorder Successor in a BST | LeetCode 285 | Medium | Successor (no parent pointer) |
| Inorder Successor in a BST II | LeetCode 510 | Medium | Successor (with parent pointer) |
| Closest Binary Search Tree Value | LeetCode 270 | Easy | Floor/Ceil comparison |
| Predecessor and Successor in BST | GeeksforGeeks | Medium | Successor & Predecessor |
| Floor in BST | GeeksforGeeks | Easy | Floor |
| Ceil in BST | GeeksforGeeks | Easy | Ceil |

### 29.6 Kth Smallest/Largest

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Kth Smallest Element in a BST | LeetCode 230 | Medium | Inorder + early exit |
| Kth largest element in BST | GeeksforGeeks | Medium | Reverse inorder |
| Binary Search Tree Iterator | LeetCode 173 | Medium | BST Iterator (O(h) space) |

### 29.7 Range Queries & Construction

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Range Sum of BST | LeetCode 938 | Easy | Range Sum with pruning |
| Trim a Binary Search Tree | LeetCode 669 | Medium | Trim BST |
| Convert Sorted Array to BST | LeetCode 108 | Easy | Balanced construction |
| Convert Sorted List to BST | LeetCode 109 | Medium | Balanced construction |
| Construct BST from Preorder Traversal | LeetCode 1008 | Medium | Bound-passing construction |
| Binary Search Tree to Greater Sum Tree | LeetCode 1038 / 538 | Medium | Reverse inorder accumulation |

### 29.8 LCA & Advanced

| Problem | Platform | Difficulty | Concept |
|---|---|---|---|
| Lowest Common Ancestor of a BST | LeetCode 235 | Easy | BST-optimized LCA |
| Lowest Common Ancestor of a Binary Tree | LeetCode 236 | Medium | Generic LCA (contrast) |
| Serialize and Deserialize BST | LeetCode 449 | Medium | No-null-marker serialization |
| Two Sum IV - Input is a BST | LeetCode 653 | Easy | Inorder + two-pointer / hashset |
| Balance a Binary Search Tree | LeetCode 1382 | Medium | Inorder + rebuild balanced |
| Unique Binary Search Trees | LeetCode 96 | Medium | Catalan number counting |
| Unique Binary Search Trees II | LeetCode 95 | Medium | Generate all structurally distinct BSTs |
| Minimum Absolute Difference in BST | LeetCode 530 | Easy | Inorder adjacent difference |
| Trim a Binary Search Tree | LeetCode 669 | Medium | (see above) |
| Two Sum BSTs | LeetCode 1214 | Medium | Cross-tree inorder + two pointer |

### 29.9 Competitive Programming (CP-Style Judges)

| Problem | Platform | Concept |
|---|---|---|
| BST Insert/Delete/Query practice sets | Codeforces (search "BST" tag) | General BST operations under CP constraints |
| Order statistics / kth-element queries | CSES "Order Statistics Tree" style problems | Augmented BST / Fenwick alternative |
| Range queries with updates | AtCoder / CodeChef (various) | Range Sum/Search patterns generalized |
| BST-based simulation problems | HackerRank (Trees domain) | Search, Insert, Traversal fundamentals |

### 29.10 Recommended Study Order (Blind-75 / NeetCode Style Priority)

1. Search in a BST (LC 700)
2. Insert into a BST (LC 701)
3. Delete Node in a BST (LC 450)
4. Validate Binary Search Tree (LC 98)
5. Kth Smallest Element in a BST (LC 230)
6. Lowest Common Ancestor of a BST (LC 235)
7. Convert Sorted Array to BST (LC 108)
8. Inorder Successor in a BST (LC 285)
9. Range Sum of BST (LC 938)
10. Recover Binary Search Tree (LC 99)
11. Binary Search Tree Iterator (LC 173)
12. Serialize and Deserialize BST (LC 449)
13. Construct BST from Preorder Traversal (LC 1008)
14. Trim a Binary Search Tree (LC 669)
15. Balance a Binary Search Tree (LC 1382)


---

## 30. Final Revision & FAQs

### 30.1 One-Page Mind Map

```
                              BINARY SEARCH TREE
                                      │
        ┌─────────────┬──────────────┼──────────────┬─────────────┐
        │              │              │               │             │
   FUNDAMENTALS    OPERATIONS     TRAVERSALS       PATTERNS       ADVANCED
        │              │              │               │             │
  Root/Leaf/Height  Search(§4)    Inorder(sorted)  Kth Smallest  AVL Trees
  Balanced/Skewed   Insert(§5)    Preorder         Kth Largest   Red-Black Trees
  BST Property      Delete(§6)    Postorder        Successor/    Rotations
                    Min/Max(§9)   Level Order      Predecessor   Order-Statistic
                    Successor/    Reverse Inorder  Floor/Ceil    Threaded BST
                    Predecessor   Morris(O(1))     LCA           Persistent BST
                    (§10)                          Range Sum/
                    Floor/Ceil(§11)                Search
                    Validation(§12)                Trim
                    Recover(§13)                   Convert to
                                                    Greater Tree
                                                    Construction
                                                    Serialize/
                                                    Deserialize
```

### 30.2 15-Minute Revision (Absolute Essentials)

1. **BST Property:** left < node < right, globally (not just parent).
2. **Search/Insert/Delete:** all O(log n) balanced, O(n) skewed. Delete has 3 cases (leaf, 1 child, 2 children → successor swap).
3. **Inorder traversal = sorted order** — the single most important fact about BSTs.
4. **Validation:** must pass a `(low, high)` range down, never compare to parent alone.
5. **Kth smallest = kth element in inorder** (early-exit for efficiency).
6. **LCA in a BST:** O(h), using value comparisons (`both < root`→left, `both > root`→right, else root is LCA) — do NOT use the generic O(n) binary-tree algorithm.
7. **Morris Traversal:** O(1) space traversal using temporary "threads"; know it exists and roughly how it works.
8. **Self-balancing trees (AVL/Red-Black) exist because plain BSTs can degrade to O(n)** on sorted/adversarial input.

### 30.3 1-Hour Revision (Full Pass)

Work through, in order: §1 (Intro) → §3 (Implementation) → §4-6 (Search/Insert/Delete, code + dry runs) → §7 (Traversals) → §10-11 (Successor/Predecessor, Floor/Ceil) → §12 (Validation) → §14 (Kth Smallest/Largest) → §16 (LCA) → §22 (Advanced overview) → §28 (Cheat Sheets) — this sequence covers every concept that appears in ≥90% of real BST interview questions.

### 30.4 Frequently Asked Questions

**Q1: Is a BST the same as a Binary Tree?**
No. Every BST is a binary tree, but not every binary tree is a BST. A binary tree only requires "at most two children per node"; a BST additionally requires the ordering property (left < node < right, globally).

**Q2: What is the worst-case time complexity of BST operations?**
O(n), when the tree is skewed (degenerates into a linked list) — e.g., after inserting already-sorted data into a plain, non-self-balancing BST.

**Q3: Why does inorder traversal of a BST give sorted output?**
Because inorder visits (left subtree, node, right subtree) in that order, and the BST property guarantees everything in the left subtree is smaller and everything in the right subtree is larger — recursively, this produces strictly increasing order.

**Q4: How do you validate a BST correctly?**
Pass down a valid `(low, high)` range as you recurse, tightening it at each step (left recursion updates `high`, right recursion updates `low`). Never compare a node only to its immediate parent — that misses violations from higher ancestors.

**Q5: How is deleting a node with two children handled?**
Find the inorder successor (minimum of the right subtree), copy its value into the node being "deleted," then recursively delete the successor's original node (which will always be a simpler 0-or-1-child case).

**Q6: Does Python have a built-in BST?**
No. Python's `dict`/`set` are hash tables. There's no BST in the standard library — `sortedcontainers.SortedList`/`SortedDict` (third-party) provide similar sorted-order guarantees using a different underlying implementation (a list of sorted sublists), not a classic BST.

**Q7: When should I use an iterative approach instead of recursive?**
When explicitly asked for O(1) auxiliary space, or when working with potentially very large/skewed trees where recursion could hit Python's recursion limit (`RecursionError`).

**Q8: What's the difference between successor/predecessor and floor/ceil?**
Successor/predecessor operate relative to a **specific node already in the tree**, using strict `<`/`>`. Floor/ceil operate relative to **any query value** (which may or may not be present in the tree), using inclusive `≤`/`≥`.

**Q9: Why use Morris Traversal if it's more complex than stack-based traversal?**
It achieves true O(1) auxiliary space (no stack, no recursion), which matters in memory-constrained scenarios or when explicitly requested. The trade-off is temporary tree mutation and higher implementation complexity/bug risk.

**Q10: What's the point of self-balancing trees like AVL or Red-Black?**
They guarantee O(log n) height regardless of insertion order, protecting against the worst-case O(n) degradation that plain BSTs suffer when given sorted or adversarial input.

**Q11: How do I recognize that a problem needs a BST-specific optimization rather than a generic tree algorithm?**
Look for value-ordering clues: "sorted," "kth smallest/largest," "range between two values," "closest value," "floor/ceil." If the problem explicitly states or implies the tree is a BST, always ask whether the ordering property enables a faster-than-generic-tree solution (e.g., O(h) LCA instead of generic O(n) LCA).

**Q12: Can a BST have duplicate values?**
By strict definition, no (values are unique). Many implementations, if duplicates must be supported, adopt a convention (e.g., "duplicates go to the right subtree") — always clarify and state this convention explicitly, since it affects search, insert, delete, and validation logic consistently.

### 30.5 Closing Summary

This handbook covered the Binary Search Tree from first principles (why it exists, its defining property) through every core operation (search, insert, delete with all three cases), every traversal (including O(1)-space Morris traversal), every major interview pattern (successor/predecessor, floor/ceil, validation, recovery, kth-smallest/largest, iterator design, LCA, range queries, trimming, greater-tree conversion, construction, and serialization), and closed with an overview of the advanced self-balancing and augmented variants (AVL, Red-Black, order-statistic, threaded, persistent) that underpin real-world systems. Combined with the cheat sheets, mistake catalogue, and practice problem bank, this document is intended to serve as a **single, comprehensive reference** for BST mastery — from first exposure through FAANG-level interview preparation.

