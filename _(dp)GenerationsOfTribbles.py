import sys

def koong(n):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        dp = [0] * (n + 4)
        dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4
        
        for i in range(4, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
        
        return dp[n]

input = sys.stdin.readline
a = int(input())

for i in range(a):
    print(koong(int(input())))