from puzzleinput import getlines
from collections import defaultdict

class FileSystem:
    def __init__(self):
        self.loc = []
        self.dsizes = defaultdict(int)
        self.parse()

    def add(self,n):
        for i in range(1,len(self.loc)+1):
            self.dsizes['/'.join(self.loc[:i])] += n

    def parse(self):
        for line in getlines(7):
            s = line.split()
            if s[0] == '$':
                if s[1] == 'cd':
                    if s[2] == '/': self.loc = ['/']
                    elif s[2] == '..': self.loc.pop()
                    else: self.loc.append(s[2])
            if s[0].isdigit(): self.add(int(s[0]))

    def part1(self):
        return sum(n for n in self.dsizes.values() if n <= 100000)
    def part2(self):
        cur = 70000000-F.dsizes['/']
        need = 30000000-cur
        for i in sorted(F.dsizes.values()):
            if i > need: return i

F = FileSystem()

if __name__ == '__main__':
    assert F.part1()==1243729
    assert F.part2()==4443914
