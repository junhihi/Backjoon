a, b, v = map(int, input().split())


day = (v - a) / (a - b)

if day <= 0:
    print(1)
else:
    if day == int(day):
        print(int(day)+1)
    else: 
        print(int(day)+2)