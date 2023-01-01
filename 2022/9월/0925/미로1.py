def bfs(S,G):
    a ,b= S[0],S[1]
    now = [a,b]
    stack.append(now)
    a=0
    while stack:
        for i in range(4):
            ni = now[0] + di[i]
            nj = now[1] + dj[i]
            if 0<=ni<16 and 0<=nj<16 and visited[ni][nj]==0 and data[ni][nj] != '1':
                now = [ni,nj]
                visited[ni][nj] = 1
                stack.append(now)
                # print(now , stack)
                break
        else:
            if stack:
                now = stack.pop()
        if now == G:
            a= 1
            return a
    return a




for tc in range(1,11):
    T = int(input())
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    visited = [[0] * 16 for _ in range(16)]
    stack = []
    data = [list(input()) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if data[i][j] == '2':
                S = [i,j]
            elif data[i][j] == '3':
                G = [i,j]
    ans = bfs(S,G)
    print(f'#{T} {ans}')