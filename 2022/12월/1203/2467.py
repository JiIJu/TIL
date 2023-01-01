#안전영역
import sys
sys.setrecursionlimit(10**9)

def dfs(x,y,z):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<N and 0<=ny<N and visit[nx][ny]==0 and data[nx][ny]>z:
            visit[nx][ny]=1
            dfs(nx,ny,z)

N = int(input())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

maxv=0
for i in data:
    maxv = max(max(i),maxv)

max_cnt=0
for k in range(maxv+1):
    visit = [[0] * N for _ in range(N)]
    cnt=0
    for i in range(N):
        for j in range(N):
            if visit[i][j]==0 and data[i][j]>k:
                visit[i][j]=1
                dfs(i,j,k)
                cnt+=1

    max_cnt=max(cnt,max_cnt)
print(max_cnt)