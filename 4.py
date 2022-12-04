from puzzleinput import getlines

def rset(x):
    x1,x2=map(int,x.split('-'))
    return set(range(x1,x2+1))

L = [tuple(map(rset,l.split(',')))for l in getlines(4)]

def part1():
    return sum(a<=b or b<=a for a,b in L)

def part2():
    return sum(bool(a&b)for a,b in L)

if __name__ == '__main__':
    assert part1()==471
    assert part2()==888

