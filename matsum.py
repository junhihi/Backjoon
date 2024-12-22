n, m = map(int, input().split())

a = [[int (i) for i in input().split()] for _ in range(n)]
b = [[int (i) for i in input().split()] for _ in range(n)]
c = list(map(lambda p,q: list(map(lambda x,y: x + y, p, q)), a, b))

for i in c:
    print(*i)