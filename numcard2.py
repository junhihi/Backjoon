import sys
from collections import Counter

n = int(sys.stdin.readline())
a = [int(i) for i in sys.stdin.readline().split()]
m = int(sys.stdin.readline())
b = [int(i) for i in sys.stdin.readline().split()]

if len(a) != n or len(b) != m:
    raise Exception('error')

counter = Counter(a)

r = [0] * m
cnt = 0
for i in b:
    r[cnt] = counter[i]
    cnt += 1

print(*r)