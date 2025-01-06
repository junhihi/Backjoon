import sys

input = sys.stdin.readline

while 1:
    try:
        l = [int(i) for i in input().split()]
        li = [i for i in range(1,l[0])]
        tf = True
        for i in range(l[0]-1):
            j = l[i+1]
            k = l[i+2]
            ab = abs(j - k) - 1
            if li[ab] == 0 or ab < 0 or len(l) != l[0] + 1:
                print("Not jolly")
                tf = False
                break
            else:
                li[ab] = 0
        if tf:
            print("Jolly")
    except:
        break