N = int(input())
lst = list(map(int, input().split()))
M = int(input())
opp = [1, 0]
for _ in range(M):
    tp, num = map(int, input().split())
    if tp == 1:
        for i in range(1, N+1):
            if i % num == 0:
                lst[i-1] = opp[lst[i-1]]
    else:
        ch_lst = [num-1]
        flag = 0
        for j in range(1, 51):
            if flag == 1:
                break
            else:
                if num-j > 0 and num+j <= N and lst[num-j-1] == lst[num+j-1]:
                    ch_lst.append(num-j-1)
                    ch_lst.append(num+j-1)
                else:
                    flag = 1
                    break

        for obj in ch_lst:
            lst[obj] = opp[lst[obj]]

cnt = 0
while cnt != N:
    print(lst[cnt], end=' ')
    cnt += 1
    if cnt % 20 == 0:
        print()


