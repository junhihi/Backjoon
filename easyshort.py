from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

l = [[] for _ in range(n)]
v = [[0]*m for _ in range(n)]

two = []
for y in range(n):
    x = 0
    for j in input().split():
        k = int(j)
        if k == 2:
            two = [y,x]
        l[y].append(k)
        x += 1

qx, qy = deque(), deque()
qx.append(two[1])
qy.append(two[0])
while qx:
    cx = qx.popleft()
    cy = qy.popleft()
    if cx < m-1:
        if v[cy][cx+1] == 0 and (cx+1 != two[1] or cy != two[0]) and l[cy][cx+1] == 1:
            qx.append(cx+1)
            qy.append(cy)
            v[cy][cx+1] = v[cy][cx] + 1
    if cx > 0:
        if v[cy][cx-1] == 0 and (cx-1 != two[1] or cy != two[0]) and l[cy][cx-1] == 1:
            qx.append(cx-1)
            qy.append(cy)
            v[cy][cx-1] = v[cy][cx] + 1
    if cy < n-1:
        if v[cy+1][cx] == 0 and (cx != two[1] or cy+1 != two[0]) and l[cy+1][cx] == 1:
            qx.append(cx)
            qy.append(cy+1)
            v[cy+1][cx] = v[cy][cx] + 1
    if cy > 0:
        if v[cy-1][cx] == 0 and (cx != two[1] or cy-1 != two[0]) and l[cy-1][cx] == 1:
            qx.append(cx)
            qy.append(cy-1)
            v[cy-1][cx] = v[cy][cx] + 1

cy = 0
for i in v:
    cx = 0
    for j in i:
        if l[cy][cx] == 1 and v[cy][cx] == 0:
            i[cx] = -1
        cx += 1
    cy += 1
    print(*i)

# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# l = []
# v = [[0]*m for _ in range(n)]  # 거리 기록을 위한 배열
# two = []  # 시작점(2)의 좌표 저장

# # 입력을 받아서 2차원 배열 l에 저장
# for y in range(n):
#     row = list(map(int, input().split()))
#     l.append(row)
#     for x in range(m):
#         if row[x] == 2:
#             two = (x, y)  # 시작점 저장

# # BFS를 위한 큐 초기화
# queue = deque()
# queue.append(two)

# while queue:
#     cx, cy = queue.popleft()
    
#     # 상하좌우 방향으로 이동할 좌표 계산
#     for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         nx, ny = cx + dx, cy + dy
        
#         # 범위를 벗어나지 않고, 아직 방문하지 않았으며, 이동할 수 있는 경우(값이 1인 경우)
#         if 0 <= nx < m and 0 <= ny < n and v[ny][nx] == 0 and l[ny][nx] == 1:
#             queue.append((nx, ny))
#             v[ny][nx] = v[cy][cx] + 1

# # 거리 기록 배열에 -1을 기록하는 부분
# for y in range(n):
#     for x in range(m):
#         if l[y][x] == 1 and v[y][x] == 0:  # 1인데 방문되지 않은 경우
#             v[y][x] = -1

# # 출력
# for row in v:
#     print(*row)