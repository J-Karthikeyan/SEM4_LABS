class queue:
    def __init__(self, q: list = []):
        self.arr = q
        
    def enqueue(self, ele):
        self.arr.append(ele)
        
    def dequeue(self):
        if self.arr:
            return self.arr.pop(0)


def WaterJugBFS(x, y, goal):   
    path = []
    q = queue([(0,0)])
    visited = set()
    flag = False 

    while q.arr:
        
        a, b = q.dequeue()

        if goal in path:
            flag = True
            return flag, path
        
        if (a,b) in visited:
            continue

        visited.add((a,b))
        path.append((a,b))

        #filling jugs
        if a < x:
            q.enqueue((x,b))
        if b < y:
            q.enqueue((a,y))

        #emptying jugs
        if a > 0:
            q.enqueue((0,b))
        if b > 0:
            q.enqueue((a,0))

        #pouring water from one jug to another
        if a+b >= x:
            q.enqueue((x, b-(x-a)))
        else:
            q.enqueue((a+b,0))
        if a+b >= y:
            q.enqueue((a-(y-b), y))
        else:
            q.enqueue((0,a+b))
    
    return flag, path

if __name__ == '__main__':
    x = 4
    y = 3
    goal = (2,0)
    flag, path = WaterJugBFS(x, y, goal)
    print("Path:", path)
    print("Goal reached:", flag)
