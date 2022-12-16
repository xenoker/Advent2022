from collections import defaultdict
from itertools import combinations
from puzzleinput import getlines
from dijkstra import Dijkstra
L = getlines(16)

class valve:
    def __init__(self, text):
        S = text.split()
        self.name = S[1]
        self.flow = int(S[4].split('=')[1][:-1])
        self.exits = [x.replace(',','') for x in S[9:]]
    def total(self, t, tmax):
        return max(0,tmax-t)*self.flow

VALVES = dict((v.name,v) for v in [valve(l) for l in L])
DIS = dict()
class dist(Dijkstra):
    def search(self, p1):
        for ex in VALVES[p1].exits:
            yield ex
for p1 in VALVES.keys():
    for p2 in VALVES.keys():
        DIS[(p1,p2)] = dist(VALVES,p1,p2).solve()

class Solution:
    def __init__(self):
        self.maxtime = 30
        self.best = 0
        self.flows = [x for x in VALVES.keys() if VALVES[x].flow>0]
    def solve(self, time, loc, opn, score):
        if score > self.best:
            self.best = score
        for opt in self.flows:
            if opt in opn: continue
            d = DIS[(loc,opt)]
            if d+1 > (self.maxtime-time): continue
            self.solve(time+d+1, opt, opn+[opt], score + VALVES[opt].total(time+d+1,self.maxtime))
    def solve2(self, time, loc, opn, score, time2, loc2, turn):
        if score > self.best:
            self.best = score
        if turn:
            for opt in self.flows:
                if opt in opn: continue
                d = DIS[(loc,opt)]
                if d+1 > (self.maxtime-time): continue
                self.solve2(time+d+1, opt, opn+[opt], score + VALVES[opt].total(time+d+1,self.maxtime),time2, loc2, not turn)
        else:
            for opt in self.flows:
                if opt in opn: continue
                d = DIS[(loc2,opt)]
                if d+1 > (self.maxtime-time2): continue
                self.solve2(time, loc, opn+[opt], score + VALVES[opt].total(time2+d+1,self.maxtime), time2+d+1, opt, not turn)

def part1():
    S = Solution()
    S.solve(0,'AA',[],0)
    return S.best

def part2():
    S = Solution()
    S.solve2(4,'AA',[],0,4,'AA',True) #takes near 5 minutes
    return S.best

if __name__ == '__main__':
    assert part1()==1584
    assert part2()==2052
