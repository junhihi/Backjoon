import sys

while 1:
    b = sys.stdin.readline().rstrip()

    if b == '.':
         break

    cnt = 0
    scount = 0
    lcount = 0
    p = []
    for j in b:
        cnt += 1

        if j == '(':
            scount += 1 
            p.append(j)
        elif j == ')':
            if len(p) != 0 and p[len(p)-1] == '(':
                p.pop(len(p)-1)
                scount -= 1
            else:
                print('no')
                break
        elif j == '[':
            lcount += 1
            p.append(j)
        elif j == ']':
            if len(p) != 0 and p[len(p)-1] == '[':
                p.pop(len(p)-1)
                lcount -= 1
            else:
                print('no')
                break
        

        if scount < 0 or lcount < 0:
            print('no')
            break

        if cnt == len(b):
            if j == '.' and scount == 0 and lcount == 0:
                print('yes')
            else: print('no')