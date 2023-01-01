#11724 연결요소의 개수
import sys
sys.setrecursionlimit(10**6)

def dfs(s):
    for i in data[s]:
        if visit[i]==0:
            visit[i]=1
            dfs(i)

N , M = map(int,input().split())
data = [[] for _ in range(N+1)]
visit =[0]*(N+1)
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)
cnt = 0
for i in range(1,N+1):
    if visit[i]==0:
        dfs(i)
        cnt+=1
print(cnt)


