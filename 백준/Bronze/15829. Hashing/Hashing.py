N = int(input())
ipt = input()

hashV = 0
for i in range(N):
    hashV += (ord(ipt[i])-96) * 31**i
print(hashV)