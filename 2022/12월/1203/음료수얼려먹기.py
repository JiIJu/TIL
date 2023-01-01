#이코테 음료수얼려먹기

def dfs(x,y):
    if data[x][y]=='0':
        data[x][y]='1'
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<M and data[nx][ny]=='0':
                dfs(nx,ny)
        return True
    return False

N,M = map(int,input().split())
data = [list(input()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt=0
for i in range(N):
    for j in range(M):
        if dfs(i,j):
            cnt+=1
print(cnt)