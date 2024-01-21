import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

social_network_graph = nx.Graph()

user_nodes = range(1, 10)

# Вага ребер - інтенсивність спілкування. Більша вага - більше спілкування, і навпаки.
friendship_edges = [
    (1, 2, 7), (1, 3, 9), (1, 4, 3),
    (2, 4, 2), (2, 5, 3),
    (3, 4, 2), (3, 6, 12),
    (4, 6, 4), (4, 7, 2),
    (5, 7, 4), (5, 8, 5),
    (6, 7, 1), (6, 9, 5),
    (7, 8, 6), (7, 9, 3),
    (8, 9, 8)
]
social_network_graph.add_weighted_edges_from(friendship_edges)

user_positions = {
    1: [-1.0, 0.05],
    2: [-0.55, -0.519],
    3: [-0.644, 0.644],
    4: [-0.373, 0.126],
    5: [0.261, -0.705],
    6: [0.132, 0.541],
    7: [0.391, -0.043],
    8: [0.918, -0.388],
    9: [0.868, 0.292]
}

user_colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'cyan', 'magenta', 'grey']

plt.figure(figsize=(12, 8))
nx.draw(social_network_graph, pos=user_positions, with_labels=True, node_color=user_colors, node_size=1000, edge_color='blue')
labels = nx.get_edge_attributes(social_network_graph, 'weight')
nx.draw_networkx_edge_labels(social_network_graph, pos=user_positions, edge_labels=labels)
plt.title('Соціальна мережа "Online Forever" з вагами ребер')
plt.show()

# Алгоритм Дейкстри
def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

graph_dict = {node: {neigh: attr['weight'] for neigh, attr in social_network_graph[node].items()} for node in social_network_graph.nodes()}

def format_dijkstra_results(results):
    table_data = []
    for start_vertex, paths in results.items():
        row = [f"Від {start_vertex}"]
        for target_vertex, distance in paths.items():
            if distance == float('infinity'):
                distance_str = "∞"
            else:
                distance_str = str(distance)
            row.append(distance_str)
        table_data.append(row)
    return table_data

all_paths = {vertex: dijkstra(graph_dict, vertex) for vertex in graph_dict}
table_data = format_dijkstra_results(all_paths)

headers = ["Вершина"] + [f"До {i}" for i in user_nodes]
print(tabulate(table_data, headers=headers, tablefmt="github", numalign="center"))