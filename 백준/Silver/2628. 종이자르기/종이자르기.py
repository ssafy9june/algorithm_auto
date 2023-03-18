c, r = map(int, input().split())
N = int(input())
R, C = [], []

for _ in range(N):
    d, n = map(int, input().split())
    if d == 0:
        R.append(n)
    else:
        C.append(n)

R.append(0)
R.append(r)
C.append(0)
C.append(c)

R.sort()
C.sort()

mxr = 0
for ri in range(0, len(R)-1):
    if mxr < R[ri+1] - R[ri]:
        mxr = R[ri+1] - R[ri]

mxc = 0
for ci in range(0, len(C)-1):
    if mxc < C[ci+1] - C[ci]:
        mxc = C[ci+1] - C[ci]

print(mxr*mxc)