# 5397 키로거

from collections import deque

T = int(input())

for tc in range(T):
    data = input()
    q = []
    w = []
    for i in data:
        if i=='<':
            if q:
                w.append(q.pop())
        elif i=='>':
            if w:
                q.append(w.pop())
        elif i=='-':
            if not q:
                continue
            else:
                q.pop()
        else:
            q.append(i)
    for i in q:
        print(i,end='')
    for i in w[::-1]:
        print(i,end='')
