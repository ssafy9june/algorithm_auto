cnt_lst = [0] * 42
for _ in range(10):
    cnt_lst[int(input())%42] = 1
print(sum(cnt_lst))