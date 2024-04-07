def WaterJugBFS(x, y, goal):
    path = []
    queue = [(0, 0)]  
    visited = set()
    flag = False

    while queue:
        a, b = queue.pop(0)  

        if goal in path:
            flag = True
            return flag, path

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path.append((a, b))

        # Filling jugs
        if a < x:
            queue.append((x, b))  
        if b < y:
            queue.append((a, y))

        # Emptying jugs
        if a > 0:
            queue.append((0, b))
        if b > 0:
            queue.append((a, 0))

        # Pouring water from one jug to another
        if a + b >= x:
            queue.append((x, b - (x - a)))
        else:
            queue.append((a + b, 0))
        if a + b >= y:
            queue.append((a - (y - b), y))
        else:
            queue.append((0, a + b))

    return flag, path

if __name__ == '__main__':
    x = 4
    y = 3
    goal = (2, 0)
    flag, path = WaterJugBFS(x, y, goal)
    print("Path:", path)
    print("Goal reached:", flag)
