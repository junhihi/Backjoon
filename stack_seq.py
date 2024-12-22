import sys
input = sys.stdin.readline

a = int(input())
li = [int(input()) for _ in range(a)]
l = [i + 1 for i in range(a)]
r = []
re = []
i = 0
tf = False
t = True
while i < a:
    if t == False:
            break
    for j in l:
        if tf:
            if r[-1] == li[i]:
                r.pop(-1)
                re.append('-')
                i += 1
                break
            else:
                print('NO')
                t = False
                break
        else:
            if j == l[-1]:
                tf = True
            if j not in r and li[i] == j:
                re.append('+')
                re.append('-')
                i += 1
                continue
            if len(r) > 0:
                if li[i] == r[-1]:
                    r.pop(-1)
                    r.append(j)
                    re.append('-')
                    re.append('+')
                    i += 1
                    continue
            if li[i] != j:
                r.append(j)
                re.append('+')

if t:
    for i in re:
        print(i)

# import sys
# input = sys.stdin.readline

# a = int(input())
# li = [int(input()) for _ in range(a)]

# stack = []
# result = []
# current = 1
# possible = True

# for num in li:
#     while current <= num:
#         stack.append(current)
#         result.append('+')
#         current += 1
    
#     if stack[-1] == num:
#         stack.pop()
#         result.append('-')
#     else:
#         possible = False
#         break

# if possible:
#     print("\n".join(result))
# else:
#     print("NO")
