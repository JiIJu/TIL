def bfs():
    cost = [[99999]*N for _ in range(N)]
    cost[0][0] = 0
    q = [(0,0)]

    while q:
        i,j = q.pop(0)
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<N:
                if data[ni][nj]> data[i][j] and  cost[ni][nj]>1+cost[i][j]+data[ni][nj]-data[i][j]:
                    cost[ni][nj] = 1 + cost[i][j]+ data[ni][nj]-data[i][j]
                    q.append((ni, nj))
                elif data[ni][nj]<=data[i][j] and cost[ni][nj]>1+cost[i][j]:
                    cost[ni][nj] = 1+cost[i][j]
                    q.append((ni,nj))

    return cost[N-1][N-1]

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    data = [list(map(int,input().split())) for _ in range(N)]

    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    print(f'#{tc} {bfs()}')
