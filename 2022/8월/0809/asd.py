for tc in range(1,2):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(100)]
    x =0
    y = 0

    dx = [0 ,1, 1,-1]
    dy = [1 ,0, 1,0]
    nx = 0
    ny = 0
    k = 0
    start = 0
    for i in range(100):
        if data[99][i] == 2:
            start = i
            break
    print(start)
    # while True:
    #     down = 0

    #     nx = x + dx[k]
    #     ny = y + dy[k]
    #     if data[nx][ny] == 1 and 0<=nx<N and 0<=ny<N and (data[nx][ny-1]==1:
    #         pass
    #     elif data[nx][ny] ==0:
    #         nx -= dx[k]
    #         ny -= dy[k]
    #         k = (k + 1) % 3