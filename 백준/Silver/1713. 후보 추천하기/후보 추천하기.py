N = int(input())
M = int(input())
ipt_lst = list(map(int, input().split()))

cnt_lst = [0] * 101
lst = []

for i in ipt_lst:
    if i in lst:
        cnt_lst[i] += 1
    else:
        if len(lst) != N:
            cnt_lst[i] += 1
            lst.append(i)
        else:
            mn = 999999999999
            mn_idx = 0
            for j in lst:
                if mn > cnt_lst[j]:
                    mn = cnt_lst[j]
                    mn_idx = j

            k_lst = []
            for k in range(N):
                if cnt_lst[lst[k]] == mn:
                    k_lst.append(k)

            cnt_lst[lst[k_lst[0]]] = 0
            lst.pop(k_lst[0])

            lst.append(i)
            cnt_lst[i] += 1

lst.sort()
print(*lst)