n, m = map(int, input().split())

tree = [int(i) for i in input().split()]
tree.sort(reverse=True)

cut = tree[0] - 1
while 1:
    sum = 0
    for i in tree:
        e = i - cut
        if e > 0:
            sum += e
        else: 
            break

    if sum < m:
        cut -= 1
    elif sum == m:
        break

print(cut)

n, m = map(int, input().split())
tree = [int(i) for i in input().split()]

start, end = 0, max(tree)

def wood_collected(height):
    return sum((i - height) for i in tree if i > height)

while start <= end:
    mid = (start + end) // 2
    total_wood = wood_collected(mid)

    if total_wood < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)
