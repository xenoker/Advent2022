from functools import cache
from puzzleinput import getlines
L = getlines(24)
START = (L[0].find('.'),0)
END = (L[-1].find('.'),len(L)-1)
MAP = [(x,y)for y,line in enumerate(L) for x,c in enumerate(line)if c!='#']
W = len(L[0])-2
H = len(L)-2

class Blizzard:
    XL = list(range(1,W+1))
    YL = list(range(1,H+1))
    def __init__(self,pos,c):
        self.ipos = pos
        if c == '>':
            self.L = self.XL[pos[0]-1:] + self.XL[:pos[0]-1]
        elif c == '<':
            self.L = self.XL[pos[0]-1::-1] + self.XL[:pos[0]-1:-1]
        if c == '>' or c == '<':
            self.XYL = [(x,pos[1]) for x in self.L]
        if c == 'v':
            self.L = self.YL[pos[1]-1:] + self.YL[:pos[1]-1]
        elif c == '^':
            self.L = self.YL[pos[1]-1::-1] + self.YL[:pos[1]-1:-1]
        if c == 'v' or c == '^':
            self.XYL = [(pos[0],y) for y in self.L]
        self.Llen = len(self.L)
    def location(self,time):
        return self.XYL[time%self.Llen]

BLIZZARDS = [Blizzard((x,y),c) for y,line in enumerate(L) for x,c in enumerate(line)if c in '<>v^']

class Solver:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def search(self, p1):
        px, py = p1
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1),(0,0)]:
            yield (px+dx,py+dy)

    @cache
    def bloc(self,t):
        return [b.location(t) for b in BLIZZARDS]
    @cache
    def vpoint(self,p2):
        return p2 in MAP
    @cache
    def valid(self, p2, t):
        return p2 not in self.bloc(t)

    def solve(self,t0=0):
        T = t0
        Ps = {self.start}
        while self.end not in Ps:
            T += 1
            new = set()
            for p1 in Ps:
                for p2 in self.search(p1):
                    if not self.vpoint(p2): continue
                    if not self.valid(p2,T): continue
                    new.add(p2)
            Ps = new
        return T

def part1():
    return Solver(START,END).solve() 

def part2():
    A = Solver(START,END).solve()
    B = Solver(END,START).solve(A)
    C = Solver(START,END).solve(B)
    return C

if __name__ == '__main__':
    assert part1()==326
    assert part2()==976

