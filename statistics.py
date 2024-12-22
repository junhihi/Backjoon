def avg(li, n):
    avg = sum(li)/n
    if avg >= 0:
        if avg - int(avg) >= 0.5:
            return(int(avg) + 1)
        else: return(int(avg))
    else:
        if avg - int(avg) <= -0.5:
            return(int(avg) - 1)
        else: return(int(avg))

def mid(li):
    return(li[int(len(li)/2)])

# def mode(li):
#     a = [0] * (max(li) - min(li) + 1)
#     for i in li:
#         a[i - min(li)] += 1
#     b = a.index(max(a)) + 1
#     if b == len(a):
#         b = a.index(max(a))
#     if max(a) != max(a[b:]):
#         return(a.index(max(a)) + min(li))
#     else :
#         return(b + a[b:].index(max(a)) + min(li))

from collections import Counter

def mode(li):
    frequency = Counter(li)
    most_common = frequency.most_common()
    # 최빈값이 여러 개인 경우
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        candidates = [num for num, count in most_common if count == most_common[0][1]]
        return sorted(candidates)[1]  # 두 번째로 작은 값 반환
    return most_common[0][0]  # 최빈값 반환

def ranger(li):
    return(li[-1] - li[0])

import sys
iinput = sys.stdin.readline

n = int(iinput())

li = [int(iinput()) for _ in range(n)]
li.sort()

print(avg(li, n))
print(mid(li))
print(mode(li))
print(ranger(li))