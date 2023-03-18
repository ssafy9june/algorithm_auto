K = int(input())
d_lst, l_lst = [], []
cnt_lst = [0] * 6

for _ in range(6):
    d, l = map(int, input().split())
    d_lst.append(d)
    l_lst.append(l)

d_lst.insert(0, d_lst[5])
l_lst.insert(0, l_lst[5])
d_lst.append(d_lst[1])
l_lst.append(l_lst[1])

br, bc = 0, 0
for j in range(6):
    if d_lst[j] == 1 or d_lst[j] == 2:
        if bc < l_lst[j]:
            bc = l_lst[j]
    else:
        if br < l_lst[j]:
            br = l_lst[j]

sr, sc = 0, 0
for i in range(1, 7):
    if d_lst[i] == 1 or d_lst[i] == 2:
        if l_lst[i-1] != br and l_lst[i+1] != br:
            sr = l_lst[i]
    else:
        if l_lst[i - 1] != bc and l_lst[i + 1] != bc:
            sc = l_lst[i]


print(K*(br*bc-sr*sc))