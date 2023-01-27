# 14620 꽃길

def check(i,j,visited):
    for d in range(4):
        nx = i+dx[d]
        ny = j+dy[d]
        if (nx,ny) in visited:
            return False
    return True

def dfs(visited,total):
    global ans
    if total>=ans:
        return
    if len(visited)==15:
        ans = min(ans,total)
    else:
        for i in range(1,N-1):
            for j in range(1,N-1):
                if check(i,j,visited) and (i,j) not in visited:
                    temp = [(i,j)]
                    temp_cost = data[i][j]
                    for d in range(4):
                        nx = i+dx[d]
                        ny = j + dy[d]
                        temp.append((nx,ny))
                        temp_cost+=data[nx][ny]
                    dfs(visited+temp,total+temp_cost)

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 9999999
dfs([],0)
print(ans)