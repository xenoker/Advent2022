from puzzleinput import getlines
D = dict()
for line in getlines(21):
    name, op = line.split(': ')
    if op.isdigit(): D[name] = int(op)
    else: D[name] = op.split()

def result(key):
    x = D[key]
    if type(x) is int: return x
    a,op,b = x
    if op == '+': return result(a)+result(b)
    if op == '-': return result(a)-result(b)
    if op == '*': return result(a)*result(b)
    if op == '/': return result(a)/result(b)

def part1():
    return result('root')

def part2():
    n1,_,n2 = D['root']
    D['humn'] = 1
    while True:
        a,b = result(n1),result(n2)
        if a==b: return D['humn']
        D['humn'] = int(D['humn']*a/b) #possibly not applicable to all puzzle inputs

if __name__ == '__main__':
    assert part1()==124765768589550
    assert part2()==3059361893920

