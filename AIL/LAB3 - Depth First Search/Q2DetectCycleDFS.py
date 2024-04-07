class Graph:
    def __init__(self):
        self.adj_list = dict()

    def connect(self, from_vertex, to_vertex) -> None:
        self.adj_list.setdefault(from_vertex, []).append(to_vertex)

    def cycle(self):
        visited = set()
        stack = set()

        def dfs(node):
            visited.add(node)
            stack.add(node)

            if node in self.adj_list:
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        if dfs(neighbor):
                            return True
                    elif neighbor in stack:
                        return True

            stack.remove(node)
            return False

        for node in self.adj_list:
            if node not in visited:
                if dfs(node):
                    return True

        return False
    
if __name__ == "__main__":
    g = Graph()
    #nodes = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]
    nodes = [(0,1), (0,2), (1,2), (2,0), (2,3), (3,3)]
    #nodes = [(0,2), (2,3), (3,4), (4,2), (4,5), (1,6), (6,7), (7,5), (7,6)]
    for frm, to in nodes:
        g.connect(frm, to)
    print("Adjacency List:", g.adj_list)
    if(g.cycle()):
        print("Cyclic")
    else:
        print("Acyclic")


'''
OUTPUT

Adjacency List: {2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}
Acyclic

Adjacency List: {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
Cyclic

https://www.baeldung.com/cs/detecting-cycles-in-directed-graph

https://www.javatpoint.com/python-program-to-detect-a-cycle-in-a-directed-graph#:~:text=Python%20Program%20to%20Detect%20a%20Cycle%20in,%C2%B7%20def%20dfs(node):%20%C2%B7%20visited.add(node)%20%C2%B7%20stack.add(
'''
