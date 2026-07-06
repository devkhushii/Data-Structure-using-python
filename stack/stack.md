# 📚 THE COMPLETE STACK HANDBOOK 


---

## 📑 Table of Contents

1. [Introduction to Stacks](#1-introduction-to-stacks)
2. [Stacks in Python](#2-stacks-in-python)
3. [Core Stack Operations](#3-core-stack-operations)
4. [Stack Implementations](#4-stack-implementations)
5. [Stack Patterns](#5-stack-patterns)
6. [Real-World Applications](#6-real-world-applications)
7. [Recognizing Stack Problems](#7-recognizing-stack-problems)
8. [Optimization Playbook (Brute → Optimal)](#8-optimization-playbook)
9. [Interview Preparation](#9-interview-preparation)
10. [Python-Specific Tips](#10-python-specific-tips)
11. [Common Mistakes](#11-common-mistakes)
12. [Cheat Sheets](#12-cheat-sheets)
13. [Practice Problem Bank](#13-practice-problem-bank)
14. [Final Revision Kit](#14-final-revision-kit)

---

## 1. Introduction to Stacks

### 1.1 What is a Stack?

A **Stack** is a linear data structure that stores elements in a specific order, allowing insertion and deletion **only from one end**, called the **top**.

> **Definition:** A Stack is an ordered collection of items following the **LIFO (Last In, First Out)** principle — the last element added is the first one removed.

### 1.2 Why Does the Stack Exist?

Programs constantly need to "remember where they came from" — a function call needs to know where to return, an editor needs to know the last action to undo, a parser needs to know which bracket is still open. Arrays and lists let you touch *any* element; a Stack **deliberately restricts** access to only the top, and that restriction is the whole point — it models "the most recent unfinished thing" cheaply and unambiguously, in O(1).

### 1.3 Intuition & Real-World Analogy

| Real World | Stack Equivalent |
|---|---|
| Stack of plates in a cafeteria | You take the top plate first |
| Pile of books on a desk | Last book placed is first picked up |
| Browser back button | Last page visited is the first you go back to |
| Undo in a text editor | Last action performed is first undone |
| Stack of trays | Bottom trays only accessible after top ones removed |

### 1.4 ASCII Visualization

```
        TOP →  [ 30 ]   <- last pushed, first to pop
               [ 20 ]
               [ 10 ]   <- first pushed, last to pop
               ┗━━━━┛
               BOTTOM
```

### 1.5 History

The stack concept traces back to the 1940s–1950s with early work on subroutine calling (Turing, von Neumann architectures) and was formalized as an abstract data type in the 1950s–60s alongside the development of compilers — the **call stack** was essential for handling nested and recursive procedure calls, and **stack-based (postfix/RPN)** evaluation was popularized by Friedrich L. Bauer and Klaus Samelson, and later famously used in Forth and HP calculators.

### 1.6 Characteristics

- LIFO ordering
- Access restricted to the top element only
- Dynamic or fixed size depending on implementation
- Supports push, pop, peek as primary operations
- No random access (unlike arrays)

### 1.7 Advantages

- O(1) insertion and deletion at the top
- Simple and predictable memory access pattern
- Naturally models recursive/nested structures
- Easy to reason about correctness (LIFO invariant)

### 1.8 Disadvantages

- No random access to middle elements — O(n) to reach them
- Fixed-size array implementations can overflow
- Not suitable when you need FIFO order (use a Queue instead)
- Searching is O(n)

### 1.9 Applications (Preview)

- Function call management (call stack, recursion)
- Expression evaluation & conversion (infix/postfix/prefix)
- Balanced parentheses / syntax checking
- Undo-Redo systems
- Browser history navigation
- Backtracking algorithms
- DFS traversal (iterative)
- Monotonic stack problems (Next Greater Element, histograms)

> **📝 Interview Note:** If an interviewer says "last operation should be undone first" or "match opening/closing pairs" or "look at the nearest previous/next greater element" — think **Stack** immediately.

---
## 2. Stacks in Python

Python has no built-in `Stack` class — you build one from existing containers. Three common approaches:

### 2.1 Using `list` as a Stack

```python
stack = []
stack.append(10)   # push
stack.append(20)
stack.append(30)
top = stack.pop()   # pop -> 30
peek = stack[-1]    # peek -> 20
is_empty = len(stack) == 0
```

**How it works internally:** A Python `list` is a dynamic array (over-allocated `PyObject*` array). `append()`/`pop()` at the **end** are amortized O(1) because Python over-allocates extra capacity and only reallocates/copies occasionally (growth pattern roughly 1.125x). Operating at the *front* of a list (`insert(0, x)`, `pop(0)`) is O(n) because every remaining element must shift — this is why **you must always push/pop from the end**, never the front.

```
Memory (list as dynamic array):
index:   0    1    2    3   [free][free]
value: [10] [20] [30] [ ]  [ ]   [ ]
                    ↑
                   top (stack[-1])
```

### 2.2 Using `collections.deque`

```python
from collections import deque
stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)
top = stack.pop()     # 30
peek = stack[-1]
```

`deque` is implemented as a **doubly linked list of fixed-size blocks**, giving true O(1) append/pop at **both** ends with no amortized copying — this is why `deque` is the officially recommended stack/queue structure in the Python docs when you need guaranteed O(1) performance and/or operations at both ends.

### 2.3 Custom Stack Class (encapsulated, safe)

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"
```

**Line-by-line:**
- `self._data = []` → internal storage, name-mangled with underscore to signal "private."
- `push` → simple `append`, O(1) amortized.
- `pop` → guards against underflow before delegating to list's `pop()`.
- `peek` → reads `[-1]` without removing, guards against empty access.
- `is_empty`/`size` → O(1) queries using `len()`.

### 2.4 `list` vs `deque` — Performance Comparison

| Feature | `list` | `collections.deque` |
|---|---|---|
| Push/pop at end | Amortized O(1) | True O(1) |
| Push/pop at front | O(n) | O(1) |
| Random access `stack[i]` | O(1) | O(n) |
| Memory overhead | Lower | Slightly higher (block pointers) |
| Thread-safety for append/pop | No | Yes (atomic for single append/pop) |
| Best for | Simple stack-only use | Stack + Queue hybrid, high-frequency push/pop |

### 2.5 Best Practices

- Prefer `list` for a **pure stack** with only end operations — it's simpler and has lower memory overhead.
- Prefer `deque` if you might also need queue-like behavior, or want documented O(1) guarantees.
- **Never** use `list.insert(0, x)` / `list.pop(0)` to simulate a stack — that's an O(n) anti-pattern.
- Wrap raw containers in a class (§2.3) in production code to prevent silent misuse (e.g., someone calling `.pop(0)` by mistake).
- Avoid using `queue.LifoQueue` unless you specifically need thread-safety with blocking semantics — it has more overhead than `list`/`deque` for single-threaded use.

---
## 3. Core Stack Operations

### 3.1 Operation Summary Table

| Operation | Description | Time | Space |
|---|---|---|---|
| `push(x)` | Insert `x` at the top | O(1) amortized | O(1) |
| `pop()` | Remove and return top element | O(1) amortized | O(1) |
| `peek()` / `top()` | Return top without removing | O(1) | O(1) |
| `is_empty()` | Check if stack has 0 elements | O(1) | O(1) |
| `is_full()` | Check capacity (fixed-size only) | O(1) | O(1) |
| `size()` | Number of elements | O(1) | O(1) |
| `clear()` | Remove all elements | O(1) (`list.clear()`) or O(n) | O(1) |
| `traverse()` | Visit every element | O(n) | O(1) |
| `search(x)` | Find position of `x` | O(n) | O(1) |

### 3.2 Push — Visualization

```
Before push(40):        After push(40):
   [ 30 ] <- top            [ 40 ] <- top
   [ 20 ]                   [ 30 ]
   [ 10 ]                   [ 20 ]
                             [ 10 ]
```

### 3.3 Pop — Visualization

```
Before pop():           After pop():  (returns 40)
   [ 40 ] <- top            [ 30 ] <- top
   [ 30 ]                   [ 20 ]
   [ 20 ]                   [ 10 ]
   [ 10 ]
```

### 3.4 Overflow & Underflow

```
UNDERFLOW (pop on empty stack)          OVERFLOW (push on full fixed stack)
   [ empty ]                               [ 10 ][ 20 ][ 30 ]  <- capacity = 3
     pop() → ERROR!                        push(40) → ERROR! (no room)
```

```python
def pop(self):
    if self.is_empty():
        raise IndexError("Stack Underflow: cannot pop from empty stack")
    return self._data.pop()

def push(self, item):
    if self.is_full():          # only relevant for fixed-capacity stacks
        raise OverflowError("Stack Overflow: capacity reached")
    self._data.append(item)
```

> **⚠️ Warning:** In Python, `list`/`deque` are dynamically sized, so true "overflow" rarely happens unless you enforce an artificial capacity limit (interview-style fixed-size stack questions) or actually run out of memory.

### 3.5 Traverse & Search — Dry Run

Searching for `20` in `[10, 20, 30]` (top = 30):

| Step | Stack (top→bottom view) | Current Element | Operation | Explanation |
|---|---|---|---|---|
| 1 | [30, 20, 10] | 30 | compare 30 == 20? No | move to next |
| 2 | [30, 20, 10] | 20 | compare 20 == 20? Yes | found at distance 1 from top |

```python
def search(stack_list, target):
    for distance, value in enumerate(reversed(stack_list), start=1):
        if value == target:
            return distance   # 1-indexed distance from top
    return -1
```

---
## 4. Stack Implementations

### 4.1 Array-Based Stack (Fixed Capacity)

**Problem:** Implement a stack with a fixed maximum capacity, raising errors on overflow/underflow.

**Approach:** Use a Python list as the backing array but enforce a `capacity` limit manually.

```python
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self._data = [None] * capacity
        self._top = -1                     # index of top element

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack Overflow")
        self._top += 1
        self._data[self._top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        item = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[self._top]
```

**Dry Run:** `push(5); push(8); pop(); push(3)` with capacity 3

| Step | Array | `_top` | Operation | Explanation |
|---|---|---|---|---|
| 0 | [None, None, None] | -1 | init | empty stack |
| 1 | [5, None, None] | 0 | push(5) | top moves to index 0 |
| 2 | [5, 8, None] | 1 | push(8) | top moves to index 1 |
| 3 | [5, None, None] | 0 | pop() → 8 | top moves back to 0 |
| 4 | [5, 3, None] | 1 | push(3) | top moves to index 1 |

**Complexity:** All ops O(1) time, O(capacity) space.
**When to use:** Interview questions that explicitly test overflow handling; embedded/fixed-memory contexts.
**When NOT to use:** General Python development — a plain `list` is simpler and dynamically sized.
**Common mistakes:** Forgetting to decrement/increment `_top`; not nulling out popped slots (minor memory-leak habit carried from C).

### 4.2 Linked-List-Based Stack

**Approach:** Each node points to the node below it; `top` is a pointer to the head node. Push/pop happen at the head — O(1), no shifting.

```python
class Node:
    __slots__ = ("value", "next")
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        self._top = Node(value, self._top)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        node = self._top
        self._top = node.next
        self._size -= 1
        return node.value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._top.value

    def is_empty(self):
        return self._top is None

    def size(self):
        return self._size
```

**ASCII:**
```
push(10) -> push(20) -> push(30)

top -> [30|•]--> [20|•]--> [10|None]
```

**Complexity:** O(1) push/pop/peek, O(n) space for n nodes (plus per-node pointer overhead).
**When to use:** When you need guaranteed no-resize O(1) behavior or are building stacks of unknown, potentially huge size without amortized copy spikes.
**When NOT to use:** When simplicity/memory efficiency matters more — Python lists have less per-element overhead than linked nodes.

### 4.3 Dynamic (Resizable) Stack — how Python's list already does this

```python
# Conceptual illustration of dynamic resizing (Python does this internally in C)
class DynamicArrayStack:
    def __init__(self):
        self._capacity = 4
        self._data = [None] * self._capacity
        self._size = 0

    def push(self, item):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)   # double capacity
        self._data[self._size] = item
        self._size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def pop(self):
        if self._size == 0:
            raise IndexError("Stack Underflow")
        self._size -= 1
        item = self._data[self._size]
        self._data[self._size] = None
        return item
```

Doubling capacity when full gives **amortized O(1)** push, since resizing (O(n)) happens exponentially less often as the stack grows — the same trick CPython uses for `list`.

### 4.4 Multiple Stacks in One Array

**Problem:** Implement `k` stacks using a single array efficiently.

**Approach (fixed division):** Divide the array into `k` equal blocks, each with its own top pointer.

```python
class KStacks:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.arr = [0] * n
        self.top = [-1] * k                 # top index for each stack, relative to its block
        self.block_size = n // k

    def push(self, stack_num, item):
        top = self.top[stack_num]
        if top + 1 >= self.block_size:
            raise OverflowError(f"Stack {stack_num} Overflow")
        top += 1
        self.arr[stack_num * self.block_size + top] = item
        self.top[stack_num] = top

    def pop(self, stack_num):
        top = self.top[stack_num]
        if top == -1:
            raise IndexError(f"Stack {stack_num} Underflow")
        item = self.arr[stack_num * self.block_size + top]
        self.top[stack_num] = top - 1
        return item
```

**Better approach (efficient, shared free list):** Use a single array plus a linked "next free index" list so stacks can grow into each other's unused space — avoids wasting fixed blocks. (Common as a follow-up interview question — mention it even if you implement the simple version first.)

### 4.5 Min Stack — O(1) `getMin()`

**Problem:** Design a stack supporting `push`, `pop`, `top`, and `getMin()` — all in O(1).

**Approach 1 (Auxiliary Stack):** Maintain a second stack that tracks the minimum at each level.

```python
class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []          # min_stack[i] = min of stack[0..i]

    def push(self, val):
        self._stack.append(val)
        current_min = val if not self._min_stack else min(val, self._min_stack[-1])
        self._min_stack.append(current_min)

    def pop(self):
        self._min_stack.pop()
        return self._stack.pop()

    def top(self):
        return self._stack[-1]

    def get_min(self):
        return self._min_stack[-1]
```

**Dry Run:** `push(5), push(3), push(7), getMin(), pop(), getMin()`

| Step | Stack | Min-Stack | Operation | getMin() result |
|---|---|---|---|---|
| 1 | [5] | [5] | push(5) | — |
| 2 | [5,3] | [5,3] | push(3) | — |
| 3 | [5,3,7] | [5,3,3] | push(7) | — |
| 4 | [5,3,7] | [5,3,3] | getMin() | 3 |
| 5 | [5,3] | [5,3] | pop() removes 7 | — |
| 6 | [5,3] | [5,3] | getMin() | 3 |

**Complexity:** O(1) all ops, O(n) extra space for min_stack.

**Approach 2 (Space-optimized, single stack storing differences):** Store `val - current_min` instead of `val` when `val < current_min`, updating a single `min_val` variable — reduces extra space to O(1) but is trickier to implement and reason about; use Approach 1 in interviews unless explicitly asked to optimize space.

### 4.6 Max Stack

Symmetric to Min Stack — maintain a parallel `max_stack` using `max()` instead of `min()`. Popular follow-up: support `popMax()` in O(n) with a plain second stack, or O(log n) using a balanced structure (advanced, rarely needed unless explicitly asked).

---
## 5. Stack Patterns

This is the section that matters most for interviews. Master these patterns and 90% of "stack problems" become recognizable templates.

### 5.1 Monotonic Stack — The Core Idea

A **monotonic stack** keeps its elements in strictly increasing or strictly decreasing order at all times. Whenever a new element would break that order, you **pop** elements until the order is restored — and each pop is the answer to some query ("who is my next greater element?").

```
Monotonic Decreasing Stack while scanning [4, 5, 2, 10]:

scan 4: stack = [4]
scan 5: 5 > 4 → pop 4 (4's "next greater" = 5) → stack = [5]
scan 2: 2 < 5 → push → stack = [5, 2]
scan 10: 10 > 2 → pop 2 (NGE=10); 10 > 5 → pop 5 (NGE=10) → stack = [10]
```

Because each element is pushed once and popped at most once, any monotonic stack scan is **O(n)** overall, even though it "looks like" nested loops.

### 5.2 Next Greater Element (NGE)

**Problem:** For each element, find the first element to its right that is strictly greater. If none exists, output -1.

**Brute Force:** For each `i`, scan rightwards until you find a greater element. O(n²).

**Optimal — Monotonic Decreasing Stack (store indices):**

```python
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []                      # stores indices, values are decreasing top→bottom... 
                                     # actually top is smallest unresolved
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result
```

**Dry Run** on `[2, 1, 2, 4, 3]`:

| Step | i | nums[i] | Stack (indices) | Action | result so far |
|---|---|---|---|---|---|
| 1 | 0 | 2 | [] → [0] | push 0 | [-1,-1,-1,-1,-1] |
| 2 | 1 | 1 | [0,1] | 1 < 2, push | [-1,-1,-1,-1,-1] |
| 3 | 2 | 2 | pop 1 (nums[1]=1<2) → result[1]=2; nums[0]=2 not < 2, stop; push 2 | [0,2] | [-1,2,-1,-1,-1] |
| 4 | 3 | 4 | pop 2 (2<4)→result[2]=4; pop 0 (2<4)→result[0]=4; push 3 | [3] | [4,2,4,-1,-1] |
| 5 | 4 | 3 | 3<4 stop; push 4 | [3,4] | [4,2,4,-1,-1] |
| end | — | — | remaining indices stay -1 | | [4,2,4,-1,-1] |

**Complexity:** O(n) time (amortized), O(n) space.

### 5.3 Previous Greater Element

Same idea, scanned left→right but comparing against a stack that represents "unresolved elements to the left":

```python
def previous_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        result[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return result
```

### 5.4 Next Smaller Element / Previous Smaller Element

Flip the comparison direction — use a **monotonic increasing stack**:

```python
def next_smaller_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

| Pattern | Stack Type | Comparison |
|---|---|---|
| Next Greater Element | Monotonic Decreasing | pop while `top < current` |
| Previous Greater Element | Monotonic Decreasing | pop while `top <= current` |
| Next Smaller Element | Monotonic Increasing | pop while `top > current` |
| Previous Smaller Element | Monotonic Increasing | pop while `top >= current` |

### 5.5 Parentheses / Bracket Matching

**Problem:** Determine if a string of brackets `(){}[]` is balanced.

**Approach:** Push opening brackets; on a closing bracket, pop and check it matches.

```python
def is_balanced(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False
        # ignore other characters
    return not stack
```

**Dry Run** on `"{[()]}"`:

| Step | Char | Stack | Explanation |
|---|---|---|---|
| 1 | `{` | [{] | push |
| 2 | `[` | [{,[] | push |
| 3 | `(` | [{,[,(] | push |
| 4 | `)` | [{,[] | pop `(`, matches |
| 5 | `]` | [{] | pop `[`, matches |
| 6 | `}` | [] | pop `{`, matches |
| end | — | [] empty | balanced ✅ |

**Complexity:** O(n) time, O(n) space.
**Edge cases:** empty string (balanced), unmatched closing first (`)(`), leftover openings (`(()`), non-bracket characters mixed in.

```
Visualization:
{ [ ( ) ] }
    ↑ ↑
    ├─┤ matched innermost first — this IS the LIFO property in action
```

### 5.6 Expression Evaluation & Conversion

#### 5.6.1 Infix, Prefix, Postfix — What They Are

| Notation | Example (`a + b`) | Operator Position |
|---|---|---|
| Infix | `a + b` | between operands |
| Prefix (Polish) | `+ a b` | before operands |
| Postfix (RPN) | `a b +` | after operands |

Postfix is preferred for machine evaluation because it needs **no parentheses and no precedence rules** — a single left-to-right scan with a stack evaluates it unambiguously.

#### 5.6.2 Evaluate Postfix Expression

```python
def evaluate_postfix(tokens):
    stack = []
    for tok in tokens:
        if tok.lstrip('-').isdigit():
            stack.append(int(tok))
        else:
            b = stack.pop()
            a = stack.pop()
            if tok == '+': stack.append(a + b)
            elif tok == '-': stack.append(a - b)
            elif tok == '*': stack.append(a * b)
            elif tok == '/': stack.append(int(a / b))   # truncate toward zero
    return stack[-1]
```

**Dry Run** on `["2", "3", "+", "4", "*"]` (= (2+3)*4 = 20):

| Step | Token | Stack | Explanation |
|---|---|---|---|
| 1 | "2" | [2] | push number |
| 2 | "3" | [2,3] | push number |
| 3 | "+" | [5] | pop 3,2 → 2+3=5, push |
| 4 | "4" | [5,4] | push number |
| 5 | "*" | [20] | pop 4,5 → 5*4=20, push |
| end | — | [20] | result = 20 |

#### 5.6.3 Infix → Postfix (Shunting-Yard, simplified)

```python
def infix_to_postfix(expr):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    right_assoc = {'^'}
    output, stack = [], []
    for token in expr.split():
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()                       # discard '('
        else:                                  # operator
            while (stack and stack[-1] != '(' and
                   (precedence[stack[-1]] > precedence[token] or
                    (precedence[stack[-1]] == precedence[token] and token not in right_assoc))):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output
```

**When to use:** Building calculators, compilers, expression parsers.
**Common mistakes:** Forgetting operator associativity for `^` (right-associative), mishandling unary minus, not discarding `(` after popping to `)`.

#### 5.6.4 Infix → Prefix

Reverse the infix expression (swapping `(`/`)`), convert to postfix, then reverse the result.

### 5.7 Next Greater Element II (Circular Array)

**Problem:** Same as NGE, but the array is circular.

**Approach:** Simulate circularity by iterating `2n` times using `i % n`.

```python
def next_greater_circular(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(2 * n):
        idx = i % n
        while stack and nums[stack[-1]] < nums[idx]:
            result[stack.pop()] = nums[idx]
        if i < n:
            stack.append(idx)
    return result
```

### 5.8 Largest Rectangle in Histogram

**Problem:** Given bar heights, find the area of the largest rectangle that fits under the skyline.

**Brute Force:** For each bar, expand left/right while bars are ≥ its height. O(n²).

**Optimal — Monotonic Increasing Stack:**

```python
def largest_rectangle_area(heights):
    stack = []                # indices, heights increasing bottom→top
    max_area = 0
    heights = heights + [0]   # sentinel to flush remaining bars
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
```

**Dry Run** on `[2, 1, 5, 6, 2, 3]`:

| Step | i | h | Stack (before pop) | Pops & area computed | max_area |
|---|---|---|---|---|---|
| 1 | 0 | 2 | [] | push 0 | 0 |
| 2 | 1 | 1 | [0] | pop 0 (h=2), width=1, area=2 | 2 |
| 3 | 1 | 1 | [] | push 1 | 2 |
| 4 | 2 | 5 | [1] | push 2 | 2 |
| 5 | 3 | 6 | [1,2] | push 3 | 2 |
| 6 | 4 | 2 | [1,2,3] | pop 3(h=6,w=1,area=6); pop 2(h=5,w=2,area=10) | 10 |
| 7 | 4 | 2 | [1] | push 4 | 10 |
| 8 | 5 | 3 | [1,4] | push 5 | 10 |
| 9 | 6 | 0(sentinel) | [1,4,5] | pop5(h=3,w=1,area=3); pop4(h=2,w=4,area=8); pop1(h=1,w=6,area=6) | 10 |

**Result: 10.** Complexity: O(n) time, O(n) space.
**When to use:** Any "largest rectangle / maximal area" skyline-style problem, including Maximal Rectangle in a binary matrix (apply this row-by-row).

### 5.9 Trapping Rain Water (Stack Approach)

```python
def trap(height):
    stack = []
    water = 0
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()
            if not stack:
                break
            width = i - stack[-1] - 1
            bounded_height = min(h, height[stack[-1]]) - height[bottom]
            water += width * bounded_height
        stack.append(i)
    return water
```

**Approach:** Monotonic decreasing stack of indices; when a taller bar appears, water sits above the popped "valley" bar, bounded by the shorter of the current bar and the new stack top.

### 5.10 Stock Span Problem

**Problem:** For each day's stock price, find how many consecutive previous days (including today) had price ≤ today's price.

```python
def stock_span(prices):
    n = len(prices)
    span = [1] * n
    stack = []                 # stores indices with decreasing price
    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    return span
```

**Dry Run** on `[100, 80, 60, 70, 60, 75, 85]`:

| Day(i) | Price | Stack after | Span |
|---|---|---|---|
| 0 | 100 | [0] | 1 |
| 1 | 80 | [0,1] | 1 |
| 2 | 60 | [0,1,2] | 1 |
| 3 | 70 | pop 2 → [0,1,3] | 2 |
| 4 | 60 | [0,1,3,4] | 1 |
| 5 | 75 | pop 4,3 → [0,1,5] | 4 |
| 6 | 85 | pop 5,1 → [0,6] | 6 |

Result: `[1,1,1,2,1,4,6]`. This is literally the "Next Greater Element to the left, as a distance" pattern.

### 5.11 Sliding Window Maximum (Deque as Monotonic Stack Variant)

Not a classic "stack" problem, but uses the same monotonic-deque idea — worth knowing since interviewers often ask "how is this related to monotonic stack?":

```python
from collections import deque
def max_sliding_window(nums, k):
    dq = deque()          # stores indices, decreasing values
    result = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

### 5.12 Recursion as an Implicit Stack

Every recursive call is pushed onto the **call stack**; returning pops it. Any recursive algorithm can be rewritten iteratively using an explicit stack — this equivalence is a favorite interview question ("convert this recursion to iteration").

```python
# Recursive factorial (uses the implicit call stack)
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative equivalent using an explicit stack
def factorial_iterative(n):
    stack = []
    while n > 1:
        stack.append(n)
        n -= 1
    result = 1
    while stack:
        result *= stack.pop()
    return result
```

```
Call stack visualization for factorial_recursive(4):

factorial(4)
 └─ factorial(3)
     └─ factorial(2)
         └─ factorial(1) → returns 1
     ← returns 2*1=2
 ← returns 3*2=6
← returns 4*6=24

Stack grows downward on each call, unwinds (pops) as each call returns.
```

---
## 6. Real-World Applications

### 6.1 Function Call Stack

Every function call frame (local variables, return address, parameters) is pushed onto the **call stack** when a function is invoked, and popped when it returns. Deep or unbounded recursion exhausts this stack, causing a **stack overflow** — in Python this surfaces as `RecursionError: maximum recursion depth exceeded`.

```python
import sys
print(sys.getrecursionlimit())   # default is usually 1000
```

### 6.2 Recursion

Recursion is simply "the programmer relying on the call stack to remember pending work" instead of maintaining an explicit stack. Anything recursive is convertible to an explicit-stack iterative version (§5.12) — useful when recursion depth would exceed Python's limit.

### 6.3 Undo / Redo

```python
class UndoRedo:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def do_action(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()          # new action invalidates redo history

    def undo(self):
        if not self.undo_stack:
            return None
        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        return action

    def redo(self):
        if not self.redo_stack:
            return None
        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        return action
```

**Why two stacks:** Undo needs LIFO access to past actions; redo needs LIFO access to *undone* actions, and a fresh action must clear the redo history (the "future" is invalidated the moment you do something new).

### 6.4 Browser History (Back/Forward)

```python
class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = [homepage]
        self.forward_stack = []

    def visit(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()

    def back(self):
        if len(self.back_stack) > 1:
            self.forward_stack.append(self.back_stack.pop())
        return self.back_stack[-1]

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.forward_stack.pop())
        return self.back_stack[-1]
```

### 6.5 Backtracking (Overview)

Backtracking algorithms (N-Queens, Sudoku solver, permutation generation) rely on the call stack to hold partial state so it can be "rolled back" (popped) when a branch fails — the stack IS the mechanism that makes backtracking possible, even though the topic itself belongs to a separate algorithms family.

### 6.6 DFS Traversal (Stack-Based, Iterative)

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in reversed(graph[node]):   # reversed to match recursive DFS order
                if neighbor not in visited:
                    stack.append(neighbor)
    return order
```

Contrast with BFS, which uses a **Queue** — this Stack-vs-Queue distinction (DFS vs BFS) is one of the most common conceptual interview questions.

### 6.7 Parsing & Syntax Checking

Compilers and interpreters use stacks for:
- Matching brackets/tags (HTML/XML tag validation, JSON/code bracket matching — §5.5)
- Operator precedence parsing (Shunting-Yard, §5.6.3)
- Tracking indentation levels (Python's own tokenizer uses a stack of indent levels internally)

```python
def is_valid_html_tags(tags):
    stack = []
    for tag in tags:
        if not tag.startswith('/'):
            stack.append(tag)
        else:
            if not stack or stack.pop() != tag[1:]:
                return False
    return not stack
```

---
## 7. Recognizing Stack Problems

### 7.1 Decision Tree

```
Does the problem involve...
│
├── Matching/nesting pairs (brackets, tags, "valid" structures)?
│   └── YES → Stack (push open, pop+match on close)   [§5.5]
│
├── "Last performed action" / undo / reverse-of-recent-order?
│   └── YES → Stack                                    [§6.3]
│
├── "Next/previous greater/smaller element" phrasing?
│   └── YES → Monotonic Stack                          [§5.2–5.4]
│
├── Largest rectangle / histogram / skyline / maximal area under bars?
│   └── YES → Monotonic Stack                          [§5.8]
│
├── Expression parsing (infix/postfix/prefix, calculator)?
│   └── YES → Stack                                    [§5.6]
│
├── Need DFS but iterative (avoid recursion depth limits)?
│   └── YES → Explicit Stack                           [§6.6]
│
├── Need FIFO (first-in-first-out) order instead?
│   └── NO to Stack → Use a Queue instead
│
└── Need random access to arbitrary elements?
    └── NO to Stack → Use an Array/List/Hash Map instead
```

### 7.2 Keyword Cheat Sheet

| Keyword / Phrase in Problem | Likely Pattern |
|---|---|
| "valid parentheses", "balanced" | Bracket Matching |
| "next greater", "next smaller" | Monotonic Stack |
| "span", "days until warmer" | Monotonic Stack (Stock Span family) |
| "largest rectangle", "histogram" | Monotonic Stack |
| "evaluate expression", "calculator" | Expression Stack |
| "undo", "redo", "back", "forward" | Two-Stack Pattern |
| "nested", "recursive structure flattening" | Explicit Stack Simulation |
| "min/max in O(1)" alongside stack ops | Min/Max Stack (auxiliary stack) |

---
## 8. Optimization Playbook

For every classic pattern, here's the progression from naive to optimal:

| Problem | Brute Force | Better | Optimal |
|---|---|---|---|
| Next Greater Element | O(n²) nested scan | — | O(n) monotonic stack |
| Balanced Parentheses | O(n²) repeated removal of `()`/`[]`/`{}` substrings | — | O(n) single-pass stack |
| Largest Rectangle in Histogram | O(n²) expand left/right per bar | O(n log n) divide & conquer | O(n) monotonic stack |
| Stock Span | O(n²) scan backwards per day | — | O(n) monotonic stack |
| Min Stack | O(n) scan for min on every query | — | O(1) with auxiliary min-stack |
| Evaluate Expression | Recursive descent parser (more complex) | — | O(n) postfix stack evaluation |
| Trapping Rain Water | O(n²) per-index min(maxLeft,maxRight) scan | O(n) two-pointer (no stack) | O(n) monotonic stack (also valid) |

> **📝 Interview Tip:** Always *state* the brute force first out loud, then explain *why* it's slow (repeated scanning = wasted work), and *then* introduce the stack — this shows the interviewer your reasoning process, not just a memorized answer.

---
## 9. Interview Preparation

### 9.1 Difficulty-Wise Question List

**Easy**
- Valid Parentheses (LeetCode 20)
- Implement Stack using Queues (LeetCode 225)
- Implement Queue using Stacks (LeetCode 232)
- Baseball Game (LeetCode 682)
- Backspace String Compare (LeetCode 844)
- Min Stack (LeetCode 155)
- Remove All Adjacent Duplicates In String (LeetCode 1047)

**Medium**
- Next Greater Element II (LeetCode 503)
- Daily Temperatures (LeetCode 739)
- Evaluate Reverse Polish Notation (LeetCode 150)
- Decode String (LeetCode 394)
- Asteroid Collision (LeetCode 735)
- Online Stock Span (LeetCode 901)
- Simplify Path (LeetCode 71)
- Basic Calculator II (LeetCode 227)
- Remove K Digits (LeetCode 402)
- Car Fleet (LeetCode 853)

**Hard**
- Largest Rectangle in Histogram (LeetCode 84)
- Maximal Rectangle (LeetCode 85)
- Trapping Rain Water (LeetCode 42)
- Basic Calculator (LeetCode 224)
- Longest Valid Parentheses (LeetCode 32)
- Number of Visible People in a Queue (LeetCode 1944)

### 9.2 Pattern-Wise Grouping

| Pattern | Representative Problems |
|---|---|
| Bracket Matching | Valid Parentheses, Longest Valid Parentheses, Remove Invalid Parentheses |
| Monotonic Stack (NGE family) | Next Greater Element I/II, Daily Temperatures, Online Stock Span |
| Histogram/Area | Largest Rectangle in Histogram, Maximal Rectangle, Trapping Rain Water |
| Expression Evaluation | Evaluate RPN, Basic Calculator I/II/III, Decode String |
| Design Problems | Min Stack, Implement Queue using Stacks, Implement Stack using Queues |
| String Simplification | Backspace String Compare, Remove Adjacent Duplicates, Simplify Path |

### 9.3 Company-Wise Tendencies (general trends, not guarantees)

| Company | Typical Focus |
|---|---|
| Amazon | Min Stack, Valid Parentheses, Simplify Path (unix-path style) |
| Google | Basic Calculator variants, Decode String, complex expression parsing |
| Microsoft | Asteroid Collision, Daily Temperatures, Next Greater Element |
| Meta | Valid Parentheses variants, Min Stack, Largest Rectangle in Histogram |
| Bloomberg | Basic Calculator, Expression Evaluation |

### 9.4 Blind 75 / NeetCode Stack Problems

- Valid Parentheses
- Min Stack
- Evaluate Reverse Polish Notation
- Generate Parentheses (uses backtracking + implicit stack via recursion)
- Daily Temperatures
- Car Fleet
- Largest Rectangle in Histogram

### 9.5 Interview Tricks

- If asked to "implement Queue using Stacks" or vice versa — know both the **two-stack amortized O(1)** and **single-stack recursive** tricks.
- For "Basic Calculator" family — always separate the *tokenizing* from the *evaluating*; use a stack for parentheses/sign-tracking, not for arithmetic precedence unless multiplication/division are involved (then combine with a running-result stack).
- When asked to detect the **pattern name** first, verbally connect it back to LIFO: "this needs to reference the most recently seen unmatched/unresolved element, so a stack fits."
- Always clarify empty-input and single-element edge cases before coding.

---
## 10. Python-Specific Tips

### 10.1 `list` vs `deque` — Decision Guide

```
Need stack only, small-to-medium size, simplicity matters?
   → use list

Need guaranteed O(1) at both ends, or stack+queue hybrid?
   → use collections.deque

Need thread-safe blocking stack (producer/consumer)?
   → use queue.LifoQueue
```

### 10.2 Performance Tips

- Avoid `list.insert(0, x)` / `list.pop(0)` — always O(n). Use `deque.appendleft()`/`popleft()` if front operations are needed.
- Preallocate capacity is not something Python lists expose directly, but you can hint by `list_ = [None] * n` if you know the max size in advance (fixed-size stack simulation).
- `len(stack) == 0` and `not stack` are both O(1); `not stack` is idiomatic Python and marginally faster/more Pythonic.
- Avoid unnecessary `copy.deepcopy()` of stack contents inside loops — it's O(n) per call and easily turns an O(n) algorithm into O(n²).

### 10.3 Memory Tips

- A Python list's `sys.getsizeof()` reflects allocated capacity, not just logical length — don't assume `len(stack)` equals memory footprint.
- `__slots__` on custom Node classes (as in §4.2) meaningfully cuts per-node memory overhead for linked-list-based stacks.
- Clearing a large stack with `stack.clear()` is O(1) reference-drop for the list container itself (Python then garbage-collects the freed objects), versus rebuilding `stack = []` which is also fine but creates a new list object.

### 10.4 Common Python Pitfalls

```python
# PITFALL 1: Using mutable default arguments as a "stack" — shared across calls!
def bad_stack(item, stack=[]):     # DANGEROUS — same list reused across all calls
    stack.append(item)
    return stack

def good_stack(item, stack=None):
    if stack is None:
        stack = []
    stack.append(item)
    return stack
```

```python
# PITFALL 2: Confusing pop() with pop(0)
stack = [1, 2, 3]
stack.pop()      # correct: removes 3 (O(1))
stack.pop(0)     # WRONG for a stack: removes 1 (O(n), breaks LIFO)
```

```python
# PITFALL 3: Checking emptiness with len() == 0 vs truthiness — both work,
# but forgetting to check at all before pop()/peek() causes IndexError.
if stack:            # Pythonic and safe
    top = stack[-1]
```

---
## 11. Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---|---|---|
| Popping from an empty stack | Raises `IndexError` / undefined behavior | Always check `is_empty()` first |
| Using `pop(0)` for stack behavior | O(n), breaks LIFO semantics silently if misused for FIFO | Use `pop()` (no arg) for stack top |
| Forgetting to push back after a failed match check | Corrupts stack state for subsequent operations | Design pop/check as a single atomic step, or push placeholders back explicitly if needed |
| Off-by-one in monotonic stack width calc | Wrong area/span results (§5.8, §5.10) | Carefully derive width as `i - stack[-1] - 1` (or similar) and verify via dry run |
| Mutable objects pushed without copying | Later mutation of the object changes what's "stored" in the stack retroactively | Push immutable values, or `copy.deepcopy()` when necessary |
| Ignoring overflow in fixed-capacity implementations | Silent data corruption or crash | Explicitly raise `OverflowError` when capacity is reached |
| Confusing recursion depth limits with actual algorithmic complexity | `RecursionError` mistaken for a logic bug | Convert to iterative + explicit stack for deep recursion (§5.12) |
| Not clearing the redo-stack on a new action (Undo/Redo) | Redo replays stale/incorrect future state | Always `.clear()` the redo stack on any new action (§6.3) |

---
## 12. Cheat Sheets

### 12.1 Operations Cheat Sheet

```python
stack = []
stack.append(x)        # push
stack.pop()             # pop (returns removed top)
stack[-1]               # peek
not stack               # is_empty check
len(stack)              # size
stack.clear()           # clear
```

### 12.2 Complexity Cheat Sheet

| Operation | list | deque | Linked-list stack |
|---|---|---|---|
| push | O(1)* | O(1) | O(1) |
| pop | O(1)* | O(1) | O(1) |
| peek | O(1) | O(1) | O(1) |
| search | O(n) | O(n) | O(n) |
| space | O(n) | O(n) | O(n) + pointer overhead |

*amortized

### 12.3 Pattern Cheat Sheet

| Pattern | Stack Type | Core Trick |
|---|---|---|
| Bracket Matching | plain stack | push open, pop+compare on close |
| Next Greater Element | decreasing monotonic | pop while `top < current` |
| Next Smaller Element | increasing monotonic | pop while `top > current` |
| Largest Rectangle in Histogram | increasing monotonic | pop → compute width via new stack top |
| Stock Span | decreasing monotonic | span = distance to last greater element |
| Expression Evaluation (postfix) | plain stack | push operands, pop 2 on operator |
| Min/Max Stack | auxiliary stack | parallel stack tracks running min/max |
| Undo/Redo | two stacks | redo cleared on new action |

### 12.4 Recognition Cheat Sheet

See §7.2 keyword table — keep it pinned during mock interviews.

### 12.5 Python Syntax Cheat Sheet

```python
from collections import deque
dq = deque()
dq.append(x)       # push right
dq.pop()           # pop right
dq.appendleft(x)   # push left
dq.popleft()       # pop left

import queue
lifo = queue.LifoQueue()
lifo.put(x)
lifo.get()
```

---
## 13. Practice Problem Bank

### 13.1 Basics

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Implement Stack | GeeksforGeeks | Easy | Basics | geeksforgeeks.org/stack-data-structure |
| Implement Stack using Array | Code360 | Easy | Basics | naukri.com/code360 |
| Implement Two Stacks in an Array | GeeksforGeeks | Medium | Multiple Stacks | geeksforgeeks.org |
| Design a stack that supports getMin() in O(1) | LeetCode 155 | Medium | Min Stack | leetcode.com/problems/min-stack |
| Implement Queue using Stacks | LeetCode 232 | Easy | Design | leetcode.com/problems/implement-queue-using-stacks |
| Implement Stack using Queues | LeetCode 225 | Easy | Design | leetcode.com/problems/implement-stack-using-queues |

### 13.2 Monotonic Stack

| Problem | Platform | Difficulty | Concept | Link |
|---|---|---|---|---|
| Next Greater Element I | LeetCode 496 | Easy | NGE | leetcode.com/problems/next-greater-element-i |
| Next Greater Element II | LeetCode 503 | Medium | Circular NGE | leetcode.com/problems/next-greater-element-ii |
| Daily Temperatures | LeetCode 739 | Medium | NGE variant | leetcode.com/problems/daily-temperatures |
| Online Stock Span | LeetCode 901 | Medium | Stock Span | leetcode.com/problems/online-stock-span |
| Car Fleet | LeetCode 853 | Medium | Monotonic Stack | leetcode.com/problems/car-fleet |
| Sum of Subarray Minimums | LeetCode 907 | Medium | Monotonic Stack | leetcode.com/problems/sum-of-subarray-minimums |
| Remove K Digits | LeetCode 402 | Medium | Monotonic Stack | leetcode.com/problems/remove-k-digits |

### 13.3 Parentheses / Matching

| Problem | Platform | Difficulty | Concept | Link |
|---|---|---|---|---|
| Valid Parentheses | LeetCode 20 | Easy | Bracket Matching | leetcode.com/problems/valid-parentheses |
| Longest Valid Parentheses | LeetCode 32 | Hard | Bracket Matching | leetcode.com/problems/longest-valid-parentheses |
| Generate Parentheses | LeetCode 22 | Medium | Backtracking + Stack | leetcode.com/problems/generate-parentheses |
| Remove Invalid Parentheses | LeetCode 301 | Hard | BFS + Stack validation | leetcode.com/problems/remove-invalid-parentheses |
| Check for Balanced Parentheses | GeeksforGeeks | Easy | Bracket Matching | geeksforgeeks.org |
| Minimum Add to Make Parentheses Valid | LeetCode 921 | Medium | Bracket Matching | leetcode.com/problems/minimum-add-to-make-parentheses-valid |

### 13.4 Expressions

| Problem | Platform | Difficulty | Concept | Link |
|---|---|---|---|---|
| Evaluate Reverse Polish Notation | LeetCode 150 | Medium | Postfix Eval | leetcode.com/problems/evaluate-reverse-polish-notation |
| Basic Calculator | LeetCode 224 | Hard | Expression Eval | leetcode.com/problems/basic-calculator |
| Basic Calculator II | LeetCode 227 | Medium | Expression Eval | leetcode.com/problems/basic-calculator-ii |
| Basic Calculator III | LeetCode 772 | Hard | Expression Eval | leetcode.com/problems/basic-calculator-iii |
| Decode String | LeetCode 394 | Medium | Nested Stack Decode | leetcode.com/problems/decode-string |
| Infix to Postfix | GeeksforGeeks | Medium | Conversion | geeksforgeeks.org |
| Prefix to Infix | GeeksforGeeks | Medium | Conversion | geeksforgeeks.org |

### 13.5 Next Greater / Smaller Family

Covered in §13.2 (grouped for interview prep) — additionally:

| Problem | Platform | Difficulty | Concept | Link |
|---|---|---|---|---|
| 132 Pattern | LeetCode 456 | Medium | Monotonic Stack | leetcode.com/problems/132-pattern |
| Next Greater Node in Linked List | LeetCode 1019 | Medium | Monotonic Stack | leetcode.com/problems/next-greater-node-in-linked-list |

### 13.6 Histogram / Area

| Problem | Platform | Difficulty | Concept | Link |
|---|---|---|---|---|
| Largest Rectangle in Histogram | LeetCode 84 | Hard | Monotonic Stack | leetcode.com/problems/largest-rectangle-in-histogram |
| Maximal Rectangle | LeetCode 85 | Hard | Histogram row-by-row | leetcode.com/problems/maximal-rectangle |
| Trapping Rain Water | LeetCode 42 | Hard | Monotonic Stack | leetcode.com/problems/trapping-rain-water |

### 13.7 Min Stack / Design Problems

| Problem | Platform | Difficulty | Concept | Link |
|---|---|---|---|---|
| Min Stack | LeetCode 155 | Medium | Auxiliary Stack | leetcode.com/problems/min-stack |
| Max Stack | LeetCode 716 | Hard | Auxiliary Stack | leetcode.com/problems/max-stack |
| Design a Stack With Increment Operation | LeetCode 1381 | Medium | Design | leetcode.com/problems/design-a-stack-with-increment-operation |
| Dinner Plate Stacks | LeetCode 1172 | Hard | Multiple Stacks | leetcode.com/problems/dinner-plate-stacks |

### 13.8 More Practice Across Platforms

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Stack Permutations (Check if an array is a stack permutation of another) | GeeksforGeeks | Medium | Simulation |
| Celebrity Problem | GeeksforGeeks / InterviewBit | Medium | Stack Elimination |
| Simplify Path (Unix-style) | LeetCode 71 | Medium | Stack Simulation |
| Asteroid Collision | LeetCode 735 | Medium | Stack Simulation |
| Backspace String Compare | LeetCode 844 | Easy | Stack Simulation |
| Baseball Game | LeetCode 682 | Easy | Stack Simulation |
| Remove All Adjacent Duplicates In String | LeetCode 1047 | Easy | Stack Simulation |
| Remove All Adjacent Duplicates in String II | LeetCode 1209 | Medium | Stack with counts |
| Exclusive Time of Functions | LeetCode 636 | Medium | Call Stack Simulation |
| Number of Visible People in a Queue | LeetCode 1944 | Hard | Monotonic Stack |
| CSES: Stack Sequence problems | CSES | Varies | Simulation |
| Codeforces: "Stack" tagged problems | Codeforces | Varies | Search tag `data structures` + `stacks` |
| AtCoder: ABC problems tagged stack/queue | AtCoder | Varies | Search by tag |

> **Note:** Always verify exact links on the platform since problem numbering and URLs can shift over time — search the problem name directly on the platform if a link doesn't resolve.

---
## 14. Final Revision Kit

### 14.1 One-Page Notes

- Stack = LIFO. Only the top is accessible.
- Python: `list` (simple) or `deque` (guaranteed O(1) both ends).
- Core ops: push, pop, peek, is_empty — all O(1).
- Monotonic stack = O(n) trick for "next/previous greater/smaller" and histogram-style problems.
- Two-stack pattern = undo/redo, browser history, implement queue with stacks.
- Recursion = implicit stack; convert to explicit stack to avoid `RecursionError`.
- Auxiliary stack = O(1) min/max tracking.

### 14.2 Mind Map (ASCII)

```
                              STACK
                                │
      ┌────────────┬───────────┼────────────┬─────────────┐
      │            │           │            │             │
  Implementation  Operations  Patterns  Applications   Design
      │            │           │            │             │
  list/deque/   push/pop/   Monotonic   Call Stack    Min/Max Stack
  linked-list    peek        Stack       Recursion     Two-Stack
                             Brackets    Undo/Redo     Multi-Stack
                             Expressions DFS
                             Histogram   Parsing
```

### 14.3 Pattern Map

```
"next/prev greater/smaller"      → Monotonic Stack
"balanced / valid brackets"      → Plain Stack, push-open/pop-match
"largest rectangle / histogram"  → Monotonic Increasing Stack
"evaluate expression"            → Postfix stack evaluation
"min/max in O(1)"                → Auxiliary stack
"undo/redo, back/forward"        → Two-stack pattern
"iterative DFS"                  → Explicit stack, LIFO traversal
```

### 14.4 Formula / Complexity Sheet

| Structure | Push | Pop | Peek | Space |
|---|---|---|---|---|
| list-based stack | O(1)* | O(1)* | O(1) | O(n) |
| deque-based stack | O(1) | O(1) | O(1) | O(n) |
| linked-list stack | O(1) | O(1) | O(1) | O(n) + overhead |

*amortized

### 14.5 Interview Cheat Sheet (Say This Out Loud)

> "This needs LIFO access to the most recent unresolved element, so I'll use a stack. If it's asking for next/previous greater or smaller elements, I'll make it a monotonic stack so each element is pushed and popped at most once, giving O(n) overall instead of O(n²)."

### 14.6 15-Minute Revision

1. Re-read §12 Cheat Sheets in full (5 min).
2. Re-derive Next Greater Element from memory (3 min).
3. Re-derive Valid Parentheses from memory (2 min).
4. Skim §7 Decision Tree + §7.2 keyword table (3 min).
5. Say the Interview Cheat Sheet line (§14.5) out loud (2 min).

### 14.7 1-Hour Revision

| Time | Activity |
|---|---|
| 0–10 min | Re-read §1–2 (fundamentals + Python stack options) |
| 10–25 min | Re-implement Min Stack, Valid Parentheses, and NGE from scratch, no peeking |
| 25–40 min | Re-derive Largest Rectangle in Histogram with a fresh dry run |
| 40–50 min | Solve 2 problems from §13.2 (Monotonic Stack) live, timed |
| 50–60 min | Review §11 Common Mistakes + §9.5 Interview Tricks |

---

## FAQs

**Q: Is a stack the same as a call stack?**
A: The "call stack" is one specific *use* of the stack data structure — the one your language runtime maintains automatically for function calls. The general "Stack" concept is broader and can be used for anything requiring LIFO access.

**Q: Why is `deque` recommended over `list` for stacks in the Python docs?**
A: Because `deque` guarantees O(1) for operations at both ends with no amortized resizing, whereas `list` operations at the end are only *amortized* O(1) (occasional O(n) resize copies) and operations at the front are O(n).

**Q: When should I use a Min Stack instead of just calling `min(stack)`?**
A: When you need repeated O(1) minimum queries interleaved with pushes/pops — `min(stack)` is O(n) every call, which turns an otherwise O(n) algorithm into O(n²) if called in a loop.

**Q: Can every recursive algorithm be converted to use an explicit stack?**
A: Yes — recursion is just the language runtime managing an implicit stack for you; anything recursive can be rewritten iteratively with a manual stack, which is useful to sidestep Python's recursion depth limit.

**Q: What's the difference between a Stack and a Queue?**
A: Stack = LIFO (top-only access); Queue = FIFO (access at both front and back, remove from front). Use a Queue for BFS, task scheduling, and any "process in arrival order" scenario, and Python's `collections.deque` can implement both.

