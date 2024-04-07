class Graph:

    def __init__(self, adjlist : dict):
        self.adjlist = adjlist
        
    def ucs(self, start, end):
        fringe = [[start, 0]]
        visited = set()
        while fringe:
            node = fringe.pop(0)

            if node[0] == end:
                return node
            
            visited.add(node[0])

            for neighbour in self.adjlist[node[0]]:
                if neighbour[0] not in visited:
                    new_cost = node[1] + neighbour[1]
                    fringe.append([neighbour[0], new_cost])
                    fringe.sort(key=lambda a : a[1])
        return None

if __name__ == "__main__":
    graph = {
        'S':[['1',2], ['3',5]],
        '1':[['G',1]],
        '2':[['1',4]],
        '3':[['1',5], ['3',2], ['G',6]],
        '4':[['2',4], ['5',3]],
        '5':[['2',6], ['G',3]],
        'G':[['4',7]]
    }
    g = Graph(graph)
    _ , min_cost = g.ucs('S','G')
    print(min_cost)
