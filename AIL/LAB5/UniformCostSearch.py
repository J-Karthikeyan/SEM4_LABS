class UniformCostSearch:

    def __init__(self, adjlist : dict()):
        self.adjlist = adjlist
        
    def ucs(self, start, end):
       fringe = list()
       visited = list()
       for to_vertex in self.adjlist[start]:
            fringe.append(to_vertex)
            fringe.sort(key=lambda a : a[1])
            print(fringe)
            #while 'G' not in visited:
               #do something

if __name__ == "__main__":
    graph = {
        'S':[['1',2], ['3',5]],
        '1':[['G',1]],
        '2':[['1',4]],
        '3':[['1',5], ['3',2], ['G',6]],
        '4':[['2',4], ['5',3]],
        '5':[['2',6], ['G',3]],
        'G':[['4',7]]
    }
    g = UniformCostSearch(graph)
    g.ucs('S','G')