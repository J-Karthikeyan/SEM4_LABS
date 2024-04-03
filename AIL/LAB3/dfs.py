'''
pseudocode for dfs

dfs(graph, start)
    visit start
    for not visited neighbour of start:
        dfs(neighbour)

pseudocode for specific path

dfs(graph, start, end):
    visit start 
    add start to path
    for not visited neighbour of start:
        

'''

def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            neighbors = sorted(graph[node], key=lambda x: (x, graph[x]))  
            for neighbor in neighbors:
                stack.append(neighbor)

    return traversal_order

if __name__ == "__main__":

    graph = {
        'a': ['b', 'c', 'd', 'e'],
        'b': ['a', 'd', 'f'],
        'c': ['a', 'g'],
        'd': ['a', 'b', 'f'],
        'e': ['a', 'g'],
        'f': ['b', 'd'],
        'g': ['c', 'e']
    }

    print(dfs(graph, 'a'))
