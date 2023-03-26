N = int(input())
lst = list(map(int, input().split()))
mx, mn = -1000000, 1000000
for obj in lst:
    if mx < obj:
        mx = obj
    if mn > obj:
        mn = obj
print(mn, mx)