from collections import defaultdict as DD
from puzzleinput import getlines
from itertools import cycle
EPOS = [(x,y)for y,line in enumerate(getlines(23))for x,c in enumerate(line)if c=='#']
V8 = ((-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0))
VN = ((-1,-1),(0,-1),(1,-1))
VS = ((1,1),(0,1),(-1,1))
VW = ((-1,1),(-1,0),(-1,-1))
VE = ((1,-1),(1,0),(1,1))
VC = [(VN,(0,-1)),(VS,(0,1)),(VW,(-1,0)),(VE,(1,0))]*2

class Elves:
    def __init__(self):
        self.ELVES = EPOS.copy()
        self.occ()
        self.round = 0
    def occ(self):
        self.OCC = set(self.ELVES)
    def test(self, pos, lst):
        x0,y0 = pos
        tset = set((x0+x,y0+y) for x,y in lst)
        return bool(tset&self.OCC)
    def proposal(self, epos):
        x,y = epos
        if not self.test(epos, V8): return False
        r4 = self.round%4
        for test,d in VC[r4:r4+4]:
            if not self.test(epos, test): return (x+d[0],y+d[1])
        return False
    def rounds(self, num, part2=False):
        for r in range(num):
            self.round = r
            moves,targets = dict(),DD(int)
            for elf in self.ELVES:
                p = self.proposal(elf)
                if not p: continue
                moves[elf] = p
                targets[p] += 1
            if part2 and not moves: return r+1
            for elf,move in moves.items():
                if targets[move] > 1: continue
                self.ELVES.remove(elf)
                self.ELVES.append(move)
            self.occ()
        return self.unocc()
    def unocc(self):
        N = len(self.ELVES)
        xs = [p[0] for p in self.ELVES]
        ys = [p[1] for p in self.ELVES]
        return (max(xs)-min(xs)+1) * (max(ys)-min(ys)+1) - N

def part1():
    return Elves().rounds(10)

def part2():
    return Elves().rounds(len(EPOS), True)

if __name__ == '__main__':
    assert part1()==4138
    assert part2()==1010

