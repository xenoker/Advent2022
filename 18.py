from puzzleinput import getlines
from collections import defaultdict
L = [tuple(map(int,l.split(','))) for l in getlines(18)]
D = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def part1():
    surf = 6*len(L)
    for A in L:
        N = [tuple(a+d for a,d in zip(A,s)) for s in D]
        b = sum(n in L for n in N)
        surf -= b
    return surf

def part2():
    xyzmax = max(max(p)for p in L)+1
    sr = defaultdict(int)
    todo, done = [(0, 0, 0)], []
    while todo:
        new = []
        for p0 in todo:
            for d in D:
                p = tuple(map(sum,zip(p0, d)))
                if not all(-1<=a<=xyzmax for a in p): continue
                if p in L: sr[p] += 1
                elif not p in done:
                    new.append(p)
                    done.append(p)                        
        todo = new
    return sum(sr.values())

if __name__ == '__main__':
    assert part1()==3466
    assert part2()==2012
