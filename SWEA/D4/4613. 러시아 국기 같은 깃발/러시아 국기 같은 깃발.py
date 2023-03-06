def change_cnt(loc1, loc2, array, color):
    sr, sc = loc1
    er, ec = loc2
    ccnt = 0
    # 해당하는 색과 다르면 ccnt++
    for cr in range(sr, er+1):
        for cc in range(sc, ec+1):
            if array[cr][cc] != color:
                ccnt += 1
    return ccnt


color_dict = {'W': 1, 'B': 2, 'R': 3}  # 숫자로 저장해서 index 활용하기 위해 생성

T = int(input())
for tcnum in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * M for _ in range(N)]

    # 주어진 데이터를 color_dict를 활용해 숫자 2차원 배열로 저장
    for r in range(N):
        ipt = input()
        for c in range(M):
            arr[r][c] = color_dict[ipt[c]]

    mn = 2501  # 새로 칠하는 칸의 개수의 최솟값
    for r1 in range(1, N-1):
        for r2 in range(r1, N):
            rnge = [(0, 0), (r1-1, M-1), (r1, 0), (r2-1, M-1), (r2, 0), (N-1, M-1)]
            sum_cnt = 0
            for i in range(1, 4):
                cnt = change_cnt(rnge[(i-1)*2], rnge[(i-1)*2+1], arr, i)
                sum_cnt += cnt
            if mn > sum_cnt:
                mn = sum_cnt

    print(f'#{tcnum} {mn}')