def get(i):
    with open(f'./inputs/{i}.txt') as f:
        return f.read()
def getlines(i, emptys=False):
    with open(f'./inputs/{i}.txt') as f:
        return [x for x in f.read().split('\n') if x or emptys]
def getints(i):
    with open(f'./inputs/{i}.txt') as f:
        return [int(x) for x in f.read().split('\n') if x]

def look_4way(LL, x, y, m = 1000):
    left  = [ix for ix in LL[y][:x][::-1]][:m]
    right = [ix for ix in LL[y][x+1:]][:m]
    up    = [iy[x] for iy in LL[:y][::-1]][:m]
    down  = [iy[x] for iy in LL[y+1:]][:m]
    return [left,right,up,down]


import unittest
class TestFunctionality(unittest.TestCase):
    def test_look_4way(self):
        LL = [list(range(i,i+5)) for i in range(1,26,5)]
        self.assertEqual(look_4way(LL,2,2), [[12, 11], [14, 15], [8, 3], [18, 23]])
        self.assertEqual(look_4way(LL,2,2,1), [[12], [14], [8], [18]])

if __name__ == '__main__':
    unittest.main(verbosity=2)
