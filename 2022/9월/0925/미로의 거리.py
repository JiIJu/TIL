def dfs(S,G):
    # global cnt
    a,b = S[0],S[1]
    now = [a,b]
    visited[a][b] = 1
    stack.append(now)
    # stack.append(now)
    while True:
        for d in range(4):
            ni = now[0]+di[d]
            nj = now[1]+dj[d]
            if 0<=ni<N and 0<=nj<N and data[ni][nj]!=1 and visited[ni][nj]==0:
                stack.append(now)
                visited[ni][nj]= 1
                now = [ni,nj]
                # print(stack)
                # cnt+=1
                # print(now)
                break
        else:
            if stack:
                now = stack.pop()

        # print(visited)
        if now == G:
            return len(stack)
        elif len(stack)==0:
            return 0


T = int(input())

for tc in range(1,T+1):
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    N = int(input())
    cnt = 0
    data = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            data[i][j] = int(data[i][j])
            if data[i][j] == 2:
                S = [i,j]
            elif data[i][j] == 3:
                G = [i,j]
    stack = []
    visited = [[0]*N for _ in range(N)]
    ans = dfs(S,G)
    print(ans)