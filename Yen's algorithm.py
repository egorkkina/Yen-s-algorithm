import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
import networkx as nx

import random
# import heapq

# Создание окна tkinter
window = tk.Tk()
window.title('Егоркина Маргарита. АС-22-05. Поиск кратчайшего пути в графе. Алгоритм Йена.')
window.geometry('1300x1000')
window['bg'] = 'gray'

tk.Label(text='Поиск кратчайшего пути в графе. Алгоритм Йена.', bg='darkorange', fg='black',
         font=('Liberation Serif', 16)).place(x=0, y=5)
tk.Label(text='Кол-во вершин графа', bg='darkorange', fg='black', font=('Liberation Serif', 14)).place(x=0, y=65)
tk.Label(text='Кол-во ребер графа', bg='darkorange', fg='black', font=('Liberation Serif', 14)).place(x=0, y=100)


# Визуализация графа, который передан в параметр g
def DrawGraph(g):
    position = nx.spring_layout(g, seed=7)

    edges = g.edges()  # получение всех рёбер

    nx.draw_networkx_nodes(g, position, node_size=700, node_color='skyblue')  # рисование узлов (вершин) графа
    nx.draw_networkx_labels(g, position, font_size=14, font_color='black')  # рисование подписей узлов графа

    nx.draw_networkx_edges(g, position, edgelist=edges, width=3, alpha=0.5, edge_color='darkorange')

    edge_labels = nx.get_edge_attributes(g, 'weight')  # получение атрибутов ребер графа
    nx.draw_networkx_edge_labels(g, position, edge_labels)  # рисование подписей ребер графа

    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f'{g}.png')
    plt.show()


def CreateGraph():
    # получение значения количества вершин и ребер из комбинированных полей
    tops_amount = combo_top.get()
    edges_amount = combo_edge.get()

    if not tops_amount or not edges_amount:
        print("Пожалуйста, выберите количество вершин и ребер.")
        return

    tops_amount = int(tops_amount)
    edges_amount = int(edges_amount)

    graph = nx.Graph()  # создание нового пустого графа

    tops = tuple(range(1, tops_amount + 1))
    graph.add_nodes_from(tops)  # добавление узлов (вершин) в граф

    # генерация случайных ребер для графа с проверкой на уникальность, отличие между вершинами и отсутствие уже существующих ребер
    while len(graph.edges) < edges_amount:
        top_a, top_b = random.randint(1, tops_amount), random.randint(1, tops_amount)
        if top_a != top_b and not graph.has_edge(top_a, top_b):
            graph.add_edge(top_a, top_b, weight=random.randint(1, 30))

    DrawGraph(graph)


# def YensAlgorithm(graph, source, destination, k):
#     shortest_paths = []
#
#     # Находим первый кратчайший путь с помощью алгоритма Дейкстры
#     shortest_path = Dijkstra(graph, source, destination)
#     shortest_paths.append(shortest_path)
#
#     for i in range(1, k):
#         last_shortest_path = shortest_paths[-1]
#         for j in range(len(last_shortest_path) - 1):
#             spur_node = last_shortest_path[j]
#             root_path = last_shortest_path[:j + 1]
#
#             # Удаляем ребро, которое встречается в других кратчайших путях
#             edge = (root_path[-1], last_shortest_path[j + 1])
#             if edge in graph[root_path[-1]]:
#                 graph[root_path[-1]].pop(edge)
#
#             # Находим новый кратчайший путь от spur вершины до целевой вершины
#             spur_path = Dijkstra(graph, spur_node, destination)
#
#             # Объединяем spur путь с root путём
#             total_path = root_path + spur_path
#
#             # Добавляем новый кратчайший путь в список кратчайших путей
#             shortest_paths.append(total_path)
#
#             # Восстанавливаем граф для следующей итерации
#             graph[root_path[-1]][(total_path[j], total_path[j + 1])] = GetPathLength(total_path[:j + 1])
#
#         # Сортируем кратчайшие пути по длине
#         shortest_paths.sort(key=lambda p: GetPathLength(p))
#
#         # Удаляем дубликаты кратчайших путей
#         shortest_paths = RemoveDuplicates(shortest_paths)
#
#     return shortest_paths
#
#
# def Dijkstra(graph, source, destination):
#     # Инициализируем начальную точку и очередь с приоритетом
#     distances = {source: 0}
#     queue = [(0, source)]
#     previous = {}
#
#     while queue:
#         current_distance, current_node = heapq.heappop(queue)
#
#         if current_node == destination:
#             path = []
#             while current_node in previous:
#                 path.insert(0, current_node)
#                 current_node = previous[current_node]
#             path.insert(0, source)
#             return path
#
#         for neighbor, weight in graph[current_node]:
#             distance = current_distance + weight
#             if neighbor not in distances or distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 previous[neighbor] = current_node
#                 heapq.heappush(queue, (distance, neighbor))
#
#     return None
#
#
# def GetPathLength(path):
#     return sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
#
#
# def RemoveDuplicates(paths):
#     unique_paths = []
#     for path in paths:
#         if path not in unique_paths:
#             unique_paths.append(path)
#     return unique_paths
#
#
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'D': 3, 'E': 2},
#     'C': {'B': 2, 'D': 5},
#     'D': {'E': 1},
#     'E': {}
# }
#
# source = 'A'
# destination = 'E'
# k = 3
#
# shortest_paths = YensAlgorithm(graph, source, destination, k)
# for i, path in enumerate(shortest_paths):
#     print(f"Кратчайший путь {i + 1}: {' -> '.join(path)}. Длина пути: {GetPathLength(path)}")

# Добавление полей для указания начальной и конечной вершин для поиска кратчайшего пути
tk.Label(window, text='Начальная вершина').pack()
entry_start = ttk.Entry(window)
entry_start.pack()

tk.Label(window, text='Конечная вершина').pack()
entry_end = ttk.Entry(window)
entry_end.pack()

combo_top = ttk.Combobox(window, values=[str(i) for i in range(1, 13)])
combo_top.place(x=200, y=65)
combo_edge = ttk.Combobox(window, values=[str(i) for i in range(1, 13)])
combo_edge.place(x=200, y=100)

# Создание стиля
style = ttk.Style()
style.configure("LargeButton.TButton", font=('Liberation Serif', 14), foreground='RoyalBlue1', background='RoyalBlue1')

# Создание кнопки с применением стиля и установка размера
random_graph_button = ttk.Button(window, text='Create Graph', command=CreateGraph, style='LargeButton.TButton',
                                 width=20)
random_graph_button.place(x=0, y=150)

# window.mainloop()
