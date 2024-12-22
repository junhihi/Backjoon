import sys

a = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip()

r = 0
cnt = 0
for i in b:
    r += (ord(i) - 96) * (31 ** cnt)
    cnt += 1

print(r % 1234567891)