import sys
input = sys.stdin.readline

a = int(input())
l = [int(i) for i in input().split()]
l.sort()

t = 0
w = 0
for i in l:
    t += i * (a - w)
    w += 1
print(t)