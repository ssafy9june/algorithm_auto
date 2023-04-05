def answer(string):
    global i
    for obj in string:
        if obj == '(':
            i += 1
        elif obj == ')':
            i -= 1
            if i < -1:
                return

T = int(input())
for _ in range(T):
    i = -1
    pa_str = input()
    answer(pa_str)
    ans = 'YES' if i == -1 else 'NO'
    print(ans)