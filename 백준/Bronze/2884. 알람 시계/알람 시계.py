H, M = map(int, input().split())
NH, NM = 0, 0
if M - 45 >= 0:
    NH, NM = H, M-45
else:
    NH, NM = H-1, M+60-45
if H == 0 and M - 45 < 0:
    NH = 23
print(NH, NM)