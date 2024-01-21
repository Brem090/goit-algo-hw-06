import networkx as nx
from collections import deque

social_network_graph = nx.Graph()

user_nodes = range(1, 10)

friendship_edges = [
    (1, 2), (1, 3), (1, 4),
    (2, 4), (2, 5),
    (3, 4), (3, 6),
    (4, 6), (4, 7),
    (5, 7), (5, 8),
    (6, 7), (6, 9),
    (7, 8), (7, 9),
    (8, 9)
]
social_network_graph.add_nodes_from(user_nodes)
social_network_graph.add_edges_from(friendship_edges)

# Перетворення графу у словник
graph_dict = nx.to_dict_of_lists(social_network_graph)

# Ітеративний DFS
def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    dfs_result = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            dfs_result.append(vertex)
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
    return dfs_result

# Ітеративний BFS
def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    bfs_result = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            bfs_result.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return bfs_result

dfs_result = dfs_iterative(graph_dict, 1)
bfs_result = bfs_iterative(graph_dict, 1)

print("Ітеративний пошук в глибину (DFS):", ", ".join(map(str, dfs_result)))
print("Ітеративний пошук в ширину (BFS):", ", ".join(map(str, bfs_result)))



