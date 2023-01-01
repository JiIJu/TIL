# HSAT 장애물 인식 프로그램
def dfs(x,y,check):
    data[x][y] = check
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<=nx<N and 0<=ny<N and data[nx][ny]=='1':
            data[nx][ny] = check
            dfs(nx,ny,check)

N = int(input())

data = [list(input()) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
temp = 1
for i in range(N):
    for j in range(N):
        if data[i][j]=='1':
            dfs(i,j,temp)
            temp+=1
num = [0]*(N*N+1)

for i in range(N):
    for j in range(N):
        if data[i][j]!='0':
            num[int(data[i][j])]+=1
print(temp-1)
num.sort()

for i in num:
    if i!=0:
        print(i)
