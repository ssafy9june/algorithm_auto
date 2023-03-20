cnt_lst = [0] * 26
for char in input():
    cnt_lst[ord(char.upper())-65] += 1

mx = max(cnt_lst)
if cnt_lst.count(mx) > 1:
    print('?')
else:
    print(chr(cnt_lst.index(mx)+65))
