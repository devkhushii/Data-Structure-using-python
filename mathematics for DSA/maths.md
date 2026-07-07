# Mathematics for DSA & Competitive Programming — The Complete Handbook

---

## Table of Contents

1. [Mathematical Foundations](#1-mathematical-foundations)
2. [Number Theory](#2-number-theory)
3. [Combinatorics](#3-combinatorics)
4. [Probability](#4-probability)
5. [Bit Mathematics](#5-bit-mathematics)
6. [Logarithms, Exponents & Complexity Math](#6-logarithms-exponents--complexity-math)
7. [Mathematical Sequences & Recurrences](#7-mathematical-sequences--recurrences)
8. [Geometry for DSA](#8-geometry-for-dsa)
9. [Matrix Mathematics](#9-matrix-mathematics)
10. [Algorithm Analysis Mathematics](#10-algorithm-analysis-mathematics)
11. [Competitive Programming Toolbox](#11-competitive-programming-toolbox)
12. [Mathematical Pattern Recognition](#12-mathematical-pattern-recognition)
13. [Real-World Applications](#13-real-world-applications)
14. [Problem Recognition Flowcharts](#14-problem-recognition-flowcharts)
15. [Optimization Playbook](#15-optimization-playbook)
16. [Interview Preparation Guide](#16-interview-preparation-guide)
17. [Python Tips for Math-Heavy CP](#17-python-tips-for-math-heavy-cp)
18. [Common Mistakes](#18-common-mistakes)
19. [Cheat Sheets](#19-cheat-sheets)
20. [Practice Problems](#20-practice-problems)
21. [Final Revision](#21-final-revision)

---

## 1. Mathematical Foundations

### 1.1 Number Systems at a Glance

```
            REAL NUMBERS
                 │
   ┌─────────────┴─────────────┐
 RATIONAL                  IRRATIONAL
   │                             (√2, π, e)
┌──┴───┐
INTEGERS   NON-INTEGER FRACTIONS
   │            (1/2, 3/4 ...)
┌──┴───┐
NATURAL   NEGATIVE INTEGERS
(0,1,2..)     (-1,-2,-3..)
```

**Why it matters for DSA:** knowing which "number world" a value lives in tells you which bugs to expect — integer division truncation, floating point rounding, or overflow.

### 1.2 Integers, Floor, Ceil, Modulo

| Concept | Formula | Python |
|---|---|---|
| Floor division | `⌊a/b⌋` | `a // b` |
| Ceiling division | `⌈a/b⌉ = ⌊(a + b - 1)/b⌋` (positive ints) | `-(-a // b)` |
| Modulo | `a mod b = a - b*⌊a/b⌋` | `a % b` |
| Truncation toward 0 | `int(a/b)` in C-like langs | `math.trunc(a/b)` |

**Warning — Python vs C++ modulo:** Python's `%` always returns a result with the **same sign as the divisor**, so `-7 % 3 == 2` in Python but `-1` in C++. This trips up a huge number of CP submissions ported between languages.

```python
print(-7 % 3)   # 2  (Python)
print(-7 // 3)  # -3 (floor division, not truncation)
```

**Ceiling division trick (the single most reused one-liner in CP):**
```python
def ceil_div(a: int, b: int) -> int:
    """Ceiling division for non-negative a, b (b > 0)."""
    return -(-a // b)   # equivalent to (a + b - 1) // b

# Dry run: a=7, b=3
# -a = -7, -a // b = -7 // 3 = -3 (floor), negate -> 3
# check: ceil(7/3) = ceil(2.33) = 3 ✔
```

### 1.3 Absolute Value, Scientific Notation, Exponents

```python
abs(-5)          # 5
2 ** 10           # 1024, exponent
10 ** -3          # 0.001, negative exponent -> float
format(6.02e23, '.3e')  # scientific notation formatting
```

### 1.4 Divisibility Rules (quick recognition table)

| Divisor | Rule |
|---|---|
| 2 | last digit even |
| 3 | digit sum divisible by 3 |
| 4 | last 2 digits divisible by 4 |
| 5 | last digit 0 or 5 |
| 6 | divisible by 2 and 3 |
| 8 | last 3 digits divisible by 8 |
| 9 | digit sum divisible by 9 |
| 11 | alternating digit-sum divisible by 11 |

**Interview tip:** digit-sum divisibility rules are the seed idea behind a whole class of "digit DP" problems.

---

## 2. Number Theory

Number theory is the single highest-leverage topic in CP math — GCD, modular arithmetic, and primes appear in a large fraction of "math" tagged problems on Codeforces/LeetCode.

### 2.1 Primes & Composite Numbers

**Definition:** A prime `p > 1` has exactly two divisors: `1` and `p`. A composite number has more than two.

**Naive primality test — O(√n):**
```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:                 # 2, 3
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:          # only test up to sqrt(n)
        if n % i == 0:
            return False
        i += 2                 # skip even numbers
    return True
```
**Why √n is enough (proof):** if `n = a * b` with `a <= b`, then `a <= sqrt(n)` (otherwise `a*b > n`). So if no factor exists up to `sqrt(n)`, none exists beyond it either.

**Dry run** (`n = 29`):

| step | i | i*i | condition | action |
|---|---|---|---|---|
| 1 | 3 | 9 | 9 ≤ 29 | 29%3=2 ≠0, i→5 |
| 2 | 5 | 25 | 25 ≤ 29 | 29%5=4≠0, i→7 |
| 3 | 7 | 49 | 49 > 29 | loop ends |

Result: `True` (29 is prime).

Time: `O(√n)`, Space: `O(1)`.

### 2.2 Sieve of Eratosthenes

**Intuition:** instead of testing each number individually, cross off multiples of every prime found, starting from 2.

```
n=30 sieve visualization (● = marked composite):

2  3  4● 5  6●  7  8●  9●  10●
11 12● 13 14● 15● 16● 17 18● 19 20●
21● 22● 23 24● 25● 26● 27● 28● 29 30●
```

```python
def sieve(n: int) -> list[int]:
    """Return list of primes <= n using the classic sieve."""
    is_comp = [False] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):   # start at i*i: smaller multiples already marked
                is_comp[j] = True
    return primes
```
**Why start marking at `i*i`?** Any composite multiple of `i` smaller than `i*i` (like `2i, 3i, ..., (i-1)i`) already has a smaller prime factor and was marked earlier.

**Complexity:** `O(n log log n)` time (harmonic-like sum over primes), `O(n)` space. This is a **must-memorize** bound — it comes from summing `n/p` over all primes `p ≤ n`.

**Linear (SPF) Sieve — O(n):**
```python
def linear_sieve(n: int):
    spf = [0] * (n + 1)        # smallest prime factor
    primes = []
    for i in range(2, n + 1):
        if spf[i] == 0:         # i is prime
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > n:
                break
            spf[i * p] = p       # p is guaranteed the smallest prime factor of i*p
    return spf, primes
```
**Why it's O(n):** every composite number is marked **exactly once**, by its smallest prime factor — unlike the classic sieve where a number can be marked multiple times (once per prime factor).

**Applications of SPF array:** O(log n) factorization of any number, fast GCD/LCM batch queries, multiplicative function computation (Euler's totient, divisor counts).

### 2.3 Prime Factorization

```python
def prime_factorize(n: int) -> dict[int, int]:
    """Return {prime: exponent} using trial division up to sqrt(n)."""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:                 # leftover n is itself prime
        factors[n] = factors.get(n, 0) + 1
    return factors

# Dry run n=360
# d=2: 360/2=180,/2=90,/2=45 -> factors{2:3}, n=45
# d=3: 45/3=15,/3=5 -> factors{2:3,3:2}, n=5
# d=4..: 4*4=16>5? no wait d*d<=n check with n=5, 4*4=16>5 stop loop... but d moved to 4 first
# leftover n=5 -> factors{2:3,3:2,5:1}
# 360 = 2^3 * 3^2 * 5^1 ✔
```

**Prime factor tree (ASCII):**
```
                 360
               /     \
              2      180
                    /     \
                   2       90
                          /   \
                         2     45
                              /   \
                             3     15
                                  /   \
                                 3      5
```

Time: `O(√n)` worst case (n prime). Space: `O(log n)` for the factor map.

### 2.4 GCD & the Euclidean Algorithm

**Theorem:** `gcd(a, b) = gcd(b, a mod b)`, with `gcd(a, 0) = a`.

**Proof sketch:** any common divisor of `a` and `b` also divides `a - k*b` for any integer `k`; setting `k = ⌊a/b⌋` gives `a mod b`. So the set of common divisors of `(a,b)` equals that of `(b, a mod b)`, hence equal GCDs.

```python
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b     # divide first to avoid overflow-style intermediate blowup
```

**Dry run** `gcd(48, 18)`:

| a | b | a % b |
|---|---|---|
| 48 | 18 | 12 |
| 18 | 12 | 6 |
| 12 | 6 | 0 |

Result: `6`.

**Complexity:** `O(log(min(a,b)))` — this bound comes from Fibonacci numbers being the worst case input (Lamé's theorem): consecutive Fibonacci numbers force the maximum number of steps.

### 2.5 Extended Euclidean Algorithm

Finds integers `x, y` such that `a*x + b*y = gcd(a, b)` (Bézout's identity).

```python
def ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (g, x, y) with a*x + b*y = g = gcd(a,b)."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = ext_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# Dry run a=35, b=15
# ext_gcd(35,15) -> ext_gcd(15,5) -> ext_gcd(5,0) = (5,1,0)
# back at (15,5): x=0, y=1-(15//5)*0=1        -> (5,0,1)
# back at (35,15): x=1, y=0-(35//15)*1=0-2=-2 -> (5,1,-2)
# check: 35*1 + 15*(-2) = 35-30=5 ✔
```

**Primary use in CP:** computing the **modular inverse** when `mod` is not prime, and solving linear Diophantine equations.

### 2.6 Modular Arithmetic

```
Modular cycle for mod 5:

   0 → 1 → 2 → 3 → 4 → 0 → 1 → ...
   ▲___________________________│
        (wraps around every 5 steps)
```

**Core identities** (all mod `m`):
- `(a + b) % m = ((a%m) + (b%m)) % m`
- `(a - b) % m = ((a%m) - (b%m) + m) % m`  ← the `+m` guards against negative results
- `(a * b) % m = ((a%m) * (b%m)) % m`
- Division is **not** distributive under mod — you need the modular inverse (below).

### 2.7 Fast (Binary) Modular Exponentiation

**Problem:** compute `a^b mod m` when `b` can be up to `10^18`.

**Idea:** write `b` in binary; `a^b = a^(2^k1) * a^(2^k2) * ...` for the set bits of `b`. Square-and-multiply.

```python
def power_mod(a: int, b: int, m: int) -> int:
    a %= m
    result = 1
    while b > 0:
        if b & 1:                 # current bit is 1
            result = (result * a) % m
        a = (a * a) % m            # square the base
        b >>= 1                    # move to next bit
    return result

# Dry run: 3^13 mod 7   (13 = 1101 in binary)
# b=13(1101) a=3   result=1
# bit1=1: result=1*3%7=3 ; a=9%7=2  ; b=6(0110)
# bit0=0:                 a=4%7=4  ; b=3(0011)
# bit1=1: result=3*4%7=5 ; a=16%7=2; b=1(0001)
# bit1=1: result=5*2%7=3 ; a=4%7=4 ; b=0
# answer: 3
```
**Complexity:** `O(log b)` multiplications — this is *the* workhorse formula behind fast power, matrix exponentiation, and RSA.

### 2.8 Fermat's Little Theorem & Modular Inverse

**Theorem:** if `p` is prime and `gcd(a, p) = 1`, then `a^(p-1) ≡ 1 (mod p)`. Consequently `a^(p-2) ≡ a^(-1) (mod p)`.

```python
def mod_inverse_fermat(a: int, p: int) -> int:
    """Requires p prime and gcd(a, p) == 1."""
    return power_mod(a, p - 2, p)

def mod_inverse_ext_gcd(a: int, m: int) -> int:
    """Works for any m, provided gcd(a, m) == 1."""
    g, x, _ = ext_gcd(a, m)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x % m
```

**Interview tip:** if the modulus is the classic CP prime `10**9 + 7`, prefer `power_mod(a, MOD-2, MOD)` — it's simpler to reason about and equally fast (`O(log MOD)`).

### 2.9 Euler's Totient Function φ(n)

**Definition:** count of integers in `[1, n]` coprime to `n`.

**Formula:** if `n = p1^e1 * p2^e2 * ... * pk^ek`, then
`φ(n) = n * Π(1 - 1/pi)` over distinct prime factors `pi`.

```python
def euler_totient(n: int) -> int:
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p         # multiply by (1 - 1/p)
        p += 1
    if temp > 1:
        result -= result // temp
    return result

# Dry run n=36 = 2^2 * 3^2
# result=36; p=2: 36%2==0 -> temp=9, result=36-36//2=18
# p=3: 9%3==0 -> temp=1, result=18-18//3=12
# temp==1 loop ends. φ(36)=12
```
**Euler's theorem** generalizes Fermat: `a^φ(m) ≡ 1 (mod m)` whenever `gcd(a,m)=1` (m need not be prime).

**Applications:** counting coprime pairs, RSA key generation, modular inverse when `m` is not prime (`a^(φ(m)-1) mod m`).

### 2.10 Chinese Remainder Theorem (overview)

Given `x ≡ r1 (mod m1)`, `x ≡ r2 (mod m2)` with `gcd(m1, m2) = 1`, there's a unique `x mod (m1*m2)` satisfying both.

```python
def crt(r1: int, m1: int, r2: int, m2: int) -> int:
    g, p, q = ext_gcd(m1, m2)
    # g must be 1 for a solution to exist
    lcm_ = m1 * m2
    x = (r1 * m2 * q + r2 * m1 * p) % lcm_
    return x % lcm_
```
Used for combining modular results across coprime moduli — common in problems that give you a huge modulus factored into primes.

### 2.11 Wilson's Theorem (overview)

`(p-1)! ≡ -1 (mod p)` iff `p` is prime. Rarely used directly in CP but occasionally appears as a primality-flavored trick question.

---

## 3. Combinatorics

### 3.1 Factorials, Permutations, Combinations

```
nPr = n! / (n-r)!        (order matters)
nCr = n! / (r! * (n-r)!) (order doesn't matter)
```

**Why nCr divides evenly (intuition):** nPr counts ordered arrangements; each unordered group of `r` items can be arranged in `r!` orders, so dividing by `r!` collapses those duplicates into one count.

```python
import math

def nPr(n: int, r: int) -> int:
    return math.factorial(n) // math.factorial(n - r)

def nCr(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
```

**Modular nCr with precomputed factorials — the standard CP template:**
```python
MOD = 10**9 + 7
MAXN = 2 * 10**6 + 5

fact = [1] * MAXN
inv_fact = [1] * MAXN
for i in range(1, MAXN):
    fact[i] = fact[i - 1] * i % MOD
inv_fact[MAXN - 1] = power_mod(fact[MAXN - 1], MOD - 2, MOD)
for i in range(MAXN - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def nCr_mod(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
```
**Why precompute inverse factorials backwards?** `inv_fact[i] = inv_fact[i+1] * (i+1)` because `inv_fact[i+1] = 1/(i+1)!` and multiplying by `(i+1)` gives `1/i!` — this avoids `n` separate `O(log MOD)` modular-inverse calls, dropping total precompute to `O(n + log MOD)`.

### 3.2 Pascal's Triangle

```
                1
              1   1
            1   2   1
          1   3   3   1
        1   4   6   4   1
      1   5  10  10   5   1
```
`C(n, r) = C(n-1, r-1) + C(n-1, r)` — every entry is the sum of the two above it. This recurrence is how you build an nCr DP table without factorials/overflow.

```python
def pascal_triangle(n: int) -> list[list[int]]:
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle
```

### 3.3 Stars and Bars

**Problem:** number of ways to distribute `n` identical items into `k` distinct groups (each group ≥ 0) is `C(n + k - 1, k - 1)`.

```
n=5 items, k=3 groups, one arrangement:
★ ★ | ★ ★ ★ |         (bars separate groups; stars = items)
```
```python
def stars_and_bars(n: int, k: int) -> int:
    return nCr(n + k - 1, k - 1)
```

### 3.4 Inclusion–Exclusion Principle

`|A ∪ B| = |A| + |B| - |A ∩ B|`, generalized:
`|A1 ∪ ... ∪ An| = Σ|Ai| - Σ|Ai∩Aj| + Σ|Ai∩Aj∩Ak| - ...`

**Classic CP use — counting numbers ≤ n divisible by at least one of a set of primes:**
```python
def count_divisible_by_any(n: int, primes: list[int]) -> int:
    total = 0
    k = len(primes)
    for mask in range(1, 1 << k):          # iterate all non-empty subsets
        bits = bin(mask).count("1")
        prod = 1
        for i in range(k):
            if mask & (1 << i):
                prod *= primes[i]
            if prod > n:
                break
        if prod <= n:
            term = n // prod
            total += term if bits % 2 == 1 else -term
    return total
```
Complexity: `O(2^k)` over the number of prime factors `k` (typically small, k ≤ ~10).

### 3.5 Catalan Numbers

`Cn = C(2n, n) / (n+1)`, counts balanced parenthesis sequences, binary search tree shapes, valid mountain paths, etc.

```python
def catalan(n: int) -> int:
    return nCr(2 * n, n) // (n + 1)
```
**Recurrence form** (useful for DP): `C0=1`, `C_{n+1} = Σ_{i=0}^{n} Ci * C_{n-i}`.

### 3.6 Derangements

A derangement is a permutation with **no fixed points** (nobody gets their own item back — the classic "hat check" problem).

`D(n) = (n-1) * (D(n-1) + D(n-2))`, `D(0)=1, D(1)=0`.

```python
def derangements(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 0
    d0, d1 = 1, 0
    for i in range(2, n + 1):
        d0, d1 = d1, (i - 1) * (d0 + d1)
    return d1
```

### 3.7 Pigeonhole Principle

If `n` items are placed into `k` boxes and `n > k`, some box has more than one item. Not computational, but a **proof technique** — used to argue existence bounds (e.g., proving a cycle must exist in a functional graph, or that a subarray sum is divisible by `k` among any `k+1` prefix sums).

---

## 4. Probability

### 4.1 Basic Probability & Expected Value

`P(event) = favorable outcomes / total outcomes` (for equally likely outcomes).

`E[X] = Σ x * P(X = x)` — **linearity of expectation** holds *always*, even for dependent variables: `E[X+Y] = E[X] + E[Y]`. This is the single most useful probability fact in CP.

```python
def expected_value(outcomes: list[float], probs: list[float]) -> float:
    return sum(x * p for x, p in zip(outcomes, probs))
```

### 4.2 Conditional Probability

`P(A|B) = P(A ∩ B) / P(B)`

### 4.3 Probability Tree (coin flips)

```
                 start
               /       \
            H(0.5)    T(0.5)
            /   \      /   \
         HH    HT    TH    TT
        0.25  0.25  0.25  0.25
```

### 4.4 A Classic CP Probability Problem — Expected Number of Coin Flips to Get Heads

Let `E` = expected flips. `E = 1 + 0.5*0 + 0.5*E` → `E = 2`. This "set up an equation for E, solve" pattern recurs constantly (random walks, expected steps in Markov chains, DP with probabilities).

```python
def expected_flips_for_heads(p_heads: float) -> float:
    return 1 / p_heads     # geometric distribution expectation
```

---

## 5. Bit Mathematics

### 5.1 Binary / Decimal / Hex / Octal Conversions

```python
bin(42)     # '0b101010'
hex(42)     # '0x2a'
oct(42)     # '0o52'
int('101010', 2)   # 42
int('2a', 16)      # 42
```

### 5.2 Bit Tricks Cheat Table

| Trick | Expression | Meaning |
|---|---|---|
| Check bit i | `n & (1 << i)` | is bit i set? |
| Set bit i | `n \| (1 << i)` | turn bit i on |
| Clear bit i | `n & ~(1 << i)` | turn bit i off |
| Toggle bit i | `n ^ (1 << i)` | flip bit i |
| Check power of 2 | `n & (n-1) == 0` | true iff exactly one bit set |
| Isolate lowest set bit | `n & (-n)` | e.g. Fenwick tree indexing |
| Clear lowest set bit | `n & (n-1)` | used to count set bits |
| Count set bits | `bin(n).count('1')` or `n.bit_count()` (Python 3.10+) | popcount |

**Why `n & (n-1)` clears the lowest set bit (proof):** `n-1` flips all bits after (and including) the lowest set bit of `n`. ANDing with the original `n` zeroes exactly that lowest bit while leaving higher bits untouched.

```
n     = 0b10110100
n-1   = 0b10110011
n&n-1 = 0b10110000   ← lowest set bit cleared
```

### 5.3 XOR Mathematics

Key identities: `a ^ a = 0`, `a ^ 0 = a`, XOR is commutative & associative. This underlies the "find the single non-duplicate element" family of problems.

```python
def find_unique(nums: list[int]) -> int:
    result = 0
    for x in nums:
        result ^= x       # all paired duplicates cancel out
    return result
```

### 5.4 Powers of Two & Bitmask DP

Bitmask DP represents subsets of up to ~20-25 elements as integers, enabling `O(2^n * n)` algorithms (e.g., Travelling Salesman DP).

```python
# iterate all subsets of a set of size n
n = 4
for mask in range(1 << n):
    subset = [i for i in range(n) if mask & (1 << i)]
```

---

## 6. Logarithms, Exponents & Complexity Math

### 6.1 Laws of Logarithms

```
log(a*b) = log a + log b
log(a/b) = log a - log b
log(a^k) = k * log a
log_b(x) = log(x) / log(b)     (change of base)
```

### 6.2 Why Binary Search is O(log n)

Each comparison halves the search space: after `k` steps, remaining size is `n / 2^k`. Search ends when `n/2^k ≈ 1`, i.e., `k ≈ log2(n)`.

```
n=16 search space shrink:
16 → 8 → 4 → 2 → 1     (4 steps = log2(16))
```

### 6.3 Tree Height & log

A balanced binary tree with `n` nodes has height `O(log n)` because each level doubles the node count: level `h` holds up to `2^h` nodes, and total nodes `= 2^(h+1) - 1`.

### 6.4 Divide & Conquer Complexity — Master Theorem

For `T(n) = a*T(n/b) + f(n)`:

| Case | Condition | Result |
|---|---|---|
| 1 | `f(n) = O(n^(log_b a - ε))` | `T(n) = Θ(n^log_b a)` |
| 2 | `f(n) = Θ(n^log_b a)` | `T(n) = Θ(n^log_b a * log n)` |
| 3 | `f(n) = Ω(n^(log_b a + ε))`, regularity holds | `T(n) = Θ(f(n))` |

**Worked example — Merge Sort:** `T(n) = 2T(n/2) + O(n)`. Here `a=2, b=2`, `log_b a = 1`, and `f(n) = Θ(n^1)` → Case 2 → `T(n) = Θ(n log n)`.

### 6.5 Summations Every CP Programmer Should Know

| Sum | Closed form |
|---|---|
| `1+2+...+n` | `n(n+1)/2` |
| `1²+2²+...+n²` | `n(n+1)(2n+1)/6` |
| `1+2+4+...+2^k` | `2^(k+1) - 1` |
| Harmonic `1+1/2+...+1/n` | `≈ ln(n) + γ` (this is *why* sieve is `n log log n` and why per-divisor loops sum to `O(n log n)`) |

---

## 7. Mathematical Sequences & Recurrences

### 7.1 Arithmetic & Geometric Progressions

```python
def ap_sum(a1: int, d: int, n: int) -> int:
    """Sum of n terms of arithmetic progression."""
    return n * (2 * a1 + (n - 1) * d) // 2

def gp_sum(a1: float, r: float, n: int) -> float:
    """Sum of n terms of geometric progression, r != 1."""
    return a1 * (r**n - 1) / (r - 1)
```

### 7.2 Fibonacci & Matrix Exponentiation

Naive recursion is `O(2^n)`. Linear DP is `O(n)`. **Matrix exponentiation gets you `O(log n)`:**

```
[F(n+1)]   [1 1]^n   [F(1)]
[F(n)  ] = [1 0]   * [F(0)]
```

```python
def mat_mult(A, B, mod):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % mod
             for j in range(len(B[0]))] for i in range(len(A))]

def mat_power(M, power, mod):
    n = len(M)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # identity
    while power > 0:
        if power & 1:
            result = mat_mult(result, M, mod)
        M = mat_mult(M, M, mod)
        power >>= 1
    return result

def fib_fast(n: int, mod: int = 10**9 + 7) -> int:
    if n == 0:
        return 0
    M = mat_power([[1, 1], [1, 0]], n - 1, mod)
    return M[0][0]
```
Complexity: `O(log n)` matrix multiplications, each `O(2^3)` for 2x2 matrices → effectively `O(log n)`.

### 7.3 Recurrence Relations — General DP Lens

Any linear recurrence `f(n) = c1*f(n-1) + c2*f(n-2) + ... + ck*f(n-k)` can be expressed as a `k x k` matrix and exponentiated in `O(k^3 log n)`, turning an `O(n)` DP into `O(log n)` when `n` is astronomically large (e.g., `10^18`).

---

## 8. Geometry for DSA

### 8.1 Distance & Midpoint

```python
import math

def distance(p1, p2):
    return math.hypot(p2[0]-p1[0], p2[1]-p1[1])

def midpoint(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
```

### 8.2 Slope & Line Equation

```
Coordinate plane:

  y
  │        • (x2,y2)
  │      /
  │    /
  │  • (x1,y1)
  └──────────── x

slope m = (y2-y1)/(x2-x1)
line: y - y1 = m(x - x1)
```

### 8.3 Cross Product & Orientation Test

**Cross product** of vectors `(x1,y1)` and `(x2,y2)`: `x1*y2 - x2*y1`. Sign tells turn direction — the backbone of convex hull and polygon algorithms.

```python
def cross(o, a, b):
    """> 0 : counter-clockwise turn, < 0 : clockwise, = 0 : collinear"""
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
```

```
  Left turn (CCW, cross > 0):        Right turn (CW, cross < 0):
        b                                    a
       /                                      \
      /                                        \
     o───────a                          o───────b
```

### 8.4 Shoelace Formula (Polygon Area)

`Area = 0.5 * |Σ(xi * y(i+1) - x(i+1) * yi)|`

```python
def polygon_area(points: list[tuple[int, int]]) -> float:
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2
```

### 8.5 Convex Hull Intuition (Graham Scan sketch)

Sort points by angle from the lowest point, then repeatedly pop the stack while the last three points make a non-left turn (using the cross product / orientation test above). `O(n log n)` dominated by the sort.

---

## 9. Matrix Mathematics

### 9.1 Matrix Multiplication

```python
def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0]*p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if A[i][k] == 0:
                continue
            for j in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C
```
Complexity: `O(n^3)` for `n x n` matrices (naive). Used for graph adjacency-power tricks (counting walks of length `k`), linear recurrences, and image/grid transforms.

### 9.2 Counting Walks via Adjacency Matrix Powers

`(A^k)[i][j]` = number of walks of length `k` from node `i` to `j` in a graph with adjacency matrix `A`. This is why matrix exponentiation generalizes far beyond Fibonacci.

### 9.3 Prefix Sum "Matrix" (2D Prefix Sums)

```
prefix[i][j] = grid[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
```
Enables `O(1)` rectangle-sum queries after `O(nm)` preprocessing — a staple in grid problems.

---

## 10. Algorithm Analysis Mathematics

### 10.1 Big-O, Big-Θ, Big-Ω — Precise Definitions

- `f(n) = O(g(n))`: `∃ c, n0` such that `f(n) ≤ c*g(n)` for all `n ≥ n0` (**upper bound**).
- `f(n) = Ω(g(n))`: `f(n) ≥ c*g(n)` (**lower bound**).
- `f(n) = Θ(g(n))`: both hold — **tight bound**.

### 10.2 Amortized Analysis (Aggregate Method)

**Example — dynamic array doubling:** each append is `O(1)` normally, `O(n)` when resizing. Total cost of `n` appends is bounded by the geometric series `1+2+4+...+n < 2n`, so **amortized** cost per append is `O(1)`.

```python
class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._data = [None]

    def append(self, x):
        if self._size == self._capacity:
            self._capacity *= 2                 # doubling: amortized O(1)
            new_data = [None] * self._capacity
            new_data[:self._size] = self._data[:self._size]
            self._data = new_data
        self._data[self._size] = x
        self._size += 1
```

---

## 11. Competitive Programming Toolbox

### 11.1 Overflow Handling in Python (and why it barely matters)

Python integers are arbitrary precision, so classic C++ overflow bugs don't exist — but you still pay a **speed** cost for huge integers, and you must still apply `% MOD` when the problem demands modular answers (the math is defined mod `p`, not just "avoid overflow").

### 11.2 Coordinate Compression (math aspect)

Replace large/sparse coordinate values with their **rank** among all distinct values, preserving relative order — turns an `O(V)`-indexed structure (Fenwick tree, segment tree) into an `O(n)`-indexed one.

```python
def compress(values: list[int]) -> dict[int, int]:
    sorted_unique = sorted(set(values))
    return {v: i for i, v in enumerate(sorted_unique)}
```

### 11.3 Difference Arrays (math intuition)

To add `v` to every element in range `[l, r]` in `O(1)`, do `diff[l] += v; diff[r+1] -= v`, then prefix-sum `diff` at the end. This works because a prefix sum of a "delta impulse at l, negative impulse at r+1" reconstructs a constant `+v` exactly on `[l, r]` — the discrete analogue of the derivative/integral relationship.

```python
def range_add_apply(n, updates):
    diff = [0] * (n + 1)
    for l, r, v in updates:
        diff[l] += v
        diff[r + 1] -= v
    result = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]
        result[i] = running
    return result
```

---

## 12. Mathematical Pattern Recognition

| Signal in problem statement | Likely math topic |
|---|---|
| "modulo 10^9+7" | modular arithmetic / combinatorics |
| "number of ways to..." | combinatorics (nCr, Catalan, stars & bars) |
| "GCD / LCM / coprime" | number theory |
| "expected value / probability" | probability, linearity of expectation |
| "XOR of..." | bit mathematics |
| "convex hull / points / area" | geometry |
| "n up to 10^18, recurrence" | matrix exponentiation |
| "count subsets" | bitmask DP / combinatorics |
| "digit sum / digit DP" | number theory + DP |
| "prime factorize many queries" | sieve + SPF precompute |

---

## 13. Real-World Applications

- **Cryptography:** RSA relies directly on Euler's theorem, modular exponentiation, and the difficulty of prime factorization.
- **Hashing:** polynomial rolling hashes use modular arithmetic and fast exponentiation (mod a large prime to reduce collisions).
- **Computer graphics:** rotation matrices, cross products for backface culling, geometry intersection tests.
- **Scheduling & optimization:** LCM for periodic task scheduling, greedy/DP with mathematical proofs of optimality.
- **Data compression:** entropy calculations use logarithms; Huffman coding relies on the log-based information-theoretic bound.

---

## 14. Problem Recognition Flowcharts

```
                 Does the problem mention a MODULUS?
                          │
              ┌───────────┴───────────┐
             YES                      NO
              │                        │
    Counting? → Combinatorics    Geometry keywords (points, area)?
    Else → modular arithmetic          │
    (inverse, fast pow, CRT)   ┌───────┴────────┐
                               YES              NO
                                │                │
                        distance/cross/hull   Sequence/recurrence
                                              with huge n?
                                                  │
                                          ┌───────┴────────┐
                                         YES              NO
                                          │                │
                                 matrix exponentiation   plain DP /
                                                          number theory
```

---

## 15. Optimization Playbook

| From (naive) | To (optimized) | Mathematical reason |
|---|---|---|
| Trial-division primality per query | Sieve + SPF precompute | Amortizes `O(√n)` per query into `O(n log log n)` total |
| `O(n)` modular inverse per query | Precompute `inv_fact[]` | Reuses one `O(log MOD)` inversion for all `n` |
| `O(n)` recurrence for huge `n` | Matrix exponentiation | `O(log n)` via repeated squaring |
| `O(n)` range updates | Difference array | Turns range update into two `O(1)` point updates |
| `O(n²)` all-pair distance-like sums | Prefix sums / sorting + math identity | Converts to closed-form sum, `O(n log n)` or `O(n)` |

---

## 16. Interview Preparation Guide

**High-yield math patterns for interviews (Blind 75 / NeetCode style):**
- Fast power (`pow(x, n)` — LeetCode 50)
- GCD/LCM based problems (e.g., "Ugly Number", "Nice Divisors")
- Bit manipulation (Single Number, Counting Bits, Power of Two)
- Combinatorics counting (Unique Paths — nCr closed form vs DP)
- Probability / random pick problems (reservoir sampling)
- Geometry (Valid Square, Max Points on a Line — uses slope + GCD to normalize)

**Interview trick:** when asked "can you do better than DP," think whether the recurrence is linear — if so, matrix exponentiation is often the "wow" answer.

---

## 17. Python Tips for Math-Heavy CP

```python
import math
math.gcd(a, b)          # built-in, fast C implementation
math.lcm(a, b)          # Python 3.9+
math.isqrt(n)           # exact integer sqrt, avoids float errors
math.comb(n, r)         # built-in nCr (Python 3.8+)
math.perm(n, r)         # built-in nPr

from fractions import Fraction   # exact rational arithmetic, avoids float error
from decimal import Decimal, getcontext  # arbitrary precision decimals

import itertools
itertools.permutations(range(4))
itertools.combinations(range(4), 2)
itertools.product([0,1], repeat=3)   # all bitmasks of length 3

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

import bisect
bisect.bisect_left(sorted_list, x)    # binary search insertion point
```

**Performance tip:** for tight loops, prefer `math.isqrt` over `int(n**0.5)` (the latter can be off by one due to floating point) and prefer built-in `math.comb`/`math.gcd` over hand-rolled versions when you don't need a modulus.

---

## 18. Common Mistakes

- Using `int(n ** 0.5)` for integer square root — floating point error can give the wrong answer near perfect squares; use `math.isqrt(n)`.
- Forgetting the `+ m` when computing `(a - b) % m` for negative intermediate values (Python actually handles this correctly automatically, but porting from C++ often reintroduces the bug).
- Computing `nCr` with plain factorials when a modulus is required — must use modular inverse, not integer division after `% MOD`.
- Off-by-one in sieve loops (`range(i*i, n+1, i)` vs `range(i*i, n, i)`).
- Assuming `gcd(0, 0) = 0` is undefined behavior — by convention it's `0`, and most implementations (including Python's `math.gcd`) return `0`.
- Confusing `nPr` and `nCr` — always ask "does order matter?" first.
- Precision loss with `float` in geometry — prefer integer cross products where possible to avoid epsilon comparisons.

---

## 19. Cheat Sheets

### 19.1 Number Theory Cheat Sheet
```
gcd(a,b) = gcd(b, a%b)                     lcm(a,b) = a*b/gcd(a,b)
a^(p-1) ≡ 1 (mod p)   [Fermat, p prime]     a^(-1) ≡ a^(p-2) (mod p)
φ(n) = n * Π(1 - 1/p) over prime factors p
Sieve: O(n log log n)     SPF sieve: O(n)     Factorize via SPF: O(log n)
```

### 19.2 Combinatorics Cheat Sheet
```
nPr = n!/(n-r)!        nCr = n!/(r!(n-r)!)     C(n,r)=C(n-1,r-1)+C(n-1,r)
Stars & bars: C(n+k-1, k-1)         Catalan: C(2n,n)/(n+1)
Derangements: D(n)=(n-1)(D(n-1)+D(n-2))
```

### 19.3 Complexity Cheat Sheet
```
T(n)=aT(n/b)+f(n)  → Master Theorem (3 cases, compare f(n) to n^log_b(a))
Sum 1..n = n(n+1)/2      Harmonic sum ≈ ln(n)
Binary search / balanced tree height: O(log n)
```

### 19.4 Geometry Cheat Sheet
```
distance = hypot(dx, dy)          slope = dy/dx
cross(o,a,b) > 0 → CCW turn        Shoelace area = |Σ x_i y_{i+1} - x_{i+1} y_i| / 2
```

### 19.5 Python Math Syntax Cheat Sheet
```
math.gcd, math.lcm, math.isqrt, math.comb, math.perm, math.factorial
pow(a, b, m)   ← Python's BUILT-IN fast modular exponentiation (use this in practice!)
```
> **Important practical note:** everywhere above we hand-wrote `power_mod` for teaching purposes — in real contests just call Python's built-in three-argument `pow(a, b, m)`, which is implemented in C and does exactly binary exponentiation under the hood.

---

## 20. Practice Problems

| Name | Platform | Difficulty | Pattern | Concept |
|---|---|---|---|---|
| Pow(x, n) | LeetCode 50 | Medium | Fast power | Binary exponentiation |
| GCD of Strings | LeetCode 1071 | Easy | GCD | Euclidean algorithm |
| Count Primes | LeetCode 204 | Medium | Sieve | Sieve of Eratosthenes |
| Ugly Number II | LeetCode 264 | Medium | Multiples | Number theory / DP |
| Unique Paths | LeetCode 62 | Medium | Combinatorics | nCr closed form |
| Single Number | LeetCode 136 | Easy | XOR | Bit math |
| Number of 1 Bits | LeetCode 191 | Easy | Popcount | Bit math |
| Max Points on a Line | LeetCode 149 | Hard | Slope normalization | GCD + geometry |
| Valid Square | LeetCode 593 | Medium | Distance | Coordinate geometry |
| K-th Symbol in Grammar | LeetCode 779 | Medium | Recursion/bit | Bit math |
| Exponentiation (POW) | SPOJ | Easy | Fast power | Modular exponentiation |
| GCD Extreme | SPOJ | Medium | Number theory | Sum of GCDs / Euler φ |
| Josephus Problem | CSES | Easy | Simulation | Recurrence |
| Exponentiation | CSES | Easy | Fast power | Modular exponentiation |
| Counting Divisors | CSES | Easy | Number theory | SPF / factorization |
| Common Divisors | CSES | Easy | Number theory | GCD |
| Binomial Coefficients | CSES | Easy | Combinatorics | Pascal triangle / nCr mod |
| Creating Strings II | CSES | Medium | Combinatorics | Multinomial coefficients |
| Bit Strings | CSES | Easy | Bit math | Powers of two mod p |
| Convex Hull | CSES | Medium | Geometry | Graham scan |
| Point Location Test | CSES | Easy | Geometry | Cross product / orientation |
| Modular Exponentiation | Codeforces (edu) | Easy | Fast power | Binary exponentiation |
| Chess Rook | Codeforces | Easy | Combinatorics | Counting |
| Petya and Divisors | Codeforces | Easy | Number theory | Divisor counting |
| Sherlock and Array | HackerRank | Medium | Prefix sums | Summation math |
| Fibonacci Modified | HackerRank | Medium | Recurrence | Big integer / recurrence |
| Find Digits | HackerRank | Easy | Digit math | Modulo / divisibility |
| Sum of Digits | GeeksforGeeks | Easy | Digit math | Modulo |
| nCr mod p | GeeksforGeeks | Medium | Combinatorics | Fermat's little theorem |
| Chinese Remainder Theorem | GeeksforGeeks | Hard | Number theory | CRT |
| Ways to Reach nth Stair | InterviewBit | Medium | Combinatorics | nCr / DP |
| Highest Product | InterviewBit | Medium | Sorting + math | Sign/parity reasoning |

*(This is a representative, curated starter set across every math category in this handbook — ask if you'd like this expanded into a much larger, fully categorized problem bank of 100+ problems.)*

---

## 21. Final Revision

### 21.1 One-Page Revision

```
NUMBER THEORY   → gcd/lcm, sieve, SPF, fast pow, fermat, φ(n)
COMBINATORICS   → nPr/nCr, pascal, stars&bars, incl-excl, catalan, derangement
PROBABILITY     → linearity of expectation, conditional prob
BIT MATH        → set/clear/toggle bit, popcount, XOR pair-cancel, n&(n-1)
COMPLEXITY      → master theorem, amortized (doubling array), sums/harmonic
SEQUENCES       → AP/GP closed forms, fibonacci via matrix power O(log n)
GEOMETRY        → distance, slope, cross product sign, shoelace area
MATRIX          → matmul O(n^3), matrix power for linear recurrences
```

### 21.2 Formula Map (ASCII Mind Map)

```
                       ┌── GCD/LCM ── Euclidean / Ext-Euclidean
                       │
        NUMBER THEORY ─┼── Primes ── Sieve / SPF / Factorization
                       │
                       └── Modular ── Fast Pow / Fermat / φ(n) / CRT

                       ┌── nPr, nCr ── Pascal Triangle
      COMBINATORICS ───┼── Stars & Bars
                       └── Inclusion-Exclusion / Catalan / Derangement

                       ┌── O/Θ/Ω definitions
   COMPLEXITY MATH ────┼── Master Theorem
                       └── Amortized Analysis / Summations

                       ┌── Distance / Slope
        GEOMETRY ──────┼── Cross Product (orientation)
                       └── Shoelace Area / Convex Hull
```

### 21.3 15-Minute Revision

1. Re-derive `power_mod` and the modular inverse via Fermat.
2. Re-derive `gcd`/`ext_gcd` and Bézout's identity.
3. Recall Master Theorem's 3 cases and one example each.
4. Recall nCr formula + modular version with precomputed factorials.
5. Recall cross product sign convention for orientation tests.

### 21.4 1-Hour Revision

Work through, from memory, then check against this handbook:
- Sieve of Eratosthenes + SPF sieve, both implementations.
- Extended Euclidean algorithm with a full dry run.
- nCr mod p using precomputed factorials/inverse factorials.
- Fibonacci via matrix exponentiation, `O(log n)`.
- Shoelace formula on a 4-point polygon, by hand.
- Master theorem classification on 3 different recurrences.

### 21.5 Interview Notes (final)

- Always state the **mathematical reason** a solution is correct before coding it — interviewers reward derivation, not just recall.
- When a modulus like `10^9+7` appears, immediately think: precompute factorials + inverse factorials, and use `pow(a, b, m)`.
- When `n` is enormous (`>10^7` for direct simulation, or up to `10^18`), look for a closed form or a linear-recurrence-to-matrix-exponentiation reduction.

---

### FAQ

**Q: Why `10^9 + 7` specifically as a modulus?**
A: It's a prime close to `2^31`, small enough that `(mod-1)*(mod-1)` fits safely in 64-bit integer types (relevant in C++/Java), and prime so Fermat's little theorem gives an easy modular inverse.

**Q: Do I need matrix exponentiation for every recurrence?**
A: No — only when `n` is too large for `O(n)` DP (roughly `n > 10^7`) *and* the recurrence is linear with constant coefficients.

**Q: Is Python's arbitrary precision integer a free pass on all number theory problems?**
A: For correctness, mostly yes (no silent overflow). For speed, no — huge integers are slower to multiply/mod than fixed-width ones, so you still want modular reduction and efficient algorithms (Sieve, fast pow) rather than relying on brute force.