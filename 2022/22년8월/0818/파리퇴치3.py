T = int(input())

for tc in range(1,T+1):
    N , M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    x,y = 0,0
    dx = [-1 ,1 ,0 ,0] #상하좌우
    dy = [0 ,0 ,-1, 1]
    dxx = [-1,1,1,-1] #시계방향
    dyy = [1,1,-1,-1]
    nx,ny = 0,0
    count = 0
    s = 0
    m = 0
    max = 0

    for i in range(N):
        for j in range(N):
               count = data[i][j]
               for k in range(4):
                   for l in range(1,M):
                       if 0<=j+dy[k]*l<N and 0<=i+dx[k]*l<N:
                           count += data[i+dx[k]*l][j+dy[k]*l]
                   if max<count:
                       max = count
    for i in range(N):
        for j in range(N):
            count = data[i][j]
            for k in range(4):
                for l in range(1,M):
                    if 0 <= j + dyy[k] * l < N and 0 <= i + dxx[k] * l < N:
                        count += data[i + dxx[k] * l][j + dyy[k] * l]
                    if max < count:
                        max = count


    print(f'#{tc} {max}')