import matplotlib.pyplot as plt
from typing import Callable, List, Tuple, Dict
import numpy as np
from itertools import permutations

class Graph:
    def __init__(self, edge_set:Callable[[int], List] = None, vertex_set: Callable[[int], List]= None, weights:Dict=None):
        self.edge_set = edge_set
        self.vertex_set = vertex_set
        self.build_adjacency_list()
        if weights is None:
            self.weights = None
        else:
            self.weights = dict(zip(edge_set,weights))

    def build_adjacency_list(self):
        adjacency_list = {}
        for node in self.vertex_set:
            adjacency_list[node] = []

        for u, v in self.edge_set:
            if v not in adjacency_list[u]:
                adjacency_list[u].append(v)
            
        self.edges = adjacency_list

def build_edge_list(adjacency_list):
    edges = []
    
    for u in adjacency_list:
        for v in adjacency_list[u]:
            edges.append((u, v))
    
    return edges


def count_vertices(graph: Graph) -> int:
    # Case 1: Countably finite
    count = 0
    if isinstance(graph.vertex_set, list):
        return len(graph.vertex_set)

    # Case 3: Uncountably infinite
    else:
        return "Uncountably infinite"
    
def count_edges(graph: Graph) -> int:
    # Case 1: Countably finite
    count = 0
    if isinstance(graph.edge_set, list):
        return len(graph.edge_set)
    # Case 2: Countably infinite
    elif isinstance(graph.edge_set, Callable):
        return "Countably infinite"

    # Case 3: Uncountably infinite
    else:
        return "Uncountably infinite"
    

def degree_of_vertex(graph: Graph, vertex: int) -> int:
    return len(graph.edges[vertex])

def visualize_infinite_grid(graph: Graph, start:int, steps: int) -> None:
    grid = {0:[]}
    visited = []
    if start in graph.vertex_set:
        print(start, end='-')
        for v in graph.edges[start]:
            grid[0].append(v)
    else:
        graph.vertex_set.append(start)
        if start + 1 in graph.vertex_set:
            graph.edges.append((start, start + 1))
        if start - 1 in graph.vertex_set:
            graph.edges.append((start, start - 1))
        for v in graph.edges[start]:
            grid[0].append(v)
    
    visited.append(start)
    
    for i in range(steps-1):
        grid[i+1] = []
        for node in grid[i]:
            if node in graph.vertex_set and node not in visited:
                print(node, end='-')
                for v in graph.edges[node]:
                    grid[i+1].append(v)
            elif node in visited:
                continue
            else:
                graph.vertex_set.append(node)
                if node + 1 in graph.vertex_set:
                    graph.edges.append((node, node + 1))
                if node - 1 in graph.vertex_set:
                    graph.edges.append((node, node - 1))
                for v in graph.edges[node]:
                    grid[i+1].append(v)

            visited.append(node)

        
def bellman_ford(graph: Graph, source: int) -> Dict[int, float]:
    distance = {}

    for v in graph.vertex_set:
        if v == source:
            distance[v] = 0
        else:
            distance[v] = np.inf

    if graph.weights is not None:
        for _ in range(len(graph.vertex_set)-1):   # |V| is the number of vertices
            for (u, v) in graph.edges:
                if distance[u] + graph.weights[(u,v)] < distance[v]:
                    distance[v] = distance[u] + graph.weights[(u,v)]

        # Step 3: Check for negative-weight cycles by one more relaxation
        for (u, v) in graph.edges:
            if distance[u] + graph.weights[(u,v)] < distance[v]:
                print("Graph contains a negative-weight cycle")

    else:
        for u in graph.edges:
            for v in graph.edges[u]:
                distance[v] = min(distance[v], distance[u] + 1)  # Assume all edges have weight 1

    return distance  # The shortest distance to each vertex from the source

