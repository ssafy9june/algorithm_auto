N = int(input())
length = len(str(N))


a = N - (length*9) if (N - (length*9) > 0) else 0
sm = 0
while sm != N:
    if a > N:
        a = 0
        break
    else:
        a += 1
        sm = a
        for obj in str(a):
            sm += int(obj)
print(a)