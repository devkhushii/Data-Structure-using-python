# THE COMPLETE TRIE (PREFIX TREE) HANDBOOK

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Python Trie Implementation](#2-python-trie-implementation)
3. [Trie Fundamentals](#3-trie-fundamentals)
4. [Trie Operations](#4-trie-operations)
5. [Types of Tries](#5-types-of-tries)
6. [Trie Patterns](#6-trie-patterns)
7. [Advanced Trie Concepts](#7-advanced-trie-concepts)
8. [Applications](#8-applications)
9. [Problem Recognition](#9-problem-recognition)
10. [Optimization](#10-optimization)
11. [Interview Preparation](#11-interview-preparation)
12. [Python Tips](#12-python-tips)
13. [Common Mistakes](#13-common-mistakes)
14. [Cheat Sheets](#14-cheat-sheets)
15. [Practice Problems](#15-practice-problems)
16. [Final Revision](#16-final-revision)

---

## 1. Introduction

### 1.1 What is a Trie?

A **Trie** (pronounced "try", from re**TRIE**val) is a tree-shaped data structure used to store a dynamic set of strings, where each node represents a single character and paths from the root down to marked nodes spell out the strings stored in the structure.

Unlike a Binary Search Tree, where each node holds an entire key, a Trie **decomposes** each key into its individual characters and spreads them across a path in the tree. Keys that share a common prefix literally share the same path in memory — this is the single most important idea in the entire data structure.

> **Note:** A Trie is also called a **Prefix Tree**, **Digital Tree**, or **Radix Tree** (the compressed variant). All refer to the same underlying concept: organizing strings by shared prefixes.

### 1.2 History

- The idea traces to work by **Axel Thue** in 1912 in formal language theory, but the data structure as used in computing was **formalized by Edward Fredkin in 1960**, who coined the term "trie" by extracting it from the middle of the word "retrieval".
- **René de la Briandais** described a similar structure in 1959 for fast string lookups.
- Since then, tries have become foundational in **information retrieval, compilers, networking (IP routing), and bioinformatics**.

### 1.3 Why Tries Exist

Consider storing the words `{"cat", "car", "cart", "dog"}` in a hash set. A hash set answers "is this exact word present?" in O(1) average time, but it **cannot answer prefix questions efficiently**:

- "What words start with `ca`?"
- "What is the longest prefix of `caterpillar` present in my dictionary?"
- "Auto-complete the word the user is typing."

To answer these with a hash map, you would need to enumerate every key and check `str.startswith()` — an **O(N × L)** operation where N is the number of words and L is average word length. A Trie answers these in **O(L)**, where L is just the length of the query string, completely independent of how many words are stored.

This is the core motivation: **Tries trade memory for prefix-query speed.**

### 1.4 The Prefix Tree Concept

```
Words: "car", "cart", "care", "dog"

                (root)
               /      \
              c        d
              |        |
              a        o
              |        |
              r*       g*
            / | 
           t*  e*
```

`r` after `ca` is marked end-of-word (for "car"). Branching continues to `t` (for "cart") and `e` (for "care"). Every node on the path `c -> a -> r` is **shared** by three words. This sharing is what gives Tries their power for prefix-heavy datasets.

### 1.5 Characteristics

| Property | Description |
|---|---|
| Node degree | Up to `\|alphabet\|` children per node (26 for lowercase English) |
| Depth | Equal to the length of the longest key on that path |
| Key storage | Implicit — keys are represented by root-to-node paths, not stored in a single node |
| Ordering | Naturally supports lexicographic (sorted) traversal |
| Shared prefixes | Stored exactly once |
| Search cost | O(L) where L = length of the search string |

### 1.6 Advantages

1. **O(L) search, insert, and prefix queries** — independent of the number of stored words (N).
2. **Natural prefix operations** — `startsWith`, autocomplete, and longest-prefix-match are trivial.
3. **Lexicographically sorted iteration** — a DFS traversal yields keys in sorted order for free.
4. **No hash collisions** — unlike hash maps, there's no collision handling needed.
5. **Efficient shared storage** for datasets with heavy prefix overlap (dictionaries, IP tables, genomic data).

### 1.7 Disadvantages

1. **High memory overhead** — each node may reserve space for up to 26 (or more) child pointers, even if only 1–2 are used.
2. **Cache-unfriendliness** — nodes are scattered across the heap connected by pointers/references, unlike a contiguous array, so traversal often causes cache misses.
3. **Not ideal for small datasets** — a plain list or hash set is simpler and often faster when N is small.
4. **Alphabet-size dependent** — a large or unicode alphabet increases branching factor and memory per node dramatically (mitigated using dictionaries — see Section 2).

### 1.8 Applications (Preview — expanded in Section 8)

- Autocomplete / search-bar suggestions (Google, IDEs)
- Spell checkers and dictionaries
- IP routing tables (longest prefix match)
- T9 predictive text on phone keypads
- Bioinformatics (DNA/protein substring/prefix matching)
- Word games (Boggle, Scrabble word validation)
- Competitive programming (maximum XOR pair, string matching)

### 1.9 Real-World Analogy

Think of a **library card catalog organized letter-by-letter**. To find all books whose title starts with "PYTH", you walk to the drawer labeled P, then within it to the section labeled PY, then PYT, then PYTH — narrowing down at each letter. You never re-scan books that don't match the prefix you've already committed to. This is *exactly* how a Trie search works: each character you consume moves you one level deeper and narrows the candidate set, never requiring you to backtrack over already-eliminated branches.

> **Interview Tip:** If an interviewer's problem repeatedly mentions "prefix", "starts with", "dictionary of words", or "autocomplete" — a Trie is very likely the intended data structure. See Section 9 for a full recognition flowchart.

---

## 2. Python Trie Implementation

### 2.1 The TrieNode Class

Every Trie is built out of nodes. In Python, the most idiomatic and interview-friendly representation of a node uses a **dictionary** to map characters to child nodes, plus a boolean flag marking word endings.

```python
class TrieNode:
    """
    A single node in the Trie.

    Attributes:
        children (dict[str, TrieNode]): maps a character to the next TrieNode
        is_end_of_word (bool): True if a word ends exactly at this node
    """
    __slots__ = ("children", "is_end_of_word")  # memory optimization, see 2.9

    def __init__(self):
        self.children = {}          # dict-based adjacency: O(1) average lookup
        self.is_end_of_word = False # marks a complete word boundary
```

**Line-by-line explanation:**

- `__slots__ = ("children", "is_end_of_word")`: tells Python not to create a per-instance `__dict__`. Since a Trie can have millions of nodes, this alone can cut memory usage by 30–50%.
- `self.children = {}`: an empty dictionary — no character edges exist yet. Keys are single characters, values are `TrieNode` instances.
- `self.is_end_of_word = False`: by default, no word ends here. Set to `True` only when an insertion terminates at this exact node.

### 2.2 The Trie Class (Dictionary-Based — RECOMMENDED)

```python
class Trie:
    """
    Standard Trie supporting insert, search, and prefix queries.
    Dictionary-based children => works for ANY alphabet (unicode-safe).
    """

    def __init__(self):
        self.root = TrieNode()   # the root never represents a character itself

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:                      # walk/create one edge per character
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True            # mark the final node

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def _traverse(self, s: str):
        """Shared helper: walk from root following each character of s.
        Returns the final TrieNode, or None if the path breaks early."""
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

**Line-by-line explanation:**

- `self.root = TrieNode()`: an empty sentinel node; it holds no character itself, only the first-letter edges of all inserted words.
- `insert`: for each character in `word`, either follow an existing edge or create a brand-new `TrieNode`. After the loop, `node` points at the node representing the *last* character — this gets flagged `is_end_of_word = True`.
- `search`: reuses `_traverse` to walk the full string, then additionally checks `is_end_of_word` — this is what distinguishes a **complete word** from a **mere prefix**.
- `starts_with`: identical traversal, but does **not** check `is_end_of_word` — any valid path means the prefix exists.
- `_traverse`: the DRY (Don't Repeat Yourself) helper. If any character is missing from `children`, the path is broken and we return `None` immediately — an O(1) short-circuit.

> **Why this design is preferred in interviews:** it cleanly separates "does this exact word exist" from "does this prefix exist", which are the two most commonly confused concepts in Trie problems (see Section 13.3).

### 2.3 Complete Dry Run — Insert + Search

Insert `"cat"`, `"car"`, `"dog"` then search `"car"` and `"ca"`.

| Step | Operation | Current Node | Action | Trie State (edges created) |
|---|---|---|---|---|
| 1 | insert("cat") | root | create 'c' | root→c |
| 2 | insert("cat") | c | create 'a' | root→c→a |
| 3 | insert("cat") | a | create 't' | root→c→a→t |
| 4 | insert("cat") | t | mark end | t.is_end_of_word = True |
| 5 | insert("car") | root | reuse 'c' | (no new node) |
| 6 | insert("car") | c | reuse 'a' | (no new node) |
| 7 | insert("car") | a | create 'r' | root→c→a→r |
| 8 | insert("car") | r | mark end | r.is_end_of_word = True |
| 9 | insert("dog") | root | create 'd' | root→d |
| 10 | insert("dog") | d | create 'o' | root→d→o |
| 11 | insert("dog") | o | create 'g' | root→d→o→g |
| 12 | insert("dog") | g | mark end | g.is_end_of_word = True |
| 13 | search("car") | walk c→a→r | r.is_end_of_word == True | return **True** |
| 14 | search("ca") | walk c→a | a.is_end_of_word == False | return **False** |
| 15 | starts_with("ca") | walk c→a | path exists | return **True** |

Final Trie shape:

```
root
├── c
│   └── a
│       ├── t*      (end: "cat")
│       └── r*      (end: "car")
└── d
    └── o
        └── g*      (end: "dog")
```

### 2.4 Fixed-Array Implementation (Alternative)

When the alphabet is known and small (e.g., lowercase English `a`–`z`), a fixed-size array of 26 pointers can replace the dictionary for slightly faster constant-factor lookups (no hashing needed):

```python
class ArrayTrieNode:
    def __init__(self):
        self.children = [None] * 26   # index i => character chr(ord('a') + i)
        self.is_end_of_word = False


class ArrayTrie:
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = ArrayTrieNode()
            node = node.children[idx]
        node.is_end_of_word = True

    def __init__(self):
        self.root = ArrayTrieNode()
```

**Trade-off table:**

| Aspect | Dictionary-based | Fixed-array-based |
|---|---|---|
| Alphabet support | Any (unicode, mixed-case, symbols) | Fixed, must know alphabet size upfront |
| Memory per node (empty) | ~64 bytes (empty dict) | 26 × 8 bytes = 208 bytes (pointers), always allocated |
| Lookup speed | O(1) average (hashing cost) | O(1) worst-case (direct indexing, no hashing) |
| Best for | Interviews, general text, unknown alphabets | Competitive programming with only lowercase letters, performance-critical code |

> **Interview Tip:** Default to the **dictionary-based** implementation unless the problem explicitly restricts the alphabet (e.g., "words consist of lowercase English letters only") AND performance is paramount — then array-based may be asked as a follow-up optimization.

### 2.5 Recursive Implementation

Some interviewers ask for recursive insert/search to test comfort with recursion:

```python
class RecursiveTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        self._insert(self.root, word, 0)

    def _insert(self, node: TrieNode, word: str, i: int) -> None:
        if i == len(word):
            node.is_end_of_word = True
            return
        ch = word[i]
        if ch not in node.children:
            node.children[ch] = TrieNode()
        self._insert(node.children[ch], word, i + 1)

    def search(self, word: str) -> bool:
        return self._search(self.root, word, 0)

    def _search(self, node: TrieNode, word: str, i: int) -> bool:
        if node is None:
            return False
        if i == len(word):
            return node.is_end_of_word
        ch = word[i]
        return self._search(node.children.get(ch), word, i + 1)
```

**Line-by-line explanation:**

- `_insert(node, word, i)`: base case `i == len(word)` means we've consumed every character — mark the current node as a word end.
- Otherwise, ensure the edge for `word[i]` exists, then recurse one level deeper with `i + 1`.
- `_search` mirrors this, but with an added `node is None` guard since `.get(ch)` may return `None` if the edge doesn't exist.

> **Warning:** Recursive versions add O(L) call-stack frames. For extremely long strings (e.g., DNA sequences with length in the millions), this risks a `RecursionError`. Iterative is safer in production; recursive is fine — even preferred for readability — in interviews with small inputs.

### 2.6 Iterative vs Recursive — When to Use Which

| Criterion | Iterative | Recursive |
|---|---|---|
| Stack safety | Safe for arbitrarily long strings | Risk of stack overflow for very long strings |
| Readability | Slightly more verbose | Often cleaner, mirrors the mathematical definition |
| Performance | Marginally faster (no call overhead) | Marginally slower |
| Interview preference | Preferred for production-quality code | Acceptable, sometimes expected for elegance |

### 2.7 Using `defaultdict` for Compact Insert

```python
from collections import defaultdict

class CompactTrie:
    def __init__(self):
        # nested defaultdicts: no explicit TrieNode class needed
        self.root = defaultdict(lambda: defaultdict(...))
```

In practice, a cleaner idiom is a **single defaultdict of defaultdicts**, often written as:

```python
def make_trie():
    return defaultdict(make_trie)

trie = make_trie()
word = "cat"
node = trie
for ch in word:
    node = node[ch]          # auto-vivifies missing keys
node["#"] = True             # "#" is a sentinel marking end-of-word
```

**Explanation:** `defaultdict(make_trie)` means accessing any missing key auto-creates a new nested `defaultdict` — this eliminates the `if ch not in node.children` check entirely. The `"#"` key is a common competitive-programming trick to mark word endings without a separate boolean field. This is **extremely fast to write** in a contest but **less readable and less explicit** than the class-based version — use in speed-coding contexts (Codeforces/CSES), not in interviews where clarity is graded.

### 2.8 Memory Representation — What Actually Happens Under the Hood

```
TrieNode instance (dict-based, with __slots__):
┌─────────────────────────────┐
│ children: {'a': <ptr>, ...} │  <- a Python dict object (hash table)
│ is_end_of_word: False       │  <- a single bool (interned True/False)
└─────────────────────────────┘

Each entry in `children` dict:
  key   -> single-character str object (Python interns 1-char strings, so
            no duplicate string objects are created for repeated letters)
  value -> reference (pointer) to another TrieNode object on the heap
```

Because Python **interns single-character strings**, using single characters as dict keys is memory-cheap — you are never allocating a new string object per edge, only reusing cached ones.

### 2.9 Performance Considerations & Best Practices

1. **Always use `__slots__`** on `TrieNode` in performance-sensitive code — this can reduce memory by 30–50% when millions of nodes exist.
2. **Prefer dictionaries over arrays** unless the alphabet is small and fixed AND you've profiled that array indexing meaningfully helps.
3. **Avoid recursive implementations for extremely long strings** (bioinformatics, whole-file text) — use iterative loops.
4. **Batch insert during construction**, then treat the Trie as read-mostly if your workload is query-heavy (e.g., autocomplete engines) — this allows further optimizations like **compression** (Section 5.3) after the fact.
5. **Avoid storing the actual word string in every node** — that defeats the purpose of prefix sharing. Reconstruct words by walking root-to-node paths only when needed (e.g., during DFS enumeration).


---

## 3. Trie Fundamentals

### 3.1 Root

The **root** is the unique entry point of every Trie. It represents an empty string `""` and holds no character itself — only outgoing edges to the first characters of stored words. Every traversal begins here.

### 3.2 Node

A **node** represents a position along one or more words' paths. A node does not necessarily represent a complete word — only nodes flagged `is_end_of_word = True` do.

### 3.3 Character Edge

An **edge** connects a parent node to a child node and is labeled with exactly one character. In the dictionary-based implementation, an edge is literally a `(key, value)` pair inside `node.children`.

### 3.4 Prefix

A **prefix** of a string `s` is any string formed by taking the first `k` characters of `s`, for `0 <= k <= len(s)`. In a Trie, every prefix of every inserted word corresponds to exactly one root-to-node path — this is the structural invariant that makes prefix queries O(L).

### 3.5 End-of-Word Marker

Because Trie nodes are shared across multiple words (e.g., "car" is a prefix of "cart"), you cannot infer "is this a complete word?" merely from whether a node has children or not. The **end-of-word marker** (`is_end_of_word` boolean, or a sentinel `"#"` key) is mandatory bookkeeping to disambiguate a "path that happens to continue" from a "complete stored word".

```
Insert "car" then "cart":

root -> c -> a -> r* -> t*
                  ^      ^
             end of "car" end of "cart"

Both r and t are marked. If you only checked "does r have children",
you could NOT tell that "car" itself is a valid complete word,
since r has a child (t).
```

> **Common Mistake:** Forgetting the end-of-word marker and instead checking `len(node.children) == 0` to decide if a word ends — this silently breaks whenever one stored word is a prefix of another. See Section 13.1.

### 3.6 Shared Prefix

When multiple words share a leading substring, they share the corresponding root-to-node path. This is Trie's central space-saving mechanism.

```
Words: "app", "apple", "application", "apply"

root -> a -> p -> p*
                  |
                  l -> e*
                  |
                  i -> c -> a -> t -> i -> o -> n*
                  |
                  y*

All four words share the "app" path (3 nodes) before diverging.
```

### 3.7 Branching

A node **branches** when it has more than one child — this is where stored words diverge from one another. The number of children indicates how many distinct next-characters exist for words sharing the prefix up to that node.

### 3.8 Leaf Node

A **leaf node** has no children. In a Trie, a leaf is always `is_end_of_word = True` (since nothing continues past it) — but the converse is not true: a node marked `is_end_of_word = True` may still have children (as with "car" inside "cart").

### 3.9 Path Representation

The identity of a stored word is entirely encoded as **the sequence of edge-labels from root to a marked node** — no node stores the full word itself (unless deliberately added as an optimization for reconstruction, which is generally discouraged, see 2.9).

### 3.10 Alphabet Size

The **alphabet size** (`|Σ|`) is the number of distinct characters that can appear (26 for lowercase English, 52 for mixed case, 256 for extended ASCII, unbounded for Unicode). Alphabet size directly determines:

- Maximum branching factor per node
- Memory footprint of array-based implementations (`|Σ|` pointers per node, whether used or not)
- Whether dictionary-based (sparse) representation is preferable

| Alphabet | Recommended representation |
|---|---|
| Lowercase English (26) | Array or dict, either fine |
| Mixed case + digits (62) | Dictionary preferred |
| Unicode / arbitrary text | Dictionary mandatory |
| Binary (0/1, for XOR tries) | Fixed 2-element array — see Section 6 |


---

## 4. Trie Operations

### 4.1 Insert (Iterative — Canonical)

Already introduced in 2.2. Full standalone reference:

```python
def insert(self, word: str) -> None:
    node = self.root
    for ch in word:
        node = node.children.setdefault(ch, TrieNode())
    node.is_end_of_word = True
```

`setdefault` is a compact idiom: it returns `node.children[ch]` if present, otherwise inserts a new `TrieNode()` under `ch` first and returns that. This collapses the earlier 3-line `if` check into one line.

- **Time Complexity:** O(L), L = length of `word`.
- **Space Complexity:** O(L) worst case (all new nodes), O(1) extra if the path already fully exists.

### 4.2 Search (Exact Word Match)

```python
def search(self, word: str) -> bool:
    node = self.root
    for ch in word:
        if ch not in node.children:
            return False
        node = node.children[ch]
    return node.is_end_of_word
```

- **Time Complexity:** O(L).
- **Space Complexity:** O(1) extra (iterative, no recursion stack).
- **Edge case:** empty string `""` — returns `self.root.is_end_of_word`, which is `True` only if `""` was explicitly inserted.

### 4.3 StartsWith / Prefix Search

```python
def starts_with(self, prefix: str) -> bool:
    node = self.root
    for ch in prefix:
        if ch not in node.children:
            return False
        node = node.children[ch]
    return True   # reaching here means the full prefix path exists
```

Note the **only** difference from `search`: the final return does not check `is_end_of_word`. Confusing these two return statements is the single most common Trie bug in interviews (Section 13.3).

### 4.4 Delete (With Pruning)

Deleting a word is the trickiest standard operation because you must remove nodes **only if they become useless** — i.e., they have no children AND are not the end of some other word.

```python
def delete(self, word: str) -> bool:
    """Returns True if the word was found and deleted."""
    found = [False]   # mutable cell so the nested function can report success upward

    def _delete(node: TrieNode, word: str, depth: int) -> bool:
        if depth == len(word):
            if not node.is_end_of_word:
                return False              # word was never present
            node.is_end_of_word = False
            found[0] = True
            return len(node.children) == 0   # tell parent: "I'm now prunable"

        ch = word[depth]
        child = node.children.get(ch)
        if child is None:
            return False                  # word not present

        should_prune_child = _delete(child, word, depth + 1)

        if should_prune_child:
            del node.children[ch]          # remove the now-useless child

        # Current node is prunable itself only if it has no children left
        # AND it is not the end of a different word.
        return len(node.children) == 0 and not node.is_end_of_word

    _delete(self.root, word, 0)
    return found[0]
```

> **Note:** `_delete`'s return value tracks *prunability* (used internally by the parent call to decide whether to remove an edge), which is a different signal than "was the word actually found and deleted". The `found` mutable cell separates these two concerns cleanly — a subtle but important distinction that's easy to get wrong (returning the raw `_delete(...)` result directly from `delete()` would incorrectly report the *root's* prunability instead of whether deletion happened).

**Line-by-line explanation:**

- The recursion walks down to the exact end node of `word` (`depth == len(word)`).
- At the target node: if it was never marked `is_end_of_word`, the word doesn't exist — return `False` (nothing to prune, nothing deleted).
- Otherwise, un-mark it. If it now has zero children, it's safe to tell the parent to prune the edge leading to it.
- Unwinding the recursion: each parent checks if its child should be pruned (`should_prune_child`), deletes the edge if so, then computes its **own** prunability the same way — no children left AND not an end-of-word itself.
- This guarantees words like `"car"` remain fully intact when you delete `"cart"` — the shared `c-a-r` path is preserved because `r.is_end_of_word` is still `True`.

#### Dry Run — Delete "cart" from {"car", "cart"}

| Depth | Node | Action | Prunable? |
|---|---|---|---|
| 4 (i='t', end) | t | is_end_of_word → False; children empty | True |
| 3 (i='r') | r | delete child 't'; r.is_end_of_word is True (for "car") | False (still marks "car") |
| 2 (i='a') | a | r remains (not pruned); a has children | False |
| 1 (i='c') | c | a remains; c has children | False |
| 0 (root) | root | c remains | — |

Result: only node `t` is removed. `"car"` remains searchable; `"cart"` no longer does.

- **Time Complexity:** O(L).
- **Space Complexity:** O(L) recursion stack (or convert to iterative with an explicit stack + second pass if stack depth is a concern).

> **Common Mistake:** Deleting nodes eagerly without checking `is_end_of_word` on intermediate nodes — this destroys other words that share the deleted word's prefix. Always check both conditions: **no children** AND **not itself a word end**.

### 4.5 Count Words (with a given prefix, or total)

```python
def count_words_with_prefix(self, prefix: str) -> int:
    node = self._traverse(prefix)
    if node is None:
        return 0
    return self._count_words(node)

def _count_words(self, node: TrieNode) -> int:
    count = 1 if node.is_end_of_word else 0
    for child in node.children.values():
        count += self._count_words(child)
    return count
```

An interview-favorite optimization: **store a running counter on each node** (`word_count_below`) that is incremented during every `insert` call along the path — this converts `count_words_with_prefix` from O(nodes in subtree) to O(L):

```python
class CountingTrieNode:
    __slots__ = ("children", "is_end_of_word", "words_below")
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.words_below = 0     # number of words passing through this node

def insert(self, word: str) -> None:
    node = self.root
    for ch in word:
        node = node.children.setdefault(ch, CountingTrieNode())
        node.words_below += 1
    node.is_end_of_word = True

def count_words_with_prefix(self, prefix: str) -> int:
    node = self._traverse(prefix)
    return node.words_below if node else 0
```

### 4.6 Longest Prefix Match (LPM)

Given a Trie of "known" strings, find the **longest one that is a prefix of a query string**. This is exactly how **IP routing tables** work (Section 6).

```python
def longest_prefix_match(self, s: str) -> str:
    node = self.root
    longest = ""
    current = []
    for ch in s:
        if ch not in node.children:
            break
        current.append(ch)
        node = node.children[ch]
        if node.is_end_of_word:
            longest = "".join(current)   # update on every valid word boundary
    return longest
```

**Explanation:** walk character by character; every time the current path lands on an `is_end_of_word` node, record it as the best-so-far — because it's a longer valid prefix than any previous match. Stop as soon as the path breaks (no matching child).

#### Dry Run — Trie = {"a", "ab", "abc"}, query = "abcd"

| Step | Char | Path so far | is_end_of_word? | longest so far |
|---|---|---|---|---|
| 1 | a | "a" | True | "a" |
| 2 | b | "ab" | True | "ab" |
| 3 | c | "abc" | True | "abc" |
| 4 | d | (no child 'd' under 'c') | — | loop breaks |

Result: `"abc"`.

- **Time Complexity:** O(L), L = length of query string.
- **Space Complexity:** O(L) for the `current` buffer.

### 4.7 Auto-complete / Auto-suggestions

Given a prefix, return all stored words starting with it (often the top-k by some ranking, but the base version returns all).

```python
def autocomplete(self, prefix: str, limit: int = None) -> list[str]:
    node = self._traverse(prefix)
    if node is None:
        return []
    results = []
    self._collect(node, list(prefix), results, limit)
    return results

def _collect(self, node: TrieNode, path: list[str], results: list[str], limit) -> None:
    if limit is not None and len(results) >= limit:
        return
    if node.is_end_of_word:
        results.append("".join(path))
    for ch, child in sorted(node.children.items()):   # sorted => lexicographic order
        path.append(ch)
        self._collect(child, path, results, limit)
        path.pop()                                     # backtrack
```

**Explanation:**

- First, traverse to the node representing `prefix` — O(L).
- Then run a DFS from that node, collecting every `is_end_of_word` node encountered, appending each completed character along the way to a mutable `path` list (using `path.pop()` to backtrack — a classic backtracking pattern).
- Sorting `node.children.items()` guarantees lexicographic ("dictionary") output order, matching real-world autocomplete UX (also mirrors sorted DFS order mentioned in 1.5).
- The optional `limit` parameter supports "top-k suggestions" style UIs, stopping the DFS early once enough results are collected.

#### Dry Run — Trie = {"cat", "car", "cart", "dog"}, prefix = "ca"

| Step | Node visited | path | is_end_of_word? | results |
|---|---|---|---|---|
| 1 | traverse "ca" → node 'a' | "ca" | — | [] |
| 2 | visit child 'r' | "car" | True | ["car"] |
| 3 | visit child 't' (under r) | "cart" | True | ["car", "cart"] |
| 4 | backtrack to 'a', visit child 't' | "cat" | True | ["car", "cart", "cat"] |

(Order among children depends on sort order — 'r' < 't', so "car"/"cart" are visited before "cat".)

- **Time Complexity:** O(L + number of nodes in the matching subtree) = O(L + K) where K is total characters across all matches.
- **Space Complexity:** O(K) for results + O(depth) recursion stack.

### 4.8 Lexicographical Traversal

A plain DFS over the entire Trie (starting from root, always visiting children in sorted key order) yields **every stored word in sorted order** — this is a free byproduct of the Trie's structure and is often used to implement `words()` or `to_sorted_list()` utility methods:

```python
def all_words_sorted(self) -> list[str]:
    results = []
    self._collect(self.root, [], results, None)
    return results
```

> **Interview Tip:** If asked to "return all words in sorted order" without a `sorted()` call anywhere — a Trie followed by a plain DFS is the expected elegant answer, since a hash-based dictionary would need an explicit `sorted()` step (O(N log N)), whereas the Trie gives sorted order "for free" during traversal (O(total characters)).


---

## 5. Types of Tries

### 5.1 Standard Trie

The plain structure described in Sections 2–4: one node per character, no compression. Simple, but can waste memory on long chains of single-child nodes (e.g., a word like `"internationalization"` with no sibling words creates 21 single-child nodes in a row).

### 5.2 Prefix Trie

This is simply another name for the Standard Trie when the emphasis is on prefix-query use cases (autocomplete, dictionary lookup) rather than exact-match use cases. There is no structural difference — "Prefix Trie" is a usage-oriented label, not a distinct variant.

### 5.3 Compressed Trie (Radix Tree / PATRICIA Trie)

A **Radix Tree** (also called a **Compressed Trie** or, in its bit-level form, a **PATRICIA trie** — Practical Algorithm To Retrieve Information Coded In Alphanumeric) collapses every chain of single-child nodes into a single edge labeled with a **substring** instead of a single character.

```
Standard Trie for {"romane", "romanus", "romulus", "rubens"}:

r-o-m-a-n-e*
        |
        u-s*
    |
    u-l-u-s*   (branches off after "rom")
|
u-b-e-n-s*     (branches off after "r")

Compressed (Radix) Trie — same words:

              r
              |
          "om" / \ "ub"
             /     \
        "an"        "ens"*
        /   \
   "e"*      "us"*
   
      (plus "rom" -> "ulus"* branch, omitted for brevity)
```

**Key idea:** instead of one node per character, a node's edge stores an entire substring. This reduces node count from O(total characters) to O(number of branching points), which is a massive memory win for sparse datasets (e.g., IP routing tables, where most prefixes don't branch until near the end).

- **Time Complexity:** Still O(L) for search (you compare substrings instead of single characters, but total characters compared per query is bounded by L).
- **Space Complexity:** O(number of words) in the best case, vastly better than O(total characters) for a Standard Trie on sparse data.
- **Trade-off:** insertion and especially deletion are more complex, since a single new word can force **splitting** an existing compressed edge into two.

> **Note:** Real-world systems that need Radix Trees (e.g., Linux kernel routing tables, Redis) implement them exactly this way — this is not just an academic exercise.

### 5.4 Patricia Trie

Historically, "Patricia Trie" refers to the specific **bit-level** radix tree used for binary keys (e.g., IP addresses treated as 32-bit or 128-bit strings), where each node's decision is based on a single differing bit rather than a full character. In modern usage, "Patricia Trie" and "Radix Tree" are frequently used interchangeably; the distinction (bit-level vs character-level compression) is mostly historical/academic — most interviews will just say "compressed trie" or "radix tree".

### 5.5 Ternary Search Tree (TST)

A **Ternary Search Tree** is a hybrid between a BST and a Trie: each node stores **one character** and has exactly **three** children — `less`, `equal`, `greater` — instead of up to 26+ children in a dict/array.

```python
class TSTNode:
    __slots__ = ("char", "left", "mid", "right", "is_end_of_word")
    def __init__(self, char):
        self.char = char
        self.left = self.mid = self.right = None
        self.is_end_of_word = False

class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word: str) -> None:
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, i):
        ch = word[i]
        if node is None:
            node = TSTNode(ch)
        if ch < node.char:
            node.left = self._insert(node.left, word, i)
        elif ch > node.char:
            node.right = self._insert(node.right, word, i)
        elif i + 1 < len(word):
            node.mid = self._insert(node.mid, word, i + 1)
        else:
            node.is_end_of_word = True
        return node
```

**Why it exists:** a standard Trie node with a 26-way dict/array wastes space when most nodes only have 1–2 children (common for sparse alphabets or large datasets with limited branching). TST trades a bit of extra search time (O(L) becomes O(L) *comparisons but with BST-like constant factors, effectively closer to O(L × log Σ) in the worst case) for **significantly less memory per node** — only 3 pointers + 1 char, versus a full dict/array.

| Aspect | Standard Trie | Ternary Search Tree |
|---|---|---|
| Children per node | Up to `\|Σ\|` | Exactly 3 |
| Memory per node | Higher (dict overhead or Σ pointers) | Lower (fixed 3 pointers) |
| Cache locality | Poor | Better (similar to BST) |
| Best for | Dense, small alphabets, prefix-heavy queries | Sparse datasets, large or unknown alphabets, memory-constrained systems |

### 5.6 Binary Trie (Bitwise Trie)

A **Binary Trie** stores numbers as their **binary representations**, with each node having exactly 2 children (0 and 1). This is the standard tool for **Maximum XOR Pair / Maximum XOR Query** problems (Section 6.13–6.14).

```
Insert 5 (binary: 101) and 12 (binary: 1100), using 4 bits:

5  = 0101
12 = 1100

           root
          /    \
         0      1
         |      |
         1      1
         |      |
         0      0
         |      |
         1*     0*
      (5=0101) (12=1100)
```

```python
class BinaryTrieNode:
    __slots__ = ("children",)
    def __init__(self):
        self.children = [None, None]   # index 0 and index 1

class BinaryTrie:
    def __init__(self, bit_length=32):
        self.root = BinaryTrieNode()
        self.bit_length = bit_length

    def insert(self, num: int) -> None:
        node = self.root
        for i in range(self.bit_length - 1, -1, -1):   # MSB to LSB
            bit = (num >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = BinaryTrieNode()
            node = node.children[bit]

    def max_xor_with(self, num: int) -> int:
        """Find the maximum XOR of `num` with any inserted number."""
        node = self.root
        result = 0
        for i in range(self.bit_length - 1, -1, -1):
            bit = (num >> i) & 1
            toggled = 1 - bit                          # the bit that maximizes XOR at this position
            if node.children[toggled] is not None:
                result |= (1 << i)
                node = node.children[toggled]
            else:
                node = node.children[bit]
        return result
```

**Explanation:** to maximize XOR, at every bit position we greedily prefer to walk into the child representing the **opposite** bit of the query number (since `bit XOR opposite_bit = 1`, contributing maximally to that bit position of the result). If that opposite child doesn't exist, we're forced down the same-bit child (contributing a 0 at that position).

- **Time Complexity:** O(bit_length) per insert/query — effectively O(32) or O(64), i.e., O(1) in practice for fixed-width integers.
- **Space Complexity:** O(N × bit_length) nodes in the worst case.

### 5.7 Suffix Trie (Overview)

A **Suffix Trie** stores **every suffix** of a string `s` (not just `s` itself), enabling O(pattern length) substring search after O(n²) or O(n) construction (depending on algorithm sophistication — e.g., Ukkonen's algorithm for O(n) suffix tree construction). Related to but simpler (and more memory-hungry) than a **Suffix Tree**, which is the compressed version.

```
s = "banana"
Suffixes: "banana", "anana", "nana", "ana", "na", "a"

A Suffix Trie contains a root-to-leaf path for EACH suffix,
enabling queries like "is 'nan' a substring of banana?" in O(len('nan')).
```

> **Note:** Full suffix tree/array construction algorithms (Ukkonen's, DC3) are out of scope for this Trie-focused handbook — mentioned here only for context on how Tries generalize to substring (not just prefix) matching.

### 5.8 Persistent Trie (Overview)

A **Persistent Trie** preserves previous versions of itself after every modification, using **path copying**: only the O(L) nodes along the modified path are cloned; all unmodified subtrees are shared (referenced, not copied) between versions. This enables O(L) "checkpoint" snapshots without O(N) full copies — useful in problems requiring **version history** (e.g., "maximum XOR pair within array range [l, r]", solved with persistent binary tries).


---

## 6. Trie Patterns

### 6.1 Pattern Overview Table

| Pattern | Core Idea | Example Problems |
|---|---|---|
| Prefix Matching | Traverse & check path existence | `startsWith`, Implement Trie |
| Auto-complete | DFS from prefix node | Search Suggestions System |
| Dictionary Search | Exact match via `is_end_of_word` | Word Search II |
| Word Dictionary (wildcards) | DFS with `.` branching | Design Add and Search Words |
| Replace Words | Shortest-prefix match (root) | Replace Words |
| Longest Common Prefix | Single-child chain traversal | Longest Common Prefix |
| Stream Checker | Reverse-insert + suffix matching | Stream of Characters |
| Word Search (grid) | Trie + DFS/backtracking on grid | Word Search II |
| Maximum XOR | Binary Trie greedy traversal | Maximum XOR of Two Numbers |
| IP Routing | Longest Prefix Match on Binary Trie | Longest Prefix Match (networking) |

### 6.2 Prefix Matching

Covered fully in Section 4.3 (`starts_with`). The universal signal: any problem asking "does X start with Y" for a dynamic, queryable set of strings.

### 6.3 Auto-complete (Search Suggestions System)

**Problem:** Given a list of products and a search word typed character by character, return up to 3 lexicographically-smallest products that share a prefix with what's typed so far, after each character.

```python
def suggested_products(products: list[str], search_word: str) -> list[list[str]]:
    trie = Trie()
    for p in products:
        trie.insert(p)

    result = []
    prefix = ""
    for ch in search_word:
        prefix += ch
        suggestions = trie.autocomplete(prefix, limit=None)
        suggestions.sort()
        result.append(suggestions[:3])
    return result
```

- **Approach:** Insert all products into a Trie once — O(total characters across products). For each prefix length as the user types, run autocomplete and take the smallest 3.
- **Alternative (Brute Force):** For each prefix, filter the full product list with `startswith()` and sort — O(len(search_word) × N × L). Works for small inputs but doesn't scale.
- **When to use Trie:** Products list is large and queried repeatedly (real search engines); Trie amortizes prefix cost.
- **When NOT to use Trie:** One-off, tiny product lists — sorting + binary search on the list directly (via `bisect`) can be simpler and just as fast.

### 6.4 Dictionary Search / Word Search II (Grid + Trie)

**Problem:** Given an `m x n` board of letters and a list of words, find all words that can be constructed from adjacent cells (no cell reused within a single word).

**Approach:** Build a Trie of all target words. DFS from every cell on the board, walking the Trie in lockstep with board moves — this prunes impossible paths immediately (if the current cell's letter isn't a valid Trie edge, stop early) instead of independently searching for each word.

```python
def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end_of_word = True
        node.word = w   # store the full word at terminal nodes for easy collection

    rows, cols = len(board), len(board[0])
    found = set()

    def dfs(r, c, node):
        ch = board[r][c]
        child = node.children.get(ch)
        if child is None:
            return
        if child.is_end_of_word:
            found.add(child.word)

        board[r][c] = "#"   # mark visited
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, child)
        board[r][c] = ch     # backtrack

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return list(found)
```

**Line-by-line explanation:**

- Build one shared Trie of all words upfront — O(total characters in `words`).
- `node.word = w` at terminal nodes avoids reconstructing the string from the DFS path.
- `dfs(r, c, node)`: at each board cell, check if the current letter is a valid next-edge in the Trie (`node.children.get(ch)`). If not, prune immediately — this is the key efficiency win over searching each word independently.
- Mark the cell visited using a sentinel `"#"`, recurse into the 4 neighbors, then backtrack (restore the original letter) — standard grid backtracking.

- **Time Complexity:** O(rows × cols × 4^L) worst case (L = max word length), but the Trie pruning makes real-world performance far better than searching each word independently (O(words × rows × cols × 4^L)).
- **Space Complexity:** O(total characters in words) for the Trie + O(L) recursion stack.
- **Common Mistake:** Rebuilding a fresh Trie or re-scanning the word list per board cell — always build the Trie **once**, shared across all DFS calls.

### 6.5 Word Dictionary (Wildcard `.` Search)

**Problem:** Support `addWord(word)` and `search(word)` where `search` may contain `.` to match any single character.

```python
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end_of_word
            ch = word[i]
            if ch == '.':
                return any(dfs(child, i + 1) for child in node.children.values())
            child = node.children.get(ch)
            return child is not None and dfs(child, i + 1)
        return dfs(self.root, 0)
```

**Explanation:** identical Trie insert as always. `search` uses DFS instead of a simple loop because `.` requires **branching into every child** at that position — a plain iterative walk can't express "try all possibilities". `any(...)` short-circuits as soon as one branch succeeds.

- **Time Complexity:** O(26^(number of dots) × L) worst case (all dots), O(L) best case (no dots).
- **Space Complexity:** O(L) recursion depth.

### 6.6 Replace Words

**Problem:** Given a dictionary of "roots" and a sentence, replace every word in the sentence with its shortest root from the dictionary (if any root is a prefix of the word).

```python
def replace_words(roots: list[str], sentence: str) -> str:
    trie = Trie()
    for root in roots:
        trie.insert(root)

    def shortest_root(word: str) -> str:
        node = trie.root
        prefix = []
        for ch in word:
            if ch not in node.children:
                break
            prefix.append(ch)
            node = node.children[ch]
            if node.is_end_of_word:
                return "".join(prefix)   # shortest root found — stop immediately
        return word   # no root matched

    return " ".join(shortest_root(w) for w in sentence.split())
```

**Explanation:** this is a direct application of Longest-Prefix-Match logic (Section 4.6), except we want the **shortest** matching root, so we return as soon as we hit the **first** `is_end_of_word` node while walking — no need to keep searching deeper.

- **Time Complexity:** O(total characters in roots) to build + O(total characters in sentence) to process.

### 6.7 Longest Common Prefix (LCP) via Trie

**Problem:** Given a list of strings, find their longest common prefix.

```python
def longest_common_prefix(strs: list[str]) -> str:
    trie = Trie()
    for s in strs:
        trie.insert(s)

    prefix = []
    node = trie.root
    while (len(node.children) == 1        # single-child chain = still common
           and not node.is_end_of_word     # stop if a shorter string ends here
           and len(prefix) < len(min(strs, key=len))):
        ch = next(iter(node.children))
        prefix.append(ch)
        node = node.children[ch]
    return "".join(prefix)
```

**Explanation:** the LCP of all strings corresponds exactly to the unbranched chain from the root — as soon as a node has more than one child (words diverge) or represents the end of one of the strings (a shorter string terminates), the common prefix stops growing.

- **Alternative (simpler, no Trie needed):** vertical character-by-character scanning across all strings, or divide-and-conquer, or sorting + comparing only the first and last strings. A Trie is **overkill** for this specific problem in practice, but it's commonly taught as a Trie exercise to reinforce the "single-child chain" intuition, which generalizes directly to Radix Tree compression (Section 5.3).

### 6.8 Stream Checker

**Problem:** Given a list of words, design a `query(letter)` that processes one character of a live stream at a time and returns `True` if any suffix of the stream so far (ending at the current character) matches a word in the dictionary.

```python
class StreamChecker:
    def __init__(self, words: list[str]):
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])   # insert REVERSED words
        self.stream = []
        self.max_len = max(len(w) for w in words)

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        if len(self.stream) > self.max_len:
            self.stream.pop(0)

        node = self.trie.root
        for ch in reversed(self.stream):     # walk the stream BACKWARDS
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_end_of_word:
                return True
        return False
```

**Explanation:** since we care about **suffixes** of the stream matching **whole words**, the trick is to insert every word **reversed** into the Trie. Then, checking "does some suffix of the stream match a word" becomes "does the stream, read backwards from the current character, match some reversed word from the start" — an ordinary prefix-match on the reversed Trie.

- **Time Complexity:** O(max word length) per query.
- **Space Complexity:** O(total characters in words) for the Trie + O(max word length) for the stream buffer.

### 6.9 Phone Directory / Contact List / Spell Checker / Search Suggestions

These four are essentially the same pattern applied to different domains — all are **autocomplete variants** (Section 4.7):

| Application | What's inserted | What's queried |
|---|---|---|
| Phone Directory | Contact names | Partial name typed → matching contacts |
| Contact List | Names/numbers | Prefix as user types |
| Spell Checker | Dictionary words | Exact match (misspelling detection) + nearby suggestions (often combined with edit distance, outside pure-Trie scope) |
| Search Suggestions | Query logs / product names | Prefix typed → ranked suggestions |

> **Interview Tip:** If you see any of these four framed as a "system design"-flavored coding question, the expected answer is: build a Trie over the corpus, and implement autocomplete via DFS-from-prefix-node exactly as in Section 4.7 — optionally augmented with frequency counts per node for ranking.

### 6.10 Maximum XOR of Two Numbers in an Array

**Problem:** Given an array of integers, find the maximum XOR of any two elements.

```python
def find_maximum_xor(nums: list[int]) -> int:
    bit_length = max(nums).bit_length()
    binary_trie = BinaryTrie(bit_length=bit_length)
    max_result = 0
    for num in nums:
        if binary_trie.root.children != [None, None]:   # trie non-empty
            max_result = max(max_result, binary_trie.max_xor_with(num))
        binary_trie.insert(num)
    return max_result
```

Uses the `BinaryTrie` class from Section 5.6. Each number is inserted, and (except for the very first) queried against all previously-inserted numbers via the greedy bit-toggling traversal — giving the best XOR partner in O(bit_length) instead of the brute-force O(N²) pairwise comparison.

- **Brute Force:** O(N²) — compare every pair.
- **Binary Trie:** O(N × bit_length) — a massive improvement for large N.

### 6.11 Maximum XOR With an Element From Array (Queries with Limit)

**Problem:** For each query `(x, m)`, find the maximum XOR of `x` with any array element `<= m`.

**Approach:** Sort array elements and queries both by the limit `m`. Process queries in increasing order of `m`, inserting array elements into the Binary Trie only once they are `<= m` (two-pointer style), then answer each query with `max_xor_with(x)`. This combines the Binary Trie pattern with **offline query sorting** — a common competitive-programming trick when queries have an upper-bound constraint.

- **Time Complexity:** O((N + Q) log(N + Q) + (N + Q) × bit_length).

### 6.12 IP Routing (Longest Prefix Match)

Real router hardware stores routing table entries as **binary prefixes** (e.g., `192.168.0.0/16`) in a Binary Trie / Radix Tree. Given a destination IP, the router walks the trie bit-by-bit and returns the **longest matching prefix** — exactly the algorithm in Section 4.6, but operating on binary strings instead of alphabetic ones. This is why the "Longest Prefix Match" pattern is not just academic — it's literally how the internet's core routers forward every packet.


---

## 7. Advanced Trie Concepts

### 7.1 Compressed Trie / Radix Tree — Implementation Sketch

A simplified Python sketch showing edge-substring compression (full production Radix Trees handle splitting on insert, which is significantly more code):

```python
class RadixNode:
    __slots__ = ("children", "is_end_of_word")
    def __init__(self):
        self.children = {}   # maps a SUBSTRING (not single char) -> RadixNode
        self.is_end_of_word = False

def radix_insert(root: RadixNode, word: str) -> None:
    node = root
    remaining = word
    while remaining:
        matched_edge = None
        for edge in node.children:
            common = _common_prefix_len(edge, remaining)
            if common > 0:
                matched_edge = edge
                break
        if matched_edge is None:
            # no overlapping edge: create a brand-new edge for the whole remainder
            new_node = RadixNode()
            new_node.is_end_of_word = True
            node.children[remaining] = new_node
            return

        common = _common_prefix_len(matched_edge, remaining)
        if common < len(matched_edge):
            # SPLIT the existing edge at the point of divergence
            old_child = node.children.pop(matched_edge)
            split_node = RadixNode()
            split_node.children[matched_edge[common:]] = old_child
            node.children[matched_edge[:common]] = split_node
            node = split_node
        else:
            node = node.children[matched_edge]
        remaining = remaining[common:]
    node.is_end_of_word = True

def _common_prefix_len(a: str, b: str) -> int:
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i
```

**Why splitting is necessary:** if the tree already has an edge `"omanus"` and you insert `"omulus"`, the shared prefix `"om"` must be factored out into its own node, with `"anus"` and `"ulus"` becoming two separate child edges. This splitting logic is what makes Radix Tree insertion meaningfully more complex than Standard Trie insertion — but it is also what keeps node count proportional to branching points, not total characters.

### 7.2 Double Array Trie (Overview)

A **Double Array Trie (DAT)** represents the entire Trie using **two parallel integer arrays** (`base[]` and `check[]`) instead of node objects with pointers. Each state transition is computed as `base[s] + c` (an arithmetic index into the array), and `check[]` validates that the transition is legitimate. This gives Trie-like functionality with **array-level cache locality and minimal memory** (no per-node object/pointer overhead), at the cost of much more complex construction logic (often requiring relocation of `base` values when collisions occur). Used in production systems like **MeCab** (Japanese morphological analyzer) and **Darts** (Double-ARray Trie System). This is implementation-heavy and rarely expected to be written from scratch in interviews — awareness of its existence and trade-offs is what's typically tested.

### 7.3 DAWG — Directed Acyclic Word Graph (Overview)

A **DAWG** further compresses a Trie by merging not just chains (like a Radix Tree) but **identical suffixes** across different words — turning the tree into a general directed acyclic graph. For example, `"tap"` and `"cap"` might share their `"ap*"` suffix subtree entirely as a single shared node, rather than duplicating it. This yields the most memory-efficient representation of a word set at the cost of significant construction complexity (typically built incrementally with suffix-merging via minimization algorithms). Used in advanced spell-checkers and Scrabble-move-generation engines.

### 7.4 Persistent Trie — Deeper Look

Building on Section 5.8, here's a Python sketch of a persistent Binary Trie supporting versioned max-XOR queries (a well-known competitive programming pattern: "max XOR pair with index in range [l, r]"):

```python
class PersistentNode:
    __slots__ = ("children",)
    def __init__(self, children=None):
        self.children = children or [None, None]

def persistent_insert(prev_root, num, bit_length=32):
    new_root = PersistentNode(list(prev_root.children)) if prev_root else PersistentNode()
    node, prev_node = new_root, prev_root
    for i in range(bit_length - 1, -1, -1):
        bit = (num >> i) & 1
        prev_child = prev_node.children[bit] if prev_node else None
        new_child = PersistentNode(list(prev_child.children)) if prev_child else PersistentNode()
        node.children[bit] = new_child
        node, prev_node = new_child, prev_child
    return new_root   # roots[] array stores one root per prefix-version
```

Only O(bit_length) new nodes are created per insert; every other subtree is **shared by reference** with the previous version. An array `roots[0..n]` then lets you query "max XOR using only elements inserted up to version `k`" in O(bit_length), enabling range-restricted queries via `roots[r] "minus" roots[l-1]`-style logic (implemented by tracking per-node insertion counts).

### 7.5 Suffix Automaton (Brief Mention)

A **Suffix Automaton** is the minimal DFA (deterministic finite automaton) recognizing all substrings of a string — conceptually the DAWG idea (7.3) applied specifically to *all suffixes* of one string. It supports O(1) amortized substring-existence checks after O(n) construction. Considered a natural "next topic" after mastering Tries and Suffix Tries, but its construction algorithm is a separate, advanced topic outside this handbook's Trie-only scope.

---

## 8. Applications

### 8.1 Search Engines

Search engines use Trie-like (usually DAWG or compressed-trie hybrid, at massive scale) structures to power **query autocomplete** — suggesting completions as you type, ranked by historical query frequency stored per terminal node.

### 8.2 Auto-complete in IDEs

Code editors (VS Code, PyCharm, etc.) use Tries over the symbol table (variable names, function names, keywords) of your current file/project to power instant code-completion dropdowns as you type an identifier prefix.

### 8.3 Spell Checkers

A Trie of a dictionary provides instant "is this a valid word?" checks. Combined with edit-distance algorithms (outside pure-Trie scope), Tries also power "did you mean...?" suggestion engines by exploring nearby Trie paths within a bounded edit distance.

### 8.4 Contact Search / Phone Directories

Contact apps and telecom directory services use Tries to instantly filter contacts as digits or letters are typed on a keypad (T9 predictive text is a classic Trie + phone-keypad-mapping application).

### 8.5 IP Routing Tables

Routers store network prefixes (e.g., `10.0.0.0/8`, `10.1.0.0/16`) in Binary/Radix Tries and perform **Longest Prefix Match** (Section 6.12) on every incoming packet's destination address to decide the next hop — a Trie operation happening billions of times per second across the global internet backbone.

### 8.6 DNA / Protein Sequence Matching

Bioinformatics tools build Suffix Tries/Trees over genomic sequences to answer "does this substring/pattern occur in the genome?" and "what are the repeated motifs?" in time proportional to the pattern length, independent of genome size (which can be billions of characters).

### 8.7 Word Games

Scrabble/Boggle solvers use a Trie (often a DAWG in production engines) over the full dictionary to validate words during board-traversal search (exactly the pattern in Section 6.4's Word Search II), pruning any path the instant it stops matching a valid dictionary prefix.

---

## 9. Problem Recognition

### 9.1 Recognition Flowchart

```
                     ┌─────────────────────────────┐
                     │ Does the problem involve a  │
                     │ SET of strings queried by    │
                     │ PREFIX, not just exact match?│
                     └──────────────┬───────────────┘
                                    │ YES
                                    ▼
                  ┌─────────────────────────────────┐
                  │ Keywords: "starts with",         │
                  │ "prefix", "autocomplete",         │
                  │ "dictionary", "word search",      │
                  │ "longest common prefix"?          │
                  └──────────────┬────────────────────┘
                                 │ YES
                                 ▼
                     ┌───────────────────────┐
                     │   USE A TRIE           │
                     └───────────────────────┘

                                 │ NO (numeric, XOR-related)
                                 ▼
                  ┌─────────────────────────────────┐
                  │ Keywords: "maximum XOR",          │
                  │ "XOR pair", "binary representation"│
                  └──────────────┬────────────────────┘
                                 │ YES
                                 ▼
                     ┌───────────────────────┐
                     │  USE A BINARY TRIE     │
                     └───────────────────────┘
```

### 9.2 Interview Clues Checklist

| Clue in problem statement | Suggests |
|---|---|
| "Implement a data structure that supports insert/search/startsWith" | Standard Trie — textbook signal |
| "autocomplete", "search suggestions" | Trie + DFS collection |
| "dictionary of words", multiple words share letters | Trie (shared prefix storage) |
| Wildcard character (`.`, `*`) in search queries | Trie + DFS branching |
| "word can be formed from a grid of letters" | Trie + backtracking on grid |
| "maximum XOR of two numbers" | Binary Trie |
| "longest prefix" / "IP routing" / networking context | Binary Trie / Radix Tree, Longest Prefix Match |
| Extremely large alphabet, but very sparse branching | Consider Compressed Trie / Radix Tree for memory |
| Repeated substring / suffix queries on ONE string | Suffix Trie / Suffix Automaton (beyond this handbook) |

### 9.3 Trie vs Hash Map

| Criterion | Trie | Hash Map |
|---|---|---|
| Exact match lookup | O(L) | O(L) average (hashing cost) |
| Prefix query (`startsWith`) | O(L) | O(N × L) (must scan all keys) |
| Memory | Higher (many small nodes) | Lower (one entry per string) |
| Sorted iteration | Free (DFS) | Requires explicit `sorted()` |
| Best for | Prefix-heavy workloads | Exact-match-only workloads |

> **Rule of thumb:** if the word "prefix" never appears in the problem and you only ever need exact-match lookups, a hash set/dict is simpler and just as fast — don't reach for a Trie by default.

### 9.4 Trie vs BST

| Criterion | Trie | BST (of strings) |
|---|---|---|
| Comparison unit | Single character per level | Full string per comparison |
| Search cost | O(L) | O(L × log N) (L per comparison, log N comparisons) |
| Shared prefixes | Explicitly stored once | Not exploited at all |
| Best for | Many strings sharing prefixes | General ordered string sets without prefix overlap requirements |

### 9.5 Trie vs Binary Search (on a sorted list of strings)

Binary search on a sorted array of strings gives O(L × log N) per query (each of the log N comparisons costs O(L) to compare full strings) — asymptotically worse than a Trie's O(L), especially as N grows. However, for **static, rarely-queried datasets**, binary search avoids the memory overhead and construction cost of building a Trie — another instance of the general "build cost vs query cost" trade-off.

---

## 10. Optimization

### 10.1 Hash Map → Trie (When and Why)

Migrate from a hash-map-of-strings to a Trie when your workload shifts from **pure exact-match** to including **any** prefix-based query (`startsWith`, autocomplete, longest-common-prefix). The migration cost is O(total characters) to rebuild, paid once, in exchange for O(L) prefix queries indefinitely after.

### 10.2 Recursive → Iterative

Convert recursive insert/search/delete to iterative loops (Sections 2.5–2.6, 4.4) when:
- Input strings can be very long (avoid `RecursionError`, default Python recursion limit is 1000).
- Micro-optimizing hot-path performance (function call overhead in Python is non-trivial).

### 10.3 Dictionary vs Array Nodes (Revisited)

Already detailed in Section 2.4. Rule of thumb: **default to dict**; switch to array **only** when you've confirmed a small, fixed alphabet AND profiling shows the dict's hashing overhead matters.

### 10.4 Memory Optimization Techniques

1. **`__slots__`** on node classes (Section 2.1) — eliminates per-instance `__dict__`, often the single biggest win.
2. **Path compression** (Radix Tree, Section 5.3/7.1) — collapses single-child chains, reducing node count from O(total characters) to O(branch points).
3. **Suffix sharing** (DAWG, Section 7.3) — merges identical subtrees, the most aggressive compression available.
4. **Lazy node creation** — never eagerly allocate empty child arrays/dicts (dictionary-based nodes naturally already do this — arrays don't, another point in favor of dicts for sparse data).
5. **Avoid storing redundant data per node** — don't cache the full word string at every node; reconstruct only when needed via DFS path tracking (Section 4.7).

### 10.5 Time Optimization Techniques

1. **Precompute counts** (`words_below`, Section 4.5) to answer count-queries in O(L) instead of O(subtree size).
2. **Offline query processing** for constrained queries (Section 6.11) — sort queries to amortize Trie construction across them.
3. **Early termination** — return as soon as an answer is determined (e.g., Replace Words returns at the first `is_end_of_word` hit, Section 6.6) rather than continuing to traverse unnecessarily.
4. **Iterative traversal** avoids Python function-call overhead versus recursive DFS in performance-critical paths.


---

## 11. Interview Preparation

### 11.1 Standard Templates to Memorize

**Template 1 — Basic Trie (Insert/Search/StartsWith):**

```python
class TrieNode:
    __slots__ = ("children", "is_end_of_word")
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

**Template 2 — Binary Trie (Max XOR):** see Section 5.6.

**Template 3 — Wildcard Search (DFS branching):** see Section 6.5.

### 11.2 Problems by Difficulty

| Difficulty | Problem | Platform | Pattern |
|---|---|---|---|
| Easy | Implement Trie (Prefix Tree) | LeetCode 208 | Basic insert/search/startsWith |
| Easy | Longest Common Prefix | LeetCode 14 | LCP (Section 6.7) |
| Medium | Design Add and Search Words Data Structure | LeetCode 211 | Wildcard DFS |
| Medium | Replace Words | LeetCode 648 | Shortest prefix match |
| Medium | Map Sum Pairs | LeetCode 677 | Trie + prefix sum |
| Medium | Search Suggestions System | LeetCode 1268 | Autocomplete |
| Medium | Stream of Characters | LeetCode 1032 | Reversed-Trie suffix match |
| Medium | Maximum XOR of Two Numbers in an Array | LeetCode 421 | Binary Trie |
| Hard | Word Search II | LeetCode 212 | Trie + grid backtracking |
| Hard | Palindrome Pairs | LeetCode 336 | Trie + palindrome checks |
| Hard | Maximum XOR With an Element From Array | LeetCode 1707 | Binary Trie + offline queries |
| Hard | Concatenated Words | LeetCode 472 | Trie/DP hybrid |

### 11.3 Company-Wise Frequently Asked (General Trends)

| Company | Commonly Tests |
|---|---|
| Google | Word Search II, autocomplete/search-suggestion system design |
| Amazon | Implement Trie, Replace Words, prefix-based product search |
| Microsoft | Add and Search Words, Longest Common Prefix |
| Meta | Word Search II, Maximum XOR problems |
| Bloomberg | Implement Trie, autocomplete features |

> **Note:** Company-specific patterns shift over time; treat this table as a general guide, not a guarantee — always check current community-reported interview experiences closer to your interview date.

### 11.4 Blind 75 / NeetCode Trie Coverage

The Blind 75 and NeetCode 150 lists typically include these Trie problems: **Implement Trie (Prefix Tree)**, **Design Add and Search Words Data Structure**, and **Word Search II**. Mastering these three, plus the Binary Trie pattern (Section 5.6/6.10, common in NeetCode's "Bit Manipulation" or "Advanced" lists depending on version), covers the large majority of Trie questions across major prep lists.

### 11.5 Interview Tricks & Tactics

1. **Always clarify the alphabet** ("lowercase only? mixed case? unicode?") before choosing dict vs array nodes — shows engineering judgement.
2. **State the "why" before coding** — briefly explain why a Trie beats a hash map for this specific problem (prefix operations) before diving into code.
3. **Draw the Trie on the whiteboard/notes** for the given example — interviewers consistently reward visual reasoning (see all the ASCII diagrams throughout this handbook as a model).
4. **Mention complexity proactively** — state O(L) search / O(total chars) space unprompted; don't wait to be asked.
5. **Offer the optimization path** — mention that a Radix Tree could reduce memory further if the interviewer probes on space, without over-engineering the initial solution.

---

## 12. Python Tips

### 12.1 `dict` — The Backbone of Trie Nodes

Python's `dict` is a hash table with O(1) average-case get/set — this is why dict-based Trie nodes achieve the same O(1)-per-character cost as array-based nodes, without needing to know the alphabet size upfront.

### 12.2 `defaultdict` for Terse Contest Code

```python
from collections import defaultdict

def Trie(): return defaultdict(Trie)

root = Trie()
node = root
for ch in "cat":
    node = node[ch]
node['#'] = True   # sentinel end-of-word marker
```

Fast to write, ideal for competitive programming (Section 2.7), but sacrifices some clarity — avoid in interviews unless speed is explicitly prioritized over readability.

### 12.3 `dataclass` for Cleaner Node Definitions

```python
from dataclasses import dataclass, field

@dataclass
class TrieNode:
    children: dict = field(default_factory=dict)
    is_end_of_word: bool = False
```

Equivalent to the manual `__init__` version but more concise. **Caveat:** `@dataclass` does not automatically add `__slots__` unless you pass `slots=True` (Python 3.10+) — do so explicitly for memory-critical code: `@dataclass(slots=True)`.

### 12.4 Recursion in Python — Practical Limits

Python's default recursion limit is **1000** (`sys.getrecursionlimit()`). Any recursive Trie operation on strings longer than ~1000 characters (e.g., long DNA sequences) will raise `RecursionError` unless you either convert to iteration or explicitly raise the limit with `sys.setrecursionlimit(...)` (risky — can crash the interpreter on deep recursion by exhausting the actual C call stack).

### 12.5 Generators for Lazy Word Enumeration

Instead of building a full `list` of all matching words (Section 4.7), a generator avoids materializing potentially huge result sets in memory:

```python
def autocomplete_gen(node, path):
    if node.is_end_of_word:
        yield "".join(path)
    for ch, child in sorted(node.children.items()):
        path.append(ch)
        yield from autocomplete_gen(child, path)
        path.pop()
```

Useful when only the **first few** results are needed (e.g., `itertools.islice(autocomplete_gen(...), 3)`) without wastefully enumerating the entire subtree.

### 12.6 Performance Tips

- Prefer `node.children.setdefault(ch, TrieNode())` over explicit `if/else` — marginally faster and more idiomatic.
- Avoid rebuilding the Trie repeatedly inside a loop — build once, query many times.
- Use `__slots__` universally on node classes in performance-sensitive contexts (Section 2.1, 2.9, 10.4).
- Batch-insert during a dedicated construction phase; treat as read-mostly afterward when possible (enables further compression optimizations).

### 12.7 Common Python Pitfalls

1. **Mutable default arguments:** never write `def __init__(self, children={})` — this shares the *same* dict across all instances. Always use `field(default_factory=dict)` (dataclass) or set inside `__init__` explicitly.
2. **Forgetting to backtrack** mutable path lists in DFS (`path.pop()`) — leads to corrupted results across recursive branches.
3. **Confusing `.get(ch)` returning `None` vs `ch in dict`** — both work but mixing styles inconsistently in the same function invites bugs; pick one idiom and stick to it.
4. **String immutability overhead** — repeatedly doing `prefix = prefix + ch` in a loop is O(L²) overall due to string immutability; use a `list` and `"".join()` at the end instead (as done throughout this handbook's autocomplete code).

---

## 13. Common Mistakes

### 13.1 Missing End-of-Word Marker

Checking `len(node.children) == 0` instead of a dedicated `is_end_of_word` flag to determine "is this a complete word" — breaks the instant one word is a prefix of another (e.g., "car" inside "cart"). **Always use an explicit marker** (Section 3.5).

### 13.2 Incorrect Delete Logic

Deleting nodes without checking both **(a) no children remain** and **(b) not itself a different word's end** — destroys sibling words that share the deleted word's prefix path. Revisit the full correct algorithm in Section 4.4.

### 13.3 Prefix vs Complete Word Confusion

The single most common bug: writing `search()` without checking `is_end_of_word` (making it behave like `startsWith`), or writing `startsWith()` while checking `is_end_of_word` (making it fail on partial prefixes that are also complete words elsewhere). Always double check which of the two you intend at the final `return` statement (Sections 4.2 vs 4.3).

### 13.4 Duplicate Insertions

Inserting the same word twice is harmless correctness-wise (idempotent — same nodes get reused, the end marker just gets set to `True` again) but **breaks counting logic** if you're using a `words_below` counter (Section 4.5) without checking for duplicates first — the count will be inflated. Decide explicitly whether your Trie is a **set** (dedupe) or a **multiset** (allow counted duplicates) semantics upfront.

### 13.5 Node Pruning Mistakes

Pruning a node's children dict while iterating over it directly (`for ch in node.children: del node.children[ch]`) raises `RuntimeError: dictionary changed size during iteration` in Python. Always collect keys to delete into a separate list first, or restructure as the bottom-up recursive delete shown in Section 4.4 (which never iterates-while-mutating).

### 13.6 Dictionary Mutation Errors

Similarly, never mutate `node.children` inside a `for ch, child in node.children.items()` loop (as might be tempting during compression/merging operations) — always build a new dict or collect changes and apply them after the loop completes.

### 13.7 Memory Inefficiency

Forgetting `__slots__`, storing full word strings redundantly at every node, or eagerly pre-allocating 26-element arrays for a Unicode-heavy or highly sparse dataset — all avoidable memory blowups covered in Sections 2.9 and 10.4.


---

## 14. Cheat Sheets

### 14.1 Trie Operations Cheat Sheet

| Operation | Time | Space | One-line summary |
|---|---|---|---|
| Insert | O(L) | O(L) worst case | Walk/create edges, mark end |
| Search (exact) | O(L) | O(1) | Walk edges, check `is_end_of_word` |
| StartsWith | O(L) | O(1) | Walk edges, path existence only |
| Delete | O(L) | O(L) recursion | Bottom-up prune if childless & not another word's end |
| Count words w/ prefix | O(L) or O(1) with counter | O(1) | Traverse then DFS-count, or precomputed `words_below` |
| Longest Prefix Match | O(L) | O(L) | Track last `is_end_of_word` seen while walking |
| Autocomplete | O(L + K) | O(K) | Traverse to prefix, DFS-collect all words below |

### 14.2 Complexity Table (Full)

| Structure | Build | Search | Insert | Delete | Space |
|---|---|---|---|---|---|
| Standard Trie | O(total chars) | O(L) | O(L) | O(L) | O(total chars) |
| Compressed Trie (Radix) | O(total chars) | O(L) | O(L) (may split edge) | O(L) | O(branch points) |
| Ternary Search Tree | O(total chars) | O(L·logΣ) avg | O(L·logΣ) avg | O(L·logΣ) avg | O(total chars), lower constant |
| Binary Trie | O(N·bits) | O(bits) | O(bits) | O(bits) | O(N·bits) |
| Hash Set (comparison) | O(total chars) | O(L) | O(L) | O(L) | O(total chars), no prefix support |

### 14.3 Pattern Recognition Guide (Quick Reference)

| See this... | Do this |
|---|---|
| "startsWith" / prefix set membership | Standard Trie |
| Autocomplete / suggestions | Trie + DFS collect (sorted) |
| Wildcard `.` in search | Trie + DFS branching |
| Grid + word list | Trie + backtracking |
| "Maximum XOR" | Binary Trie |
| IP / networking / longest matching prefix | Binary Trie / Radix Tree |
| Huge sparse dataset, memory-constrained | Compressed Trie / TST / DAWG |

### 14.4 Python Syntax Cheat Sheet

```python
node.children.setdefault(ch, TrieNode())      # insert-or-get in one line
node.children.get(ch)                         # safe lookup, returns None if absent
ch in node.children                           # existence check
sorted(node.children.items())                 # lexicographic child order
"".join(path_list)                            # efficient string building from list
```

### 14.5 Trie Formula Sheet

- Number of nodes (Standard Trie, worst case, no shared prefixes) = **Σ (length of each word)**
- Number of nodes (best case, maximal sharing) ≈ **size of the union of all prefixes** (≤ total chars)
- Binary Trie depth = **fixed bit-width** (commonly 32 or 64), independent of value magnitude
- Radix Tree nodes ≈ **O(number of branching points)**, always ≤ Standard Trie's node count

### 14.6 Decision Tree — Which Trie Variant?

```
Need prefix queries on strings?
├── NO  -> use hash set/dict
└── YES
    ├── Alphabet small & fixed, dense branching -> Standard Trie (array or dict)
    ├── Alphabet large/unicode, or sparse branching -> Compressed Trie (Radix) or TST
    ├── Numbers, need max-XOR / bitwise ops -> Binary Trie
    ├── Need versioned/historical queries -> Persistent Trie
    └── Need maximal memory compression, many shared suffixes -> DAWG
```

---

## 15. Practice Problems

### 15.1 Basics

| # | Problem | Platform | Difficulty | Link |
|---|---|---|---|---|
| 1 | Implement Trie (Prefix Tree) | LeetCode 208 | Medium | leetcode.com/problems/implement-trie-prefix-tree |
| 2 | Implement Trie II (Prefix Tree) | LeetCode 1804 | Medium | leetcode.com/problems/implement-trie-ii-prefix-tree |
| 3 | Trie | GeeksforGeeks | Basic | geeksforgeeks.org/trie-insert-and-search |

### 15.2 Insert / Search

| # | Problem | Platform | Difficulty | Link |
|---|---|---|---|---|
| 4 | Design Add and Search Words Data Structure | LeetCode 211 | Medium | leetcode.com/problems/design-add-and-search-words-data-structure |
| 5 | Search Word | HackerRank | Medium | hackerrank.com/challenges/contacts (contact search variant) |

### 15.3 Prefix Search

| # | Problem | Platform | Difficulty | Link |
|---|---|---|---|---|
| 6 | Longest Common Prefix | LeetCode 14 | Easy | leetcode.com/problems/longest-common-prefix |
| 7 | Replace Words | LeetCode 648 | Medium | leetcode.com/problems/replace-words |
| 8 | Short Encoding of Words | LeetCode 820 | Medium | leetcode.com/problems/short-encoding-of-words |

### 15.4 Auto-complete

| # | Problem | Platform | Difficulty | Link |
|---|---|---|---|---|
| 9 | Search Suggestions System | LeetCode 1268 | Medium | leetcode.com/problems/search-suggestions-system |
| 10 | Contacts | HackerRank | Medium | hackerrank.com/challenges/contacts |

### 15.5 Dictionary

| # | Problem | Platform | Difficulty | Link |
|---|---|---|---|---|
| 11 | Map Sum Pairs | LeetCode 677 | Medium | leetcode.com/problems/map-sum-pairs |
| 12 | Stream of Characters | LeetCode 1032 | Hard | leetcode.com/problems/stream-of-characters |

### 15.6 Word Search / Grid

| # | Problem | Platform | Difficulty | Link |
|---|---|---|---|---|
| 13 | Word Search II | LeetCode 212 | Hard | leetcode.com/problems/word-search-ii |
| 14 | Boggle (Find all possible words on a board) | GeeksforGeeks | Hard | geeksforgeeks.org/boggle-find-possible-words-board-characters |

### 15.7 Longest Common Prefix Variants

| # | Problem | Platform | Difficulty | Link |
|---|---|---|---|---|
| 15 | Longest Common Prefix using Trie | GeeksforGeeks | Medium | geeksforgeeks.org/longest-common-prefix-using-trie |

### 15.8 Binary Trie / XOR Problems

| # | Problem | Platform | Difficulty | Link |
|---|---|---|---|---|
| 16 | Maximum XOR of Two Numbers in an Array | LeetCode 421 | Medium | leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array |
| 17 | Maximum XOR With an Element From Array | LeetCode 1707 | Hard | leetcode.com/problems/maximum-xor-with-an-element-from-array |
| 18 | Maximum XOR Queries | Codeforces | Medium–Hard | codeforces.com (search "XOR trie") |
| 19 | Maximum Subarray XOR | InterviewBit | Medium | interviewbit.com/problems/maximum-subarray-xor |

### 15.9 Advanced Trie

| # | Problem | Platform | Difficulty | Link |
|---|---|---|---|---|
| 20 | Palindrome Pairs | LeetCode 336 | Hard | leetcode.com/problems/palindrome-pairs |
| 21 | Concatenated Words | LeetCode 472 | Hard | leetcode.com/problems/concatenated-words |
| 22 | Word Break II | LeetCode 140 | Hard | leetcode.com/problems/word-break-ii |
| 23 | Prefix and Suffix Search | LeetCode 745 | Hard | leetcode.com/problems/prefix-and-suffix-search |
| 24 | Number of Matching Subsequences | LeetCode 792 | Medium | leetcode.com/problems/number-of-matching-subsequences |
| 25 | String Matching (CSES) | CSES | Medium | cses.fi/problemset/task/1753 |

> **Note:** Always verify current problem links and difficulty ratings directly on each platform, as these occasionally get renumbered or re-rated.

---

## 16. Final Revision

### 16.1 One-Page Notes

- A Trie stores strings by **decomposing them into shared character paths**, trading memory for O(L) prefix-query speed.
- **Dictionary-based nodes** are the default interview-safe choice; **arrays** only for small, fixed alphabets.
- **Never forget the `is_end_of_word` marker** — it is the only way to distinguish a complete word from a mere prefix path.
- **Delete requires bottom-up pruning**, checking both "no children" and "not another word's end" before removing a node.
- **Binary Tries** solve XOR-maximization problems via greedy opposite-bit traversal.
- **Compressed Tries (Radix Trees)** collapse single-child chains into substring-labeled edges — critical for sparse, large-scale datasets like IP routing tables.
- **Autocomplete = traverse to prefix node, then DFS-collect**, sorting children for lexicographic order.

### 16.2 Mind Map (ASCII)

```
                                TRIE
                                 |
      ┌───────────┬──────────────┼───────────────┬───────────────┐
   Fundamentals  Operations    Types           Patterns       Advanced
      |              |            |                |               |
   root,node    insert/search  Standard        autocomplete    Radix Tree
   edge,prefix  startsWith     Compressed      word search      DAWG
   end-marker   delete         TST             wildcard search  Persistent
   branching    count/LPM      Binary Trie     max XOR          Suffix Trie
   leaf         autocomplete   Suffix Trie     IP routing       Double Array
```

### 16.3 Recognition Flowchart (Repeated for Quick Recall)

See Section 9.1 — the two-question test: **(1) is it a set of strings queried by prefix? (2) is it numeric XOR-maximization?** covers the overwhelming majority of Trie interview problems.

### 16.4 Complexity Sheet (Repeated for Quick Recall)

See Section 14.2 for the full comparison table across Standard Trie, Radix Tree, TST, Binary Trie, and Hash Set.

### 16.5 Interview Cheat Sheet — Final Checklist

- [ ] Clarify alphabet size and case-sensitivity before choosing dict vs array nodes.
- [ ] State why a Trie beats a hash map for this specific problem (prefix operations) before coding.
- [ ] Use the standard template (Section 11.1) as your starting skeleton.
- [ ] Distinguish `search` (checks `is_end_of_word`) from `startsWith` (doesn't) explicitly in your explanation.
- [ ] For delete, mention the "prunable" bottom-up recursion explicitly.
- [ ] For grid/wildcard problems, build the Trie **once**, share it across all DFS calls.
- [ ] Proactively state time/space complexity.
- [ ] Mention Radix Tree / TST as a memory-optimization follow-up if asked "how would you optimize further?"

### 16.6 15-Minute Revision

1. Re-read Section 3 (Fundamentals) — root, node, edge, end-marker, shared prefix (3 min).
2. Re-type the standard Trie template from memory (Section 11.1) (5 min).
3. Re-derive the delete algorithm's two pruning conditions out loud (Section 4.4) (3 min).
4. Skim the Recognition Flowchart (Section 9.1) and Pattern Table (Section 6.1) (4 min).

### 16.7 1-Hour Revision

1. Re-implement Standard Trie (insert/search/startsWith) from scratch, dictionary-based (15 min).
2. Re-implement delete with pruning, dry-run it on a 3-word example by hand (15 min).
3. Re-implement Binary Trie + max-XOR-with query (15 min).
4. Solve (or re-solve) one problem each from Sections 15.4 (autocomplete), 15.6 (grid), and 15.8 (XOR) (15 min, pick the fastest one you can recall fully).

---

## FAQs

**Q: Is a Trie always better than a hash map for storing strings?**
A: No. Tries win specifically for prefix-based queries. For pure exact-match membership testing with no prefix requirements, a hash set is simpler, often more memory-efficient, and equally fast.

**Q: Why does my Trie's `search("car")` return `True` even though I only inserted `"cart"`?**
A: You likely forgot to check `is_end_of_word` in your `search` method — you're accidentally implementing `startsWith` logic. See Section 13.3.

**Q: When should I use a Ternary Search Tree instead of a standard dict-based Trie?**
A: When memory is tight and your alphabet is large or the branching factor per node is typically low (1–2 children) — TST's 3-pointer nodes are far cheaper than dict/array nodes in that regime. See Section 5.5.

**Q: How do Binary Tries relate to string Tries?**
A: They're the same core idea (branch on the "next symbol") applied to a fixed binary alphabet (bits 0/1) instead of a character alphabet — used specifically for numeric XOR-maximization problems. See Section 5.6.

**Q: Do I need to implement a Radix Tree from scratch in interviews?**
A: Rarely as the primary ask, but you should be able to explain the concept (edge = substring, not single character) and mention it as a memory-optimization follow-up. See Section 5.3 and 7.1.

**Q: What's the difference between a Trie and a Suffix Trie?**
A: A Trie stores whole words (root-to-node = a prefix of one stored word). A Suffix Trie stores **every suffix of a single string**, enabling substring (not just prefix) queries. See Section 5.7.

---

