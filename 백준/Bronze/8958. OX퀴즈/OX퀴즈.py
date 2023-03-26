T = int(input())
for _ in range(T):
    score, cnt = 0, 0
    ipt = input()
    for obj in ipt:
        if obj == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)