import sys

a = int(sys.stdin.readline())

for i in range(a):
    b = sys.stdin.readline()

    cnt = 0
    count = 0
    for j in b:
        cnt += 1

        if j == '(':
            count += 1
        elif j == ')':
            count -= 1

        if count < 0:
            print('NO')
            break

        if cnt == len(b):
            if count == 0:
                print('YES')
            else: print('NO')