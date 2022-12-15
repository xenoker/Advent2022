from puzzleinput import getlines
L = getlines(15)

def mhd(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

class sensor:
    def __init__(self, line):
        ls = line.replace(',','').replace(':','').split()
        l = [int(x[2:]) for x in [ls[y] for y in [2,3,8,9]]]
        self.pos = tuple(l[:2])
        self.close = tuple(l[2:])
        self.mhd = mhd(self.pos,self.close)
    def lcoverage(self, y):
        xr = range(self.pos[0]-self.mhd,self.pos[0]+self.mhd+1)
        return [x for x in xr if mhd(self.pos,(x,y))<=self.mhd and (x,y) not in BEACONS]
    def ring(self):
        xr = range(-self.mhd-1,self.mhd+2)
        x0,y0 = self.pos
        return [(x0+dx,y0+self.mhd+1-dx)for dx in xr]+[(x0+dx,y0-(self.mhd+1-dx))for dx in xr]
    def covered(self,p):
        return mhd(p,self.pos)<=self.mhd

SENSORS = [sensor(l) for l in L]
BEACONS = [s.close for s in SENSORS]

def part1():
    l = []
    for sens in SENSORS:
        l.extend(sens.lcoverage(2000000))
    return len(set(l))

def part2():
    points = []
    for sens in SENSORS:
        points.extend(sens.ring())
    for p in points:
        if not (0<=p[0]<=4000000 and 0<=p[1]<=4000000): continue
        if any(sens.covered(p) for sens in SENSORS): continue
        break
    return p[0]*4000000+p[1]

if __name__ == '__main__':
    assert part1()==4665948
    assert part2()==13543690671045
