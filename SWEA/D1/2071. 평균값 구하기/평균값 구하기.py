T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    answer = round(sum(numbers)/10)
    print(f'#{test_case} {answer}')