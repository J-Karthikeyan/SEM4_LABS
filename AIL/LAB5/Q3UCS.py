class Graph:

    def __init__(self, adjlist: dict):
        self.adjlist = adjlist

    def ucs(self, start, end):
        fringe = [[start, 0, []]]
        visited = set()
        while fringe:
            node = fringe.pop(0)

            if node[0] == end:
                return node[1], node[2] + [node[0]]

            visited.add(node[0])

            for neighbor in self.adjlist[node[0]]:
                if neighbor[0] not in visited:
                    new_cost = node[1] + neighbor[1]
                    new_path = node[2] + [node[0]]
                    fringe.append([neighbor[0], new_cost, new_path])
                    fringe.sort(key=lambda a: a[1])
        return None, None

if __name__ == "__main__":
    graph = {
        'maldon': [['tiptree', 8]],
        'tiptree': [['feering', 3], ['clacton', 29]],
        'feering': [['maldon', 11], ['blaxhali', 46]],
        'clacton': [['maldon', 40], ['harwich', 17]],
        'harwich': [['tiptree', 31], ['blaxhali', 40], ['dunwich', 53]],
        'blaxhali': [['dunwich', 15]],
        'dunwich': [['blaxhali', 17]],
    }
    g = Graph(graph)
    min_cost, path = g.ucs('maldon', 'dunwich')
    print("Min Cost:", min_cost)
    print("Path:", path)
