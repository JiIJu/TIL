def dfs(x,y):

    for d in range(4):
        nx = x + di[d]
        ny = y + dj[d]
        if 0<=nx<N and 0<=ny<M and int(data[nx][ny])==0:
            data[nx][ny]=1
            dfs(nx,ny)
            # print(nx,ny)


import sys
N , M = map(int,input().split())
data = [list(sys.stdin.readline().strip('\n')) for _ in range(N)]

visit = [[0]*M for _ in range(N)]
# print(visit)
# print(data)
di = [-1,1,0,0]
dj = [0,0,-1,1]
cnt = 0
visit[0][0]=1
for i in range(N):
    for j in range(M):
        if data[i][j]=='0':
            dfs(i,j)
            cnt+=1
# print(visit)
print(cnt)