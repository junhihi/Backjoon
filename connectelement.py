from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [[] for _ in range(n)]
visit = [True] * n
for _ in range(m):
    u, v = map(int, input().split())
    l[u-1].append(v-1)
    l[v-1].append(u-1)

q = deque()
cnt = 0
for index, i in enumerate (l):
    if i:
        for j in i:
            q.append(j)
            while q:
                cur = q.popleft()
                visit[cur] = False
                for k in range(len(l[cur])-1, -1, -1):
                    q.append(l[cur][k])
                    l[cur].pop(k)
        cnt += 1
    elif visit[index]:
        cnt += 1

print(cnt)