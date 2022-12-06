from puzzleinput import get
T = get(6)

def upos(n):
    return [i for i in range(len(T))if len(set(T[i-n:i]))==n][0]

if __name__ == '__main__':
    assert upos( 4)==1100
    assert upos(14)==2421
