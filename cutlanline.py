import sys
input = sys.stdin.readline
a, b = map(int, input().split())
c = [int(input()) for _ in range(a)]
d = sum(c)//b
tf = True
if d == 0:
    print(0)
else:
    while tf:
        for j in range(d, 0, -1):
            s = 0
            for i in c:
                s += i // j
                if s >= b:
                    print(j)
                    tf = False
                    break
            if tf == False : break


# import sys
# input = sys.stdin.readline

# a, b = map(int, input().split())
# c = [int(input()) for _ in range(a)]

# # 이분 탐색을 위한 변수 설정
# low, high = 1, sum(c) // b

# def can_divide(mid):
#     count = 0
#     for i in c:
#         count += i // mid
#         if count >= b:
#             return True
#     return False

# result = 0
# while low <= high:
#     mid = (low + high) // 2
#     if can_divide(mid):
#         result = mid
#         low = mid + 1  # 더 큰 값을 시도
#     else:
#         high = mid - 1  # 더 작은 값을 시도

# print(result)