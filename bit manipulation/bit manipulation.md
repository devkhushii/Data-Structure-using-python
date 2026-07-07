# The Complete Bit Manipulation Handbook (
---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Python & Bit Manipulation](#2-python--bit-manipulation)
3. [Binary Number System](#3-binary-number-system)
4. [Bitwise Operators](#4-bitwise-operators)
   - [4.1 AND (&)](#41-and-)
   - [4.2 OR (|)](#42-or-)
   - [4.3 XOR (^)](#43-xor-)
   - [4.4 NOT (~)](#44-not-)
   - [4.5 Left Shift (<<)](#45-left-shift-)
   - [4.6 Right Shift (>>)](#46-right-shift-)
5. [Bit Manipulation Fundamentals](#5-bit-manipulation-fundamentals)
6. [Bit Manipulation Patterns](#6-bit-manipulation-patterns)
7. [Advanced Concepts](#7-advanced-concepts)
8. [Real-World Applications](#8-real-world-applications)
9. [Problem Recognition](#9-problem-recognition)
10. [Optimization Playbook](#10-optimization-playbook)
11. [Interview Preparation](#11-interview-preparation)
12. [Python Tips & Idioms](#12-python-tips--idioms)
13. [Common Mistakes](#13-common-mistakes)
14. [Cheat Sheets](#14-cheat-sheets)
15. [Practice Problems](#15-practice-problems)
16. [Final Revision](#16-final-revision)

---

## 1. Introduction

### 1.1 What is Bit Manipulation?

**Definition:** Bit manipulation is the technique of directly working with the individual bits (0s and 1s) that make up a number's binary representation, using bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) instead of arithmetic on the "whole" number.

**Why it exists:** CPUs are fundamentally digital circuits that only understand two voltage levels — high and low, mapped to `1` and `0`. Every arithmetic operation a computer performs is, underneath, a sequence of bitwise operations executed by logic gates. Bit manipulation exposes that layer directly to the programmer, enabling:

- Extreme speed (single CPU instructions instead of loops)
- Extreme memory efficiency (packing many boolean flags into one integer)
- Solving problems that are naturally about "which bits are on" (subsets, parity, permissions)

> **Analogy:** Think of a row of light switches on a wall. Each switch is either ON or OFF. A binary number is just that row of switches read left to right. Bitwise operators are ways of flipping, comparing, or combining rows of switches *all at once*, rather than one switch at a time.

### 1.2 A Brief History

- **1679** — Gottfried Leibniz formalizes the binary number system.
- **1854** — George Boole publishes *An Investigation of the Laws of Thought*, founding Boolean algebra (AND/OR/NOT).
- **1937** — Claude Shannon's MIT thesis shows Boolean algebra can model electrical switching circuits — the theoretical birth of digital computing.
- **1940s–50s** — Early computers (ENIAC, EDVAC) adopt binary storage and arithmetic because it maps perfectly to two-state electronic components (on/off, charged/uncharged).
- **1970s onward** — C exposes bitwise operators directly to programmers; the tradition carries into virtually every modern language, including Python.

### 1.3 Bits, Nibbles, Bytes, Words

| Unit | Size | Example |
|---|---|---|
| Bit | 1 binary digit (0 or 1) | `1` |
| Nibble | 4 bits | `1010` |
| Byte | 8 bits | `10101100` |
| Word | Platform-dependent (commonly 32 or 64 bits) | `00000000000000000000000000101100` |

```
Byte layout (8 bits), Most Significant Bit (MSB) on the left:

 MSB                         LSB
  ↓                           ↓
+---+---+---+---+---+---+---+---+
| 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
+---+---+---+---+---+---+---+---+
 128  64  32  16   8   4   2   1   <- place values (powers of 2)
```

### 1.4 Number Systems at a Glance

| System | Base | Digits Used | Prefix in Python |
|---|---|---|---|
| Binary | 2 | 0, 1 | `0b` |
| Octal | 8 | 0–7 | `0o` |
| Decimal | 10 | 0–9 | *(none)* |
| Hexadecimal | 16 | 0–9, A–F | `0x` |

**Why hex matters:** 1 hex digit = exactly 4 bits (a nibble), so hex is a compact, human-friendly way to write binary. `0xAC` = `10101100`.

### 1.5 Advantages of Bit Manipulation

- **Speed:** Bitwise ops are O(1) hardware instructions — often 1 CPU cycle.
- **Memory:** Store 32 boolean flags in a single 32-bit integer instead of 32 separate booleans.
- **Elegance:** Many problems (subsets, toggling, parity, unique elements) collapse into a few lines.
- **No extra space:** Many bit tricks solve problems in O(1) extra space where array-based approaches need O(n).

### 1.6 Disadvantages / Trade-offs

- **Readability:** `n & (n - 1)` is unreadable to someone unfamiliar with the trick — needs comments.
- **Portability pitfalls (in other languages):** Fixed-width overflow, signed/unsigned confusion — Python mostly avoids this due to arbitrary-precision integers, but you must understand it for interviews and for languages like C++/Java.
- **Debuggability:** Bugs in bitwise logic can be subtle (off-by-one bit positions, wrong masks).
- **Not always the clearest first solution:** Sometimes a bitmask solution should be presented after a brute-force explanation so the reasoning is clear.

### 1.7 Real-World Applications (Preview)

| Domain | Use of Bit Manipulation |
|---|---|
| Operating Systems | File permission bits (`rwxrwxrwx`), process flags |
| Networking | IP subnet masks, checksums, packet flags |
| Graphics | Pixel color packing (RGBA in 32 bits), image masks |
| Cryptography | XOR ciphers, hashing, block cipher rounds |
| Databases | Bitmap indexes, boolean flag columns packed into bitmasks |
| Embedded Systems | Direct hardware register manipulation (GPIO pins) |
| Competitive Programming | Bitmask DP, subset enumeration, XOR tricks |
| Compression | Huffman coding, run-length encoding at the bit level |

---
## 2. Python & Bit Manipulation

### 2.1 Integers in Python Are Special

Unlike C++/Java, Python's `int` has **arbitrary precision** — it grows automatically to fit any value, and there is no fixed bit-width (no 32-bit/64-bit overflow). Internally, CPython stores large integers as an array of "digits" in base 2³⁰ (implementation detail), but conceptually you should treat Python integers as **infinite-precision, sign-extended binary numbers**.

> **Key Insight:** In Python, there's no overflow. `2**1000` just works. This is a huge relief compared to C++, but it also means you must be *extra* careful with bitmask sizes when you actually want fixed-width (e.g., 32-bit) behavior — Python won't do it for you.

### 2.2 Core Built-in Tools

| Function / Method | Purpose | Example |
|---|---|---|
| `bin(n)` | Decimal → binary string (`0b` prefix) | `bin(10)` → `'0b1010'` |
| `oct(n)` | Decimal → octal string | `oct(10)` → `'0o12'` |
| `hex(n)` | Decimal → hex string | `hex(10)` → `'0xa'` |
| `int(s, base)` | String (any base) → decimal int | `int('1010', 2)` → `10` |
| `format(n, spec)` | Custom formatted string | `format(10, '08b')` → `'00001010'` |
| `f'{n:08b}'` | f-string binary formatting | `f'{10:08b}'` → `'00001010'` |
| `n.bit_length()` | Number of bits needed (excluding sign) | `(10).bit_length()` → `4` |
| `n.to_bytes(len, 'big')` | Int → bytes object | `(10).to_bytes(2,'big')` → `b'\x00\n'` |
| `int.from_bytes(b, 'big')` | Bytes → int | `int.from_bytes(b'\x00\n','big')` → `10` |
| `n.bit_count()` (3.10+) | Number of set bits (popcount) | `(10).bit_count()` → `2` |

```python
n = 10

print(bin(n))              # '0b1010'
print(oct(n))               # '0o12'
print(hex(n))                # '0xa'
print(format(n, '#010b'))    # '0b00001010' (width 10 incl. '0b')
print(f'{n:08b}')            # '00001010'
print(n.bit_length())        # 4
print(n.bit_count())         # 2 (Python 3.10+)
print(n.to_bytes(2, 'big'))  # b'\x00\n'
print(int.from_bytes(b'\x00\n', 'big'))  # 10
```

**Line-by-line explanation:**
1. `bin(n)` returns a string prefixed with `0b`; slice `[2:]` to drop the prefix if needed.
2. `format(n, '08b')` pads with leading zeros to width 8 — the most common way to display a fixed-width binary string in Python.
3. `bit_length()` returns the minimum number of bits to represent `abs(n)` in binary, excluding sign and leading zeros — critical for computing MSB position.
4. `bit_count()` is the modern (3.10+) built-in replacement for the classic `bin(n).count('1')` popcount trick.
5. `to_bytes`/`from_bytes` convert between integers and raw byte sequences — used in networking, file formats, and cryptography.

### 2.3 Negative Numbers in Python (Important!)

Python does **not** use fixed-width two's complement storage for negative integers the way C/C++/Java do. Conceptually, Python treats negative numbers as having an **infinite sign-extension of 1-bits** to the left.

```python
print(bin(-5))   # '-0b101'   <-- Python prints sign + magnitude, NOT two's complement!
```

This is a common **trap**: `bin(-5)` does *not* show you the two's complement bit pattern. If you want the true two's complement bit pattern (like you'd see in C++ for a 32-bit int), you must mask explicitly:

```python
def twos_complement_bits(n: int, bits: int = 32) -> str:
    """Return the 'bits'-wide two's complement binary string for n."""
    mask = (1 << bits) - 1        # e.g., 0xFFFFFFFF for 32 bits
    return format(n & mask, f'0{bits}b')

print(twos_complement_bits(-5, 8))   # '11111011' (8-bit two's complement of -5)
print(twos_complement_bits(-5, 32))  # '11111111111111111111111111111011'
```

**Dry run** (`twos_complement_bits(-5, 8)`):

| Step | Expression | Value | Explanation |
|---|---|---|---|
| 1 | `bits = 8` | 8 | Width requested |
| 2 | `mask = (1 << 8) - 1` | `0b11111111` (255) | All 8 bits set |
| 3 | `n & mask` = `-5 & 255` | `251` | Python computes this correctly using infinite sign extension internally, masked to 8 bits |
| 4 | `format(251, '08b')` | `'11111011'` | Zero-padded 8-bit binary string |

> **Note:** This masking trick (`n & mask`) is the standard way to simulate fixed-width (8/16/32/64-bit) integer behavior in Python — essential for interview problems that assume C++/Java-style overflow.

### 2.4 Performance Considerations

- Bitwise operators on small ints are extremely fast (implemented as single C-level operations in CPython for machine-word-sized ints).
- For very large integers (thousands of bits), operations become O(k) where k is the number of machine words — still typically much faster than equivalent loops.
- Prefer built-in `bit_count()` over manual popcount loops for performance and readability (Python 3.10+).
- Avoid repeated `bin(n)` string conversions in hot loops — string operations are much slower than integer bitwise ops.

### 2.5 Best Practices

- Always be explicit about bit-width (`mask = (1 << 32) - 1`) when simulating fixed-width arithmetic.
- Use `format(n, '0{}b'.format(width))` or f-strings for clean, padded binary output.
- Prefer `n.bit_count()` (3.10+) over `bin(n).count('1')` for clarity and speed.
- Comment bit tricks — `n & (n - 1)` should always have an inline comment explaining intent for maintainability.
- Use named constants for masks (`READ = 1 << 0`, `WRITE = 1 << 1`) instead of magic numbers.

---
## 3. Binary Number System

### 3.1 Place Values

Binary is base-2 positional notation. Each position represents a power of 2, read right to left starting at 2⁰.

```
Binary:      1    0    1    1
Position:    3    2    1    0
Value:      2³   2²   2¹   2⁰
           = 8    4    2    1

1*8 + 0*4 + 1*2 + 1*1 = 11 (decimal)
```

### 3.2 Decimal → Binary (Division Method)

**Algorithm:** Repeatedly divide by 2, collect remainders bottom-up.

```python
def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    sign = "-" if n < 0 else ""
    n = abs(n)
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return sign + "".join(reversed(bits))

print(decimal_to_binary(11))  # '1011'
```

**Dry run for n = 11:**

| Step | n | n % 2 (bit) | n // 2 |
|---|---|---|---|
| 1 | 11 | 1 | 5 |
| 2 | 5 | 1 | 2 |
| 3 | 2 | 0 | 1 |
| 4 | 1 | 1 | 0 (stop) |

Reading remainders bottom-up: `1011` ✅

### 3.3 Binary → Decimal (Positional Sum)

```python
def binary_to_decimal(b: str) -> int:
    result = 0
    for ch in b:
        result = result * 2 + int(ch)   # Horner's method
    return result

print(binary_to_decimal("1011"))  # 11
```

**Line-by-line:** Each iteration shifts the accumulated result left by 1 bit (`result * 2`) and adds the new bit — this is Horner's method applied to base 2, avoiding explicit power computation.

### 3.4 Binary Arithmetic

**Addition** (like decimal addition, but carry happens at 2 instead of 10):

```
   1 0 1 1   (11)
 + 0 1 1 0   ( 6)
 ---------
 1 0 0 0 1   (17)

Bit-by-bit (right to left):
1+0=1        no carry
1+1=10 -> write 0, carry 1
0+1+carry1=10 -> write 0, carry 1
1+0+carry1=10 -> write 0, carry 1
carry1 -> write 1
Result: 10001 = 17 ✓
```

**Subtraction via two's complement:** `A - B == A + (~B + 1)` — this is *why* two's complement exists: it lets hardware use the same adder circuit for both addition and subtraction.

### 3.5 Signed Numbers: One's & Two's Complement

| Representation | Rule | Example (4-bit, value -3) |
|---|---|---|
| Sign-Magnitude | MSB = sign, rest = magnitude | `1011` (sign=1, magnitude=011=3) |
| One's Complement | Flip all bits of positive value | `~0011` = `1100` |
| Two's Complement | One's complement + 1 | `1100 + 1` = `1101` |

**Two's complement is the industry standard** because:
1. There's only one representation of zero (`0000`), unlike one's complement which has `+0` and `-0`.
2. Addition/subtraction use the same circuit — no special-casing for sign.

```python
def to_twos_complement(n: int, bits: int = 4) -> str:
    if n >= 0:
        return format(n, f'0{bits}b')
    return format((1 << bits) + n, f'0{bits}b')

print(to_twos_complement(-3, 4))   # '1101'
print(to_twos_complement(3, 4))    # '0011'
```

**ASCII visualization — 4-bit two's complement wheel:**

```
        0000 (0)
   1111        0001
   (-1)         (1)
1110              0010
(-2)               (2)
 1101              0011
 (-3)               (3)
   1100          0100
   (-4)          (4)
       1011  0101
        ...
   Range: -8 (1000) to 7 (0111)
```

### 3.6 Signed vs Unsigned in Fixed-Width Systems

| Bit Pattern (8-bit) | Unsigned Value | Signed (Two's Complement) Value |
|---|---|---|
| `00000000` | 0 | 0 |
| `01111111` | 127 | 127 |
| `10000000` | 128 | -128 |
| `11111111` | 255 | -1 |

> **Warning:** Python integers are NOT fixed-width, so this table applies to *simulated* 8/32/64-bit behavior (common in interview questions ported from C++/Java), not to native Python ints.

### 3.7 Overflow (Conceptual, for Interview Awareness)

In a fixed-width system (e.g., 32-bit signed int), adding 1 to the maximum value wraps around to the minimum negative value. Python doesn't do this natively — but many interview problems (e.g., "Sum of Two Integers without +") expect you to simulate 32-bit overflow using masking:

```python
def add_no_plus(a: int, b: int) -> int:
    mask = 0xFFFFFFFF  # 32-bit mask
    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask
    # if result overflows into negative range (bit 31 set), convert back
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

print(add_no_plus(3, 5))    # 8
print(add_no_plus(-1, 1))   # 0
```

### 3.8 Endianness (Overview)

- **Big-endian:** Most significant byte stored first (network byte order).
- **Little-endian:** Least significant byte stored first (x86/x64 native).

```python
n = 1
print(n.to_bytes(4, 'big'))     # b'\x00\x00\x00\x01'
print(n.to_bytes(4, 'little'))  # b'\x01\x00\x00\x00'
```

---
## 4. Bitwise Operators

### 4.1 AND (`&`)

**Definition:** Result bit is `1` only if *both* corresponding input bits are `1`.

**Truth Table:**

| A | B | A & B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Why it exists:** Models the logical "both conditions must hold" — in circuits, an AND gate only outputs high voltage when both inputs are high.

```
  1 0 1 1   (11)
& 0 1 1 0   ( 6)
---------
  0 0 1 0   ( 2)
```

```python
a, b = 11, 6
print(a & b)          # 2
print(bin(a & b))     # '0b10'
```

**Applications:** Checking a specific bit (`n & (1 << i)`), masking off unwanted bits, checking evenness (`n & 1`), intersection of bitmask sets.

**Interview question example:** *"Check if a number is even without using `%`."*
```python
def is_even(n: int) -> bool:
    return (n & 1) == 0   # last bit 0 means even
```

### 4.2 OR (`|`)

**Definition:** Result bit is `1` if *at least one* input bit is `1`.

**Truth Table:**

| A | B | A \| B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

```
  1 0 1 1   (11)
| 0 1 1 0   ( 6)
---------
  1 1 1 1   (15)
```

```python
a, b = 11, 6
print(a | b)   # 15
```

**Applications:** Setting a specific bit (`n | (1 << i)`), combining flags/permissions, union of bitmask sets.

### 4.3 XOR (`^`)

**Definition:** Result bit is `1` if the input bits *differ*.

**Truth Table:**

| A | B | A ^ B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

```
  1 0 1 1   (11)
^ 0 1 1 0   ( 6)
---------
  1 1 0 1   (13)
```

```python
a, b = 11, 6
print(a ^ b)   # 13
```

**Fundamental XOR properties (memorize these — they power an entire family of interview problems):**

| Property | Meaning |
|---|---|
| `a ^ a = 0` | Self-cancellation |
| `a ^ 0 = a` | Identity element |
| `a ^ b = b ^ a` | Commutative |
| `(a ^ b) ^ c = a ^ (b ^ c)` | Associative |
| `a ^ b ^ a = b` | Cancellation regardless of order |

> **Why XOR is special:** It's the only common bitwise op that's its own inverse (`a ^ b ^ b = a`), making it perfect for toggling bits, swapping values without a temp variable, and finding "the odd one out" among duplicates.

**Toggling a bit:** `n ^ (1 << i)` flips bit `i`.

### 4.4 NOT (`~`)

**Definition:** Flips every bit — `0` becomes `1`, `1` becomes `0`.

**Truth Table:**

| A | ~A |
|---|---|
| 0 | 1 |
| 1 | 0 |

**Critical Python-specific behavior:** `~n` in Python equals `-(n + 1)`, because of infinite two's-complement sign extension.

```python
print(~5)    # -6   (since ~n = -n - 1)
print(~0)    # -1
print(~-1)   # 0
```

**Dry run for `~5`:**

| Step | Value | Explanation |
|---|---|---|
| 1 | `5` = `...0000101` | conceptually infinite leading zeros |
| 2 | flip all bits | `...1111010` (infinite leading ones) |
| 3 | interpret as two's complement | `-(5+1) = -6` |

> **Warning:** If you want a fixed-width NOT (e.g., 8-bit `~00000101` = `11111010` = 250 unsigned), you must mask: `(~n) & 0xFF`.

```python
def not_8bit(n: int) -> int:
    return (~n) & 0xFF

print(not_8bit(5))   # 250  (binary 11111010)
```

### 4.5 Left Shift (`<<`)

**Definition:** Shifts all bits left by `k` positions, filling with `0`s on the right. Equivalent to multiplying by `2^k`.

```
n = 3 = 0011
n << 1 = 0110 = 6
n << 2 = 1100 = 12
```

```python
print(3 << 1)   # 6
print(3 << 2)   # 12
print(1 << 5)   # 32  (2^5)
```

**Applications:** Fast multiplication by powers of 2, building bitmasks (`1 << i` isolates bit position `i`), constructing numbers bit by bit.

### 4.6 Right Shift (`>>`)

**Definition:** Shifts all bits right by `k` positions. For non-negative numbers, equivalent to floor division by `2^k`. Python performs an **arithmetic shift** for negative numbers — it sign-extends (fills with `1`s) rather than zero-filling, preserving the sign.

```
n = 12 = 1100
n >> 1 = 0110 = 6
n >> 2 = 0011 = 3

n = -12
n >> 2 = -3   (sign preserved, floor division semantics)
```

```python
print(12 >> 2)    # 3
print(-12 >> 2)   # -3  (arithmetic shift; floor(-12/4) = -3)
print(-5 >> 1)    # -3  (floor(-5/2) = -3, NOT -2!)
```

> **Common Mistake:** People assume `>>` truncates toward zero like integer division in C. In Python, `>>` for negative numbers performs a **floor** shift, matching `//`, which can surprise engineers coming from other languages.

**Combined operator summary table:**

| Operator | Symbol | Nature | Common Use |
|---|---|---|---|
| AND | `&` | Bitwise multiply-like (both must be 1) | Masking, checking bits |
| OR | `\|` | Bitwise "at least one" | Setting bits, combining flags |
| XOR | `^` | Bitwise "exactly one" | Toggling, uniqueness, swapping |
| NOT | `~` | Bitwise inversion | Building inverse masks |
| Left Shift | `<<` | Multiply by 2^k | Building masks, fast multiply |
| Right Shift | `>>` | Divide by 2^k (floor, sign-extending) | Fast divide, extracting high bits |

---
## 5. Bit Manipulation Fundamentals

Every technique below follows the same template: **Definition → Why → Code → Dry Run → Complexity → Edge Cases**.

### 5.1 Check Even / Odd

**Why:** The last bit of a binary number determines parity — `0` = even, `1` = odd. Faster than `% 2` in some low-level contexts and idiomatic in bit-heavy code.

```python
def is_odd(n: int) -> bool:
    return (n & 1) == 1
```
Dry run: `n=13` → `1101 & 0001 = 0001` → `True`.
**Complexity:** O(1) time, O(1) space. **Edge case:** works correctly for negative numbers too, since Python's `&` respects two's complement semantics (`-3 & 1 == 1`).

### 5.2 Check i-th Bit

```python
def get_bit(n: int, i: int) -> int:
    return (n >> i) & 1
```
**Why:** Shift the target bit to position 0, then mask off everything else with `& 1`.
Dry run: `n=10 (1010)`, `i=1` → `n >> 1 = 0101` → `& 1 = 1` → bit is set.

### 5.3 Set i-th Bit

```python
def set_bit(n: int, i: int) -> int:
    return n | (1 << i)
```
`1 << i` creates a mask with only bit `i` set; OR-ing guarantees that bit becomes 1 while leaving others untouched.

### 5.4 Clear i-th Bit

```python
def clear_bit(n: int, i: int) -> int:
    return n & ~(1 << i)
```
`~(1 << i)` is all 1s except position `i`; AND-ing forces bit `i` to 0 while preserving the rest.

### 5.5 Toggle i-th Bit

```python
def toggle_bit(n: int, i: int) -> int:
    return n ^ (1 << i)
```
XOR with a single-bit mask flips exactly that bit (property `a^1` flips a bit, `a^0` leaves it).

### 5.6 Update (Set to value v) i-th Bit

```python
def update_bit(n: int, i: int, v: int) -> int:
    mask = ~(1 << i)
    return (n & mask) | (v << i)
```
Clear the bit first, then OR in the new value shifted into place.

### 5.7 Count Set Bits (Popcount)

**Brute force:**
```python
def count_set_bits_v1(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

**Optimized — Brian Kernighan's Algorithm:**
```python
def count_set_bits_v2(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)   # drops the lowest set bit
        count += 1
    return count
```

**Pythonic (built-in, fastest):**
```python
def count_set_bits_v3(n: int) -> int:
    return n.bit_count()      # Python 3.10+
    # or: bin(n).count('1')   # portable to older Python
```

**Dry run (Kernighan) for n = 12 (`1100`):**

| Step | n (binary) | n - 1 | n & (n-1) | count |
|---|---|---|---|---|
| 1 | 1100 | 1011 | 1000 | 1 |
| 2 | 1000 | 0111 | 0000 | 2 |
| 3 | 0000 | — | loop ends | 2 |

**Complexity:** Brute force O(bit_length); Kernighan's O(number of set bits) — faster for sparse numbers.

### 5.8 Least Significant Set Bit (Isolate)

```python
def lowest_set_bit(n: int) -> int:
    return n & (-n)
```
**Why it works:** In two's complement, `-n = ~n + 1`. Flipping bits and adding 1 causes everything up to and including the lowest set bit to be preserved as a single isolated bit when ANDed with `n`.

Dry run: `n = 12 = 1100`, `-n = ...110100` (two's complement) → `n & -n = 0100 = 4`.

### 5.9 Remove Lowest Set Bit

```python
def remove_lowest_set_bit(n: int) -> int:
    return n & (n - 1)
```
Same trick used in Kernighan's popcount — this is *the* single most reused bit trick in this entire handbook.

### 5.10 Check Power of Two

```python
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
```
**Why:** A power of two has exactly one set bit. `n & (n-1)` clears the lowest set bit — if that results in 0, there was only one bit to begin with.

Dry run: `n=16=10000`, `n-1=01111`, AND → `00000` → `True`.
**Edge case:** must check `n > 0` — the formula wrongly returns True for `n = 0` otherwise (`0 & -1 == 0`).

### 5.11 Check Power of Four

```python
def is_power_of_four(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0
```
**Why the extra check:** Powers of 4 are a subset of powers of 2 where the single set bit sits at an *even* position (0,4,16,64…). A neat number-theory fact: for any power of two `n`, `n-1` is divisible by 3 **iff** `n` is a power of 4 (since `4^k - 1` is always divisible by 3).

### 5.12 Highest/Lowest Power of Two ≤ n

```python
def highest_power_of_two(n: int) -> int:
    if n <= 0:
        return 0
    return 1 << (n.bit_length() - 1)
```
`bit_length()` tells you how many bits are needed; subtracting 1 gives the position of the MSB.

### 5.13 Most Significant Bit (MSB) Position

```python
def msb_position(n: int) -> int:
    return n.bit_length() - 1   # 0-indexed from LSB
```

### 5.14 Bit Length

`n.bit_length()` — minimum bits needed to represent `n` (ignoring sign), e.g., `(255).bit_length() == 8`, `(256).bit_length() == 9`.

### 5.15 Summary Table

| Operation | Formula |
|---|---|
| Check even | `n & 1 == 0` |
| Get bit i | `(n >> i) & 1` |
| Set bit i | `n \| (1 << i)` |
| Clear bit i | `n & ~(1 << i)` |
| Toggle bit i | `n ^ (1 << i)` |
| Count set bits | `n.bit_count()` |
| Lowest set bit | `n & -n` |
| Remove lowest set bit | `n & (n-1)` |
| Power of two check | `n>0 and n&(n-1)==0` |

---
## 6. Bit Manipulation Patterns

### 6.1 XOR Pattern — Single Number (all others appear twice)

**Problem:** Given an array where every element appears twice except one, find the single one.

**Approach:** XOR everything together. Pairs cancel out (`a^a=0`), and XOR with 0 is identity, leaving only the unique value.

```python
def single_number(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

print(single_number([4, 1, 2, 1, 2]))  # 4
```

**Dry run:** `result=0 ^4=4 ^1=5 ^2=7 ^1=6 ^2=4` → final `4`. Matches expectation ✅

**Complexity:** O(n) time, O(1) space — strictly better than a hash-set approach (O(n) space).

### 6.2 Two Single Numbers (all others appear twice, two uniques)

**Approach:**
1. XOR all numbers → get `xor_all = a ^ b` (the two unique numbers XORed).
2. Find any set bit in `xor_all` (e.g., lowest set bit) — this bit *must* differ between `a` and `b`.
3. Partition all numbers into two groups based on that bit; XOR within each group isolates `a` and `b` separately.

```python
def two_single_numbers(nums: list[int]) -> tuple[int, int]:
    xor_all = 0
    for num in nums:
        xor_all ^= num
    diff_bit = xor_all & (-xor_all)   # lowest set bit where a and b differ

    a = 0
    for num in nums:
        if num & diff_bit:
            a ^= num
    b = xor_all ^ a
    return a, b

print(two_single_numbers([1, 2, 1, 3, 2, 5]))  # (3, 5)
```

**Complexity:** O(n) time, O(1) space.

### 6.3 Missing Number (0..n, one missing)

```python
def missing_number(nums: list[int]) -> int:
    n = len(nums)
    result = n
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result

print(missing_number([3, 0, 1]))  # 2
```
**Why it works:** XOR together every index `0..n` and every value in the array. All matching pairs cancel, leaving the missing number.

### 6.4 Bit Masking — Subset Representation

A set of `n` elements can be represented as an `n`-bit integer, where bit `i` = 1 means "element i is included."

```
Set {0,1,2}, subset {0,2} -> bitmask 101 (bit0=1, bit1=0, bit2=1)
```

```python
def subset_from_mask(elements: list, mask: int) -> list:
    return [elements[i] for i in range(len(elements)) if mask & (1 << i)]

elements = ['a', 'b', 'c']
print(subset_from_mask(elements, 0b101))  # ['a', 'c']
```

### 6.5 Generate All Subsets via Bitmask Enumeration

```python
def all_subsets(elements: list) -> list[list]:
    n = len(elements)
    result = []
    for mask in range(1 << n):        # 0 to 2^n - 1
        subset = [elements[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result

print(all_subsets(['a', 'b']))
# [[], ['a'], ['b'], ['a', 'b']]
```
**Complexity:** O(2^n * n) time (n for building each subset), O(2^n) space for the output. This is the canonical bitmask approach to the "Power Set" problem, an alternative to recursive backtracking.

### 6.6 Prefix XOR

Analogous to prefix sums, but with XOR — useful for answering "XOR of subarray [l, r]" queries in O(1) after O(n) preprocessing.

```python
def build_prefix_xor(nums: list[int]) -> list[int]:
    prefix = [0] * (len(nums) + 1)
    for i, num in enumerate(nums):
        prefix[i + 1] = prefix[i] ^ num
    return prefix

def range_xor(prefix: list[int], l: int, r: int) -> int:
    # inclusive range [l, r], 0-indexed
    return prefix[r + 1] ^ prefix[l]

nums = [1, 2, 3, 4, 5]
prefix = build_prefix_xor(nums)
print(range_xor(prefix, 1, 3))  # 2^3^4 = 5
```

### 6.7 Counting Bits for a Range 0..n (DP + Bit Trick)

```python
def count_bits_dp(n: int) -> list[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)   # i >> 1 already computed; add last bit
    return dp

print(count_bits_dp(5))   # [0, 1, 1, 2, 1, 2]
```
**Why it works:** `i >> 1` removes the last bit, so `dp[i >> 1]` already holds the popcount of the remaining bits — just add whether the last bit is set.

### 6.8 Hamming Distance

**Definition:** Number of differing bit positions between two integers.

```python
def hamming_distance(x: int, y: int) -> int:
    return (x ^ y).bit_count()

print(hamming_distance(1, 4))  # 001 vs 100 -> 2
```

### 6.9 Gray Code

**Definition:** A binary sequence where consecutive values differ in exactly one bit.

```python
def gray_code(n: int) -> list[int]:
    return [i ^ (i >> 1) for i in range(1 << n)]

print(gray_code(2))  # [0, 1, 3, 2]  -> binary: 00, 01, 11, 10
```
**Why it works:** `i ^ (i >> 1)` is the standard binary-to-Gray-code conversion formula; each successive value flips exactly one bit relative to the previous.

### 6.10 State Compression / Bitmask DP (Overview)

**Idea:** When a DP state depends on "which subset of items has been used/visited," encode that subset as an integer bitmask and use it as a DP dimension. Classic example: **Traveling Salesman Problem (TSP)** — `dp[mask][i]` = minimum cost to visit exactly the cities in `mask`, ending at city `i`.

```python
# Skeleton only (conceptual) — full TSP is a DP + Graph topic, out of scope here.
# dp[mask][i] = min(dp[mask ^ (1<<i)][j] + dist[j][i] for j in mask if j != i)
```
This handbook covers bitmask DP only as a *pattern preview* since the DP framework itself belongs to Dynamic Programming, not Bit Manipulation.

### 6.11 XOR Swap (Swap Without Temp Variable)

```python
def xor_swap(a: int, b: int) -> tuple[int, int]:
    a ^= b
    b ^= a
    a ^= b
    return a, b

print(xor_swap(3, 5))  # (5, 3)
```
> **Interview Note:** In real Python code, `a, b = b, a` is idiomatic and faster. XOR swap is taught for its cleverness and is relevant in low-level languages without tuple unpacking, but is rarely "better" in Python.

### 6.12 Parity

```python
def parity(n: int) -> int:
    return n.bit_count() % 2   # 1 = odd number of set bits, 0 = even
```
Used in error-detection codes (parity bit in serial communication, simple checksums).

---
## 7. Advanced Concepts

### 7.1 Bit Masks & Bit Fields (Flags)

**Definition:** Encoding multiple boolean flags into one integer, each flag occupying one bit.

```python
READ    = 1 << 0   # 0001
WRITE   = 1 << 1   # 0010
EXECUTE = 1 << 2   # 0100
DELETE  = 1 << 3   # 1000

permissions = READ | WRITE          # 0011
print(bin(permissions))              # '0b11'
print(bool(permissions & WRITE))     # True  -> has write permission
print(bool(permissions & EXECUTE))   # False -> no execute permission

permissions |= EXECUTE               # grant execute
permissions &= ~WRITE                # revoke write
print(bin(permissions))              # '0b101' (READ + EXECUTE)
```

This is exactly how Unix file permission bits and many OS-level flag systems work.

### 7.2 Bloom Filter (Overview Only)

A **Bloom filter** is a probabilistic, space-efficient data structure for approximate set-membership testing (no false negatives, possible false positives). It's built on a bit array plus multiple hash functions that each set one bit per inserted element. Checking membership means checking that *all* corresponding hashed bits are set. This is an application-level use of bit arrays — implementation details belong to a dedicated Bloom Filter topic, out of scope here.

### 7.3 CRC — Cyclic Redundancy Check (Overview Only)

CRC is an error-detecting code used in networking and storage, computed via polynomial division over GF(2) — implemented efficiently using XOR and shift operations on the bit representation of the data. Full CRC implementation is a specialized topic; the key takeaway for this handbook is that **XOR and shifts are the core primitives** behind checksum and error-detection algorithms.

### 7.4 Fast (Binary) Exponentiation Using Bits

**Problem:** Compute `a^b` in O(log b) instead of O(b).

**Idea:** Write `b` in binary. `a^b = product of a^(2^i) for every set bit i in b`.

```python
def fast_power(a: int, b: int) -> int:
    result = 1
    base = a
    while b > 0:
        if b & 1:            # if current bit is set, multiply it in
            result *= base
        base *= base          # square the base each iteration
        b >>= 1                # move to next bit
    return result

print(fast_power(2, 10))  # 1024
```

**Dry run for `fast_power(2, 10)`** (`10 = 1010` in binary):

| Step | b (binary) | b&1 | result | base |
|---|---|---|---|---|
| start | 1010 | - | 1 | 2 |
| 1 | 1010 | 0 | 1 | 4 |
| 2 | 0101 | 1 | 1*4=4 | 16 |
| 3 | 0010 | 0 | 4 | 256 |
| 4 | 0001 | 1 | 4*256=1024 | 65536 |
| 5 | 0000 | loop ends | **1024** | - |

**Complexity:** O(log b) time vs O(b) naive — a huge improvement for large exponents.

### 7.5 Modular Exponentiation (Bit Perspective)

Same idea as fast exponentiation, but take `% mod` at every multiplication to keep numbers bounded — critical in cryptography (RSA) where exponents are enormous.

```python
def mod_power(a: int, b: int, mod: int) -> int:
    result = 1
    base = a % mod
    while b > 0:
        if b & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        b >>= 1
    return result

print(mod_power(2, 10, 1000))  # 24  (1024 % 1000)
```

### 7.6 Binary Lifting (Overview Only)

**Binary lifting** precomputes "jump 2^k steps" tables (e.g., ancestors in a tree) so any jump of size `k` can be decomposed into O(log k) precomputed jumps by reading the binary representation of `k` — the same bit-decomposition idea as fast exponentiation, applied to tree/graph ancestor queries (e.g., LCA — Lowest Common Ancestor). Full algorithm belongs to Trees/Graphs; mentioned here only because its core trick is reading `k`'s bits one at a time.

---
## 8. Real-World Applications

| Domain | Concrete Example |
|---|---|
| **Permission Systems** | Unix `chmod 754` — each digit is 3 bits: read(4)+write(2)+execute(1) |
| **Compression** | Huffman coding assigns variable-length bit codes; run-length encoding packs repeated bit patterns |
| **Cryptography** | XOR-based stream ciphers (e.g., one-time pad), block cipher round functions (AES uses bitwise XOR extensively) |
| **Networking** | IP subnet masks (`/24` = `255.255.255.0`), packet flag fields (TCP flags: SYN, ACK, FIN each a single bit) |
| **Graphics** | Packing RGBA color channels into a 32-bit integer: `color = (r << 24) \| (g << 16) \| (b << 8) \| a` |
| **Embedded Systems** | Direct hardware register manipulation — setting/clearing GPIO pin bits to control hardware |
| **Competitive Programming** | Bitmask DP (TSP-style), subset enumeration, XOR-based uniqueness tricks |
| **Operating Systems** | Process state flags, memory page table flags (present/dirty/accessed bits) |
| **Database Systems** | Bitmap indexes for fast boolean column queries; storing multiple boolean columns as one bitmask integer |

**Worked example — packing RGBA:**
```python
def pack_rgba(r: int, g: int, b: int, a: int) -> int:
    return (r << 24) | (g << 16) | (b << 8) | a

def unpack_rgba(color: int) -> tuple[int, int, int, int]:
    r = (color >> 24) & 0xFF
    g = (color >> 16) & 0xFF
    b = (color >> 8) & 0xFF
    a = color & 0xFF
    return r, g, b, a

packed = pack_rgba(255, 128, 0, 255)
print(hex(packed))          # 0xff8000ff
print(unpack_rgba(packed))  # (255, 128, 0, 255)
```

---

## 9. Problem Recognition

### 9.1 Keywords That Signal Bit Manipulation

- "every element appears **twice/thrice** except one" → XOR pattern
- "**subsets**", "power set", "all combinations" → bitmask enumeration
- "**permissions**", "flags", "states" → bitmask flags
- "count **set bits**", "population count", "hamming weight" → popcount
- "**power of two/four**" → `n & (n-1)` trick
- "without using `+`/`-`/`*`/`/`" → bitwise arithmetic simulation
- "**XOR** of range/array" → prefix XOR
- "single number / missing number / duplicate number" → XOR patterns
- "minimum number of **states**" combined with small `n` (≤ 20) → bitmask DP

### 9.2 Recognition Decision Tree

```
Does the problem mention duplicates/uniqueness with a twist (twice except one)?
 ├── YES → XOR pattern
 └── NO
      └── Does it involve subsets / combinations of a SMALL set (n ≤ 20)?
           ├── YES → Bitmask enumeration / Bitmask DP
           └── NO
                └── Does it mention permissions / flags / on-off states?
                     ├── YES → Bit flags / masking
                     └── NO
                          └── Does it ask to avoid arithmetic operators?
                               ├── YES → Simulate with bitwise ops (add/multiply via bits)
                               └── NO → Probably NOT a bit manipulation problem
```

### 9.3 Interview Clues Checklist

- [ ] Input size constraint like `n ≤ 20` (strong hint for bitmask DP, since `2^20 ≈ 10^6`)
- [ ] Array of integers with "exactly one/two odd occurrences"
- [ ] Explicit ban on `+`, `-`, `*`, `/`
- [ ] Talk of "states," "on/off," "flags," "subsets"
- [ ] Numbers described as powers of two
- [ ] Need for O(1) extra space where hashing would otherwise be the obvious approach

---
## 10. Optimization Playbook

### 10.1 Brute Force → Bit Manipulation (Worked Transformation)

**Problem:** Find the single number appearing once among duplicates (each other number appears twice).

| Approach | Code Idea | Time | Space |
|---|---|---|---|
| Brute Force | Nested loop counting occurrences | O(n²) | O(1) |
| Hash Map | Count occurrences, find count==1 | O(n) | O(n) |
| **Bit Manipulation (XOR)** | XOR all elements | **O(n)** | **O(1)** |

```python
# Brute force
def single_number_brute(nums):
    for x in nums:
        if nums.count(x) == 1:
            return x

# Hash map
def single_number_hash(nums):
    from collections import Counter
    counts = Counter(nums)
    for num, c in counts.items():
        if c == 1:
            return num

# Bit manipulation (optimal)
def single_number_xor(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

**Takeaway:** Bit manipulation frequently converts an O(n) *space* solution into an O(1) *space* solution while keeping O(n) time — this space optimization is the #1 reason interviewers love these problems.

### 10.2 Constant-Time Optimizations Cheat List

| Task | Naive | Optimized (Bit Trick) |
|---|---|---|
| Multiply/divide by 2^k | `n * 2**k` | `n << k` |
| Check even/odd | `n % 2` | `n & 1` |
| Check power of two | Loop dividing by 2 | `n & (n-1) == 0` |
| Count set bits | Loop over all bits | `n & (n-1)` loop, or `n.bit_count()` |
| Swap two variables | Temp variable | `a, b = b, a` (Pythonic) or XOR swap |
| Toggle a flag | If/else | `flag ^= 1` |

### 10.3 Space Optimization Using Bitmasks

Replacing a `bool[] visited` array of size `n` with a single integer bitmask (when `n` is small, e.g., ≤ 64) turns O(n) space into O(1) space (a single machine word), and set/query operations become O(1) instead of O(1) amortized array access — mainly a *space*, not asymptotic time, win, but with excellent cache locality.

---
## 11. Interview Preparation

### 11.1 Difficulty-Wise Problem Map

**Easy**
- Number of 1 Bits (Hamming Weight)
- Single Number
- Power of Two
- Missing Number
- Counting Bits
- Reverse Bits
- Hamming Distance
- Binary Number with Alternating Bits

**Medium**
- Single Number II (every element thrice except one)
- Single Number III (two uniques)
- Subsets (bitmask enumeration)
- Sum of Two Integers (no `+`/`-`)
- Divide Two Integers (no `*`/`/`)
- Gray Code
- UTF-8 Validation
- Bitwise AND of Numbers Range
- Maximum XOR of Two Numbers in an Array

**Hard**
- Bitmask DP: Traveling Salesman Problem
- Minimum XOR sum of two arrays (bitmask DP)
- Shortest Path Visiting All Nodes (bitmask BFS)
- Maximum Students Taking Exam (bitmask DP with adjacency constraints)

### 11.2 Pattern-Wise Question Map

| Pattern | Representative Problems |
|---|---|
| XOR basics | Single Number, Missing Number, Hamming Distance |
| XOR advanced | Single Number II/III, Maximum XOR of Two Numbers |
| Bit masking / flags | Subsets, Permissions design questions |
| Popcount | Counting Bits, Number of 1 Bits |
| Power of two/four | Power of Two, Power of Four |
| Bit simulation of arithmetic | Sum of Two Integers, Divide Two Integers |
| Bitmask DP | TSP, Shortest Path Visiting All Nodes, Partition to K subsets |
| Bit tricks in strings | UTF-8 Validation, Binary Watch |

### 11.3 Company-Wise Themes (General Trends, Not Guarantees)

| Company | Typical Emphasis |
|---|---|
| Google | XOR tricks, elegant O(1)-space solutions, bit DP |
| Amazon | Practical bitmask flags, permission-style design questions |
| Meta | Fast bitwise arithmetic simulation (add/multiply without operators) |
| Microsoft | Counting bits, reverse bits, power-of-two checks |
| Bloomberg / Fintech | Bit-level encoding for compact data representation |

> **Note:** Company patterns shift over time — always check recent community-reported experiences (e.g., LeetCode discuss, Blind) close to your interview date rather than relying solely on any static list.

### 11.4 Blind 75 / NeetCode Bit Manipulation Subset

- Single Number
- Number of 1 Bits
- Counting Bits
- Missing Number
- Reverse Bits
- Sum of Two Integers

### 11.5 Standard Bit Manipulation Interview Templates

**Template 1 — XOR uniqueness:**
```python
def find_unique(nums):
    res = 0
    for n in nums:
        res ^= n
    return res
```

**Template 2 — Bitmask subset generation:**
```python
def subsets_bitmask(nums):
    n = len(nums)
    return [[nums[i] for i in range(n) if mask & (1 << i)]
            for mask in range(1 << n)]
```

**Template 3 — Bit-by-bit arithmetic simulation:**
```python
def add_without_plus(a, b):
    mask = 0xFFFFFFFF
    while b & mask:
        carry = (a & b) << 1
        a, b = (a ^ b) & mask, carry & mask
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)
```

**Template 4 — Popcount:**
```python
def popcount(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
```

### 11.6 Interview Tricks & Tips

- Always clarify: "Should I assume fixed-width (32-bit) integers, as in C++/Java, or Python's arbitrary precision?" — this changes overflow handling entirely.
- State the brute-force solution first, then optimize — interviewers want to see your reasoning path, not just the final trick.
- When using `n & (n-1)`, always narrate: *"this clears the lowest set bit"* — interviewers reward explained intuition over silent cleverness.
- For XOR problems, explicitly state the properties you're relying on (`a^a=0`, `a^0=a`) before applying them.
- Draw the truth table or a small binary example on the whiteboard/doc before diving into code — it demonstrates structured thinking.

---
## 12. Python Tips & Idioms

```python
# 1. Padded binary string
f'{42:08b}'                      # '00101010'

# 2. Binary literal
x = 0b1010                       # 10

# 3. Hex/Octal literals
y = 0xFF                          # 255
z = 0o17                          # 15

# 4. Strip '0b' prefix cleanly
bin(10)[2:]                       # '1010'

# 5. Fixed-width mask simulation
MASK32 = (1 << 32) - 1
result = (a + b) & MASK32         # simulate 32-bit overflow wraparound

# 6. Fast popcount (3.10+)
n.bit_count()

# 7. Iterating over set bits only
n = 0b10110
while n:
    lsb = n & (-n)
    print(lsb)          # process this bit
    n &= n - 1           # remove it

# 8. Byte <-> int conversions
(1024).to_bytes(2, 'big')          # b'\x04\x00'
int.from_bytes(b'\x04\x00', 'big')  # 1024
```

### 12.1 Performance Tips

- Prefer built-in `bit_count()` over manual loops — it's implemented in C.
- Avoid converting to strings (`bin()`) inside performance-critical loops; work with integers directly.
- For repeated masking, precompute the mask once outside loops.
- Arbitrary precision means very large numbers are slower — if you truly need fixed 32/64-bit behavior for speed (e.g., simulating hardware), consider `numpy` integer types (`numpy.uint32`), which wrap around exactly like C.

### 12.2 Memory Optimization

- Use a single `int` as a bitmask instead of a `list[bool]` when the domain size fits comfortably (≤ a few hundred bits, since Python ints grow gracefully).
- `array` module or `bytearray` for very large bit arrays if you need mutable, indexable byte-level storage.

### 12.3 Common Python Pitfalls (Preview of Section 13)

- `bin(-5)` prints `'-0b101'`, not two's complement.
- `~n` is `-n-1`, not a fixed-width flip unless masked.
- `>>` on negative numbers floors, doesn't truncate toward zero.
- No native overflow — must simulate manually for interview-style problems.

---
## 13. Common Mistakes

| # | Mistake | Why It Happens | Fix |
|---|---|---|---|
| 1 | Assuming `bin(-5)` shows two's complement | Python shows sign+magnitude for negatives | Mask explicitly: `format(n & mask, '0Nb')` |
| 2 | Forgetting operator precedence: `a & b == c` | `==` binds tighter than `&` in Python | Always parenthesize: `(a & b) == c` |
| 3 | Assuming fixed-width overflow happens automatically | Python ints are arbitrary precision | Manually mask with `& 0xFFFFFFFF` etc. |
| 4 | Confusing `>>` with truncating division | Arithmetic right shift floors for negatives | Use `//` mental model, not C-style truncation |
| 5 | Using wrong mask width | Copy-pasted from a different bit-width context | Always define `mask = (1 << bits) - 1` explicitly per problem |
| 6 | Treating one's complement and two's complement as the same | Historical confusion | Two's complement = one's complement + 1; only two's complement is used in modern systems |
| 7 | Forgetting `n > 0` check in power-of-two test | `0 & -1 == 0` incorrectly passes | Always guard: `n > 0 and n & (n-1) == 0` |
| 8 | Using `~n` expecting a fixed-width flip | `~n == -n-1` in Python | Mask: `(~n) & mask` |
| 9 | Shifting by negative or huge amounts | `n << -1` raises `ValueError`; huge shifts are slow/huge | Validate shift amount range before shifting |
| 10 | Assuming XOR-swap is faster/better in Python | Python has native tuple-swap | Prefer `a, b = b, a` in real code |

---

## 14. Cheat Sheets

### 14.1 Operator Cheat Sheet

| Op | Symbol | Effect | Mnemonic |
|---|---|---|---|
| AND | `&` | both 1 → 1 | "and gate" |
| OR | `\|` | either 1 → 1 | "or gate" |
| XOR | `^` | differ → 1 | "exactly one" |
| NOT | `~` | flips all | "-n-1 in Python" |
| Left Shift | `<<` | ×2^k | "grow" |
| Right Shift | `>>` | ÷2^k (floor) | "shrink" |

### 14.2 Bit Trick Cheat Sheet

```
n & 1                → is odd
n & (n-1)             → remove lowest set bit / check power of two if ==0
n & (-n)              → isolate lowest set bit
n | (1<<i)            → set bit i
n & ~(1<<i)           → clear bit i
n ^ (1<<i)            → toggle bit i
(n>>i) & 1             → get bit i
n.bit_length()         → position of MSB + 1
n.bit_count()           → popcount
a^a=0, a^0=a           → XOR identities
```

### 14.3 Complexity Cheat Sheet

| Operation | Time | Space |
|---|---|---|
| Any single bitwise op | O(1)* | O(1) |
| Popcount (loop) | O(bit_length) | O(1) |
| Popcount (Kernighan) | O(set bits) | O(1) |
| Subset enumeration | O(2^n · n) | O(2^n) |
| Fast exponentiation | O(log b) | O(1) |
| Prefix XOR build | O(n) | O(n) |

\* For Python arbitrary-precision ints, technically O(digits), but effectively O(1) for typical interview-sized numbers.

### 14.4 Binary Conversion Cheat Sheet

| From → To | Method |
|---|---|
| Decimal → Binary | `bin(n)[2:]` or repeated `%2, //2` |
| Binary → Decimal | `int(s, 2)` |
| Decimal → Hex | `hex(n)[2:]` |
| Hex → Decimal | `int(s, 16)` |
| Decimal → Octal | `oct(n)[2:]` |

### 14.5 Pattern Recognition Cheat Sheet

| Signal | Pattern |
|---|---|
| "appears twice except one" | XOR |
| "subsets/power set", small n | Bitmask enumeration |
| "permissions/flags" | Bit flags |
| "no +/-/*//" | Bitwise arithmetic simulation |
| "count set bits" | Popcount |
| "power of two/four" | `n&(n-1)` |
| small n ≤ 20, optimization | Bitmask DP |

---
## 15. Practice Problems

### 15.1 Basics

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Number of 1 Bits | LeetCode | Easy | Popcount | leetcode.com/problems/number-of-1-bits |
| Counting Bits | LeetCode | Easy | Popcount DP | leetcode.com/problems/counting-bits |
| Power of Two | LeetCode | Easy | n&(n-1) | leetcode.com/problems/power-of-two |
| Power of Four | LeetCode | Easy | n&(n-1) + mod 3 | leetcode.com/problems/power-of-four |
| Binary Representation | GeeksforGeeks | Easy | Basics | geeksforgeeks.org |

### 15.2 XOR

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Single Number | LeetCode | Easy | XOR | leetcode.com/problems/single-number |
| Single Number II | LeetCode | Medium | XOR + bit counting | leetcode.com/problems/single-number-ii |
| Single Number III | LeetCode | Medium | XOR partitioning | leetcode.com/problems/single-number-iii |
| Missing Number | LeetCode | Easy | XOR | leetcode.com/problems/missing-number |
| Maximum XOR of Two Numbers in an Array | LeetCode | Medium | XOR + Trie | leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array |
| XOR Queries of a Subarray | LeetCode | Medium | Prefix XOR | leetcode.com/problems/xor-queries-of-a-subarray |

### 15.3 Bit Masks

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Subsets | LeetCode | Medium | Bitmask enumeration | leetcode.com/problems/subsets |
| Partition to K Equal Sum Subsets | LeetCode | Medium | Bitmask DP | leetcode.com/problems/partition-to-k-equal-sum-subsets |
| Maximum Students Taking Exam | LeetCode | Hard | Bitmask DP | leetcode.com/problems/maximum-students-taking-exam |

### 15.4 Counting Bits & Related

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Hamming Distance | LeetCode | Easy | XOR + popcount | leetcode.com/problems/hamming-distance |
| Total Hamming Distance | LeetCode | Medium | Bit-position counting | leetcode.com/problems/total-hamming-distance |
| Reverse Bits | LeetCode | Easy | Bit manipulation | leetcode.com/problems/reverse-bits |

### 15.5 Unique Number Variants

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Find the Duplicate Number | LeetCode | Medium | Bit counting variant | leetcode.com/problems/find-the-duplicate-number |
| Single Number II/III | LeetCode | Medium | XOR variants | (see above) |

### 15.6 Bit DP (Conceptual)

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Traveling Salesman Problem | GeeksforGeeks / Codeforces | Hard | Bitmask DP | geeksforgeeks.org/travelling-salesman-problem |
| Shortest Path Visiting All Nodes | LeetCode | Hard | Bitmask BFS | leetcode.com/problems/shortest-path-visiting-all-nodes |

### 15.7 Prefix XOR / State Compression

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| XOR Queries of a Subarray | LeetCode | Medium | Prefix XOR | (see above) |
| Minimum XOR Sum of Two Arrays | LeetCode | Hard | Bitmask DP | leetcode.com/problems/minimum-xor-sum-of-two-arrays |

### 15.8 Subset Generation

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Subsets II | LeetCode | Medium | Bitmask + dedup | leetcode.com/problems/subsets-ii |
| Beautiful Arrangement | LeetCode | Medium | Bitmask DP | leetcode.com/problems/beautiful-arrangement |

### 15.9 Advanced Bit Manipulation

| Problem | Platform | Difficulty | Pattern | Link |
|---|---|---|---|---|
| Sum of Two Integers | LeetCode | Medium | Bit arithmetic simulation | leetcode.com/problems/sum-of-two-integers |
| Divide Two Integers | LeetCode | Medium | Bit-shift division | leetcode.com/problems/divide-two-integers |
| Bitwise AND of Numbers Range | LeetCode | Medium | Common prefix trick | leetcode.com/problems/bitwise-and-of-numbers-range |
| UTF-8 Validation | LeetCode | Medium | Bit pattern matching | leetcode.com/problems/utf-8-validation |
| Gray Code | LeetCode | Medium | `i ^ (i>>1)` | leetcode.com/problems/gray-code |

### 15.10 Additional Platforms

| Platform | Example Problem |
|---|---|
| Codeforces | "Xenia and Bit Operations" (educational bit DP/segment-style problem) |
| CodeChef | Various "XOR" tagged problems in the practice section |
| AtCoder | ABC/ARC problems tagged "bitwise" |
| CSES | "Bit Strings", "Two Sets" (combinatorics with bit reasoning) |
| HackerRank | "Lonely Integer", "Flipping bits", "AND product" |
| InterviewBit | "Single Number", "Reverse Bits" |
| Code360 (Coding Ninjas) | "Bit Manipulation" topic-tagged problem set |

> **Note:** Always verify exact links on the platform's search, since URLs and problem numbering occasionally change over time.

---
## 16. Final Revision

### 16.1 One-Page Mind Map (Text Form)

```
                         BIT MANIPULATION
                                |
     -------------------------------------------------------
     |            |             |            |              |
  Operators   Fundamentals   Patterns     Advanced       Applications
     |            |             |            |              |
  & | ^ ~ <<   check/set/    XOR-unique   fast pow      permissions
   >>          clear/toggle  subsets(2^n)  bit DP        graphics(RGBA)
              popcount       prefix XOR   binary lift    crypto/CRC
              power-of-2     Gray code                   networking
```

### 16.2 Bit Trick Sheet (Rapid Fire)

```
Even/Odd:            n & 1
Get bit i:            (n >> i) & 1
Set bit i:             n | (1 << i)
Clear bit i:           n & ~(1 << i)
Toggle bit i:          n ^ (1 << i)
Remove lowest set bit: n & (n - 1)
Isolate lowest set bit:n & (-n)
Power of two check:    n > 0 and n & (n-1) == 0
Popcount:              n.bit_count()
Swap without temp:     a, b = b, a   (or XOR swap)
```

### 16.3 Pattern Map (Quick Lookup)

| If you see... | Reach for... |
|---|---|
| duplicates except one/two | XOR |
| subsets/power set | Bitmask enumeration |
| flags/permissions | Bit masking |
| small n (≤20) + optimization | Bitmask DP |
| no arithmetic operators allowed | Bit-level simulation |
| range XOR queries | Prefix XOR |

### 16.4 Recognition Flowchart (Repeated for Quick Reference)

```
Uniqueness with duplicates? --YES--> XOR
        |NO
Small set, subset/combo? --YES--> Bitmask enumeration/DP
        |NO
Flags/permissions/states? --YES--> Bit masking
        |NO
No +/-/*// allowed? --YES--> Bit arithmetic simulation
        |NO
--> Probably not bit manipulation
```

### 16.5 Complexity Sheet (Recap)

| Technique | Time | Space |
|---|---|---|
| Single bitwise op | O(1) | O(1) |
| Popcount (Kernighan) | O(set bits) | O(1) |
| Subset enumeration | O(2^n · n) | O(2^n) |
| Fast exponentiation | O(log n) | O(1) |
| Prefix XOR | O(n) build, O(1) query | O(n) |

### 16.6 Binary Conversion Sheet (Recap)

```
bin(n)[2:]        decimal -> binary string
int(s, 2)          binary string -> decimal
hex(n)[2:]         decimal -> hex string
int(s, 16)          hex string -> decimal
format(n, '08b')    padded binary string
```

### 16.7 Interview Cheat Sheet (Final Recap)

1. Clarify fixed-width vs arbitrary precision assumptions first.
2. State brute force, then optimize to bit trick.
3. Narrate the trick's intuition out loud ("this clears the lowest set bit").
4. Watch for `n > 0` guards, operator precedence, and masking width.
5. Know the XOR identity properties cold: `a^a=0`, `a^0=a`, commutative & associative.

### 16.8 15-Minute Revision Plan

1. (3 min) Re-read operator truth tables (AND/OR/XOR/NOT/shifts).
2. (4 min) Recite the fundamentals table (get/set/clear/toggle bit, popcount, power of two).
3. (4 min) Walk through XOR pattern problems mentally (Single Number, Missing Number).
4. (4 min) Skim the Common Mistakes table — these are the fastest points to lose in an interview.

### 16.9 1-Hour Deep Revision Plan

| Time | Activity |
|---|---|
| 0–10 min | Re-derive two's complement and Python's negative-number quirks from scratch |
| 10–20 min | Re-implement popcount (loop, Kernighan, built-in) from memory |
| 20–35 min | Solve Single Number, Single Number II, Single Number III without looking at notes |
| 35–50 min | Solve Subsets via bitmask enumeration + one bitmask DP skeleton (TSP outline) |
| 50–60 min | Review Cheat Sheets (Section 14) end-to-end and self-quiz with the FAQs below |

### 16.10 Frequently Asked Questions (FAQ)

**Q1: Does Python have fixed-width integers like C++/Java?**
No. Python integers are arbitrary precision. You must manually simulate fixed-width behavior with explicit masks (e.g., `& 0xFFFFFFFF`) when a problem assumes 32-bit semantics.

**Q2: Why does `bin(-5)` not show two's complement bits?**
Python displays negative numbers as a minus sign plus the binary of their absolute value, for readability. To see the actual two's complement bit pattern, mask the number to a fixed width first: `format(-5 & 0xFF, '08b')`.

**Q3: Is XOR swap better than `a, b = b, a` in Python?**
No — Python's tuple assignment is idiomatic, readable, and just as fast (if not faster). XOR swap is taught for conceptual understanding and is more relevant in languages without native multiple assignment.

**Q4: When should I use a bitmask instead of a boolean array?**
When the domain size is small enough to fit in a machine word (typically ≤ 64, though Python ints can go further), and when you need O(1) set/query operations with minimal memory overhead — very common in competitive programming subset problems.

**Q5: What's the difference between `n & (n-1)` for popcount vs. power-of-two check?**
Same operation, different use: repeatedly applying it and counting iterations gives popcount (Kernighan's algorithm); applying it once and checking if the result is `0` tells you if exactly one bit was set (power of two).

**Q6: Why does XOR "cancel" duplicates?**
Because `a ^ a = 0` and `a ^ 0 = a`. XOR-ing a multiset where every element appears an even number of times except one collapses all paired elements to 0, leaving the odd one out.

**Q7: How do I know when a problem needs Bitmask DP vs plain DP?**
Look for small constraints (commonly `n ≤ 20`) combined with a need to track "which subset of items has been used/visited" — that subset becomes the DP dimension, encoded as an integer bitmask.

**Q8: Is right shift the same as integer division by 2 for negative numbers in Python?**
It's the same as floor division (`//`), not truncating division. `-5 >> 1 == -3`, matching `-5 // 2 == -3`, which can differ from what you'd expect from languages that truncate toward zero.

---

## Closing Notes

This handbook is designed to be revisited, not read once. Bit manipulation rewards repetition — the tricks in Section 14's Cheat Sheets should eventually become as automatic as basic arithmetic. When in doubt during an interview: **write out the binary, draw the truth table, and reason bit by bit before reaching for a clever one-liner.**

