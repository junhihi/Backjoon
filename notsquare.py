def isprimenum(target):
    for i in range(2 , target):
        if target % i == 0 : return False
    return True
    

a, b = map(int, input().split())

if a > b:
    temp = b
    b = a
    a = temp

n = list(range(a,b+1))

for i in range(2, b+1):
    square = i**2
    if square > b:
        break
    if isprimenum(i):
        for j in range(len(n)-1, 0, -1):
            if n[j] % square == 0:
                n.pop(j)

print(len(n))

# def sieve(n):
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False
#     p = 2
#     while (p * p <= n):
#         if is_prime[p]:
#             for i in range(p * p, n + 1, p):
#                 is_prime[i] = False
#         p += 1
#     return [p for p in range(n + 1) if is_prime[p]]

# def count(a, b):
#     if a > b:
#         a, b = b, a

#     max_prime = int(b ** 0.5) + 1
#     primes = sieve(max_prime)

#     is_square_free = [True] * (b - a + 1)

#     for prime in primes:
#         square = prime * prime
#         start = max(square, a + (square - a % square) % square)
#         for j in range(start, b + 1, square):
#             is_square_free[j - a] = False

#     return sum(is_square_free)

# a, b = map(int, input().split())
# result = count(a, b)
# print(result)