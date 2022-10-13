def check(i,j,length,visit,n):
    global core,minv , l
    if n==N-1:
        # print(length)
        minv = min(minv,l)
        return
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        while 0<=ni<N and 0<=nj<N and visit[ni][nj]==0:
            visit[ni][nj]=2
            ni+=di[d]
            nj+=dj[d]
            l +=1
        if ni<0 or ni>=N or nj<0 or nj>=N:
            i,j = core[n][0],core[n][1]
            check(i,j,length+l,visit,n+1)





T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [[0]*(N)]
    for i in range(N):
        data.append(list(map(int,input().split())))
    minv =99999
    l=0
    core = []
    visit = [[0]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j]==1:
                core.append((i,j))
                visit[i][j]=1
    for i in core:
        if (i[0] ==0 or i[0]==N-1) or i[1]==0 or i[1]==N-1:
            l+=1
    print(l)
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    i,j = core.pop(0)
    check(i,j,l,visit,1)
    print(minv)