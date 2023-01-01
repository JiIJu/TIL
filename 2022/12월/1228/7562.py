# 7562 나이트의 이동
# import sys
# sys.setrecursionlimit(10**9)
def dfs(x,y,cnt):
    global minv
    if cnt>=minv:
        return
    if x==goal[0] and y==goal[1]:
        # print(x,y,cnt)
        minv = min(visit[goal[0]][goal[1]],minv)
        return

    for d in range(8):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<=nx<N and 0<=ny<N and (visit[x][y]+1<visit[nx][ny]):
            visit[nx][ny]= visit[x][y]+1
            dfs(nx,ny,cnt+1)
            # visit[nx][ny] = temp
def bfs(i,j):
    q = [(i,j,0)]
    while q:
        x,y,cnt = q.pop(0)
        if x==goal[0] and y==goal[1]:
            return cnt
        for d in range(8):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny]==0:
                q.append((nx,ny,cnt+1))
                visit[nx][ny] = 1

T = int(input())

for tc in range(T):
    N = int(input())
    now = list(map(int,input().split()))
    goal = list(map(int,input().split()))
    # minv = 999999
    # temp=10**6
    visit = [[0]*N for _ in range(N)]

    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    # dfs(now[0],now[1],0)
    print(bfs(now[0],now[1]))
    # print(visit[goal[0]][goal[1]])