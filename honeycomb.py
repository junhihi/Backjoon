a = int(input())

cnt = 0
k = 1
r = 0
while 1:
    r += cnt
    if a // k == 0:
        break
    cnt += 1
    k = 2 + r * 6

if a == 1:
    cnt = 1

print(cnt)