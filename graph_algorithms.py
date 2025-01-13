from collections import deque
import copy

class GraphAlgorithms:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    


    def add_edge(self, u, v, capacity, undirected=False):
    #Добавление ребра
        self.graph[u][v] = capacity
        if undirected:
            self.graph[v][u] = capacity


#Алгоритм Форда-Фалкерсона для нахождения максимального потока
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.vertices
        max_flow = 0
        
        while self._bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            
            max_flow += path_flow
        
        return max_flow

#Поиск в ширину для нахождения пути с ненулевой пропускной способностью
    def _bfs(self, source, sink, parent):
        visited = [False] * self.vertices
        queue = deque([source])
        visited[source] = True
        parent[source] = -1

        while queue:
            u = queue.popleft()

            for v in range(self.vertices):
                #Проверка ненулевой и проверка непосещения вершины
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True

        return False 

#Алгоритм Эдмондса-Карпа для нахождения максимального потока
    def edmonds_karp(self, source, sink):
        max_flow = 0
        parent = [-1] * self.vertices

        while self._bfs(source, sink, parent):
            #Пропускная способность на пути(минимальная)
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            #Обновление остатка(v3.3)
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow  #Уменьшение прямого потока
                self.graph[v][u] += path_flow  #Увеличение обратного потока
                v = parent[v]

            max_flow += path_flow

        return max_flow


    @staticmethod
    def from_keyboard():
    #Ввод графа с клавиатуры
        try:
            vertices = int(input("Введите количество вершин в графе: "))
            edges = int(input("Введите количество рёбер в графе: "))
            graph = GraphAlgorithms(vertices)

            print("Введите рёбра в формате: источник цель пропускная_способность")
            for _ in range(edges):
                u, v, capacity = map(int, input().split())
                graph.add_edge(u, v, capacity)

            return graph
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
            return None

    def visualize_graph(self):
        #Зарисовка графа
        print("\nВизуализация графа:")
        print("Вершины и рёбра (источник -> цель [пропускная способность]):\n")
        
        has_edges = False
        for u in range(self.vertices):
            for v in range(self.vertices):
                if self.graph[u][v] > 0:
                    has_edges = True
                    print(f"{u} -> {v} [{self.graph[u][v]}]")
        
        if not has_edges:
            print("Граф не содержит рёбер.")

    def visualize_adjacency_matrix(self):
        #Та самая матрица смежности
        print("\nМатрица смежности графа:")
        for row in self.graph:
            print(" ".join(f"{cell:3}" for cell in row))

    def copy_graph(self):

        #Копия графа создается для вычисления максимального потока по методу Эдмондса-Карпа(Без этого нихуя не равные значения максимального потока)
        
        return copy.deepcopy(self.graph)


if __name__ == "__main__":
    print("Создание графа с клавиатуры")
    g = GraphAlgorithms.from_keyboard()
    if g:
        #Визуальное отображение матрицы смежности и графа
        g.visualize_graph()
        g.visualize_adjacency_matrix()

        source = int(input("Введите вершину-источник: "))
        sink = int(input("Введите вершину-сток: "))
        
        #Сохранение копии графа
        original_graph = g.copy_graph()
        
        print("Максимальный поток (Форд-Фалкерсон):", g.ford_fulkerson(source, sink))
        
        #Восстанавление графа
        g.graph = original_graph
        
        print("Максимальный поток (Эдмондс-Карп):", g.edmonds_karp(source, sink))