# Граф представляє собою приклад соціальних зв'язків в соціальній мережі "Online Forever".
# На прикладі зображенні 9 користувачів (вузли). Всі вони мають зв'язок між собою у вигляді ребер.
# Це означає, що користувачі є друзями, товаришами, або просто якось пов'язані між собою, наприклад 
# реакціями оди на одного в соцмережі (лайками).

import networkx as nx
import matplotlib.pyplot as plt

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

social_network_graph.add_nodes_from(user_nodes)
social_network_graph.add_edges_from(friendship_edges)

user_colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'cyan', 'magenta', 'grey']
plt.figure(figsize=(12, 8))
nx.draw(social_network_graph, pos=user_positions, with_labels=True, node_color=user_colors, node_size=1000, edge_color='blue')
plt.title('Соціальна мережа "Online Forever" ')
plt.show()

total_users = social_network_graph.number_of_nodes()
total_friendships = social_network_graph.number_of_edges()
user_degrees = dict(social_network_graph.degree())

network_analysis = {
    "Кількість користувачів": total_users,
    "Кількість дружніх зв'язків": total_friendships,
    "Ступені користувачів": {f"Користувач {user}": degree for user, degree in user_degrees.items()}
}

print(network_analysis)

