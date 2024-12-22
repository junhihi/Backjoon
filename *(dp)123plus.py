# def p(n):
#     if n == 0:
#         return 1
#     return n * p(n - 1)

# import sys
# input = sys.stdin.readline

# t = int(input())
# for i in range(t):
#     n = int(input())
#     two = 1
#     three = 1
#     onlytwo = 0
#     onlythree = 0
#     mix = 0

#     twoClear = False
#     threeClear = False
#     mixClear = False
#     while 1:
#         if (n - 2*two) >= 0:
#             onlytwo += p(n - two)//(p(n - 2*two) * p(two))
#             two += 1
#         else:
#             twoClear = True
#         if (n - 3*three) >= 0:
#             onlythree += p(n - 2*three)//(p(n - 3*three) * p(three))
#             three += 1
#         else: 
#             threeClear = True
#         if twoClear&threeClear:
#             two = 1
#             three = 1
#             one = n - 2*two - 3*three
#             while one >= 0:
#                 one = n - 2*two - 3*three
#                 mix += p(one + two + three)//(p(two) * p(three) * p(one))
            
#                 two += 1
#                 if (n - 2*two - 3*three) < 0:
#                     two = 1
#                     three += 1
#                     if (n - 2*two - 3*three) < 0:
#                         break
#             if one <= 0:
#                 break

#     result = onlytwo + onlythree + mix + 1
#     print(result)

import sys
input = sys.stdin.readline

def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 4
        
        for i in range(4, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))