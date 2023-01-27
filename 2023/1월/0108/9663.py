# 9663 N-Queen

def visit(x,y,visited):
    check = [a[:] for a in visited]
    for i in range(1,N-x):
        check[x+i][y] = 1
        if 0<= y-i < N:
            check[x+i][y-i] = 1
        if 0<= y+i <N:
            check[x+i][y+i] = 1
    return check

def dfs(x,visited):
    global cnt
    for i in range(x,N):
        if sum(visited[x])==N:
            return 0
    if x==N-1:
        cnt += N - sum(visited[x])
        return 0
    for i in range(N):
        if visited[x][i]==0:
            tmp = visit(x,i,visited)
            dfs(x+1,tmp)
N = int(input())
data = [[0]*N for _ in range(N)]
cnt = 0
dfs(0,data)
print(cnt)