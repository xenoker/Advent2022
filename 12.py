from puzzleinput import getlines
from heapq import heapify, heappop, heappush
from collections import defaultdict

DIR = [(1,0),(0,1),(-1,0),(0,-1)]
MAP = dict(((x,y),h) for y,l in enumerate(getlines(12)) for x,h in enumerate(l))
START = [a for a,b in MAP.items() if b=='S'][0]
END = [a for a,b in MAP.items() if b=='E'][0]

def height(p):
    c = MAP[p]
    if c == 'E': c = 'z'
    return max(ord(c)-97,0)

def run(start):
    Q = [(0, start)]
    heapify(Q)
    DIST = defaultdict(lambda:999999)
    while Q:
        dist, point = heappop(Q)
        x, y = point
        for dx,dy in DIR:
            p2 = x+dx, y+dy
            if p2 not in MAP: continue
            h1,h2 = height(point), height(p2)
            if (h2-h1) > 1: continue
            if dist + 1 < DIST[p2]:
                DIST[p2] = dist + 1
                heappush(Q, (dist+1, p2))
    return DIST[END]

def part1():
    return run(START)

def part2():
    return min(run(p) for p,h in MAP.items() if h=='a')

if __name__ == '__main__':
    assert part1()==497
    assert part2()==492
