from puzzleinput import getlines
L = getlines(25)

P = [5**i for i in range(25)]
C = dict(zip('012=-',(0,1,2,-2,-1)))

def s2d(s):
    D = 0
    for c,p in zip(s[::-1],P):
        D += C[c]*p
    return D

def d2s(d):
    out = []
    while d:
        out.insert(0,"012=-"[d%5])
        d = (d+2)//5
    return ''.join(out)

def part1():
    return d2s(sum(map(s2d,L)))

if __name__ == '__main__':
    for x in range(1,5000): assert s2d(d2s(x))==x
    assert part1()=="2011-=2=-1020-1===-1"
