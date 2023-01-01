def check(i,j,visit,n):
    global minv , l
    if n==len(core)-1:
        a=0
        for c in range(N):
            for d in range(N):
                if visit[c][d]==1:
                    a += visit[c][d]
        print(visit)
        minv = min(minv,a)
        return
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        temp=[[0]*N for _ in range(N)]
        for a in range(N):
            for b in range(N):
                if visit[a][b]==1:
                    temp[a][b]=1
        while 0<=ni<N and 0<=nj<N and visit[ni][nj]==0:
            visit[ni][nj]=1
            ni+=di[d]
            nj+=dj[d]
            # l +=1
        if ni<0 or ni>=N or nj<0 or nj>=N:
            i,j = core[n][0],core[n][1]
            check(i,j,visit,n+1)
            # print(visit)
            # visit = temp





T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int,input().split())))
    minv =99999
    l=0
    core = []
    visit = [[0]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j]==1 and i!=0 and i !=N-1 and j !=0 and j!=N-1:
                core.append((i,j))
                visit[i][j]=2
            if data[i][j]==1 and (i==0 or i==N-1 or j==N-1 or j==0):
                l+=1

    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    i,j = core.pop(0)
    check(i,j,visit,1)
    print(f'#{tc} {minv+l}')