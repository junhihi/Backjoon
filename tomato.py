from collections import deque
import sys
input = sys.stdin.readline

qx = deque()
qy = deque()
m, n = map(int, input().split())
l = []
xcnt = 0
ycnt = 0
for _ in range(n):
    xcnt = 0
    t = [int(i) for i in input().split()]
    l.append(t)
    for i in t:
        if i == 1:
            qx.append(xcnt)
            qy.append(ycnt)
        xcnt += 1
    ycnt += 1


while qx:
    cx = qx.popleft()
    cy = qy.popleft()
    if cy < n-1:
        if l[cy+1][cx] == 0:
            l[cy+1][cx] = l[cy][cx] + 1
            qx.append(cx)
            qy.append(cy+1)
    if cy > 0:
        if l[cy-1][cx] == 0:
            l[cy-1][cx] = l[cy][cx] + 1
            qx.append(cx)
            qy.append(cy-1)
    if cx < m-1:
        if l[cy][cx+1] == 0:
            l[cy][cx+1] = l[cy][cx] + 1
            qx.append(cx+1)
            qy.append(cy)
    if cx > 0:
        if l[cy][cx-1] == 0:
            l[cy][cx-1] = l[cy][cx] + 1
            qx.append(cx-1)
            qy.append(cy)
tf = True
for i in l:
    if 0 in i:
        tf = False
        break

if tf:
    r = max(max(row) for row in l)
    if r < 0:
        print(-1)
    else:
        print(r-1)
else:
    print(-1)