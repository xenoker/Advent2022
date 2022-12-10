from puzzleinput import getlines
CYCLES = [20,60,100,140,180,220]
SCREEN = [['.']*40 for r in range(6)]

class CPU:
    def __init__(self, ops):
        self.X = 1
        self.ops = ops
        self.queue = []
        self.i = 0
        self.S = 0
    def load(self, ins):
        if ins[0] == 'noop': return
        if ins[0] == 'addx': self.queue.append(ins)
    def unload(self):
        ins = self.queue.pop()
        if ins[0] == 'addx': self.X += int(ins[1])
    def tick(self):
        self.i += 1
        if self.i in CYCLES: self.S += self.i*self.X
        self.pixel()
        if not self.queue: self.load(self.ops.pop(0).split())
        else: self.unload()
    def run(self):
        while self.ops or self.queue:
            self.tick()
        print('\n'.join(''.join(row) for row in SCREEN))
        return self.S
    def pixel(self):
        y = self.i // 40
        x = (self.i-1)%40
        if abs(self.X-x)<=1: SCREEN[y][x] = '#'

if __name__ == '__main__':
    C = CPU(getlines(10))
    assert C.run()==14540
#   ####.#..#.####.####.####.#..#..##..####.
#   #....#..#....#.#.......#.#..#.#..#....#.
#   ###..####...#..###....#..####.#......#..
#   #....#..#..#...#.....#...#..#.#.....#...
#   #....#..#.#....#....#....#..#.#..#.#....
#   ####.#..#.####.#....####.#..#..##..####.
