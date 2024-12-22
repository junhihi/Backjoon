from collections import deque
n, k = map(int, input().split())

vis = [0] * 100002

q = deque()
q.append(n)
while q:
    cur = q.popleft()
    if cur == k:
        break
    if (cur*2) < (k+2) and cur*2 != cur:
        if vis[cur*2] > vis[cur] + 1 or vis[cur*2] == 0:
            vis[cur*2] = vis[cur] + 1
            q.append(cur*2)
    if cur + 1 <= k:
        if vis[cur+1] > vis[cur] + 1 or vis[cur+1] == 0:
            vis[cur+1] = vis[cur] + 1
            q.append(cur+1)
    if cur > 0:
        if vis[cur-1] > vis[cur] + 1 or vis[cur-1] == 0:
            vis[cur-1] = vis[cur] + 1
            q.append(cur-1)
            
print(vis[k])