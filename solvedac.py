def rround(a):
    if a - int(a) >= 0.5:
        return int(a) + 1
    else: return int(a)

def j(a):
    return rround(a * 0.15)

import sys
input = sys.stdin.readline

a = int(input().rstrip())

if a == 0:
    print(0)

else: 
    f = j(a)

    p = a - 2 * f

    li = [int(input().rstrip()) for _ in range(a)]
    li.sort()

    r = 0
    for i in range(f, a - f):
        r += li[i]

    print(rround(r/p))