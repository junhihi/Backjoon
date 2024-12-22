# import sys

# a, b = map(int, sys.stdin.readline().split())

# l = []
# for i in range(a):
#     l.append(i+1)

# ll = []
# # for i in range(a):
# #     l *= (i+1)
# #     ll.append(l[b*(i+1) - 1])

# cnt = 1
# while len(ll) != a :
#     lll = l
#     c = b * cnt - 1
#     if c > len(l):
#         for i in range(cnt - 1,0,-1):
#             lll.pop(b * i - 1)
#         for i in lll:
#             l.append(i)
        
#         continue
#     ll.append(l[c])
#     cnt += 1



# print(ll)

import sys

a, b = map(int, sys.stdin.readline().split())

l = []
for i in range(a):
    l.append(i + 1)

ll = []
index = 0

while len(ll) < a:
    index = (index + b - 1) % len(l) 
    ll.append(l.pop(index))  

r = '<'
for i in ll:
    r += str(i)
    if i != ll[len(ll)-1]:
        r += ', '

r += '>'
print(r)
