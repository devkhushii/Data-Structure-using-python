# 🔑 THE COMPLETE HASHING HANDBOOK 
---

## 📖 Table of Contents

1. [Introduction to Hashing](#1-introduction-to-hashing)
2. [Hashing in Python](#2-hashing-in-python)
3. [Hash Functions](#3-hash-functions)
4. [Collision Resolution](#4-collision-resolution)
5. [Hashing Patterns (Problem-Solving Templates)](#5-hashing-patterns-problem-solving-templates)
6. [Real-World Applications](#6-real-world-applications)
7. [Problem Recognition — "Is This a Hashing Problem?"](#7-problem-recognition--is-this-a-hashing-problem)
8. [Optimization Journey: Brute Force → Better → Optimal](#8-optimization-journey-brute-force--better--optimal)
9. [Interview Preparation](#9-interview-preparation)
10. [Python Tips & Tool Belt](#10-python-tips--tool-belt)
11. [Common Mistakes & Pitfalls](#11-common-mistakes--pitfalls)
12. [Cheat Sheets](#12-cheat-sheets)
13. [Practice Problems (Curated, Multi-Platform)](#13-practice-problems-curated-multi-platform)
14. [Final Revision — Mind Maps & Quick Recall](#14-final-revision--mind-maps--quick-recall)
15. [FAQs](#15-faqs)



---

## 1. Introduction to Hashing

### 1.1 What Is Hashing?

**Definition:** Hashing is the process of converting an input (called a **key**) of arbitrary size into a fixed-size value (called a **hash value**, **hash code**, or simply **hash**) using a mathematical function called a **hash function**. This hash value is then used as an index to store or retrieve the associated data extremely fast — ideally in **O(1)** time.

**Why it exists:** Searching for a value in an unsorted array takes O(n). Searching in a sorted array/BST takes O(log n). Humans wanted something faster — **O(1)** average-case lookup. Hashing was invented to achieve near-constant time storage and retrieval by trading memory for speed and using a clever mapping instead of comparison-based search.

**Intuition:** Instead of *searching* for where a value might be, we *compute* where it should be. If you know the formula, you don't need to look — you go directly there.

**Real-world analogy:** Think of a library that doesn't use alphabetical shelving. Instead, every book title is fed into a formula that spits out a shelf number (e.g., "Harry Potter" → shelf 42). To find the book again, you don't scan every shelf — you recompute the formula, go straight to shelf 42, and pick it up. A coat-check counter works the same way: your coat gets a numbered tag (hash), and retrieval is just "go to peg number N," not "search every peg."

### 1.2 A Brief History

| Era | Milestone |
|---|---|
| 1950s | Hans Peter Luhn (IBM) proposes hash coding for information retrieval |
| 1960s | Open addressing & chaining formalized in early computer science literature |
| 1970s | Knuth's *The Art of Computer Programming Vol. 3* formalizes hashing theory |
| 1979 | Universal hashing introduced by Carter & Wegman |
| 1990s–2000s | Cryptographic hash functions (MD5, SHA family) mature |
| 2000s+ | Language-level hash tables (Python `dict`, Java `HashMap`, C++ `unordered_map`) become ubiquitous |
| 2012+ | Python and other languages add hash randomization (SipHash) to prevent DoS via hash-flooding attacks |

### 1.3 Core Vocabulary

| Term | Meaning |
|---|---|
| **Key** | The original input value you want to store/retrieve (e.g., `"apple"`) |
| **Hash Function** | A function `h(key)` that converts a key into an integer |
| **Hash Value / Hash Code** | The integer output of the hash function |
| **Hash Table** | The underlying array/data structure that stores key-value pairs using hash-derived indices |
| **Bucket / Slot** | A position in the hash table array |
| **Collision** | Two different keys producing the same index |
| **Load Factor** | `(number of entries) / (number of buckets)` — a measure of how "full" the table is |
| **Rehashing** | Growing the table and redistributing all entries when load factor gets too high |

### 1.4 ASCII Visualization — The Big Picture

```
            KEY                  HASH FUNCTION              INDEX          HASH TABLE (array of buckets)
        ┌─────────┐            ┌───────────────┐        ┌─────────┐      ┌───────────────────────────┐
        │ "apple"  │ ────────▶ │ h(key) % size │ ─────▶ │    3    │ ──▶  │ 0: None                    │
        └─────────┘            └───────────────┘        └─────────┘      │ 1: None                    │
                                                                          │ 2: None                    │
                                                                          │ 3: [("apple", 10)]  ◀──────┤
                                                                          │ 4: None                    │
                                                                          │ 5: None                    │
                                                                          └───────────────────────────┘
```

### 1.5 Why Hashing Exists — Comparison With Other Lookup Structures

| Structure | Search | Insert | Delete | Ordered? | Notes |
|---|---|---|---|---|---|
| Unsorted Array | O(n) | O(1) | O(n) | No | Simple, slow search |
| Sorted Array | O(log n) | O(n) | O(n) | Yes | Binary search possible |
| Balanced BST | O(log n) | O(log n) | O(log n) | Yes | Ordered traversal possible |
| **Hash Table** | **O(1) avg** | **O(1) avg** | **O(1) avg** | **No** | Fastest average case, no ordering guarantee |

> ⚠️ **Warning:** Hash table operations are O(1) **on average**, not worst-case. Worst case (many collisions) can degrade to O(n). This is a favorite interview trap — always mention average vs worst case.

### 1.6 Characteristics of a Hash Table

- **Fast average-case access** — O(1) for insert, delete, search.
- **No inherent ordering** — unlike arrays or BSTs (Python 3.7+ dicts preserve *insertion* order, but that's an implementation detail, not a hashing property).
- **Space overhead** — hash tables typically use more memory than arrays to keep load factor low.
- **Dependent on hash function quality** — a poor hash function destroys performance.

### 1.7 Advantages & Disadvantages

**Advantages**
- Average O(1) time complexity for core operations.
- Extremely versatile — used in caching, databases, compilers, networking, cryptography.
- Simplifies many algorithmic problems (frequency counting, duplicate detection, etc.) from O(n²) to O(n).

**Disadvantages**
- Worst-case O(n) if hash function is poor or adversarial collisions occur.
- No ordering — can't easily do range queries or "find the next largest key."
- Extra memory overhead compared to arrays.
- Hash function design is non-trivial to get right for arbitrary data.

### 1.8 Applications At a Glance

Dictionaries • Caching (LRU/LFU) • Database indexing • Compiler symbol tables • Spell checkers • Networking (routing tables, load balancers) • Deduplication • Cryptographic integrity checks • Blockchain • Password storage • Bloom filters • Rate limiting • Content-addressable storage (Git, IPFS)

We will cover each of these in [Section 6](#6-real-world-applications).

### 1.9 Summary & Revision Notes

- Hashing converts arbitrary keys → fixed-size integers → array indices.
- Goal: O(1) average-case operations by direct computation instead of search.
- Core vocabulary: key, hash function, hash value, hash table, bucket, collision, load factor, rehashing.
- Average case ≠ worst case — always qualify complexity claims in interviews.

---

## 2. Hashing in Python

### 2.1 The `hash()` Built-in

**Definition:** Python's built-in `hash(obj)` function returns an integer hash value for any **hashable** object. Python's `dict` and `set` use this value internally to decide bucket placement.

```python
print(hash(42))          # Integers hash to themselves (mostly)
print(hash("apple"))     # Randomized per process (see 2.9)
print(hash((1, 2, 3)))   # Tuples are hashable if all elements are hashable
print(hash(3.14))        # Floats are hashable
```

**Line-by-line explanation:**
- `hash(42)` → For small integers, Python's hash is the integer itself (with a special case for -1).
- `hash("apple")` → Strings use **SipHash**, seeded randomly per process (PYTHONHASHSEED), so the value differs between runs unless the seed is fixed.
- `hash((1, 2, 3))` → Tuples combine the hashes of their elements. Tuple is hashable **only if every element inside it is hashable**.
- `hash(3.14)` → Floats are hashable; note that `hash(1) == hash(1.0)` because Python guarantees equal values hash equally, even across numeric types.

> 📝 **Note:** `hash(1) == hash(1.0) == hash(True)` — this is required because `1 == 1.0 == True` in Python, and hashable objects that are `==` **must** hash the same (this is the Hash-Equality Contract, see 2.7).

### 2.2 Hashability — What Can Be Hashed?

| Type | Hashable? | Why |
|---|---|---|
| `int`, `float`, `bool`, `complex` | ✅ Yes | Immutable |
| `str`, `bytes` | ✅ Yes | Immutable |
| `tuple` | ✅ Yes, if all elements hashable | Immutable container |
| `frozenset` | ✅ Yes | Immutable set |
| `list` | ❌ No | Mutable |
| `dict` | ❌ No | Mutable |
| `set` | ❌ No | Mutable |
| Custom object (default) | ✅ Yes | Uses `id()`-based identity hash by default |

```python
d = {}
d[(1, 2)] = "point"       # OK — tuple is hashable
d[frozenset([1, 2])] = "s" # OK — frozenset is hashable
d[[1, 2]] = "fail"         # ❌ TypeError: unhashable type: 'list'
```

**Why mutability matters:** If a mutable object were used as a dict key and then modified, its hash value could change — but the dict has already placed it in a bucket based on the *old* hash. This would make the entry permanently unfindable, silently corrupting the data structure. Python prevents this entire class of bugs by disallowing mutable keys.

### 2.3 `dict` — Python's Hash Map

```python
d = {"a": 1, "b": 2}
d["c"] = 3          # Insert  — O(1) average
print(d["a"])        # Access  — O(1) average
del d["b"]           # Delete  — O(1) average
print("a" in d)      # Membership — O(1) average
```

**Internal working (CPython):**
- CPython dicts are implemented as **open-addressed hash tables** (not chaining!) with a **combined table** design since Python 3.6, storing insertion order separately from the hash table for memory efficiency.
- Each slot stores `(hash, key, value)`.
- On collision, CPython uses a **pseudo-random probing sequence** (open addressing with perturbation), not simple linear probing.
- Dicts resize (grow) when roughly 2/3 full, and the growth factor is typically 4x for small tables, 2x for larger ones.

### 2.4 ASCII Diagram — Python Dict Memory Layout (Simplified, 3.6+)

```
   Insertion-order array (compact table)         Hash table (sparse index array)
   ┌────┬─────────┬────────┐                     ┌───┬───┬───┬───┬───┬───┬───┬───┐
   │ 0  │ "a"     │ 1      │                     │ - │ 0 │ - │ 1 │ - │ - │ - │ - │
   ├────┼─────────┼────────┤                     └───┴───┴───┴───┴───┴───┴───┴───┘
   │ 1  │ "c"     │ 3      │                        index = hash("a") % 8 → slot 1 → points to entry 0
   └────┴─────────┴────────┘                        index = hash("c") % 8 → slot 3 → points to entry 1
```
This split-table design is why Python dicts (3.6+) preserve insertion order while still being true hash tables.

### 2.5 `set` — Python's Hash Set

```python
s = {1, 2, 3}
s.add(4)             # O(1) average
s.discard(2)         # O(1) average
print(3 in s)         # O(1) average membership test
```

`set` uses the **same underlying hash table mechanics as dict**, but stores only keys (no values). Internally implemented via a similar open-addressing scheme in CPython's `setobject.c`.

### 2.6 `frozenset` — Immutable Set

```python
fs = frozenset([1, 2, 3])
d = {fs: "immutable set as key"}   # Legal because frozenset is hashable
```

Use when you need a **hashable, unordered collection** — e.g., as a dict key or set element, or to guarantee the caller can't mutate it.

### 2.7 `__hash__()` and `__eq__()` — The Hash-Equality Contract

**Rule:** If `a == b`, then `hash(a) == hash(b)` **must** hold. Violating this breaks dict/set behavior silently.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
```

**Line-by-line explanation:**
- `__eq__` defines when two `Point`s are considered equal (component-wise).
- `__hash__` **must** be consistent with `__eq__`: we hash the tuple `(x, y)` so equal points always hash identically.
- If you define `__eq__` but forget `__hash__`, Python **automatically sets `__hash__ = None`**, making instances unhashable!

> ⚠️ **Warning (Very common mistake):** Defining `__eq__` without `__hash__` makes your objects **unhashable** — you cannot put them in a `set` or use them as `dict` keys anymore. Always define both together, or explicitly set `__hash__ = SomeBaseClass.__hash__` if you want to keep default identity hashing.

```python
class Bad:
    def __eq__(self, other):
        return True

b = Bad()
{b}  # TypeError: unhashable type: 'Bad'
```

### 2.8 Default Object Hashing (Identity-Based)

By default (no `__eq__`/`__hash__` override), Python objects hash based on `id(obj)` (memory address), and `==` behaves like `is`. Two distinct objects with identical *contents* are **not** equal or hash-equal unless you override these methods.

### 2.9 Hash Randomization (Security)

Since Python 3.3, string/bytes hashing is randomized per-process using **SipHash-1-3** (formerly SipHash-2-4), seeded by `PYTHONHASHSEED`. This defends against **hash-flooding DoS attacks**, where an attacker crafts many keys that collide in a predictable, non-randomized hash function, forcing O(n) behavior on every operation.

```bash
# Reproducible hashing for debugging (disables randomization)
PYTHONHASHSEED=0 python3 script.py
```

> 📝 **Note:** This is why you should never rely on `hash()` output being the same across different runs of a program (for `str`/`bytes`). It's stable *within* a single run, not across runs.

### 2.10 Python Dictionary Internals — Deep Dive

```
Step 1: hash(key) computed
Step 2: mask = table_size - 1   (table size is always a power of 2)
Step 3: initial_slot = hash & mask
Step 4: If slot occupied by a different key → perturbation-based probing:
            j = ((5*j) + 1 + perturb) & mask;  perturb >>= PERTURB_SHIFT
        Repeat until an empty slot or matching key is found.
Step 5: On growth (load factor > ~2/3): allocate bigger table, re-insert all entries.
```

This differs from "textbook" linear probing — CPython's probing sequence pseudo-randomly jumps around the table, which reduces clustering.

### 2.11 Python Set Internals

Sets in CPython (`Objects/setobject.c`) use a very similar open-addressing table to dicts, but store only keys and use a slightly different resize policy (grows more aggressively — 4x — for very small sets to reduce early resize churn).

### 2.12 `dict` vs `set` vs `list` — Performance Comparison

| Operation | `list` | `set` | `dict` |
|---|---|---|---|
| Membership (`in`) | O(n) | O(1) avg | O(1) avg (key lookup) |
| Insert | O(1) amortized (`append`) | O(1) avg | O(1) avg |
| Delete | O(n) | O(1) avg | O(1) avg |
| Ordered iteration | Yes (index order) | No guaranteed order | Yes (insertion order, 3.7+) |
| Duplicate elements | Allowed | Not allowed | Keys unique, values can repeat |

### 2.13 Best Practices

- Use `set`/`dict` for membership tests instead of `list` whenever the collection is large or checked repeatedly.
- Use `frozenset` for hashable, immutable groupings.
- Always pair custom `__eq__` with custom `__hash__`.
- Don't mutate objects that are currently used as dict keys or set members (even if technically hashable via identity), since it can violate the hash-equality contract in subtle ways for composite objects.
- Prefer `collections.defaultdict` and `collections.Counter` for cleaner frequency/grouping code (see [Section 10](#10-python-tips--tool-belt)).

### 2.14 Summary & Revision Notes

- `hash()` is the entry point; hashability requires immutability (by convention) and a consistent `__eq__`/`__hash__` pair.
- CPython's `dict`/`set` use open addressing with pseudo-random probing, not textbook chaining.
- Since 3.7, dicts preserve insertion order (implementation detail, guaranteed by spec since 3.7).
- String hashing is randomized per process for security (SipHash).

---

## 3. Hash Functions

### 3.1 What Makes a Good Hash Function?

| Property | Meaning |
|---|---|
| **Deterministic** | Same input always produces same output (within a run) |
| **Uniform distribution** | Outputs spread evenly across the output range, minimizing collisions |
| **Fast to compute** | O(length of key), ideally with small constants |
| **Avalanche effect** | A tiny change in input causes a large, unpredictable change in output |
| **Low collision rate** | Different inputs rarely map to the same output |

### 3.2 Bad Hash Function — Example & Why It Fails

```python
def bad_hash(key: str) -> int:
    return len(key) % 10   # Only considers length!
```
**Why it's bad:** `"cat"`, `"dog"`, `"bat"` all have length 3 → all collide. Ignores actual content entirely. This is deterministic but has terrible uniformity and no avalanche effect.

### 3.3 A Simple Polynomial Rolling Hash

**Problem:** Design a hash function for strings that considers every character and position.

**Approach:** Treat the string as a number in base `p` (a prime, e.g., 31), take modulo a large prime `M` to bound the result.

```python
def polynomial_hash(s: str, base: int = 31, mod: int = 10**9 + 7) -> int:
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod
    return h
```

**Line-by-line explanation:**
- `h = 0` — accumulator initialized.
- Loop over each character: `h = h * base + ord(ch)` — this is Horner's method, treating the string like a polynomial `s[0]*base^(n-1) + s[1]*base^(n-2) + ... + s[n-1]`.
- `% mod` — keeps the number bounded and prevents overflow (not a concern in Python, but keeps values in a fixed range for table indexing).

**Dry run** for `s = "abc"`, `base = 31`, `mod = 1000000007`:

| Step | ch | ord(ch) | h before | h = h*31 + ord(ch) |
|---|---|---|---|---|
| 1 | 'a' | 97 | 0 | 0*31+97 = 97 |
| 2 | 'b' | 98 | 97 | 97*31+98 = 3105 |
| 3 | 'c' | 99 | 3105 | 3105*31+99 = 96354 |

Final hash = `96354`.

**Time Complexity:** O(n) where n = length of string.
**Space Complexity:** O(1) extra.

**Use case:** Rolling hash for substring hashing (see Section 5.13), string comparison, plagiarism detection, Rabin–Karp string matching.

### 3.4 Rolling Hash — The "Rolling" Trick

The magic of a **rolling** hash is being able to compute the hash of `s[i+1:i+1+k]` from the hash of `s[i:i+k]` in O(1), instead of recomputing from scratch in O(k).

```
hash(s[i+1 : i+1+k]) = (hash(s[i:i+k]) - s[i]*base^(k-1)) * base + s[i+k]   (mod M)
```

```python
def rolling_hash_example(s: str, k: int, base: int = 31, mod: int = 10**9 + 7):
    n = len(s)
    if n < k:
        return []
    base_k_minus_1 = pow(base, k - 1, mod)
    h = 0
    for i in range(k):
        h = (h * base + ord(s[i])) % mod
    hashes = [h]
    for i in range(1, n - k + 1):
        h = (h - ord(s[i - 1]) * base_k_minus_1) % mod
        h = (h * base + ord(s[i + k - 1])) % mod
        hashes.append(h % mod)
    return hashes
```

**Dry run** for `s = "abcab"`, `k = 3`:
- Window 0: `"abc"` → compute directly → h0
- Window 1: `"bca"` → remove `'a'`'s contribution, shift, add `'a'` (new last char) → h1, computed in O(1)
- Window 2: `"cab"` → same O(1) update → h2

**Complexity:** O(n) total for all windows (vs O(n·k) naive recomputation) — this is the entire point of a rolling hash.

### 3.5 Modulo Hashing

The simplest hashing scheme for integers: `index = key % table_size`.

```python
def modulo_hash(key: int, table_size: int) -> int:
    return key % table_size
```

**Warning:** Choosing `table_size` as a power of 2 combined with poorly distributed keys (e.g., all keys even) can cause severe clustering, since `% 2^k` only looks at the lowest `k` bits. This is why many hash table implementations prefer **prime-sized tables** for modulo hashing, or mix bits before taking modulo (as CPython does internally).

### 3.6 Universal Hashing (Overview)

**Definition:** A family of hash functions `H` is *universal* if, for any two distinct keys `x ≠ y`, the probability that a randomly chosen `h` from `H` causes a collision (`h(x) == h(y)`) is at most `1/m` (where `m` = table size).

**Why it matters:** Universal hashing gives *provable* average-case guarantees **even against an adversary who knows your hash function family**, because the adversary can't predict which specific function will be chosen at runtime. This defeats hash-flooding attacks in theory — one motivation for Python's SipHash randomization in practice.

A classic universal family for integers modulo a prime `p`:
```python
import random

def make_universal_hash(m: int, p: int = 2_147_483_647):
    a = random.randint(1, p - 1)
    b = random.randint(0, p - 1)
    def h(x: int) -> int:
        return ((a * x + b) % p) % m
    return h
```

### 3.7 Avalanche Effect — Visualized

```
Input:  "hello"                     Input:  "hellp"   (1 char changed)
Hash:   0x1a2b3c4d                  Hash:   0xf9e8d7c6
        ↑ small input change   →    ↑ large, unpredictable output change (good avalanche)
```
A hash function with a strong avalanche effect ensures similar keys don't cluster together in the table.

### 3.8 Cryptographic vs Non-Cryptographic Hashing (Overview)

| Aspect | Non-Cryptographic (e.g., used in dict/set) | Cryptographic (e.g., SHA-256) |
|---|---|---|
| Goal | Speed + good distribution | Security guarantees |
| Collision resistance | Not guaranteed against adversaries | Computationally infeasible to find collisions |
| Reversibility | N/A | One-way (pre-image resistance) |
| Speed | Very fast | Slower, deliberately expensive (for password hashing) |
| Examples | SipHash, MurmurHash, FNV, CPython's tuple/str hash | MD5 (broken), SHA-1 (broken), SHA-256, SHA-3, BLAKE2 |

```python
import hashlib

data = b"hello world"
print(hashlib.sha256(data).hexdigest())   # Cryptographic digest — fixed 256-bit output
print(hashlib.md5(data).hexdigest())      # Legacy, NOT secure for cryptographic purposes anymore
```

> ⚠️ **Warning:** Never use `hash()` for cryptography or security-sensitive comparisons (e.g., password storage, integrity verification against tampering). Use `hashlib` (SHA-256/SHA-3) or dedicated password hashing libraries (`bcrypt`, `argon2`) instead. `hash()` is randomized per-process and designed for speed, not security.

### 3.9 Common Mistakes With Hash Functions

- Using a hash function that only looks at part of the key (like length) → poor distribution.
- Using `hash()` output directly across program runs/machines expecting stability (it's randomized for strings).
- Using non-cryptographic hashing for security purposes (password storage, tamper detection).
- Forgetting to take modulo table size consistently, causing negative indices in languages where modulo can be negative (not an issue in Python, since `%` always returns non-negative for positive divisor, but a classic bug in C/C++/Java ports).

### 3.10 Interview Tips

- Be ready to **design a simple hash function** for strings (polynomial rolling hash is the standard answer).
- Know how to explain **why prime table sizes** help with modulo hashing.
- Be able to explain **avalanche effect** and **uniform distribution** in your own words with an analogy.
- Know the difference between cryptographic and non-cryptographic hashing — interviewers sometimes probe this to check real understanding vs memorized `dict` usage.

### 3.11 Summary & Revision Notes

- A good hash function is deterministic, fast, uniformly distributed, and has strong avalanche behavior.
- Polynomial rolling hash is the standard technique for hashing strings/substrings in competitive programming.
- Universal hashing gives provable average-case guarantees against adversarial inputs.
- Never conflate cryptographic hashing (`hashlib`) with Python's built-in `hash()` (non-cryptographic, randomized per-process).

---

## 4. Collision Resolution

### 4.1 What Is a Collision?

**Definition:** A collision occurs when two distinct keys `k1 ≠ k2` produce the same index: `h(k1) == h(k2)`. Collisions are **mathematically unavoidable** once the number of possible keys exceeds the number of table slots (Pigeonhole Principle) — so every real hash table needs a collision resolution strategy.

```
ASCII Visualization:

  "cat" ──▶ h(cat) = 3   ┐
                          ├──▶  Index 3   ◀── COLLISION!
  "dog" ──▶ h(dog) = 3   ┘
```

### 4.2 Strategy 1 — Separate Chaining

**Definition:** Each bucket holds a **collection** (commonly a linked list, or in Python, a list) of all key-value pairs that hash to that index.

```
Index 0: []
Index 1: []
Index 2: []
Index 3: [("cat", 1) -> ("dog", 2)]     ← both live in the same bucket
Index 4: []
```

```python
class ChainingHashTable:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _index(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)   # update existing
                return
        bucket.append((key, value))         # new entry

    def get(self, key):
        idx = self._index(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(key)
```

**Line-by-line explanation:**
- `self.buckets` — a list of empty lists, one per slot.
- `_index` — computes bucket index via `hash(key) % size`.
- `put` — scans the target bucket; if key exists, updates value; otherwise appends new pair. Scanning is necessary because multiple keys can share a bucket.
- `get`/`remove` — same linear scan within the (hopefully short) bucket.

**Dry run:** Insert `"cat"→1`, `"dog"→2` where both hash to index 3 (`size=8`):

| Step | Operation | Index | Bucket 3 Before | Bucket 3 After |
|---|---|---|---|---|
| 1 | put("cat", 1) | 3 | `[]` | `[("cat", 1)]` |
| 2 | put("dog", 2) | 3 | `[("cat", 1)]` | `[("cat", 1), ("dog", 2)]` |
| 3 | get("dog") | 3 | scan bucket → match "dog" → returns 2 | — |

**Time Complexity:** O(1) average (short buckets), O(n) worst case (all keys collide into one bucket — e.g., malicious input or terrible hash function).
**Space Complexity:** O(n) for n entries + O(m) for m buckets.

**When to use:** Simple to implement, handles high load factors gracefully, deletion is straightforward.
**When NOT to use:** Memory-constrained environments (each chain node has pointer overhead), or when guaranteed cache-friendly contiguous memory access matters (open addressing wins there).

### 4.3 Strategy 2 — Open Addressing (General Idea)

**Definition:** All entries live directly inside the table array itself (no external chains). On collision, we **probe** for the next available slot using a defined sequence.

```
ASCII Visualization (table size 8):

Index:   0    1    2    3    4    5    6    7
Value:  [ ]  [ ]  [ ] [cat] [ ]  [ ]  [ ]  [ ]
                       ↑ h("cat") = 3

Insert "dog" also hashing to 3 → probe to next slot:
Index:   0    1    2    3    4    5    6    7
Value:  [ ]  [ ]  [ ] [cat] [dog] [ ]  [ ]  [ ]
                       ↑ 3    ↑ 4 (probed, was empty)
```

#### 4.3.1 Linear Probing

**Rule:** If slot `i` is occupied, try `i+1`, `i+2`, `i+3`, ... (mod table size) until an empty slot is found.

```python
class LinearProbingHashTable:
    def __init__(self, size=8):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _probe(self, key):
        idx = hash(key) % self.size
        start = idx
        while self.keys[idx] is not None and self.keys[idx] != key:
            idx = (idx + 1) % self.size
            if idx == start:
                raise Exception("Hash table is full")
        return idx

    def put(self, key, value):
        idx = self._probe(key)
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        idx = hash(key) % self.size
        start = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.size
            if idx == start:
                break
        raise KeyError(key)
```

**Dry run:** size=8, insert `"cat"` (h=3), `"dog"` (h=3), `"bat"` (h=4):

| Step | Key | h(key) | Probe sequence | Final index |
|---|---|---|---|---|
| 1 | cat | 3 | 3 (empty) | 3 |
| 2 | dog | 3 | 3 (taken) → 4 (empty) | 4 |
| 3 | bat | 4 | 4 (taken) → 5 (empty) | 5 |

Notice how `"bat"`, which never actually collided with `"cat"` at hash time, still got pushed to slot 5 because of `"dog"` occupying slot 4. This chain reaction is called **primary clustering**.

**Complexity:** O(1) average at low load factor; degrades sharply as load factor → 1 due to clustering.

**Common mistake:** Forgetting to handle deletion properly — naively setting a slot to `None` on delete can break the probe chain for later lookups (see 4.7, "tombstones").

#### 4.3.2 Quadratic Probing

**Rule:** Probe sequence uses a quadratic function of the attempt number: `index = (h(key) + c1*i + c2*i²) % size`.

```python
def quadratic_probe(key, size, attempt):
    return (hash(key) + attempt**2) % size
```

**Why:** Reduces **primary clustering** (long runs of occupied slots) compared to linear probing, since jumps grow quadratically instead of by 1 each time.

**Trade-off:** Introduces **secondary clustering** (keys with the same initial hash follow the exact same probe sequence) and can fail to find an empty slot even if one exists, unless table size and constants are chosen carefully (commonly table size = prime, and only checking `size/2` slots by design).

#### 4.3.3 Double Hashing

**Rule:** Use a second hash function to determine the step size: `index = (h1(key) + i * h2(key)) % size`.

```python
def double_hash_probe(key, size, attempt):
    h1 = hash(key) % size
    h2 = 1 + (hash(key) // size) % (size - 1)   # ensure h2 is never 0
    return (h1 + attempt * h2) % size
```

**Why it's better:** Different keys with the same `h1` will usually have different `h2`, so their probe sequences diverge quickly — this **eliminates secondary clustering** and gives the most uniform probe behavior of the open-addressing family.

### 4.4 ASCII Comparison — Probing Sequences Side by Side

```
Linear Probing:      i, i+1, i+2, i+3, i+4, ...
Quadratic Probing:   i, i+1, i+4, i+9, i+16, ...
Double Hashing:      i, i+h2, i+2h2, i+3h2, ...   (h2 varies per key)
```

### 4.5 Chaining vs Open Addressing — Full Comparison

| Aspect | Separate Chaining | Open Addressing |
|---|---|---|
| Extra memory per entry | Pointer/list overhead | None (in-place) |
| Cache performance | Poorer (pointer chasing) | Better (contiguous array) |
| Deletion | Simple (remove from list) | Tricky (needs tombstones) |
| Load factor > 1 | Possible (buckets just grow) | Impossible (table has fixed capacity) |
| Worst-case behavior | All keys in 1 bucket → O(n) | Long probe chains → O(n) |
| Used by | Java `HashMap` (chaining + trees for long chains) | CPython `dict`/`set`, C++ open-addressed variants |

### 4.6 Load Factor & Rehashing

**Definition:** `load_factor = n / m` where `n` = number of entries, `m` = number of buckets/slots.

```
ASCII Visualization:

Low load factor (0.25):      High load factor (0.9):
[cat][ ][ ][ ]                [cat][dog][bat][rat]
[  1 occupied / 4 ]            [ nearly full — collisions likely ]
```

**Rule of thumb:** Most implementations trigger **rehashing** (resize + redistribute all entries) when load factor crosses a threshold (commonly 0.7 for open addressing, Python dict resizes around 2/3 full).

```python
class ResizingHashTable:
    def __init__(self, size=8):
        self.size = size
        self.count = 0
        self.buckets = [[] for _ in range(size)]

    def _index(self, key, size):
        return hash(key) % size

    def put(self, key, value):
        idx = self._index(key, self.size)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))
        self.count += 1
        if self.count / self.size > 0.7:
            self._resize()

    def _resize(self):
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        for bucket in old_buckets:
            for key, value in bucket:
                idx = self._index(key, self.size)
                self.buckets[idx].append((key, value))
```

**Why rehashing is O(n) amortized:** Each individual resize is O(n) (must revisit every entry), but because table size **doubles** each time, the total cost of all resizes across n insertions sums to O(n) — this is the same amortized analysis used for Python list `append()`.

### 4.7 Deletion in Open Addressing — Tombstones

**Problem:** If you delete a key by setting its slot to `None`, later lookups that need to probe *through* that slot will incorrectly think the probe chain ended, causing false "not found" results for keys that were pushed past the deleted slot.

**Solution — Tombstones:** Mark deleted slots with a special sentinel (`DELETED`) that lookups treat as "occupied, keep probing" but insertions treat as "available, can reuse."

```
Before delete:        [cat][dog][bat][ ]
Delete "dog":         [cat][DEL][bat][ ]     ← get("bat") still finds it by probing THROUGH the tombstone
Naive delete (WRONG): [cat][ ]  [bat][ ]     ← get("bat") stops early at the None, returns wrong "not found"
```

### 4.8 Clustering — Visual Summary

```
Primary Clustering (Linear Probing):
[A][A][A][A][ ][ ][ ][ ]   ← long unbroken run grows and grows, "sticky"

Secondary Clustering (Quadratic Probing):
Keys with same h1 always follow the identical probe path — still clumpy, just less so than linear

Well-distributed (Double Hashing):
[A][ ][B][ ][A][B][ ][A]   ← probe paths diverge quickly, minimal clumping
```

### 4.9 Edge Cases

- Table completely full under open addressing → insertion impossible without resize (must check before probing forever / infinite loop).
- All keys hashing to the same bucket under chaining → degrades to O(n) per operation (worst case).
- Deleting during iteration → can skip entries or cause `RuntimeError: dictionary changed size during iteration` in Python — iterate over a copy (`list(d.items())`) if mutating.
- Using a mutable object as a key that gets mutated after insertion → silently breaks lookups.

### 4.10 Interview Tips

- Always mention **average vs worst case** complexity when discussing hash tables.
- Know **why Python dicts use open addressing**, not chaining (memory efficiency + cache locality).
- Be ready to explain **tombstones** if asked how deletion works in open addressing.
- If asked to "implement a hash map from scratch," separate chaining is usually the simplest correct answer to code under interview time pressure.

### 4.11 Summary & Revision Notes

- Collisions are unavoidable — the question is only *how* you resolve them.
- Chaining: buckets hold lists; simple; more memory overhead; graceful degradation.
- Open addressing: entries stored in-place; linear/quadratic/double probing trade off clustering vs implementation complexity.
- Double hashing gives the best probe distribution; linear probing is simplest but clusters most.
- Load factor governs when to rehash; amortized cost of rehashing is O(1) per insertion over time.
- Tombstones are required for correct deletion under open addressing.

---

## 5. Hashing Patterns (Problem-Solving Templates)

> This is the **most important section for interviews**. Master these patterns and you can solve the vast majority of "hashing-tagged" problems by pattern-matching, not by reinventing logic each time.

### 5.1 Pattern Map — Quick Overview

| Pattern | Core Idea | Typical Signal Words |
|---|---|---|
| Frequency Counting | Count occurrences of each element | "count", "frequency", "most/least common" |
| Presence Lookup | O(1) membership check | "contains", "exists", "seen before" |
| Duplicate Detection | Track seen elements | "duplicate", "distinct", "unique" |
| Two Sum / Pair Sum | Complement lookup | "pair that sums to", "two numbers" |
| Prefix Sum + Hash Map | Cumulative sum lookup | "subarray sum equals k" |
| Prefix XOR + Hash Map | Cumulative XOR lookup | "subarray XOR equals k" |
| Grouping / Anagrams | Canonical key → bucket | "group by", "anagrams" |
| Sliding Window + Hash Map | Window state tracking | "longest substring without...", "at most k distinct" |
| Rolling Hash | Fast substring comparison | "repeated substring", "string matching" |

### 5.2 Pattern: Frequency Counting

**Problem Statement:** Given a collection, count how many times each element appears.

**Approach:** Iterate once, use a hash map `element → count`.

```python
def frequency_count(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq
```

**Line-by-line:** `freq.get(x, 0)` returns existing count or `0` if unseen, then increments — avoids `KeyError`.

**Dry run:** `arr = [1, 2, 2, 3, 1, 1]`

| Step | x | freq before | freq after |
|---|---|---|---|
| 1 | 1 | `{}` | `{1: 1}` |
| 2 | 2 | `{1: 1}` | `{1: 1, 2: 1}` |
| 3 | 2 | `{1: 1, 2: 1}` | `{1: 1, 2: 2}` |
| 4 | 3 | `{1: 1, 2: 2}` | `{1: 1, 2: 2, 3: 1}` |
| 5 | 1 | ... | `{1: 2, 2: 2, 3: 1}` |
| 6 | 1 | ... | `{1: 3, 2: 2, 3: 1}` |

**Complexity:** O(n) time, O(k) space (k = distinct elements).

**Pythonic alternative:** `from collections import Counter; Counter(arr)` — same idea, cleaner, optimized in C.

**Common mistakes:** Using `freq[x] += 1` without initializing → `KeyError`; forgetting `Counter` exists and hand-rolling unnecessarily in production code.

### 5.3 Pattern: Presence Lookup / Duplicate Detection

**Problem Statement (LeetCode 217 - Contains Duplicate):** Given an array, determine if any value appears at least twice.

**Brute Force:** Compare every pair → O(n²).
**Better:** Sort, then check adjacent elements → O(n log n).
**Optimal:** Hash set membership → O(n).

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:          # O(1) average membership check
            return True
        seen.add(num)
    return False
```

**Dry run:** `nums = [1, 2, 3, 1]`

| Step | num | in seen? | seen after |
|---|---|---|---|
| 1 | 1 | No | `{1}` |
| 2 | 2 | No | `{1, 2}` |
| 3 | 3 | No | `{1, 2, 3}` |
| 4 | 1 | **Yes** → return `True` | — |

**Complexity:** O(n) time, O(n) space.
**Edge cases:** Empty array → `False`; single element → `False`.
**When NOT to use:** If memory is severely constrained and array is already sorted, the O(n log n)/O(1)-extra-space sort approach may be preferable.

### 5.4 Pattern: Two Sum (The Classic)

**Problem Statement (LeetCode 1):** Given an array `nums` and target `target`, return indices of two numbers that add up to `target`.

**Brute Force:** Check every pair → O(n²) time, O(1) space.
**Optimal:** For each number, look up its **complement** (`target - num`) in a hash map built as you go → O(n) time, O(n) space.

```python
def two_sum(nums, target):
    seen = {}   # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**Line-by-line:**
- `seen` maps a *value already visited* to its index.
- For each `num`, compute what value we'd need (`complement`) to reach `target`.
- If that complement was seen earlier, we've found our pair — return both indices immediately.
- Otherwise, record the current number so future elements can find it as *their* complement.

**Dry run:** `nums = [2, 7, 11, 15]`, `target = 9`

| Step | i | num | complement | complement in seen? | Action | seen after |
|---|---|---|---|---|---|---|
| 1 | 0 | 2 | 7 | No | add 2→0 | `{2:0}` |
| 2 | 1 | 7 | 2 | **Yes** (index 0) | return `[0, 1]` | — |

**Complexity:** O(n) time, O(n) space.
**Edge cases:** No valid pair exists → return `[]`; duplicate values (`nums=[3,3]`, `target=6`) → works correctly because we check `complement in seen` *before* inserting current number, avoiding self-pairing.
**Common mistake:** Inserting `num` into `seen` **before** checking for the complement — this can cause a number to pair with itself when `target == 2*num`.

### 5.5 Pattern: Prefix Sum + Hash Map (Subarray Sum Equals K)

**Problem Statement (LeetCode 560):** Count the number of contiguous subarrays whose sum equals `k`.

**Key Insight:** `sum(i..j) = prefixSum[j] - prefixSum[i-1]`. So `sum(i..j) == k` ⟺ `prefixSum[i-1] == prefixSum[j] - k`. Store frequency of each prefix sum seen so far.

```python
def subarray_sum_equals_k(nums, k):
    count = 0
    prefix_sum = 0
    freq = {0: 1}     # empty prefix (sum 0) occurs once, before we start
    for num in nums:
        prefix_sum += num
        count += freq.get(prefix_sum - k, 0)
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    return count
```

**Line-by-line:**
- `freq = {0: 1}` — seeds the map with prefix sum 0 occurring once (represents "no elements taken yet"), so subarrays starting at index 0 are counted correctly.
- For each number, update running `prefix_sum`.
- `freq.get(prefix_sum - k, 0)` — how many earlier prefix sums, if subtracted from the current one, would give exactly `k`? Add that count to the running total.
- Record the current prefix sum's frequency for future iterations.

**Dry run:** `nums = [1, 1, 1]`, `k = 2`

| Step | num | prefix_sum | prefix_sum-k | freq.get(...) | count | freq after |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | -1 | 0 | 0 | `{0:1, 1:1}` |
| 2 | 1 | 2 | 0 | 1 | 1 | `{0:1, 1:1, 2:1}` |
| 3 | 1 | 3 | 1 | 1 | 2 | `{0:1, 1:1, 2:1, 3:1}` |

Result: `2` — subarrays `[1,1]` (indices 0-1) and `[1,1]` (indices 1-2).

**Complexity:** O(n) time, O(n) space. (Brute force nested loops would be O(n²).)
**Edge cases:** Negative numbers are fine (unlike sliding window, which requires non-negative for monotonic sum assumptions); `k = 0` works correctly because of the seeded `{0: 1}`.

### 5.6 Pattern: Prefix XOR + Hash Map

**Problem Statement:** Count subarrays whose XOR equals `k` (structurally identical to prefix sum, but using XOR's self-inverse property: `a ^ a = 0`).

```python
def subarray_xor_equals_k(nums, k):
    count = 0
    prefix_xor = 0
    freq = {0: 1}
    for num in nums:
        prefix_xor ^= num
        count += freq.get(prefix_xor ^ k, 0)
        freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
    return count
```

**Why it works:** `xor(i..j) = prefixXor[j] ^ prefixXor[i-1]`. So `xor(i..j) == k` ⟺ `prefixXor[i-1] == prefixXor[j] ^ k` (since XOR is its own inverse: if `a ^ b = k` then `a = b ^ k`).

**Complexity:** O(n) time, O(n) space. Structurally the *same pattern* as 5.5 — recognize this transferability in interviews.

### 5.7 Pattern: Grouping — Group Anagrams

**Problem Statement (LeetCode 49):** Group strings that are anagrams of each other.

**Key Insight:** Two strings are anagrams iff their **sorted character sequences are identical**. Use the sorted string (or character-count tuple) as a canonical hash-map key.

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))     # canonical form
        groups[key].append(s)
    return list(groups.values())
```

**Line-by-line:**
- `defaultdict(list)` — auto-creates an empty list for any new key, avoiding manual existence checks.
- `sorted(s)` — canonicalizes each string; anagrams always produce the identical sorted sequence.
- Append original string under its canonical key.

**Dry run:** `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

| Step | s | sorted(s) | groups after |
|---|---|---|---|
| 1 | eat | aet | `{aet: [eat]}` |
| 2 | tea | aet | `{aet: [eat, tea]}` |
| 3 | tan | ant | `{aet: [...], ant: [tan]}` |
| 4 | ate | aet | `{aet: [eat, tea, ate], ant: [tan]}` |
| 5 | nat | ant | `{aet: [...], ant: [tan, nat]}` |
| 6 | bat | abt | `{..., abt: [bat]}` |

**Complexity:** O(n · k log k) time (n strings, average length k, sorting each), O(n·k) space. **Optimization:** Use a fixed-size character-count tuple (26 letters) as the key instead of sorting → O(n·k) time, avoiding the `log k` sort factor.

```python
def group_anagrams_optimized(strs):
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)   # tuple is hashable, list is not
    return list(groups.values())
```

**Common mistake:** Using a `list` directly as a dict key (unhashable) — must convert to `tuple` or `str` first.

### 5.8 Pattern: Sliding Window + Hash Map

**Problem Statement (LeetCode 3 - Longest Substring Without Repeating Characters):** Find the length of the longest substring without repeating characters.

**Brute Force:** Check every substring → O(n³) (generate + validate).
**Better:** Sliding window with a `set` → O(n) but may re-scan on collision.
**Optimal:** Sliding window with a `dict` storing **last seen index** of each character → O(n), jumps the window directly instead of shrinking one step at a time.

```python
def longest_substring_without_repeat(s):
    last_seen = {}       # char -> most recent index
    window_start = 0
    best = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= window_start:
            window_start = last_seen[ch] + 1   # jump window start past the repeat
        last_seen[ch] = i
        best = max(best, i - window_start + 1)
    return best
```

**Line-by-line:**
- `last_seen[ch] >= window_start` — checks if the repeat occurred **inside the current window** (a stale, out-of-window repeat should be ignored).
- If it's a live repeat, jump `window_start` right past the previous occurrence — this is the O(1)-jump optimization over the naive "shrink one at a time" approach.
- Always update `last_seen[ch] = i` and track the best window length so far.

**Dry run:** `s = "abcabcbb"`

| i | ch | last_seen[ch] before | window_start before | repeat in window? | window_start after | best |
|---|---|---|---|---|---|---|
| 0 | a | — | 0 | No | 0 | 1 |
| 1 | b | — | 0 | No | 0 | 2 |
| 2 | c | — | 0 | No | 0 | 3 |
| 3 | a | 0 | 0 | Yes (0>=0) | 1 | 3 |
| 4 | b | 1 | 1 | Yes (1>=1) | 2 | 3 |
| 5 | c | 2 | 2 | Yes (2>=2) | 3 | 3 |
| 6 | b | 4 | 3 | No (4<3 is false... wait 4>=3 True) | 5 | 2 |
| 7 | b | 6 | 5 | Yes (6>=5) | 7 | 1 |

Result: `3` (substring `"abc"`).

**Complexity:** O(n) time — every index visited once; O(min(n, alphabet size)) space.
**Edge cases:** Empty string → `0`; all unique characters → `len(s)`; all identical characters → `1`.

### 5.9 Pattern: Sliding Window — At Most K Distinct Characters

**Problem Statement (LeetCode 340-style):** Find the longest substring with at most `k` distinct characters.

```python
from collections import defaultdict

def longest_substring_k_distinct(s, k):
    freq = defaultdict(int)
    window_start = 0
    best = 0
    for window_end, ch in enumerate(s):
        freq[ch] += 1
        while len(freq) > k:
            left_ch = s[window_start]
            freq[left_ch] -= 1
            if freq[left_ch] == 0:
                del freq[left_ch]
            window_start += 1
        best = max(best, window_end - window_start + 1)
    return best
```

**Why a hash map (not just a set):** We need **counts**, not just presence, so we know exactly when a character's count drops to zero and can be fully removed from consideration — a `set` alone can't track "how many left in the window."

**Complexity:** O(n) time — amortized, since `window_start` only moves forward; O(k) space.

### 5.10 Pattern: Hash Set for Cycle/Path Detection

**Problem Statement (e.g., LeetCode 202 - Happy Number):** Detect if a sequence of transformations eventually cycles.

```python
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
```

**Key Insight:** Any process that deterministically maps a finite state space to itself will either terminate or **cycle**. A hash set tracks visited states in O(1) to detect the cycle instantly, instead of relying on cycle-detection algorithms like Floyd's (though that's a valid O(1)-space alternative).

### 5.11 Pattern: Coordinate Compression (Overview)

**Definition:** When values are large/sparse but only their **relative order** matters, map them to a small dense range `[0, k)` using a hash map built from sorted unique values.

```python
def coordinate_compress(values):
    sorted_unique = sorted(set(values))
    rank = {v: i for i, v in enumerate(sorted_unique)}
    return [rank[v] for v in values]
```

**Use case:** Reduces the value range for algorithms that need array-indexable structures (like Fenwick trees / segment trees) when raw values are too large or sparse to index directly. Hashing (via the `rank` dict) is what makes the compression lookup O(1) per element.

### 5.12 Pattern: Hash Map for Isomorphism / Bijection Checks

**Problem Statement (LeetCode 205 - Isomorphic Strings):** Check whether characters in string `s` map consistently 1-to-1 to characters in string `t`.

```python
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    map_st, map_ts = {}, {}
    for a, b in zip(s, t):
        if a in map_st and map_st[a] != b:
            return False
        if b in map_ts and map_ts[b] != a:
            return False
        map_st[a] = b
        map_ts[b] = a
    return True
```

**Why two maps:** We must enforce a **bijection** (one-to-one both ways), not just a one-directional mapping — a single map would allow two different source characters to map to the same target character, which violates isomorphism.

### 5.13 Pattern: Rolling Hash for Substring Matching (Rabin–Karp, String Perspective)

**Problem Statement:** Find all occurrences of pattern `p` in text `t`.

```python
def rabin_karp(text, pattern, base=31, mod=10**9 + 7):
    n, m = len(text), len(pattern)
    if m > n:
        return []
    pattern_hash = 0
    for ch in pattern:
        pattern_hash = (pattern_hash * base + ord(ch)) % mod
    base_m_minus_1 = pow(base, m - 1, mod)
    window_hash = 0
    for i in range(m):
        window_hash = (window_hash * base + ord(text[i])) % mod
    matches = []
    for i in range(n - m + 1):
        if window_hash == pattern_hash and text[i:i+m] == pattern:  # verify to rule out false positives
            matches.append(i)
        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * base_m_minus_1) % mod
            window_hash = (window_hash * base + ord(text[i + m])) % mod
    return matches
```

**Why the verification step (`text[i:i+m] == pattern`):** Hash collisions are possible (two different substrings sharing the same hash mod a finite number). Always verify with an actual string comparison before confirming a match — otherwise you risk **false positives**.

**Complexity:** O(n + m) average time (verification adds O(m) only on hash matches, which are rare with a good hash), O(1) extra space (excluding pattern/text storage). Worst case (adversarial/many collisions) O(n·m).

### 5.14 Master Cheat Table — Which Structure for Which Pattern

| Need | Use |
|---|---|
| Just "have I seen this?" | `set` |
| "How many times have I seen this?" | `dict` / `Counter` |
| "Map original → transformed/grouped value" | `dict` / `defaultdict` |
| "Fast prefix-sum / prefix-xor lookup" | `dict` (value → frequency of prefix) |
| "Track last position for sliding window" | `dict` (value → last index) |
| "Canonical grouping key" | sorted string / tuple as dict key |

### 5.15 Summary & Revision Notes

- Nearly every hashing pattern reduces to: *"turn an O(n²) nested-loop search into an O(n) single pass by remembering what you've already seen."*
- Two Sum, Subarray Sum = K, and Longest Substring Without Repeats are the three archetypal problems — nearly every other hashing problem is a variation on one of these three templates.
- Always ask: do I need presence (`set`), count (`dict`/`Counter`), or last-position (`dict`)?

---

## 6. Real-World Applications

### 6.1 Dictionaries / Symbol Tables

Every programming language's variable/function lookup (compilers, interpreters) uses a hash-map-backed **symbol table** mapping identifier names to memory locations, types, or scopes. Python's own `globals()`/`locals()` are dicts.

### 6.2 Caching

**LRU Cache** combines a hash map (O(1) key → node lookup) with a doubly linked list (O(1) reordering by recency).

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)   # mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)   # evict least recently used
```

**Role of hashing:** `OrderedDict` is fundamentally a hash map with an attached doubly linked list for order tracking; the hash map is what gives O(1) `get`/`put` — without it, LRU cache lookups would be O(n).

### 6.3 Databases — Hash Indexing

Databases use hash indexes for **equality lookups** (`WHERE id = ?`) to achieve O(1) row access, as an alternative to B-Tree indexes (which support range queries but are O(log n)). Hash partitioning also distributes rows across shards by hashing a partition key.

```
ASCII: Hash Index vs B-Tree Index

Hash Index:                       B-Tree Index:
key → h(key) → bucket → row       key → traverse tree → row
Great for: WHERE id = 5           Great for: WHERE id BETWEEN 5 AND 50
Bad for: range queries            Slightly slower for pure equality
```

### 6.4 Compiler Design

Symbol tables (6.1), string interning (mapping identical string literals to one shared object via a hash-based intern pool), and hash-consing in some functional-language compilers all rely on hashing for O(1) lookups during parsing/semantic analysis.

### 6.5 Networking

- **Routing tables** hash IP prefixes to next-hop interfaces.
- **Load balancers** use **consistent hashing** to map requests to servers so that adding/removing a server reshuffles only a small fraction of mappings (critical for distributed caches like Memcached/Redis clusters, and CDNs).
- **Hash-based load distribution** ensures a specific client's requests to consistently land on the same backend (session stickiness) without a centralized lookup table.

```
Consistent Hashing (ASCII, ring topology):

         Server A
            |
   ┌────────┼────────┐
   │      (ring)      │
Server D          Server B
   │                  │
   └────────┬─────────┘
         Server C

Key "user123" hashes to a ring position → walk clockwise → lands on nearest server.
Removing Server B only reassigns keys between A and B — not the entire ring.
```

### 6.6 Spell Checkers & Dictionaries of Words

A hash set of valid dictionary words gives O(1) "is this a real word?" checks; more advanced spell checkers combine this with **edit distance** or **BK-trees**, but the base membership test is hash-driven.

### 6.7 Duplicate Detection & Data Deduplication

Deduplication systems (backup software, Git object storage) hash file contents (often with SHA-1/SHA-256) and store only one copy per unique hash — if two files hash identically, they're treated as duplicates (with tunable collision risk).

### 6.8 Frequency Analysis

Word-frequency counters, log analysis (`Counter` on error codes), and analytics pipelines rely directly on the [Frequency Counting pattern](#52-pattern-frequency-counting).

### 6.9 Memoization (Hash Map Usage)

```python
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```
A hash map (`memo`) stores previously computed results keyed by input, converting exponential recursive calls into linear ones — the hashing role here is purely "O(1) has-this-been-computed" lookup, not the DP algorithm itself (DP as a topic is out of scope for this handbook, per the SCOPE section).

### 6.10 Blockchain & Cryptographic Integrity

Blocks store the **cryptographic hash** of the previous block, chaining integrity — altering any historical block changes its hash, breaking every subsequent link. This is an application of cryptographic hashing (hashlib/SHA-256-style), distinct from the non-cryptographic hashing used in `dict`/`set` (see 3.8).

### 6.11 Password Storage (Overview)

Never store plaintext passwords. Store a **salted, slow cryptographic hash** (bcrypt/argon2/scrypt) so that even if the database leaks, recovering passwords requires expensive brute force per password (salting also defeats precomputed rainbow-table attacks).

### 6.12 Bloom Filters (Overview)

**Definition:** A probabilistic, space-efficient structure using **multiple hash functions** to answer "definitely not present" or "possibly present" — trading a small false-positive rate for huge space savings versus a real hash set.

```
Bloom Filter (m=10 bits, k=2 hash functions):

Insert "cat": h1("cat")=2, h2("cat")=5 → set bits 2 and 5
Insert "dog": h1("dog")=5, h2("dog")=8 → set bits 5 and 8

Bit array: 0 0 1 0 0 1 0 0 1 0
                ↑2      ↑5   ↑8

Query "bat": h1("bat")=2, h2("bat")=8 → both bits set → "possibly present" (FALSE POSITIVE — bat was never inserted!)
Query "rat": h1("rat")=0, h2("rat")=3 → bit 0 not set → "definitely NOT present" (always correct)
```
Used in: web crawlers (avoid re-crawling URLs), CDNs, databases (e.g., Cassandra uses Bloom filters to skip SSTables that definitely don't contain a key).

### 6.13 Summary & Revision Notes

- Hashing powers: symbol tables, LRU caches, hash indexes, consistent hashing/load balancing, deduplication, memoization, Bloom filters, and (via cryptographic hashing) blockchains and password storage.
- Distinguish clearly: **non-cryptographic hashing** (speed, `dict`/`set`) vs **cryptographic hashing** (security, `hashlib`, passwords, blockchains).
- Bloom filters trade certainty for massive space savings — know the false-positive-only guarantee (never false negatives).

---

## 7. Problem Recognition — "Is This a Hashing Problem?"

### 7.1 Recognition Flowchart (ASCII Decision Tree)

```
                        ┌───────────────────────────────┐
                        │ Does the problem require fast │
                        │ "have I seen this?" checks?   │
                        └───────────────┬───────────────┘
                                        │
                     ┌──────────Yes────┴────No───────────┐
                     ▼                                     ▼
      ┌─────────────────────────────┐         ┌─────────────────────────────┐
      │ Do you need COUNTS,          │         │ Is it about ORDER / RANGE   │
      │ or just PRESENCE?            │         │ queries (sorted, next-      │
      └───────────┬─────────────────┘         │ greater, range sum)?        │
                  │                            └───────────┬─────────────────┘
        ┌─Presence┴─Counts──┐                              │
        ▼                    ▼                     ┌───Yes─┴───No──────┐
     use `set`          use `dict`/Counter          ▼                    ▼
                                              Consider BST /        Probably NOT
                                              sorted structures      a hashing problem
                                              (out of scope here)    — reconsider
```

### 7.2 Interview Clues — Keyword Triggers

| Clue phrase in problem statement | Likely pattern |
|---|---|
| "return **true** if any value appears twice" | Duplicate detection (`set`) |
| "find two numbers that add up to..." | Two Sum (`dict`: value→index) |
| "count subarrays whose sum equals k" | Prefix Sum + `dict` |
| "group anagrams / group by some property" | Grouping (canonical key → `defaultdict(list)`) |
| "longest substring without repeating..." | Sliding Window + `dict` |
| "first non-repeating character" | Frequency count (`Counter`) then re-scan |
| "check if two strings are anagrams" | `Counter(s1) == Counter(s2)` |
| "design a cache with O(1) get/put" | `dict` + `OrderedDict`/linked list (LRU) |
| "have I visited this state before" (cycles) | `set` of visited states |
| "intersection / union of two collections" | `set` operations |

### 7.3 Signals That It's NOT (Purely) a Hashing Problem

- Problem needs **sorted order** or **range queries** ("find the smallest element greater than X") → BST / sorted structures, not hashing alone.
- Problem needs the **k-th smallest/largest repeatedly** → heaps.
- Problem is fundamentally about **graph traversal/paths** → hashing might help (visited sets, adjacency maps) but graph algorithms are the primary tool, not the topic itself.
- Problem is a pure **DP optimization** — hashing may assist (memoization keys) but isn't the core technique.

> 📝 **Note:** Many real interview problems *combine* hashing with something else (e.g., "hashing + sliding window", "hashing + two pointers", "hashing + graph"). Recognizing hashing as *one ingredient* rather than the entire solution is itself a skill.

### 7.4 Quick Self-Test Questions

Ask yourself, in order:
1. "If I had infinite memory and O(1) lookup, would this problem become trivial?" → If **yes**, it's a hashing problem.
2. "Do I care about the *order* of elements, or just *which* elements/values exist and how often?" → Order matters heavily → maybe not hashing; existence/frequency → hashing.
3. "Am I repeatedly asking 'have I seen X before' inside a loop?" → Classic hashing signal.

### 7.5 Summary

- Presence → `set`. Frequency → `dict`/`Counter`. Complement/pair lookup → `dict`. Canonical grouping → `defaultdict`.
- If the problem needs order/range, hashing alone won't fully solve it.
- Hashing is often one tool combined with sliding window, two pointers, or prefix sums — learn to spot it as an ingredient, not just a whole-problem label.

---

## 8. Optimization Journey: Brute Force → Better → Optimal

### 8.1 General Template

For nearly every hashing-solvable problem, the optimization path looks like:

```
Brute Force:  Nested loops, O(n²) or worse — compare every pair/subarray directly
     │
     ▼
Better:       Sort first, then use two pointers or binary search — O(n log n)
     │
     ▼
Optimal:      Single pass with a hash map/set remembering state — O(n)
```

### 8.2 Case Study: Two Sum

| Approach | Time | Space | Idea |
|---|---|---|---|
| Brute Force | O(n²) | O(1) | Check every pair |
| Better | O(n log n) | O(1) (if in-place sort) | Sort + two pointers (loses original indices unless tracked separately) |
| **Optimal** | **O(n)** | **O(n)** | Hash map storing value→index, single pass |

### 8.3 Case Study: Contains Duplicate

| Approach | Time | Space |
|---|---|---|
| Brute Force (all pairs) | O(n²) | O(1) |
| Better (sort, check adjacent) | O(n log n) | O(1) extra (in-place sort) |
| **Optimal (hash set)** | **O(n)** | **O(n)** |

### 8.4 Case Study: Subarray Sum Equals K

| Approach | Time | Space |
|---|---|---|
| Brute Force (all subarrays, direct sum) | O(n²) or O(n³) naive | O(1) |
| Better (precompute prefix sums, still nested check) | O(n²) | O(n) |
| **Optimal (prefix sum + hash map)** | **O(n)** | **O(n)** |

### 8.5 Case Study: Longest Substring Without Repeating Characters

| Approach | Time | Space |
|---|---|---|
| Brute Force (check every substring) | O(n³) | O(min(n, alphabet)) |
| Better (sliding window with `set`, shrink one at a time) | O(n) amortized but 2n worst-case pointer moves | O(min(n, alphabet)) |
| **Optimal (sliding window with `dict` of last index, direct jump)** | **O(n)**, fewer pointer moves | O(min(n, alphabet)) |

### 8.6 The General Trade-off: Time vs Space

Hashing's central trade-off: **spend O(n) extra memory to convert O(n²) time into O(n) time.** Always state this trade-off explicitly in interviews — it shows you understand *why* hashing helps, not just *that* it helps.

### 8.7 When NOT to Optimize With Hashing

- Input is tiny (n < ~20) — brute force is simpler, and constant factors dominate.
- Memory is severely constrained (embedded systems) — an O(n log n) sort-based approach with O(1) extra space may be preferable to an O(n) hash-based approach using O(n) extra space.
- You need sorted/ordered results anyway — sorting-based approaches may end up doing "double duty."

### 8.8 Summary

- The brute force → better → optimal pipeline for hashing problems almost always ends at: single pass + hash map/set = O(n) time, O(n) space.
- Always explicitly state the time-space trade-off in interviews.
- Know when hashing is *not* the best trade-off (tiny inputs, extreme memory constraints, or a genuine need for order).

---

## 9. Interview Preparation

### 9.1 Difficulty-Tiered Problem List

**Easy**
- Two Sum (LeetCode 1)
- Contains Duplicate (LeetCode 217)
- Valid Anagram (LeetCode 242)
- Ransom Note (LeetCode 383)
- Single Number (LeetCode 136) — XOR trick, hashing alternative
- Majority Element (LeetCode 169) — hashing or Boyer-Moore
- First Unique Character in a String (LeetCode 387)
- Jewels and Stones (LeetCode 771)
- Two Sum II variants
- Isomorphic Strings (LeetCode 205)

**Medium**
- Group Anagrams (LeetCode 49)
- Subarray Sum Equals K (LeetCode 560)
- Longest Substring Without Repeating Characters (LeetCode 3)
- Top K Frequent Elements (LeetCode 347)
- Longest Consecutive Sequence (LeetCode 128)
- 4Sum II (LeetCode 454)
- Copy List with Random Pointer (LeetCode 138) — hash map for node cloning
- Design a HashSet/HashMap from scratch (LeetCode 705/706)
- Insert Delete GetRandom O(1) (LeetCode 380)
- Continuous Subarray Sum (LeetCode 523) — prefix sum + modulo + hash map
- Subarray Sums Divisible by K (LeetCode 974)
- LRU Cache (LeetCode 146)

**Hard**
- Longest Substring with At Most K Distinct Characters (LeetCode 340 - premium)
- Minimum Window Substring (LeetCode 76)
- LFU Cache (LeetCode 460)
- Substring with Concatenation of All Words (LeetCode 30)
- Count of Range Sum (LeetCode 327) — merge sort or hashing-adjacent variants
- Design Twitter (LeetCode 355) — hash map heavy system design

### 9.2 Pattern-Wise Grouping

| Pattern | Representative Problems |
|---|---|
| Frequency Counting | Valid Anagram, Top K Frequent Elements, First Unique Character |
| Two Sum family | Two Sum, 4Sum II, Two Sum II |
| Prefix Sum/XOR | Subarray Sum Equals K, Subarray Sums Divisible by K, Continuous Subarray Sum |
| Grouping | Group Anagrams |
| Sliding Window + Hash Map | Longest Substring Without Repeating Chars, Minimum Window Substring |
| Design Problems | LRU Cache, LFU Cache, Insert Delete GetRandom O(1), Design Twitter |
| Sequence/Set tricks | Longest Consecutive Sequence, Happy Number |

### 9.3 Company-Wise Common Themes (General Patterns, Not Leaked Questions)

| Company | Commonly Emphasized Hashing Themes |
|---|---|
| Google | Design problems (LRU/LFU), clean abstraction, complexity analysis rigor |
| Meta | Fast-paced array/string hashing problems (Two Sum family, Group Anagrams) |
| Amazon | Practical system-flavored problems (caching, deduplication) tied to Leadership Principles discussion |
| Microsoft | Balanced mix of correctness + edge cases (nulls, empty inputs, duplicates) |
| Apple | Clean code + memory-conscious discussion (chaining vs open addressing trade-offs) |

> 📝 **Note:** Company-specific "exact" questions change constantly and shouldn't be memorized verbatim — focus on the *pattern*, since interviewers frequently create novel variations of the same underlying template.

### 9.4 Blind 75 / NeetCode Hashing-Tagged Problems

- Two Sum
- Contains Duplicate
- Group Anagrams
- Top K Frequent Elements
- Valid Anagram
- Longest Consecutive Sequence
- Encode and Decode Strings (NeetCode extra)
- Product of Array Except Self (array-focused, sometimes paired with hashing discussions)
- Longest Substring Without Repeating Characters

### 9.5 Frequently Asked Interview Questions (Conceptual)

1. "What is the time complexity of dict/set operations, and why can it degrade?"
2. "How does Python's dict handle collisions internally?"
3. "What is the difference between a `set` and a `frozenset`?"
4. "Why must mutable objects not be used as dictionary keys?"
5. "Explain the difference between `__eq__` and `__hash__`, and why they must be consistent."
6. "How would you design a hash map from scratch? What collision strategy would you pick and why?"
7. "What's the difference between chaining and open addressing?"
8. "What is load factor, and how does it affect performance?"
9. "How does Python prevent hash-flooding attacks?"
10. "Explain a real-world use of consistent hashing."

### 9.6 Interview Tricks

- **Always clarify constraints first:** value ranges, duplicates allowed, sorted or not, memory limits — this shapes whether hashing is even the right tool.
- **State complexity trade-offs out loud** before coding — interviewers reward this heavily.
- **Start with brute force verbally**, then optimize — shows structured thinking rather than jumping straight to a memorized solution.
- **Dry run on a small example** before declaring "done" — catches off-by-one errors live.
- **Mention edge cases proactively**: empty input, all duplicates, negative numbers, single element.
- If stuck, explicitly ask: "Can I use extra space to trade for speed?" — this often is the hint toward hashing.

### 9.7 Summary

- Master the "big three" archetypes (Two Sum, Subarray Sum = K, Longest Substring Without Repeats) — most problems are variations.
- Always narrate brute force → optimization → complexity trade-offs.
- Practice explaining Python dict/set internals conceptually — a very common conceptual follow-up.

---

## 10. Python Tips & Tool Belt

### 10.1 `dict` — The Workhorse

```python
d = {}
d.setdefault("a", []).append(1)     # create default list if missing, then mutate — avoids KeyError
value = d.get("missing", "default")  # safe access without exceptions
```

### 10.2 `set` — Membership & Set Algebra

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)   # intersection {2, 3}
print(a | b)   # union {1, 2, 3, 4}
print(a - b)   # difference {1}
print(a ^ b)   # symmetric difference {1, 4}
```

### 10.3 `collections.defaultdict`

```python
from collections import defaultdict

graph = defaultdict(list)
graph["A"].append("B")   # no KeyError even though "A" wasn't pre-initialized
```

**Why it exists:** Eliminates repetitive `if key not in d: d[key] = default_value` boilerplate. `defaultdict(int)` → default `0`; `defaultdict(list)` → default `[]`; `defaultdict(set)` → default `set()`.

> ⚠️ **Warning:** `defaultdict` creates an entry (with the default value) on **any** access, even a failed lookup like `d[key]` in a condition check — this can silently bloat your dict with unwanted empty entries. Use `key in d` or `.get()` for pure existence checks instead of triggering default creation.

### 10.4 `collections.Counter`

```python
from collections import Counter

c = Counter("mississippi")
print(c)                     # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(c.most_common(2))      # [('i', 4), ('s', 4)]
c2 = Counter("aabbcc")
print(c + c2)                 # element-wise addition of counts
print(c - c2)                 # element-wise subtraction (negative results dropped)
```

**Best for:** Frequency counting, "top-k frequent," multiset arithmetic (`+`, `-`, `&`, `|` between Counters).

### 10.5 `collections.OrderedDict`

```python
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od.move_to_end("a")     # reorder — useful for LRU cache
print(list(od.keys()))   # ['b', 'a']
```

**Note:** Since Python 3.7, plain `dict` also preserves insertion order — `OrderedDict` remains useful specifically for its extra methods like `move_to_end()` and for order-sensitive equality (`OrderedDict` compares order too; plain `dict` equality ignores order).

### 10.6 `defaultdict` vs plain `dict`

| Aspect | `dict` | `defaultdict` |
|---|---|---|
| Missing key access | `KeyError` | Auto-creates default value |
| Best for | Explicit control | Grouping/accumulation code |
| Risk | Explicit checks needed | Can silently create unwanted entries |

### 10.7 `Counter` vs plain `dict`

| Aspect | `dict` | `Counter` |
|---|---|---|
| Missing key access | `KeyError` (unless `.get()`) | Returns `0` automatically |
| Extra methods | None | `.most_common()`, multiset arithmetic |
| Best for | General mapping | Frequency-specific tasks |

### 10.8 `frozenset` Use Cases

```python
memo_cache = {}
def solve(state_set):
    key = frozenset(state_set)     # make a mutable set hashable for use as a cache key
    if key in memo_cache:
        return memo_cache[key]
    # ... compute result ...
```

### 10.9 Dictionary/Set Comprehensions

```python
squares = {x: x*x for x in range(5)}          # dict comprehension
evens = {x for x in range(20) if x % 2 == 0}   # set comprehension
```

### 10.10 Performance Tips

- Prefer `Counter(iterable)` over manual loops for frequency counting — implemented in C, faster.
- Avoid repeated `key in dict` **followed by** `dict[key]` when you can use `.get()` once — saves a redundant hash computation/lookup.
- For very hot-path code, avoid creating unnecessary intermediate lists/sets inside loops — hashing has overhead too, just less than searching.
- `dict.keys()`, `.values()`, `.items()` return **views**, not copies — iterating them is O(1) extra space, but mutating the dict while iterating a view raises `RuntimeError`.

### 10.11 Memory Tips

- Hash tables trade memory for speed — expect ~2-3x the raw data size in overhead for CPython dicts/sets due to sparse table slots.
- Use `sys.getsizeof()` to inspect actual memory footprint if memory-constrained.
- For huge datasets where you truly need to save memory, consider `array` module for fixed-type numeric data (not hashing-specific, but a common companion optimization) or specialized structures (Bloom filters, see 6.12).

### 10.12 Common Python Pitfalls

```python
# Pitfall 1: mutable default argument accidentally shared across calls
def bad(d={}):
    d["x"] = 1
    return d

# Pitfall 2: modifying dict while iterating
d = {"a": 1, "b": 2}
for k in d:
    if k == "a":
        del d[k]     # RuntimeError: dictionary changed size during iteration

# Fix: iterate over a copy
for k in list(d.keys()):
    if k == "a":
        del d[k]     # Safe

# Pitfall 3: assuming dict/set order is guaranteed pre-3.7 (it is guaranteed 3.7+, but don't rely on it in cross-version code without checking)
```

### 10.13 Summary & Revision Notes

- `defaultdict` for grouping, `Counter` for frequency, `OrderedDict` for explicit order manipulation, `frozenset` for hashable immutable sets.
- Beware default-value auto-creation side effects with `defaultdict`.
- Never mutate a dict while iterating it directly — iterate over a snapshot copy instead.

---

## 11. Common Mistakes & Pitfalls

| # | Mistake | Why It Happens | Fix |
|---|---|---|---|
| 1 | Using a mutable object (`list`) as a dict key | Forgetting hashability requires immutability | Use `tuple`/`frozenset` instead |
| 2 | Defining `__eq__` without `__hash__` | Not knowing Python auto-nulls `__hash__` in this case | Always define both together |
| 3 | Assuming `hash()` is stable across runs for strings | Not knowing about SipHash randomization | Don't persist/compare raw `hash()` values across processes |
| 4 | Assuming O(1) is guaranteed worst-case | Confusing average-case with worst-case | Always say "average case" explicitly |
| 5 | `KeyError` from `d[key]` on missing key | Forgetting to use `.get()`/`setdefault`/`defaultdict` | Use safe accessors |
| 6 | Two-Sum self-pairing bug | Inserting current number before checking complement | Check complement **before** inserting current value |
| 7 | Modifying dict/set while iterating | Not knowing this raises `RuntimeError` | Iterate over `list(d.keys())` copy |
| 8 | Using unhashable `list` as a canonical grouping key | Forgetting lists aren't hashable | Convert to `tuple` |
| 9 | Believing hash equality implies value equality | Confusing "collision possible" with "guaranteed distinct" | Verify with `==` after a hash match (esp. in rolling hash/Rabin-Karp) |
| 10 | Ignoring load factor impact | Not realizing high load factor degrades performance | Understand/monitor resizing behavior; pre-size when count is known |
| 11 | Using non-cryptographic hash for security | Not knowing `hash()`/dict hashing isn't secure | Use `hashlib` + salting for security-sensitive hashing |
| 12 | Assuming dict order pre-3.7 | Version confusion | Know that insertion-order guarantee started in 3.7 |
| 13 | Poor custom hash function ignoring most of the key | E.g., hashing only `len(key)` | Consider all relevant fields/characters in the hash |
| 14 | Off-by-one errors in prefix sum / rolling hash math | Forgetting the `{0: 1}` seed or window boundary math | Dry run on a small example before trusting the code |
| 15 | Forgetting to verify matches in Rabin–Karp | Assuming hash match = definite match | Always compare actual substrings after a hash hit |

### 11.1 Deep Dive: Mutable Keys Gone Wrong

```python
class BadKey:
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return self.val == other.val
    def __hash__(self):
        return hash(self.val)

k = BadKey(1)
d = {k: "original"}
k.val = 2          # MUTATING the key after insertion!
print(d.get(k))     # None — the dict can no longer find it under its NEW hash
print(k in d)        # False — silently "lost" the entry
```
**Lesson:** Even if an object is technically hashable, mutating fields that participate in `__hash__`/`__eq__` **after** it's used as a key corrupts the table logically (the entry still physically exists, but is unreachable under the new hash).

### 11.2 Deep Dive: Equality vs Identity

```python
a = [1, 2]
b = [1, 2]
print(a == b)   # True  (value equality)
print(a is b)   # False (different objects in memory)
# Neither is hashable anyway, but the a==b vs a is b distinction is the root of the __eq__/__hash__ contract discussion
```

### 11.3 Summary

- Most hashing bugs trace back to: (a) mutable keys, (b) broken `__eq__`/`__hash__` contracts, (c) confusing average vs worst case, or (d) trusting a hash match without verifying actual equality.
- When debugging a "missing key that should be there" bug, suspect key mutation after insertion first.

---

## 12. Cheat Sheets

### 12.1 Core Concepts Cheat Sheet

| Concept | One-Line Definition |
|---|---|
| Hash Function | Maps arbitrary key → fixed-size integer |
| Hash Table | Array-backed structure using hash-derived indices for O(1) avg access |
| Collision | Two keys mapping to same index |
| Chaining | Bucket holds a list of colliding entries |
| Open Addressing | Colliding entries stored in-place via a probe sequence |
| Load Factor | entries / buckets — controls when to resize |
| Rehashing | Growing table + redistributing entries |
| Avalanche Effect | Small input change → large output change |
| Universal Hashing | Randomized hash family with provable low collision probability |

### 12.2 Complexity Cheat Sheet

| Operation | Average Case | Worst Case |
|---|---|---|
| `dict`/`set` insert | O(1) | O(n) |
| `dict`/`set` lookup | O(1) | O(n) |
| `dict`/`set` delete | O(1) | O(n) |
| Rehash (single event) | O(n) | O(n) |
| Rehash (amortized per insert) | O(1) | O(1) |
| Polynomial hash computation | O(k) (k = key length) | O(k) |
| Rolling hash window update | O(1) | O(1) |
| Rabin–Karp search | O(n+m) average | O(n·m) worst (many collisions) |

### 12.3 Hash Table Operations Cheat Sheet

```python
d = {}
d[key] = value          # insert/update — O(1) avg
value = d[key]           # lookup (raises KeyError if missing) — O(1) avg
value = d.get(key, dflt) # safe lookup — O(1) avg
del d[key]                # delete — O(1) avg
key in d                  # membership — O(1) avg
len(d)                    # size — O(1)
d.keys() / .values() / .items()  # views — O(1) to obtain, O(n) to fully iterate
```

### 12.4 Python Syntax Cheat Sheet

| Task | Snippet |
|---|---|
| Frequency count | `Counter(iterable)` |
| Group by key | `defaultdict(list)` |
| Safe default access | `d.get(key, default)` |
| Auto-init on missing key | `d.setdefault(key, []).append(x)` |
| Hashable immutable set | `frozenset(iterable)` |
| Set algebra | `a & b`, `a \| b`, `a - b`, `a ^ b` |
| Ordered dict with reordering | `OrderedDict()` + `.move_to_end(key)` |
| Custom hashable class | Define `__eq__` **and** `__hash__` together |

### 12.5 Recognition Guide Cheat Sheet

| Signal | Pattern |
|---|---|
| "seen before / duplicate" | `set` |
| "count / frequency / most common" | `dict` / `Counter` |
| "pair that sums to X" | `dict` value→index (Two Sum) |
| "subarray sum/xor equals k" | Prefix sum/xor + `dict` |
| "group by property" | `defaultdict(list)` + canonical key |
| "longest substring without X" | Sliding window + `dict` |
| "O(1) cache with eviction" | `OrderedDict` / hashmap + linked list |

### 12.6 Pattern Summary Cheat Sheet

```
PRESENCE            →  set
FREQUENCY           →  dict / Counter
PAIR LOOKUP         →  dict (value → index)
PREFIX SUM/XOR      →  dict (prefix value → count/first-index)
CANONICAL GROUPING  →  defaultdict(list) keyed by sorted/tuple form
SLIDING WINDOW      →  dict (char → count or last index)
ROLLING HASH        →  polynomial hash + modulo, O(1) window update
```

### 12.7 Collision Strategy Cheat Sheet

| Strategy | Clustering | Deletion | Memory |
|---|---|---|---|
| Chaining | None (buckets grow) | Easy | Higher (pointers/lists) |
| Linear Probing | High (primary) | Needs tombstones | Lower |
| Quadratic Probing | Medium (secondary) | Needs tombstones | Lower |
| Double Hashing | Low | Needs tombstones | Lower |

---

## 13. Practice Problems (Curated, Multi-Platform)

> 🔗 Links point to each platform's general problem/search page where the exact problem name should be searched, since some platforms restructure URLs over time — search the **Problem Name** on the given **Platform** to find it reliably.

### 13.1 Basics

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Two Sum | LeetCode | Easy | Two Sum | dict value→index |
| Contains Duplicate | LeetCode | Easy | Duplicate Detection | set membership |
| Valid Anagram | LeetCode | Easy | Frequency Counting | Counter comparison |
| First Unique Character | LeetCode | Easy | Frequency Counting | Counter + re-scan |
| Ransom Note | LeetCode | Easy | Frequency Counting | Counter subtraction |

### 13.2 Frequency Counting

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Top K Frequent Elements | LeetCode | Medium | Frequency + Heap | Counter.most_common |
| Sort Characters By Frequency | LeetCode | Medium | Frequency Counting | Counter |
| Word Frequency | GeeksforGeeks | Easy | Frequency Counting | dict |
| Majority Element | LeetCode | Easy | Frequency Counting | dict / Boyer-Moore |

### 13.3 Hash Set

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Longest Consecutive Sequence | LeetCode | Medium | Hash Set | set + expansion check |
| Happy Number | LeetCode | Easy | Cycle Detection | set of seen states |
| Intersection of Two Arrays | LeetCode | Easy | Set Algebra | set intersection |
| Single Number | LeetCode | Easy | Set/XOR | set or XOR trick |

### 13.4 Hash Map

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Isomorphic Strings | LeetCode | Easy | Bijection Mapping | two dicts |
| Word Pattern | LeetCode | Easy | Bijection Mapping | two dicts |
| Copy List with Random Pointer | LeetCode | Medium | Node Cloning | dict old→new node |
| Design HashMap | LeetCode | Easy | Design | Chaining implementation |

### 13.5 Two Sum Family

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Two Sum | LeetCode | Easy | Two Sum | dict |
| 3Sum | LeetCode | Medium | Two Sum + sort/two-pointer | hybrid |
| 4Sum II | LeetCode | Medium | Pair Sum Extension | dict of pair-sums |
| Two Sum IV - Input is a BST | LeetCode | Easy | Two Sum | set traversal |

### 13.6 Prefix Sum / Prefix XOR

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Subarray Sum Equals K | LeetCode | Medium | Prefix Sum | dict of prefix sums |
| Continuous Subarray Sum | LeetCode | Medium | Prefix Sum + Modulo | dict of remainders |
| Subarray Sums Divisible by K | LeetCode | Medium | Prefix Sum + Modulo | dict of remainders |
| XOR Queries of a Subarray | LeetCode | Medium | Prefix XOR | prefix xor array |
| Subarrays with XOR equal to K | GeeksforGeeks | Medium | Prefix XOR | dict of prefix xor |

### 13.7 Sliding Window + Hashing

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Longest Substring Without Repeating Characters | LeetCode | Medium | Sliding Window | dict of last index |
| Minimum Window Substring | LeetCode | Hard | Sliding Window | dict of required counts |
| Permutation in String | LeetCode | Medium | Sliding Window | Counter comparison |
| Find All Anagrams in a String | LeetCode | Medium | Sliding Window | Counter comparison |
| Longest Substring with At Most K Distinct Characters | LeetCode (Premium) / GeeksforGeeks | Medium/Hard | Sliding Window | dict of counts |

### 13.8 Anagrams

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Group Anagrams | LeetCode | Medium | Grouping | canonical key |
| Valid Anagram | LeetCode | Easy | Frequency Counting | Counter |
| Find All Anagrams in a String | LeetCode | Medium | Sliding Window | Counter |

### 13.9 Design Problems

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| LRU Cache | LeetCode | Medium | Design | dict + OrderedDict |
| LFU Cache | LeetCode | Hard | Design | dict + frequency buckets |
| Design HashSet | LeetCode | Easy | Design | Chaining |
| Design HashMap | LeetCode | Easy | Design | Chaining |
| Insert Delete GetRandom O(1) | LeetCode | Medium | Design | dict + array |
| Design Twitter | LeetCode | Medium | Design | dict of user→tweets |
| Encode and Decode TinyURL | LeetCode | Medium | Design | dict short↔long |

### 13.10 Cross-Platform Extra Practice

| Problem | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Distinct Elements in Every Window | GeeksforGeeks | Medium | Sliding Window | dict of counts |
| Check If Array Pairs Are Divisible by K | HackerRank | Medium | Frequency + Modulo | dict of remainders |
| Frequency of the Most Frequent Element | LeetCode | Medium | Frequency Counting | Counter/dict |
| Cycle Detection in Sequences | InterviewBit | Medium | Hash Set | set of visited states |
| Pairs with Given Sum | Code360 (Coding Ninjas) | Easy | Two Sum | dict |
| Longest Subarray with Sum K | Code360 (Coding Ninjas) | Medium | Prefix Sum | dict |
| Anagram Substring Search | GeeksforGeeks | Medium | Sliding Window | Counter |
| Distinct Substrings Count | Codeforces (search tag: strings/hashing) | Medium | Rolling Hash | polynomial hash + set |
| String Matching (Rabin-Karp practice) | CSES (String Algorithms section) | Medium | Rolling Hash | Rabin–Karp |
| Password (hash-based string problems) | AtCoder (search: string hashing) | Medium | Rolling Hash | polynomial hash |
| Two Sets (partition, hashing/DP hybrid) | CodeChef | Medium | Frequency + partition logic | dict |

### 13.11 How to Practice Effectively

1. **First pass:** Solve using brute force to build intuition, even if slow.
2. **Second pass:** Identify which hashing pattern applies (Section 5.1 table) before coding the optimal solution.
3. **Third pass (a week later):** Re-solve from scratch without looking at your old code — true retention check.
4. Keep a personal **pattern log**: for every problem solved, write one line — "Pattern used + why hashing fit here."

---

## 14. Final Revision — Mind Maps & Quick Recall

### 14.1 One-Page Mind Map (ASCII)

```
                                   HASHING
                                      │
      ┌──────────────┬───────────────┼───────────────┬──────────────┐
      ▼              ▼               ▼               ▼              ▼
 HASH FUNCTIONS  COLLISION      PYTHON TOOLS      PATTERNS     APPLICATIONS
      │          RESOLUTION          │               │              │
  ┌───┴───┐      ┌────┴────┐   ┌─────┴─────┐   ┌─────┴─────┐  ┌─────┴─────┐
  │Modulo │      │Chaining │   │dict/set   │   │Frequency  │  │Caching    │
  │Polynom│      │Linear   │   │Counter    │   │Two Sum    │  │Databases  │
  │Rolling│      │Quadratic│   │defaultdict│   │PrefixSum  │  │Networking │
  │Univers│      │Double   │   │OrderedDict│   │Grouping   │  │Compilers  │
  │al     │      │Hashing  │   │frozenset  │   │SlidingWin │  │Blockchain │
  └───────┘      └─────────┘   └───────────┘   │RollingHash│  │BloomFilter│
                                                 └───────────┘  └───────────┘
```

### 14.2 Pattern Decision Map (Quick Recall)

```
Need existence check only?        → set
Need counts?                      → dict / Counter
Need value → index/position?      → dict
Need cumulative sum/xor lookup?   → dict seeded with {0: 1}
Need canonical grouping?          → defaultdict(list) + sorted/tuple key
Need window state (chars/counts)? → dict, shrink/expand window
Need fast substring comparison?  → rolling/polynomial hash + verify
```

### 14.3 Complexity Master Sheet

| Structure/Operation | Time (avg) | Time (worst) | Space |
|---|---|---|---|
| dict/set insert/lookup/delete | O(1) | O(n) | O(n) |
| Two Sum (hash approach) | O(n) | O(n) | O(n) |
| Subarray Sum = K | O(n) | O(n) | O(n) |
| Group Anagrams (sort key) | O(n·k log k) | same | O(n·k) |
| Group Anagrams (count key) | O(n·k) | same | O(n·k) |
| Longest Substring w/o Repeat | O(n) | O(n) | O(min(n,alphabet)) |
| Rabin–Karp search | O(n+m) | O(n·m) | O(1) extra |
| Rehashing (amortized per op) | O(1) | O(1) amortized | O(n) |

### 14.4 Hashing Decision Tree (Final Recall Version)

```
Is fast "have I seen this" the core need?
        │
       Yes
        │
        ▼
Do you need counts, not just yes/no?
   │                    │
  Yes                  No
   │                    │
   ▼                    ▼
dict/Counter          set
   │
   ▼
Is it cumulative (subarray) rather than per-element?
   │
  Yes → prefix sum/xor + dict (seed {0:1})
   │
  No → plain frequency map

Is grouping by a derived/canonical property needed?
   │
  Yes → defaultdict(list) + canonical key

Is a moving window with add/remove needed?
   │
  Yes → dict tracking counts/last-index inside a sliding window loop
```

### 14.5 Interview Cheat Sheet (Last-Minute)

- Average O(1), worst O(n) — always say both.
- Chaining = buckets of lists; Open addressing = probe sequences (linear/quadratic/double).
- Tombstones needed for correct deletion in open addressing.
- `__eq__` requires matching `__hash__`; mutable objects shouldn't be dict keys.
- Two Sum: check complement **before** inserting current value.
- Prefix sum/xor problems: seed the map with `{0: 1}`.
- Rabin–Karp: always verify actual substring after a hash match (avoid false positives).
- Python dict/set: open addressing internally, insertion order preserved since 3.7.
- Hash randomization (SipHash) defends against hash-flooding DoS — not relevant to correctness, only security/performance under adversarial input.

### 14.6 15-Minute Revision

1. Re-read Section 12 (Cheat Sheets) top to bottom. (5 min)
2. Re-derive Two Sum and Subarray Sum = K from memory without looking. (5 min)
3. Say out loud: chaining vs open addressing trade-offs, and why `__eq__`/`__hash__` must match. (5 min)

### 14.7 1-Hour Revision

1. Re-read Sections 1–4 (Foundations) — 15 min.
2. Re-implement (from scratch, no peeking) Two Sum, Subarray Sum = K, Group Anagrams, and Longest Substring Without Repeating Characters — 25 min.
3. Re-read Section 5.1 pattern map + Section 7 recognition flowchart — 10 min.
4. Solve 2 new problems from Section 13 timed at 10 minutes each, applying pattern recognition before coding — 10 min (choose short/easy problems for the time-box).

### 14.8 Summary of the Entire Handbook (One Paragraph)

Hashing converts arbitrary keys into fixed-size integers via a hash function, enabling near O(1) average-case storage and retrieval by direct computation instead of search; collisions are unavoidable and resolved via chaining or open addressing (linear/quadratic/double probing), with load factor and rehashing keeping performance stable; Python's `dict`/`set` implement this internally via open addressing with insertion-order preservation since 3.7 and randomized string hashing for security; nearly all "hashing pattern" interview problems reduce to remembering what's been seen (`set`), counting occurrences (`dict`/`Counter`), tracking complements/positions (`dict`), or maintaining cumulative/windowed state (`dict` with prefix sums/xors or sliding windows) — mastering these few templates, plus real-world uses like caching, indexing, consistent hashing, deduplication, and Bloom filters, covers the entire practical and interview surface area of hashing.

---

## 15. FAQs

**Q1: Why is hash table lookup O(1) on average but O(n) in the worst case?**
Because the average case assumes a well-distributed hash function spreading keys evenly across buckets. The worst case occurs when many/all keys collide into the same bucket (poor hash function, or an adversary crafting colliding keys), degrading lookup to a linear scan.

**Q2: Why can't I use a list as a dictionary key in Python?**
Lists are mutable. If a mutable object's contents changed after being used as a key, its hash value could change, but the dict has already placed it based on the old hash — making the entry unfindable. Python disallows this entire bug class by requiring key hashability, and lists don't implement `__hash__` (it's set to `None`).

**Q3: Does Python's dict guarantee insertion order?**
Yes, as a **language specification guarantee** since Python 3.7 (it was a CPython implementation detail in 3.6). Before 3.6, order was not guaranteed at all.

**Q4: What's the difference between `dict.get(key)` and `dict[key]`?**
`dict[key]` raises `KeyError` if the key is missing. `dict.get(key, default)` returns `default` (or `None` if unspecified) instead of raising — safer for optional lookups.

**Q5: When should I use `Counter` instead of a plain `dict`?**
Whenever the task is fundamentally about counting occurrences — `Counter` gives you `.most_common()`, default-zero counting, and multiset arithmetic (`+`, `-`) for free.

**Q6: Why does Python randomize string hashing?**
To prevent **hash-flooding denial-of-service attacks**, where an attacker submits many strings engineered to collide under a fixed, known hash algorithm, forcing your application's dict/set operations toward O(n) and causing a slowdown/outage.

**Q7: Is `hash()` safe to use for security purposes (e.g., checking data integrity)?**
No. Python's `hash()` is a fast, non-cryptographic, per-process-randomized function meant for internal data-structure use — not designed to resist deliberate collision attacks. For security/integrity, use `hashlib` (SHA-256/SHA-3) and, for passwords, dedicated slow hashing (bcrypt/argon2).

**Q8: What's the difference between chaining and open addressing, in one sentence each?**
Chaining stores colliding entries in a list attached to each bucket; open addressing stores every entry directly inside the table array itself, resolving collisions by probing for another slot.

**Q9: Why do CPython dicts use open addressing instead of chaining?**
Open addressing avoids the memory overhead and cache-unfriendly pointer-chasing of linked chains, giving better real-world performance for typical workloads despite chaining's simpler deletion semantics.

**Q10: What is a "good" load factor threshold?**
Commonly around 0.7 for open addressing schemes (CPython resizes around two-thirds full); separate chaining can tolerate a higher load factor since buckets simply grow, though performance still degrades gradually as chains lengthen.

**Q11: Why do we seed prefix-sum hash maps with `{0: 1}`?**
It represents the "empty prefix" (sum of zero elements = 0) occurring once before any elements are processed, ensuring subarrays that start at index 0 are counted correctly when their sum matches the target exactly.

**Q12: How is a Bloom filter different from a regular hash set?**
A hash set stores actual elements and gives exact answers with no false positives/negatives, using O(n) space proportional to elements stored. A Bloom filter stores only a bit array and multiple hash functions, using far less memory, but can produce false positives (says "maybe present" for something never inserted) while never producing false negatives.

**Q13: Can two different objects have the same hash value?**
Yes — this is a collision, and it's mathematically guaranteed to happen eventually (Pigeonhole Principle) since the space of possible inputs is larger than the space of possible hash outputs. A correct hash-based system must always resolve collisions (chaining/open addressing) and, when comparing hashed values for equality (e.g., Rabin–Karp), verify with a true equality check afterward.

**Q14: What's the practical difference between `set` and `frozenset`?**
`set` is mutable (supports `.add()`, `.remove()`) and therefore unhashable itself. `frozenset` is immutable and hashable, so it can be used as a dict key or as an element inside another set.

**Q15: Is it ever correct to use hashing when I need sorted/ordered output?**
Hashing itself provides no ordering guarantee (aside from Python's insertion-order-preserving dict, which is *not* value-sorted order). If you need range queries or sorted traversal, pair hashing with sorting a snapshot of keys, or use a different structure (sorted containers/BSTs) as the primary structure.

---

### 📌 Closing Note

This handbook intentionally stayed within the boundaries of **Hashing** as a standalone topic — other data structures and algorithms (arrays, trees, graphs, DP, heaps) were mentioned only where necessary for contrast or as companions to a hashing-based solution (e.g., LRU Cache pairing a hash map with a linked list). For deeper practice, revisit [Section 13](#13-practice-problems-curated-multi-platform) regularly and use [Section 14](#14-final-revision--mind-maps--quick-recall) as a pre-interview warm-up.

