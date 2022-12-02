from puzzleinput import getlines
GAMES = [game.split() for game in getlines(2)]
OUTCOME = {'A':'ZXY', 'B':'XYZ', 'C':'YZX'} #lose/same/win

def score(op, me):
    score = {'X':1,'Y':2,'Z':3}[me]
    if OUTCOME[op][1]==me: score+=3
    elif OUTCOME[op][2]==me: score+=6
    return score

def touse(op, act):
    return OUTCOME[op][(ord(act)-88)]

def part1():
    return sum(score(op,me) for op,me in GAMES)

def part2():
    return sum(score(op, touse(op,act)) for op,act in GAMES)

if __name__ == '__main__':
    assert part1()==14375
    assert part2()==10274

    

