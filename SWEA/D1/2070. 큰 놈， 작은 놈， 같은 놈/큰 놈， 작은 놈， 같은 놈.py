T = int(input())
for tc in range (1, T+1):
    hi = list(map(int, input().split()))
    if hi[0] > hi[1]:
        answer = '>'
    elif hi[0] == hi[1]:
        answer = '='
    else:
        answer = '<'
    
    print(f'#{tc} {answer}')