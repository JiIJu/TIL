T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    tower = []
    cnt = 0
    for i in range(N):  # 타워의 위치를 찾는다.
        for j in range(N):
            if data[i][j]==2:
                tower.append([i,j])


    di = [-1,1,0,0] #상하좌우 방향을 가기위해 선언
    dj = [0,0,-1,1]


    while tower:    #타워의 위치에서 상하좌우를 탐색해서 공격가능 공간이 있으면 그 곳의 값을 바꿔준다,
        i,j = tower.pop()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            while 0<=ni<N and 0<=nj<N and (data[ni][nj] == 0 or data[ni][nj]==3):
                data[ni][nj]=3
                ni+=di[d]
                nj+=dj[d]

    for i in range(N):  # 공격을 할 수 없는 공간(0)의 수를 센다.
        for j in range(N):
            if data[i][j]==0:
                cnt+=1
    print(f'#{tc} {cnt}')


