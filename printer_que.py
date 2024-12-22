import sys
input = sys.stdin.readline

a = int(input())
for i in range(a):
    n, m = map(int, input().rstrip().split())
    li = [int(i) for i in input().rstrip().split()]

    cnt = 0
    tf = True
    j = 0
    for i in range(max(li), 0, -1):
        count = 0
        while tf and i in li:
            if i == li[j]:
                li.pop(j)
                cnt += 1
                if m == j:
                    tf = False
                    break
                elif m > j:
                    m -= 1
            else:
                li.append(li[j])
                li.pop(j)
                if m > j:
                    m -= 1
                elif m == j:
                    m = len(li) - 1
        if tf == False:
            break

    print(cnt)