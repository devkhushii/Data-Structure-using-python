# The Complete Python String Handbook
### From First Principles to FAANG Interviews and Competitive Programming

> *"A string is not just a sequence of characters. It is a data structure, a protocol, and a puzzle — all at once."*

---


## Table of Contents

[**Chapter 1 — Introduction to Strings**](#chapter-1--introduction-to-strings)

[**Chapter 2 — Python Strings**](#chapter-2--python-strings)


[**Chapter 3 — String Operations (Every Method)**](#chapter-3--string-operations-every-method)

[**Chapter 4 — String Patterns**](#chapter-4--string-patterns)


[**Chapter 5 — Substrings**](#chapter-5--substrings)


[**Chapter 6 — Palindromes**](#chapter-6--palindromes)


[**Chapter 7 — Pattern Matching**](#chapter-7--pattern-matching)


[**Chapter 8 — String Transformations**](#chapter-8--string-transformations)


[**Chapter 9 — Problem Recognition**](#chapter-9--problem-recognition)


[**Chapter 10 — Optimization Playbook**](#chapter-10--optimization-playbook)


[**Chapter 11 — Interview Preparation**](#chapter-11--interview-preparation)


[**Chapter 12 — Python String Tips & Internals**](#chapter-12--python-string-tips--internals)


[**Chapter 13 — Common Mistakes**](#chapter-13--common-mistakes)


[**Chapter 14 — Cheat Sheets**](#chapter-14--cheat-sheets)


[**Chapter 15 — Practice Problems**](#chapter-15--practice-problems-categorized)

[**Chapter 16 — Final Revision**](#chapter-16--final-revision)


---

# Chapter 1 — Introduction to Strings

**Learning Objectives:** Understand what a string fundamentally is, how computers store text, and why strings deserve their own chapter in every CS curriculum.
**Prerequisites:** None.
**Estimated Reading Time:** 20 minutes
**Difficulty Level:** Beginner
**Real-World Applications:** Text editors, search engines, compilers, DNA sequencing, networking protocols, file formats.
**Interview Relevance:** Low directly, but forms the mental model interviewers assume you already have.

## 1.1 What Is a String

### Definition
A **string** is an ordered, finite sequence of characters drawn from some alphabet (a character set), typically used to represent text.

### Why It Exists
Computers only understand numbers (bits). Humans communicate in text. Strings are the bridge — a standardized way to store, transmit, and manipulate textual data as sequences of numeric codes that are *interpreted* as characters.

### Intuition
Think of a string as a **train of connected boxcars**, where each boxcar holds exactly one character, and the boxcars are numbered starting from 0.

### Real-World Analogy
A string is like a **shelf of labeled boxes** in a library — each box (index) holds one letter, and the whole shelf, read left to right, spells a word or sentence.

### ASCII Diagram — Character Indexing
```
String:      H    E    L    L    O
Index:       0    1    2    3    4
            +----+----+----+----+----+
            | H  | E  | L  | L  | O  |
            +----+----+----+----+----+
```

### Negative Indexing Diagram
```
String:      H    E    L    L    O
Positive:    0    1    2    3    4
Negative:   -5   -4   -3   -2   -1
```

> **Note:** In Python, strings are sequences — they support indexing, slicing, iteration, and membership testing just like lists, but they are **immutable**.

## 1.2 History of String Representation

| Era | Representation | Notes |
|---|---|---|
| Early computing (1950s–60s) | Fixed-width character codes (6-bit BCD) | Very limited character sets |
| ASCII (1963) | 7-bit encoding, 128 characters | English-centric |
| Extended ASCII (1980s) | 8-bit, 256 characters | Added accented characters, symbols |
| Unicode (1991–present) | Variable-width, 1.1M+ code points | Universal character set |
| UTF-8 (1993) | Variable-width byte encoding of Unicode | Backward-compatible with ASCII, dominant on the web |

## 1.3 Character Encoding

### 1.3.1 ASCII
ASCII (American Standard Code for Information Interchange) maps 128 characters to integers 0–127 using 7 bits.

```python
print(ord('A'))   # 65
print(chr(65))     # 'A'
print(ord('a'))   # 97
```

> **Interview Tip:** `ord('a') - ord('A') == 32`. This fact is the backbone of many case-conversion and Caesar-cipher problems.

### 1.3.2 Unicode
Unicode assigns every character a unique **code point** (e.g., `U+0041` for 'A'), covering virtually every writing system in the world, plus emoji.

```python
print(ord('अ'))      # Devanagari letter - code point
print(ord('😀'))     # Emoji code point
```

### 1.3.3 UTF-8
A variable-length encoding of Unicode code points into 1–4 bytes. ASCII characters use exactly 1 byte, making UTF-8 backward compatible with ASCII. It is the dominant encoding on the web.

```python
s = "café"
print(s.encode('utf-8'))     # b'caf\xc3\xa9'  -> 'é' takes 2 bytes
print(len(s))                 # 4 (characters)
print(len(s.encode('utf-8'))) # 5 (bytes)
```

### 1.3.4 UTF-16
Encodes code points in 2 or 4 bytes. Used internally by Java, Windows, and JavaScript strings.

### 1.3.5 UTF-32
Fixed-width, 4 bytes per code point. Simple but memory-heavy.

| Encoding | Width | ASCII Compatible | Common Use |
|---|---|---|---|
| ASCII | 7-bit fixed | Yes | Legacy systems |
| UTF-8 | 1–4 bytes variable | Yes | Web, Python 3 source files, Linux |
| UTF-16 | 2 or 4 bytes | No | Windows, Java, JS internals |
| UTF-32 | 4 bytes fixed | No | Rare, simplicity over memory |

> **Warning:** `len()` in Python counts **code points**, not bytes and not grapheme clusters. A single visible emoji formed from multiple code points (e.g., a flag or a skin-toned emoji) may have `len() > 1`.

## 1.4 Why Strings Exist as a Data Type

Without a dedicated string type, every piece of text would need to be manually managed as an array of integers, with the programmer responsible for encoding/decoding, bounds tracking, and null-termination. Strings exist to:
- Provide safe, ergonomic text manipulation.
- Encapsulate encoding details.
- Enable language-level operations (concatenation, comparison, formatting).

## 1.5 Characteristics & Properties

- **Ordered:** Character positions matter.
- **Iterable:** Can be traversed character by character.
- **Immutable (in Python, Java, C#, JS):** Cannot be changed in place.
- **Indexable:** Supports O(1) random access by position.
- **Sequence type:** Supports slicing, concatenation, repetition, membership.

## 1.6 Advantages & Disadvantages

| Advantages | Disadvantages |
|---|---|
| O(1) indexing | Immutability makes repeated modification costly |
| Safe to share (immutable → no aliasing bugs) | Concatenation in a loop is O(n²) if done naively |
| Hashable (usable as dict keys) | Unicode/encoding bugs are easy to introduce |
| Rich built-in method support | Higher memory overhead per object than raw bytes |

## 1.7 Real-World Applications

- **Search engines** — indexing and matching text (inverted indices, tokenization).
- **Compilers/Interpreters** — lexical analysis (tokenizing source code).
- **Bioinformatics** — DNA/RNA/protein sequences are strings over a small alphabet.
- **Networking** — HTTP headers, URLs, JSON/XML payloads are strings.
- **Version control (git)** — diffing is fundamentally a string/sequence problem.
- **Data validation** — emails, passwords, phone numbers via pattern matching.

## 1.8 Immutable vs Mutable Strings

In Python, `str` is **immutable**: once created, its contents can never change. Every "modification" produces a **new** string object.

```python
s = "hello"
s2 = s.replace("h", "j")
print(s)   # "hello"  (unchanged)
print(s2)  # "jello"  (new object)
```

### ASCII Diagram — Immutability
```
s  ----> [ h e l l o ]   (id: 0x1000)
s2 ----> [ j e l l o ]   (id: 0x2000)   <- brand new object
```

> **Why immutability?** Safety (no accidental aliasing bugs), hashability (usable as dict/set keys), and thread-safety (no locks needed for read-only sharing).

If you need mutability, use a `list` of characters, `bytearray`, or `io.StringIO`, and convert back with `''.join(...)` when done.

## 1.9 Common Misconceptions

| Misconception | Reality |
|---|---|
| "Strings are arrays of chars in Python" | Python has no separate `char` type — a "character" is just a length-1 `str`. |
| "`s[0] = 'x'` works like in C" | Raises `TypeError: 'str' object does not support item assignment`. |
| "`len(s)` gives byte count" | It gives the number of Unicode code points, not bytes. |
| "String comparison is by length" | It's lexicographic (dictionary order), comparing code points left to right. |
| "`+=` in a loop is fine performance-wise" | For large loops it can be O(n²); prefer list + `join`. |

## Summary
Strings are immutable, ordered sequences of Unicode code points in Python. Understanding encoding (ASCII vs UTF-8/16/32) prevents an entire category of bugs. Immutability is a deliberate design tradeoff favoring safety and hashability over in-place mutation speed.

## Revision Notes
- `ord()`/`chr()` convert between character and code point.
- UTF-8 is variable width, ASCII-compatible; UTF-16/32 are not ASCII-compatible in general.
- `len()` counts code points, not bytes or visual glyphs.
- Python strings are immutable; every mutation creates a new object.

## Cheat Sheet
```python
ord('A')          # 65
chr(65)            # 'A'
'A'.encode('utf-8')# b'A'
b'A'.decode('utf-8')# 'A'
len('café')        # 4
len('café'.encode('utf-8')) # 5
```

## Complexity Summary
| Operation | Complexity |
|---|---|
| Indexing `s[i]` | O(1) |
| `len(s)` | O(1) (cached) |
| Slicing `s[a:b]` | O(b-a) |
| Concatenation `s1+s2` | O(len(s1)+len(s2)) |

## Common Mistakes
- Assuming `len()` counts bytes.
- Mixing `str` and `bytes` without explicit encode/decode (`TypeError` in Python 3).
- Believing strings can be mutated in place.

## FAQs
**Q: Is a Python string a list of characters?**
A: No. It's its own immutable sequence type; Python has no distinct `char` type.

**Q: Why is UTF-8 preferred over UTF-16/32 on the web?**
A: It's backward-compatible with ASCII and space-efficient for English-heavy text, which dominates web traffic historically.

## Practice Problems
- Convert a string to its ASCII values — GfG: https://www.geeksforgeeks.org/problems/convert-a-sentence-into-its-equivalent-mobile-numeric-keypad-sequence0805/1
- Detect if a string is valid ASCII — Practice on HackerRank: https://www.hackerrank.com/domains/tutorials/10-days-of-javascript (conceptual, adapt to Python)
- Unicode code point sum — LeetCode discuss / custom practice


# Chapter 2 — Python Strings

**Learning Objectives:** Master every syntactic and semantic detail of Python's `str` type.
**Prerequisites:** Chapter 1
**Estimated Reading Time:** 35 minutes
**Difficulty Level:** Beginner–Intermediate
**Interview Relevance:** High — slicing and formatting questions are extremely common.

## 2.1 String Creation & Quoting Styles

```python
s1 = 'single quotes'
s2 = "double quotes"
s3 = '''triple single'''
s4 = """triple double"""
s5 = str(123)          # "123" via constructor
s6 = "It's fine"        # double quotes avoid escaping apostrophe
s7 = 'She said "hi"'    # single quotes avoid escaping double quotes
```

> **Tip:** Single and double quotes are functionally identical in Python — choice is a style preference (PEP 8 has no strong preference; be consistent).

## 2.2 Escape Sequences

| Sequence | Meaning |
|---|---|
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\r` | Carriage return |
| `\0` | Null character |
| `\xhh` | Hex-valued character |
| `\uxxxx` | 16-bit Unicode character |
| `\Uxxxxxxxx` | 32-bit Unicode character |
| `\N{NAME}` | Unicode by name |

```python
print("Line1\nLine2")
print("Tab\tSeparated")
print("\u2764")     # ❤
print("\N{HEAVY BLACK HEART}")  # ❤
```

## 2.3 Raw Strings

Prefixing with `r` disables escape-sequence processing — essential for regex and Windows file paths.

```python
path = r"C:\new_folder\test"
print(path)   # C:\new_folder\test  (no escape processing)

normal = "C:\new_folder\test"
print(normal)  # C:
               #  ew_folder	est   <- \n and \t got interpreted!
```

> **Warning:** A raw string cannot end with an odd number of backslashes: `r"path\"` is a `SyntaxError`.

## 2.4 Triple-Quoted Strings

Used for multi-line strings and docstrings.

```python
paragraph = """This is
a multi-line
string."""
```

## 2.5 String Immutability Internals

Every string operation that appears to "modify" a string actually builds a new `str` object in memory (see Chapter 1.8). CPython may optimize small/short strings via **interning** (Section 2.13).

## 2.6 Indexing

```python
s = "PYTHON"
print(s[0])   # 'P'
print(s[5])   # 'N'
print(s[6])   # IndexError: string index out of range
```

### ASCII Diagram
```
Index:  0   1   2   3   4   5
        P   Y   T   H   O   N
```

## 2.7 Negative Indexing

Negative indices count from the end, with `-1` being the last character.

```python
s = "PYTHON"
print(s[-1])  # 'N'
print(s[-6])  # 'P'
print(s[-7])  # IndexError
```

### ASCII Diagram
```
Positive:  0   1   2   3   4   5
           P   Y   T   H   O   N
Negative: -6  -5  -4  -3  -2  -1
```

## 2.8 Slicing & Extended Slicing

Syntax: `s[start:stop:step]` — `start` inclusive, `stop` exclusive.

```python
s = "PYTHON"
print(s[1:4])     # 'YTH'
print(s[:3])      # 'PYT'   (start defaults to 0)
print(s[3:])      # 'HON'   (stop defaults to len(s))
print(s[:])       # 'PYTHON' (full copy — but same content, new "view" semantically a new object reference in CPython may share)
print(s[::2])     # 'PTO'   (every 2nd char)
print(s[::-1])    # 'NOHTYP' (reversed!)
print(s[-3:])     # 'HON'
print(s[1:100])   # 'YTHON' (no IndexError — clamps to length)
```

### Dry Run — `s[1:4]` where `s = "PYTHON"`

| Step | start | stop | Index scanned | Char picked | Result so far |
|---|---|---|---|---|---|
| 1 | 1 | 4 | 1 | Y | "Y" |
| 2 | 1 | 4 | 2 | T | "YT" |
| 3 | 1 | 4 | 3 | H | "YTH" |
| 4 | 1 | 4 | 4 (stop, exclusive) | — | "YTH" (done) |

### ASCII Diagram — Slicing Window
```
Index:   0   1   2   3   4   5
         P   Y   T   H   O   N
              ^-------^
            s[1:4] = "YTH"
```

> **Interview Tip:** `s[::-1]` is the fastest, most Pythonic way to reverse a string — O(n) time, implemented in C.

## 2.9 Traversal & Iteration

```python
s = "abc"
for ch in s:
    print(ch)

for i in range(len(s)):
    print(i, s[i])

for i, ch in enumerate(s):
    print(i, ch)
```

## 2.10 Membership Testing

```python
s = "hello world"
print('h' in s)          # True
print('xyz' in s)        # False
print('world' in s)      # True (substring check)
print('world' not in s)  # False
```
Membership testing on strings runs in O(n·m) worst case (naive substring search) but CPython's implementation uses an optimized algorithm (a variant of Crochemore–Perrin / two-way string matching) giving strong average-case performance.

## 2.11 Comparison & Lexicographical Order

Strings compare character by character using Unicode code point values.

```python
print("apple" < "banana")   # True  ('a' < 'b')
print("Apple" < "apple")    # True  (ord('A')=65 < ord('a')=97)
print("apple" < "app")      # False ("app" is a prefix, shorter wins if equal so far)
print("app" < "apple")      # True
```

### Dry Run — `"apple" < "app"`

| Step | i | apple[i] | app[i] | Compare | Decision |
|---|---|---|---|---|---|
| 1 | 0 | a | a | equal | continue |
| 2 | 1 | p | p | equal | continue |
| 3 | 2 | p | p | equal | continue |
| 4 | 3 | l | — (app ended) | app is shorter | "app" < "apple" → so "apple" < "app" is False |

## 2.12 String Formatting

### 2.12.1 Old-Style `%` Formatting
```python
name = "Ada"
print("Hello, %s!" % name)
print("%d + %d = %d" % (2, 3, 5))
```

### 2.12.2 `.format()`
```python
print("Hello, {}!".format("Ada"))
print("{0} + {1} = {2}".format(2, 3, 5))
print("{name} is {age}".format(name="Ada", age=30))
```

### 2.12.3 f-Strings (Python 3.6+, Recommended)
```python
name, age = "Ada", 30
print(f"{name} is {age}")
print(f"{2 + 3 = }")          # Python 3.8+ debug specifier -> "2 + 3 = 5"
pi = 3.14159
print(f"{pi:.2f}")            # "3.14"
print(f"{42:05d}")            # "00042"
print(f"{1000000:,}")         # "1,000,000"
```

| Style | Introduced | Speed | Readability | Recommended |
|---|---|---|---|---|
| `%` formatting | Python 1.x | Slowest | Low | No |
| `.format()` | Python 2.6 | Medium | Medium | For dynamic templates |
| f-strings | Python 3.6 | Fastest | High | **Yes, default choice** |

## 2.13 String Interning

CPython automatically **interns** (caches and reuses) certain strings — identifiers-like strings (alphanumeric + underscore) and string literals known at compile time — so that equal strings may share the same object in memory.

```python
a = "hello"
b = "hello"
print(a is b)   # True (interned, same object)

c = "hello world!"
d = "hello world!"
print(c is d)   # Implementation-dependent; often True for literals, but NOT guaranteed

e = "".join(["hel", "lo"])
print(a is e)   # Often False — runtime-constructed strings aren't auto-interned
```

> **Warning:** Never rely on `is` for string equality. Always use `==`. Interning is a CPython implementation detail, not a language guarantee.

You can force interning with `sys.intern()`:
```python
import sys
x = sys.intern("some long repeated string")
```

## 2.14 Memory Representation (CPython Internals)

Since Python 3.3 (PEP 393), strings use a **flexible internal representation**: CPython picks the smallest fixed-width storage that fits all characters in the string:
- **Latin-1 (1 byte/char)** if all code points ≤ 0xFF
- **UCS-2 (2 bytes/char)** if max code point ≤ 0xFFFF
- **UCS-4 (4 bytes/char)** if any code point > 0xFFFF (e.g., emoji)

```python
import sys
print(sys.getsizeof("a"))       # small, 1-byte repr
print(sys.getsizeof("😀"))      # larger, needs 4-byte repr internally
```

### ASCII Diagram — Memory Layout
```
"hello" (all ASCII, fits Latin-1):
+---+---+---+---+---+
| h | e | l | l | o |   1 byte each
+---+---+---+---+---+

"héllo" (contains é, U+00E9, still Latin-1):
+---+---+---+---+---+---+
| h | é | l | l | o |    1 byte each (still fits)
+---+---+---+---+---+---+

"😀bc" (emoji > 0xFFFF forces UCS-4):
+------+------+------+
| 😀   |  b   |  c   |   4 bytes each
+------+------+------+
```

## 2.15 Copying vs Referencing

Because strings are immutable, "copying" a string is cheap — Python often just shares the reference.

```python
a = "hello"
b = a          # b references the same object as a
print(a is b)  # True

c = a[:]       # slicing full string -- CPython optimizes this to return same object
print(a is c)  # True (implementation detail)
```

Since strings never change, this sharing is always safe — there's no risk of one variable's mutation affecting another.

## Summary
Python strings support rich literal syntax (quotes, raw, triple-quoted), zero-based and negative indexing, powerful slicing, and three generations of formatting (culminating in f-strings). Internally, CPython stores strings in the most compact fixed-width form possible and may intern short/literal strings for memory efficiency — but this is never something your code should depend on for correctness.

## Revision Notes
- `s[start:stop:step]`, stop exclusive, negative step reverses.
- Use f-strings by default.
- Never use `is` to compare string values.
- Strings are stored in the smallest encoding that fits (Latin-1/UCS-2/UCS-4).

## Cheat Sheet
```python
s[::-1]              # reverse
s[a:b]                # substring
f"{x:.2f}"            # 2 decimal places
f"{x:,}"              # thousands separator
f"{x:05d}"            # zero-padded width 5
sys.intern(s)          # force interning
```

## Complexity Summary
| Operation | Complexity |
|---|---|
| `s[i]` | O(1) |
| `s[a:b]` | O(b−a) |
| `s1 == s2` | O(min(len(s1), len(s2))) worst case O(n) |
| `x in s` | O(n) average (optimized substring search) |

## Common Mistakes
- Using `is` instead of `==` for string comparison.
- Forgetting `stop` is exclusive in slicing.
- Believing `s[:]` creates an independent mutable copy (irrelevant since strings are immutable anyway).
- Mixing `%`-formatting and f-strings inconsistently in the same codebase.

## FAQs
**Q: Are Python strings null-terminated like C strings?**
A: No. Python strings store their length explicitly; they can contain `\0` bytes.

**Q: Is slicing a string expensive?**
A: O(k) where k is the slice length — cheap for small slices, but repeated slicing in a loop can add up.

## Practice Problems
- Reverse a String — LeetCode: https://leetcode.com/problems/reverse-string/
- Reverse Words in a String — LeetCode: https://leetcode.com/problems/reverse-words-in-a-string/
- Implement strStr() — LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
- Valid Palindrome — LeetCode: https://leetcode.com/problems/valid-palindrome/


# Chapter 3 — String Operations (Every Method)

**Learning Objectives:** Know every built-in string method, its signature, complexity, and edge cases.
**Prerequisites:** Chapter 2
**Estimated Reading Time:** 45 minutes
**Difficulty Level:** Beginner–Intermediate
**Interview Relevance:** Very High.

## 3.1 Access & Pseudo-Update

Since strings are immutable, "updating" means building a new string.

```python
s = "hello"
# Change index 0 to 'H' -> must rebuild
s = 'H' + s[1:]
print(s)   # "Hello"

# Using list for multiple edits then join
chars = list("hello")
chars[0] = 'H'
s2 = ''.join(chars)
print(s2)  # "Hello"
```

## 3.2 Concatenation

```python
a, b = "foo", "bar"
print(a + b)          # "foobar"
print(a + " " + b)    # "foo bar"

# Efficient multi-piece concatenation
parts = ["foo", "bar", "baz"]
print(''.join(parts))  # "foobarbaz"
```
> **Warning:** `result = ""` then `result += s` inside a loop over n pieces is O(n²) in the worst case (each `+=` may copy the whole accumulated string). Prefer collecting into a list and `''.join()` at the end — O(n) total. (CPython has an optimization for repeated `+=` on the sole reference to a string that can make this O(n) in practice, but it's an implementation detail you should not rely on for correctness/portability, e.g. PyPy doesn't have it.)

## 3.3 Repetition

```python
print("ab" * 3)      # "ababab"
print("-" * 20)       # "--------------------"
print(3 * "xy")        # "xyxyxy" (commutative)
```

## 3.4 split / rsplit / splitlines

```python
s = "  the quick brown fox  "
print(s.split())                 # ['the', 'quick', 'brown', 'fox']  (splits on any whitespace, drops empties)
print("a,b,,c".split(","))       # ['a', 'b', '', 'c']  (keeps empty strings with explicit sep)
print("a,b,c".split(",", 1))     # ['a', 'b,c']  (maxsplit)
print("a,b,c".rsplit(",", 1))    # ['a,b', 'c']  (split from the right)
print("line1\nline2\r\nline3".splitlines())  # ['line1', 'line2', 'line3']
```

## 3.5 join

```python
print(','.join(['a', 'b', 'c']))     # "a,b,c"
print(''.join(['a', 'b', 'c']))      # "abc"
print(' '.join(str(x) for x in range(5)))  # "0 1 2 3 4"
```
> **Interview Tip:** `''.join(list_of_chars)` is the standard idiomatic way to build a string from parts efficiently.

## 3.6 replace

```python
print("banana".replace("a", "o"))         # "bonono"
print("banana".replace("a", "o", 1))      # "bonana"  (count limit)
```

## 3.7 strip / lstrip / rstrip

```python
print("  hi  ".strip())     # "hi"
print("  hi  ".lstrip())    # "hi  "
print("  hi  ".rstrip())    # "  hi"
print("xxhixx".strip("x"))  # "hi"  (strips characters in the given set, not a prefix/suffix string)
print("xyxhixyx".strip("xy")) # "hi"
```
> **Common Mistake:** `strip("xy")` strips ANY of `x` or `y` from both ends, not the literal substring `"xy"`.

## 3.8 find / rfind

```python
print("hello world".find("o"))     # 4  (first occurrence)
print("hello world".find("o", 5))  # 7  (search starting at index 5)
print("hello world".find("z"))     # -1 (not found, no exception)
print("hello world".rfind("o"))    # 7  (last occurrence)
```

## 3.9 index / rindex

Same as `find`/`rfind` but raise `ValueError` instead of returning `-1`.

```python
print("hello".index("l"))    # 2
"hello".index("z")            # ValueError: substring not found
```

## 3.10 count

```python
print("mississippi".count("s"))    # 4
print("mississippi".count("ss"))   # 2 (non-overlapping matches!)
print("aaaa".count("aa"))          # 2, NOT 3 (non-overlapping)
```

### ASCII Diagram — Non-overlapping count
```
"aaaa".count("aa")
 [aa]aa   match 1 at index 0
 aa[aa]   match 2 at index 2
 result = 2  (index 1 and 3 overlaps are skipped)
```

## 3.11 startswith / endswith

```python
print("hello.py".endswith(".py"))          # True
print("hello.py".startswith(("hi", "he"))) # True (tuple of prefixes allowed)
print("hello".startswith("ell", 1))        # True (start offset)
```

## 3.12 Case Methods

```python
print("Hello World".lower())      # "hello world"
print("Hello World".upper())      # "HELLO WORLD"
print("hello world".title())      # "Hello World"
print("hello world".capitalize()) # "Hello world"
print("Hello World".swapcase())   # "hELLO wORLD"
```
> **Edge Case:** `"HELLO WORLD".title()` capitalizes after any non-alpha char, so `"they're"` becomes `"They'Re"` — a classic bug source.

## 3.13 center / ljust / rjust / zfill

```python
print("hi".center(10, "*"))    # "****hi****"
print("hi".ljust(10, "-"))     # "hi--------"
print("hi".rjust(10, "-"))     # "--------hi"
print("42".zfill(5))            # "00042"
print("-42".zfill(5))           # "-0042"  (sign-aware)
```

## 3.14 partition / rpartition

Splits into exactly 3 parts: before, separator, after.

```python
print("key=value".partition("="))    # ('key', '=', 'value')
print("a=b=c".partition("="))         # ('a', '=', 'b=c')  (first occurrence)
print("a=b=c".rpartition("="))        # ('a=b', '=', 'c')  (last occurrence)
print("no-sep-here".partition("="))   # ('no-sep-here', '', '')  (sep not found)
```

## 3.15 translate / maketrans

Fast character-to-character (or char-to-None deletion) mapping — much faster than chained `.replace()` calls for many-character substitutions.

```python
table = str.maketrans("abc", "xyz")
print("aabbcc".translate(table))          # "xxyyzz"

# Deletion mode
del_table = str.maketrans("", "", "aeiou")
print("hello world".translate(del_table)) # "hll wrld"
```

## 3.16 encode / decode

```python
s = "café"
b = s.encode('utf-8')       # b'caf\xc3\xa9'
print(b)
print(b.decode('utf-8'))     # 'café'

# Error handling
"café".encode('ascii', errors='ignore')    # b'caf'
"café".encode('ascii', errors='replace')   # b'caf?'
```

## 3.17 Full Method Reference Table

| Method | Purpose | Returns | Complexity |
|---|---|---|---|
| `s.capitalize()` | First char upper, rest lower | str | O(n) |
| `s.casefold()` | Aggressive lowercasing for caseless matching | str | O(n) |
| `s.center(w, fill)` | Center-pad | str | O(w) |
| `s.count(sub)` | Non-overlapping count | int | O(n) |
| `s.encode(enc)` | str → bytes | bytes | O(n) |
| `s.endswith(suf)` | Suffix check | bool | O(k) |
| `s.expandtabs(n)` | Tabs → spaces | str | O(n) |
| `s.find(sub)` | First index or -1 | int | O(n·m) worst |
| `s.format(*a)` | Template formatting | str | O(n) |
| `s.index(sub)` | Like find, raises on missing | int | O(n·m) worst |
| `s.isalnum()` | All alnum? | bool | O(n) |
| `s.isalpha()` | All alphabetic? | bool | O(n) |
| `s.isdigit()` | All digits? | bool | O(n) |
| `s.isnumeric()` | All numeric (incl. fractions/unicode)? | bool | O(n) |
| `s.isdecimal()` | All decimal digits? | bool | O(n) |
| `s.isidentifier()` | Valid Python identifier? | bool | O(n) |
| `s.islower()` / `isupper()` | Case check | bool | O(n) |
| `s.isspace()` | All whitespace? | bool | O(n) |
| `s.istitle()` | Title-cased? | bool | O(n) |
| `s.isprintable()` | All printable? | bool | O(n) |
| `s.join(iter)` | Join with sep | str | O(total length) |
| `s.ljust(w)` / `rjust(w)` | Pad | str | O(w) |
| `s.lower()` / `upper()` | Case conversion | str | O(n) |
| `s.lstrip()` / `rstrip()` / `strip()` | Trim chars | str | O(n) |
| `s.maketrans(...)` | Build translation table | dict | O(k) |
| `s.partition(sep)` / `rpartition` | 3-way split | tuple | O(n) |
| `s.replace(old,new)` | Substitute | str | O(n) |
| `s.rfind()` / `rindex()` | Search from right | int | O(n·m) worst |
| `s.split(sep)` / `rsplit` | Split into list | list | O(n) |
| `s.splitlines()` | Split on line boundaries | list | O(n) |
| `s.startswith(pre)` | Prefix check | bool | O(k) |
| `s.swapcase()` | Flip case | str | O(n) |
| `s.title()` | Title case | str | O(n) |
| `s.translate(table)` | Apply translation table | str | O(n) |
| `s.zfill(w)` | Zero-pad (sign-aware) | str | O(w) |

## Summary
Python's `str` type ships with 40+ built-in methods covering search, transform, validate, pad, and split/join operations. Nearly all run in O(n) or O(n·m) time; understanding exactly what each returns (and its edge cases with empty separators / not-found cases) prevents subtle bugs.

## Revision Notes
- `find` → -1 on miss; `index` → exception on miss.
- `count` is **non-overlapping**.
- `strip(chars)` treats `chars` as a **set** of characters, not a literal substring.
- `translate` beats chained `replace()` for many single-character substitutions.

## Cheat Sheet
```python
s.split()              # whitespace split, drop empties
s.split(",")            # keep empties on explicit sep
','.join(lst)           # build from list
s.strip()               # trim whitespace both ends
s.replace(a, b)         # substitute all
s.find(a); s.index(a)   # search: -1 vs exception
s.startswith(a); s.endswith(a)
s.lower(); s.upper(); s.title(); s.capitalize(); s.swapcase()
s.center(w); s.ljust(w); s.rjust(w); s.zfill(w)
s.encode('utf-8'); b.decode('utf-8')
```

## Complexity Summary
| Category | Typical Complexity |
|---|---|
| Search (find/index/count) | O(n·m) worst, near O(n) average (optimized) |
| Transform (lower/upper/replace) | O(n) |
| Split/Join | O(n) |
| Pad (center/ljust/rjust/zfill) | O(width) |

## Common Mistakes
- Forgetting `count` doesn't count overlapping matches.
- Using `.title()` on text with apostrophes/hyphens and getting unexpected capitalization.
- Using `.strip(sub)` expecting substring stripping instead of character-set stripping.
- Calling `.index()` without a try/except and crashing on missing substrings.

## FAQs
**Q: Which is faster, `replace()` chains or `translate()`?**
A: For single-character-to-character maps over many characters, `translate()` is significantly faster since it's a single O(n) pass.

**Q: Does `split()` with no arguments handle multiple consecutive spaces?**
A: Yes — `s.split()` collapses runs of whitespace and ignores leading/trailing whitespace, unlike `s.split(" ")` which produces empty strings for consecutive spaces.

## Practice Problems
- Valid Anagram — LeetCode: https://leetcode.com/problems/valid-anagram/
- Ransom Note — LeetCode: https://leetcode.com/problems/ransom-note/
- Roman to Integer — LeetCode: https://leetcode.com/problems/roman-to-integer/
- String Compression — GfG: https://www.geeksforgeeks.org/problems/run-length-encoding/1


# Chapter 4 — String Patterns

**Learning Objectives:** Master every recurring problem-solving pattern applied to strings, from frequency counting to Manacher's algorithm.
**Prerequisites:** Chapters 1–3
**Estimated Reading Time:** 90 minutes
**Difficulty Level:** Intermediate–Advanced
**Interview Relevance:** Extremely High — this chapter is the interview core.

## 4.1 Character Frequency Counting

### Definition
Counting how many times each character appears in a string.

### Why It Exists
Foundation for anagram checks, uniqueness checks, and window-based problems.

```python
from collections import Counter

def char_frequency(s):
    return Counter(s)

freq = char_frequency("mississippi")
print(freq)   # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

### Manual Implementation (Interview Style)
```python
def char_frequency_manual(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
```

### Dry Run — `char_frequency_manual("aab")`

| Step | ch | freq before | freq after |
|---|---|---|---|
| 1 | a | {} | {'a': 1} |
| 2 | a | {'a': 1} | {'a': 2} |
| 3 | b | {'a': 2} | {'a': 2, 'b': 1} |

**Complexity:** Time O(n), Space O(k) where k = alphabet size.

## 4.2 Sliding Window on Strings

### Definition
A technique that maintains a "window" `[left, right]` over the string, expanding/shrinking it to satisfy a constraint, avoiding recomputation from scratch.

### ASCII Diagram
```
s = "a b c a b c b b"
     L
     R
Expand R until constraint violated, then shrink L.

Step:  L=0 R=0  window="a"
Step:  L=0 R=3  window="abca"  <- 'a' repeated, violate uniqueness
Step:  L=1 R=3  window="bca"   <- shrink from left until valid again
```

### Example — Longest Substring Without Repeating Characters
**Problem:** Find the length of the longest substring with all unique characters.
**Approach:** Sliding window with a set/dict tracking the last seen index of each character.

```python
def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

### Dry Run — `s = "abba"`

| right | ch | last_seen[ch] before | left | window | best |
|---|---|---|---|---|---|
| 0 | a | — | 0 | "a" | 1 |
| 1 | b | — | 0 | "ab" | 2 |
| 2 | b | 1 (>=left) | 2 | "b" | 2 |
| 3 | a | 0 (<left, stale) | 2 | "ba" | 2 |

**Result:** 2 ("ab" or "ba")

**Complexity:** Time O(n), Space O(min(n, alphabet)).

### When to Use
Contiguous substring problems with a constraint (uniqueness, at most K distinct chars, sum/count threshold).
### When NOT to Use
Subsequence problems (non-contiguous) — sliding window requires contiguity.

## 4.3 Two Pointers on Strings

### Definition
Two indices moving toward each other (or in the same direction) to solve comparison/matching problems in O(n) instead of O(n²).

### ASCII Diagram — Two Pointer Convergence
```
s = "r a c e c a r"
     L             R
     L->           <-R   (move inward, compare)
```

### Example — Valid Palindrome (ignoring non-alphanumeric, case-insensitive)
```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

### Dry Run — `s = "A man, a plan, a canal: Panama"` (abbreviated)
| left | right | s[left] | s[right] | match? |
|---|---|---|---|---|
| 0 | 29 | 'A' | 'a' | yes (case-insensitive) |
| 1 | 28 | 'm' | 'm' | yes |
| ... | ... | ... | ... | ... |
| converge | | | | True |

**Complexity:** Time O(n), Space O(1).

## 4.4 Prefix/Suffix Techniques

### ASCII Diagram
```
s = "a b c d e"
prefix[i] = s[0..i]
suffix[i] = s[i..n-1]

prefix(3) = "abc"
suffix(2) = "cde"
```
Prefix sums of character counts enable O(1) range-frequency queries; prefix/suffix arrays underpin KMP, Z-function, and palindrome algorithms (see 4.15–4.19).

## 4.5 Palindrome Pattern

Covered in depth in Chapter 6. Quick check:
```python
def is_pal(s):
    return s == s[::-1]
```
**Complexity:** O(n) time, O(n) space (due to slice copy).

## 4.6 Expand Around Center

### Definition
For each possible palindrome center (there are `2n - 1` centers — n single-character centers and n-1 between-character centers), expand outward while characters match.

### ASCII Diagram
```
s = "b a b a d"
Centers:  b|a|b|a|d  and gaps between each pair
           ^     single-char center at index 2 ('b')
          ^ ^    even-length center between index 1,2
```

```python
def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]   # actual palindrome substring

def longest_palindrome(s):
    best = ""
    for i in range(len(s)):
        odd = expand(s, i, i)
        even = expand(s, i, i+1)
        best = max(best, odd, even, key=len)
    return best
```
**Complexity:** Time O(n²) worst case, Space O(1) extra (excluding output).
Full dry run provided in Chapter 6.

## 4.7 Anagram Pattern

### Definition
Two strings are anagrams if they contain exactly the same characters with the same frequencies, in any order.

```python
from collections import Counter

def is_anagram(a: str, b: str) -> bool:
    return Counter(a) == Counter(b)

# O(n log n) alternative
def is_anagram_sort(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)
```

| Approach | Time | Space |
|---|---|---|
| Sorting | O(n log n) | O(n) |
| Counter/hashmap | O(n) | O(k) alphabet size |

## 4.8 Hashing for Strings (Frequency-Only Scope)

For this handbook, "hashing" refers strictly to using character-frequency maps or polynomial rolling hashes for **string comparison/search** — not generic hash table theory.

```python
def is_anagram_fixed_alphabet(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    freq = [0] * 26
    for ca, cb in zip(a, b):
        freq[ord(ca) - ord('a')] += 1
        freq[ord(cb) - ord('a')] -= 1
    return all(f == 0 for f in freq)
```
**Complexity:** O(n) time, O(1) space (fixed 26-size array).

## 4.9 Character Mapping / Bijection

### Definition
Checking whether two strings follow a consistent one-to-one character mapping (used in "Isomorphic Strings" and "Word Pattern" problems).

```python
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map_st, map_ts = {}, {}
    for cs, ct in zip(s, t):
        if cs in map_st and map_st[cs] != ct:
            return False
        if ct in map_ts and map_ts[ct] != cs:
            return False
        map_st[cs] = ct
        map_ts[ct] = cs
    return True

print(is_isomorphic("egg", "add"))   # True (e->a, g->d)
print(is_isomorphic("foo", "bar"))   # False (o->a then o->r conflict)
```

## 4.10 Run-Length Encoding (RLE)

### Definition
Compress consecutive repeated characters into `char + count` pairs.

```python
def rle_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    prev = s[0]
    count = 1
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            result.append(prev + str(count))
            prev = ch
            count = 1
    result.append(prev + str(count))
    return ''.join(result)

print(rle_encode("aaabbbccd"))   # "a3b3c2d1"
```

### Dry Run — `s = "aab"`

| i | ch | prev | count | result |
|---|---|---|---|---|
| start | | 'a' | 1 | [] |
| 1 | a | 'a' | 2 | [] |
| 2 | b | switch | flush 'a2', prev='b', count=1 | ['a2'] |
| end | | | flush 'b1' | ['a2', 'b1'] |

**Output:** `"a2b1"`

**Complexity:** Time O(n), Space O(n) worst case (no compression benefit if no repeats).

## 4.11 String Compression (LeetCode-Style In-Place)

```python
def compress(chars: list) -> int:
    write = 0
    read = 0
    n = len(chars)
    while read < n:
        char = chars[read]
        count = 0
        while read < n and chars[read] == char:
            read += 1
            count += 1
        chars[write] = char
        write += 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    return write
```
**Complexity:** Time O(n), Space O(1) extra (in-place).

## 4.12 Tokenization

Splitting text into meaningful units (words, punctuation) — the first stage of any parser or NLP pipeline.

```python
import re
text = "Hello, world! This is Python."
tokens = re.findall(r"\w+", text)
print(tokens)   # ['Hello', 'world', 'This', 'is', 'Python']
```

## 4.13 Subsequence vs Substring Patterns

| Concept | Contiguous? | Order Preserved? | Example from "abc" |
|---|---|---|---|
| Substring | Yes | Yes | "ab", "bc", "abc" |
| Subsequence | No | Yes | "ac", "bc", "abc" |
| Subarray (for array analogy) | Yes | Yes | (array-only term) |

```python
def is_subsequence(s: str, t: str) -> bool:
    """Is s a subsequence of t?"""
    it = iter(t)
    return all(ch in it for ch in s)

print(is_subsequence("ace", "abcde"))  # True
print(is_subsequence("aec", "abcde"))  # False (order matters)
```
**Complexity:** O(len(t)) time, O(1) extra space.

## 4.14 Rolling Hash (String Perspective)

### Definition
A hash of a substring that can be updated in O(1) when the window slides by one character, instead of recomputing from scratch.

### Formula
For a window hash of `s[i..i+k-1]` using base `B` and modulus `M`:
```
H(s[i..i+k-1]) = (s[i]*B^(k-1) + s[i+1]*B^(k-2) + ... + s[i+k-1]*B^0) mod M
```
Sliding to the next window:
```
H_next = ((H_curr - s[i]*B^(k-1)) * B + s[i+k]) mod M
```

```python
def rolling_hash_search(text: str, pattern: str) -> list:
    n, m = len(text), len(pattern)
    if m > n:
        return []
    B, M = 256, 10**9 + 7
    high_order = pow(B, m - 1, M)

    pat_hash = 0
    win_hash = 0
    for i in range(m):
        pat_hash = (pat_hash * B + ord(pattern[i])) % M
        win_hash = (win_hash * B + ord(text[i])) % M

    result = []
    for i in range(n - m + 1):
        if win_hash == pat_hash and text[i:i+m] == pattern:  # verify to handle collisions
            result.append(i)
        if i < n - m:
            win_hash = ((win_hash - ord(text[i]) * high_order) * B + ord(text[i + m])) % M
    return result
```
**Complexity:** Average O(n + m), Worst O(n·m) with adversarial collisions (mitigated by verification step).
This is the core idea behind **Rabin-Karp**, covered fully in 4.18 and Chapter 7.

## 4.15 KMP Pattern (Overview — full derivation in Chapter 7)

KMP avoids re-scanning characters in the text by precomputing an LPS (Longest Prefix Suffix) array on the pattern, achieving O(n + m) matching. See Chapter 7.2 for the complete derivation, dry run, and code.

## 4.16 Z-Algorithm (Overview — full derivation in Chapter 7)

The Z-array `Z[i]` stores the length of the longest substring starting at `i` that matches a prefix of the string. Used for pattern matching in O(n + m). See Chapter 7.3.

## 4.17 LPS / Prefix Function

The **LPS (Longest Proper Prefix which is also Suffix) array** used by KMP:

```python
def compute_lps(pattern: str) -> list:
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps

print(compute_lps("ababaca"))  # [0, 0, 1, 2, 3, 0, 1]
```

### Dry Run — `pattern = "aabaa"`

| i | length | pattern[i] | pattern[length] | action | lps |
|---|---|---|---|---|---|
| 1 | 0 | a | a | match, length=1 | [0,1,0,0,0] |
| 2 | 1 | b | a | mismatch, length=0 | [0,1,0,0,0] |
| 3 | 0 | a | a | match, length=1 | [0,1,0,1,0] |
| 4 | 1 | a | a | match, length=2 | [0,1,0,1,2] |

**Final LPS:** `[0, 1, 0, 1, 2]`

## 4.18 Rabin-Karp (String Perspective — full derivation in Chapter 7)

Uses rolling hash (4.14) to find pattern occurrences in average O(n + m) time.

## 4.19 Manacher's Algorithm (Overview — full derivation in Chapter 6)

Finds the longest palindromic substring in **O(n)**, beating the O(n²) expand-around-center approach, by reusing previously computed palindrome radii with a clever mirror trick. Full derivation in Chapter 6.5.

## Summary
This chapter catalogued every major string-specific problem-solving pattern: frequency maps, sliding window, two pointers, prefix/suffix reasoning, palindrome expansion, anagram detection, character bijection, run-length encoding, subsequence checking, and the three classical linear-time matching algorithms (KMP, Z, Rabin-Karp) plus Manacher's for palindromes.

## Revision Notes
- Sliding window → contiguous + constraint.
- Two pointers → convergence/comparison, often O(n) vs O(n²) naive.
- Anagram → sorting O(n log n) or Counter O(n).
- Rolling hash → O(1) amortized window hash updates; always verify to avoid hash-collision false positives.

## Cheat Sheet
```python
Counter(s)                      # frequency map
s == s[::-1]                    # palindrome check
sorted(a) == sorted(b)           # anagram check (simple)
Counter(a) == Counter(b)         # anagram check (optimal)
compute_lps(pattern)             # KMP preprocessing
```

## Complexity Summary
| Pattern | Time | Space |
|---|---|---|
| Frequency count | O(n) | O(k) |
| Sliding window | O(n) | O(k) |
| Two pointers | O(n) | O(1) |
| Expand around center | O(n²) | O(1) |
| Anagram (sort) | O(n log n) | O(n) |
| Anagram (counter) | O(n) | O(k) |
| Rolling hash search | O(n+m) avg | O(1) |
| KMP | O(n+m) | O(m) |
| Manacher | O(n) | O(n) |

## Common Mistakes
- Using sliding window for non-contiguous (subsequence) problems.
- Forgetting to verify actual match after a rolling-hash hit (collision risk).
- Off-by-one errors in LPS array construction.
- Confusing `count()` (non-overlapping) with the number of possible matches.

## FAQs
**Q: When should I use two pointers vs sliding window?**
A: Two pointers is for fixed-size comparison/convergence (palindrome checks, merging); sliding window is for variable-size contiguous ranges satisfying a constraint.

**Q: Is rolling hash always faster than KMP?**
A: Average case similar; KMP guarantees worst-case O(n+m) with no collision risk, so it's preferred when adversarial input is a concern.

## Practice Problems
- Longest Substring Without Repeating Characters — LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Minimum Window Substring — LeetCode: https://leetcode.com/problems/minimum-window-substring/
- Find All Anagrams in a String — LeetCode: https://leetcode.com/problems/find-all-anagrams-in-a-string/
- Group Anagrams — LeetCode: https://leetcode.com/problems/group-anagrams/
- Isomorphic Strings — LeetCode: https://leetcode.com/problems/isomorphic-strings/
- String Compression — LeetCode: https://leetcode.com/problems/string-compression/
- Implement KMP — GfG: https://www.geeksforgeeks.org/problems/search-pattern0205/1


# Chapter 5 — Substrings

**Learning Objectives:** Precisely distinguish substrings, subsequences, prefixes, and suffixes; count and generate them efficiently.
**Prerequisites:** Chapters 1–4
**Estimated Reading Time:** 25 minutes
**Difficulty Level:** Beginner–Intermediate

## 5.1 Substring vs Subsequence vs Subarray

| Term | Definition | Contiguous | Example (from "abc") |
|---|---|---|---|
| Substring | Contiguous block of characters | Yes | "a","ab","bc","abc" |
| Subsequence | Characters in order, gaps allowed | No | "a","ac","abc","b" |
| Subarray | Array analogy of substring | Yes | (used for arrays, not strings) |

### ASCII Diagram
```
s = a b c
Substrings:  a | ab | abc | b | bc | c        (6 non-empty substrings for n=3 -> n(n+1)/2)
Subsequences: a, b, c, ab, ac, bc, abc, ""     (2^n subsequences including empty)
```

## 5.2 Prefix & Suffix

```python
s = "hello"
prefixes = [s[:i] for i in range(1, len(s)+1)]
suffixes = [s[i:] for i in range(len(s))]
print(prefixes)  # ['h', 'he', 'hel', 'hell', 'hello']
print(suffixes)  # ['hello', 'ello', 'llo', 'lo', 'o']
```

## 5.3 Longest Common Prefix

**Problem:** Given a list of strings, find the longest common prefix among all of them.

```python
def longest_common_prefix(strs: list) -> str:
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for s in strs:
            if s[i] != ch:
                return shortest[:i]
    return shortest
```

### Dry Run — `strs = ["flower", "flow", "flight"]`

| i | ch (from "flow") | check against "flower" | check against "flight" | result so far |
|---|---|---|---|---|
| 0 | f | f==f | f==f | continue |
| 1 | l | l==l | l==l | continue |
| 2 | o | o==o | i≠o → return | "fl" |

**Output:** `"fl"`

**Complexity:** Time O(S) where S = sum of all character counts, Space O(1) extra.

## 5.4 Longest Common Suffix

Simple transformation: reverse all strings, find LCP, reverse the result.
```python
def longest_common_suffix(strs: list) -> str:
    reversed_strs = [s[::-1] for s in strs]
    return longest_common_prefix(reversed_strs)[::-1]
```

## 5.5 Counting Substrings

Total number of non-empty substrings of a string of length n:
```
count = n * (n + 1) / 2
```

```python
def total_substrings(n: int) -> int:
    return n * (n + 1) // 2

print(total_substrings(3))  # 6, matches "abc" example above
```

### Counting Distinct Substrings
Requires a Trie or Suffix Automaton for O(n) — beyond string-only scope; briefly: a **Trie** (mentioned only for context) can store all substrings to count uniques in O(n²) construction / O(n) with a suffix automaton.

## 5.6 Generating All Substrings

```python
def all_substrings(s: str) -> list:
    n = len(s)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.append(s[i:j])
    return result

print(all_substrings("abc"))
# ['a', 'ab', 'abc', 'b', 'bc', 'c']
```
**Complexity:** Time O(n²) to generate, O(n³) if you also print/copy each (since slicing is O(k)). Space O(n²) to store all.

## 5.7 Distinct Substrings

```python
def distinct_substrings(s: str) -> set:
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.add(s[i:j])
    return result

print(len(distinct_substrings("aaa")))  # 3: "a", "aa", "aaa" (not 6, due to duplicates)
```

## Summary
Substrings are contiguous; subsequences are order-preserving but not necessarily contiguous. A string of length n has exactly n(n+1)/2 substrings and up to 2ⁿ subsequences. LCP/LCS-of-strings problems reduce elegantly via reversal tricks.

## Revision Notes
- Substring count formula: `n(n+1)/2`.
- Subsequence count (including empty): `2^n`.
- LCP: compare shortest string against all others char by char.

## Cheat Sheet
```python
n * (n + 1) // 2          # total substrings
2 ** n                     # total subsequences (incl. empty)
s[:i]                       # prefix of length i
s[i:]                       # suffix starting at i
```

## Complexity Summary
| Task | Time | Space |
|---|---|---|
| Generate all substrings | O(n²)–O(n³) | O(n²) |
| Longest common prefix | O(S) | O(1) |
| Distinct substrings (naive) | O(n³) (with set hashing) | O(n²) |

## Common Mistakes
- Confusing subsequence with substring in problem statements.
- Off-by-one in nested substring loops (`range(i+1, n+1)` not `range(i+1, n)`).
- Forgetting the empty string counts as a subsequence.

## FAQs
**Q: How many substrings does an empty string have?**
A: Zero non-empty substrings (only the empty string itself, which is often excluded).

## Practice Problems
- Longest Common Prefix — LeetCode: https://leetcode.com/problems/longest-common-prefix/
- Count Distinct Substrings — GfG: https://www.geeksforgeeks.org/problems/count-distinct-substrings/1
- Number of Substrings Containing All Three Characters — LeetCode: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/


# Chapter 6 — Palindromes

**Learning Objectives:** Fully master palindrome checking, longest-palindrome finding (both O(n²) and O(n) approaches), and related interview problems.
**Prerequisites:** Chapters 1–5
**Estimated Reading Time:** 45 minutes
**Difficulty Level:** Intermediate–Advanced
**Interview Relevance:** Very High.

## 6.1 Palindrome Checking

### Definition
A string that reads the same forwards and backwards.

### Real-World Analogy
Like the word "racecar" or the number 121 — a mirror reflection of itself.

```python
def is_palindrome_simple(s: str) -> bool:
    return s == s[::-1]

print(is_palindrome_simple("racecar"))  # True
print(is_palindrome_simple("hello"))    # False
```
**Complexity:** O(n) time, O(n) space (slice creates a copy).

## 6.2 Two-Pointer Check (O(1) extra space)

```python
def is_palindrome_two_pointer(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

### Dry Run — `s = "level"`

| left | right | s[left] | s[right] | equal? |
|---|---|---|---|---|
| 0 | 4 | l | l | yes |
| 1 | 3 | e | e | yes |
| 2 | 2 | (crossed, loop ends) | | True |

**Complexity:** O(n) time, O(1) extra space.

## 6.3 Longest Palindromic Substring

### Brute Force
Check every substring — O(n³).
```python
def longest_pal_brute(s):
    n = len(s)
    best = ""
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if sub == sub[::-1] and len(sub) > len(best):
                best = sub
    return best
```

### Better: Expand Around Center — O(n²)
```python
def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""
    start, end = 0, 0

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1   # last valid boundaries

    for i in range(len(s)):
        l1, r1 = expand(i, i)       # odd length
        if r1 - l1 > end - start:
            start, end = l1, r1
        l2, r2 = expand(i, i + 1)   # even length
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]

print(longest_palindromic_substring("babad"))  # "bab" or "aba"
```

### Dry Run — `s = "babad"`

| i | odd expand | even expand | best so far |
|---|---|---|---|
| 0 | "b" | "" | "b" |
| 1 | "bab" | "" | "bab" |
| 2 | "aba" | "" | "bab" (tie, first kept) |
| 3 | "bab" (dup center) | "" | "bab" |
| 4 | "d" | "" | "bab" |

**Output:** `"bab"`

**Complexity:** Time O(n²), Space O(1) extra.

### Optimal: Manacher's Algorithm — O(n) (see 6.5)

## 6.4 Longest Palindromic Subsequence (Concept Only)

> **Scope Note:** LPS (subsequence version) is fundamentally a Dynamic Programming problem over two indices, so per this handbook's scope it is only mentioned here for completeness — full DP treatment belongs in a Dynamic Programming handbook. As a string-only fact: the longest palindromic subsequence of `s` equals the Longest Common Subsequence of `s` and `reversed(s)`.

## 6.5 Expand Around Center — Deep Dive & Manacher's Algorithm

### Why Expand Around Center Is O(n²)
There are `2n - 1` centers, and each expansion can take O(n) in the worst case (e.g., `"aaaaaaa"`), giving O(n²) total.

### ASCII Diagram — All Centers
```
s = "aba"
Centers (2n-1 = 5):
  ^a       (odd center at 0)
   ^ab      (even gap between 0,1)
    ^b      (odd center at 1)
     ^ba     (even gap between 1,2)
      ^a     (odd center at 2)
```

### Manacher's Algorithm (O(n)) — Full Derivation

**Core Idea:** Transform the string by inserting separators (e.g., `#`) between every character (and at both ends) so odd/even palindromes are handled uniformly. Maintain an array `P[i]` = radius of the palindrome centered at `i` in the transformed string, and reuse previously computed palindrome information via a "mirror" index whenever the current center lies inside a previously found palindrome's boundary.

```python
def manacher(s: str) -> str:
    if not s:
        return ""
    # Transform: "abc" -> "^#a#b#c#$"
    t = '#'.join(f'^{s}$')
    n = len(t)
    p = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])
        # Attempt to expand palindrome centered at i
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        # Update center/right boundary if expanded past right
        if i + p[i] > right:
            center, right = i, i + p[i]

    max_len, center_index = max((n_, i) for i, n_ in enumerate(p))
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

print(manacher("babad"))   # "bab"
print(manacher("cbbd"))    # "bb"
```

### Line-by-Line Explanation
1. `t = '#'.join(f'^{s}$')` — inserts sentinels `^` and `$` (to avoid bounds checks) and `#` between every character, unifying odd/even palindrome handling.
2. `p[i]` tracks the palindrome radius centered at transformed index `i`.
3. `center, right` track the rightmost palindrome boundary found so far.
4. If `i` is within the current rightmost palindrome, initialize `p[i]` using its mirror position (`2*center - i`) — this is the key optimization avoiding redundant comparisons.
5. Attempt to expand further beyond the mirror-based guess.
6. Update `center, right` if this palindrome extends further right than any before.
7. The maximum value in `p[]` gives the longest palindrome's length in the *original* string, and its center maps back via `(center_index - max_len) // 2`.

### Dry Run — `s = "aba"` (abbreviated)

| Transformed t | `^ # a # b # a # $` |
|---|---|
| Index | 0 1 2 3 4 5 6 7 8 |

| i | mirror logic | p[i] | center,right after |
|---|---|---|---|
| 1 (#) | — | 0 | (0,0) |
| 2 (a) | expand: matches # both sides once | 1 | (2,3) |
| 3 (#) | inside (2,3)? no, i=right | expand outward, matches a,a | 0 (stays 0, # can't extend past mismatch) → actually 0 |
| 4 (b) | expand fully (whole string is palindrome) | 3 | (4,7) |
| 5 (#) | mirror=3, p[mirror]=0, bounded by right | 0 | unchanged |
| 6 (a) | mirror=2, p[mirror]=1 | 1 | unchanged |

**Max p[i] = 3 at i=4** → `start = (4-3)//2 = 0` → `s[0:3] = "aba"` ✓.

**Complexity:** Time **O(n)**, Space O(n).

> **Interview Tip:** Manacher's is rarely required to be written from scratch in interviews (it's considered advanced), but knowing it exists and explaining the mirror trick shows depth. Expand-around-center (O(n²)) is fully acceptable for most interviews given n is usually small.

## 6.6 Palindrome Partitioning (Concept Only)

> **Scope Note:** Palindrome Partitioning (splitting a string into the minimum number of palindromic pieces, or listing all partitions) uses **Backtracking/DP**, which are out of scope for this string-only handbook. The string-relevant fact: precomputing a boolean table `is_pal[i][j]` for all substrings in O(n²) is the standard string-side preprocessing step that feeds into the DP/backtracking solution.

```python
def precompute_palindrome_table(s: str) -> list:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (length == 2) or dp[i+1][j-1]
    return dp
```
**Complexity:** O(n²) time, O(n²) space.

## 6.7 Common Palindrome Problems

| Problem | Technique | Difficulty |
|---|---|---|
| Valid Palindrome | Two pointers | Easy |
| Valid Palindrome II (one deletion allowed) | Two pointers + branch | Medium |
| Longest Palindromic Substring | Expand around center / Manacher | Medium |
| Palindromic Substrings (count) | Expand around center | Medium |
| Shortest Palindrome (prefix addition) | KMP on `s + '#' + reverse(s)` | Hard |

## Summary
Palindrome problems range from simple O(n) checks to the elegant O(n) Manacher's algorithm. The expand-around-center technique (O(n²)) is the practical interview default; Manacher's is the theoretical optimum, built on reusing symmetric information via a mirror index.

## Revision Notes
- `s == s[::-1]` for a quick check.
- Two-pointer check avoids the O(n) space of slicing.
- Expand around center handles 2n−1 centers for odd/even cases.
- Manacher's transforms the string with separators to unify odd/even handling and reuses palindrome radius info via mirroring.

## Cheat Sheet
```python
s == s[::-1]                         # O(n) check
# Expand around center template
def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]
```

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Direct reversal check | O(n) | O(n) |
| Two-pointer check | O(n) | O(1) |
| Brute force longest palindrome | O(n³) | O(1) |
| Expand around center | O(n²) | O(1) |
| Manacher's | O(n) | O(n) |

## Common Mistakes
- Forgetting the even-length center case (between two characters).
- Off-by-one in the boundary return of `expand()`.
- Applying DP-based partitioning logic when only a substring check was needed (over-engineering).

## FAQs
**Q: Is Manacher's algorithm required for interviews?**
A: Rarely required to implement from scratch, but understanding it demonstrates strong algorithmic maturity. Expand-around-center is usually sufficient.

**Q: Why insert `#` in Manacher's?**
A: To convert both odd- and even-length palindromes into odd-length palindromes in the transformed string, unifying the logic.

## Practice Problems
- Valid Palindrome — LeetCode: https://leetcode.com/problems/valid-palindrome/
- Valid Palindrome II — LeetCode: https://leetcode.com/problems/valid-palindrome-ii/
- Longest Palindromic Substring — LeetCode: https://leetcode.com/problems/longest-palindromic-substring/
- Palindromic Substrings — LeetCode: https://leetcode.com/problems/palindromic-substrings/
- Shortest Palindrome — LeetCode: https://leetcode.com/problems/shortest-palindrome/


# Chapter 7 — Pattern Matching

**Learning Objectives:** Fully derive and implement Naive Matching, KMP, Z-Algorithm, and Rabin-Karp, with complete dry runs.
**Prerequisites:** Chapters 1–6
**Estimated Reading Time:** 60 minutes
**Difficulty Level:** Advanced
**Interview Relevance:** High for senior/competitive-programming interviews.

## 7.1 Naive Pattern Matching

### Definition
Check every possible starting position in the text for a match with the pattern.

```python
def naive_search(text: str, pattern: str) -> list:
    n, m = len(text), len(pattern)
    positions = []
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            positions.append(i)
    return positions

print(naive_search("ababcababc", "abc"))  # [2, 7]
```
**Complexity:** Time O(n·m) worst case, Space O(1) extra (besides output).

### Dry Run — `text = "aaab"`, `pattern = "aab"`

| i | comparison | match? |
|---|---|---|
| 0 | "aaa" vs "aab" → mismatch at index 2 | No |
| 1 | "aab" vs "aab" | Yes! append 1 |

## 7.2 KMP Algorithm (Knuth–Morris–Pratt) — Full Derivation

### Why It Exists
Naive matching re-examines characters already known to match after a mismatch. KMP uses the **LPS array** (Chapter 4.17) to know how far to "slide" the pattern without re-checking known-matching characters, achieving O(n + m).

### Intuition
If a mismatch occurs after matching `k` characters, the LPS array tells us the pattern's longest prefix that is also a suffix of those `k` matched characters — we can resume from there instead of restarting.

```python
def compute_lps(pattern: str) -> list:
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps

def kmp_search(text: str, pattern: str) -> list:
    if not pattern:
        return []
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    positions = []
    i = j = 0  # i -> text index, j -> pattern index
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                positions.append(i - j)
                j = lps[j - 1]
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
    return positions
```

### Line-by-Line Explanation
1. `compute_lps` builds the failure function for the pattern (see 4.17 dry run).
2. `i` scans the text; `j` scans the pattern.
3. On a match, both advance; on full pattern match (`j == m`), record the position and fall back `j` using `lps`.
4. On mismatch with `j != 0`, fall back `j` to `lps[j-1]` instead of resetting to 0 — this is the key speedup, avoiding re-scanning `text[i]`.
5. On mismatch with `j == 0`, simply advance `i` (nothing to fall back to).

### Dry Run — `text = "ababcabcabababd"`, `pattern = "ababd"`

`lps("ababd") = [0, 0, 1, 2, 0]`

| i | j | text[i] | pattern[j] | action |
|---|---|---|---|---|
| 0 | 0 | a | a | match, i=1,j=1 |
| 1 | 1 | b | b | match, i=2,j=2 |
| 2 | 2 | a | a | match, i=3,j=3 |
| 3 | 3 | b | b | match, i=4,j=4 |
| 4 | 4 | c | d | mismatch, j=lps[3]=2 |
| 4 | 2 | c | a | mismatch, j=lps[1]=0 |
| 4 | 0 | c | a | mismatch, j=0, i=5 |
| ... | ... | ... (continues scanning) | | eventually finds match at index 10 |

**Complexity:** Time **O(n + m)** (amortized — `j` never decreases more total than it increases), Space O(m) for the LPS array.

### When to Use
Guaranteed linear-time matching with no collision risk; ideal for exact single-pattern search, especially with adversarial or repetitive input.
### When NOT to Use
Multiple pattern search (use Aho-Corasick — out of string-only scope, trie-based) or approximate matching.

## 7.3 Z-Algorithm — Full Derivation

### Definition
`Z[i]` = length of the longest substring starting at `i` that matches a prefix of the string (Z[0] is conventionally undefined/whole length).

### Why It Exists
Like KMP, but conceptually simpler: build one array over `pattern + '$' + text` and any position in the "text" section with `Z[i] >= len(pattern)` marks a match.

```python
def z_function(s: str) -> list:
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z

def z_search(text: str, pattern: str) -> list:
    combined = pattern + '$' + text
    z = z_function(combined)
    m = len(pattern)
    positions = []
    for i in range(m + 1, len(combined)):
        if z[i] >= m:
            positions.append(i - m - 1)
    return positions

print(z_search("ababcababc", "abc"))  # [2, 7]
```

### Line-by-Line Explanation
1. `z[0] = n` by convention (whole string matches itself).
2. `l, r` track the rightmost Z-box (substring matching a prefix) found so far.
3. If `i < r`, we can reuse `z[i - l]` (mirrored value) as a starting guess, bounded by `r - i` — same mirror idea as Manacher's.
4. Extend the match with direct comparison beyond the guess.
5. Update `l, r` if this Z-box extends further right.
6. In `z_search`, positions in the text part with `Z[i] >= len(pattern)` indicate the pattern fully matched starting there.

### Dry Run — `z_function("aabxaabxcaabxaabxay")` (abbreviated key steps)

| i | l,r before | initial guess | expand | z[i] | l,r after |
|---|---|---|---|---|---|
| 1 | 0,0 | 0 | compare s[0] vs s[1]: a vs a match, then b vs a mismatch | 1 | 1,2 |
| 2 | 1,2 | out of box (i>=r) | s[0] vs s[2]: a vs b mismatch | 0 | 1,2 |
| 4 | 1,2 | out of box | expand fully "aabx" matches prefix | 4 | 4,8 |

**Complexity:** Time **O(n + m)**, Space O(n + m) for the combined string and Z-array.

## 7.4 Rabin-Karp — Full Derivation

### Definition
Uses a rolling polynomial hash (Chapter 4.14) to compare pattern hash against every window hash in text in O(1) per window (after O(m) preprocessing), verifying actual equality only on hash matches to rule out collisions.

```python
def rabin_karp(text: str, pattern: str) -> list:
    n, m = len(text), len(pattern)
    if m > n or m == 0:
        return []
    B, M = 256, 1_000_000_007
    high_order = pow(B, m - 1, M)

    pat_hash = 0
    win_hash = 0
    for i in range(m):
        pat_hash = (pat_hash * B + ord(pattern[i])) % M
        win_hash = (win_hash * B + ord(text[i])) % M

    positions = []
    for i in range(n - m + 1):
        if pat_hash == win_hash:
            if text[i:i+m] == pattern:      # verify to defeat hash collisions
                positions.append(i)
        if i < n - m:
            win_hash = (win_hash - ord(text[i]) * high_order) % M
            win_hash = (win_hash * B + ord(text[i + m])) % M
            win_hash %= M
    return positions

print(rabin_karp("ababcababc", "abc"))  # [2, 7]
```

### Dry Run — `text = "abcab"`, `pattern = "cab"`, `B=10, M=101` (toy values for illustration)

| Step | window | hash calc | match pat_hash? |
|---|---|---|---|
| i=0 | "abc" | hash("abc") | pat_hash("cab") likely differs |
| i=1 | "bca" | roll: remove 'a', add 'b'? (illustrative) | differs |
| i=2 | "cab" | roll again | equals pat_hash → verify "cab"=="cab" → match at index 2 |

**Complexity:** Time **average O(n + m)**, worst case O(n·m) if many hash collisions occur (rare with a good modulus/base and verification step), Space O(1) extra.

## 7.5 Comparison Table

| Algorithm | Time (avg) | Time (worst) | Space | Collision Risk | Best For |
|---|---|---|---|---|---|
| Naive | O(n·m) | O(n·m) | O(1) | None | Small inputs, simplicity |
| KMP | O(n+m) | O(n+m) | O(m) | None | Guaranteed linear, adversarial input |
| Z-Algorithm | O(n+m) | O(n+m) | O(n+m) | None | Multiple related prefix queries |
| Rabin-Karp | O(n+m) | O(n·m) | O(1) | Yes (mitigated by verification) | Multiple pattern search, substring hashing |

## Summary
Naive matching is simple but quadratic. KMP achieves guaranteed linear time using the LPS "failure function" to avoid redundant comparisons. The Z-algorithm achieves the same bound via a single array built over `pattern + separator + text`. Rabin-Karp trades a small worst-case risk (mitigated by verification) for the flexibility of hashing, making it ideal when searching for many patterns simultaneously.

## Revision Notes
- KMP: precompute LPS, fall back `j` on mismatch instead of resetting to 0.
- Z-algorithm: build Z-array over `pattern + '$' + text`, matches where `Z[i] >= len(pattern)`.
- Rabin-Karp: rolling hash + mandatory verification step.
- All three achieve O(n+m); pick based on context (guarantee vs simplicity vs multi-pattern flexibility).

## Cheat Sheet
```python
compute_lps(pattern)              # KMP preprocessing
kmp_search(text, pattern)          # O(n+m) exact match positions
z_function(s)                       # Z-array
z_search(text, pattern)             # via combined string
rabin_karp(text, pattern)           # rolling hash search
```

## Complexity Summary
See Section 7.5 comparison table above.

## Common Mistakes
- Forgetting the verification step in Rabin-Karp (leads to false positives on hash collision).
- Off-by-one errors in LPS fallback (`lps[j-1]` not `lps[j]`).
- Using a poor modulus (e.g., too small) in Rabin-Karp, increasing collision probability.
- Forgetting the separator `'$'` between pattern and text in the Z-algorithm (without it, Z-values can spuriously cross the boundary).

## FAQs
**Q: Which algorithm should I use in an actual interview?**
A: KMP or Z-algorithm for guaranteed-correctness single-pattern search; mention Rabin-Karp when asked about multiple-pattern search or when hashing is the discussion topic.

**Q: Does Python's `in` operator already use one of these?**
A: CPython uses an optimized algorithm (a two-way string-matching variant) for substring search, giving strong practical performance without needing manual KMP/Z code in most applications.

## Practice Problems
- Implement strStr() — LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
- Repeated String Match — LeetCode: https://leetcode.com/problems/repeated-string-match/
- Shortest Palindrome (uses KMP) — LeetCode: https://leetcode.com/problems/shortest-palindrome/
- Search Pattern (KMP) — GfG: https://www.geeksforgeeks.org/problems/search-pattern0205/1
- Z Function practice — Codeforces EDU: https://codeforces.com/edu/course/2/lesson/3


# Chapter 8 — String Transformations

**Learning Objectives:** Master reversal, rotation, compression, encoding, normalization, and character replacement systems.
**Prerequisites:** Chapters 1–7
**Estimated Reading Time:** 30 minutes
**Difficulty Level:** Beginner–Intermediate

## 8.1 Reverse

```python
s = "hello"
print(s[::-1])                          # "olleh" — idiomatic, O(n)
print(''.join(reversed(s)))              # "olleh" — also O(n)

def reverse_manual(s):
    chars = list(s)
    l, r = 0, len(chars) - 1
    while l < r:
        chars[l], chars[r] = chars[r], chars[l]
        l += 1; r -= 1
    return ''.join(chars)
```

### Reverse Words in a Sentence
```python
def reverse_words(s: str) -> str:
    return ' '.join(reversed(s.split()))

print(reverse_words("the sky is blue"))   # "blue is sky the"
```

## 8.2 Rotate

### Definition
Shift characters left or right by `k` positions, wrapping around.

### ASCII Diagram
```
s = "abcdef", rotate left by 2:
Original:  a b c d e f
Rotated:   c d e f a b
           |<--2-->| moved to the end
```

```python
def rotate_left(s: str, k: int) -> str:
    k %= len(s)
    return s[k:] + s[:k]

def rotate_right(s: str, k: int) -> str:
    k %= len(s)
    return s[-k:] + s[:-k] if k else s

print(rotate_left("abcdef", 2))   # "cdefab"
print(rotate_right("abcdef", 2))  # "efabcd"
```
**Complexity:** O(n) time, O(n) space (new string).

### Checking If One String Is a Rotation of Another
```python
def is_rotation(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s2 in (s1 + s1)

print(is_rotation("waterbottle", "erbottlewat"))  # True
```
> **Interview Tip:** The `s2 in (s1 + s1)` trick works because any rotation of `s1` must appear as a contiguous substring of `s1` concatenated with itself.

## 8.3 Compression / Decompression

See Chapter 4.10–4.11 for Run-Length Encoding and in-place compression.

### Decompression
```python
import re
def rle_decode(s: str) -> str:
    result = []
    for ch, count in re.findall(r'([A-Za-z])(\d+)', s):
        result.append(ch * int(count))
    return ''.join(result)

print(rle_decode("a3b2c1"))  # "aaabbc"
```

## 8.4 Encoding / Decoding Schemes

```python
import base64
encoded = base64.b64encode("hello".encode('utf-8'))
print(encoded)                       # b'aGVsbG8='
print(base64.b64decode(encoded).decode('utf-8'))  # "hello"

# URL encoding
from urllib.parse import quote, unquote
print(quote("hello world!"))          # "hello%20world%21"
print(unquote("hello%20world%21"))    # "hello world!"
```

## 8.5 Normalization & Case Conversion

Unicode normalization ensures visually identical strings compare equal (e.g., composed vs decomposed accented characters).

```python
import unicodedata
s1 = "café"                              # composed é
s2 = "cafe\u0301"                        # e + combining accent
print(s1 == s2)                          # False! Different code point sequences
print(unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2))  # True
```

| Form | Meaning |
|---|---|
| NFC | Canonical Composition (preferred for storage/comparison) |
| NFD | Canonical Decomposition |
| NFKC | Compatibility Composition |
| NFKD | Compatibility Decomposition |

## 8.6 Character Replacement Systems

### Caesar Cipher
```python
def caesar_encrypt(s: str, shift: int) -> str:
    result = []
    for ch in s:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

print(caesar_encrypt("Hello, World!", 3))  # "Khoor, Zruog!"
```

## Summary
Reversal and rotation are O(n) idiomatic slicing operations. Compression algorithms (RLE) trade CPU for space savings on repetitive data. Encoding schemes (Base64, URL encoding) make binary/unsafe text transport-safe. Unicode normalization solves the "visually identical but not code-point-equal" trap.

## Revision Notes
- `s[::-1]` reverses; `s[k:] + s[:k]` rotates left by k.
- `s2 in (s1+s1)` checks rotation equivalence.
- Always normalize Unicode before comparing user-facing text from different sources.

## Cheat Sheet
```python
s[::-1]                     # reverse
s[k:] + s[:k]                # rotate left by k
s2 in (s1 + s1)              # rotation check
base64.b64encode(s.encode()) # base64 encode
unicodedata.normalize('NFC', s)  # normalize
```

## Complexity Summary
| Operation | Time | Space |
|---|---|---|
| Reverse | O(n) | O(n) |
| Rotate | O(n) | O(n) |
| RLE encode/decode | O(n) | O(n) |
| Base64 encode/decode | O(n) | O(n) |

## Common Mistakes
- Forgetting `k %= len(s)` before rotating (causes IndexError-free but wrong results, or errors if k > len(s) isn't handled).
- Comparing Unicode strings without normalization.
- Off-by-one errors implementing manual reversal with two pointers.

## FAQs
**Q: Is `s[::-1]` efficient for very large strings?**
A: Yes — it's a single O(n) C-level operation.

## Practice Problems
- Rotate String — LeetCode: https://leetcode.com/problems/rotate-string/
- Reverse Words in a String — LeetCode: https://leetcode.com/problems/reverse-words-in-a-string/
- Caesar Cipher — GfG: https://www.geeksforgeeks.org/problems/caesar-cipher1624/1
- Encode and Decode Strings — LeetCode: https://leetcode.com/problems/encode-and-decode-strings/

---

# Chapter 9 — Problem Recognition

**Learning Objectives:** Instantly recognize which pattern a given string problem calls for.
**Prerequisites:** Chapters 1–8
**Estimated Reading Time:** 15 minutes

## 9.1 Recognizing Sliding Window Problems
**Keywords:** "substring", "at most K", "longest/shortest contiguous", "without repeating".
**Signal:** Contiguous range + a constraint that can grow/shrink monotonically.

## 9.2 Recognizing Palindrome Problems
**Keywords:** "palindrome", "reads the same", "mirror".
**Signal:** Symmetry checks → two pointers or expand-around-center.

## 9.3 Recognizing Anagram Problems
**Keywords:** "anagram", "same characters", "rearrange".
**Signal:** Order doesn't matter, frequency does → Counter/sorting.

## 9.4 Recognizing Substring/Subsequence Problems
**Keywords:** "subsequence" (gaps allowed, DP likely) vs "substring" (contiguous, sliding window/two pointers likely).

## 9.5 Recognizing Pattern-Matching Problems
**Keywords:** "find all occurrences", "search pattern in text", "shortest string containing".
**Signal:** Needle-in-haystack → KMP/Z/Rabin-Karp.

## 9.6 Master Decision Flowchart

```
Is order irrelevant, only frequency matters?
   YES -> Anagram/Frequency pattern (Counter)
   NO  -> continue

Does the problem need a contiguous range satisfying a constraint?
   YES -> Sliding Window
   NO  -> continue

Is symmetry (same forwards/backwards) involved?
   YES -> Palindrome techniques (two pointer / expand center / Manacher)
   NO  -> continue

Is it "find pattern P inside text T"?
   YES -> KMP / Z / Rabin-Karp
   NO  -> continue

Is order preserved but gaps allowed ("subsequence")?
   YES -> Likely Dynamic Programming (out of string-only scope)
   NO  -> Re-read the problem statement — you're missing a keyword.
```

---

# Chapter 10 — Optimization Playbook

**Learning Objectives:** Learn the systematic ladder from brute force to optimal for string problems.
**Estimated Reading Time:** 15 minutes

## 10.1 Brute Force → Better → Optimal Ladder

| Stage | Typical Complexity | Typical Technique |
|---|---|---|
| Brute Force | O(n²) or O(n³) | Nested loops, generate all substrings |
| Better | O(n log n) | Sorting-based comparison |
| Optimal | O(n) | Hashing, two pointers, sliding window, KMP/Z |

**Example ladder — Longest Substring Without Repeats:**
1. Brute force: check every substring for uniqueness — O(n³).
2. Better: use a set, but restart window entirely on duplicate — O(n²).
3. Optimal: sliding window with last-seen index map — O(n).

## 10.2 Building Observations

Ask, in order:
1. Does character **order** matter? (anagram vs substring)
2. Is the range **contiguous**? (window vs subsequence)
3. Can I **precompute** something once and query in O(1) (prefix sums, LPS array)?
4. Is there **symmetry** I can exploit (palindromes)?
5. Can I avoid re-scanning matched characters (KMP's core insight)?

## 10.3 Space Optimization Techniques

- Use **fixed-size arrays** (size 26/128/256) instead of hash maps when alphabet is known and small.
- Use **in-place two-pointer swapping** instead of creating new strings/lists.
- Prefer **generators** (`(x for x in s)`) over building intermediate lists when only iterating once.

---

# Chapter 11 — Interview Preparation

**Learning Objectives:** Curated question bank organized by difficulty and pattern.
**Estimated Reading Time:** 20 minutes

## 11.1 Easy/Medium/Hard Question Bank

**Easy**
- Valid Anagram — https://leetcode.com/problems/valid-anagram/
- Valid Palindrome — https://leetcode.com/problems/valid-palindrome/
- Reverse String — https://leetcode.com/problems/reverse-string/
- Implement strStr() — https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
- Roman to Integer — https://leetcode.com/problems/roman-to-integer/

**Medium**
- Longest Substring Without Repeating Characters — https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Longest Palindromic Substring — https://leetcode.com/problems/longest-palindromic-substring/
- Group Anagrams — https://leetcode.com/problems/group-anagrams/
- String to Integer (atoi) — https://leetcode.com/problems/string-to-integer-atoi/
- Zigzag Conversion — https://leetcode.com/problems/zigzag-conversion/

**Hard**
- Minimum Window Substring — https://leetcode.com/problems/minimum-window-substring/
- Shortest Palindrome — https://leetcode.com/problems/shortest-palindrome/
- Text Justification — https://leetcode.com/problems/text-justification/
- Distinct Subsequences (DP-adjacent, string setup) — https://leetcode.com/problems/distinct-subsequences/

## 11.2 Pattern-wise Question Map

| Pattern | Representative Problems |
|---|---|
| Sliding Window | Longest Substring Without Repeats, Minimum Window Substring |
| Two Pointers | Valid Palindrome, Valid Palindrome II |
| Frequency/Anagram | Valid Anagram, Group Anagrams, Ransom Note |
| Palindrome Expansion | Longest Palindromic Substring, Palindromic Substrings |
| Pattern Matching | Implement strStr(), Repeated String Match |
| Transformation | Reverse Words, Rotate String |

## 11.3 Company-wise Notes

> **Note:** Company-specific question sets change frequently. Rather than memorizing a static list (which goes stale quickly), practice the *patterns* in 11.2 — they generalize across all companies' string questions. For up-to-date company tags, check LeetCode's "Company" filter (subscription feature) or GfG's company-tagged problem lists.

## 11.4 Blind 75 / NeetCode String List

The commonly cited "Blind 75" string problems include: Longest Substring Without Repeating Characters, Longest Repeating Character Replacement, Minimum Window Substring, Valid Anagram, Group Anagrams, Valid Palindrome, Longest Palindromic Substring, Palindromic Substrings, Encode and Decode Strings.
Reference list: https://neetcode.io/practice

## 11.5 Interview Tricks & Gotchas

- Always clarify: case sensitivity? Unicode/ASCII only? Empty string as valid input?
- State the brute force first, then optimize out loud — interviewers weight communication heavily.
- For sliding window, always verbally state your **invariant** ("the window always contains at most K distinct characters").
- For palindrome problems, always ask about even vs odd length handling.
- Mention time/space complexity **before** being asked.

---

# Chapter 12 — Python String Tips & Internals

**Learning Objectives:** Squeeze maximum performance and Pythonic elegance from string code.
**Estimated Reading Time:** 20 minutes

## 12.1 Built-in Method Performance
Built-in methods (`str.replace`, `str.find`, etc.) are implemented in C and are almost always faster than hand-rolled Python loops for the same task. Prefer them when available.

## 12.2 collections.Counter
```python
from collections import Counter
c = Counter("mississippi")
print(c.most_common(2))     # [('i', 4), ('s', 4)]
c2 = Counter("bob")
print(c - c2)                 # Counter subtraction, only positive counts kept
```

## 12.3 collections.defaultdict
```python
from collections import defaultdict
groups = defaultdict(list)
for word in ["eat", "tea", "tan", "ate", "nat", "bat"]:
    key = ''.join(sorted(word))
    groups[key].append(word)
print(dict(groups))
```

## 12.4 The `string` Module
```python
import string
print(string.ascii_lowercase)   # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)             # '0123456789'
print(string.punctuation)        # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.whitespace)         # ' \t\n\r\x0b\x0c'
```

## 12.5 Basics of `re` for String Processing
```python
import re
print(re.findall(r'\d+', "room 42, floor 3"))     # ['42', '3']
print(re.sub(r'\s+', ' ', "too    many   spaces")) # "too many spaces"
print(bool(re.match(r'^[A-Za-z]+$', "hello")))       # True
```
> **Scope Note:** `re` is a vast topic on its own; here it's covered only as a string-processing tool, not as a full regex handbook.

## 12.6 Pythonic Idioms
```python
# Check all chars are digits
"12345".isdigit()

# Build string from list efficiently
''.join(str(x) for x in range(10))

# Swap-free multiple assignment for readability
a, b = "hello", "world"

# Chained conditions
if "a" <= ch <= "z":
    ...
```

## 12.7 Performance & Memory Tips
- Avoid `+=` string concatenation in large loops; use `list.append` + `''.join()`.
- Use `str.translate()` over chained `.replace()` for many single-char substitutions.
- For very large text processing, consider `io.StringIO` for stream-like building.
- Fixed-size arrays (`[0]*26`) beat dict-based counters when the alphabet is small and known.

---

# Chapter 13 — Common Mistakes

**Estimated Reading Time:** 10 minutes

## 13.1 Off-by-One Errors
`range(i+1, n+1)` vs `range(i+1, n)` mistakes when generating substrings; forgetting slicing's `stop` is exclusive.

## 13.2 Unicode Bugs
Assuming `len()` equals byte count or visual glyph count; not normalizing before comparison.

## 13.3 Encoding Issues
Mixing `str` and `bytes` without explicit `.encode()`/`.decode()`, causing `TypeError`.

## 13.4 Case Sensitivity Bugs
Forgetting `.lower()`/`.casefold()` before comparison in case-insensitive contexts (`casefold()` is more aggressive and correct for many languages than `lower()`).

## 13.5 Whitespace Bugs
Forgetting `.strip()` on user input read from files/stdin, leading to failed equality checks.

## 13.6 Substring Errors
Confusing `find` (-1 on miss) with `index` (raises exception); assuming `in` gives position instead of boolean.

## 13.7 Split/Join Mistakes
`"a,,b".split(",")` gives `['a', '', 'b']` — forgetting empty strings appear with explicit separators (unlike default `.split()`).

## 13.8 Immutability Bugs
Trying `s[0] = 'x'` directly; not realizing every "mutating" method returns a **new** string that must be reassigned.

## 13.9 Performance Anti-Patterns
`result = ""` then `result += x` inside a large loop; using `+` for many small concatenations instead of `''.join()`.

---

# Chapter 14 — Cheat Sheets

## 14.1 Method Cheat Sheet
```python
s.strip(); s.lstrip(); s.rstrip()
s.split(); s.split(","); s.rsplit(",", 1)
','.join(lst)
s.replace(a, b)
s.find(a); s.index(a); s.count(a)
s.startswith(a); s.endswith(a)
s.lower(); s.upper(); s.title(); s.capitalize(); s.swapcase()
s.center(w); s.ljust(w); s.rjust(w); s.zfill(w)
s.isalnum(); s.isalpha(); s.isdigit(); s.isspace()
s.encode('utf-8'); b.decode('utf-8')
s.translate(str.maketrans(a, b))
```

## 14.2 Complexity Cheat Sheet
| Operation | Complexity |
|---|---|
| Index/length | O(1) |
| Slice | O(k) |
| Concatenation (single) | O(n) |
| `in` / find / count | O(n·m) worst, ~O(n) average |
| Sort-based anagram check | O(n log n) |
| Counter-based anagram check | O(n) |
| KMP / Z / Rabin-Karp (avg) | O(n+m) |
| Manacher | O(n) |

## 14.3 Pattern Cheat Sheet
| Trigger Words | Pattern |
|---|---|
| "longest/shortest substring with constraint" | Sliding Window |
| "palindrome" | Two Pointers / Expand Center / Manacher |
| "anagram" | Frequency Counter |
| "find pattern in text" | KMP / Z / Rabin-Karp |
| "rotation" | `s2 in (s1+s1)` trick |
| "compress repeated chars" | Run-Length Encoding |

## 14.4 Recognition Cheat Sheet
See Chapter 9.6 Decision Flowchart.

## 14.5 Syntax Cheat Sheet
```python
s[start:stop:step]
f"{value:.2f}"
r"raw\string"
"""triple
quoted"""
```

## 14.6 Interview Cheat Sheet
- State brute force → optimize → state final complexity.
- Clarify constraints (case sensitivity, charset, empty input) before coding.
- Use `Counter`/`dict` for frequency; two pointers for symmetry; sliding window for contiguous constraints.

---

# Chapter 15 — Practice Problems (Categorized)

## Basics
- Reverse String — LeetCode: https://leetcode.com/problems/reverse-string/
- Valid Anagram — LeetCode: https://leetcode.com/problems/valid-anagram/

## Palindrome
- Valid Palindrome — LeetCode: https://leetcode.com/problems/valid-palindrome/
- Longest Palindromic Substring — LeetCode: https://leetcode.com/problems/longest-palindromic-substring/
- Palindrome Partitioning (string-prep only) — LeetCode: https://leetcode.com/problems/palindrome-partitioning/

## Substring
- Longest Common Prefix — LeetCode: https://leetcode.com/problems/longest-common-prefix/
- Minimum Window Substring — LeetCode: https://leetcode.com/problems/minimum-window-substring/

## Subsequence
- Is Subsequence — LeetCode: https://leetcode.com/problems/is-subsequence/

## Sliding Window
- Longest Substring Without Repeating Characters — LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Longest Repeating Character Replacement — LeetCode: https://leetcode.com/problems/longest-repeating-character-replacement/

## Pattern Matching
- Implement strStr() — LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
- Repeated String Match — LeetCode: https://leetcode.com/problems/repeated-string-match/
- Search Pattern (KMP) — GfG: https://www.geeksforgeeks.org/problems/search-pattern0205/1

## Compression
- String Compression — LeetCode: https://leetcode.com/problems/string-compression/
- Run Length Encoding — GfG: https://www.geeksforgeeks.org/problems/run-length-encoding/1

## Easy
- Ransom Note — LeetCode: https://leetcode.com/problems/ransom-note/
- Roman to Integer — LeetCode: https://leetcode.com/problems/roman-to-integer/

## Medium
- Group Anagrams — LeetCode: https://leetcode.com/problems/group-anagrams/
- Zigzag Conversion — LeetCode: https://leetcode.com/problems/zigzag-conversion/

## Hard
- Text Justification — LeetCode: https://leetcode.com/problems/text-justification/
- Shortest Palindrome — LeetCode: https://leetcode.com/problems/shortest-palindrome/

## More Platforms
- Codeforces String problems: https://codeforces.com/problemset?tags=strings
- CodeChef String problems: https://www.codechef.com/practice/tags/strings
- AtCoder: https://atcoder.jp/
- HackerRank Strings track: https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=strings
- InterviewBit Strings: https://www.interviewbit.com/strings-interview-questions/

---

# Chapter 16 — Final Revision

## 16.1 One-Page Revision

- **Indexing:** `s[i]`, negative `s[-1]`. **Slicing:** `s[a:b:c]`, stop exclusive.
- **Immutability:** every "modification" returns a new string.
- **Search:** `find`(-1)/`index`(exception)/`count`(non-overlapping)/`in`(bool).
- **Case:** `lower/upper/title/capitalize/swapcase`.
- **Pad:** `center/ljust/rjust/zfill`.
- **Split/Join:** `split()` drops empties on whitespace; explicit sep keeps them; `join` builds.
- **Patterns:** frequency (Counter), sliding window (contiguous+constraint), two pointers (symmetry), expand-center/Manacher (palindrome), KMP/Z/Rabin-Karp (search).
- **Complexity defaults:** most single-pass string ops are O(n); matching algorithms are O(n+m).

## 16.2 Mind Map (Text Form)
```
STRINGS
├── Fundamentals (encoding, immutability, indexing, slicing)
├── Operations (40+ built-in methods)
├── Patterns
│   ├── Frequency / Anagram
│   ├── Sliding Window
│   ├── Two Pointers
│   ├── Palindrome (expand center, Manacher)
│   └── Pattern Matching (Naive, KMP, Z, Rabin-Karp)
├── Substrings & Subsequences
├── Transformations (reverse, rotate, compress, encode)
└── Interview Layer (recognition, optimization, cheat sheets)
```

## 16.3 Pattern Map
| If problem mentions... | Use... |
|---|---|
| unique/distinct chars in a window | Sliding Window |
| mirror/symmetry | Two Pointers / Palindrome expansion |
| rearrangement equality | Frequency Counter |
| find occurrences of pattern | KMP / Z / Rabin-Karp |
| compress repeats | RLE |

## 16.4 Decision Tree
See Chapter 9.6.

## 16.5 Formula Sheet
```
Total substrings of length n         = n(n+1)/2
Total subsequences (incl. empty)      = 2^n
ord('a') - ord('A')                    = 32
Rolling hash update: H' = ((H - s[i]*B^(k-1)) * B + s[i+k]) mod M
```

## 16.6 15-Minute Revision
1. Re-read Section 16.1.
2. Re-derive `s[::-1]`, two-pointer palindrome check, and sliding window template from memory.
3. Recall `find` vs `index` vs `count` differences.
4. Recall KMP's one-line idea: "use LPS to avoid re-scanning matched characters."

## 16.7 1-Hour Revision
1. Re-implement from memory: frequency counter, two-pointer palindrome, sliding window (longest unique substring), expand-around-center, KMP with LPS, Rabin-Karp.
2. Solve 3 problems from Chapter 15 (one Easy, one Medium, one Hard) without looking at notes.
3. Review Chapter 13 (Common Mistakes) as a final gut-check.
4. Skim Chapter 14 cheat sheets once more before the interview.

---
