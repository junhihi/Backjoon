from collections import deque
import sys

a = int(sys.stdin.readline())

if a == 1:
    l = deque([1])
else:
    l = deque([i for i in range(1, (a + 1))])

while len(l) > 1:
    l.popleft()
    l.append(l.popleft())


print(*l)