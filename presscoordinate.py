import sys
input = sys.stdin.readline

n = int(input())
X = [int(i) for i in input().split()]
x = list(set(X))
x.sort()
dic = dict()
for i in range(len(x)):
    dic[x[i]] = i

l = []
for i in X:
    l.append(dic.get(i))

print(*l)