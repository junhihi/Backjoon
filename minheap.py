import sys
import heapq
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    x = int(input())
    if x == 0:
        if l:
            print(heapq.heappop(l))
        else:
            print(0)
    else:
        heapq.heappush(l, x)