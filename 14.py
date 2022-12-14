from puzzleinput import getlines
from collections import defaultdict
L = getlines(14)
INLET = (500,0)
DIR = [(0,1),(-1,1),(1,1)]
ranged = lambda x,y: range(min(x,y),max(x,y)+1)

class Cave:
    def __init__(self):
        self.MAP = defaultdict(bool)
        for line in L:
            posses = [tuple(map(int,xy.split(','))) for xy in line.split(' -> ')]
            ppos,plist = posses[0],posses[1:]
            for p in plist:
                if p[0] == ppos[0]:
                    for y in ranged(p[1],ppos[1]): self.MAP[(p[0],y)] = True
                else:
                    for x in ranged(p[0],ppos[0]): self.MAP[(x,p[1])] = True
                ppos = p
        self.VOID = max(p[1] for p in self.MAP.keys())
        self.rested = 0
        self.FLOOR = self.VOID
    def dropsand(self, floor=False):
        p = INLET
        while True:
            if not floor and p[1]>self.VOID: return True
            elif p[1]>self.VOID: break
            for dx,dy in DIR:
                mayp = (p[0]+dx,p[1]+dy)
                maybe = self.MAP[mayp]
                if not maybe:
                    p = mayp
                    break
            else: break
        if p == INLET: return True
        self.MAP[p] = True
    def run(self, floor = False):
        while not self.dropsand(floor): self.rested += 1
        return self.rested +floor

def part1():
    return Cave().run()

def part2():
    return Cave().run(True)

if __name__ == '__main__':
    assert part1()==737
    assert part2()==28145
