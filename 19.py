from heapq import heapify, heappop, heappush
from puzzleinput import getlines
D = dict()
for line in getlines(19):
    ints = [int(x) for x in line.replace(':','').split() if x.isdigit()]
    D[ints[0]] = tuple(ints[1:])

class Simulation:
    def __init__(self, costs, tmax):
        self.tmax = tmax
        self.costs = costs
        self.max = 0
    def run(self):
        T = self.tmax
        C = self.costs
        Q = [(T,1,1,0,0,0,0,0,0,0)]
        S = set()
        maxORE = max(C[4],C[2],C[1],C[0])
        heapify(Q)
        while Q:
            state = heappop(Q)
            _,t,ORE,CLA,OBS,GEO,ore,cla,obs,geo = state
            if t == T:
                if geo+GEO > self.max: self.max=geo+GEO
                continue
            if state in S: continue
            S.add(state)
            f = (T-t)*(-GEO-1)-geo
            if ore >= C[4] and obs >= C[5]:
                heappush(Q,((T-t)*(-GEO-2)-geo,t+1,ORE,CLA,OBS,GEO+1,ore-C[4]+ORE,cla+CLA,obs-C[5]+OBS,geo+GEO))
                continue
            if ore >= C[2] and cla >= C[3]:
                heappush(Q,(f,t+1,ORE,CLA,OBS+1,GEO,ore-C[2]+ORE,cla-C[3]+CLA,obs+OBS,geo+GEO))
            if ore >= C[1]:
                heappush(Q,(f,t+1,ORE,CLA+1,OBS,GEO,ore-C[1]+ORE,cla+CLA,obs+OBS,geo+GEO))
            if ore >= C[0] and ORE < maxORE:
                heappush(Q,(f,t+1,ORE+1,CLA,OBS,GEO,ore-C[0]+ORE,cla+CLA,obs+OBS,geo+GEO))
            heappush(Q,(f,t+1,ORE,CLA,OBS,GEO,ore+ORE,cla+CLA,obs+OBS,geo+GEO))
        return self.max

def part1():
    T = 0
    for i,c in D.items():
        res = Simulation(c,24).run()
        T += i*res
    return T

def part2():
    T = 1
    for c in (D[1],D[2],D[3]):
        res = Simulation(c, 32).run()
        T *= res
    return T

if __name__ == '__main__':
    assert part1()==1703 #101 seconds
    assert part2()==5301 #326 seconds
