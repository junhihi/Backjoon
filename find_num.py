import sys

n = int(sys.stdin.readline())
a = set([int(i) for i in sys.stdin.readline().split()])
m = int(sys.stdin.readline())
b = [int(i) for i in sys.stdin.readline().split()]

for i in b:
    if i in a:
        print(1)
    else: print(0)