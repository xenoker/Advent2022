from puzzleinput import getlines
import json
from functools import cmp_to_key
L = [json.loads(l) for l in getlines(13)]
AB = list(zip(L[::2],L[1::2]))

def compare(a,b):
    if type(a) == int and type(b) == int:
        if a == b: return None
        return a < b
    if type(a) == list and type(b) == list:
        if len(a) == 0: return True
        if len(b) == 0: return False
        c = compare(a[0],b[0])
        if c == None: return compare(a[1:],b[1:])
        return c
    if type(a) == list and type(b) == int:
        return compare(a,[b])
    if type(a) == int and type(b) == list:
        return compare([a],b)

def part1():
    return sum(i+1 for i,ab in enumerate(AB) if compare(ab[0],ab[1]))

def part2():
    P2 = [[[2]],[[6]]]
    cmp = cmp_to_key(lambda a,b: -1 if compare(a,b) else 1)
    L2 = sorted(L+P2, key=cmp)
    D1,D2 = [L2.index(x)+1 for x in P2]
    return D1*D2

if __name__ == '__main__':
    assert part1()==5555
    assert part2()==22852
