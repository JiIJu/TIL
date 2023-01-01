T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    dxx = [-1,1,1,-1]
    dyy = [1,1,-1,-1]

    max = 0
    for i in range(N):
        for j in range(N):
            count = data[i][j]
            for l in range(4):
                for k in range(1,M):
                    if 0<=i+k*dx[l]<N and 0<=j+k*dy[l]<N:
                        count+=data[i+k*dx[l]][j+k*dy[l]]
            if max<count:
                max=count

    for i in range(N):
        for j in range(N):
            count = data[i][j]
            for l in range(4):
                for k in range(1,M):
                    if 0<=i+k*dxx[l]<N and 0<=j+k*dyy[l]<N:
                        count+=data[i+k*dxx[l]][j+k*dyy[l]]
            if max<count:
                max=count
    print(f'#{tc} {max}')