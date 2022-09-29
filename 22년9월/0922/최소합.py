def plus(sum,x,y):
    global min
    if x == N-1 and y == N-1:
        if sum<min:
            min = sum
        return
    if x<N-1:
        plus(sum + data[x+1][y],x+1,y)
    if y<N-1:
        plus(sum + data[x][y+1],x,y+1)



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    min = 99999
    plus(data[0][0],0,0)
    print(f'#{tc} {min}')