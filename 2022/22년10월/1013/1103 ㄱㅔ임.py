import sys
sys.setrecursionlimit(999999)

def dfs(i,j,cnt):
    global maxv
    maxv=max(maxv,cnt)

    for d in range(4):
        ni = i+di[d]*int(data[i][j])
        nj = j+dj[d]*int(data[i][j])
        if 0<=ni<N and 0<=nj<M and data[ni][nj]!='H' and cnt+1>check[ni][nj]:
            if visit[ni][nj]==1:
                print(-1)
                exit()
            else:
                check[ni][nj]= cnt+1
                visit[ni][nj]=1
                dfs(ni,nj,cnt+1)
                visit[ni][nj]=0


N , M = map(int,input().split())
check = [[0]*M for _ in range(N)]
di = [-1,1,0,0]
dj = [0,0,-1,1]
visit = [[0]*M for _ in range(N)]
data = []
for i in range(N):
    data.append(list(input()))
ans=0
maxv=0
dfs(0,0,0)
print(maxv+1)