class Graph:
    def __init__(self):
        self.adj_list = dict()

    def connect(self, from_vertex, to_vertex):
        self.adj_list.setdefault(from_vertex, []).append(to_vertex)

        #For nodes with in-vertex zero
        self.adj_list.setdefault(to_vertex, [])

    def kahns(self):
        #indegree dict init
        indeg = {v : 0 for v in self.adj_list}
        for frm, connections in self.adj_list.items():
            for to in connections:
                indeg[to] += 1
        
        queue = [v for v in self.adj_list if indeg[v] == 0]
        order = list()

        while queue:
            v = queue.pop(0)
            order.append(v)
            
            for neighbour in self.adj_list[v]:
                indeg[neighbour] -= 1
                if indeg[neighbour] == 0:
                    queue.append(neighbour)
        return order             
    
if __name__ == "__main__":
    g = Graph()
    nodes = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]
    for frm, to in nodes:
        g.connect(frm, to)
    order = g.kahns()
    print("Topo sort order : ", " ".join(map(str, order)))
