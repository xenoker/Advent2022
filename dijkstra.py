from heapq import heapify, heappop, heappush
from collections import defaultdict
class Dijkstra:
    def __init__(self, mapd:dict, start, end):
        self.MAP = mapd
        self.START = start
        self.END = end

    def search(self, p1):
        px, py = p1
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            yield (px+dx,py+dy)

    def valid(self, p1, p2):
        return True
    
    def cost(self, c1, p1, p2):
        return c1 + 1        

    def solve(self) -> int: 
        Q = [(0, self.START)]
        heapify(Q)
        self.DIST = defaultdict(lambda:999999999999)
        while Q:
            dist, p1 = heappop(Q)
            for p2 in self.search(p1):
                if p2 not in self.MAP: continue
                if not self.valid(p1,p2): continue
                dcost = self.cost(dist, p1, p2)
                if dcost < self.DIST[p2]:
                    self.DIST[p2] = dcost
                    heappush(Q, (dcost, p2))
        return self.DIST[self.END]        

