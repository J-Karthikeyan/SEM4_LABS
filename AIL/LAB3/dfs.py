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

def dfs(graph, start, visited=None):
    if(visited is None):
        visited = [False] * len(graph)
    visited[start] = True
    print(start)
    for neighbour in sorted(graph[start]):
        if not visited[neighbour]:
            dfs(graph, neighbour, visited)

if __name__ == "__main__":

    graph = {
        0: [1,2,3],
        1: [4],
        2: [],
        3: [2],
        4: []
    }

    dfs(graph, 0)
