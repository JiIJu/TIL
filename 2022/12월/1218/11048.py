# 11048 이동하기
import sys
# sys.setrecursionlimit(10**8)
def bfs(i,j):
    q = [(i,j)]
    while q:
        x,y = q.pop(0)
        for d in range(2):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<N and ny<M:
                # visit[nx][ny] = max(visit[x][y] + data[nx][ny],visit[nx][ny])
                if visit[nx][ny] < data[nx][ny]+visit[x][y]:
                    visit[nx][ny] = data[nx][ny] + visit[x][y]
                    q.append((nx,ny))
    return

def dfs(x,y):
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<N and 0<=ny<M:
            visit[nx][ny] = max(visit[nx][ny],data[nx][ny]+visit[x][y])
            dfs(nx,ny)
N , M = map(int,input().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
visit[0][0] = data[0][0]+1
dx = [1,0]
dy = [0,1]
bfs(0,0)
# for i in range(N):
#     for j in range(M):
#         dfs(i,j)
# ans = [[0]*(M) for i in range(N)]
# for i in range(N):
#     for j in range(M):
#         for d in range(2):
#             nx , ny = i+dx[d] , j+dy[d]
#             if ans[i][j] < ans[nx][ny]+data[i][j]:
#                 ans[i][j] = ans[ny][nx]+data[i][j]
# print(ans[N-1][M-1])
print(visit[N-1][M-1]-1)