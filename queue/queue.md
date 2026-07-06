# 🐍 THE COMPLETE PYTHON QUEUE HANDBOOK


## 📑 TABLE OF CONTENTS

1. [Introduction to Queues](#1-introduction-to-queues)
2. [Queues in Python](#2-queues-in-python)
3. [Queue Operations](#3-queue-operations)
4. [Queue Implementations](#4-queue-implementations)
   - 4.1 [Array-Based Queue](#41-array-based-queue)
   - 4.2 [Linked List Queue](#42-linked-list-queue)
   - 4.3 [Circular Queue](#43-circular-queue)
   - 4.4 [Dynamic Queue](#44-dynamic-queue)
   - 4.5 [Double-Ended Queue (Deque)](#45-double-ended-queue-deque)
   - 4.6 [Priority Queue](#46-priority-queue)
   - 4.7 [Input Restricted Deque](#47-input-restricted-deque)
   - 4.8 [Output Restricted Deque](#48-output-restricted-deque)
5. [Queue Patterns](#5-queue-patterns)
6. [Real-World Applications](#6-real-world-applications)
7. [Problem Recognition](#7-problem-recognition)
8. [Optimization: Brute Force → Optimal](#8-optimization-brute-force--optimal)
9. [Interview Preparation](#9-interview-preparation)
10. [Python Tips & Pitfalls](#10-python-tips--pitfalls)
11. [Common Mistakes](#11-common-mistakes)
12. [Cheat Sheets](#12-cheat-sheets)
13. [Practice Problems (100+)](#13-practice-problems)
14. [Final Revision](#14-final-revision)

---

## 1. Introduction to Queues

### 1.1 What is a Queue?

A **Queue** is a linear data structure that stores elements in a strict order and allows insertion only at one end (the **rear**/**back**) and removal only at the other end (the **front**). It follows the **FIFO** principle: **First In, First Out** — the first element added is the first one removed.

> **Analogy:** Think of people standing in line at a movie ticket counter. The person who joins the line first is served first. Nobody can jump the line (no random access), and new people can only join at the back.

### 1.2 History

The queue as an abstract data type emerged from early operating-system design in the 1950s–60s, where jobs submitted to a computer needed to be processed in the order they arrived (batch processing). The concept was formalized alongside the stack in foundational computer science texts (Knuth's *The Art of Computer Programming*, Vol. 1) as one of the two fundamental restricted-access linear structures.

### 1.3 The FIFO Principle

```
FIFO = First In, First Out

Enqueue (insert) →  [ A ][ B ][ C ]  → Dequeue (remove)
                     ↑              ↑
                    Rear          Front
                  (insert here)  (remove here)

Order of removal: A, B, C  (same order they entered)
```

### 1.4 Characteristics

| Property | Description |
|---|---|
| Order | FIFO (First In, First Out) |
| Insertion point | Rear / Back / Tail |
| Deletion point | Front / Head |
| Access | Sequential only — no random access to middle elements |
| Traversal | Front → Rear |
| Common backing structures | Array, Linked List, Circular Buffer |

### 1.5 Advantages

- Predictable, fair ordering — no starvation of early requests.
- O(1) enqueue and dequeue with the right implementation (deque, linked list, circular array).
- Naturally models real-world waiting-line systems.
- Backbone of level-order traversal (BFS) in trees and graphs.
- Essential for decoupling producers and consumers in concurrent systems.

### 1.6 Disadvantages

- No random access — to reach the 5th element you must conceptually pass the first four (though in an array-backed queue you *can* index directly, that violates the ADT's access contract).
- A naive array-based queue (without circular indexing) wastes memory as `front` creeps forward — dequeued slots are never reused (Section 11 covers this mistake).
- Searching is O(n).
- Fixed-size implementations can overflow if capacity is misjudged.

### 1.7 Applications (Preview — full list in Section 6)

CPU scheduling, printer spooling, task scheduling, message queues (Kafka, RabbitMQ, SQS), producer-consumer pipelines, network packet buffering, web server request handling, BFS traversal, keystroke/event buffering, call-center hold systems, and streaming data buffers.

### 1.8 Queue vs Other Linear Structures

| Feature | Array | Stack | Queue | Deque |
|---|---|---|---|---|
| Access pattern | Random (O(1)) | LIFO | FIFO | Both ends |
| Insert | Anywhere | Top only | Rear only | Both ends |
| Delete | Anywhere | Top only | Front only | Both ends |
| Real-world analogy | Bookshelf | Plate stack | Ticket line | Deck of cards (draw either end) |
| Typical use | Storage | Undo, recursion, DFS | Scheduling, BFS | Sliding window, both-end ops |

> **Note:** We only compare against other structures here for context — this handbook does **not** teach Stacks, Trees, or Graphs as standalone topics.

---

## 2. Queues in Python

Python offers several ways to implement a queue, each with different performance characteristics and use cases. Choosing the right one is itself a common interview question.

### 2.1 Using a Plain `list`

```python
queue = []

# Enqueue (append to the end) — O(1) amortized
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue (remove from the front) — O(n)  <-- THE PROBLEM
front_element = queue.pop(0)
print(front_element)   # 10
print(queue)            # [20, 30]
```

**Line-by-line explanation:**
- `queue = []` — creates a dynamic array (Python's list is a dynamic array under the hood, not a linked list).
- `queue.append(x)` — inserts at the end in amortized O(1) (occasional resize doubles capacity).
- `queue.pop(0)` — removes the element at index 0. This is **O(n)** because every remaining element must be shifted one position to the left in memory.

> ⚠️ **Warning:** `list.pop(0)` is a classic interview trap. Many candidates use a `list` as a queue without realizing dequeue is O(n), turning an algorithm that "should" be O(n) overall into O(n²).

**Why `pop(0)` is O(n) — internal working:**

```
Before pop(0):
Index:  0    1    2    3
       [10] [20] [30] [40]
        ↑
      remove this

After pop(0), everything shifts left:
Index:  0    1    2
       [20] [30] [40]

Cost: 3 elements shifted → O(n) in general
```

**When to use:** Never for queues in performance-sensitive code. Acceptable only for teaching FIFO conceptually or tiny, one-off scripts.

**When NOT to use:** Any BFS, task scheduler, or high-throughput queue. Use `collections.deque` instead.

---

### 2.2 Using `collections.deque` (Recommended Default)

`deque` (double-ended queue) is implemented in CPython as a **doubly linked list of fixed-size blocks**, giving O(1) appends and pops from **both ends**.

```python
from collections import deque

queue = deque()

# Enqueue — O(1)
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue — O(1)
front_element = queue.popleft()
print(front_element)   # 10
print(queue)             # deque([20, 30])
```

**Line-by-line explanation:**
- `from collections import deque` — imports the double-ended queue class.
- `deque()` — creates an empty deque; optionally accepts `maxlen` for a bounded/circular buffer.
- `.append(x)` — inserts at the right end, O(1).
- `.popleft()` — removes from the left end, O(1). This is the key advantage over `list.pop(0)`.

**Internal working (conceptual):**

```
deque is a doubly linked list of BLOCKS (arrays), not individual nodes:

Block1              Block2
[_,_,_,10,20,30]  <-> [_,_,_,_,_,_]
        ↑front              ↑ growth here on append

- append()      -> O(1), writes into current right block (grows a new block if full)
- popleft()     -> O(1), reads from current left block (frees block if emptied)
- No shifting of existing elements ever occurs.
```

**Dry Run:**

| Step | Operation | Deque State | Explanation |
|---|---|---|---|
| 1 | `queue.append(10)` | `[10]` | 10 inserted at rear |
| 2 | `queue.append(20)` | `[10, 20]` | 20 inserted at rear |
| 3 | `queue.append(30)` | `[10, 20, 30]` | 30 inserted at rear |
| 4 | `queue.popleft()` → 10 | `[20, 30]` | Front removed, O(1) |
| 5 | `queue.append(40)` | `[20, 30, 40]` | 40 inserted at rear |

**Complexity:**

| Operation | Time |
|---|---|
| `append` (enqueue) | O(1) amortized |
| `popleft` (dequeue) | O(1) |
| `appendleft` | O(1) |
| `pop` (right end) | O(1) |
| Random access `dq[i]` | O(n) |
| `in` search | O(n) |

**Best practice:** Use `deque` as the default queue implementation in Python for BFS, sliding window, task queues, and anywhere FIFO/LIFO/both-end behavior is needed — unless you specifically need thread-safety (see `queue.Queue` below) or priority ordering (see `heapq`/`PriorityQueue`).

---

### 2.3 `queue.Queue` (Thread-Safe Queue)

`queue.Queue` is built for **multi-threaded producer-consumer** scenarios. It wraps a `deque` internally but adds locks and condition variables.

```python
import queue
import threading
import time

q = queue.Queue(maxsize=5)

def producer():
    for i in range(5):
        q.put(i)                 # blocks if queue is full
        print(f"Produced {i}")

def consumer():
    for _ in range(5):
        item = q.get()           # blocks if queue is empty
        print(f"Consumed {item}")
        q.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()
```

**Line-by-line explanation:**
- `queue.Queue(maxsize=5)` — creates a thread-safe FIFO queue that can hold at most 5 items; `put()` blocks once full.
- `q.put(i)` — thread-safely enqueues; acquires internal lock, notifies waiting consumers.
- `q.get()` — thread-safely dequeues; blocks if empty until an item is available.
- `q.task_done()` — signals that a retrieved item has finished processing (used with `q.join()` to wait for all work to complete).

> 💡 **Tip:** Use `queue.Queue` specifically when multiple **threads** (not just logical steps) need to safely hand off data. For single-threaded code, `deque` is faster because it skips locking overhead.

**Complexity:** Same asymptotic complexity as `deque` (O(1) put/get) but with added locking overhead — slower constant factor.

---

### 2.4 `queue.SimpleQueue`

A simplified, unbounded, thread-safe FIFO queue introduced in Python 3.7. Lacks `task_done()`/`join()` and task-tracking machinery — just `put()`/`get()`.

```python
import queue

sq = queue.SimpleQueue()
sq.put(1)
sq.put(2)
print(sq.get())   # 1
print(sq.qsize())  # 1
```

**When to use:** Simple thread-safe FIFO handoff without needing task-completion tracking or a max size limit. Slightly faster than `queue.Queue` because it has less overhead.

---

### 2.5 `queue.LifoQueue` (Comparison Only)

`LifoQueue` is a **stack**, not a queue — it retrieves the most recently added item (LIFO). Mentioned here only for contrast; stacks are out of scope for this handbook.

```python
import queue
lq = queue.LifoQueue()
lq.put(1); lq.put(2)
print(lq.get())   # 2  (LIFO, not FIFO)
```

---

### 2.6 `queue.PriorityQueue`

Retrieves the **smallest-priority** item first rather than the oldest. Internally backed by the `heapq` module (a binary heap).

```python
import queue

pq = queue.PriorityQueue()
pq.put((2, "wash dishes"))
pq.put((1, "fire! evacuate"))
pq.put((3, "read a book"))

while not pq.empty():
    priority, task = pq.get()
    print(priority, task)

# Output:
# 1 fire! evacuate
# 2 wash dishes
# 3 read a book
```

**Line-by-line explanation:**
- Items are tuples `(priority, data)`; lower numeric priority is served first.
- Internally, `PriorityQueue` calls `heapq.heappush`/`heapq.heappop`, giving O(log n) insert and extract-min.
- If two tuples have equal priority, Python compares the next element (`data`) to break ties — this can crash if `data` isn't comparable (e.g., two dicts). Fix: add a unique counter as the second tuple element (see Section 11).

**Complexity:**

| Operation | Time |
|---|---|
| `put` | O(log n) |
| `get` | O(log n) |
| Peek smallest | O(1) via `queue[0]` internally, but `PriorityQueue` has no public peek |

> 📝 **Interview Note:** For competitive programming, most people skip `queue.PriorityQueue` (thread-safety overhead) and use the raw `heapq` module directly for speed:
```python
import heapq
heap = []
heapq.heappush(heap, (2, "task"))
heapq.heappush(heap, (1, "urgent"))
print(heapq.heappop(heap))   # (1, 'urgent')
```

---

### 2.7 Custom Queue Class (Building Your Own)

Implementing your own queue clarifies the underlying mechanics — a very common interview ask ("implement a queue without using built-in structures").

```python
class Queue:
    """A simple FIFO queue built on a Python list, front tracked by index."""

    def __init__(self):
        self._items = []

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def enqueue(self, item) -> None:
        self._items.append(item)          # O(1) amortized

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)          # O(n) -- see Section 4.3 for O(1) fix

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def size(self) -> int:
        return len(self._items)

    def __repr__(self):
        return f"Queue(front->{self._items}<-rear)"
```

**Dry Run:**

| Step | Code | State | Front | Explanation |
|---|---|---|---|---|
| 1 | `q = Queue()` | `[]` | — | Empty queue created |
| 2 | `q.enqueue(5)` | `[5]` | 5 | 5 added at rear |
| 3 | `q.enqueue(10)` | `[5, 10]` | 5 | 10 added at rear |
| 4 | `q.dequeue()` → 5 | `[10]` | 10 | Front removed |
| 5 | `q.peek()` → 10 | `[10]` | 10 | Front inspected, not removed |

This naive version has O(n) dequeue; Section 4.1/4.3 show how to fix that with an index pointer or circular buffer.

---

### 2.8 Performance Comparison

| Implementation | Enqueue | Dequeue | Thread-safe | Priority support | Best for |
|---|---|---|---|---|---|
| `list` | O(1)* | O(n) | ❌ | ❌ | Teaching only |
| `collections.deque` | O(1) | O(1) | ❌ | ❌ | **Default choice** — BFS, sliding window |
| `queue.Queue` | O(1) | O(1) | ✅ | ❌ | Multi-threaded producer-consumer |
| `queue.SimpleQueue` | O(1) | O(1) | ✅ | ❌ | Lightweight thread-safe handoff |
| `queue.PriorityQueue` | O(log n) | O(log n) | ✅ | ✅ | Thread-safe priority scheduling |
| `heapq` (raw) | O(log n) | O(log n) | ❌ | ✅ | Competitive programming priority queues |

\* amortized

### 2.9 Best Practices

- Default to `collections.deque` unless you specifically need thread-safety or priority ordering.
- Never use `list.pop(0)` in a hot loop — it silently degrades an O(n) algorithm to O(n²).
- Use `deque(maxlen=k)` for fixed-size sliding windows — old elements are automatically evicted.
- For priority queues in competitive programming, prefer raw `heapq` for speed; use `queue.PriorityQueue` only when thread-safety matters.
- Break priority ties in `heapq`/`PriorityQueue` with an explicit counter to avoid comparing non-comparable payloads.

---

## 3. Queue Operations

Every queue implementation exposes some subset of these core operations.

### 3.1 Operations Overview

| Operation | Description | Typical Complexity |
|---|---|---|
| `enqueue(x)` | Insert `x` at the rear | O(1) |
| `dequeue()` | Remove and return the front element | O(1) (O(n) for naive list) |
| `front()` / `peek()` | Return front element without removing | O(1) |
| `rear()` | Return rear element without removing | O(1) |
| `is_empty()` | Check if queue has zero elements | O(1) |
| `is_full()` | Check if queue is at capacity (bounded queues only) | O(1) |
| `size()` | Number of elements currently in queue | O(1) |
| `clear()` | Remove all elements | O(1) or O(n) depending on implementation |
| `traverse()` | Visit every element front→rear | O(n) |
| `search(x)` | Check if `x` exists in the queue | O(n) |

### 3.2 ASCII Visualization of Core Operations

```
Initial empty queue:
front → [ ] ← rear

enqueue(10):
front → [10] ← rear

enqueue(20):
front → [10, 20] ← rear

enqueue(30):
front → [10, 20, 30] ← rear

dequeue() → removes 10:
front → [20, 30] ← rear

peek() → returns 20 (no removal):
front → [20, 30] ← rear
         ↑ this is what peek() returns
```

### 3.3 Implementing All Operations (Reference)

```python
from collections import deque

class FullQueue:
    """Reference implementation demonstrating every core queue operation."""

    def __init__(self, capacity: int | None = None):
        self._dq = deque()
        self._capacity = capacity  # None = unbounded

    def enqueue(self, item) -> None:
        if self.is_full():
            raise OverflowError("Queue is full")
        self._dq.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._dq.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._dq[0]

    def rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._dq[-1]

    def is_empty(self) -> bool:
        return len(self._dq) == 0

    def is_full(self) -> bool:
        return self._capacity is not None and len(self._dq) >= self._capacity

    def size(self) -> int:
        return len(self._dq)

    def clear(self) -> None:
        self._dq.clear()

    def traverse(self):
        return list(self._dq)   # front -> rear order

    def search(self, item) -> bool:
        return item in self._dq

    def __repr__(self):
        return f"Queue{list(self._dq)}"
```

**Dry Run (capacity = 3):**

| Step | Operation | State | Result |
|---|---|---|---|
| 1 | `q = FullQueue(3)` | `[]` | created |
| 2 | `q.enqueue(1)` | `[1]` | — |
| 3 | `q.enqueue(2)` | `[1,2]` | — |
| 4 | `q.enqueue(3)` | `[1,2,3]` | — |
| 5 | `q.enqueue(4)` | `[1,2,3]` | raises `OverflowError` (full) |
| 6 | `q.dequeue()` | `[2,3]` | returns 1 |
| 7 | `q.front()` | `[2,3]` | returns 2 (no removal) |
| 8 | `q.search(3)` | `[2,3]` | returns True |

### 3.4 Edge Cases Checklist for Every Operation

- **Dequeue/front/rear on empty queue** → must raise/handle gracefully, never silently return `None` unless that's an explicit design choice.
- **Enqueue on full bounded queue** → must raise `OverflowError` or block (thread-safe queues) rather than silently drop data.
- **Single-element queue** → front and rear are the same element; dequeuing it must correctly reset both pointers to "empty" state (critical bug source in circular queues — Section 11).
- **Repeated enqueue/dequeue cycles** → especially relevant for circular queues; verify wrap-around logic doesn't corrupt indices.

---

## 4. Queue Implementations

### 4.1 Array-Based Queue

**Definition:** A queue built on a fixed-size array (Python list used as a fixed-capacity buffer) with explicit `front` and `rear` index pointers.

**Why it exists:** Arrays give contiguous memory and cache-friendly access; tracking indices instead of physically shifting elements avoids the O(n) `pop(0)` problem.

**Intuition:** Instead of physically removing the front element (which shifts everything), just move a `front` pointer forward. The "removed" slot is simply ignored (though this wastes space — motivating the circular queue in 4.3).

**Real-world analogy:** A row of numbered parking spots. Instead of physically moving cars when one leaves, you just note "cars now occupy spots 3 through 7" — you don't shift every car down.

**ASCII Visualization:**

```
Capacity = 5
Index:     0    1    2    3    4
Array:   [10] [20] [30] [ _] [ _]
          ↑front         ↑rear (next insert position)

After dequeue():
Index:     0    1    2    3    4
Array:   [XX] [20] [30] [ _] [ _]
                ↑front

front moves right; slot 0 is now wasted space until reset.
```

**Python Implementation:**

```python
class ArrayQueue:
    """Fixed-capacity queue using a Python list with explicit front/rear pointers."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0     # index of the front element
        self.rear = 0      # index where the NEXT element will be inserted
        self.count = 0      # number of elements currently stored

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.capacity

    def enqueue(self, item) -> None:
        if self.is_full():
            raise OverflowError("Queue overflow")
        self.arr[self.rear] = item
        self.rear += 1
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        item = self.arr[self.front]
        self.arr[self.front] = None   # help garbage collection
        self.front += 1
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.arr[self.front]
```

**Line-by-line explanation:**
- `self.arr = [None] * capacity` — pre-allocates fixed storage, unlike a dynamically growing list.
- `self.rear` tracks the next free slot (not the last used slot) — a common convention that simplifies boundary checks.
- `enqueue` writes at `rear` then advances it; `dequeue` reads at `front` then advances it — both O(1), no shifting.
- `self.count` avoids the ambiguity of `front == rear` meaning both "empty" and "full" (a classic bug — see Section 11).

**Dry Run (capacity = 4):**

| Step | Operation | Array | Front | Rear | Count | Explanation |
|---|---|---|---|---|---|---|
| 1 | init | `[_,_,_,_]` | 0 | 0 | 0 | empty queue |
| 2 | `enqueue(10)` | `[10,_,_,_]` | 0 | 1 | 1 | 10 placed at index 0 |
| 3 | `enqueue(20)` | `[10,20,_,_]` | 0 | 2 | 2 | 20 placed at index 1 |
| 4 | `dequeue()`→10 | `[_,20,_,_]` | 1 | 2 | 1 | front slot cleared |
| 5 | `enqueue(30)` | `[_,20,30,_]` | 1 | 3 | 2 | 30 at index 2 |
| 6 | `enqueue(40)` | `[_,20,30,40]`| 1 | 4 | 3 | 40 at index 3 |
| 7 | `enqueue(50)` | — | — | — | — | **raises OverflowError**: rear=4 is out of bounds even though count=3 < capacity=4 is false is not the issue — count would be 4 only after; actually here count=3 so it should succeed at index 4? |

> ⚠️ **Warning — this is exactly the bug the plain array queue has!** Once `rear` reaches `capacity`, no more insertions are possible even if slots at the front (index 0, 1) are free. This is called **false overflow** and is the entire motivation for the **Circular Queue** (Section 4.3).

**Time & Space Complexity:**

| Operation | Time | Space |
|---|---|---|
| enqueue | O(1) | O(1) extra |
| dequeue | O(1) | O(1) extra |
| Overall storage | — | O(capacity) |

**Edge Cases:** empty dequeue, full enqueue, false overflow (see warning above), single-element queue.

**Common Mistakes:** Forgetting to bound-check `rear` against `capacity`; not distinguishing "empty" (`front == rear`) from "full" without a `count` variable.

**Interview Tip:** If asked to "implement a queue using an array," always mention the false-overflow problem and offer the circular queue as the fix — this signals deeper understanding.

**Variations:** Circular Queue (4.3), Dynamic Queue (4.4).

**Practice Problems:** Design Circular Queue (LeetCode 622), Implement Queue using Array (GfG).

---

### 4.2 Linked List Queue

**Definition:** A queue built on a singly linked list, maintaining explicit `head` (front) and `tail` (rear) node references.

**Why it exists:** Avoids any fixed-capacity limitation (grows dynamically) and avoids the false-overflow issue entirely — memory is allocated per-node, not pre-reserved.

**Intuition:** Enqueue attaches a new node after the current tail and updates the tail pointer; dequeue detaches the head node and advances the head pointer. Both are O(1) because there's no shifting — just pointer rewiring.

**Real-world analogy:** A conga line where each person holds the shoulder of the person behind them — adding someone at the back just means the last person now holds the new person's shoulder; nobody in the middle needs to move.

**ASCII Visualization:**

```
head                          tail
 ↓                              ↓
[10] -> [20] -> [30] -> None

enqueue(40):
head                                   tail
 ↓                                       ↓
[10] -> [20] -> [30] -> [40] -> None

dequeue() removes 10:
        head                            tail
         ↓                                ↓
        [20] -> [30] -> [40] -> None
```

**Python Implementation:**

```python
class Node:
    __slots__ = ("data", "next")

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    """FIFO queue backed by a singly linked list with head & tail pointers."""

    def __init__(self):
        self.head = None   # front
        self.tail = None   # rear
        self._size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, data) -> None:
        node = Node(data)
        if self.tail is None:               # queue was empty
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        node = self.head
        self.head = self.head.next
        if self.head is None:               # queue became empty
            self.tail = None
        self._size -= 1
        return node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.data

    def size(self) -> int:
        return self._size
```

**Line-by-line explanation:**
- `Node` uses `__slots__` for memory efficiency — avoids per-instance `__dict__` overhead.
- `enqueue`: if the queue is empty, the new node becomes both head and tail; otherwise it's linked after the current tail, and `tail` is updated.
- `dequeue`: advances `head` to the next node; **critically**, if this makes `head` `None` (queue now empty), `tail` must also be reset to `None` — forgetting this is a classic bug (a dangling `tail` pointer causes corruption on the next enqueue).

**Dry Run:**

| Step | Operation | List State | Head | Tail | Explanation |
|---|---|---|---|---|---|
| 1 | init | `None` | None | None | empty |
| 2 | `enqueue(10)` | `10` | 10 | 10 | first node = head = tail |
| 3 | `enqueue(20)` | `10->20` | 10 | 20 | tail.next = 20; tail = 20 |
| 4 | `dequeue()`→10 | `20` | 20 | 20 | head advances to 20 |
| 5 | `dequeue()`→20 | `None` | None | None | queue empties, tail also reset |

**Complexity:** O(1) enqueue, O(1) dequeue, O(n) extra space for node overhead (pointers) compared to array-based.

**Edge Cases:** Dequeuing the last element must reset `tail` to `None` (shown above) — omitting this breaks the next enqueue.

**Common Mistakes:** Forgetting the `tail = None` reset; not handling `enqueue` on an empty queue specially (both head and tail must point to the new node).

**Interview Tip:** This is the "implement a queue using a linked list" question — always mention the tail-reset edge case unprompted; interviewers specifically probe this.

**Variations:** Doubly linked list backing enables O(1) operations at both ends → naturally leads into Deque (4.5).

**Practice Problems:** Design a queue using linked list (GfG), LRU Cache variants (uses doubly linked list + hashmap, deque-adjacent).

---

### 4.3 Circular Queue

**Definition:** An array-based queue where index arithmetic **wraps around** using the modulo operator, so freed front slots are reused — eliminating the false-overflow problem of Section 4.1.

**Why it exists:** Solves array-based queue's core weakness: wasted space after `rear` reaches the array's end even when the front has free capacity.

**Intuition:** Treat the array as a ring. When `rear` or `front` would go past the last index, wrap back to index 0 via `% capacity`.

**Real-world analogy:** A circular parking lot / roundabout — cars exit from one gate and new cars enter from the adjacent gate, continuously cycling through the same fixed set of spots.

**ASCII Visualization:**

```
Capacity = 5, indices arranged in a ring:

        [0]
      /     \
   [4]       [1]
     |         |
   [3]       [2]

Physical array:     [10][20][30][_][_]
                      0   1   2  3  4
front=0, rear=3

After 2 dequeues (front moves to 2) and 3 enqueues wrapping around:

Physical array:     [60][70][30][40][50]
                      0   1   2   3   4
                      ↑front is now at index 2? -- let's trace precisely below.
```

**Python Implementation:**

```python
class CircularQueue:
    """Array-based queue with wrap-around indexing — no false overflow."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.count = 0     # avoids ambiguity between "empty" and "full"

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.capacity

    def enqueue(self, item) -> None:
        if self.is_full():
            raise OverflowError("Circular queue overflow")
        rear = (self.front + self.count) % self.capacity
        self.arr[rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Circular queue underflow")
        item = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.arr[self.front]
```

**Line-by-line explanation:**
- `rear = (self.front + self.count) % self.capacity` — computes the next free slot by wrapping around using modulo, instead of storing a separate `rear` variable that could exceed the array bound.
- `self.front = (self.front + 1) % self.capacity` — advancing front also wraps, reusing freed slots.
- `self.count` disambiguates full vs. empty since `front` alone repeating the same value could mean either.

**Dry Run (capacity = 4):**

| Step | Operation | Array | Front | Count | Explanation |
|---|---|---|---|---|---|
| 1 | init | `[_,_,_,_]` | 0 | 0 | empty |
| 2 | `enqueue(10)` | `[10,_,_,_]` | 0 | 1 | rear = (0+0)%4 = 0 |
| 3 | `enqueue(20)` | `[10,20,_,_]` | 0 | 2 | rear = (0+1)%4 = 1 |
| 4 | `enqueue(30)` | `[10,20,30,_]` | 0 | 3 | rear = (0+2)%4 = 2 |
| 5 | `dequeue()`→10 | `[_,20,30,_]` | 1 | 2 | front moves to 1 |
| 6 | `enqueue(40)` | `[_,20,30,40]`| 1 | 3 | rear = (1+2)%4 = 3 |
| 7 | `enqueue(50)` | `[50,20,30,40]`| 1 | 4 | rear = (1+3)%4 = 0 → **wraps!** 50 placed at index 0 |
| 8 | `enqueue(60)` | — | — | — | raises OverflowError (count == capacity == 4) |

This demonstrates the wrap-around: index 0 (freed at step 5) is reused at step 7 — something the plain array queue in 4.1 could never do.

**Complexity:** O(1) enqueue/dequeue, O(capacity) space.

**Edge Cases:** Full-queue wrap where `rear` computation equals `front` (must check via `count`, not index equality); single-slot capacity (capacity=1).

**Common Mistakes:** Using `front == rear` alone to test empty/full (ambiguous — always leads to bugs); forgetting the modulo when advancing either pointer.

**Interview Tip:** LeetCode 622 "Design Circular Queue" is essentially this exact implementation — practice it directly.

**Practice Problems:** Design Circular Queue (LeetCode 622), Design Circular Deque (LeetCode 641).

---

### 4.4 Dynamic Queue

**Definition:** A circular queue that automatically **resizes** (typically doubling) when full, instead of raising `OverflowError`.

**Why it exists:** Combines the cache-friendliness of arrays with unbounded growth, similar to how Python's own `list` grows dynamically.

**Python Implementation:**

```python
class DynamicQueue:
    """Circular queue that doubles its capacity when full."""

    def __init__(self, initial_capacity: int = 4):
        self.capacity = initial_capacity
        self.arr = [None] * self.capacity
        self.front = 0
        self.count = 0

    def is_empty(self) -> bool:
        return self.count == 0

    def _resize(self, new_capacity: int) -> None:
        new_arr = [None] * new_capacity
        for i in range(self.count):
            new_arr[i] = self.arr[(self.front + i) % self.capacity]
        self.arr = new_arr
        self.capacity = new_capacity
        self.front = 0

    def enqueue(self, item) -> None:
        if self.count == self.capacity:
            self._resize(self.capacity * 2)     # grow
        rear = (self.front + self.count) % self.capacity
        self.arr[rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        item = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        if 0 < self.count <= self.capacity // 4:
            self._resize(max(1, self.capacity // 2))   # shrink to save memory
        return item
```

**Line-by-line explanation:**
- `_resize` copies elements out in logical front-to-rear order into a fresh array starting at index 0, resetting `front` to 0 — this "unwraps" the circular buffer during a resize.
- `enqueue` doubles capacity when full — amortized O(1) per operation (standard dynamic array analysis).
- `dequeue` optionally shrinks when usage drops below 25%, preventing memory bloat after a large spike (a nice-to-have, not required).

**Complexity:** O(1) amortized enqueue/dequeue; O(n) worst case during a resize, but amortized across n operations that cost is O(1) each.

**Common Mistakes:** Forgetting to reset `front = 0` after resize (the old circular offsets no longer apply to the new array); resizing by a small fixed increment instead of doubling (causes O(n²) amortized cost — this is why doubling matters).

**Practice Problems:** Design a self-resizing circular buffer (systems design interview flavor).

---

### 4.5 Double-Ended Queue (Deque)

**Definition:** A queue that allows insertion and deletion at **both** the front and the rear.

**Why it exists:** Many algorithms (sliding window maximum, palindrome checking, undo/redo with both-direction access) need O(1) access at both ends — a plain queue can't provide that.

**Real-world analogy:** A deck of cards where you can draw from the top or the bottom.

**ASCII Visualization:**

```
appendleft(x)                         append(y)
     ↓                                    ↓
    [x] <-> [10] <-> [20] <-> [30] <-> [y]
     ↑                                    ↑
  front                                 rear

popleft() removes x; pop() removes y — both O(1)
```

**Python Implementation (using `collections.deque`):**

```python
from collections import deque

dq = deque([10, 20, 30])

dq.append(40)          # [10, 20, 30, 40]
dq.appendleft(5)        # [5, 10, 20, 30, 40]
dq.pop()                 # removes 40 -> [5, 10, 20, 30]
dq.popleft()             # removes 5  -> [10, 20, 30]
print(dq[0], dq[-1])      # front=10, rear=30
```

**Custom Deque from scratch (doubly linked list):**

```python
class DNode:
    __slots__ = ("data", "prev", "next")
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class MyDeque:
    """Deque implemented with a doubly linked list — O(1) both ends."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data) -> None:            # insert at rear
        node = DNode(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1

    def appendleft(self, data) -> None:         # insert at front
        node = DNode(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def pop(self):                                # remove from rear
        if self.tail is None:
            raise IndexError("pop from empty deque")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self._size -= 1
        return data

    def popleft(self):                            # remove from front
        if self.head is None:
            raise IndexError("pop from empty deque")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self._size -= 1
        return data
```

**Line-by-line explanation:**
- Each `DNode` keeps both `prev` and `next` pointers, unlike the singly linked queue in 4.2 — this is what enables O(1) removal from *either* end.
- `append`/`appendleft` mirror each other for the two ends; `pop`/`popleft` similarly mirror each other, each carefully re-linking neighboring pointers and handling the "list becomes empty" edge case.

**Complexity:** O(1) for all four operations (`append`, `appendleft`, `pop`, `popleft`); O(n) space.

**Common Mistakes:** Forgetting to null out `prev`/`next` on the new boundary node after removal (dangling references prevent garbage collection and can cause subtle bugs); confusing which end is "front" vs "rear" when mixing custom and built-in deques.

**Variations:** Input Restricted Deque (4.7), Output Restricted Deque (4.8), Monotonic Deque (Section 5).

**Practice Problems:** Design Circular Deque (LeetCode 641), Sliding Window Maximum (LeetCode 239, uses monotonic deque — Section 5.4), Palindrome check using Deque.

---

### 4.6 Priority Queue

**Definition:** An abstract structure where each element has an associated priority, and dequeue always returns the highest-priority (often lowest-value) element regardless of insertion order — breaking strict FIFO.

**Why it exists:** Many scheduling problems need "most urgent first," not "oldest first" (e.g., OS process scheduling by priority, Dijkstra's shortest path, event simulation).

**Intuition:** Backed by a **binary heap** — a complete binary tree stored in an array where every parent is ≤ (min-heap) or ≥ (max-heap) its children, giving O(log n) insert/extract-min instead of O(n) linear scan.

**ASCII Visualization (min-heap as array & tree):**

```
Array: [1, 3, 2, 7, 4, 5]
Index:  0  1  2  3  4  5

Tree view:
                1(0)
              /      \
           3(1)       2(2)
          /    \      /
       7(3)   4(4)  5(5)

Parent of index i = (i-1)//2
Children of index i = 2i+1, 2i+2
```

**Python Implementation (using `heapq`):**

```python
import heapq

class MinPriorityQueue:
    """Min-priority queue with tie-breaking via insertion counter."""

    def __init__(self):
        self._heap = []
        self._counter = 0    # breaks ties, avoids comparing payloads directly

    def push(self, priority, item) -> None:
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self):
        if not self._heap:
            raise IndexError("pop from empty priority queue")
        priority, _, item = heapq.heappop(self._heap)
        return priority, item

    def peek(self):
        if not self._heap:
            raise IndexError("peek from empty priority queue")
        priority, _, item = self._heap[0]
        return priority, item

    def is_empty(self) -> bool:
        return len(self._heap) == 0
```

**Line-by-line explanation:**
- `heapq.heappush(self._heap, (priority, self._counter, item))` — pushes a 3-tuple; Python compares tuples element-wise, so priority decides order first.
- `self._counter` is a strictly increasing tiebreaker — if two items share a priority, Python compares the counter next (never the possibly-uncomparable `item`), avoiding a `TypeError`.
- `heapq.heappop` removes and returns the smallest tuple in O(log n) by sifting the last element to the root and bubbling it down.

**Dry Run:**

| Step | Operation | Heap (priority, counter, item) | Explanation |
|---|---|---|---|
| 1 | `push(5, "B")` | `[(5,0,"B")]` | first item |
| 2 | `push(2, "A")` | `[(2,1,"A"),(5,0,"B")]` | 2 < 5, bubbles to root |
| 3 | `push(5, "C")` | `[(2,1,"A"),(5,0,"B"),(5,2,"C")]` | tie broken by counter (0 < 2) |
| 4 | `pop()` → (2,"A") | `[(5,0,"B"),(5,2,"C")]` | smallest removed |

**Complexity:**

| Operation | Time |
|---|---|
| push | O(log n) |
| pop (extract-min) | O(log n) |
| peek | O(1) |
| build heap from n items | O(n) (via `heapify`) |

**Edge Cases:** Empty pop/peek; equal priorities without a tiebreaker (`TypeError: '<' not supported`); max-heap emulation (negate priorities since `heapq` is min-heap only).

**Common Mistakes:** Pushing raw `(priority, object)` tuples where `object` isn't comparable, causing crashes only on ties (a nasty non-deterministic-looking bug); assuming `heapq` gives a sorted list at all times (only index 0 is guaranteed to be the minimum).

**Interview Tip:** "Top K" problems (K largest/smallest, K closest points, merge K sorted lists) are the signature use case for priority queues — recognize the phrase "top K" / "Kth largest" as a heap trigger.

**Practice Problems:** Kth Largest Element (LeetCode 215), Top K Frequent Elements (LeetCode 347), Merge K Sorted Lists (LeetCode 23), Task Scheduler (LeetCode 621), Meeting Rooms II (LeetCode 253).

---

### 4.7 Input Restricted Deque

**Definition:** A deque variant where **insertion is allowed only at one end** (typically the rear), but **deletion is allowed at both ends**.

**Why it exists:** Models systems where new items must always join at a known entry point, but can be withdrawn from either end for flexibility (e.g., a print queue where jobs can be cancelled from the front or reprioritized/removed from the back, but new jobs always append at the back).

**Python Implementation:**

```python
from collections import deque

class InputRestrictedDeque:
    """Insert only at rear; delete from either end."""

    def __init__(self):
        self._dq = deque()

    def insert_rear(self, item) -> None:
        self._dq.append(item)

    def delete_front(self):
        if not self._dq:
            raise IndexError("empty deque")
        return self._dq.popleft()

    def delete_rear(self):
        if not self._dq:
            raise IndexError("empty deque")
        return self._dq.pop()

    # Note: no insert_front() is exposed — that's the "restriction"
```

**Complexity:** O(1) for all exposed operations.

**Common Mistakes:** Accidentally exposing an `insert_front` method, which defeats the entire point of the "restricted" variant — interviewers may explicitly check that you *don't* provide it.

**Practice Problems:** Mostly conceptual/design-round questions (GfG "Input Restricted Deque" theory questions); rarely appears as a raw coding problem but often as a sub-component in a larger design question.

---

### 4.8 Output Restricted Deque

**Definition:** A deque variant where **deletion is allowed only at one end** (typically the front), but **insertion is allowed at both ends**.

**Why it exists:** Models systems where results must be consumed in a fixed order, but data can be added either urgently (front) or normally (rear) — e.g., a job queue where high-priority jobs get pushed to the front, but jobs are always completed (removed) from the front only.

**Python Implementation:**

```python
from collections import deque

class OutputRestrictedDeque:
    """Insert at either end; delete only from front."""

    def __init__(self):
        self._dq = deque()

    def insert_front(self, item) -> None:
        self._dq.appendleft(item)

    def insert_rear(self, item) -> None:
        self._dq.append(item)

    def delete_front(self):
        if not self._dq:
            raise IndexError("empty deque")
        return self._dq.popleft()

    # Note: no delete_rear() is exposed — that's the "restriction"
```

**Complexity:** O(1) for all exposed operations.

**Comparison Table (Deque Variants):**

| Variant | Insert Front | Insert Rear | Delete Front | Delete Rear |
|---|---|---|---|---|
| Full Deque | ✅ | ✅ | ✅ | ✅ |
| Input Restricted Deque | ❌ | ✅ | ✅ | ✅ |
| Output Restricted Deque | ✅ | ✅ | ✅ | ❌ |

**Practice Problems:** Conceptual design questions; GfG theory MCQs frequently test the difference between these two restricted variants — memorize the table above.

---

## 5. Queue Patterns

### 5.1 BFS Queue Pattern

**Definition:** Breadth-First Search visits nodes level by level using a queue to hold the "frontier" of nodes discovered but not yet processed. (We cover only the *queue mechanics*; tree/graph traversal theory itself is out of scope.)

**Why a queue specifically:** FIFO ordering guarantees nodes are processed in the order they were discovered, which is exactly what produces level-by-level (breadth-first) behavior. Using a stack instead would produce depth-first order.

**ASCII Visualization:**

```
Graph (adjacency):  1 -> [2, 3]
                    2 -> [4]
                    3 -> [4]
                    4 -> []

Queue evolution during BFS from node 1:

Step 0: queue = [1]                 visited = {1}
Step 1: pop 1, push 2,3 -> queue = [2, 3]      visited = {1,2,3}
Step 2: pop 2, push 4   -> queue = [3, 4]      visited = {1,2,3,4}
Step 3: pop 3, (4 already visited) -> queue = [4]
Step 4: pop 4, no new neighbors -> queue = []   DONE

Level order visited: 1, 2, 3, 4
```

**Python Implementation (generic BFS skeleton):**

```python
from collections import deque

def bfs(graph: dict, start):
    visited = {start}
    order = []
    q = deque([start])

    while q:
        node = q.popleft()          # FIFO: process oldest-discovered first
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)   # mark visited at enqueue time!
                q.append(neighbor)
    return order
```

**Line-by-line explanation:**
- `visited = {start}` — marks the start node visited **before** the loop begins, avoiding it being re-enqueued.
- `q.popleft()` — dequeues the earliest-discovered unprocessed node, the core FIFO mechanic that produces level order.
- **Critical detail:** neighbors are marked `visited` at **enqueue time**, not at dequeue time. Marking at dequeue time allows the same node to be enqueued multiple times before it's first processed — a very common bug that causes redundant work or even infinite loops in graphs with cycles.

**Dry Run:** See ASCII visualization above — it doubles as the dry run table.

**Complexity:** O(V + E) time (each vertex enqueued once, each edge examined once), O(V) space for the queue and visited set.

**Edge Cases:** Disconnected graphs (BFS from one node won't reach all nodes — need to loop over all unvisited nodes for full coverage); self-loops; already-visited start node.

**Common Mistakes:** Marking visited at dequeue time instead of enqueue time (causes duplicate enqueues); forgetting to check `visited` before enqueueing at all.

---

### 5.2 Multi-Source BFS Queue

**Definition:** Instead of starting BFS from a single node, **multiple starting nodes are pushed into the queue simultaneously** before the loop begins — useful for "nearest of several sources" problems (e.g., rotting oranges, nearest exit).

**ASCII Visualization:**

```
Grid (0 = empty, R = rotten):
R . .
. . .
. . R

Initial queue = [(0,0), (2,2)]   <- both rotten oranges pushed as sources

Level 1 (1 minute later), all neighbors of both sources rot simultaneously.
```

**Python Implementation:**

```python
from collections import deque

def multi_source_bfs(grid, sources):
    """sources: list of (row, col) starting points, all at distance 0."""
    rows, cols = len(grid), len(grid[0])
    dist = {s: 0 for s in sources}
    q = deque(sources)          # seed the queue with ALL sources at once

    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                q.append((nr, nc))
    return dist
```

**Line-by-line explanation:**
- `q = deque(sources)` — seeding with multiple sources at once means they're all treated as "distance 0," and BFS naturally computes distance from the *nearest* source to every cell, since all sources expand outward in lockstep.

**Complexity:** O(R×C) for a grid, same as single-source BFS — multi-source doesn't add overhead, it just changes the initial queue contents.

**Common Mistakes:** Running separate single-source BFS for each source and taking the minimum (works but is far less efficient — O(k × R × C) instead of O(R × C)).

**Practice Problems:** Rotting Oranges (LeetCode 994), Walls and Gates (LeetCode 286), Nearest Exit from Entrance in Maze (LeetCode 1926).

---

### 5.3 Circular Queue Pattern (Round-Robin)

**Definition:** Using a circular queue to cycle repeatedly through a fixed set of participants — classic use case: CPU round-robin scheduling.

**Python Implementation:**

```python
from collections import deque

def round_robin(tasks: list, quantum: int):
    """Simulate round-robin CPU scheduling. tasks: list of [name, burst_time]."""
    q = deque(tasks)
    timeline = []

    while q:
        name, remaining = q.popleft()
        run_time = min(quantum, remaining)
        timeline.append((name, run_time))
        remaining -= run_time
        if remaining > 0:
            q.append((name, remaining))   # re-enqueue at the BACK — key idea
    return timeline
```

**Line-by-line explanation:**
- Each task runs for at most `quantum` time units, then — if unfinished — is **re-enqueued at the rear**, giving every other waiting task a fair turn before it runs again. This rear-reinsertion is the defining trait of round-robin.

**Dry Run (tasks=[("A",5),("B",3)], quantum=2):**

| Step | Queue Before | Popped | Runs | Remaining | Queue After |
|---|---|---|---|---|---|
| 1 | `[(A,5),(B,3)]` | A | 2 | 3 | `[(B,3),(A,3)]` |
| 2 | `[(B,3),(A,3)]` | B | 2 | 1 | `[(A,3),(B,1)]` |
| 3 | `[(A,3),(B,1)]` | A | 2 | 1 | `[(B,1),(A,1)]` |
| 4 | `[(B,1),(A,1)]` | B | 1 | 0 | `[(A,1)]` (B done) |
| 5 | `[(A,1)]` | A | 1 | 0 | `[]` (A done) |

**Complexity:** O(total burst time / quantum) enqueue/dequeue operations, each O(1).

**Practice Problems:** Task Scheduler (LeetCode 621, though solved with heap+cooldown logic), OS round-robin scheduling simulations.

---

### 5.4 Sliding Window Using Deque (Monotonic Queue)

**Definition:** A deque that maintains elements in **monotonically increasing or decreasing order**, used to answer "max/min in every window of size k" in O(n) instead of O(n·k).

**Why it exists:** A naive sliding window max recomputes the max for every window (O(k) per window → O(n·k) total). A monotonic deque instead keeps only *candidates that could still be the max* for some future window, discarding elements that can never win.

**Intuition:** Store **indices**, not values, in the deque. Before adding a new index, pop from the back every index whose value is smaller than the current value (they can never be the max again, since the new element is both later *and* larger). The front of the deque is always the max of the current window.

**ASCII Visualization (window size 3, array = [1,3,-1,-3,5,3,6,7]):**

```
i=0, val=1:  deque=[0]                              (values: [1])
i=1, val=3:  pop 0 (1<3), deque=[1]                  (values: [3])
i=2, val=-1: deque=[1,2]                              (values: [3,-1])  window [1,3,-1] complete -> max = arr[deque[0]] = 3
i=3, val=-3: deque=[1,2,3]                            (values: [3,-1,-3]) window [3,-1,-3] -> max = 3
i=4, val=5:  pop 3(-3<5), pop 2(-1<5), pop 1(3<5)     deque=[4]  window [-1,-3,5] -> wait, index 1 fell out of window range too -> max = 5
...
```

**Python Implementation:**

```python
from collections import deque

def sliding_window_max(nums: list, k: int) -> list:
    dq = deque()          # stores INDICES, values kept in decreasing order
    result = []

    for i, num in enumerate(nums):
        # Remove indices that are now outside the window [i-k+1, i]
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Remove all indices whose values are smaller than the current value
        # -- they can never be the max while `num` is still in the window
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])    # front of deque = index of current max

    return result
```

**Line-by-line explanation:**
- `if dq and dq[0] <= i - k: dq.popleft()` — evicts the front index once it slides outside the current window's left boundary.
- `while dq and nums[dq[-1]] < num: dq.pop()` — maintains the decreasing-value invariant by discarding any back elements smaller than the incoming value; they're now useless since `num` is both younger and bigger.
- `dq.append(i)` — the surviving candidate is added; note we always add regardless (it might get popped later, but it's never wrong to consider it now).
- `nums[dq[0]]` — since the deque is kept in decreasing order of value, the front is always the current window's maximum.

**Dry Run:** `nums=[1,3,-1,-3,5,3,6,7], k=3` → expected output `[3,3,5,5,6,7]`

| i | num | Deque After Evictions/Additions (indices) | Window Complete? | Max Added |
|---|---|---|---|---|
| 0 | 1 | `[0]` | No | — |
| 1 | 3 | pop 0 (1<3) → `[1]` | No | — |
| 2 | -1 | `[1,2]` | Yes (i≥2) | `nums[1]=3` |
| 3 | -3 | `[1,2,3]` | Yes | `nums[1]=3` |
| 4 | 5 | pop 3,2,1 (all <5) → `[4]` | Yes | `nums[4]=5` |
| 5 | 3 | `[4,5]` | Yes | `nums[4]=5` |
| 6 | 6 | pop 5,4 (<6) → `[6]` | Yes | `nums[6]=6` |
| 7 | 7 | pop 6 (<7) → `[7]` | Yes | `nums[7]=7` |

Result: `[3, 3, 5, 5, 6, 7]` ✅

**Complexity:** O(n) time — each index is pushed and popped from the deque **at most once** (amortized analysis), O(k) space.

**Edge Cases:** `k=1` (every element is its own max — deque never evicts based on value); `k == len(nums)` (single window); all elements equal (deque only ever holds the most recent index since ties get popped... actually with strict `<` in the while condition, equal values are **not** popped — verify this matches the desired tie-breaking behavior for your specific problem variant).

**Common Mistakes:** Storing values instead of indices (loses the ability to check window-boundary eviction); using `<=` instead of `<` in the eviction `while` loop, which silently changes tie-breaking behavior; forgetting the window-boundary eviction check entirely (produces wrong answers once the window has fully slid past early elements).

**Interview Tip:** "Maximum/minimum in every window of size k" is the #1 verbal signal for a monotonic deque. If you see brute force being O(n·k), immediately think "can I maintain a monotonic deque of candidates?"

**Practice Problems:** Sliding Window Maximum (LeetCode 239), Shortest Subarray with Sum at Least K (LeetCode 862), Constrained Subsequence Sum (LeetCode 1425), Jump Game VI (LeetCode 1696).

---

### 5.5 Monotonic Queue (General Pattern)

**Definition:** Generalization of 5.4 beyond sliding windows — any problem where you need to efficiently query "the max/min among currently valid candidates" while candidates are added/removed in a queue-like (mostly FIFO with selective early eviction) manner.

**Decision Tree — When to Reach for a Monotonic Queue:**

```
Does the problem involve a window (fixed or variable size) over an array?
        │
        ├── YES → Do you need max/min within each window?
        │            │
        │            ├── YES → Monotonic Deque ✅
        │            └── NO  → Maybe plain sliding window (two pointers), not a queue pattern
        │
        └── NO → Do you need "next greater/smaller element" style queries?
                     │
                     ├── YES → Monotonic STACK (out of scope here — stack, not queue)
                     └── NO  → Probably not a monotonic-queue problem
```

**Common Mistakes:** Confusing monotonic queue (used for sliding windows) with monotonic stack (used for "next greater element" style problems, which pop from one end and push to the same end, LIFO) — they solve different problem shapes.

---

### 5.6 Producer-Consumer Queue

**Definition:** A concurrency pattern where one or more "producer" threads add items to a shared queue, and one or more "consumer" threads remove and process them — the queue decouples production speed from consumption speed.

**Python Implementation:**

```python
import queue
import threading

def producer(q: queue.Queue, items):
    for item in items:
        q.put(item)
    q.put(None)     # sentinel value signaling "no more items"

def consumer(q: queue.Queue):
    while True:
        item = q.get()
        if item is None:
            q.put(None)      # re-broadcast sentinel for other consumers, if any
            break
        print(f"Processing {item}")

q = queue.Queue(maxsize=10)
t_prod = threading.Thread(target=producer, args=(q, range(5)))
t_cons = threading.Thread(target=consumer, args=(q,))
t_prod.start(); t_cons.start()
t_prod.join(); t_cons.join()
```

**Line-by-line explanation:**
- `q.put(None)` uses a **sentinel value** to signal completion — a simple, common technique to tell consumers "the stream has ended" without needing a separate shared flag.
- `maxsize=10` bounds the queue, applying **backpressure**: if the queue fills up, `q.put()` blocks until a consumer frees space, preventing unbounded memory growth if the producer is much faster than the consumer.

**Complexity:** O(1) per put/get; overall throughput bounded by the slower of producer/consumer.

**Common Mistakes:** Forgetting the sentinel (consumer blocks forever waiting on an empty queue with no way to know production is done); unbounded queue with a fast producer and slow consumer causing memory exhaustion in production systems.

**Practice Problems:** Design a bounded blocking queue (systems design interview staple); Design Hit Counter (LeetCode 362, deque-based sliding window of timestamps).

---

### 5.7 Task Scheduling Queue

**Definition:** Using a queue (often a priority queue) to order tasks by arrival time, deadline, or priority for execution.

**Python Implementation (priority-based, using heapq):**

```python
import heapq

def schedule_tasks(tasks):
    """tasks: list of (deadline, task_name). Returns execution order by deadline."""
    heap = list(tasks)
    heapq.heapify(heap)     # O(n) build
    order = []
    while heap:
        deadline, name = heapq.heappop(heap)
        order.append(name)
    return order
```

**Complexity:** O(n log n) overall (n pops, each O(log n)).

**Practice Problems:** Task Scheduler (LeetCode 621), Course Schedule (topological-sort-adjacent, uses a queue for Kahn's algorithm), Reorganize String (heap-based scheduling).

---

### 5.8 Simulation Queue

**Definition:** Using a queue to directly simulate a real-world sequential process step-by-step (bank teller lines, elevator requests, order processing) rather than as part of an abstract algorithm.

**Python Implementation (simple bank queue simulation):**

```python
from collections import deque

def simulate_bank(customers, service_time_per_customer):
    """customers: list of arrival times (sorted). Returns each customer's finish time."""
    q = deque(customers)
    finish_times = []
    current_time = 0

    while q:
        arrival = q.popleft()
        start = max(current_time, arrival)     # teller waits if idle, customer waits if teller busy
        finish = start + service_time_per_customer
        finish_times.append(finish)
        current_time = finish
    return finish_times
```

**Complexity:** O(n) for n customers.

**Practice Problems:** Time Needed to Buy Tickets (LeetCode 2073, direct queue simulation), Design a queue-based elevator system (systems design interview).

---

## 6. Real-World Applications

| Application | How Queues Are Used |
|---|---|
| **CPU Scheduling** | The OS scheduler maintains a ready queue of processes waiting for CPU time; round-robin scheduling (5.3) cycles through it fairly. |
| **Printer Queue** | Print jobs are queued FIFO; the printer processes them in submission order (sometimes with a priority queue for urgent jobs). |
| **Task Scheduling** | Cron-like systems and job runners queue tasks for sequential or worker-pool execution. |
| **Message Queues** | Systems like Kafka, RabbitMQ, and AWS SQS decouple producers and consumers across distributed services using durable, persistent queues. |
| **Producer-Consumer Pipelines** | Multi-threaded/multi-process pipelines use queues (Section 5.6) to hand off work between stages safely. |
| **Network Packet Processing** | Routers and network interface cards buffer incoming/outgoing packets in queues to handle bursty traffic and enforce QoS ordering. |
| **Web Servers** | Incoming HTTP requests are queued when all worker threads/processes are busy (e.g., a backlog queue in a TCP listen socket). |
| **BFS Traversal** | Level-order graph/tree exploration fundamentally relies on FIFO queue ordering (Section 5.1). |
| **Buffering** | I/O buffers (keyboard input, audio/video streaming buffers) use queues to smooth out speed mismatches between producer and consumer. |
| **Streaming** | Video/audio streaming services buffer incoming data chunks in a queue to allow smooth playback despite variable network speed. |
| **Event Processing** | GUI event loops and event-driven architectures queue events (clicks, key presses, messages) for sequential dispatch. |
| **Call Center Systems** | Callers are held in a FIFO (or priority) queue until an agent becomes available. |

### 6.1 ASCII: Message Queue Architecture

```
Producer Service --> [ Message Queue ] --> Consumer Service
                        (Kafka/RabbitMQ)

  Producer keeps publishing        Consumer processes at its own pace
  even if consumer is slow  ---->  Queue absorbs the burst (backpressure/buffering)
```

---

## 7. Problem Recognition

### 7.1 Recognition Flowchart

```
Does the problem mention "level order", "shortest path in unweighted graph/grid",
or "minimum steps/moves"?
        │
        ├── YES → Think BFS Queue Pattern (5.1) / Multi-source BFS (5.2)
        │
        └── NO → Does it mention "sliding window" + "maximum/minimum"?
                     │
                     ├── YES → Monotonic Deque (5.4)
                     │
                     └── NO → Does it mention "top K", "Kth largest/smallest",
                               "merge K sorted", "schedule by priority/deadline"?
                                    │
                                    ├── YES → Priority Queue / heapq (4.6, 5.7)
                                    │
                                    └── NO → Does it mention "recent requests in
                                              last X time/seconds" or "hit counter"?
                                                   │
                                                   ├── YES → Deque as sliding time window (4.5)
                                                   │
                                                   └── NO → Does it describe strict
                                                             first-come-first-served
                                                             processing, rotating turns,
                                                             or a literal "queue"/"line"?
                                                                  │
                                                                  ├── YES → Plain FIFO Queue /
                                                                  │         Circular Queue (4.1-4.3)
                                                                  │
                                                                  └── NO → Probably not a queue problem
```

### 7.2 Interview Clues (Keyword → Pattern Table)

| Keyword / Phrase in Problem | Likely Pattern |
|---|---|
| "level order traversal" | BFS Queue (5.1) |
| "minimum number of steps/moves to reach" | BFS (unweighted shortest path) |
| "rotting", "spreading", "infection", "multiple starting points" | Multi-source BFS (5.2) |
| "sliding window maximum/minimum" | Monotonic Deque (5.4) |
| "Kth largest/smallest", "top K frequent" | Priority Queue / heapq (4.6) |
| "merge K sorted lists/arrays" | Priority Queue (4.6) |
| "schedule", "deadline", "cooldown" | Priority Queue / Task Scheduling (5.7) |
| "requests in the last N seconds/minutes" | Deque as time window (4.5) |
| "round robin", "CPU burst", "time quantum" | Circular Queue (5.3) |
| "design a queue with O(1) operations" | Circular Queue (4.3) / Deque (4.5) |
| "first unique character/element in a stream" | Plain Queue + hashmap |
| "implement stack using queues" / "queue using stacks" | Classic queue/stack conversion drills |

### 7.3 Decision Tree: Which Queue Implementation to Choose

```
Do you need thread-safety (multiple OS threads)?
   │
   ├── YES → Do you need priority ordering?
   │            ├── YES → queue.PriorityQueue
   │            └── NO  → queue.Queue or queue.SimpleQueue
   │
   └── NO → Do you need priority ordering (single-threaded)?
                ├── YES → heapq (raw)
                └── NO  → Do you need access at both ends?
                             ├── YES → collections.deque
                             └── NO  → collections.deque (still — never plain list.pop(0))
```

> 💡 Notice `collections.deque` is nearly always the right single-threaded answer — even for a "plain" queue, since `popleft()` is O(1) while `list.pop(0)` is O(n).

---

## 8. Optimization: Brute Force → Optimal

### 8.1 Case Study: Sliding Window Maximum

| Approach | Idea | Time | Space |
|---|---|---|---|
| **Brute Force** | For every window, scan all k elements to find the max | O(n·k) | O(1) extra |
| **Better** | Use a max-heap of (value, index); lazily discard stale indices on pop | O(n log n) | O(n) |
| **Optimal** | Monotonic deque (Section 5.4) — each element pushed/popped at most once | O(n) | O(k) |

```python
# Brute Force
def sliding_window_max_brute(nums, k):
    return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]

# Better (heap-based, handles stale indices lazily)
import heapq
def sliding_window_max_heap(nums, k):
    heap = []       # stores (-value, index) for a max-heap using heapq's min-heap
    result = []
    for i, num in enumerate(nums):
        heapq.heappush(heap, (-num, i))
        while heap[0][1] <= i - k:      # discard indices outside window
            heapq.heappop(heap)
        if i >= k - 1:
            result.append(-heap[0][0])
    return result

# Optimal — see Section 5.4 for the full monotonic deque solution
```

**Why the optimal wins:** The brute force redoes work every window; the heap approach adds unnecessary O(log n) overhead per element and stale entries bloat the heap; the monotonic deque discards useless candidates immediately and guarantees each element enters/exits the deque exactly once, yielding true O(n).

### 8.2 Case Study: Implement Queue Using Stacks (Classic Conversion Drill)

**Brute Force:** Use two stacks; every dequeue transfers everything from stack1 to stack2, pops, then transfers back — O(n) per dequeue.

**Optimal (Amortized O(1)):** Transfer lazily — only move elements from `in_stack` to `out_stack` when `out_stack` is empty.

```python
class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x) -> None:
        self.in_stack.append(x)                     # O(1)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:                      # only transfer when needed
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("dequeue from empty queue")
        return self.out_stack.pop()
```

**Why it's amortized O(1):** Each element is moved from `in_stack` to `out_stack` **exactly once** over its lifetime, regardless of how many dequeue calls happen. Spreading that one-time O(1) move cost across all operations gives amortized O(1) per dequeue.

**Practice Problems:** Implement Queue using Stacks (LeetCode 232), Implement Stack using Queues (LeetCode 225 — the mirror-image drill).

---

## 9. Interview Preparation

### 9.1 Difficulty-Tiered Problem List

**Easy:**
- Implement Queue using Stacks — LeetCode 232
- Number of Recent Calls — LeetCode 933
- Design Circular Queue — LeetCode 622
- Moving Average from Data Stream — LeetCode 346
- First Unique Character in a String (queue + hashmap variant) — LeetCode 387

**Medium:**
- Sliding Window Maximum — LeetCode 239 (usually labeled Hard, conceptually a core Medium-level pattern once monotonic deque is known)
- Design Circular Deque — LeetCode 641
- Rotting Oranges — LeetCode 994
- Task Scheduler — LeetCode 621
- Design Hit Counter — LeetCode 362
- Walls and Gates — LeetCode 286
- Perfect Squares (BFS shortest path variant) — LeetCode 279
- Open the Lock — LeetCode 752
- Course Schedule (Kahn's algorithm, queue-based topological sort) — LeetCode 207

**Hard:**
- Sliding Window Maximum — LeetCode 239
- Merge K Sorted Lists — LeetCode 23
- Shortest Subarray with Sum at Least K — LeetCode 862
- Constrained Subsequence Sum — LeetCode 1425
- Reorganize String / Task Scheduler variants with cooldown — LeetCode 358, 621

### 9.2 Pattern-Wise Question Map

| Pattern | Representative Problems |
|---|---|
| BFS Queue | Rotting Oranges, Open the Lock, Perfect Squares, Word Ladder |
| Multi-Source BFS | Rotting Oranges, Walls and Gates, Nearest Exit from Entrance in Maze |
| Monotonic Deque | Sliding Window Maximum, Jump Game VI, Constrained Subsequence Sum |
| Priority Queue | Kth Largest Element, Merge K Sorted Lists, Top K Frequent Elements |
| Circular Queue | Design Circular Queue, Design Circular Deque |
| Queue Design | Implement Queue using Stacks, Moving Average from Data Stream, Design Hit Counter |
| Topological Sort (Kahn's, queue-based) | Course Schedule, Course Schedule II, Alien Dictionary |

### 9.3 Company-Wise Flavor (General Trends)

| Company | Typical Queue-Flavored Focus |
|---|---|
| Google | BFS/graph problems, monotonic deque optimization questions |
| Amazon | Priority queue / task scheduling (fits their systems/OA focus), design questions |
| Microsoft | Queue design (circular queue, implement queue using stacks) |
| Meta | Sliding window + deque combination problems |
| Bloomberg | Simulation-style queue problems (ticket systems, order books) |

> Company trends shift over time — always cross-check with the latest community-reported interview experiences (e.g., LeetCode's company tag, Blind) closer to your interview date.

### 9.4 Blind 75 / NeetCode Queue-Relevant Problems

- Number of Islands (BFS/multi-source flavor available) — NeetCode Graphs
- Course Schedule — NeetCode Graphs
- Sliding Window Maximum — NeetCode Sliding Window (only "hard" one requiring deque)
- Merge K Sorted Lists — NeetCode Linked List (heap-based)
- Task Scheduler — NeetCode Greedy/Heap

### 9.5 Interview Tricks & Talking Points

- When implementing a queue in an interview, **always ask**: "Do you need thread-safety?" and "Do you need priority ordering, or strict FIFO?" — this shows you know the design space (Section 2.8).
- If asked to "design a queue with O(1) enqueue/dequeue" using arrays, proactively mention the false-overflow issue and pivot to circular indexing — interviewers love unprompted awareness of pitfalls.
- For BFS problems, always state explicitly: "I'll mark nodes visited at enqueue time, not dequeue time, to avoid duplicate processing." This single sentence signals strong fundamentals.
- For sliding window max/min, saying "this needs a monotonic deque to get O(n) instead of O(n·k)" immediately signals pattern recognition.
- If two heap entries could tie and aren't naturally comparable, mention adding a tiebreaker counter — a small detail that shows production-code awareness.

### 9.6 Frequently Asked Interview Questions (Conceptual)

**Q: Why is `list.pop(0)` bad for queues?**
A: It's O(n) because every remaining element must shift left in memory; `deque.popleft()` is O(1) because deque is a doubly linked list of blocks with no shifting required.

**Q: How do you implement a queue using two stacks?**
A: Push onto `in_stack`; on dequeue, if `out_stack` is empty, transfer all of `in_stack` onto it (reversing order), then pop from `out_stack`. This gives amortized O(1) dequeue (Section 8.2).

**Q: What's the difference between a circular queue and a regular array queue?**
A: A regular array queue wastes space once `rear` reaches the array's end even if front slots are free ("false overflow"); a circular queue wraps indices using modulo to reuse freed slots (Section 4.3).

**Q: When would you use `queue.Queue` over `collections.deque`?**
A: When multiple threads need thread-safe, blocking put/get semantics; `deque` is not thread-safe for compound operations (though individual append/pop calls are atomic due to the GIL, complex sequences are not safe).

**Q: How does a monotonic deque achieve O(n) for sliding window maximum?**
A: Each array index is pushed onto the deque exactly once and popped at most once (either due to going out of the window or being dominated by a larger later value), so total deque operations are bounded by O(n) regardless of window count.

---

## 10. Python Tips & Pitfalls

### 10.1 `deque` vs `list` — When Each Wins

| Need | Use |
|---|---|
| FIFO queue (enqueue/dequeue) | `deque` — never `list.pop(0)` |
| Random access by index frequently | `list` |
| Both-end insert/delete | `deque` |
| Fixed-size sliding window (auto-evict oldest) | `deque(maxlen=k)` |
| Sorting / slicing | `list` |

### 10.2 `deque(maxlen=k)` — Automatic Sliding Window

```python
from collections import deque

window = deque(maxlen=3)
for x in [1, 2, 3, 4, 5]:
    window.append(x)
    print(list(window))

# Output:
# [1]
# [1, 2]
# [1, 2, 3]
# [2, 3, 4]   <- 1 automatically evicted once maxlen exceeded
# [3, 4, 5]   <- 2 automatically evicted
```

**Why this matters:** `maxlen` gives you a free, O(1)-per-op sliding window buffer without manually tracking eviction — extremely useful for "last N events" style problems (e.g., moving averages, hit counters).

### 10.3 `queue` Module Gotchas

- `queue.Queue.qsize()` is **approximate** in multi-threaded contexts — don't rely on it for exact control flow (race conditions between the check and subsequent `get()`/`put()`).
- `queue.Queue.empty()` / `full()` are similarly advisory only, not authoritative, in concurrent code — use blocking `get()`/`put()` with timeouts instead of polling these.

### 10.4 `collections` Module Recap

| Class | Purpose |
|---|---|
| `deque` | Double-ended queue, O(1) both-end ops |
| `Counter` | Frequency counting (useful alongside queues for "top K frequent" problems) |
| `OrderedDict` | Preserves insertion order (pre-3.7 dicts didn't); useful for LRU-cache-style queue+hashmap combos |
| `defaultdict` | Auto-initializing dict, handy for adjacency lists in BFS |

### 10.5 Performance Tips

- Prefer `deque.append`/`popleft` over list-based shifting in any loop that runs more than a handful of times.
- For priority queues in tight competitive-programming loops, raw `heapq` beats `queue.PriorityQueue` because it avoids lock acquisition overhead.
- Pre-size structures when possible (e.g., `[None] * capacity` for array-based queues) to avoid repeated reallocation.
- Avoid `in` checks on large `deque`/`list` objects in hot loops (O(n)) — use a `set` alongside for O(1) membership testing (as done in the BFS `visited` set).

### 10.6 Memory Tips

- `__slots__` on custom `Node` classes (Section 4.2, 4.5) meaningfully reduces per-node memory overhead in large linked structures.
- Circular queues (4.3) avoid the memory churn of resizing that naive dynamic queues might otherwise need more frequently.
- Clearing references (`self.arr[self.front] = None`) on dequeue helps garbage collection reclaim memory for large stored objects.

### 10.7 Common Python Pitfalls

- Using `queue.Queue()` when you don't need thread-safety — pure overhead in single-threaded code.
- Forgetting `deque` doesn't support slicing (`dq[1:3]` raises `TypeError`) — convert to `list()` first if you need slicing.
- Mutating a `deque` while iterating over it directly (`for x in dq: dq.append(...)`) — causes `RuntimeError: deque mutated during iteration`.
- Assuming `heapq` gives a fully sorted structure — only index 0 is guaranteed to be the extreme value at any time.

---

## 11. Common Mistakes

### 11.1 Overflow (Bounded Queues)

**Mistake:** Not checking `is_full()` before enqueue in a fixed-capacity queue, silently overwriting data or throwing an unhandled `IndexError`.

```python
# WRONG
def enqueue(self, item):
    self.arr[self.rear] = item     # IndexError if rear == capacity, no bounds check!
    self.rear += 1

# RIGHT
def enqueue(self, item):
    if self.is_full():
        raise OverflowError("Queue is full")
    self.arr[self.rear] = item
    self.rear += 1
```

### 11.2 Underflow (Empty Queue)

**Mistake:** Calling `dequeue()`/`front()` on an empty queue without a guard, causing an unhandled exception or, worse, silently returning garbage/`None` that gets mistaken for valid data.

### 11.3 Incorrect Front/Rear Handling

**Mistake:** Using a plain `front == rear` check to distinguish empty vs. full in an array/circular queue — this is fundamentally **ambiguous** (both states can produce `front == rear`). Always maintain a separate `count` variable (as done throughout Section 4) or intentionally leave one slot empty as a sentinel.

### 11.4 Circular Queue Wrap-Around Errors

**Mistake:** Forgetting the modulo when advancing `front` or computing `rear`, causing an `IndexError` once the physical array end is reached.

```python
# WRONG
self.rear += 1              # will eventually exceed capacity

# RIGHT
self.rear = (self.rear + 1) % self.capacity
```

### 11.5 Off-by-One Errors

**Mistake:** In sliding window problems, using `i - k` instead of `i - k + 1` (or vice versa) when checking whether an index has fallen outside the window — always trace through a small example by hand (as done in every dry run in this handbook) before trusting the boundary condition.

### 11.6 Deque Misuse

**Mistake:** Using `deque` when you actually need random access or sorting — `dq[5]` is O(n), and `sorted(dq)` re-materializes a list anyway; if you're doing this often, a `list` (or different structure entirely) may be more appropriate.

### 11.7 Queue Synchronization Mistakes (Concurrency)

**Mistake:** Sharing a plain `collections.deque` across threads and assuming it's fully thread-safe for compound operations (check-then-act patterns like `if dq: dq.popleft()`) — individual deque methods are atomic thanks to the GIL, but sequences of calls are not. Use `queue.Queue` for genuine multi-threaded producer-consumer safety.

### 11.8 Heap Tie-Breaking Crash

**Mistake:** Pushing `(priority, payload)` tuples into `heapq` where `payload` isn't comparable (e.g., a dict or custom object without `__lt__`), causing a `TypeError` — but only on ties, making it look intermittent. Fix: add a monotonically increasing counter as the middle tuple element (Section 4.6).

---

## 12. Cheat Sheets

### 12.1 Operations Cheat Sheet

| Operation | `deque` method | Time |
|---|---|---|
| Enqueue (rear) | `append(x)` | O(1) |
| Dequeue (front) | `popleft()` | O(1) |
| Peek front | `dq[0]` | O(1) |
| Peek rear | `dq[-1]` | O(1) |
| Insert front | `appendleft(x)` | O(1) |
| Remove rear | `pop()` | O(1) |
| Size | `len(dq)` | O(1) |
| Membership check | `x in dq` | O(n) |

### 12.2 Complexity Cheat Sheet

| Structure | Enqueue | Dequeue | Peek | Space |
|---|---|---|---|---|
| `list` (misused as queue) | O(1)* | O(n) | O(1) | O(n) |
| `collections.deque` | O(1) | O(1) | O(1) | O(n) |
| Array-based (fixed) | O(1) | O(1) | O(1) | O(capacity) |
| Circular Queue | O(1) | O(1) | O(1) | O(capacity) |
| Linked List Queue | O(1) | O(1) | O(1) | O(n) + pointer overhead |
| Priority Queue (heap) | O(log n) | O(log n) | O(1) | O(n) |

\* amortized

### 12.3 Queue Types Cheat Sheet

| Type | Insert | Delete | Notes |
|---|---|---|---|
| Simple Queue | Rear only | Front only | Classic FIFO |
| Circular Queue | Rear (wraps) | Front (wraps) | No false overflow |
| Deque | Both ends | Both ends | Most flexible |
| Input Restricted Deque | Rear only | Both ends | |
| Output Restricted Deque | Both ends | Front only | |
| Priority Queue | By priority | Highest priority first | Heap-backed |

### 12.4 Pattern Recognition Cheat Sheet

| Signal | Pattern |
|---|---|
| "level order" / "shortest path unweighted" | BFS Queue |
| "multiple sources spreading" | Multi-source BFS |
| "sliding window max/min" | Monotonic Deque |
| "top K" / "Kth largest" / "merge K sorted" | Priority Queue (heap) |
| "recent events in last N seconds" | Deque as time window / `maxlen` |
| "round robin" / "time quantum" | Circular Queue |

### 12.5 Python Syntax Quick Reference

```python
from collections import deque
import heapq
import queue

dq = deque()                    # empty deque
dq = deque([1,2,3])              # from iterable
dq = deque(maxlen=5)             # bounded, auto-evicting

dq.append(x); dq.appendleft(x)     # insert rear / front
dq.pop(); dq.popleft()              # remove rear / front
dq.rotate(1)                          # rotate right by 1 (rotate(-1) rotates left)
dq.extend([1,2]); dq.extendleft([1,2])

heap = []
heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heapify(existing_list)          # O(n) in-place min-heap conversion
heapq.nlargest(k, iterable)
heapq.nsmallest(k, iterable)

q = queue.Queue(maxsize=10)
q.put(item); q.get()
q.task_done(); q.join()
```

---

## 13. Practice Problems

> Format: **Problem Name** | Platform | Difficulty | Pattern | Concept

### 13.1 Basics (FIFO / Queue Fundamentals)

1. Implement Queue using Array | GeeksforGeeks | Easy | Basics | Array-based queue — [gfg.in/queue](https://www.geeksforgeeks.org/implementation-queue-using-array/)
2. Implement Queue using Linked List | GeeksforGeeks | Easy | Basics | Linked list queue
3. Implement Queue using Stacks | LeetCode 232 | Easy | Conversion | Two-stack amortized O(1)
4. Implement Stack using Queues | LeetCode 225 | Easy | Conversion | Mirror-image drill
5. Number of Recent Calls | LeetCode 933 | Easy | Time window | Deque as sliding time window
6. Moving Average from Data Stream | LeetCode 346 | Easy | Time window | `deque(maxlen=k)`
7. Reveal Cards In Increasing Order | LeetCode 950 | Medium | Simulation | Deque simulation
8. Time Needed to Buy Tickets | LeetCode 2073 | Easy | Simulation | Direct queue simulation
9. Design a Queue-based Stack (theory) | InterviewBit | Easy | Conversion | Concept drill
10. Dota2 Senate | LeetCode 649 | Medium | Simulation | Circular queue simulation

### 13.2 Circular Queue

11. Design Circular Queue | LeetCode 622 | Medium | Circular Queue | Wrap-around indexing
12. Design Circular Deque | LeetCode 641 | Medium | Circular Deque | Both-end wrap-around
13. Josephus Problem | GeeksforGeeks | Medium | Circular Queue | Round-robin elimination
14. Circular Tour / Gas Station | LeetCode 134 | Medium | Circular Queue (conceptual) | Circular traversal logic
15. Round Robin Scheduling Simulation | GeeksforGeeks | Medium | Circular Queue | OS scheduling simulation

### 13.3 Deque

16. Sliding Window Maximum | LeetCode 239 | Hard | Monotonic Deque | Section 5.4
17. Shortest Subarray with Sum at Least K | LeetCode 862 | Hard | Monotonic Deque | Prefix sum + deque
18. Constrained Subsequence Sum | LeetCode 1425 | Hard | Monotonic Deque | DP + deque optimization
19. Jump Game VI | LeetCode 1696 | Medium | Monotonic Deque | DP + deque optimization
20. Max Value of Equation | LeetCode 1499 | Hard | Monotonic Deque | Deque + slope trick
21. Palindrome Checker Using Deque | GeeksforGeeks | Easy | Deque | Both-end comparison
22. Design Front Middle Back Queue | LeetCode 1670 | Medium | Deque variant | Multi-position design
23. Find the Winner of the Circular Game | LeetCode 1823 | Medium | Deque/Circular | Simulation

### 13.4 Priority Queue

24. Kth Largest Element in an Array | LeetCode 215 | Medium | Priority Queue | heapq
25. Top K Frequent Elements | LeetCode 347 | Medium | Priority Queue | heap + Counter
26. Merge K Sorted Lists | LeetCode 23 | Hard | Priority Queue | heap of list heads
27. Task Scheduler | LeetCode 621 | Medium | Priority Queue | heap + cooldown
28. Meeting Rooms II | LeetCode 253 | Medium | Priority Queue | heap of end times
29. K Closest Points to Origin | LeetCode 973 | Medium | Priority Queue | heap by distance
30. Find Median from Data Stream | LeetCode 295 | Hard | Priority Queue | two-heap technique
31. Ugly Number II | LeetCode 264 | Medium | Priority Queue | heap-based generation
32. Reorganize String | LeetCode 767 | Medium | Priority Queue | heap-based greedy
33. Last Stone Weight | LeetCode 1046 | Easy | Priority Queue | max-heap simulation
34. Kth Smallest Element in a Sorted Matrix | LeetCode 378 | Medium | Priority Queue | heap on matrix
35. Smallest Range Covering Elements from K Lists | LeetCode 632 | Hard | Priority Queue | heap across k lists

### 13.5 Sliding Window (Deque-Based)

36. Sliding Window Maximum | LeetCode 239 | Hard | Sliding Window | See #16
37. Sliding Window Median | LeetCode 480 | Hard | Sliding Window | Two heaps + lazy deletion
38. Longest Continuous Subarray With Absolute Diff ≤ Limit | LeetCode 1438 | Medium | Sliding Window | Two monotonic deques
39. Grumpy Bookstore Owner | LeetCode 1052 | Medium | Sliding Window | Fixed window sum
40. Maximum Number of Robots Within Budget | LeetCode 2398 | Hard | Sliding Window | Monotonic deque + running sum

### 13.6 BFS Queue

41. Binary Tree Level Order Traversal | LeetCode 102 | Medium | BFS Queue | Level-by-level with queue
42. Rotting Oranges | LeetCode 994 | Medium | Multi-source BFS | Section 5.2
43. Walls and Gates | LeetCode 286 | Medium | Multi-source BFS | Distance propagation
44. Nearest Exit from Entrance in Maze | LeetCode 1926 | Medium | BFS Queue | Shortest path grid
45. Open the Lock | LeetCode 752 | Medium | BFS Queue | State-space BFS
46. Word Ladder | LeetCode 127 | Hard | BFS Queue | Shortest transformation sequence
47. Perfect Squares | LeetCode 279 | Medium | BFS Queue | Shortest path via BFS (alt to DP)
48. 01 Matrix | LeetCode 542 | Medium | Multi-source BFS | Nearest zero distance
49. Course Schedule | LeetCode 207 | Medium | BFS (Kahn's Algorithm) | Topological sort via queue
50. Course Schedule II | LeetCode 210 | Medium | BFS (Kahn's Algorithm) | Topological order output
51. Snakes and Ladders | LeetCode 909 | Medium | BFS Queue | Shortest path on board
52. Shortest Path in Binary Matrix | LeetCode 1091 | Medium | BFS Queue | 8-directional shortest path
53. Minimum Knight Moves | LeetCode 1197 | Medium | BFS Queue | Chessboard shortest path
54. As Far from Land as Possible | LeetCode 1162 | Medium | Multi-source BFS | Max of min distances
55. Bus Routes | LeetCode 815 | Hard | BFS Queue | Graph modeling + BFS
56. Alien Dictionary | LeetCode 269 (Premium) | Hard | BFS (Kahn's Algorithm) | Topological sort

### 13.7 Monotonic Queue (Beyond Sliding Window)

57. Sum of Subarray Minimums | LeetCode 907 | Medium | Monotonic Queue/Stack | Contribution technique
58. Maximum Sum Circular Subarray | LeetCode 918 | Medium | Monotonic Deque | Prefix sum + deque
59. Trapping Rain Water | LeetCode 42 | Hard | Monotonic Queue/Stack (alt approach) | Two-pointer preferred, monotonic viable
60. Largest Rectangle in Histogram | LeetCode 84 | Hard | Monotonic Stack (contrast) | Compare vs monotonic queue

### 13.8 Design Problems

61. Design Circular Queue | LeetCode 622 | Medium | Design | See #11
62. Design Circular Deque | LeetCode 641 | Medium | Design | See #12
63. Design Hit Counter | LeetCode 362 | Medium | Design | Deque-based time window
64. Design Front Middle Back Queue | LeetCode 1670 | Medium | Design | See #22
65. Design a Stack With Increment Operation | LeetCode 1381 | Medium | Design (contrast) | Stack, included for comparison
66. LRU Cache | LeetCode 146 | Medium | Design | Doubly linked list + hashmap (deque-adjacent)
67. LFU Cache | LeetCode 460 | Hard | Design | Multiple deques by frequency
68. Design Snake Game | LeetCode 353 | Medium | Design | Deque for snake body
69. Design a Food Rating System | LeetCode 2353 | Medium | Design | Heap-based design
70. Design Twitter | LeetCode 355 | Medium | Design | Heap-based feed merge

### 13.9 Cross-Platform Additional Problems

71. Queue using two Stacks | GeeksforGeeks | Easy | Basics | Classic conversion
72. Reverse a Queue | GeeksforGeeks | Easy | Basics | Recursion/stack-assisted
73. Reverse First K elements of Queue | GeeksforGeeks | Medium | Basics | Combined stack+queue technique
74. Interleave the First Half of the Queue with Second Half | GeeksforGeeks | Medium | Basics | Queue manipulation
75. Circular Tour Problem | GeeksforGeeks | Medium | Circular Queue | Petrol pump variant
76. Generate Binary Numbers from 1 to N | GeeksforGeeks | Easy | BFS Queue | Queue-based generation
77. First Negative Number in Every Window of Size K | GeeksforGeeks | Medium | Monotonic Deque | Window-based
78. Maximum of All Subarrays of Size K | GeeksforGeeks | Medium | Monotonic Deque | Same as #16 (GfG phrasing)
79. LRU Cache Design | InterviewBit | Medium | Design | Queue + hashmap
80. Sliding Window Maximum | Code360 (Coding Ninjas) | Hard | Monotonic Deque | Practice on alt platform
81. N-Queen Combinations (BFS-based state search variant) | Code360 | Hard | BFS-adjacent | State enumeration
82. Rotting Oranges | Code360 | Medium | Multi-source BFS | Grid problem
83. Task Scheduler CPU | HackerRank | Medium | Priority Queue | Scheduling simulation
84. Queue using Array | HackerRank | Easy | Basics | Fundamentals
85. Down to Zero II (BFS shortest path) | HackerRank | Medium | BFS Queue | Number-transformation BFS
86. Truck Delivery / Fleet Management (queue simulation) | InterviewBit | Medium | Simulation | Operations research flavor
87. Perfect Squares | InterviewBit | Medium | BFS Queue | Same as #47
88. Order Book Simulation | Bloomberg-style OA | Medium | Priority Queue | Buy/sell order matching
89. Sliding Window Maximum | Codeforces (various problem sets) | Medium | Monotonic Deque | Competitive variant with tight constraints
90. CF 1000+ rated "queue simulation" tagged problems | Codeforces | Varies | Simulation | Search tag "queue" on Codeforces problemset
91. Ration Distribution (queue simulation) | CodeChef | Medium | Simulation | Fair allocation via queue
92. CSES: Josephus Problem I | CSES Problem Set | Easy | Circular Queue | Classic elimination
93. CSES: Josephus Problem II | CSES Problem Set | Medium | Circular Queue + BIT | Advanced elimination
94. CSES: Sliding Window Minimum | CSES Problem Set | Medium | Monotonic Deque | Direct application of Section 5.4
95. CSES: Traffic Lights (ordered structure, deque-adjacent) | CSES Problem Set | Medium | Ordered structure | Related concept
96. AtCoder: Sliding Window style problems (search "deque" tag) | AtCoder | Varies | Monotonic Deque | Practice variety
97. Design a Circular Buffer for Logging | GeeksforGeeks (System Design flavor) | Medium | Circular Queue | Applied systems use
98. Simulate a Print Queue | GeeksforGeeks | Easy | Simulation | Applied FIFO scenario
99. Sum of Minimum and Maximum Elements of All Subarrays of size K | GeeksforGeeks | Hard | Monotonic Deque | Combines max+min deques
100. First non-repeating character in a stream | GeeksforGeeks | Medium | Queue + hashmap | Streaming uniqueness tracking

> 📌 **Note:** Items 80–96 point to problem *categories/tags* on their respective platforms (Code360, HackerRank, Codeforces, CodeChef, CSES, AtCoder) rather than single fixed URLs, since exact links/IDs shift over time on these platforms — search the platform's tag or problem name directly for the current link.

---

## 14. Final Revision

### 14.1 One-Page Notes

- **Queue = FIFO.** First In, First Out. Insert at rear, remove at front.
- **Default Python choice:** `collections.deque` — O(1) both ends. Never `list.pop(0)` (O(n)).
- **Thread-safe needs:** `queue.Queue` (full-featured) or `queue.SimpleQueue` (lightweight).
- **Priority needs:** `heapq` (raw, fast) or `queue.PriorityQueue` (thread-safe).
- **Circular Queue** fixes array-based "false overflow" via modulo wrap-around.
- **Deque** = both-end access; **Monotonic Deque** = sliding window max/min in O(n).
- **BFS** = queue-driven level-order traversal; mark visited **at enqueue time**.
- **Multi-source BFS** = seed the queue with all sources before the loop starts.
- **Round-robin** = circular re-enqueue at the rear when a task isn't finished.
- **Queue via two stacks** = amortized O(1) by lazy transfer only when the output stack is empty.

### 14.2 Mind Map (ASCII)

```
                                   QUEUE
                                     │
        ┌───────────────┬───────────┼───────────┬────────────────┐
        │                │           │           │                │
   Implementations   Operations   Patterns   Applications   Python Tools
        │                │           │           │                │
  ┌─────┼─────┐      enqueue    BFS Queue     CPU Sched      deque
  │     │     │      dequeue    Multi-src     Printer Q      queue.Queue
Array Linked Circular front     BFS           Msg Queues     heapq
  │  List     │      rear       Circular      Networking     queue.
Dynamic  Deque   PriorityQ      Round-robin   Web Servers    PriorityQueue
              │                 Sliding       BFS
      Input/Output              Window Deque  Streaming
      Restricted                Monotonic Q   Event Proc.
                                 Producer-
                                 Consumer
                                 Task Sched.
                                 Simulation
```

### 14.3 Pattern Map

```
"Level order / shortest unweighted path"     -> BFS Queue
"Multiple sources spreading simultaneously"  -> Multi-source BFS
"Window max/min"                             -> Monotonic Deque
"Top K / Kth largest / merge K sorted"       -> Priority Queue (heap)
"Recent events in last N seconds"            -> Deque / maxlen
"Round robin / time quantum"                 -> Circular Queue
"Implement queue with O(1) ops"              -> Circular Queue or Deque
```

### 14.4 Queue Comparison Table (Master Reference)

| Type | Insert | Delete | Order | Backing | Typical Use |
|---|---|---|---|---|---|
| Simple Queue | Rear | Front | FIFO | Array/Linked List | General FIFO tasks |
| Circular Queue | Rear (wraps) | Front (wraps) | FIFO | Array | Fixed-capacity buffers, round-robin |
| Dynamic Queue | Rear (resizes) | Front (wraps) | FIFO | Array | Unbounded FIFO growth |
| Linked List Queue | Rear | Front | FIFO | Singly Linked List | Unbounded, no resize cost |
| Deque | Both | Both | Both-end | Doubly Linked List / Blocks | Sliding window, both-end access |
| Priority Queue | By priority | Highest priority | Priority order | Binary Heap | Scheduling, Top-K |
| Input Restricted Deque | Rear only | Both | Mixed | Doubly Linked List | Controlled entry, flexible exit |
| Output Restricted Deque | Both | Front only | Mixed | Doubly Linked List | Flexible entry, controlled exit |

### 14.5 Complexity Sheet (Master Reference)

| Structure | Enqueue | Dequeue | Peek | Search |
|---|---|---|---|---|
| `list` (misused) | O(1)* | O(n) | O(1) | O(n) |
| `deque` | O(1) | O(1) | O(1) | O(n) |
| Array/Circular Queue | O(1) | O(1) | O(1) | O(n) |
| Linked List Queue | O(1) | O(1) | O(1) | O(n) |
| Priority Queue (heap) | O(log n) | O(log n) | O(1) | O(n) |

\* amortized

### 14.6 Interview Cheat Sheet (Final)

1. Default to `deque` — justify why (O(1) both ends vs. O(n) `list.pop(0)`).
2. State the false-overflow problem when discussing array-based queues; pivot to circular indexing.
3. For BFS, say "mark visited at enqueue time" out loud.
4. For window max/min, say "monotonic deque, O(n) since each index pushed/popped once."
5. For Top-K / scheduling, say "priority queue via heap, O(log n) per operation."
6. For thread-safety, mention `queue.Queue`/`SimpleQueue` explicitly; for single-threaded, prefer `deque`/`heapq`.
7. Always state complexity **before** being asked.
8. Always mention at least one edge case (empty queue, single element, all-equal values) unprompted.

### 14.7 15-Minute Revision

- Read Section 12 (Cheat Sheets) top to bottom.
- Re-derive the circular queue index formulas from memory: `rear = (front + count) % capacity`, `front = (front + 1) % capacity`.
- Recite the monotonic deque invariant: "decreasing order of value, indices only, evict from back on smaller-value violation, evict from front on window-boundary violation."
- Skim the Pattern Recognition table (7.2) once.

### 14.8 1-Hour Revision

- Re-implement from scratch (no peeking): `ArrayQueue`, `CircularQueue`, `LinkedQueue`, `MinPriorityQueue` (Sections 4.1, 4.3, 4.2, 4.6).
- Solve one problem per pattern category: one BFS (e.g., Rotting Oranges), one monotonic deque (Sliding Window Maximum), one priority queue (Kth Largest Element), one design problem (Design Circular Queue).
- Review Common Mistakes (Section 11) end-to-end and confirm you can explain *why* each one is wrong, not just *that* it's wrong.
- Time yourself dry-running the sliding window maximum example (5.4) on a fresh array without looking at the table.

---

## FAQs

**Q: Is a `deque` the same as a queue?**
A: `deque` is a more general **double-ended** structure that can be *used as* a queue (via `append`/`popleft`), a stack (via `append`/`pop`), or a genuine both-ends structure. A "queue" is the restricted FIFO-only abstract concept; `deque` is one concrete, flexible tool that implements it (among other things).

**Q: Why doesn't Python have a built-in `Queue` class the way it has `list` or `dict`?**
A: Python instead offers purpose-specific tools: `collections.deque` for general-purpose fast queues, and the `queue` module for thread-safety and priority variants — giving flexibility rather than one-size-fits-all.

**Q: Is `queue.Queue` slower than `deque`?**
A: Yes, due to internal locking for thread-safety. Use `deque` in single-threaded code for better performance.

**Q: Can a queue be implemented without any built-in structure at all?**
A: Yes — Section 4.1/4.2 show pure array-index and linked-list implementations using only basic Python primitives.

**Q: What's the single most common Queue interview question?**
A: "Implement a Queue using two Stacks" and "Design a Circular Queue" are consistently among the most frequently asked — both are covered in full in this handbook (Sections 8.2 and 4.3).

---

