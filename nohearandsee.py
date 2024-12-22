import sys
input = sys.stdin.readline

a, b = map(int, input().split())

s = set([input().rstrip() for _ in range(a)])
h = set([input().rstrip() for _ in range(b)])

r = list(s & h)
r.sort()
print(len(r))
for i in r:
    print(i)