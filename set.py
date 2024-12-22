def add(s, x):
    if x not in s:
        s.append(x)

def remove(s, x):
    if x in s:
        s.pop(s.index(x))

def check(s, x):
    if x in s:
        print(1)
    else: print(0)

def toggle(s, x):
    if x in s:
        s.pop(s.index(x))
    else: s.append(x)

def all(s):
    s = [str(i) for i in range(1,21)]
    return s

def empty(s):
    s = []
    return s

import sys
input = sys.stdin.readline
a = int(input().strip())

s = []
for i in range(a):
    b = input().strip()
    if 'add' in b:
        c, d = b.split()
        add(s, d)
    elif 'check' in b:
        c, d = b.split()
        check(s, d)
    elif 'remove' in b:
        c, d = b.split()
        remove(s, d)
    elif 'toggle' in b:
        c, d = b.split()
        toggle(s, d)
    elif b == 'all':
        s = all(s)
    elif b == 'empty':
        s = empty(s)
    else : print(s)