lst = [0] * 5

for i in range(5):
    lst[i] = sum(list(map(int, input().split())))

mx = 0
mx_idx = 0
for j in range(5):
    if mx < lst[j]:
        mx = lst[j]
        mx_idx = j

print(mx_idx+1, mx)