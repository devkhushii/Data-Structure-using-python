# 🐍 The Python for DSA Handbook
---

## 📖 Table of Contents

1. [Python Fundamentals for DSA](#1-python-fundamentals-for-dsa)
2. [Operators](#2-operators)
3. [Control Flow](#3-control-flow)
4. [Functions](#4-functions)
5. [Built-in Data Types](#5-built-in-data-types)
6. [Python Collections Module](#6-python-collections-module)
7. [Standard Library for DSA](#7-standard-library-for-dsa)
8. [Iterators & Generators](#8-iterators--generators)
9. [Comprehensions](#9-comprehensions)
10. [Functional Programming](#10-functional-programming)
11. [Object-Oriented Concepts for DSA](#11-object-oriented-concepts-for-dsa)
12. [Memory & Performance](#12-memory--performance)
13. [Competitive Programming in Python](#13-competitive-programming-in-python)
14. [Python Idioms](#14-python-idioms)
15. [Common Built-in Functions Reference](#15-common-built-in-functions-reference)
16. [Complexity Tables (Master Reference)](#16-complexity-tables-master-reference)
17. [Debugging](#17-debugging)
18. [Python Pitfalls](#18-python-pitfalls)
19. [Best Practices](#19-best-practices)
20. [Problem Recognition — What Structure to Use When](#20-problem-recognition--what-structure-to-use-when)
21. [Cheat Sheets](#21-cheat-sheets)
22. [Practice Problems](#22-practice-problems)
23. [Final Revision — Mind Maps & Quick Recall](#23-final-revision--mind-maps--quick-recall)

---

# 1. Python Fundamentals for DSA

## 1.1 Variables — Names, Not Boxes

**Definition:** A variable in Python is not a memory box that holds a value — it's a **name (label) bound to an object living somewhere on the heap**.

**Why it exists:** DSA code constantly reassigns pointers/references (linked list `next`, tree `left`/`right`, sliding-window pointers). Understanding that variables are *labels* explains why reassignment doesn't mutate the original object, and why two names can point to the same list.

**Intuition (name → object model):**

```
CPython variable model
=======================

   x = [1, 2, 3]

   Namespace                Heap
   ┌─────────┐        ┌────────────────┐
   │  x  ────┼───────▶│ list object    │
   └─────────┘        │ id: 0x7f2a10   │
                       │ refcount: 1    │
                       │ [1, 2, 3]      │
                       └────────────────┘

   y = x        # y is now ANOTHER LABEL on the SAME object

   ┌─────────┐        ┌────────────────┐
   │  x  ────┼───┬───▶│ list object    │
   ├─────────┤   │    │ refcount: 2    │
   │  y  ────┼───┘    │ [1, 2, 3]      │
   └─────────┘        └────────────────┘
```

**Syntax:**

```python
x = 10              # binding, not "storage"
x = "now a string"  # rebinding — old int object may be garbage collected
a = b = c = 5       # chained assignment — all point to the SAME int object
```

**Interview Tip:** When asked "is Python pass-by-value or pass-by-reference?" — the correct answer is **pass-by-object-reference** (also called "call by sharing"): the reference is copied, not the object.

**Common Mistake:**
```python
def append_one(lst):
    lst = lst + [1]   # rebinds local name -> caller's list unaffected

def append_one_correct(lst):
    lst.append(1)     # mutates the SAME object -> caller's list affected
```

---

## 1.2 Data Types & Objects

**Everything in Python is an object** — `int`, `float`, `function`, `class`, even `type` itself. Every object has:

| Property | Description | DSA Relevance |
|---|---|---|
| **Identity** | Unique id (`id(obj)`), effectively memory address in CPython | Detecting aliasing, cycle detection |
| **Type** | Fixed for life (`type(obj)`) | Type-checking in polymorphic problems |
| **Value** | May or may not be mutable | Determines hashability, safe defaults |

```python
x = 42
print(id(x), type(x), x)
```

---

## 1.3 References, Identity vs Equality

**`==` checks value equality. `is` checks identity (same object in memory).**

```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b   # True  -> same contents
a is b   # False -> different objects

c = a
c is a   # True  -> same object
```

**ASCII Diagram:**
```
a ──▶ [1,2,3]  (id: 100)
b ──▶ [1,2,3]  (id: 200)      a == b -> True,  a is b -> False
c ──┘ (points to id:100)       c is a -> True
```

> **Interview Tip:** Always use `is` for `None`, `True`, `False` checks (`if x is None`), never `==`. Using `is` for numbers/strings beyond small cached values is undefined behavior across implementations (see Integer Caching in §12).

---

## 1.4 Mutable vs Immutable Types

| Immutable | Mutable |
|---|---|
| `int`, `float`, `bool`, `complex` | `list` |
| `str` | `dict` |
| `tuple` (if elements immutable) | `set` |
| `frozenset` | `bytearray` |
| `bytes` | custom objects (by default) |

**Why this matters for DSA:**
- Only **immutable, hashable** objects can be dict keys / set elements.
- Mutable default arguments are a classic bug source (§18).
- Strings being immutable means `s += char` in a loop is **O(n) per operation** → O(n²) total; use `list` + `''.join()` instead.

**Memory diagram — mutation vs rebinding:**
```
IMMUTABLE (str)                    MUTABLE (list)
================                   ===============
s = "abc"                          lst = [1, 2]
s ──▶ "abc" (id:1)                 lst ──▶ [1, 2] (id:5)

s += "d"   # NEW object created    lst.append(3)  # SAME object mutated
s ──▶ "abcd" (id:2)                lst ──▶ [1, 2, 3] (id:5)   <- id unchanged
   (id:1 now unreferenced)
```

---

## 1.5 Type Conversion

```python
int("42")        # 42          str -> int
int(3.99)        # 3           truncates toward zero, NOT round
float("3.14")    # 3.14
str(123)         # "123"
list("abc")      # ['a','b','c']
tuple([1,2,3])   # (1, 2, 3)
set([1,1,2])     # {1, 2}
bool(0), bool("")# False, False   -- falsy values
bool([]), bool({})# False, False
```

**Falsy values in Python:** `False`, `None`, `0`, `0.0`, `''`, `[]`, `{}`, `set()`, `()`.

**Common Mistake:** `int("3.14")` raises `ValueError` — must go through `float()` first: `int(float("3.14"))`.

---

## 1.6 Input / Output for DSA

```python
# Single integer
n = int(input())

# Space-separated integers on one line
arr = list(map(int, input().split()))

# Multiple values
a, b = map(int, input().split())

# n lines of input
grid = [input() for _ in range(n)]

# Fast I/O for competitive programming (see §13)
import sys
data = sys.stdin.read().split()
```

**Output:**
```python
print(x)                          # default: adds newline
print(x, end="")                  # no newline
print(*arr)                       # space-separated unpack
print(*arr, sep=",")              # custom separator
print("\n".join(map(str, arr)))   # fastest for many lines
```

---

## 1.7 Comments & Naming Conventions (PEP 8 essentials)

```python
# Single line comment
"""
Multi-line docstring / block comment
"""
```

| Convention | Example | Use |
|---|---|---|
| `snake_case` | `max_profit`, `left_ptr` | variables, functions |
| `PascalCase` | `TreeNode`, `UnionFind` | classes |
| `UPPER_CASE` | `MOD = 10**9+7` | constants |
| `_leading_underscore` | `_helper()` | "private"/internal convention |
| `dunder__` | `__init__`, `__len__` | magic/special methods |

---

# 2. Operators

## 2.1 Arithmetic Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Add | `3 + 2` | `5` |
| `-` | Subtract | `3 - 2` | `1` |
| `*` | Multiply | `3 * 2` | `6` |
| `/` | True division (always float) | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Modulo | `7 % 2` | `1` |
| `**` | Exponent | `2 ** 10` | `1024` |
| `-x` | Unary negation | `-5` | `-5` |

**Critical DSA gotcha — floor division with negatives:**
```python
7 // 2    # 3
-7 // 2   # -4   (floors toward -infinity, NOT toward zero!)
-7 % 2    # 1    (result has sign of divisor)
```
```
Number line for -7 // 2:
... -4    -3.5    -3 ...
     ▲ floor here (rounds DOWN, away from 0)
```
> **Interview Tip:** For "round toward zero" (like C++/Java integer division), use `int(a / b)` or `math.trunc(a / b)` — not `//` when negatives are involved.

**Modulo for hashing / cyclic indexing:**
```python
MOD = 10**9 + 7
result = (a * b) % MOD          # always keep intermediate values bounded
idx = (i + 1) % n                # circular buffer / circular array indexing
```

## 2.2 Comparison Operators

`==  !=  >  <  >=  <=` — work element-wise-lexicographically on sequences:
```python
[1,2,3] < [1,2,4]   # True (lexicographic comparison)
"abc" < "abd"        # True
(1,2) == (1,2)       # True — tuples compare by value
```

## 2.3 Assignment Operators

```python
x = 5
x += 1   # x = x + 1
x -= 1
x *= 2
x //= 2
x **= 2
x %= 3
x &= mask   # bitwise-and assign
x |= mask
x ^= mask
x <<= 1
x >>= 1
```

## 2.4 Logical Operators

```python
a and b   # returns a if falsy, else b  (short-circuits)
a or b    # returns a if truthy, else b (short-circuits)
not a
```

**Idiom — default value via `or`:**
```python
name = user_input or "default"   # falls back if user_input is falsy
```
⚠️ **Pitfall:** this fails if `0` or `""` are *valid* intended values — use `is None` check instead when zero/empty are legitimate.

## 2.5 Membership & Identity Operators

```python
3 in [1,2,3]        # True   -> O(n) for list, O(1) avg for set/dict
"a" in "cat"         # True   -> substring check
x is None
x is not None
```

> **Interview Tip:** If you do repeated `in` checks, **convert list → set first**: turns O(n) per lookup into O(1) average, changing total complexity from O(n·q) to O(n+q).

## 2.6 Bitwise Operators

| Op | Meaning | Example |
|---|---|---|
| `&` | AND | `5 & 3 = 1` |
| `\|` | OR | `5 \| 3 = 7` |
| `^` | XOR | `5 ^ 3 = 6` |
| `~` | NOT (invert) | `~5 = -6` |
| `<<` | Left shift | `1 << 4 = 16` |
| `>>` | Right shift | `16 >> 2 = 4` |

```
Bit tricks cheat-sheet:
  n & (n-1)      -> removes lowest set bit
  n & (-n)       -> isolates lowest set bit
  n | (n+1)      -> sets lowest unset bit
  n ^ n = 0,  n ^ 0 = n
  check power of 2:  n > 0 and (n & (n-1)) == 0
  count set bits:    bin(n).count('1')  or  n.bit_count()  (3.10+)
  swap without temp: a, b = b, a   (Pythonic; XOR swap is NOT idiomatic here)
```

Python integers are **arbitrary precision** — no overflow, but `~`, `<<` on negative numbers use Python's own two's-complement-like infinite-bit model, which differs subtly from fixed-width C/Java behavior. Be careful porting bit-manipulation tricks from C++.

## 2.7 Ternary (Conditional Expression)

```python
result = "even" if n % 2 == 0 else "odd"
max_val = a if a > b else b
```

## 2.8 Walrus Operator `:=` (3.8+)

Assigns and returns a value **within an expression** — very handy in DSA loops.

```python
# Without walrus
n = len(arr)
while n > 0:
    ...

# With walrus - avoids duplicate computation
while (n := len(stack)) > 0:
    process(stack.pop())

# Classic use: avoid calling a function twice
if (result := expensive_check(x)) is not None:
    use(result)

# In comprehensions
filtered = [y for x in data if (y := transform(x)) > 0]
```

## 2.9 Operator Precedence (high → low, DSA-relevant subset)

```
1. ()                          grouping
2. **                          exponent (right-assoc)
3. +x, -x, ~x                  unary
4. *, /, //, %                 
5. +, -                        
6. <<, >>                      
7. &                           
8. ^                           
9. |                           
10. ==, !=, <, <=, >, >=, is, in
11. not
12. and
13. or
14. if-else (ternary)
15. :=                         (walrus — lowest, always parenthesize)
```
> **Tip:** When mixing bitwise and comparison (`if x & 1 == 0`), add explicit parens: `if (x & 1) == 0` — `==` binds tighter than `&`, a classic Python gotcha ported from C mental models.

---

# 3. Control Flow

## 3.1 if / elif / else

```python
if n < 0:
    sign = -1
elif n == 0:
    sign = 0
else:
    sign = 1
```

**Chained comparison (Pythonic, unique to Python):**
```python
if 0 <= i < n:          # equivalent to: 0 <= i and i < n
    ...
if a < b < c < d:
    ...
```

## 3.2 for loops

Python's `for` iterates over **any iterable** (not index-based like C).

```python
for x in [1, 2, 3]:
    print(x)

for i in range(n):              # index-based
    print(i)

for i, x in enumerate(arr):     # index + value
    print(i, x)

for a, b in zip(arr1, arr2):    # parallel iteration
    print(a, b)

for k, v in d.items():          # dict iteration
    print(k, v)
```

## 3.3 while loops

```python
left, right = 0, n - 1
while left <= right:
    mid = (left + right) // 2
    ...
```

## 3.4 break, continue, pass

```python
for x in arr:
    if x < 0:
        continue    # skip this iteration
    if x == target:
        break       # exit loop entirely
    pass            # no-op placeholder
```

## 3.5 The `for...else` / `while...else` clause (underused, DSA-relevant!)

The `else` block runs **only if the loop completed WITHOUT hitting `break`.** Extremely useful for search patterns.

```python
def has_pair_with_sum(arr, target):
    seen = set()
    for x in arr:
        if target - x in seen:
            print("Found!")
            break
        seen.add(x)
    else:
        print("Not found")   # runs only if loop never broke
```

```
Flow:
  for ...:
      if condition: break ──────┐
  else: ◀── runs only if NO break│
      (normal completion)        │
  (code after loop) ◀────────────┘ (skips else, jumps here)
```

## 3.6 match-case (3.10+, structural pattern matching)

```python
def describe(x):
    match x:
        case 0:
            return "zero"
        case int() if x < 0:
            return "negative int"
        case [a, b]:
            return f"pair: {a},{b}"
        case [a, *rest]:
            return f"head {a}, rest {rest}"
        case {"type": "circle", "radius": r}:
            return f"circle r={r}"
        case _:
            return "unknown"
```
Useful for state-machine simulation problems, tree/JSON traversal, and command dispatch.

## 3.7 Nested loops & labeled-break simulation

Python has **no `break` with labels** (unlike Java). Common workarounds:

```python
# 1. Flag variable
found = False
for i in range(n):
    for j in range(m):
        if grid[i][j] == target:
            found = True
            break
    if found:
        break

# 2. Function + return (cleanest)
def search(grid, target):
    for row in grid:
        for val in row:
            if val == target:
                return True
    return False

# 3. itertools.product to flatten
from itertools import product
for i, j in product(range(n), range(m)):
    if grid[i][j] == target:
        break
```
> **Interview Tip:** Wrapping nested loops in a function and using `return` is the cleanest, most Pythonic "labeled break."


# 4. Functions

## 4.1 Function Definition & Parameters

```python
def add(a, b):              # positional parameters
    return a + b

def greet(name="World"):    # default argument
    return f"Hello, {name}"

def total(*args):           # variable positional args -> tuple
    return sum(args)

def config(**kwargs):       # variable keyword args -> dict
    return kwargs

def full(a, b, *args, c=10, **kwargs):   # everything combined
    ...
```

**Call-site variations:**
```python
add(1, 2)              # positional
add(a=1, b=2)           # keyword
add(b=2, a=1)           # order doesn't matter with keywords

nums = [1, 2, 3]
total(*nums)             # unpack list as positional args

d = {"name": "Alice"}
greet(**d)                # unpack dict as keyword args
```

## 4.2 Positional-only & Keyword-only params (3.8+)

```python
def f(a, b, /, c, d, *, e, f):
    #    ▲ pos-only  ▲normal  ▲kw-only
    ...
# a, b: MUST be positional
# e, f: MUST be keyword
```

## 4.3 Return Values

```python
def divmod_custom(a, b):
    return a // b, a % b     # returns a TUPLE (multiple return values)

q, r = divmod_custom(7, 2)   # unpacked automatically
```
A function with no `return` (or bare `return`) returns `None`.

## 4.4 Scope — LEGB Rule

**L**ocal → **E**nclosing → **G**lobal → **B**uilt-in

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)          # "local"
    inner()
    print(x)               # "enclosing"

print(x)                    # "global"
```

## 4.5 global and nonlocal

```python
counter = 0
def increment():
    global counter
    counter += 1              # modifies the GLOBAL name

def make_counter():
    count = 0
    def increment():
        nonlocal count        # modifies ENCLOSING (not global) name
        count += 1
        return count
    return increment
```

## 4.6 Lambda (anonymous functions)

```python
square = lambda x: x * x
add = lambda a, b: a + b

# Most common DSA use: custom sort keys
arr.sort(key=lambda x: (-x[1], x[0]))    # sort by 2nd desc, 1st asc
```
> Lambdas are restricted to a **single expression** — no statements, no assignments (pre-3.8), no multi-line logic. Use a full `def` for anything complex.

## 4.7 Recursion Basics

```python
def factorial(n):
    if n <= 1:               # base case — MUST exist
        return 1
    return n * factorial(n - 1)   # recursive case, moves toward base case
```

```
Call stack visualization for factorial(4):

factorial(4)
 └─ factorial(3)
     └─ factorial(2)
         └─ factorial(1) -> returns 1
     returns 2 * 1 = 2
 returns 3 * 2 = 6
returns 4 * 6 = 24

Stack frames (LIFO):
┌───────────────┐
│ factorial(1)  │ <- top, executes/returns first
├───────────────┤
│ factorial(2)  │
├───────────────┤
│ factorial(3)  │
├───────────────┤
│ factorial(4)  │ <- bottom, called first
└───────────────┘
```

⚠️ Python has **no tail-call optimization** — deep recursion (>1000 by default) raises `RecursionError`. See §13 for `sys.setrecursionlimit`.

## 4.8 Closures

A closure is a function that **remembers variables from its enclosing scope**, even after that scope has finished executing.

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor      # 'factor' is captured from enclosing scope
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
double(5)   # 10
triple(5)   # 15
```

**Classic late-binding closure pitfall (see §18 for full detail):**
```python
funcs = [lambda: i for i in range(3)]
[f() for f in funcs]   # [2, 2, 2]  NOT [0, 1, 2]! closures capture by reference
```

## 4.9 Higher-Order Functions

Functions that take/return other functions:
```python
def apply_twice(f, x):
    return f(f(x))

apply_twice(lambda x: x + 3, 10)   # 16
sorted(words, key=len)              # len is passed as a function
```

## 4.10 Decorators (Basics)

A decorator wraps a function to extend its behavior without modifying its source.

```python
import functools
import time

def timer(func):
    @functools.wraps(func)          # preserves original __name__/__doc__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter()-start:.6f}s")
        return result
    return wrapper

@timer
def slow_fib(n):
    return n if n < 2 else slow_fib(n-1) + slow_fib(n-2)
```

```
Decorator flow:
  @timer
  def slow_fib(n): ...

  is equivalent to:
  slow_fib = timer(slow_fib)

  Call slow_fib(10)
     │
     ▼
  wrapper(10)  <- this is what actually runs now
     │
     ├─ start timer
     ├─ call original slow_fib(10)  <- the real logic
     ├─ stop timer, print
     ▼
  return result
```

**Most useful decorator for DSA: `functools.lru_cache`** (memoization) — covered in §7.4.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```
This turns exponential recursion O(2ⁿ) into linear O(n) via automatic memoization.

---

# 5. Built-in Data Types

## 5.1 `int` — Arbitrary Precision Integers

**Internal working:** Unlike C/Java's fixed 32/64-bit ints, Python ints are **arbitrary precision** (limited only by memory), stored as an array of "digits" in base 2³⁰ (implementation detail, `PyLongObject`). This means no integer overflow — a huge advantage for big-number DSA problems (factorial of 100, big Fibonacci, etc.) but arithmetic on very large ints is technically no longer strict O(1).

```python
x = 10 ** 100          # works fine, no overflow
y = 2 ** 1000           # still exact
```

**Integer Caching:** CPython pre-allocates and caches small integers `-5` to `256`. `a = 5; b = 5; a is b` → `True`. Beyond this range, `is` comparisons are unreliable (§12.3).

**Complexity:** For "reasonably sized" numbers that fit in a machine word, all ops are O(1) amortized. For huge numbers, `+`/`-` are O(d), `*` is O(d^1.585) (Karatsuba) or better, where d = number of digits.

## 5.2 `float` — IEEE-754 Double Precision

```python
0.1 + 0.2                 # 0.30000000000000004  -- binary floating point imprecision
round(0.1 + 0.2, 2)       # 0.3
math.isclose(0.1+0.2, 0.3)  # True -- correct way to compare floats
```
⚠️ **Never use `==` to compare floats** in DSA correctness checks — use `math.isclose()` or an epsilon.

## 5.3 `bool`

`bool` is a **subclass of `int`** (`True == 1`, `False == 0`). This lets you sum booleans directly:
```python
count_positive = sum(x > 0 for x in arr)    # bools summed as ints
isinstance(True, int)    # True
```

## 5.4 `complex`

Rarely used in DSA except geometry/FFT-adjacent problems.
```python
z = 3 + 4j
abs(z)          # 5.0  (magnitude)
z.real, z.imag  # 3.0, 4.0
```

## 5.5 `str` — Immutable Unicode Sequence

**Internal working:** Strings are immutable arrays of Unicode code points. CPython uses flexible string representation (1/2/4 bytes per char depending on max code point) — so operations are still effectively O(n) but memory-efficient.

**Key operations & complexity:**

| Operation | Example | Complexity |
|---|---|---|
| Indexing | `s[i]` | O(1) |
| Slicing | `s[a:b]` | O(b-a) |
| Concatenation | `s1 + s2` | O(len(s1)+len(s2)) |
| `in` (substring) | `"ab" in s` | O(n·m) worst case |
| `len(s)` | | O(1) (cached) |
| `s.find/index` | | O(n) |
| `s.split()` | | O(n) |
| `s.join(iterable)` | | O(total chars) |
| `s.replace()` | | O(n) |
| `s.upper/lower()` | | O(n) |
| `s == s2` | | O(n) worst case |

```python
s = "hello world"
s[0]              # 'h'
s[-1]              # 'd'
s[0:5]             # 'hello'
s[::-1]            # 'dlrow olleh' -- reverse via slicing
s.split()          # ['hello', 'world']
"-".join(["a","b"]) # 'a-b'
s.strip()           # remove leading/trailing whitespace
s.replace('l', 'L')
s.count('l')        # 3
ord('a'), chr(97)   # 97, 'a'
s.isalpha(), s.isdigit(), s.isalnum()
f"{s.upper()}"       # f-strings for formatting
```

**String Building — the O(n²) trap:**
```python
# BAD: O(n²) -- each += creates a new string, copying all previous chars
result = ""
for c in chars:
    result += c

# GOOD: O(n) -- list append is amortized O(1), join is O(n) once
result = []
for c in chars:
    result.append(c)
result = "".join(result)
```
```
Why += is O(n²):
Iteration 1: "a"                 (copy 1 char)
Iteration 2: "ab"                (copy 2 chars: old "a" + new "b")
Iteration 3: "abc"               (copy 3 chars)
...
Iteration n: copy n chars
Total copies: 1+2+...+n = O(n²)
```

## 5.6 `list` — Dynamic Array

**Internal working:** A CPython `list` is a **dynamic array of pointers** to objects (not a linked list!). It over-allocates capacity so `append` is amortized O(1).

```
List memory layout:
┌────────────────────────────────┐
│ PyListObject                    │
│  ob_size = 3      (length)      │
│  allocated = 8    (capacity)    │
│  ob_item ──────┐                │
└────────────────┼────────────────┘
                  ▼
         ┌────┬────┬────┬───┬───┬───┬───┬───┐
         │ p1 │ p2 │ p3 │ - │ - │ - │ - │ - │   <- array of POINTERS
         └─┬──┴─┬──┴─┬──┴───┴───┴───┴───┴───┘
           ▼    ▼    ▼
          [10] [20] [30]      <- actual int objects elsewhere on heap
```

**Growth pattern (over-allocation):** When capacity is exceeded, CPython grows the array by roughly **1.125x + a constant** (not doubling exactly) — this amortizes the cost of resizing across many appends, giving O(1) amortized `append`.

```
Resize on overflow:
append() when full:
  [1,2,3,4] (cap=4, full)
       │  append(5)
       ▼
  allocate NEW larger array (cap ~8)
  copy all 4 old pointers -> new array   (O(n) this ONE time)
  insert new pointer at index 4
  [1,2,3,4,5,_,_,_] (cap=8)
```

**Complexity Table:**

| Operation | Complexity | Notes |
|---|---|---|
| `lst[i]` (index) | O(1) | direct pointer access |
| `lst[i] = x` | O(1) | |
| `lst.append(x)` | O(1) amortized | |
| `lst.pop()` | O(1) | removes from END |
| `lst.pop(0)` | O(n) | shifts ALL elements left |
| `lst.insert(i, x)` | O(n) | shifts elements |
| `del lst[i]` | O(n) | shifts elements |
| `x in lst` | O(n) | linear scan |
| `lst.index(x)` | O(n) | |
| `lst.sort()` | O(n log n) | Timsort, stable |
| `lst.reverse()` | O(n) | in-place |
| `len(lst)` | O(1) | cached |
| slicing `lst[a:b]` | O(b-a) | creates new list (copy) |
| `lst.count(x)` | O(n) | |
| `+` concatenation | O(n+m) | new list |
| `*` repetition | O(n*k) | |

```python
lst = [1, 2, 3]
lst.append(4)          # [1,2,3,4]
lst.extend([5,6])       # [1,2,3,4,5,6] -- adds each element (vs append which adds the list itself)
lst.insert(0, 0)         # [0,1,2,3,4,5,6]
lst.pop()                 # removes+returns last: 6
lst.pop(0)                 # removes+returns first: 0 -- O(n)!
lst.remove(3)               # removes FIRST occurrence of value 3
lst.sort(reverse=True)       # in-place sort
sorted(lst)                   # returns NEW sorted list
lst.reverse()                  # in-place reverse
lst[::-1]                       # reversed COPY (non-destructive)
lst.copy()  # or lst[:]           # shallow copy
```

> **Interview Tip:** `append` vs `extend` is a top interview gotcha:
> `[1,2].append([3,4])` → `[1, 2, [3, 4]]` (nested!)
> `[1,2].extend([3,4])` → `[1, 2, 3, 4]` (flattened)

## 5.7 `tuple` — Immutable Fixed Sequence

```python
t = (1, 2, 3)
single = (5,)          # trailing comma REQUIRED for single-element tuple
t[0]                     # 1  -- O(1) indexing, same as list
```
**Why tuples exist for DSA:**
1. **Hashable** (if elements are hashable) → usable as dict keys / set elements — e.g., `visited = set()`; `visited.add((r, c))` for grid coordinates.
2. Slightly more memory-efficient than lists (no over-allocation).
3. Signal intent: "this data shouldn't change" (e.g., returning multiple values).

```python
memo = {}
def solve(i, j):
    key = (i, j)                 # tuple as dict key -- classic memoization pattern
    if key in memo:
        return memo[key]
    ...
```

**Complexity:** Same as list for read operations (O(1) index, O(n) `in`), but no mutating methods (`append`, `sort`, etc. don't exist).

## 5.8 `set` — Hash-Based Unique Collection

**Internal working:** Implemented as an open-addressing hash table (like `dict` but no values). Elements must be hashable.

```
Set/hashing model:
   add(42)
      │
      ▼
   hash(42) = 42          (for small ints, hash(x) == x)
      │
      ▼
   bucket_index = hash(42) % table_size
      │
      ▼
┌───┬───┬───┬───┬───┬───┬───┬───┐
│ - │ - │42 │ - │ - │ - │ - │ - │   <- open addressing hash table
└───┴───┴───┴───┴───┴───┴───┴───┘
  0   1   2   3   4   5   6   7

On collision -> probe next slot (open addressing, not chaining)
```

**Complexity Table:**

| Operation | Average | Worst Case |
|---|---|---|
| `x in s` | O(1) | O(n) (hash collisions) |
| `s.add(x)` | O(1) | O(n) |
| `s.remove(x)` / `s.discard(x)` | O(1) | O(n) |
| `s1 \| s2` (union) | O(len(s1)+len(s2)) | |
| `s1 & s2` (intersection) | O(min(len(s1),len(s2))) | |
| `s1 - s2` (difference) | O(len(s1)) | |
| `s1 ^ s2` (symmetric diff) | O(len(s1)+len(s2)) | |
| `s1 <= s2` (subset) | O(len(s1)) | |

```python
s = {1, 2, 3}
s.add(4)
s.discard(5)      # no error if missing
s.remove(5)        # KeyError if missing
s1 | s2             # union
s1 & s2              # intersection
s1 - s2               # difference
s1 ^ s2                # symmetric difference
s1.issubset(s2)
s1.issuperset(s2)
frozenset({1,2,3})     # immutable, hashable version -- can be a dict key / set element
```
> **Interview Tip:** Convert list to set for O(1) membership: turns "two sum" style brute force O(n²) into O(n).

## 5.9 `dict` — Hash Map

**Internal working:** Since Python 3.7+, dicts maintain **insertion order** (guaranteed by language spec, not just implementation detail). Implemented as a compact hash table: a separate dense array holds entries (key, hash, value) in insertion order, and a sparse hash table holds indices into that array.

```
Modern dict layout (compact dict, 3.6+):
  Hash table (sparse, indices only):
  ┌────┬────┬────┬────┬────┬────┐
  │ -1 │  1 │ -1 │  0 │ -1 │  2 │   <- index into entries[] or -1 (empty)
  └────┴────┴────┴────┴────┴────┘

  Entries (dense, INSERTION ORDER preserved):
  ┌───────────────────┬───────────────────┬───────────────────┐
  │ hash,'b',2          │ hash,'a',1         │ hash,'c',3         │
  └───────────────────┴───────────────────┴───────────────────┘
     entries[0]              entries[1]           entries[2]
```

**Complexity Table:**

| Operation | Average | Worst Case |
|---|---|---|
| `d[k]` get/set | O(1) | O(n) |
| `k in d` | O(1) | O(n) |
| `del d[k]` | O(1) | O(n) |
| `d.get(k, default)` | O(1) | O(n) |
| `d.keys()/values()/items()` | O(1) to create view | iterating is O(n) |
| `len(d)` | O(1) | |
| `dict(sorted(d.items()))` | O(n log n) | |

```python
d = {"a": 1, "b": 2}
d["c"] = 3                    # insert/update
d.get("z", 0)                  # 0 -- safe access with default, no KeyError
d.setdefault("d", []).append(1) # get-or-initialize idiom
del d["a"]
d.pop("b", None)                 # remove with default (no error if missing)
"a" in d                          # membership -- checks KEYS
for k, v in d.items(): ...
for k in d: ...                    # iterates keys by default
sorted(d.items(), key=lambda kv: kv[1])   # sort by value
{v: k for k, v in d.items()}         # invert dict (dict comprehension)
```

**Dict comprehension for frequency counting:**
```python
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
# Better: use collections.Counter (§6.1)
```

## 5.10 `frozenset`

Immutable, hashable version of `set`. Use when you need a set that must itself be a dict key or set member.
```python
fs = frozenset([1, 2, 3])
cache = {frozenset([1,2]): "result"}
```

## 5.11 `bytes` and `bytearray`

Rare in classic DSA but appear in string/encoding-heavy problems and low-level bit manipulation.
```python
b = b"hello"          # immutable byte sequence
ba = bytearray(b"hi")  # mutable
ba[0] = 72              # mutate in place
```

## 5.12 Data Type Selection Summary

| Need | Use |
|---|---|
| Ordered, mutable sequence | `list` |
| Ordered, immutable, hashable | `tuple` |
| Unique elements, O(1) membership | `set` |
| Key-value mapping, O(1) lookup | `dict` |
| Immutable set (as dict key) | `frozenset` |
| Counting frequencies | `collections.Counter` |
| FIFO/queue, O(1) both ends | `collections.deque` |
| Insertion-order-safe map w/ defaults | `collections.defaultdict` |

# 6. Python Collections Module

The `collections` module provides specialized container datatypes that outperform or extend the built-ins for common DSA patterns.

## 6.1 `Counter` — Multiset / Frequency Table

**Definition:** A `dict` subclass for counting hashable objects. Missing keys return `0` instead of raising `KeyError`.

```python
from collections import Counter

c = Counter("abracadabra")
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

c['z']                    # 0 -- no KeyError!
c.most_common(2)          # [('a', 5), ('b', 2)] -- top-k frequent
c.most_common()            # all, sorted by count desc

c2 = Counter([1,1,2,3,3,3])
c + c2                       # add counts (elementwise, drops <=0)
c - c2                        # subtract counts (drops <=0, NOT negative!)
c & c2                         # min of counts (intersection multiset)
c | c2                          # max of counts (union multiset)

list(c.elements())               # expand back to element stream
c.update("xyz")                   # add more counts
c.subtract("aa")                   # subtract counts (allows negative)
```

**Dry run — `most_common(2)` on `"abracadabra"`:**
```
Counter counts: a:5, b:2, r:2, c:1, d:1
Sort by count desc (stable, ties keep insertion order):
  a(5), b(2), r(2), c(1), d(1)
Take first 2 -> [('a',5), ('b',2)]
```

**Complexity:** Build is O(n). `most_common(k)` is O(n log k) via heap internally (or O(n log n) if k is None). Arithmetic ops (`+`, `-`, `&`, `|`) are O(n+m).

**Interview Tip:** `Counter(a) == Counter(b)` is the cleanest anagram check:
```python
def is_anagram(a, b):
    return Counter(a) == Counter(b)
```

## 6.2 `defaultdict` — Auto-Initializing Dict

**Definition:** A `dict` subclass where missing keys are auto-created using a **factory function**, eliminating manual `if key not in d` checks.

```python
from collections import defaultdict

graph = defaultdict(list)
graph[1].append(2)          # no KeyError; auto-creates [] first
graph[1].append(3)
# graph = {1: [2, 3]}

count = defaultdict(int)
for x in arr:
    count[x] += 1            # auto-initializes to 0

groups = defaultdict(list)
for word in words:
    groups[len(word)].append(word)     # group by length

nested = defaultdict(lambda: defaultdict(int))   # multi-level defaultdict
nested["a"]["b"] += 1
```

**Internal working:** On `d[key]` miss, `__missing__` is called, which invokes `default_factory()` (no args), stores the result under `key`, and returns it.

⚠️ **Pitfall:** Simply *reading* `d[missing_key]` **inserts it** into the dict (side effect!). Use `.get()` if you don't want insertion.

**Complexity:** Same O(1) average as `dict` for all operations.

## 6.3 `deque` — Double-Ended Queue

**Definition:** A doubly-linked list of fixed-size blocks, giving **O(1) append/pop from BOTH ends** — unlike `list`, which is O(n) at the front.

```
deque internal structure (block-based doubly linked list):
┌──────┐    ┌──────┐    ┌──────┐
│block1│◀──▶│block2│◀──▶│block3│
│[1,2,3]    │[4,5,6]    │[7,8,_]
└──────┘    └──────┘    └──────┘
 ▲                              ▲
 appendleft() O(1)      append() O(1)
```

```python
from collections import deque

dq = deque([1,2,3])
dq.append(4)          # [1,2,3,4]      O(1)
dq.appendleft(0)       # [0,1,2,3,4]    O(1)
dq.pop()                 # removes+returns 4  O(1)
dq.popleft()               # removes+returns 0  O(1)
dq.rotate(1)                 # rotate right by 1  O(k)
dq.rotate(-1)                  # rotate left by 1
dq[0], dq[-1]                    # O(1) access at ends; O(n) for middle index!
deque(maxlen=3)                    # BOUNDED deque -- auto-evicts oldest on overflow
```

**Complexity Table:**

| Operation | Complexity |
|---|---|
| `append` / `appendleft` | O(1) |
| `pop` / `popleft` | O(1) |
| `dq[i]` (middle index) | O(n) |
| `rotate(k)` | O(k) |
| `x in dq` | O(n) |

**DSA use cases:**
- **BFS queue** (always use `deque`, never `list.pop(0)` which is O(n)).
- **Sliding window maximum** via monotonic deque.
- **Bounded history / LRU-ish buffer** via `maxlen`.

```python
# BFS template
from collections import deque
def bfs(graph, start):
    visited = {start}
    q = deque([start])
    while q:
        node = q.popleft()          # O(1) -- critical for BFS performance
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)
```

## 6.4 `OrderedDict`

Pre-3.7, dicts didn't guarantee order — `OrderedDict` did. Since 3.7+ regular `dict` preserves insertion order too, so `OrderedDict` is now mainly useful for:
- `move_to_end(key, last=True/False)` — O(1) reordering, perfect for **LRU cache implementation**.
- Order-sensitive equality (`OrderedDict` compares order too; plain `dict` doesn't).

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)     # mark as recently used -- O(1)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)   # evict LEAST recently used -- O(1)
```
This is THE canonical Python LRU Cache interview solution.

## 6.5 `ChainMap`

Groups multiple dicts into a single logical view (searches each mapping in order without merging/copying).
```python
from collections import ChainMap
defaults = {"color": "blue"}
overrides = {"color": "red"}
combined = ChainMap(overrides, defaults)
combined["color"]     # "red" -- first mapping wins
```
Occasionally used for scope-simulation problems (nested environments, symbol tables).

## 6.6 `namedtuple`

Creates lightweight, immutable, **field-named** tuple subclasses — more readable than raw tuples for structured data (e.g., graph edges, points, intervals).

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
p.x, p.y            # 1, 2  -- readable field access
p[0], p[1]            # 1, 2  -- still tuple-indexable
x, y = p               # still unpacks like a tuple

Edge = namedtuple("Edge", "u v weight")
edges = [Edge(0,1,4), Edge(1,2,3)]
edges.sort(key=lambda e: e.weight)     # Kruskal's-style sorting
```
**Why use it over plain tuple/class:** Same memory footprint & speed as a tuple (no `__dict__` overhead), but self-documenting field access — great tradeoff for interview code clarity without the overhead of a full class.

## 6.7 `UserDict`, `UserList`, `UserString`

Wrapper classes designed for **subclassing** when you need custom container behavior — safer than subclassing `dict`/`list`/`str` directly because internal CPython methods sometimes bypass overridden methods on the built-ins.

```python
from collections import UserList

class SortedList(UserList):
    def append(self, item):
        self.data.append(item)
        self.data.sort()

sl = SortedList([3, 1, 2])
sl.append(0)     # self.data -> [0,1,2,3], stays sorted
```
Rarely needed in interviews but occasionally useful for building custom data structure wrappers with extra invariants (e.g., an auto-sorted container, a case-insensitive string).

## 6.8 Collections Module — Complexity & Selection Cheat Sheet

| Type | Best For | Key Ops O(1) |
|---|---|---|
| `Counter` | Frequency counting, anagrams, top-k | `+`,`-`,`most_common` |
| `defaultdict` | Graphs (adjacency list), grouping | auto-init access |
| `deque` | BFS queues, sliding window, stacks needing both ends | append/pop both ends |
| `OrderedDict` | LRU cache | `move_to_end`, `popitem(last=False)` |
| `namedtuple` | Structured immutable records (edges, points) | field access |
| `ChainMap` | Layered/scoped lookups | — |

# 7. Standard Library for DSA

## 7.1 `math` — Mathematical Functions

```python
import math

math.sqrt(16)          # 4.0
math.isqrt(17)          # 4  -- INTEGER square root, exact, no float error (crucial for DSA!)
math.gcd(12, 18)          # 6
math.lcm(4, 6)              # 12  (3.9+)
math.factorial(5)             # 120
math.floor(3.7), math.ceil(3.2)  # 3, 4
math.trunc(-3.7)                  # -3  (toward zero, unlike //)
math.log2(1024)                     # 10.0
math.log(x, base)
math.pow(2, 10)                       # 1024.0 (float!) -- prefer ** for int results
math.inf, -math.inf                    # infinity sentinels for "unreached" states
math.isnan(x), math.isclose(a, b)
math.comb(n, r)                          # nCr -- combinations count (3.8+)
math.perm(n, r)                           # nPr -- permutations count (3.8+)
math.hypot(x, y)                           # euclidean distance
math.pi, math.e
```
> **Interview Tip:** Use `math.isqrt` instead of `int(math.sqrt(x))` — the float version can be off by one for large perfect squares due to floating-point rounding.

**`float('inf')` as sentinel — extremely common DSA idiom:**
```python
best = float('inf')            # for minimization problems
for x in candidates:
    best = min(best, cost(x))

worst = float('-inf')           # for maximization problems
```

## 7.2 `itertools` — Iterator Building Blocks

The single most powerful module for combinatorial/DSA problems — all functions are **lazy** (generators), so memory-efficient.

```python
import itertools as it

# --- Infinite iterators ---
it.count(10, 2)             # 10, 12, 14, ... (start, step) -- infinite
it.cycle([1,2,3])            # 1,2,3,1,2,3,... -- infinite
it.repeat(5, 3)                # 5,5,5

# --- Combinatorics (THE big DSA hitters) ---
list(it.permutations([1,2,3]))          # all orderings, len n! -- [(1,2,3),(1,3,2),...]
list(it.permutations([1,2,3], 2))        # length-2 permutations
list(it.combinations([1,2,3], 2))         # [(1,2),(1,3),(2,3)] -- order doesn't matter
list(it.combinations_with_replacement([1,2,3], 2))  # [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
list(it.product([0,1], repeat=3))          # all 2^3 binary strings -- [(0,0,0),(0,0,1),...]
list(it.product([1,2],[3,4]))               # cartesian product [(1,3),(1,4),(2,3),(2,4)]

# --- Grouping & filtering ---
list(it.groupby("aaabbbcc"))                  # [('a',iter),('b',iter),('c',iter)] -- consecutive runs ONLY
[(k, list(g)) for k, g in it.groupby("aaabbbcc")]
list(it.accumulate([1,2,3,4]))                  # [1,3,6,10] -- running sum (prefix sums!)
list(it.accumulate([1,2,3,4], func=max))          # running max: [1,2,3,4]
list(it.accumulate([1,2,3,4], initial=100))         # [100,101,103,106,110]

list(it.chain([1,2],[3,4]))                    # flatten multiple iterables: [1,2,3,4]
list(it.chain.from_iterable([[1,2],[3,4]]))     # same, from a single iterable-of-iterables
list(it.compress([1,2,3,4], [1,0,1,0]))           # [1,3] -- select by boolean mask
list(it.dropwhile(lambda x: x<3, [1,2,3,4,1]))     # [3,4,1] -- drop until predicate false, then take rest
list(it.takewhile(lambda x: x<3, [1,2,3,4,1]))      # [1,2] -- take until predicate false
list(it.filterfalse(lambda x: x%2==0, range(10)))    # odd numbers only
list(it.islice(range(100), 5, 10))                     # [5,6,7,8,9] -- lazy slicing of any iterable
list(it.pairwise([1,2,3,4]))                             # [(1,2),(2,3),(3,4)]  (3.10+)
list(it.starmap(pow, [(2,3),(3,2)]))                       # [8, 9] -- unpacks each tuple as args
```

**Dry run — `combinations([1,2,3,4], 2)`:**
```
Generates in lexicographic order relative to input:
(1,2) (1,3) (1,4) (2,3) (2,4) (3,4)
Total = C(4,2) = 6 combinations
Complexity: O(C(n,r)) to generate, each tuple O(r) to produce
```

**`groupby` gotcha:** It only groups **consecutive** equal elements — you almost always need `sorted()` first if you want ALL occurrences grouped:
```python
data = [("a",1),("b",2),("a",3)]
# WRONG grouping (a appears twice, not merged) unless pre-sorted:
data.sort(key=lambda x: x[0])
grouped = {k: list(g) for k, g in it.groupby(data, key=lambda x: x[0])}
```

**`accumulate` = prefix sums in one line:**
```python
prefix = list(it.accumulate(arr))          # prefix[i] = sum(arr[0..i])
range_sum = prefix[r] - (prefix[l-1] if l > 0 else 0)
```

## 7.3 `functools` — Higher-Order & Caching Tools

```python
from functools import lru_cache, cache, reduce, partial, cmp_to_key, wraps

@lru_cache(maxsize=None)          # memoization -- classic DP-via-recursion tool
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

@cache                              # 3.9+ -- shorthand for lru_cache(maxsize=None)
def f(n): ...

reduce(lambda a, b: a + b, [1,2,3,4])          # 10 -- cumulative reduction
reduce(lambda a, b: a * b, [1,2,3,4], 1)         # 24 -- with initial value

double = partial(lambda a, b: a*b, 2)              # freezes first argument -- double(5)=10

# cmp_to_key -- convert legacy C-style comparator to a sort key (for complex custom orderings)
def compare(a, b):
    if a + b > b + a: return -1
    elif a + b < b + a: return 1
    return 0
arr.sort(key=cmp_to_key(compare))     # classic "largest number" formation problem
```

**`lru_cache` internal working:** Maintains a dict mapping `(args, frozenset(kwargs))` → result, plus a doubly-linked list for LRU eviction order. `cache_info()` reports hits/misses.

```python
fib.cache_info()     # CacheInfo(hits=.., misses=.., maxsize=.., currsize=..)
fib.cache_clear()
```

⚠️ **Pitfall:** Arguments to an `lru_cache`d function must be **hashable** — lists/dicts as args will raise `TypeError`.

## 7.4 `heapq` — Binary Min-Heap on a List

**Internal working:** `heapq` operates directly on a plain Python `list`, maintaining the **min-heap invariant**: `heap[k] <= heap[2k+1]` and `heap[k] <= heap[2k+2]`. It is NOT a separate object/class.

```
Heap array <-> tree mapping:
index:   0   1   2   3   4   5
value: [ 1,  3,  2,  5,  4,  8]

Tree view:
             1(0)
           /      \
         3(1)      2(2)
        /   \      /
      5(3) 4(4)  8(5)

parent(i) = (i-1)//2
left(i)   = 2*i+1
right(i)  = 2*i+2
```

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappop(heap)              # 1 -- always removes SMALLEST
heap[0]                            # peek min without removing -- O(1)

heapq.heapify(arr)                   # convert list to heap IN-PLACE -- O(n), NOT O(n log n)!

heapq.nlargest(3, arr)                 # top-3 largest -- O(n log k)
heapq.nsmallest(3, arr)                  # top-3 smallest -- O(n log k)
heapq.nlargest(3, people, key=lambda p: p.age)

# Max-heap simulation (heapq is min-heap only) -- negate values
max_heap = []
heapq.heappush(max_heap, -5)
-heapq.heappop(max_heap)             # negate back on pop

# Push-pop combos (more efficient than separate calls)
heapq.heappushpop(heap, x)              # push then pop -- more efficient than push()+pop()
heapq.heapreplace(heap, x)                # pop then push -- assumes heap non-empty
```

**Complexity Table:**

| Operation | Complexity |
|---|---|
| `heappush` | O(log n) |
| `heappop` | O(log n) |
| `heap[0]` (peek) | O(1) |
| `heapify` | O(n) |
| `nlargest(k, ...)` / `nsmallest(k, ...)` | O(n log k) |

**Tuple-heap pattern (custom priority with tie-breaking):**
```python
# Dijkstra's algorithm pattern
heap = [(0, start)]           # (distance, node) -- heap compares tuples lexicographically
while heap:
    dist, node = heapq.heappop(heap)
    for nbr, weight in graph[node]:
        new_dist = dist + weight
        if new_dist < best[nbr]:
            best[nbr] = new_dist
            heapq.heappush(heap, (new_dist, nbr))
```
⚠️ **Pitfall:** If two tuples have equal first elements and the second elements are NOT directly comparable (e.g., custom objects without `__lt__`), Python raises `TypeError`. Fix by adding a unique tie-breaker (e.g., insertion counter) as the second tuple element: `(priority, counter, item)`.

## 7.5 `bisect` — Binary Search on Sorted Lists

```python
import bisect

arr = [1, 3, 3, 5, 7]
bisect.bisect_left(arr, 3)      # 1 -- leftmost insertion point (before existing 3s)
bisect.bisect_right(arr, 3)      # 3 -- rightmost insertion point (after existing 3s), == bisect.bisect
bisect.insort_left(arr, 4)         # inserts 4 keeping list sorted -- O(n) due to shift, O(log n) search
bisect.insort_right(arr, 4)

# Common DSA use: find first element >= target
idx = bisect.bisect_left(arr, target)
if idx < len(arr) and arr[idx] == target:
    print("found at", idx)

# Common DSA use: count elements <= x
count_le = bisect.bisect_right(arr, x)
```

```
bisect_left vs bisect_right for value 3 in [1,3,3,5,7]:
index:     0  1  2  3  4
value:     1  3  3  5  7
bisect_left(3)  -> 1   (insert BEFORE all 3s)
bisect_right(3) -> 3   (insert AFTER all 3s)
             ↑              ↑
         insert here    insert here
```

**Complexity:** Search is O(log n); `insort` is O(n) overall (O(log n) search + O(n) shift for insertion) — for many insertions, prefer a heap or `sortedcontainers.SortedList` (3rd-party, O(log n) insert) if allowed.

**Interview Tip:** `bisect` is the go-to tool for:
- Binary search on answer (parametric search)
- Longest Increasing Subsequence in O(n log n)
- Coordinate compression lookups

```python
# LIS in O(n log n) using bisect
def lis_length(nums):
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```

## 7.6 `operator` — Function Forms of Operators

```python
import operator

operator.add(2,3)             # 5
operator.mul(2,3)              # 6
operator.itemgetter(1)([1,2,3])  # 2 -- used as sort key: sorted(data, key=operator.itemgetter(1))
operator.attrgetter('name')(obj)  # obj.name -- used for sorting objects by attribute
reduce(operator.add, arr)          # sum equivalent, faster than lambda
```
`itemgetter`/`attrgetter` are faster than equivalent lambdas because they're implemented in C.

## 7.7 `statistics`

```python
import statistics as stats
stats.mean([1,2,3,4])       # 2.5
stats.median([1,2,3,4])       # 2.5
stats.mode([1,1,2,3])          # 1
stats.stdev([1,2,3,4])          # sample standard deviation
```
Rare in core DSA, occasionally useful for data-analysis-flavored problems.

## 7.8 `random`

```python
import random
random.randint(1, 10)        # inclusive both ends
random.choice([1,2,3])         # pick one
random.sample(range(100), 5)     # 5 unique random elements -- good for testing/shuffling
random.shuffle(arr)                # in-place shuffle
random.seed(42)                      # reproducibility for testing
```
Useful for: generating test cases, randomized algorithms (e.g., randomized quickselect, random pivot for avoiding worst-case).

## 7.9 `decimal` and `fractions` — Exact Arithmetic

```python
from decimal import Decimal
Decimal("0.1") + Decimal("0.2")     # Decimal('0.3') -- exact, no float error

from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)      # Fraction(1, 2) -- exact rational arithmetic
```
Use when floating-point precision errors would break correctness (financial calculations, exact rational results).

## 7.10 `array` — Compact Homogeneous Arrays

```python
from array import array
a = array('i', [1, 2, 3])    # typed array of ints -- much less memory than list of ints
```
Rarely needed in interviews (lists suffice), but relevant when memory limits matter in CP with huge numeric arrays.

## 7.11 `string` module constants

```python
import string
string.ascii_lowercase     # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase      # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits                 # '0123456789'
string.punctuation              # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```
Useful for quick alphabet-indexed frequency arrays: `[0]*26` combined with `ord(c) - ord('a')`.

## 7.12 `re` — Regular Expressions (DSA-relevant subset)

```python
import re
re.match(r'^\d+$', s)             # match from start
re.search(r'\d+', s)                # find anywhere
re.findall(r'\d+', s)                 # all non-overlapping matches
re.sub(r'\s+', ' ', s)                  # replace matches
re.split(r'[,;]', s)                      # split on multiple delimiters
```
Used for parsing/tokenizing DSA problems that involve structured strings (e.g., "Basic Calculator", expression parsing).

## 7.13 `copy` — Shallow vs Deep Copy

```python
import copy
shallow = copy.copy(obj)         # or obj[:] or list(obj), dict(obj)
deep = copy.deepcopy(obj)          # recursively copies nested objects
```
See §18 (Pitfalls) for the full shallow-vs-deep-copy memory diagram — a top interview gotcha for nested lists (e.g., initializing a 2D grid).

## 7.14 `pprint`

```python
from pprint import pprint
pprint(nested_structure, width=40)     # readable multi-line formatting for debugging
```

## 7.15 `typing` — Type Hints

```python
from typing import List, Dict, Tuple, Optional, Set, Union, Callable

def two_sum(nums: List[int], target: int) -> List[int]:
    ...

def find(d: Dict[str, int], key: str) -> Optional[int]:
    ...
```
Type hints don't affect runtime behavior but are standard in interview code for clarity (many platforms like LeetCode auto-generate signatures with them).

## 7.16 `dataclasses` — Boilerplate-Free Classes

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
p1 == p2               # True -- auto-generates __eq__ (unlike plain classes!)
print(p1)                # Point(x=1, y=2) -- auto __repr__

@dataclass(order=True)      # auto-generates comparison methods based on field order
class Task:
    priority: int
    name: str = field(compare=False)   # exclude from comparisons
```
Great for quickly defining structured objects (graph nodes, intervals) with free `__eq__`/`__repr__`.

## 7.17 `enum` — Named Constants

```python
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

Color.RED.name, Color.RED.value    # 'RED', 1
```
Useful for state-machine problems (cleaner than raw string/int constants).

## 7.18 Standard Library Quick Reference Table

| Module | Primary DSA Use |
|---|---|
| `math` | number theory, isqrt, gcd/lcm, inf sentinel |
| `itertools` | combinatorics, prefix sums, lazy chaining |
| `functools` | memoization (`lru_cache`), reduce, custom sort key |
| `heapq` | priority queues, k-th largest/smallest, Dijkstra |
| `bisect` | binary search, LIS, sorted insertion |
| `operator` | fast sort keys (`itemgetter`/`attrgetter`) |
| `collections` | Counter, deque, defaultdict, OrderedDict, namedtuple |
| `random` | test generation, randomized algorithms |
| `re` | string parsing problems |
| `copy` | deep-copying nested structures (graphs, grids) |
| `typing` | interview-style type-annotated signatures |
| `dataclasses` | quick structured objects with `__eq__`/`__repr__` |

# 8. Iterators & Generators

## 8.1 The Iterator Protocol

**Definition:** An **iterable** is any object implementing `__iter__` (returns an iterator). An **iterator** is any object implementing both `__iter__` (returns itself) and `__next__` (returns the next value or raises `StopIteration`).

```
Iterable vs Iterator:
  Iterable ──__iter__()──▶ Iterator ──__next__()──▶ value, value, value... StopIteration

  list [1,2,3]  is ITERABLE (has __iter__)
  iter([1,2,3]) is an ITERATOR (has __iter__ AND __next__)
```

```python
lst = [1, 2, 3]
it = iter(lst)          # get an iterator from the iterable
next(it)                  # 1
next(it)                   # 2
next(it)                    # 3
next(it)                     # raises StopIteration
next(it, "default")           # returns "default" instead of raising

# for loop is syntactic sugar for:
it = iter(lst)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    else:
        # loop body
        print(x)
```

**Why this matters for DSA:** Understanding iterator exhaustion prevents a classic bug — iterating a generator/iterator twice silently gives nothing the second time (§18).

## 8.2 Custom Iterators

```python
class RangeIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i - 1

for x in RangeIterator(5):    # 0,1,2,3,4
    print(x)
```

## 8.3 Generator Functions (`yield`)

**Definition:** A function containing `yield` becomes a **generator function** — calling it doesn't run the body; it returns a generator object. Execution pauses at each `yield` and resumes on the next `next()` call, preserving local state between calls.

**Why it exists:** Lazy evaluation — huge memory savings for large/infinite sequences (no need to materialize the whole list).

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(5)
next(gen)    # 1  -- runs until first yield, PAUSES
next(gen)     # 2  -- resumes right after yield, runs to next yield
for x in gen:   # continues from where it paused: 3, 4, 5
    print(x)
```

```
Generator execution model (paused coroutine):

  def count_up_to(3):
      i = 1
      while i <= 3:
          yield i    <-- execution PAUSES here, state (i) preserved
          i += 1

  Call sequence:
  gen = count_up_to(3)     # nothing runs yet
  next(gen) -> runs to first yield -> returns 1, i=1 saved
  next(gen) -> resumes after yield, i becomes 2, loops, yields 2
  next(gen) -> resumes, i becomes 3, loops, yields 3
  next(gen) -> resumes, i becomes 4, loop condition false -> StopIteration
```

**Memory comparison:**
```python
# Eager -- builds ENTIRE list in memory: O(n) space
def squares_list(n):
    return [x*x for x in range(n)]

# Lazy -- O(1) space, one value at a time
def squares_gen(n):
    for x in range(n):
        yield x*x
```

## 8.4 `yield from` — Delegating Generators

```python
def inner():
    yield 1
    yield 2

def outer():
    yield from inner()   # equivalent to: for x in inner(): yield x
    yield 3

list(outer())    # [1, 2, 3]

# Classic use: flatten nested structures via recursive generator
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

list(flatten([1, [2, 3, [4, 5]], 6]))    # [1, 2, 3, 4, 5, 6]
```

**`yield from` for tree traversal (very interview-relevant):**
```python
def inorder(node):
    if node:
        yield from inorder(node.left)
        yield node.val
        yield from inorder(node.right)
```

## 8.5 Generator Expressions

Same syntax as list comprehensions but with `()` instead of `[]` — lazy, O(1) memory.

```python
gen = (x*x for x in range(1000000))    # doesn't compute anything yet
sum(gen)                                  # consumes lazily, O(1) extra memory

# Passing directly to a function (parens can be omitted if it's the sole argument)
sum(x*x for x in range(10))
any(x > 100 for x in arr)
max(len(w) for w in words)
```

**List comprehension vs generator expression — memory tradeoff:**

| | List comprehension `[...]` | Generator expression `(...)` |
|---|---|---|
| Memory | O(n) — all values stored | O(1) — one value at a time |
| Speed (single pass) | Slightly faster (no `next()` overhead) | Slightly slower per element |
| Reusable? | Yes, can iterate many times | No — exhausted after one pass |
| Indexable? | Yes (`lst[3]`) | No |

## 8.6 Lazy Evaluation — Why It Matters in DSA

```python
# Finding first match without scanning the whole (potentially huge) sequence
first_even = next(x for x in huge_list if x % 2 == 0)   # stops at first hit -- O(k), not O(n)

# Infinite sequence handling
from itertools import count, islice
first_10_squares = list(islice((x*x for x in count(1)), 10))
```
Generators let you write pipeline-style code (filter → map → take) that never materializes intermediate full lists — critical for streaming large inputs in CP.

---

# 9. Comprehensions

## 9.1 List Comprehension

```python
squares = [x*x for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
transformed = [x*2 if x % 2 == 0 else x for x in range(10)]   # conditional expression inside
```

**Equivalent loop form (for understanding, not for writing):**
```python
squares = []
for x in range(10):
    squares.append(x*x)
```
List comprehensions are typically **faster** than the equivalent explicit loop because the append calls are done via a specialized bytecode (`LIST_APPEND`) without the overhead of attribute lookup (`.append`) each iteration.

## 9.2 Dict Comprehension

```python
squares = {x: x*x for x in range(5)}          # {0:0, 1:1, 2:4, 3:9, 4:16}
inverted = {v: k for k, v in original.items()}
filtered = {k: v for k, v in d.items() if v > 0}
```

## 9.3 Set Comprehension

```python
unique_lengths = {len(w) for w in words}
```

## 9.4 Generator Comprehension (Expression)

```python
gen = (x for x in range(10) if x % 2 == 0)
```

## 9.5 Nested Comprehensions

```python
# Flatten a 2D grid
flat = [cell for row in grid for cell in row]
#        ▲ output expr    ▲ outer loop (first)  ▲ inner loop (second)

# Equivalent nested loop:
flat = []
for row in grid:
    for cell in row:
        flat.append(cell)

# Build a 2D grid (list of lists) -- CORRECT way (each row is independent!)
grid = [[0] * cols for _ in range(rows)]

# Transpose a matrix
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Nested with condition on outer AND inner
pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
```

**Order of `for` clauses in a nested comprehension matches nested `for` loops, left to right, outer to inner** — a common source of confusion.

**⚠️ Critical Pitfall — the `[[0]*cols]*rows` trap:**
```python
# WRONG -- all rows are the SAME list object (aliased)!
grid = [[0] * cols] * rows
grid[0][0] = 1     # mutates ALL rows! grid = [[1,0,..],[1,0,..],...]

# CORRECT -- each row is independently created
grid = [[0] * cols for _ in range(rows)]
grid[0][0] = 1     # only first row affected
```
```
[[0]*cols]*rows aliasing diagram:
   grid ──▶ [ ref, ref, ref ]     <- 3 pointers to the SAME list!
                │    │    │
                └────┴────┴──▶ [0, 0, 0]   (single shared row object)

Correct version:
   grid ──▶ [ ref1, ref2, ref3 ]
               │      │      │
               ▼      ▼      ▼
            [0,0,0] [0,0,0] [0,0,0]   <- 3 INDEPENDENT row objects
```

## 9.6 Comprehension Performance Notes

- Comprehensions run in their **own scope** in Python 3 (variables inside don't leak to enclosing scope) — unlike a `for` loop.
- Prefer comprehensions over `map`/`filter` + `lambda` for **readability** in most cases; performance is comparable, with comprehensions often slightly faster due to no function-call overhead per element.
- For very large data with a **single terminal operation** (`sum`, `any`, `max`), prefer a **generator expression** over a list comprehension to avoid building the intermediate list.

---

# 10. Functional Programming

## 10.1 `lambda` — reviewed in §4.6.

## 10.2 `map`

```python
list(map(str, [1,2,3]))              # ['1','2','3']
list(map(int, input().split()))        # classic competitive programming input parsing
list(map(lambda x: x*2, arr))            # [2,4,6...]
list(map(pow, [2,3],[3,2]))                # [8, 9] -- multiple iterables, applied pairwise
```
`map` returns a **lazy iterator** in Python 3 (must wrap in `list()` to materialize).

## 10.3 `filter`

```python
list(filter(lambda x: x > 0, arr))     # keep only positives
list(filter(None, [0, 1, "", "a", None]))   # keep only truthy values: [1, 'a']
```
Also lazy. Equivalent list comprehension `[x for x in arr if x > 0]` is generally preferred for readability.

## 10.4 `functools.reduce`

```python
from functools import reduce
reduce(lambda acc, x: acc + x, arr, 0)        # sum with initial value 0
reduce(lambda acc, x: acc if acc > x else x, arr)   # max without initial value
```
`reduce` is less Pythonic than a plain loop or built-in (`sum`, `max`) for simple cases — use it mainly for custom accumulation logic that has no built-in equivalent.

## 10.5 `zip`

```python
list(zip([1,2,3], ['a','b','c']))       # [(1,'a'),(2,'b'),(3,'c')]
list(zip([1,2,3], ['a','b']))             # [(1,'a'),(2,'b')] -- STOPS at shortest iterable

a, b = [1,2,3], [4,5,6]
list(zip(*zip(a, b)))                       # unzip trick -- back to ([1,2,3],[4,5,6])

# Transpose a matrix using zip -- extremely Pythonic
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = list(zip(*matrix))              # [(1,4,7),(2,5,8),(3,6,9)]
```
Use `itertools.zip_longest` if you need padding instead of truncation to the shortest iterable.

## 10.6 `enumerate`

```python
for i, x in enumerate(arr):              # (index, value) pairs
    print(i, x)
for i, x in enumerate(arr, start=1):        # start counting from 1
    print(i, x)
```
Always prefer `enumerate` over manual `for i in range(len(arr)): x = arr[i]`.

## 10.7 `any` / `all`

```python
any(x > 0 for x in arr)      # True if AT LEAST ONE truthy -- short-circuits
all(x > 0 for x in arr)        # True if ALL truthy -- short-circuits
```
Both short-circuit and work beautifully with generator expressions for O(1) extra memory checks over huge sequences.

## 10.8 `sorted`

```python
sorted(arr)                                   # ascending, returns NEW list (vs arr.sort() in-place)
sorted(arr, reverse=True)                       # descending
sorted(words, key=len)                            # sort by custom key function
sorted(people, key=lambda p: (p.age, p.name))       # multi-key sort (tuple key)
sorted(arr, key=lambda x: (-x[0], x[1]))              # mixed asc/desc via negation
```
**Internal working:** Python's `sorted`/`list.sort` use **Timsort** — a hybrid stable merge/insertion sort, O(n log n) worst case, O(n) best case (already-sorted data), and **stable** (equal elements retain relative order — crucial for multi-pass sorting strategies).

## 10.9 `reversed`

```python
list(reversed([1,2,3]))    # [3,2,1] -- lazy iterator
arr[::-1]                    # also reverses, but creates a full copy (different performance profile)
```

## 10.10 Functional Programming Cheat Sheet

| Tool | Purpose | Lazy? |
|---|---|---|
| `map(f, it)` | transform each element | Yes |
| `filter(f, it)` | keep matching elements | Yes |
| `reduce(f, it)` | fold into single value | N/A (consumes fully) |
| `zip(a, b)` | pair elements | Yes |
| `enumerate(it)` | index+value pairs | Yes |
| `sorted(it, key=)` | sort | No (returns list) |
| `any`/`all` | boolean aggregate | short-circuits |
| `lambda` | inline anonymous function | N/A |

# 11. Object-Oriented Concepts for DSA

OOP in DSA is mostly about building clean node/structure classes (linked lists, trees, graphs, custom data structures like Trie/Union-Find/LRU Cache).

## 11.1 Classes & Objects — Minimal Required Syntax

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Building a linked list: 1 -> 2 -> 3
head = ListNode(1, ListNode(2, ListNode(3)))
```

```
Linked list memory model:
head ──▶ [1 | next]──▶[2 | next]──▶[3 | None]
```

## 11.2 `__init__` — Constructor

Called automatically right after object creation to initialize instance attributes. Not technically a constructor (that's `__new__`, rarely touched in DSA).

## 11.3 `__repr__` and `__str__`

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"     # unambiguous, for debugging/repr()
    def __str__(self):
        return f"({self.x}, {self.y})"           # readable, for print()/str()

p = Point(1, 2)
print(p)      # uses __str__: (1, 2)
p             # in REPL, uses __repr__: Point(1, 2)
[p, p]         # printing a list uses __repr__ for elements even if __str__ exists!
```
> **Interview Tip:** Always define at least `__repr__` on custom node/structure classes — makes debugging with `print()` vastly easier (default repr is an unhelpful `<ListNode object at 0x...>`).

## 11.4 `__eq__`, `__lt__` and other comparison dunders

```python
class Interval:
    def __init__(self, start, end):
        self.start, self.end = start, end
    def __lt__(self, other):
        return self.start < other.start     # enables sorted(), sort(), heapq to work directly

intervals = [Interval(3,5), Interval(1,2)]
intervals.sort()               # uses __lt__
```
Needed whenever you put custom objects directly into a `sorted()`/heap without a `key=`.

## 11.5 `__hash__` and `__eq__` together

To use custom objects as **dict keys or set elements**, both must be defined consistently:
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    def __hash__(self):
        return hash((self.x, self.y))
```
⚠️ **Pitfall:** Defining `__eq__` without `__hash__` makes the class **unhashable** (Python sets `__hash__` to `None` automatically) — it can no longer go in a `set`/dict key.

## 11.6 `__slots__` — Memory Optimization

By default, every instance gets a `__dict__` for arbitrary attributes — flexible but memory-heavy. `__slots__` pre-declares fixed attributes, saving substantial memory when creating **millions of small objects** (e.g., Trie nodes, graph nodes in huge inputs).

```python
class TrieNode:
    __slots__ = ('children', 'is_end')
    def __init__(self):
        self.children = {}
        self.is_end = False
```

```
Memory comparison (approximate, CPython):
  Without __slots__: ~56 bytes object + ~112 bytes __dict__ per instance ≈ 168+ bytes
  With __slots__:    ~56 bytes object, no __dict__ ≈ fixed, smaller footprint

For 10^6 TrieNodes, __slots__ can save tens of MB -- can be the difference
between passing/failing a memory-limited CP problem.
```
Trade-off: no dynamic attribute addition, no default multiple inheritance with other `__slots__` classes without care.

## 11.7 `dataclass` — reviewed in §7.16. Prefer for quick, readable structured types when you don't need `__slots__`-level memory tuning.

## 11.8 `staticmethod` and `classmethod`

```python
class MathUtils:
    @staticmethod
    def gcd(a, b):                 # no access to self/cls -- pure utility function grouped in a class
        while b:
            a, b = b, a % b
        return a

    @classmethod
    def from_string(cls, s):        # alternative constructor pattern
        x, y = map(int, s.split(','))
        return cls(x, y)
```

## 11.9 Building Common DSA Structures — Quick Templates

```python
# Union-Find / Disjoint Set Union (DSU)
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return False
        if self.rank[rx] < self.rank[ry]: rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]: self.rank[rx] += 1
        return True

# Trie
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    def insert(self, word):
        node = self
        for ch in word:
            node = node.children.setdefault(ch, Trie())
        node.is_end = True
    def search(self, word):
        node = self
        for ch in word:
            if ch not in node.children: return False
            node = node.children[ch]
        return node.is_end
```

---

# 12. Memory & Performance

## 12.1 Reference Counting

**Definition:** CPython's primary garbage collection mechanism — every object tracks how many references point to it (`sys.getrefcount(obj)`). When the count hits zero, the object is immediately deallocated.

```python
import sys
x = [1, 2, 3]
sys.getrefcount(x)     # baseline count (includes the temp ref from the function call itself)
y = x                    # refcount +1
del y                      # refcount -1
```

```
Refcount lifecycle:
x = [1,2,3]        refcount = 1
y = x               refcount = 2
del x                 refcount = 1
del y                  refcount = 0 -> object DEALLOCATED immediately
```

## 12.2 Garbage Collection (Cycle Detector)

Reference counting alone can't reclaim **reference cycles** (e.g., a doubly-linked list node pointing to itself, or parent↔child tree references). Python's `gc` module runs a generational cycle-detecting collector to handle these.

```python
import gc
gc.collect()          # force a collection cycle (rarely needed manually)
gc.disable()             # can sometimes speed up CP scripts with huge object counts, no cycles
```
> **CP Tip:** For scripts that create millions of short-lived objects and are guaranteed cycle-free, `gc.disable()` at the top can meaningfully reduce runtime overhead.

## 12.3 Object Caching — Integer & String Interning

**Small integer caching:** CPython pre-creates and reuses integer objects in range **[-5, 256]**.
```python
a = 100; b = 100
a is b        # True  -- both point to the SAME cached object

a = 1000; b = 1000
a is b          # False (usually) -- outside cache range, separate objects
```

**String interning:** Identifier-like strings (short, alphanumeric+underscore, compile-time constants) are automatically interned and reused.
```python
a = "hello"; b = "hello"
a is b          # True (usually) -- interned

a = "hello world!"; b = "hello world!"
a is b            # implementation-dependent, don't rely on it
```
> **Rule of thumb:** Never rely on `is` for value comparison of numbers/strings — always use `==`. Reserve `is` for `None`/`True`/`False`/singleton sentinel checks.

## 12.4 List Resizing (see also §5.6)

Over-allocation growth pattern amortizes `append` to O(1). Pre-sizing with `[0]*n` avoids ANY resizing when the final size is known upfront — marginally faster than repeated appends for large fixed-size arrays.

## 12.5 Dictionary Resizing & Hashing

Similar amortized growth strategy as lists. Dict/set resize (rehash all entries) when the load factor exceeds ~2/3 — an O(n) one-time cost, amortized to O(1) per insertion across many inserts.

**Hashing internals relevant to DSA:**
- `hash(x)` must be consistent for equal objects: `a == b` implies `hash(a) == hash(b)`.
- Mutable objects (`list`, `dict`, `set`) are unhashable by design — using them as dict keys raises `TypeError`, precisely because mutation would silently invalidate their hash bucket.

## 12.6 Time Complexity of Built-in Operations — Master Reference

*(Full detailed tables also appear per-type in §5 and §16; this is the compact master view.)*

| Type | Access | Search | Insert | Delete |
|---|---|---|---|---|
| `list` (end) | O(1) | O(n) | O(1)* | O(1) |
| `list` (arbitrary) | O(1) | O(n) | O(n) | O(n) |
| `dict` | O(1)* | O(1)* | O(1)* | O(1)* |
| `set` | — | O(1)* | O(1)* | O(1)* |
| `deque` (ends) | O(1) | O(n) | O(1) | O(1) |
| sorted `list` via `bisect` | O(1) | O(log n) | O(n) | O(n) |

*amortized average case

## 12.7 Memory Optimization Techniques for DSA/CP

1. **`__slots__`** for classes with many instances (§11.6).
2. **Generators instead of lists** when you only need one pass (§8.5).
3. **`array` module** instead of `list` for large homogeneous numeric data.
4. **In-place operations** (`sort()` not `sorted()`, `+=` for lists via `extend`) to avoid duplicate allocations.
5. **Avoid unnecessary string concatenation** — use `join` (§5.5).
6. **Reuse buffers** rather than allocating new lists/sets inside hot loops.

---

# 13. Competitive Programming in Python

## 13.1 Fast Input

The default `input()` is slow for large inputs (thousands of lines) due to per-call overhead. Read everything at once instead.

```python
import sys
input = sys.stdin.readline          # rebind input() to a faster line-reader (strip '\n' if needed!)

# For MANY tokens across the whole file:
data = sys.stdin.read().split()
idx = 0
n = int(data[idx]); idx += 1
arr = list(map(int, data[idx:idx+n])); idx += n
```

```
Why sys.stdin.read() is faster:
input() -- one system-call-ish read PER LINE -- overhead × n lines
sys.stdin.read() -- ONE bulk read of the entire input -- overhead × 1
```

## 13.2 Fast Output

```python
import sys
print(x)                                  # slow if called thousands of times (flushes each time)
sys.stdout.write(str(x) + "\n")             # faster, no extra formatting overhead

# Fastest for many lines: batch into one list, join once, print once
results = []
for ...:
    results.append(str(computed_value))
sys.stdout.write("\n".join(results) + "\n")
print(*results, sep="\n")                     # alternative one-liner
```

## 13.3 Recursion Limit

Python's default recursion limit is **1000** frames — too shallow for deep recursive DFS on large inputs (e.g., a skewed tree/graph with 10⁵ nodes).

```python
import sys
sys.setrecursionlimit(10**6)     # raise the limit
```
⚠️ Raising the limit doesn't raise your actual C-stack size — extremely deep recursion can still segfault. For very deep recursion (>10⁵), prefer converting to an **iterative** approach with an explicit stack, or increase the thread stack size:
```python
import threading
threading.stack_size(2**27)        # ~128MB stack
sys.setrecursionlimit(10**6)
t = threading.Thread(target=main)
t.start(); t.join()
```

## 13.4 Large Input Optimization Checklist

```
┌───────────────────────────────────────────────────────┐
│ 1. Use sys.stdin for input, never bare input() in loops │
│ 2. Use sys.stdout / batched print for output              │
│ 3. Avoid list.pop(0)/insert(0,x) -- use deque instead       │
│ 4. Avoid string += in loops -- build list, join once          │
│ 5. Prefer local variable references over repeated attribute │
│    lookups inside hot loops (e.g. append = lst.append)        │
│ 6. Use sets/dicts for O(1) membership instead of list scans     │
│ 7. Precompute with itertools.accumulate for prefix sums           │
│ 8. Use PyPy-friendly style if judge supports it (avoid heavy OOP)  │
│ 9. Use lru_cache/memoization to avoid recomputation                 │
│10. Vectorize with math/heapq/bisect (C-implemented) over pure Python │
└───────────────────────────────────────────────────────┘
```

## 13.5 Local Variable Lookup Trick

```python
# Slower: repeated global/attribute lookup each iteration
result = []
for x in big_range:
    result.append(f(x))

# Faster: bind method to a local variable once
append = result.append
for x in big_range:
    append(x)
```
This matters because CPython's local variable access (`LOAD_FAST`) is faster than attribute lookup (`LOAD_ATTR` + method resolution) repeated millions of times.

## 13.6 `sys.setrecursionlimit` and Iterative DFS Template

```python
def iterative_dfs(graph, start):
    stack = [start]
    visited = {start}
    while stack:
        node = stack.pop()
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                stack.append(nbr)
```
Prefer this pattern over recursive DFS whenever input size could cause `RecursionError`.

## 13.7 Common CP I/O Template (Full Boilerplate)

```python
import sys
from collections import defaultdict, deque
import heapq, bisect
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # ... solve ...
    print(answer)

if __name__ == "__main__":
    main()
```

# 14. Python Idioms

A curated set of Pythonic patterns that show up constantly in DSA/interview code.

## 14.1 Tuple Unpacking & Multiple Assignment

```python
a, b = 1, 2
a, b, *rest = [1, 2, 3, 4, 5]      # rest = [3,4,5]
*init, last = [1, 2, 3, 4, 5]       # init = [1,2,3,4], last = 5
first, *_, last = [1,2,3,4,5]         # ignore middle: first=1, last=5

for a, b in [(1,2), (3,4)]:            # unpack in loop
    print(a, b)

(x, y), z = (1, 2), 3                    # nested unpacking
```

## 14.2 Swapping Without Temp Variable

```python
a, b = b, a                # Pythonic swap -- RHS tuple built first, then unpacked
arr[i], arr[j] = arr[j], arr[i]    # swap list elements -- classic in sorting algorithms
```

## 14.3 Chained Comparison

```python
if 0 <= i < n:                  # range check in ONE readable expression
if lo <= mid <= hi:
```

## 14.4 Truthiness Idioms

```python
if not lst:            # cleaner than: if len(lst) == 0
    print("empty")

if lst:                  # cleaner than: if len(lst) > 0
    print("non-empty")

value = a or b            # fallback if `a` is falsy
value = a if a is not None else b   # fallback only for explicit None (safer if 0/'' are valid)
```

## 14.5 `enumerate` / `zip` Idioms

```python
for i, x in enumerate(arr):
    ...
for a, b in zip(list1, list2):
    ...
for i, (a, b) in enumerate(zip(list1, list2)):
    ...
```

## 14.6 Unpacking Operator `*` / `**`

```python
def f(a, b, c): ...
args = [1, 2, 3]
f(*args)                     # unpack list as positional args

merged = [*list1, *list2]      # concatenate via unpacking
merged_dict = {**d1, **d2}       # merge dicts (d2 overrides d1 on key conflict)

first, *middle, last = [1,2,3,4,5]
```

## 14.7 Slicing Tricks

```python
arr[::-1]           # reverse
arr[::2]              # every other element
arr[1:]                 # drop first
arr[:-1]                  # drop last
arr[-k:]                    # last k elements
arr[:k]                       # first k elements
a, b = arr[:mid], arr[mid:]     # split in half -- classic divide & conquer step
arr[i:i] = [x]                    # insert x at index i WITHOUT shifting via insert() call
arr[i:j] = []                       # delete slice in place
```

## 14.8 Negative Indexing

```python
arr[-1]     # last element
arr[-2]      # second-to-last
s[-3:]         # last 3 characters
```

## 14.9 Sentinel Values

```python
UNVISITED = -1
NOT_FOUND = None
INF = float('inf')

dist = [INF] * n
dist[start] = 0

parent = {node: None for node in graph}   # None as "no parent yet" sentinel
```
A **unique sentinel object** (when `None` itself might be a valid value) is created via:
```python
_SENTINEL = object()
def get(d, key, default=_SENTINEL):
    val = d.get(key, _SENTINEL)
    if val is _SENTINEL:
        return default
    return val
```

## 14.10 Dictionary "get-or-default" & "get-or-initialize" Idioms

```python
count = freq.get(x, 0) + 1                    # get with default
freq[x] = freq.get(x, 0) + 1

graph.setdefault(node, []).append(neighbor)     # get-or-initialize in one line
```

## 14.11 List/Set/Dict Building One-liners

```python
squares = [x*x for x in range(10)]
seen = set()
lookup = {v: i for i, v in enumerate(arr)}      # value -> index map, O(1) lookup later
freq = {}
for x in arr: freq[x] = freq.get(x, 0) + 1
```

## 14.12 Multi-return & Immediate Unpack

```python
def min_max(arr):
    return min(arr), max(arr)

lo, hi = min_max(arr)
```

## 14.13 Ternary Chains for Multi-way Branching (use sparingly)

```python
sign = -1 if n < 0 else (0 if n == 0 else 1)
```
For more than 2-3 branches, prefer `if/elif/else` for readability.

---

# 15. Common Built-in Functions Reference

An A-Z reference of built-ins most relevant to DSA, each with signature, behavior, and a usage note.

| Function | Signature | DSA Use |
|---|---|---|
| `abs(x)` | absolute value | distance/diff calculations |
| `all(iterable)` | True if all truthy | validity checks |
| `any(iterable)` | True if any truthy | existence checks |
| `ascii(obj)` | escaped repr string | rarely used in DSA |
| `bin(n)` | binary string `'0b101'` | bit manipulation debugging |
| `bool(x)` | truthiness | type coercion |
| `callable(obj)` | is it callable? | validating function args |
| `chr(i)` | int → unicode char | char-based array indexing |
| `divmod(a, b)` | `(a//b, a%b)` in one call | avoid computing both separately |
| `enumerate(it, start=0)` | index+value pairs | loop with index |
| `eval(expr)` | ⚠️ evaluates a string as code | **avoid** — security/safety risk, rarely appropriate |
| `filter(f, it)` | lazy filtering | functional filtering |
| `format(val, spec)` | custom string formatting | `format(255, '08b')` → binary padded |
| `hash(obj)` | hash value | understanding hashability |
| `hex(n)` | hex string | bit/number problems |
| `id(obj)` | memory identity | aliasing/debugging |
| `input()` | read a line | I/O |
| `isinstance(obj, type)` | type check | polymorphic dispatch, `match`-less type branching |
| `issubclass(cls, base)` | class hierarchy check | rarely used directly in DSA |
| `iter(obj)` | get iterator | manual iteration control |
| `len(obj)` | length | O(1) for built-ins |
| `list(it)` | build a list | materializing iterators |
| `map(f, it)` | lazy transform | functional transform |
| `max(it, key=)` / `max(a,b)` | maximum | O(n) scan |
| `min(it, key=)` / `min(a,b)` | minimum | O(n) scan |
| `next(it, default)` | advance iterator | manual iteration, generator control |
| `oct(n)` | octal string | rare |
| `ord(c)` | char → int codepoint | char-index arithmetic |
| `pow(x, y, mod)` | exponentiation, optional mod | **fast modular exponentiation** — O(log y)! |
| `print(*args, sep, end)` | output | I/O |
| `range(start, stop, step)` | lazy integer sequence | loop bounds |
| `repr(obj)` | unambiguous string form | debugging |
| `reversed(seq)` | lazy reverse iterator | reverse traversal |
| `round(x, n)` | rounding (banker's rounding!) | ⚠️ `round(0.5)==0`, `round(1.5)==2` |
| `set(it)` | build a set | dedup, O(1) membership |
| `slice(start,stop,step)` | slice object | dynamic/reusable slicing |
| `sorted(it, key=, reverse=)` | new sorted list | Timsort, O(n log n) |
| `sum(it, start=0)` | sum with optional start | prefix sums, quick totals |
| `super()` | parent class access | OOP inheritance |
| `tuple(it)` | build a tuple | hashable grouping |
| `type(obj)` | get type | debugging, dispatch |
| `vars(obj)` | `obj.__dict__` | debugging object state |
| `zip(*iterables)` | parallel iteration | pairing, transpose, unzip |

### Deep dives on the most DSA-critical ones:

**`pow(x, y, mod)` — Fast Modular Exponentiation:**
```python
pow(2, 10)            # 1024 -- same as 2**10
pow(2, 10, 1000)        # 24 -- (2**10) % 1000, computed via fast exponentiation O(log y), NOT by
                          # first computing the (potentially huge) 2**10 -- essential for modular arithmetic in CP!
```

**`divmod` — Two-in-one:**
```python
q, r = divmod(17, 5)     # (3, 2) -- one call instead of // and % separately
```

**`sorted` with `key` — the most-used DSA builtin after collections:**
```python
sorted(arr, key=abs)                          # sort by absolute value
sorted(words, key=len, reverse=True)             # longest first
sorted(points, key=lambda p: (p[0], -p[1]))        # multi-criteria sort
```

**`max`/`min` with `key` and `default`:**
```python
max(arr, key=lambda x: x[1])
max([], default=0)      # avoids ValueError on empty sequence
```

**`round` — Banker's Rounding gotcha:**
```python
round(0.5)    # 0   -- rounds to EVEN, not always "up"
round(1.5)     # 2
round(2.5)      # 2
```
For DSA problems requiring "round half up," implement manually: `math.floor(x + 0.5)`.

**`format`/f-strings for binary/hex debugging:**
```python
format(10, 'b')       # '1010'
format(10, '08b')       # '00001010' -- zero-padded to 8 bits
f"{10:08b}"                # same, via f-string
```

# 16. Complexity Tables (Master Reference)

## 16.1 `list`

| Op | Complexity |
|---|---|
| index/assign `lst[i]` | O(1) |
| `append` | O(1) amortized |
| `pop()` | O(1) |
| `pop(0)` / `insert(0,x)` | O(n) |
| `x in lst` | O(n) |
| `sort()` | O(n log n) |
| `min/max/sum` | O(n) |
| slice `lst[a:b]` | O(b-a) |

## 16.2 `tuple`

| Op | Complexity |
|---|---|
| index `t[i]` | O(1) |
| `x in t` | O(n) |
| concatenation | O(n+m) |

## 16.3 `set` / `frozenset`

| Op | Average | Worst |
|---|---|---|
| `add`/`remove`/`in` | O(1) | O(n) |
| union / intersection / difference | O(len(s1)+len(s2)) | — |

## 16.4 `dict`

| Op | Average | Worst |
|---|---|---|
| get/set/delete/`in` | O(1) | O(n) |
| iteration | O(n) | — |

## 16.5 `str`

| Op | Complexity |
|---|---|
| index | O(1) |
| slice | O(k) |
| concatenation (`+`) | O(n+m) |
| `in` (substring) | O(n·m) worst |
| `split`/`join` | O(n) |

## 16.6 `collections.deque`

| Op | Complexity |
|---|---|
| append/appendleft/pop/popleft | O(1) |
| middle index access | O(n) |
| rotate(k) | O(k) |

## 16.7 `heapq`

| Op | Complexity |
|---|---|
| heappush/heappop | O(log n) |
| heap[0] peek | O(1) |
| heapify | O(n) |
| nlargest/nsmallest(k) | O(n log k) |

## 16.8 `bisect`

| Op | Complexity |
|---|---|
| bisect_left/right | O(log n) |
| insort | O(n) (O(log n) search + O(n) shift) |

## 16.9 `Counter`

| Op | Complexity |
|---|---|
| build from iterable | O(n) |
| `most_common(k)` | O(n log k) |
| arithmetic (`+`,`-`,`&`,`\|`) | O(n+m) |

## 16.10 Sorting & Searching Algorithms (built-in)

| Algorithm | Time | Space | Stable? |
|---|---|---|---|
| `sorted()`/`.sort()` (Timsort) | O(n log n) worst, O(n) best | O(n) | Yes |
| `bisect` binary search | O(log n) | O(1) | — |

---

# 17. Debugging

## 17.1 print debugging

```python
print(f"DEBUG: i={i}, arr={arr}", file=sys.stderr)   # stderr keeps stdout clean for judges
```

## 17.2 `pprint` for nested structures

```python
from pprint import pprint
pprint(complex_nested_dict)
```

## 17.3 `assert` for invariant checking

```python
assert len(stack) > 0, "stack should never be empty here"
assert is_sorted(arr)          # sanity check during development
```
⚠️ Assertions are stripped when Python runs with `-O` (optimize flag) — never rely on `assert` for real input validation, only for internal invariant/debug checks.

## 17.4 Reading Tracebacks

```
Traceback (most recent call last):
  File "sol.py", line 10, in <module>
    result = solve(arr)
  File "sol.py", line 5, in solve
    return arr[10]
IndexError: list index out of range
```
Read **bottom-up**: the last line is the actual error type/message; the frames above show the call chain that led there, most recent call last.

## 17.5 Common Runtime Errors & Exceptions

| Exception | Typical Cause |
|---|---|
| `IndexError` | out-of-bounds list/string access |
| `KeyError` | missing dict key |
| `TypeError` | wrong type in operation (e.g., `int + str`) |
| `ValueError` | right type, invalid value (e.g., `int("abc")`) |
| `AttributeError` | calling a method that doesn't exist (e.g., `None.append()`) |
| `ZeroDivisionError` | division/modulo by zero |
| `RecursionError` | recursion too deep (§13.3) |
| `StopIteration` | manual `next()` past exhaustion |
| `NameError` | using undefined variable |
| `UnboundLocalError` | using a local var before assignment (often from missing `global`) |

```python
try:
    risky_operation()
except (KeyError, IndexError) as e:
    print(f"Handled: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("no exception occurred")
finally:
    print("always runs")
```

---

# 18. Python Pitfalls

## 18.1 Mutable Default Arguments — THE classic Python gotcha

```python
# WRONG -- default list is created ONCE at function definition time, shared across ALL calls
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

add_item(1)    # [1]
add_item(2)     # [1, 2]  <- unexpected! same list reused!

# CORRECT
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```
```
Why this happens:
def f(x=[]):   <- the list [] is created ONCE, at DEF time, stored as part of the function object
    ...
Every call that doesn't pass x explicitly reuses that SAME list object.
```

## 18.2 Shallow vs Deep Copy

```python
import copy
original = [[1, 2], [3, 4]]

shallow = original.copy()          # or list(original), original[:]
shallow[0].append(99)                # MUTATES original[0] too! (shared inner lists)
# original -> [[1, 2, 99], [3, 4]]

deep = copy.deepcopy(original)
deep[0].append(100)                    # does NOT affect original -- fully independent copies
```
```
Shallow copy memory model:
original ──▶ [ ref_A, ref_B ]
shallow  ──▶ [ ref_A, ref_B ]     <- SAME inner list references copied
                │       │
                ▼       ▼
              [1,2]   [3,4]        <- shared -- mutating via either name affects both

Deep copy memory model:
original ──▶ [ ref_A,  ref_B  ]        deep ──▶ [ ref_A', ref_B' ]
                │        │                          │         │
                ▼        ▼                          ▼         ▼
              [1,2]    [3,4]                      [1,2]     [3,4]   <- INDEPENDENT copies
```

## 18.3 Floating-Point Precision

```python
0.1 + 0.2 == 0.3          # False!
math.isclose(0.1+0.2, 0.3)  # True -- correct comparison
```

## 18.4 Integer Division Behavior with Negatives

```python
-7 // 2      # -4, NOT -3  (floors toward negative infinity)
int(-7 / 2)   # -3          (truncates toward zero)
```
See §2.1 for the full explanation.

## 18.5 Recursion Limit

Deep recursion (>~1000 frames default) raises `RecursionError`. See §13.3 for fixes.

## 18.6 Aliasing

```python
a = [1, 2, 3]
b = a           # ALIAS, not a copy!
b.append(4)      # mutates a too -- a == [1,2,3,4]
```
Always ask: "do I want a new name for the SAME object, or an independent COPY?"

## 18.7 Late Binding Closures in Loops

```python
funcs = [lambda: i for i in range(3)]
[f() for f in funcs]      # [2, 2, 2] -- NOT [0, 1, 2]!
# All lambdas share the SAME enclosing 'i' -- by the time they run, the loop has finished, i=2

# FIX 1: default argument captures value AT DEFINITION time
funcs = [lambda i=i: i for i in range(3)]
[f() for f in funcs]        # [0, 1, 2]  correct!

# FIX 2: use a factory function to create a fresh scope
def make_func(i):
    return lambda: i
funcs = [make_func(i) for i in range(3)]
```
```
Late binding diagram:
  loop variable 'i' lives in ONE shared cell in the enclosing scope
  lambda1 ──┐
  lambda2 ──┼──▶ [shared cell: i]   <- all three read whatever 'i' currently IS
  lambda3 ──┘        (ends at 2 after loop finishes)
```

## 18.8 Hashability Requirements

```python
{[1,2]: "value"}     # TypeError: unhashable type: 'list'
{(1,2): "value"}       # OK -- tuples ARE hashable (if their elements are)
```
Only immutable, hashable objects can be dict keys / set elements. `frozenset`, `tuple` (of hashables), `str`, numbers — yes. `list`, `dict`, `set` — no.

## 18.9 Iterator Exhaustion

```python
gen = (x for x in range(5))
list(gen)     # [0,1,2,3,4]
list(gen)      # [] -- EXHAUSTED! generators are single-pass only

it = iter([1,2,3])
sum(it)         # 6
sum(it)          # 0 -- also exhausted
```
> **Interview Tip:** If you need to iterate the same data multiple times, use a `list`/`tuple`, not a generator/map/filter/zip object (all single-pass iterators in Python 3).

## 18.10 `is` vs `==` Misuse

```python
if x == None: ...     # works, but non-Pythonic
if x is None: ...       # correct/idiomatic — also avoids surprises with custom __eq__
```

## 18.11 Modifying a List While Iterating Over It

```python
# WRONG -- skips elements! (index shifts as items are removed)
for x in arr:
    if x < 0:
        arr.remove(x)

# CORRECT -- iterate over a copy, or build a new list
arr = [x for x in arr if x >= 0]
# or:
for x in arr[:]:      # iterate a COPY (slice) while modifying original
    if x < 0:
        arr.remove(x)
```

## 18.12 `+=` on Function Arguments (mutable vs immutable behavior differs!)

```python
def f(x):
    x += [1]     # if x is a list, this MUTATES in place (uses __iadd__/extend semantics)

def g(x):
    x += 1        # if x is an int, this REBINDS locally, doesn't affect caller
```

---

# 19. Best Practices

## 19.1 Clean Code & PEP 8 Essentials

```
- 4 spaces per indent level (never tabs)
- snake_case for variables/functions, PascalCase for classes
- Line length ~79-99 chars (community standard varies)
- One statement per line
- Meaningful names: `left`, `right`, `mid` not `l`, `r`, `m` (though CP often shortens for speed)
- Blank line between logical sections
```

## 19.2 Efficient & Memory-Efficient Coding

- Prefer built-in functions/modules (`sum`, `heapq`, `bisect`) — implemented in C, much faster than hand-rolled pure-Python loops.
- Avoid repeated `len()` calls inside loop conditions if the length doesn't change — hoist to a variable if it's expensive to recompute (rarely matters for `list`, since `len` is O(1), but matters for chained/derived lengths).
- Use generators for single-pass large data.
- Use `set`/`dict` for membership tests over `list`.

## 19.3 Contest Coding Style vs Interview Coding Style

| Aspect | Contest (CP) | Interview |
|---|---|---|
| Variable names | short (`i`, `n`, `dp`) | descriptive (`index`, `size`, `memo`) |
| I/O | `sys.stdin`/fast I/O | usually given via function signature |
| Structure | single `main()`, minimal abstraction | classes/helper functions, readable |
| Comments | minimal/none | explain intent, especially for tricky logic |
| Edge cases | tested via stress-testing scripts | explicitly discussed out loud |
| Priorities | speed of writing + runtime | correctness + communication + complexity analysis |

## 19.4 Interview Coding Style Checklist

```
1. Clarify constraints & edge cases BEFORE coding (empty input, n=1, duplicates, negatives)
2. State your approach & complexity out loud before diving in
3. Use descriptive names
4. Write helper functions for repeated logic
5. Handle edge cases explicitly (empty list, single element, None input)
6. Test with a dry run on a small example after writing
7. State final time & space complexity
```

---

# 20. Problem Recognition — What Structure to Use When

## 20.1 Decision Tree

```
                    ┌─────────────────────────┐
                    │ What does the problem     │
                    │ need to do MOST OFTEN?      │
                    └──────────┬──────────────────┘
                               │
      ┌────────────┬───────────┼───────────┬─────────────┬───────────────┐
      ▼            ▼           ▼            ▼             ▼               ▼
 Fast membership Count freq  Order matters Need min/max  FIFO/BFS      Fixed pairs/
 check O(1)?     of items?   + duplicates?  repeatedly?   processing?   coordinates?
      │            │           │            │             │               │
      ▼            ▼           ▼            ▼             ▼               ▼
    set          Counter      list        heapq         deque          tuple
 (or dict keys)                                                       (hashable,
                                                                        dict key)

           Need key->value mapping with O(1) lookup?  -->  dict / defaultdict
           Need sorted order maintained during inserts? --> bisect (or heapq if only extremes matter)
           Need to undo/redo, matched pairs (parens)?  --> list as a STACK (append/pop)
           Need level-order / shortest-path-unweighted? --> deque as a QUEUE (append/popleft)
           Need k-th largest/smallest repeatedly?       --> heapq
           Need grouping by a derived key?              --> defaultdict(list) or itertools.groupby (sorted first)
           Need memoized recursive results?             --> functools.lru_cache or dict memo
           Need every combination/permutation/subset?   --> itertools
```

## 20.2 Structure Selection Table

| Need | Structure | Why |
|---|---|---|
| Stack (LIFO) | `list` (`append`/`pop`) | O(1) both ops at the end |
| Queue (FIFO) | `collections.deque` | O(1) both ends; `list.pop(0)` is O(n) |
| Priority queue | `heapq` | O(log n) push/pop, always min |
| Unique elements | `set` | O(1) membership |
| Frequency count | `collections.Counter` | purpose-built, `most_common` |
| Key→value lookup | `dict` | O(1) average |
| Auto-init grouping | `collections.defaultdict` | avoids manual key checks |
| Sorted insertion / binary search | `bisect` | O(log n) search |
| LRU cache | `collections.OrderedDict` or `functools.lru_cache` | O(1) reordering/eviction |
| Graph adjacency list | `defaultdict(list)` | natural sparse representation |
| Memoized recursion | `functools.lru_cache` | automatic caching |
| Combinatorics | `itertools` | lazy, no manual backtracking boilerplate needed for generation |
| Coordinates / composite keys | `tuple` | hashable, usable in `set`/`dict` |
| Union-Find operations | custom `DSU` class | path compression + union by rank |

## 20.3 Comparison: `list` vs `deque` vs `heapq` for Queue-like Needs

| | `list` | `deque` | `heapq` |
|---|---|---|---|
| Append at end | O(1) | O(1) | O(log n) |
| Remove from front | O(n) | O(1) | N/A (only min) |
| Access min/max | O(n) | O(n) | O(1) peek |
| Use case | stack | BFS queue, sliding window | priority-based processing |

# 21. Cheat Sheets

## 21.1 Python Syntax Cheat Sheet

```python
# Variables & types
x = 5; s = "str"; f = 3.14; b = True; n = None

# Conditionals
if cond: ...
elif cond2: ...
else: ...

# Loops
for x in iterable: ...
while cond: ...
for i in range(n): ...
for i, x in enumerate(arr): ...

# Functions
def f(a, b=1, *args, **kwargs): return a+b
lambda x: x*2

# Comprehensions
[x for x in it if cond]
{x: y for x, y in it}
{x for x in it}
(x for x in it)

# Classes
class Foo:
    def __init__(self, x): self.x = x
    def __repr__(self): return f"Foo({self.x})"
```

## 21.2 Built-in Functions Cheat Sheet

```python
len(x) abs(x) sum(x) min(x) max(x) sorted(x) reversed(x)
enumerate(x) zip(a,b) map(f,x) filter(f,x)
any(x) all(x) round(x,n) divmod(a,b) pow(a,b,m)
isinstance(x,T) type(x) id(x) hash(x)
ord(c) chr(i) bin(n) hex(n) oct(n)
```

## 21.3 `collections` Cheat Sheet

```python
from collections import Counter, defaultdict, deque, OrderedDict, namedtuple

Counter(iterable).most_common(k)
defaultdict(list) / defaultdict(int) / defaultdict(lambda: defaultdict(int))
deque(); dq.append(x); dq.appendleft(x); dq.pop(); dq.popleft(); dq.rotate(k)
OrderedDict(); od.move_to_end(k); od.popitem(last=False)
namedtuple("Name", "field1 field2")
```

## 21.4 `itertools` Cheat Sheet

```python
from itertools import (permutations, combinations, combinations_with_replacement,
                        product, groupby, accumulate, chain, islice,
                        count, cycle, repeat, pairwise, dropwhile, takewhile)

permutations(iterable, r=None)
combinations(iterable, r)
product(*iterables, repeat=1)
groupby(sorted_iterable, key=func)      # remember: consecutive only, sort first!
accumulate(iterable, func=add, initial=None)   # prefix sums
chain(*iterables) / chain.from_iterable(it_of_its)
islice(iterable, start, stop, step)
pairwise(iterable)                        # (a0,a1),(a1,a2),...
```

## 21.5 `heapq` Cheat Sheet

```python
import heapq
heap = []
heapq.heappush(heap, x)
heapq.heappop(heap)
heapq.heapify(list_)                # O(n)
heapq.nlargest(k, iterable)
heapq.nsmallest(k, iterable)
heapq.heappushpop(heap, x)
heapq.heapreplace(heap, x)
# max-heap: push -x, pop and negate
```

## 21.6 `bisect` Cheat Sheet

```python
import bisect
bisect.bisect_left(a, x)     # leftmost insertion point
bisect.bisect_right(a, x)      # rightmost insertion point (== bisect.bisect)
bisect.insort_left(a, x)
bisect.insort_right(a, x)
```

## 21.7 Time Complexity Cheat Sheet

```
O(1)        dict/set access, list index/append, heap peek
O(log n)    binary search (bisect), heap push/pop
O(n)        linear scan, list search, string build via join
O(n log n)  sorting, heapify+n pops, nlargest(k)
O(n^2)      nested loops, naive string += in loop, list.insert(0,x) in loop
O(2^n)      unmemoized recursive subsets/Fibonacci
O(n!)       generating all permutations
```

## 21.8 Memory Cheat Sheet

```
Mutable:    list, dict, set, bytearray
Immutable:  int, float, bool, str, tuple, frozenset, bytes

Shallow copy: lst.copy(), lst[:], list(lst), dict(d)  -- top level only
Deep copy:    copy.deepcopy(obj)                        -- fully independent

Small int cache: [-5, 256]
Use __slots__ for millions of small objects
```

## 21.9 Interview Cheat Sheet

```
Before coding:
  - restate the problem
  - clarify constraints (n range, duplicates, negatives, empty input)
  - state approach + time/space complexity

While coding:
  - descriptive names
  - handle edge cases explicitly
  - use the right data structure (see §20)

After coding:
  - dry run on a small example
  - state final complexity
  - discuss possible optimizations/alternatives
```

---

# 22. Practice Problems

Categorized by Python concept practiced. (Platform difficulty ratings are approximate/platform-defined and may shift over time.)

## 22.1 Python Basics

| Problem | Platform | Difficulty | Concepts | Link |
|---|---|---|---|---|
| Two Sum | LeetCode | Easy | dict, enumerate | leetcode.com/problems/two-sum |
| Palindrome Number | LeetCode | Easy | int/str conversion, slicing | leetcode.com/problems/palindrome-number |
| FizzBuzz | LeetCode | Easy | control flow, modulo | leetcode.com/problems/fizz-buzz |
| Reverse Integer | LeetCode | Medium | int overflow handling, sign logic | leetcode.com/problems/reverse-integer |

## 22.2 Collections

| Problem | Platform | Difficulty | Concepts | Link |
|---|---|---|---|---|
| Valid Anagram | LeetCode | Easy | Counter | leetcode.com/problems/valid-anagram |
| Top K Frequent Elements | LeetCode | Medium | Counter, heapq/most_common | leetcode.com/problems/top-k-frequent-elements |
| LRU Cache | LeetCode | Medium | OrderedDict | leetcode.com/problems/lru-cache |
| Number of Islands | LeetCode | Medium | deque (BFS) | leetcode.com/problems/number-of-islands |
| Group Anagrams | LeetCode | Medium | defaultdict | leetcode.com/problems/group-anagrams |

## 22.3 Built-ins

| Problem | Platform | Difficulty | Concepts | Link |
|---|---|---|---|---|
| Sqrt(x) | LeetCode | Easy | math.isqrt / binary search | leetcode.com/problems/sqrtx |
| Super Pow | LeetCode | Medium | pow(x,y,mod) | leetcode.com/problems/super-pow |
| Merge Intervals | LeetCode | Medium | sorted(key=) | leetcode.com/problems/merge-intervals |

## 22.4 Iterators & Generators

| Problem | Platform | Difficulty | Concepts | Link |
|---|---|---|---|---|
| Flatten Nested List Iterator | LeetCode | Medium | custom iterator protocol | leetcode.com/problems/flatten-nested-list-iterator |
| Binary Search Tree Iterator | LeetCode | Medium | generators, yield | leetcode.com/problems/binary-search-tree-iterator |
| Peeking Iterator | LeetCode | Medium | iterator wrapping | leetcode.com/problems/peeking-iterator |

## 22.5 Comprehensions

| Problem | Platform | Difficulty | Concepts | Link |
|---|---|---|---|---|
| Spiral Matrix | LeetCode | Medium | nested list comprehension, slicing | leetcode.com/problems/spiral-matrix |
| Transpose Matrix | LeetCode | Easy | zip(*matrix) | leetcode.com/problems/transpose-matrix |
| Set Matrix Zeroes | LeetCode | Medium | comprehension + set tracking | leetcode.com/problems/set-matrix-zeroes |

## 22.6 heapq

| Problem | Platform | Difficulty | Concepts | Link |
|---|---|---|---|---|
| Kth Largest Element in an Array | LeetCode | Medium | heapq.nlargest / heap of size k | leetcode.com/problems/kth-largest-element-in-an-array |
| Merge k Sorted Lists | LeetCode | Hard | heapq with tuples | leetcode.com/problems/merge-k-sorted-lists |
| Find Median from Data Stream | LeetCode | Hard | two heaps | leetcode.com/problems/find-median-from-data-stream |
| Network Delay Time | LeetCode | Medium | heapq, Dijkstra | leetcode.com/problems/network-delay-time |

## 22.7 bisect

| Problem | Platform | Difficulty | Concepts | Link |
|---|---|---|---|---|
| Search Insert Position | LeetCode | Easy | bisect_left | leetcode.com/problems/search-insert-position |
| Longest Increasing Subsequence | LeetCode | Medium | bisect, O(n log n) LIS | leetcode.com/problems/longest-increasing-subsequence |
| Find First and Last Position of Element in Sorted Array | LeetCode | Medium | bisect_left/right | leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array |

## 22.8 itertools

| Problem | Platform | Difficulty | Concepts | Link |
|---|---|---|---|---|
| Permutations | LeetCode | Medium | itertools.permutations (or manual backtracking) | leetcode.com/problems/permutations |
| Combinations | LeetCode | Medium | itertools.combinations | leetcode.com/problems/combinations |
| Subsets | LeetCode | Medium | itertools.chain + combinations | leetcode.com/problems/subsets |

## 22.9 Functional Programming

| Problem | Platform | Difficulty | Concepts | Link |
|---|---|---|---|---|
| Sort Characters By Frequency | LeetCode | Medium | Counter + sorted(key=) | leetcode.com/problems/sort-characters-by-frequency |
| Largest Number | LeetCode | Medium | functools.cmp_to_key | leetcode.com/problems/largest-number |

## 22.10 Python Tricks & Idioms

| Problem | Platform | Difficulty | Concepts | Link |
|---|---|---|---|---|
| Rotate Array | LeetCode | Medium | slicing tricks | leetcode.com/problems/rotate-array |
| Valid Parentheses | LeetCode | Easy | list as stack | leetcode.com/problems/valid-parentheses |
| Product of Array Except Self | LeetCode | Medium | itertools.accumulate / prefix-suffix | leetcode.com/problems/product-of-array-except-self |

## 22.11 Additional Practice Sources

- **HackerRank** — "Python" domain (basic syntax, closures, decorators drills): hackerrank.com/domains/python
- **Codewars** — Python kata for idiomatic-style practice: codewars.com
- **Exercism** — Python track for exercises + mentored feedback: exercism.org/tracks/python
- **GeeksforGeeks** — Python DSA article series: geeksforgeeks.org/python-data-structures-and-algorithms
- **Codeforces** — algorithmic contests, good for fast-I/O practice: codeforces.com
- **AtCoder** — clean, well-structured problems (Beginner Contest is great for Python I/O drills): atcoder.jp
- **CodeChef** — wide difficulty range: codechef.com
- **Code360 (Coding Ninjas)** — interview-pattern-focused problem sets: naukri.com/code360

---

# 23. Final Revision — Mind Maps & Quick Recall

## 23.1 One-Page Revision

```
PYTHON FOR DSA -- ONE PAGE

DATA TYPES
  list(mutable,O(1)idx) tuple(immutable) set/frozenset(O(1)membership)
  dict(O(1)kv) str(immutable)

COLLECTIONS
  Counter(freq) defaultdict(auto-init) deque(O(1)both ends)
  OrderedDict(LRU) namedtuple(readable tuples)

STD LIB
  math(isqrt,gcd) itertools(combinatorics,accumulate) functools(lru_cache,reduce)
  heapq(priority queue,O(log n)) bisect(binary search,O(log n))

ITERATION
  iterator protocol: __iter__/__next__
  generators: yield -> lazy, O(1) memory
  comprehensions: [x for x in it if cond]

FUNCTIONAL
  map/filter/reduce/zip/enumerate/sorted(key=)/any/all

OOP
  __init__ __repr__ __eq__ __hash__ __lt__ __slots__ dataclass

MEMORY
  refcounting + gc for cycles; small-int cache [-5,256]; str interning
  shallow vs deep copy; mutable default arg trap

CP TRICKS
  sys.stdin fast input; deque not list.pop(0); join not += ; lru_cache memoization
  setrecursionlimit for deep DFS

PITFALLS
  mutable default args | shallow copy aliasing | late-binding closures
  -7//2 = -4 | float imprecision | iterator exhaustion | unhashable list as key
```

## 23.2 Built-in Functions Map

```
                    ┌── math: abs, round, pow, divmod
                    │
  TRANSFORM ────────┼── map, filter, sorted, reversed, enumerate, zip
                    │
  AGGREGATE ────────┼── sum, min, max, any, all, len
                    │
  INSPECT ──────────┼── type, isinstance, id, hash, callable, vars
                    │
  CONVERT ──────────┼── int, float, str, list, tuple, set, dict, bin, hex, oct, chr, ord
                    │
  I/O ──────────────┴── input, print, format, repr
```

## 23.3 collections Map

```
                collections
                    │
        ┌───────────┼───────────┬─────────────┬───────────────┐
     Counter    defaultdict   deque       OrderedDict      namedtuple
   (frequency) (auto-init)  (both-end    (LRU cache,      (readable
                              O(1))       move_to_end)      immutable rows)
```

## 23.4 Standard Library Map

```
                     stdlib for DSA
                          │
    ┌──────────┬──────────┼───────────┬────────────┬─────────────┐
  math       itertools  functools    heapq        bisect       operator
(number      (combinat- (memoize,   (priority    (binary       (fast
 theory)      orics,     reduce,     queue)       search on     sort key
              lazy       partial)                 sorted list)  fns)
              chains)
```

## 23.5 Complexity Sheet (quick recall)

```
list append/pop(end): O(1)  |  list pop(0)/insert(0): O(n)
dict/set get/set/in:   O(1) avg
heapq push/pop:         O(log n)  |  heapify: O(n)
bisect search:            O(log n)  |  insort: O(n)
sort:                       O(n log n)
```

## 23.6 Python Syntax Sheet — see §21.1

## 23.7 Interview Notes — see §19.4 and §21.9

## 23.8 Python Tricks Sheet — see §14 (Idioms) in full

```

## 23.10 1-Hour Revision Plan

```
0:00-0:10  Fundamentals: variables, mutability, identity vs equality (§1)
0:10-0:20  Operators + control flow, walrus operator (§2-3)
0:20-0:30  Functions: closures, decorators, lru_cache (§4)
0:30-0:40  Built-in types + complexity tables (§5, §16)
0:40:0:50  Collections module: Counter/defaultdict/deque/OrderedDict (§6)
0:50-1:00  itertools + heapq + bisect walkthrough with code (§7)
(Then, time permitting: iterators/generators §8, idioms §14, pitfalls §18)
```

---

## Closing Notes

This handbook is designed to be the **single Python-language reference** you need alongside any DSA/algorithms textbook. It intentionally does *not* teach algorithms or data structure theory (arrays, trees, graphs, DP) — only the Python mechanics, standard library, idioms, and performance considerations that let you implement those algorithms correctly and efficiently in interviews and contests.

