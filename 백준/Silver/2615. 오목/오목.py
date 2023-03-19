def omok(arr):
    for r in range(19):
        for c in range(19):
            if arr[r][c] == 1 or arr[r][c] == 2:
                color = arr[r][c]
                for i in range(4):
                    for k in range(5):
                        nr = r + dr[i] * k
                        nc = c + dc[i] * k
                        if nr < 0 or nr >= 19 or nc < 0 or nc >= 19 or arr[nr][nc] != color:
                            break
                    else:
                        if 0 <= r+dr[i]*5 < 19 and 0 <= c+dc[i]*5 < 19 and arr[r+dr[i]*5][c+dc[i]*5] == color:
                            pass
                        elif 0 <= r+dr[i]*-1 < 19 and 0 <= c+dc[i]*-1 < 19 and arr[r+dr[i]*-1][c+dc[i]*-1] == color:
                            pass
                        else:
                            print(color)
                            print(r + 1, c + 1)
                            return
    print(0)
    return


dr = (-1, 0, 1, 1)
dc = (1, 1, 1, 0)

array = [list(map(int, input().split())) for _ in range(19)]
omok(array)