rec = ''
N = int(input())
lst = [0] * N
S = [0] * N
for j in range(N):
    lst[j] = int(input())

i = -1
k = 0
num = 1
while k != N:
    if num > N+1:
        rec = 'NO'
        break
    else:
        if i == -1 or S[i] != lst[k]:
            i += 1
            S[i] = num
            rec += '+'
            num += 1
        elif S[i] == lst[k]:
            i -= 1
            rec += '-'
            k += 1
if rec != 'NO':
    for obj in rec:
        print(obj)
else:
    print(rec)




