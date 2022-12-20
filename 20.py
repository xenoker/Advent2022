from puzzleinput import getlines
L = getlines(20)

class Point:
    def __init__(self,v,p2):
        self.v = int(v)
        if p2: self.v*=811589153
        self.next, self.prev = None, None

def part(part2=False):
    points = [Point(v,part2) for v in L]
    for p1,p2 in zip(points, points[1:]):
        p1.next, p2.prev = p2, p1
    points[0].prev = points[-1]
    points[-1].next = points[0]
    for _ in range(part2 and 10 or 1):
        for p in points:
            p.prev.next = p.next
            p.next.prev = p.prev
            pp, pn = p.prev, p.next
            for i in range(p.v%(len(points)-1)):
                pp,pn = pp.next, pn.next
            pp.next, p.prev = p, pp
            pn.prev, p.next = p, pn
    for p in points:
        if p.v != 0: continue
        ret, px = 0, p
        for i in range(0,3001):
            if i%1000 == 0: ret += px.v
            px = px.next
    return ret

if __name__ == '__main__':
    assert part()==7278
    assert part(part2=True)==14375678667089
