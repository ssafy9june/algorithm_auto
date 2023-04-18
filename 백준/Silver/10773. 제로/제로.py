import sys
from collections import deque

input = sys.stdin.readline
S = deque()

N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        S.pop()
    else:
        S.append(num)

print(sum(S))