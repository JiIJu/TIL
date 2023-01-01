def dfs(v):
    visit1[v]=1
    print(v,end=' ')
    for i in range(1,N+1):
        if visit1[i]==0 and data[v][i]==1:
            dfs(i)

def bfs(v):
    visit2[v]=1
    q=[]
    q.append(v)
    while q:
        s = q.pop(0)
        print(s,end=' ')
        for i in range(1,N+1):
            if visit2[i]==0 and data[s][i]==1:
                q.append(i)
                visit2[i]=1

#N:정점수 M:간선수 V:시작정점
N , M , V = map(int,input().split())
visit1=[0]*(N+1)
visit2=[0]*(N+1)
data = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    data[a][b]=1
    data[b][a]=1
dfs(V)
print()
bfs(V)
