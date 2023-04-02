A, B = map(int, input().split())
#
# for i in range(min(A, B), 0, -1):
#     if A % i == 0 and B % i == 0:
#         print(i)
#         num = i
#         while True:
#             if num % A == 0 and num % B == 0:
#                 print(num)
#                 break
#             else:
#                 num += i

A_cnt = [0] * 10000
B_cnt = [0] * 10000

i = 2
while A != 1:
    if A % i == 0:
        A_cnt[i] += 1
        A = A // i
        i = 2
    else:
        i += 1

i = 2
while B != 1:
    if B % i == 0:
        B_cnt[i] += 1
        B = B // i
        i = 2
    else:
        i += 1

sm, lg = 1, 1
for j in range(10000):
    if A_cnt[j] == 0 and B_cnt[j] == 0:
        continue
    elif A_cnt[j] != 0 and B_cnt[j] != 0:
        sm *= j ** (min(A_cnt[j], B_cnt[j]))
    lg *= j ** (max(A_cnt[j], B_cnt[j]))

print(sm)
print(lg)