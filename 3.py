from puzzleinput import getlines
L = getlines(3)

def pri(x):
    return ord(x)>96 and ord(x)-96 or ord(x)-38

def part1():
    return sum(pri((set(l[:len(l)//2])&set(l[len(l)//2:])).pop())for l in L)

def part2():
    return sum(pri((set(L[i*3])&set(L[i*3+1])&set(L[i*3+2])).pop())for i in range(len(L)//3))

#from functools import reduce
#def part2(): #better, but longer and needs to import reduce
#    return sum(pri((reduce(set.intersection,map(set,L[i:i+3]))).pop())for i in range(0,len(L),3))

if __name__ == '__main__':
    assert part1()==7746
    assert part2()==2604
