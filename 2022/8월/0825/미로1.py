def bfs(data,start,goal):
    stack = []
    visited = [[0]*16 for _ in range(16)]
    stack.append(start)
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    i,j = start
    visited[i][j] = 1
    now = [i,j]
    while stack:

        for d in range(4):
           ni = i + di[d]
           nj = j + dj[d]
           if 0<=ni<16 and 0<=nj<16 and visited[ni][nj] ==0 and data[ni][nj]!=1:
               stack.append([i,j])
               visited[ni][nj] = 1
               i,j = ni , nj
               now = [i,j]

               break
        else:
            if stack:
                now = stack.pop()
                i,j = now[0],now[1]

        if now == goal:
            return 1
        elif len(stack)==0:
            return 0

for tc in range(1,11):
    T = int(input())
    data = [list(input()) for _ in range(16)]
    start,goal = [],[]
    for i in range(16):
        for j in range(16):
            data[i][j] = int(data[i][j])

    for i in range(16):
        for j in range(16):
            if data[i][j] == 2:
                start += [i,j]
            elif data[i][j] == 3:
                goal += [i,j]

    s = bfs(data,start,goal)
    print(f'#{T} {s}')