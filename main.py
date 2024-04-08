import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()  # создаём объект графа

# определяем список узлов (ID узлов)
nodes = [1, 2, 3, 4, 5]

# определяем список рёбер
# список кортежей, каждый из которых представляет ребро
# кортеж (id_1, id_2) означает, что узлы id_1 и id_2 соединены ребром
edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 5)]

# добавляем информацию в объект графа
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# рисуем граф и отображаем его
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()