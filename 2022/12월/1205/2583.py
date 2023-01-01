# 영역구하기
import sys
sys.setrecursionlimit(10*9)
def dfs(x,y):
    size = 0
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<=nx<M+1 and 0<=ny<N+1 and data[nx][ny]==0 and visit[nx][ny]==0:
            visit[nx][ny]=1
            dfs(nx,ny)
            size+=1
    res.append(size)
def bfs(x,y):
    q = [(x,y)]
    size=1
    while q:
        i,j = q.pop(0)
        for d in range(4):
            ni = i+dx[d]
            nj = j+dy[d]
            if 0 <= ni < M  and 0 <= nj < N  and data[ni][nj] == 0:
                data[ni][nj]=1
                q.append((ni,nj))
                size+=1
    res.append(size)

M , N , K = map(int,input().split())

data = [[0]*(N) for _ in range(M)]
for i in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            data[i][j]=1
visit = [[0]*(N+1) for _ in range(M+1)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
res=[]
# for i in range(M+1):
#     for j in range(N+1):
#         if visit[i][j]==0 and data[i][j]==0:
#             visit[i][j]=1
#             dfs(i,j)
#             cnt+=1
for i in range(M):
    for j in range(N):
        if data[i][j]==0:
            bfs(i,j)
            cnt+=1

print(cnt)
res.sort()
for i in res:
    if i==0:
        print(i+1)
    else:
        print(i)
'''
[[0, 0, 0, 0, 1, 1, 1, 0],
[0, 1, 1, 0, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 0, 0, 0],
[1, 1, 1, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0]]

'''