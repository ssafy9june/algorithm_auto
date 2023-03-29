N, X = map(int, input().split())
lst = list(map(int, input().split()))

for obj in lst:
    if obj < X:
        print(obj, end=' ')