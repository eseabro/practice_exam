# Assignment: Uncountable Graph Functions and Bellman-Ford Algorithm

This assignment involves implementing various functionalities for handling uncountable graphs, as well as a task related to the Bellman-Ford algorithm. The goal is to create a robust `Graph` class and explore the properties of both countable and uncountable vertex sets.

## Tasks

### 1. Create a Graph Class Object
Your first task is to implement a Python class that represents a graph. This class should handle both countable and uncountable sets of vertices. You will need to decide how to represent the vertices and edges in such cases, especially when dealing with infinite sets.

### 2. Vertex Set Counter Function
Write a function that counts the number of vertices in the graph. For uncountable vertex sets (like the real numbers), return an appropriate message (e.g., "The vertex set is uncountable").

### 3. Edge Set Counter Function
Write a function to count the number of edges in the graph. Similarly to the vertex set, if the edge set is infinite, return an appropriate message.

### 4. Degree of a Vertex Function
Write a function that calculates and returns the degree of a given vertex. This function should work for both finite and infinite graphs, considering how degrees can be represented in infinite graphs (e.g., countable or uncountable).

### 5. Visualize an Infinite Grid
Create a Python function `visualize_infinite_grid(start, steps)` that prints the first `steps` number of nodes from a specified starting node in a 2D coordinate system. Assume that each node is connected to its immediate neighbors, forming a grid. The grid is infinite, and you should limit the output based on the `steps` parameter.

### 6. Bellman-Ford Algorithm
Write a Python function that implements the **Bellman-Ford** algorithm to find the shortest path from a given source node to all other nodes in a graph. Make sure the function handles both finite and infinite graphs appropriately.

## Example Graphs

1. **Uncountable 2-Regular Graph**: 
   - `V = R`
   - `{x, y} ∈ E` if and only if `|x − y| = 1`
   
2. **Countably Infinite Graph**: 
   - `V = R`
   - `{x, y} ∈ E` if and only if `x − y ∈ Q \ {0}`

## Submission
Submit the code for the following tasks:
1. `Graph` class
2. Function for counting vertices
3. Function for counting edges
4. Function for calculating the degree of a vertex
5. Function `visualize_infinite_grid(start, steps)`
6. Bellman-Ford algorithm implementation


OLD Tasks:

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