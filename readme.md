# Practice Exam: Uncountable Graph Functions and Bellman-Ford Algorithm

This exam is designed to deepen your understanding of graphs by exploring uncountable graphs, and also requires you to implement fundamental algorithms like Bellman-Ford. You will create a robust `Graph` class, handle infinite vertex and edge sets, and develop visualization and algorithmic solutions.

---

## Introduction to Infinite Graphs

In graph theory, **infinite graphs** are graphs that contain an infinite number of vertices, edges, or both. They are divided into two categories:

1. **Countably Infinite Graphs**: The vertices of these graphs can be listed or enumerated, much like the set of natural numbers. An example is a graph where each integer represents a vertex and edges connect adjacent integers (e.g., in a line or grid).



2. **Uncountably Infinite Graphs**: These graphs have vertex sets that are so large they cannot be enumerated. An example of an uncountable set is the real numbers \( R \). For instance, consider a graph where vertices represent real numbers and two vertices are connected if their absolute difference equals 1. In this scenario, the vertex set is uncountable, and the graph's properties require non-standard approaches.

---

## Tasks and Guidelines

You will be building a `Graph` class that handles infinite graphs, implementing functions for common graph properties, and writing code to visualize these graphs. In addition, you will work on an implementation of the Bellman-Ford algorithm for shortest path problems.

### Task 1: Create a `Graph` Class Object
Put all of your code in a file called graph.py. You need to implement a Python class to represent a graph. This class should accommodate infinite graphs and include:

- A vertex set, which could be finite, countably infinite (e.g., integers), or uncountable (e.g., real numbers).
- An edge set, represented in a way that supports infinite graphs. For example, you could describe edges with a mathematical rule (e.g., connect vertices if their difference is 1).
  
*Considerations*: 
- How will you handle uncountable graphs like those involving real numbers?
- How will you handle edge definitions for infinite graphs?


### Task 2: Vertex Set Counter
Create a method that counts the number of vertices in the graph. 

- For finite graphs, the function should return an integer count.
- For countably infinite graphs, the function should return something like "The vertex set is countably infinite."
- For uncountable graphs, return "The vertex set is uncountable."

*Considerations*: 
- How will you differentiate between countably infinite and uncountable vertex sets in your code?

```python

def count_vertices(graph: Graph) -> int:
    return 0

```

#### Graph examples:
**2-Regular Uncountable Graph:**
The 2-regular uncountable graph has a vertex set defined as V=RV=R, and two vertices xx and yy are connected if ∣x−y∣=1∣x−y∣=1.

In Python, we'll represent a finite portion of this graph by considering a range of real numbers and linking any two vertices that are exactly 1 unit apart.
```python
from typing import List, Tuple

class TwoRegularGraph:
    def __init__(self, vertices: List[float]):
        self.vertices = vertices
        self.edges = self.generate_edges()

    def generate_edges(self) -> List[Tuple[float, float]]:
        edges = []
        for v in self.vertices:
            if v + 1 in self.vertices:
                edges.append((v, v + 1))
            if v - 1 in self.vertices:
                edges.append((v, v - 1))
        return edges

# Example usage:
vertices = [0.0, 1.0, 2.0, 3.0, 4.0]  # A finite portion of R
graph = TwoRegularGraph(vertices)
print("Vertices:", graph.vertices)
print("Edges:", graph.edges)
```
**Countably Infinite Graph:**
The countably infinite graph has a vertex set V=RV=R, and two vertices xx and yy are connected if x−y∈Q∖{0}x−y∈Q∖{0}, meaning the difference between the two vertices is a non-zero rational number.

In Python, we'll simulate this by using a set of rational numbers to define the connections between vertices.
```python
from fractions import Fraction
from typing import List, Tuple, Set

class CountablyInfiniteGraph:
    def __init__(self, vertices: List[float], rationals: Set[Fraction]):
        self.vertices = vertices
        self.rationals = rationals  # Set of rational numbers defining the edges
        self.edges = self.generate_edges()

    def generate_edges(self) -> List[Tuple[float, float]]:
        edges = []
        for v in self.vertices:
            for q in self.rationals:
                if v + float(q) in self.vertices:
                    edges.append((v, v + float(q)))
                if v - float(q) in self.vertices:
                    edges.append((v, v - float(q)))
        return edges

# Example usage:
vertices = [0.0, 0.5, 1.0, 1.5, 2.0]  # A finite portion of R
rationals = {Fraction(1, 2), Fraction(1, 3), Fraction(1)}  # Set of rationals
graph = CountablyInfiniteGraph(vertices, rationals)
print("Vertices:", graph.vertices)
print("Edges:", graph.edges)
```

### Task 3: Edge Set Counter
Write a method to count the number of edges in the graph.

- For finite graphs, return the number of edges.
- For infinite graphs, return an appropriate message indicating if the edge set is countably infinite or uncountable.

