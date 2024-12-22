import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
l = []
l.append(b)
r = b
for i in range(a-1):
    b = int(input())
    if b == 0:
        r -= l[len(l)-1]
        l.pop(len(l)-1)
    else:
        l.append(b)
        r += l[len(l)-1]

print(r)