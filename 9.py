from puzzleinput import getlines, abs_limit
DIR ={'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}

class Knot:
    def __init__(self, rope, n):
        self.rope = rope
        self.n = n
        self.P = [0,0]
    def move(self, d):
        self.Pl = self.P.copy()
        self.P[0] += d[0]
        self.P[1] += d[1]
    def chain(self):
        KP = self.rope.K[self.n-1]
        dx = KP.P[0]-self.P[0]
        dy = KP.P[1]-self.P[1]
        if abs(dx)<2 and abs(dy)<2: return
        self.move((abs_limit(dx,1),abs_limit(dy,1)))

class Rope:
    def __init__(self, l):
        self.l = l
        self.K = [Knot(self,i) for i in range(l)]
        self.path = dict()
        self.parse()
    def log(self, p):
        self.path[tuple(p)] = True
    def parse(self):
        for l in getlines(9):
            di,ni = l.split()
            d,n = DIR[di], int(ni)
            for move in range(n):
                self.K[0].move(d)
                for i in range(1,self.l): self.K[i].chain()
                self.log(self.K[self.l-1].P)
    def visits(self):
        return len(self.path.keys())

def part1():
    R = Rope(2)
    return R.visits()

def part2():
    R = Rope(10)
    return R.visits()

if __name__ == '__main__':
    assert part1()==6357
    assert part2()==2627
