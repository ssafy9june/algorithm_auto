N, M = map(int, input().split())
lst = list(map(int, input().split()))

mx = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if mx < lst[i]+lst[j]+lst[k] <= M:
                mx = lst[i]+lst[j]+lst[k]
print(mx)