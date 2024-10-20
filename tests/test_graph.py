from src.graph import Graph
def sample_graph():
    vertices = {0: [], 1: [], 2: [], 3: []}
    edges = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1]
    }
    return Graph(build_edge_list(edges),list(vertices.keys()))

def build_edge_list(adjacency_list):
    edges = []
    
    for u in adjacency_list:
        for v in adjacency_list[u]:
            edges.append((u, v))
    
    return edges


def test_count_vertices():
    from src.graph import Graph, count_vertices
    assert count_vertices(sample_graph()) == 4

def test_count_edges():
    from src.graph import Graph, count_edges
    assert count_edges(sample_graph()) == 6

def test_degree_of_vertex():
    from src.graph import Graph, degree_of_vertex
    assert degree_of_vertex(sample_graph(), 0) == 2
    assert degree_of_vertex(sample_graph(), 1) == 2
    assert degree_of_vertex(sample_graph(), 2) == 1
    assert degree_of_vertex(sample_graph(), 3) == 1

def test_bellman_ford():
    from src.graph import Graph, bellman_ford
    paths = bellman_ford(sample_graph(), 0)
    assert paths[0] == 0
    assert paths[1] == 1
    assert paths[2] == 1
    assert paths[3] == 2

def test_bfs():
    from src.graph import Graph, bfs
    result = bfs(sample_graph(), 0, 3)
    expected = [0, 1, 3]
    assert result == expected

def test_dfs():
    from src.graph import Graph, dfs
    result = dfs(sample_graph(), 0, 3)
    expected = [0, 1, 3]  # Note that DFS can have different valid orders
    assert set(result) == set(expected)  # Check for membership

def is_isomorphic(graph1: Graph, graph2: Graph) -> bool:
    # Placeholder for the actual isomorphic check logic
    return False

# Test Cases for the is_isomorphic function
def test_is_isomorphic():
    # Graphs with the same structure
    graph_a = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
    }
    graph_b = {
        'a': ['b', 'c'],
        'b': ['a', 'c'],
        'c': ['a', 'b'],
    }
    assert is_isomorphic(graph_a, graph_b) is True

    # Graphs that are not isomorphic (different structures)
    graph_c = {
        0: [1],
        1: [0, 2],
        2: [1],
    }
    graph_d = {
        'x': ['y'],
        'y': ['x'],
    }
    assert is_isomorphic(graph_c, graph_d) is False

    # Graphs with different number of vertices
    graph_e = {
        0: [1],
        1: [0],
    }
    graph_f = {
        'p': ['q'],
        'q': ['p'],
        'r': []
    }
    assert is_isomorphic(graph_e, graph_f) is False

    # Empty graphs should be isomorphic
    graph_g = {}
    graph_h = {}
    assert is_isomorphic(graph_g, graph_h) is True

    # Graphs with one vertex and no edges should be isomorphic
    graph_i = {0: []}
    graph_j = {'a': []}
    assert is_isomorphic(graph_i, graph_j) is True

    
def test_is_bipartite():
    from src.graph import Graph, is_bipartite
    assert is_bipartite(sample_graph()) is True

def test_connected_components():
    from src.graph import Graph, connected_components
    components = connected_components(sample_graph())
    assert len(components) == 1
    assert set(components[0]) == {0, 1, 2, 3}

def test_empty_graph():
    from src.graph import Graph, count_vertices, count_edges
    empty_graph = Graph([], [])
    assert count_vertices(empty_graph) == 0
    assert count_edges(empty_graph) == 0

def test_single_node_graph():
    from src.graph import Graph, count_vertices, degree_of_vertex, is_bipartite, count_edges
    single_node = Graph([], [0])
    assert count_vertices(single_node) == 1
    assert count_edges(single_node) == 0
    assert degree_of_vertex(single_node, 0) == 0
    assert is_bipartite(single_node) is True

def test_disconnected_graph():
    from src.graph import Graph, connected_components
    vertices = {0: [], 1: [], 2: []}
    edges = {
        0: [1],
        1: [0],
        2: []  # Disconnected node
    }
    disconnected_graph = Graph(vertices, edges)
    assert len(connected_components(disconnected_graph)) == 2
