T = int(input())
for tc in range(1, T+1):
    hi = list(map(int, input().split()))
    hi.sort()
    print(f'#{tc} {hi[-1]}')