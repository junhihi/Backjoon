import sys

N = int(sys.stdin.readline().rstrip())
num_list = [0] * 10001
for i in range(N):
    num_list[int(sys.stdin.readline().rstrip())] += 1

for i in range(len(num_list)):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)