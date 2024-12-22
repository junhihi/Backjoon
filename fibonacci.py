import sys
input = sys.stdin.readline

zl = [0]*42
ol = [0]*42

zl[0] = 1
ol[1] = 1

a = int(input())
for i in range(a):
    b = int(input())
    if b > 1:
        for j in range(2, b+1):
            zl[j] = zl[j-1] + zl[j-2]
            ol[j] = ol[j-1] + ol[j-2]
    print(zl[b], ol[b])