def func(ipt):
    n = len(ipt)
    if n % 2 == 1:
        for i in range(n//2):
            if ipt[i] != ipt[n-1-i]:
                return 'no'
        else:
            return 'yes'
    else:
        for i in range(n//2):
            if ipt[i] != ipt[n-1-i]:
                return 'no'
        else:
            return 'yes'


while True:
    num = input()
    if num == '0':
        break
    print(func(num))