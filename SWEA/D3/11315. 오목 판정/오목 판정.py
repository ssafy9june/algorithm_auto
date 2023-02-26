T = int(input())

dr = [0, 1, 1, 1]
dc = [1, 0, 1, -1] # 우, 하, 오른쪽대각선, 왼쪽대각선

for tc in range(1, T+1):
    N = int(input())
    arr = [[0 if i == '.' else 1 for i in input()] for _ in range(N)]

    ans = 'NO'
    for r in range(N):
        for c in range(N):
            for i in range(4):
                for k in range(5):
                    nr = r + dr[i] * k
                    nc = c + dc[i] * k
                    if not 0 <= nr < N or not 0 <= nc < N or arr[nr][nc] == 0:
                        break
                else:
                    ans = 'YES'

    print(f'#{tc} {ans}')