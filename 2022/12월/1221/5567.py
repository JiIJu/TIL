# 5567 결혼식


def dfs(n,k):
    if k==2:
        return
    for i in data[n]:
        if visit[i]==0:
            visit[i]=1
        dfs(i,k+1)
N = int(input())
M = int(input())
data = [[] for _ in range(N+1)]
visit = [0]*(N+1)
for i in range(M):
    a,b= map(int,input().split())
    data[a].append(b)
    data[b].append(a)
ans = [1]
visit = [0]*(N+1)
visit[1]=1
dfs(1,0)

print(visit.count(1)-1)