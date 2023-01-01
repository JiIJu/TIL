T = int(input())

for tc in range(1,T+1):
    N = int(input())

    data = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    result = 0
    room = [[0]*401 for _ in range(N)]
    for i in range(N):
        if data[i][0]>data[i][1]:
            data[i][0],data[i][1] = data[i][1],data[i][0]


    for i in range(N):
        if data[i][0] %2 ==0:
            data[i][0] = data[i][0]-1
        if data[i][1] %2 ==1:
            data[i][1] = data[i][1]+1


    for i in range(N):
            for j in range(data[i][0],data[i][1]+1):
                room[i][j] =1


    for i in range(1,N):
        for j in range(1,401):
            room[0][j] += room[i][j]

    print(f'#{tc} {max(room[0])}')