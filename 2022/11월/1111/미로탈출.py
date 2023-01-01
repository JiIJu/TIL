def dfs(i,j,cnt):
    global minv
    if i==N-1 and j ==M-1:
        minv= min(minv,cnt)
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<N and 0<=nj<M and data[ni][nj]=='1' and visit[ni][nj]==0:
            # print(ni,nj)
            visit[ni][nj] = 1
            dfs(ni,nj,cnt+1)
            visit[i][j] = 0

import sys
N , M = map(int,input().split())

data = [list(sys.stdin.readline().strip('\n')) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
di = [-1,1,0,0]
dj = [0,0,-1,1]
minv = 99999
dfs(0,0,0)
print(minv+1)
