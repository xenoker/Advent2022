import os
from sys import argv

def get(i):
    with open(f'./inputs/{i}.txt') as f:
        return f.read()
def getlines(i, emptys=False):
    with open(f'./inputs/{i}.txt') as f:
        return [x for x in f.read().split('\n') if x or emptys]
def getints(i):
    with open(f'./inputs/{i}.txt') as f:
        return [int(x) for x in f.read().split('\n') if x]

try: name = os.path.basename(argv[0]).split('.')[0]
except: pass
else: L = getlines(name) #running 15.py gets the lines from /inputs/15.txt

def look_4way(LL, x, y, m = 1000):
    left  = [ix for ix in LL[y][:x][::-1]][:m]
    right = [ix for ix in LL[y][x+1:]][:m]
    up    = [iy[x] for iy in LL[:y][::-1]][:m]
    down  = [iy[x] for iy in LL[y+1:]][:m]
    return [left,right,up,down]

def abs_limit(i,m):
    if i == 0: return 0
    if i > 0: return min(i,m)
    if i < 0: return max(i,-m)

def abs_subtract(i,m):
    if i == 0: return 0
    if i > 0: return i-m
    if i < 0: return i+m

import unittest
class TestFunctionality(unittest.TestCase):
    def test_look_4way(self):
        LL = [list(range(i,i+5)) for i in range(1,26,5)]
        self.assertEqual(look_4way(LL,2,2), [[12, 11], [14, 15], [8, 3], [18, 23]])
        self.assertEqual(look_4way(LL,2,2,1), [[12], [14], [8], [18]])
    def test_abs_limit(self):
        self.assertEqual(abs_limit(5,2),2)
        self.assertEqual(abs_limit(-5,2),-2)
        self.assertEqual(abs_limit(0,2),0)
    def test_abs_subtract(self):
        self.assertEqual(abs_subtract(5,2),3)
        self.assertEqual(abs_subtract(-5,2),-3)
        self.assertEqual(abs_subtract(0,2),0)
if __name__ == '__main__':
    unittest.main(verbosity=2)
