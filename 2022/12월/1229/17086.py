# 17086 아기상어2

def bfs(i,j):
    q = [(i,j,0)]
    visit = [[0]*M for _ in range(N)]
    visit[i][j]=1
    while q:
        x,y,cnt = q.pop(0)
        if data[x][y]==1:
            return cnt
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny]==0:
                q.append((nx,ny,cnt+1))
                visit[nx][ny]=1

N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,0,1,1,1,0,-1,-1]
dy = [1,1,1,0,-1,-1,-1,0]
maxv = 0
for i in range(N):
    for j in range(M):
        if data[i][j]==0:
            maxv = max(bfs(i,j),maxv)
print(maxv)