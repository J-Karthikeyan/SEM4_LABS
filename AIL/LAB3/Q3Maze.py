class Graph:
    def __init__(self):
        self.adj_list = dict()

    def connect(self, vertex1, vertex2):
        self.adj_list.setdefault(vertex1, []).append(vertex2)
        self.adj_list.setdefault(vertex2, []).append(vertex1)
    
    def dfs(self, v:int, goal:int, visited:set, path:list):
        visited.add(v)
        path.append(v)

        if v == goal:
            return True

        for neighbour in self.adj_list[v]:
            if neighbour not in visited:
                if self.dfs(neighbour, goal, visited, path):
                    return True
        path.pop()
        return False

    def path(self, start, goal):
        visited = set()
        path = list()

        if self.dfs(start, goal, visited, path):
            print("Path found : ", " ".join(map(str, path)))
        else:
            print("Path not found")


if __name__ == '__main__':
    g = Graph()
    nodes = [(1,2), (1,6), (2,3), (3,8), (8,7), (6, 11), (11,12), (12,17), (17,16), (17,18), (18,19), (19,14), (14,13), (14,9), (9,10), (10,5), (5,4), (10, 15), (15,20)]

    for frm, to in nodes:
        g.connect(frm, to)
    print("Adjacency List:", g.adj_list)

    g.path(2,20)
    