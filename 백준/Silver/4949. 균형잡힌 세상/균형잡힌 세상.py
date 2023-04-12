import sys
from collections import deque


def func(string):
    s = deque()
    for char in string:
        if char == '(' or char == '[':
            s.append(char)
        elif char == ')' or char == ']':
            if s and s[-1] == dct.get(char):
                s.pop()
            else:
                return 'no'
    else:
        if not s:
            return 'yes'
    return 'no'


dct = {')': '(', ']': '['}
while True:
    ipt = sys.stdin.readline().rstrip()
    if ipt == ".":
        break
    print(func(ipt))
