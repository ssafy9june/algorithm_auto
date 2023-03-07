A, B = input().split()
N, M = len(A), len(B)

com = ''
for i in range(N):
    if A[i] in A and A[i] in B:
        com = A[i]
        break

arr = [['.'] * N for _ in range(M)]

for i in range(N):
    arr[B.index(com)][i] = A[i]

for j in range(M):
    arr[j][A.index(com)] = B[j]

for a in range(M):
    for b in range(N):
        print(arr[a][b], end='')
    print()