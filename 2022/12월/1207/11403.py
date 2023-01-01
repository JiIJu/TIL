#경로찾기

def bfs(x):
    check = [0]*N
    q = [x]
    while q:
        a = q.pop(0)
        for i in range(N):
            if check[i]==0 and data[a][i]==1:
                q.append(i)
                check[i]=1
                visit[x][i]=1

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

for i in range(N):
    bfs(i)

for i in visit:
    print(*i)