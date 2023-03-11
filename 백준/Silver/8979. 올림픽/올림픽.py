N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

for i in range(N-1, 0, -1):
    for j in range(i):
        if lst[j][1] < lst[j+1][1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
        elif lst[j][1] == lst[j+1][1]:
            if lst[j][2] < lst[j+1][2]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            elif lst[j][2] == lst[j+1][2]:
                if lst[j][3] < lst[j+1][3]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

cnt = 0
if lst[0][0] == M:
    print(1)
else:
    for a in range(1, N):
        if lst[a-1][1] == lst[a][1] and lst[a-1][2] == lst[a][2] and lst[a-1][3] == lst[a][3]:
            cnt += 1
        else:
            cnt = 0
        if lst[a][0] == M:
            print(a+1-cnt)
