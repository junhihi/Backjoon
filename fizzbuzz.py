def fizzbuzz(a):
    if a % 3 == 0 and a % 5 == 0:
        print('FizzBuzz')
    elif a % 3 == 0:
        print('Fizz')
    elif a % 5 == 0:
        print('Buzz')
    else: print(a)

a = input()
b = input()
c = input()

l = [a,b,c]
s = 0
for i in l:
    try:
        s = int(i)
    except:
        continue

s += 3 - l.index(str(s))
fizzbuzz(s)