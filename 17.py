from itertools import cycle
from puzzleinput import get

shapel = [
    (((0,0),(1,0),(2,0),(3,0)),1,4), #-
    (((1,0),(0,1),(1,1),(2,1),(1,2)),3,3), #+
    (((0,0),(1,0),(2,0),(2,1),(2,2)),3,3), #_|
    (((0,0),(0,1),(0,2),(0,3)),4,1), #|
    (((0,0),(1,0),(0,1),(1,1)),2,2), ##
    ]

class Rock:
    def __init__(self, shape, h, w, b):
        self.xs = 2
        self.shape = shape
        self.h = h
        self.w = w
        self.maxxs = 7-w
        self.b = b
    def shift(self, d):
        if d == '>': self.xs += 1
        if d == '<': self.xs -= 1
        if d == 'd': self.b -= 1
    def occupy(self):
        return [(x+self.xs,y+self.b) for x,y in self.shape]
    def doccupy(self, d):
        if d == '>': dx,dy = 1,0
        elif d == '<': dx,dy = -1,0
        elif d == 'd': dx,dy = 0,-1
        return [(x+dx,y+dy) for x,y in self.occupy()]
    def move(self, d, others):
        if d == '>' and self.xs == self.maxxs: return None
        if d == '<' and self.xs == 0: return None
        if d == 'd' and self.b == 0: return False
        pc = self.doccupy(d)
        for o in others:
            if abs(self.b-o.b) > 4: continue
            if set(pc)&set(o.occupy()):
                if d == 'd': return False
                return None
        self.shift(d)
    
class Chamber:
    def __init__(self, maxr):
        self.rocks = []
        self.maxr = maxr
        self.shapes = cycle(shapel)
        self.pushes = cycle(get(17))
    def dropb(self):
        if not len(self.rocks): return 3
        return max(rock.b+rock.h for rock in self.rocks)+3
    def simulate(self, rep=False):
        D,D0 = dict(),0
        for i in range(self.maxr):
            rh = self.dropb()
            s,h,w = next(self.shapes)
            R = Rock(s,h,w,rh)
            while True:
                p = next(self.pushes)
                R.move(p,self.rocks)
                if R.move('d', self.rocks) == False: break
            self.rocks.append(R)
            if i > 30: self.rocks.pop(0)
            
            if rep and i%5 == 0 and i>10:
                lab = tuple(r.xs for r in self.rocks[-10:])
                if lab in D:
                    diff = i-D[lab]
                    if diff == D0:
                        return (i,D[lab],i-D[lab])
                    D0 = diff
                else: D[lab] = i
        return self.dropb()-3
            
def part1():
    C = Chamber(2022)
    return C.simulate()

def part2():
    C = Chamber(50000)
    B,A,AB = C.simulate(True)

    CA = Chamber(A)
    C1 = CA.simulate()
    CB = Chamber(B)
    C2 = CB.simulate()
    HAB = C2-C1

    mul = ((1000000000000-B)//AB)
    rem = (1000000000000-B)%AB

    CC = Chamber(B+rem)
    C3 = CC.simulate()
    return HAB*mul+C3

if __name__ == '__main__':
    assert part1()==3171
    assert part2()==1586627906921
