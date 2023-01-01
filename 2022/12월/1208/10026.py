# 적록색약

def bfs(i,j,check):
    q = [(i,j)]
    while q:
        x,y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N and data[nx][ny]==check and visit1[nx][ny]==0:
                visit1[nx][ny]=1
                q.append((nx,ny))
def bfs2(i,j,check):
    q = [(i,j)]
    while q:
        x,y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if check=='B':
                if 0<=nx<N and 0<=ny<N and data[nx][ny]=='B' and visit2[nx][ny]==0:
                    visit2[nx][ny]=1
                    q.append((nx,ny))
            else:
                if 0<=nx<N and 0<=ny<N  and visit2[nx][ny]==0 and (data[nx][ny]=='R' or data[nx][ny]=='G'):
                    visit2[nx][ny]=1
                    q.append((nx,ny))


N = int(input())

data = [list(input()) for _ in range(N)]
# data2 = [[0]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         data2[i][j] = data[i][j]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt=0
cnt2=0
visit1 = [[0]*N for _ in range(N)]
visit2 = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit1[i][j]==0:
            bfs(i,j,data[i][j])
            cnt+=1
for i in range(N):
    for j in range(N):
        if visit2[i][j]==0:
            bfs2(i,j,data[i][j])
            cnt2+=1
print(cnt,cnt2)