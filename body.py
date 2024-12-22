n = int(input())

l = []
for i in range(n):
    l.append([int(i) for i in input().split()])

r = [1] * n
for i,(x,y) in enumerate(l):
    for j in range(len(l)):
        if x < l[j][0] and y < l[j][1]:
            r[i] += 1

print(*r)