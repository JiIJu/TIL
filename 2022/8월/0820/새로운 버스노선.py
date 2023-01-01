T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    stop = [[0]*1001 for _ in range(N)]

    for i in range(N):
        stop[i][data[i][1]] = 1
        stop[i][data[i][2]] = 1
        for j in range(data[i][1],data[i][2]+1):
            if data[i][0] == 1:
                stop[i][j] =1
            elif data[i][0] == 2:
                if data[i][1] %2 ==0:
                    if j%2==0:
                        stop[i][j] = 1
                elif data[i][1]%2 ==1:
                    if j%2==1:
                        stop[i][j] = 1

            elif data[i][0] == 3:
                if data[i][1]%2 ==0:
                    if j%4==0:
                        stop[i][j] = 1
                elif data[i][1]%2 ==1:
                    if j%3==0 and j%10 !=0:
                        stop[i][j]=1

    for i in range(1,N):
        for j in range(1001):
            stop[0][j] += stop[i][j]

    max =0
    for i in range(1001):
        if max<stop[0][i]:
            max = stop[0][i]
    print(f'#{tc} {max}')