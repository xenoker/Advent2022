from collections import defaultdict
from puzzleinput import getlines
import re
MAP = defaultdict(str)
for y,line in enumerate(getlines(22)[:-1]):
    for x,c in enumerate(line):
        MAP[(x+1,y+1)] = c
INS = re.findall('(\d+|R|L)',getlines(22)[-1])
DIR = [(1,0),(0,1),(-1,0),(0,-1)]
START = (min(p[0] for p in MAP if p[1]==1 and MAP[p]!=' '),1)

def wrap1(loc,fac):
    rfac = (fac+2)%4
    cloc = loc
    while True:
        x,y = loc
        npos = (x+DIR[rfac][0],y+DIR[rfac][1])
        if MAP[npos] == '' or MAP[npos] == ' ': break
        loc = npos
    if MAP[loc] == '#':
        loc = cloc
    return loc

###0       #B##E#
####       A####C
##49       ####D#
##50       ###
####       F#D
##99       ###
#100    #F####
####    A####C
#149    ####G#
#150    ###
####    B#G
#199    #E#

def wrap2(pos,fac):
    x,y = pos
    x = x-1
    y = y-1
    x3y4 = (x//50, y//50)
    if x3y4 == (1,0):
        if fac == 2: return (0+1, 149-y+1),0 #A
        if fac == 3: return (0+1, 100+x+1),0 #B
    if x3y4 == (2,0):
        if fac == 0: return (99+1, 149-y+1),2 #C
        if fac == 1: return (99+1, x-50+1),2 #D
        if fac == 3: return (x-100+1, 199+1),3 #E
    if x3y4 == (1,1):
        if fac == 0: return (y+50+1, 49+1),3 #D
        if fac == 2: return (y-50+1, 100+1),1 #F
    if x3y4 == (0,2):
        if fac == 2: return (50+1, 149-y+1),0 #A
        if fac == 3: return (50+1, x+50+1),0 #F
    if x3y4 == (1,2):
        if fac == 0: return (149+1, 149-y+1),2 #C
        if fac == 1: return (49+1, 100+x+1),2 #G
    if x3y4 == (0,3):
        if fac == 0: return (y-100+1 ,149+1),3 #G
        if fac == 1: return (x+100+1, 0+1),1 #E
        if fac == 2: return (y-100+1, 0+1),1 #B
    assert False

def travel(part2=False):
    loc = START
    fac = 0
    for ins in INS:
        if ins == 'L':
            fac = (fac-1)%4
            continue
        if ins == 'R':
            fac = (fac+1)%4
            continue
        n = int(ins)
        for i in range(n):
            x,y = loc
            new = (x+DIR[fac][0],y+DIR[fac][1])
            mnew = MAP[new]
            undo = loc,fac
            if mnew == '#':
                break
            if mnew == '.':
                loc = new
            if mnew == ' ' or mnew == '':
                if not part2: loc = wrap1(loc, fac)
                else: loc, fac = wrap2(loc, fac)
                assert MAP[loc] != ''
                if MAP[loc] == '#':
                    loc,fac = undo
    return 1000*loc[1] + 4*loc[0] + fac

if __name__ == '__main__':
    assert travel()==144244
    assert travel(part2=True)==138131

