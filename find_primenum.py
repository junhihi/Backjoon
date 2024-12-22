def isprime(n):
    s = int(n ** 0.5)
    if n == 1:
         return False
    for i in range(2, s + 1):
            if n % i == 0:
                return False
    return True

import sys
a, b = map(int, sys.stdin.readline().rstrip().split())

for i in range(a, b + 1):
    if isprime(i):
        print(i)