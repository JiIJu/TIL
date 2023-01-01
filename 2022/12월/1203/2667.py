# 단지번호붙이기

def dfs(x,y,a):
    if data[x][y]==1:
        data[x][y]=a+1
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<N and data[nx][ny]==1:
                dfs(nx,ny,a)
        return True
    return False
N = int(input())
data = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        data[i][j] = int(data[i][j])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
k=1
for i in range(N):
    for j in range(N):
        if dfs(i,j,k):
            k+=1
maxv=0
for i in data:
    maxv=max(max(i),maxv)
num = [0]*maxv
for i in range(1,maxv):
    for j in range(N):
        for k in range(N):
            if data[j][k] == i+1:
                num[i]+=1
print(maxv-1)
num.sort()
for i in range(1,maxv):
    print(num[i])
