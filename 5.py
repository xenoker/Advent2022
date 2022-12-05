from puzzleinput import getlines
L = getlines(5)
MOVES = [tuple(map(int,s.split()[1::2])) for s in L[8:]]

def crates():
    return [[l[1+i*4] for l in L[7::-1] if l[1+i*4]!=' '] for i in range(9)]

def part():
    P1,P2 = crates(), crates()
    ans = lambda L:''.join(x[-1] for x in L)
    for n,a,b in MOVES:
        for i in range(n): P1[b-1].append(P1[a-1].pop())
        P2[b-1].extend(P2[a-1][-n:])
        del P2[a-1][-n:]
    return ans(P1),ans(P2)

if __name__ == '__main__':
    p1,p2 = part()
    assert p1=='TLFGBZHCN'
    assert p2=='QRQFHFWCL'

