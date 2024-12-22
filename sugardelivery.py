a = int(input())

cnt = a // 5
while 1:
    b = 5 * cnt
    if b < 0:
        print(-1)
        break

    t = (a - b) // 3
    if (a - b) % 3 == 0:
        print(cnt + t)
        break
    else:
        cnt -= 1