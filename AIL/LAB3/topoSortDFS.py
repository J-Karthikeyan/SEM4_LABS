class Graph:
    def __init__(self):
        self.adj_list = dict()

    def connect(self, from_vertex, to_vertex) -> None:
        self.adj_list.setdefault(from_vertex, []).append(to_vertex)
        if to_vertex not in self.adj_list:
            self.adj_list.setdefault(to_vertex, [])

    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbour in self.adj_list[v]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited, stack)
        stack.append(v)

    def TopologicalSort(self, start):
        n = len(self.adj_list)
        visited = [False] * n
        stack = []
        self.dfs(start, visited, stack)
        
        print("Depth First Traversal for the graph is:", end=" ")
        for vertex in stack[::-1]:
            print(vertex, end=" ")
        print()

if __name__ == "__main__":
    g = Graph()
    #for i in [(0, 1), (0, 2), (0, 3), (1, 3), (2, 4), (3, 5), (3, 6), (4, 7), (4, 5), (5, 2)]:

    for i in [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]:
        g.connect(i[0], i[1])
    print("Adjacency List:", g.adj_list)
    g.TopologicalSort(4)
