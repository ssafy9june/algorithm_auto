lst = [0]*10

for i in range(10):
    lst[i] = int(input())

for j in range(1, 10):
    lst[j] = lst[j-1] + lst[j]

lst.append(0xffff)

ans = 0
for k in range(10):
    if lst[k] <= 100 < lst[k+1]:
        if 100 - lst[k] < lst[k+1] - 100:
            ans = lst[k]
        else:
            ans = lst[k+1]


print(ans)