# 11725 트리의 부모찾기
import sys
def dfs():
    q = []
    for i in data[1]:
        q.append(i)
        ans[i]=1
    while q:
        a = q.pop(0)
        if visit[a]==0:
            visit[a]=1
            for j in data[a]:
                if visit[j]==0:
                    q.append(j)
                    ans[j]=a

N = int(input())
data = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)
ans = [0]*(N+1)
visit=[0]*(N+1)
dfs()
for i in range(2,N+1):
    print(ans[i])
    