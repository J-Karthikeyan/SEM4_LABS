class Graph:
    def __init__(self):
        self.adj_list = dict()

    def connect(self, from_vertex, to_vertex) -> None:
        self.adj_list.setdefault(from_vertex, []).append(to_vertex)
        if to_vertex not in self.adj_list:
            self.adj_list.setdefault(to_vertex, [])

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        print(start)

        for next in self.adj_list[start]:
            if next not in visited:
                self.dfs(next, visited)
        return visited

if __name__ == "__main__":
    g = Graph()
    for i in [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]:
        g.connect(i[0], i[1])
    print(g.adj_list)
    g.dfs(5)
