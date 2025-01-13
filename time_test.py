import time
import random
from graph_algorithms import GraphAlgorithms
def generate_random_graph(vertices, edges, max_capacity=100):
    graph = GraphAlgorithms(vertices)
    for _ in range(edges):
        u = random.randint(0, vertices - 1)
        v = random.randint(0, vertices - 1)
        while u == v:
            v = random.randint(0, vertices - 1)
        capacity = random.randint(1, max_capacity)
        graph.add_edge(u, v, capacity)
    return graph
def measure_execution_time(graph, source, sink, algorithm):
    start_time = time.time()
    if algorithm == "ford_fulkerson":
        result = graph.ford_fulkerson(source, sink)
    elif algorithm == "edmonds_karp":
        result = graph.edmonds_karp(source, sink)
    else:
        raise ValueError("Неизвестный алгоритм")
    end_time = time.time()
    return end_time - start_time, result
def analyze_algorithms(vertex_counts, edge_factor, max_capacity=100):
    results = {"vertices": [], "ford_fulkerson": [], "edmonds_karp": []}
    for vertices in vertex_counts:
        edges = vertices * edge_factor
        graph = generate_random_graph(vertices, edges, max_capacity)
        source = 0
        sink = vertices - 1
        graph_copy = graph.copy_graph()
        ford_time, _ = measure_execution_time(graph, source, sink, "ford_fulkerson")
        graph.graph = graph_copy
        edmonds_time, _ = measure_execution_time(graph, source, sink, "edmonds_karp")
        results["vertices"].append(vertices)
        results["ford_fulkerson"].append(ford_time)
        results["edmonds_karp"].append(edmonds_time)
    return results
def display_results(results):
    print("\nРезультаты анализа:")
    print(f"{'Вершины':<10} {'Форд-Фалкерсон (с)':<20} {'Эдмондс-Карп (с)':<20}")
    print("-" * 50)
    for i in range(len(results["vertices"])):
        print(f"{results['vertices'][i]:<10} {results['ford_fulkerson'][i]:<20.5f} {results['edmonds_karp'][i]:<20.5f}")
def main():
    vertex_counts = [10, 50, 100, 200, 500]
    edge_factor = 2
    print("Анализ производительности алгоритмов")
    results = analyze_algorithms(vertex_counts, edge_factor)
    display_results(results)

if __name__ == "__main__":
    main()