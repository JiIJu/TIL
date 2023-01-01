# 7576 토마토
from collections import deque
import sys
def bfs():
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<M and data[nx][ny]==0:
                data[nx][ny]=data[x][y]+1
                q.append((nx,ny))

M , N = map(int,input().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
for i in range(N):
    for j in range(M):
        if data[i][j]==1:
            q.append((i,j))
maxv = 0
temp = 0


bfs()
for i in data:
    if 0 in i:
        temp=1
        print(-1)
        break
    maxv = max(max(i),maxv)
if temp==0:
    print(maxv-1)

