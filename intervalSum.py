import sys
input = sys.stdin.readline

n, m = map(int, input().split())

l = []
s = 0
for i in input().split():
    s += int(i)
    l.append(s)

for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(l[j-1])
    else: print(l[j-1] - l[i-2])