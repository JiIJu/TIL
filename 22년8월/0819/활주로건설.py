T = int(input())

for tc in range(1,T+1):
    N,X = map(int,input().split())
    data = [list(map(int,input().split()))for _ in range(N)]
    road =0
    ground = [[0]*(20+X) for _ in range(20+X)]
    for i in range(N):
        for j in range(N):
            ground[i][j] = data[i][j]

    for i in range(N):
        for j in range(N):
            if data[i][j]


