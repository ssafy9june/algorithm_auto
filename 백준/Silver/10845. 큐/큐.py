import sys

N = int(sys.stdin.readline().strip())

Q = [0] * 10000
front = rear = -1

for _ in range(N):
    ipt = sys.stdin.readline().strip()
    if ipt == 'front':
        if rear != front:
            print(Q[front+1])
        else:
            print(-1)
    elif ipt == 'back':
        if rear != front:
            print(Q[rear])
        else:
            print(-1)
    elif ipt == 'size':
        print(rear - front)
    elif ipt == 'pop':
        if rear != front:
            front += 1
            print(Q[front])
        else:
            print(-1)
    elif ipt == 'empty':
        if rear != front:
            print(0)
        else:
            print(1)
    else:
        command, num = ipt.split()
        num = int(num)
        rear += 1
        Q[rear] = num