A, B = input().split()
NA, NB = 0, 0
for i in range(3):
    NA += int(A[i]) * 10**i
    NB += int(B[i]) * 10**i
print(NA) if NA > NB else print(NB)