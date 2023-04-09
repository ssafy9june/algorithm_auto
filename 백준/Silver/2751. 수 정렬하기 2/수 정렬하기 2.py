import sys

from heapq import heappush, heappop

N = int(input())
lst = []
for i in range(N):
    heappush(lst, int(sys.stdin.readline()))

while lst:
    print(heappop(lst))