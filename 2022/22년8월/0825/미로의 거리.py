def bfs(start,finish,N):
    queue = []
    visited = [[0]*(N) for _ in range(N)]
    queue.append(start)
    global now
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    count = 0
    i,j = start
    visited[i][j] = 1
    while queue:

        # if visited[finish[0]][finish[1]] ==1:
        #     return len(queue)

        count = 0

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and data[ni][nj]!=1:
                queue.append([i,j])
                i,j = ni,nj
                visited[i][j] = 1
                now = [i,j]
                break
        else:
            if queue:
                now = queue.pop()
                i,j = now[0],now[1]
        if now == finish:
            print(now,finish)
            return len(queue)
        elif len(queue)==0:
            return 0




T = int(input())

for tc in range(1,T+1):
    N = int(input())

    data = [list(input()) for _ in range(N)]

    start = []
    finish = []
    for i in range(N):
        for j in range(N):
            data[i][j] = int(data[i][j])

    for i in range(N):
        for j in range(N):
            if data[i][j] ==2:
                start = [i,j]
            elif data[i][j] ==3:
                finish = [i,j]

    print(bfs(start,finish,N))
