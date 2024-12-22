a = int(input())

l = []
for _ in range(a):
    l.append([int(i) for i in input().split()])

l.sort(key = lambda x: (x[1], x[0]))

for i in l:
    print(*i)