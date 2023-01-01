#그룹단어 체커
import sys

N = int(input())
data = []
for i in range(N):
    data.append(sys.stdin.readline())
cnt=0
for i in range(N):
    stack=[]
    tmp=0
    for j in data[i]:
        if j not in stack:
            stack.append(j)
        elif stack[-1]!=j:
            tmp=1
            break
    if tmp==0:
        cnt+=1
print(cnt)