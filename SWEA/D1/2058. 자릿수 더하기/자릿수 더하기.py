answer = 0
N = int(input())
# answer = answer + N // 1000
# N = N % 1000
# answer = answer + N // 100
# N = N % 100
# answer = answer + N // 10
# N = N % 10
# answer = answer + N // 1

for i in [1000, 100, 10, 1]:
    answer = answer + N//i
    N = N % i

print(answer)