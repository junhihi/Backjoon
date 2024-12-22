n = int(input())

l = [0] * (n+1)
l[0] = 1
l[1] = 2
for i in range(2, n):
    l[i] = (l[i-1] + l[i-2]) % 10007

print(l[n - 1])