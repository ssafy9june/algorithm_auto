dr = (-1, -1, -1, 0, 0, 1, 1, 1)
dc = (-1, 0, 1, -1, 1, -1, 0, 1)

# 주어진 돌의 반대되는 돌을 인덱스를 활용해 선언
opp = (0, 2, 1)

T = int(input())
for tcnum in range(1, T+1):
    # 판의 크기 N, 놓는 횟수 M
    N, M = map(int, input().split())
    arr = [[0] * (N+2) for _ in range(N+2)]  # 패딩 활용

    # 헷갈리지 않게 검은돌 하얀돌 변수선언
    black, white = 1, 2

    # 중간 돌 설정
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = white
    arr[N//2+1][N//2] = arr[N//2][N//2+1] = black

    for i in range(M):
        # 문제를 잘 읽고 데이터가 어떻게 주어지는 반드시 확인!!
        c, r, color = map(int, input().split())
        arr[r][c] = color

        for d in range(8):
            lst = []
            for k in range(1, N):
                nr = r + dr[d] * k
                nc = c + dc[d] * k
                if arr[nr][nc] == opp[color]:
                    lst.append((nr, nc))
                elif arr[nr][nc] != opp[color]:  # 나랑 같은 색이거나 0인 경우 일단 break
                    break
            if arr[nr][nc] == color:  # 만약 break한 이유가 나랑 같은 색이라면
                while lst:  # lst 내부의 좌표를 활용해 나랑 같은 색으로 바꿔줌
                    tr, tc = lst.pop()
                    arr[tr][tc] = color

    bcnt = wcnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == white:
                wcnt += 1
            elif arr[i][j] == black:
                bcnt += 1

    print(f'#{tcnum} {bcnt} {wcnt}')