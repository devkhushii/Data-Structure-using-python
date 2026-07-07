# 🕸️ THE COMPLETE PYTHON GRAPH HANDBOOK


---

## 📚 TABLE OF CONTENTS

1. [Introduction to Graphs](#1-introduction-to-graphs)
2. [Graph Fundamentals & Terminology](#2-graph-fundamentals--terminology)
3. [Types of Graphs](#3-types-of-graphs)
4. [Python Graph Representations](#4-python-graph-representations)
5. [Graph Traversals — DFS & BFS](#5-graph-traversals--dfs--bfs)
6. [Connected Components & Flood Fill](#6-connected-components--flood-fill)
7. [Cycle Detection](#7-cycle-detection)
8. [Topological Sorting](#8-topological-sorting)
9. [Shortest Path Algorithms](#9-shortest-path-algorithms)
10. [Minimum Spanning Tree (MST)](#10-minimum-spanning-tree-mst)
11. [Disjoint Set Union / Union-Find](#11-disjoint-set-union--union-find)
12. [Strongly Connected Components](#12-strongly-connected-components)
13. [Bridges & Articulation Points](#13-bridges--articulation-points)
14. [Bipartite Graphs](#14-bipartite-graphs)
15. [Euler Path, Circuit & Hamiltonian Path](#15-euler-path-circuit--hamiltonian-path)
16. [Maximum Flow](#16-maximum-flow)
17. [Advanced Graph Concepts](#17-advanced-graph-concepts)
18. [Graph Patterns for Interviews](#18-graph-patterns-for-interviews)
19. [Problem Recognition — Decision Trees](#19-problem-recognition--decision-trees)
20. [Optimization Guide](#20-optimization-guide)
21. [Python Tips for Graph Problems](#21-python-tips-for-graph-problems)
22. [Common Mistakes](#22-common-mistakes)
23. [Cheat Sheets](#23-cheat-sheets)
24. [Practice Problem Bank](#24-practice-problem-bank)
25. [Final Revision & Roadmap](#25-final-revision--roadmap)

---

## 1. Introduction to Graphs

### 1.1 What Is a Graph?

A **graph** is a non-linear data structure consisting of a set of **vertices** (also called nodes) connected by **edges**. Formally, a graph `G` is defined as an ordered pair:

```
G = (V, E)
```

where `V` is a finite set of vertices and `E` is a set of edges, each edge being a pair of vertices `(u, v)`.

Unlike arrays, linked lists, or trees (which impose a strict linear or hierarchical structure), graphs can model **arbitrary relationships** — many-to-many, cyclic, or hierarchical — making them the most general and powerful data structure in computer science.

### 1.2 Why Graphs Exist

Every tree is a graph, but not every graph is a tree. Real-world systems are rarely purely hierarchical:

- Cities aren't arranged in a tree — roads form cycles and shortcuts.
- People in a social network don't have a single "parent."
- Tasks in a build system depend on multiple other tasks, not just one.

Graphs exist because **relationships in the real world are networks, not lists or hierarchies**. Whenever you have "things" and "connections between things," you have a graph.

### 1.3 A Brief History

Graph theory was born in 1736 when Leonhard Euler solved the **Seven Bridges of Königsberg** problem — proving it was impossible to walk through the city crossing each of its seven bridges exactly once. This gave rise to the concept of **Eulerian paths** and is considered the founding result of graph theory. Since then, graph theory has grown into a central pillar of discrete mathematics, computer science, operations research, and network science.

### 1.4 Real-World Analogy

Think of a graph like a **city road map**:
- **Vertices** = cities/intersections
- **Edges** = roads connecting them
- **Edge weight** = distance or travel time
- **Directed edge** = a one-way street
- **Undirected edge** = a two-way street

Any question you'd ask about a road network ("shortest route," "can I reach city B from city A," "minimum roads needed to connect all cities") is a graph problem in disguise.

### 1.5 ASCII Visualization — A Simple Graph

```
        (A)-------(B)
         |  \       |
         |   \      |
         |    \     |
        (C)----(D)-(E)

Vertices: {A, B, C, D, E}
Edges: {(A,B), (A,C), (A,D), (B,E), (C,D), (D,E)}
```

### 1.6 Applications of Graphs

| Domain | Application |
|---|---|
| Maps & Navigation | Shortest route (Google Maps, GPS) |
| Social Networks | Friend suggestions, influence spread |
| Web | Web crawling, PageRank |
| Software Engineering | Build systems, dependency resolution |
| Compilers | Data-flow analysis, register allocation |
| Networking | Routing protocols (OSPF, BGP) |
| AI | State-space search, game trees |
| Scheduling | Task ordering, deadlock detection |
| Biology | Protein interaction networks |
| Recommendation Systems | Collaborative filtering graphs |
| Games | Pathfinding (A*, Dijkstra) |

### 1.7 Advantages & Disadvantages

**Advantages**
- Models arbitrary relationships (many-to-many)
- Naturally represents networks, hierarchies, and cycles
- Rich algorithmic toolkit (shortest path, flow, connectivity)

**Disadvantages**
- Higher memory overhead for dense graphs (adjacency matrix)
- More complex to implement and reason about than linear structures
- Some problems (Hamiltonian path, graph isomorphism) are NP-hard

> 💡 **Interview Tip:** Interviewers love graphs because they test recursion, iteration, greedy reasoning, and invariant thinking all at once. Master the "big 6" — DFS, BFS, Union-Find, Dijkstra, Topological Sort, and MST — and you can solve 90% of graph interview questions.

---

## 2. Graph Fundamentals & Terminology

| Term | Definition |
|---|---|
| **Vertex (Node)** | A fundamental unit/entity in the graph |
| **Edge** | A connection between two vertices |
| **Degree** | Number of edges incident to a vertex |
| **In-degree** | Number of incoming edges to a vertex (directed graphs) |
| **Out-degree** | Number of outgoing edges from a vertex (directed graphs) |
| **Path** | Sequence of vertices connected by edges, no repeated vertices |
| **Walk** | Sequence of vertices/edges, vertices/edges CAN repeat |
| **Trail** | A walk with no repeated edges (vertices may repeat) |
| **Circuit** | A trail that starts and ends at the same vertex |
| **Cycle** | A path that starts and ends at the same vertex, no repeated edges/vertices (except start=end) |
| **Connected Component** | A maximal set of vertices all reachable from each other |
| **Density** | Ratio of actual edges to maximum possible edges |
| **Self-loop** | An edge connecting a vertex to itself |
| **Parallel Edges** | Multiple edges between the same pair of vertices |
| **Complete Graph** | Every pair of vertices is connected by an edge |
| **Sparse Graph** | `E ≈ O(V)` — few edges relative to vertices |
| **Dense Graph** | `E ≈ O(V²)` — edges close to the maximum possible |

### 2.1 ASCII: Degree, In-degree, Out-degree

```
Undirected:              Directed:
   (A)---(B)                (A)--->(B)
    |                         ^      |
    |                         |      v
   (C)                       (C)<---(D)

deg(A) = 2                indeg(B)=1, outdeg(B)=1
deg(B) = 1                indeg(A)=1, outdeg(A)=1
deg(C) = 1
```

### 2.2 Path vs Walk vs Trail vs Circuit vs Cycle

```
Walk:    A -> B -> A -> C     (repeats vertex A, repeats edge A-B)
Trail:   A -> B -> C -> A     (repeats vertex A, no repeated edge)
Path:    A -> B -> C -> D     (no repeats at all)
Circuit: A -> B -> C -> A     (trail returning to start)
Cycle:   A -> B -> C -> A     (path returning to start, no repeated edges/vertices except endpoints)
```

> ⚠️ **Common Confusion:** "Path" and "Cycle" are often used loosely in interviews to mean "any route," but formally a path has no repeated vertices. Always clarify in interviews whether repeated vertices are allowed.

---

## 3. Types of Graphs

### 3.1 Directed vs Undirected

```
Undirected:          Directed:
  (A)---(B)            (A)--->(B)
   edge A-B == B-A      edge A->B ≠ B->A
```
In an **undirected** graph, edge `(u,v)` implies you can travel both `u→v` and `v→u`. In a **directed** graph (digraph), `(u,v)` only allows `u→v`.

### 3.2 Weighted vs Unweighted

```
Unweighted:  (A)---(B)          Weighted:  (A)--5--(B)
```
Weighted edges carry a cost (distance, time, capacity). Unweighted edges imply cost = 1 for every edge (used directly in BFS shortest-path).

### 3.3 Connected vs Disconnected

```
Connected:                Disconnected:
 (A)-(B)-(C)                (A)-(B)     (C)-(D)
     |                       (two components)
    (D)
```

### 3.4 Complete Graph

Every vertex connects to every other vertex. For `n` vertices, a complete undirected graph has `n(n-1)/2` edges.

```
   (A)---(B)
    | \ / |
    |  X  |
    | / \ |
   (C)---(D)
```

### 3.5 Bipartite Graph

Vertices can be split into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other (no edges within the same set).

```
Set 1:  (A)   (B)
          \   /  \
           \ /    \
Set 2:    (C)     (D)
```

### 3.6 Cyclic vs Acyclic (DAG)

```
Cyclic:                DAG (Directed Acyclic Graph):
 (A)->(B)                (A)->(B)->(D)
  ^     |                  \        ^
  |     v                   v      /
 (C)<---+                  (C)----+
```
A **DAG** has no directed cycles — critical for topological sorting, scheduling, and dependency resolution.

### 3.7 Multigraph & Pseudograph

- **Multigraph**: allows parallel edges between the same pair of vertices.
- **Pseudograph**: a multigraph that additionally allows self-loops.

```
Multigraph:  (A)===(B)   (two parallel edges)
Pseudograph: (A)--(A)    (self-loop) plus parallel edges allowed
```

### 3.8 Planar Graph

A graph that can be drawn on a plane without any edges crossing. Important in map coloring and circuit design.

### 3.9 Grid Graph

An implicit graph where each cell in a 2D matrix is a vertex, and edges connect adjacent cells (4-directional or 8-directional). Extremely common in interview problems (islands, mazes, flood fill).

```
Grid:                  As a Graph:
1 1 0                  (0,0)-(0,1)
1 0 0                    |
0 0 1                  (1,0)

Each cell connects to up/down/left/right (and optionally diagonal) neighbors.
```

### 3.10 Tree — A Special Graph (Comparison Only)

A tree is a **connected, acyclic, undirected graph** with exactly `V - 1` edges for `V` vertices. Every tree is a graph, but a graph is a tree only if it satisfies all three properties: connected, acyclic, and undirected with `V-1` edges. This handbook does not cover trees as a standalone topic — only where relevant for comparison (e.g., MST *is* a tree; DFS traversal produces a *traversal tree*).

### 3.11 Summary Table

| Graph Type | Key Property | Example Use Case |
|---|---|---|
| Directed | Edges have direction | Web page links, task dependencies |
| Undirected | Edges are bidirectional | Friendships, road networks |
| Weighted | Edges carry cost | Distances, travel time |
| Unweighted | All edges cost 1 | BFS shortest path |
| Connected | One component | Guaranteed reachability |
| Disconnected | Multiple components | Isolated subnetworks |
| Complete | All pairs connected | Worst-case density analysis |
| Bipartite | Two-colorable | Matching, scheduling |
| Cyclic | Contains a cycle | Deadlock detection |
| DAG | No directed cycle | Task scheduling, build systems |
| Multigraph | Parallel edges allowed | Multiple flights between cities |
| Planar | No crossing edges | Circuit layout, map coloring |
| Grid Graph | Implicit graph over matrix | Islands, mazes, flood fill |


---

## 4. Python Graph Representations

There are three standard ways to represent a graph in Python. Choosing the right one affects both memory usage and algorithm speed.

### 4.1 Adjacency List (Most Common in Interviews)

**Definition:** For each vertex, store a list of its neighbors.

**Why it exists:** Most real-world graphs are sparse (`E << V²`). An adjacency list uses `O(V + E)` memory instead of `O(V²)`, and is the default choice for almost all interview problems.

```
Graph:            Adjacency List:
(A)---(B)         A: [B, C]
 |                B: [A, D]
(C)---(D)         C: [A, D]
                  D: [B, C]
```

```python
from collections import defaultdict

def build_adjacency_list(n, edges, directed=False):
    """
    Build an adjacency list from a list of edges.

    n       : number of vertices (labeled 0 to n-1)
    edges   : list of (u, v) or (u, v, w) tuples
    directed: whether the graph is directed
    """
    graph = defaultdict(list)          # graph[u] -> list of neighbors
    for edge in edges:
        if len(edge) == 2:
            u, v = edge
            graph[u].append(v)         # add edge u -> v
            if not directed:
                graph[v].append(u)     # add edge v -> u (undirected)
        else:
            u, v, w = edge
            graph[u].append((v, w))    # weighted edge u -> v with weight w
            if not directed:
                graph[v].append((u, w))
    return graph

# Example
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
g = build_adjacency_list(4, edges)
print(dict(g))
# {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
```

**Line-by-line explanation:**
- `defaultdict(list)` automatically creates an empty list for any new key, avoiding `KeyError`.
- For each edge, we append `v` to `graph[u]`'s list. This means "u is connected to v."
- If undirected, we also append `u` to `graph[v]` (edge works both ways).
- For weighted edges, we store `(neighbor, weight)` tuples instead of plain neighbors.

**Time Complexity:** `O(V + E)` to build. **Space Complexity:** `O(V + E)`.

| Operation | Adjacency List Cost |
|---|---|
| Add edge | O(1) |
| Check if edge exists | O(degree(u)) |
| Iterate all neighbors of u | O(degree(u)) |
| Iterate all edges | O(V + E) |

### 4.2 Adjacency Matrix

**Definition:** A `V x V` 2D array where `matrix[u][v] = 1` (or weight) if an edge exists, else `0` (or infinity).

```
Graph:            Adjacency Matrix:
(A)---(B)              A  B  C  D
 |                   A[ 0  1  1  0 ]
(C)---(D)            B[ 1  0  0  1 ]
                     C[ 1  0  0  1 ]
                     D[ 0  1  1  0 ]
```

```python
def build_adjacency_matrix(n, edges, directed=False):
    matrix = [[0] * n for _ in range(n)]   # n x n grid initialized to 0
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix
```

**Time Complexity:** `O(V²)` to build/store. **Space Complexity:** `O(V²)` always, regardless of edge count.

| Operation | Adjacency Matrix Cost |
|---|---|
| Add edge | O(1) |
| Check if edge exists | O(1) |
| Iterate all neighbors of u | O(V) |
| Iterate all edges | O(V²) |

> ⚠️ **When to avoid:** Never use an adjacency matrix for sparse graphs with `V > ~5000` — memory blows up quadratically. Use it only when `V` is small or the graph is dense, or when O(1) edge lookup is critical (e.g., Floyd-Warshall).

### 4.3 Edge List

**Definition:** Simply a list of all edges `(u, v)` or `(u, v, w)`.

```python
edges = [(0, 1), (0, 2), (1, 3), (2, 3, 7)]   # last one weighted
```

Best suited for algorithms that process **all edges globally** rather than per-vertex neighbors — e.g., **Kruskal's MST** (sort all edges) and **Bellman-Ford** (relax all edges every iteration).

**Time/Space:** `O(E)` space; `O(E log E)` if sorting is needed.

### 4.4 Dictionary-Based / Object-Oriented Graph Class

For larger systems, wrapping the graph in a class keeps state and behavior together.

```python
class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj = defaultdict(list)

    def add_edge(self, u, v, w=None):
        self.adj[u].append((v, w) if w is not None else v)
        if not self.directed:
            self.adj[v].append((u, w) if w is not None else u)

    def neighbors(self, u):
        return self.adj[u]

    def vertices(self):
        return list(self.adj.keys())

    def __repr__(self):
        return f"Graph({dict(self.adj)})"

g = Graph(directed=True)
g.add_edge(0, 1)
g.add_edge(1, 2)
print(g)   # Graph({0: [1], 1: [2]})
```

### 4.5 Comparison Table — Which Representation to Use

| Representation | Space | Edge Lookup | Best For |
|---|---|---|---|
| Adjacency List | O(V+E) | O(deg(u)) | Sparse graphs, DFS/BFS, most interview problems |
| Adjacency Matrix | O(V²) | O(1) | Dense graphs, Floyd-Warshall, small V |
| Edge List | O(E) | O(E) | Kruskal's MST, Bellman-Ford |
| OOP Graph Class | O(V+E) | O(deg(u)) | Larger systems, reusable graph library code |

> 💡 **Interview Tip:** Default to adjacency list unless the problem explicitly gives you a matrix (e.g., "grid of 0s and 1s") or needs O(1) edge existence checks. 95% of LeetCode graph problems expect adjacency-list thinking.

### 4.6 Best Practices

- Use `defaultdict(list)` to avoid manual key initialization.
- Use 0-indexed vertices unless the problem states otherwise.
- For weighted graphs, store `(neighbor, weight)` tuples — keep the order consistent throughout your codebase.
- For grid-graph problems, don't build an explicit graph — treat `(row, col)` as vertices and compute neighbors on the fly using direction vectors.


---

## 5. Graph Traversals — DFS & BFS

Traversal is the foundation of almost every graph algorithm. Master these two and everything else (cycle detection, topological sort, components, bipartite check) becomes a small variation.

### 5.1 Depth-First Search (DFS)

**Definition:** Explore as far as possible along each branch before backtracking.

**Intuition:** Like solving a maze — you pick a direction and keep going until you hit a dead end, then backtrack.

**Real-world analogy:** Exploring a cave system with a rope — you go as deep as possible down one tunnel before backing out and trying another.

**ASCII Visualization:**

```
        A
       / \
      B   C
     /     \
    D       E

DFS from A: A -> B -> D -> (backtrack) -> C -> E
```

#### 5.1.1 Recursive DFS

```python
def dfs_recursive(graph, node, visited=None):
    """
    graph   : adjacency list, dict[node] -> list of neighbors
    node    : current node
    visited : set of visited nodes
    """
    if visited is None:
        visited = set()
    visited.add(node)          # mark current node as visited
    print(node, end=" ")       # process node (here: print)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)   # recurse deeper

    return visited

graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
dfs_recursive(graph, 0)   # Output: 0 1 3 2
```

**Line-by-line explanation:**
- `visited` set prevents revisiting a node and causing infinite recursion (critical in cyclic graphs).
- We mark `node` visited **before** recursing to avoid two branches visiting it simultaneously.
- The recursive call goes as deep as possible before returning (backtracking) to try other neighbors.

**Dry Run:**

| Step | Current Node | Call Stack | Visited | Output |
|---|---|---|---|---|
| 1 | 0 | [0] | {0} | 0 |
| 2 | 1 | [0,1] | {0,1} | 1 |
| 3 | 3 | [0,1,3] | {0,1,3} | 3 |
| 4 | (backtrack to 1, no more neighbors) | [0,1] | {0,1,3} | — |
| 5 | (backtrack to 0) | [0] | {0,1,3} | — |
| 6 | 2 | [0,2] | {0,1,2,3} | 2 |

**Time Complexity:** `O(V + E)` — every vertex and edge is visited once.
**Space Complexity:** `O(V)` for visited set + `O(V)` recursion stack (worst case, a long chain).

#### 5.1.2 Iterative DFS (Using an Explicit Stack)

```python
def dfs_iterative(graph, start):
    visited = set([start])
    stack = [start]
    order = []

    while stack:
        node = stack.pop()          # LIFO -> depth-first behavior
        order.append(node)
        for neighbor in reversed(graph[node]):   # reversed to match recursive order
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return order
```

> ⚠️ **Common Mistake:** Marking a node visited when it's *popped* instead of when it's *pushed* can cause the same node to be pushed multiple times, wasting memory (though still correct). Mark visited at push time to avoid duplicate stack entries.

**When to use recursive vs iterative DFS:**
- Recursive: cleaner code, but risks `RecursionError` on deep graphs (Python's default recursion limit is 1000).
- Iterative: use for very large/deep graphs, or when you need explicit control over the stack (e.g., tracking path).

### 5.2 Breadth-First Search (BFS)

**Definition:** Explore all neighbors at the current depth before moving to nodes at the next depth level.

**Intuition:** Ripples spreading outward from a stone dropped in water — level by level.

**Real-world analogy:** Fire spreading through a building floor by floor, or a rumor spreading through direct friends first, then friends-of-friends.

**ASCII Visualization:**

```
        A
       / \
      B   C
     /     \
    D       E

BFS from A: Level 0: A
            Level 1: B, C
            Level 2: D, E
Output: A B C D E
```

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])       # FIFO -> breadth-first behavior
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)      # mark visited at ENQUEUE time
                queue.append(neighbor)
    return order

graph = {0: [1, 2], 1: [0, 3], 2: [0, 4], 3: [1], 4: [2]}
print(bfs(graph, 0))   # [0, 1, 2, 3, 4]
```

**Line-by-line explanation:**
- `deque` gives O(1) `popleft()`, unlike a plain list (`O(n)` for `pop(0)`).
- We mark nodes visited **when enqueued**, not when dequeued — this prevents adding the same node to the queue multiple times.
- BFS guarantees the first time you reach a node is via the **shortest path** (in terms of edge count) from the start — this is why BFS is used for unweighted shortest-path problems.

**Dry Run:**

| Step | Current Node | Queue | Visited | Output |
|---|---|---|---|---|
| 1 | — | [0] | {0} | [] |
| 2 | 0 | [1,2] | {0,1,2} | [0] |
| 3 | 1 | [2,3] | {0,1,2,3} | [0,1] |
| 4 | 2 | [3,4] | {0,1,2,3,4} | [0,1,2] |
| 5 | 3 | [4] | {0,1,2,3,4} | [0,1,2,3] |
| 6 | 4 | [] | {0,1,2,3,4} | [0,1,2,3,4] |

**Time Complexity:** `O(V + E)`. **Space Complexity:** `O(V)`.

### 5.3 Multi-Source BFS

**Definition:** Start BFS simultaneously from multiple source nodes by initializing the queue with all of them at once (all at "level 0").

**Why it exists:** Problems like "distance from nearest gas station" or "rotting oranges" require finding shortest distance to *any* of several sources — running BFS separately from each source would be inefficient (`O(k*(V+E))`); multi-source BFS does it in one pass — `O(V+E)`.

```python
def multi_source_bfs(graph, sources):
    visited = set(sources)
    queue = deque(sources)         # enqueue ALL sources at once, distance 0
    dist = {s: 0 for s in sources}

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist
```

**Classic problem:** LeetCode 994 "Rotting Oranges" — all initially rotten oranges are sources; find minimum time until all oranges rot.

### 5.4 DFS vs BFS — When to Use Which

| Criterion | DFS | BFS |
|---|---|---|
| Shortest path (unweighted) | ❌ Not guaranteed | ✅ Guaranteed |
| Memory usage | O(depth) — better for wide, shallow graphs | O(width) — better for deep, narrow graphs |
| Detecting cycles | ✅ Natural fit | ✅ Also works |
| Topological sort | ✅ Natural fit | ✅ (Kahn's algorithm) |
| Connected components | ✅ | ✅ |
| Finding ANY path | ✅ Simple | ✅ Simple |
| Level-order / distance | ❌ | ✅ Natural fit |
| Exploring all paths / backtracking | ✅ | ❌ |

> 💡 **Interview Recognition Clue:** If the question mentions "shortest," "minimum steps," or "levels," think **BFS**. If it mentions "all paths," "connectivity," "can you reach," or involves backtracking/recursion naturally, think **DFS**.

### 5.5 Edge Cases for Traversals

- **Empty graph** (`V = 0`): return empty result immediately.
- **Disconnected graph**: a single BFS/DFS call from one node won't visit everything — must loop over all vertices and start a new traversal for each unvisited one (see Section 6).
- **Self-loops**: a node connected to itself — visited-check prevents infinite loop.
- **Single node, no edges**: traversal should return just that node.

### 5.6 Common Mistakes

- Forgetting the `visited` set entirely → infinite loop on cyclic graphs.
- Marking visited at the wrong time in BFS (should be at enqueue, not dequeue) → duplicate queue entries, incorrect distances in weighted variants.
- Using recursion for very deep graphs → `RecursionError: maximum recursion depth exceeded`. Fix: increase `sys.setrecursionlimit()` or convert to iterative.
- Confusing adjacency list direction — iterating `graph[node]` when you meant `graph[neighbor]`.


---

## 6. Connected Components & Flood Fill

### 6.1 Connected Components (Undirected Graphs)

**Definition:** A connected component is a maximal subset of vertices such that every vertex is reachable from every other vertex within that subset.

**Why it exists:** Real graphs are often disconnected — social networks have isolated clusters, road networks have unreachable islands. Counting/labeling components answers "how many separate groups exist?"

```
Graph:
(0)-(1)   (2)-(3)     (4)

Components: {0,1}, {2,3}, {4}   -> 3 components
```

```python
def count_components(n, graph):
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for v in range(n):
        if v not in visited:
            dfs(v)              # new component found
            count += 1
    return count
```

**Complexity:** `O(V + E)` time, `O(V)` space.

### 6.2 Flood Fill / Grid Connected Components

**Definition:** Same idea applied to a 2D grid — find/label connected regions of matching cells (e.g., "islands" of 1s in a matrix of 0s/1s).

**ASCII:**
```
Grid:              Island 1        Island 2
1 1 0 0            1 1 . .         . . . .
1 1 0 0     -->    1 1 . .    +    . . . .
0 0 0 1            . . . .         . . . 1
```

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # up, down, left, right

    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and not visited[nr][nc] and grid[nr][nc] == '1'):
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:
                bfs(r, c)
                islands += 1
    return islands
```

**Line-by-line explanation:**
- `visited` grid mirrors the input grid's shape to track explored cells.
- `directions` list encodes the 4 cardinal neighbor offsets — add diagonals `(-1,-1),(-1,1),(1,-1),(1,1)` for 8-directional connectivity.
- Each unvisited land cell (`'1'`) triggers a new BFS which "floods" the entire connected region, marking it visited — hence "flood fill."

**Time Complexity:** `O(rows × cols)`. **Space Complexity:** `O(rows × cols)` for visited + queue.

**Dry Run** (grid `[["1","1","0"],["0","1","0"],["0","0","1"]]`):

| Step | Action | Islands Found |
|---|---|---|
| 1 | (0,0)='1', unvisited -> BFS floods (0,0),(0,1),(1,1) | 1 |
| 2 | (2,2)='1', unvisited -> BFS floods just (2,2) | 2 |
| 3 | All other cells are '0' or visited | Final: 2 |

### 6.3 Edge Cases

- Empty grid → return 0 immediately.
- Grid with all water (`0`) → return 0.
- Grid with all land → return 1 (one giant component).
- 4-directional vs 8-directional connectivity must be clarified from the problem statement.

### 6.4 Common Mistakes

- Mutating the input grid in-place to mark visited (works, but destroys input — prefer a separate `visited` matrix unless explicitly allowed).
- Forgetting boundary checks (`0 <= nr < rows`) → `IndexError`.
- Off-by-one errors when computing `rows`/`cols` from `len(grid)` / `len(grid[0])`.

### 6.5 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Number of Islands | LeetCode 200 | Grid flood fill (BFS/DFS) |
| Number of Provinces | LeetCode 547 | Connected components (adjacency matrix) |
| Flood Fill | LeetCode 733 | Basic flood fill |
| Max Area of Island | LeetCode 695 | Flood fill + size tracking |
| Number of Closed Islands | LeetCode 1254 | Boundary-aware flood fill |


---

## 7. Cycle Detection

Cycle detection differs fundamentally between **undirected** and **directed** graphs — this is one of the most common interview trip-ups.

### 7.1 Cycle Detection in Undirected Graphs — DFS (Parent Tracking)

**Definition:** A cycle exists if, during DFS, we reach an already-visited vertex that is **not** the immediate parent of the current vertex.

**Why parent tracking matters:** In an undirected graph, edge `(u,v)` means `v` appears in `u`'s adjacency list AND `u` appears in `v`'s list. So when DFS goes `u -> v`, `v`'s neighbor list contains `u` right back — that is NOT a cycle, just the same edge traversed backward. We must ignore the immediate parent.

**ASCII:**
```
Cyclic:                  Acyclic (Tree):
 (A)---(B)                (A)---(B)
  |     |                        |
 (C)---(D)                      (D)

DFS A->B->D->C->A(visited, not parent) => CYCLE
```

```python
def has_cycle_undirected(n, graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):        # recurse; pass current node as parent
                    return True
            elif neighbor != parent:           # visited AND not the parent => cycle
                return True
        return False

    for v in range(n):
        if v not in visited:
            if dfs(v, -1):
                return True
    return False
```

**Dry Run** (Graph: `0-1, 1-2, 2-0` — a triangle):

| Step | Node | Parent | Visited | Action |
|---|---|---|---|---|
| 1 | 0 | -1 | {0} | Visit neighbor 1 |
| 2 | 1 | 0 | {0,1} | Visit neighbor 2 |
| 3 | 2 | 1 | {0,1,2} | Neighbor 0 is visited AND ≠ parent(1) → **CYCLE** |

**Time Complexity:** `O(V + E)`. **Space Complexity:** `O(V)`.

### 7.2 Cycle Detection in Undirected Graphs — BFS

```python
def has_cycle_undirected_bfs(n, graph):
    visited = set()

    for start in range(n):
        if start in visited:
            continue
        visited.add(start)
        queue = deque([(start, -1)])   # (node, parent)
        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
    return False
```

### 7.3 Cycle Detection in Directed Graphs — DFS (3-Color / Recursion Stack)

**Why this is different:** In a directed graph, revisiting a "visited" node does NOT necessarily mean a cycle — it might just be a **cross edge** to an already-finished branch. We must track whether the node is still **in the current recursion path** (the "gray" state), not just "ever visited."

**3-Color Scheme:**
- **White (0):** unvisited
- **Gray (1):** currently in the recursion stack (being processed)
- **Black (2):** fully processed, recursion finished

A cycle exists **iff** we encounter a **gray** node during DFS.

```
DAG (no cycle):            Directed Cycle:
 (A)->(B)->(C)               (A)->(B)
                              ^     |
                              |     v
                              +----(C)

DFS on cycle: A(gray)->B(gray)->C(gray)->A is GRAY => CYCLE
```

```python
def has_cycle_directed(n, graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY                  # entering recursion stack
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True                  # back edge to an ancestor -> cycle
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK                  # done processing this node
        return False

    for v in range(n):
        if color[v] == WHITE:
            if dfs(v):
                return True
    return False
```

**Line-by-line explanation:**
- `color[node] = GRAY` marks entry into the DFS recursion for this node.
- If we see a `GRAY` neighbor, that's a **back edge** — pointing to an ancestor still being processed — the defining signature of a directed cycle.
- After exploring all neighbors, `color[node] = BLACK` — this node is fully resolved and safe to revisit (it will never trigger a cycle again).

**Dry Run** (Graph: `0->1, 1->2, 2->0`):

| Step | Node | Color Before | Action | Color After |
|---|---|---|---|---|
| 1 | 0 | WHITE | color=GRAY, visit 1 | GRAY |
| 2 | 1 | WHITE | color=GRAY, visit 2 | GRAY |
| 3 | 2 | WHITE | color=GRAY, visit 0 | GRAY |
| 4 | 0 | **GRAY** | neighbor 0 is GRAY → **CYCLE DETECTED** | — |

**Time Complexity:** `O(V + E)`. **Space Complexity:** `O(V)`.

### 7.4 Cycle Detection in Directed Graphs — Kahn's Algorithm (BFS)

If a topological sort (Section 8) cannot include all `V` vertices, the graph contains a cycle. This is a natural byproduct of Kahn's algorithm — see Section 8.2.

```python
def has_cycle_directed_kahn(n, graph):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([v for v in range(n) if indegree[v] == 0])
    visited_count = 0

    while queue:
        node = queue.popleft()
        visited_count += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return visited_count != n   # True => cycle exists
```

### 7.5 Cycle Detection Comparison

| Method | Graph Type | Approach | Complexity |
|---|---|---|---|
| DFS + Parent | Undirected | Ignore immediate parent edge | O(V+E) |
| BFS + Parent | Undirected | Same idea, iterative | O(V+E) |
| DFS + 3-Color | Directed | Detect GRAY (in-stack) node | O(V+E) |
| Kahn's Algorithm | Directed | Topological sort fails to cover all nodes | O(V+E) |

> ⚠️ **The #1 Interview Mistake:** Using the undirected "visited-set" cycle check on a **directed** graph. This gives **false positives** because it doesn't distinguish "ancestor in progress" from "already-finished sibling branch." Always match your cycle detection method to the graph's directedness.

### 7.6 Edge Cases

- Self-loop (`u -> u`): trivially a cycle — must be caught (in directed 3-color, neighbor==node will be GRAY immediately).
- Disconnected graph: must iterate over all unvisited vertices, not just vertex 0.
- Graph with no edges: never a cycle.

### 7.7 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Course Schedule | LeetCode 207 | Directed cycle detection |
| Course Schedule II | LeetCode 210 | Directed cycle + topological order |
| Detect Cycle in Undirected Graph | GeeksforGeeks | DFS parent tracking |
| Graph Valid Tree | LeetCode 261 | Undirected cycle + connectivity |
| Redundant Connection | LeetCode 684 | Union-Find cycle detection |


---

## 8. Topological Sorting

**Definition:** A topological sort of a DAG is a linear ordering of vertices such that for every directed edge `u -> v`, `u` appears before `v` in the ordering.

**Why it exists:** Many real-world problems are "do X before Y" dependency chains — course prerequisites, build systems, spreadsheet formula evaluation. Topological sort gives a valid execution order.

> ⚠️ Topological sort only exists for **DAGs**. If the graph has a cycle, no valid ordering exists.

**Real-world analogy:** Getting dressed — socks before shoes, shirt before jacket. Topological sort finds *a* valid order (not necessarily unique).

**ASCII:**
```
   (Shirt)  (Socks)
      |         |
      v         v
   (Jacket)  (Shoes)

Valid Topo Order: Shirt, Socks, Jacket, Shoes
                   (or Socks, Shirt, Shoes, Jacket, etc.)
```

### 8.1 DFS-Based Topological Sort

**Intuition:** Do a DFS; when a node finishes (all its descendants are processed), push it onto a stack. Reverse the stack at the end — a node's descendants always finish before it, so reversing gives the correct dependency order.

```python
def topo_sort_dfs(n, graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)          # push AFTER all descendants are processed

    for v in range(n):
        if v not in visited:
            dfs(v)

    return stack[::-1]              # reverse to get correct topological order
```

**Line-by-line explanation:**
- We push `node` onto `stack` only after the `for` loop finishes — meaning every descendant has already been fully explored and pushed first.
- Reversing the stack places nodes with no remaining dependents first.

**Dry Run** (Graph: `0->1, 0->2, 1->3, 2->3`):

| Step | Node | Action | Stack |
|---|---|---|---|
| 1 | 0 | visit 1 first | [] |
| 2 | 1 | visit 3 first | [] |
| 3 | 3 | no neighbors, push 3 | [3] |
| 4 | 1 | done, push 1 | [3,1] |
| 5 | 0 | visit 2 | [3,1] |
| 6 | 2 | 3 already visited, push 2 | [3,1,2] |
| 7 | 0 | done, push 0 | [3,1,2,0] |
| Final | — | reverse | [0,2,1,3] |

**Time Complexity:** `O(V + E)`. **Space Complexity:** `O(V)`.

### 8.2 Kahn's Algorithm (BFS-Based Topological Sort)

**Intuition:** Repeatedly remove vertices with **in-degree 0** (no remaining prerequisites) — these can safely go next in the order. Removing a vertex decrements its neighbors' in-degrees, potentially creating new in-degree-0 vertices.

```python
def topo_sort_kahn(n, graph):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([v for v in range(n) if indegree[v] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != n:
        raise ValueError("Graph has a cycle — no valid topological order exists")
    return order
```

**Dry Run** (Graph: `0->1, 0->2, 1->3, 2->3`):

| Step | Queue | Indegree {0,1,2,3} | Order |
|---|---|---|---|
| init | [0] | {0,1,1,2} | [] |
| 1 | [] then [1,2] | {0,0,0,2} | [0] |
| 2 | [2] | {0,0,0,1} | [0,1] |
| 3 | [3] | {0,0,0,0} | [0,1,2] |
| 4 | [] | {0,0,0,0} | [0,1,2,3] |

**Time Complexity:** `O(V + E)`. **Space Complexity:** `O(V)`.

### 8.3 DFS vs Kahn's — When to Use Which

| Criterion | DFS-based | Kahn's (BFS) |
|---|---|---|
| Cycle detection built-in? | Needs separate 3-color check | ✅ Automatic (order.length != n) |
| Detects "all valid orderings" | ❌ One specific order | ✅ Can enumerate level-by-level |
| Preferred when... | You're already doing DFS elsewhere | You need cycle detection + ordering together |
| Implementation simplicity | Slightly simpler recursively | Requires indegree array |

> 💡 **Interview Tip:** Kahn's algorithm is generally preferred in interviews because it naturally detects cycles as a side effect — no need for a separate check.

### 8.4 Edge Cases

- Graph with a cycle → DFS-based sort will produce an *invalid* order silently (must combine with cycle detection); Kahn's naturally detects it via `len(order) != n`.
- Multiple valid topological orders can exist — any one is generally acceptable unless the problem requires lexicographically smallest (use a min-heap instead of a plain queue in Kahn's).
- Disconnected DAG components → both algorithms still work; DFS-based must loop over all unvisited starting vertices.

### 8.5 Common Mistakes

- Forgetting to check for a cycle before trusting the topological order.
- Off-by-one in in-degree counting (counting self-loops incorrectly).
- Using topological sort on an undirected graph — it's undefined for undirected graphs.

### 8.6 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Course Schedule II | LeetCode 210 | Kahn's algorithm |
| Alien Dictionary | LeetCode 269 | Build graph from constraints + topo sort |
| Sequence Reconstruction | LeetCode 444 | Topo sort uniqueness check |
| Minimum Height Trees | LeetCode 310 | Topological "peeling" (leaves) |
| Task Scheduling | GeeksforGeeks | Kahn's algorithm |


---

## 9. Shortest Path Algorithms

### 9.1 BFS Shortest Path (Unweighted Graphs)

**Why it works:** BFS explores nodes level by level, so the first time a node is reached, it's via the minimum number of edges.

```python
def bfs_shortest_path(graph, start, n):
    dist = [-1] * n
    dist[start] = 0
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist
```

**Complexity:** `O(V + E)`. Only valid when **all edges have equal weight (or no weight)**.

### 9.2 Dijkstra's Algorithm (Non-Negative Weighted Graphs)

**Definition:** Finds shortest paths from a single source to all vertices, using a greedy approach: always expand the currently-closest unvisited vertex.

**Why it exists:** BFS fails when edges have different weights — a path with more edges but lower total weight might be shorter. Dijkstra generalizes BFS using a **priority queue (min-heap)** instead of a plain queue.

**Real-world analogy:** GPS navigation — always explore the nearest unvisited intersection next, since it's guaranteed no shorter path to it exists (as long as no negative weights).

**ASCII:**
```
       (A)
      /    \
    4/      \1
    /        \
  (B)---2---(C)
    \        /
    5\      /8
      \    /
       (D)

Dijkstra from A: A=0, C=1, B=min(4, 1+2)=3, D=min(3+5,1+8)=8
```

```python
import heapq

def dijkstra(n, graph, source):
    """
    graph[u] = list of (v, weight) tuples
    """
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]           # (distance, node) — heap orders by distance
    visited = set()

    while pq:
        d, node = heapq.heappop(pq)     # always pop the SMALLEST distance
        if node in visited:
            continue                     # stale entry, skip (lazy deletion)
        visited.add(node)

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist
```

**Line-by-line explanation:**
- `heapq` is a min-heap; `pq[0]` always has the smallest distance — this replaces BFS's FIFO queue.
- `visited` set implements **lazy deletion**: instead of removing stale (outdated) heap entries, we simply skip them when popped, since a fresher, shorter distance was already found.
- Relaxation step (`if new_dist < dist[neighbor]`) is the core of *every* shortest-path algorithm — update if we found a better path.

**Dry Run** (graph above, `A=0,B=1,C=2,D=3`, edges A-B:4, A-C:1, B-C:2, B-D:5, C-D:8):

| Step | Pop (d,node) | Visited | Updates | PQ after |
|---|---|---|---|---|
| 1 | (0,A) | {A} | B=4, C=1 | [(1,C),(4,B)] |
| 2 | (1,C) | {A,C} | B=min(4,1+2)=3, D=1+8=9 | [(3,B),(4,B),(9,D)] |
| 3 | (3,B) | {A,C,B} | D=min(9,3+5)=8 | [(4,B) stale,(8,D),(9,D) stale] |
| 4 | (4,B) stale | skip | — | [(8,D),(9,D)] |
| 5 | (8,D) | {A,C,B,D} | done | — |

Final: `dist = [0, 3, 1, 8]`

**Time Complexity:** `O((V + E) log V)` with a binary heap. **Space Complexity:** `O(V + E)`.

> ⚠️ **Critical Limitation:** Dijkstra **fails with negative edge weights** — once a vertex is marked visited/finalized, we never revisit it, but a negative edge could later produce a shorter path. Use Bellman-Ford for negative weights.

### 9.3 Bellman-Ford Algorithm (Handles Negative Weights)

**Definition:** Relax **all edges** `V-1` times. Guaranteed to find shortest paths even with negative edges, and can detect **negative weight cycles**.

**Why V-1 iterations:** The longest possible shortest path (without cycles) visits at most `V-1` edges. After `V-1` full relaxation passes, all shortest distances are guaranteed correct (if no negative cycle exists).

```python
def bellman_ford(n, edges, source):
    """
    edges: list of (u, v, w)
    """
    dist = [float('inf')] * n
    dist[source] = 0

    for _ in range(n - 1):                  # relax all edges V-1 times
        updated = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:                     # early exit optimization
            break

    # One more pass to detect negative weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return dist
```

**Line-by-line explanation:**
- Outer loop runs `V-1` times — each pass can "extend" the shortest known path by one more edge.
- `updated` flag allows early termination once no distances change (optimization for graphs that converge faster).
- The **extra Vth pass** checks for further improvement — if any edge can still relax, a negative cycle exists (distances would keep decreasing forever).

**Dry Run** (edges: `(0,1,4), (0,2,1), (2,1,2), (1,3,1), (2,3,5)`, source=0):

| Pass | dist[0,1,2,3] | Changes |
|---|---|---|
| init | [0,inf,inf,inf] | — |
| 1 | [0,4,1,inf] | via (0,1),(0,2) |
| 2 | [0,3,1,5] | (2,1): 1+2=3 < 4; (1,3): 3+1=4? wait order matters, dist[3]=min(inf,4+1,1+5)=5 |
| 3 | [0,3,1,4] | (1,3): 3+1=4 < 5 |

**Time Complexity:** `O(V × E)`. **Space Complexity:** `O(V)`.

### 9.4 Floyd-Warshall Algorithm (All-Pairs Shortest Path)

**Definition:** Computes shortest paths between **every pair** of vertices using dynamic programming: "is it shorter to go from i to j directly, or via some intermediate vertex k?"

**Why it exists:** Running Dijkstra/Bellman-Ford from every single source is `O(V × E log V)` or `O(V² × E)`. Floyd-Warshall directly computes all pairs in `O(V³)`, which is simpler and often faster for dense/small graphs.

```python
def floyd_warshall(n, adj_matrix):
    """
    adj_matrix[i][j] = weight of edge i->j, or float('inf') if no edge, 0 if i==j
    """
    dist = [row[:] for row in adj_matrix]     # deep copy

    for k in range(n):                # try every vertex as an intermediate
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
```

**Line-by-line explanation:**
- `k` is the "intermediate" vertex being considered in this DP layer — after the `k`-loop finishes, `dist[i][j]` is guaranteed correct for paths using only vertices `0..k` as intermediates.
- The order of loops (`k` outermost) is **essential** — swapping it breaks correctness because it relies on the DP invariant building up layer by layer.

**Time Complexity:** `O(V³)`. **Space Complexity:** `O(V²)`.

> ⚠️ **When to avoid:** Never use Floyd-Warshall for `V > ~500` — cubic time becomes prohibitive. Use it only for all-pairs queries on small/dense graphs.

### 9.5 A* Search (Overview)

**Definition:** A heuristic-guided variant of Dijkstra that uses `f(n) = g(n) + h(n)` — actual cost so far (`g`) plus an estimated cost to the goal (`h`, the heuristic) — to prioritize exploring nodes likely to be on the shortest path.

**When to use:** Single-source, single-target searches where a good admissible heuristic exists (e.g., Euclidean/Manhattan distance in grid pathfinding, common in games and robotics). A* with `h(n) = 0` degenerates into plain Dijkstra.

```python
def a_star_grid(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])   # Manhattan distance

    pq = [(heuristic(start, goal), 0, start)]    # (f, g, node)
    g_score = {start: 0}
    while pq:
        f, g, node = heapq.heappop(pq)
        if node == goal:
            return g
        r, c = node
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 1:
                new_g = g + 1
                if new_g < g_score.get((nr, nc), float('inf')):
                    g_score[(nr, nc)] = new_g
                    heapq.heappush(pq, (new_g + heuristic((nr,nc), goal), new_g, (nr, nc)))
    return -1
```

### 9.6 Johnson's Algorithm (Overview)

**Definition:** Computes all-pairs shortest paths for **sparse graphs with negative edges** (but no negative cycles) in `O(V² log V + VE)` — faster than Floyd-Warshall's `O(V³)` for sparse graphs.

**How it works (high level):**
1. Add a new vertex connected to all others with weight 0; run Bellman-Ford from it to get potential values `h(v)`.
2. Reweight every edge `(u,v,w)` to `w + h(u) - h(v)` — this makes all weights non-negative without changing shortest paths' relative order.
3. Run Dijkstra from every vertex on the reweighted graph.
4. Convert distances back using the potentials.

> 💡 **Interview Tip:** Johnson's is rarely implemented from scratch in interviews — knowing it exists and *why* it beats Floyd-Warshall on sparse graphs is usually sufficient.

### 9.7 Shortest Path Algorithm Comparison

| Algorithm | Handles Negative Weights? | Detects Negative Cycle? | Complexity | Use Case |
|---|---|---|---|---|
| BFS | N/A (unweighted only) | No | O(V+E) | Unweighted shortest path |
| Dijkstra | ❌ No | No | O((V+E) log V) | Single-source, non-negative weights |
| Bellman-Ford | ✅ Yes | ✅ Yes | O(V×E) | Single-source, negative weights allowed |
| Floyd-Warshall | ✅ Yes | ✅ Yes (diagonal < 0) | O(V³) | All-pairs, small/dense graphs |
| Johnson's | ✅ Yes | ✅ Yes | O(V² log V + VE) | All-pairs, sparse graphs w/ negatives |
| A* | ❌ No (like Dijkstra) | No | O((V+E) log V) w/ heuristic pruning | Single-source-single-target w/ heuristic |

> 💡 **Dijkstra vs Bellman-Ford Interview Clue:** "Non-negative weights, need speed" → Dijkstra. "Negative weights possible, or need to detect a negative cycle (e.g., arbitrage detection)" → Bellman-Ford.

### 9.8 Common Mistakes

- Using Dijkstra on graphs with negative weights → silently wrong answers (no error thrown!).
- Forgetting lazy deletion / stale-entry handling in Dijkstra's heap → can process a node multiple times (still correct, but wasteful without the `visited` check).
- Floyd-Warshall loop order (`k` must be outermost) — a very common bug.
- Not initializing `dist[i][i] = 0` in Floyd-Warshall's matrix.

### 9.9 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Network Delay Time | LeetCode 743 | Dijkstra |
| Cheapest Flights Within K Stops | LeetCode 787 | Bellman-Ford (bounded relaxation) |
| Path With Minimum Effort | LeetCode 1631 | Dijkstra variant (minimax) |
| Find the City With the Smallest Number of Neighbors | LeetCode 1334 | Floyd-Warshall |
| Currency Arbitrage | GeeksforGeeks | Bellman-Ford negative cycle detection |


---

## 7. Cycle Detection

Cycle detection is one of the most frequently tested graph skills — but the algorithm you use **depends entirely on whether the graph is directed or undirected**. This is the single biggest source of interview mistakes.

### 7.1 Cycle Detection in Undirected Graphs (DFS)

**Definition:** A cycle exists if, during DFS, you reach a vertex that is already visited **and is not the immediate parent** of the current vertex.

**Why the parent check matters:** In an undirected graph, edge `(u,v)` is stored as `v` in `graph[u]` AND `u` in `graph[v]`. So from `u`, DFS visits `v`, and from `v`, the neighbor list includes `u` right back — this is NOT a cycle, just the edge you came from.

```
Graph:            DFS from 0:
0 - 1             0 -> 1 -> 2 -> back to 0 (0 is visited AND not parent of 2) => CYCLE
|   |
3 - 2
```

```python
def has_cycle_undirected(n, graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):     # recurse, passing current node as parent
                    return True
            elif neighbor != parent:        # visited AND not the edge we came from
                return True                 # found a back-edge => cycle
        return False

    for v in range(n):
        if v not in visited:
            if dfs(v, -1):
                return True
    return False
```

**Line-by-line explanation:**
- `parent` tracks where we came from, so we don't falsely flag the trivial "back-edge" to our own parent.
- If we encounter a visited neighbor that ISN'T our parent, that means there are two distinct paths to that neighbor — i.e., a cycle.
- The outer loop over all vertices handles disconnected graphs (cycle could be in any component).

**Dry Run** (graph `0-1, 1-2, 2-3, 3-0`):

| Step | Node | Parent | Visited | Action |
|---|---|---|---|---|
| 1 | 0 | -1 | {0} | visit neighbor 1 |
| 2 | 1 | 0 | {0,1} | visit neighbor 2 |
| 3 | 2 | 1 | {0,1,2} | visit neighbor 3 |
| 4 | 3 | 2 | {0,1,2,3} | neighbor 0 is visited AND != parent(2) → CYCLE found |

**Complexity:** `O(V + E)` time, `O(V)` space.

### 7.2 Cycle Detection in Undirected Graphs (BFS / Union-Find)

Alternative using **Union-Find** (see Section 11): for each edge `(u,v)`, if `u` and `v` are already in the same set, adding this edge creates a cycle.

```python
def has_cycle_union_find(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]   # path compression
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return True              # already connected => this edge creates a cycle
        parent[ru] = rv              # union
    return False
```

> 💡 **Interview Tip:** Union-Find cycle detection is preferred for **edge-list style** problems ("Redundant Connection" — LeetCode 684) since it directly identifies *which edge* creates the cycle.

### 7.3 Cycle Detection in Directed Graphs (DFS with Recursion Stack)

**Critical difference:** In directed graphs, a visited node is only part of a cycle if it's in the **current recursion path** (recursion stack), not just visited overall.

```
Graph:  0 -> 1 -> 2       (no cycle — 2 has no outgoing edge back)
        0 -> 1 -> 2 -> 0  (cycle — 2 points back to 0, which IS in recursion stack)
```

```python
def has_cycle_directed(n, graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n           # WHITE=unvisited, GRAY=in current path, BLACK=fully done

    def dfs(node):
        color[node] = GRAY        # mark as "in progress" (on the current DFS path)
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True        # back-edge to a node in current path => cycle
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK        # done exploring this node completely
        return False

    for v in range(n):
        if color[v] == WHITE:
            if dfs(v):
                return True
    return False
```

**Line-by-line explanation:**
- **WHITE** = never visited. **GRAY** = currently on the DFS call stack (ancestor in the current path). **BLACK** = fully processed, popped off the stack.
- A cycle exists **only** if we reach a GRAY node — meaning we've looped back to an ancestor.
- Reaching a BLACK node is fine — it means that node was already fully explored via a *different* path (this is normal in DAGs with shared descendants, NOT a cycle).

> ⚠️ **Common Mistake:** Using a single `visited` set (like the undirected version) for directed cycle detection gives **false positives** — it flags shared descendants (diamond-shaped DAGs) as cycles even when there is none. Always use the 3-color (or a separate `on_stack` boolean array) technique for directed graphs.

**Dry Run** (graph `0->1, 1->2, 2->0`):

| Step | Node | Color Before | Action | Color After |
|---|---|---|---|---|
| 1 | 0 | WHITE | mark GRAY, visit neighbor 1 | GRAY |
| 2 | 1 | WHITE | mark GRAY, visit neighbor 2 | GRAY |
| 3 | 2 | WHITE | mark GRAY, visit neighbor 0 | GRAY |
| 4 | 0 | GRAY | neighbor 0 is GRAY => CYCLE detected | — |

**Complexity:** `O(V + E)` time, `O(V)` space.

### 7.4 Cycle Detection via Kahn's Algorithm (Directed Graphs)

An elegant side-effect of Kahn's topological sort (Section 8.2): **if the topological order produced contains fewer than `V` nodes, the graph has a cycle** (because nodes stuck in a cycle never reach in-degree 0).

```python
def has_cycle_kahn(n, graph):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([v for v in range(n) if indegree[v] == 0])
    processed = 0

    while queue:
        node = queue.popleft()
        processed += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return processed != n     # True if a cycle exists
```

### 7.5 Summary — Choosing the Right Cycle Detection Method

| Graph Type | Best Method | Why |
|---|---|---|
| Undirected, adjacency list | DFS with parent tracking | Simple, O(V+E) |
| Undirected, edge list | Union-Find | Identifies the exact cycle-causing edge |
| Directed, adjacency list | DFS with 3-color / recursion stack | Correctly distinguishes cross-edges from back-edges |
| Directed, need topological order too | Kahn's Algorithm | Two birds, one stone: get order + detect cycle |

### 7.6 Common Mistakes (Cycle Detection)

- Applying the undirected algorithm (with `parent` check only) to a directed graph → false negatives (misses real cycles) or false positives.
- Forgetting to loop over **all vertices** for disconnected graphs → missing cycles in components not reachable from vertex 0.
- Using a single global `visited` set in directed cycle detection instead of a recursion-stack/color scheme → false positives on DAGs with shared nodes (diamond pattern).

### 7.7 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Course Schedule | LeetCode 207 | Directed cycle detection |
| Detect Cycle in Undirected Graph | GeeksforGeeks | Undirected DFS/BFS |
| Redundant Connection | LeetCode 684 | Union-Find |
| Redundant Connection II | LeetCode 685 | Union-Find (directed variant) |
| Find Eventual Safe States | LeetCode 802 | 3-color DFS |


---

## 7. Cycle Detection

Cycle detection differs fundamentally between **undirected** and **directed** graphs, and this distinction is one of the most common interview trip-ups.

### 7.1 Cycle Detection in Undirected Graphs (DFS)

**Intuition:** While doing DFS, if you encounter a neighbor that is already visited **and is not the immediate parent**, you've found a cycle (a "back edge" to a non-parent ancestor).

```
   (0)---(1)
    |     |
   (2)---(3)

DFS from 0: 0 -> 1 -> 3 -> 2 -> back to 0 (visited, not parent) => CYCLE
```

```python
def has_cycle_undirected(n, graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:      # visited AND not the parent -> cycle
                return True
        return False

    for v in range(n):
        if v not in visited:
            if dfs(v, -1):
                return True
    return False
```

**Line-by-line explanation:**
- We track `parent` to avoid falsely flagging the trivial "back-edge" to the vertex we just came from (since undirected edges are stored both ways: `A->B` and `B->A`).
- If we hit a visited neighbor that ISN'T our parent, that means there's another path to reach it — a cycle.

**Complexity:** `O(V + E)` time, `O(V)` space.

### 7.2 Cycle Detection in Undirected Graphs (Union-Find Approach)

An alternative, iterative approach: process each edge; if both endpoints are already in the same set, adding this edge creates a cycle. (Full DSU implementation in Section 11.)

```python
def has_cycle_undirected_dsu(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]   # path compression
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return True         # already connected -> new edge creates a cycle
        parent[ru] = rv
    return False
```

> 💡 **Interview Tip:** DSU-based cycle detection is the standard approach for **Kruskal's MST** validity checks and is often faster to write under time pressure than recursive DFS with parent tracking.

### 7.3 Cycle Detection in Directed Graphs (DFS — 3-Color / Recursion Stack Method)

**Why it's different:** In directed graphs, a "visited" node isn't necessarily part of a cycle — it might just be reachable via multiple paths (a DAG can have this). We need to track nodes in the **current recursion path** specifically.

**Intuition:** Use 3 states — **WHITE** (unvisited), **GRAY** (in current DFS path/recursion stack), **BLACK** (fully processed). A cycle exists if we ever reach a GRAY node.

```
(A)->(B)->(C)
 ^          |
 +----------+

DFS: A(gray) -> B(gray) -> C(gray) -> back to A (GRAY!) => CYCLE
```

```python
def has_cycle_directed(n, graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY                   # mark as "in progress"
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True                  # back edge to an ancestor -> cycle
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK                  # mark fully processed
        return False

    for v in range(n):
        if color[v] == WHITE:
            if dfs(v):
                return True
    return False
```

**Dry Run** (edges: `0->1, 1->2, 2->0`):

| Step | Node | Color Before | Action | Color After |
|---|---|---|---|---|
| 1 | 0 | WHITE | mark GRAY, visit neighbor 1 | GRAY |
| 2 | 1 | WHITE | mark GRAY, visit neighbor 2 | GRAY |
| 3 | 2 | WHITE | mark GRAY, visit neighbor 0 | GRAY |
| 4 | 0 | GRAY | neighbor 0 is GRAY -> **CYCLE DETECTED** | — |

**Complexity:** `O(V + E)` time, `O(V)` space (color array + recursion stack).

### 7.4 Cycle Detection in Directed Graphs (Kahn's Algorithm / BFS Topological Sort)

**Intuition:** If topological sort (Section 8) using Kahn's algorithm cannot process all `V` vertices (some remain with nonzero in-degree), a cycle exists.

```python
def has_cycle_directed_kahn(n, graph):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([v for v in range(n) if indegree[v] == 0])
    processed = 0

    while queue:
        node = queue.popleft()
        processed += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return processed != n     # if not all nodes processed -> cycle exists
```

**Complexity:** `O(V + E)` time, `O(V)` space.

### 7.5 Comparison — Which Cycle Detection to Use

| Graph Type | Recommended Method | Alternative |
|---|---|---|
| Undirected | DFS with parent tracking | Union-Find |
| Directed | DFS with 3-color / recursion stack | Kahn's algorithm (BFS) |

### 7.6 Common Mistakes

- Using undirected cycle logic (parent tracking) on a **directed** graph — gives wrong answers, since direction matters.
- Forgetting to reset/track the recursion stack (`GRAY` set) per DFS call in directed cycle detection — using only a single `visited` set (as in undirected) will falsely detect cycles in valid DAGs with shared descendants.
- Not handling disconnected graphs — must loop over all vertices and start DFS/BFS from each unvisited one.

### 7.7 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Course Schedule | LeetCode 207 | Directed cycle detection |
| Graph Valid Tree | LeetCode 261 | Undirected cycle + connectivity |
| Redundant Connection | LeetCode 684 | Union-Find cycle detection |
| Detect Cycle in Directed Graph | GeeksforGeeks | 3-color DFS |
| Detect Cycle in Undirected Graph | GeeksforGeeks | Parent-tracking DFS |


---

## 7. Cycle Detection

### 7.1 Why Cycle Detection Matters

Cycles indicate circular dependencies (deadlocks in scheduling, infinite loops in build systems, contradictions in prerequisite chains). Detecting them is a prerequisite check before running algorithms like topological sort (which only works on DAGs).

### 7.2 Cycle Detection in Undirected Graphs — DFS (Parent Tracking)

**Intuition:** In an undirected graph, if DFS reaches an already-visited vertex that is **not** the immediate parent, a cycle exists.

```
(A)---(B)
  \   /
   (C)

DFS from A -> B -> C -> back to A (not parent of C) => CYCLE
```

```python
def has_cycle_undirected(n, graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):        # recurse with current node as parent
                    return True
            elif neighbor != parent:           # visited AND not the parent -> cycle
                return True
        return False

    for v in range(n):
        if v not in visited:
            if dfs(v, -1):
                return True
    return False
```

**Line-by-line explanation:**
- `parent` tracks where we came from, so we don't falsely flag the trivial "back-edge" to our immediate parent (which is just the edge we came from, not a cycle).
- If we hit a visited neighbor that ISN'T the parent, we've found a back-edge to an ancestor → cycle confirmed.

**Complexity:** `O(V + E)` time, `O(V)` space.

> ⚠️ **Common Mistake:** Forgetting the `parent` check entirely causes every single edge to be flagged as a "cycle" (since undirected edges are stored both ways: `A: [B]`, `B: [A]`), producing false positives on every graph, even trees.

### 7.3 Cycle Detection in Undirected Graphs — BFS (Union-Find is also common; shown here via BFS)

```python
def has_cycle_undirected_bfs(n, graph):
    visited = set()

    for start in range(n):
        if start in visited:
            continue
        visited.add(start)
        queue = deque([(start, -1)])     # (node, parent)
        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
    return False
```

### 7.4 Cycle Detection in Directed Graphs — DFS (Recursion Stack / Coloring)

**Intuition:** In a directed graph, a cycle exists if DFS encounters a node that is **currently on the recursion stack** (i.e., an ancestor in the current DFS path), not just any visited node.

```
(A)->(B)->(C)
 ^          |
 +----------+

DFS: A -> B -> C -> A (A is on the current recursion stack) => CYCLE
```

We use **3-coloring**: `WHITE` (unvisited), `GRAY` (on current recursion stack), `BLACK` (fully processed).

```python
WHITE, GRAY, BLACK = 0, 1, 2

def has_cycle_directed(n, graph):
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY                 # entering: mark on current path
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True                 # back-edge to ancestor -> cycle
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK                 # done exploring: no longer on path
        return False

    for v in range(n):
        if color[v] == WHITE:
            if dfs(v):
                return True
    return False
```

**Line-by-line explanation:**
- `GRAY` means "currently being explored in this DFS branch" — encountering a `GRAY` neighbor means we've looped back to an ancestor: a true directed cycle.
- `BLACK` means "fully explored, safe" — a `BLACK` neighbor is just a **cross edge** or **forward edge**, not a cycle.
- This distinguishes directed cycle detection from the undirected "parent" trick — in directed graphs you need the full recursion-stack state, not just the immediate parent, because a node can be revisited via a different (non-cyclic) path.

**Dry Run:**

| Step | Node | Color Before | Action | Color After |
|---|---|---|---|---|
| 1 | A | WHITE | Mark GRAY, visit B | GRAY |
| 2 | B | WHITE | Mark GRAY, visit C | GRAY |
| 3 | C | WHITE | Mark GRAY, visit A | GRAY |
| 4 | A | GRAY | Neighbor A is GRAY -> CYCLE detected | — |

**Complexity:** `O(V + E)` time, `O(V)` space.

### 7.5 Cycle Detection in Directed Graphs — Kahn's Algorithm (BFS/Topological)

**Intuition:** A DAG always has at least one node with in-degree 0. If, during Kahn's algorithm, we can't process all `V` nodes (some remain with in-degree > 0 forever), a cycle exists among the leftover nodes.

```python
def has_cycle_directed_kahn(n, graph):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([v for v in range(n) if indegree[v] == 0])
    processed = 0

    while queue:
        node = queue.popleft()
        processed += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return processed != n     # True if cycle exists (not all nodes processed)
```

**Complexity:** `O(V + E)` time, `O(V)` space.

### 7.6 Comparison — Undirected vs Directed Cycle Detection

| Aspect | Undirected | Directed |
|---|---|---|
| Technique | Track parent | Track recursion stack (coloring) or Kahn's in-degree |
| Key check | `neighbor != parent` and visited | `neighbor` is GRAY (on current stack) |
| Alternative method | Union-Find (if union(u,v) already same set → cycle) | Kahn's algorithm (BFS-based) |
| Complexity | O(V+E) | O(V+E) |

### 7.7 Common Mistakes

- Using the undirected "parent" trick on a directed graph — **incorrect**, will miss cycles or report false positives, since direction matters.
- Forgetting to reset "on-stack" status (`BLACK`) after fully exploring a node — leads to false cycle detection on unrelated branches.
- Not handling disconnected graphs — must loop over all unvisited vertices, not just vertex 0.

### 7.8 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Course Schedule | LeetCode 207 | Directed cycle detection (topological) |
| Graph Valid Tree | LeetCode 261 | Undirected cycle detection |
| Redundant Connection | LeetCode 684 | Union-Find cycle detection |
| Find Eventual Safe States | LeetCode 802 | Directed cycle detection (coloring) |
| Detect Cycle in Directed Graph | GeeksforGeeks | DFS recursion-stack |


---

## 8. Topological Sorting

### 8.1 Definition & Why It Exists

A **topological sort** of a DAG is a linear ordering of vertices such that for every directed edge `u -> v`, `u` comes before `v` in the ordering. It only exists for DAGs (no cycles).

**Real-world analogy:** Course prerequisites — you must take "Calculus I" before "Calculus II." A topological sort gives a valid order to take all courses satisfying every prerequisite.

```
Graph:                     Valid Topo Order:
(A)->(B)->(D)              A, C, B, D
  \        ^
   ->(C)---+
```

### 8.2 Method 1 — DFS-Based Topological Sort

**Intuition:** Do a DFS; when a node finishes exploring ALL its descendants, push it onto a stack. Reverse the stack at the end — a node's descendants always finish before it does, so reversing gives the correct order.

```python
def topo_sort_dfs(n, graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)          # push AFTER exploring all descendants

    for v in range(n):
        if v not in visited:
            dfs(v)

    return stack[::-1]              # reverse for correct topological order
```

**Line-by-line explanation:**
- We push a node to `stack` only after recursing into all its neighbors — meaning everything reachable from it is already "settled" (pushed earlier / appears later after reversal).
- Reversing the finished-order stack yields nodes in "must-come-first" order.

**Dry Run** (`A->B, A->C, B->D, C->D`):

| Step | Node | Action | Stack |
|---|---|---|---|
| 1 | A | visit B first | |
| 2 | B | visit D | |
| 3 | D | no neighbors, push D | [D] |
| 4 | B | done, push B | [D, B] |
| 5 | A | visit C | |
| 6 | C | D already visited, push C | [D, B, C] |
| 7 | A | done, push A | [D, B, C, A] |
| — | Reverse | | [A, C, B, D] |

**Complexity:** `O(V + E)` time, `O(V)` space.

> ⚠️ **Common Mistake:** This DFS-based method does NOT detect cycles by itself — you must combine it with the 3-coloring cycle check (Section 7.4) if the input isn't guaranteed to be a DAG.

### 8.3 Method 2 — Kahn's Algorithm (BFS-Based)

**Intuition:** Repeatedly remove nodes with in-degree 0 (no remaining prerequisites), decrementing the in-degree of their neighbors. This naturally produces topological order and detects cycles for free (Section 7.5).

```python
def topo_sort_kahn(n, graph):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([v for v in range(n) if indegree[v] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != n:
        raise ValueError("Graph has a cycle — no valid topological order")
    return order
```

**Dry Run** (`A->B, A->C, B->D, C->D`, indices A=0,B=1,C=2,D=3):

| Step | Queue | Order | Indegree State |
|---|---|---|---|
| 0 | [A] | [] | A:0, B:1, C:1, D:2 |
| 1 | [B,C] | [A] | B:0, C:0, D:2 |
| 2 | [C,D?] | [A,B] | D:1 (from B) |
| 3 | [D] | [A,B,C] | D:0 (from C) |
| 4 | [] | [A,B,C,D] | done |

**Complexity:** `O(V + E)` time, `O(V)` space.

### 8.4 DFS vs Kahn's — Comparison

| Criterion | DFS-based | Kahn's (BFS-based) |
|---|---|---|
| Cycle detection | Needs separate coloring check | Built-in (leftover in-degree > 0) |
| Implementation style | Recursive | Iterative, queue-based |
| Lexicographically smallest order | Harder to control | Easy — use a min-heap instead of queue |
| Preferred in interviews | When recursion is natural | When cycle-check is also required (e.g., Course Schedule) |

> 💡 **Interview Tip:** If a problem asks for topological order AND mentions "if there's a cycle, return an empty array" (like LeetCode 210 "Course Schedule II"), Kahn's algorithm is usually cleaner since it detects cycles as a side effect.

### 8.5 Edge Cases

- Graph with no edges → any permutation of vertices is a valid topological order.
- Multiple valid topological orders can exist — problems either accept any valid one or specify tie-breaking (e.g., smallest lexicographic — use a min-heap in Kahn's).
- Disconnected DAG components → both methods handle this naturally by looping over all vertices.

### 8.6 Common Mistakes

- Forgetting to reverse the stack in the DFS method.
- Not validating `len(order) == n` in Kahn's algorithm before trusting the result — a cyclic graph will silently produce an incomplete order otherwise.
- Confusing in-degree with out-degree when initializing Kahn's algorithm.

### 8.7 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Course Schedule II | LeetCode 210 | Kahn's algorithm |
| Alien Dictionary | LeetCode 269 (Premium) | Build graph + topo sort |
| Sequence Reconstruction | LeetCode 444 | Topo sort uniqueness |
| Minimum Height Trees | LeetCode 310 | Topological "peeling" (leaves) |
| Task Scheduling | GeeksforGeeks | Kahn's algorithm |


---

## 9. Shortest Path Algorithms

### 9.1 Overview — Which Algorithm to Use

| Scenario | Algorithm | Complexity |
|---|---|---|
| Unweighted graph | BFS | O(V+E) |
| Weighted, non-negative edges, single source | Dijkstra | O((V+E) log V) |
| Weighted, negative edges allowed, single source | Bellman-Ford | O(V·E) |
| All-pairs shortest path | Floyd-Warshall | O(V³) |
| Negative edges + all-pairs (sparse) | Johnson's Algorithm | O(V² log V + VE) |
| Heuristic-guided single-target search | A* | O(E) with good heuristic |

### 9.2 BFS Shortest Path (Unweighted Graphs)

Already covered in Section 5.2 — BFS naturally computes shortest path in terms of edge count because it explores level by level.

```python
def bfs_shortest_path(graph, start, target):
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1   # unreachable
```

### 9.3 Dijkstra's Algorithm

**Definition:** Finds shortest paths from a single source to all vertices in a graph with **non-negative** edge weights, using a greedy strategy with a min-heap (priority queue).

**Intuition:** Always expand the closest unvisited vertex next — once a vertex is "finalized" (popped with its true shortest distance), it can never be improved later since all other edge weights are non-negative.

**Real-world analogy:** GPS navigation — always explore the road that currently offers the shortest known travel time first.

**ASCII Visualization:**

```
        4
   (A)-----(B)
    |  \     |
   1|   2\  1|
    |     \ |
   (C)-----(D)
        5

Dijkstra from A:
  dist[A]=0, dist[C]=1 (via A-C), dist[D]=3 (via A-C-D:1+5? or A-D:2)
  Actual shortest: A-D direct edge weight 2 -> dist[D]=2
  dist[B]=3 (via A-D-B: 2+1=3, better than direct A-B:4)
```

```python
import heapq

def dijkstra(graph, start, n):
    """
    graph: dict[node] -> list of (neighbor, weight)
    """
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]            # (distance, node) — heapq is a min-heap by first element
    visited = set()

    while pq:
        d, node = heapq.heappop(pq)   # always pop the SMALLEST known distance
        if node in visited:
            continue                   # stale entry, skip (lazy deletion)
        visited.add(node)

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist
```

**Line-by-line explanation:**
- `dist[]` array tracks the best known distance to each node, initialized to infinity (unreached).
- The min-heap `pq` always gives us the node with smallest tentative distance next — this greedy choice is safe because edge weights are non-negative (no shorter path can appear later through a longer prefix).
- `visited` set implements "lazy deletion" — instead of removing stale heap entries (expensive), we just skip them when popped if already finalized.
- **Relaxation step**: if going through `node` gives a shorter distance to `neighbor` than currently known, update and push the improved distance.

**Dry Run** (`A=0,B=1,C=2,D=3`; edges: A-B:4, A-C:1, A-D:2, C-D:5, D-B:1):

| Step | Popped (dist,node) | dist[] state | pq after |
|---|---|---|---|
| 1 | (0,A) | [0,inf,inf,inf] | [(4,B),(1,C),(2,D)] |
| 2 | (1,C) | [0,inf,1,inf] | [(2,D),(4,B),(6,D via C)] |
| 3 | (2,D) | [0,inf,1,2] | [(3,B via D),(4,B),(6,D)] |
| 4 | (3,B) | [0,3,1,2] | [(4,B) stale, (6,D) stale] |
| 5 | (4,B) stale, skip | [0,3,1,2] | [(6,D) stale] |
| 6 | (6,D) stale, skip | [0,3,1,2] | [] |

Final: `dist = [0, 3, 1, 2]`.

**Time Complexity:** `O((V + E) log V)` with a binary heap. **Space Complexity:** `O(V + E)`.

> ⚠️ **Critical Limitation:** Dijkstra FAILS with negative edge weights — the greedy "finalize smallest distance" assumption breaks because a longer initial path could later be shortened by a negative edge. Use Bellman-Ford instead.

### 9.4 Bellman-Ford Algorithm

**Definition:** Finds shortest paths from a single source, supporting **negative edge weights**, and can detect negative-weight cycles.

**Intuition:** Relax every edge in the graph, `V-1` times. After `V-1` iterations, all shortest paths (which use at most `V-1` edges in a graph with no negative cycles) are guaranteed correct. A `V`-th iteration that still improves a distance indicates a negative cycle.

```python
def bellman_ford(n, edges, start):
    """
    edges: list of (u, v, w)
    """
    dist = [float('inf')] * n
    dist[start] = 0

    for _ in range(n - 1):                  # relax all edges V-1 times
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Nth pass: detect negative cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist
```

**Line-by-line explanation:**
- Each of the `V-1` outer iterations relaxes every edge — after iteration `k`, all shortest paths using at most `k` edges are correctly computed.
- Since the shortest simple path can have at most `V-1` edges, `V-1` full passes guarantee convergence (if no negative cycle exists).
- The extra `V`-th pass checks for further improvement — if any edge can still relax a distance, a negative cycle exists (distances would decrease forever).

**Complexity:** `O(V · E)` time, `O(V)` space — much slower than Dijkstra, but necessary for negative weights.

**Dry Run** (edges: A→B:4, A→C:5, B→C:-3, C→D:2; start A; A=0,B=1,C=2,D=3):

| Pass | dist[A,B,C,D] | Notes |
|---|---|---|
| init | [0,inf,inf,inf] | |
| 1 | [0,4,1,3] | A→B relaxes B=4; A→C relaxes C=5, then B→C relaxes C=1; C→D relaxes D=3 |
| 2 | [0,4,1,3] | no further improvement — converged |

### 9.5 Floyd-Warshall Algorithm (All-Pairs Shortest Path)

**Definition:** Computes shortest paths between **every pair** of vertices using dynamic programming.

**Intuition:** For every pair `(i, j)`, consider whether routing through an intermediate vertex `k` gives a shorter path: `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`, iterating `k` over all vertices.

```python
def floyd_warshall(n, edges):
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)     # handle parallel edges: keep the smaller

    for k in range(n):              # intermediate vertex
        for i in range(n):           # source
            for j in range(n):       # destination
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
```

**Line-by-line explanation:**
- The triple-nested loop tries every vertex `k` as a potential "bridge" between every pair `(i, j)`.
- Crucially, `k` must be the OUTERMOST loop — this ensures that when we consider `k` as an intermediate, `dist[i][k]` and `dist[k][j]` have already been optimized using intermediates `0..k-1`. This is the DP recurrence at the heart of the algorithm.

**Complexity:** `O(V³)` time, `O(V²)` space. Practical only for `V` up to a few hundred/thousand.

> 💡 **Interview Tip:** Floyd-Warshall is preferred when `V` is small (≤ ~500) and you need distances between ALL pairs, not just from one source. Running Dijkstra from every vertex (`O(V·(V+E)logV)`) can sometimes beat Floyd-Warshall on sparse graphs — this is essentially **Johnson's Algorithm** (see 9.7).

### 9.6 A* Search (Overview)

**Definition:** A heuristic-guided variant of Dijkstra for single-source, single-target shortest path. Uses `f(n) = g(n) + h(n)` where `g(n)` is the known cost from start, and `h(n)` is an admissible heuristic (never overestimates true cost) estimating remaining distance to target.

```python
def a_star(graph, start, goal, heuristic):
    pq = [(heuristic(start), 0, start)]     # (f, g, node)
    visited = set()
    while pq:
        f, g, node = heapq.heappop(pq)
        if node == goal:
            return g
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            new_g = g + weight
            heapq.heappush(pq, (new_g + heuristic(neighbor), new_g, neighbor))
    return -1
```

Common in pathfinding for games and robotics, using Euclidean or Manhattan distance as the heuristic on grid maps.

### 9.7 Johnson's Algorithm (Overview)

**Definition:** Computes all-pairs shortest paths for sparse graphs, even with negative edges (no negative cycles), in `O(V² log V + VE)` — faster than Floyd-Warshall for sparse graphs.

**How it works (high level):**
1. Add a virtual vertex connected to all vertices with 0-weight edges.
2. Run Bellman-Ford from the virtual vertex to compute a potential `h(v)` for each vertex.
3. Re-weight every edge: `w'(u,v) = w(u,v) + h(u) - h(v)` — this makes all weights non-negative while preserving shortest paths.
4. Run Dijkstra from every vertex on the re-weighted graph.
5. Convert distances back using the potentials.

### 9.8 Comparison Table

| Algorithm | Handles Negative Weights | Handles Negative Cycles (detect) | Time Complexity | Use Case |
|---|---|---|---|---|
| BFS | N/A (unweighted) | N/A | O(V+E) | Unweighted shortest path |
| Dijkstra | ❌ | ❌ | O((V+E) log V) | Single-source, non-negative weights |
| Bellman-Ford | ✅ | ✅ | O(V·E) | Single-source, negative weights allowed |
| Floyd-Warshall | ✅ | ✅ (diagonal goes negative) | O(V³) | All-pairs, small V |
| Johnson's | ✅ | ✅ (via Bellman-Ford step) | O(V² log V + VE) | All-pairs, sparse graph |
| A* | ❌ (typically) | N/A | O(E) with good heuristic | Single-target with heuristic |

### 9.9 Edge Cases

- Negative edge weight with Dijkstra → silently gives WRONG answer (no error raised) — always verify weight sign before choosing Dijkstra.
- Disconnected graph → unreachable nodes remain at `float('inf')`.
- Self-loops with negative weight → immediately signal a negative cycle if the loop weight is negative.
- Multiple edges between same pair → always keep the minimum weight when initializing.

### 9.10 Common Mistakes

- Using a plain list instead of `heapq` for Dijkstra's priority queue → degrades to `O(V²)` unnecessarily.
- Forgetting the "stale entry" check (`if node in visited: continue`) in Dijkstra → can lead to incorrect results or wasted work.
- Running Dijkstra on graphs with negative weights (common trap in interviews with adversarial test cases).
- In Floyd-Warshall, looping `i, j, k` in the wrong order (must be `k` outermost) — silently produces incorrect results.

### 9.11 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Network Delay Time | LeetCode 743 | Dijkstra |
| Cheapest Flights Within K Stops | LeetCode 787 | Bellman-Ford (bounded) / modified Dijkstra |
| Path With Minimum Effort | LeetCode 1631 | Dijkstra variant (minimax path) |
| Find the City With the Smallest Number of Neighbors | LeetCode 1334 | Floyd-Warshall |
| Negative Weight Cycle | GeeksforGeeks | Bellman-Ford |
| Shortest Path in Binary Matrix | LeetCode 1091 | BFS on grid |


---

## 10. Minimum Spanning Tree (MST)

### 10.1 Definition & Why It Exists

A **Minimum Spanning Tree** of a connected, undirected, weighted graph is a subset of edges that connects all vertices, contains no cycles, and has the minimum possible total edge weight. "Spanning" means it touches every vertex; "tree" means `V-1` edges and no cycles.

**Real-world analogy:** Laying the cheapest possible network of cables to connect a set of cities such that every city is reachable — no redundant (cycle-forming) cables.

```
Graph:                    MST (bold):
   4        8
(A)---(B)------(C)         (A)   (B)------(C)
  \    |   3   /              \    2       /
  2\   |1     /1              2\  1|      /1
    \  |     /                  \  |     /
     (D)---(E)                   (D)   (E)

Total weight before: many edges
MST total weight: 2+1+2+1 = 6 (example)
```

### 10.2 Kruskal's Algorithm

**Intuition:** Greedily pick the smallest-weight edge that doesn't create a cycle, using Union-Find to detect cycles in O(nearly 1) time. Repeat until `V-1` edges are chosen.

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False              # already connected -> would form a cycle
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def kruskal_mst(n, edges):
    """
    edges: list of (weight, u, v)
    """
    edges = sorted(edges)             # sort ALL edges by weight ascending
    dsu = DSU(n)
    mst_weight = 0
    mst_edges = []

    for weight, u, v in edges:
        if dsu.union(u, v):           # only add if it doesn't form a cycle
            mst_weight += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:
                break                  # MST complete

    return mst_weight, mst_edges
```

**Line-by-line explanation:**
- Sorting edges by weight lets us greedily consider the cheapest edges first.
- `DSU.union()` returns `False` if `u` and `v` are already in the same set — adding this edge would form a cycle, so we skip it.
- We stop early once we have `V-1` edges — no more can be added to a spanning tree.

**Dry Run** (edges sorted: (1,D,E),(2,A,D),(2,B,E)... simplified 4 nodes A,B,C,D with edges (1,A,B),(2,B,C),(3,A,C),(4,C,D)):

| Step | Edge (w,u,v) | Union Result | MST So Far | Total Weight |
|---|---|---|---|---|
| 1 | (1,A,B) | union succeeds | {A-B} | 1 |
| 2 | (2,B,C) | union succeeds | {A-B, B-C} | 3 |
| 3 | (3,A,C) | union FAILS (cycle, A&C already connected) | skip | 3 |
| 4 | (4,C,D) | union succeeds | {A-B,B-C,C-D} | 7 |

**Time Complexity:** `O(E log E)` (dominated by sorting). **Space Complexity:** `O(V + E)`.

### 10.3 Prim's Algorithm

**Intuition:** Start from any vertex; greedily grow the MST by always adding the cheapest edge that connects a vertex INSIDE the current tree to a vertex OUTSIDE it. Uses a min-heap, similar to Dijkstra.

```python
def prim_mst(n, graph, start=0):
    """
    graph: dict[node] -> list of (neighbor, weight)
    """
    visited = set([start])
    pq = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(pq)
    mst_weight = 0
    mst_edges = []

    while pq and len(visited) < n:
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue                    # would form a cycle within the tree
        visited.add(v)
        mst_weight += w
        mst_edges.append((u, v, w))
        for neighbor, weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(pq, (weight, v, neighbor))

    return mst_weight, mst_edges
```

**Line-by-line explanation:**
- We start with all edges from `start` pushed to the heap.
- We always pop the smallest-weight edge; if it leads to an already-visited node, skip (cycle avoidance).
- Otherwise, add the node to the tree, add its outgoing edges to the heap for future consideration.

**Time Complexity:** `O(E log V)` with a binary heap. **Space Complexity:** `O(V + E)`.

### 10.4 Kruskal vs Prim — When to Use Which

| Criterion | Kruskal | Prim |
|---|---|---|
| Best for | Sparse graphs (edge list-based) | Dense graphs (adjacency list/matrix-based) |
| Data structure | Union-Find (DSU) | Min-heap |
| Natural representation | Edge list | Adjacency list |
| Grows | Forest → single tree (can add edges anywhere) | Single tree grows outward from a start node |
| Complexity | O(E log E) | O(E log V) |

> 💡 **Interview Tip:** If the input is already given as an edge list (common in MST problems), reach for Kruskal. If given as an adjacency list/matrix and the graph is dense, Prim is often more natural.

### 10.5 Borůvka's Algorithm (Overview)

The oldest MST algorithm (1926). Works in rounds: in each round, every component finds its cheapest outgoing edge and merges via that edge (using Union-Find), all in parallel. Repeats until one component remains. Runs in `O(E log V)` and is notable for being naturally **parallelizable**, making it popular in distributed/parallel MST computation.

### 10.6 Edge Cases

- Disconnected graph → no spanning tree exists for the entire graph; algorithms will produce a **minimum spanning forest** instead (one tree per component).
- Graph with duplicate/parallel edges → keep only the minimum-weight edge between any pair before running Kruskal (though Kruskal handles this naturally via sorting).
- Single vertex → MST is empty (0 edges, 0 weight).
- Negative edge weights → MST algorithms handle negative weights correctly (no special-casing needed, unlike Dijkstra).

### 10.7 Common Mistakes

- Forgetting path compression / union by rank in DSU → degrades Kruskal to near `O(E·V)`.
- Using Prim's algorithm starting from an arbitrary node on a disconnected graph without checking that all vertices got visited.
- Confusing MST (undirected only) with shortest-path tree — an MST minimizes total edge weight, NOT the path from a specific source to every other node; these are generally different trees.

### 10.8 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Min Cost to Connect All Points | LeetCode 1584 | Prim's / Kruskal's |
| Connecting Cities With Minimum Cost | LeetCode 1135 | Kruskal's |
| Optimize Water Distribution | LeetCode 1168 | Kruskal's with virtual source |
| Minimum Spanning Tree | GeeksforGeeks | Kruskal's / Prim's |
| Network Connection (Number of Operations to Connect) | LeetCode 1319 | Union-Find (component counting) |


---

## 11. Disjoint Set Union / Union-Find

### 11.1 Definition & Why It Exists

**Union-Find (Disjoint Set Union / DSU)** is a data structure that efficiently tracks a partition of elements into disjoint (non-overlapping) sets, supporting two operations: `find(x)` (which set does x belong to?) and `union(x, y)` (merge the sets containing x and y).

**Why it exists:** Answering "are these two nodes connected?" via BFS/DFS after every update is `O(V+E)` per query. Union-Find answers both `find` and `union` in **nearly O(1)** amortized time (technically `O(α(n))`, the inverse Ackermann function — effectively constant for all practical input sizes).

### 11.2 Core Operations

```
Make Set: each element starts as its own parent (its own set)
  0  1  2  3  4       parent = [0,1,2,3,4]

Union(0, 1):
  0<-1  (1's root now points to 0)   parent = [0,0,2,3,4]

Union(2, 3):
  parent = [0,0,3,3,4]  (or [0,0,2,2,4] depending on rank/size heuristic)

Find(1): follows 1 -> 0 -> root is 0
```

### 11.3 Full Implementation

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))     # each node is its own parent initially
        self.rank = [0] * n              # tracks approximate tree height
        self.size = [1] * n              # tracks size of each component
        self.count = n                   # number of disjoint components

    def find(self, x):
        """Path compression: flatten the tree during find for future speedups."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_by_rank(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.count -= 1
        return True

    def union_by_size(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        self.count -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

**Line-by-line explanation:**
- `find(x)` recursively follows parent pointers to the root, and **path compression** rewires every visited node directly to the root — future `find` calls on these nodes become O(1).
- `union_by_rank` always attaches the shorter tree under the taller tree's root, keeping tree height logarithmic.
- `union_by_size` is an equivalent heuristic that attaches the smaller set under the larger set's root — both achieve the same amortized complexity.
- `self.count` tracks the number of distinct components — decremented on every successful union.

### 11.4 Why Path Compression + Union by Rank/Size Matters

| Optimization | Without It | With It |
|---|---|---|
| Neither | O(n) per find (degenerate chain) | — |
| Path compression only | O(log n) amortized | — |
| Union by rank/size only | O(log n) per find | — |
| Both combined | — | O(α(n)) ≈ O(1) amortized |

**ASCII: Path Compression Effect**

```
Before find(4):        After find(4):
    0                       0
    |                     / | \ \
    1                    1  2  3  4
    |
    2
    |
    3
    |
    4
```

### 11.5 Dry Run — Cycle Detection Using Union-Find

```python
def has_cycle_via_dsu(n, edges):
    dsu = DSU(n)
    for u, v in edges:
        if not dsu.union_by_rank(u, v):
            return True     # u and v already connected -> adding this edge forms a cycle
    return False
```

| Step | Edge | find(u) | find(v) | Union Result | Cycle? |
|---|---|---|---|---|---|
| 1 | (0,1) | 0 | 1 | success | No |
| 2 | (1,2) | 0 | 2 | success | No |
| 3 | (0,2) | 0 | 0 | FAILS (same root) | **Yes** |

**Complexity:** `O(E · α(V))` ≈ `O(E)` for all practical purposes.

### 11.6 Applications of Union-Find

| Application | How DSU Helps |
|---|---|
| Cycle detection (undirected) | union() fails if already connected |
| Kruskal's MST | Efficiently checks/merges components while sorting edges |
| Number of Connected Components | Count distinct roots after all unions |
| Number of Islands II (dynamic) | Incrementally union newly added land cells |
| Accounts Merge | Union accounts sharing an email |
| Redundant Connection | Find the one edge that creates a cycle |
| Percolation / Network connectivity | Track whether top and bottom rows are connected |

### 11.7 Edge Cases

- Union of an element with itself → should be a no-op (already same root).
- Very large `n` with sparse unions → path compression prevents worst-case linear chains.
- Union-Find does NOT support "un-union" (splitting sets back apart) efficiently — if you need deletions, a different structure (e.g., link-cut trees) is required.

### 11.8 Common Mistakes

- Forgetting path compression → find() degrades toward O(n) for skewed trees.
- Forgetting union by rank/size → same degradation risk.
- Confusing `find(x)` (returns root) with a direct "is-equal" check on `parent[x]` (which only points to the *immediate* parent, not the ultimate root, before compression finishes).
- Off-by-one when initializing `parent = list(range(n))` — must match the graph's indexing (0-indexed vs 1-indexed).

### 11.9 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Number of Provinces | LeetCode 547 | Union-Find over adjacency matrix |
| Redundant Connection | LeetCode 684 | Cycle detection via DSU |
| Accounts Merge | LeetCode 721 | Union-Find over string keys |
| Number of Islands II | LeetCode 305 | Dynamic connectivity |
| Satisfiability of Equality Equations | LeetCode 990 | Union-Find over constraints |
| Most Stones Removed | LeetCode 947 | Union-Find + component counting |


---

## 12. Strongly Connected Components

### 12.1 Definition & Why It Exists

A **Strongly Connected Component (SCC)** of a directed graph is a maximal set of vertices such that every vertex is reachable from every other vertex **within that set**, respecting edge direction.

**Real-world analogy:** A group of web pages that all link to each other (directly or via chains) forms an SCC — you can navigate from any page in the group to any other.

```
Directed Graph:
(A)->(B)->(C)
 ^         |
 +---------+
      (D)->(E)

SCC 1: {A, B, C}   (cycle: A->B->C->A)
SCC 2: {D}
SCC 3: {E}
```

### 12.2 Kosaraju's Algorithm

**Intuition:** Two-pass algorithm using the key insight — reversing all edges preserves SCCs (if u and v are mutually reachable, they remain mutually reachable after reversal).

**Steps:**
1. Run DFS on the original graph, pushing nodes to a stack in order of **finish time** (like topological sort).
2. Reverse all edges (build the transpose graph).
3. Pop nodes from the stack one at a time; for each unvisited node, run DFS on the **transpose** graph — each DFS call discovers exactly one SCC.

```python
def kosaraju_scc(n, graph):
    visited = set()
    stack = []

    def dfs1(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs1(neighbor)
        stack.append(node)          # finish-time ordering

    for v in range(n):
        if v not in visited:
            dfs1(v)

    # Build transpose graph
    transpose = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transpose[v].append(u)

    visited.clear()
    sccs = []

    def dfs2(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in transpose[node]:
            if neighbor not in visited:
                dfs2(neighbor, component)

    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs2(node, component)
            sccs.append(component)

    return sccs
```

**Line-by-line explanation:**
- `dfs1` computes finish-order (same idea as topological sort finish-time push).
- The transpose graph reverses every edge — this is `O(V+E)` to build.
- Processing nodes in **decreasing finish time** and running DFS on the transpose ensures each DFS call is confined to exactly one SCC — this works because the node with the latest finish time in the original graph must be a "source" SCC in the transpose's condensation ordering.

**Complexity:** `O(V + E)` time (two DFS passes + transpose construction), `O(V + E)` space.

### 12.3 Tarjan's Algorithm

**Intuition:** Single-pass DFS using discovery times and "low-link" values. A node is the root of an SCC if its low-link value equals its own discovery time — meaning no ancestor can be reached from its subtree.

```python
def tarjan_scc(n, graph):
    index_counter = [0]
    stack = []
    on_stack = [False] * n
    indices = [-1] * n         # discovery time
    lowlink = [0] * n
    sccs = []

    def strongconnect(node):
        indices[node] = index_counter[0]
        lowlink[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
        on_stack[node] = True

        for neighbor in graph[node]:
            if indices[neighbor] == -1:
                strongconnect(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
            elif on_stack[neighbor]:
                # neighbor is on the stack -> part of the current SCC being built
                lowlink[node] = min(lowlink[node], indices[neighbor])

        if lowlink[node] == indices[node]:      # node is a root of an SCC
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == node:
                    break
            sccs.append(component)

    for v in range(n):
        if indices[v] == -1:
            strongconnect(v)

    return sccs
```

**Line-by-line explanation:**
- `indices[node]` = when this node was first discovered (DFS pre-order number).
- `lowlink[node]` = the smallest discovery index reachable from `node`'s subtree (including back-edges to ancestors still on the stack).
- When we return from recursing into a neighbor, we propagate its `lowlink` up — this tells us if the subtree can "reach back" to an earlier ancestor.
- If `lowlink[node] == indices[node]`, no back-edge escapes this node's subtree — it's the SCC root, so we pop the stack until we get back to `node`, collecting the whole SCC.

**Complexity:** `O(V + E)` time (single DFS pass), `O(V)` space — often preferred over Kosaraju's for being single-pass.

### 12.4 Kosaraju vs Tarjan — Comparison

| Criterion | Kosaraju's | Tarjan's |
|---|---|---|
| Number of DFS passes | 2 (+ transpose build) | 1 |
| Conceptual simplicity | Easier to explain/remember | Requires understanding low-link values |
| Extra structure needed | Transpose graph | Explicit stack + on_stack array |
| Typical interview preference | Good for explaining SCC concept | Preferred for competitive programming (faster constant factor) |

### 12.5 Condensation Graph (Overview)

Contracting each SCC into a single "super-node" produces the **condensation graph**, which is always a DAG. This is useful for problems that ask "what's the minimum number of edges to add to make the whole graph strongly connected" or for running topological sort/DP over SCC groups.

```
Original SCCs: {A,B,C}, {D}, {E}
Condensation:  [ABC] -> [D] -> [E]     (a DAG of super-nodes)
```

### 12.6 Edge Cases

- Every vertex isolated (no edges) → each vertex is its own SCC.
- Fully strongly connected graph → the entire graph is one SCC.
- Self-loops → don't affect SCC membership but should not break implementation (skip trivial self-edges in low-link updates if needed).

### 12.7 Common Mistakes

- Forgetting the `on_stack` check in Tarjan's — using only `indices[neighbor] != -1` instead of also checking `on_stack` incorrectly includes cross-edges to already-finished SCCs.
- Building the transpose graph incorrectly (swapping too many/few edges) in Kosaraju's.
- Processing the stack in the wrong order (must be popped in decreasing finish-time order) in Kosaraju's second pass.

### 12.8 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Strongly Connected Components (Kosaraju) | GeeksforGeeks | Kosaraju's algorithm |
| Critical Connections in a Network | LeetCode 1192 | Tarjan's (bridges, related concept) |
| Number of SCC | Codeforces / CSES | Tarjan's / Kosaraju's |
| Strongly Connected Components | CSES Graph Series | Tarjan's / Kosaraju's |


---

## 13. Bridges & Articulation Points

### 13.1 Definitions

- **Bridge (Cut Edge):** An edge whose removal increases the number of connected components (disconnects the graph).
- **Articulation Point (Cut Vertex):** A vertex whose removal (along with its incident edges) increases the number of connected components.

**Real-world analogy:** In a road network, a bridge is a road that's the ONLY connection between two regions — destroy it and the regions become unreachable from each other. An articulation point is a city that, if it disappeared, would split the remaining road network into disconnected pieces.

```
Graph:
(A)---(B)---(C)---(D)
        |
       (E)

Bridge: (C)-(D) — removing it disconnects D
Articulation Points: B (connects {A} to {C,D,E} branch and to E),
                      C (connects {A,B,E} to {D})
```

### 13.2 Tarjan's Algorithm for Bridges

**Intuition:** Same `low-link` idea as SCC — an edge `(u, v)` (where `v` is a DFS child of `u`) is a bridge if `low[v] > disc[u]`, meaning `v`'s subtree has NO back-edge reaching `u` or any of `u`'s ancestors.

```python
def find_bridges(n, graph):
    disc = [-1] * n
    low = [0] * n
    timer = [0]
    bridges = []

    def dfs(node, parent):
        disc[node] = low[node] = timer[0]
        timer[0] += 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue                       # skip the edge back to immediate parent
            if disc[neighbor] == -1:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > disc[node]:
                    bridges.append((node, neighbor))   # no back-edge escapes -> bridge
            else:
                low[node] = min(low[node], disc[neighbor])   # back-edge

    for v in range(n):
        if disc[v] == -1:
            dfs(v, -1)

    return bridges
```

**Line-by-line explanation:**
- `disc[node]` = discovery time (DFS pre-order index). `low[node]` = smallest discovery time reachable via subtree + back-edges.
- We explicitly skip the edge back to the immediate `parent` (unlike SCC's `on_stack` check) because undirected edges are stored both ways, and we don't want to treat "going back the way we came" as a back-edge.
- If `low[neighbor] > disc[node]` after fully exploring `neighbor`'s subtree, it means nothing in that subtree can reach `node` or higher — so the edge `(node, neighbor)` is critical (a bridge).

**Dry Run** (path graph `A-B-C-D` plus `B-E`):

| Node | disc | low | Bridge Check |
|---|---|---|---|
| A(0) | 0 | 0 | |
| B(1) | 1 | 1 | low[C]=2 > disc[B]=1 -> (B,C) is a bridge; also (A,B) bridge since low[B]=1>disc[A]=0 |
| C(2) | 2 | 2 | low[D]=3 > disc[C]=2 -> (C,D) is a bridge |
| D(3) | 3 | 3 | leaf |
| E(4) | 4 | 4 | low[E]=4 > disc[B]=1 -> (B,E) is a bridge |

**Complexity:** `O(V + E)` time, `O(V)` space.

### 13.3 Tarjan's Algorithm for Articulation Points

**Intuition:** A vertex `u` is an articulation point if:
1. `u` is the DFS root AND has **2 or more children** in the DFS tree, OR
2. `u` is NOT the root AND has some child `v` where `low[v] >= disc[u]` (v's subtree cannot reach above `u`).

```python
def find_articulation_points(n, graph):
    disc = [-1] * n
    low = [0] * n
    timer = [0]
    ap = set()

    def dfs(node, parent):
        disc[node] = low[node] = timer[0]
        timer[0] += 1
        children = 0

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if disc[neighbor] == -1:
                children += 1
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])

                # Case 2: non-root articulation point
                if parent != -1 and low[neighbor] >= disc[node]:
                    ap.add(node)
            else:
                low[node] = min(low[node], disc[neighbor])

        # Case 1: root articulation point
        if parent == -1 and children >= 2:
            ap.add(node)

    for v in range(n):
        if disc[v] == -1:
            dfs(v, -1)

    return ap
```

**Line-by-line explanation:**
- The root condition is special: a root with only one DFS child is never a cut vertex (removing it just leaves one connected subtree); a root with 2+ children means those children's subtrees are only connected through the root.
- The non-root condition `low[neighbor] >= disc[node]` (note: `>=`, not `>` as in bridges) — even a back-edge reaching exactly `node` itself doesn't help `neighbor`'s subtree bypass `node`.

**Complexity:** `O(V + E)` time, `O(V)` space.

### 13.4 Bridges vs Articulation Points — Key Difference

| Aspect | Bridge | Articulation Point |
|---|---|---|
| Removes | An edge | A vertex (and all its edges) |
| Condition | `low[v] > disc[u]` | `low[v] >= disc[u]` (non-root) or 2+ children (root) |
| Effect | Splits graph into exactly 2 components | Can split into 2 or more components |

### 13.5 Edge Cases

- Tree graphs (no cycles) → every single edge is a bridge, and every internal node is an articulation point.
- Fully 2-edge-connected graph (e.g., a simple cycle) → no bridges exist at all.
- Isolated vertex → trivially not an articulation point (no edges to remove).
- Disconnected input → must loop DFS over all unvisited vertices.

### 13.6 Common Mistakes

- Forgetting the special root-case handling for articulation points (using only the general "non-root" rule undercounts articulation points at the root).
- Using `>` instead of `>=` (or vice versa) — swapping the bridge/articulation-point conditions is a very common bug.
- Not skipping the parent edge correctly when there are parallel edges between `node` and `parent` (in multigraphs, you should only skip ONE occurrence of the parent edge, not all edges to the parent).

### 13.7 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Critical Connections in a Network | LeetCode 1192 | Bridges (Tarjan's) |
| Articulation Points | GeeksforGeeks | Tarjan's algorithm |
| Cut Vertices (Articulation Points) | CSES Graph Series | Tarjan's algorithm |
| Bridges in a Graph | CSES Graph Series | Tarjan's algorithm |


---

## 14. Bipartite Graphs

### 14.1 Definition & Why It Exists

A graph is **bipartite** if its vertices can be divided into two disjoint sets `X` and `Y` such that every edge connects a vertex in `X` to a vertex in `Y` (no edge connects two vertices within the same set). Equivalently: **a graph is bipartite if and only if it contains no odd-length cycle.**

**Real-world analogy:** Matching job applicants to jobs, or students to dorm rooms — two distinct groups where connections only go between the groups, never within.

```
Bipartite:                  NOT Bipartite (odd cycle):
Set X:  A   B                    A
         \ / \                  / \
Set Y:    C   D                B---C
                            (triangle = odd cycle -> not bipartite)
```

### 14.2 Checking Bipartiteness — BFS (2-Coloring)

**Intuition:** Try to color the graph using 2 colors such that no two adjacent vertices share a color. If successful, the graph is bipartite; if a conflict arises, it's not.

```python
def is_bipartite_bfs(n, graph):
    color = [-1] * n            # -1 = uncolored

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]   # opposite color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False                         # same color adjacent -> conflict
    return True
```

**Line-by-line explanation:**
- `1 - color[node]` flips between 0 and 1 — assigning the opposite color to each neighbor.
- If we ever find an already-colored neighbor sharing the SAME color as the current node, we have two adjacent same-colored vertices — proof of an odd cycle, hence not bipartite.

**Complexity:** `O(V + E)` time, `O(V)` space.

### 14.3 Checking Bipartiteness — DFS

```python
def is_bipartite_dfs(n, graph):
    color = [-1] * n

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for v in range(n):
        if color[v] == -1:
            if not dfs(v, 0):
                return False
    return True
```

### 14.4 Edge Cases

- Disconnected graph → each component must be checked independently (a graph is bipartite iff ALL its components are bipartite).
- Empty graph → trivially bipartite.
- Self-loop → automatically NOT bipartite (a node can't have a different color from itself).
- Single edge → always bipartite.

### 14.5 Common Mistakes

- Checking only from vertex 0 and ignoring disconnected components.
- Forgetting self-loops make bipartiteness impossible.
- Confusing "no odd cycle" with "no cycle at all" — bipartite graphs CAN have even-length cycles.

### 14.6 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Is Graph Bipartite? | LeetCode 785 | BFS/DFS 2-coloring |
| Possible Bipartition | LeetCode 886 | 2-coloring with constraints |
| Bipartite Graph Check | GeeksforGeeks | BFS/DFS 2-coloring |

---

## 15. Euler Path, Circuit & Hamiltonian Path

### 15.1 Euler Path & Euler Circuit

- **Euler Path:** A walk that visits **every edge exactly once** (vertices may repeat).
- **Euler Circuit:** An Euler path that starts and ends at the same vertex.

**Existence conditions (undirected graph):**
- **Euler Circuit** exists iff the graph is connected AND every vertex has an **even degree**.
- **Euler Path** (not circuit) exists iff the graph is connected AND **exactly 0 or 2** vertices have odd degree (if 2, path must start/end at those vertices).

```
Seven Bridges of Königsberg (historical origin):
Land masses = vertices, bridges = edges.
All 4 land masses had odd degree -> NO Euler path exists (Euler's original proof).
```

### 15.2 Hierholzer's Algorithm (Finding an Euler Circuit)

```python
def find_euler_circuit(n, graph):
    """
    graph: dict[node] -> list of neighbors (as a multiset/list, edges consumed as used)
    """
    graph = {u: list(v) for u, v in graph.items()}   # mutable copy
    stack = [0]
    circuit = []

    while stack:
        node = stack[-1]
        if graph[node]:
            next_node = graph[node].pop()     # consume this edge
            stack.append(next_node)
        else:
            circuit.append(stack.pop())       # dead end -> add to circuit
    return circuit[::-1]
```

**Line-by-line explanation:**
- We greedily walk forward, consuming edges as we use them (removing from the adjacency list).
- When stuck (no more unused edges from the current node), we backtrack and record the node into the circuit.
- Reversing at the end gives the correct Euler circuit order — this is the standard **Hierholzer's algorithm**.

**Complexity:** `O(E)` time (each edge visited/consumed exactly once).

### 15.3 Hamiltonian Path (Overview)

A **Hamiltonian Path** visits every **vertex** exactly once (as opposed to Euler's every-edge-once). Unlike Euler paths, there's no simple degree-based condition for existence — determining if a Hamiltonian path/cycle exists is **NP-complete** in general.

```python
def hamiltonian_path_exists(n, graph):
    """Brute-force backtracking — exponential time, only for small n."""
    visited = [False] * n

    def backtrack(node, count):
        if count == n:
            return True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if backtrack(neighbor, count + 1):
                    return True
                visited[neighbor] = False   # backtrack
        return False

    for start in range(n):
        visited = [False] * n
        visited[start] = True
        if backtrack(start, 1):
            return True
    return False
```

**Complexity:** `O(V!)` worst case — exponential; practical only for very small `V` (≤ ~15-20 with bitmask DP, ≤ ~10 with pure backtracking).

> 💡 **Interview Tip:** Hamiltonian Path problems on LeetCode (e.g., "Traveling Salesman"-style) are usually solved with **bitmask DP** (`O(2^V · V²)`) rather than pure backtracking, since `V` is typically ≤ 20.

### 15.4 Euler vs Hamiltonian — Comparison

| Aspect | Euler Path/Circuit | Hamiltonian Path/Cycle |
|---|---|---|
| Visits every... | Edge exactly once | Vertex exactly once |
| Existence check | O(V) — degree parity rule | NP-complete — no simple rule |
| Algorithm | Hierholzer's — O(E) | Backtracking / Bitmask DP — exponential |

### 15.5 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Reconstruct Itinerary | LeetCode 332 | Hierholzer's algorithm (Euler path) |
| Valid Arrangement of Pairs | LeetCode 2097 | Euler path construction |
| Traveling Salesman Problem | GeeksforGeeks / CSES | Hamiltonian cycle, bitmask DP |
| Shortest Hamiltonian Path | CSES Graph Series | Bitmask DP |

---

## 16. Maximum Flow

### 16.1 Definition & Why It Exists

The **Maximum Flow** problem asks: given a directed graph with edge capacities, a source `s`, and a sink `t`, what is the maximum amount of "flow" that can be pushed from `s` to `t` without exceeding any edge's capacity?

**Real-world analogy:** Water pipes — each pipe (edge) has a maximum flow rate (capacity); find the max water throughput from a reservoir (source) to a city (sink).

```
        10        5
   (S)------(A)------(T)
    |                 |
   5|                 |10
    |        15        |
   (B)----------------(A already shown)

Max flow = limited by the "bottleneck" (minimum cut) along all paths.
```

### 16.2 Ford-Fulkerson Method

**Intuition:** Repeatedly find an **augmenting path** (a path from `s` to `t` with available residual capacity) using DFS/BFS, push flow equal to the path's bottleneck capacity, and update residual capacities (forward edges decrease, reverse/residual edges increase — allowing flow to be "undone" later if beneficial). Repeat until no augmenting path exists.

```python
def ford_fulkerson(n, capacity, s, t):
    """
    capacity: n x n matrix, capacity[u][v] = capacity of edge u->v (0 if none)
    """
    def bfs_find_path():
        parent = [-1] * n
        parent[s] = s
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v in range(n):
                if parent[v] == -1 and capacity[u][v] > 0:
                    parent[v] = u
                    if v == t:
                        return parent
                    queue.append(v)
        return None

    max_flow = 0
    while True:
        parent = bfs_find_path()
        if parent is None:
            break                       # no augmenting path left
        # find bottleneck capacity along the found path
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u
        # update residual capacities
        v = t
        while v != s:
            u = parent[v]
            capacity[u][v] -= path_flow      # reduce forward capacity
            capacity[v][u] += path_flow      # increase residual (reverse) capacity
            v = u
        max_flow += path_flow

    return max_flow
```

**Line-by-line explanation:**
- Using BFS to find augmenting paths (instead of plain DFS) makes this specifically the **Edmonds-Karp** variant — it guarantees polynomial time.
- The residual graph lets flow be "undone": if we push flow along `u->v`, we add capacity to the reverse edge `v->u`, allowing a future augmenting path to effectively cancel part of an earlier suboptimal choice.
- We repeat until BFS can no longer find a path from `s` to `t` in the residual graph — at that point, by the **max-flow min-cut theorem**, the flow found equals the minimum cut capacity.

**Complexity:**
- **Ford-Fulkerson** (generic, DFS-based): `O(E · max_flow)` — can be slow if capacities are large integers (not polynomial in graph size alone).
- **Edmonds-Karp** (BFS-based, shown above): `O(V · E²)` — polynomial, since BFS always finds the shortest augmenting path.

### 16.3 Dinic's Algorithm (Overview)

**Definition:** An improvement over Edmonds-Karp using **level graphs** (BFS to assign levels) and **blocking flows** (DFS to push flow along multiple augmenting paths per phase). Runs in `O(V² · E)` generally, and `O(E · √V)` for unit-capacity graphs (e.g., bipartite matching).

**High-level steps:**
1. Build a level graph via BFS from `s` (only keep edges going from level `i` to level `i+1`).
2. Find a blocking flow in the level graph via DFS (push flow along multiple paths until no more augmenting paths exist at this level structure).
3. Repeat until `t` is unreachable in the level graph.

### 16.4 Max-Flow Min-Cut Theorem

The maximum flow from `s` to `t` equals the capacity of the **minimum cut** — the smallest total capacity of edges that, if removed, would disconnect `s` from `t`. This duality is why max-flow algorithms can also solve minimum-cut problems directly.

### 16.5 Comparison Table

| Algorithm | Path-Finding Method | Complexity | Notes |
|---|---|---|---|
| Ford-Fulkerson (generic) | DFS | O(E · max_flow) | Can be slow for large capacities |
| Edmonds-Karp | BFS | O(V · E²) | Polynomial, simple to implement |
| Dinic's | BFS (levels) + DFS (blocking flow) | O(V² · E) | Faster in practice, standard for competitive programming |

### 16.6 Edge Cases

- No path from `s` to `t` at all → max flow = 0.
- `s == t` → undefined/trivial, typically handled as a special case returning 0 or infinity depending on problem convention.
- Parallel edges → sum capacities or keep them as separate edges in the residual graph, depending on implementation choice.

### 16.7 Common Mistakes

- Forgetting to add/update the **residual (reverse) edge** — without it, the algorithm cannot "undo" a suboptimal flow choice and may get stuck at a suboptimal max flow.
- Using plain DFS (not BFS) for path-finding without realizing generic Ford-Fulkerson can degrade badly on graphs with large integer capacities.
- Not distinguishing between "capacity" and "flow" — capacity is fixed, flow is what's being computed/updated.

### 16.8 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Maximum Flow | CSES Graph Series | Edmonds-Karp / Dinic's |
| Network Flow | GeeksforGeeks | Ford-Fulkerson |
| Maximum Bipartite Matching | GeeksforGeeks | Max flow reduction |
| Downloading Videos | CSES | Max flow modeling |
| Police Chase / Min Cut | CSES | Max-flow min-cut |


---

## 17. Advanced Graph Concepts

### 17.1 Transitive Closure

**Definition:** For every pair `(u, v)`, determine whether `v` is reachable from `u` (not the shortest distance — just reachability, true/false).

```python
def transitive_closure(n, graph):
    reach = [[False] * n for _ in range(n)]
    for i in range(n):
        reach[i][i] = True
    for u in graph:
        for v in graph[u]:
            reach[u][v] = True

    for k in range(n):              # Floyd-Warshall style DP
        for i in range(n):
            for j in range(n):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = True
    return reach
```

**Complexity:** `O(V³)` — same structural pattern as Floyd-Warshall, just with boolean OR/AND instead of min/sum.

### 17.2 Graph Coloring (Overview)

**Definition:** Assign colors to vertices such that no two adjacent vertices share a color, using the minimum number of colors (the **chromatic number**).

- Bipartite check (Section 14) is exactly 2-coloring.
- General graph coloring (with `k > 2` colors) is **NP-hard**; typically solved via backtracking for small graphs or greedy heuristics for large ones.

```python
def greedy_coloring(n, graph):
    colors = [-1] * n
    for node in range(n):
        used = {colors[neighbor] for neighbor in graph[node] if colors[neighbor] != -1}
        color = 0
        while color in used:
            color += 1
        colors[node] = color
    return colors
```

> ⚠️ **Note:** Greedy coloring does NOT guarantee the minimum number of colors — it guarantees a valid coloring using at most `Δ+1` colors, where `Δ` is the maximum degree.

### 17.3 Lowest Common Ancestor — Graph/Tree Perspective (Overview)

In a tree (a special connected acyclic graph), the **LCA** of two nodes `u, v` is the deepest node that is an ancestor of both. Common approaches: binary lifting (`O(log V)` per query after `O(V log V)` preprocessing), Euler tour + sparse table (`O(1)` per query), or DSU-based offline (Tarjan's offline LCA).

### 17.4 Binary Lifting (Overview)

**Definition:** A technique to answer "who is the 2^k-th ancestor of node v?" in `O(log V)` by precomputing ancestors at powers of 2.

```python
def build_binary_lifting(n, parent, LOG=20):
    up = [[0] * n for _ in range(LOG)]
    up[0] = parent[:]                      # 2^0 = direct parent
    for k in range(1, LOG):
        for v in range(n):
            up[k][v] = up[k-1][up[k-1][v]]  # jump 2^(k-1), then another 2^(k-1)
    return up
```

Used heavily for LCA queries, ancestor queries, and jump-pointer techniques in trees.

### 17.5 Condensation Graph — Revisited

As introduced in Section 12.5, contracting each SCC to a single node produces a DAG. This is a critical technique for problems requiring DP over strongly connected components, or determining the minimum edges needed to make a graph strongly connected (count of source SCCs with in-degree 0 in the condensation graph, matched against sink SCCs with out-degree 0).

### 17.6 Matching (Overview)

**Definition:** A matching is a set of edges with no shared vertices. **Maximum bipartite matching** can be solved via:
- Reduction to max-flow (add source connected to all left-side nodes, sink connected from all right-side nodes, capacity 1 on all edges).
- The **Hopcroft-Karp algorithm**, which runs in `O(E√V)` — faster than a naive augmenting-path approach for bipartite matching.

```
Left:  A   B          Matching: A-1, B-2
        \ / \
Right:  1   2
```

### 17.7 Summary Table — Advanced Concepts

| Concept | Complexity | Use Case |
|---|---|---|
| Transitive Closure | O(V³) | Reachability queries |
| Graph Coloring (greedy) | O(V+E) | Register allocation, scheduling |
| Binary Lifting | O(V log V) preprocess, O(log V) query | LCA, ancestor jumps |
| Condensation Graph | O(V+E) | DP over SCCs |
| Bipartite Matching (max flow) | O(E√V) with Hopcroft-Karp | Job assignment, scheduling |

---

## 18. Graph Patterns for Interviews

Recognizing which **pattern** a problem belongs to is often more valuable than memorizing individual algorithms. Below are the recurring templates.

### 18.1 The Big Patterns

| Pattern | Signal Phrases | Core Technique |
|---|---|---|
| **DFS Pattern** | "explore all paths," "connectivity," "backtracking" | Recursive/iterative DFS |
| **BFS Pattern** | "shortest," "minimum steps," "levels" | Queue-based BFS |
| **Topological Sort Pattern** | "order," "prerequisite," "dependency," "schedule" | Kahn's / DFS-based topo sort |
| **Union-Find Pattern** | "connected," "group," "merge," "redundant," "dynamic connectivity" | DSU with path compression |
| **Shortest Path Pattern** | "minimum cost," "cheapest," "weighted distance" | Dijkstra / Bellman-Ford |
| **MST Pattern** | "connect all," "minimum total cost network" | Kruskal's / Prim's |
| **Cycle Detection Pattern** | "valid tree," "can finish all courses," "redundant edge" | DFS coloring / Union-Find |
| **Grid Problems** | "matrix," "islands," "maze," "rooms" | BFS/DFS on implicit grid graph |
| **Multi-source BFS** | "nearest X to every cell," "rotting," "distance to closest" | BFS seeded with multiple sources |
| **State-Space Search** | "minimum moves," "puzzle," "transform word/state" | BFS/DFS/Dijkstra over abstract states |
| **Implicit Graphs** | No explicit graph given — build one from rules | Model relationships as a graph first |
| **Graph Coloring** | "assign categories," "no two adjacent same" | 2-coloring / greedy coloring |

### 18.2 Implicit Graph Construction (Very Common Trap)

Many problems don't hand you a graph — you must recognize the hidden graph structure:

- **Word Ladder** (LeetCode 127): words are vertices, edges connect words differing by 1 letter → BFS for shortest transformation.
- **Sliding Puzzle** (LeetCode 773): each board configuration is a vertex, edges connect configurations one move apart → BFS.
- **Jump Game** style problems: array indices are vertices, edges represent valid jumps.

```python
# Example: Word Ladder — implicit graph via letter substitution
def word_ladder_length(begin_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    return 0
```

> 💡 **Interview Tip:** The single most valuable skill for graph interviews is spotting an **implicit graph** in a problem that doesn't mention "graph" at all. Ask yourself: "What are the states/entities?" (vertices) and "What legal transitions exist between them?" (edges).

### 18.3 Pattern Decision Flow

```
Does the problem mention explicit nodes/edges?
 ├── No -> Can you model states as nodes and valid moves as edges?
 │         └── Yes -> Implicit graph -> usually BFS (shortest) or DFS (all paths)
 └── Yes -> What's being asked?
           ├── "Shortest/minimum steps" (unweighted) -> BFS
           ├── "Shortest/minimum cost" (weighted, non-negative) -> Dijkstra
           ├── "Shortest cost" (negative weights possible) -> Bellman-Ford
           ├── "Valid order / dependency" -> Topological Sort
           ├── "Cycle exists?" -> DFS coloring (directed) / Union-Find (undirected)
           ├── "Connect all with min cost" -> MST (Kruskal/Prim)
           ├── "Are these connected / same group?" -> Union-Find
           ├── "All pairs shortest path" -> Floyd-Warshall
           └── "Two-group split possible?" -> Bipartite check
```


---

## 19. Problem Recognition — Decision Trees

### 19.1 DFS vs BFS Decision Tree

```
Need shortest path / minimum steps (unweighted)?
 ├── Yes -> BFS
 └── No
     Need to explore ALL paths / do backtracking?
      ├── Yes -> DFS
      └── No
          Need connectivity / component labeling only?
           ├── Yes -> Either DFS or BFS (pick based on comfort)
           └── No -> Reconsider problem — likely needs a specific algorithm below
```

### 19.2 Dijkstra vs Bellman-Ford Decision Tree

```
Are there negative edge weights?
 ├── Yes -> Bellman-Ford (or Johnson's for all-pairs)
 └── No
     Do you need all-pairs shortest paths?
      ├── Yes, and V is small (≤ ~500) -> Floyd-Warshall
      ├── Yes, and graph is sparse/large -> Run Dijkstra from every vertex
      └── No (single source) -> Dijkstra
```

### 19.3 Kruskal vs Prim Decision Tree

```
Is the input given as an edge list?
 ├── Yes -> Kruskal's (sort + Union-Find)
 └── No, given as adjacency list/matrix
     Is the graph dense?
      ├── Yes -> Prim's (min-heap growth from a node)
      └── No -> Either works; Kruskal's often simpler to reason about
```

### 19.4 Union-Find Recognition Clues

Look for phrases: "connected," "same group," "merge accounts," "redundant edge," "dynamic connectivity" (edges added over time), "number of provinces/islands," "minimum edges to remove/add for connectivity."

### 19.5 Topological Sort Recognition Clues

Look for phrases: "prerequisite," "must come before," "build order," "task scheduling," "course schedule," "valid sequence," "dependency resolution."

### 19.6 Grid → Graph Conversion Checklist

1. Each cell `(r, c)` is a vertex.
2. Neighbors are computed on the fly using direction vectors — no explicit adjacency list needed.
3. Boundary checks (`0 <= r < rows`, `0 <= c < cols`) replace explicit edge existence checks.
4. A `visited` 2D array (or in-place mutation) replaces the `visited` set used for regular graphs.

```python
DIRECTIONS_4 = [(-1,0),(1,0),(0,-1),(0,1)]
DIRECTIONS_8 = DIRECTIONS_4 + [(-1,-1),(-1,1),(1,-1),(1,1)]
```

### 19.7 Full Master Decision Tree

```
START: Read the problem carefully.
 |
 ├── Mentions matrix/grid? -> Treat cells as implicit graph vertices
 |
 ├── Asks for shortest/minimum steps?
 |     ├── Unweighted -> BFS
 |     └── Weighted -> Dijkstra (non-negative) / Bellman-Ford (negative)
 |
 ├── Asks about connectivity/grouping? -> Union-Find or DFS/BFS component labeling
 |
 ├── Asks for a valid order/sequence with dependencies? -> Topological Sort
 |
 ├── Asks to detect a cycle? -> DFS coloring (directed) / Union-Find (undirected)
 |
 ├── Asks to connect everything at minimum cost? -> MST (Kruskal/Prim)
 |
 ├── Asks if two groups can be split with no internal conflict? -> Bipartite check
 |
 ├── Asks about "flow," "capacity," "maximum throughput"? -> Max Flow (Ford-Fulkerson/Dinic's)
 |
 └── No explicit graph mentioned at all? -> Model states as vertices, transitions as edges
       (implicit graph — then re-enter this decision tree)
```

---

## 20. Optimization Guide

### 20.1 Brute Force → Optimized Graph Thinking

| Naive Approach | Optimized Graph Approach |
|---|---|
| Re-run BFS/DFS from every node for every query | Precompute components once via Union-Find or single traversal |
| Try all permutations for shortest path | Dijkstra / BFS — greedy or layered exploration |
| Nested loops checking all pairs for connectivity | Union-Find — O(α(n)) per check |
| Recomputing shortest paths for each new query | Floyd-Warshall precompute (all-pairs) if V is small |
| DFS-based cycle check repeated on every edge addition | Union-Find incremental cycle check |

### 20.2 Adjacency List vs Matrix — Optimization Impact

| Graph Density | Better Choice | Why |
|---|---|---|
| Sparse (E ≈ V) | Adjacency List | O(V+E) space vs O(V²) |
| Dense (E ≈ V²) | Adjacency Matrix | O(1) edge lookup matters more than space |
| Need O(1) edge existence check | Adjacency Matrix (or a `set` per node) | Direct indexing |
| Need to iterate all edges once | Edge List | Avoids redundant iteration over empty entries |

### 20.3 Heap Optimization (Dijkstra/Prim)

- Naive Dijkstra without a heap: `O(V²)` — fine for dense small graphs.
- With a binary heap (`heapq`): `O((V+E) log V)` — better for sparse graphs.
- With a Fibonacci heap (theoretical): `O(E + V log V)` — rarely implemented in practice due to complexity/overhead, but relevant in complexity-theory discussions.

### 20.4 Path Compression & Union by Rank/Size

Already detailed in Section 11.4 — combined, they bring Union-Find operations down to `O(α(n))`, effectively constant.

### 20.5 Time Optimization Checklist

- Avoid recomputing `len(graph[node])` inside loops — cache it if used repeatedly.
- Use `deque` instead of `list` for BFS queues (`list.pop(0)` is O(n); `deque.popleft()` is O(1)).
- Use `sys.setrecursionlimit()` cautiously for deep DFS, or convert to iterative to avoid Python's recursion overhead entirely.
- Precompute in-degree/out-degree arrays once rather than recalculating inside loops.

### 20.6 Space Optimization Checklist

- Use adjacency list instead of matrix for sparse graphs.
- For grid problems, mutate the grid in-place (if allowed) instead of allocating a separate `visited` matrix.
- Use bitmasks instead of sets for small vertex counts (`V ≤ 20`) in Hamiltonian/TSP-style DP.


---

## 21. Python Tips for Graph Problems

### 21.1 `collections.deque`

Always use `deque` for BFS queues — `list.pop(0)` is `O(n)`, while `deque.popleft()` is `O(1)`.

```python
from collections import deque
queue = deque([start])
queue.append(x)       # O(1)
queue.popleft()        # O(1)
```

### 21.2 `heapq`

Python's built-in min-heap — essential for Dijkstra, Prim's, and A*.

```python
import heapq
heap = []
heapq.heappush(heap, (distance, node))
dist, node = heapq.heappop(heap)     # always the smallest tuple (by distance first)
```

> 💡 To simulate a max-heap, push negated values: `heapq.heappush(heap, (-value, node))`.

### 21.3 `defaultdict`

Avoids manual key-existence checks when building adjacency lists.

```python
from collections import defaultdict
graph = defaultdict(list)
graph[0].append(1)     # no KeyError even though graph[0] didn't exist before
```

### 21.4 `set` for Visited Tracking

Sets give `O(1)` average membership checks — always prefer `set` over `list` for `visited`.

```python
visited = set()
if node not in visited:   # O(1) average
    visited.add(node)
```

### 21.5 Recursion Tips

```python
import sys
sys.setrecursionlimit(10**6)   # increase for deep DFS recursion (use cautiously)
```

For very deep graphs (chains of thousands of nodes), prefer **iterative** DFS to avoid `RecursionError` entirely — Python doesn't optimize tail recursion.

### 21.6 `itertools` for Graph Generation/Combinatorics

```python
from itertools import combinations
all_possible_edges = list(combinations(range(n), 2))   # useful for complete-graph generation, testing
```

### 21.7 `dataclass` for Cleaner Graph Node Representations

```python
from dataclasses import dataclass, field

@dataclass
class GraphNode:
    val: int
    neighbors: list = field(default_factory=list)
```

Useful when problems give you an explicit `Node` class (e.g., LeetCode's "Clone Graph").

### 21.8 Performance & Memory Tips

- Prefer `array` module or plain lists over `numpy` for small/medium graphs — `numpy` overhead isn't worth it unless doing heavy matrix math (e.g., Floyd-Warshall on very large V).
- Use tuple `(u, v)` or `(u, v, w)` for edges — tuples are hashable and memory-efficient compared to lists.
- For adjacency matrices, use `float('inf')` consistently for "no edge," not `-1` or `0` (which could be confused with a valid zero-weight edge).

### 21.9 Common Python Pitfalls

| Pitfall | Fix |
|---|---|
| Using `list.pop(0)` for BFS queue | Use `deque.popleft()` |
| Mutable default argument (`def f(visited=set())`) | Use `None` default, initialize inside function |
| Modifying a list while iterating over it | Iterate over a copy, or collect changes and apply after |
| Confusing `graph[node]` (list) vs `graph.get(node, [])` when node might not exist | Use `defaultdict` or explicit `.get()` |
| Shallow-copying nested lists (`matrix = [[0]*n]*n`) | Use `[[0]*n for _ in range(n)]` — list multiplication shares references! |

> ⚠️ **Critical Gotcha:** `matrix = [[0] * n] * n` creates `n` references to the **SAME** inner list — mutating one row mutates all rows! Always use a list comprehension: `[[0] * n for _ in range(n)]`.

---

## 22. Common Mistakes

| Mistake Category | Description | Fix |
|---|---|---|
| **Visited array errors** | Marking visited at the wrong time (pop vs push in BFS) | Mark visited at enqueue time for BFS |
| **Directed vs Undirected confusion** | Applying undirected cycle logic to directed graphs | Use coloring (GRAY/BLACK) for directed cycle detection |
| **Parent tracking mistakes** | Forgetting to pass/check parent in undirected cycle detection | Always pass `parent` explicitly in DFS calls |
| **Wrong graph representation** | Using adjacency matrix for huge sparse graphs → memory error | Use adjacency list for sparse graphs |
| **Infinite traversal** | Missing or improperly-scoped `visited` check | Ensure `visited` persists correctly across recursive calls |
| **Cycle detection bugs** | Using `>` vs `>=` incorrectly in bridge/articulation logic | Bridges: `low[v] > disc[u]`; Articulation: `low[v] >= disc[u]` |
| **Heap misuse** | Using a list instead of `heapq`, or forgetting to check stale entries | Always use `heapq` + lazy deletion pattern |
| **Union-Find mistakes** | Forgetting path compression or union by rank/size | Always implement both optimizations together |
| **Off-by-one indexing** | Mixing 0-indexed and 1-indexed vertices | Normalize all inputs to a single indexing scheme at the start |
| **Disconnected graph oversight** | Only running BFS/DFS from a single starting vertex | Loop over ALL vertices, skip already-visited ones |
| **Shallow list copy bug** | `[[0]*n]*n` shares row references | Use list comprehension for 2D array initialization |
| **Negative weights with Dijkstra** | Silently wrong answers, no error thrown | Check for negative weights; switch to Bellman-Ford if present |


---

## 23. Cheat Sheets

### 23.1 Graph Representation Cheat Sheet

```python
# Adjacency List (most common)
from collections import defaultdict
graph = defaultdict(list)
graph[u].append(v)          # unweighted
graph[u].append((v, w))     # weighted

# Adjacency Matrix
matrix = [[0]*n for _ in range(n)]
matrix[u][v] = 1            # or weight

# Edge List
edges = [(u, v, w), ...]
```

### 23.2 Traversal Templates

```python
# DFS (recursive)
def dfs(node, visited):
    visited.add(node)
    for nbr in graph[node]:
        if nbr not in visited:
            dfs(nbr, visited)

# BFS
def bfs(start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
```

### 23.3 Shortest Path Guide

| Need | Algorithm | Template Complexity |
|---|---|---|
| Unweighted shortest path | BFS | O(V+E) |
| Weighted, non-negative | Dijkstra | O((V+E)logV) |
| Weighted, negative edges | Bellman-Ford | O(VE) |
| All-pairs, small V | Floyd-Warshall | O(V³) |

### 23.4 MST Guide

| Input Format | Algorithm |
|---|---|
| Edge list | Kruskal's + DSU |
| Adjacency list, dense graph | Prim's + heap |

### 23.5 Union-Find Template

```python
parent = list(range(n))
rank = [0]*n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return False
    if rank[rx] < rank[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    if rank[rx] == rank[ry]:
        rank[rx] += 1
    return True
```

### 23.6 Complexity Master Table

| Algorithm | Time | Space |
|---|---|---|
| DFS / BFS | O(V+E) | O(V) |
| Cycle Detection (any) | O(V+E) | O(V) |
| Topological Sort (both methods) | O(V+E) | O(V) |
| Dijkstra (heap) | O((V+E)logV) | O(V+E) |
| Bellman-Ford | O(V·E) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| Kruskal's MST | O(E log E) | O(V+E) |
| Prim's MST | O(E log V) | O(V+E) |
| Union-Find (per op) | O(α(V)) ≈ O(1) | O(V) |
| Kosaraju's / Tarjan's SCC | O(V+E) | O(V+E) |
| Bridges / Articulation Points | O(V+E) | O(V) |
| Bipartite Check | O(V+E) | O(V) |
| Ford-Fulkerson / Edmonds-Karp | O(E·max_flow) / O(V·E²) | O(V²) |
| Dinic's Max Flow | O(V²·E) | O(V+E) |

### 23.7 Pattern Recognition Quick Reference

```
"shortest path, unweighted"        -> BFS
"shortest path, weighted, +ve"     -> Dijkstra
"shortest path, weighted, -ve"     -> Bellman-Ford
"all pairs shortest path"          -> Floyd-Warshall
"minimum cost to connect all"      -> MST (Kruskal/Prim)
"are these connected / same group" -> Union-Find
"valid order / prerequisite"       -> Topological Sort
"detect cycle"                     -> DFS coloring (directed) / Union-Find (undirected)
"critical edge/node"               -> Bridges / Articulation Points
"two-group split"                  -> Bipartite Check
"strongly connected groups"        -> Kosaraju's / Tarjan's SCC
"maximum flow / capacity"          -> Ford-Fulkerson / Dinic's
"visit every edge once"            -> Euler Path (Hierholzer's)
"visit every vertex once"          -> Hamiltonian Path (backtracking/bitmask DP)
```

### 23.8 Python Syntax Quick Reference

```python
from collections import deque, defaultdict
import heapq

deque([1,2,3])            # O(1) append/pop from both ends
heapq.heappush(h, item)    # min-heap push
heapq.heappop(h)           # min-heap pop
defaultdict(list)          # auto-initializing dict
sorted(edges)              # sort by first tuple element (weight) by default
```

---

## 24. Practice Problem Bank

### 24.1 Basics & Representation

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Find the Town Judge | LeetCode 997 | Easy | In-degree/out-degree |
| Clone Graph | LeetCode 133 | Medium | DFS/BFS + hashmap |
| All Paths From Source to Target | LeetCode 797 | Medium | DFS backtracking |

### 24.2 DFS Pattern

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Number of Provinces | LeetCode 547 | Medium | DFS components |
| Keys and Rooms | LeetCode 841 | Medium | DFS reachability |
| Pacific Atlantic Water Flow | LeetCode 417 | Medium | Multi-source DFS |

### 24.3 BFS Pattern

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Rotting Oranges | LeetCode 994 | Medium | Multi-source BFS |
| Word Ladder | LeetCode 127 | Hard | Implicit graph BFS |
| Open the Lock | LeetCode 752 | Medium | State-space BFS |
| Shortest Bridge | LeetCode 934 | Medium | BFS + flood fill |

### 24.4 Grid Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Number of Islands | LeetCode 200 | Medium | Grid flood fill |
| Surrounded Regions | LeetCode 130 | Medium | Boundary DFS/BFS |
| Walls and Gates | LeetCode 286 | Medium | Multi-source BFS |
| Max Area of Island | LeetCode 695 | Medium | Flood fill + size |

### 24.5 Cycle Detection

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Course Schedule | LeetCode 207 | Medium | Directed cycle (topo) |
| Graph Valid Tree | LeetCode 261 | Medium | Undirected cycle |
| Redundant Connection | LeetCode 684 | Medium | Union-Find |
| Find Eventual Safe States | LeetCode 802 | Medium | DFS coloring |

### 24.6 Topological Sort

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Course Schedule II | LeetCode 210 | Medium | Kahn's algorithm |
| Alien Dictionary | LeetCode 269 | Hard | Build graph + topo sort |
| Minimum Height Trees | LeetCode 310 | Medium | Leaf-peeling topo variant |
| Sequence Reconstruction | LeetCode 444 | Medium | Topo sort uniqueness |

### 24.7 Shortest Path

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Network Delay Time | LeetCode 743 | Medium | Dijkstra |
| Cheapest Flights Within K Stops | LeetCode 787 | Medium | Bellman-Ford (bounded) |
| Path With Minimum Effort | LeetCode 1631 | Medium | Modified Dijkstra |
| Find City With Smallest Number of Neighbors | LeetCode 1334 | Medium | Floyd-Warshall |
| Swim in Rising Water | LeetCode 778 | Hard | Dijkstra / binary search + BFS |

### 24.8 MST

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Min Cost to Connect All Points | LeetCode 1584 | Medium | Prim's / Kruskal's |
| Connecting Cities With Minimum Cost | LeetCode 1135 | Medium | Kruskal's |
| Optimize Water Distribution | LeetCode 1168 | Hard | Kruskal's + virtual node |

### 24.9 Union-Find

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Number of Provinces | LeetCode 547 | Medium | Union-Find |
| Accounts Merge | LeetCode 721 | Medium | Union-Find over strings |
| Number of Islands II | LeetCode 305 | Hard | Dynamic connectivity |
| Satisfiability of Equality Equations | LeetCode 990 | Medium | Union-Find constraints |
| Most Stones Removed | LeetCode 947 | Medium | Union-Find components |

### 24.10 SCC

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Strongly Connected Components | GeeksforGeeks | Medium | Kosaraju's / Tarjan's |
| Strongly Connected Components | CSES Graph Series | Medium | Tarjan's |
| Critical Connections in a Network | LeetCode 1192 | Hard | Tarjan's (bridges) |

### 24.11 Bridges & Articulation Points

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Critical Connections in a Network | LeetCode 1192 | Hard | Bridges |
| Articulation Points | GeeksforGeeks | Hard | Tarjan's |
| Cut Vertices | CSES Graph Series | Hard | Tarjan's |
| Bridges | CSES Graph Series | Hard | Tarjan's |

### 24.12 Bipartite

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Is Graph Bipartite? | LeetCode 785 | Medium | 2-coloring |
| Possible Bipartition | LeetCode 886 | Medium | 2-coloring with constraints |

### 24.13 Network Flow

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Maximum Flow | CSES Graph Series | Hard | Edmonds-Karp / Dinic's |
| Maximum Bipartite Matching | GeeksforGeeks | Hard | Max flow reduction |
| Police Chase | CSES Graph Series | Hard | Min cut |

### 24.14 Advanced / Miscellaneous

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Reconstruct Itinerary | LeetCode 332 | Hard | Euler path (Hierholzer's) |
| Shortest Hamiltonian Path | CSES Graph Series | Hard | Bitmask DP |
| Word Ladder II | LeetCode 126 | Hard | BFS + path reconstruction |
| Evaluate Division | LeetCode 399 | Medium | Weighted graph + DFS/BFS |
| Bus Routes | LeetCode 815 | Hard | BFS over implicit graph |

> 💡 **Company-Wise Note:** Graph problems (especially BFS/DFS, Union-Find, Dijkstra, and topological sort) are heavily featured at Google, Amazon, Meta, Microsoft, and Bloomberg. Grid-based BFS/DFS and Union-Find questions are especially common in OA (online assessment) rounds across most product-based companies including Indian service/product firms like Flipkart, Razorpay, and Zoho.


---

## 25. Final Revision & Roadmap

### 25.1 One-Page Summary

```
GRAPH REPRESENTATIONS:  Adjacency List (default) | Matrix (dense/O(1) lookup) | Edge List (Kruskal/Bellman-Ford)
TRAVERSAL:              DFS (deep/backtrack) | BFS (shortest/levels)
COMPONENTS:             DFS/BFS loop over all vertices | Union-Find (dynamic)
CYCLE DETECTION:        Undirected: parent-tracking DFS or Union-Find
                        Directed: 3-coloring DFS or Kahn's leftover check
TOPOLOGICAL SORT:       DFS finish-time + reverse | Kahn's (BFS + in-degree)
SHORTEST PATH:          BFS (unweighted) | Dijkstra (+ve weights) | Bellman-Ford (-ve weights)
                        Floyd-Warshall (all-pairs, small V)
MST:                    Kruskal's (edge list + DSU) | Prim's (adjacency + heap)
UNION-FIND:             Path compression + union by rank/size => O(α(n))
SCC:                    Kosaraju's (2-pass + transpose) | Tarjan's (1-pass, low-link)
BRIDGES/AP:             Tarjan's low-link: bridge if low[v]>disc[u]; AP if low[v]>=disc[u] (non-root)
BIPARTITE:              2-coloring via BFS/DFS
EULER PATH:             Hierholzer's algorithm, O(E)
MAX FLOW:               Ford-Fulkerson/Edmonds-Karp (BFS augmenting paths) | Dinic's (levels+blocking flow)
```

### 25.2 Algorithm Selection Mind Map

```
                              GRAPH PROBLEM
                                    |
      +----------------+-----------+-----------+------------------+
      |                |                       |                  |
  TRAVERSAL      CONNECTIVITY            ORDERING          OPTIMIZATION
      |                |                       |                  |
  DFS / BFS      Union-Find /            Topological       Shortest Path /
                 Components DFS              Sort            MST / Flow
                                                                    |
                                                    +---------------+---------------+
                                                    |               |               |
                                              Single-Source    All-Pairs      Connect-All
                                              (BFS/Dijkstra/   (Floyd-        (Kruskal's/
                                               Bellman-Ford)    Warshall)      Prim's)
```

### 25.3 15-Minute Rapid Revision

1. **Representations**: adjacency list (default), matrix (dense), edge list (Kruskal/Bellman-Ford).
2. **DFS/BFS**: know both recursive & iterative DFS; BFS uses `deque` + visited-at-enqueue.
3. **Cycle detection**: parent-check (undirected) vs coloring (directed).
4. **Topo sort**: Kahn's for cycle-aware ordering; DFS+reverse-stack otherwise.
5. **Shortest path**: BFS < Dijkstra < Bellman-Ford < Floyd-Warshall, by weight complexity.
6. **MST**: Kruskal's (sort+DSU) vs Prim's (heap growth).
7. **Union-Find**: always combine path compression + union by rank/size.
8. **SCC**: Tarjan's low-link (1-pass) preferred; Kosaraju's (2-pass) easier to explain.
9. **Bridges/AP**: same low-link idea, different inequality (`>` vs `>=`).
10. **Bipartite**: 2-coloring, watch for disconnected components.

### 25.4 1-Hour Deep Revision Checklist

- [ ] Re-derive DFS and BFS from scratch without looking at notes.
- [ ] Implement Union-Find with both path compression and union by rank.
- [ ] Implement Dijkstra using `heapq`, trace through a 5-node example by hand.
- [ ] Implement Kahn's algorithm and DFS-based topological sort; compare outputs.
- [ ] Implement Kruskal's and Prim's; verify they produce the same total MST weight on the same input.
- [ ] Implement Tarjan's SCC algorithm; manually trace `low[]`/`disc[]` values on a small cyclic digraph.
- [ ] Implement bridge-finding; verify against a simple tree (every edge should be a bridge).
- [ ] Solve 3 problems from each category in Section 24 without hints.
- [ ] Time yourself: aim to write a correct BFS/DFS template in under 3 minutes from memory.
- [ ] Review the Common Mistakes table (Section 22) and check you've internalized each fix.

### 25.5 Interview Cheat Sheet — Final Words

> **The 6 algorithms that solve 90% of graph interview questions:**
> 1. DFS (recursive + iterative)
> 2. BFS (+ multi-source variant)
> 3. Union-Find (with both optimizations)
> 4. Dijkstra's Algorithm
> 5. Topological Sort (Kahn's)
> 6. Kruskal's / Prim's MST

> **The meta-skill that matters most:** recognizing when a problem is secretly a graph problem, even when it doesn't say "graph" — grids, state transformations, word chains, dependency lists, and scheduling problems are all graphs in disguise.

---

## 📎 FAQ

**Q: Should I always default to adjacency list?**
A: Yes, unless the graph is small/dense or you need O(1) edge-existence checks — then use a matrix.

**Q: When does Dijkstra fail?**
A: With negative edge weights. Switch to Bellman-Ford.

**Q: Is BFS always better than DFS for shortest path?**
A: Only for **unweighted** graphs. For weighted graphs, use Dijkstra/Bellman-Ford instead — BFS alone does not account for edge weights.

**Q: Do I need to memorize Tarjan's SCC AND Kosaraju's?**
A: Understand both conceptually, but pick one to implement fluently from memory — Tarjan's is more common in competitive programming; Kosaraju's is easier to explain in interviews.

**Q: How do I know if a problem needs Union-Find vs BFS/DFS for connectivity?**
A: If connectivity is queried **once**, BFS/DFS is simpler. If edges are added **incrementally** and you need connectivity checked after each addition (dynamic connectivity), Union-Find is far more efficient.

**Q: What's the difference between a bridge and an articulation point in terms of impact?**
A: A bridge removes exactly one edge and always splits the graph into exactly 2 components (if it was connected). An articulation point removes a vertex and can split the graph into 2 or more components.

---

*End of Handbook — Graphs: from first principles to FAANG mastery.*

---

## 7. Cycle Detection

Cycle detection differs fundamentally between **undirected** and **directed** graphs — this is one of the most common interview trip-ups.

### 7.1 Cycle Detection in Undirected Graphs — DFS (Parent Tracking)

**Intuition:** In an undirected graph, a cycle exists if you reach an already-visited node that is **not your immediate parent** (since the edge back to parent is expected and not a cycle).

```
Graph:            
(0)---(1)          DFS from 0: 0 -> 1 -> 2 -> 0 (0 already visited, and 0 is NOT
  \     |           parent of 2) => CYCLE detected
   \    |
    (2)-+
```

```python
def has_cycle_undirected(n, graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:      # visited AND not the parent -> cycle
                return True
        return False

    for v in range(n):
        if v not in visited:
            if dfs(v, -1):
                return True
    return False
```

**Line-by-line explanation:**
- `parent` tracks where we came from, so we don't falsely flag the trivial "back-edge" to our own parent as a cycle.
- If we hit a visited neighbor that isn't the parent, we've found a **back edge** to an ancestor — a cycle.
- We loop over all vertices to handle disconnected graphs.

**Complexity:** `O(V + E)` time, `O(V)` space.

### 7.2 Cycle Detection in Undirected Graphs — BFS (Union-Find Alternative)

Union-Find (Section 11) offers an elegant alternative: process edges one by one; if both endpoints already belong to the same set, adding this edge creates a cycle.

```python
def has_cycle_undirected_bfs(n, graph):
    visited = set()
    for start in range(n):
        if start in visited:
            continue
        visited.add(start)
        queue = deque([(start, -1)])   # (node, parent)
        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
    return False
```

### 7.3 Cycle Detection in Directed Graphs — DFS (Recursion Stack / Colors)

**Why undirected logic fails here:** In a directed graph, reaching a visited node that isn't your parent does **not** necessarily mean a cycle — it could just be a valid "cross edge" (e.g., a diamond-shaped DAG: `A->B->D` and `A->C->D` — D is visited twice but no cycle exists). We need to track nodes **currently in the recursion stack**, not just globally visited nodes.

```
DAG (no cycle):          Cyclic:
   A                        A
  / \                      / \
 B   C                    B   C
  \ /                      \ /
   D                        A   <- back edge to ancestor A = CYCLE
(D visited twice,
 but NOT a cycle)
```

```python
def has_cycle_directed(n, graph):
    WHITE, GRAY, BLACK = 0, 1, 2      # unvisited, in recursion stack, fully done
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY            # mark as "currently being explored"
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True            # back edge to an ancestor -> cycle
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK            # fully explored, safe forever
        return False

    for v in range(n):
        if color[v] == WHITE:
            if dfs(v):
                return True
    return False
```

**Line-by-line explanation:**
- **WHITE** = never visited. **GRAY** = currently on the DFS call stack (an ancestor of the current node). **BLACK** = fully processed, no longer on the stack.
- A `GRAY` neighbor means we've looped back to an ancestor — a genuine directed cycle.
- A `BLACK` neighbor means it was fully explored via a different path — safe, just a cross/forward edge, not a cycle.

**Dry Run** (graph `0->1, 1->2, 2->0`):

| Step | Node | Color Before | Action | Color After |
|---|---|---|---|---|
| 1 | 0 | WHITE | mark GRAY, visit neighbor 1 | GRAY |
| 2 | 1 | WHITE | mark GRAY, visit neighbor 2 | GRAY |
| 3 | 2 | WHITE | mark GRAY, visit neighbor 0 | GRAY |
| 4 | 0 | GRAY | neighbor 0 is GRAY -> **CYCLE FOUND** | — |

**Complexity:** `O(V + E)` time, `O(V)` space.

### 7.4 Cycle Detection in Directed Graphs — Kahn's Algorithm (BFS/Topological)

**Intuition:** A DAG always has at least one node with in-degree 0 (a valid starting point). If, after repeatedly removing zero-in-degree nodes, some nodes remain that never reach in-degree 0, those nodes are part of a cycle.

```python
def has_cycle_directed_kahn(n, graph):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([v for v in range(n) if indegree[v] == 0])
    processed = 0

    while queue:
        node = queue.popleft()
        processed += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return processed != n     # if not all nodes processed, a cycle exists
```

**Why this works:** Nodes stuck in a cycle can never reach in-degree 0 (each cycle node always has at least one incoming edge from within the cycle that never gets removed). So `processed < n` implies a cycle.

**Complexity:** `O(V + E)` time, `O(V)` space.

### 7.5 Comparison Table

| Scenario | Best Technique |
|---|---|
| Undirected graph | DFS with parent-tracking, or Union-Find |
| Directed graph | DFS with 3-color (WHITE/GRAY/BLACK) states |
| Directed graph + need topological order too | Kahn's Algorithm (BFS) |
| Need to detect AND print the cycle | DFS with explicit path/stack tracking |

> 💡 **Interview Tip:** If asked to detect a cycle in a directed graph AND perform topological sort, use Kahn's algorithm — it gives you both in one pass.

### 7.6 Common Mistakes

- Using the undirected parent-check technique on a directed graph — gives **false positives** on valid DAGs (like the diamond example above).
- Forgetting to reset "in recursion stack" state (GRAY -> BLACK) after fully exploring a node — causes false cycle detection across unrelated branches.
- Not handling disconnected components — must loop over all unvisited nodes.

### 7.7 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Course Schedule | LeetCode 207 | Directed cycle detection (Kahn's) |
| Detect Cycle in a Directed Graph | GeeksforGeeks | DFS 3-color |
| Detect Cycle in an Undirected Graph | GeeksforGeeks | DFS parent tracking |
| Graph Valid Tree | LeetCode 261 | Undirected cycle + connectivity |
| Redundant Connection | LeetCode 684 | Union-Find cycle detection |


---

## 8. Topological Sorting

### 8.1 Definition & Why It Exists

A **topological sort** of a DAG is a linear ordering of vertices such that for every directed edge `u -> v`, `u` comes before `v` in the ordering. It exists because many real problems require **respecting dependencies**: you can't compile a file before its imports, can't take an advanced course before its prerequisite, can't run a build step before its dependency finishes.

> ⚠️ Topological sort is **only defined for DAGs**. If the graph has a cycle, no valid ordering exists.

**Real-world analogy:** Getting dressed — you must put on socks before shoes, and a shirt before a jacket. Topological sort finds a valid order for many such constraints simultaneously.

```
Graph (course prerequisites):
  Math101 -> Math201 -> Math301
      \                    ^
       -> CS101 -----------+

Valid Topological Order: Math101, CS101, Math201, Math301
(Math101 must precede CS101 and Math201; Math201 and CS101 both precede Math301)
```

### 8.2 DFS-Based Topological Sort

**Intuition:** Do a DFS; when a node has finished exploring *all* its descendants (no more unvisited neighbors), push it onto a stack. Since a node is only pushed after everything it depends on has already been pushed, reversing the stack gives a valid topological order.

```python
def topo_sort_dfs(n, graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)          # push AFTER all descendants are processed

    for v in range(n):
        if v not in visited:
            dfs(v)

    return stack[::-1]              # reverse to get correct order
```

**Line-by-line explanation:**
- We recurse into all neighbors first — this guarantees every node that `node` depends on is already on the stack before `node` itself is pushed.
- Appending to `stack` after the recursive calls (post-order) is the key trick.
- Reversing at the end converts "finish order" into "dependency order."

**Dry Run** (graph: `0->1, 0->2, 1->3, 2->3`):

| Step | Node | Action | Stack |
|---|---|---|---|
| 1 | 0 | visit 0, recurse into 1 | [] |
| 2 | 1 | visit 1, recurse into 3 | [] |
| 3 | 3 | visit 3, no neighbors, push 3 | [3] |
| 4 | 1 | done, push 1 | [3, 1] |
| 5 | 0 | recurse into 2 | [3, 1] |
| 6 | 2 | visit 2, neighbor 3 visited, push 2 | [3, 1, 2] |
| 7 | 0 | done, push 0 | [3, 1, 2, 0] |
| — | — | reverse | [0, 2, 1, 3] |

**Complexity:** `O(V + E)` time, `O(V)` space.

### 8.3 Kahn's Algorithm (BFS-Based Topological Sort)

**Intuition:** Repeatedly pick nodes with in-degree 0 (no unresolved dependencies), "remove" them, and decrement the in-degree of their neighbors. This mirrors literally resolving dependencies one at a time.

```python
def topo_sort_kahn(n, graph):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([v for v in range(n) if indegree[v] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != n:
        raise ValueError("Graph has a cycle — no topological order exists")
    return order
```

**Complexity:** `O(V + E)` time, `O(V)` space.

### 8.4 DFS vs Kahn's — When to Use Which

| Criterion | DFS-Based | Kahn's (BFS-Based) |
|---|---|---|
| Cycle detection built-in | ❌ (needs separate 3-color check) | ✅ (if `len(order) != n`) |
| Multiple valid orderings | Gives one valid order (harder to enumerate all) | Naturally supports "lexicographically smallest" via a min-heap |
| Intuition | Post-order DFS + reverse | Iterative dependency removal |
| Preferred when | Recursion is natural / doing DFS anyway | Need cycle detection + order together, or need level info |

> 💡 **Interview Tip:** If the problem says "return the lexicographically smallest valid order," use Kahn's algorithm with a **min-heap** instead of a plain queue, so you always pick the smallest available zero-in-degree node.

### 8.5 Edge Cases

- Graph with a cycle → no valid order exists; Kahn's naturally detects this (`len(order) < n`).
- Disconnected DAG components → still produces a valid combined order; both algorithms handle this automatically by iterating all vertices.
- Single node, no edges → topological order is just that node.

### 8.6 Common Mistakes

- Forgetting to reverse the stack in DFS-based topo sort (a very common bug — produces exactly the wrong order).
- Not checking `len(order) != n` in Kahn's algorithm — silently returns a partial (and wrong) order on cyclic input.
- Confusing in-degree with out-degree when computing Kahn's initial queue.

### 8.7 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Course Schedule II | LeetCode 210 | Topological sort (return order) |
| Alien Dictionary | LeetCode 269 | Build graph from constraints + topo sort |
| Sequence Reconstruction | LeetCode 444 | Uniqueness of topological order |
| Minimum Height Trees | LeetCode 310 | Topological "peeling" from leaves |
| Parallel Courses | LeetCode 1136 | Topo sort + level/time tracking |


---

## 9. Shortest Path Algorithms

### 9.1 Overview — Choosing the Right Algorithm

| Graph Type | Best Algorithm | Complexity |
|---|---|---|
| Unweighted | BFS | O(V + E) |
| Weighted, non-negative edges, single source | Dijkstra | O((V+E) log V) with heap |
| Weighted, negative edges allowed, single source | Bellman-Ford | O(V × E) |
| All-pairs shortest paths | Floyd-Warshall | O(V³) |
| Heuristic-guided single-pair shortest path | A* | O(E) with good heuristic |
| All-pairs with negative edges (sparse) | Johnson's Algorithm | O(V² log V + VE) |

### 9.2 BFS for Unweighted Shortest Path

Already covered in Section 5.2 — BFS is optimal here because every edge has implicit weight 1, so the first-visit order **is** the shortest-path order.

```python
def shortest_path_unweighted(graph, start):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist
```

### 9.3 Dijkstra's Algorithm

**Definition:** Finds shortest paths from a single source to all other vertices in a graph with **non-negative** edge weights.

**Why it exists:** BFS fails when edges have different weights — the "fewest edges" path isn't necessarily the "lowest total cost" path. Dijkstra greedily always expands the **currently-closest known unvisited node**, guaranteeing that once a node is finalized, its distance is truly the shortest possible (since all other edge weights are non-negative, no future discovery can improve it).

**Real-world analogy:** GPS navigation — always explore the road that currently has the shortest known travel time first.

```
Graph:
    (A)--4--(B)
     |        \
     1         2
     |          \
    (C)--1------(D)

Shortest distances from A: A=0, C=1, D=2 (via C), B=4
```

```python
import heapq

def dijkstra(n, graph, src):
    """
    graph[u] = list of (neighbor, weight)
    """
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]           # (distance, node) min-heap
    visited = set()

    while pq:
        d, node = heapq.heappop(pq)
        if node in visited:
            continue           # stale entry, skip
        visited.add(node)

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist
```

**Line-by-line explanation:**
- `heapq` is a min-heap, so `heappop` always gives the currently-smallest tentative distance — this is the "greedy" step.
- The `visited` check skips **stale** heap entries — Python's `heapq` has no decrease-key, so we just push duplicates and ignore outdated ones when popped.
- **Relaxation**: if going through `node` gives a shorter path to `neighbor` than previously known, update it and push the new candidate distance.

**Dry Run:**

| Step | Popped (dist, node) | Action | dist array |
|---|---|---|---|
| 1 | (0, A) | relax C(1), B(4) | A=0, C=1, B=4, D=inf |
| 2 | (1, C) | relax D via C: 1+1=2 < inf | D=2 |
| 3 | (2, D) | relax B via D: 2+2=4, not better than 4 | no change |
| 4 | (4, B) | no better relaxations | done |

**Complexity:** `O((V + E) log V)` with a binary heap. **Space:** `O(V + E)`.

> ⚠️ **Critical Limitation:** Dijkstra **fails with negative edge weights** — once a node is marked visited/finalized, we never revisit it, but a negative edge discovered later could still shorten its distance, producing a wrong answer.

### 9.4 Bellman-Ford Algorithm

**Definition:** Finds shortest paths from a single source even with **negative edge weights**, and can detect **negative weight cycles**.

**Why it exists:** Some real graphs have negative weights (e.g., financial arbitrage, refunds/credits). Dijkstra can't handle these; Bellman-Ford can, at the cost of higher complexity.

**Intuition:** Relax **every edge**, `V-1` times. Why `V-1`? The longest possible shortest path (without cycles) visits at most `V-1` edges, so after `V-1` full relaxation passes, all shortest distances are guaranteed correct (assuming no negative cycle).

```python
def bellman_ford(n, edges, src):
    """
    edges: list of (u, v, w)
    """
    dist = [float('inf')] * n
    dist[src] = 0

    for _ in range(n - 1):               # relax all edges V-1 times
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # One more pass to detect negative weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return dist
```

**Line-by-line explanation:**
- The outer loop runs `n-1` times because that's the maximum number of edges in any simple shortest path.
- Each inner pass tries to relax **every** edge — unlike Dijkstra, there's no greedy "pick the closest node" step, so it works even when a shorter path is discovered via a negative edge later.
- The extra `n`-th pass: if any edge can *still* be relaxed, a negative cycle exists (distances would keep decreasing forever).

**Dry Run** (edges: `(0,1,4), (0,2,5), (1,2,-3)`, src=0, n=3):

| Pass | Relaxations | dist |
|---|---|---|
| Init | — | [0, inf, inf] |
| 1 | (0,1,4): dist[1]=4; (0,2,5): dist[2]=5; (1,2,-3): dist[2]=min(5,4-3)=1 | [0,4,1] |
| 2 | no further improvement | [0,4,1] |

**Complexity:** `O(V × E)` time, `O(V)` space — much slower than Dijkstra but handles negative weights.

### 9.5 Floyd-Warshall Algorithm

**Definition:** Computes shortest paths between **all pairs** of vertices in `O(V³)`.

**Why it exists:** When you need distances between every pair (not just from one source), running Dijkstra/Bellman-Ford from every vertex is possible but Floyd-Warshall's DP formulation is simpler to implement and works with negative edges (no negative cycles).

**Intuition (DP):** `dist[i][j]` = shortest distance from `i` to `j` using only vertices `{0...k}` as intermediate stops. We try allowing each vertex `k` one at a time as a possible "waypoint."

```python
def floyd_warshall(n, edges):
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)   # handle parallel edges

    for k in range(n):                     # try k as intermediate vertex
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
```

**Line-by-line explanation:**
- Base case: `dist[i][i] = 0`, direct edges initialized from input.
- The triple loop tries every vertex `k` as a potential shortcut between every pair `(i, j)` — if routing through `k` is shorter, update.
- Order of loops matters: `k` **must** be the outermost loop for the DP to be correct (it represents "using only vertices up to k so far").

**Complexity:** `O(V³)` time, `O(V²)` space. Best suited when `V` is small (typically `V ≤ 400-500`).

> ⚠️ **Common Mistake:** Swapping loop order (`i, j, k` instead of `k, i, j`) breaks the DP invariant and gives **wrong answers silently** — one of the most notorious subtle bugs in competitive programming.

### 9.6 A* Search Algorithm (Overview)

**Definition:** A* is Dijkstra enhanced with a **heuristic** `h(n)` estimating remaining distance to the goal, prioritizing nodes with the lowest `f(n) = g(n) + h(n)` (actual cost so far + estimated cost to goal).

**Why it exists:** Dijkstra explores uniformly in all directions; A* uses domain knowledge (e.g., straight-line distance in a map) to explore **toward the goal** more directly, often visiting far fewer nodes.

```python
def a_star(graph, start, goal, heuristic):
    pq = [(heuristic(start), 0, start)]   # (f = g+h, g, node)
    best_g = {start: 0}

    while pq:
        f, g, node = heapq.heappop(pq)
        if node == goal:
            return g
        for neighbor, weight in graph[node]:
            new_g = g + weight
            if new_g < best_g.get(neighbor, float('inf')):
                best_g[neighbor] = new_g
                heapq.heappush(pq, (new_g + heuristic(neighbor), new_g, neighbor))
    return float('inf')
```

**Key requirement:** The heuristic must be **admissible** (never overestimates true cost) for A* to guarantee optimality — e.g., Euclidean distance for grid/map pathfinding.

### 9.7 Johnson's Algorithm (Overview)

**Definition:** Computes all-pairs shortest paths in **sparse** graphs with negative edges, faster than Floyd-Warshall (`O(V² log V + VE)` vs `O(V³)`).

**Intuition:** Add a virtual source node connected to all vertices with weight 0, run Bellman-Ford once from it to compute a re-weighting function `h(v)` that eliminates negative edges without changing shortest-path structure, then run Dijkstra from every vertex on the re-weighted graph.

> This is primarily useful in competitive programming when `V` is large and the graph is sparse but has negative edges — rare in typical interviews, good to know conceptually.

### 9.8 Complexity Comparison Table

| Algorithm | Time | Space | Handles Negative Weights | Use Case |
|---|---|---|---|---|
| BFS | O(V+E) | O(V) | N/A (unweighted) | Unweighted shortest path |
| Dijkstra | O((V+E) log V) | O(V+E) | ❌ | Single-source, non-negative weights |
| Bellman-Ford | O(V×E) | O(V) | ✅ (detects neg. cycles) | Single-source, negative weights allowed |
| Floyd-Warshall | O(V³) | O(V²) | ✅ (no neg. cycles) | All-pairs, small V |
| A* | O(E) best case | O(V) | ❌ | Single-pair with good heuristic |
| Johnson's | O(V² log V + VE) | O(V²) | ✅ | All-pairs, sparse, negative weights |

### 9.9 Common Mistakes

- Using Dijkstra on graphs with negative weights — silently wrong answers.
- Forgetting the `visited`/stale-check in Dijkstra's heap loop — leads to redundant relaxation (correct but inefficient) or, if `visited` is misused, incorrect skips.
- Wrong loop order in Floyd-Warshall (`k` must be outermost).
- Not detecting negative cycles when required (interview problems sometimes explicitly ask "does a negative cycle exist reachable from source?").

### 9.10 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Network Delay Time | LeetCode 743 | Dijkstra |
| Cheapest Flights Within K Stops | LeetCode 787 | Bellman-Ford (limited relaxations) |
| Path With Minimum Effort | LeetCode 1631 | Dijkstra variant (minimize max edge) |
| Find the City With the Smallest Number of Neighbors | LeetCode 1334 | Floyd-Warshall |
| Negative Weight Cycle | GeeksforGeeks | Bellman-Ford cycle detection |


---

## 10. Minimum Spanning Tree (MST)

### 10.1 Definition & Why It Exists

A **Minimum Spanning Tree** of a connected, undirected, weighted graph is a subset of edges that connects all vertices, contains no cycles, and has the **minimum possible total edge weight**. It exists because many real problems need to connect all nodes as cheaply as possible — laying cable, building roads, or designing networks — without redundant (cycle-forming) connections.

**Real-world analogy:** An internet provider wants to connect all cities with fiber cable at minimum total cost, without laying redundant lines.

```
Graph:                     MST (bold edges):
  (A)--4--(B)                (A)--4--(B)
   |  \    |                  |       |
   1   3   2                  1       2
   |    \  |                  |       |
  (C)----(D)                 (C)     (D)

Total weight of all edges: 4+1+3+2 = 10
MST picks: A-C(1), A-B(4)? No -- optimal MST = A-C(1), C-D? etc.
(MST always has exactly V-1 edges, here 3 edges for 4 vertices)
```

### 10.2 Kruskal's Algorithm

**Intuition:** Greedily pick the smallest-weight edge that doesn't form a cycle, using **Union-Find** to efficiently check "would this edge connect two vertices already in the same component?"

```python
def kruskal(n, edges):
    """
    edges: list of (weight, u, v)
    """
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]   # path compression
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False              # already connected -> would form a cycle
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True

    edges.sort()                       # sort by weight ascending
    mst_weight = 0
    mst_edges = []

    for w, u, v in edges:
        if union(u, v):                 # only add if it doesn't create a cycle
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges
```

**Line-by-line explanation:**
- Sorting edges by weight ensures we always consider the cheapest available edge first (greedy choice).
- `find`/`union` with path compression and union by rank make cycle-checking near `O(1)` amortized.
- We only add an edge if its endpoints are in **different** components — adding an edge within the same component would create a cycle, violating the "tree" property.

**Dry Run** (edges sorted: `(1,A,C), (2,B,D), (3,C,D), (4,A,B)`):

| Step | Edge | Union Result | MST So Far | Weight |
|---|---|---|---|---|
| 1 | (1,A,C) | different sets -> union | {A-C} | 1 |
| 2 | (2,B,D) | different sets -> union | {A-C},{B-D} | 3 |
| 3 | (3,C,D) | different sets -> union | {A-C-B-D} | 6 |
| 4 | (4,A,B) | same set -> **skip** (cycle) | — | 6 (final) |

**Complexity:** `O(E log E)` for sorting + `O(E α(V))` for union-find (α = inverse Ackermann, effectively constant). Overall: `O(E log E)`.

### 10.3 Prim's Algorithm

**Intuition:** Start from any vertex and greedily grow the MST by always adding the **cheapest edge that connects the current tree to a new vertex** — similar to Dijkstra, but tracking edge weight to reach a node rather than cumulative path distance.

```python
def prim(n, graph, start=0):
    """
    graph[u] = list of (neighbor, weight)
    """
    visited = [False] * n
    min_heap = [(0, start)]      # (edge weight, node)
    mst_weight = 0
    edges_used = 0

    while min_heap and edges_used < n:
        w, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        mst_weight += w
        edges_used += 1

        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight, neighbor))

    return mst_weight
```

**Line-by-line explanation:**
- We always pop the cheapest available edge connecting the "grown" tree to an unvisited vertex — this is the greedy step (analogous to Dijkstra, but comparing edge weight, not path sum).
- Stale heap entries (edges to already-visited nodes) are skipped via the `visited` check.
- Unlike Dijkstra, weight is **not cumulative** — it's just the single edge weight to bring in the new vertex.

**Complexity:** `O(E log V)` with a binary heap — similar to Dijkstra.

### 10.4 Kruskal vs Prim — When to Use Which

| Criterion | Kruskal | Prim |
|---|---|---|
| Best for | Sparse graphs (edge list based) | Dense graphs (adjacency list/matrix based) |
| Core data structure | Union-Find | Min-Heap |
| Natural starting point | Sort all edges globally | Start from one vertex, grow outward |
| Easier to reason about MST edges directly | ✅ | Less direct |
| Works well when edges are given as a flat list | ✅ | Needs adjacency structure |

> 💡 **Interview Tip:** If the input is naturally an edge list (`(u,v,w)` tuples), reach for Kruskal. If it's naturally an adjacency list/matrix, Prim tends to be more natural.

### 10.5 Borůvka's Algorithm (Overview)

**Intuition:** In parallel, each component finds its own cheapest outgoing edge and adds it, merging components; repeat until one component remains. It's the oldest MST algorithm (1926) and is naturally parallelizable, which makes it attractive for distributed/parallel computing, though rarely asked in standard interviews.

**Complexity:** `O(E log V)`.

### 10.6 Edge Cases

- Disconnected graph → no spanning tree exists for the whole graph; only a **minimum spanning forest** can be found (one MST per component).
- Graph with duplicate/parallel edges → keep only the minimum-weight edge between any pair before running Kruskal (or let Union-Find naturally skip the redundant heavier one).
- Single vertex → MST weight is 0, no edges needed.

### 10.7 Common Mistakes

- Forgetting path compression / union by rank in Union-Find → Kruskal degrades toward `O(E × V)`.
- Not checking `visited` before adding weight in Prim → double-counting stale heap entries.
- Assuming MST is unique — it's **not** unique if there are ties in edge weights (though the total MST weight is always unique).

### 10.8 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Min Cost to Connect All Points | LeetCode 1584 | Prim's / Kruskal's |
| Connecting Cities With Minimum Cost | LeetCode 1135 | Kruskal's |
| Optimize Water Distribution in a Village | LeetCode 1168 | Kruskal's with virtual source node |
| Minimum Spanning Tree | GeeksforGeeks | Both Kruskal's and Prim's |


---

## 11. Disjoint Set Union / Union-Find

### 11.1 Definition & Why It Exists

**Union-Find** (Disjoint Set Union, DSU) is a data structure that tracks a partition of elements into disjoint sets, supporting two operations efficiently:
- `find(x)`: which set does `x` belong to?
- `union(x, y)`: merge the sets containing `x` and `y`.

It exists because many problems boil down to "are these two things connected/grouped together?" — dynamic connectivity, cycle detection, and Kruskal's MST all need this efficiently, and naive approaches (like re-running BFS/DFS on every query) are far too slow.

**Real-world analogy:** Friend groups merging — if Alice and Bob become friends, and Bob and Carol are already friends, then Alice, Bob, and Carol are all in the same "friend group." Union-Find tracks these merges efficiently.

### 11.2 ASCII Visualization

```
Initial (each its own set):    After union(A,B) and union(C,D):
 A   B   C   D                  A---B      C---D
 (4 separate sets)              (2 sets: {A,B}, {C,D})

After union(B,C):
 A---B---C---D
 (1 set: {A,B,C,D})
```

### 11.3 Implementation — Make Set, Find, Union

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   # each node is its own parent initially
        self.rank = [0] * n            # tracks approximate tree height
        self.count = n                  # number of disjoint sets

    def find(self, x):
        # Path compression: point x directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False               # already in the same set

        # Union by rank: attach smaller tree under bigger tree's root
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.count -= 1                 # one fewer disjoint set
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

**Line-by-line explanation:**
- `parent[x] = x` initially — every node starts as its own set (a singleton).
- **Path Compression** in `find`: while finding the root, we rewire every visited node directly to the root, flattening the tree for future queries.
- **Union by Rank**: always attach the shorter tree under the taller tree's root, keeping the overall tree shallow.
- `count` tracks the number of remaining disjoint sets — useful for "how many connected components" questions.

**Dry Run** (operations: `union(0,1)`, `union(2,3)`, `union(1,2)`, `find(0)`):

| Step | Operation | parent array (index=node) | Explanation |
|---|---|---|---|
| 0 | init n=4 | [0,1,2,3] | all separate |
| 1 | union(0,1) | [0,0,2,3] | 1's root -> 0 |
| 2 | union(2,3) | [0,0,2,2] | 3's root -> 2 |
| 3 | union(1,2) | [0,0,0,2] | root(1)=0, root(2)=2, attach 2 under 0 |
| 4 | find(0) | [0,0,0,2] | returns 0 (already root) |

**Complexity:** With both path compression and union by rank, each operation is `O(α(V))` amortized — where `α` is the inverse Ackermann function, which is less than 5 for any realistic input size, so effectively **O(1)**.

### 11.4 Union by Rank vs Union by Size

| Approach | What it tracks | Merge rule |
|---|---|---|
| Union by Rank | Approximate tree height | Attach shorter tree under taller |
| Union by Size | Number of elements in each set | Attach smaller set under larger |

Both achieve the same `O(α(V))` amortized complexity; union by size is sometimes preferred because it directly gives you set sizes for free (useful for "largest connected component" queries).

```python
# Union by size variant
class UnionFindBySize:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True
```

### 11.5 Why Path Compression + Union by Rank/Size Matters

Without either optimization, Union-Find degenerates to `O(V)` per operation in the worst case (a long chain). With **both** optimizations together, the amortized complexity drops to `O(α(V))` — practically constant. Using only one of the two still gives `O(log V)` amortized, which is good but not optimal.

### 11.6 Applications

- Cycle detection in undirected graphs (Section 7.2)
- Kruskal's MST (Section 10.2)
- Counting connected components dynamically
- Percolation / grid connectivity problems
- Detecting redundant connections
- Accounts merging (grouping emails belonging to the same person)
- Kruskal-style clustering algorithms

### 11.7 Edge Cases

- Calling `union(x, x)` — should be a no-op (`find(x) == find(x)`).
- Very large `n` with recursive `find` — can hit Python recursion limits; convert to **iterative path compression** for huge inputs:

```python
def find_iterative(self, x):
    root = x
    while self.parent[root] != root:
        root = self.parent[root]
    while self.parent[x] != root:          # second pass: compress path
        self.parent[x], x = root, self.parent[x]
    return root
```

### 11.8 Common Mistakes

- Forgetting path compression → degraded performance on large inputs.
- Comparing `x == y` instead of `find(x) == find(y)` when checking connectivity.
- Off-by-one errors when nodes are 1-indexed but the `UnionFind` array is 0-indexed.

### 11.9 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Number of Provinces | LeetCode 547 | Union-Find component counting |
| Redundant Connection | LeetCode 684 | Union-Find cycle detection |
| Accounts Merge | LeetCode 721 | Union-Find grouping |
| Satisfiability of Equality Equations | LeetCode 990 | Union-Find with constraints |
| Number of Islands II | LeetCode 305 | Dynamic connectivity |


---

## 12. Strongly Connected Components

### 12.1 Definition & Why It Exists

A **Strongly Connected Component (SCC)** of a directed graph is a maximal set of vertices such that every vertex is reachable from every other vertex **within that set**, respecting edge direction. SCCs matter because they reveal the "true" cyclic clusters in a directed graph — useful for compiler dependency cycles, analyzing web-link structures, and simplifying a graph into a DAG of components (condensation graph).

```
Directed Graph:              SCCs:
  A -> B -> C                {A, B, C} (A->B->C->A is a cycle)
  ^         |                {D}
  |         v
  +---------+
            D <- (E)         {E}  (E -> D but D doesn't reach E)
```

### 12.2 Kosaraju's Algorithm

**Intuition:** Run DFS to compute a **finish-order** stack (like topological sort), reverse all edges (transpose the graph), then run DFS again in finish-order — each DFS tree in this second pass is exactly one SCC.

**Why it works:** If `u` and `v` are in the same SCC, they're mutually reachable in both the original graph and its transpose. Processing nodes in decreasing finish-time order on the transposed graph ensures we never "leak" into a different SCC during the second DFS.

```python
def kosaraju_scc(n, graph):
    # Step 1: order vertices by finish time (like topo sort)
    visited = set()
    finish_stack = []

    def dfs1(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs1(neighbor)
        finish_stack.append(node)

    for v in range(n):
        if v not in visited:
            dfs1(v)

    # Step 2: transpose the graph (reverse every edge)
    transpose = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transpose[v].append(u)

    # Step 3: DFS on transpose in reverse finish order
    visited.clear()
    sccs = []

    def dfs2(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in transpose[node]:
            if neighbor not in visited:
                dfs2(neighbor, component)

    for node in reversed(finish_stack):
        if node not in visited:
            component = []
            dfs2(node, component)
            sccs.append(component)

    return sccs
```

**Line-by-line explanation:**
- `dfs1` computes finish order exactly like DFS-based topological sort.
- Building the `transpose` graph is `O(V+E)` — reverse every directed edge.
- `dfs2`, run in decreasing finish-time order over the **transposed** graph, discovers exactly one SCC per call — because any path leading "out" of the true SCC in the transpose would have had to finish earlier in step 1, so it can't be reached.

**Complexity:** `O(V + E)` — three linear passes.

### 12.3 Tarjan's Algorithm

**Intuition:** A single DFS pass using a **discovery time** and a **low-link value** per node. `low[u]` = the smallest discovery time reachable from `u`'s subtree (including back edges to ancestors). A node is the **root of an SCC** if `low[u] == disc[u]` — meaning nothing in its subtree can reach further back than itself.

```python
def tarjan_scc(n, graph):
    disc = [-1] * n
    low = [-1] * n
    on_stack = [False] * n
    stack = []
    timer = [0]
    sccs = []

    def dfs(u):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        stack.append(u)
        on_stack[u] = True

        for v in graph[u]:
            if disc[v] == -1:                  # v not visited yet
                dfs(v)
                low[u] = min(low[u], low[v])   # propagate low-link up
            elif on_stack[v]:                   # v is an ancestor still on stack
                low[u] = min(low[u], disc[v])

        if low[u] == disc[u]:                   # u is the root of an SCC
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == u:
                    break
            sccs.append(component)

    for v in range(n):
        if disc[v] == -1:
            dfs(v)

    return sccs
```

**Line-by-line explanation:**
- `disc[u]` records when `u` was first visited; `low[u]` tracks the earliest-discovered node reachable from `u`'s DFS subtree.
- For a **tree edge** (`v` unvisited): recurse, then propagate `low[v]` up to `low[u]`.
- For a **back edge** to an ancestor still on the stack: update `low[u]` using `disc[v]` (not `low[v]` — this distinction matters and is a classic subtlety).
- When `low[u] == disc[u]`, `u` cannot reach any earlier ancestor — it is the "root" of its SCC, so we pop the stack until we get back to `u`, collecting the whole component.

**Complexity:** `O(V + E)` — single DFS pass, slightly more efficient in practice than Kosaraju's (no need to build a transpose graph).

### 12.4 Kosaraju vs Tarjan

| Criterion | Kosaraju's | Tarjan's |
|---|---|---|
| Number of DFS passes | 2 (+ building transpose) | 1 |
| Conceptual simplicity | Easier to understand/explain | Requires low-link intuition |
| Extra graph needed | Yes (transpose) | No |
| Typical preference | Teaching / interviews | Competitive programming (faster, single pass) |

### 12.5 Condensation Graph

**Definition:** Collapse each SCC into a single "super-node." The resulting graph is guaranteed to be a **DAG** (since any cycle would mean the original nodes should have been in the same SCC).

```
Original SCCs: {A,B,C}, {D}, {E}
Condensation:  SCC1 -> SCC2    (if any edge existed from {A,B,C} to {D})
                        ^
                       SCC3   ({E} -> {D})
```

The condensation graph is extremely useful for problems that require reasoning about dependencies **between clusters** once internal cycles are collapsed away — e.g., "minimum edges to add so the whole graph becomes strongly connected."

### 12.6 Edge Cases

- A single node with no edges is trivially its own SCC.
- Fully strongly connected graph → one SCC containing all vertices.
- DAG (no cycles at all) → every vertex is its own SCC.

### 12.7 Common Mistakes

- In Tarjan's, using `low[v]` instead of `disc[v]` when updating `low[u]` for a back edge — this is a **very common bug** that silently produces wrong SCCs in some graphs.
- Forgetting to check `on_stack[v]` in Tarjan's — without it, cross-edges to already-fully-processed nodes (in a *different*, already-popped SCC) get wrongly treated as back edges.
- In Kosaraju's, running the second DFS in the wrong order (must be **decreasing** finish time).

### 12.8 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Strongly Connected Components (Kosaraju's) | GeeksforGeeks | Kosaraju's |
| Critical Connections in a Network | LeetCode 1192 | Tarjan's (bridges, related concept) |
| Strongly Connected Component | CSES | Kosaraju's / Tarjan's |
| Number of SCCs | Codeforces (various) | Tarjan's |


---

## 13. Bridges & Articulation Points

### 13.1 Definitions & Why They Exist

- A **bridge** (cut edge) is an edge whose removal **increases** the number of connected components.
- An **articulation point** (cut vertex) is a vertex whose removal **increases** the number of connected components.

These identify **single points of failure** in a network — critical for network reliability analysis (e.g., "which server/cable, if it fails, disconnects part of the network?").

**Real-world analogy:** A bridge in a road network — if it's the only connection between two towns and it collapses, the towns become disconnected. An articulation point is like a single town that all routes must pass through.

```
Graph:
  (A)---(B)---(C)
          |
         (D)

Bridges: (B,C) and (B,D) -- removing either disconnects the graph
Articulation Points: B -- removing B splits {A}, {C}, {D} apart
```

### 13.2 Tarjan's Algorithm for Bridges

**Intuition:** Same `disc`/`low` machinery as SCC's Tarjan algorithm, adapted for undirected graphs. An edge `(u, v)` (tree edge in DFS) is a bridge if `low[v] > disc[u]` — meaning `v`'s subtree has **no other way back** to `u` or any ancestor of `u`.

```python
def find_bridges(n, graph):
    disc = [-1] * n
    low = [-1] * n
    timer = [0]
    bridges = []

    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1

        for v in graph[u]:
            if v == parent:
                continue                     # skip the edge back to immediate parent
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:          # no back-edge from v's subtree to u or above
                    bridges.append((u, v))
            else:
                low[u] = min(low[u], disc[v])  # back edge to an ancestor

    for v in range(n):
        if disc[v] == -1:
            dfs(v, -1)

    return bridges
```

**Line-by-line explanation:**
- We skip the trivial edge back to the immediate parent (`v == parent`) — but only **once**; if there are parallel edges to the parent, this needs adjusting (track edge IDs instead of just parent node).
- `low[v] > disc[u]` is the bridge condition: it means the subtree rooted at `v` has no back edge reaching `u` or any of `u`'s ancestors — so the edge `(u,v)` is the **only** connection between that subtree and the rest of the graph.

**Complexity:** `O(V + E)`.

### 13.3 Tarjan's Algorithm for Articulation Points

**Intuition:** A vertex `u` is an articulation point if either:
1. `u` is the **DFS root** and has **2 or more** children in the DFS tree (removing `u` disconnects its subtrees from each other).
2. `u` is **not the root**, and it has a child `v` such that `low[v] >= disc[u]` — meaning `v`'s subtree cannot reach back above `u` without going through `u`.

```python
def find_articulation_points(n, graph):
    disc = [-1] * n
    low = [-1] * n
    timer = [0]
    is_articulation = [False] * n

    def dfs(u, parent):
        children = 0
        disc[u] = low[u] = timer[0]
        timer[0] += 1

        for v in graph[u]:
            if v == parent:
                continue
            if disc[v] == -1:
                children += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])

                if parent != -1 and low[v] >= disc[u]:
                    is_articulation[u] = True
            else:
                low[u] = min(low[u], disc[v])

        if parent == -1 and children > 1:      # root special case
            is_articulation[u] = True

    for v in range(n):
        if disc[v] == -1:
            dfs(v, -1)

    return [v for v in range(n) if is_articulation[v]]
```

**Line-by-line explanation:**
- Note the subtle but critical difference from the bridge condition: articulation points use `low[v] >= disc[u]` (inclusive `>=`), while bridges use `low[v] > disc[u]` (strict `>`). This is because a vertex can still be an articulation point even if the child's subtree loops back exactly to `u` itself (but not beyond) — removing `u` still disconnects that subtree from the rest.
- The **root special case** exists because the root has no ancestors to check against; it's only an articulation point if removing it splits the DFS tree into 2+ separate children subtrees.

**Complexity:** `O(V + E)`.

### 13.4 Dry Run (Bridges) on Sample Graph

Graph: `A-B, B-C, B-D` (a "star" from B):

| Node | disc | low | Notes |
|---|---|---|---|
| A | 0 | 0 | leaf |
| B | 1 | 1 | connects to A, C, D |
| C | 2 | 2 | leaf, low[C]=2 > disc[B]=1 -> (B,C) is a bridge |
| D | 3 | 3 | leaf, low[D]=3 > disc[B]=1 -> (B,D) is a bridge |

Result: bridges = `[(B,A), (B,C), (B,D)]`; articulation point = `{B}`.

### 13.5 Edge Cases

- Graph with a single edge → that edge is trivially a bridge.
- Fully cyclic graph (e.g., a ring) → **no bridges and no articulation points** (every node has an alternate path).
- Multiple edges between the same pair of vertices (multigraph) → must track by edge index, not just parent vertex, or the "skip parent" logic incorrectly treats a genuine back-edge-via-parallel-edge as the trivial parent edge.

### 13.6 Common Mistakes

- Using `low[v] > disc[u]` (bridge condition) when you meant articulation points (`>=`) — swapping these two conditions is the single most common bug in this topic.
- Not special-casing the DFS root for articulation points.
- Failing to handle parallel edges to the parent correctly in multigraphs.

### 13.7 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Critical Connections in a Network | LeetCode 1192 | Bridges (Tarjan's) |
| Articulation Points | GeeksforGeeks | Articulation Points (Tarjan's) |
| Bridges in a Graph | GeeksforGeeks | Bridges (Tarjan's) |
| Number of Operations to Make Network Connected | LeetCode 1319 | Related — connectivity + Union-Find |


---

## 14. Bipartite Graphs

### 14.1 Definition & Why It Exists

A graph is **bipartite** if its vertices can be divided into two disjoint sets `U` and `V` such that every edge connects a vertex in `U` to a vertex in `V` — no edge connects two vertices within the same set. Equivalently: **a graph is bipartite if and only if it contains no odd-length cycle.**

Bipartite graphs model countless real problems: matching job applicants to jobs, students to schools, or checking if a set of constraints ("A and B must differ") is satisfiable — this is essentially 2-coloring.

```
Bipartite:                 Not Bipartite (odd cycle):
Set U: A   B                  A---B
        \ / \                  \ / 
         X   \                 C  <- triangle A-B-C-A (odd cycle) => not bipartite
        / \   \
Set V: C   D
```

### 14.2 Checking Bipartiteness — BFS (2-Coloring)

**Intuition:** Try to color the graph with 2 colors such that no two adjacent vertices share a color. If we ever find an edge connecting two same-colored vertices, the graph is not bipartite.

```python
def is_bipartite_bfs(n, graph):
    color = [-1] * n     # -1 = uncolored, 0/1 = the two colors

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]   # opposite color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False                          # conflict -> not bipartite
    return True
```

**Line-by-line explanation:**
- `color[node] = 0` starts one side; every discovered neighbor gets `1 - color[node]`, flipping between 0 and 1.
- If we ever find a neighbor already colored the **same** as the current node, we've found an odd cycle — not bipartite.
- Looping over all `start` values handles disconnected components (each component is independently checked).

**Complexity:** `O(V + E)`.

### 14.3 Checking Bipartiteness — DFS

```python
def is_bipartite_dfs(n, graph):
    color = [-1] * n

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for v in range(n):
        if color[v] == -1:
            if not dfs(v, 0):
                return False
    return True
```

### 14.4 Edge Cases

- Graph with no edges → trivially bipartite (any 2-coloring works).
- Disconnected graph → check each component independently.
- Self-loop → automatically **not** bipartite (a node can't be a different color from itself).

### 14.5 Common Mistakes

- Not handling disconnected components — must loop over all unvisited vertices.
- Forgetting that a self-loop makes bipartiteness impossible.
- Confusing "bipartite" with "2 connected components" — they are unrelated concepts.

### 14.6 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Is Graph Bipartite? | LeetCode 785 | BFS/DFS 2-coloring |
| Possible Bipartition | LeetCode 886 | 2-coloring with constraints |
| Bipartite Graph | GeeksforGeeks | Basic bipartite check |

---

## 15. Euler Path, Circuit & Hamiltonian Path

### 15.1 Euler Path & Circuit

**Definition:** An **Euler path** visits **every edge exactly once**. An **Euler circuit** is an Euler path that starts and ends at the same vertex.

**Historical origin:** This is literally the original graph theory problem — Euler's 1736 solution to the Seven Bridges of Königsberg proved no such walk existed for that city's bridge layout.

**Existence Conditions (Undirected Graph):**
| Condition | Result |
|---|---|
| All vertices have even degree, graph connected | Euler **Circuit** exists |
| Exactly 2 vertices have odd degree, rest even, graph connected | Euler **Path** exists (must start/end at the odd-degree vertices) |
| More than 2 odd-degree vertices | Neither exists |

```
Euler Circuit example (all even degrees):
   (A)---(B)
    |     |
   (D)---(C)
deg(A)=deg(B)=deg(C)=deg(D)=2 (all even) -> Euler circuit exists
e.g., A -> B -> C -> D -> A
```

```python
def has_euler_path_or_circuit(n, graph):
    odd_count = sum(1 for v in range(n) if len(graph[v]) % 2 != 0)
    if odd_count == 0:
        return "Euler Circuit"
    elif odd_count == 2:
        return "Euler Path"
    else:
        return "Neither"
```

**Finding the actual Euler path — Hierholzer's Algorithm:**

```python
def find_euler_circuit(n, graph):
    """
    graph: adjacency list with edge multiplicities preserved (use lists, remove used edges)
    Assumes an Euler circuit exists.
    """
    adj = {u: list(neighbors) for u, neighbors in graph.items()}
    stack = [0]
    circuit = []

    while stack:
        node = stack[-1]
        if adj[node]:
            next_node = adj[node].pop()
            adj[next_node].remove(node)     # remove the edge in both directions
            stack.append(next_node)
        else:
            circuit.append(stack.pop())      # dead end -> add to circuit

    return circuit[::-1]
```

**Line-by-line explanation:** Hierholzer's algorithm greedily walks edges, pushing to a stack; when stuck (no more unused edges from current node), it backtracks and records the node into the circuit — this naturally produces a valid Euler circuit in `O(E)` time.

### 15.2 Hamiltonian Path (Overview)

**Definition:** A **Hamiltonian path** visits every **vertex** exactly once (contrast with Euler path, which visits every **edge** exactly once). A **Hamiltonian circuit** returns to the start.

**Why it's different/harder:** Unlike Euler paths (checkable in `O(V+E)` via degree conditions), determining whether a Hamiltonian path exists is **NP-complete** — no known polynomial-time algorithm. For small `n`, it's solved via backtracking or bitmask DP (Held-Karp, `O(2^n × n^2)`), which is the same technique used for the Traveling Salesman Problem.

```python
def has_hamiltonian_path(n, graph):
    def backtrack(node, visited, count):
        if count == n:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                if backtrack(neighbor, visited, count + 1):
                    return True
                visited.remove(neighbor)     # backtrack
        return False

    for start in range(n):
        if backtrack(start, {start}, 1):
            return True
    return False
```

> ⚠️ **Interview Note:** Hamiltonian path/circuit problems are rarely asked to be solved optimally in interviews (since it's NP-complete) — they're more often asked conceptually ("why is this different from Euler path?") or with small, bounded `n` where brute-force/backtracking or bitmask DP is acceptable.

### 15.3 Euler vs Hamiltonian — Quick Comparison

| | Euler Path/Circuit | Hamiltonian Path/Circuit |
|---|---|---|
| Visits every... | Edge exactly once | Vertex exactly once |
| Existence check | O(V+E) — simple degree rule | NP-complete — no known polynomial check |
| Classic algorithm | Hierholzer's | Backtracking / Held-Karp DP |

### 15.4 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Reconstruct Itinerary | LeetCode 332 | Euler path (Hierholzer's) |
| Valid Arrangement of Pairs | LeetCode 2097 | Euler path construction |
| Hamiltonian Path | GeeksforGeeks | Backtracking |
| Travelling Salesman Problem | GeeksforGeeks / CSES | Bitmask DP (Held-Karp) |


---

## 16. Maximum Flow

### 16.1 Definition & Why It Exists

Given a directed graph where each edge has a **capacity**, the **maximum flow** problem asks: what is the greatest amount of "flow" that can be pushed from a source `s` to a sink `t`, respecting capacity constraints on every edge? It models real bottleneck problems — network bandwidth, traffic flow, fluid through pipes, bipartite matching (as a flow problem), and project scheduling.

**Real-world analogy:** Water pipes — each pipe (edge) has a maximum flow rate (capacity); how much total water can flow from the reservoir (source) to the city (sink)?

```
     10        5
 S -----> A -----> T
 |                  ^
 |        10        |
 +------> B --------+
             15

Max flow from S to T is limited by the bottleneck capacities along used paths.
```

### 16.2 Ford-Fulkerson Method

**Intuition:** Repeatedly find any **augmenting path** (a path from `s` to `t` with available capacity) using DFS/BFS, push as much flow as the bottleneck (minimum capacity edge) along that path allows, and update a **residual graph** (which also includes reverse edges representing flow that could be "undone"). Repeat until no augmenting path remains.

```python
def ford_fulkerson(n, capacity, s, t):
    """
    capacity: n x n matrix, capacity[u][v] = capacity of edge u->v (0 if no edge)
    """
    residual = [row[:] for row in capacity]     # copy — residual capacities
    max_flow = 0

    def bfs_find_path():
        parent = [-1] * n
        parent[s] = s
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v in range(n):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    if v == t:
                        return parent
                    queue.append(v)
        return None

    while True:
        parent = bfs_find_path()
        if parent is None:
            break                      # no augmenting path left

        # find bottleneck capacity along the path
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        # update residual capacities along the path
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= path_flow      # forward edge: reduce capacity
            residual[v][u] += path_flow      # reverse edge: allow "undoing" flow
            v = u

        max_flow += path_flow

    return max_flow
```

**Line-by-line explanation:**
- We use BFS to find augmenting paths — this specific variant (Ford-Fulkerson using BFS) is called **Edmonds-Karp** (see below).
- The **residual graph** tracks remaining capacity; pushing flow along `u->v` reduces `residual[u][v]` but **increases** `residual[v][u]` — this reverse edge lets a later augmenting path "cancel" a suboptimal earlier choice, which is essential for correctness.
- We repeat until BFS can no longer find any path from `s` to `t` in the residual graph — at that point, max flow is achieved (by the Max-Flow Min-Cut theorem).

**Complexity:** Ford-Fulkerson's complexity depends on the path-finding strategy:
- Generic DFS-based Ford-Fulkerson: `O(E × max_flow)` — can be slow if capacities are large integers (not polynomial in input size alone).
- **Edmonds-Karp** (BFS-based, as coded above): `O(V × E²)` — polynomial, because BFS always finds the shortest augmenting path, bounding the number of iterations.

### 16.3 Edmonds-Karp — Why BFS Instead of DFS Matters

Using BFS (shortest augmenting path by edge count) instead of DFS guarantees the number of augmentations is bounded polynomially (`O(V×E)` augmentations, each found in `O(E)` BFS time → `O(VE²)` total). Plain DFS-based Ford-Fulkerson has no such guarantee and can be pathologically slow on adversarial capacity values.

### 16.4 Dinic's Algorithm (Overview)

**Intuition:** Dinic's improves on Edmonds-Karp by building **level graphs** (BFS layering) and finding **all augmenting paths at that level simultaneously** using DFS with pointers (blocking flow), rather than one path per BFS call.

**Complexity:** `O(V² × E)` in general graphs, `O(E × √V)` for unit-capacity graphs (e.g., bipartite matching) — significantly faster than Edmonds-Karp in practice, and the standard choice in competitive programming for max-flow problems.

### 16.5 Max-Flow Min-Cut Theorem

**Statement:** The maximum flow from `s` to `t` equals the **minimum capacity cut** separating `s` from `t` — i.e., the smallest total capacity of edges you'd need to remove to fully disconnect `s` from `t`.

**Why it matters:** This duality means max-flow algorithms can directly answer "min-cut" questions (e.g., network reliability: minimum links to sever to isolate a target).

### 16.6 Bipartite Matching as a Flow Problem

Maximum bipartite matching (e.g., "match applicants to jobs, each applicant to at most one job") can be reduced to max-flow: add a source connected to all left-side nodes (capacity 1 each), a sink connected from all right-side nodes (capacity 1 each), and capacity-1 edges between compatible pairs. Max flow = maximum matching size.

```
S -> [applicants] -> [jobs] -> T   (all capacities = 1)
Max Flow(S,T) = Max Bipartite Matching
```

### 16.7 Edge Cases

- No path from `s` to `t` at all → max flow = 0.
- `s == t` → undefined/trivial (usually treated as 0 or disallowed by problem constraints).
- Disconnected graph → max flow limited to 0 for unreachable sink.

### 16.8 Common Mistakes

- Forgetting to add **reverse residual edges** — without them, the algorithm can get stuck in a suboptimal flow configuration and never find the true maximum.
- Using DFS instead of BFS and hitting worst-case slow performance on certain capacity configurations.
- Confusing "capacity" with "flow" — capacity is the maximum limit; flow is the amount currently being pushed (must never exceed capacity).

### 16.9 Practice Problems

| Problem | Platform | Pattern |
|---|---|---|
| Maximum Flow | CSES | Edmonds-Karp / Dinic's |
| Maximum Bipartite Matching | GeeksforGeeks | Flow-based matching |
| Distribute Candies to People / Job Assignment | GeeksforGeeks | Bipartite matching (Hungarian algorithm / max-flow) |
| Fruits Into Baskets style flow problems | Codeforces | Max-flow modeling |


---

## 17. Advanced Graph Concepts

### 17.1 Transitive Closure

**Definition:** For every pair `(u,v)`, determine whether `v` is reachable from `u` at all (boolean reachability, ignoring weights/distance).

```python
def transitive_closure(n, graph):
    reach = [[False] * n for _ in range(n)]
    for i in range(n):
        reach[i][i] = True
    for u in graph:
        for v in graph[u]:
            reach[u][v] = True

    for k in range(n):                # Floyd-Warshall style DP
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return reach
```
**Complexity:** `O(V³)` using the Floyd-Warshall pattern, or `O(V × (V+E))` by running BFS/DFS from every vertex.

### 17.2 Graph Coloring

**Definition:** Assign colors to vertices such that no two adjacent vertices share a color, using the minimum number of colors possible (the **chromatic number**). Determining the exact minimum is NP-hard in general, but checking **k-colorability** for small `k` (especially `k=2`, i.e., bipartite check) is efficient.

**Application:** Register allocation in compilers, scheduling (exam timetabling — no student should have two exams at once), map coloring (adjacent regions differ).

```python
def can_color_with_k(n, graph, k):
    colors = [-1] * n

    def backtrack(node):
        if node == n:
            return True
        for c in range(k):
            if all(colors[neighbor] != c for neighbor in graph[node] if colors[neighbor] != -1):
                colors[node] = c
                if backtrack(node + 1):
                    return True
                colors[node] = -1
        return False

    return backtrack(0)
```

### 17.3 Binary Lifting (Overview)

**Definition:** A technique to answer "kth ancestor" or LCA (Lowest Common Ancestor) queries in `O(log n)` by precomputing `up[k][v]` = the `2^k`-th ancestor of `v`, built via `up[k][v] = up[k-1][up[k-1][v]]`. While traditionally taught in tree contexts, it generalizes to any DAG/functional graph where you need fast "jump ahead N steps" queries.

### 17.4 Lowest Common Ancestor — Graph Perspective

In a general graph context (not just trees), LCA-style reasoning appears in DAG problems (e.g., "common ancestor task in a dependency DAG") — solved via binary lifting on a BFS/DFS tree built from the DAG, or via SCC condensation followed by tree-LCA techniques.

### 17.5 Network Flow — Matching (Overview)

Beyond simple bipartite matching (Section 16.6), more advanced matching includes:
- **Maximum weight bipartite matching** — solved via the **Hungarian Algorithm**, `O(V³)`.
- **General graph matching** (not bipartite) — solved via **Edmonds' Blossom Algorithm**, `O(V³)`, handling odd-length cycles ("blossoms") that break simple bipartite techniques.

> These are advanced/competitive-programming topics rarely required in standard software interviews but valuable to know conceptually for research, operations research, or highly algorithmic roles.

### 17.6 Summary Table — Advanced Concepts

| Concept | Purpose | Typical Complexity |
|---|---|---|
| Transitive Closure | All-pairs reachability | O(V³) |
| Graph Coloring | Minimum colors, no adjacent conflict | NP-hard in general; O(V×k) per attempt for fixed k |
| Binary Lifting | Fast ancestor/jump queries | O(log n) per query after O(n log n) preprocessing |
| LCA (graph/DAG) | Common ancestor queries | O(log n) with binary lifting |
| Hungarian Algorithm | Max weight bipartite matching | O(V³) |
| Blossom Algorithm | General graph matching | O(V³) |


---

## 18. Graph Patterns for Interviews

Almost every graph interview question is a variation on one of these core patterns.

### 18.1 Pattern: Plain DFS/BFS Traversal
**Recognize when:** "Can you reach X from Y?", "how many nodes are reachable?", basic exploration.
**Template:** Section 5.

### 18.2 Pattern: Grid as Implicit Graph
**Recognize when:** Input is a 2D matrix; movement is up/down/left/right (or diagonals).
**Template:** Treat `(row, col)` as a node; neighbors computed via direction vectors; use BFS/DFS as in Section 6.

```python
DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]
def get_neighbors(r, c, rows, cols):
    for dr, dc in DIRECTIONS:
        nr, nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc
```

### 18.3 Pattern: Multi-Source BFS
**Recognize when:** Multiple starting points, need shortest distance to *any* of them (e.g., "rotting oranges," "walls and gates").
**Template:** Section 5.3.

### 18.4 Pattern: Union-Find for Dynamic Connectivity
**Recognize when:** Edges/connections are added incrementally, and you need to repeatedly answer "are these connected?" or detect the edge that first creates a cycle.
**Template:** Section 11.

### 18.5 Pattern: Topological Sort for Ordering/Dependencies
**Recognize when:** Words like "prerequisite," "must come before," "build order," "schedule," "dependency."
**Template:** Section 8.

### 18.6 Pattern: Dijkstra / Weighted Shortest Path
**Recognize when:** Edges have varying costs/times, need shortest/cheapest/minimum path, all weights non-negative.
**Template:** Section 9.3.

### 18.7 Pattern: Cycle Detection
**Recognize when:** "Detect if a cycle exists," "can all tasks be finished," "is this a valid tree."
**Template:** Section 7.

### 18.8 Pattern: State-Space Search (Implicit Graphs)
**Recognize when:** The "graph" isn't given explicitly — states are generated on the fly (e.g., word ladder: each word is a node, edges connect words differing by one letter).

```python
def word_ladder_bfs(begin, end, word_list):
    word_set = set(word_list)
    if end not in word_set:
        return 0
    queue = deque([(begin, 1)])
    visited = {begin}
    while queue:
        word, steps = queue.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                candidate = word[:i] + c + word[i+1:]
                if candidate in word_set and candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate, steps + 1))
    return 0
```
This is a graph problem where the adjacency list is **generated lazily** rather than given — a very common advanced pattern (LeetCode 127 "Word Ladder").

### 18.9 Pattern: Graph Coloring / Bipartite Check
**Recognize when:** "Divide into two groups," "no two adjacent can be the same," "is this graph 2-colorable."
**Template:** Section 14.

### 18.10 Pattern Recognition Summary Table

| Keyword / Clue in Problem | Likely Pattern |
|---|---|
| "shortest path," equal weight edges | BFS |
| "shortest path," varying weights, non-negative | Dijkstra |
| "shortest path," negative weights | Bellman-Ford |
| "all pairs shortest path" | Floyd-Warshall |
| "minimum cost to connect all" | MST (Kruskal/Prim) |
| "prerequisite," "build order," "can finish all" | Topological Sort |
| "detect cycle" | DFS (color-based) / Union-Find |
| "connected components," "provinces," "islands" | DFS/BFS/Union-Find |
| "divide into two groups," "bipartition" | Bipartite check |
| "critical connection," "single point of failure" | Bridges / Articulation Points |
| "strongly connected," "mutual reachability" | Kosaraju's / Tarjan's SCC |
| "maximum matching," "assign X to Y" | Bipartite Matching / Max Flow |
| "word transformations," "implicit states" | BFS on implicit/generated graph |
| "rotting," "spreading," "multiple sources" | Multi-source BFS |


---

## 19. Problem Recognition — Decision Trees

### 19.1 Master Decision Flowchart

```
START: Is the input already a graph, or do you need to build one?
│
├── Grid/matrix input? ──────────────► Treat cells as nodes (Section 18.2)
│
├── Words/states with implicit transitions? ─► Implicit graph + BFS (Section 18.8)
│
└── Explicit graph (edges/adjacency given)
    │
    ├── Need shortest path?
    │   ├── Unweighted ─────────────► BFS
    │   ├── Weighted, non-negative ─► Dijkstra
    │   ├── Weighted, negative ─────► Bellman-Ford
    │   └── All pairs ──────────────► Floyd-Warshall
    │
    ├── Need to order/schedule tasks? ──► Topological Sort (DFS or Kahn's)
    │
    ├── Need min cost to connect all nodes? ─► MST (Kruskal/Prim)
    │
    ├── Need dynamic "are these connected?" ─► Union-Find
    │
    ├── Need to detect a cycle?
    │   ├── Undirected ──────────────► DFS parent-check / Union-Find
    │   └── Directed ────────────────► DFS 3-color / Kahn's
    │
    ├── Need mutual reachability (directed)? ─► SCC (Kosaraju's/Tarjan's)
    │
    ├── Need single points of failure? ──► Bridges / Articulation Points
    │
    ├── Need 2-group partition? ─────────► Bipartite Check
    │
    └── Need max matching/throughput? ───► Max Flow (Ford-Fulkerson/Dinic)
```

### 19.2 DFS vs BFS Decision

```
Does the problem need shortest path / levels / minimum steps?
    YES -> BFS
    NO  -> Does it need to explore all paths, backtrack, or check connectivity?
              YES -> DFS
              NO  -> Either works; pick based on graph shape (deep&narrow -> BFS,
                     wide&shallow -> DFS for lower memory)
```

### 19.3 Dijkstra vs Bellman-Ford Decision

```
Are all edge weights non-negative?
    YES -> Dijkstra (faster: O((V+E) log V))
    NO  -> Does the problem require detecting negative cycles?
              YES -> Bellman-Ford
              NO but negative edges exist -> Bellman-Ford (Dijkstra is unsafe)
```

### 19.4 Kruskal vs Prim Decision

```
Is the input a flat edge list, and is the graph sparse?
    YES -> Kruskal (sort edges + Union-Find)
    NO (dense graph, adjacency list/matrix given) -> Prim (heap-based growth)
```

### 19.5 Union-Find Recognition

```
Does the problem involve:
  - Incrementally adding edges/connections?
  - Repeated "are X and Y connected?" queries?
  - Finding the FIRST edge that creates a cycle/redundant connection?
      YES to any -> Union-Find is likely the cleanest solution
```

### 19.6 Topological Sort Recognition

```
Does the problem mention:
  - "prerequisite" / "must come before" / "depends on"?
  - "valid order to complete all tasks"?
  - A DAG structure is implied or given?
      YES -> Topological Sort (DFS-based or Kahn's)
```

### 19.7 Grid → Graph Conversion Checklist

1. Each cell `(r, c)` is a node.
2. Neighbors = adjacent cells passing the problem's validity rule (in bounds, correct value, not visited).
3. Decide 4-directional vs 8-directional connectivity from the problem statement.
4. Choose BFS for shortest-distance-style grid problems, DFS/flood-fill for pure connectivity/region-counting problems.


---

## 20. Optimization Guide

### 20.1 Brute Force → Optimized Graph Thinking

| Naive Approach | Why It's Slow | Optimized Approach |
|---|---|---|
| Re-running BFS/DFS for every connectivity query | O(V+E) per query | Union-Find: ~O(1) amortized per query |
| Checking all pairs for shortest path via BFS from each node | O(V×(V+E)) | Floyd-Warshall O(V³) (better for small dense V), or Johnson's for sparse |
| Brute-force all edge subsets for MST | O(2^E) | Kruskal's/Prim's O(E log E) |
| DFS-based Ford-Fulkerson with arbitrary paths | Can be exponential on adversarial capacities | Edmonds-Karp (BFS) O(VE²), or Dinic's O(V²E) |
| Recomputing shortest path from scratch after every edge relaxation | Redundant work | Dijkstra's greedy finalization avoids reprocessing |

### 20.2 Adjacency List vs Matrix — Optimization Impact

- Switching from adjacency matrix to adjacency list on a sparse graph can turn an `O(V²)` traversal into `O(V+E)` — critical when `V` is large (e.g., `V > 10^4`).
- Conversely, if the algorithm needs O(1) edge-existence checks repeatedly (like Floyd-Warshall), a matrix avoids `O(deg(u))` linear scans of adjacency lists.

### 20.3 Heap Optimization (Dijkstra, Prim, A*)

Using a binary heap (`heapq`) turns the "find minimum unvisited distance" operation from `O(V)` (linear scan) into `O(log V)`, changing overall complexity from `O(V²)` to `O((V+E) log V)` — a massive win on sparse graphs. For extremely performance-critical code, a **Fibonacci heap** theoretically improves Dijkstra to `O(E + V log V)`, though it's rarely implemented in practice due to high constant factors.

### 20.4 Path Compression & Union by Rank — Optimization Impact

Without these Union-Find optimizations, operations can degrade to `O(V)` in the worst case (e.g., union operations forming a long chain). With both optimizations, operations become `O(α(V))` — practically constant, a critical difference at scale (e.g., 10^6 union/find operations).

### 20.5 Time Optimization Checklist

- Avoid recomputing `len(graph[node])` or rebuilding adjacency structures inside loops.
- Use `deque` instead of `list` for BFS queues (`list.pop(0)` is `O(n)`; `deque.popleft()` is `O(1)`).
- Use `heapq` instead of manually scanning for the minimum in Dijkstra/Prim.
- Precompute in-degrees once for Kahn's algorithm rather than recalculating.
- For repeated `find()` calls, ensure path compression is applied every single time (not conditionally).

### 20.6 Space Optimization Checklist

- Use adjacency lists (`O(V+E)`) instead of matrices (`O(V²)`) for sparse graphs.
- For BFS/DFS visited tracking on graphs with integer nodes `0..n-1`, prefer a `list`/array over a `set` — arrays have lower constant-factor overhead.
- For very large graphs where recursion depth would exceed Python's limit, convert recursive DFS to iterative to avoid excessive stack frame memory.
- Free/discard intermediate structures (like a transpose graph in Kosaraju's) once no longer needed, especially in memory-constrained environments.


---

## 21. Python Tips for Graph Problems

### 21.1 `collections.deque` — For BFS Queues

```python
from collections import deque
queue = deque([start])
queue.append(x)        # O(1) enqueue
queue.popleft()         # O(1) dequeue -- NEVER use list.pop(0), which is O(n)
```

### 21.2 `heapq` — For Priority Queues (Dijkstra, Prim, A*)

```python
import heapq
heap = []
heapq.heappush(heap, (distance, node))     # push (priority, item)
dist, node = heapq.heappop(heap)           # pop smallest priority
```
Python's `heapq` is a **min-heap only**. For a max-heap, negate the values you push: `heapq.heappush(heap, (-value, node))`.

### 21.3 `defaultdict` — For Adjacency Lists

```python
from collections import defaultdict
graph = defaultdict(list)
graph[u].append(v)     # no need to check "if u not in graph" first
```

### 21.4 `set` — For Visited Tracking & Fast Membership

```python
visited = set()
if node not in visited:    # O(1) average lookup, vs O(n) for a list
    visited.add(node)
```

### 21.5 Recursion Limits & `sys.setrecursionlimit`

Python's default recursion limit is 1000 — recursive DFS on graphs with long chains (e.g., a 5000-node linked-list-like graph) will crash with `RecursionError`.

```python
import sys
sys.setrecursionlimit(10**6)   # raise the limit for deep recursive DFS
```
> ⚠️ Even after raising the limit, very deep recursion can hit the actual **C stack limit** and segfault. For graphs with unbounded depth, prefer **iterative DFS**.

### 21.6 `itertools` — Useful Helpers

```python
from itertools import combinations
for u, v in combinations(range(n), 2):   # all pairs -- useful for building complete graphs
    ...
```

### 21.7 `dataclass` — Cleaner Edge/Node Representations

```python
from dataclasses import dataclass

@dataclass
class Edge:
    u: int
    v: int
    weight: int

edges = [Edge(0, 1, 4), Edge(1, 2, 2)]
```

### 21.8 Memory & Performance Tips

- Prefer tuples `(neighbor, weight)` over dicts/objects for adjacency list entries — tuples have lower memory overhead and faster attribute access via indexing.
- For very large graphs, consider using arrays (`array` module) or NumPy arrays instead of Python lists/dicts for `disc`, `low`, `visited`, `dist` arrays — this significantly reduces memory footprint at scale.
- Avoid rebuilding the adjacency list on every function call — build it once and pass it by reference.

### 21.9 Common Python Pitfalls Specific to Graphs

- **Mutable default arguments**: `def dfs(graph, node, visited=set()):` — the default `set()` is created **once** and shared across all calls, causing stale state across separate invocations. Always use `None` and initialize inside the function.
- **Shallow vs deep copy of adjacency structures**: `graph.copy()` on a `defaultdict(list)` copies the dict but not the inner lists — mutating a neighbor list in the copy can affect the original.
- **Iterating over a dict while modifying it**: `for u in graph: graph[u].append(...)` can raise `RuntimeError: dictionary changed size during iteration` if the modification adds new keys.


---

## 22. Common Mistakes (Consolidated Reference)

| Mistake | Where It Happens | Fix |
|---|---|---|
| Forgetting the `visited` set | Any traversal | Always track visited; mark at push/enqueue time for BFS |
| Marking visited at pop-time instead of push-time in BFS | BFS | Mark visited when enqueuing to avoid duplicate queue entries |
| Confusing directed vs undirected cycle detection logic | Cycle Detection | Use parent-tracking for undirected, 3-color for directed |
| Wrong loop order in Floyd-Warshall | Shortest Path | `k` must be the outermost loop |
| Using Dijkstra with negative weights | Shortest Path | Switch to Bellman-Ford |
| Forgetting path compression / union by rank | Union-Find | Always implement both for O(α(V)) performance |
| Not reversing the stack in DFS-based topo sort | Topological Sort | Reverse post-order stack before returning |
| Not checking `len(order) != n` in Kahn's algorithm | Topological Sort | This check is how you detect a cycle |
| Using `low[v]` instead of `disc[v]` for back edges in Tarjan's SCC | SCC | Use `disc[v]` for back-edge updates, `low[v]` only for tree-edge propagation |
| Swapping `>` and `>=` between bridge and articulation point conditions | Bridges/Articulation Points | Bridge: `low[v] > disc[u]`. Articulation: `low[v] >= disc[u]` |
| Not special-casing the DFS root in articulation points | Articulation Points | Root is an AP only if it has 2+ DFS children |
| Forgetting reverse residual edges | Max Flow | Always add/update the reverse edge during augmentation |
| Off-by-one indexing (0-indexed vs 1-indexed nodes) | Everywhere | Clarify indexing convention up front; convert consistently |
| Mutable default arguments (`visited=set()`) | Python-specific | Use `None` as default, initialize inside function |
| Not handling disconnected components | Traversal, Cycle Detection, Bipartite Check | Loop over all vertices, start new traversal for each unvisited one |

---

## 23. Cheat Sheets

### 23.1 Graph Representation Cheat Sheet

```python
# Adjacency List (default choice)
graph = defaultdict(list)
graph[u].append(v)                    # unweighted
graph[u].append((v, w))               # weighted

# Adjacency Matrix
matrix = [[0]*n for _ in range(n)]
matrix[u][v] = 1                      # or weight

# Edge List
edges = [(u, v, w), ...]
```

### 23.2 Traversal Template Cheat Sheet

```python
# DFS (recursive)
def dfs(node, visited):
    visited.add(node)
    for nxt in graph[node]:
        if nxt not in visited:
            dfs(nxt, visited)

# BFS
def bfs(start):
    visited, queue = {start}, deque([start])
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
```

### 23.3 Shortest Path Cheat Sheet

| Need | Algorithm | Snippet Reference |
|---|---|---|
| Unweighted shortest path | BFS | Section 9.2 |
| Weighted, non-negative | Dijkstra | Section 9.3 |
| Negative weights / cycle detection | Bellman-Ford | Section 9.4 |
| All pairs | Floyd-Warshall | Section 9.5 |
| Heuristic-guided | A* | Section 9.6 |

### 23.4 MST Cheat Sheet

| Need | Algorithm |
|---|---|
| Edge list input, sparse graph | Kruskal's (sort + Union-Find) |
| Adjacency list input, dense graph | Prim's (heap-based) |

### 23.5 Union-Find Template Cheat Sheet

```python
parent = list(range(n))
rank = [0]*n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])     # path compression
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry: return False
    if rank[rx] < rank[ry]: rx, ry = ry, rx
    parent[ry] = rx
    if rank[rx] == rank[ry]: rank[rx] += 1
    return True
```

### 23.6 Complexity Master Table

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| DFS / BFS | O(V + E) | O(V) |
| Cycle Detection (undirected/directed) | O(V + E) | O(V) |
| Topological Sort (DFS / Kahn's) | O(V + E) | O(V) |
| Dijkstra (binary heap) | O((V+E) log V) | O(V+E) |
| Bellman-Ford | O(V × E) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| Kruskal's MST | O(E log E) | O(V+E) |
| Prim's MST (heap) | O(E log V) | O(V+E) |
| Union-Find (per op, amortized) | O(α(V)) ≈ O(1) | O(V) |
| Kosaraju's SCC | O(V + E) | O(V+E) |
| Tarjan's SCC / Bridges / AP | O(V + E) | O(V) |
| Ford-Fulkerson (generic) | O(E × max_flow) | O(V²) |
| Edmonds-Karp | O(V × E²) | O(V²) |
| Dinic's | O(V² × E) | O(V+E) |

### 23.7 Pattern Recognition Cheat Sheet

See Section 18.10 and Section 19 for the full decision trees and keyword-to-pattern mapping table.

### 23.8 Python Syntax Cheat Sheet

```python
from collections import deque, defaultdict
import heapq

# Queue
q = deque(); q.append(x); q.popleft()

# Min-heap
h = []; heapq.heappush(h, (priority, item)); heapq.heappop(h)

# Adjacency list
g = defaultdict(list)

# Infinity
INF = float('inf')
```


---

## 24. Practice Problem Bank

### 24.1 Basics & Representations

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Clone Graph | LeetCode 133 | Medium | DFS/BFS + hashmap |
| Find Center of Star Graph | LeetCode 1791 | Easy | Degree analysis |
| All Paths From Source to Target | LeetCode 797 | Medium | DFS backtracking |

### 24.2 DFS

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Number of Provinces | LeetCode 547 | Medium | DFS components |
| Employee Importance | LeetCode 690 | Easy | DFS tree-like graph |
| Keys and Rooms | LeetCode 841 | Medium | DFS reachability |
| Path with Maximum Gold | Code360 | Medium | DFS backtracking on grid |

### 24.3 BFS

| Problem | Problem | Difficulty | Pattern |
|---|---|---|---|
| Rotting Oranges | LeetCode 994 | Medium | Multi-source BFS |
| Word Ladder | LeetCode 127 | Hard | Implicit graph BFS |
| Snakes and Ladders | LeetCode 909 | Medium | BFS on implicit board graph |
| 01 Matrix | LeetCode 542 | Medium | Multi-source BFS |

### 24.4 Grid Problems

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Number of Islands | LeetCode 200 | Medium | Flood fill |
| Max Area of Island | LeetCode 695 | Medium | Flood fill + size |
| Surrounded Regions | LeetCode 130 | Medium | Boundary DFS/BFS |
| Pacific Atlantic Water Flow | LeetCode 417 | Hard | Multi-source DFS/BFS from boundaries |

### 24.5 Cycle Detection

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Course Schedule | LeetCode 207 | Medium | Directed cycle (Kahn's) |
| Graph Valid Tree | LeetCode 261 | Medium | Undirected cycle + connectivity |
| Redundant Connection | LeetCode 684 | Medium | Union-Find |
| Redundant Connection II | LeetCode 685 | Hard | Union-Find (directed variant) |

### 24.6 Topological Sort

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Course Schedule II | LeetCode 210 | Medium | Topo sort (order) |
| Alien Dictionary | LeetCode 269 | Hard | Build graph + topo sort |
| Minimum Height Trees | LeetCode 310 | Medium | Topological peeling |
| Parallel Courses III | LeetCode 2050 | Hard | Topo sort + DP on time |

### 24.7 Shortest Path

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Network Delay Time | LeetCode 743 | Medium | Dijkstra |
| Cheapest Flights Within K Stops | LeetCode 787 | Medium | Bellman-Ford (bounded) |
| Path With Minimum Effort | LeetCode 1631 | Medium | Dijkstra variant |
| Swim in Rising Water | LeetCode 778 | Hard | Dijkstra / binary search + BFS |
| Shortest Path in Binary Matrix | LeetCode 1091 | Medium | BFS (8-directional) |

### 24.8 MST

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Min Cost to Connect All Points | LeetCode 1584 | Medium | Prim's/Kruskal's |
| Connecting Cities With Minimum Cost | LeetCode 1135 | Medium | Kruskal's |
| Optimize Water Distribution in a Village | LeetCode 1168 | Hard | Kruskal's with virtual node |

### 24.9 Union-Find

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Accounts Merge | LeetCode 721 | Medium | Union-Find grouping |
| Satisfiability of Equality Equations | LeetCode 990 | Medium | Union-Find constraints |
| Number of Islands II | LeetCode 305 | Hard | Dynamic Union-Find |
| Smallest String With Swaps | LeetCode 1202 | Medium | Union-Find + sorting |

### 24.10 SCC

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Strongly Connected Components | GeeksforGeeks | Medium | Kosaraju's/Tarjan's |
| Course Schedule (SCC variant reasoning) | Codeforces (various) | Medium | SCC |
| Strongly Connected Component (Advanced) | CSES | Hard | Tarjan's |

### 24.11 Bridges & Articulation Points

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Critical Connections in a Network | LeetCode 1192 | Hard | Bridges (Tarjan's) |
| Articulation Points | GeeksforGeeks | Hard | Tarjan's |
| Bridges in a Graph | GeeksforGeeks | Hard | Tarjan's |

### 24.12 Bipartite

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Is Graph Bipartite? | LeetCode 785 | Medium | 2-coloring |
| Possible Bipartition | LeetCode 886 | Medium | 2-coloring with constraints |

### 24.13 Network Flow / Advanced

| Problem | Platform | Difficulty | Pattern |
|---|---|---|---|
| Maximum Flow | CSES | Hard | Edmonds-Karp/Dinic's |
| Maximum Bipartite Matching | GeeksforGeeks | Hard | Flow-based matching |
| Reconstruct Itinerary | LeetCode 332 | Hard | Euler path (Hierholzer's) |

### 24.14 Company-Wise Frequently Asked (General Guide)

| Company | Commonly Tests |
|---|---|
| Google | Dijkstra, Union-Find, BFS/DFS on grids, topological sort |
| Amazon | BFS/DFS, shortest path, connected components |
| Meta | Cycle detection, clone graph, BFS/DFS on trees-as-graphs |
| Microsoft | Topological sort, Union-Find, grid BFS |
| Bloomberg | Dijkstra, MST, dependency resolution |

> Note: Company-specific patterns shift over time; treat this as a general guide, not a guarantee, and always verify against current interview experiences (e.g., LeetCode Discuss, Blind).

### 24.15 Blind 75 / NeetCode Graph Subset

The most commonly recommended graph problems from the Blind 75 / NeetCode 150 lists: Number of Islands, Clone Graph, Course Schedule, Pacific Atlantic Water Flow, Number of Connected Components in an Undirected Graph, Graph Valid Tree, Word Ladder, Alien Dictionary. These cover DFS/BFS, Union-Find, topological sort, and implicit-graph BFS — the core skill set for most interviews.


---

## 25. Final Revision & Roadmap

### 25.1 One-Page Summary

```
GRAPH REPRESENTATIONS: Adjacency List (default) | Matrix (dense/O(1) lookup) | Edge List (Kruskal/Bellman-Ford)

TRAVERSAL:      DFS = go deep, backtrack | BFS = go wide, level by level

CYCLE:          Undirected -> parent-check DFS or Union-Find
                Directed   -> 3-color DFS or Kahn's (leftover nodes = cycle)

ORDERING:       Topological Sort -> DFS post-order reversed, OR Kahn's (in-degree 0 queue)

SHORTEST PATH:  Unweighted -> BFS
                Non-negative weights -> Dijkstra (heap)
                Negative weights -> Bellman-Ford (V-1 relaxations)
                All pairs -> Floyd-Warshall (k outermost!)

MST:            Kruskal (sort edges + Union-Find) | Prim (heap, grow from a vertex)

UNION-FIND:     find() with path compression + union() by rank/size = O(α(V)) ≈ O(1)

SCC:            Kosaraju (2 DFS passes + transpose) | Tarjan (1 pass, disc/low)

BRIDGES/AP:     Tarjan disc/low | Bridge: low[v] > disc[u] | AP: low[v] >= disc[u] (+ root special case)

BIPARTITE:      2-color BFS/DFS; fails on any odd cycle or self-loop

EULER:          0 or 2 odd-degree vertices (undirected) -> Euler circuit/path; Hierholzer's to construct

MAX FLOW:       Ford-Fulkerson + residual graph; BFS version = Edmonds-Karp O(VE²); Dinic's = fastest practical
```

### 25.2 Mind Map — Graph Algorithm Family Tree

```
                              GRAPHS
                                |
        ┌───────────┬──────────┼───────────┬─────────────┐
   Traversal    Connectivity  Ordering   Shortest Path   Flow/Matching
        |            |           |            |               |
   DFS, BFS    Union-Find,   Topological   BFS, Dijkstra,   Ford-Fulkerson,
   Multi-src   Components,   Sort (DFS/    Bellman-Ford,    Edmonds-Karp,
   BFS         Bipartite     Kahn's)       Floyd-Warshall,  Dinic's,
                                            A*               Bipartite Matching
        |            |
   SCC (Kosaraju,  Bridges &
   Tarjan)         Articulation Points
                   (Tarjan disc/low)
```

### 25.3 Algorithm Selection Guide (Quick Reference)

| If you need to... | Use... |
|---|---|
| Explore/reach all nodes | DFS or BFS |
| Find shortest path, no weights | BFS |
| Find shortest path, weighted, non-negative | Dijkstra |
| Find shortest path, negative weights possible | Bellman-Ford |
| Find all-pairs shortest paths | Floyd-Warshall |
| Connect all nodes at minimum cost | Kruskal's or Prim's |
| Check/track dynamic connectivity | Union-Find |
| Order tasks with dependencies | Topological Sort |
| Detect a cycle | DFS (color/parent) or Kahn's |
| Find mutually-reachable clusters (directed) | SCC (Kosaraju's/Tarjan's) |
| Find single points of failure | Bridges/Articulation Points |
| Split into two non-conflicting groups | Bipartite Check |
| Maximize flow/matching | Max Flow (Ford-Fulkerson family) |



### 25.5 1-Hour Revision

1. Re-implement from scratch (no peeking): DFS, BFS, Union-Find, Kahn's Topological Sort, Dijkstra, Kruskal's.
2. Dry-run each on a small hand-drawn graph (5-6 nodes) on paper.
3. Solve one problem from each category in Section 24 (Cycle Detection, MST, Shortest Path, Union-Find, Bipartite).
4. Review the Common Mistakes table (Section 22) and check you haven't repeated any of them.
5. Explain out loud (to yourself or a peer) WHY Dijkstra fails on negative weights, and WHY Floyd-Warshall needs `k` as the outer loop.

### 25.6 Interview-Day Cheat Sheet (Mental Checklist)

1. **Clarify the graph**: directed or undirected? Weighted? Possible negative weights? Connected or not?
2. **Choose representation**: adjacency list unless told otherwise.
3. **Identify the pattern** using Section 18.10 / Section 19's decision trees.
4. **State time/space complexity** before coding.
5. **Code the template**, adapting variable names to the problem's domain.
6. **Dry-run on the example input** the interviewer gave you.
7. **Discuss edge cases**: empty graph, disconnected graph, self-loops, single node.
8. **Discuss optimizations** if time remains (e.g., "we could use Union-Find here instead of re-running BFS").

### 25.7 Closing Note

Graphs are the single most versatile data structure in computer science — nearly every real-world system of relationships (social, physical, logical, or temporal) can be modeled as one. Mastering the "big six" (DFS, BFS, Union-Find, Dijkstra, Topological Sort, MST) unlocks the overwhelming majority of interview and real-world graph problems. Everything else in this handbook — SCC, bridges, flow, Euler/Hamiltonian paths — builds directly on those same `disc`/`low`/`visited`/`parent` primitives you've now practiced repeatedly.