def bfs(graph: Graph, start: int, target: int, max_iterations: int=100) -> List[int]:
    curr_node = start
    visited = [start]
    v_ind = 0
    full_graph = False
    parents = {start:None}

    if start == target:
        return [start]
    c_iter = 0
    while not full_graph and c_iter<max_iterations:
        curr_neigh = graph.edges[curr_node]
        for neighbour in curr_neigh:

            if neighbour not in parents.keys():
                parents[neighbour] = curr_node

            if neighbour == target:
                path = []
                curr = target
                path.append(target)
                while parents[curr] is not None:
                    curr = parents[curr]
                    path.append(curr)
                path.reverse()
                return path
            
            if neighbour not in visited:
                visited.append(neighbour)

        v_ind += 1
        if v_ind >= len(visited):
            return None
        curr_node = visited[v_ind]
        c_iter +=1


def dfs(graph: Graph, start: int, target: int, max_iterations: int=100) -> List[int]:
    curr_node = start
    stack = [start]
    visited = [start]
    parents = {start:None}
    
    if start == target:
        return [start]
    n_iter = 0
    while len(stack)>0 and n_iter<max_iterations:
        curr_node = stack.pop()
        curr_neigh = graph.edges[curr_node]
        curr_neigh.reverse()
        
        for neighbour in curr_neigh:
            if neighbour not in parents.keys():
                parents[neighbour] = curr_node
            if neighbour == target:
                path = []
                curr = target
                path.append(target)
                while parents[curr] is not None:
                    curr = parents[curr]
                    path.append(curr)
                path.reverse()
                return path
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
        n_iter +=1
    return None

def is_isomorphic(graph1: Graph, graph2: Graph) -> bool:
    if len(graph1.edge_set) != len(graph2.edge_set):
        return False
    if len(graph1.vertex_set) != len(graph2.vertex_set):
        return False
    
    degree_g1 = sorted([len(graph1.edges[v]) for v in graph1.vertex_set])
    degree_g2 = sorted([len(graph2.edges[v]) for v in graph2.vertex_set])
    
    if degree_g1 != degree_g2:
        return False

    # Assume 1-1 correct mapping
    mapping = dict(zip(graph1.vertex_set, graph2.vertex_set))

    new_edges = {}
    for v_b, neighbors_b in graph1.edges.items():
        v_a = mapping[v_b]
        relabeled_neighbors = [mapping[neighbor] for neighbor in neighbors_b]
        new_edges[v_a] = relabeled_neighbors
    if new_edges == graph2.edges:
        return True
    else:
        return False
    

def is_bipartite(graph1: Graph) -> bool:
    return len(connected_components(graph1)) == 2


def connected_components(graph: Graph) -> List[List[int]]:
    out = []
    first = True
    for edge in graph.edge_set:
        if first:
            out.append([edge[0], edge[1]])
            first = False
        elif (edge[0] in [item for sublist in out for item in sublist]):
            found = next((sublist for sublist in out if edge[0] in sublist), None)
            if edge[1] not in found:
                found.append(edge[1])
        elif (edge[1] in [item for sublist in out for item in sublist]):
            found = next((sublist for sublist in out if edge[1] in sublist), None)
            if edge[0] not in found:
                found.append(edge[0])
        else:
            out.append([edge[0], edge[1]])
    for node in graph.vertex_set:
        if node not in [item for sublist in out for item in sublist]:
            out.append([node])
    return out




if __name__ == "__main__":
    from typing import List, Tuple

    class TwoRegularGraph:
        def __init__(self, vertices: List[float]):
            self.vertex_set = vertices
            self.edge_set = self.generate_edges()
            self.edges = build_adjacency_list(self.edge_set)

        def generate_edges(self) -> List[Tuple[float, float]]:
            edges = []
            for v in self.vertex_set:
                if v + 1 in self.vertex_set:
                    edges.append((v, v + 1))
                if v - 1 in self.vertex_set:
                    edges.append((v, v - 1))
            return edges

    # Example usage:
    vertices = [0.0, 1.0, 2.0, 3.0, 4.0]  # A finite portion of R
    graph = TwoRegularGraph(vertices)
    print("Vertices:", graph.vertex_set)
    print("Edges:", graph.edge_set)
    visualize_infinite_grid(graph, 0.0, 4)