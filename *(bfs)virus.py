import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

l = [[] for _ in range(a)]
v = []
for i in range(b):
    n, m = map(int, input().split())
    if m == 1:
        v.append(n)
    if n == 1:
        v.append(m)
    l[n-1].append(m)

visit = v[:]
while v:
    t = v.pop() #1에 연결된 것의 첫번째 값을 반환
    if l[t-1]: #l[t-1]에 저장된 값이 있다면
        for j in l[t-1]:
            index = 1
            while index < a:
                k = l[index-1]
                for i in k:
                    if index not in visit and i == t and index != 1:
                        visit.append(index)
                        v.append(index)
                index += 1
            if j not in visit and j != 1:#j가 visit에 없고 1이 아니라면
                visit.append(j)
                v.append(j)#추가
                idx = 1#인덱스 번호 보정
                while idx < a:
                    k = l[idx-1]
                    for i in k:
                        if idx not in visit and i == j:
                            visit.append(idx)
                            v.append(idx)
                    idx += 1
    else:
        idx = 1
        while idx < a:
            k = l[idx-1]
            for i in k:
                if idx not in visit and i == t and idx != 1:
                    visit.append(idx)
                    v.append(idx)
            idx += 1
print(len(visit))

# from collections import deque
# import sys

# input = sys.stdin.readline

# a = int(input())
# b = int(input())

# # 그래프 초기화
# l = [[] for _ in range(a)]

# # 간선 정보 입력
# for i in range(b):
#     n, m = map(int, input().split())
#     l[n-1].append(m)
#     l[m-1].append(n)  # 양방향 그래프를 고려해 반대 방향도 추가

# # BFS를 위한 큐와 방문 리스트
# queue = deque([1])
# visit = [False] * a
# visit[0] = True
# count = 0

# # BFS 탐색 시작
# while queue:
#     node = queue.popleft()
#     count += 1
#     for neighbor in l[node-1]:
#         if not visit[neighbor-1]:
#             visit[neighbor-1] = True
#             queue.append(neighbor)

# if count != 0:
#     print(count - 1)  # 1번 노드를 제외하고 방문한 노드의 수 출력
# else: print(0)
