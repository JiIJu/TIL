#미로탐색

def bfs(i,j):
    cnt=1
    q = [(i,j)]
    while q:
        x,y = q.pop(0)
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<M and data[nx][ny]==1:
                data[nx][ny]= data[x][y]+1
                q.append((nx,ny))
N ,M = map(int,input().split())
data = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        data[i][j] = int(data[i][j])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
data[0][0]=0
bfs(0,0)
print(data[N-1][M-1]+1)