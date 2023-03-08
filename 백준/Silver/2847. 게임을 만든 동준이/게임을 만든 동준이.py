N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))

ans = 0
for i in range(N-1, 0, -1):
    if lst[i] <= lst[i-1]:
        diff = lst[i-1] - lst[i] + 1
        lst[i-1] -= diff
        ans += diff

print(ans)