# THE COMPLETE PYTHON LINKED LIST HANDBOOK


## 📖 TABLE OF CONTENTS

1. [Introduction](#1-introduction)
2. [Python Linked List Implementation](#2-python-linked-list-implementation)
3. [Linked List Fundamentals](#3-linked-list-fundamentals)
4. [Types of Linked Lists](#4-types-of-linked-lists)
5. [Core Operations](#5-core-operations)
6. [Important Linked List Algorithms](#6-important-linked-list-algorithms)
7. [Pointer Patterns](#7-pointer-patterns)
8. [Advanced Linked List Concepts](#8-advanced-linked-list-concepts)
9. [Applications](#9-applications)
10. [Problem Recognition](#10-problem-recognition)
11. [Optimization](#11-optimization)
12. [Interview Preparation](#12-interview-preparation)
13. [Python Tips](#13-python-tips)
14. [Common Mistakes](#14-common-mistakes)
15. [Cheat Sheets](#15-cheat-sheets)
16. [Practice Problems](#16-practice-problems)
17. [Final Revision](#17-final-revision)
18. [FAQs](#18-faqs)

---

## 1. INTRODUCTION

### 1.1 What Is a Linked List?

A **Linked List** is a linear data structure in which elements (called **nodes**) are not stored in contiguous memory locations. Instead, each node stores:

1. **Data** — the actual value.
2. **A reference (pointer)** — to the next node in the sequence.

Unlike an array, where the position of an element is *computed* from a base address (`base + index * size`), a linked list finds an element by **following references one hop at a time**.

```
ARRAY (contiguous memory):
+----+----+----+----+----+
| 10 | 20 | 30 | 40 | 50 |
+----+----+----+----+----+
 1000 1004 1008 1012 1016   <- addresses are predictable

LINKED LIST (scattered memory):
[10 | 0x3F2] --> [20 | 0x9A1] --> [30 | 0x0C4] --> [40 | None]
  addr 0x100        addr 0x3F2       addr 0x9A1       addr 0x0C4
```

### 1.2 History

The linked list concept originates from **Allen Newell, Cliff Shaw, and Herbert A. Simon** at RAND Corporation in 1955–56, as part of the **IPL (Information Processing Language)** used to build the *Logic Theorist*, one of the earliest AI programs. Linked structures allowed dynamic manipulation of symbolic data — something fixed arrays could not do efficiently. Since then, linked lists have become a foundational data structure taught in every computer science curriculum and used inside real systems (kernels, language runtimes, databases).

### 1.3 Why Linked Lists Exist

Arrays solve many problems, but they have two structural weaknesses:

| Problem with Arrays | How Linked Lists Solve It |
|---|---|
| Fixed size (static arrays) — must know size upfront | Nodes are allocated dynamically, one at a time |
| Insertion/deletion in the middle is O(n) due to shifting | Insertion/deletion is O(1) once you have a pointer to the location |
| Resizing (dynamic arrays) requires costly reallocation + copy | No reallocation ever needed — just link a new node |
| Wastes memory when over-allocated | Uses exactly as much memory as needed (plus pointer overhead) |

**Trade-off**: Linked lists give up O(1) random access (`arr[i]`) in exchange for O(1) structural mutation.

### 1.4 Characteristics

- **Linear** structure — one node leads to the next.
- **Dynamic size** — grows/shrinks at runtime.
- **Sequential access only** — no direct indexing.
- **Non-contiguous memory** — nodes can live anywhere in the heap.
- Each node has **extra memory overhead** for storing pointer(s).

### 1.5 Properties

| Property | Value |
|---|---|
| Access by index | O(n) |
| Search | O(n) |
| Insert at head | O(1) |
| Insert at tail | O(1) with tail pointer, else O(n) |
| Insert at middle | O(n) to find + O(1) to link |
| Delete at head | O(1) |
| Delete at tail | O(n) for singly (need prev), O(1) for doubly with tail pointer |
| Extra space per node | O(1) pointer(s) |

### 1.6 Advantages

- ✅ Dynamic size — no pre-allocation needed.
- ✅ Efficient insertion/deletion at known positions (O(1)).
- ✅ No memory wasted on unused capacity.
- ✅ Easy to implement stacks, queues, deques, adjacency lists.
- ✅ No "shifting" cost like arrays.

### 1.7 Disadvantages

- ❌ No O(1) random access — must traverse.
- ❌ Extra memory per node for storing pointers.
- ❌ Poor **cache locality** (nodes scattered in memory → more cache misses vs arrays).
- ❌ Reverse traversal impossible in singly linked lists.
- ❌ More complex pointer bookkeeping → more bugs.

### 1.8 Applications

- Implementing **Stacks** and **Queues**.
- **Hash table chaining** (collision resolution).
- **Graph adjacency lists**.
- **LRU/LFU caches**.
- **Undo/Redo** functionality in editors.
- **Browser history** (back/forward — doubly linked list).
- **Music/video playlists** (circular linked list, next/prev track).
- Operating system **memory management** (free block lists).
- **Polynomial representation** in symbolic math.
- **Big integer arithmetic** (digit-by-digit linked representation).

### 1.9 Real-World Examples

| Real World | Linked List Analogy |
|---|---|
| A treasure hunt where each clue tells you where the next clue is | Singly linked list traversal |
| A train — each coach connects to the next and previous coach | Doubly linked list |
| A circular relay race where the last runner passes back to the first | Circular linked list |
| A music player's "shuffle" that loops back to song 1 after the last song | Circular linked list |
| Browser back/forward buttons | Doubly linked list with a "current" pointer |

> 💡 **Tip**: Whenever an interview problem says "you cannot use extra memory" or "modify the list in-place using pointers," that's your signal you're in Linked-List-Pointer-Manipulation land.


---

## 2. PYTHON LINKED LIST IMPLEMENTATION

### 2.1 The Node Class

A node is the atomic building block. In Python, we typically implement it as a small class holding `val` (data) and `next` (reference).

```python
class Node:
    """A single node in a singly linked list."""
    __slots__ = ("val", "next")   # memory optimization: no per-instance __dict__

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"
```

**Line-by-line explanation:**
- `__slots__ = ("val", "next")`: tells Python not to create a per-instance `__dict__`. This saves memory — important when you have millions of nodes.
- `val`: the payload / data stored in this node.
- `next`: a reference to the next `Node` object, or `None` if this is the last node.
- `__repr__`: helps debugging by printing `Node(10)` instead of `<__main__.Node object at 0x7f...>`.

### 2.2 Memory Representation

```
Node object in Python heap:
+--------------------------+
| Node                     |
|--------------------------|
| val  : 10                |
| next : ----> (points to next Node object, or None)
+--------------------------+
```

Every Python variable is a **reference** to an object on the heap (Python has no raw pointers, but references behave the same way conceptually). When you write `node.next = other_node`, you are copying a *reference* — not the object itself.

### 2.3 The LinkedList Wrapper Class

```python
class LinkedList:
    """A singly linked list with head/tail tracking and O(1) size lookup."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.head is None

    def append(self, val):
        """Insert at the end — O(1) because we track tail."""
        new_node = Node(val)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def __iter__(self):
        current = self.head
        while current:
            yield current.val
            current = current.next

    def __repr__(self):
        return " -> ".join(str(v) for v in self) + " -> None"
```

**Why a wrapper class?** Keeping `head`/`tail`/`size` bundled avoids passing them around as loose variables, and gives you O(1) `append` and O(1) `len()` instead of recomputing every time.

### 2.4 Dataclass Implementation (Modern Python)

```python
from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class DataNode:
    val: Any
    next: Optional["DataNode"] = None
```

`@dataclass` auto-generates `__init__`, `__repr__`, and `__eq__`. The forward reference `"DataNode"` (as a string) is required because the class refers to itself before it's fully defined — this is a classic **self-referential type** pattern.

> 📝 **Note**: `typing.Optional[X]` is shorthand for `Union[X, None]`. It documents that `next` might legitimately be `None` (end of list) — extremely useful for static type checkers like `mypy`.

### 2.5 Generic Node (Type-Safe)

```python
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class GenericNode(Generic[T]):
    def __init__(self, val: T, next: Optional["GenericNode[T]"] = None):
        self.val: T = val
        self.next: Optional["GenericNode[T]"] = next
```

This lets you write `GenericNode[int]` or `GenericNode[str]` and have your type checker enforce consistent typing across the whole list.

### 2.6 Object References — The Core Mental Model

```python
a = Node(1)
b = Node(2)
a.next = b        # a's "next" slot now references the same object as b

print(a.next is b)   # True — they are literally the same object in memory
```

> ⚠️ **Warning**: `a.next = b` does **not** copy `b`. If you later mutate `b.val`, `a.next.val` changes too, because both names refer to the *same* object. This is the #1 source of subtle linked-list bugs for beginners coming from array-only backgrounds.

### 2.7 Best Practices

- Use `__slots__` on `Node` classes when building performance-critical or large-scale lists (saves ~50% memory per node vs a normal class with `__dict__`).
- Prefer a **dummy/sentinel head** in list-mutation algorithms to eliminate "is this the first node?" special-casing (covered in depth in §7.3).
- Keep `Node` "dumb" (just data + pointers); keep list-level logic (`insert`, `delete`, `reverse`) in the `LinkedList` class or as free functions. This separation of concerns matches how real-world linked structures (e.g., Linux kernel `list_head`) are designed.
- Always null-out (`node.next = None`) removed nodes if you're worried about lingering references causing memory leaks or accidental cycles.

### 2.8 Performance Considerations

| Concern | Detail |
|---|---|
| Memory per node | A plain Python object with 2 attributes uses ~56 bytes+ overhead without `__slots__`; `__slots__` cuts this significantly. |
| Cache locality | Nodes are scattered in heap memory (unlike arrays), causing more CPU cache misses on traversal — arrays are faster for pure iteration despite same Big-O. |
| Garbage collection | Python's reference counting frees nodes as soon as no references remain — but **reference cycles** (e.g., in circular lists) need the cyclic garbage collector to clean up. |
| CPython overhead | Native Python linked lists are slower than `collections.deque` (a C-implemented doubly linked list) for most general use — use `deque` in production unless you need custom node-level logic for an interview/algorithm. |


---

## 3. LINKED LIST FUNDAMENTALS

### 3.1 Core Terminology

| Term | Meaning |
|---|---|
| **Node** | A container holding data + reference(s) to other node(s) |
| **Head** | Reference to the first node of the list |
| **Tail** | Reference to the last node (its `next` is `None`) |
| **Pointer / Reference** | A variable holding the memory address (in Python: the object reference) of another node |
| **Next** | The forward-direction pointer field of a node |
| **Previous** | The backward-direction pointer field (only in doubly linked lists) |
| **Traversal** | The process of visiting each node in order by following `next` (and/or `prev`) |
| **Length** | Number of nodes in the list |
| **Null / None** | Represents "no node here" — the natural list terminator in Python |
| **Sentinel / Dummy Node** | A placeholder node (often with no meaningful data) used to simplify edge-case handling |

### 3.2 Traversal Visualization

```
head
 |
 v
[10|*]--->[20|*]--->[30|*]--->[40|None]

Step 1: current = head        -> visiting 10
Step 2: current = current.next-> visiting 20
Step 3: current = current.next-> visiting 30
Step 4: current = current.next-> visiting 40
Step 5: current = current.next-> current is None -> STOP
```

```python
def traverse(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
```

### 3.3 The "Dynamic Memory" Concept

Arrays (in low-level languages) require a contiguous memory block allocated once. Linked lists instead call the memory allocator **once per node**, on demand:

```
Array allocation (conceptual):
malloc(5 * sizeof(int))   -> one big contiguous block

Linked List allocation (conceptual):
malloc(sizeof(Node))  -- node 1
malloc(sizeof(Node))  -- node 2
malloc(sizeof(Node))  -- node 3
... each can live ANYWHERE in the heap
```

In Python, this happens implicitly every time you write `Node(val)` — the CPython memory allocator (`pymalloc`) grabs a chunk from the heap.

### 3.4 The Empty List

An empty linked list is represented simply as `head = None`. There are zero nodes.

```
head = None      (no nodes exist at all)
```

> ⚠️ **Warning**: Always special-case (or dummy-node-protect) the empty list in every operation you write — it's the single most common source of interview bugs (`AttributeError: 'NoneType' object has no attribute 'next'`).

### 3.5 Length of a List

```python
def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
```

- **Time**: O(n) unless you maintain a running `size` counter in a wrapper class (then O(1)).
- **Space**: O(1).

### 3.6 Sentinel / Dummy Node — Deep Dive

A **dummy node** is a fake node placed *before* the real head, so that "inserting/deleting the head" is no longer a special case — it becomes identical to inserting/deleting any other node.

```
WITHOUT dummy:                         WITH dummy:
head -> [10] -> [20] -> [30] -> None   dummy -> [10] -> [20] -> [30] -> None
 ^ special-cased in delete/insert        ^ head = dummy.next (real head)
```

```python
def delete_value(head, target):
    dummy = Node(0, head)     # dummy.next points at the real head
    prev, current = dummy, head
    while current:
        if current.val == target:
            prev.next = current.next   # unlink — works even if current is head!
        else:
            prev = current
        current = current.next
    return dummy.next   # new head (might have changed if old head was deleted)
```

Notice there's **no special "if current is head" branch** — the dummy node absorbed that case automatically.

> 💡 **Interview Tip**: Whenever a problem involves *possibly deleting/modifying the head node itself*, reach for a dummy node immediately. It's one of the highest-leverage tricks in this entire handbook.


---

## 4. TYPES OF LINKED LISTS

### 4.1 Singly Linked List (SLL)

Each node points only **forward**.

```
head -> [10|*] -> [20|*] -> [30|*] -> None
```

```python
class SNode:
    __slots__ = ("val", "next")
    def __init__(self, val, next=None):
        self.val, self.next = val, next
```

- ✅ Least memory per node (1 pointer).
- ❌ Cannot traverse backward.
- ❌ Deleting the tail requires O(n) traversal to find the previous node.

### 4.2 Doubly Linked List (DLL)

Each node points **forward and backward**.

```
None <- [10|prev|next] <-> [20|prev|next] <-> [30|prev|next] -> None
              ^head                                 ^tail
```

```python
class DNode:
    __slots__ = ("val", "prev", "next")
    def __init__(self, val, prev=None, next=None):
        self.val, self.prev, self.next = val, prev, next
```

- ✅ Bidirectional traversal.
- ✅ O(1) deletion given only a node reference (no need to find `prev` by scanning).
- ❌ Extra pointer = more memory per node.
- ❌ More pointers to update correctly on every mutation (easier to introduce bugs).

**Insertion in a DLL (visual):**
```
Before:  [A] <-> [B] <-> [C]
Insert X between A and B:

  1. X.prev = A         2. X.next = B
  3. A.next = X         4. B.prev = X

After:   [A] <-> [X] <-> [B] <-> [C]
```

> ⚠️ **Warning**: Order matters! If you set `A.next = X` *before* saving `B = A.next`, you lose the reference to `B` forever. Always capture old pointers into local variables before overwriting them.

### 4.3 Circular Singly Linked List

The tail's `next` points back to the `head` instead of `None`.

```
+-----------------------------------+
|                                   v
[10|*] -> [20|*] -> [30|*] --------+
 ^head
```

```python
def traverse_circular(head):
    if not head:
        return
    current = head
    while True:
        print(current.val, end=" -> ")
        current = current.next
        if current is head:
            break
    print("(back to head)")
```

> ⚠️ **Warning**: Naive `while current:` traversal on a circular list **never terminates** — `current` is never `None`. Always terminate on `current is head` (or track a count / use fast-slow detection).

### 4.4 Circular Doubly Linked List

Combines both: `tail.next == head` and `head.prev == tail`.

```
   +----------------------------------------------+
   |                                                |
   v                                                |
[10] <-> [20] <-> [30] --------------------------->+
 ^head                 ^tail
```

Used in real systems like the **Linux kernel's `list_head`** structure and **Python's own `OrderedDict`** internals (a doubly linked list of hash entries to preserve insertion order).

### 4.5 Header Linked List

A specialized list that always keeps a dedicated **header node** (distinct from a data node) storing metadata — e.g., count of nodes, or acting purely as a permanent sentinel. Conceptually the "dummy node" pattern (§3.6) made permanent and structural rather than a temporary local variable.

### 4.6 Multi-Level Linked List

Each node may have an additional pointer, e.g. `child`, that leads to another independent linked list ("flattening" problems ask you to merge these into one list). See §6 "Flatten Multilevel Linked List."

```
1 -> 2 -> 3 -> 4 -> 5
     |
     7 -> 8 -> 9
          |
          10 -> 11
```

### 4.7 XOR Linked List (Concept Only)

A memory-optimization trick (mainly relevant in C/C++, shown here conceptually) where each node stores a **single field** equal to `XOR(address_of_prev, address_of_next)` instead of two separate pointers. To move forward you XOR that field with the address you came from.

> 📝 **Note**: XOR linked lists are **not practical in Python** because Python doesn't expose raw memory addresses for user manipulation (no pointer arithmetic), and its garbage collector requires real references to keep objects alive — an XOR'd address isn't a real reference, so the referenced node could get garbage collected. This is included for CS-theory completeness only.

### 4.8 Unrolled Linked List (Overview)

A hybrid data structure: each node holds a **small array of elements** instead of a single value, plus a `next` pointer to the next block.

```
[10,20,30|*] -> [40,50,60|*] -> [70,80|None]
```

This improves cache locality (fewer pointer hops, more array-like reads) while retaining O(1)-ish insertion behavior within a block. Used in some text editor "rope"-like structures and database page layouts.

### 4.9 Skip List (Comparison Only)

Not technically a "type of linked list" in the traditional sense, but built **on top of** multiple layered linked lists to give O(log n) search — used in Redis' sorted sets and LevelDB.

```
Level 2: 1 -----------------> 9 --------------> 21
Level 1: 1 -------> 5 ------> 9 ------> 15 ---> 21
Level 0: 1 -> 3 -> 5 -> 7 -> 9 -> 12 -> 15 -> 18 -> 21
```

| Structure | Search | Insert | Notes |
|---|---|---|---|
| Singly Linked List | O(n) | O(1) at known position | Simplest |
| Skip List | O(log n) expected | O(log n) expected | Probabilistic balancing via multiple levels |

### 4.10 Comparison Table — All Types

| Type | Forward Traversal | Backward Traversal | Extra Memory/Node | Common Use Case |
|---|---|---|---|---|
| Singly | ✅ | ❌ | 1 pointer | Stacks, simple sequences |
| Doubly | ✅ | ✅ | 2 pointers | Browser history, LRU cache |
| Circular Singly | ✅ (looped) | ❌ | 1 pointer | Round-robin scheduling |
| Circular Doubly | ✅ (looped) | ✅ (looped) | 2 pointers | Music playlists, `OrderedDict`-style structures |
| Multi-level | ✅ + child traversal | depends | 2+ pointers | Nested/flattening problems |


---

## 5. CORE OPERATIONS

> All examples use this base `Node`:
> ```python
> class Node:
>     __slots__ = ("val", "next")
>     def __init__(self, val, next=None):
>         self.val, self.next = val, next
> ```

### 5.1 Create

```python
def build_list(values):
    """Build a linked list from a Python list. Returns head."""
    dummy = Node(0)
    tail = dummy
    for v in values:
        tail.next = Node(v)
        tail = tail.next
    return dummy.next
```

**Dry Run** — `build_list([10, 20, 30])`:

| Step | v | tail before | Action | List State |
|---|---|---|---|---|
| 1 | 10 | dummy | tail.next = Node(10); tail = Node(10) | 10 |
| 2 | 20 | Node(10) | tail.next = Node(20); tail = Node(20) | 10 -> 20 |
| 3 | 30 | Node(20) | tail.next = Node(30); tail = Node(30) | 10 -> 20 -> 30 |

**Complexity**: Time O(n), Space O(n) (n new nodes).

### 5.2 Traverse

Covered fully in §3.2. Time O(n), Space O(1).

### 5.3 Search

```python
def search(head, target):
    current = head
    position = 0
    while current:
        if current.val == target:
            return position
        current = current.next
        position += 1
    return -1
```

**Complexity**: Time O(n), Space O(1). No binary search possible — no random access.

### 5.4 Insert at Beginning

```python
def insert_at_beginning(head, val):
    new_node = Node(val, head)   # new_node.next = old head
    return new_node              # new_node is the new head
```

```
Before: head -> [10] -> [20] -> None
Insert 5:
        new_node[5] --next--> [10]
        head = new_node

After:  head -> [5] -> [10] -> [20] -> None
```

**Complexity**: Time O(1), Space O(1).

### 5.5 Insert at End

```python
def insert_at_end(head, val):
    new_node = Node(val)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head
```

- Without a tracked `tail`: Time O(n) (must walk to the end).
- With a tracked `tail` pointer (wrapper class, §2.3): Time O(1).

### 5.6 Insert at Position

```python
def insert_at_position(head, val, pos):
    """0-indexed position."""
    if pos == 0:
        return Node(val, head)
    dummy = Node(0, head)
    prev = dummy
    for _ in range(pos):
        if prev.next is None:
            raise IndexError("Position out of bounds")
        prev = prev.next
    prev.next = Node(val, prev.next)
    return dummy.next
```

**Dry Run** — insert `99` at position `2` into `10 -> 20 -> 30 -> 40`:

| Step | prev | Explanation |
|---|---|---|
| start | dummy | dummy.next = 10 |
| loop i=0 | prev=10 | move forward |
| loop i=1 | prev=20 | move forward (stop, ran `range(2)` twice) |
| insert | new=Node(99, prev.next=30) | prev.next = new |

Result: `10 -> 20 -> 99 -> 30 -> 40`

**Complexity**: Time O(pos), Space O(1).

### 5.7 Delete from Beginning

```python
def delete_from_beginning(head):
    if head is None:
        return None
    return head.next
```
**Complexity**: O(1).

### 5.8 Delete from End

```python
def delete_from_end(head):
    if head is None or head.next is None:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head
```
Need to stop at the **second-last** node (since singly linked lists can't look backward). **Complexity**: O(n).

### 5.9 Delete by Value

```python
def delete_by_value(head, target):
    dummy = Node(0, head)
    prev, current = dummy, head
    while current:
        if current.val == target:
            prev.next = current.next
            break
        prev, current = current, current.next
    return dummy.next
```
**Complexity**: O(n) worst case (target near the end / absent).

### 5.10 Delete by Position

```python
def delete_by_position(head, pos):
    dummy = Node(0, head)
    prev = dummy
    for _ in range(pos):
        prev = prev.next
    if prev.next:
        prev.next = prev.next.next
    return dummy.next
```
**Complexity**: O(pos).

### 5.11 Update (Set Value at Position)

```python
def update_value(head, pos, new_val):
    current = head
    for _ in range(pos):
        current = current.next
    current.val = new_val
```
**Complexity**: O(pos).

### 5.12 Count Nodes / Find Length

See §3.5. Iterative O(n). Recursive version:

```python
def length_recursive(head):
    if head is None:
        return 0
    return 1 + length_recursive(head.next)
```
**Complexity**: Time O(n), **Space O(n)** due to recursion call stack — worse than iterative for very long lists (risk of `RecursionError`).

### 5.13 Reverse (Preview — full deep dive in §6.1)

```python
def reverse(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
```

### 5.14 Copy / Clone (Simple, No Random Pointer)

```python
def clone(head):
    dummy = Node(0)
    tail = dummy
    current = head
    while current:
        tail.next = Node(current.val)
        tail = tail.next
        current = current.next
    return dummy.next
```
This creates **entirely new nodes** with copied values — mutating the clone never affects the original. (Contrast with `new_list = head`, which just copies the *reference* to the same nodes — a shallow alias, not a clone!)

### 5.15 Compare Two Lists

```python
def are_equal(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1, head2 = head1.next, head2.next
    return head1 is None and head2 is None   # both must end together
```
**Complexity**: O(min(n, m)).

### 5.16 Concatenate Two Lists

```python
def concatenate(head1, head2):
    if head1 is None:
        return head2
    current = head1
    while current.next:
        current = current.next
    current.next = head2
    return head1
```
**Complexity**: O(n) without a tail pointer, O(1) with one.

### 5.17 Split List (Into Two Halves)

```python
def split_list(head):
    """Split using fast/slow pointers. Returns (first_half_head, second_half_head)."""
    if head is None or head.next is None:
        return head, None
    slow, fast = head, head.next     # fast starts 1 ahead so slow lands
    while fast and fast.next:        # on the END of the first half for even lengths
        slow = slow.next
        fast = fast.next.next
    second_half = slow.next
    slow.next = None                 # cut the link
    return head, second_half
```
**Complexity**: Time O(n), Space O(1). (Full fast/slow explanation in §7.1.)

### 5.18 Recursive vs Iterative — Summary Table

| Operation | Iterative Space | Recursive Space | Preferred |
|---|---|---|---|
| Traverse | O(1) | O(n) call stack | Iterative |
| Reverse | O(1) | O(n) call stack | Iterative (unless asked recursively) |
| Length | O(1) | O(n) call stack | Iterative |
| Search | O(1) | O(n) call stack | Iterative |

> 💡 **Interview Tip**: Interviewers sometimes explicitly ask for the *recursive* version of reverse/traverse to test your understanding of the call stack. Know both — but default to iterative for production-quality code (avoids `RecursionError` on lists with thousands of nodes, since CPython's default recursion limit is ~1000).


---

## 6. IMPORTANT LINKED LIST ALGORITHMS

### 6.1 Reverse a Linked List

**Problem**: Given the head of a singly linked list, reverse it in place and return the new head.

**Intuition**: We must flip every `next` pointer to point backward. Since a singly linked list can't look backward, we need to remember the previous node as we go, *before* we overwrite `current.next`.

**Visualization:**
```
Initial:   None <- prev   current -> [10]->[20]->[30]->None

Step 1:    None <-[10]   prev=10, current=20
                  ^next now points to None (was pointing to 20)

Step 2:    None<-[10]<-[20]   prev=20, current=30

Step 3:    None<-[10]<-[20]<-[30]   prev=30, current=None -> STOP

Final head = prev = [30]
```

```python
def reverse_iterative(head):
    prev = None
    current = head
    while current:
        nxt = current.next     # (1) save next before overwriting
        current.next = prev    # (2) reverse the pointer
        prev = current          # (3) advance prev
        current = nxt           # (4) advance current
    return prev                 # prev is the new head
```

**Why this exact order?** If you did `current.next = prev` *before* saving `nxt`, you'd lose the rest of the list forever — `current.next` was your only link to it.

**Dry Run** — reverse `10 -> 20 -> 30`:

| Step | current | prev (before) | nxt | current.next (after) | prev (after) | List so far |
|---|---|---|---|---|---|---|
| 1 | 10 | None | 20 | None | 10 | 10->None |
| 2 | 20 | 10 | 30 | 10 | 20 | 20->10->None |
| 3 | 30 | 20 | None | 20 | 30 | 30->20->10->None |
| end | None | — | — | — | — | loop stops |

Result: `30 -> 20 -> 10 -> None` ✅

**Recursive version:**
```python
def reverse_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head   # make the next node point back at current
    head.next = None        # break the old forward link
    return new_head
```

**Complexity**: Iterative — Time O(n), Space O(1). Recursive — Time O(n), Space O(n) (call stack).

**Common Mistakes**:
- Forgetting to save `nxt` before reassigning `current.next` → losing the rest of the list.
- Returning `head` instead of `prev` (returns the old head, now the *tail*, which is wrong).
- Off-by-one in recursive base case (`head is None` alone is not enough — must also check `head.next is None`).

**Interview Tip**: This is the #1 most-asked linked list warm-up. Master it cold — many harder problems (Reverse Between, Reverse K Group, Palindrome check) build directly on this pattern.

---

### 6.2 Reverse Between (Reverse a Sub-List from position m to n)

**Problem**: Reverse only the nodes from position `left` to `right` (1-indexed), leaving the rest untouched.

```
Input:  1 -> 2 -> 3 -> 4 -> 5,  left=2, right=4
Output: 1 -> 4 -> 3 -> 2 -> 5
```

```python
def reverse_between(head, left, right):
    dummy = Node(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next          # prev now sits just BEFORE the sublist

    current = prev.next           # current will become the sublist's tail
    for _ in range(right - left):
        temp = current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next = temp
    return dummy.next
```

**Visualization (head-insertion inside the sublist):**
```
prev -> [2] -> [3] -> [4] -> [5]     (current = 2)

iter1: temp=3
       [2]->[4]  (current.next skips 3)
       [3]->[2]  (temp.next = prev.next = 2)
       prev->[3] (prev.next = temp)
Result: prev -> [3] -> [2] -> [4] -> [5]

iter2: temp=4
       [2]->[5]
       [4]->[3]
       prev->[4]
Result: prev -> [4] -> [3] -> [2] -> [5]
```

**Complexity**: Time O(right), Space O(1).

**Common mistakes**: Forgetting the dummy node when `left == 1` (reversing starting at the head) — without it you'd need a separate branch.

---

### 6.3 Reverse Nodes in K-Group

**Problem**: Reverse every consecutive group of `k` nodes. If remaining nodes `< k`, leave them as-is.

```
Input: 1->2->3->4->5, k=2
Output: 2->1->4->3->5
```

```python
def reverse_k_group(head, k):
    # Step 1: check there are at least k nodes left
    node = head
    for _ in range(k):
        if node is None:
            return head          # fewer than k nodes remain — leave as-is
        node = node.next

    # Step 2: reverse the first k nodes (standard reversal, bounded)
    prev, current = None, head
    for _ in range(k):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    # Step 3: recurse for the rest of the list, then attach
    head.next = reverse_k_group(current, k)  # 'head' is now the tail of this reversed group
    return prev   # prev is the new head of this reversed group
```

**Complexity**: Time O(n), Space O(n/k) for the recursion stack (or O(1) if written iteratively with explicit group tracking).

**Interview Tip**: This problem combines two patterns you've already learned — bounded reversal (§6.1) + recursive "solve subproblem, attach result" — a very common FAANG "Hard" pattern.

---

### 6.4 Find Middle Node (Fast & Slow Pointer)

**Problem**: Return the middle node of a linked list in one pass.

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

**Visualization** — list `1->2->3->4->5`:
```
Step 0: slow=1, fast=1
Step 1: slow=2, fast=3
Step 2: slow=3, fast=5
Step 3: fast.next is None -> stop
Middle = slow = 3
```

**Why it works**: `fast` moves 2 steps for every 1 step of `slow`. When `fast` reaches the end, `slow` has covered exactly half the distance.

**Complexity**: Time O(n), Space O(1) — vs. the naive two-pass approach (count length, then walk `length//2` steps) which is also O(n) but requires two full traversals rather than one.

**Common Mistake**: For **even-length** lists, this returns the **second** middle node (e.g., for `1,2,3,4` it returns `3`, not `2`). Clarify with your interviewer which middle is expected, or adjust the fast pointer's starting offset.

---

### 6.5 Detect Cycle (Floyd's Tortoise and Hare)

**Problem**: Determine if a linked list has a cycle (a node's `next` eventually points back to a previously visited node).

```
[1] -> [2] -> [3] -> [4]
        ^             |
        +-------------+
```

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

**Why it works (intuition)**: Think of two runners on a circular track — the faster runner (2x speed) *must* eventually lap the slower one if the track is a loop. If there's no loop, `fast` simply reaches `None` and exits.

**Dry Run** on the cyclic list above (`1->2->3->4->2...`):

| Step | slow | fast |
|---|---|---|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 2 (wrapped via cycle) |
| 3 | 4 | 4 → **slow is fast!** cycle confirmed |

**Complexity**: Time O(n), Space O(1) — dramatically better than the naive "store visited nodes in a set" approach, which is O(n) time **and** O(n) space.

---

### 6.6 Find Cycle Start Node

**Problem**: If a cycle exists, return the node where it *begins*.

```python
def detect_cycle_start(head):
    slow = fast = head
    # Phase 1: detect if a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None   # no cycle (loop ended naturally via None)

    # Phase 2: find the entry point
    pointer = head
    while pointer is not slow:
        pointer = pointer.next
        slow = slow.next
    return pointer   # the cycle's starting node
```

**Why Phase 2 works (the math)**: Let `L` = distance from head to cycle start, `C` = cycle length, and the meeting point is `k` steps into the cycle. It can be proven that `L == C - k` (mod C). So moving one pointer from `head` and another from the `meeting point`, both at speed 1, they meet exactly at the cycle's start.

```
head ----L----> [cycle start] ----k----> [meeting point]
                     ^_________ C - k _______|  (rest of cycle back to start)
```

**Complexity**: Time O(n), Space O(1).

**Interview Tip**: This is a classic "prove it" follow-up after Floyd's cycle detection — be ready to explain the math, not just recite the code.

---

### 6.7 Remove Cycle

**Problem**: Given a list with a cycle, break it (make the last node's `next` = `None`).

```python
def remove_cycle(head):
    start = detect_cycle_start(head)
    if start is None:
        return head   # no cycle
    current = start
    while current.next is not start:
        current = current.next
    current.next = None
    return head
```

**Complexity**: Time O(n), Space O(1).

---

### 6.8 Merge Two Sorted Lists

**Problem**: Merge two sorted linked lists into one sorted list.

```
List A: 1 -> 3 -> 5
List B: 2 -> 4 -> 6
Result: 1 -> 2 -> 3 -> 4 -> 5 -> 6
```

```python
def merge_two_sorted(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2   # attach the remaining tail directly (no need to loop)
    return dummy.next
```

**Dry Run:**

| Step | l1 | l2 | Chosen | Merged so far |
|---|---|---|---|---|
| 1 | 1 | 2 | 1 | 1 |
| 2 | 3 | 2 | 2 | 1->2 |
| 3 | 3 | 4 | 3 | 1->2->3 |
| 4 | 5 | 4 | 4 | 1->2->3->4 |
| 5 | 5 | 6 | 5 | 1->2->3->4->5 |
| 6 | None | 6 | attach remaining l2 | 1->2->3->4->5->6 |

**Complexity**: Time O(n + m), Space O(1) (we relink existing nodes, no new ones created — a "merge in place").

**Recursive version:**
```python
def merge_two_sorted_recursive(l1, l2):
    if l1 is None: return l2
    if l2 is None: return l1
    if l1.val <= l2.val:
        l1.next = merge_two_sorted_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_recursive(l1, l2.next)
        return l2
```
Space O(n+m) due to recursion stack — iterative preferred for large lists.

---

### 6.9 Merge K Sorted Lists

**Problem**: Merge `k` sorted linked lists into one.

**Approach 1 — Divide and Conquer (pair up lists, like merge sort):**
```python
def merge_k_lists(lists):
    if not lists:
        return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two_sorted(l1, l2))
        lists = merged
    return lists[0]
```

**Approach 2 — Min-Heap (better when k is large):**
```python
import heapq

def merge_k_lists_heap(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))  # 'i' breaks ties (Node isn't comparable)

    dummy = Node(0)
    tail = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

| Approach | Time | Space | When to Use |
|---|---|---|---|
| Divide & Conquer | O(N log k) | O(1) extra (in-place relinking) | Best general-purpose choice |
| Min-Heap | O(N log k) | O(k) for the heap | Simpler to reason about; good when lists arrive as a stream |
| Brute Force (collect all, sort) | O(N log N) | O(N) | Never preferred — ignores that inputs are already sorted |

`N` = total number of nodes across all lists.

**Common Mistake**: Pushing raw `Node` objects into a heap without a tie-breaker (`i`) — Python will try to compare `Node` objects directly on ties and raise `TypeError` since `Node` has no `__lt__`.

---

### 6.10 Sort a Linked List (Merge Sort)

**Problem**: Sort a linked list in O(n log n) time, O(1) extra space (excluding recursion stack).

**Why Merge Sort (not Quick Sort or Insertion Sort)?** Merge sort doesn't need random access — it only needs sequential splitting and merging, both of which linked lists support naturally. Quick sort's partitioning benefits from random access (arrays); insertion sort is O(n²).

```python
def sort_list(head):
    if head is None or head.next is None:
        return head

    # Split into halves using fast/slow
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None    # cut the list into two halves

    left = sort_list(head)
    right = sort_list(mid)
    return merge_two_sorted(left, right)
```

**Visualization:**
```
        [4,2,1,3]
        /        \
    [4,2]       [1,3]
    /   \        /   \
  [4]   [2]    [1]   [3]
    \   /        \   /
    [2,4]        [1,3]
        \        /
        [1,2,3,4]
```

**Complexity**: Time O(n log n), Space O(log n) (recursion stack only — no auxiliary arrays needed, unlike array merge sort's O(n) buffer).

---

### 6.11 Remove Duplicates

**From a SORTED list:**
```python
def remove_duplicates_sorted(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next   # skip the duplicate
        else:
            current = current.next
    return head
```
Time O(n), Space O(1).

**From an UNSORTED list (using a set):**
```python
def remove_duplicates_unsorted(head):
    seen = set()
    dummy = Node(0, head)
    prev, current = dummy, head
    while current:
        if current.val in seen:
            prev.next = current.next   # skip duplicate
        else:
            seen.add(current.val)
            prev = current
        current = current.next
    return dummy.next
```
Time O(n), Space O(n) for the `seen` set.

**Follow-up (no extra space, O(n²) time)**: For each node, scan forward and remove all matching values — a classic time/space trade-off interview follow-up.

---

### 6.12 Remove N-th Node From End (One Pass)

**Problem**: Remove the `n`-th node from the end in a single traversal.

```python
def remove_nth_from_end(head, n):
    dummy = Node(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next          # advance fast n steps first
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next    # slow is now just BEFORE the target
    return dummy.next
```

**Visualization** — remove 2nd-from-end of `1->2->3->4->5`, n=2:
```
dummy->1->2->3->4->5
fast advances 2: fast at node 2
Then both move together until fast.next is None:
  fast=2->3->4->5(fast.next=None stop when fast=5)
  slow moves in lockstep from dummy: dummy->1->2->3 (slow lands on 3)
slow.next(=4) becomes slow.next.next(=5)
Result: 1->2->3->5
```

**Why the dummy node?** Without it, removing the actual head (n == length) would need a special case.

**Complexity**: Time O(L) (one pass, L = length), Space O(1). Beats the naive two-pass (find length, then walk to position) — still O(L) but with two traversals instead of one.

---

### 6.13 Rotate List

**Problem**: Rotate the list to the right by `k` places.

```
Input: 1->2->3->4->5, k=2
Output: 4->5->1->2->3
```

```python
def rotate_right(head, k):
    if not head or not head.next:
        return head

    # Step 1: find length and connect tail to head (make it circular temporarily)
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    tail.next = head   # temporarily circular

    # Step 2: find new tail = (length - k % length - 1)-th node from head
    k %= length
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None   # break the circle
    return new_head
```

**Why make it circular first?** It lets us find the new "break point" with simple arithmetic instead of juggling multiple traversals, then we cut it back open.

**Complexity**: Time O(n), Space O(1). **Edge case**: `k % length == 0` means no rotation is needed — the loop naturally handles this since `steps_to_new_tail == length`.

---

### 6.14 Reorder List

**Problem**: Reorder `L0 -> L1 -> ... -> Ln` into `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`

```
Input: 1->2->3->4->5
Output: 1->5->2->4->3
```

**Approach**: (1) find middle, (2) reverse second half, (3) merge alternately.

```python
def reorder_list(head):
    if not head or not head.next:
        return

    # Step 1: find middle (first middle for odd/even split)
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half
    second = slow.next
    slow.next = None
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev   # head of reversed second half

    # Step 3: merge two halves alternately
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
```

**Complexity**: Time O(n), Space O(1) — combines three patterns you already know (§6.4 middle-finding, §6.1 reversal, alternating merge).

---

### 6.15 Odd-Even Linked List

**Problem**: Group all odd-indexed nodes together, followed by even-indexed nodes (1-indexed by position, not value).

```
Input:  1->2->3->4->5
Output: 1->3->5->2->4
```

```python
def odd_even_list(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head   # attach even chain after odd chain
    return head
```

**Complexity**: Time O(n), Space O(1) — no new nodes created, just relinked.

---

### 6.16 Partition List

**Problem**: Partition a list around value `x` so all nodes `< x` come before nodes `>= x`, preserving relative order.

```
Input: 1->4->3->2->5->2, x=3
Output: 1->2->2->4->3->5
```

```python
def partition(head, x):
    less_dummy = Node(0)
    greater_dummy = Node(0)
    less_tail, greater_tail = less_dummy, greater_dummy

    current = head
    while current:
        if current.val < x:
            less_tail.next = current
            less_tail = less_tail.next
        else:
            greater_tail.next = current
            greater_tail = greater_tail.next
        current = current.next

    greater_tail.next = None       # IMPORTANT: terminate to avoid an accidental cycle
    less_tail.next = greater_dummy.next
    return less_dummy.next
```

**Common Mistake**: Forgetting `greater_tail.next = None` — since original nodes are being reused/relinked, the last node in the ">=" chain might still point at a node that's now in the "<" chain, silently creating a cycle.

**Complexity**: Time O(n), Space O(1) (two dummy heads, no new value-nodes).

---

### 6.17 Swap Nodes in Pairs

**Problem**: Swap every two adjacent nodes.

```
Input: 1->2->3->4
Output: 2->1->4->3
```

```python
def swap_pairs(head):
    dummy = Node(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first     # 'first' is now in the second position of this swapped pair
    return dummy.next
```

**Visualization:**
```
prev -> [1] -> [2] -> [3]
Step 1: first=1, second=2
        first.next = second.next(=3)  ->  1 -> 3
        second.next = first            ->  2 -> 1
        prev.next = second             -> prev -> 2 -> 1 -> 3
```

**Complexity**: Time O(n), Space O(1).

---

### 6.18 Intersection of Two Linked Lists

**Problem**: Find the node at which two singly linked lists intersect (by reference, not value).

```
A: a1 -> a2
              \
               c1 -> c2 -> c3
              /
B: b1 -> b2 -> b3
```

**Elegant Two-Pointer Approach** (no length calculation needed):

```python
def get_intersection_node(headA, headB):
    p1, p2 = headA, headB
    while p1 is not p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1   # either the intersection node, or None (if both hit None together)
```

**Why this works**: `p1` travels `A` then `B` (`lenA + lenB` total steps to reach intersection); `p2` travels `B` then `A` (`lenB + lenA` steps). Both cover the *same total distance* before reaching the intersection point, so they arrive there simultaneously — like two people walking each other's routes, meeting exactly at the fork.

**Complexity**: Time O(n + m), Space O(1) — superior to the naive hash-set approach (O(n+m) time, O(n) space).

---

### 6.19 Palindrome Linked List

**Problem**: Check if a linked list reads the same forward and backward.

```python
def is_palindrome(head):
    if not head or not head.next:
        return True

    # Step 1: find middle
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half
    prev = None
    current = slow.next
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    # Step 3: compare both halves
    first, second = head, prev
    result = True
    while second:
        if first.val != second.val:
            result = False
            break
        first, second = first.next, second.next

    # Step 4 (best practice): restore the list to its original shape
    current = prev
    prev2 = None
    while current:
        nxt = current.next
        current.next = prev2
        prev2 = current
        current = nxt
    slow.next = prev2

    return result
```

**Complexity**: Time O(n), Space O(1) — vs the naive approach (copy values into a Python list, check `lst == lst[::-1]`), which is O(n) time but O(n) space.

> 📝 **Note**: Restoring the list (Step 4) is good practice in production code / when the interviewer asks you not to mutate input permanently — but is often skipped in quick interview answers if not required.

---

### 6.20 Add Two Numbers (Represented as Linked Lists)

**Problem**: Each list represents a non-negative integer, digits stored in **reverse order** (ones digit first). Add the two numbers and return the sum as a linked list in the same format.

```
Input: (2->4->3) + (5->6->4)   [i.e., 342 + 465]
Output: 7->0->8                 [i.e., 807]
```

```python
def add_two_numbers(l1, l2):
    dummy = Node(0)
    tail = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry, digit = divmod(total, 10)
        tail.next = Node(digit)
        tail = tail.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
```

**Dry Run** — `2->4->3` + `5->6->4`:

| Step | v1 | v2 | carry(in) | total | digit | carry(out) |
|---|---|---|---|---|---|---|
| 1 | 2 | 5 | 0 | 7 | 7 | 0 |
| 2 | 4 | 6 | 0 | 10 | 0 | 1 |
| 3 | 3 | 4 | 1 | 8 | 8 | 0 |

Result: `7 -> 0 -> 8` ✅

**Complexity**: Time O(max(n, m)), Space O(max(n, m)) for the output list.

**Variation — digits stored in FORWARD order** (most significant digit first): reverse both lists first (§6.1), add as above, then reverse the result — or use two stacks to process from the least-significant digit without mutating input order.

---

### 6.21 Copy List with Random Pointer

**Problem**: Each node has a `next` pointer **and** a `random` pointer that can point to *any* node in the list (or `None`). Deep-copy the entire structure.

```
Original:  [1]---random--->[3]
            |next            |next
            v                v
           [2]<---random----[3]... etc.
```

**Approach 1 — Hash Map (O(n) time, O(n) space):**
```python
class RNode:
    def __init__(self, val, next=None, random=None):
        self.val, self.next, self.random = val, next, random

def copy_random_list_hashmap(head):
    if not head:
        return None
    old_to_new = {}
    current = head
    while current:
        old_to_new[current] = RNode(current.val)
        current = current.next
    current = head
    while current:
        old_to_new[current].next = old_to_new.get(current.next)
        old_to_new[current].random = old_to_new.get(current.random)
        current = current.next
    return old_to_new[head]
```

**Approach 2 — O(1) Space (Interleaving Trick):**
```python
def copy_random_list_optimal(head):
    if not head:
        return None

    # Step 1: interleave copied nodes: A -> A' -> B -> B' -> C -> C'
    current = head
    while current:
        copy = RNode(current.val, current.next)
        current.next = copy
        current = copy.next

    # Step 2: assign random pointers using the interleaving
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next   # copy's random = original's random's copy
        current = current.next.next

    # Step 3: un-interleave (restore original + extract copy)
    current = head
    dummy = RNode(0)
    copy_tail = dummy
    while current:
        copy = current.next
        current.next = copy.next   # restore original list
        copy_tail.next = copy
        copy_tail = copy
        current = current.next
    return dummy.next
```

**Visualization of interleaving:**
```
Before: [A]->[B]->[C]->None
After interleaving: [A]->[A']->[B]->[B']->[C]->[C']->None
```
Because each copy sits immediately after its original, `original.random.next` is always exactly `copy_of(original.random)` — this is the key insight that avoids a hash map.

**Complexity Comparison:**

| Approach | Time | Space |
|---|---|---|
| Hash Map | O(n) | O(n) |
| Interleaving | O(n) | **O(1)** extra (excluding output) |

**Interview Tip**: Start with the hash map approach (easy to explain correctly), then mention the O(1)-space interleaving trick as an optimization if asked.

---

### 6.22 Flatten a Multilevel Doubly Linked List

**Problem**: Each node may have a `child` pointer to a separate doubly linked list. Flatten it into a single-level DLL.

```
1 - 2 - 3 - 4 - 5
        |
        7 - 8 - 9
            |
            10-11

Flattened: 1-2-3-7-8-10-11-9-4-5
```

```python
class MNode:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val, self.prev, self.next, self.child = val, prev, next, child

def flatten(head):
    if not head:
        return head
    current = head
    while current:
        if current.child:
            next_node = current.next
            child_head = current.child

            current.next = child_head     # attach child right after current
            child_head.prev = current
            current.child = None          # remove the child pointer (now merged)

            # find tail of the child list to reconnect with next_node
            tail = child_head
            while tail.next:
                tail = tail.next
            tail.next = next_node
            if next_node:
                next_node.prev = tail
        current = current.next
    return head
```

**Why iterative "current = current.next" still visits the newly-inserted child nodes?** Because we spliced the child list *in place* right where `current.next` used to be — the traversal naturally flows into it next.

**Complexity**: Time O(n) total across all nodes (each node visited once, tail-finding amortizes across the whole structure), Space O(1) (excluding recursion if you choose a recursive variant, which would use O(depth) stack space).

---

### 6.23 LRU Cache (Linked-List Perspective)

**Problem**: Design a cache with O(1) `get` and `put`, evicting the **Least Recently Used** item when capacity is exceeded.

**Why a Doubly Linked List + Hash Map?**
- The hash map gives O(1) lookup of a node by key.
- The DLL gives O(1) removal/insertion at *any* position (no shifting like an array/list would require), and lets us maintain **recency order**: most-recently-used at one end, least-recently-used at the other.

```python
class DLLNode:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}                    # key -> DLLNode
        self.head = DLLNode()              # dummy head (most-recently-used side)
        self.tail = DLLNode()              # dummy tail (least-recently-used side)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_at_front(node)   # mark as most-recently-used
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = DLLNode(key, value)
        self.cache[key] = node
        self._insert_at_front(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev            # least-recently-used node
            self._remove(lru)
            del self.cache[lru.key]
```

**Complexity**: `get` and `put` are both O(1) time, O(capacity) space.

> 💡 **Interview Tip**: This is one of the most frequently asked "design" questions at FAANG companies. The key insight to articulate out loud: *"I need O(1) lookup → hash map. I need O(1) reordering without shifting → doubly linked list with dummy head/tail sentinels to avoid null-checks."*


---

## 7. POINTER PATTERNS

This section distills every algorithm above into **reusable templates**. Memorize these shapes — nearly every linked list interview question is a combination of 2-3 of them.

### 7.1 Fast & Slow Pointer (Tortoise and Hare)

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is now at the middle (or meeting point in cycle detection)
```

**Used for**: middle-finding (§6.4), cycle detection (§6.5, §6.6), palindrome check (§6.19), reorder list (§6.14), splitting (§5.17).

```
slow: 1 step/iteration     [S]
fast: 2 steps/iteration    [F....F]
When fast reaches the end, slow is at the midpoint.
```

### 7.2 Two Pointer (Offset / Gap Pattern)

```python
fast = head
for _ in range(n):
    fast = fast.next     # give 'fast' a head start of n nodes

slow = head
while fast:
    slow = slow.next
    fast = fast.next
# slow is now n nodes from the end
```

**Used for**: Remove N-th from end (§6.12), finding intersection (§6.18 — a variant where both pointers eventually traverse both lists).

### 7.3 Dummy Node Pattern

```python
dummy = Node(0, head)
prev = dummy
# ... perform operations using 'prev' and 'prev.next' ...
return dummy.next   # new head, safe even if original head changed
```

**Used for**: virtually every insertion/deletion algorithm where the head itself might change (§3.6, §6.2, §6.9, §6.12, §6.16, §6.17).

**Golden Rule**: *If the head could be removed or replaced, use a dummy node.*

### 7.4 Prev-Current-Next (The Reversal Triplet)

```python
prev, current = None, head
while current:
    nxt = current.next     # 1. remember what's ahead
    current.next = prev    # 2. rewire backward
    prev, current = current, nxt   # 3. slide the whole window forward
```

**Used for**: reverse (§6.1), reverse between (§6.2), reverse k-group (§6.3).

```
     prev   current   next
      |        |        |
      v        v        v
[None]      [10]------>[20]------>[30]
```

### 7.5 Multiple Pointer Manipulation

Some problems require tracking **3 or more** pointers simultaneously (e.g., odd-even list needs `odd`, `even`, `even_head`; swap pairs needs `prev`, `first`, `second`). The discipline is always the same:

1. **Save** every pointer you're about to overwrite into a local variable *before* you overwrite anything.
2. **Rewire** in an order that never strands a piece of the list.
3. **Advance** all tracking pointers together at the end of the iteration.

### 7.6 Head Insertion Pattern

```python
new_node.next = head
head = new_node
```
O(1) — always insert at the front when order doesn't matter (e.g., building a list from a stream where you'll reverse or sort later) since it avoids tail-tracking.

### 7.7 Tail Insertion Pattern

```python
tail.next = new_node
tail = new_node
```
Requires tracking `tail` explicitly (§2.3) for O(1); otherwise O(n) per insertion.

### 7.8 Merge Pattern (Two-Pointer Zipper)

```python
dummy = Node(0)
tail = dummy
while l1 and l2:
    if l1.val <= l2.val:
        tail.next, l1 = l1, l1.next
    else:
        tail.next, l2 = l2, l2.next
    tail = tail.next
tail.next = l1 or l2
```
**Used for**: merge two sorted lists (§6.8), reorder list's final merge step (§6.14).

### 7.9 Split Pattern

```python
slow, fast = head, head.next
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
second_half = slow.next
slow.next = None
```
**Used for**: merge sort (§6.10), reorder list (§6.14).

### Pattern Selection Cheat Table

| Symptom in Problem Statement | Pattern to Reach For |
|---|---|
| "middle of the list" | Fast & Slow (§7.1) |
| "has a cycle" / "loop" | Fast & Slow (§7.1) |
| "n-th node from the end" | Two Pointer Gap (§7.2) |
| "the head node might change" | Dummy Node (§7.3) |
| "reverse" (fully or partially) | Prev-Current-Next (§7.4) |
| "merge two/many sorted lists" | Merge Pattern (§7.8) |
| "split / divide the list" | Split Pattern (§7.9) |
| "group odd/even, or partition" | Multiple Pointers (§7.5) |

---

## 8. ADVANCED LINKED LIST CONCEPTS

### 8.1 Sentinel Nodes — Beyond Dummy Heads

Sentinels can also be placed at the **tail** to avoid checking `if node.next is None` everywhere:

```python
TAIL_SENTINEL = Node(None)   # a permanent marker for "end of list"
```

In circular buffer/skip-list implementations, sentinels frequently exist as **permanent** structural fixtures, not throwaway locals (contrast with the temporary `dummy` used in §3.6 — that pattern's cousin, made permanent, is the "header linked list" from §4.5).

### 8.2 Random Pointer Structures — General Principle

Whenever a data structure has more than one type of link (`next` + `random`, or `next` + `child`), the safe general strategy is:

1. First, resolve/copy the **primary structural link** (`next`).
2. Then, resolve the **auxiliary link** using a mapping (hash map) or an interleaving trick (§6.21).

### 8.3 Circular Operations — Extra Care Points

| Operation | Extra Care Needed |
|---|---|
| Traversal | Must terminate on `node is head`, not `node is None` |
| Insertion | Must correctly re-link `tail.next` to still point at `head` |
| Deletion | If deleting `head` itself, must update the *old tail's* `next` pointer to the *new* head |
| Length | Same termination care as traversal |

### 8.4 Merge Sort on Linked Lists — Why It's the Canonical Sort

- No random access needed (unlike quicksort's partitioning, which is much more natural on arrays).
- No auxiliary array needed for merging (as opposed to array-based merge sort, which typically needs O(n) extra buffer) — nodes are simply **relinked**.
- Stable sort — equal elements retain their relative order, an often-overlooked interview follow-up question.

### 8.5 Flattening — General Pattern Recap

Flattening problems (multilevel lists, nested structures) generally reduce to: *depth-first splice each child list in at the point of its parent, then continue traversal linearly.* See full solution at §6.22.

### 8.6 Memory Optimization Techniques

- `__slots__` on node classes (§2.7) — avoids per-instance `__dict__`, meaningfully reduces memory for lists with millions of nodes.
- Reuse existing nodes via relinking instead of creating new ones wherever the algorithm allows (e.g., merge, partition, reverse all relink instead of copying).
- Avoid unnecessary auxiliary data structures (arrays/sets) when an O(1)-space pointer trick exists (e.g., prefer Floyd's cycle detection over a `visited` set).

### 8.7 Persistent Linked List (Overview)

A **persistent** (immutable) linked list never mutates existing nodes — every "modification" creates new nodes for the changed portion while **sharing** the unchanged tail with the original structure. This is the backbone of functional languages (Lisp/Haskell/Clojure `cons` cells) and Python's own immutable `tuple`-based linked structures used in some parser/AST implementations.

```python
class PersistentNode:
    __slots__ = ("val", "next")
    def __init__(self, val, next=None):
        self.val, self.next = val, next   # never mutated after creation

def persistent_push_front(head, val):
    return PersistentNode(val, head)   # O(1) — old list is untouched and still valid!
```

```
Original: A -> B -> C
push_front(A->B->C, X):
New:      X -> A -> B -> C
Original (A->B->C) is STILL VALID and unmodified — both lists coexist, sharing A,B,C.
```

**Why this matters**: enables cheap "snapshots" / undo history without copying the entire structure — directly relevant to the Undo/Redo application in §9.


---

## 9. APPLICATIONS

### 9.1 Undo/Redo

A doubly linked list (or two stacks) tracks states. The "current" pointer moves `prev` on Undo and `next` on Redo — new actions truncate the "redo" branch by cutting `current.next = None` before appending a new state.

### 9.2 Browser History

```
Back <- [Page1] <-> [Page2] <-> [Page3] -> Forward
                        ^current
```
`prev` pointer = "Back" button, `next` pointer = "Forward" button. Visiting a *new* page from the middle of history truncates everything ahead (classic browser behavior) — same pattern as Undo/Redo.

### 9.3 Music Playlist

A **circular doubly linked list** models "repeat all" mode naturally — `next` from the last song loops to the first, `prev` from the first loops to the last. Shuffle can be implemented by randomizing the link order without touching song data.

### 9.4 LRU Cache

Covered in full at §6.23 — doubly linked list + hash map combo.

### 9.5 Hash Table Chaining

When multiple keys hash to the same bucket (a collision), most hash table implementations store colliding entries as a **singly linked list** hanging off that bucket:

```
bucket[3] -> [key="foo", val=1] -> [key="bar", val=2] -> None
```

Python's own `dict` uses open addressing internally rather than chaining, but many textbook/from-scratch hash table implementations (and Java's `HashMap` pre-treeification) use exactly this pattern.

### 9.6 File Systems

Some file systems represent a file's data blocks as a linked list of blocks-on-disk (each block storing a pointer to the next block's disk address) — this is the classic **linked allocation** strategy in OS textbooks, as opposed to contiguous or indexed allocation.

### 9.7 Memory Management

Operating systems and language runtimes track **free memory blocks** using a linked list (the "free list") — when memory is freed, the block is pushed onto this list; when new memory is requested, the allocator searches/pops from this list. CPython's own `pymalloc` uses free-lists for small object allocation internally.

### 9.8 Scheduling (Round-Robin)

A **circular linked list** naturally models round-robin CPU scheduling — after servicing the last process in the queue, the scheduler pointer wraps back to the first.

### 9.9 Graph Adjacency Lists

Representing a graph's adjacency list as an array of linked lists (`adj[v]` = linked list of `v`'s neighbors) is the standard sparse-graph representation, giving O(1) edge insertion and O(degree(v)) neighbor iteration — much better than an O(V²) adjacency matrix for sparse graphs.

```
adj[0] -> 1 -> 3 -> None
adj[1] -> 0 -> 2 -> None
adj[2] -> 1 -> None
adj[3] -> 0 -> None
```

---

## 10. PROBLEM RECOGNITION

### 10.1 Master Recognition Flowchart

```
                    "Linked list problem"
                            |
             +--------------+--------------+
             |                             |
      Mentions cycle/loop?          No cycle mentioned
             |                             |
            YES                    +-------+--------+
             |                     |                |
    Use Fast & Slow (§7.1)   Needs middle?    Needs to reverse
    (§6.5, §6.6, §6.7)             |           all/part of list?
                                  YES                |
                             Fast & Slow (§7.1)      YES
                             (§6.4)          Prev-Current-Next (§7.4)
                                                (§6.1, §6.2, §6.3)
                                                      |
                                              +-------+--------+
                                              |                |
                                     Merging 2+ lists?   Head might change
                                              |          (insert/delete)?
                                             YES                |
                                     Merge Pattern (§7.8)       YES
                                     (§6.8, §6.9)         Dummy Node (§7.3)
                                                          (§6.2, §6.9, §6.12...)
```

### 10.2 Interview Clue Table

| Keyword / Phrase in the Prompt | Likely Pattern |
|---|---|
| "detect a cycle", "has a loop" | Fast & Slow Pointer |
| "find the middle" | Fast & Slow Pointer |
| "k-th from the end", "n-th node from end" | Two Pointer Gap |
| "reverse", "reverse between", "reverse in groups" | Prev-Current-Next |
| "merge k sorted lists" | Divide & Conquer / Min-Heap |
| "sort the list" | Merge Sort (split + merge patterns) |
| "in-place", "O(1) space", "without extra memory" | Pointer manipulation, no auxiliary array/set |
| "the head node may be removed" | Dummy Node |
| "random pointer" | Hash map or interleaving trick |
| "child pointer", "multilevel", "flatten" | Depth-first splice |
| "palindrome" | Fast/Slow (middle) + Reversal + Compare |
| "intersection of two lists" | Two-pointer switch-lists trick |
| "LRU", "recently used" | Doubly Linked List + Hash Map |
| "rotate the list" | Circular trick + arithmetic cut point |

### 10.3 Fast & Slow Pointer Recognition Checklist

Ask yourself:
- Do I need the **middle** of the list? → Fast & Slow.
- Could the list **loop back on itself**? → Fast & Slow.
- Do I need something at a relative **position from the end**, not a cycle/middle? → That's actually the *Two Pointer Gap* variant, not Fast & Slow — don't confuse them.

### 10.4 Dummy Node Recognition Checklist

Ask yourself:
- Could my operation **delete or replace the very first node**?
- Am I **building a new list from scratch** by appending (§5.1)?
- Would I otherwise need an `if is_head: ... else: ...` branch?

If yes to any — use a dummy node. It's *always* safe to add one, even when not strictly required — it costs O(1) extra space and simplifies code.

### 10.5 Reversal Recognition Checklist

- The word "reverse" appears explicitly (most obvious).
- You need to **compare a list against itself in reverse** (palindrome, §6.19).
- You need to process nodes in **reverse order without extra space** (e.g., adding numbers stored in forward-digit-order, without a stack).

### 10.6 Merge Recognition Checklist

- Two or more **already-sorted** lists need to be combined into one sorted list.
- You need to **interleave** two lists (reorder list, §6.14; odd-even list, §6.15).

---

## 11. OPTIMIZATION

### 11.1 Brute Force → Optimal Pointer Manipulation

| Problem | Brute Force | Optimal |
|---|---|---|
| Detect Cycle | Hash set of visited nodes — O(n) space | Floyd's Fast/Slow — O(1) space |
| Find Middle | Two passes (count then walk) — 2 traversals | Fast/Slow — 1 traversal |
| N-th from End | Two passes (count then walk) | Two-Pointer Gap — 1 traversal |
| Palindrome Check | Copy to array, compare reversed — O(n) space | Reverse second half in place — O(1) space |
| Copy Random List | Hash map — O(n) space | Interleaving trick — O(1) extra space |
| Merge K Lists | Concatenate all + sort — O(N log N) | Divide & Conquer / Heap — O(N log k) |

### 11.2 Dummy Node Optimization

Removing special-case branches with a dummy node doesn't just simplify code — it also often **removes redundant conditional checks per iteration**, giving a minor constant-factor speedup in addition to code clarity.

### 11.3 Space Optimization Principles

1. **Relink instead of recreate** — mutate existing node pointers rather than allocating new `Node` objects whenever the problem allows in-place modification.
2. **Use O(1)-space pointer tricks** in place of hash sets/maps wherever a mathematical relationship (like Floyd's algorithm) exists.
3. **Use `__slots__`** to cut per-node memory overhead at scale.

### 11.4 One-Pass Solutions

Many "two-pass" naive solutions (compute length first, then act) can be collapsed into **one pass** using the two-pointer gap technique (§7.2) — this is a favorite "can you optimize further?" interview follow-up.

### 11.5 Time Optimization Principles

- Prefer **iterative** over recursive implementations for large inputs — avoids O(n) call-stack space and Python's recursion limit (~1000 by default).
- Prefer a **single well-chosen pass** with multiple pointers over multiple simple passes when both are O(n) — same asymptotic complexity, but fewer constant-factor operations and better cache behavior.


---

## 12. INTERVIEW PREPARATION

### 12.1 Difficulty-Based Roadmap

**Easy** (build muscle memory):
- Reverse Linked List (§6.1)
- Merge Two Sorted Lists (§6.8)
- Middle of the Linked List (§6.4)
- Linked List Cycle (§6.5)
- Palindrome Linked List (§6.19)
- Remove Duplicates from Sorted List (§6.11)
- Delete Node in a Linked List (given only that node, no head — swap value trick)
- Intersection of Two Linked Lists (§6.18)

**Medium** (combine 2 patterns):
- Add Two Numbers (§6.20)
- Remove Nth Node From End (§6.12)
- Odd Even Linked List (§6.15)
- Reorder List (§6.14)
- Rotate List (§6.13)
- Partition List (§6.16)
- Swap Nodes in Pairs (§6.17)
- Copy List with Random Pointer (§6.21)
- Sort List (§6.10)
- Reverse Linked List II / Reverse Between (§6.2)
- Linked List Cycle II / Find Cycle Start (§6.6)
- Flatten a Multilevel Doubly Linked List (§6.22)
- LRU Cache (§6.23)

**Hard** (multi-pattern, careful edge cases):
- Merge K Sorted Lists (§6.9)
- Reverse Nodes in K-Group (§6.3)
- LFU Cache (LRU Cache extended with frequency buckets)
- Design Skip List

### 12.2 Pattern-Wise Question Grouping

| Pattern | Representative Problems |
|---|---|
| Fast & Slow Pointer | Middle of List, Cycle Detection, Cycle Start, Palindrome, Reorder List |
| Two Pointer Gap | Remove Nth From End, Intersection of Two Lists |
| Reversal | Reverse List, Reverse Between, Reverse K-Group, Add Two Numbers (forward-digit variant) |
| Dummy Node | Merge Two Lists, Remove Duplicates, Partition List, Remove Nth From End |
| Merge/Split | Merge Two/K Sorted Lists, Sort List, Reorder List |
| Design (DLL + HashMap) | LRU Cache, LFU Cache, Browser History |
| Multi-pointer Structural | Copy Random List, Flatten Multilevel List |

### 12.3 Company-Wise Frequently Asked (General Trends)

> These reflect commonly reported patterns across major tech companies (Google, Amazon, Meta, Microsoft, Apple) rather than any official/current list — always check up-to-date sources like LeetCode's company tag feature (subscription-gated) closer to your interview.

| Company (commonly reported) | Frequently Reported Topics |
|---|---|
| Amazon | Reverse List, Merge K Lists, LRU Cache, Cycle Detection |
| Google | Copy Random List, Flatten Multilevel List, Merge K Lists |
| Meta/Facebook | Add Two Numbers, Reorder List, Palindrome List |
| Microsoft | Reverse List, Remove Nth From End, Intersection of Lists |
| Apple | LRU Cache, Merge Two Sorted Lists |

### 12.4 "Blind 75" / NeetCode Linked List Set

The widely-circulated **Blind 75** and **NeetCode 150** lists both include a dedicated Linked List section, commonly featuring:

- Reverse Linked List
- Linked List Cycle
- Merge Two Sorted Lists
- Merge K Sorted Lists
- Remove Nth Node From End of List
- Reorder List
- Copy List with Random Pointer
- Add Two Numbers
- Find the Duplicate Number (array problem solved *using* Floyd's cycle algorithm — a great cross-topic example!)
- LRU Cache

> 💡 **Tip**: "Find the Duplicate Number" is technically an *array* problem, but it's solved by treating array indices/values as an implicit linked list and running Floyd's cycle detection on it — a favorite "aha" moment interviewers love to probe.

### 12.5 Interview Tricks & Standard Templates

**Template 1 — Safe Traversal Guard:**
```python
current = head
while current:
    ...
    current = current.next
```

**Template 2 — Dummy Node Skeleton (use for ANY insert/delete problem):**
```python
dummy = Node(0, head)
prev = dummy
# mutate using prev / prev.next
return dummy.next
```

**Template 3 — Fast/Slow Skeleton:**
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

**Template 4 — Reversal Skeleton:**
```python
prev, current = None, head
while current:
    nxt = current.next
    current.next = prev
    prev, current = current, nxt
```

**Interview Tricks:**
- Always ask: *"Can the list be empty? Can it have exactly one node? Are values guaranteed unique?"* before coding.
- Draw the list with boxes and arrows on the whiteboard/shared doc *before* writing code — it prevents pointer-order mistakes.
- Narrate your pointer updates out loud in the order you're doing them — interviewers grade communication, not just correctness.
- After coding, **always dry run** on a small example (3-4 nodes) before saying "I'm done."


---

## 13. PYTHON TIPS

### 13.1 `dataclass` for Nodes

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    val: int
    next: Optional["Node"] = None
```
Gives free `__repr__`/`__eq__`; slightly more overhead than a plain `__slots__` class unless combined with `@dataclass(slots=True)` (Python 3.10+):
```python
@dataclass(slots=True)
class Node:
    val: int
    next: Optional["Node"] = None
```

### 13.2 `typing.Optional` for Self-Referential Types

Always type `next` (and `prev`, `child`, `random`) as `Optional[...]` — this documents to both humans and static checkers (`mypy`, `pyright`) that reaching the end of the list (`None`) is an expected, valid state, not an error condition.

### 13.3 Object References — Recap

- Assigning `a = b` where both are `Node` objects makes `a` and `b` **the same object** — mutating one mutates both, as seen via `a is b`.
- Cloning requires **explicitly creating new `Node` objects** with copied `val` fields (§5.14) — never assume `=` performs a deep copy.

### 13.4 `None` Handling Idioms

```python
value = node.val if node else default          # safe attribute access
current = current.next if current else None    # safe chained traversal
```

Avoid deeply nested `if x is not None and x.next is not None:` chains — Python's short-circuit `and`/`or` combined with `if head and head.next:` is idiomatic and readable.

### 13.5 Iterators & Generators for Traversal

```python
class LinkedList:
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
```
This lets you write `for node in my_list:` naturally, and combine with other Python idioms:
```python
values = [node.val for node in my_list]
total = sum(node.val for node in my_list)
```

### 13.6 Performance Tips

- Prefer `collections.deque` (a C-implemented doubly linked list) over hand-rolled Python node classes for **production** use-cases needing O(1) append/pop from both ends — it's significantly faster due to C-level implementation.
- Use `__slots__` (§2.7) for custom node classes at scale.
- Avoid creating unnecessary intermediate Python lists (`list(linked_list)`) when a generator/iterator suffices — saves memory on huge lists.

### 13.7 Memory Optimization Tips

- Explicitly set `node.next = None` on removed nodes if you suspect long-lived stray references elsewhere in your program (helps reference counting reclaim memory immediately, rather than waiting on the cyclic GC — relevant mainly for circular structures, §8.3).
- Avoid deeply recursive implementations (§5.12, recursive reverse) for lists that might have thousands of nodes — recursion depth is limited (`sys.getrecursionlimit()`, default 1000) and each frame consumes stack memory.

### 13.8 Common Python-Specific Pitfalls

| Pitfall | Explanation |
|---|---|
| `if node.next:` vs `if node.next is not None:` | Usually equivalent for `Node` objects (both fail only on `None`), but be careful if `val`/objects define custom `__bool__`/`__len__` — prefer `is None`/`is not None` for pointer checks to be explicit and correct. |
| Comparing nodes with `==` instead of `is` | `==` calls `__eq__` (compares by value, if defined, e.g. via `@dataclass`) while `is` compares object identity. For "is this the SAME node" questions (e.g. cycle detection, intersection), always use `is`. |
| Mutating a list while iterating it incorrectly | E.g., `current.next = current.next.next` while also doing `current = current.next` in the same loop body — advances past a node accidentally. Always be explicit about which pointer you advance and when. |
| Recursion limit errors on long lists | `RecursionError: maximum recursion depth exceeded` — switch to the iterative equivalent. |
| Forgetting `__slots__` causes memory bloat at scale | A plain class instance carries a `__dict__` (typically ~296+ bytes) per node — devastating for lists with millions of nodes. |


---

## 14. COMMON MISTAKES

### 14.1 Losing the Head Pointer

```python
# WRONG:
while head:
    print(head.val)
    head = head.next
# head is now None — the entire list reference is GONE if you needed it again!
```
**Fix**: Always traverse with a *separate* variable (`current = head`), never overwrite `head` itself unless you intentionally mean to return a new head.

### 14.2 Losing the Next Pointer Mid-Mutation

```python
# WRONG (in reversal):
current.next = prev   # overwritten BEFORE saving the old next!
nxt = current.next     # this is now 'prev', not the real next — list is broken
```
**Fix**: Always capture `nxt = current.next` **before** any reassignment of `current.next` (§6.1, §7.4).

### 14.3 Incorrect Pointer Update Order

In multi-pointer rewiring (DLL insertion, §4.2; swap pairs, §6.17), updating pointers in the wrong order can strand or duplicate parts of the list. **Fix**: Save every "old" pointer you'll need into a local variable *before* doing any writes, then write in an order that never depends on an already-overwritten value.

### 14.4 Null Reference Errors

```python
# WRONG:
current.next.next   # crashes if current.next is None
```
**Fix**: Always guard multi-hop pointer chains: `if current.next and current.next.next:`.

### 14.5 Accidental Cycle Creation

```python
# WRONG (common in partition/relinking problems, §6.16):
greater_tail.next = None   # <-- forgetting this line can leave a stale pointer
                            #     from an old traversal, silently creating a cycle
```
**Fix**: Whenever you relink existing nodes rather than creating new ones, explicitly terminate the new tail's `next` to `None`.

### 14.6 Infinite Loops

- Forgetting to advance a pointer inside a `while` loop.
- Traversing a circular list with `while current:` instead of `while current is not head:` (§4.3, §8.3).
- An accidentally created cycle (§14.5) turning an otherwise-terminating traversal into an infinite one.

### 14.7 Dummy Node Misuse

- Forgetting to return `dummy.next` (returning `dummy` itself, or the original `head` which may be stale) — a very common submission bug.
- Using `dummy = head` instead of `dummy = Node(0, head)` — this doesn't create a real sentinel, it just aliases the original head, defeating the purpose.

### 14.8 Edge Case Failures

Always explicitly test your solution against:

| Edge Case | Why It Matters |
|---|---|
| Empty list (`head is None`) | Many operations assume at least one node exists |
| Single node list | "prev"/"next" neighbors may not exist — breaks naive 2-pointer logic |
| Two node list | Boundary for swap/reverse-pair algorithms |
| All values identical | Breaks naive "find by value" assumptions; relevant for duplicate-removal |
| List with a cycle (when not expected) | Can cause infinite loops in naive traversal-based solutions |
| Very long list (1000+ nodes) | Surfaces `RecursionError` in recursive solutions |

> ⚠️ **Warning**: The single most common reason a *correct-looking* linked list solution fails on a judge (LeetCode/HackerRank) is an untested edge case — especially the empty list and single-node list. Always dry-run these two first.


---

## 15. CHEAT SHEETS

### 15.1 Linked List Templates (Quick Copy-Paste)

```python
# --- Node Definition ---
class Node:
    __slots__ = ("val", "next")
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# --- Traverse ---
current = head
while current:
    current = current.next

# --- Dummy Node Skeleton ---
dummy = Node(0, head)
prev = dummy
return dummy.next

# --- Fast & Slow ---
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next

# --- Reversal ---
prev, current = None, head
while current:
    nxt = current.next
    current.next = prev
    prev, current = current, nxt
return prev

# --- Merge Two Sorted ---
dummy = Node(0)
tail = dummy
while l1 and l2:
    if l1.val <= l2.val:
        tail.next, l1 = l1, l1.next
    else:
        tail.next, l2 = l2, l2.next
    tail = tail.next
tail.next = l1 or l2
return dummy.next
```

### 15.2 Pointer Patterns Quick Reference

| Pattern | One-Line Summary |
|---|---|
| Fast & Slow | 2x speed pointer finds middle / detects cycles in O(n)/O(1) |
| Two Pointer Gap | Offset one pointer by `n` to find position from the end |
| Dummy Node | Fake head eliminates head-mutation special cases |
| Prev-Current-Next | Save `next` before rewiring `current.next` backward |
| Merge (Zipper) | Compare heads of two lists, attach smaller, advance |
| Split | Fast/slow to find midpoint, then cut `slow.next = None` |

### 15.3 Complexity Table (All Core Operations)

| Operation | Singly LL | Doubly LL | Array (for comparison) |
|---|---|---|---|
| Access by index | O(n) | O(n) | O(1) |
| Search by value | O(n) | O(n) | O(n) |
| Insert at head | O(1) | O(1) | O(n) (shift) |
| Insert at tail (tail tracked) | O(1) | O(1) | O(1) amortized |
| Insert at tail (no tail ptr) | O(n) | O(n) | O(1) amortized |
| Insert at middle | O(n) find + O(1) link | O(n) find + O(1) link | O(n) (shift) |
| Delete at head | O(1) | O(1) | O(n) (shift) |
| Delete at tail | O(n) | O(1) (tail tracked) | O(1) |
| Reverse | O(n) | O(n) | O(n) |
| Extra memory/node | 1 pointer | 2 pointers | 0 (contiguous) |

### 15.4 Pattern Recognition Quick Guide

See full flowchart in §10.1 and clue table in §10.2 — condensed version:

```
cycle/loop      -> Fast & Slow
middle          -> Fast & Slow
Nth from end    -> Two Pointer Gap
reverse         -> Prev-Current-Next
merge sorted    -> Merge/Zipper
head may change -> Dummy Node
random pointer  -> Hash Map / Interleaving
multilevel      -> DFS Splice
```

### 15.5 Python Syntax Cheat Sheet

```python
node.val                 # access data
node.next                # access next pointer
node.next = other_node   # rewire pointer (reference assignment)
node is None              # correct null check (identity, not equality)
node1 is node2            # correct "same object" check
a, b = b, a                # swap two pointer variables safely (tuple unpacking)
current.next, l1 = l1, l1.next   # simultaneous multi-assign (careful with RHS-first evaluation!)
```

> 📝 **Note**: In `a, b = expr1, expr2`, Python evaluates the entire right-hand side **first**, then assigns left-to-right. This lets you write pointer swaps like `current.next, l1 = l1, l1.next` safely in one line — the old `l1.next` is read before `l1` itself is reassigned.

### 15.6 Interview Guide — 60-Second Recap Before Any Linked List Round

1. Confirm: singly or doubly? Circular? Sorted?
2. Ask about edge cases: empty list, one node, duplicates, cycles.
3. Identify the pattern from §10.2's clue table.
4. Decide: need a dummy node? (If head might change — yes.)
5. Write pointer updates in **safe order** (save-before-overwrite).
6. Dry run on a 3-4 node example.
7. State time/space complexity out loud.
8. Mention at least one optimization/trade-off, even if your first solution is already optimal.


---

## 16. PRACTICE PROBLEMS

> 📝 **Note on links**: Exact URLs shift over time and platform slugs can change, so instead of guessing links that might be stale or wrong, each problem lists its **platform** and **name** — search that exact phrase on the platform for the current link. Where a well-known problem number exists (e.g., LeetCode), it's included to make searching unambiguous.

### 16.1 Basics

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| Reverse a Linked List (LeetCode #206) | LeetCode | Easy | Reversal |
| Middle of the Linked List (LeetCode #876) | LeetCode | Easy | Fast & Slow |
| Delete Node in a Linked List (LeetCode #237) | LeetCode | Easy | Value-swap trick (no head access) |
| Linked List Insertion | GeeksforGeeks | Basic | Core Operations |
| Linked List Traversal | HackerRank | Basic | Core Operations |
| Print in Reverse | GeeksforGeeks | Basic | Recursion |

### 16.2 Traversal

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| Get Nth Node | GeeksforGeeks | Easy | Traversal / Indexing |
| Print Linked List Elements | HackerRank | Easy | Traversal |
| Count Nodes in Linked List | GeeksforGeeks | Easy | Traversal |

### 16.3 Reversal

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| Reverse Linked List II (LeetCode #92) | LeetCode | Medium | Reverse Between (§6.2) |
| Reverse Nodes in K-Group (LeetCode #25) | LeetCode | Hard | Reverse K-Group (§6.3) |
| Swap Nodes in Pairs (LeetCode #24) | LeetCode | Medium | Pairwise swap (§6.17) |
| Reverse Doubly Linked List | GeeksforGeeks | Medium | DLL Reversal |

### 16.4 Fast & Slow Pointer

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| Linked List Cycle (LeetCode #141) | LeetCode | Easy | Cycle Detection (§6.5) |
| Linked List Cycle II (LeetCode #142) | LeetCode | Medium | Cycle Start (§6.6) |
| Palindrome Linked List (LeetCode #234) | LeetCode | Easy | Middle + Reverse + Compare (§6.19) |
| Reorder List (LeetCode #143) | LeetCode | Medium | Middle + Reverse + Merge (§6.14) |
| Happy Number (LeetCode #202) | LeetCode | Easy | Cycle Detection on implicit list |
| Find the Duplicate Number (LeetCode #287) | LeetCode | Medium | Floyd's Algorithm on array-as-list |

### 16.5 Cycle Detection

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| Detect Loop in Linked List | GeeksforGeeks | Medium | Floyd's Algorithm |
| Remove Loop in Linked List | GeeksforGeeks | Medium | Cycle Removal (§6.7) |
| Find Length of Loop | GeeksforGeeks | Medium | Cycle Analysis |

### 16.6 Merge

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| Merge Two Sorted Lists (LeetCode #21) | LeetCode | Easy | Merge/Zipper (§6.8) |
| Merge K Sorted Lists (LeetCode #23) | LeetCode | Hard | Divide & Conquer / Heap (§6.9) |
| Add Two Numbers (LeetCode #2) | LeetCode | Medium | Digit-wise Merge (§6.20) |
| Add Two Numbers II (LeetCode #445) | LeetCode | Medium | Reverse + Add, or Stack-based |

### 16.7 Sorting

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| Sort List (LeetCode #148) | LeetCode | Medium | Merge Sort (§6.10) |
| Insertion Sort List (LeetCode #147) | LeetCode | Medium | Insertion Sort adapted for lists |
| Sort a Linked List of 0s, 1s, 2s | GeeksforGeeks | Medium | Counting / Three-Pointer Partition |

### 16.8 Random Pointer

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| Copy List with Random Pointer (LeetCode #138) | LeetCode | Medium | Hash Map / Interleaving (§6.21) |
| Clone a Linked List with Next and Random Pointer | GeeksforGeeks | Medium | Same as above |

### 16.9 Circular Linked List

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| Circular Linked List Implementation | GeeksforGeeks | Medium | Circular structure (§4.3) |
| Split a Circular Linked List into Two Halves | GeeksforGeeks | Medium | Fast/Slow on circular list |
| Josephus Problem using Circular Linked List | GeeksforGeeks | Medium | Circular elimination simulation |

### 16.10 Advanced Linked List

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| LRU Cache (LeetCode #146) | LeetCode | Medium | DLL + HashMap (§6.23) |
| LFU Cache (LeetCode #460) | LeetCode | Hard | DLL + HashMap + Frequency buckets |
| Flatten a Multilevel Doubly Linked List (LeetCode #430) | LeetCode | Medium | DFS Splice (§6.22) |
| Rotate List (LeetCode #61) | LeetCode | Medium | Circular trick (§6.13) |
| Partition List (LeetCode #86) | LeetCode | Medium | Two-Dummy Partition (§6.16) |
| Odd Even Linked List (LeetCode #328) | LeetCode | Medium | Multi-pointer (§6.15) |
| Remove Nth Node From End of List (LeetCode #19) | LeetCode | Medium | Two Pointer Gap (§6.12) |
| Intersection of Two Linked Lists (LeetCode #160) | LeetCode | Easy | Two-pointer switch (§6.18) |
| Design Skip List (LeetCode #1206) | LeetCode | Hard | Layered linked lists (§4.9) |
| Design Browser History (LeetCode #1472) | LeetCode | Medium | DLL application (§9.2) |
| Design a Music Player (Circular) | InterviewBit / Custom | Medium | Circular DLL application (§9.3) |
| Sum Lists (CTCI-style) | InterviewBit | Medium | Digit-wise Add |

### 16.11 Competitive Programming Style

| Problem | Platform | Difficulty | Pattern/Concept |
|---|---|---|---|
| Linked List sequence simulation problems | Codeforces | Varies | Often array-simulated linked lists for speed |
| List manipulation / deque-heavy problems | AtCoder | Varies | Often solved via `collections.deque` in Python |
| Static Range / dynamic structure problems | CSES | Varies | Sometimes solved with an explicit "linked list over array" (next/prev index arrays) technique for O(1) deletion |
| Graph Adjacency List construction | CodeChef | Varies | Adjacency-list-as-linked-list representation (§9.9) |

> 💡 **Competitive Programming Tip**: In competitive programming (Codeforces/AtCoder/CSES), true node-based linked lists (with Python objects) are often **too slow** due to per-object overhead. The standard trick is an **"array-based linked list"**: maintain `next[i]` and `prev[i]` arrays of plain integers representing indices, giving O(1) deletion/insertion without object allocation overhead — this is a distinct but closely related technique worth knowing for CP contexts.


---

## 17. FINAL REVISION

### 17.1 One-Page Notes

- A linked list is nodes (`val` + `next`) connected by references, not contiguous memory.
- O(1) insert/delete at known positions; O(n) access/search — the opposite trade-off of arrays.
- Six templates cover ~90% of problems: Traverse, Dummy Node, Fast/Slow, Reversal, Merge, Split.
- Dummy node whenever the head might change.
- Fast/Slow for middle-finding and cycle detection.
- Save-before-overwrite is the golden rule for every pointer rewiring.
- Doubly linked list + hash map = O(1) LRU cache — the canonical "design" answer.
- Prefer iterative over recursive for large lists (recursion limit + stack space).

### 17.2 Mind Map (Text Form)

```
LINKED LIST
├── Types
│   ├── Singly / Doubly
│   └── Circular (Singly/Doubly)
├── Core Operations
│   ├── Insert (head/tail/position)
│   ├── Delete (head/tail/value/position)
│   └── Search / Traverse / Reverse
├── Pointer Patterns
│   ├── Fast & Slow
│   ├── Two Pointer Gap
│   ├── Dummy Node
│   ├── Prev-Current-Next
│   └── Merge / Split
├── Algorithms
│   ├── Reversal family (full / between / k-group)
│   ├── Cycle family (detect / find start / remove)
│   ├── Merge family (2 lists / k lists / sort)
│   ├── Structural (partition / odd-even / rotate / reorder)
│   └── Advanced (random pointer / flatten / LRU)
└── Applications
    ├── LRU Cache, Undo/Redo, Browser History
    └── Hash Chaining, Graph Adjacency Lists, OS Memory Mgmt
```

### 17.3 Pointer Pattern Map

```
"middle / cycle"        -> Fast & Slow
"n-th from end"         -> Two Pointer Gap
"head may change"       -> Dummy Node
"reverse (any form)"    -> Prev-Current-Next
"combine sorted lists"  -> Merge/Zipper
"divide the list"       -> Split
```

### 17.4 Recognition Flowchart

(Full version in §10.1 — condensed):
```
cycle/loop keyword?      -> Fast & Slow
middle keyword?          -> Fast & Slow
"from the end"?          -> Two Pointer Gap
reverse (full/partial)?  -> Prev-Current-Next
merge/sort multiple?     -> Merge + Split
random/child pointer?    -> Hash Map or Interleave/Splice
```

### 17.5 Complexity Sheet (Condensed)

| Operation | Time | Space |
|---|---|---|
| Traverse / Search | O(n) | O(1) |
| Insert/Delete at head | O(1) | O(1) |
| Insert/Delete at tail (tail tracked) | O(1) | O(1) |
| Reverse | O(n) | O(1) iterative / O(n) recursive |
| Detect Cycle | O(n) | O(1) |
| Merge 2 sorted lists | O(n+m) | O(1) |
| Merge k sorted lists | O(N log k) | O(k) heap or O(1) D&C |
| Sort (merge sort) | O(n log n) | O(log n) recursion |
| Copy w/ random pointer | O(n) | O(1) interleaving / O(n) hashmap |

### 17.6 Interview Cheat Sheet (One Screen)

```
1. Clarify: singly/doubly? circular? sorted? duplicates? cycle possible?
2. Pick pattern from clue table (§10.2).
3. Dummy node if head may change.
4. Write pointer updates save-before-overwrite.
5. Dry run 3-4 node example.
6. State complexity + one optimization/trade-off.
```

### 17.7 Standard Templates Recap

See §15.1 for full copy-paste templates (Node definition, traverse, dummy skeleton, fast/slow, reversal, merge).

### 17.8 15-Minute Revision Plan

1. (3 min) Re-read §17.1 One-Page Notes.
2. (4 min) Re-derive the Reversal template (§6.1) from memory, without looking.
3. (4 min) Re-derive the Fast & Slow template (§7.1) and explain *why* it finds the middle/cycle.
4. (4 min) Skim the Pattern Recognition Clue Table (§10.2).

### 17.9 1-Hour Revision Plan

1. (10 min) Re-read Introduction + Fundamentals (§1, §3) — refresh terminology.
2. (15 min) Re-implement from scratch, without looking: Reverse (§6.1), Detect Cycle (§6.5), Merge Two Sorted Lists (§6.8), Remove Nth From End (§6.12).
3. (15 min) Re-implement one "combo" problem: Palindrome Check (§6.19) or Reorder List (§6.14) — both stack 2-3 patterns together.
4. (10 min) Read through Common Mistakes (§14) and Cheat Sheets (§15).
5. (10 min) Pick 2 problems from the Practice Problems table (§16) you haven't solved and attempt them cold.

---

## 18. FAQs

**Q: Why not just use `collections.deque` instead of building linked lists by hand?**
A: In production Python, `deque` (a C-implemented doubly linked list) is almost always the right choice for O(1) append/pop at both ends. Hand-rolled node-based linked lists matter for (a) interviews/algorithm practice where the interviewer wants to see pointer manipulation, and (b) custom structures needing node-level access that `deque` doesn't expose (e.g., LRU cache internals, multilevel/random-pointer structures).

**Q: When should I use a doubly linked list instead of singly linked?**
A: When you need backward traversal, or O(1) deletion given only a reference to the node itself (no need to find its predecessor by scanning) — this is exactly why LRU Cache (§6.23) needs a DLL.

**Q: Why does Floyd's algorithm use a 2x speed pointer specifically, not 3x or some other ratio?**
A: Any ratio ≥ 2 would technically still guarantee a meeting inside a cycle, but 2x is the simplest that guarantees the meeting happens within one full lap of the cycle, keeping the proof and implementation clean. It also naturally aligns fast pointer's "2 steps" with the two-hop safety checks (`fast and fast.next`) needed anyway.

**Q: Why do interview solutions favor iterative over recursive, if recursive is often more elegant?**
A: Python's default recursion limit (~1000) and O(n) stack space per recursive call make recursive linked-list solutions risk `RecursionError` on real-world inputs with thousands of nodes. Iterative solutions are the production-safe default; recursive versions are shown for understanding and are sometimes explicitly requested by interviewers.

**Q: Is a Skip List a type of linked list?**
A: Not exactly — it's a probabilistic, layered structure *built from* multiple linked lists to achieve O(log n) expected search time, at the cost of extra pointers and randomized level assignment. It's included here for comparison since it directly evolves from the linked list concept (§4.9).

**Q: My reversal function returns the wrong node as the head — why?**
A: The most common cause is returning `head` (the *original* first node, now the new *tail*) instead of `prev` (which holds the new head after the loop ends). Always return `prev` in the iterative reversal template (§6.1).

**Q: How do I know if I should use a hash set/map or a pointer trick for a given problem?**
A: If the interviewer/problem allows O(n) extra space, a hash set/map is usually the fastest to implement correctly. If they ask for O(1) space as a follow-up, look for a mathematical/structural pointer trick — this handbook covers the two most important ones: Floyd's cycle detection (§6.5–6.7, replaces a "visited" set) and the interleaving trick for random pointers (§6.21, replaces a hash map).

**Q: What's the difference between `node1 == node2` and `node1 is node2` for linked list nodes?**
A: `is` checks object identity (are they literally the same object in memory) — this is what you want for cycle detection, intersection detection, and most pointer-comparison logic. `==` checks value equality, which only works meaningfully if your `Node` class defines `__eq__` (e.g., via `@dataclass`), and even then compares `val`/`next` recursively, which is usually **not** what you want (and can cause infinite recursion or huge unintended comparisons on long lists).

**Q: Should removed/deleted nodes be explicitly cleaned up in Python?**
A: Usually not necessary — Python's reference counting reclaims a node's memory automatically once no references point to it. The one exception is circular references (a node whose removal doesn't break every incoming reference) — Python's cyclic garbage collector handles these too, but explicitly setting `node.next = None` on deletion (§13.7) can help memory be reclaimed sooner and makes bugs (stray references) easier to catch during debugging.

---
