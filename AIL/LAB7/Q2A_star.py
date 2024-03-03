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
    if __name__ == "__main__":
        heuristics = {
            'A': 7,
            'B': 3,
            'C': 4,
            'D': 6,
            'E': 5,
            'F': 6,
            'G1': 0,
            'G2': 0,
            'G3': 0,
            'S': 5,
        }

        graph = {
            'A': [('B', 3), ('G1', 9)],
            'B': [('A', 2), ('C', 1)],
            'C': [('F', 7), ('G2', 5), ('S', 6)],
            'D': [('C', 2), ('E', 2), ('S', 1)],
            'E': [('G3', 7)],
            'F': [('D', 2), ('G3', 8)],
            'G1': [],
            'G2': [],
            'G3': [],
            'S': [('A', 7), ('B', 9), ('D', 6)],
        }

    g = Graph(graph, heuristics)

    goals = ['G1', 'G2', 'G3']
    min_cost = float('inf')
    min_path = None

    for goal in goals:
        cost, path = g.A_star('S', goal)
        if cost is not None and cost < min_cost:
            min_cost = cost
            min_path = path

    if min_path:
        print("Minimum cost path:", " ".join(min_path))
        print(f"Minimum cost: {min_cost}")
    else:
        print("No valid path found to any goal.")
