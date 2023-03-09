ipt = int(input())
cnt = 0
N = -1

while N != ipt:
    if N == -1:
        N = ipt
    if N < 10:
        N = N + 10*N
        cnt += 1
    else:
        N = (N % 10) * 10 + (N % 10 + N // 10) % 10
        cnt += 1
print(cnt)