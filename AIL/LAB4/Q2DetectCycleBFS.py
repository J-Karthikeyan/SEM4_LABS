class Graph:
    def __init__(self):
        self.adj_list = dict()

    def connect(self, from_vertex, to_vertex):
        self.adj_list.setdefault(from_vertex, []).append(to_vertex)
        #For nodes with in-vertex zero
        self.adj_list.setdefault(to_vertex, [])

    def is_cyclic(self):
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
        if len(order) != len(self.adj_list):
            return None
        return order      
    
if __name__ == "__main__":
    g = Graph()
    #nodes = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]
    nodes = [(0,1), (0,2), (1,2), (2,0), (2,3), (3,3)]
    for frm, to in nodes:
        g.connect(frm, to)
    temp = g.is_cyclic()
    if temp:
        print("Acyclic", " ".join(map(str, temp)))
    else:
        print("Cyclic")
