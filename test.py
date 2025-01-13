import logging
from graph_algorithms import GraphAlgorithms  #Использование библиотеки

def run_tests():
    logging.basicConfig(filename='test_results.log', level=logging.INFO)

    #Ориентированный граф
    directed_graph = GraphAlgorithms(3)
    directed_graph.add_edge(0, 1, 10)
    directed_graph.add_edge(1, 2, 5)
    directed_graph.add_edge(0, 2, 15)
    directed_max_flow = directed_graph.ford_fulkerson(0, 2)
    logging.info(f'Максимальный поток в ориентированном графе(0 до 2): {directed_max_flow}')
    
    #Неориентированный граф
    undirected_graph = GraphAlgorithms(3)
    undirected_graph.add_edge(0, 1, 10, undirected=True)
    undirected_graph.add_edge(1, 2, 5, undirected=True)
    undirected_graph.add_edge(0, 2, 15, undirected=True)
    undirected_max_flow = undirected_graph.ford_fulkerson(0, 2)
    logging.info(f'Максимальный поток в неориентированном графе(0 до 2): {undirected_max_flow}')
    
    #Связный граф
    connected_graph = GraphAlgorithms(4)
    connected_graph.add_edge(0, 1, 10)
    connected_graph.add_edge(1, 2, 5)
    connected_graph.add_edge(2, 3, 10)
    connected_max_flow = connected_graph.ford_fulkerson(0, 3)
    logging.info(f'Максимальный поток в связном графе(0 до 3): {connected_max_flow}')
    
    #Несвязный граф
    disconnected_graph = GraphAlgorithms(4)
    disconnected_graph.add_edge(0, 1, 10)
    #Теперь нет рёбер, соединяющих вершины 2 и 3
    disconnected_max_flow = disconnected_graph.ford_fulkerson(0, 3)
    logging.info(f'Максимальный поток в несвязном графе(0 до 3): {disconnected_max_flow}')
    
    #Граф с отрицательными весами
    negative_weights_graph = GraphAlgorithms(3)
    negative_weights_graph.add_edge(0, 1, 10)
    negative_weights_graph.add_edge(1, 2, -5)
    negative_max_flow = negative_weights_graph.ford_fulkerson(0, 2)
    logging.info(f'Максимальный поток в графе с отрицательными весами(0 до 2): {negative_max_flow}')
    
    #Циклический граф
    cyclic_graph = GraphAlgorithms(4)
    cyclic_graph.add_edge(0, 1, 10)
    cyclic_graph.add_edge(1, 2, 10)
    cyclic_graph.add_edge(2, 0, 10)
    cyclic_graph.add_edge(2, 3, 15)
    cyclic_max_flow = cyclic_graph.ford_fulkerson(0, 3)
    logging.info(f'Максимальный поток в циклическом графе(0 до 3): {cyclic_max_flow}')
    
    #Ациклический граф
    acyclic_graph = GraphAlgorithms(4)
    acyclic_graph.add_edge(0, 1, 10)
    acyclic_graph.add_edge(1, 2, 10)
    acyclic_graph.add_edge(1, 3, 5)
    acyclic_max_flow = acyclic_graph.ford_fulkerson(0, 3)
    logging.info(f'Максимальный поток в ациклическом графе(0 до 3): {acyclic_max_flow}')
    
if __name__ == "__main__":
    run_tests()