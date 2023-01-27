# 14502 연구소
from collections import deque
# 0빈칸 1벽 2바이러스

def bfs():
    global maxv
    ans=0
    visit = [a[:] for a in data]
    temp = deque()
    for i in virus:
        temp.append(i)
    while temp:
        x,y = temp.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny]==0:
                visit[nx][ny]=2
                temp.append([nx,ny])
    for i in visit:
        ans+=i.count(0)
    maxv = max(maxv,ans)

def wall(cnt):
    if cnt==3:
        bfs()
        return 0
    for i in range(N):
        for j in range(M):
            if data[i][j]==0:
                data[i][j]=1
                wall(cnt+1)
                data[i][j]=0


N , M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(M):
        if data[i][j]==2:
            virus.append((i,j))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
maxv = 0
wall(0)
print(maxv)