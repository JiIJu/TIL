def dfs(i,j,s,N):
    global answer
    global minV
    if maze[i][j] ==3:
        answer +=1
        if minV > s:
            minV = s
        return
    else:
        visited[i][j] == 1
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di , j +dj
            if maze[ni][nj] !=1 and visited[ni][nj] == 0:
                dfs(ni,nj,N)
        visited[i][j] = 0
        return