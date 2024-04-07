class Graph:

    def __init__(self, adjlist: dict):
        self.adjlist = adjlist

    def ucs(self, start, end):
        fringe = [[start, 0]]
        visited = set()
        while fringe:
            node = fringe.pop(0)

            if node[0] in end:  
                return node

            visited.add(node[0])

            for neighbour in self.adjlist[node[0]]:
                if neighbour[0] not in visited:
                    new_cost = node[1] + neighbour[1]
                    fringe.append([neighbour[0], new_cost])
                    fringe.sort(key=lambda a: a[1])
        return None

if __name__ == "__main__":
    graph = {
        's': [['a', 5], ['b', 9], ['d', 6]],
        'a': [['b', 3], ['g1', 9]],
        'b': [['a', 2], ['c', 1]],
        'c': [['s', 6], ['f', 7], ['g2', 5]],
        'd': [['c', 2], ['e', 2]],
        'e': [['g3', 7]], 
        'f': [['d', 2], ['g3', 8]],
        'g1': [],
        'g2': [],
        'g3': [],
    }
    goal = ['g1', 'g2', 'g3']
    g = Graph(graph)
    name, min_cost = g.ucs('s', goal)
    print(f"s to {name}, cost = {min_cost}")
