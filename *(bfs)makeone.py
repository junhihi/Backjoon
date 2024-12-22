# deque, sys
import sys
from collections import deque
# 입력
n = int(sys.stdin.readline())
# 방문리스트
vis = [0 for _ in range(n+1)]
# bfs
def bfs() :
  q = deque()
  q.append(n)
  while q :
    cur = q.popleft()
    if cur == 1 :
      break
    if cur % 3 == 0 and vis[cur//3] == 0 :
      vis[cur//3] = vis[cur] + 1
      q.append(cur//3)
    if cur % 2 == 0 and vis[cur//2] == 0 :
      vis[cur//2] = vis[cur] + 1
      q.append(cur//2)
    if vis[cur-1] == 0 :
      vis[cur-1] = vis[cur] + 1
      q.append(cur-1)

bfs()
print(vis[1])