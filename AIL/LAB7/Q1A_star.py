class Graph:
    def __init__(self, adjlist: dict, heuristics: dict):
        self.heuristics = heuristics
        self.adjlist = adjlist
    
    def A_star(self, start, end):
        queue = [{'name':start, 'cost':self.heuristics[start], 'path':[start]}]
        visited = set()

        while queue:
            node = queue.pop(0)
            if node['name'] == end:
                cost = node['cost'] - self.heuristics[node['name']]
                return cost, node['path']
            
            visited.add(node['name'])

            for neighbour, weight in self.adjlist[node['name']]:
                if neighbour not in visited:
                    new_cost = (node['cost'] -self.heuristics[node['name']]) + (weight + self.heuristics[neighbour])
                    new_path = node['path'] + [neighbour]
                    queue.append({'name':neighbour, 'cost':new_cost, 'path':new_path})
                    queue.sort(key = lambda a : a['cost'])
            
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
