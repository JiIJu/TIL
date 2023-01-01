# 10971 외판원순회2
import sys
def dfs(start,next,num):
    global minV
    if num>=minV:
        return
    # if n==N:
        # print(num+data[a][start])
    if len(visit)==N and data[next][start]!=0:
        minV = min(minV,num+data[next][start])
        return
    for i in range(N):
        if i not in visit and data[next][i]!=0:
            visit.append(i)
            dfs(start,i,num+data[next][i])
            visit.pop()
N = int(input())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

minV = 9999999
for i in range(N):
    visit = [i]
    dfs(i,i,0)
print(minV)