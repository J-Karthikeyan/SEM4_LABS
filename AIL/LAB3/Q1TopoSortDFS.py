'''
Toposort dfs approach:

iterate through nodes sequentially 
if the node is not visited yet then apply dfs on that node  
when you reach end append to stack
print the stack
'''

class Graph:
    def __init__(self):
        self.adj_list = dict()

    def connect(self, from_vertex, to_vertex):
        self.adj_list.setdefault(from_vertex, []).append(to_vertex)

        #For nodes with in-vertex zero
        self.adj_list.setdefault(to_vertex, [])

    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbour in self.adj_list[v]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited, stack)
        stack.append(v)
        
    def TopologicalSort(self):
        n = len(self.adj_list)
        visited = [False] * n
        stack = []
        for i in range(n):
            if not visited[i]:
                self.dfs(i, visited, stack)
        
        print("Depth First Traversal for the graph is:", end=" ")
        print(" ".join(map(str, stack[::-1])))

if __name__ == "__main__":
    g = Graph()
    #nodes = [(0,1), (0,2), (1,2), (2,0), (2,3), (3,3)]
    nodes = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]
    for frm, to in nodes:
        g.connect(frm, to)
    print("Adjacency List:", g.adj_list)
    g.TopologicalSort()

'''
OUTPUT
Adjacency List: {2: [3], 3: [1], 1: [], 4: [0, 1], 0: [], 5: [0, 2]}
Depth First Traversal for the graph is: 5 4 2 3 1 0
'''
