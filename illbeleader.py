import sys

a = int(sys.stdin.readline().strip())

for i in range(a):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    
    l = []
    for j in range(1,n+1):
        l.append(j)
    
    for _ in range(k):
        for j in range(n):
            if j != 0:
                l[j] = l[j] + l[j-1]

    print(l[n-1])