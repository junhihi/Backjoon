import sys

a = sys.stdin.readline()
n = int(a)
b = n - len(a)*9
if b < 0:
    b = 0

s = 0
r = 0
for i in range(b, n):
    r = str(i)
    s = i
    for j in r:
        s += int(j)
    if s == n:
        break
    r = 0

print(int(r))