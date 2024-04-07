def WaterJugDFS(x, y, goal):
    path = []
    stack = [(0,0)]
    visited = set()
    flag = False

    while stack:
        a, b = stack.pop()

        if goal in path:
            flag = True
            return flag, path
        
        if (a,b) in visited:
            continue

        visited.add((a,b))
        path.append((a,b))

        #filling jugs
        if a < x:
            stack.append((x,b))
        if b < y:    
            stack.append((a,y))
        
        #emptying jugs
        if a > 0:
            stack.append((0,b))
        if b > 0:    
            stack.append((a,0))
        
        #pouring water from one jug to another
        if a+b >= x:
            stack.append((x, b-(x-a)))
        else:
            stack.append((a+b,0))
        if a+b >= y:
            stack.append((a-(y-b), y))
        else:
            stack.append((0,a+b))
        
    return flag, path
    
if __name__ == '__main__':
    x = 4
    y = 3
    goal = (2,0)
    flag, path = WaterJugDFS(x, y, goal)
    print("Path:", path)
    print("Goal reached:", flag)
