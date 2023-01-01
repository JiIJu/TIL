# 5212 지구온난화

def island(x,y):
    cnt = 0
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if nx<0 or nx>=R or ny<0 or ny>=C:
            cnt+=1
            continue
        if data[nx][ny]=='.':
            cnt+=1
    if cnt>=3:
        new_island[x][y]='.'

R , C = map(int,input().split())


data = [list(input()) for _ in range(R)]
new_island = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        new_island[i][j] = data[i][j]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(R):
    for j in range(C):
        if data[i][j]=='X':
            island(i,j)
check = []
for i in range(R):
    for j in range(C):
        if new_island[i][j]=='X':
            check.append((i,j))

i_min , i_max , j_min , j_max = 999,-100,999,-100
for i,j in check:
    i_min = min(i,i_min)
    i_max = max(i, i_max)
    j_min = min(j, j_min)
    j_max = max(j, j_max)

for i in range(i_min,i_max+1):
    for j in range(j_min,j_max+1):
        print(new_island[i][j],end='')
    print()
