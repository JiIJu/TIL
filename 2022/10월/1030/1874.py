# 수택수열
import sys
n = int(input())
data = [0]*n
for i in range(n):
    data[i] = int(sys.stdin.readline().strip('\n'))
stack = []
tmp= 1
q=[]
ans = 0
for i in range(n):
    a = data[i]
    while tmp<=a:
        stack.append(tmp)
        q.append('+')
        tmp+=1
    if stack[-1] == a:
        stack.pop()
        q.append('-')
    elif stack[-1]>a:
        print('NO')
        ans = 1
        break
if ans == 0:
    for i in q:
        print(i)