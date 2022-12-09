from puzzleinput import getlines, look_4way
from functools import reduce
L = getlines(8)

def view(H, L):
    V = 0
    for x in L:
        V += 1
        if x>=H: break
    return V

def part(p):
    V = 0
    for y,R in enumerate(L):
        for x,H in enumerate(R):
            if p == 1:
                for dl in look_4way(L,x,y):
                    if all(H>h for h in dl): V+=1; break
            if p == 2:
                V = max(V, reduce(lambda x,y:x*y, [view(H,x) for x in look_4way(L,x,y)]))
    return V

if __name__ == '__main__':
    assert part(1)==1851
    assert part(2)==574080
