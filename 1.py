from puzzleinput import getlines
L = getlines(1, emptys=True)

CALS = [0]
for x in L:
    if not x: CALS.append(0)
    else: CALS[-1] += int(x)
    
def part1():
    return max(CALS)
def part2():
    return sum(sorted(CALS)[-3:])

if __name__ == '__main__':
    assert part1()==73211
    assert part2()==213958

    

