def bingo(arr, lst):
    n_cnt = 0
    for num in lst:
        for r in range(5):
            for c in range(5):
                if arr[r][c] == num:
                    arr[r][c] = 0
                    n_cnt += 1
                    if bingo_check(arr) == 1:
                        return n_cnt


def bingo_check(arr):
    b_cnt = 0
    for r in range(5):
        for c in range(5):
            for i in range(4):
                for k in range(5):
                    nr = r + dr[i] * k
                    nc = c + dc[i] * k
                    if 0 > nr or nr >= 5 or 0 > nc or nc >= 5 or arr[nr][nc] != 0:
                        break
                else:
                    b_cnt += 1
    if b_cnt >= 3:
        return 1
    else:
        return 0


dr = (-1, -1, -1, 0)
dc = (0, -1, 1, 1)

array = [list(map(int, input().split())) for _ in range(5)]
call_lst = []
for _ in range(5):
    call_lst.extend(list(map(int, input().split())))

print(bingo(array, call_lst))