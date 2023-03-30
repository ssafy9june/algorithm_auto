N = int(input())
lst = []
for i in range(N):
    ipt = input()
    if ipt not in lst:
        lst.append(ipt)
lst.sort()
lst = sorted(lst, key=lambda x: len(x))

for k in range(len(lst)):
    print(lst[k])