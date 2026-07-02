# The Complete Java Arrays Handbook


*Language: Java 21 (LTS)*

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Java Array Fundamentals](#2-java-array-fundamentals)
   - 2.1 [What Is a Java Array](#21-what-is-a-java-array)
   - 2.2 [Why Java Arrays Are Fixed Size](#22-why-java-arrays-are-fixed-size)
   - 2.3 [Arrays as Objects](#23-arrays-as-objects)
   - 2.4 [Array Memory Layout](#24-array-memory-layout)
   - 2.5 [Default Initialization Values](#25-default-initialization-values)
   - 2.6 [Primitive Arrays vs Object Arrays](#26-primitive-arrays-vs-object-arrays)
   - 2.7 [Multidimensional, Jagged, and Anonymous Arrays (Preview)](#27-multidimensional-jagged-and-anonymous-arrays-preview)
3. [The JVM Memory Model and Arrays](#3-the-jvm-memory-model-and-arrays)
   - 3.1 [Stack Memory](#31-stack-memory)
   - 3.2 [Heap Memory](#32-heap-memory)
   - 3.3 [Method Area / Metaspace](#33-method-area--metaspace)
   - 3.4 [References vs Objects](#34-references-vs-objects)
   - 3.5 [Object Creation Lifecycle](#35-object-creation-lifecycle)
   - 3.6 [Garbage Collection and Arrays](#36-garbage-collection-and-arrays)
   - 3.7 [Full Memory Diagram Walkthrough](#37-full-memory-diagram-walkthrough)
4. [Array Declaration](#4-array-declaration)
5. [Array Initialization](#5-array-initialization)
6. [Traversing Arrays](#6-traversing-arrays)
7. [The java.util.Arrays Utility Class](#7-the-javautilarrays-utility-class)
8. [System.arraycopy()](#8-systemarraycopy)
9. [Copying Arrays — Shallow, Deep, and Reference Copies](#9-copying-arrays--shallow-deep-and-reference-copies)
10. [Multidimensional Arrays](#10-multidimensional-arrays)
11. [Array vs ArrayList](#11-array-vs-arraylist)
12. [Java Language Features Relevant to Arrays](#12-java-language-features-relevant-to-arrays)
13. [Performance Deep Dive](#13-performance-deep-dive)
14. [Core Array Algorithms & Fully-Worked Interview Problems](#14-core-array-algorithms--fully-worked-interview-problems)
15. [Array Patterns Cheat Sheet](#15-array-patterns-cheat-sheet)
16. [Common Mistakes Compendium](#16-common-mistakes-compendium)
17. [Interview Quick-Reference Sheet](#17-interview-quick-reference-sheet)
18. [Practice Problem List](#18-practice-problem-list)

---

## 1. Introduction

An **array** is the oldest, simplest, and most heavily used data structure in Java. Almost every other data structure — `ArrayList`, `HashMap`'s bucket table, `String`'s internal `byte[]`, heaps, hash tables — is *built on top of* an array at some level. If you don't deeply understand arrays, you don't fully understand how the JVM stores and moves data.

This handbook treats arrays not as "a list of numbers" but as what they actually are in Java: a special kind of **object**, with its own slot in the type system, its own bytecode instructions, its own memory layout rules, and its own set of gotchas that show up constantly in interviews.

Every section explains **why** a rule exists before showing **how** to use it. Every algorithm is presented with a problem statement, an approach, full Java code, a line-by-line explanation, a dry run, complexity analysis, at least one alternative approach, edge cases, common mistakes, and interview tips — so this document can be used standalone, without needing outside references.


---

## 2. Java Array Fundamentals

### 2.1 What Is a Java Array

A Java array is a **fixed-length, ordered, homogeneous container** of elements, all of the same declared type, stored in **contiguous memory** and accessed by a **zero-based integer index** in constant time.

Formally, in the Java Language Specification, an array is an **object** — not a primitive, not a "collection" in the `java.util.Collection` sense, but a genuine object with:

- A **type** (its *component type* + one or more dimensions), e.g. `int[]`, `String[]`, `int[][]`.
- A **length**, fixed at creation time and exposed via the public final field `.length`.
- A **runtime class object**, obtainable via `arr.getClass()`, whose name for `int[]` is `"[I"` and for `String[]` is `"[Ljava.lang.String;"`.
- Elements accessible via `[]` indexing, which the compiler turns into the bytecode instructions `iaload`/`iastore` (for `int[]`), `aaload`/`aastore` (for object arrays), etc.

```java
int[] scores = new int[5];   // an array object holding 5 ints
System.out.println(scores.getClass().getName()); // [I
System.out.println(scores.length);                // 5
```

Because an array is an object, an array *variable* is always a **reference** to that object — never the object itself. This single fact explains nearly every "surprising" array behavior in Java (aliasing, pass-by-reference-looking behavior in methods, `==` vs `.equals()`, etc.), and we will return to it repeatedly.

**Key properties of a Java array:**

| Property | Value |
|---|---|
| Size | Fixed at creation; cannot grow or shrink |
| Element type | Homogeneous — all elements share one declared component type |
| Indexing | Zero-based, `0` to `length - 1` |
| Access time | O(1) — direct address computation |
| Storage | Contiguous memory block on the heap |
| Type | Reference type (object), even for primitive component types |
| Default values | Auto-initialized (see §2.5) |

### 2.2 Why Java Arrays Are Fixed Size

This is one of the most-asked "why" questions in interviews, and the answer lies in **how array indexing is implemented**.

An array's O(1) access is possible only because the JVM can compute the memory address of `arr[i]` directly, using a simple formula:

```
address(arr[i]) = base_address + header_size + (i * element_size)
```

For this formula to work, the elements **must** occupy a single, unbroken, contiguous block of memory. If arrays were resizable in place, growing the array might require memory *immediately after* the current block — memory that could easily be occupied by something else. The JVM would then be forced to:

1. Allocate a brand-new, larger contiguous block elsewhere on the heap.
2. Copy every existing element into the new block.
3. Update every reference that pointed to the old array.

Step 3 is the real killer — Java has no way to transparently "redirect" all existing references to an object to a *different* object. Once you hand out a reference to an array, that reference points to one fixed object, at one fixed size, for its entire life.

This is precisely why `ArrayList` (an array-vs-ArrayList comparison, not a teaching of ArrayList internals, per scope) does not resize the underlying array in place — it allocates a new, larger backing array and copies elements over, then swaps the internal reference. The variable `list` you hold never changes identity; only the *internal* array reference inside `ArrayList` changes.

**Consequence for API design:** because arrays can't grow, any array-processing method that needs to "add" elements has exactly three real options:

1. Return a **brand new array** of the correct size (common in this handbook's problems).
2. Use a pre-sized array supplied by the caller and track a logical "used length" separately.
3. Rely on `System.arraycopy` / `Arrays.copyOf` to build a bigger array when needed.

### 2.3 Arrays as Objects

Because arrays are objects, they inherit from `java.lang.Object` and behave like objects in every relevant sense:

```java
int[] a = {1, 2, 3};
Object o = a;                 // legal — array IS-A Object
System.out.println(o instanceof int[]); // true
System.out.println(a.hashCode());        // identity hash, like any Object
System.out.println(a.equals(a));         // true (reference equality, from Object)
System.out.println(a.equals(new int[]{1,2,3})); // false! content isn't compared
```

Arrays do **not** override `equals()` or `toString()` — they inherit `Object`'s default implementations, which are based on reference identity. This is why `arr.equals(otherArr)` almost never does what beginners expect, and why `Arrays.equals()` / `Arrays.deepEquals()` exist (§7).

Similarly, `System.out.println(arr)` prints something like `[I@1b6d3586` — the type descriptor followed by the identity hash in hex — because `toString()` is never overridden. Use `Arrays.toString()` / `Arrays.deepToString()` instead.

Arrays also implement `Cloneable` and `java.io.Serializable` implicitly, which is why `.clone()` works on arrays without you declaring anything (see §9).

### 2.4 Array Memory Layout

When you write `int[] arr = new int[5];`, the JVM allocates a single contiguous object on the heap that conceptually looks like this:

```
Heap:
 ┌────────────────────────────────────────────────────────────┐
 │  Object Header (mark word + klass pointer)   [12-16 bytes]  │
 │  length field                                 [4 bytes]      │
 │  element[0] = 0                               [4 bytes]      │
 │  element[1] = 0                               [4 bytes]      │
 │  element[2] = 0                               [4 bytes]      │
 │  element[3] = 0                               [4 bytes]      │
 │  element[4] = 0                               [4 bytes]      │
 │  (padding to 8-byte alignment if needed)                     │
 └────────────────────────────────────────────────────────────┘
        ▲
        │
 arr ───┘   (reference stored on the stack, pointing at the heap object)
```

Stack vs heap placement:

```
Stack (method frame)          Heap
┌───────────────┐             ┌───────────────────────────┐
│ arr : 0x7f3a10 │────────────▶│ 0x7f3a10: [int[5] object] │
└───────────────┘             │   header | len=5 | 0 0 0 0 0│
                               └───────────────────────────┘
```

Because primitive-typed arrays store the **actual values** inline, contiguously, they enjoy excellent **cache locality** — walking `arr[0]`, `arr[1]`, `arr[2]`... touches sequential memory, which is extremely CPU-cache-friendly (see §13). Object arrays (`String[]`, `Integer[]`, custom classes) store contiguous **references**, but the objects those references point to may be scattered anywhere on the heap — this is discussed in depth in §13.

### 2.5 Default Initialization Values

When you create an array with `new`, Java **guarantees** every slot is initialized to a well-defined default — you never read "garbage" memory in Java, unlike C/C++.

| Component Type | Default Value |
|---|---|
| `byte` | `0` |
| `short` | `0` |
| `int` | `0` |
| `long` | `0L` |
| `float` | `0.0f` |
| `double` | `0.0d` |
| `char` | `'\u0000'` (null character) |
| `boolean` | `false` |
| Any object type (`String`, `Integer`, custom class, etc.) | `null` |

```java
int[] ints = new int[3];
boolean[] flags = new boolean[3];
String[] names = new String[3];

System.out.println(Arrays.toString(ints));  // [0, 0, 0]
System.out.println(Arrays.toString(flags)); // [false, false, false]
System.out.println(Arrays.toString(names)); // [null, null, null]
```

**Why this matters in interviews:** a very common bug is calling `names[0].length()` on a freshly created `String[]` before populating it — this throws `NullPointerException` because the default value is `null`, not `""`. Similarly, forgetting that `new int[n]` is already all-zeros leads people to write unnecessary manual zero-fill loops.

### 2.6 Primitive Arrays vs Object Arrays

Java has two fundamentally different families of arrays:

**Primitive arrays** (`int[]`, `double[]`, `char[]`, `boolean[]`, `byte[]`, `short[]`, `long[]`, `float[]`) store the raw primitive **values themselves**, packed contiguously, with no per-element object overhead.

**Object/reference arrays** (`String[]`, `Integer[]`, `Object[]`, any `T[]`) store **references** (pointers), contiguously, to objects that live elsewhere on the heap (or `null`).

```
int[] a = {1, 2, 3};                Integer[] b = {1, 2, 3};

Heap (a):                           Heap (b):
┌───┬───┬───┐                       ┌──────┬──────┬──────┐
│ 1 │ 2 │ 3 │  ← values inline      │ ref0 │ ref1 │ ref2 │  ← references
└───┴───┴───┘                       └──┬───┴──┬───┴──┬───┘
                                        │      │      │
                                        ▼      ▼      ▼
                                     [Integer│Integer│Integer
                                        1]      2]      3]  ← separate heap objects
```

This distinction drives autoboxing costs, cache performance differences, and why generics can't use primitive arrays directly (`List<int>` is illegal; `int[]` must be boxed to `Integer[]` to interoperate with generic collection APIs). Full treatment is in §12 and §13.

### 2.7 Multidimensional, Jagged, and Anonymous Arrays (Preview)

Java has **no true multidimensional arrays** in the sense that C has (a single contiguous N-D block). What Java calls `int[][]` is really an **array of arrays** — a 1D array whose elements are themselves references to (possibly differently-sized) 1D arrays. This is why "jagged arrays" (rows of different lengths) are natural in Java, and why `int[][] grid = new int[3][4];` is really "allocate an array of 3 references, then allocate 3 separate `int[4]` arrays and point each reference at one." Full details, diagrams, and traversal patterns are in §10.

An **anonymous array** is an array created and used without ever being assigned to a named variable, most often when passed directly as a method argument:

```java
printSum(new int[]{4, 8, 15, 16, 23, 42});
```

We cover the full syntax rules for anonymous arrays in §4.

---

## 3. The JVM Memory Model and Arrays

Understanding arrays properly requires understanding *where* the JVM puts things. This section explains the JVM runtime data areas relevant to arrays, in detail, with diagrams.

### 3.1 Stack Memory

Each thread in the JVM has its own **thread stack**, made up of **stack frames**, one per active method call. A stack frame holds:

- Local variables (including primitive values and object/array **references**)
- The operand stack (used for intermediate computation during bytecode execution)
- A reference to the runtime constant pool of the current class

**Crucially: array *objects themselves* are never stored on the stack.** Only **references** to arrays live in local variables on the stack. This is true even for local array variables inside a method.

```java
void method() {
    int[] arr = new int[5];   // 'arr' (a reference/pointer) lives on the stack
                               // the actual int[5] object lives on the heap
}
```

When `method()` returns, the stack frame is popped and `arr` (the reference) disappears — but the array object on the heap only disappears once the garbage collector determines nothing references it anymore (§3.6).

### 3.2 Heap Memory

The **heap** is a single, shared memory region (across all threads) where **all objects and arrays are allocated**, no exceptions. This includes:

- Every array, primitive or object type, of any dimension.
- Every non-array object (`new String(...)`, custom class instances, etc.)
- The boxed wrapper objects (`Integer`, `Double`, etc.) used inside object arrays like `Integer[]`.

Modern JVMs (HotSpot) subdivide the heap generationally for garbage collection efficiency:

```
┌───────────────────────────────── Heap ─────────────────────────────────┐
│  ┌───────────── Young Generation ─────────────┐  ┌── Old Generation ──┐│
│  │  Eden Space   │  Survivor 0  │ Survivor 1   │  │   (Tenured)        ││
│  │ (new objects) │              │              │  │ (long-lived objs)  ││
│  └───────────────┴──────────────┴──────────────┘  └────────────────────┘│
└───────────────────────────────────────────────────────────────────────┘
```

Most arrays are allocated in **Eden space**. Small, short-lived arrays (e.g., a temporary array inside a loop iteration) are typically collected quickly during a **minor GC** without ever being promoted. Large or long-lived arrays (e.g., a cache array held for the program's lifetime) get promoted to the **old generation** after surviving several GC cycles.

Very large arrays may qualify for **direct allocation into the old generation** (bypassing Eden) if they exceed a JVM-specific size threshold, since copying huge arrays between survivor spaces on every minor GC would be wasteful.

### 3.3 Method Area / Metaspace

The **Method Area** (implemented as **Metaspace** in modern HotSpot JVMs, replacing the old "PermGen") stores **class-level, per-type metadata** — not array *instances*, but the array *type descriptors* used by the JVM to understand what `int[]` or `String[][]` even mean.

For every distinct array type used in a program (`int[]`, `int[][]`, `String[]`, `MyClass[]`, ...), the JVM creates (once) a corresponding `Class` object describing that array type, stored in the Method Area. This is why `int[].class` and `new int[5].getClass()` both return the *same shared* `Class<int[]>` object regardless of how many actual `int[]` array instances exist on the heap.

### 3.4 References vs Objects

This is the single most important mental model for arrays in Java:

```
 Reference (lives on stack, or as a field inside another heap object)
   │
   │  "points to"
   ▼
 Array Object (always lives on the heap)
```

An array **variable** is not the array — it's an address that tells the JVM where the real array object lives. This has direct, testable consequences:

```java
int[] a = {1, 2, 3};
int[] b = a;          // b now points to the SAME array object as a
b[0] = 99;
System.out.println(a[0]); // 99 — because a and b are aliases of one object!

int[] c = a.clone();  // c points to a NEW, separate array object (copy)
c[0] = -1;
System.out.println(a[0]); // still 99 — c is independent
```

```
Before c = a.clone():           After c = a.clone():
a ──┐                            a ──┐
    ▼                                ▼
   [99, 2, 3]  ◀── b               [99, 2, 3]  ◀── b
                                  c ──▶ [99, 2, 3]  (separate object)
```

### 3.5 Object Creation Lifecycle

When the JVM executes `new int[5]`, the following happens, in order:

1. **Bytecode dispatch:** the compiler emits a `newarray` (primitive) or `anewarray`/`multianewarray` (object/multi-dim) instruction.
2. **Size check:** the JVM validates the requested length is `>= 0` (a negative length throws `NegativeArraySizeException` at runtime — this cannot be caught at compile time since lengths are often computed dynamically).
3. **Memory allocation:** the JVM's allocator (typically a fast "bump-the-pointer" allocation in Eden space, using Thread-Local Allocation Buffers/TLABs to avoid cross-thread locking) reserves a contiguous block sized as `header + length-field + (length * element size)`, rounded up to the platform's alignment (usually 8 bytes).
4. **Zeroing:** the block is zero-filled, which is *why* Java arrays have guaranteed default values (§2.5) — this isn't a "convenience feature," it's an artifact of how the memory is prepared for safety (Java never exposes uninitialized memory, unlike C).
5. **Header population:** the object header's klass pointer is set to point at the `int[]`'s `Class` metadata (from the Method Area), and the length field is set.
6. **Reference return:** the address of the new object is pushed onto the operand stack, ready to be stored into a local variable, field, or array slot.

```java
int[] arr = new int[5];
```

```
Step 1: newarray bytecode issued
Step 2: length=5 validated (>= 0)
Step 3: allocate contiguous block on heap (Eden, via TLAB bump pointer)
Step 4: zero-fill all 5 int slots -> [0,0,0,0,0]
Step 5: header set: klass -> "int[]" Class object (in Metaspace)
Step 6: reference to this new object stored into local var 'arr' (on stack)
```

### 3.6 Garbage Collection and Arrays

An array becomes eligible for garbage collection the moment **no live reference path** from any GC root (stack references, static fields, active thread objects, etc.) reaches it anymore.

```java
void method() {
    int[] big = new int[1_000_000];
    // ... use big ...
    big = null;   // explicitly drop the only reference
    // 'big' is now eligible for GC even before method() returns
}
```

Common array-related GC considerations:

- **Large arrays and GC pauses:** because arrays are contiguous, copying a very large array during a generational GC promotion (or during a compacting old-gen collection) can be relatively expensive — this is one reason extremely large arrays sometimes cause noticeable GC pause spikes.
- **Memory leaks via retained references:** a classic mistake (famously discussed for stack implementations) is removing a *logical* element from an array-backed structure without nulling out the now-unused reference slot, leaving a dangling reference that prevents GC from reclaiming the object:

```java
Object[] stack = new Object[10];
int top = 3;
Object popped = stack[--top];
// stack[top] (index 3) still references the popped object!
// Fix:
stack[top] = null; // allow GC to reclaim it
```

- **Object arrays vs primitive arrays:** GC only needs to *scan* object arrays (to trace references inside them) — primitive arrays are "leaf" data as far as the garbage collector's reachability graph is concerned, since they contain no further references to trace. This makes primitive arrays cheaper to scan during GC.

### 3.7 Full Memory Diagram Walkthrough

Let's trace a small, complete program through stack and heap:

```java
public class Demo {
    public static void main(String[] args) {
        int[] scores = new int[3];      // (1)
        scores[0] = 90;                 // (2)
        int[] alias = scores;           // (3)
        alias[1] = 85;                  // (4)
        int[] copy = scores.clone();    // (5)
        copy[2] = 100;                  // (6)
    }
}
```

```
After (1):                         After (3):
Stack                Heap          Stack                Heap
┌─────────┐          ┌────────┐    ┌─────────┐          ┌────────┐
│scores─┐ │          │[0,0,0] │    │scores─┐ │          │[0,0,0] │
└───────│─┘          └───▲────┘    │alias──┼─┼──────────▶(same)  │
        └────────────────┘         └───────│─┘          └────────┘
                                            └──────────────▲

After (4) & (5) & (6):
Stack                          Heap
┌─────────┐                    ┌──────────────┐
│scores─┐ │                    │[90, 85, 0]    │◀── scores, alias
│alias──┼─┼────────────────────┤              │
│copy───┼─┼───┐                └──────────────┘
└───────│─┘   │                ┌──────────────┐
        └─────┴───────────────▶│[90, 85, 100]  │◀── copy (independent object)
                                └──────────────┘
```

Notice `scores` and `alias` point to the **same** heap object (mutating through either name is visible through the other), while `copy` — created via `.clone()` — points to a **distinct** heap object that started as a snapshot of `scores` at the moment of cloning, and diverges afterward.

---

## 4. Array Declaration

Java supports several declaration syntaxes, some inherited from C-style compatibility, some idiomatic Java.

### 4.1 The Two Bracket Positions

```java
int[] arr;   // Preferred, idiomatic Java style — brackets attach to the TYPE
int arr[];   // Legal, C-style — brackets attach to the VARIABLE NAME
```

Both are 100% equivalent to the compiler — `arr` has type `int[]` either way. The `int[] arr` form is strongly preferred in Java because it visually groups the type (`int[]`) together, making the declared type obvious at a glance, and it scales better for multiple declarations:

```java
int[] a, b, c;      // a, b, c are ALL int[]   (brackets-on-type: consistent)
int d[], e, f[];     // d is int[], e is int, f is int[]  (brackets-on-name: confusing!)
```

This asymmetry is exactly why style guides (including Java's own conventions) mandate `int[] arr` over `int arr[]`.

### 4.2 Declaration Without Initialization

```java
int[] arr;          // declared, but arr is null — no array object exists yet
System.out.println(arr); // null
// arr[0] = 1;      // NullPointerException — no array object to index into!
```

A bare declaration only creates the **reference variable**; it does not allocate an array object. The reference defaults to `null` (for local variables, you must assign before use, or the compiler rejects the code with "variable might not have been initialized").

### 4.3 Declaration With `new` (Size-Based)

```java
int[] arr = new int[5];          // array of 5 ints, all default 0
String[] names = new String[3];  // array of 3 String refs, all default null
```

`new` allocates the heap object at a fixed length, immediately populated with default values (§2.5).

### 4.4 Declaration With Array Literal (Static Initializer)

```java
int[] arr = {1, 2, 3};              // shorthand array literal
int[] arr2 = new int[]{1, 2, 3};    // explicit equivalent form
```

The bare `{1, 2, 3}` form is **only** legal in a variable declaration statement — it cannot be used to *reassign* an already-declared variable:

```java
int[] arr;
arr = {1, 2, 3};        // COMPILE ERROR — illegal start of expression
arr = new int[]{1,2,3}; // OK — the "new int[]" prefix is required outside declarations
```

### 4.5 Anonymous Array Syntax

An anonymous array is created with `new Type[]{...}` and used immediately, without ever being bound to a variable — most commonly as a method argument or return value:

```java
printAll(new int[]{4, 8, 15, 16, 23, 42});

int[] getDefaults() {
    return new int[]{0, 0, 0};
}
```

### 4.6 Multidimensional Declaration Syntax

```java
int[][] grid;                  // reference to a 2D array, currently null
int[][] grid2 = new int[3][4]; // fully allocated 3x4 grid, all zero
int[][] grid3 = new int[3][];  // 3 row references, each currently null (jagged setup)
int grid4[][];                 // legal C-style, discouraged
int[] grid5[];                 // legal but very confusing — mixed style, AVOID
```

Full multidimensional coverage, including jagged arrays, is in §10.

### 4.7 Declaring Arrays of Generic-Adjacent Types

```java
List<String>[] listArray;         // legal to DECLARE (unchecked warning), but...
listArray = new List[5];          // ...you must create it as a raw type
// listArray = new List<String>[5]; // ILLEGAL — generic array creation not allowed
```

This is discussed fully in §12 ("Generic Limitations").

---

## 5. Array Initialization

Initialization determines *what values* an array's slots hold, as opposed to declaration (the type) or allocation (the size). Java distinguishes several initialization styles:

### 5.1 Default Initialization

Covered in depth in §2.5 — any array created with `new Type[n]` (without an explicit literal) is automatically zero/`null`-filled by the JVM during allocation. This is **automatic** and requires no code from the programmer.

### 5.2 Static Initialization (Compile-Time / Literal Initialization)

Values are known and fixed at compile time, written directly in source code:

```java
int[] primes = {2, 3, 5, 7, 11};
```

This is called "static" initialization not because of the `static` keyword, but because the values are statically (fixedly) known when the code is written — contrast with "dynamic" initialization below.

### 5.3 Dynamic Initialization (Runtime Initialization)

Values are computed or supplied while the program runs — e.g., from user input, a loop, a computation, or an external source:

```java
Scanner sc = new Scanner(System.in);
int[] arr = new int[5];
for (int i = 0; i < arr.length; i++) {
    arr[i] = sc.nextInt();       // filled at runtime, not compile time
}
```

```java
int[] squares = new int[10];
for (int i = 0; i < squares.length; i++) {
    squares[i] = i * i;          // computed dynamically
}
```

### 5.4 Anonymous Initialization

As shown in §4.5, initializing and using an array without naming it:

```java
System.out.println(Arrays.stream(new int[]{3, 1, 4, 1, 5}).sum());
```

### 5.5 User-Input Initialization Patterns

A common real-world/interview setup: read `n`, then read `n` values.

```java
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int[] arr = new int[n];
for (int i = 0; i < n; i++) {
    arr[i] = sc.nextInt();
}
```

**Common mistake:** forgetting that `Scanner.nextInt()` does not consume the trailing newline, which can cause bugs if you mix `nextInt()` with `nextLine()` calls afterward (a String-handling detail, out of scope here, but worth flagging since it frequently corrupts array-input loops in practice).

### 5.6 Initialization with `Arrays.fill` and `Arrays.setAll`

Covered fully in §7, these provide idiomatic ways to dynamically initialize every slot without a manual loop:

```java
int[] arr = new int[5];
Arrays.fill(arr, 7);                          // [7, 7, 7, 7, 7]
Arrays.setAll(arr, i -> i * i);                // [0, 1, 4, 9, 16]
```

### 5.7 Partial Initialization

If you supply fewer literal values than the declared size using `new int[n]` mixed with assignment, remaining slots keep their default:

```java
int[] arr = new int[5];
arr[0] = 10;
arr[2] = 20;
System.out.println(Arrays.toString(arr)); // [10, 0, 20, 0, 0]
```

There is no syntax to *partially* specify a literal array (`{1, 2, }` trailing commas are allowed, but you can't skip an index) — every slot must be assigned individually if you don't want the default.

---

## 6. Traversing Arrays

### 6.1 Classic `for` Loop (Index-Based)

```java
int[] arr = {10, 20, 30, 40};
for (int i = 0; i < arr.length; i++) {
    System.out.println("Index " + i + " = " + arr[i]);
}
```

**When to use:** whenever you need the **index** — for modifying elements, comparing neighbors, traversing multiple arrays in lockstep, iterating backward, or skipping/striding.

### 6.2 Enhanced `for` Loop (For-Each)

```java
for (int value : arr) {
    System.out.println(value);
}
```

**When to use:** when you only need the **values**, not indices, and don't need to mutate the array. Internally, the compiler desugars this into an index-based loop for arrays (unlike for `Iterable`, where it uses an `Iterator`), so there's no performance penalty versus a manual `for` loop.

**Important gotcha:** you **cannot** modify the original array through the for-each variable:

```java
for (int value : arr) {
    value = 0;   // only changes the LOCAL COPY 'value', arr is unchanged!
}
```

This works differently for object arrays regarding the *object's internal state* (you can mutate the object's fields) but you still can't reassign which element of the array that slot refers to — you'd need the index-based form for that.

### 6.3 `while` Loop

```java
int i = 0;
while (i < arr.length) {
    System.out.println(arr[i]);
    i++;
}
```

**When to use:** when the number of iterations, or the termination condition, isn't a simple counter — e.g., traversing until a sentinel value is found, or when the increment logic is non-trivial (two-pointer patterns, see §15).

### 6.4 `do-while` Loop

```java
int i = 0;
do {
    System.out.println(arr[i]);
    i++;
} while (i < arr.length);
```

**When to use:** rarely, for arrays — mainly when you must guarantee at least one iteration executes even if the array might be empty (though for empty arrays this is usually a bug source, since `arr[0]` would throw if `length == 0`). Generally the plain `for` loop is safer and more idiomatic for array traversal.

### 6.5 Streams (Basic Traversal)

```java
int[] arr = {1, 2, 3, 4, 5};

int sum = Arrays.stream(arr).sum();
double avg = Arrays.stream(arr).average().orElse(0);
int max = Arrays.stream(arr).max().getAsInt();
Arrays.stream(arr).forEach(System.out::println);
int[] doubled = Arrays.stream(arr).map(x -> x * 2).toArray();
```

`Arrays.stream(int[])` returns an `IntStream` (a primitive specialization, avoiding boxing overhead). For object arrays, `Arrays.stream(T[])` returns a `Stream<T>`.

**When to use:** for concise, functional-style aggregate operations (sum, max, filtering, mapping to a new array). Streams have per-call overhead (pipeline setup) that makes them slower than a raw loop for very simple/hot-path operations, so in performance-critical or competitive-programming contexts, a manual loop is usually still preferred (see §13).

### 6.6 Traversal Direction and Index vs Value — When to Use Each

| Goal | Best traversal |
|---|---|
| Need index (modify, compare positions, two-pointer) | Classic `for` |
| Only need values, read-only | Enhanced `for` |
| Traverse backward | Classic `for` (`i = arr.length - 1; i >= 0; i--`) |
| Traverse two arrays in lockstep | Classic `for` |
| Aggregate computation (sum/max/filter/map) | Streams (readability) or classic `for` (raw speed) |
| Early exit / complex condition | `while` |
| Multidimensional traversal | Nested classic `for` (see §10) |

### 6.7 Traversing Multidimensional Arrays

```java
int[][] grid = {{1,2,3},{4,5},{6,7,8,9}};   // jagged
for (int i = 0; i < grid.length; i++) {
    for (int j = 0; j < grid[i].length; j++) {   // NOTE: grid[i].length, not grid.length!
        System.out.print(grid[i][j] + " ");
    }
    System.out.println();
}
```

Using `grid[0].length` as the inner bound for *every* row is a classic bug for jagged arrays — each row can have a different length, so you must query `grid[i].length` inside the outer loop.

---

## 7. The java.util.Arrays Utility Class

`java.util.Arrays` is a **final class of static utility methods** for array manipulation — you never instantiate it (its constructor is private). It is the single most important API surface for practical array work in Java.

### 7.1 `Arrays.toString(T[])` / `Arrays.toString(int[])` etc.

Produces a readable, single-level string representation.

```java
int[] a = {1, 2, 3};
System.out.println(Arrays.toString(a));   // [1, 2, 3]
```

Overloaded for every primitive array type and `Object[]`. **Does not** recurse into nested arrays — for 2D+ arrays it prints inner array identity hashes, e.g. `[[I@1b6d3586, [I@4554617c]`.

### 7.2 `Arrays.deepToString(Object[])`

Recursively stringifies nested (multidimensional) arrays.

```java
int[][] grid = {{1,2},{3,4}};
System.out.println(Arrays.deepToString(grid));  // [[1, 2], [3, 4]]
```

### 7.3 `Arrays.fill(...)`

Fills an entire array, or a sub-range, with a single value.

```java
int[] a = new int[5];
Arrays.fill(a, 9);                 // [9, 9, 9, 9, 9]
Arrays.fill(a, 1, 3, 0);           // fill indices [1,3) -> [9, 0, 0, 9, 9]
```

### 7.4 `Arrays.copyOf(original, newLength)`

Returns a **new array** of the given length, copying elements from `original`. If `newLength` is larger, extra slots get default values; if smaller, elements are truncated.

```java
int[] a = {1, 2, 3};
int[] b = Arrays.copyOf(a, 5);   // [1, 2, 3, 0, 0]
int[] c = Arrays.copyOf(a, 2);   // [1, 2]
```

Internally, `Arrays.copyOf` allocates the new array and delegates to `System.arraycopy` (§8) for the actual bulk copy — it is essentially a convenience wrapper.

### 7.5 `Arrays.copyOfRange(original, from, to)`

Returns a new array containing elements `[from, to)` — `to` is exclusive and may exceed `original.length` (padding with defaults).

```java
int[] a = {10, 20, 30, 40, 50};
int[] b = Arrays.copyOfRange(a, 1, 4);  // [20, 30, 40]
```

### 7.6 `Arrays.equals(a, b)` and `Arrays.deepEquals(a, b)`

`Arrays.equals` does an element-by-element (shallow) comparison for 1D arrays — exactly what beginners *expect* `arr1.equals(arr2)` to do, but which `Object.equals` does not provide (§2.3).

```java
int[] a = {1, 2, 3};
int[] b = {1, 2, 3};
System.out.println(a.equals(b));         // false (reference equality)
System.out.println(Arrays.equals(a, b)); // true (content equality)
```

For nested/multidimensional arrays, `Arrays.equals` only compares the *outer* references (so two equal 2D arrays would still report `false`, because it compares `int[]` element references, not their contents) — you need `Arrays.deepEquals` for recursive, content-based comparison:

```java
int[][] g1 = {{1,2},{3,4}};
int[][] g2 = {{1,2},{3,4}};
System.out.println(Arrays.equals(g1, g2));      // false! compares row REFERENCES
System.out.println(Arrays.deepEquals(g1, g2));  // true — recursive content compare
```

### 7.7 `Arrays.compare(a, b)`

Lexicographic comparison, similar in spirit to `String.compareTo`. Returns negative/zero/positive.

```java
System.out.println(Arrays.compare(new int[]{1,2,3}, new int[]{1,2,4})); // negative
System.out.println(Arrays.compare(new int[]{1,2}, new int[]{1,2,3}));   // negative (shorter prefix < longer)
```

### 7.8 `Arrays.binarySearch(a, key)` — API Usage Only

Performs a binary search on a **sorted** array and returns the index of `key`, or `-(insertion point) - 1` if not found. (This handbook covers *usage* of this API method only — the binary search *algorithm* itself belongs to a dedicated searching-algorithms handbook.)

```java
int[] sorted = {1, 3, 5, 7, 9};
System.out.println(Arrays.binarySearch(sorted, 5));  // 2
System.out.println(Arrays.binarySearch(sorted, 4));  // negative, e.g. -3 (insert before index 2)
```

**Precondition:** the array **must already be sorted**, or behavior is undefined (no exception — just wrong answers).

### 7.9 `Arrays.mismatch(a, b)`

Returns the index of the first differing element, or `-1` if the arrays are equal (up to the shorter length).

```java
System.out.println(Arrays.mismatch(new int[]{1,2,3}, new int[]{1,2,9})); // 2
System.out.println(Arrays.mismatch(new int[]{1,2}, new int[]{1,2,3}));   // 2 (length diff counts as mismatch point)
```

### 7.10 `Arrays.setAll(array, generator)` / `Arrays.parallelSetAll(...)`

Fills every index using an `IntUnaryOperator` (for `int[]`) or `IntFunction<T>` (for object arrays), receiving the index as input.

```java
int[] squares = new int[5];
Arrays.setAll(squares, i -> i * i);       // [0, 1, 4, 9, 16]

String[] labels = new String[3];
Arrays.setAll(labels, i -> "item-" + i);  // [item-0, item-1, item-2]
```

`Arrays.parallelSetAll` does the same thing but splits work across multiple threads via the common `ForkJoinPool` — worthwhile only for very large arrays with expensive generator functions (thread coordination overhead dominates for small arrays).

### 7.11 `Arrays.parallelPrefix(array, op)`

Computes an in-place prefix computation (like a running total) in parallel.

```java
int[] a = {1, 2, 3, 4};
Arrays.parallelPrefix(a, (x, y) -> x + y);
System.out.println(Arrays.toString(a));   // [1, 3, 6, 10] (running sums)
```

### 7.12 `Arrays.stream(array)`

Converts an array into a `Stream` (covered with examples in §6.5).

### 7.13 `Arrays.spliterator(array)`

Returns a `Spliterator` over the array, the lower-level abstraction that backs stream traversal and supports splitting for parallel processing. Rarely used directly except when hand-building custom parallel/stream pipelines.

```java
Spliterator<Integer> sp = Arrays.spliterator(new Integer[]{1,2,3});
sp.forEachRemaining(System.out::println);
```

### 7.14 `Arrays.hashCode(array)` / `Arrays.deepHashCode(array)`

Computes a content-based hash code (unlike `array.hashCode()`, which is identity-based, §2.3). `deepHashCode` recurses into nested arrays, mirroring `deepEquals`.

```java
System.out.println(Arrays.hashCode(new int[]{1,2,3}));      // content-based, consistent across calls with equal content
System.out.println(Arrays.deepHashCode(new int[][]{{1,2}}));// recursive
```

### 7.15 `Arrays.sort(...)` (Mentioned for Completeness — API Usage Only)

`Arrays.sort(array)` sorts in place, ascending. (The sorting **algorithm** itself — dual-pivot quicksort for primitives, a stable Timsort-derived merge sort for objects — is out of scope for this handbook, per the array-only scope; it belongs in a dedicated sorting-algorithms handbook. We mention the API call only because it's frequently a *prerequisite step* inside array-manipulation interview problems, e.g. §14.)

```java
int[] a = {5, 3, 1, 4, 2};
Arrays.sort(a);                          // [1, 2, 3, 4, 5]
Arrays.sort(a, 1, 4);                    // sort only sub-range [1,4)
```

### 7.16 Full API Quick Table

| Method | Purpose |
|---|---|
| `toString` | Print 1D array |
| `deepToString` | Print nested array |
| `fill` | Fill with constant |
| `copyOf` | New array, resized |
| `copyOfRange` | New array, sub-range |
| `equals` | Shallow content compare |
| `deepEquals` | Recursive content compare |
| `compare` | Lexicographic ordering |
| `binarySearch` | Search sorted array |
| `mismatch` | First differing index |
| `setAll` / `parallelSetAll` | Generate values by index |
| `parallelPrefix` | In-place running aggregate |
| `stream` | Convert to Stream |
| `spliterator` | Low-level split-traversal source |
| `hashCode` / `deepHashCode` | Content-based hash |
| `sort` | In-place sort (algorithm out of scope) |
| `asList` | View array as fixed-size `List` (see §11) |

---

## 8. System.arraycopy()

### 8.1 Signature and Working

```java
public static void arraycopy(Object src, int srcPos,
                              Object dest, int destPos, int length)
```

`System.arraycopy` is a **native method** (implemented in C/C++ inside the JVM itself, not in Java bytecode), which lets the JVM use highly optimized, platform-specific bulk-memory-move instructions (often a direct `memmove`-equivalent) rather than a per-element Java loop.

```java
int[] src = {1, 2, 3, 4, 5};
int[] dest = new int[5];
System.arraycopy(src, 0, dest, 0, 5);
System.out.println(Arrays.toString(dest)); // [1, 2, 3, 4, 5]
```

**Parameters explained:**
- `src` — the source array.
- `srcPos` — starting index in `src` to begin copying from.
- `dest` — the destination array (**must already exist** — `arraycopy` never allocates).
- `destPos` — starting index in `dest` to begin writing to.
- `length` — number of elements to copy.

### 8.2 Overlapping Copies Are Safe

Unlike a naive hand-written loop, `System.arraycopy` correctly handles the case where `src` and `dest` are the **same array** and the ranges overlap — it behaves like `memmove` (copies via a temporary buffer semantics), not like a naive `memcpy`:

```java
int[] a = {1, 2, 3, 4, 5};
System.arraycopy(a, 0, a, 1, 4);   // shift everything right by one
System.out.println(Arrays.toString(a)); // [1, 1, 2, 3, 4]
```

A hand-rolled forward loop doing `a[i+1] = a[i]` for increasing `i` would corrupt the data (it would overwrite `a[i]` before reading it for the next iteration in some directions) — `System.arraycopy` avoids this entirely, which is one of its biggest practical advantages for in-place shifting (used heavily in §14's rotate-array and insert/delete-in-place problems).

### 8.3 Performance

Because it's implemented natively and can leverage vectorized/SIMD or block-move CPU instructions, `System.arraycopy` is typically **faster** than an equivalent hand-written Java `for` loop for medium-to-large copies, and it's what `Arrays.copyOf`, `Arrays.copyOfRange`, `ArrayList`'s internal resizing, and `Collections` bulk operations all use under the hood.

| Approach | Relative speed | Notes |
|---|---|---|
| `System.arraycopy` | Fastest | Native, often vectorized, handles overlap safely |
| `Arrays.copyOf` / `copyOfRange` | Same as arraycopy | Thin wrapper — allocates then delegates |
| Manual `for` loop | Slower for bulk copy | JIT can sometimes optimize simple loops well, but rarely beats native arraycopy for large N |
| `.clone()` | Comparable to arraycopy | JVM-intrinsic for array clone, internally similar to a bulk copy |

### 8.4 Type Requirements

Both `src` and `dest` must be arrays of **compatible** types (same primitive type, or a supertype-compatible object array); mismatches throw `ArrayStoreException` at runtime (for object arrays) or `ArrayStoreException`/`ArrayIndexOutOfBoundsException` as appropriate. Copying between different primitive types (e.g., `int[]` into `double[]`) is **not** allowed — there's no implicit widening across whole arrays.

### 8.5 Comparison with `Arrays.copyOf()`

- `System.arraycopy` copies **into an existing, pre-allocated destination array** — you control exactly where in `dest` the data lands, and it can copy partial ranges to/from arbitrary offsets in *both* source and destination.
- `Arrays.copyOf` **always allocates a brand-new array** starting at index 0 of the destination, sized exactly as requested — simpler API, less flexible.

Use `System.arraycopy` when you need fine control (partial overwrites, shifting within one array, merging into a pre-sized buffer). Use `Arrays.copyOf`/`copyOfRange` when you just want "give me a resized/sub-range copy" without managing the destination array yourself.

---

## 9. Copying Arrays — Shallow, Deep, and Reference Copies

Java offers several distinct ways to "copy" an array, and they are **not interchangeable** — mixing them up is one of the most common sources of subtle bugs.

### 9.1 Reference Copy (Assignment) — NOT a Real Copy

```java
int[] a = {1, 2, 3};
int[] b = a;     // b is just another name for the SAME object
b[0] = 99;
System.out.println(a[0]); // 99 — 'a' changed too!
```

This is not a copy at all — both variables alias one heap object (§3.4). This is the single most common source of "I didn't even touch that array!" bugs.

### 9.2 Shallow Copy via `.clone()`

```java
int[] a = {1, 2, 3};
int[] b = a.clone();
b[0] = 99;
System.out.println(a[0]); // 1 — independent array now
```

For **primitive arrays**, `.clone()` is effectively a full/deep copy, since the elements *are* the values — there's nothing further to alias.

For **object arrays**, `.clone()` is only **shallow**: it copies the array of references, but the objects those references point to are still shared:

```java
int[][] grid = {{1,2},{3,4}};
int[][] copyGrid = grid.clone();
copyGrid[0][0] = 99;
System.out.println(grid[0][0]); // 99! grid[0] and copyGrid[0] are the SAME inner array
```

```
grid.clone() shallow copy of a 2D array:

grid      ──▶ [ref_row0, ref_row1]
copyGrid  ──▶ [ref_row0, ref_row1]   ← new OUTER array, but SAME inner row objects
                   │         │
                   ▼         ▼
                [1,2]      [3,4]     ← shared! mutating via either outer array shows through
```

### 9.3 Shallow Copy via `Arrays.copyOf` / `Arrays.copyOfRange` / `System.arraycopy`

All three behave the same way regarding depth: for primitive arrays they produce full independent copies; for object/2D arrays they only copy the top-level references, leaving inner arrays/objects shared — identical caveat to `.clone()`.

```java
String[][] a = {{"a","b"}};
String[][] b = Arrays.copyOf(a, a.length);
b[0][0] = "Z";
System.out.println(a[0][0]); // "Z" — inner row array still shared
```

### 9.4 Deep Copy

A **true deep copy** of a multidimensional or object array requires manually copying every nested level:

```java
int[][] original = {{1,2},{3,4,5}};
int[][] deepCopy = new int[original.length][];
for (int i = 0; i < original.length; i++) {
    deepCopy[i] = Arrays.copyOf(original[i], original[i].length); // copy EACH row independently
}
deepCopy[0][0] = 99;
System.out.println(original[0][0]); // 1 — fully independent now
```

For arrays of mutable custom objects, a true deep copy additionally requires either a copy constructor or a `deepClone()`-style method on the element type itself — `Arrays`/`System.arraycopy` alone cannot deep-copy arbitrary object graphs.

### 9.5 Summary Table

| Method | Copies outer array? | Copies nested/referenced content? | Speed |
|---|---|---|---|
| `b = a` (assignment) | No — same object | No | O(1), but NOT a copy |
| `a.clone()` | Yes, new outer array | No (shallow) | Fast, native |
| `Arrays.copyOf(a, n)` | Yes | No (shallow) | Fast, native (delegates to arraycopy) |
| `Arrays.copyOfRange(a, i, j)` | Yes | No (shallow) | Fast, native |
| `System.arraycopy(...)` | Copies into given dest | No (shallow) | Fastest, native |
| Manual nested loop | Yes | Yes, if applied recursively | Slower, but only real deep-copy option |

### 9.6 Memory Diagram: All Four Together

```java
int[] original = {1, 2, 3};
int[] refCopy    = original;
int[] shallow    = original.clone();
int[] range      = Arrays.copyOfRange(original, 0, 3);
```

```
original ──┐
refCopy  ──┴──▶ [1, 2, 3]   (ONE shared object)

shallow  ──▶ [1, 2, 3]   (independent object #2)

range    ──▶ [1, 2, 3]   (independent object #3)
```

(For primitive arrays, "shallow" and "deep" collapse into the same thing, since there's no further nesting to worry about — the shallow-vs-deep distinction only bites for object/multidimensional arrays.)

---

## 10. Multidimensional Arrays

### 10.1 Java Has No True Multidimensional Arrays

As previewed in §2.7: `int[][] grid` is really an **array of `int[]` references**. There is no single contiguous N-dimensional memory block, unlike languages like C or Fortran. Understanding this is essential — it explains jagged arrays, per-row `.length`, and why 2D array creation is really two allocation steps.

### 10.2 2D Array Creation, Step by Step

```java
int[][] grid = new int[3][4];
```

What actually happens:

1. Allocate an **outer array** of length 3, holding `int[]` references (initially would-be `null`, but...)
2. Because both dimensions were specified, the JVM **also immediately allocates** 3 separate `int[4]` arrays and wires each outer slot to point at one.

```
Outer array (length 3, holds references):
┌─────┬─────┬─────┐
│ ref │ ref │ ref │
└──┬──┴──┬──┴──┬──┘
   ▼     ▼     ▼
 [0,0, [0,0, [0,0,
  0,0]  0,0]  0,0]     ← 3 independent int[4] row arrays
```

```java
grid[1][2] = 99;   // navigate: outer[1] -> gives a row (int[4]); then row[2] = 99
```

### 10.3 Jagged Arrays

Because rows are independent array objects, they can have **different lengths** — this is a "jagged" (a.k.a. "ragged") array, and it is the **normal, native** form of multidimensional array in Java (a rectangular grid is just a special case where all rows happen to be equal length).

```java
int[][] jagged = new int[3][];        // only allocate the OUTER array; rows are null
jagged[0] = new int[]{1};
jagged[1] = new int[]{1, 2, 3};
jagged[2] = new int[]{1, 2};

for (int[] row : jagged) {
    System.out.println(Arrays.toString(row));
}
// [1]
// [1, 2, 3]
// [1, 2]
```

```
jagged ──▶ [ref0, ref1, ref2]
              │     │     │
              ▼     ▼     ▼
             [1]  [1,2,3] [1,2]     ← different lengths, perfectly legal
```

Jagged array literals can also be written directly:

```java
int[][] jagged2 = {{1}, {1, 2, 3}, {1, 2}};
```

### 10.4 3D Arrays

The same "array of arrays (of arrays)" principle extends recursively:

```java
int[][][] cube = new int[2][3][4];
// cube: 2 refs to int[3][4]; each of THOSE is 3 refs to int[4]
cube[1][2][3] = 7;
```

```
cube (length 2)
 ├── cube[0] (int[3][4])
 │     ├── cube[0][0] (int[4])
 │     ├── cube[0][1] (int[4])
 │     └── cube[0][2] (int[4])
 └── cube[1] (int[3][4])
       ├── cube[1][0] (int[4])
       ├── cube[1][1] (int[4])
       └── cube[1][2] (int[4])   <- cube[1][2][3] = 7 lands here
```

3D (and higher) arrays are legal but rare in typical application code; they appear more often in numerical/scientific computing or specific competitive-programming problems (e.g., 3D DP state tables — DP itself out of scope here, but the *array* mechanics are the same).

### 10.5 Partial Allocation Patterns

```java
int[][] a = new int[3][4];   // fully allocated rectangular grid
int[][] b = new int[3][];    // only outer allocated; must fill rows manually
// int[][] c = new int[][4]; // ILLEGAL — cannot specify inner size while leaving outer unsized
```

The rule: you may omit trailing dimension sizes (rightmost), but never a *leading* one — the JVM must always know the outer length first to allocate the reference array.

### 10.6 Multidimensional Traversal Patterns

**Row-major traversal (idiomatic, matches memory-adjacency of the outer array):**

```java
for (int i = 0; i < grid.length; i++) {
    for (int j = 0; j < grid[i].length; j++) {
        process(grid[i][j]);
    }
}
```

**Enhanced for-each (read-only, cleanest for simple processing):**

```java
for (int[] row : grid) {
    for (int val : row) {
        process(val);
    }
}
```

**Column-major traversal** (less cache-friendly, since it jumps between different row objects on each step — see §13):

```java
for (int j = 0; j < grid[0].length; j++) {
    for (int i = 0; i < grid.length; i++) {
        process(grid[i][j]);
    }
}
```

### 10.7 Multidimensional Array Utility Support

`Arrays.deepToString` and `Arrays.deepEquals`/`deepHashCode` (§7) are specifically designed for multidimensional arrays, since the plain (non-deep) versions only look one level deep. `Arrays.fill` does **not** recurse — filling a 2D array requires an explicit loop over rows:

```java
int[][] grid = new int[3][4];
for (int[] row : grid) {
    Arrays.fill(row, -1);
}
```

### 10.8 Visualization: Rectangular vs Jagged

```
Rectangular (new int[3][4]):        Jagged ({{1},{1,2,3},{1,2}}):
┌──┬──┬──┬──┐                       ┌──┐
│ 0│ 0│ 0│ 0│                       │ 1│
├──┼──┼──┼──┤                       ├──┼──┬──┐
│ 0│ 0│ 0│ 0│                       │ 1│ 2│ 3│
├──┼──┼──┼──┤                       ├──┼──┤
│ 0│ 0│ 0│ 0│                       │ 1│ 2│
└──┴──┴──┴──┘                       └──┴──┘
```

---

## 11. Array vs ArrayList

This section **only compares** arrays against `ArrayList` — it does not teach `ArrayList`'s internal implementation, API, or usage patterns in depth, per the scope of this handbook.

### 11.1 Fixed vs Dynamic Sizing

| | Array | ArrayList |
|---|---|---|
| Size | Fixed at creation, immutable for the object's life | Logically dynamic — grows/shrinks via `add`/`remove` |
| Underlying storage | The array itself | Wraps an internal array, reallocated (grown) as needed |
| Resizing mechanism | None — must create a new array manually | Automatic, amortized internally via array-doubling-style growth |

### 11.2 Primitive Support

| | Array | ArrayList |
|---|---|---|
| Primitive types | Native support: `int[]`, `double[]`, etc. — no boxing | **No** primitive support — `ArrayList<Integer>`, `ArrayList<Double>`, etc. only; every element is boxed |

This is a major performance differentiator (§13): `int[]` stores raw ints contiguously; `ArrayList<Integer>` stores references to boxed `Integer` objects scattered across the heap, with associated boxing/unboxing overhead on every read/write.

### 11.3 Performance

| Operation | Array | ArrayList |
|---|---|---|
| Random access `[i]` | O(1), no overhead | O(1), but with method-call + (for `<Integer>`) unboxing overhead |
| Append at end | N/A (fixed size) | O(1) amortized (occasional O(n) resize) |
| Insert/remove in middle | Manual shifting required, O(n) | O(n) internally (still shifts), but API does it for you |
| Memory overhead | Minimal — just header + elements | Extra: object wrapper overhead, boxed elements, unused capacity slack |

### 11.4 Type Safety and Generics

Arrays support primitives directly and are **covariant** (`Object[] objs = new String[3];` compiles — see §12), which trades compile-time safety for runtime flexibility (and can cause `ArrayStoreException`). `ArrayList<T>` uses generics, which are **invariant** and **type-erased**, giving stronger compile-time checking but no primitive support and no reflection-visible element type at runtime.

### 11.5 API Richness

Arrays have a comparatively **minimal API** — indexing, `.length`, and whatever `java.util.Arrays` provides externally (§7). `ArrayList` (via the `List`/`Collection` interfaces) offers a much richer built-in API surface — but discussing that API in depth is out of scope here; we mention its *existence* only for comparison purposes.

### 11.6 When to Use Which (Interview Framing)

**Use an array when:**
- The size is known and fixed for the object's lifetime.
- You need primitive elements without boxing overhead (performance-critical numeric code).
- You're implementing a lower-level data structure yourself (a heap, hash table, custom buffer) that needs raw, predictable memory layout.
- Competitive programming, where raw speed and minimal overhead matter most.

**Use an ArrayList when:**
- The number of elements isn't known upfront or changes over the object's lifetime.
- You want built-in insert/remove/search convenience methods.
- You need to store objects and want generics-based compile-time type safety alongside the rest of the Collections Framework (sorting via `Comparator`, iterators, etc. — details out of scope here).

### 11.7 Converting Between Them

```java
// Array -> List view (fixed-size, backed by the array — writes show through!)
Integer[] boxed = {1, 2, 3};
List<Integer> view = Arrays.asList(boxed);
view.set(0, 99);
System.out.println(boxed[0]); // 99 — Arrays.asList is a VIEW, not a copy!
// view.add(4);  // UnsupportedOperationException — fixed-size view, can't grow

// List -> Array
List<Integer> list = new ArrayList<>(List.of(1, 2, 3));
Integer[] arr = list.toArray(new Integer[0]);
```

`Arrays.asList` cannot be used directly on a primitive array as you might expect — `Arrays.asList(new int[]{1,2,3})` produces a `List<int[]>` with **one element** (the whole array itself), not a `List<Integer>`, because generics require a reference type and `int[]` itself satisfies that as a single object. This is a classic gotcha.

---

## 12. Java Language Features Relevant to Arrays

### 12.1 `.length`

Every array (of any type, any dimension) exposes a **public, final field** called `length` (note: a field, not a method — unlike `String.length()`, which *is* a method; mixing these up is an extremely common beginner mistake).

```java
int[] arr = {1, 2, 3};
System.out.println(arr.length);      // 3 (field access, no parentheses)
// System.out.println(arr.length()); // COMPILE ERROR
```

For multidimensional arrays, `.length` at each level tells you that level's size:

```java
int[][] grid = new int[3][4];
System.out.println(grid.length);     // 3 (number of rows)
System.out.println(grid[0].length);  // 4 (length of first row)
```

### 12.2 `final` Arrays

`final` on an array variable locks the **reference**, not the contents:

```java
final int[] arr = {1, 2, 3};
arr[0] = 99;          // LEGAL — mutating contents through a final reference is fine
// arr = new int[5];  // COMPILE ERROR — cannot reassign a final reference
```

This is a very common interview trick question: "is a `final` array mutable?" — Yes, its *elements* are mutable; only *reassignment of the variable itself* is prohibited. There is no built-in way to make an array's contents immutable (unlike, say, wrapping a `List` with `Collections.unmodifiableList`) — you'd need to manually wrap access or defensively copy.

### 12.3 Passing Arrays to Methods

Arrays are objects, so they are passed **by reference value** — technically Java is always pass-by-value, but what gets passed *is a copy of the reference*, which still points at the same heap object. This means:

```java
static void zeroOut(int[] a) {
    for (int i = 0; i < a.length; i++) a[i] = 0;  // mutates the ORIGINAL array's contents
}

static void reassign(int[] a) {
    a = new int[]{9, 9, 9};   // only reassigns the LOCAL parameter variable, caller unaffected
}

int[] data = {1, 2, 3};
zeroOut(data);
System.out.println(Arrays.toString(data));  // [0, 0, 0] — mutation visible!
reassign(data);
System.out.println(Arrays.toString(data));  // [0, 0, 0] — unaffected, reassignment was local
```

### 12.4 Returning Arrays from Methods

Perfectly normal and common — the method returns a reference to a (usually newly-created) array object:

```java
static int[] makeSquares(int n) {
    int[] result = new int[n];
    for (int i = 0; i < n; i++) result[i] = i * i;
    return result;
}
```

**Best practice:** avoid returning a reference to an internal, mutable array field directly if callers shouldn't be able to corrupt your object's internal state — return a defensive copy (`.clone()` or `Arrays.copyOf`) instead when encapsulation matters.

### 12.5 Varargs

Varargs (`Type... name`) is syntactic sugar — under the hood, the compiler transforms the parameter into an actual array (`Type[] name`) at the call site.

```java
static int sum(int... nums) {          // 'nums' is really an int[] inside the method
    int total = 0;
    for (int n : nums) total += n;
    return total;
}

sum();                 // nums = new int[0] (empty array, not null!)
sum(1, 2, 3);           // nums = new int[]{1, 2, 3}
sum(new int[]{4, 5});   // you can also pass an actual array directly
```

Varargs must be the **last** parameter in a method signature, and a method may have at most one varargs parameter.

### 12.6 Arrays of Objects, Classes, Records, Enums, and Interfaces

Arrays work uniformly across all reference types:

```java
record Point(int x, int y) {}
enum Direction { NORTH, SOUTH, EAST, WEST }
interface Shape { double area(); }

Point[] points = { new Point(0,0), new Point(1,1) };
Direction[] dirs = Direction.values();          // built-in array-returning method on every enum
Shape[] shapes = { () -> 3.14, () -> 2.71 };    // array of lambda-backed interface instances
```

`Enum.values()` deserves special mention: it **returns a new array on every call** (a defensive copy of the enum constants), specifically to prevent callers from mutating the enum's canonical constant ordering — calling `.values()` in a hot loop repeatedly is a minor but real performance smell.

### 12.7 Generic Array Limitations

You **cannot** directly create a generic array in Java, e.g. `new T[10]` or `new List<String>[5]` — this is disallowed due to **type erasure**: at runtime, the JVM has no record of `T` or `<String>`, so it cannot populate the array's runtime component-type metadata correctly, which would silently break the array-covariance runtime check (`ArrayStoreException`, §12.8) that arrays rely on for safety.

```java
class Box<T> {
    // T[] items = new T[10];        // COMPILE ERROR
    Object[] items = new Object[10]; // common workaround: use Object[] and cast on read
    
    @SuppressWarnings("unchecked")
    T[] itemsAlt = (T[]) new Object[10]; // "unchecked" cast workaround, used cautiously
}
```

This is precisely why generic collections (`ArrayList<T>`) internally store an `Object[]` and cast on retrieval, rather than a true `T[]`.

### 12.8 Autoboxing, Unboxing, and Array Covariance / `ArrayStoreException`

**Autoboxing/unboxing** happens automatically when converting between primitives and their wrapper classes — but this does **not** extend to whole arrays. `int[]` can never be autoboxed into `Integer[]`, or vice versa; you must manually loop and box/unbox each element.

```java
int[] primArr = {1, 2, 3};
// Integer[] boxedArr = primArr;   // COMPILE ERROR — no array-level autoboxing
Integer[] boxedArr = new Integer[primArr.length];
for (int i = 0; i < primArr.length; i++) boxedArr[i] = primArr[i]; // per-element autobox
```

**Array covariance:** object arrays in Java are *covariant* — `String[]` is-a `Object[]` at the type-system level, which allows flexible method signatures (e.g., a method taking `Object[]`) but introduces a **runtime-only safety check**:

```java
Object[] objs = new String[3];   // legal — covariance
objs[0] = "ok";                  // fine, String fits
objs[1] = 42;                    // COMPILES fine (Integer is an Object)...
                                  // ...but throws ArrayStoreException AT RUNTIME!
```

The JVM stores the *actual* runtime component type (`String`, from the original `new String[3]`) in the array's header metadata, and checks every object-array write against it — this is the safety net that generic-array-creation restrictions (§12.7) exist to preserve, since generics erase this information at compile time but arrays enforce it live, at runtime.

**Primitive arrays are NOT covariant** — `int[]` is not an `Object[]` subtype at all (primitives aren't objects), so there's no equivalent runtime check needed or possible; `double[] d = new int[3];` doesn't even compile.

### 12.9 Primitive Arrays vs Wrapper Arrays — Summary

| | `int[]` | `Integer[]` |
|---|---|---|
| Storage | Raw values, inline, contiguous | References to boxed `Integer` objects |
| Default value | `0` | `null` |
| Can use with generics (`List<T>`, etc.) | No (must box) | Yes |
| Autoboxing per element | N/A | Automatic on assignment of an `int` literal |
| Cache locality | Excellent | Poor (pointer chasing, §13) |
| `null` elements possible | No | Yes — and a frequent source of `NullPointerException` during unboxing |

---

## 13. Performance Deep Dive

### 13.1 Cache Locality

Modern CPUs read memory into small, fast **cache lines** (typically 64 bytes). When you access `arr[i]`, the CPU doesn't fetch just that one value — it pulls in the whole cache line around it, anticipating that nearby memory will be accessed soon (**spatial locality**).

Because primitive arrays store values **contiguously**, sequential traversal (`for i in 0..n: use(arr[i])`) gets near-maximum cache benefit — most accesses are "free" cache hits after the first one per cache line.

```
Cache line (64 bytes) for int[] (4 bytes/int):
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│a[0]│a[1]│a[2]│a[3]│a[4]│a[5]│a[6]│a[7]│a[8]│a[9]│... │    │    │    │    │    │
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
  One memory fetch loads 16 ints — sequential access reuses this heavily.
```

### 13.2 Primitive Arrays vs Object Arrays — Performance

Object arrays (`Integer[]`, `String[]`, custom types) store only **references** contiguously; the actual objects are typically scattered across the heap (allocated at different times, in different Eden regions). Iterating an `Integer[]` therefore involves **pointer chasing**: each access is a cache-line fetch for the reference array *plus* a likely cache-miss fetch for the referenced object itself.

```
int[] (contiguous values):        Integer[] (contiguous refs, scattered objects):
[1][2][3][4][5]                   [ref][ref][ref][ref][ref]
 ▲ all in one cache-friendly line    │    │    │    │    │
                                     ▼    ▼    ▼    ▼    ▼
                                   [1]  [2]  [3]  [4]  [5]   ← scattered across heap!
```

This is the primary reason `int[]` significantly outperforms `Integer[]` / `ArrayList<Integer>` for numeric-heavy workloads (numerical algorithms, competitive programming, matrix math) — not just because of boxing CPU cost, but because of cache-miss-driven memory latency.

### 13.3 Reference Chasing Cost in Multidimensional Arrays

A 2D array `int[][]` is itself "array of arrays" (§10) — so row-major traversal (iterating `j` in the inner loop) is cache-friendly *within* a row, but jumping between rows (`grid[i]`) is a pointer dereference to a **potentially distant** heap location. Column-major traversal (iterating `i` in the inner loop) is significantly worse, since it jumps between different row objects on almost every access.

```java
// GOOD: row-major (cache-friendly)
for (int i = 0; i < rows; i++)
    for (int j = 0; j < cols; j++)
        sum += grid[i][j];

// BAD: column-major (cache-hostile for large grids)
for (int j = 0; j < cols; j++)
    for (int i = 0; i < rows; i++)
        sum += grid[i][j];
```

For large grids, row-major traversal can be **several times faster** in practice due to cache effects, even though both do the exact same number of arithmetic operations — a favorite performance-reasoning interview question.

### 13.4 GC Impact

- **Primitive arrays** contain no references, so the garbage collector treats them as "leaf" memory during reachability tracing — cheap to scan.
- **Object arrays** must be fully scanned by the GC to trace every contained reference — larger object arrays with many live references add more work to each GC cycle.
- Very large arrays (of either kind) can affect **pause times** during compacting/copying collections, since moving a huge contiguous block (or updating many reference fields) takes proportional time.

### 13.5 Memory Footprint

| Array type | Per-element overhead |
|---|---|
| `int[]` | 4 bytes (just the value) |
| `Integer[]` | 4 bytes (reference) + ~16 bytes (boxed `Integer` object header + value), often more with alignment padding — roughly 5x+ the memory of `int[]` for the same logical data |
| `boolean[]` | 1 byte per element (JVM-dependent; not bit-packed by default) |

If you need a genuinely bit-packed boolean array for memory efficiency (e.g., a large boolean flag array), a `long[]` used as a manual bitset (each `long` holding 64 flags) uses 64x less memory than `boolean[]` — a common competitive-programming optimization.

### 13.6 Performance Optimization Checklist

- Prefer primitive arrays (`int[]`, `double[]`, ...) over boxed object arrays / `ArrayList<Integer>` whenever raw numeric performance matters.
- Favor row-major traversal order for 2D/3D arrays to maximize cache locality.
- Use `System.arraycopy` / `Arrays.copyOf` for bulk copies instead of manual element-by-element loops.
- Avoid unnecessary array reallocation inside hot loops — pre-size arrays when the final size is knowable upfront.
- Be aware that `Arrays.asList`/streams add small per-call overhead versus raw loops — fine for readability in most code, but avoid in extremely hot, tight numeric loops (e.g., inner loops of competitive-programming solutions under tight time limits).
- Minimize repeated calls to methods that allocate a defensive array copy internally (e.g., `enum.values()`) inside loops — cache the result once outside the loop instead.

---

## 14. Core Array Algorithms & Fully-Worked Interview Problems

Each problem below follows the same structure: **Problem Statement → Approach → Java Code → Line-by-Line Explanation → Dry Run → Complexity Analysis → Alternative Approach → Edge Cases → Common Mistakes → Interview Tips.**


### 14.1 Find the Maximum and Minimum Element

**Problem Statement:** Given an integer array, find the maximum and minimum values in a single pass.

**Approach:** Initialize both `max` and `min` to the first element, then scan once, updating each as a strictly-better candidate is found.

```java
static int[] findMinMax(int[] arr) {
    if (arr == null || arr.length == 0) {
        throw new IllegalArgumentException("Array must be non-empty");
    }
    int min = arr[0];
    int max = arr[0];
    for (int i = 1; i < arr.length; i++) {
        if (arr[i] < min) min = arr[i];
        if (arr[i] > max) max = arr[i];
    }
    return new int[]{min, max};
}
```

**Line-by-Line Explanation:**
- Guard clause rejects `null`/empty input up front — indexing `arr[0]` below would otherwise throw.
- `min` and `max` both seed from `arr[0]` so the loop can start at index `1` (avoids a wasted self-comparison at index 0).
- A single `for` loop with two independent `if` checks updates both trackers in one pass — no need for two separate loops.

**Dry Run:** `arr = {4, 2, 9, 1, 7}`
- `min=4, max=4`
- `i=1, arr[1]=2`: `2<4` → `min=2`
- `i=2, arr[2]=9`: `9>4` → `max=9`
- `i=3, arr[3]=1`: `1<2` → `min=1`
- `i=4, arr[4]=7`: no change
- Result: `min=1, max=9`

**Complexity:** Time O(n), Space O(1).

**Alternative Approach:** `Arrays.stream(arr).min().getAsInt()` and `.max().getAsInt()` — clean, but performs **two full passes** and boxes internally via `OptionalInt` handling; for a hot path, the manual single-pass loop above is faster.

**Edge Cases:** empty array (throws/guard), single-element array (`min == max`), all-equal elements, all-negative elements.

**Common Mistakes:** seeding `min`/`max` with `0` or `Integer.MAX_VALUE`/`MIN_VALUE` incorrectly swapped, which silently gives wrong answers for all-negative or all-positive arrays; forgetting the empty-array guard.

**Interview Tips:** Interviewers often follow up asking for the **index** of the min/max too — track `minIdx`/`maxIdx` alongside the values with the same single-pass technique.

---

### 14.2 Reverse an Array In-Place (Two-Pointer Technique)

**Problem Statement:** Reverse the order of elements in an array without allocating a second array.

**Approach:** Use two pointers, `left` starting at index 0 and `right` at the last index, swapping and moving inward until they meet.

```java
static void reverse(int[] arr) {
    int left = 0, right = arr.length - 1;
    while (left < right) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}
```

**Line-by-Line Explanation:**
- `left`/`right` start at opposite ends.
- Each iteration swaps the pair via a temp variable, then moves both pointers toward the center.
- Loop stops when pointers meet or cross (`left < right` false) — for odd-length arrays the middle element is untouched (correctly, since it doesn't need to move).

**Dry Run:** `arr = {1, 2, 3, 4, 5}`
- `left=0,right=4`: swap → `{5,2,3,4,1}`; `left=1,right=3`
- `left=1,right=3`: swap → `{5,4,3,2,1}`; `left=2,right=2`
- `left < right` false → stop
- Result: `{5,4,3,2,1}`

**Complexity:** Time O(n) (exactly n/2 swaps), Space O(1) — true in-place reversal.

**Alternative Approach:** Allocate a new array and copy `arr[n-1-i]` into `result[i]` — O(n) time, but O(n) **extra** space; useful only when the original array must remain unmodified.

**Edge Cases:** empty array (loop body never runs, safe), single element (loop never runs), even vs odd length (both handled correctly by `left < right`).

**Common Mistakes:** using `left <= right` instead of `left < right` (causes a redundant/no-op self-swap on the middle element for odd lengths — harmless but wasteful, and a sign of imprecise reasoning to interviewers); off-by-one on `right = arr.length` instead of `arr.length - 1`.

**Interview Tips:** This exact two-pointer swap pattern is the foundation for rotate-array (§14.3), palindrome-checking on arrays, and many in-place manipulation problems — memorize it cold.

---

### 14.3 Rotate an Array by K Positions

**Problem Statement:** Rotate an array to the right by `k` positions, in place. E.g., `{1,2,3,4,5,6,7}` rotated right by `3` becomes `{5,6,7,1,2,3,4}`.

**Approach (Reversal Algorithm):** A right rotation by `k` is equivalent to: reverse the whole array, then reverse the first `k` elements, then reverse the remaining `n-k` elements. This elegant trick achieves an in-place rotation in linear time with only O(1) extra space.

```java
static void rotate(int[] arr, int k) {
    int n = arr.length;
    if (n == 0) return;
    k = ((k % n) + n) % n;      // normalize k (handles k > n and negative k)
    reverseRange(arr, 0, n - 1);
    reverseRange(arr, 0, k - 1);
    reverseRange(arr, k, n - 1);
}

static void reverseRange(int[] arr, int left, int right) {
    while (left < right) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}
```

**Line-by-Line Explanation:**
- `k = ((k % n) + n) % n` normalizes any `k` (including negative or `k > n`) into the valid range `[0, n-1]`.
- Reversing the *entire* array first flips relative order globally.
- Re-reversing the first `k` elements and the last `n-k` elements individually restores the correct internal order **within** each segment while keeping the overall rotated arrangement.

**Dry Run:** `arr = {1,2,3,4,5,6,7}, k = 3`
- `n=7, k = 3`
- Reverse whole: `{7,6,5,4,3,2,1}`
- Reverse `[0,2]` (first 3): `{5,6,7,4,3,2,1}`
- Reverse `[3,6]` (last 4): `{5,6,7,1,2,3,4}`
- Result: `{5,6,7,1,2,3,4}` ✓ matches expected right-rotation by 3.

**Complexity:** Time O(n) (three linear passes, still O(n) total), Space O(1).

**Alternative Approach 1 — Extra Array:** Compute `result[(i + k) % n] = arr[i]` for each `i`, writing into a new array. Time O(n), Space O(n) — simpler to reason about but not in-place.

**Alternative Approach 2 — Juggling/Cyclic Replacement:** Move elements in cycles determined by `gcd(n, k)`, placing each element directly into its final position without any reversal. Also O(n) time, O(1) space, but noticeably trickier to implement correctly (cycle-length bookkeeping) — the reversal algorithm above is generally preferred in interviews for its clarity.

**Edge Cases:** `k == 0` (no-op, code handles via `k` normalization), `k == n` (equivalent to `k=0` after modulo), `k > n` (must normalize via modulo), negative `k` (interpreted as a left rotation, correctly normalized by the `((k % n) + n) % n` formula), single-element array (any rotation is a no-op).

**Common Mistakes:** forgetting to normalize `k` when `k >= n`, causing an `ArrayIndexOutOfBoundsException` in `reverseRange(arr, 0, k-1)`; using `%` alone without the extra `+ n) % n` for negative `k`, since Java's `%` can return negative results for negative operands (unlike Python's).

**Interview Tips:** This is one of the most frequently asked array problems. Always ask the interviewer to clarify **left vs right** rotation direction, and whether in-place O(1) space is required — that determines whether the extra-array approach is acceptable.

---

### 14.4 Move All Zeroes to the End

**Problem Statement:** Given an array, move all `0`s to the end while maintaining the relative order of the non-zero elements, in place.

**Approach (Two-Pointer / "Write Pointer"):** Maintain a `writePos` pointer marking where the next non-zero element should go. Scan the array; every time a non-zero is found, place it at `writePos` and advance. After the scan, fill everything from `writePos` to the end with zeroes.

```java
static void moveZeroes(int[] arr) {
    int writePos = 0;
    for (int readPos = 0; readPos < arr.length; readPos++) {
        if (arr[readPos] != 0) {
            arr[writePos] = arr[readPos];
            writePos++;
        }
    }
    for (int i = writePos; i < arr.length; i++) {
        arr[i] = 0;
    }
}
```

**Line-by-Line Explanation:**
- `writePos` trails `readPos`, only advancing when a non-zero value is written — this compacts all non-zero elements to the front, preserving their relative order.
- The second loop zero-fills the remaining tail slots — everything from `writePos` onward was either overwritten already or is now stale/duplicate data that must become `0`.

**Dry Run:** `arr = {0, 1, 0, 3, 12}`
- `readPos=0, arr[0]=0`: skip
- `readPos=1, arr[1]=1`: `arr[0]=1`, `writePos=1` → `{1,1,0,3,12}`
- `readPos=2, arr[2]=0`: skip
- `readPos=3, arr[3]=3`: `arr[1]=3`, `writePos=2` → `{1,3,0,3,12}`
- `readPos=4, arr[4]=12`: `arr[2]=12`, `writePos=3` → `{1,3,12,3,12}`
- Zero-fill from `writePos=3`: `{1,3,12,0,0}` ✓

**Complexity:** Time O(n), Space O(1).

**Alternative Approach:** Swap-based single pass — instead of a separate zero-fill loop, swap `arr[readPos]` and `arr[writePos]` whenever a non-zero is found (rather than just overwriting). This achieves the same result in one pass with the minimum number of swaps, and is preferred when swap cost matters (e.g., swapping large objects instead of ints) since it avoids redundant overwrites.

```java
static void moveZeroesSwap(int[] arr) {
    int writePos = 0;
    for (int readPos = 0; readPos < arr.length; readPos++) {
        if (arr[readPos] != 0) {
            int temp = arr[writePos];
            arr[writePos] = arr[readPos];
            arr[readPos] = temp;
            writePos++;
        }
    }
}
```

**Edge Cases:** all zeroes (`writePos` never advances, everything zero-filled — correctly a no-op result), no zeroes (array unchanged), empty array, single element.

**Common Mistakes:** forgetting to zero-fill the tail after the compaction loop when using the overwrite (non-swap) version; accidentally changing the *relative order* of non-zero elements by using an incorrect two-pointer strategy (e.g., swapping from both ends, which is the wrong pattern for this particular "preserve order" requirement — that pattern is correct for §14.5 instead, where order doesn't matter).

**Interview Tips:** This exact write-pointer/compaction pattern generalizes to "remove all instances of value X in place" and "partition array by a predicate" — recognize it as a reusable template, not a one-off trick.

---

### 14.5 Dutch National Flag — Sort an Array of 0s, 1s, and 2s

**Problem Statement:** Given an array containing only `0`s, `1`s, and `2`s, sort it in place in a single pass, without using a general-purpose sorting algorithm.

**Approach (Three-Pointer Partitioning):** Maintain three pointers: `low` (boundary for the next `0`), `mid` (current scan position), and `high` (boundary for the next `2`). Classify `arr[mid]` and swap accordingly, growing the three partitions (`0`s, `1`s, `2`s) as `mid` scans through.

```java
static void sortColors(int[] arr) {
    int low = 0, mid = 0, high = arr.length - 1;
    while (mid <= high) {
        if (arr[mid] == 0) {
            swap(arr, low, mid);
            low++;
            mid++;
        } else if (arr[mid] == 1) {
            mid++;
        } else { // arr[mid] == 2
            swap(arr, mid, high);
            high--;
            // NOTE: mid is NOT incremented here — the swapped-in value must still be classified
        }
    }
}

static void swap(int[] arr, int i, int j) {
    int t = arr[i]; arr[i] = arr[j]; arr[j] = t;
}
```

**Line-by-Line Explanation:**
- Invariant maintained throughout: `arr[0..low-1]` are all `0`, `arr[low..mid-1]` are all `1`, `arr[high+1..n-1]` are all `2`, and `arr[mid..high]` is unexamined.
- On seeing `0`: swap it to the `low` boundary (guaranteed to hold a `1` or itself), then advance both `low` and `mid` — safe to advance `mid` here because the element swapped *into* `arr[mid]` (from the `low` region) is already known to be a `1` (or this is a self-swap when `low == mid`).
- On seeing `1`: it's already in the correct middle region — just advance `mid`.
- On seeing `2`: swap it to the `high` boundary, shrink `high`, but **do not advance `mid`**, since the newly swapped-in element at `arr[mid]` hasn't been classified yet and could be a `0`, `1`, or `2`.

**Dry Run:** `arr = {2, 0, 2, 1, 1, 0}`
- `low=0,mid=0,high=5`: `arr[0]=2` → swap(0,5) → `{0,0,2,1,1,2}`, `high=4`
- `arr[0]=0` → swap(0,0) → `low=1,mid=1`
- `arr[1]=0` → swap(1,1) → `low=2,mid=2`
- `arr[2]=2` → swap(2,4) → `{0,0,1,1,2,2}`, `high=3`
- `arr[2]=1` → `mid=3`
- `arr[3]=1` → `mid=4`
- `mid(4) <= high(3)`? No → stop
- Result: `{0,0,1,1,2,2}` ✓

**Complexity:** Time O(n) — single pass, each element visited/swapped a bounded number of times. Space O(1).

**Alternative Approach:** Counting pass — count occurrences of `0`, `1`, `2` in one pass, then overwrite the array in a second pass with the correct counts of each. Also O(n) time, O(1) extra space, and arguably simpler to reason about, but requires two passes and doesn't generalize as a partitioning template the way the three-pointer approach does.

**Edge Cases:** already sorted, reverse sorted, all same value, empty array, single element.

**Common Mistakes:** incrementing `mid` after a `2`-swap (breaks correctness — the newly swapped element is unexamined); using `mid < high` as the loop condition instead of `mid <= high` (misses classifying the last element).

**Interview Tips:** This is the classic "Dutch National Flag" partitioning problem (three-way partitioning), and the same `low/mid/high` pattern is the core building block of three-way quicksort partitioning (sorting algorithm itself out of scope here).

---

### 14.6 Maximum Subarray Sum (Kadane's Technique)

**Problem Statement:** Given an integer array (possibly containing negatives), find the contiguous subarray with the largest sum, and return that sum.

**Approach:** Track two running values while scanning once: `currentSum` (best sum of a subarray *ending exactly at* the current index) and `maxSum` (best seen so far, globally). At each element, decide whether extending the previous subarray is better than starting fresh at the current element.

```java
static int maxSubArraySum(int[] arr) {
    if (arr == null || arr.length == 0) {
        throw new IllegalArgumentException("Array must be non-empty");
    }
    int currentSum = arr[0];
    int maxSum = arr[0];
    for (int i = 1; i < arr.length; i++) {
        currentSum = Math.max(arr[i], currentSum + arr[i]);
        maxSum = Math.max(maxSum, currentSum);
    }
    return maxSum;
}
```

**Line-by-Line Explanation:**
- `currentSum = Math.max(arr[i], currentSum + arr[i])` is the central decision: if the running sum so far is negative (a net drag), it's better to abandon it and start a new subarray at `arr[i]` alone; otherwise, extend.
- `maxSum` independently tracks the best `currentSum` ever observed, since the best subarray doesn't necessarily end at the last index.

**Dry Run:** `arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4}`
- `currentSum=-2, maxSum=-2`
- `i=1`: `max(1, -2+1=-1)=1` → `currentSum=1`, `maxSum=1`
- `i=2`: `max(-3, 1-3=-2)=-2` → `currentSum=-2`, `maxSum=1`
- `i=3`: `max(4, -2+4=2)=4` → `currentSum=4`, `maxSum=4`
- `i=4`: `max(-1, 4-1=3)=3` → `currentSum=3`, `maxSum=4`
- `i=5`: `max(2, 3+2=5)=5` → `currentSum=5`, `maxSum=5`
- `i=6`: `max(1, 5+1=6)=6` → `currentSum=6`, `maxSum=6`
- `i=7`: `max(-5, 6-5=1)=1` → `currentSum=1`, `maxSum=6`
- `i=8`: `max(4, 1+4=5)=5` → `currentSum=5`, `maxSum=6`
- Result: `6` (subarray `[4,-1,2,1]`) ✓

**Complexity:** Time O(n), Space O(1).

**Alternative Approach:** Brute force — check every pair of `(start, end)` indices and sum each subarray directly: O(n²) or O(n³) depending on whether prefix sums are precomputed. Useful only as a baseline/correctness check; Kadane's linear scan dominates in every practical setting.

**Edge Cases:** all-negative array (answer is the single largest — i.e., least negative — element, correctly handled since `currentSum` is allowed to reset to a single negative element rather than being clamped at 0); single-element array; all-equal elements.

**Common Mistakes:** initializing `maxSum`/`currentSum` to `0` instead of `arr[0]` — this silently produces a wrong (too-high, e.g. `0`) answer for all-negative arrays, since it implicitly allows an "empty subarray" of sum `0` to win, which most problem definitions disallow.

**Interview Tips:** Interviewers frequently ask a follow-up: "also return the actual subarray, not just the sum" — extend the algorithm by tracking `start`/`end` index candidates alongside the sums, updating them whenever `maxSum` improves. Note: while this technique is commonly taught alongside Dynamic Programming as "the simplest 1D DP," it is presented here purely as a linear-scan array technique, since it requires no auxiliary DP table.

---

### 14.7 Best Time to Buy and Sell Stock (Single Transaction)

**Problem Statement:** Given an array `prices` where `prices[i]` is the stock price on day `i`, find the maximum profit achievable from a single buy followed by a single sell (buy must occur before sell). Return `0` if no profit is possible.

**Approach:** Track the minimum price seen so far while scanning left to right; at each day, compute the profit if selling *today* against the minimum-so-far, and keep the best such profit.

```java
static int maxProfit(int[] prices) {
    if (prices == null || prices.length == 0) return 0;
    int minPriceSoFar = prices[0];
    int maxProfit = 0;
    for (int i = 1; i < prices.length; i++) {
        int profitIfSellToday = prices[i] - minPriceSoFar;
        maxProfit = Math.max(maxProfit, profitIfSellToday);
        minPriceSoFar = Math.min(minPriceSoFar, prices[i]);
    }
    return maxProfit;
}
```

**Line-by-Line Explanation:**
- `minPriceSoFar` always reflects the cheapest **buy** opportunity available strictly before or at the current day.
- `profitIfSellToday` simulates selling at today's price after having bought at the best price so far.
- `minPriceSoFar` is updated *after* computing today's profit, ensuring you never "buy and sell on the same conceptual step" using a future price incorrectly.

**Dry Run:** `prices = {7, 1, 5, 3, 6, 4}`
- `minPriceSoFar=7, maxProfit=0`
- `i=1`: profit=`1-7=-6`→`maxProfit=0`; `minPriceSoFar=1`
- `i=2`: profit=`5-1=4`→`maxProfit=4`; `minPriceSoFar=1`
- `i=3`: profit=`3-1=2`→`maxProfit=4`; `minPriceSoFar=1`
- `i=4`: profit=`6-1=5`→`maxProfit=5`; `minPriceSoFar=1`
- `i=5`: profit=`4-1=3`→`maxProfit=5`
- Result: `5` (buy at 1, sell at 6) ✓

**Complexity:** Time O(n), Space O(1).

**Alternative Approach:** Brute force checks every `(buyDay, sellDay)` pair with `buyDay < sellDay`: O(n²) time, O(1) space — correct but far slower; useful only as a correctness baseline.

**Edge Cases:** strictly decreasing prices (answer `0`, no profitable transaction exists), single-day array (no transaction possible, answer `0`), all equal prices (`0`), empty array (guard returns `0`).

**Common Mistakes:** updating `minPriceSoFar` *before* computing `profitIfSellToday` on the same iteration (which would incorrectly allow buying and selling on the same day using that day's own price as both bought-at and sold-at); initializing `maxProfit` to a negative sentinel instead of `0` when the problem defines "no transaction" as an acceptable (zero-profit) outcome.

**Interview Tips:** This is a specific case of the general "maximum difference `arr[j] - arr[i]` for `j > i`" pattern — recognizing that generalization helps you quickly solve related variants (e.g., "best time to buy/sell with at most two transactions," which layers additional state on top of this same core single-pass idea — full multi-transaction variants typically move into dynamic-programming territory, out of scope here).

---

### 14.8 Product of Array Except Self

**Problem Statement:** Given an array `nums`, return an array `output` where `output[i]` equals the product of all elements of `nums` except `nums[i]`, without using division, in O(n) time.

**Approach (Prefix and Suffix Products):** For each index `i`, the answer is `(product of everything to the left of i) * (product of everything to the right of i)`. Compute left-running-products into the output array in a first pass, then multiply in right-running-products in a second (reverse) pass, using a single rolling variable instead of a separate suffix array.

```java
static int[] productExceptSelf(int[] nums) {
    int n = nums.length;
    int[] output = new int[n];

    output[0] = 1;
    for (int i = 1; i < n; i++) {
        output[i] = output[i - 1] * nums[i - 1];   // left-side running product
    }

    int rightProduct = 1;
    for (int i = n - 1; i >= 0; i--) {
        output[i] *= rightProduct;                  // fold in right-side running product
        rightProduct *= nums[i];
    }

    return output;
}
```

**Line-by-Line Explanation:**
- First loop: `output[i]` ends up holding the product of all elements **strictly left** of `i` (`output[0] = 1` since there's nothing to the left of index 0).
- Second loop (right to left): `rightProduct` accumulates the product of all elements **strictly right** of the current `i`, multiplying it into the already-stored left product at each step, and only *then* folding `nums[i]` itself into `rightProduct` for the next (further-left) iteration.
- The output array itself is reused as the "left product" storage, so only O(1) *extra* space (`rightProduct`) is needed beyond the required output array.

**Dry Run:** `nums = {1, 2, 3, 4}`
- Left pass: `output[0]=1`; `output[1]=1*1=1`; `output[2]=1*2=2`; `output[3]=2*3=6` → `output = {1,1,2,6}`
- Right pass: `rightProduct=1`
  - `i=3`: `output[3] *= 1` → `6`; `rightProduct = 1*4 = 4`
  - `i=2`: `output[2] *= 4` → `8`; `rightProduct = 4*3 = 12`
  - `i=1`: `output[1] *= 12` → `12`; `rightProduct = 12*2 = 24`
  - `i=0`: `output[0] *= 24` → `24`; `rightProduct = 24*1 = 24`
- Result: `{24, 12, 8, 6}` ✓ (check: `2*3*4=24`, `1*3*4=12`, `1*2*4=8`, `1*2*3=6`)

**Complexity:** Time O(n) (two linear passes), Space O(1) extra (excluding the required output array — the problem explicitly asks for this, since it's the mandated return value, not auxiliary working space).

**Alternative Approach:** Compute the total product of all elements once, then divide by `nums[i]` for each output slot — O(n) time, O(1) space, but **fails whenever any element is `0`** (division by zero) and generally division-based numeric tricks are considered a weaker solution in interviews since the problem usually explicitly forbids division.

**Edge Cases:** array containing exactly one `0` (only that index's output is nonzero — the two-pass algorithm handles this correctly automatically, since multiplying by `0` naturally zeroes out every other position); array containing two or more `0`s (every output is `0`); single-element array (typically ill-defined / returns `{1}` by convention, since "everything except itself" is an empty product).

**Common Mistakes:** attempting the division-based shortcut without handling zero elements; allocating an explicit separate suffix-product array (works, but uses O(n) *extra* space beyond the required output, whereas the rolling `rightProduct` variable achieves true O(1) extra space).

**Interview Tips:** This problem is a strong test of whether a candidate can decompose "value depends on both left and right context" into two independent, composable single-direction passes — a pattern that recurs in trapping-rain-water (§14.10) and various other array problems.

---

### 14.9 Two Sum (Sorted Array — Two-Pointer Approach)

**Problem Statement:** Given an array sorted in ascending order and a target value, find the indices of two elements that sum to the target (assume exactly one solution, and you may not use the same element twice).

**Approach:** Because the array is sorted, use two pointers starting at both ends. If the current pair's sum is too small, move `left` right (to increase the sum); if too large, move `right` left (to decrease it); this narrows the search space by one element per step instead of checking every pair.

```java
static int[] twoSumSorted(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) {
            return new int[]{left, right};
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return new int[]{-1, -1}; // no solution found
}
```

**Line-by-Line Explanation:**
- `sum == target` is an immediate win — return both indices.
- `sum < target` means the pair's total is too small; since the array is sorted, moving `right` leftward can only decrease the sum further (wrong direction) — only increasing `left` can raise the sum toward the target.
- `sum > target` mirrors this: only decreasing `right` can lower the sum toward the target.

**Dry Run:** `arr = {2, 7, 11, 15}, target = 9`
- `left=0(2), right=3(15)`: sum=17 > 9 → `right--`
- `left=0(2), right=2(11)`: sum=13 > 9 → `right--`
- `left=0(2), right=1(7)`: sum=9 == 9 → return `{0, 1}` ✓

**Complexity:** Time O(n) — each step moves one pointer, and the pointers can move at most `n` total steps combined. Space O(1).

**Alternative Approach (Unsorted Array — Hashing):** If the array is *not* sorted (or sorting it first isn't acceptable because original indices/order must be preserved without the O(n log n) sort cost), use a hash map from value → index, checking for `target - arr[i]` as you scan once: O(n) time, O(n) space. This is the standard approach for the more commonly asked *unsorted* Two Sum variant. (Hash map usage is mentioned here only as a comparison baseline — hash-table internals are out of scope for this array-focused handbook.)

**Edge Cases:** no valid pair exists (returns `{-1,-1}` sentinel, or the problem may guarantee a solution always exists), duplicate values in the array (still works correctly as long as `left != right`, i.e., you never use the same index twice), array of length `< 2` (loop never executes meaningfully — should be guarded/documented).

**Common Mistakes:** applying the two-pointer approach to an **unsorted** array (silently gives wrong answers — the greedy pointer-movement logic depends entirely on sortedness); off-by-one with `left < right` vs `left <= right` (using `<=` would allow `left == right`, incorrectly reusing one element as both halves of the pair).

**Interview Tips:** Always confirm with the interviewer whether the array is sorted — that single fact determines whether the O(n) two-pointer approach or the O(n) hashing approach (for unsorted input) is the right tool; both are linear time but for different reasons and different tradeoffs (extra space vs. requiring sorted input).

---

### 14.10 Trapping Rain Water

**Problem Statement:** Given an array of non-negative integers representing an elevation map where each bar has width `1`, compute how much rainwater can be trapped between the bars after raining.

**Approach (Two-Pointer, O(1) Extra Space):** The water trapped above index `i` equals `min(maxLeft, maxRight) - height[i]`, where `maxLeft`/`maxRight` are the tallest bars to the left/right of `i` (inclusive of `i`). Rather than precomputing full `leftMax[]`/`rightMax[]` arrays, use two pointers converging from both ends, always processing the side with the smaller running max first — that side's water level is fully determined regardless of what's further away on the *other* side.

```java
static int trap(int[] height) {
    if (height == null || height.length == 0) return 0;
    int left = 0, right = height.length - 1;
    int leftMax = 0, rightMax = 0;
    int water = 0;

    while (left < right) {
        if (height[left] < height[right]) {
            leftMax = Math.max(leftMax, height[left]);
            water += leftMax - height[left];
            left++;
        } else {
            rightMax = Math.max(rightMax, height[right]);
            water += rightMax - height[right];
            right--;
        }
    }
    return water;
}
```

**Line-by-Line Explanation:**
- `leftMax`/`rightMax` track the tallest bar seen so far from each respective side.
- Whenever `height[left] < height[right]`, we know for certain that the water level above `left` is bounded by `leftMax` (not by anything on the right side — because there's already a bar at least `height[right]` tall somewhere to the right, and `height[right] > height[left]`, so the right boundary is never the limiting factor for `left`'s column). This lets us safely finalize and accumulate `left`'s trapped water immediately, then advance `left`.
- The symmetric logic applies when processing from the right.

**Dry Run:** `height = {0,1,0,2,1,0,1,3,2,1,2,1}`
- Key intermediate checkpoint: as pointers converge, water accumulates at indices `2` (`1`), `4` (`1`), `5` (`2`), `6` (`1`), `9` (`1`) — total trapped water sums to `6`.
- Result: `6` ✓ (this is the classic, widely-known example for this problem)

**Complexity:** Time O(n) — single pass, each pointer moves at most `n` steps combined. Space O(1).

**Alternative Approach:** Precompute `leftMax[i]` (max height from `0..i`) and `rightMax[i]` (max height from `i..n-1`) as two full auxiliary arrays in two separate passes, then compute `water += min(leftMax[i], rightMax[i]) - height[i]` in a third pass. Time O(n), but Space O(n) due to the two auxiliary arrays — conceptually simpler to derive from first principles, and a reasonable stepping stone toward the more space-efficient two-pointer version above.

**Edge Cases:** monotonically increasing or decreasing heights (no water trapped, answer `0`), empty array or single bar (`0`, guarded), all-equal heights (`0`, since there are no "walls" taller than any given bar).

**Common Mistakes:** comparing `leftMax`/`rightMax` against each other instead of against `height[left]`/`height[right]` directly when deciding which pointer to advance (subtly wrong logic that can under/over-count in certain configurations); forgetting that this problem implicitly assumes bar width `1` and non-negative heights.

**Interview Tips:** This is considered a "hard" array problem specifically because the O(1)-space two-pointer insight (which side is safe to finalize) is non-obvious; it's very reasonable to first present the O(n)-space prefix/suffix-max approach (§14.10 alternative) to establish correctness, then optimize to two pointers as a follow-up — this progression itself is often what interviewers are evaluating.

---

### 14.11 Maximum Sum Subarray of Fixed Size K (Sliding Window)

**Problem Statement:** Given an array and an integer `k`, find the maximum sum among all contiguous subarrays of exactly size `k`.

**Approach (Fixed-Size Sliding Window):** Compute the sum of the first `k` elements as the initial window. Then slide the window one position at a time: each slide adds the newly-entering element and subtracts the element that just left the window — an O(1) update per step, instead of recomputing the whole window sum from scratch (which would be O(k) per step, O(nk) overall).

```java
static int maxSumSubarrayOfSizeK(int[] arr, int k) {
    if (arr.length < k) throw new IllegalArgumentException("k exceeds array length");

    int windowSum = 0;
    for (int i = 0; i < k; i++) {
        windowSum += arr[i];
    }
    int maxSum = windowSum;

    for (int i = k; i < arr.length; i++) {
        windowSum += arr[i] - arr[i - k];   // slide: add new element, remove leftmost of old window
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}
```

**Line-by-Line Explanation:**
- First loop establishes the sum of the initial window `arr[0..k-1]`.
- Second loop, for each new index `i` (which is the new right edge of the window), the window has logically shifted to `arr[i-k+1..i]`; the O(1) update adds `arr[i]` (entering) and subtracts `arr[i-k]` (the element that just exited on the left).

**Dry Run:** `arr = {2, 1, 5, 1, 3, 2}, k = 3`
- Initial window `[0..2]`: `2+1+5=8` → `maxSum=8`
- `i=3`: `windowSum = 8 + arr[3] - arr[0] = 8+1-2=7` → `maxSum` stays `8`
- `i=4`: `windowSum = 7 + arr[4] - arr[1] = 7+3-1=9` → `maxSum=9`
- `i=5`: `windowSum = 9 + arr[5] - arr[2] = 9+2-5=6` → `maxSum` stays `9`
- Result: `9` (subarray `[5,1,3]`) ✓

**Complexity:** Time O(n), Space O(1).

**Alternative Approach:** Brute force — for each of the `n - k + 1` starting positions, sum `k` elements directly: O(n*k) time, O(1) space. Correct, but the sliding window reduces this to O(n) by reusing the previous window's sum instead of recomputing it.

**Edge Cases:** `k == arr.length` (only one window, its sum is trivially the answer), `k == 1` (degenerates to "find the maximum single element"), `k > arr.length` (invalid — should be guarded/rejected).

**Common Mistakes:** recomputing the full window sum on every slide instead of using the O(1) incremental update (defeats the entire purpose of the sliding-window optimization); off-by-one errors in the subtracted index (`arr[i-k]` vs `arr[i-k+1]` — always double-check against a small dry run).

**Interview Tips:** This is the canonical **fixed-size** sliding window template. The **variable-size** sliding window variant (e.g., "smallest subarray with sum ≥ target") uses a similar `windowSum` idea but with an inner `while` loop that shrinks the window from the left whenever a condition is satisfied — recognizing which variant a problem calls for is the key skill being tested.

---

### 14.12 Merge Two Sorted Arrays In-Place (Merge Sorted Array)

**Problem Statement:** `nums1` has length `m + n`, where the first `m` elements are valid sorted data and the last `n` slots are empty placeholders (commonly `0`s). `nums2` has `n` sorted elements. Merge `nums2` into `nums1` in place so that `nums1` becomes one fully sorted array of length `m + n`.

**Approach (Merge From the Back):** Merging from the *front* would require shifting `nums1`'s existing elements repeatedly to make room — expensive. Instead, merge starting from the **back** of both arrays into the back of `nums1`, since `nums1` already has empty capacity there — no shifting is ever needed.

```java
static void merge(int[] nums1, int m, int[] nums2, int n) {
    int i = m - 1;          // last valid element in nums1
    int j = n - 1;          // last element in nums2
    int writePos = m + n - 1; // last slot in nums1 (fill from the back)

    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[writePos] = nums1[i];
            i--;
        } else {
            nums1[writePos] = nums2[j];
            j--;
        }
        writePos--;
    }
    // If nums2 is exhausted first, nums1's remaining prefix is already correctly in place.
    // If nums1's real elements are exhausted first (i < 0), the loop above still
    // correctly copies any remaining nums2 elements, since the 'else' branch handles it.
}
```

**Line-by-Line Explanation:**
- `i` and `j` walk backward through the *valid* portions of `nums1` and `nums2` respectively.
- `writePos` walks backward through the full combined length of `nums1`, always placing the larger of the two current candidates at the current back position.
- The loop condition is `j >= 0` only (not `i >= 0`) — once `nums2` is fully merged, any remaining `nums1` elements are already in their correct final positions (they started at the front and nothing needed to move past them), so nothing further needs to be written.

**Dry Run:** `nums1 = {1,2,3,0,0,0}, m=3, nums2 = {2,5,6}, n=3`
- `i=2(3), j=2(6), writePos=5`: `6>3`? nums1[i]=3, nums2[j]=6 → `3>6`? No → write `6` at pos5, `j=1`, `writePos=4` → `{1,2,3,0,0,6}`
- `i=2(3), j=1(5)`: `3>5`? No → write `5` at pos4, `j=0`, `writePos=3` → `{1,2,3,0,5,6}`
- `i=2(3), j=0(2)`: `3>2`? Yes → write `3` at pos3, `i=1`, `writePos=2` → `{1,2,3,3,5,6}`
- `i=1(2), j=0(2)`: `2>2`? No → write `2` at pos2, `j=-1`, `writePos=1` → `{1,2,2,3,5,6}`
- `j<0` → stop
- Result: `{1,2,2,3,5,6}` ✓

**Complexity:** Time O(m + n), Space O(1) — genuinely in-place, unlike a naive "merge into a new array" approach.

**Alternative Approach:** Copy `nums2` into the tail of `nums1`, then call `Arrays.sort` on the combined array — O((m+n) log(m+n)) time (sort algorithm itself out of scope), simpler code but asymptotically worse than the linear-time merge-from-back approach, and it wastes the fact that both inputs are already individually sorted.

**Edge Cases:** `nums2` is empty (`n=0`, loop never runs, `nums1` already correct), `nums1`'s valid portion is empty (`m=0`, every element comes from `nums2`), all elements in `nums2` smaller/larger than all in `nums1`.

**Common Mistakes:** merging from the front (forces expensive shifting to avoid overwriting not-yet-read `nums1` elements); forgetting the loop only needs to check `j >= 0` (checking `i >= 0` as an additional loop condition is a subtle bug — it can terminate the loop too early, leaving trailing `nums2` elements uncopied).

**Interview Tips:** "Merge from the back" is a reusable trick anytime you're merging into a buffer that has trailing empty capacity — recognize the pattern rather than re-deriving it from scratch every time.

---

### 14.13 Find the Missing Number (0 to N Range)

**Problem Statement:** Given an array containing `n` distinct numbers taken from the range `[0, n]` (so exactly one number in that range is missing), find the missing number.

**Approach (XOR Trick):** XOR-ing a number with itself yields `0`, and XOR is commutative/associative, so if you XOR together **all indices/values from `0` to `n`** and **all elements of the array**, every present number cancels out with its duplicate, leaving only the missing number.

```java
static int findMissingNumber(int[] arr) {
    int n = arr.length; // array has n elements, drawn from range [0, n]
    int result = n;      // start by including the "extra" upper bound value
    for (int i = 0; i < n; i++) {
        result ^= i ^ arr[i];
    }
    return result;
}
```

**Line-by-Line Explanation:**
- `result` is seeded with `n` because the full expected range `[0, n]` has `n+1` values, but indices `i` only run `0..n-1` — seeding with `n` accounts for the one range value (`n` itself) with no corresponding index.
- Each loop iteration XORs in both `i` (a value we expect to see, from the index side) and `arr[i]` (a value we actually have).
- Every value that appears in **both** the expected range and the actual array cancels itself out via XOR (`x ^ x = 0`); the one value present in the expected range but absent from `arr` remains un-canceled in `result`.

**Dry Run:** `arr = {3, 0, 1}` (n=3, expected range `[0,3]`, missing = 2)
- `result = 3`
- `i=0`: `result ^= 0 ^ arr[0](3)` → `result = 3 ^ 0 ^ 3 = 0`
- `i=1`: `result ^= 1 ^ arr[1](0)` → `result = 0 ^ 1 ^ 0 = 1`
- `i=2`: `result ^= 2 ^ arr[2](1)` → `result = 1 ^ 2 ^ 1 = 2`
- Result: `2` ✓

**Complexity:** Time O(n), Space O(1).

**Alternative Approach (Sum Formula):** Compute `expectedSum = n*(n+1)/2` (sum of `0..n`) and `actualSum = sum(arr)`; the answer is `expectedSum - actualSum`. Also O(n) time, O(1) space, and arguably more intuitive — but it can risk integer overflow for very large `n` (where the XOR approach cannot overflow, since XOR never exceeds the bit-width of the operands), making XOR the more robust choice for very large inputs.

**Edge Cases:** missing number is `0` (both approaches handle this correctly — XOR naturally leaves `0` un-canceled just like any other value); missing number is `n` itself (the largest); array of length `0` (only possible value is `[0]` missing from range `[0,0]`, i.e., answer trivially `0`).

**Common Mistakes:** using the sum-formula approach with `int` on very large `n` where `n*(n+1)/2` overflows `int` range (should use `long` arithmetic, or prefer the overflow-immune XOR approach); off-by-one in the expected range bound (`[0,n]` has `n+1` values, easy to miscount).

**Interview Tips:** This XOR pattern generalizes to a well-known family of "find the unique/missing/duplicate number using bit manipulation" problems (e.g., "every element appears twice except one — find it" is solved by simply XOR-ing the whole array together, no range/seed needed at all) — recognizing when a problem's structure allows an O(1)-space, O(n)-time XOR solution (versus needing a hash set, which uses O(n) space) is a strong signal of algorithmic maturity to interviewers.

---

### 14.14 Spiral Matrix Traversal

**Problem Statement:** Given a 2D array (matrix), return all its elements in spiral order (clockwise, starting from the top-left).

**Approach (Shrinking Boundaries):** Maintain four boundary variables — `top`, `bottom`, `left`, `right` — representing the current unvisited rectangular region. Traverse the top row left-to-right, the right column top-to-bottom, the bottom row right-to-left, and the left column bottom-to-top, shrinking each boundary inward after completing that side, and stop once the boundaries cross.

```java
static List<Integer> spiralOrder(int[][] matrix) {
    List<Integer> result = new ArrayList<>();
    if (matrix == null || matrix.length == 0) return result;

    int top = 0, bottom = matrix.length - 1;
    int left = 0, right = matrix[0].length - 1;

    while (top <= bottom && left <= right) {
        for (int col = left; col <= right; col++) {
            result.add(matrix[top][col]);
        }
        top++;

        for (int row = top; row <= bottom; row++) {
            result.add(matrix[row][right]);
        }
        right--;

        if (top <= bottom) {
            for (int col = right; col >= left; col--) {
                result.add(matrix[bottom][col]);
            }
            bottom--;
        }

        if (left <= right) {
            for (int row = bottom; row >= top; row--) {
                result.add(matrix[row][left]);
            }
            left++;
        }
    }
    return result;
}
```

**Line-by-Line Explanation:**
- The outer `while` loop continues as long as there's a valid rectangular region left to traverse.
- Each of the four inner loops walks one edge of the current rectangle, immediately followed by shrinking the corresponding boundary inward (`top++`, `right--`, `bottom--`, `left++`).
- The `if (top <= bottom)` and `if (left <= right)` guards before the bottom-row and left-column passes prevent **double-counting** a row or column that was already fully consumed by the top-row/right-column passes in the same iteration — this happens for single-row or single-column remaining regions.

**Dry Run:** `matrix = {{1,2,3},{4,5,6},{7,8,9}}`
- `top=0,bottom=2,left=0,right=2`
- Top row `[0][0..2]`: add `1,2,3`; `top=1`
- Right col `[1..2][2]`: add `6,9`; `right=1`
- `top(1)<=bottom(2)` true → bottom row `[2][1..0]`: add `8,7`; `bottom=1`
- `left(0)<=right(1)` true → left col `[1..1][0]`: add `4`; `left=1`
- `top(1)<=bottom(1) && left(1)<=right(1)` true → continue
- Top row `[1][1..1]`: add `5`; `top=2`
- Right col: `row=2..1` (invalid range, loop doesn't execute since `2>1`... wait bottom=1 now)
- Actually with `top=2 > bottom=1`, outer while condition now false at next check, but this inner pass already ran once — result correctly ends at `5`.
- Result: `[1,2,3,6,9,8,7,4,5]` ✓

**Complexity:** Time O(rows × cols) — every element visited exactly once. Space O(1) extra (excluding the output list, which is mandated by the problem).

**Alternative Approach:** Simulate a "walking direction" with a direction vector that turns clockwise whenever the next cell would be out of bounds or already visited (tracked via a separate `visited` boolean matrix). Also O(rows×cols) time, but uses O(rows×cols) extra space for the visited matrix — the boundary-shrinking approach above is more space-efficient and is generally preferred.

**Edge Cases:** single row (`top==bottom` throughout — the guarded bottom/left passes correctly skip re-traversal), single column, single element (`1x1` matrix), non-square (rectangular) matrices, empty matrix.

**Common Mistakes:** omitting the `if (top <= bottom)` / `if (left <= right)` guards, which causes elements to be added **twice** for matrices with a single remaining row or column at the end of the spiral; mixing up row/column bounds when the matrix isn't square.

**Interview Tips:** Spiral traversal is fundamentally a **simulation** problem, not a clever mathematical trick — interviewers are mainly testing careful boundary/index bookkeeping. Always trace through a small non-square example (e.g., 3 rows × 4 columns) by hand before coding, since square-only mental models often hide the guard-condition bugs above.

---

### 14.15 Rotate a Square Matrix 90° In-Place

**Problem Statement:** Given an `n x n` 2D matrix, rotate it 90 degrees clockwise, in place (without allocating another `n x n` matrix).

**Approach (Transpose, Then Reverse Each Row):** A 90° clockwise rotation can be decomposed into two simpler, well-understood steps: (1) transpose the matrix (swap `matrix[i][j]` with `matrix[j][i]` across the main diagonal), then (2) reverse each row. Both steps are individually easy to prove correct and are done fully in place.

```java
static void rotate(int[][] matrix) {
    int n = matrix.length;

    // Step 1: Transpose (swap across the main diagonal)
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    // Step 2: Reverse each row
    for (int i = 0; i < n; i++) {
        int left = 0, right = n - 1;
        while (left < right) {
            int temp = matrix[i][left];
            matrix[i][left] = matrix[i][right];
            matrix[i][right] = temp;
            left++;
            right--;
        }
    }
}
```

**Line-by-Line Explanation:**
- The transpose loop's inner bound starts at `j = i + 1` (not `j = 0`) specifically to avoid swapping each pair twice (which would cancel out to a no-op) and to avoid needlessly "swapping" diagonal elements with themselves.
- After transposing, row `i`'s content is exactly what the *final* column `i` should contain, but in the wrong (top-to-bottom instead of bottom-to-top) order — reversing each row fixes this ordering, completing the 90° clockwise rotation.

**Dry Run:** `matrix = {{1,2,3},{4,5,6},{7,8,9}}`
- Transpose: swap `(0,1)`↔`(1,0)`: `2↔4`; swap `(0,2)`↔`(2,0)`: `3↔7`; swap `(1,2)`↔`(2,1)`: `6↔8`
  → `{{1,4,7},{2,5,8},{3,6,9}}`
- Reverse each row: `{7,4,1}`, `{8,5,2}`, `{9,6,3}`
  → `{{7,4,1},{8,5,2},{9,6,3}}` ✓ (matches the expected 90° clockwise rotation)

**Complexity:** Time O(n²) (every cell touched a constant number of times), Space O(1) — genuinely in-place.

**Alternative Approach:** Allocate a new `n x n` matrix and directly compute `rotated[j][n-1-i] = original[i][j]` for every cell in one pass: O(n²) time, but O(n²) **extra** space — simpler to derive the index formula from a diagram, but not in-place, which many interviewers explicitly require for this problem.

**Edge Cases:** `1x1` matrix (no-op, both loops trivially do nothing meaningful), even vs odd `n` (both handled identically by the transpose+reverse approach, unlike some layer-by-layer rotation approaches that need separate handling), already-rotated/symmetric matrices (still correctly processed, since the algorithm doesn't special-case content, only positions).

**Common Mistakes:** starting the transpose inner loop at `j = 0` instead of `j = i + 1` (double-swaps everything back to the original, silently producing a no-op transposition); attempting to rotate a **non-square** (`rows != cols`) matrix in place with this technique — true in-place rotation is fundamentally only well-defined for square matrices, since rotating a rectangular matrix changes its dimensions.

**Interview Tips:** Presenting the decomposition ("this is just transpose + row-reverse, two operations I already know how to do in place") is a strong signal — it shows the ability to break an unfamiliar-looking problem into previously mastered primitives (transposition and the two-pointer reversal from §14.2), rather than deriving a monolithic index formula from scratch.

---

## 15. Array Patterns Cheat Sheet

Recognizing which **pattern** a problem fits is often more valuable than memorizing individual solutions. These are the recurring templates used throughout §14:

| Pattern | Signal Phrases | Core Idea | Example (§) |
|---|---|---|---|
| **Two Pointers (opposite ends)** | "sorted array", "palindrome", "pair that sums to X" | Start at both ends, move inward based on a comparison | §14.2, §14.9, §14.10 |
| **Two Pointers (same direction / fast-slow or read-write)** | "remove/move elements in place", "compact array" | One pointer scans, another marks the write boundary | §14.4 |
| **Three-Way Partitioning** | "sort with only 3 distinct values", "partition around a pivot" | `low/mid/high` boundaries dividing the array into 3 zones | §14.5 |
| **Sliding Window (fixed size)** | "subarray of size k" | Maintain a running aggregate; add entering / remove leaving element in O(1) | §14.11 |
| **Sliding Window (variable size)** | "smallest/longest subarray with property X" | Expand right pointer; shrink left pointer while condition holds | (extension of §14.11) |
| **Prefix / Suffix Aggregation** | "range sum query", "product except self", "value depends on both sides" | Precompute running aggregate(s) in one or two linear passes | §14.8, §14.10 (alt) |
| **Kadane's Running-Best** | "maximum/minimum contiguous subarray" | Track best-ending-here vs best-overall while scanning | §14.6 |
| **Greedy Single Pass with Running Extremum** | "buy low sell high", "max difference" | Track running min/max; compute candidate answer at each step | §14.1, §14.7 |
| **Merge From the Back** | "merge into array with existing trailing capacity" | Fill destination from the highest index downward to avoid shifting | §14.12 |
| **XOR / Bit Trick** | "find the missing/duplicate/unique number", O(1) space required | Exploit `x^x=0` and XOR's commutativity | §14.13 |
| **Boundary Shrinking (2D)** | "spiral order", "print matrix in a specific order" | Track `top/bottom/left/right`; traverse and shrink each edge | §14.14 |
| **Transpose + Reverse (2D)** | "rotate matrix in place" | Decompose a 2D geometric transform into simpler composable steps | §14.15 |
| **Reversal Algorithm** | "rotate array in place, O(1) space" | Reverse whole, then reverse each logical segment | §14.3 |

---

## 16. Common Mistakes Compendium

A consolidated list of the Java-array-specific mistakes that appear repeatedly across beginner and even experienced code:

1. **Confusing `.length` (field) with `.length()` (method).** Arrays use the field `arr.length`; `String`/`ArrayList`-style `.length()`/`.size()` are methods. Mixing these up is a compile error, not a runtime bug — but it trips up almost everyone at least once.
2. **Assuming `arr.equals(other)` compares contents.** It doesn't — `Object.equals` is reference-based. Use `Arrays.equals`/`Arrays.deepEquals`.
3. **Assuming assignment (`b = a`) copies an array.** It only copies the reference — both variables alias the same object (§3.4, §9.1).
4. **Using `.clone()` (or `Arrays.copyOf`) on a 2D array and expecting a deep copy.** These are shallow — inner rows remain shared (§9.2, §9.3).
5. **Forgetting arrays have guaranteed default values.** `new int[n]` is already all-zeros; `new String[n]` is already all-`null`s — no manual zero-fill loop is needed, and indexing into a `null` object-array slot before assigning it throws `NullPointerException`.
6. **Off-by-one errors in bounds.** `arr.length` is the count of elements; the last valid index is `arr.length - 1`. `ArrayIndexOutOfBoundsException` is the direct consequence of miscounting this.
7. **Negative or invalid array sizes.** `new int[-1]` compiles fine (size is a runtime `int` expression) but throws `NegativeArraySizeException` at runtime — always validate sizes computed from user input or arithmetic.
8. **Not normalizing rotation/modulo indices.** Java's `%` can return negative results for negative operands (unlike some other languages) — always use `((x % n) + n) % n` when negative wraparound is possible.
9. **Mutating an array through the enhanced for-each loop variable and expecting it to persist.** For-each gives you a copy of each value for primitives — reassigning the loop variable never affects the array (§6.2).
10. **Row-length assumptions on jagged arrays.** Using `grid[0].length` as a universal inner bound is wrong once any row has a different length — always query `grid[i].length` per row (§6.7, §10.3).
11. **Generic array creation.** `new T[n]` and `new List<String>[n]` don't compile due to type erasure — use `Object[]` internally with casts, or `List<T[]>`-adjacent workarounds (§12.7).
12. **`ArrayStoreException` from covariant object arrays.** Assigning an incompatible runtime type into a covariant array reference (e.g., an `Integer` into an array whose *actual* runtime type is `String[]`, viewed through an `Object[]` variable) compiles but throws at runtime (§12.8).
13. **Reusing `Arrays.asList()` on a primitive array.** `Arrays.asList(int[])` produces a `List<int[]>` with one element, not a `List<Integer>` — a classic and very common trap (§11.7).
14. **Trying to `.add()` to `Arrays.asList()`'s result.** It's a fixed-size view backed by the original array — structural modification throws `UnsupportedOperationException`.
15. **Assuming `final` makes array contents immutable.** `final` only locks the reference from reassignment; elements remain fully mutable (§12.2).
16. **Leaving stale references after "logical" removal from an array-backed structure.** This can silently leak memory by preventing garbage collection (§3.6).
17. **Column-major traversal of large 2D arrays for performance-sensitive code**, when row-major would be dramatically more cache-friendly (§13.3).
18. **Using `Integer[]`/boxed types by default** in numerically heavy code without considering the boxing and cache-locality performance cost of primitive `int[]` alternatives (§13.2).

---

## 17. Interview Quick-Reference Sheet

**Before coding, always clarify:**
- Is the array sorted?
- Can it contain duplicates / negatives / zero?
- Is in-place (O(1) extra space) modification required, or is a new array acceptable?
- What should happen on empty input, or if no valid answer exists?
- Are you allowed to use `java.util.Arrays` helper methods, or must you implement the underlying logic by hand?

**Complexity cheat sheet for common array operations:**

| Operation | Time | Space |
|---|---|---|
| Access by index | O(1) | O(1) |
| Linear scan (search unsorted) | O(n) | O(1) |
| Two-pointer scan | O(n) | O(1) |
| Sliding window (fixed/variable) | O(n) | O(1) or O(k) |
| `Arrays.sort` (primitive, dual-pivot quicksort) | O(n log n) avg | O(log n) |
| `Arrays.sort` (object, stable mergesort-derived) | O(n log n) | O(n) |
| `Arrays.binarySearch` (sorted array) | O(log n) | O(1) |
| `System.arraycopy` / `Arrays.copyOf` | O(n) | O(n) new array |
| Insert/delete at arbitrary index (manual shift) | O(n) | O(1) |
| 2D traversal | O(rows × cols) | O(1) extra |

**Communication tips:**
- State the brute-force approach and its complexity first, even briefly — it anchors the conversation and often reveals the "why" behind the optimized approach.
- Narrate the invariant you're maintaining in loops (e.g., "everything left of `writePos` is guaranteed non-zero") — this is exactly what interviewers listen for to confirm real understanding versus memorized code.
- Always dry-run your final code on a small example out loud before declaring it done — this catches off-by-one bugs live, which is far better than an interviewer catching them for you.

---

## 18. Practice Problem List

Organized by pattern (§15) for structured practice, roughly in increasing difficulty within each group:

**Two Pointers / In-Place Manipulation**
- Reverse an array (§14.2)
- Rotate array by k (§14.3)
- Move zeroes to end (§14.4)
- Remove duplicates from a sorted array in place
- Sort an array of 0s, 1s, 2s (§14.5)
- Container with most water
- Trapping rain water (§14.10)

**Sliding Window**
- Maximum sum subarray of size k (§14.11)
- Smallest subarray with a sum ≥ target (variable window)
- Longest subarray with at most K distinct values

**Prefix / Suffix**
- Product of array except self (§14.8)
- Range sum query (immutable array)
- Equilibrium index of an array

**Running Extremum / Greedy**
- Find min and max in one pass (§14.1)
- Best time to buy and sell stock (§14.7)
- Maximum difference between two elements (larger after smaller)

**Kadane's Technique**
- Maximum subarray sum (§14.6)
- Maximum product subarray
- Maximum sum circular subarray

**Two Sum Family**
- Two Sum — sorted array (§14.9)
- Two Sum — unsorted array
- 3Sum / 4Sum (extensions requiring sorting + multi-pointer techniques)

**Bit Tricks**
- Find the missing number (§14.13)
- Find the number that appears once (all others appear twice)
- Find two numbers that appear once (all others appear twice)

**Merging**
- Merge two sorted arrays in place (§14.12)
- Merge intervals (requires sorting first)

**2D Arrays / Matrices**
- Spiral matrix traversal (§14.14)
- Rotate matrix 90° in place (§14.15)
- Set matrix zeroes in place
- Search a 2D sorted matrix
- Transpose a matrix

---

