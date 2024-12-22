import sys
input = sys.stdin.readline

n = int(input())
l = dict()
for _ in range(n):
    s, e = map(int, input().split())
    l[s] = e

print(l)