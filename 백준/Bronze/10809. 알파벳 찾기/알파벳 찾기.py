lst = [-1] * 26
ipt = input()
for i in range(len(ipt)):
    if lst[ord(ipt[i])-97] == -1:
        lst[ord(ipt[i])-97] = i

print(*lst)