import sys

def push(a, x):
    return a.append(x)

def pop(a):
    if len(a) > 0:
        popa = a[0]
        a = a[1:]
        return a, popa
    else:
        return a, -1

def size(a):
    return len(a)

def empty(a):
    if len(a) == 0:
        return 1
    else: return 0

def front(a):
    if len(a) > 0:
        return a[0]
    else: return -1

def back(a):
    if len(a) > 0:
        return a[len(a) - 1]
    else: return -1

a = int(sys.stdin.readline())
l = []
for i in range(a):
    b = sys.stdin.readline().split()
    if 'push' in b:
        push(l, int(b[1]))
    if 'pop' in b:
        l, popl = pop(l)
        print(popl)
    if 'size' in b:
        print(size(l))
    if 'empty' in b:
        print(empty(l))
    if 'front' in b:
        print(front(l))
    if 'back' in b:
        print(back(l))
