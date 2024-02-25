class Graph:

    def __init__(self, adjlist: dict, heuristics: dict):
        self.heuristics = heuristics
        self.adjlist = adjlist

    def A_star(self, start, end):
        fringe = [[start, self.heuristics[start], [start]]]
        visited = set()

        while fringe:
            node = fringe.pop(0)

            if node[0] == end:
                cost = node[1] - self.heuristics[node[0]]
                return cost, node[2]

            visited.add(node[0])

            for neighbor in self.adjlist[node[0]]:
                if neighbor[0] not in visited:
                    new_cost = node[1] - self.heuristics[node[0]] + self.heuristics[neighbor[0]] + neighbor[1]
                    new_path = node[2] + [neighbor[0]]
                    fringe.append([neighbor[0], new_cost, new_path])
                    fringe.sort(key=lambda a: a[1])

        return None, None

if __name__ == '__main__':
    heuristics = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0,
    }

    graph = {
        'A': [('B', 6), ('F', 3)],
        'B': [('A', 6), ('C', 3), ('D', 2)],
        'C': [('B', 3), ('D', 1), ('E', 5)],
        'D': [('B', 2), ('C', 1), ('E', 8)],
        'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
        'F': [('A', 3), ('G', 1), ('H', 7)],
        'G': [('F', 1), ('I', 3)],
        'H': [('F', 7), ('I', 2)],
        'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
        'J': [('E', 5), ('I', 3)],
    }

    g = Graph(graph, heuristics)
    cost, path = g.A_star('A', 'J')
    
    if path:
        print("Path: ", ' '.join(path))
        print("Cost: ", cost)
    else:
        print("No path found.")
