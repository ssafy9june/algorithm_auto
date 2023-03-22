T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    for obj in S:
        print(obj*R, end='')
    print()