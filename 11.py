from puzzleinput import getlines
from math import lcm
L = getlines(11)
OP = {'+':lambda a,b:a+b,'*':lambda a,b:a*b}

class Monkey:
    def __init__(self,lines,M):
        self.inspections = 0
        self.M = M
        self.items = list(map(int,lines[1][18:].split(', ')))
        self.opop, self.opnum = lines[2].split()[-2:]
        if self.opnum.isdigit(): self.opnum = int(self.opnum)
        self.testdiv = int(lines[3].split()[-1])
        self.throwto = [int(lines[5].split()[-1]), int(lines[4].split()[-1])]
    def operate(self,n):
        func = OP[self.opop]
        if self.opnum == 'old': n2 = n
        else: n2 = self.opnum
        return func(n,n2)
    def throw(self,n):
        to = self.throwto[(n%self.testdiv)==0]
        self.M[to].items.append(n)
    def actions(self, part2=0):
        while self.items:
            i = self.items.pop(0)
            i = self.operate(i)
            if not part2: i = i//3
            else: i = i%part2
            self.inspections += 1
            self.throw(i)

def rounds(n, part2=False):
    M = []
    for l in [L[i:i+6] for i in range(0,len(L),6)]:
        M.append(Monkey(l,M))
    if part2: lc = lcm(*[m.testdiv for m in M])
    else: lc = 0
    for _ in range(n):
        for m in M: m.actions(lc)
    ins = [m.inspections for m in M]
    A,B = sorted(ins)[-2:]
    return A*B    

def part1():
    return rounds(20)

def part2():
    return rounds(10000, part2=True)

if __name__ == '__main__':
    assert part1()==100345
    assert part2()==28537348205
