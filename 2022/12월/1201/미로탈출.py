# 이코테 미로탈출

def bfs(a,b):
    q = [(a,b)]
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and data[nx][ny]==1:
                data[nx][ny] = data[x][y]+1
                q.append((nx, ny))


N , M = map(int,input().split())
data = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        data[i][j] = int(data[i][j])
graph = [[0]*M for _ in range(N)]
minV = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
bfs(0,0)
print(data[N-1][M-1])