*Considerations*: 
- Similar to vertices, edges in infinite graphs need special handling. How can you describe the edges in an uncountable graph?

```python
def count_edges(graph: Graph) -> int:
    return 0
```


### Task 4: Degree of a Vertex
Develop a function that returns the **degree** of a specific vertex (i.e., the number of edges connected to the vertex).

- In a finite graph, this will be a number.
- In countably infinite graphs, a vertex can have an infinite degree (e.g., the number of rational points connected to a real number in the example graph).
- In uncountable graphs, the degree of a vertex may depend on the specific rule used to define connections.

*Considerations*: 
- What does "degree" mean for vertices in uncountable graphs, and how would you implement it?

```python
def degree_of_vertex(graph: Graph, vertex: int) -> int:
    return 0
```

### Task 5: Visualize an Infinite Grid
Create a Python function `visualize_infinite_grid(start, steps)` to simulate and print the first few nodes of an infinite 2D grid starting from a given node. 

- The grid is infinite, but the function should print only the first `steps` number of nodes.
- Each node in the grid is represented by its coordinates (x, y), and each node is connected to its immediate neighbors.

*Considerations*: 
- How will you visually represent the grid for a limited number of steps?
- Can you expand this visualization to more complex infinite graphs later?

```python
def visualize_infinite_grid(start: Tuple[int, int], steps: int) -> None:
```

### Task 6: Bellman-Ford Algorithm for Shortest Path
The Bellman-Ford algorithm computes the shortest paths from a given source vertex to all other vertices in a graph, even when edges have negative weights. Your task is to implement the **Bellman-Ford algorithm** in Python.

- Ensure the algorithm works with both finite and infinite graphs, considering that infinite graphs may require specialized handling.
  
*Considerations*: 
- How would you handle infinite graphs in the context of Bellman-Ford? 
- Could there be scenarios where infinite distances need to be considered?

```python
def bellman_ford(graph: Graph, source: int) -> Dict[int, float]:
    return {}
```

---

## Related Tasks

### Task 7: Breadth-First Search (BFS) in Infinite Graphs
Extend your `Graph` class to support a breadth-first search (BFS) algorithm. This algorithm should handle infinite graphs and return results within the first `n` steps.

- Use BFS to explore a specific region of a countably infinite graph.

```python
def bfs(graph: Graph, start: int, steps: int) -> List[int]:
    return []
```

### Task 8: Depth-First Search (DFS) in Infinite Graphs
Implement the depth-first search (DFS) algorithm for your `Graph` class. Like BFS, this should support infinite graphs but terminate after exploring the first `n` vertices or edges.

```python
def dfs(graph: Graph, start: int, steps: int) -> List[int]:
    return []
```

### Task 9: Graph Isomorphism Check
Write a function to determine if two finite graphs are isomorphic (i.e., if there is a one-to-one correspondence between their vertex sets and edge sets).

```python
def is_isomorphic(graph1: Graph, graph2: Graph) -> bool:
    return False
```

### Task 10: Infinite Graph Isomorphism Exploration
Speculate on methods for identifying isomorphisms between two infinite graphs. This task involves writing a short explanation rather than code.

```python
def connected_components(graph: Graph) -> List[List[int]]:
    return []
```

---

## Example Graphs

1. **2-Regular Uncountable Graph**: 
   - Vertex set \( V = R \)
   - Edge set defined by \( {x, y} \in E \) if and only if \( |x - y| = 1 \).
   
2. **Countably Infinite Graph**:
   - Vertex set \( V = R \)
   - Edge set defined by \( {x, y} \in E \) if and only if \( x - y \in Q \setminus \{0\} \).
   
---

## Submission
Submit the following:
1. Your Python `Graph` class code.
2. Functions for counting vertices, counting edges, and determining vertex degree.
3. The `visualize_infinite_grid(start, steps)` function.
4. Bellman-Ford algorithm implementation.
5. (Optional) Implementations of BFS, DFS, and isomorphism checks.

Make sure to comment your code thoroughly to explain your design decisions and how infinite graphs are handled.

## OLD Tasks (ignore this):

Consider the uncountable graph function:
An example of an uncountable graph is the simple graph G1 = (V (G1), E(G1))
where V (G1) = R and {x, y} ∈ E(G1) if and only if |x − y| = 1. Notice that this
is a 2-regular graph. A related example is Gq = (V (Gq), E(Gq)) where V (Gq) = R
and {x, y} ∈ E(Gq) if and only if x − y ∈ Q \ {0}. In this case, each vertex is
(countably) infinite in degree.


1. create a graph class object
2. write a function to count the vertex set 
3. write a function to count the edge set
4. Write a function to count the degree of a vertex
5. Create a Python function visualize_infinite_grid(start, steps) that prints the first steps number of nodes of an infinite grid starting from a node in a 2D coordinate system
6. 