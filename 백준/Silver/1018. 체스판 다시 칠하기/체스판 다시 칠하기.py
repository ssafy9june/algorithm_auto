N, M = map(int, input().split())
arr = [input() for _ in range(N)]

cnt1, cnt2 = 0, 0
ans = 0xffffff
for ar in range(N - 7):
    for ac in range(M - 7):
        cnt1, cnt2 = 0, 0
        for r in range(8):
            for c in range(8):
                if (ar + r + ac + c) % 2 == 0:
                    if arr[ar + r][ac + c] == 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if arr[ar + r][ac + c] == 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        tmp = cnt1 if cnt1 < cnt2 else cnt2
        if ans > tmp:
            ans = tmp
print(ans)

