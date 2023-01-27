# 13565 침투
import sys

def bfs(i,j):
    q = [(i,j)]
    while q:
        x,y = q.pop(0)
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<M and 0<=ny<N and data[nx][ny]=='0':
                data[nx][ny] = '2'
                q.append((nx,ny))


M , N = map(int,input().split())

data = [list(sys.stdin.readline().rstrip()) for _ in range(M)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]
start = []
for i in range(N):
    if data[0][i]=='0':
        start.append(i)

for i in start:
    bfs(0,i)
check = 0
if '2' in data[M-1]:
    check=1
# print(start,data)
if check:
    print('YES')
else:
    print('NO')