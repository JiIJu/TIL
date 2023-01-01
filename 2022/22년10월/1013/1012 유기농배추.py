def bfs(n):
    global cnt
    q=[]
    for a in range(N):
        for b in range(M):
            if data[a][b]==1 and visit[a][b]==0:
                q.append((a,b))
                while q:
                    i,j = q.pop(0)
                    for d in range(4):
                        ni = i + di[d]
                        nj = j + dj[d]
                        while 0<=ni<N and 0<=nj<M and visit[ni][nj]==0 and data[ni][nj]==1:
                            visit[ni][nj]=1
                            q.append((ni,nj))

                cnt+=1

T = int(input())
for tc in range(T):
    # M:가로 N:세로 K:배추수
    M , N , K = map(int,input().split())
    data = [[0]*M for _ in range(N)]
    cab = []
    for i in range(K):
        a,b = map(int,input().split())
        data[b][a] = 1
        cab.append((b,a))

    visit = [[0]*M for _ in range(N)]
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    cnt = 0
    bfs(0)
    print(cnt)