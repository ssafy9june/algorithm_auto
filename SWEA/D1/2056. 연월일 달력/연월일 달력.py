T = int(input())
# for tc in range (1, T+1):

truedays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, T+1):

    ymd = str(input())
    for i in range(0,12):
            if int(ymd[4:6]) == i+1:
                if int(ymd[6:8]) <= truedays[i]:
                    print(f'#{tc} {ymd[0:4]}/{ymd[4:6]}/{ymd[6:8]}')
                else:
                    print(f'#{tc} -1')
    if int(ymd[4:6]) <= 0:
        print(f'#{tc} -1')